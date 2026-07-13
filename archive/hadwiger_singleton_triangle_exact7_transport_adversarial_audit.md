# Adversarial audit of exact-seven-cut linkage transport

## Verdict

**GREEN, conditional only on the already stated two-pair web theorem and
the nested minimum-cut linkage lemma.**  I found no branch-set overlap,
unjustified contraction, or missing adjacency in the transport argument.
The proof does not close the terminal singleton cell, and it does not claim
to do so.

Two short exposition patches are needed before the note should be used as a
stand-alone lemma:

1. after Lemma 3.2, explicitly note that Lemma 3.1 implies \(|F|\ge4\)
   (the four pair-root portal sets have at least eight incidences, while a
   vertex contributes at most two), so that “no cutvertex and no two-cut”
   really does imply three-connectivity under the standard order convention;
2. in Lemma 2.1, write down the two nested separations explicitly.  This
   removes any ambiguity about where the linkage interiors lie.

Neither patch changes the mathematics.  A third, optional clarity patch is
to display the lifted carriers in Lemma 2.2 rather than describe their
concatenation verbally.

## 1. Nested linkage and confinement

For the outer cut use

\[
 (O_0,I_0)=(O\cup B,\;B\cup D),
\]

and for the inner cut use

\[
 (O_1,I_1)=(V(G)-F,\;S\cup F).
\]

Since \(F\subseteq D\), \(O\) is anticomplete to \(F\), and
\(S=N_G(F)\), we have \(S\subseteq B\cup D\).  Hence

\[
 O_0\subseteq O_1,\qquad I_1\subseteq I_0.
\]

The nested minimum-cut linkage lemma therefore gives seven disjoint
\(B\)-\(S\) paths.  Fixing every vertex of \(B\cap S\) by a trivial path
is legitimate: apply Menger in \(G-(B\cap S)\), whose connectivity is at
least \(7-|B\cap S|\).  Minimal truncation confines every other path to

\[
 D-(F\cup B\cup S).
\]

Consequently:

* no path interior enters the owner shore \(O\);
* no path interior enters \(F\);
* no path contains a second vertex of either adhesion;
* distinct transported bags can meet neither along an adhesion nor in an
  annulus.

The five bags in (2.2) are therefore genuinely disjoint.  The owner
carriers connect the two paths in each pair block, and every adjacency
between the five bags is an old edge witnessing the complete five-block
quotient.  The claimed traces on \(S\) are exact.

The comparison note
`hadwiger_triangle_linkage_transport_descent.md` uses the same linkage.
Its initial family includes \((B,D)\) itself, whereas the audited note first
invokes Corollary 6.3 to obtain a proper descendant.  The former packaging
is slightly cleaner, but the two proofs are logically equivalent in the
triangle application.

## 2. Packet lift

Let \(Y_P,Y_Q\subseteq F\) be hypothetical disjoint inner carriers.  For
\(x\in P\cup Q\), put

\[
 T_x=
 \begin{cases}
   V(L_x)-\{x\},&L_x\text{ is nontrivial},\\
   \varnothing,&L_x\text{ is trivial}.
 \end{cases}
\]

Then the two lifted sets are

\[
 \widehat Y_P=Y_P\cup\bigcup_{p\in P}T_p,
 \qquad
 \widehat Y_Q=Y_Q\cup\bigcup_{q\in Q}T_q.
\]

For a nontrivial path, its inner endpoint lies in \(S-B\subseteq D\) and
is adjacent to the relevant inner carrier; its first vertex after the old
root is an old-root portal.  For a trivial path, the inner carrier itself
is adjacent to the old root.  Thus both lifted sets lie in \(D\), are
connected, and meet their two old portal classes.  Linkage disjointness and
avoidance of \(F\) make the two sets disjoint.  Hence an inner packet would
indeed give a forbidden packet in \(D\).

There is no hidden use of an equality of boundary graphs: only the
transported labels and the linkage tails are used.

## 3. Minimum-fragment atomicity

For every nonempty proper \(Y\subsetneq F\), all external neighbours of
\(Y\) lie in \((F-Y)\cup S\), so the set in (3.1) is exactly
\(N_G(Y)\).  Seven-connectivity gives size at least seven.  If it has size
seven, take a component \(K\) of \(G[Y]\).  Then

\[
 N_G(K)\subseteq N_G(Y).
\]

The old owner shore \(O\) survives outside \(N_G(K)\), so
seven-connectivity applies and forces equality.  Therefore \(K\) is a
component behind an exact seven-cut and \(|K|<|F|\), contradicting the
minimum choice.  The strict lower bound eight is valid even when \(Y\) is
disconnected.

The transported boundary is full because \(S=N_G(F)\), and it has exactly
seven distinct labels because the linkage induces a bijection.  Thus the
two-pair packet/web theorem applies.

### Small-order patch

To infer three-connectivity after excluding one- and two-cuts, add:

> Every one of the four pair-root labels has at least two portals, while
> Lemma 3.1 forbids a vertex from serving both labels of either pair.  Hence
> there are at least eight pair-root portal incidences and at most two per
> vertex, so \(|F|\ge4\).

This closes the standard \(|V(F)|>3\) convention explicitly.

## 4. Two Paths/web dependency

The use is the ordinary set-terminal reduction.  Add four artificial
terminals, one for each root of \(P'\cup Q'\), and join each terminal to
its whole portal set.  Two vertex-disjoint paths for the two prescribed
pairs are equivalent to two disjoint carriers, so packet-freeness is
exactly crosslessness.

The cited Two Paths theorem characterizes a crossless graph as a spanning
subgraph of a web (equivalently, take a same-vertex edge-maximal crossless
completion).  If an original shore vertex lies in a clique part supported
by a facial triangle \(T\), take all original vertices off \(T\) in that
part.  Their internal boundary and represented pair-root boundary together
use at most the three vertices of \(T\); the three \(R'\)-labels add at
most three more.  The set is proper because a triangle cannot contain all
four artificial terminals and fullness supplies a shore neighbour of the
fourth.  This contradicts relative boundary at least seven.  Hence every
original vertex lies in the planar rib.

Deleting the artificial terminals merges their incident faces with the
outer face, so all four full portal sets are cofacial.  This is precisely
the conclusion used later; no selected-portal order is assumed.

## 5. Crossed two-cut model

The atomic two-cut lemma gives two components \(K_1,K_2\) with
complementary one-root defects in (say) \(P'\), full contact to
\(Q'\cup R'\), and common internal boundary \(Z\).  Put

\[
 W_0=K_1\cup Z,\qquad W_1=K_2.
\]

Both are connected and disjoint, and an edge joins them.  Each sees:

* \(A_P\), through its retained root of \(P'\);
* \(A_Q,A_1,A_2,A_3\), through fullness to \(Q'\cup R'\).

The five transported bags already form \(K_5\), so these are exactly the
21 adjacencies of the displayed \(K_7\)-model.  No lobe is absorbed into a
bag that already uses a vertex of \(F\).

The more label-specific certificate (3.2) in
`hadwiger_triangle_linkage_transport_descent.md` is also correct.  Its
last three bags use, respectively, the old \(ab\)-edge and the transported
\(a\)- and \(b\)-contacts of the complementary lobe.  The generic
certificate in the audited note is preferable because it needs only the
complete five-block quotient.

## 6. Curvature, cofaciality, and rooted \(K_4\)

After the small-order patch, \(F\) is a simple three-connected plane graph.
Triangulating bounded faces gives

\[
 \sum_{u\in\operatorname{int}T}(6-d_T(u))+
 \sum_{u\in\partial T}(4-d_T(u))=6.
\]

An interior vertex has no \(P'\)- or \(Q'\)-contact and therefore has
\(F\)-degree at least five.  An outer vertex has degree at least three.
Thus every positive term is one, and atomicity forces its vertex to see all
three roots of \(R'\).  There are at least six such vertices.

If four common \(R'\)-neighbours are not cofacial, the planar
three-connected rooted-\(K_4\) criterion gives four disjoint mutually
adjacent bags rooted at them.  Each of those bags is adjacent to each of
\(A_1,A_2,A_3\), and the latter form a triangle, yielding \(K_7\).
Hence every four are cofacial.  To make the next sentence fully explicit,
fix three of the at least six vertices.  The face containing them and any
fourth vertex is unique, because two faces in a three-connected plane graph
cannot share three vertices.  Therefore all common neighbours lie on one
face.

If that face is not outer, it meets the outer face in at most two vertices.
Fan-triangulating it adds a diagonal at every one of its boundary vertices
except at most two.  At most two common neighbours can also lie on the outer
face.  Since every positive vertex is a common neighbour, the total positive
curvature is at most four, contradicting the identity.  The common face is
therefore the outer face.

Now every positive vertex \(z\) is outer with \(d_F(z)=3\).  Atomicity
requires at least five boundary contacts.  Since no vertex sees both roots
of either pair, five is also the maximum, giving exactly

\[
 N_S(z)=R'\cup\{p(z),q(z)\},
 \qquad p(z)\in P',\ q(z)\in Q'.
\]

## 7. The two-positive-vertex model

There are at least six positive vertices, so choose distinct \(z_0,z_1\).
Deleting an edge of their path in a spanning tree produces a connected
bipartition \(F=W_0\dot\cup W_1\), with \(z_i\in W_i\), and the deleted
tree edge is an edge between the two parts.

Each \(W_i\) sees all five transported bags through the exact contact row
of \(z_i\).  Thus

\[
 A_P\mid A_Q\mid A_1\mid A_2\mid A_3\mid W_0\mid W_1
\]

is a valid \(K_7\)-model.  All seven bags are connected and pairwise
disjoint; the first five lie outside \(F\), while the last two partition
\(F\).

## 8. Degree-seven endpoint and exact scope

Corollary 6.3 of the two-pair note supplies a proper exact descendant of a
nonsingleton nonowner.  Choosing one of minimum order and applying the
audited theorem yields \(F=\{z\}\).  Since

\[
 S=N_G(F)=N_G(z),\qquad |S|=7,
\]

we have \(d_G(z)=7\).  The seven linkage ends on \(S\), grouped as
\(2,2,1,1,1\), give five transported bags; with \(\{z\}\) they form only
a \(K_6\)-model.  The note correctly does **not** infer the missing seventh
bag from contact counts.

For a component \(K\) of \(D-z\), every exit lies in \(\{z\}\cup B\).
That set separates \(K\) from the nonempty owner shore, so
seven-connectivity gives \(|N_B(K)|\ge6\).  Again, this is only a defect-one
row and does not justify absorbing \(K\), because linkage strands can run
through it.

Accordingly the exact proved advance is:

> every nonsingleton exact-cut descendant in this oriented two-pair residue
> collapses to a genuine degree-seven singleton.

The remaining owner-carrier/one-defect splitter is still open.

