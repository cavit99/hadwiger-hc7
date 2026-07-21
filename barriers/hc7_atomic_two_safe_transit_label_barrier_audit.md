# Independent audit of the two-safe-transit-label barrier

**Verdict:** GREEN.

This is a separate internal mathematical and computational audit, not
external peer review.  No unresolved assumption, encoding error, exhaustive-
search gap, or scope overstatement was found in the stated finite barrier.

## Audited revisions and planned promotion

- barrier note
  [`hc7_atomic_two_safe_transit_label_barrier.md`](hc7_atomic_two_safe_transit_label_barrier.md),
  SHA-256
  `68373c4733538acfe9d1872a6cd7a39b8c4bfebb4e79db239fd3e6f0f7621155`;
- retained verifier
  [`hc7_atomic_two_safe_transit_label_barrier_verify.py`](hc7_atomic_two_safe_transit_label_barrier_verify.py),
  SHA-256
  `4f9e9727a27202a207d8bcf25831928e2f3933cbb7010721813c0d54cc5d12a4`.

The planned promoted source differs from the audited barrier note only by
replacing the status metadata `separate internal audit pending` with
`separate internal audit GREEN`.  That exact status-only replacement has
expected promoted SHA-256

```text
38263278bc25f1b0dd3005ee5ee11ac24158799d3fe33a56a55cb9513202dd9c
```

The verifier is unchanged.

## 1. Exact graph and forced-hub encoding

I reconstructed the core independently from the literal definition.  The
result has the claimed thirteen vertices and 32 edges.  The verifier starts
with `K_7-{ab,cd}`, adds the four `x` edges, replaces exactly
`fa,ga,fg,ac` by the ordered paths `f-p-a,g-q-a,f-h-g,a-r-s-c`, and adds
`eh,hx,pr,sq`.  Its candidate list is exactly

```text
a,b,c,d,e,f,g,h,p,r,s = V(C)-{q,x}.
```

For each candidate `v`, it adds precisely `qv,vx,qe`; use of a simple graph
correctly ignores an edge already present in `C`.  The added edges `qv,vx`
make `{q,v,x}` connected.  Contracting that set is equivalent to the formal
forced-hub condition:

- a `K_7` model in `C_v` whose one branch set contains `q,v,x` contracts to
  a model in the contracted graph; and
- a model in the contracted graph expands its contracted vertex to the
  connected set `{q,v,x}`, preserving all branch-set contacts.

Thus the implementation tests exactly the assertion in Proposition 1.1.

## 2. Exhaustiveness of the partition search

Every contracted graph has eleven vertices.  The recursive search processes
them in a fixed order.  At each step it inserts the next vertex into each
existing block or opens one new last block.  This is the standard
restricted-growth enumeration, so every unordered set partition occurs
exactly once.  The terminal test requires exactly seven nonempty blocks,
checks connectedness of each block, and checks adjacency for all 21 unordered
pairs.

The spanning restriction loses no minor model.  Each contracted graph is
connected.  Given a nonspanning clique-minor model, every component of the
unused induced subgraph has an edge to the used union; assign that entire
component to one adjacent branch set.  This preserves disjointness,
connectedness, and every old contact.  Repeating over the unused components
produces a spanning seven-bag model.

I also ran an independent census using a literal edge reconstruction and a
separate pure-bitset restricted-growth enumerator.  For every candidate it
examined all

```text
S(11,7)=63,987
```

canonical spanning seven-block partitions.  The numbers of valid models
were

```text
a:0  b:0  c:0  d:0  e:0  f:0  g:0  h:0  p:8  r:0  s:0.
```

This independently reproduces the classification `{p}`.  In particular,
the retained verifier's early return after finding a positive model does not
affect any negative conclusion; for every unsafe candidate its search
exhausts the entire partition space.

## 3. Positive certificate and 21 contacts

For `v=p`, the displayed bags

```text
{p,q,x}, {a,c,r,s}, {b}, {d}, {e}, {f,h}, {g}
```

are nonempty, disjoint, and span all thirteen vertices of `C_p`.  The first
bag is connected through the added edges `qp,px`; the second contains the
path `a-r-s-c`; and the sixth contains `fh`.

I checked every displayed contact independently:

```text
{p,q,x}:    qa, xb, xd, qe, pf, qg
{a,c,r,s}:  cb, ad, ae, cf, cg
{b}:        bd, be, bf, bg
{d}:        de, df, dg
{e}:        ef, eg
{f,h}:      hg
```

These are exactly 21 contacts, one for every unordered pair of bags.  The
verifier's direct certificate check also requires seven bags, exact spanning
coverage, connectedness of every induced bag, and all 21 pairwise
adjacencies.

## 4. Verifier rerun and scope

The retained verifier ran successfully with

```text
.venv/bin/python -B barriers/hc7_atomic_two_safe_transit_label_barrier_verify.py
```

and printed

```text
GREEN atomic two-safe-transit-label barrier
candidates=a,b,c,d,e,f,g,h,p,r,s
forced_hub_safe=p
forced_hub_unsafe=a,b,c,d,e,f,g,h,r,s
explicit_positive_hub={p,q,x}
```

The exact proved scope is that only `p` is admissible for the formal model
requiring one retained transit label `v` and one branch set containing all of
`q,v,x` in `C+qv+vx+qe`.  This refutes the proposed prerequisite of two
distinct labels under that ownership rule.  It does not claim that `C_v`
lacks every unrestricted `K_7` model for `v!=p`, and it does not address paths
with several retained labels, another allocation of the path, or additional
ambient-host structure.  Those limitations are stated accurately in the
barrier note.

NetworkX graph construction, Python assertion execution, and the retained
search implementation remain inside the recorded software trust boundary.
The independent literal reconstruction, full 63,987-partition census, and
manual positive-certificate audit provide separate checks of the finite
encoding and conclusion.
