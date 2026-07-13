# Audit of the first-incompatible-rotation two-torso note

## Verdict

**GREEN.**  The rooted models and the connectivity claims in
`hadwiger_first_incompatible_rotation_two_torso.md` are label-preserving
as stated.  No patch to that note is required.

## 1. Column contraction and union connectivity

After contracting the four pairwise disjoint columns `Q_i`, the image of
each `W_epsilon` is isomorphic to `W_epsilon`: no two vertices belonging
to the same page are identified.  The two page images intersect exactly
in the four distinct column images

\[
                         X=\{x_1,x_2,x_3,x_4\}.
\]

If both pages are four-connected, deletion of at most three vertices
leaves each page image connected.  At least one of the four vertices of
`X` survives, and that same surviving vertex lies in both connected page
remainders.  Their union is therefore connected.  Thus the contracted
union really is four-connected; this argument does not assume that the
deleted vertices all lie in `X`.

The analogous assertion in Theorem 2.4 is also correct: two
three-connected pages glued on four vertices remain connected after any
two deletions, since at least two common roots survive.

## 2. Full components behind the roots

A four-connected page has at least five vertices, so deleting its four
roots leaves a nonempty graph.  For any component `D` of that remainder,
all external neighbours of `D` in the page lie in `X`.  If
`|N(D)|<=3`, then some root lies outside `N(D)`, and deleting `N(D)`
separates the nonempty set `D` from that surviving root.  This contradicts
four-connectivity.  Hence

\[
                            N(D)=X.
\]

The two page components selected in Theorem 2.2 are automatically
disjoint because the page images intersect only in `X`, which the
components avoid.  The hypotheses of the double-full-page lemma are
therefore genuinely present.

In Theorem 2.4, failure of outcome 3 means exactly that each of the two
pages has at least one such `X`-full component; the quantifiers there are
correct.

## 3. Rooted `K_4` and the cofacial alternative

The four-connected specialization of the rooted-`K_4` theorem is used at
the correct strength: absence of an `X`-rooted `K_4` in a
four-connected graph leaves the planar embedding with all four named
roots on one face.  Four-connectivity excludes the lower-order
separation pieces appearing in the general rooted theorem.

In that embedding, an `X`-full connected component supplies an
`x_1`--`x_3` path with all internal vertices outside `X`; the other full
component supplies an internally disjoint `x_2`--`x_4` path.  The roots
are in facial cyclic order, so the two paths join alternating pairs in
the closed disk on the nonfacial side of the facial cycle.  The
Jordan-curve obstruction is applicable exactly as written.

For planar three-connected pages, a facial boundary is a cycle.  Thus
different root rotations yield two cycles meeting exactly in the four
roots after the pages are joined by the disjoint columns, and Lemma 1.1
applies without using a virtual edge.

## 4. Label-preserving lift

In the rooted model after column contraction, the four vertices `x_i`
belong to four distinct root bags.  Taking full inverse images under the
contraction replaces `x_i` by the entire connected path `Q_i` in its own
bag.  A connected branch bag lifts to a connected branch bag, quotient
adjacencies lift to actual edges, and pairwise disjointness is preserved
because the four contracted preimages are disjoint.  Hence every lifted
`i`th bag contains its named column and no column is split between bags.

The direct `K_7` lift is consequently sound: contacts from `Q_i` to
`B,T,U` become contacts from the named rooted bag `F_i`, and the seven
bags displayed in Corollary 3.1 satisfy all connectivity, disjointness,
and adjacency requirements.

## 5. Scope qualifications retained correctly

The note does not infer terminal rurality from treewidth two.  Its
`K_{2,3}` example correctly blocks that inference, and Theorem 4.2 adds
the annular terminal embedding as an explicit hypothesis.  Likewise the
final section requires four actual disjoint columns and state-forcing
marks; it does not replace them by abstract portal incidences or virtual
torso edges.

