# Independent audit: two disjoint Kempe paths need not uncross a rooted certificate

**Verdict:** **GREEN** for the stated local counterexample and its exhaustive
finite claim.  This is a separate internal mathematical and computational
cold audit, not external peer review.  The certificate does not satisfy the
minor-exclusion, contraction-criticality, or complete five-root routing
hypotheses of the bounded-interface programme.

## Exact revisions audited

```text
3bbe964e26d4b689978433cf3de717d249884b46aedc1272c819510c5746543b  barriers/hc7_degree8_dirty_path_local_uncrossing_barrier.md
f4b67a6c76d6b78d623581a6c05b1a91d121cac80ea3dcc9aa366b78cf48128e  barriers/hc7_degree8_dirty_path_local_uncrossing_barrier_verify.py
```

The mathematical source content was audited at SHA-256
`c73457db1a1d8648e00b09523c33cb424091aba7943238922b4ac0655d91367e`.
The only later source change was the status-line link to this audit.  Any
mathematical change to either file requires a renewed audit.

## 1. The inference actually refuted

The source considers five rooted connected bags whose quotient is
`K_5-{ae,bc}`, where the two omitted pairs have four distinct ends.  It also
provides vertex-disjoint bichromatic paths with end pairs `ae` and `bc` in
one fixed colouring.  The refuted conclusion is that arbitrary reallocation
inside the union of those bags and paths must produce a rooted five-bag
quotient with at most one missing adjacency.

The finite search checks the full stated conclusion: it does not merely ask
whether one of the two named defects can be repaired while all other contacts
are fixed.  It checks the empty allowed-defect set and each of all ten
possible singleton allowed-defect sets.  All eleven counts are zero, while a
model with the two named defects exists.  Thus the minimum quotient defect is
exactly two, even though reallocation can move the identities of the two
missing pairs.

The two literature inputs used to motivate this local configuration were
checked against their primary sources.  Rolek--Song, Lemma 1.7, applied with
`k=7`, `s=1`, pole `u`, and the independent triple `Q`, gives paths whose
internal vertices lie in `G-N[u]`; paths for missing edges with four distinct
ends are vertex-disjoint.  Kriesell--Mohr, Theorem 7, says exactly that every
five-vertex graph with at most six edges has property `(*)`.  Since
`G[U]+ae+bc` is the spanning path `e-a-b-c-d`, its six complementary demands
fall within that theorem.  The displayed wrapper itself is not claimed to
satisfy the hypotheses of either full host application.

## 2. Independent reconstruction of the slice

An independent transcription gives ten slice vertices and thirteen edges.
The displayed five colour classes are independent.  The paths

```text
e-x-y-a,   b-r-s-c
```

are respectively `E-A-E-A` and `B-C-B-C`, have disjoint vertex sets, and
have all internal vertices among `x,y,r,s,t`.

The five displayed bags are pairwise disjoint, rooted, and connected.  Their
eight quotient contacts have the following literal witnesses:

```text
ab: ab       ac: tc       ad: ay       bd: bx
be: br       cd: cd       ce: cs       de: ex.
```

There is no edge between the `a`- and `e`-bags or between the `b`- and
`c`-bags.  Hence their quotient is exactly `K_5-{ae,bc}`.  The path traces
are exactly

```text
e,d,a   and   b,e,c,
```

so neither contains a consecutive transition across either missing bag
pair.  The union of the certificate and the two paths is the entire
ten-vertex slice.

## 3. Interface, colouring, and connectivity

The independently reconstructed wrapper has 21 vertices and 109 edges.
The pole has neighbourhood exactly `S=Q union U` and degree eight.  Removing
`N[u]` leaves exactly

```text
C={h,h1,h2,h3,h4,h5,h6,x,y,r,s,t},
```

which is connected and has full external neighbourhood `S`.  The root graph
is exactly `ab+cd+e`, `Q` is independent and jointly dominates `U`, and a
direct independent-set enumeration gives `alpha(G[S])=3`.

After deleting `uQ`, the displayed six colour classes are all independent;
`Q` is exactly the sixth-colour class on `S`, and the roots in `U` have five
distinct other colours.  Both specified path interiors lie in the literal
component `C`.

The retained verifier checks every one of

```text
sum(binomial(21,j), j=0,...,6) = 82,160
```

vertex deletions of order at most six and finds the residual graph connected.
Independently repeating that enumeration gives the same result.  Moreover

```text
N(q0)={u,a,b,c,d,x,y}
```

is a seven-vertex cut isolating `q0`, so the vertex-connectivity is exactly
seven.

## 4. Separator, routing graph, and scope witness

The model union is the whole five-colour slice.  Every component of
`(G-u)-W` is a singleton, so none contains two vertices of `Q`.  In `G-u`,

```text
Z={a,b,c,d,x,y}=N(q0)=N(q1).
```

Deleting `Z` leaves `q0` and `q1` as singleton distinguished components,
each full to `Z`.  Restoring any one member `z` of `Z` gives the path
`q0-z-q1`, proving inclusion-minimality.  The `d`-bag meets `Z` in the three
vertices `d,x,y`.  In the original graph, both singleton components are full
to the actual order-seven separator `Z union {u}`.

The five-root routing graph of the displayed colouring is exactly
`{ab,ae,bc,cd}`, not the complete graph.  The eight proposed branch sets

```text
{h,a}, {h1,b}, {h2,c}, {h3,d},
{h4,e}, {h5,x}, {h6}, {y}
```

are disjoint, connected, and pairwise adjacent, so they form an explicit
`K_8`-minor model.  These two facts correctly exclude any inference that the
example is a full-hypothesis counterexample to `HC_7` or to the
bounded-interface programme.

## 5. Exhaustive model audit

Every rooted minor model in the ten-vertex slice is represented by assigning
each of the five nonroots to one of five labelled root bags or leaving it
unused.  Thus the `6^5=7,776` assignments are exhaustive: disjointness fixes
each root in its own bag, and every other vertex has exactly those six
possibilities.  Connectivity and every required interbag adjacency are then
checked in the exact induced slice.

The retained verifier finds eight models when `{ae,bc}` is the allowed
defect set, zero models for the empty set, and zero for every singleton
allowed-defect set.  A separate exact-missing-set enumeration, implemented
without importing the verifier, examined all 324 assignments having five
connected rooted bags and independently found minimum defect two.  This
confirms both the exhaustive encoding and the claimed negative outcome.

The retained script compiled successfully and returned the same GREEN
certificate under `PYTHONHASHSEED` values `0,1,2,7,31,123456`, and `random`.

## Trust boundary

No unresolved assumption remains in the local counterexample.  Its scope is
exactly the one stated: same-colouring path provenance, disjoint demand ends,
vertex-disjoint paths, high connectivity, and a model-carried full separator
do not by themselves justify local bag uncrossing.  The example supplies no
evidence that the obstruction persists after imposing complete Kempe routing,
`K_7`-minor exclusion, or contraction-criticality, and it yields no
same-form anti-neighbourhood reduction.
