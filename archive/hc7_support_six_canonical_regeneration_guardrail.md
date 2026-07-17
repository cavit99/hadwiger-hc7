# Guardrail: quotient `K_6` regeneration can be entirely canonical

**Status:** proved parametric construction with a concrete verified member.
The construction is seven-connected and `K_7`-minor-free but is not
seven-chromatic or contraction-critical.  It is therefore a methodological
barrier, not a counterexample to the active `HC_7` theorem.

The verifier for the concrete member is
[`hc7_support_six_canonical_regeneration_guardrail_verify.py`](hc7_support_six_canonical_regeneration_guardrail_verify.py).

## 1. Parametric construction

Let `B` be a five-connected planar graph, let `u in V(B)` be such that
`B-u` is still five-connected, and let `T` be a triangle of `B-u` to which
`u` is not complete.  Add two nonadjacent vertices `a,b`, each universal
to `B`, and call the resulting graph

\[
                         G=\overline {K_2}\vee B.       \tag{1.1}
\]

Put

\[
                         Q=T\cup\{a\},\qquad e=ub.      \tag{1.2}
\]

Then `Q` is a literal `K_4`, `e` is an edge disjoint from it, and the edge
bag `e` is complete to `Q` collectively: `b` contacts all of `T`, while
`u` contacts `a`.  Neither endpoint is complete to `Q`; `b` misses `a`,
and `u` misses at least one member of `T`.  Thus (1.2) is a normalized
support-six `K_5` model.

### Proposition 1.1

The graph and model above have all of the following properties.

1. `G` is seven-connected and has no `K_7` minor.
2. `G` has no literal `K_5`, so any two-set disjoint from the displayed
   support is a literal-`K_5` transversal.
3. If `H=G/ub` and `z` is the contracted image, then

   \[
                           H=K_2\vee(B-u),              \tag{1.3}
   \]

   where the adjacent universal vertices are `a,z`.  Hence `H` is
   seven-connected and two-apex.
4. The quotient clique `L=T\cup\{a,z\}` and the connected remainder
   `B-(T\cup\{u\})` form exactly the canonical spanning `K_6` model of
   Lemma 2.1 in the adjacent result.
5. The fixed pair `\{a,b\}` is terminal: deleting it leaves the planar
   graph `B`.

#### Proof

Deleting fewer than seven vertices from `G` either leaves an apex together
with a base vertex, which connects the remainder, or deletes both apices
and fewer than five vertices of the five-connected base.  Thus `G` is
seven-connected.

At most two bags of a clique model can contain `a,b`.  A `K_7` model would
therefore leave five pairwise adjacent connected bags wholly in `B`, a
`K_5` minor in a planar graph.  This proves item 1.

A literal `K_5` could use at most one of the nonadjacent apices and would
then require a literal `K_4` in `B`.  A five-connected planar graph has no
literal `K_4`, because a displayed planar `K_4` exposes a separating
triangle.  This proves item 2.

Contracting `ub` makes its image universal to `B-u` through `b` and
adjacent to `a` through the edge `ua`.  Thus (1.3) holds.  The
two-universal connectivity characterization and five-connectivity of
`B-u` give seven-connectivity.  Deleting `a,z` leaves the planar graph
`B-u`, proving item 3.

The graph `B-u-T` is connected because `B-u` is five-connected.  Each
member of `T` has a neighbour outside `T` in `B-u`, while `a,z` are
universal.  This proves item 4.  Item 5 is immediate from (1.1).  \(\square\)

## 2. Concrete member

Take `B` to be the 32-vertex planar dual of the truncated icosahedron used
in the contraction-pullback guardrail.  In its fixed labelling, take

\[
                  u=1,qquad T=\{0,12,13\},qquad
                  a=32,quad b=33.                     \tag{2.1}
\]

The verifier checks

\[
 \kappa(B)=\kappa(B-u)=5,qquad
 \kappa(G)=\kappa(G/ub)=7,                              \tag{2.2}
\]

and the exact deficiency sets

\[
                         D_u=\{0\},\qquad D_b=\{a\}.   \tag{2.3}
\]

Thus even the smallest asymmetric deficiency type `(1,1,2)` can carry the
fully canonical quotient model without producing `K_7`.

## 3. Exact lesson

This family already has the desired terminal, and the audited two-apex
contraction-pullback theorem finds it.  It proves that the terminal cannot
be recovered from the **existence** of the quotient `K_6` alone: that model
is present for the elementary reason that a literal `K_5` in a
seven-connected graph has a connected full remainder.

Accordingly a valid criticality-based proof must distinguish the residual
non-two-apex quotient by one of the following genuinely new facts:

* a `K_6` model avoiding the contracted vertex;
* a second row-compatible literal `K_5` clique or near-full carrier;
* a proper-minor state which splits a labelled regenerated row; or
* a global terminal pair invariant under the split.

Unrooted `HC_6` regeneration in the quotient is not such a fact.
