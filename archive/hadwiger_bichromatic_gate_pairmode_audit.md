# Adversarial audit: pair-mode normalization at the antipodal gate

## Verdict

**GREEN for Theorem 6.1 and Lemmas 6.2--6.3** of
`hadwiger_bichromatic_gate_peel_or_adhesion.md`, with the exact scope
stated there.  The path localization uses essentially that the gate cut
has exactly two components; this is supplied by Theorem 2.1 of
`hadwiger_gate_exact_adhesion_multishore.md`.  The results produce a
pair-mode, capacity, a two-shore rooted star, or the displayed portal
separator.  They do not yet upgrade two-block capacity to the three
carriers required by Lemma 6.2.

The helper condition in the current Lemma 6.2 is correctly phrased as
adjacency of the whole set (\{q\}\cup Z) to each block-carrier bag.  This
includes the previously omitted case in which (q) sees (L_i) directly.

## 1. Localization and the finite (C_4) split

Fix the original exact-trace colouring.  The cut is

\[
 L=\{v,1,2,3,4,p,q\}.
\]

For a missing core edge (ij), the only vertices of (L-v) in its two
core colours are (i) and (j): the other two roots have different core
colours, while (p,q) have the omitted gate colours.  Therefore a simple
bichromatic (i)-(j) path in (H=G-v) cannot pass from one component of
(G-L) to the other.  Its interior lies wholly in (C_0) or wholly in the
unique far component.  The uniqueness of that far component is precisely
where the no-multishore theorem is used.

Four-saturation supplies a global bichromatic path for every edge of the
missing (C_4).  Hence every edge outside (F_0) has a far-side path.

The set-theoretic trichotomy in Theorem 6.1 is exhaustive:

* if (\overline{F_0}) contains one of the two opposite-edge matchings,
  the corresponding two pairs are disconnected in their two-colour
  graphs on the (C_0)-side; switching one endpoint component for each
  pair creates the matching state;
* if (F_0) contains such a matching, the two paths use disjoint pairs of
  colours, so their nonempty interiors are disjoint carriers; and
* otherwise (F_0) contains exactly one edge from each opposite pair.
  Its two edges form a star and the complementary two edges form the
  star at the root joined to the first centre by (12) or (34).

In the third case, the union of the two paths in one shore with their
common root is connected.  The two centre bags are disjoint because their
interiors lie in opposite shores, and the other two roots remain singleton
bags.  One of (12,34) joins the centres, the other joins the singleton
bags, and the four star arms give all centre-to-singleton adjacencies.
Thus the asserted rooted (K_4) is literal; no path is counted in two bags.

The switches in the first case are also localized correctly.  The two
root pairs use disjoint colour pairs, so their bichromatic components are
vertex-disjoint and the switches commute.  They do not change the gate
colours on (v,p,q), and the resulting boundary equality partition is
exactly one of (6.2).

## 2. The helper contraction and gluing

For each (i), the carrier (L_i) lies in (C_0), is connected, and meets
both portal sets of the boundary pair (B_i).  Hence (B_i\cup L_i) is
connected.  The three such sets are disjoint.  The (B_0)-bag sees the two
core bags through the edges from (v) to (X); the two core bags see each
other through (12) and (34).  The helper hypothesis gives exactly the
three remaining adjacencies from (\{q\}\cup Z).

Contracting the four bags is a proper minor operation.  The four images
form a clique and therefore receive four distinct colours in every proper
six-colouring of the minor.  To recover the far-side boundary state, give
each original cut vertex the colour of its bag image and discard the
contracted (C_0)-interior.  This expansion is proper:

* each intended pair in (6.2) is a boundary nonedge;
* every boundary-to-far edge survives as an image-to-far edge; and
* distinct blocks receive distinct colours.

Thus the far side realizes the same labelled equality partition as the
original (C_0)-side state.  A palette permutation aligns the two
colourings pointwise on (L), so gluing is valid.

## 3. Minimal carriers and the portal separator

An inclusion-minimal connected carrier for two portal classes is a path:
each non-cutvertex must be uniquely charged to one of the two classes,
so there are at most two; the standard block injection then leaves only
edge blocks.  Shrinking the three carriers preserves their pairwise
disjointness.

Let (\mathcal W) consist of components of
(C_0-(L_0\cup L_1\cup L_2)) which contain a neighbour of (q).  Their
union, together with (q), is connected because every member has a literal
edge to (q).  If it fails to contact some bag (B_i\cup L_i), then (q)
misses that bag and no member of (\mathcal W) attaches to (L_i).  A path
from a (q)-neighbour to (L_i) avoiding the other two carrier paths would
start either in (L_i), contradicting the first fact, or in one member of
(\mathcal W) and give that member an attachment to (L_i).  This proves
the separator statement (6.5), including the case in which every
(q)-neighbour already lies on one of the two separating paths.

## 4. Remaining gate-colour placements of (p,q)

The current Section 6 treats only the richest orbit: (p,q) lie in two
distinct extra (\alpha,\beta)-components.  The other placements are
genuinely different finite-boundary states.

1. **Same extra component.**  Its Kempe switch toggles (p,q) jointly,
   while the (K_0)-switch toggles (v) independently.  If
   (c(p)=c(q)), the two equality partitions on these vertices are
   (vpq) and (v\mid pq).  If (c(p)\ne c(q)), the two partitions are
   (vp\mid q) and (vq\mid p).  There is no three-bit cube.
2. **Exactly one extra-component vertex.**  Say (p) has a gate colour
   and (q) lies in the four-colour core.  Then (q) is paired, in the
   boundary partition, with the unique root (x_r\in X) of its core
   colour.  The orbit gives either
   (vp\mid qx_r) plus three core singletons, or
   (v\mid p\mid qx_r) plus those three singletons.
3. **Pure core.**  Both (p,q) lie in (J), and the (K_0)-switch does not
   change the equality partition.  If they have one core colour, the
   fixed block is (pqx_r); if they have distinct core colours, the fixed
   blocks are (px_r) and (qx_s).  Vertex (v) is a singleton in either
   case.

Thus the same-component branch needs a component-splitting transition,
the exactly-one branch needs one additional core-pair normalization, and
the pure-core branch needs a four-terminal/web argument.  None is covered
merely by renaming the distinct-component cube.

## 5. Connector-support correction

The current `hadwiger_c4_reserved_connector_gate.md` is already patched
correctly.  Its Theorem 3.2 now concludes only that each clean connector
cuts **at least one** of the four fixed (C_4) supports.  Corollary 3.3 is
the sound last-support statement: if all four survive, property ((\*))
gives the rooted model.  There is no remaining claim that one connector
must cut two supports.

