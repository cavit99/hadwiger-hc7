# Clean root capture for the (2\times4) contact lock

## 1. Why ordinary rooted (K_{2,4}) is not yet the target

Let (D) be the multiply rooted branch bag, with distinct roots
(a,z\in D\cap N(v)), and let (B_1,\ldots,B_4) be the four retained
clique bags.  Contract each (B_i) to a terminal (t_i), delete the
dropped bag, and retain (D) and any vertices that will be used for
rerouting.  Write

\[
        X=\{t_1,t_2,t_3,t_4\}.
\]

The standard (X)-rooted (K_{2,4}) problem prescribes only that the
four large-side branch sets contain the four terminals.  It does **not**
prescribe the two small-side branch sets, and it does not require them
to be adjacent.  The contact problem needs both extra properties:

* the two small-side branch sets must contain (a,z), one each; and
* they must be adjacent.

With the terminal (K_4) restored, a standard rooted (K_{2,4}) gives
only a (K_6^-)-model in general.  Thus the exact object is a doubly
rooted (K_{2,4}+e), where (e) joins the two vertices on the side of
order two.

The planar theorem of Demasi--Mohar is nevertheless useful for finding
the underlying four-terminal packing.  Its exact scope is planar
four-terminal graphs: after low-connectivity reductions, a
three-connected graph either contains the rooted (K_{2,4}), or its
reduced graph has one of the five structures 3F, OWO, DF, HF, DCJ.
It does not supply the two bullets above.

## 2. A clean capture lemma

The root-placement part is substantially simpler than a prescribed
two-paths problem once the two small-side carriers are regarded as
unlabelled.

### Theorem 2.1 (clean rooted-(K_{2,4}) capture)

Let (H) contain an (X)-rooted (K_{2,4})-model

\[
        (T_1,T_2,T_3,T_4;C_1,C_2),                 \tag{2.1}
\]

where (t_i\in T_i), and suppose (a,z) are outside all six branch
sets.  Put

\[
        R=H-\bigcup_{i=1}^4 T_i .                  \tag{2.2}
\]

Contract (C_1,C_2) in (R) to distinct vertices (c_1,c_2), replace
every remaining undirected edge by its two orientations, and delete all
arcs leaving (c_1,c_2).  Thus (c_1,c_2) are genuine directed sinks.
Give every vertex (including (a,z,c_1,c_2)) capacity one.  Call the
resulting auxiliary digraph \(\widehat R\).  Suppose one component of the
original undirected graph \(R\) contains \(a,z\) and meets both
\(C_1,C_2\).  If no set of at most one vertex separates
\(\{a,z\}\) from \(\{c_1,c_2\}\) in the unit-capacity source--sink
sense, then (2.1) can be changed into a doubly rooted
(K_{2,4}+e)-model.

Equivalently, if the desired root capture fails for this clean model,
then either no component of the original undirected \(R\) contains all
four objects, or there is an order-at-most-one directed source--sink
separator in \(\widehat R\).  The separating vertex is allowed to be one of the
sources \(a,z\) or one of the contracted carrier vertices.  A source
separator is a distinct endpoint-gate outcome.  The sink alternative is a
**target-reachability failure**: after lifting, every admissible path to
the other free carrier meets the first carrier.  It does not assert that
one vertex of the first carrier is a cutvertex of the undirected graph.

#### Proof

Apply the vertex-capacitated source--sink form of Menger's theorem.  A
linkage of order two necessarily uses both source vertices and both
sink vertices, because all four have capacity one.  The sink convention
prevents one target from being used internally on a path to the other.
Thus there are two vertex-disjoint paths from the two distinct sources
(a,z) to the two distinct targets (C_1,C_2), in some order.  Restore
the carriers and absorb one path into each target carrier.  Call the
resulting disjoint connected sets (A,Z); they contain (a,z),
respectively, and each remains adjacent to every (T_i).

Both sets lie in the same (undirected) component of (R), by the separate
component hypothesis on the original remainder.
Choose a shortest
(A)-to-(Z) path in that component.  Its internal vertices avoid
(A\cup Z).  Absorb all its internal vertices into (A) (or split the
path at any edge).  The two enlarged sets remain disjoint and connected
and are now adjacent.  They and (T_1,\ldots,T_4) form the required
doubly rooted (K_{2,4}+e)-model. \(\square\)

### Corollary 2.2 (the exact residual is an order-one directed obstruction)

If (H-\{a,z\}) has a clean (X)-rooted (K_{2,4})-model, then a
surviving contact lock forces, for every such model, either a component
obstruction in the original \(R\), an internal ordinary order-one gate,
a source gate at \(a\) or \(z\), or a sink target-reachability failure in
the complement of its four terminal branch sets, after its two free
carriers have been contracted to directed sinks.

This is stronger and more precise than saying that root capture is an
arbitrary Two Paths web.  The two small carriers are interchangeable,
so the pairing is not prescribed; directed set-to-set Menger reduces
the failure to order at most one.  What remains difficult is lifting
that quotient gate through the four terminal branch bags to a genuine
separator of the ambient graph.

## 3. Lifting back to the contact model

In the (K_6)-model, the four original retained bags are pairwise
adjacent.  Therefore, after lifting contractions, the four branch sets
(T_i) in Theorem 2.1 remain pairwise adjacent.  The two captured
carriers are adjacent to one another and to every (T_i).  Hence they
and the four (T_i)'s form a (K_6)-model in (G-v), with two
different bags meeting (N(v)) at (a,z).

Every originally contacted retained bag still contains its old root,
because its original branch bag is contained in its lifted (T_i).
Thus the lifted model has one more contacted bag than the original
contact-maximal model, even in the two-uncontacted case.  This is the
required contradiction.  It is not necessary at this stage that the
lifted model together with (v) already be a (K_7)-model.

Consequently the (2\times4) problem has now split into two exact
subproblems:

1. find a rooted (K_{2,4})-packing avoiding (a,z); or place the
   four-terminal graph in one of the rooted-minor obstruction classes;
2. for every clean packing, eliminate the component/cutvertex gate in
   (2.2) using the ambient seven-connectivity and the minor-transition
   colouring witnesses.

The second item, rather than an unrestricted two-linkage theorem, is the
place where the five Kempe detours and the locked-Steiner-tree charges
must be used.

## 4. Sharpness: the promoted icosahedral architecture lands exactly
##    in the cutvertex alternative

This section aligns the known graph (K_2\vee I) with the *exact*
Hall-circuit promotion, rather than using it only as a generic
connectivity counterexample.

Label the icosahedron by

\[
V(I)=\{t,b,u_0,\ldots,u_4,w_0,\ldots,w_4\}
\]

with indices modulo five and edges

\[
tu_i,\quad bw_i,\quad u_iu_{i+1},\quad w_iw_{i+1},
\quad u_iw_i,\quad u_iw_{i-1}.
\]

Let (G=K_2\vee I), with universal vertices (p,q), and take (v=t).
In (G-v) use the six bags

\[
\begin{aligned}
B_0&=\{b\},& B_1&=\{u_0,w_0\},&B_2&=\{u_1,w_1\},\\
B_3&=\{u_2,w_2,w_3,w_4\},&B_4&=\{p\},&B_5&=\{q\}.
\end{aligned}                                      \tag{4.1}
\]

They form a (K_6)-model.  The five contacted bags contain exactly the
five roots (u_0,u_1,u_2,p,q), one each; (B_0) is uncontacted.  The
unused-root component is

\[
        U=G[\{u_3,u_4\}].                           \tag{4.2}
\]

It has no portal to (B_0), so the singleton Hall circuit is genuine.
Its actual portal vertices are

\[
 P\cap B_1=\{u_0\},\quad P\cap B_2=\varnothing,
 \quad P\cap B_3=\{u_2,w_2,w_3,w_4\},
 \quad P\cap B_4=\{p\},\quad P\cap B_5=\{q\}.     \tag{4.3}
\]

Thus (|P|=7), strictly above the six forced by connectivity, and the
portal surplus is real.  Contact maximality follows from
(eta(K_2\vee I)=6): a sixth contacted bag would give a (K_7)-minor.

Absorb all of (U) into (B_3).  The promoted bag is

\[
 D=\{u_2,u_3,u_4,w_2,w_3,w_4\},                    \tag{4.4}
\]

with roots (a=u_2,z=u_3).  After dropping (B_0), its four portal
classes to (B_1,B_2,B_4,B_5) are

\[
 \{u_4,w_4\},\qquad \{u_2,w_2\},\qquad D,\qquad D. \tag{4.5}
\]

There is no literal connected rooted bipartition splitting (4.5).  In
fact (\{u_3,w_2\}) separates (u_2) from (\{u_4,w_4\}) in (D):
an (u_2)-side which reaches the first portal class without using the
(z)-root (u_3) must use (w_2), leaving no second-side vertex in the
second portal class.

Nevertheless the four-terminal packing itself exists cleanly.  With
artificial terminals (t_1,\ldots,t_4) for the classes in (4.5), take

\[
 T_1=\{t_1\},\quad
 T_2=\{t_2,w_2,w_3\},\quad
 T_3=\{t_3\},\quad T_4=\{t_4\},
 \quad C_1=\{u_4\},\quad C_2=\{w_4\}.              \tag{4.6}
\]

These sets form a rooted (K_{2,4}); (C_1C_2\) is already an edge,
and the model avoids (a,z).  But after deleting the four terminal
branches, the relevant remainder is the path

\[
        u_2-u_3-u_4-w_4.                            \tag{4.7}
\]

The ordinary vertex (u_3) blocks two disjoint root-to-carrier paths.  In
the directed-sink formulation, (u_4) can instead appear as the sink
separator: every admissible route to the other carrier (w_4) first enters
the carrier (\{u_4\}).  The latter is a target-reachability failure, not
an assertion that an internal vertex of that carrier is an undirected
cutvertex.  Thus the architecture realizes both exact order-one outcomes
of Theorem 2.1.

The graph is seven-connected, has minimum degree seven, and is
(K_7)-minor-free, but it is six-colourable.  It therefore shows that
seven-connectivity, the exact Hall circuit, a strict portal surplus, a
clean rooted (K_{2,4}), and the (2\times4) lock still do not lift the
one-vertex gate.  The remaining lemma must use the *negative* part of
minor criticality: the boundary state created after an internal
contraction cannot extend to the uncontracted side.  Merely observing
that the relevant contractions are six-colourable is not enough.

## 5. The sharpened target

There is one further consequence when the quotient gate lies inside the
original root-accessible Hall region.

### Lemma 5.1 (gate multiplicity or a tight seven-cut)

Let (G) be seven-connected.  In the setting of Theorem 2.1, suppose a
failed clean capture gives an **ordinary** gate vertex

\[
 s\in R-(C_1\cup C_2),
\]

not one of the two contracted sink vertices.  Let (W) be a nonempty
union of root-side components of (R-s), and assume that both free
carriers (C_1,C_2) lie in (R-(W\cup\{s\})).  (Thus this lemma does
not cover the alternative in which an entire free carrier is the
order-one sink gate.)  Suppose, as in the contact-maximal Hall region,
that

1. (W) contains a neighbour of (v);
2. (W) has no neighbour in an uncontacted branch bag; and
3. every neighbour of (W) other than (v,s) lies in one of the four
   retained terminal carriers (T_1,\ldots,T_4).

Put (P_i=N_G(W)\cap T_i).  Then

\[
             \sum_{i=1}^4 |P_i|\ge5.               \tag{5.1}
\]

If equality holds, then

\[
             \{v,s\}\cup P_1\cup\cdots\cup P_4    \tag{5.2}
\]

is a tight separator of order seven.  If (5.1) is strict, the gate has
at least six actual terminal-carrier attachments.  In either case some
(T_i) contains at least two distinct attachment vertices from (W).

#### Proof

The hypotheses give

\[
 N_G(W)\subseteq \{v,s\}\cup P_1\cup\cdots\cup P_4.
\]

The set (W) is nonempty and lies on the root side, while both free
carriers are nonempty and lie outside it.  Hence the displayed set is a
genuine separator.
Seven-connectivity therefore gives

\[
 7\le |N_G(W)|\le2+\sum_i|P_i|,
\]

which is (5.1).  At equality every inclusion above is equality and the
displayed separator has order seven.  Finally five (or more) distinct
vertices distributed among four terminal carriers force a repeated
carrier. \(\square\)

This recovers, at the **root-capture gate itself**, the portal
multiplicity formerly obtained only at the coarse Hall adhesion.  It
also gives the exact recursion point.  A size-minimal repeated carrier
is a locked Steiner tree: every removable (W)-portal must be uniquely
responsible for one of its three other terminal-carrier adjacencies or
one of its two free-carrier adjacencies.  If a Kempe detour repairs that
unique charge, the gate opens.  If the attachment bound in Lemma 5.1 is
an equality, its tight seven-cut is the surface on which boundary-state
gluing must be attempted.  Failure of all repairs does **not** by itself
force equality; the strict-surplus locked core remains a separate
outcome.

The icosahedral architecture has strict inequality in (5.1) and a
locked repeated carrier, so the last sentence genuinely requires the
minor-transition exclusion state; portal counting alone cannot prove
it.

The next valid local theorem is now:

> **Clean-packing gate elimination.**  In a seven-contraction-critical
> (K_7)-minor-free graph, let a contact-maximal (K_6)-model produce
> the promoted two-root bag.  For some dropped uncontacted bag, either
> the four-terminal quotient has no clean rooted (K_{2,4}), in which
> case its rooted-minor obstruction structure produces a colour-gluable
> adhesion, or every clean rooted (K_{2,4}) has a component, source,
> internal-gate, or sink-reachability obstruction as in Theorem 2.1,
> and one internal edge at that obstruction has a Kempe detour which
> performs a terminal-branch exchange.

This target is strictly narrower than the former portal-split lemma.  It
asks the Kempe--Steiner machinery to break a one-vertex gate after the
four-terminal packing is already present, rather than to construct all
six branch sets simultaneously.
