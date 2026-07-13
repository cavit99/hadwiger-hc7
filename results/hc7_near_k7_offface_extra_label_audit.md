# Independent audit: off-face extra-label exchange

## Verdict

**GREEN AS PATCHED.**  The rooted-model theorem is correct, and the
capacity-clone corollary is correct after explicitly requiring (i) four
distinct actual roots satisfying the theorem and (ii) a pairwise disjoint
underlying crossing-carrier family.  An abstract incidence matching alone
does not imply either condition.

## 1. SDR saturation and facial coherence

Lemma 1.1 is exact.  Starting from one full SDR, an element `q` outside
its image can replace the representative of any set containing `q` without
colliding with the other representatives.  If `q` is already in the image,
that SDR already witnesses its occurrence.  The lemma claims occurrence in
the image, not assignment to a prescribed row, which is precisely what the
fixed-extension facial-coherence theorem uses.

Consequently Corollary 1.2 correctly puts the entire union of the four
portal families on one face once their transversal rank is four.  The
off-face degree escape is therefore not an unusable member of one of those
families; it carries an additional literal role.  This conclusion remains
local to the stated locked page and its fixed extensions.

## 2. Rooted-`K_4` step

In Theorem 3.1 the four roots `l,r,h,w` are actual, distinct vertices.
The rooted-`K_4` dichotomy for a 4-connected graph gives either the rooted
model or a planar embedding with all four roots on one face.  The graph
`K` is planar and 4-connected, hence 3-connected and has a unique plane
embedding up to reflection.  In a 3-connected plane graph two different
faces cannot share three distinct vertices: facial boundaries are cycles
and two of them meet in at most one edge.  Thus the three roots on `F`
force any common face to be `F`, contradicting `w notin V(F)`.  The rooted
model exists.

Adjoining its four disjoint rooted pieces separately to the disjoint
outside sets `L,R,H,J` preserves connectedness and disjointness.  Pairwise
adjacency is inherited from the rooted `K_4` model.  Hence the construction
really duplicates the two row duties `H,J` across the two path shores.

## 3. Capacity clone

The first clause of Corollary 3.2 explicitly assumes the portals of
Theorem 3.1 and is sound.  The other row duties use mutually disjoint
carriers outside `K`, so rooted row promotion composes with the four pieces
inside `K`; literal shore completion then gives `K_7`.

The original formal-clone wording needed two explicit hypotheses.  A
matching in the row--carrier incidence graph records only nonempty contact:
the same vertex of `K` can carry the left-side, right-side and face-row
contacts, so it need not supply distinct `l,r,h`.  Also, simultaneous
promotion requires the carrier vertices of the incidence graph to denote
pairwise disjoint connected pieces.  The patched statement now requires
both a pairwise disjoint crossing-carrier family and four distinct actual
roots `l,r,h,w` satisfying (3.1)--(3.2).  Under those hypotheses Theorem
3.1 literally realizes the two formal copies, and the proof is valid.

## 4. Scope

The result does not show that every off-face extra label repairs the
original Hall defect.  The square-antiprism example correctly shows the
wrong-label obstruction: an extra attachment can lie off the locked face
without helping either crossing terminal pair.  The theorem closes only
the capacity-compatible subcase certified by the distinct rooted portals;
the surviving wrong-label cell still needs a label exchange, a faithful
proper-minor state splice, or a split of the extra-row carrier.
