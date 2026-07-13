# The forced off-face attachment has an extra literal label

## Status

The planar degree-escape theorem forces an external attachment away from
the coherent locked face.  This note proves that such an attachment
cannot be a Hall-deficient representative of one of the four locked
portal families.  Once one full portal SDR exists, every vertex in the
union of those families occurs in a full SDR.  Facial coherence therefore
puts their entire union on the locked face.

The degree escape consequently has a genuinely extra literal label.  A
square-antiprism witness shows that wrong-label attachment alone does not
repair the alternating protected linkage.  The next theorem must use the
reserve/pool adjacencies of that extra row; there is no remaining
four-family Hall-rank alternative.

## 1. No unusable portal exists at full rank

### Lemma 1.1 (one-swap SDR saturation)

Let `P_1,...,P_r` be finite sets which admit a system of distinct
representatives.  Every element of

\[
                         P_1\cup\cdots\cup P_r             \tag{1.1}
\]

occurs in the image of some full system of distinct representatives.

#### Proof

Fix an SDR `(p_1,...,p_r)`.  Let `q in P_i` for some `i`.  If `q` is
already among the `p_j`, the fixed SDR contains it.  Otherwise replace
`p_i` by `q` and retain every other representative.  Since `q` was not
in the old image, the resulting representatives remain distinct.  QED.

The statement concerns occurrence as a portal vertex, not occurrence in
one prescribed row role.  That is exactly the notion used by the SDR
facial-coherence theorem.

### Corollary 1.2 (all locked portals lie on the coherent face)

Let `K` be the four-connected planar obstruction page in the locked
two-row theorem, and let `P_1,...,P_4` be its four literal portal
families.  Assume their transversal rank is four.  If `G` has no
`K_7` minor, then the coherent face supplied by the active-root theorem
contains

\[
                           P_1\cup P_2\cup P_3\cup P_4.    \tag{1.2}
\]

#### Proof

The SDR face theorem puts on one face every portal vertex which occurs
in at least one full SDR.  Lemma 1.1 says that this is the entire union
in (1.2).  QED.

### Corollary 1.3 (the degree escape has an extra label)

In the hypothetical `HC_7` setting, let `F` be the coherent locked face.
The off-face external attachment forced by the planar carrier degree-
escape theorem is not a member of any of `P_1,...,P_4`.  Its external
edge therefore belongs to another foreign row, another part of the path
carrier, or another expansion society.

In particular, the alternative “a locked portal exists off `F` but is
excluded from every full SDR by Hall failure” is empty.

## 2. Smallest portal-system obstruction to relabelling the escape

Let `K=C_8^2` be the square-antiprism.  Its four even vertices form a
facial square; in cyclic order call them

\[
                         a_L,a_R,p_H,p_Q.                  \tag{2.1}
\]

Take the four locked portal sets to be the corresponding singletons.
They have a unique full SDR, and their two prescribed pairs

\[
                         (a_L,p_H),\qquad(a_R,p_Q)         \tag{2.2}

alternate on the face.  The Jordan curve theorem therefore forbids two
vertex-disjoint paths for (2.2) inside `K`.

Now give an odd vertex, say vertex `1`, an external edge carrying a
fifth row label `R`.  This is a literal off-face attachment, but it is
not a member of any of the four portal sets.  It neither changes their
rank nor supplies either path in (2.2).  Adding arbitrarily many further
wrong-label attachments at odd vertices has the same property.

This is a portal-system counterexample, not a full critical host.  It
refutes the purely local implication

\[
 \text{off-face external attachment + rank-four locked portals}
 \Longrightarrow \text{locked SDR exchange or protected linkage}.
\]

The obstruction is label-exact: the escape has useful geometric
location but the wrong branch-set duty.

## 3. Exact additional hypothesis needed

The off-face location does have one uniform label-preserving use.

### Theorem 3.1 (off-face portal gives capacity two)

Let `K` be four-connected and planar, and let `F` be a face.  Let
`L,R,H,J` be four pairwise disjoint connected sets outside `K`.  Suppose
there are distinct vertices

\[
 l\in N_K(L),\quad r\in N_K(R),\quad h\in N_K(H)
                         \quad\hbox{on }F,                 \tag{3.1}
\]

and a vertex

\[
                         w\in N_K(J)-V(F).                 \tag{3.2}
\]

Then `K` contains four pairwise disjoint connected pairwise adjacent
sets rooted respectively at `l,r,h,w`.  Consequently the four enlarged
sets obtained by adjoining the rooted pieces to `L,R,H,J` are connected,
disjoint and pairwise adjacent.  In particular, this one carrier
simultaneously makes both rows `H,J` adjacent to both path shores
`L,R`.

#### Proof

Apply the rooted-`K_4` theorem to `l,r,h,w`.  Its non-model outcome would
put all four roots on one face of the unique plane embedding of `K`.
But a face other than `F` cannot share the three distinct vertices
`l,r,h` with `F` in a three-connected plane graph, while `F` does not
contain `w`.  Hence the rooted `K_4` model exists.

Adjoin its four rooted branch sets to `L,R,H,J` through the four literal
portal edges.  Rooted branch sets are disjoint, connected and pairwise
adjacent; adjoining the disjoint outside roots preserves all three
properties.  QED.

Theorem 3.1 is the precise benefit of the Euler escape: an off-face row
turns a unit-capacity carrier into a two-row carrier.  It does not choose
which old helper can be released.

### Corollary 3.2 (capacity-clone criterion)

In the one-missing path-cut capacity system, suppose all row duties other
than `H,J` can be assigned to pairwise disjoint crossing carriers outside
`K`.  If `K` has the portals (3.1)--(3.2), then the two shores and the
five retained foreign rows form a literal `K_7` model.

More generally, form the row--carrier incidence graph from a pairwise
disjoint family of crossing carriers and add one formal clone of `K`
dedicated to the off-face row `J`.  If this augmented
incidence graph has a row-saturating matching in which the original copy
of `K` is assigned to a row having a face portal, **and the selected
matching comes with four distinct actual roots `l,r,h,w` satisfying
(3.1)--(3.2)**, Theorem 3.1 realizes the two matched copies by disjoint
rooted branch sets; ordinary whole-carrier promotion realizes every other
matched edge.  Literal shore completion then gives `K_7`.

#### Proof

Use Theorem 3.1 for the two duties assigned to `K` and its clone.  Use
rooted row promotion for every other matched carrier.  All selected old
exterior carriers are pairwise disjoint and disjoint from the foreign
rows and path sides, so the enlarged shores and rows remain disjoint.
Both shores see all five rows and are adjacent across the path cut;
the one-missing shore-completion lemma applies.  QED.

The distinct-root hypothesis in the formal-clone formulation is
essential.  An incidence matching records only that `K` meets the two
path sides and the two rows; the same vertex of `K` may carry several of
those contacts.  Such a matching alone does not supply the four rooted
pieces required by Theorem 3.1.

This also pinpoints the surviving static obstruction.  If the off-face
row `J` lies outside the minimal Hall-deficient row set (for example the
deficient set is exactly `{H,Q}` with sole neighbour `K`), dedicating the
extra capacity to `J` need not repair the unmatched row `Q`.  The
square-antiprism portal witness realizes precisely this wrong-label
situation.  A proper-minor state or a further labelled alternating
exchange is still required.

A positive continuation must show that the extra row carrying the escape
has enough literal reserve/pool adjacencies to be **spent**, for example
by one of the following operations:

1. absorb a connected off-face-to-face corridor into that extra row and
   promote one of its old face contacts into the vacated locked duty;
2. split the extra-row carrier into two adjacent connected pieces, one
   retaining the extra row and one taking a locked duty; or
3. use a proper-minor equality state to exchange the extra row label with
   a locked row across the actual adhesion.

Merely knowing that an external neighbour exists off `F` supplies none
of these label-preserving operations.  Conversely, no further Hall
analysis of the original four portal sets can help: Lemma 1.1 has already
made their whole union facial.
