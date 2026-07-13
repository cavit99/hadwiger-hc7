# Set-rooted Two Paths gives one labelled rural order

## Status and proof-spine role

This is an **audited theorem**.  It removes a
specific part of the frame-transport gap: changing the chosen attachment
vertices inside one fixed 4-connected connector cannot create signed
holonomy.  Failure of the required private carrier pair places the *whole
attachment sets*, not merely one selected root pair, in one labelled
four-block order on one facial cycle.

The theorem uses only the standard 4-connected form of the Two Paths
Theorem quoted in
`../results/hc7_near_k7_common_row_rural_book.md`.

## Theorem 1 (four-set rural block theorem)

Let `H` be a 4-connected graph and let `A,B,P,Q` be nonempty, pairwise
disjoint subsets of `V(H)`.  Exactly one of the following holds.

1. `H` contains two vertex-disjoint paths, one joining `A` to `P` and
   the other joining `B` to `Q`.
2. `H` is planar.  In its unique spherical embedding there is one facial
   cycle `F` containing every vertex of

   \[
                         A\cup B\cup P\cup Q.             \tag{1.1}
   \]

   Up to reflection, the four sets occur on `F` in the cyclic block order

   \[
                              A,\ Q,\ P,\ B.              \tag{1.2}
   \]

   More precisely, after choosing an orientation of `F`, every `A`
   occurrence precedes every `Q` occurrence, every `Q` occurrence
   precedes every `P` occurrence, every `P` occurrence precedes every
   `B` occurrence, and every `B` occurrence precedes every `A`
   occurrence, with no member of another displayed set between two
   consecutive blocks.

### Proof

Suppose outcome 1 fails.  For every choice

\[
                a\in A,\quad b\in B,\quad p\in P,\quad q\in Q,
                                                               \tag{1.3}
\]

the four terminals are distinct and there are no disjoint `a-p` and
`b-q` paths.  The 4-connected Two Paths Theorem therefore makes `H`
planar and puts `a,b,p,q` in alternating order on one facial cycle.
Four-connectivity implies 3-connectivity, so Whitney uniqueness gives one
spherical embedding up to reflection.

Fix `a_0,b_0,p_0,q_0` and call their alternating face `F`.  Replace one
of the four selected terminals at a time.  The new alternating face and
`F` contain the other three fixed vertices.  Two distinct faces of a
3-connected plane graph cannot have three distinct common boundary
vertices: their common boundary would give a separation of order at most
two.  Hence the new face is always `F`.  Varying all four choices proves
(1.1).

Reflect the embedding if necessary so that the cyclic order of the fixed
quadruple is

\[
                         a_0,\ q_0,\ p_0,\ b_0.           \tag{1.4}
\]

Let `J` be the open `a_0-b_0` arc of `F` containing `q_0,p_0`.
For any `p in P`, alternation of
`a_0,b_0,p,q_0` puts `p` on `J`; for any `q in Q`, alternation of
`a_0,b_0,p_0,q` puts `q` on `J`.  Applying alternation simultaneously to
an arbitrary `p in P,q in Q` shows that, on the oriented arc from `a_0`
to `b_0`, every `q` precedes every `p`.  Thus `Q` and `P` are two
noninterleaving blocks on `J`, in that order.

Use now the complementary open `p_0-q_0` arc of `F`, the one containing
`b_0,a_0`.  Alternation of `a,b_0,p_0,q_0` puts every `a in A` on that
arc, and alternation of `a_0,b,p_0,q_0` puts every `b in B` there.
For arbitrary `a in A,b in B`, alternation says that on the oriented arc
from `p_0` to `q_0`, every `b` precedes every `a`.  Combining this with
the `Q,P` order on `J` gives precisely the cyclic block order
`A,Q,P,B`.  This proves outcome 2.

Conversely, in a plane graph the ends of the two prescribed paths
alternate on the common facial cycle in (1.2).  The Jordan curve theorem
precludes two vertex-disjoint paths for those crossing pairs.  Hence the
two outcomes are exclusive. \(\square\)

## Theorem 2 (set-rooted rural holonomy is flat)

Let `H` be 4-connected, let `A,B` be nonempty disjoint root sets, let `I`
contain at least two labels, and let `P_i` (`i in I`) be nonempty pairwise
disjoint portal sets, all disjoint from `A union B`.  Let `Q_0` be a
loopless directed graph with nonempty arc set on `I` whose underlying
undirected graph is connected.  For every arc `i -> j`, assume that there
are no disjoint paths joining `A` to `P_i` and `B` to `P_j`.

Then `H` has one spherical embedding and one facial cycle containing

\[
                         A\cup B\cup\bigcup_{i\in I}P_i. \tag{2.1}
\]

All portal sets occur between the same two root blocks.  Orient that
facial arc from the `B` block towards the `A` block.  For every arc
`i -> j`, every occurrence of `P_i` precedes every occurrence of `P_j`.
Consequently `Q_0` is acyclic and every comparison is the restriction of
one linear facial order.

### Proof

Apply Theorem 1 to `A,B,P_i,P_j` for one arc.  It gives one face and the
block order `A,P_j,P_i,B`, up to reflection.  Traverse a spanning tree of
the underlying connected graph of `Q_0`.  On each new edge, the face
given by Theorem 1 shares all vertices of the two nonempty root sets and
all vertices of the already placed nonempty portal set with the old face;
in particular it shares three distinct vertices.  It is therefore the
same face.  This puts all portal sets on that face and between the same
two root blocks.

On the arc oriented from `B` to `A`, the order
`A,P_j,P_i,B` reads `B,P_i,P_j,A`.  Hence every arc `i -> j` is a strict
left-to-right comparison `P_i<P_j` on one line.  A directed cycle is
impossible. \(\square\)

## Corollary 3 (literal HC7 discharge inside one connector)

In an overlap-one rotation `D={a,i}`, `E={a,j}`, take

\[
 A=N_Z(X),\qquad B=N_Z(W),\qquad P_i=N_Z(F_i),\qquad
 P_j=N_Z(F_j).                                             \tag{3.1}
\]

Whenever these four sets are nonempty and pairwise disjoint, either the
private carrier pair exists, in which case Lemma 2 of
`../results/hc7_near_k7_common_row_rural_book.md` and the robust rotation
theorem give a `K_7^-` model, or all possible choices of the two literal
attachment roots lie in the one labelled rural block order of Theorem 1.

Thus attachment-root changes *within the fixed connector `Z`* cannot be
the source of nontrivial signed holonomy.  A surviving holonomy must
change the connector torso, cross an actual adhesion, use overlapping
portal classes, or use the separate concentrated two-piece rotation.

## Trust boundary

The theorem does not transport a facial order across different
4-connected torsos or across a cutvertex/2-adhesion.  It also deliberately
requires disjoint portal classes; a vertex serving two row labels must be
handled by a literal common-portal absorption/promotion argument.  The
remaining proof-spine link is therefore an actual torso/adhesion exchange,
not a choice-of-root problem.
