# Adversarial audit: Moser three-shore owner count

## Verdict

**GREEN, after the clarifying repairs recorded in
hadwiger_moser_three_shore_owner_count.md.**

The exact theorem that survives is the following.

> Let \(G\) be seven-connected and six-minor-critical, with
> \(\delta(G)\ge 7\), and let a seven-cut \(S\) have exactly three full
> components \(D_1,D_2,D_3\).  If \(G[S]\) is the pure Moser spindle,
> then at least one \(D_i\) satisfies one of:
>
> 1. \(|D_i|\le 5\);
> 2. \(D_i\) has a cutvertex or a two-cut; or
> 3. there are \(s\in S\), \(X\subseteq V(D_i)\) with \(|X|=6\), and a
>    component \(C\) of \(D_i-X\) such that
>    \(N_G(C)=X\cup\{s\}\).

Equivalently, the three shores cannot all be atomic in the explicit
sense now given by (1.2) of the source note.

This conclusion is conditional on two already isolated inputs:

1. unique capacity ownership, Corollary 6.2 of
   hadwiger_three_shore_block_capacity.md; and
2. the standard same-vertex Two Paths Theorem in its maximal-crossless
   web form.

The first has its own GREEN audit.  The second is exactly Theorem 1.5
of Humeau--Pous: a maximally crossless tuple is the frame of a web.

## 1. Boundary states and the ownership count

The complement of the displayed Moser spindle is

\[
05,06,13,14,15,23,24,25,36,46.
\]

It is triangle-free, so every colour class in a four-colouring has
order at most two.  A four-colouring is therefore precisely a
three-edge matching in this complement plus its unmatched vertex.
Direct enumeration gives sixteen matchings, in the distribution

\[
4,2,2,2,2,2,2
\]

over the seven possible unmatched vertices.  The list in the source
contains all sixteen and no repetitions.

For each partition, Corollary 6.2 gives exactly one owner.  Its
at-most-one half allows the pair of blocks realized by a shore to
depend on the shore; its at-least-one half uses the three-web closure.
Thus each partition has exactly two non-owners, and the total number
of non-owner incidences is exactly \(2\cdot16=32\).

## 2. Portal SDR

For a fixed unmatched singleton \(s\), the six classes
\(P_x=N_D(x)\), \(x\ne s\), have an SDR.

Indeed, if a subfamily indexed by \(I\) has union \(U\) of order below
\(|I|\), then either \(D=U\), which contradicts
\(|D|\ge6\ge |I|>|U|\), or a component of \(D-U\) has all neighbours
in

\[
U\cup(S-I),
\]

of order at most six.  A different full shore remains on the far side,
contradicting seven-connectivity.  This argument permits arbitrary
overlap among portal sets; it only produces one fixed set of six
distinct representatives.

## 3. Exact use of the Two Paths Theorem

For two pair blocks, add four artificial terminals and join each to
its complete portal set.  Two disjoint crossing paths are exactly two
disjoint connected block carriers.  Non-ownership therefore makes the
four-terminal tuple crossless.

Complete on the same vertex set to a maximal crossless graph.  The
Two Paths Theorem yields a web whose frame is the artificial terminal
tuple.  A nonempty clique behind a facial triangle cannot contain an
original shore vertex.  If it did, replace any artificial frame
vertices among its at most three attachments by the corresponding
boundary roots, and add the other three boundary roots omitted from
this demand.  At most six actual vertices would separate that clique
interior from another full shore.  This contradicts
seven-connectivity.

Thus the web is bare.  Removing its four artificial frame vertices
merges all incident faces with the frame face, so all four complete
portal sets, not merely four selected representatives, lie on one face
of \(D\).  Removing completion edges only merges faces.  The first such
web proves \(D\) planar; three-connectivity and Whitney uniqueness then
put all three demand faces in the same fixed embedding, up to a global
reflection.

This resolves the two potential quantifier errors:

* different demands do not choose unrelated embeddings of \(D\); and
* different demands do not choose unrelated representatives of a
  portal class.

## 4. Face intersections and the prism alternative

In a three-connected plane graph, two distinct facial cycles meet in
at most one edge.  If two demand faces coincide, the coincident face
contains all six portal classes.  A distinct third demand face would
share four fixed SDR representatives with it, impossible.  Hence
either all three faces coincide or all three are distinct.

In the all-distinct case, two faces corresponding to demands that share
the matching edge \(xy\) contain both complete sets \(P_x,P_y\).
Their intersection contains the distinct SDR representatives
\(p_x,p_y\), so it is exactly one edge.  Moreover

\[
P_x\cup P_y
\]

is contained in that edge and contains its two ends.  Thus it equals
the two-end set.  The three shared edges are disjoint, and the union
of all six portal sets has exactly six vertices.  Portal-set overlap is
therefore harmless: a vertex can belong to both classes assigned to
its shared edge, but to no class assigned to either other shared edge.

If vertices of \(D\) remain outside this six-set \(X\), a component
\(C\) of \(D-X\) has

\[
N_G(C)\subseteq X\cup\{s\}.
\]

Seven-connectivity and an untouched shore on the far side force
equality.  This is exactly the explicitly quantified nested
six-shore-plus-one-boundary cut excluded by atomicity; there is no
uncovered orientation or residual-component case.

If \(D=X\), each of the three demand faces contains its two designated
shared edges and cannot contain an end of the third shared edge.
Hence all three are four-cycles.  Their union is an annulus with two
triangular boundary components.  The selected four-cycles are faces,
and a triangular complementary region admits no chord, so extra prism
edges are impossible.  Thus \(D\) is exactly the triangular prism.

Each prism vertex has three shore neighbours, at most two neighbours
among the six represented boundary roots (the two classes belonging
to its shared edge), and at most the omitted root \(s\).  Therefore
its degree is at most six, contradicting \(\delta(G)\ge7\).

The all-distinct case is eliminated, so every non-owner matching puts
all six complete portal sets on one face.

## 5. Antipodal uniqueness

On a facial cycle, two disjoint pairs that do not alternate have
vertex-disjoint facial arcs joining their respective ends.  Those arcs
are valid connected carriers; they may pass through portal vertices of
the third pair, which is allowed.  Non-ownership therefore forces every
two matching chords to alternate.

Three disjoint pair chords on six points are pairwise alternating only
in cyclic order

\[
e_1,e_2,e_3,e_1,e_2,e_3,
\]

up to permutation and reversal.  Hence the matching is the unique
antipodal perfect matching of those six fixed representatives.

For a fixed singleton \(s\), two non-owner matchings would give two
faces containing the same six complete portal sets.  The faces must be
the same, since otherwise they share six distinct SDR representatives.
That one cyclic order has only one antipodal perfect matching.
Therefore a fixed shore is a non-owner for at most one partition for
each \(s\), and for at most seven partitions overall.

The three atomic shores would consequently contribute at most
\(3\cdot7=21\) non-owner incidences, contradicting the exact count
\(32\).

## 6. Scope corrections

The proof eliminates all three-connected large shores without the
specified nested exact cut.  It does not show that a shore with a
one- or two-cut has bounded order.  The source note was repaired to
describe that outcome only as a low-order portal decomposition.  The
finite conclusion applies solely to the \(|D|\le5\) branch.

