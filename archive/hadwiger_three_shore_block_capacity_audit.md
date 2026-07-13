# Adversarial audit: three-shore block capacity

## Verdict

**GREEN.**  Theorems 2.1 and 5.1 of
`hadwiger_three_shore_block_capacity.md` are sound.  The contraction
models are genuine proper minors, their colourings expand to the claimed
labelled equality partitions, the Two Paths obstruction gives the stated
bare web under seven-connectivity, and Diwan's safe-precolouring theorem
applies exactly to the induced four-cycle used in Theorem 5.1.

The resulting theorem is substantive: the entire three-shore
\((3,2,2)\) branch is eliminated.  Together with the audited boundary
classification and clique-residual gluing, every three-shore cut now has
the pure Moser spindle as its boundary.

The analogous unrestricted planar-extension step is false in the pure
Moser branch.  Section 6 of the source note now records two explicit
safe-colouring barriers.

## 1. Two-block capacity and contraction

If a shore \(D\) contains disjoint connected carriers \(X_h,X_k\) for
two boundary blocks, connectedness of \(D\) makes the carriers adjacent:
take a shortest path between them and divide its internal vertices at
one edge.  The enlarged carriers remain disjoint and retain every portal
contact.

For a fixed side \(D_i\), choose a capable opposite shore \(R\) and let
\(F\) be the remaining shore.  The branch sets

\[
 X_h\cup A_h,\qquad X_k\cup A_k,\qquad F\cup A_\ell
\]

are connected and disjoint.  The first two are adjacent by construction;
the third is adjacent to both because \(F\) is full.  Contracting these
sets and deleting unused vertices is a proper minor operation.

For a three-block partition the images form \(K_3\).  For a four-block
partition with singleton \(s\), optimality forces \(s\) to have a
boundary neighbour in every other colour block.  Therefore the three
contracted images together with \(s\) form \(K_4\).  An \(r\)-colouring
of the minor assigns the displayed blocks distinct colours.

Expansion is legitimate.  An edge from a boundary block to \(D_i\)
survives as an edge from its contracted image to the same vertex of
\(D_i\); internal shore vertices used in the contraction have no edges
to \(D_i\), since different components of \(G-S\) are anticomplete.
Thus the expanded side colouring is proper and has exactly the original
labelled partition.  Two capable shores suffice for all three choices of
\(D_i\), even when they realize different pairs in the four-block case.
Palette permutations align the common labelled blocks, and the side
colourings glue.

## 2. The bare-web reduction

For pair blocks \(A=\{a_1,a_2\}\) and
\(B=\{b_1,b_2\}\), attach four artificial terminals to their complete
portal sets in a shore.  A cross in order
\(a_1,b_1,a_2,b_2\) is equivalent to two disjoint carriers: deleting
the terminal ends yields disjoint connected portal paths, and the
shortest-connector operation makes their carriers adjacent.

In the crossless case, the same-vertex web form of the Two Paths Theorem
applies.  A nonempty inserted part behind a facial triangle cannot contain
original shore vertices.  Its represented neighbours are among at most
three facial vertices.  Replacing any artificial terminal among them by
its actual root does not increase the count; adding the three unrepresented
roots of the seven-set gives an actual separator of order at most six.
Either of the other full shores remains on the far side, contradicting
seven-connectivity.  Hence the web is bare.

After replacing artificial terminals by the roots, all actual root-root
edges lie in the added \(K_{2,2}\) frame: each colour block is independent,
and every possible cross-block edge is one of those four frame edges.
Therefore

\[
H_i^+=G[D_i\cup A\cup B]+E(K_{A,B})
\]

is planar, and its four roots induce exactly the frame \(C_4\).

## 3. Audit of the forcing minor in Theorem 5.1

For the optimal partition \(S=T\dot\cup A\dot\cup B\) of sizes
\(3,2,2\), two shores \(D_1,D_2\) are crossless for the paired demand.
Contract

\[
Q_0=D_1\cup T,qquad Q_1=D_2\cup A.
\]

Both sets are connected by fullness, they are disjoint, and they are
adjacent because \(D_1\) sees every vertex of \(A\).  Each contracted
image sees both retained vertices of \(B\).  A six-colouring of this
proper minor, expanded over the boundary but retaining its colouring on
\(D_3\), consequently has:

* one colour \(0\) on all of \(T\);
* a different colour \(1\) on all of \(A\);
* neither \(0\) nor \(1\) on either vertex of \(B\).

All edges to \(D_3\) remain represented after contraction, so this is a
proper colouring of \(G[S\cup D_3]\), not merely of its boundary.

On the induced frame cycle in either bare web, the restriction uses
colour \(1\) on \(A\) and at most two colours from \(\{2,3,4,5\}\) on
\(B\).  It is proper on all four added frame edges and uses at most three
of the five available colours.

Diwan's Corollary 1 states that a proper \(k\)-colouring of an induced
cycle of length at most \(2k-5\), using at most \(k-1\) colours, is safe
in every planar supergraph containing that induced cycle.  With \(k=5\)
and cycle length four, every hypothesis holds.  The theorem was checked
against the primary source, arXiv:2306.04944, Corollary 1.

The two five-colour extensions agree with the retained side colouring on
\(A\cup B\).  They omit colour \(0\), so every edge from either web shore
to the colour-zero block \(T\) is proper.  There are no edges between
distinct shores.  Every boundary edge and every edge incident with
\(D_3\) was already proper in the retained minor colouring.  The global
six-colouring contradiction follows.

## 4. Pure-Moser extension barrier

The unrestricted two-web question has a positive answer.  Glue the two
bare disks on opposite sides of their common induced frame \(C_4\).  The
union is planar and the cycle stays induced.  Any proper six-precolouring
of the frame uses at most four colours, so Diwan's corollary with \(k=6\)
extends it over the entire glued union.  This is Lemma 6.1 of the source
note.

What fails is compatibility with the three boundary roots omitted from
that frame.

For the pure Moser partition

\[
\{1,3\}\mid\{2,5\}\mid\{4,6\}\mid\{0\},
\]

a single four-web omits one pair block and the singleton.  They require
two distinct reserved colours, leaving only four colours for the frame.
Diwan proves that no proper four-colouring of a cycle of length at least
four is universally safe, so the exact manoeuvre of Theorem 5.1 cannot
work with an arbitrary bare web.

Even perfect synchronization of the three pair webs would not make the
obvious five-colour argument valid.  The six paired roots have cyclic
word \(ABCABC\).  On the three arcs \([1,3],[3,5],[5,1]\), every one of
the colours \(A,B,C\) occurs.  For \(k=5\), their common set has size
\(3=k-2\), Diwan's explicit bad-colouring condition.  Adding an interior
triangle whose three vertices respectively see those three arcs gives a
planar graph to which this precolouring does not extend: every triangle
vertex loses \(A,B,C\) and only two colours remain.

Using all six colours does make an arbitrary frame-\(C_4\) precolouring
safe, but it does not solve the original gluing problem.  A planar
extension may use either omitted boundary colour on an actual portal
neighbour of that omitted root.  Fullness ensures those edges exist, and
neither the safe-colouring theorem nor bare planarity controls their
locations.

Therefore the exact remaining three-shore problem is the pure-Moser
portal/list-colour lock.  Closing it requires a portal-specific forbidden-
colour extension or a minor-critical state transition; unrestricted
planar precolouring is demonstrably insufficient.
