# Finite-or-descent theorem for the three-shore Moser core

## 1. Setting and conclusion

Let \(G\) be seven-connected with \(\delta(G)\ge7\), let \(S\) be a
seven-vertex cut, and
suppose

\[
 G-S=D_1\mathbin{\dot\cup}D_2\mathbin{\dot\cup}D_3,
 \qquad N(D_i)=S.
\]

Assume that \(G[S]\) is the pure Moser spindle and that the unique
capacity-owner conclusion of
`hadwiger_three_shore_block_capacity.md`, Corollary 6.2, holds.  Thus
every optimal partition

\[
 \Pi=A_1\mid A_2\mid A_3\mid\{s\},
 \qquad |A_1|=|A_2|=|A_3|=2,
 \tag{1.1}
\]

has exactly one shore containing disjoint connected carriers for two
of its three pair blocks.

### Theorem 1.1 (low-owner finite-or-descent)

Some shore \(D\) owns at most five of the sixteen optimal Moser
partitions.  For every such shore, one of the following holds.

1. \(|D|\le5\).
2. A proper connected set \(C\subsetneq D\) has
   \(|N_G(C)|=7\).  More precisely, \(C\) is a component behind an
   internal two-cut of \(D\), or behind the three-face obstruction in a
   three-connected web synchronization.

In particular, if the selected low-owner shore is an inclusion-minimal
fragment among all seven-cuts of \(G\), then it has order at most five.

This eliminates every unbounded internally atomic three-shore Moser
cell.  The remaining obstruction is finite or descends through a
strictly smaller exact seven-cut.  This is a strict size descent, but it
is not by itself an iterable recursion theorem: the new seven-cut need
not have a Moser boundary, three shores, or an inherited ownership
state.

## 2. The sixteen matching states and ownership count

The non-singleton blocks of (1.1) are three disjoint nonedges of the
Moser spindle, covering \(S-\{s\}\).  There are exactly sixteen such
partitions.  This follows by the direct matching enumeration recorded
in `moser_three_shore_ownership_verify.py`; equivalently, list the
perfect matchings of the missing-edge graph after deleting each possible
singleton.

Since every partition has one owner, the three ownership counts sum to
sixteen.  Hence one shore \(D\) owns at most five partitions.  Fix it.
It is a nonowner for at least eleven partitions, and therefore it fails
all three two-pair demands in each of those partitions.

The singleton multiplicities are

\[
 4,2,2,2,2,2,2,                                      \tag{2.1}
\]

in the standard Moser labelling (the exceptional multiplicity belongs
to vertex \(0\)).  This is the same one-line perfect-matching list used
to obtain the total sixteen, and is checked by the verifier.  In
particular, no one singleton occurs in more than four partitions.

## 3. A Hall lemma for every six portal classes

For \(x\in S\), put \(P_x=N_D(x)\).  Every \(P_x\) is nonempty.

### Lemma 3.1 (six-class transversal or small shore)

For every \(s\in S\), either \(|D|\le5\), or the six sets
\((P_x:x\in S-\{s\})\) have a system of six distinct representatives.

#### Proof

If Hall fails, take \(I\subseteq S-\{s\}\) and

\[
 U=\bigcup_{x\in I}P_x,
 \qquad |U|<|I|.
\]

If \(D-U\ne\varnothing\), a component \(C\) of \(D-U\) has

\[
 N_G(C)\subseteq U\cup(S-I).
\]

Indeed, every portal in a class indexed by \(I\) lies in \(U\), and
different components of \(D-U\) are anticomplete.  The right side has
order at most

\[
 (|I|-1)+(7-|I|)=6,
\]

and separates \(C\) from either other full shore.  This contradicts
seven-connectivity.  Hence \(D=U\), so
\(|D|<|I|\le6\), and therefore \(|D|\le5\). \(\square\)

## 4. Synchronizing the three pair webs

Fix an unowned partition (1.1).  For every two of its pair blocks,
the corresponding four-terminal demand is crossless in \(D\).  The
bare-web argument from `hadwiger_three_shore_block_capacity.md` applies:
the same-vertex Two Paths completion has no nonempty clique inserted
behind a facial triangle, because the triangle together with the three
omitted boundary roots would be a cut of order at most six.  Thus \(D\)
is planar and there are faces

\[
 F_{12}\supseteq P(A_1)\cup P(A_2),\quad
 F_{13}\supseteq P(A_1)\cup P(A_3),\quad
 F_{23}\supseteq P(A_2)\cup P(A_3),                 \tag{4.1}
\]

where \(P(A)=\bigcup_{x\in A}P_x\).

### Lemma 4.1 (three-web synchronization)

Suppose \(D\) is three-connected, \(|D|\ge6\), and the six portal
classes outside the singleton of the selected partition have an SDR.
For an unowned partition, either all three faces in (4.1) coincide, or
a proper connected set \(C\subsetneq D\) has exactly seven neighbours
in \(G\).

#### Proof

Use the unique plane embedding of the three-connected graph \(D\).
Two distinct faces meet in at most one vertex or one edge.

If exactly two of the faces in (4.1) coincide, their common face and
the third face share the four portal classes belonging to two pair
blocks.  Their SDR supplies four distinct common vertices, impossible
for distinct faces.  Thus either all faces coincide or all are distinct.

In the latter case, the three pairwise face intersections respectively
contain the two portal classes of \(A_1,A_2,A_3\).  The SDR makes the
six selected representatives distinct.  Since a pair of distinct faces
has at most two common vertices, both complete portal classes belonging
to a shared pair are contained in the corresponding two-vertex face
intersection.  Their two distinct SDR representatives occupy its two
ends.  Hence the union

\[
 X=\bigcup_{x\in S-\{s\}}P_x
\]

has order exactly six; in fact each intersection is precisely its two
portal representatives.  If \(D-X\ne\varnothing\), take a component
\(C\) of \(D-X\).  Then

\[
 N_G(C)\subseteq X\cup\{s\}.                       \tag{4.2}
\]

The other full shores lie outside this set.  Seven-connectivity applied
to (4.2) forces equality throughout, so \(|N_G(C)|=7\).  Moreover
\(C\subsetneq D\), giving the second outcome.

It remains that \(D=X\), so \(|D|=6\).  Let the three pairwise face
intersections be the disjoint edges \(E_1,E_2,E_3\).  Each displayed
face contains two of these edges and cannot contain an endpoint of the
third, since that would enlarge one of its intersections with another
face.  Hence the three faces are four-cycles.  Their union is the
triangular prism, with no room for a further plane edge.

Every prism vertex has three neighbours in \(D\).  It belongs only to
the two represented boundary portal classes assigned to its shared
edge, and it can additionally see the omitted singleton \(s\).  Thus
its degree in \(G\) is at most \(3+2+1=6\), contrary to
\(\delta(G)\ge7\).  The all-distinct case is impossible when
\(D=X\) as well. \(\square\)

The lemma is label-free: it applies to any boundary partition into
three independent pairs and one omitted vertex.

## 5. The circular ownership bound

Assume now that \(|D|\ge6\), that \(D\) is three-connected, and that
the exact-cut outcome of Lemma 4.1 does not occur.  Lemma 3.1 gives the
required six-class SDR for each singleton.

Fix a singleton \(s\).  Suppose two partitions with singleton \(s\)
were both unowned.  Lemma 4.1 puts the same six complete portal classes
on a face for each partition.  The two faces coincide: their
intersection contains the union of those six portal classes, which has
order at least six by Hall, whereas two distinct faces of a
three-connected plane graph meet in at most one edge.

Choose an SDR for the six classes and read its representatives in
cyclic order on that common facial cycle.  In either unowned partition,
every two matching chords must alternate.  Otherwise two disjoint
facial arcs are connected carriers for the corresponding two blocks.
But on six cyclically ordered points there is only one pairwise-
alternating perfect matching: if the points occur as

\[
 x_1,x_2,x_3,x_4,x_5,x_6,
\]

it is forced to be

\[
 x_1x_4,\quad x_2x_5,\quad x_3x_6.                \tag{5.1}
\]

Thus at most one partition per singleton, and therefore at most seven
optimal partitions in total, can be unowned by \(D\).  But the
low-owner shore is unowned for at least eleven.
This contradiction proves Theorem 1.1 whenever \(D\) is
three-connected.

The verifier `moser_three_shore_ownership_verify.py` independently
checks the two finite inputs: there are sixteen optimal partitions, and
the sharp maximum in the circular count is seven.  Formula (5.1), not
the computation, is the proof of the latter bound.

## 6. Internal one- and two-separators

It remains to show that lack of three-connectivity gives the exact-cut
outcome, rather than a new infinite case.

### Lemma 6.1 (a cutvertex shore owns every partition)

If \(D\) has a cutvertex, then it owns all sixteen optimal partitions.

#### Proof

Let \(q\) be a cutvertex and choose two components \(C_1,C_2\) of
\(D-q\).  Since

\[
 N_G(C_i)\subseteq S\cup\{q\},
\]

seven-connectivity gives \(|N_S(C_i)|\ge6\).  For any partition
(1.1), each \(C_i\) fully contacts at least two of the three pair
blocks.  Choose distinct contacted pair blocks, one for each component.
The sets \(C_1\cup\{q\}\) and \(C_2\) are disjoint, connected and
adjacent, and realize those two blocks.  Hence \(D\) owns the partition.
\(\square\)

The low-owner shore therefore has no cutvertex.

### Lemma 6.2 (a low-owner two-cut descends)

Suppose \(D\) is two-connected but not three-connected.  Then a proper
connected set \(C\subsetneq D\) has \(|N_G(C)|=7\).

#### Proof

Take a two-cut \(\{p,q\}\) of \(D\), and let
\(R_1,\ldots,R_h\) be the components of \(D-\{p,q\}\).  Two-connectivity
implies that each \(R_j\) has a neighbour at both \(p\) and \(q\).
Moreover

\[
 N_G(R_j)\subseteq S\cup\{p,q\},
\]

so seven-connectivity gives \(|N_S(R_j)|\ge5\).

Fix any partition not owned by \(D\).  Let \({\cal F}_j\) be the set
of its three pair blocks which are fully contacted by \(R_j\).  Since
\(R_j\) misses at most two boundary roots, \({\cal F}_j\ne\varnothing\).
If two components admitted distinct choices from their sets
\({\cal F}_j\), the carriers

\[
 R_i\cup\{p\},\qquad R_j\cup\{q\}
\]

would be disjoint, connected and adjacent (each component attaches to
both cut vertices), giving a forbidden two-block realization.
Therefore the nonempty sets \({\cal F}_j\) have no distinct
representatives for any two indices.  They must all equal the same
singleton pair block.

It follows that every \(R_j\) misses exactly two boundary roots, one
from each of the other two pair blocks.  Hence

\[
 |N_S(R_j)|=5,
 \qquad
 N_G(R_j)=N_S(R_j)\cup\{p,q\},
\]

an exact seven-cut.  Taking \(C=R_j\) proves the lemma. \(\square\)

Lemmas 6.1--6.2 and the three-connected argument exhaust all connected
shores, completing the proof of Theorem 1.1.

## 7. What this changes

The three-shore pure-Moser residue is no longer an arbitrary collection
of portal-list conflicts.  Its unbounded part has a strict descent:

\[
 \text{low ownership}
 \Longrightarrow
 \text{simultaneous pair webs}
 \Longrightarrow
 \text{one facial portal order}
 \Longrightarrow
 \text{too many owned matchings},
\]

unless a smaller exact seven-cut appears.  This is precisely the
structural mechanism suggested by the finite web calculations.  The
only non-descending base has at most five shore vertices.

The word “descent” here has a precise but limited scope.  The new
fragment has strictly fewer vertices, so a chain of such exact fragments
cannot be infinite.  However, its new seven-vertex boundary is not shown
to be Moser and its complement is not shown to have three full shores.
Consequently this theorem alone cannot be reapplied at the next cut.
Closing the exported exact cut requires the separate general
two-/three-shore normalization, or an independently chosen global
minimum-fragment argument.  The present theorem does not justify
assuming that the low-owner shore of an arbitrary Moser cut is globally
minimum.
