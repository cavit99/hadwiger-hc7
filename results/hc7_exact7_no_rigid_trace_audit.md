# Audit of the exact-seven no-rigid-trace theorem

**Verdict:** GREEN for the exact mathematical source revision identified
below.

This is an independent internal mathematical audit.  It verifies the stated
boundary-minor exclusion, the seven-vertex classification, the canonical
connected `(1,1)` consequence, and the no-rigid-trace consequence.  It is
not external peer review and does not prove `HC_7` or the conjectural
opposite-response theorem in Section 5 of the source.

## Audited revision

The audited file is `results/hc7_exact7_no_rigid_trace.md`.

**Mathematical source SHA-256:**
`c54201e47d829bc6e954b23679ce2442f50c84d16859efd7d0399f90a72df78c`.

After the line-by-line audit, the source status line alone was changed from
"written proof; the strengthened revision awaits an updated separate
internal audit" to "written proof; separate internal audit GREEN."  The
resulting current source SHA-256 is
`cd4b7fcf03242e41434522ac2eedd83425c418b83917d2ba1e94dd6740b3a568`.
Restoring the former status text reproduces the mathematical source hash
exactly.  No hypothesis, conclusion, proof, dependency, or strategic
trust-boundary text changed, so this verdict applies to the current
status-only revision.

## 1. Disconnected shores and boundary fullness

Because `L` and `R` are anticomplete and both have external neighbourhood
contained in `S`, every component of `G[L]` or `G[R]` is a component of
`G-S`.  If such a component missed a boundary vertex, its full external
neighbourhood would have order at most six and would separate it from the
nonempty opposite open shore.  This contradicts seven-connectivity.
Thus the proof correctly handles disconnected open shores: one may choose
one `S`-full component from each side without assuming that either whole
shore is connected.

## 2. The explicit minor model and its uniform form

Fix `v in S` and a `K_5`-minor model `Q_1,...,Q_5` in `G[S-v]`.
The seven displayed sets

\[
 P_L\cup\{v\},\qquad P_R,\qquad Q_1,\ldots,Q_5
\]

are pairwise disjoint and connected.  Fullness supplies all adjacencies
from each of the first two sets to every `Q_i`.  It also supplies an edge
from `P_R` to `v`, which is exactly the adjacency between the first two
sets.  The five `Q_i` have all mutual adjacencies by the assumed minor
model.  Hence this is an explicit `K_7`-minor model and proves
`K_5 not preccurlyeq G[S-v]` for every boundary vertex `v`.

The parameter-uniform statement is the identical construction.  Two
disjoint connected subgraphs outside `T`, both adjacent to every vertex of
`T`, together with a `K_{t-2}` model in `G[T-v]`, give `t` disjoint branch
sets by adjoining `v` to the first outside subgraph and leaving the second
outside subgraph separate.  No unstated adjacency between the two outside
subgraphs is required: the second is adjacent to `v` by fullness.

The clique-number consequence is also correct.  A five-vertex clique in
the seven-vertex boundary avoids either one of the other two boundary
vertices and so contradicts the just-proved deletion statement.

## 3. Five-chromatic boundary classification

The use of the established case `HC_5` is exact: each
`K_5`-minor-free graph `G[S-v]` is four-colourable, so adding `v` in a
new colour shows `chi(G[S])<=5`.  Equality makes the seven-vertex graph
`H=G[S]` vertex-critical, whence `delta(H)>=4` and
`Delta(complement(H))<=2`.

For a maximum-degree-two graph `F`, a clique partition uses an isolated
vertex as one class, an edge as one class, and all three vertices of a
`C_3` as one class.  Equivalently, outside `C_3` its saving
`|F|-theta(F)` is the maximum matching number of each path or cycle
component.  The source's list is therefore complete:

- `P_2,P_3` have saving one;
- `P_4,P_5,C_3,C_4,C_5` have saving two; and
- every longer path or cycle has saving at least three.

Savings add across components.  Since `theta(F)=5` on seven vertices,
the total saving is two; since `theta(F-v)<=4`, deleting any vertex must
leave saving at least two.  Two saving-one components fail this deletion
test.  Among the saving-two components, deleting an endpoint of `P_4`, a
vertex next to an endpoint of `P_5`, any vertex of `C_3`, or any vertex of
`C_4` lowers the saving.  Only `C_5` retains saving two after every vertex
deletion.  The remaining two vertices must be isolated, so

\[
 \overline H=C_5\mathbin{\dot\cup}2K_1,
 \qquad H=K_2\vee C_5.
\]

This verifies both the completeness and the uniqueness of the claimed
seven-vertex classification.

## 4. Canonical connected `(1,1)` residue

Corollary 2.3 adds exactly the hypotheses needed by the audited exact-seven
full-packet theorem: seven-chromaticity and six-colourability of every
proper minor, in addition to the standing seven-connectivity and
`K_7`-minor exclusion.  For `G[S]=K_2 vee C_5`, the boundary clique number
is four.  The packet theorem gives

\[
 4\le 6-(\nu_L+\nu_R),
\]

while Lemma 2.1 gives `nu_L,nu_R>=1`.  Hence both packing numbers equal
one.  Since every component of either open shore is itself an `S`-full
connected subgraph, two components in one shore would be two disjoint full
packets.  Each open shore is therefore connected.  No implication from
packing number one to a small vertex transversal is used.

Writing the two join vertices as `p,q`, deleting them can lower chromatic
number by at most two, so `chi(G-{p,q})>=5`.  The contrapositive of the
established `HC_5` therefore supplies an unrooted `K_5` minor in that
graph.  The source correctly distinguishes this from a `K_5` model rooted
at the five cycle vertices.  If rooted branch sets existed, the singleton
sets `{p}` and `{q}` would be adjacent to each other and to all five rooted
sets, producing an explicit `K_7`-minor model.  Thus the unrooted model
exists but no such cycle-rooted model exists.

## 5. Unique five-colourability and the rigid trace

On six vertices, every proper five-colouring has one two-vertex colour
class and four singleton classes.  Every nonedge can serve as that pair.
Thus the colour-class partition is unique up to colour permutation exactly
when there is exactly one nonedge, namely for `K_6-e`; this graph contains
a `K_5`.  The five-vertex case is necessarily `K_5`.

For nonempty `I subseteq S`, a five-chromatic `G[S-I]` has five or six
vertices.  Unique five-colourability would therefore give a `K_5`
subgraph in `G[S]`, contradicting the boundary clique bound.  Independence
of `I` is not needed for this contradiction, but is correctly retained
because it is a hypothesis of the rigid-boundary contraction splice being
excluded.

## 6. Strategic discussion

The equality-partition claims in Section 5 are correctly scoped.  A common
partition from colourings of the two closed shores would glue after a
permutation of the six colour names, so a seven-chromatic graph has
disjoint extension families.  The stronger operation-response statement
is explicitly conditioned on every proper minor being six-colourable;
that hypothesis is necessary and is now present.

The three listed outcomes are explicitly conjectural.  The third is a
valid terminal outcome under `HC_5`: if two vertices meet every `K_5`
minor model, deleting them leaves a `K_5`-minor-free, hence
four-colourable, graph, and assigning two additional colours gives a
six-colouring of `G`.  The cited promoted theorem separately upgrades the
same pair to an actual order-seven separation under the contraction-
critical hypotheses.  The source does not assert that the conjectural
opposite-response theorem has been proved.

## 7. Trust boundary

The audited source proves:

1. boundary fullness for every component of either open shore;
2. `K_5 not preccurlyeq G[S-v]` for every `v in S`;
3. `chi(G[S])<=5`, assuming `HC_5`, with equality only for
   `K_2 vee C_5`;
4. under the contraction-critical hypotheses, the five-chromatic boundary
   has connected `(1,1)` open shores, and `G-{p,q}` has an unrooted but no
   cycle-rooted `K_5` model; and
5. impossibility of a nonempty uniquely five-colourable independent
   trace on an exact seven-vertex boundary.

It does **not** prove:

1. that the two closed shores attain a common equality partition;
2. the label-preserving opposite-response theorem proposed in Section 5;
3. that an arbitrary separator of order above seven can be trimmed while
   preserving colouring data;
4. that every hypothetical counterexample reaches an exact order-seven
   separation; or
5. `HC_7`.

## Unresolved assumptions or gaps

None within Lemma 2.1, its parameter-uniform extension, Corollaries 2.2 and
2.3, Lemma 3.1, Theorem 4.1, or Corollary 4.2 at the audited mathematical
source hash.
