# Two disjoint Kempe paths need not uncross a five-root certificate

**Status:** barrier/counterexample to an intermediate claim; computer-assisted
finite result; [separately audited GREEN](hc7_degree8_dirty_path_local_uncrossing_barrier_audit.md).
The deterministic verifier is
[`hc7_degree8_dirty_path_local_uncrossing_barrier_verify.py`](hc7_degree8_dirty_path_local_uncrossing_barrier_verify.py).
This is not a counterexample to `HC_7`, to the bounded-interface bridge
composition theorem, to Rolek--Song's path lemma, or to the
Kriesell--Mohr property-`(*)` question.

## 1. The refuted matching-defect inference

Let

```text
U={a,b,c,d,e},    L=G[U]={ab,cd}.
```

Thus `L=2K2+K1`, with isolated vertex `e`.  The two nonedges

```text
                         f=ae,   g=bc
```

have four distinct ends, and `L+{f,g}` is the spanning path
`e-a-b-c-d`.  The complement of those four path edges has six edges.
Consequently
[Rolek--Song, Lemma 1.7](https://sciences.ucf.edu/math/zxsong/wp-content/uploads/sites/13/2018/04/Coloring-graphs-with-forbidden-minors.pdf)
supplies vertex-disjoint bichromatic paths for `f,g` from the degree-eight
contraction colouring, while
[Kriesell--Mohr, Theorem 7](https://arxiv.org/abs/1911.09998) packages the
other six demands into a rooted certificate.

The tempting next inference is:

> If a five-root certificate has exactly the two missing matching
> adjacencies `ae,bc`, and one fixed colouring supplies vertex-disjoint
> bichromatic paths `P_ae,P_bc`, then the union of the bags and paths has
> five rooted bags whose quotient misses at most one adjacency.

The construction below refutes this purely local inference.  It does so
even inside an exactly seven-connected degree-eight interface with an
independent triple `Q`, a full connected component of `G-N[u]`, an
exact-`Q` contraction colouring, and the usual connector-or-full-separator
alternative.  Both paths are dirty against the certificate, and exhaustive
reallocation of every nonroot slice vertex never reduces the number of
missing quotient adjacencies below two.

## 2. The local five-colour slice

Take roots `U={a,b,c,d,e}` and five additional vertices `x,y,r,s,t`.  The
slice edges are

```text
ex, xy, ya, dx,
br, rs, sc, er,
ab, cd, bx, at, tc.
```

Use the proper five-colouring

```text
A: a,x       B: b,s,t       C: c,r       D: d       E: e,y.
```

The roots induce exactly `ab+cd+e`.  In this one colouring the paths

```text
P_ae=e-x-y-a,        P_bc=b-r-s-c
```

are bichromatic and vertex-disjoint.  Take the rooted bags

```text
M_a={a,t},   M_b={b},   M_c={c},
M_d={d,x,y}, M_e={e,r,s}.
```

They are connected and pairwise adjacent except for `M_a M_e` and
`M_b M_c`.  The literal root edges `ab,cd` supply two adjacencies; the
remaining six quotient adjacencies form precisely the six-demand graph
covered by Kriesell--Mohr's theorem.

The reduced bag traces of the two paths are

```text
P_ae: M_e, M_d, M_a,
P_bc: M_b, M_e, M_c.
```

Neither trace has a consecutive transition across one of the two missing
bag pairs.  The interiors of `P_ae` and `P_bc` are swallowed by `M_d` and
`M_e`, respectively.  Moving either useful path segment disconnects or
removes contacts from its current rooted bag.

## 3. A degree-eight, exactly seven-connected wrapper

Put `Q={q0,q1,q2}` and `S=Q union U`.  Add a pole `u` adjacent exactly to
`S`.  Make `Q` independent.  Join each of `q0,q1` to

```text
                         a,b,c,d,x,y,
```

and join `q2` to all of `U` and to `x`.  Thus `Q` jointly dominates `U`
and `alpha(G[S])=3`.

Add seven pairwise nonadjacent vertices

```text
                         R={h,h1,h2,h3,h4,h5,h6}
```

and make each complete to the ten-vertex five-colour slice.  Put

```text
                         C=R union {x,y,r,s,t}.
```

There are no other edges.  Then `d(u)=8`, `C` is a component of `G-N[u]`,
and `N(C)=S`.  Give `u,Q,R` a sixth colour and delete the three edges from
`u` to `Q`; together with the displayed slice colouring this is a proper
six-colouring in which `Q` is an exact boundary colour class and the five
roots have the other five colours distinctly.  Both path interiors lie in
the literal component `C`.

The verifier checks all 82,160 deletions of at most six vertices, so the
wrapper is seven-connected.  The seven neighbours of `q0` form a cut,
hence its connectivity is exactly seven.

Let `W` be the union of the five bags in `G-u`.  No component of
`(G-u)-W` contains two vertices of `Q`.  Moreover

```text
                         Z={a,b,c,d,x,y}
```

is an inclusion-minimal order-six `q0-q1` separator.  The two distinguished
components are the singletons `{q0},{q1}`, both full to `Z`, and `M_d`
contains `d,x,y` from `Z`.  Thus `Z union {u}` is an actual order-seven
full separator.  The connector/separator alternative records the collision
but does not uncross either path or produce a same-form anti-neighbourhood
restart.

## 4. Exhaustive rooted reallocation

The five-colour slice has ten vertices, five of them nonroots.  For each
nonroot, the verifier considers assignment to any of the five labelled
root bags or to no bag.  It therefore checks all

```text
                         6^5=7,776
```

assignments for each permitted defect set.  It finds eight rooted models
when both matching defects `ae,bc` may remain.  It then checks each of all
ten possible singleton allowed-defect sets, as well as the empty set, and
finds none.  The minimum possible number of missing quotient adjacencies is
therefore exactly two.  This exhausts all rooted minor models inside the
union of the displayed certificate and paths, not merely bag-preserving
enlargements.

Run:

```text
.venv/bin/python barriers/hc7_degree8_dirty_path_local_uncrossing_barrier_verify.py
```

The expected final lines include

```text
two_matching_defect_models=8
singleton_allowed_defect_counts {'ab': 0, ..., 'de': 0}
minimum_missing_adjacencies=2
scope=local_certificate_only; minor exclusion and criticality absent
```

## 5. Exact forcing condition and trust boundary

For an arbitrary rooted certificate, reduce a path to the sequence of bags
it meets, suppressing repeated consecutive labels.  If an excursion has as
its two consecutive labels a missing pair, its interior is disjoint from all
bags.  Split that excursion at its last edge and add the first part to one
endpoint bag.  This repairs the missing adjacency while preserving every
old bag and contact.  A missing-pair transition in a reduced bag trace is
therefore a sufficient clean-repair condition.  The two traces above show
that vertex-disjointness of the paths does not force that condition.

The wrapper deliberately fails the decisive full-host hypotheses.  Its
five-colour routing graph on `U` has only the four path edges
`ae,ab,bc,cd`, rather than being complete.  The seven sixth-colour hubs also
give the explicit `K_8`-minor bags

```text
{h,a}, {h1,b}, {h2,c}, {h3,d}, {h4,e}, {h5,x}, {h6}, {y}.
```

Thus it is not `K_7`-minor-free, and no contraction-critical chromatic claim
is made.  The construction does not show that the dirty obstruction occurs
under all host hypotheses.  Its exact conclusion is narrower and reusable:
same-colouring provenance, disjoint demand endpoints, disjoint path
interiors, seven-connectivity, and the full-separator alternative still do
not make local bag uncrossing formal.  A successful proof must use the six
unused bichromatic routing components coherently, exploit `K_7`-minor
exclusion or contraction-criticality, or derive the literal aligned smaller
component required by the declared restart.
