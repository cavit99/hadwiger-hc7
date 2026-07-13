# Audit: permutation-labelled non-returning paths as an attained-duty mechanism

**Verdict:** the packing/transversal theorem is real and gives the desired
numerical bound `2` at packing threshold two.  There is not yet a faithful
encoding of the audited packet rotations.  The current data form a groupoid
of partial reversible moves: encoding states preserves legality but loses
literal disjointness, while encoding literal resources preserves
disjointness but does not yet give a well-defined permutation action.  The
literature therefore supplies a promising engine, not an `HC_7` lemma.

This assessment is separate from the GREEN point--tree deduction in
`../results/hc7_exact7_point_tree_gate_core.md`.

## 1. Exact theorem and the threshold-two corollary

Pap's permutation-labelled graph (a `p`-graph) consists of an oriented
reference graph `J`, a terminal set `A`, a potential set `Omega`, terminal
potentials `omega:A->Omega`, and for every oriented edge `e=uv` a
permutation `pi(e)` of `Omega`; traversing the edge backwards uses
`pi(e)^{-1}`.  If an `A`-path `W` runs from `a` to `b`, it is
**non-returning** when

\[
                         \pi(W)(\omega(a))\ne\omega(b).
\]

Pap's Theorem 2.1 states

\[
 \nu_{\rm nr}(J,A,\omega,\pi)
   =\min_F \nu_{A\cup V(F)}(J-F),                       \tag{1.1}
\]

where `F` ranges over `A`-balanced edge sets and the quantity on the right
is the ordinary maximum number of vertex-disjoint
`(A union V(F))`-paths.  An edge set is balanced when the terminal
potential assignment extends to `A union V(F)` so that every edge of `F`
preserves the assigned potentials.

Combining (1.1) with Gallai's ordinary `A`-path theorem gives the following
corollary.

### Corollary 1.1 (packing or a small literal transversal)

For every positive integer `k`, a `p`-graph contains either `k`
vertex-disjoint non-returning `A`-paths or a set of at most `2k-2`
vertices meeting every non-returning `A`-path.  In particular, at `k=2`
there are either two disjoint non-returning paths or a transversal of
order at most two.

#### Verification

If the maximum non-returning packing has order below `k`, choose a balanced
`F` attaining (1.1).  Gallai supplies a set `X` of at most `2k-2` vertices
meeting every ordinary `(A union V(F))`-path in `J-F`.  A non-returning
`A`-path cannot lie wholly in balanced `F`; Pap's easy inequality extracts
from it an `(A union V(F))`-path section in `J-F`.  Hence it meets `X`.

The permutation-labelled form is materially more general than the usual
group-labelled nonzero-path form.  The latter has the same `2k-2`
packing/transversal bound, but arbitrary packet rotations need not act by
translations in one group.

Primary sources:

* G. Pap, *Packing non-returning A-paths*, Combinatorica 27 (2007),
  247--251, Theorem 2.1; the accessible precursor is EGRES Technical
  Report TR-2005-12 (2005);
* G. Pap, *Packing non-returning A-paths algorithmically*, EuroComb 2005,
  pp. 139--144, especially the `p`-graph definition and Theorems 3.1--3.3;
* M. Chudnovsky, J. Geelen, B. Gerards, L. Goddyn, M. Lohman and
  P. Seymour, *Packing non-zero A-paths in group-labelled graphs*,
  Combinatorica 26 (2006), 521--532, for the group-labelled special case
  and the explicit `2k-2` corollary.

Pap's theorem should not be paraphrased as a bare alternative "two paths,
or a balanced graph, or two vertices."  Its exact dual is (1.1).  The
two-vertex transversal follows only after applying Gallai inside a
balanced-edge minimizer.

## 2. What the audited rotations presently provide

The portal-free packet-bridge move is exactly reversible.  On complete
labelled packet configurations it is a partial involution

\[
                         c\longleftrightarrow c'.        \tag{2.1}
\]

Likewise, a fixed-frame single-gate deficiency rotation has a literal
inverse.  These facts supply the inverse consistency expected of an edge
permutation.

They do **not** yet supply a `p`-graph:

1. A rotation is legal only on configurations containing its particular
   tree segment, bridge, portals, and named bags.  It is a partial
   bijection, whereas a `p`-edge carries one total permutation of one
   common potential set.
2. The packet rotation preserves the seven selected portal witnesses and
   frees a segment of known support.  It does not induce a deterministic
   map between exact equality partitions, nor does every nontrivial move
   discharge a new attained duty.
3. Composition is a groupoid of actual model configurations.  Two paths
   through that state graph being vertex-disjoint says only that they use
   different **configuration vertices**; their literal packet, bridge, or
   gate supports may overlap completely.

Extending every partial involution by fixing all out-of-domain potentials
does not repair item 1.  An auxiliary path could traverse an edge while its
current potential lies outside the move's legal domain, remain fixed, and
later become non-returning.  That would be a false positive rather than a
sequence of literal rotations.

## 3. Narrowest faithful encoding target

The right first target is not all packet rotations.  Restrict to one
rotation-closed block-terminal society in the surviving alternating web
cell and prove a **literal regular-cover encoding** with the following
data.

1. A base graph `J` whose nonterminal vertices represent literal,
   pairwise capacity-bearing rich-shore vertices (including every gate and
   first-hit portal), not whole bridge components or model states.
2. A finite potential set `Omega` which is a quotient of complete
   attained-duty packet configurations.
3. For each oriented base edge, one total permutation `pi(e)` such that
   every potential at its tail has a legal, reversible local realization
   on the literal support represented by that edge, with the reverse edge
   realizing `pi(e)^{-1}`.
4. Literal terminals `A` with prescribed first-hit identities and an
   endpoint criterion:

   \[
   \text{non-returning}
     \quad\Longleftrightarrow\quad
   \text{a named useful duty/state change, not a harmless portal change}.
                                                               \tag{3.1}
   \]
5. A lifting rule under which the union of the atoms on an auxiliary path
   is one connected labelled carrier, and two vertex-disjoint auxiliary
   paths lift to two vertex-disjoint literal carriers whose rotations can
   be performed simultaneously.
6. Completeness: every duty-correct rerouting relevant to the fixed-pair
   endgame appears as a non-returning `A`-path.

The present audited material verifies only reversibility in item 3 for
individual moves.  It does not yet verify the common total action,
criterion (3.1), simultaneous lifting, or completeness.

A useful way to expose the obstruction is the following state/resource
duality.

* If vertices of `J` are complete configurations, every edge is an actual
  legal rotation and the potential action is easy to define, but disjoint
  auxiliary paths need not have disjoint literal supports.
* If vertices of `J` are literal packet/bridge resources, auxiliary
  disjointness has the desired physical meaning, but one move generally
  consumes several resources and its effect depends on the incoming
  configuration.  No edgewise total permutation is presently defined.

Any successful encoding must solve both halves at once.  Contracting a
whole bridge or segment to one auxiliary vertex is insufficient for the
desired endgame: Pap's order-two transversal would then hit at most two
**atoms**, not two literal vertices.  Making separate state copies of one
literal vertex has the opposite defect, since two auxiliary paths can use
different copies of the same literal vertex.

## 4. What Pap would give after a faithful encoding

If items 1--6 were proved, Corollary 1.1 would give:

* two disjoint non-returning auxiliary paths, hence two compatible
  duty-changing literal carriers; or
* at most two literal rich-shore vertices meeting every encoded useful
  transition.

Even the second conclusion is not yet the desired fixed-pair theorem.  One
still needs a **completeness-to-minor** statement saying that a `K_5` model
in `G-X` would generate an encoded non-returning path avoiding `X`.
Without it, `X` only hits the chosen transition language and need not make
`G-X` `K_5`-minor-free.

The balanced set in Pap's dual is potentially valuable: on it, one
potential assignment is coherent across all labelled edges.  But
`A`-balance is only consistency in the auxiliary label system.  It yields
a common boundary equality state or coherent two-apex society only if the
encoding proves that those notions are equivalent.

## 5. Perfect--Pym endpoint augmentation: exact limitation

Perfect's fan-augmentation theorem can retain `k-1` already prescribed
fan endpoints while augmenting to `k`.  Pym's linkage theorem similarly
combines two vertex-disjoint path families so that the new family retains
the start set required from the first and the end set required from the
second.  These are appropriate tools for preserving literal first-hit
identities.

Neither theorem preserves a permutation label or the non-returning status
of a path.  Pym's splice may concatenate an initial segment of one path
with a terminal segment of another, changing the composed permutation.
Nor do these theorems make two paths avoid a shared internal packet gate
unless that gate is represented as an ordinary capacity vertex.  They can
therefore be used only **after** the label-compatible lifting conditions in
Section 3 have been proved; they do not supply those conditions.

Primary endpoint-preservation sources are H. Perfect, *Applications of
Menger's graph theorem*, J. Math. Anal. Appl. 22 (1968), 96--111, and
J. S. Pym, *The linking of sets in graphs*, J. London Math. Soc. 44
(1969), 542--550.

## 6. Strategic verdict

The point--tree deduction is immediately usable.  The permutation-labelled
route is higher-upside but one full encoding lemma away from applicability.
The most economical experiment is the atomic `A B D A B D` web with a
fixed literal portal skeleton: attempt to construct the total potential
fiber and label one reversible bridge rotation.  If even one edge cannot
act on every fiber state without an illegal move or a false non-returning
path, the Pap route should remain a conceptual guide rather than a proof
engine.  If it can, the next test is whether two disjoint auxiliary paths
lift to simultaneous literal duty carriers; only then should the
packing/transversal theorem be invoked.
