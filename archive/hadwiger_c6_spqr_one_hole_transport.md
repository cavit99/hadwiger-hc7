# One-hole transport through an arbitrary SPQR tree

## 1. Purpose and status

This note asks exactly how far the audited direct `R--R` exchange in
`hadwiger_colorful_rk4_spqr_exchange.md` propagates through an arbitrary
SPQR tree.  The answer is not that portal vertices may be projected to the
poles of a virtual edge.  They may not.  Instead one carries an actual
portal occurrence on the boundary of the expansion behind that edge.

The resulting invariant passes through every `S`- and `P`-node.  At an
`R`-node, a portal-rich outgoing edge which is disjoint from, but not
cofacial with, the incoming edge gives the colourful rooted `K_4` and hence
`K_7`.  Thus the first genuine obstruction is a **co-polar wedge**: a
noncofacial outgoing edge sharing one incoming pole.  This is the precise
local form of the possible coherent two-apex residue.

The note proves this reduction.  It does not eliminate the co-polar wedge,
the two-face polarity described in Section 6, or the real-portal lock, and
therefore does not close the whole SPQR tree or `HC_7`.

We also assume the residual SPQR decomposition is planar torso-by-torso.
In particular every `R`-skeleton used below is planar.  Without this input
neither facial transport nor the planar rooted-`K_4` theorem applies.

Throughout, use the boundary notation

\[
 S=\{c_0,\ldots,c_5,z\},\qquad
 \overline{G[S]}=C_6\mathbin{\dot\cup}K_1,
\]

and the antipodal four-sets `X_j` of Section 2 of
`hadwiger_colorful_rk4_spqr_exchange.md`.  A portal occurrence of a label
`s` is an actual vertex in `P_s=N_D(s)`.  No virtual edge endpoint is called
a portal unless the corresponding boundary edge is literally present.

We work after excluding the following already isolated outcomes:

1. a colourful rooted `K_4` (and hence `K_7`);
2. a nested exact seven-cut;
3. the defect-one order-eight forced-incidence gate; and
4. a bounded capacity core.

Consequently every portal occurrence used below can be forced into the
required two- or four-label transversal by Lemmas 4.1--4.2 of the cited
note.  Every oriented proper two-separation side has boundary defect at
most one; in the negative two-piece state its defect is a singleton.

## 2. The one-hole state at a leaf

Let `e=pq` be the virtual edge by which a leaf `R`-torso `T_e` is attached
to the rest of the SPQR tree.  Let `L_e` be its open expansion.  Suppose its
singleton defect is `alpha` and the opposite open expansion has singleton
defect `beta`.

### Lemma 2.1 (leaf pole-face coherence)

All cycle-label portal occurrences in `L_e` lie on one face of `T_e`
incident with `e`.  If `alpha=z`, this face contains portal occurrences of
all six cycle labels.  If `alpha=c_a`, it contains all five cycle classes
other than `c_a`; the only demand which must be transported through the
rest of the SPQR tree is one actual `c_a`-portal.

### Proof

The left-hand half of Theorem 7.2 in
`hadwiger_colorful_rk4_spqr_exchange.md` uses only that the left augmented
side is a planar three-connected torso.  It does not use planarity of the
opposite expansion.  For an edge `ik` of the compatibility graph
`H(alpha|beta)`, force any prescribed occurrence of `i` into a distinct
two-label transversal in `L_e`, and force the complementary two roots of
the corresponding `X_j` on the opposite side.  A rooted `K_4` at
`i,k,p,q` in `T_e` would lift by Fabila--Monroy--Wood Lemma 12 to a
colourful rooted `K_4`.  Its absence puts the two occurrences with `p,q`
on one face.  The fixed-partner argument from the independent audit then
puts the full two portal classes on that face, and connectedness of
`H(alpha|beta)` propagates the face.

The sole disconnected compatibility graph occurs when
`alpha=beta=c_a`.  Both open sides then miss `c_a`, so fullness puts an
actual `c_a`-portal at one of `p,q`.  Lemma 7.3 of the cited note uses this
literal gate root to put the isolated antipodal-mate class on the same
face.  Hence every class which occurs in `L_e` is on one `e`-face.  The
last two assertions are just the two possible positions of the singleton
defect.  \(\square\)

If `alpha=z`, glue any embedding of the complementary expansion into the
other side of `e`.  The face in Lemma 2.1 survives and already supplies a
common-face SDR of the six cycle labels.  This is not yet the hypothesis of
the audited circular obstruction theorem, which needs the relevant full
portal sets on one face: further occurrences of those labels may lie in the
complementary expansion.  Thus `alpha=z` closes the *selection* problem,
but duplicate portal occurrences must still be transported.  If
`alpha=c_a`, there is additionally one missing-label demand for an actual
`c_a`-portal.

## 3. Exact transport invariant

Root the SPQR tree at the leaf edge `e`.  At a later node `mu`, let `f` be
the virtual edge toward the processed leaf subtree.  The processed
expansion has a plane embedding in a disk whose boundary contains:

* both poles of `f`; and
* actual, distinct representatives of the five cycle labels other than
  the hole `alpha`.

Call this the **one-hole invariant**.  It is completed at `mu` if an actual
`alpha`-portal in the unprocessed expansion can be put on a face incident
with `f`.  Gluing along `f` then gives one face containing a six-label SDR.

For a full-portal conclusion one must carry more data.  The **full-set
invariant** says that every occurrence, in the processed expansion, of each
of the six portal classes lies on the exposed boundary.  Every occurrence
still in the unprocessed expansion is a separate demand; it is not
represented by a pole.  Completion of the one-hole invariant therefore
does not by itself complete the full-set invariant.

### Lemma 3.1 (`S`- and `P`-nodes are transparent)

The one-hole invariant can be passed through any string of `S`- and
`P`-nodes until either it is completed or an `R`-node is reached.

### Proof

In an `S`-skeleton all skeleton edges lie on the same two facial cycles.
Choose an outgoing virtual edge whose expansion contains an
`alpha`-portal (or stop at a real portal vertex).  The incoming and
outgoing edges are incident with a common face, so the two disk embeddings
glue.  The five actual representatives already in the processed expansion
remain on the exposed boundary, while the unfilled `alpha` demand is passed
to the chosen outgoing expansion.  No `alpha`-portal is moved or projected.

In a `P`-skeleton choose an outgoing parallel edge whose expansion contains
an `alpha`-portal.  Permute the parallel edges so that it and the incoming
edge are consecutive and incident with the outer face.  Again glue the two
disk embeddings.  This operation moves no portal to a pole; the unfilled
demand remains attached to the outgoing expansion which actually contains
it.  Repeating proves the lemma.
\(\square\)

Thus branching at an `S`-node is harmless.  A `P`-node is also transparent
to a single demand.  For the full-set invariant we use the audited
two-component lock: a separation pair has only two nontrivial expansion
bridges, so after fixing the incoming bridge there is at most one
nontrivial outgoing bridge (a possible third parallel edge is real).
Hence all portal occurrences pass through the same outgoing expansion.
Without this two-component input, a `P`-node with portal-bearing expansions
on two different parallel edges would already be a full-set obstruction.

## 4. The disjoint-edge transport theorem

Let `T` be a planar three-connected `R`-skeleton.  Let `e=pq` be the
incoming virtual edge, and let `f=uv` be an outgoing virtual edge.  Say that
`f` is **alpha-active** if its expansion contains an actual
`alpha`-portal and, for some second cycle label `s`, distinct occurrences
of `alpha,s` can be forced in that expansion.  Outside the four excluded
capacity/adhesion outcomes, every edge whose expansion contains an
`alpha`-portal is alpha-active: choose any compatible `s` which is not the
one possible defect and apply the forced-incidence Hall lemma.

### Theorem 4.1 (disjoint noncofacial edges close)

If `e` and an alpha-active edge `f` have four distinct endpoints, then
they are incident with a common face of `T`.  Otherwise `G` has a `K_7`
minor.

### Proof

Suppose `e` and `f` are not cofacial.  Choose distinct portal occurrences
`x in P_alpha` and `y in P_s` in the expansion behind `f`.  Choose an
antipodal four-set `X_j` containing `alpha,s`; let its other two labels be
`a,b`.  Since the processed leaf side misses only `alpha`, Lemma 2.1
supplies distinct occurrences of `a,b` there.

The four endpoints `p,q,u,v` do not lie on one face of the plane
three-connected graph `T`: a face containing `p,q` is incident with the
edge `e`, and a face containing `u,v` is incident with `f`.  By the planar
rooted-`K_4` theorem, `T` has a `K_4` minor rooted at `p,q,u,v`.

Expand every virtual edge used by this model through its connected SPQR
expansion.  Apply Fabila--Monroy--Wood Lemma 12 first across `f`.  The
rooted model at `p,q,u,v` on the completed skeleton side lifts to a rooted
`K_4` at `p,q,x,y` in the unprocessed expansion.  Apply the same lemma a
second time across `e`.  The latter rooted model lifts to a rooted `K_4`
at the four actual portal occurrences for `a,b,alpha,s` in `D`.

These four labels are exactly `X_j`, so this is a colourful rooted `K_4`.
Lemma 2.1 of `hadwiger_colorful_rk4_spqr_exchange.md` completes it with
the opposite full shore, the universal root, and the omitted antipodal
pair to a `K_7` model.  This contradicts the standing exclusion.  Hence
`e,f` are cofacial.  \(\square\)

The theorem is genuinely about portal vertices inside the `f`-expansion.
The two applications of the rooted two-sum lemma are what transport them;
neither `u` nor `v` is substituted for `x` or `y`.

The identical proof applies to a duplicate occurrence of any already
carried label `r`, provided the `f`-expansion supplies a compatible second
label `s` and the other two labels of one antipodal four-set have actual
representatives in the processed expansion.  For the four labels outside
the antipodal pair containing the hole, this condition is automatic.  The
mate of the hole is exceptional: every antipodal four-set containing it
also contains the hole, so it cannot be treated until an actual hole-label
representative has been transported.

### Corollary 4.2 (first exact SPQR obstruction)

At the first `R`-node where the one-hole invariant cannot be passed, every
noncofacial alpha-active outgoing edge shares an endpoint with the incoming
edge `e=pq`.  Equivalently, the obstruction is contained in the union of
two rotation wedges

\[
 \{pr:pr\text{ is alpha-active and not cofacial with }pq\}
 \ \cup\
 \{qr:qr\text{ is alpha-active and not cofacial with }pq\}.
 \tag{4.1}
\]

All alpha-active edges disjoint from `e` lie on one of the two faces
incident with `e` and are individually transportable.  Thus an arbitrary
branching `R`-torso is reduced to a coherent two-pole, or two-apex, rotation
lock, together with the two-face compatibility issue below.

### Proof

An outgoing edge which is cofacial with `e` is transparent: choose their
common face and glue its expansion on that face.  Theorem 4.1 excludes
every disjoint noncofacial outgoing edge.  The only remaining graph edges
not cofacial with `e` are therefore incident with `p` or `q`, which is
exactly (4.1).  \(\square\)

### Theorem 4.3 (two active edges on opposite faces)

Let `f=uv` and `g=rs` be portal-bearing outgoing edges of `T`.  Suppose
each expansion has defect at most one and none of the Hall/adhesion/capacity
outcomes occurs.  If `f,g` have four distinct endpoints and are not
cofacial, then `G` has a `K_7` minor.

### Proof

Choose one antipodal four-set `X_j` and split it into two labels assigned
to the `f`-expansion and two assigned to the `g`-expansion.  Such a choice
always exists.  Each expansion misses at most one cycle label.  If their
two missing labels are different, put the label missed by `g` (when it
belongs to `X_j`) on the `f` side and the label missed by `f` on the `g`
side.  If the missing labels agree, choose `X_j` omitting their antipodal
pair.  A defect equal to `z` imposes no restriction because `z` is in no
`X_j`.  Fill the remaining positions arbitrarily.  The forced-incidence
Hall lemmas give two distinct actual representatives in each expansion.

Since `u,v,r,s` are not cofacial in the planar three-connected skeleton,
they root a `K_4` minor in `T`.  Apply Fabila--Monroy--Wood Lemma 12 across
`f`, and then across `g`.  Exactly as in Theorem 4.1, the two lifts produce
a rooted `K_4` at the four selected actual portal occurrences.  Their
labels are `X_j`, so colourful completion gives `K_7`.  \(\square\)

Now suppose `f` lies on one face incident with the incoming edge `e`, and
`g` lies on the other.  If Theorem 4.3 does not close the state, then
either `f,g` share an endpoint (the co-polar case), or they are themselves
cofacial.  In the latter case the three skeleton edges `e,f,g` correspond
to a triangle in the planar dual.  When `f,g` are disjoint this dual
triangle is nonfacial, hence separating.  We call this the **dual-triangle
polarity**.  It is a concrete three-face structure, not an arbitrary SPQR
branching.

## 5. The second exact obstruction: an off-face real portal

A real `alpha`-portal `r` of `T` is transportable exactly when it lies on
one of the two faces incident with `e`.  If it does not, then for every
vertex `t` distinct from `p,q,r`, the four vertices `p,q,r,t` are not
cofacial and hence root a `K_4` in `T`.

Consequently, if a compatible second-label portal can be represented by a
real vertex `t`, the colourful completion proof above applies directly.
Indeed `p,q,r,t` are not cofacial, so the planar rooted theorem gives the
needed rooted `K_4` in `T`.

If every compatible second-label representative lies strictly inside
outgoing expansions, this direct argument is no longer justified.  A
rooted `K_4` model in `T` may itself use the virtual edge whose expansion
contains the representative, so appending a path from an endpoint can
destroy branch-set disjointness.  Fabila--Monroy--Wood Lemma 12 is a
`(2,2)` theorem and does not cover this `(3,1)` distribution of roots.
Accordingly an off-face real `alpha`-portal with every compatible partner
strictly virtual is a second exact obstruction.  It should not be silently
folded into the co-polar case without a rooted `(3,1)` transport lemma.

Failure even to choose a distinct compatible partner is, by the
forced-incidence Hall theorem, one of the excluded order-seven,
order-eight, or bounded-capacity outcomes.

## 6. Exact conclusion and remaining lemma

Even when every active outgoing edge is cofacial with `e`, different edges
may occur on the two different faces incident with `e`.  A selected SDR can
choose one side, but the full portal sets cannot lie on one face when
portal occurrences are required through both sides.  Call this the
**two-face polarity** at `e`.  It is a genuine obstruction to invoking the
full-set circular theorem, not a cosmetic choice of reflection.

### Proposition 6.1 (conditional full-set composition)

Root the SPQR tree at a leaf.  Suppose that at every encountered `R`-node
with incoming edge `e` there is one face `F_e` incident with `e` such that

1. every real portal occurrence in the skeleton lies on `F_e`; and
2. every outgoing virtual edge whose expansion contains a portal
   occurrence is incident with `F_e`.

Assume recursively the same condition in every portal-bearing outgoing
expansion.  Then the whole shore has a plane embedding in which all six
portal sets lie on one face.

### Proof

Induct on the SPQR tree.  At an `R`-node glue every recursively embedded
portal-bearing expansion into the common face `F_e`, choosing the side of
its virtual edge opposite the already assembled part.  Conditions 1--2
keep every real and expanded portal occurrence on the boundary of the
merged face.  At an `S`-node use its facial cycle.  At a `P`-node the
two-component lock leaves only one nontrivial outgoing expansion, so order
the parallel edges with the incoming and outgoing expansions incident to
the outer face.  Leaf expansions start the induction by Lemma 2.1.  At no
step is an internal portal replaced by a pole.  \(\square\)

Thus failure of the global face has a first node, and that node is exactly
one of: an off-face real portal, portal-bearing edges on both `e`-faces, or
a portal-bearing edge not cofacial with `e`.  Theorem 4.1 reduces the last
case to the co-polar wedge whenever the edge carries a compatible
two-label state.

The audited direct `R--R` theorem does compose through an arbitrary SPQR
tree for a selected one-hole transversal.  For the full portal sets its
exact residual is:

\[
\boxed{
\begin{array}{c}
\text{common six-portal face}\quad\text{or}\quad K_7
\quad\text{or}\quad\text{exact-7/order-8/capacity descent}\cr
\text{or a co-polar nonconsecutive rotation wedge at one `R`-node,}\cr
\text{or an off-face real-portal `(3,1)` lock,}\cr
\text{or a co-polar/dual-triangle two-face polarity.}
\end{array}}
\tag{6.1}
\]

The old invalid induction failed because it treated an entire portal-rich
subtree as if its labels were situated at the poles.  The invariant above
keeps the actual occurrences, and Theorem 4.1 shows that only an
incident-edge degeneration evades the rooted `(2,2)` theorem.

The next theorem needed for closure is now exact and local.

> **Co-polar wedge exchange.**  In the residual `C_6 dotunion K_1`
> state, a collection of alpha-active virtual edges trapped in
> nonconsecutive rotation intervals around `p` or `q` either gives a
> colourful rooted `K_4`, exposes the defect-one order-eight gate, or all
> portal-bearing expansions lie in two disks after deleting `p,q`.

The companion local statement must either transport an off-face real root
and a partner hidden in one virtual expansion, or reduce that `(3,1)` state
to the same two-disk outcome.

The concentrated-fan theorem in `hadwiger_palette_anchor_rooted_star.md`
fits the last outcome exactly: a full Kempe fan at one pole contains a
literal `K_2 join overline{K_5}` minor, with the two centre bags playing
the pole pair.  This verifies that the static geometry of the residue is a
two-apex frame.  It does not yet identify its five palette-labelled leaves
with the boundary portal classes, so it is supporting structure rather
than a closure of the wedge.

The last outcome is the coherent 2-apex structure anticipated by the
near-`K_7` programme.  Proving this wedge exchange would make the one-hole
transport induction global; without it, claiming one global portal face is
not justified.
