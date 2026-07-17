# Degree-nine pole: exceptional local completion verifier

**Status:** computer-assisted finite result; separately audited GREEN.

## Claim checked

Let `H` be a graph on nine vertices with minimum degree at least five, and
let `c` be an additional vertex.  In each of the following cases, `H+c`
contains a `K_6`-minor model whose six branch sets all contain a vertex of
`H`:

1. `e(H)=23` and `d_H(c)=7`;
2. `e(H)=23` and `d_H(c)=8`;
3. `e(H)=24` and `d_H(c)=7`.

The verifier proves the stronger finite statement that the model may always
be chosen as three edges of `H`, three singleton vertices of `H`, and `c`
adjoined to one of those six branch sets.

## Why these are the only exceptional degree-nine cases

In the degree-nine pole argument, put `H=G[N(u)]`.  If every edge incident
with `u` were double-critical, every vertex of `H` would have at least five
neighbours in `H`, so `e(H)>=23`.  Contracting a component of
`G-N[u]` gives a vertex `c` with at least seven neighbours in `H`.

The graph on `N[u]` together with `c` has 11 vertices and

```text
9 + e(H) + d_H(c)
```

edges.  Mader's `K_7` extremal bound is `5*11-15=40`.  Therefore all cases
except the three listed above already have more than 40 edges and contain a
`K_7` minor.  In each listed case, a `K_6` model in `H+c` whose branch sets
all meet `H` is completed by the singleton branch set `{u}` to a `K_7`
model.

Writing `F` for the complement of `H`, the finite input classes are exactly:

```text
e(F)=13, Delta(F)<=3, c has 2 non-neighbours in H;
e(F)=13, Delta(F)<=3, c has 1 non-neighbour in H;
e(F)=12, Delta(F)<=3, c has 2 non-neighbours in H.
```

## Reproduction

The script uses the Python standard library and Brendan McKay's `geng` from
nauty.  Install nauty so that `geng` is on `PATH`, then run:

```bash
python3 results/hc7_degree9_pole_verifier.py
```

Alternatively, provide the executable explicitly:

```bash
python3 results/hc7_degree9_pole_verifier.py --geng /path/to/geng
```

`geng` exhausts unlabelled simple graphs on nine vertices with the specified
edge count and maximum degree.  The script independently decodes every
graph6 representative, checks its edge and degree constraints, tries every
possible non-neighbour set of `c`, constructs a restricted `K_6` model, and
then verifies connectivity, disjointness, coverage, and every pairwise
branch-set adjacency from scratch.

The expected census is:

```text
20 * C(9,2) = 720
20 * C(9,1) = 180
103 * C(9,2) = 3708
```

Thus 4,608 rooted instances are checked.  The default output includes one
explicit branch-set certificate per regime and SHA-256 digests of the full
unlabelled catalogue and all 4,608 deterministic witnesses.  Use
`--emit-all` to print every witness.

Expected output:

```text
degree9_pole_verifier version=1
restricted_partitions=1260
case F_edges=13 c_nonneighbours=2 complements=20 instances=720 bad=0
certificate F=H?`vAqo missing=0,1 bags={0} {1} {2,c} {4,5} {3,6} {7,8}
case F_edges=13 c_nonneighbours=1 complements=20 instances=180 bad=0
certificate F=H?`vAqo missing=0 bags={0} {1} {2} {3,4} {5,6,c} {7,8}
case F_edges=12 c_nonneighbours=2 complements=103 instances=3708 bad=0
certificate F=H?Bed`o missing=0,1 bags={0} {1} {2,c} {3,5} {4,6} {7,8}
total_instances=4608 bad=0
catalogue_sha256=489ef6397133a86bddaabb3c0a27b78b36e172d041ec5aab05e9c89ed9e175eb
witness_sha256=168b7a1b4c863029ee4ee14b1b53d8843b9b79d4b0c2205d093636a13a1abdb1
PASS degree-nine local completion
```

## Trust boundary

The verifier establishes only the finite local completion statement above.
The reduction from a hypothetical minimal counterexample to these three
cases, Mader's extremal bound, and the common-neighbour consequence of a
double-critical edge are mathematical inputs and must be audited separately.
