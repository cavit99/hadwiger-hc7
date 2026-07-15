# Rooted-`K_4` decoder in the overlap-four cross-arm cell

## Status

Proved by the explicit finite table below and the dependency-free exhaustive
checker
[`../active/hc7_cross_arm_overlap_four_decoder_verify.py`](../active/hc7_cross_arm_overlap_four_decoder_verify.py).
An independent cold audit is **GREEN**; see
[`hc7_cross_arm_overlap_four_rooted_k4_decoder_audit.md`](hc7_cross_arm_overlap_four_rooted_k4_decoder_audit.md).

This is a labelled composition theorem, not a census of arbitrary graphs.
It closes the overlap-four cell whenever the five-terminal exterior
contains a rooted `K_4` on any four terminals.  The remaining exterior
outcome is therefore a genuine rooted-`K_4`/web obstruction.

## 1. Normalized cell

Let

```text
A={0,1,2,3,4,5},        I={0,1,2,3},
X=I union {6},           p=7, q=8,
T={4,5,6,7,8}.
```

Assume that each of the following eleven six-sets is an irredundant
support of a spanning `K_5` model:

```text
A, X union {p}, X union {q},
(A-{i}) union {p}, (A-{i}) union {q}    for i in I.
```

Here irredundant means that none of the six five-subsets is a literal
`K_5`.

### Theorem 1.1

If `G-I` contains a `K_4` model rooted at `T-{t}` for some `t in T`, then
one of the following holds.

1. For some `i in I`, the five-set `A-{i}` contains a `K_4` model of
   support at most five contacted by each of `i,p,q`.
2. There is a literal `K_7` model obtained from the rooted exterior model
   and the eight local labels other than `t`.

Consequently, if `G` is seven-connected, then `G` has a `K_7` minor: in
outcome 1 apply the audited three-rooted small-`K_4` composition theorem,
and outcome 2 is already the desired model.

The exterior rooted model need not avoid the fifth terminal `t`.  The
direct model in outcome 2 never uses `t` as a separate bag, so it remains
valid even if `t` was absorbed by one of the four rooted exterior bags.

## 2. Six-support complement language

On six vertices, a spanning `K_5` model consists of one two-vertex edge
bag `{x,y}` and four singleton bags.  Therefore its complement has no
edge inside the four singleton vertices, no edge `xy`, and every singleton
is nonadjacent in the original graph to at most one of `x,y`.  Equivalently,
the complement is a union of two vertex-disjoint stars centred at `x,y`,
plus isolated vertices.

The support is irredundant exactly when both star components are
nontrivial.  If all complement edges met one vertex, deleting that vertex
would leave a literal `K_5`; conversely a literal `K_5` after one deletion
says that every complement edge met the deleted vertex.

Thus every one of the eleven hypotheses is a copy of one finite relation:
the complement induced on that six-set is a union of two nonempty disjoint
stars.  There are 375 distinct labelled relations of this kind.  Joining
the eleven relations on their literal common edges gives the table in the
next section.

## 3. Complete table

There are two edge layers, and keeping them separate is essential.

* The eleven support relations constrain only the **original** edges of
  `G`.
* After those relations have been joined, the exterior rooted model
  supplies six **virtual** clique adjacencies on `T-{t}`.  These virtual
  edges are used only when testing the final model; they are never fed
  back into an irredundancy constraint.

The join has 387 consistent partial original-edge states.  Complete their
few still-unconstrained relevant edges in both ways.  For every completion,
either outcome 1 occurs in the original graph, or, after adding the six
virtual adjacencies, the complement on

```text
V=I union (T-{t}),
```

has exactly the form

```text
{ab,cd}                         or
{ab,cd, s6},
```

where `{ab,cd}` is one of the three perfect matchings of `I` and
`s in I`.  The optional edge is unavailable when `t=6`.  Thus there are
three direct projected patterns for `t=6` and `3(1+4)=15` for every other
choice of `t`.

These patterns give outcome 2 explicitly.  If the optional edge `s6`
occurs, let
`ss'` be its matching edge and choose either endpoint `c` of the other
matching edge.  Use `{s,c}` as the only two-vertex bag and every other
vertex of `V` as a singleton bag.  If the optional edge is absent, choose
one endpoint from each matching edge for the two-vertex bag.  In either
case the chosen two vertices are adjacent in `G`, every complement edge
meets that pair, and no remaining vertex is nonadjacent to both of them.
Hence the six singleton vertices form a clique and the edge bag contacts
all six: this is a spanning `K_7` model on `V`.

The complete original-state table is:

| omitted `t` | relevant original completions | outcome 1 | direct outcome 2 | distinct direct projections after virtual edges |
|---:|---:|---:|---:|---:|
| `q` | 2520 | 1440 | 1080 | 15 |
| `p` | 2520 | 1440 | 1080 | 15 |
| `6` | 126 | 72 | 54 | 3 |
| `5` | 1548 | 1008 | 540 | 15 |
| `4` | 1548 | 1008 | 540 | 15 |

For outcome 1 the checker directly enumerates the four disjoint connected
bags in `A-{i}` and verifies all root contacts.  For outcome 2 the
parameterized matching table above supplies the displayed branch sets.
Thus every row has a literal certificate, rather than merely failing an
unsatisfiability query.

## 4. Lifting an exterior rooted model

Let `B_c`, for `c in T-{t}`, be the four pairwise disjoint, pairwise
adjacent connected bags of the exterior rooted `K_4`.  If outcome 1 holds,
ignore these bags and apply the audited three-rooted theorem in the
original graph.

Otherwise use the explicit direct model on `V` above.  Replace every
singleton terminal `c in T-{t}` by `B_c`; its only two-vertex bag lies
inside `I`, so no further merger is required.  Every original local edge
incident with `c` remains a bag adjacency because `c in B_c`, and every
virtual clique edge is supplied by adjacency of the rooted bags.  The
direct model avoids `t`.  Hence it remains disjoint even if `t` lies inside
one of the exterior bags `B_c`.  This proves Theorem 1.1 without treating
the virtual clique edges as literal edges of `G`.

## 5. Exhaustiveness and trust boundary

The checker uses no SAT solver and no external graph library.  It:

1. examines all `2^15` complements on a labelled six-set and retains
   exactly the 375 which directly pass the spanning-`K_5` and
   irredundancy tests;
2. joins eleven copies on their shared literal edge variables, producing
   387 partial original-edge states;
3. completes every still-unknown relevant original edge;
4. independently enumerates every support-at-most-five common rooted
   `K_4` in the original edge layer;
5. only then clears the six complement bits corresponding to the virtual
   exterior clique, and independently enumerates every `K_7` model
   avoiding `t`; and
6. checks that every direct residue has the parameterized matching form
   above.

This theorem does not produce the rooted exterior `K_4`.  In the actual
overlap-four cell `G-I` is three-connected, but three-connectivity alone
does not root `K_4` at arbitrary terminals.  The precise remaining step is
therefore structural: obtain one of these five rooted `K_4` models, or turn
its rooted-minor obstruction into a state-preserving web/gate handoff.
