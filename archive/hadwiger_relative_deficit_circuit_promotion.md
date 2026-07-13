# Promoting a relative Hall deficit: an exact linkage circuit and a genuine portal adhesion

## 1. Counterexample setup

Let \(G\) be a graph, let \(v\in V(G)\), put

\[
 L=G-v,\qquad N=N_G(v),
\]

and let \(\mathcal B=(B_1,\ldots,B_m)\) be a \(K_m\)-model in
\(L\).  Write

\[
 Q=\bigcup_{j=1}^m B_j.
\]

Assume that every contacted bag contains exactly one vertex of \(N\).
Let \(I_0\) be the set of uncontacted bag indices and let

\[
 R=N-Q.
\]

Use the following directed version of the auxiliary graph.  Replace every
edge of \(L-Q\) by its two orientations and, for each \(i\in I_0\), add an
artificial sink \(\tau_i\), with an arc from every external portal of
\(B_i\) to \(\tau_i\).  Denote the resulting digraph by \(\vec A\).  Here
an external portal is a vertex of \(L-Q\) with a neighbour in \(B_i\).
The sinks have outdegree zero.  This directed formulation prevents a
terminal belonging to one bag from being used as an artificial bridge on
a path to another bag.  It encodes exactly the model-avoiding linkages in
\(L-Q\).

It is essential that the ambient graph in this construction is \(L=G-v\),
not \(G\).  Otherwise an augmenting path may use \(v\), after which \(v\)
cannot also be used as the extra singleton branch set.

For \(J\subseteq I_0\), call \(J\) **linkable** if \(\vec A\) contains
\(|J|\) pairwise vertex-disjoint paths from distinct vertices of \(R\) to
the distinct terminals \(\{\tau_j:j\in J\}\).

## 2. Exact circuit theorem

### Theorem 2.1 (minimal Hall deficit is an exact linkage circuit)

Suppose \(I_0\) is not linkable.  Then there are a nonempty
inclusion-minimal nonlinkable set \(I\subseteq I_0\) and a set

\[
 X\subseteq V(L-Q)
\]

with all of the following properties.

1. \(|X|=|I|-1\).
2. In \(\vec A-X\), no directed path joins a vertex of \(R-X\) to any
   \(\tau_i\), \(i\in I\).
3. Every proper subset of \(I\) is linkable.
4. For every \(i\in I\), there is a linkage \(\mathcal P_i\) from
   distinct roots in \(R\) to all terminals \(\tau_j\),
   \(j\in I-\{i\}\), such that every path of \(\mathcal P_i\) contains
   exactly one vertex of \(X\), and the paths collectively exhaust \(X\).

In particular, after deleting the artificial terminal and adding the last
edge into its bag, property 4 gives, for every omitted index \(i\), an
\(X\)-saturating family of disjoint model-avoiding paths to every bag in
\(I-\{i\}\).

#### Proof

Choose \(I\) inclusion-minimal among the nonlinkable subsets of \(I_0\).
For any \(i\in I\), minimality makes \(I-\{i\}\) linkable.  Consequently
the maximum number of disjoint \(R\)-to-\(T_I\) paths, where
\(T_I=\{\tau_i:i\in I\}\), is at least \(|I|-1\).  It is at most
\(|I|-1\), because \(I\) itself is not linkable.  Thus its value is
exactly \(|I|-1\).

Apply the directed vertex form of Menger's theorem in the subdigraph
containing \(L-Q\) and only the sinks in \(T_I\) (with the standard
vertex-capacity-one convention also on source and target vertices).
There is an \(R\)-\(T_I\) separator \(Z\) of order
\(|I|-1\).  We claim that \(Z\) contains no artificial terminal.  Put

\[
 W=Z\cap T_I,\qquad X=Z-T_I.
\]

The set \(I-W\) is nonempty, since \(|Z|<|I|\).  Moreover \(X\) separates
\(R\) from every terminal in \(T_I-W\): a directed path avoiding \(X\)
and ending at a terminal outside \(W\) cannot pass through a member of
\(W\), because all artificial terminals are sinks, and would therefore
avoid all of \(Z\).  But

\[
 |X|=|I|-1-|W|=|I-W|-1,
\]

so \(I-W\) is nonlinkable: if it had \(|I-W|=|X|+1\) disjoint
paths, every path would have to meet \(X\) (possibly at its source),
which is impossible for vertex-disjoint paths through a set of size
\(|X|\).  Thus \(I-W\) would be a proper nonlinkable subset of \(I\),
contrary to the choice of \(I\).  Hence \(W=\varnothing\),
\(Z=X\subseteq V(L-Q)\), and
properties 1--3 follow.

Fix \(i\in I\).  A linkage to \(I-\{i\}\) has \(|I|-1=|X|\) paths.
Since \(X\) separates \(R\) from every terminal in \(T_I\), each path
meets \(X\).  The paths are disjoint, so they use distinct vertices of
\(X\).  There are exactly \(|X|\) paths and \(|X|\) vertices; consequently
every path meets \(X\) exactly once and all of \(X\) is used.  This proves
property 4. \(\square\)

### Corollary 2.2 (two-sided factorisation)

Let \(U\) be the union of the components of

\[
 (L-Q)-X

\]

which contain a vertex of \(R-X\).  If \(|I|\ge2\), then:

* there is a linkage in \(L[U\cup X]\) from distinct roots to all of
  \(X\); and
* for every \(i\in I\), there is an \(X\)-to-\((I-\{i\})\) linkage in
  \(L-U\), ending at external portals of the indicated bags and otherwise
  avoiding \(Q\).

The root-to-\(X\) linkage may be fixed once and then concatenated with any
one of the far-side linkages.

#### Proof

Take the paths from Theorem 2.1(4).  Their prefixes through their unique
vertices of \(X\) lie in \(U\cup X\).  Their suffixes cannot return to
\(U\): such a return followed by the suffix would give an
\((R-X)\)-to-\(T_I\) path in \(\vec A-X\).  Thus the suffixes lie on the far
side.  Prefixes and suffixes have disjoint interiors, so a fixed prefix
linkage can be combined with any far-side linkage. \(\square\)

This is the precise exchange structure hidden by the inequality
\(|X|<|I|\): the deficit is a circuit, and deleting any one bag label
restores a perfect linkage through the same saturated interface \(X\).

### Corollary 2.3 (the far side clique-knits the circuit interface)

If \(|I|\ge2\), then for every \(i\in I\), the far side contains an \(X\)-rooted
\(K_{|X|}\)-model: its branch sets contain the vertices of \(X\) one each.
After adjoining the root-side prefixes and the vertex \(v\), the same
certificate gives a \(K_{|I|}\)-model in which one branch set contains
\(v\), and the other \(|I|-1\) branch sets are the bags
\(B_j\), \(j\in I-\{i\}\), augmented by the circuit paths.

#### Proof

Use the far-side suffixes in Corollary 2.2.  For each \(j\ne i\), adjoin
its suffix, its final edge, and its external portal to \(B_j\).  These
sets are disjoint and connected, contain the vertices of \(X\) one each,
and remain pairwise adjacent because the original \(B_j\)'s are clique
bags.  This is the rooted clique model.

Equivalently, use the full paths of Theorem 2.1(4).  Each augmented bag
then contains a distinct root in \(N(v)\), so the singleton \(\{v\}\) is
adjacent to every one of them. \(\square\)

Thus the circuit certificate is already a one-sided knitting theorem:
the far side realizes the singleton partition of \(X\) by mutually
adjacent connected blocks.  The missing colour-gluing input is on the
root side and on the additional portal vertices \(P\), not on the
deficient bags themselves.

### Corollary 2.4 (deficit circuits obey matroid exchange)

The linkable subsets of \(I_0\) are the independent sets of a gammoid.
Consequently the minimal Hall-deficit sets satisfy circuit elimination:
if \(I_1,I_2\) are distinct minimal deficits and
\(e\in I_1\cap I_2\), then some minimal deficit is contained in

\[
 (I_1\cup I_2)-\{e\}.
\]

More concretely, if \(J\) is a maximum linkable set, then every
\(e\in I_0-J\) has a unique fundamental circuit
\(C_e\subseteq J\cup\{e\}\), and for every
\(f\in C_e-\{e\}\), the set \(J-f+e\) is linkable.

#### Proof

Reverse all arcs of \(\vec A\).  A subset of the artificial terminals is
linkable precisely when its vertices can be linked by disjoint directed
paths to distinct vertices of the fixed set \(R\).  This is the defining
presentation of a strict gammoid.  The asserted circuit-elimination and
fundamental-circuit exchange statements are the standard matroid circuit
axioms. \(\square\)

Thus different relative deficits cannot be arranged independently.  They
form a single exchange system, and a maximum-contact routing can swap any
unlinked bag with a bag in its fundamental circuit without losing routing
rank.  This is a uniform invariant available for a future portal-surgery
argument.

## 3. Promotion to a genuine separation

For \(j\in[m]\), define the actual portal set

\[
 P_j=N_L(U)\cap B_j,
 \qquad
 P=\bigcup_{j=1}^m P_j.
\]

### Theorem 3.1 (relative-to-global promotion)

With \(I,X,U,P\) as above, assume additionally that
\(R-X\ne\varnothing\).  (This is automatic in the counterexample
application: \(|N|\ge m\) gives
\(|R|\ge |I_0|\ge |I|>|X|\).)  Then:

1. \(P_i=\varnothing\) for every \(i\in I\);
2. \(N_L(U)\subseteq X\cup P\);
3. \(S=\{v\}\cup X\cup P\) is a genuine vertex separator in \(G\),
   separating the nonempty set \(U\) from every bag \(B_i\), \(i\in I\).

Consequently, if \(G\) is \(k\)-connected, then

\[
 |P|\ge k-1-|X|=k-|I|.                 \tag{3.1}
\]

Moreover the portal surplus in accessible bags satisfies

\[
 \sum_{j\notin I} \max\{0,|P_j|-1\}
 \ge k-m.                              \tag{3.2}
\]

#### Proof

The set \(U\) is nonempty because \(R-X\ne\varnothing\).

If \(P_i\ne\varnothing\), an edge joins a vertex of \(U\) to \(B_i\).
That vertex of \(U\) is therefore itself an external
portal of \(B_i\), contradicting Theorem 2.1(2).  Thus property 1 holds.

By the definition of \(U\), every neighbour in \(L-Q\) of \(U\) which
does not lie in \(U\) belongs to \(X\).  Its neighbours in \(Q\) are
exactly the vertices in \(P\).  This proves property 2.  Passing from
\(L\) to \(G\) adds only the vertex \(v\), so

\[
 N_G(U)\subseteq \{v\}\cup X\cup P.
\]

The set on the right is disjoint from \(U\).  After its deletion, every
\(B_i\), \(i\in I\), remains nonempty because \(P_i=\varnothing\), and
there is no path from \(U\) to those bags.  Hence it is a genuine
separator.

If \(G\) is \(k\)-connected, this genuine separator has order at least
\(k\), giving (3.1).
At most \(m-|I|\) sets \(P_j\), \(j\notin I\), are nonempty, whence

\[
 \begin{aligned}
 \sum_{j\notin I}\max\{0,|P_j|-1\}
 &=|P|-|\{j\notin I:P_j\ne\varnothing\}|\\
 &\ge (k-|I|)-(m-|I|)=k-m.
 \end{aligned}
\]

This proves (3.2). \(\square\)

### Consequence 3.2 (the sharp \(HC_7\) output)

For a hypothetical \(7\)-contraction-critical counterexample, take
\(m=6\) and use \(\kappa(G)\ge7\).  Every relative Hall circuit therefore
has

\[
 \sum_{j\notin I}\max\{0,|P_j|-1\}\ge1.
\]

Thus some accessible branch bag contains at least two distinct attachment
vertices from the root side.  This conclusion is uniform over the size of
the circuit \(I\); it is not an artefact of a particular Moser labelling.

The extra vertex \(v\) in the separator is necessary.  Omitting it would
incorrectly improve the lower bound by one, because all vertices of
\(R\subseteq N(v)\) can use \(v\) as a bypass in \(G\).

### Corollary 3.3 (minor-critical state exchange on the promoted adhesion)

Suppose in addition that \(G\) is minor-minimal non-\(r\)-colourable, and
put

\[
 S=\{v\}\cup X\cup P.
\]

Let \(\mathcal E_r(U,S)\) be the set of labelled \(r\)-colourings of
\(S\) which extend to \(G[U\cup S]\).  For every edge
\(e\in E(G[U])\),

\[
 \mathcal E_r(U/e,S)-\mathcal E_r(U,S)\ne\varnothing.       \tag{3.3}
\]

The analogous assertion holds for deletion of an internal edge or
internal vertex, with the evident modified side.

#### Proof

Colour the proper minor \(G/e\) with \(r\) colours and restrict the
colouring to \(S\).  This boundary state extends to the contracted
root side and, unchanged, to \(G-U\).  If it also extended to the original
root side, the two extensions would glue across the genuine separator
\(S\) and give an \(r\)-colouring of \(G\), a contradiction.  Deletion is
identical. \(\square\)

Consequently a portal-preserving contraction inside \(U\) cannot be
boundary-state neutral.  Any splitter applied to the promoted adhesion
must either expose a smaller/tight separation or create an explicitly new
colour-extension state.  This is the precise point at which
minor-criticality strengthens the purely linkage-theoretic promotion.

## 4. Contact-maximal specialization

Suppose \(|N|\ge m\), the fixed \(K_m\)-model maximizes the number \(c\)
of contacted bags, and every contacted bag contains exactly one root.
If the model is not \(N\)-meeting, then \(R\ne\varnothing\), and for every
uncontacted bag \(B_i\) there is no
model-avoiding path in \(L\) from an unused root to an external portal of
\(B_i\); adjoining such a path to \(B_i\) would increase contact.
Therefore every singleton \(\{i\}\), \(i\in I_0\), is a Hall circuit with
\(X=\varnothing\).

Let \(U\) be the union of all components of \(L-Q\) containing unused
roots, and put \(P=N_L(U)\cap Q\).  The same argument works
simultaneously for all \(i\in I_0\):

\[
 P\cap B_i=\varnothing\qquad(i\in I_0).
\]

Thus the whole root-side region is separated in \(G\) from every
uncontacted bag by

\[
 \{v\}\cup P,
\]

where \(P\) lies in the \(c\) contacted bags.  If \(G\) is \(k\)-connected,
then

\[
 |P|\ge k-1,
 \qquad
 \sum_{j\notin I_0}\max\{0,|P\cap B_j|-1\}
 \ge k-1-c.                                      \tag{4.1}
\]

In the \(HC_7\) case, \(|P|\ge6\).  If
\(d=|I_0|=6-c\) bags remain uncontacted, then the total surplus portal
load in the contacted bags is at least

\[
 6-c=d.                                          \tag{4.2}
\]

So the number of surplus root-side attachment vertices is at least the
number of missing contacts, not merely one.  In particular, at least one
contacted bag is multiply hit.

There is a stronger conclusion which uses only \(P\ne\varnothing\), not
the surplus estimate.  Choose \(p\in P\cap B_j\).  The bag \(B_j\) is
contacted, since \(P\) avoids every uncontacted bag.  A component of \(U\)
contains both a neighbour of \(p\) and an unused root \(z\); choose a
\(z\)-to-\(p\) path whose internal vertices lie in \(U\), and adjoin the
path up to its last edge to \(B_j\).  This preserves the \(K_m\)-model
and produces a bag \(B'_j\) containing two distinct roots: its original
root and \(z\).

Thus:

> **Multiply-root promotion.**  If \(P\ne\varnothing\), every
> non-\(N\)-meeting contact-maximal model in the
> one-root-per-contacted-bag cell can be transformed, without reducing
> contact, into a clique model having a multiply rooted bag.

The exact obstruction after this promotion is finite-interface rather
than an amorphous failed linkage.  Let \(a,z\in N\cap B'_j\) be the two
roots, and choose any uncontacted bag \(B_i\).  If there is a partition

\[
 B'_j=Y_a\mathbin{\dot\cup}Y_z
\]

into nonempty connected adjacent sets, with \(a\in Y_a\),
\(z\in Y_z\), such that **each** of \(Y_a,Y_z\) is adjacent to every bag

\[
 B_\ell\qquad(\ell\notin\{i,j\}),                 \tag{4.3}
\]

then delete the uncontacted bag \(B_i\) and replace \(B'_j\) by
\(Y_a,Y_z\).  The result is again a \(K_m\)-model, now with \(c+1\)
contacted bags, contradicting contact maximality.

Consequently every rooted connected bipartition of \(B'_j\) fails the
two-sided portal requirement (4.3), for every choice of the dropped
uncontacted bag.  When \(m=6\), this is exactly a \(2\)-by-\(4\)
label-preserving portal-split lock: both rooted pieces would have to see
the same four retained clique bags.  A uniform proof may therefore target
this explicit split lock directly.

This is the cleanest promotion of the original relative separator: after
contact maximization the outside separator disappears, and all of the
obstruction is forced into actual, labelled branch-bag portals.

## 5. Star-deficient near-clique certificate

Let \(\rho\) be the maximum size of a linkable subset of \(I_0\), and put

\[
 d=|I_0|-\rho.
\]

Choose a maximum linkage and absorb its paths into the corresponding
bags.  Together with the originally contacted bags, exactly \(m-d\) bags
now meet \(N(v)\).  The \(m\) clique bags and the singleton \(\{v\}\)
therefore form a minor isomorphic to

\[
 K_{m+1}-K_{1,d},
\]

where all \(d\) missing edges are incident with \(v\).  In particular,
if \(d=1\), the graph contains a \(K_{m+1}^{-}\)-minor.

If the entire uncontacted set \(I_0\) is a Hall circuit, then
Theorem 2.1(4) gives, for every \(i\in I_0\), such a \(K_{m+1}^{-}\)-model
whose unique missing edge is the edge from \(v\) to the prescribed bag
\(B_i\).

This near-clique certificate uses the fact that the original branch bags
form a clique.  It is stronger than merely recording a failed linkage,
but it does not by itself turn \(K_{m+1}^{-}\) into \(K_{m+1}\); that last
step remains a label-preserving bag-splitting problem.

## 6. Exact remaining gap

The relative Hall obstruction is now promoted to two simultaneous,
audited objects:

1. an exact gammoid circuit with a common saturated interface and one
   exchange linkage for every omitted bag; and
2. a genuine adhesion \(\{v\}\cup X\cup P\), where all surplus over the
   ambient connectivity is forced to occur as multiple actual portals in
   accessible clique bags.

For \(HC_7\), portal multiplicity is automatic.  What is not proved here
is that one multiply hit bag can always be split while preserving its four
retained clique adjacencies after one deficient bag is dropped (more
generally, its \(m-2\) retained adjacencies).  For arbitrary \(t\), current lower bounds on
\(\kappa(G)\) can be much smaller than \(m=t-1\), so (3.2) need not force
any portal multiplicity.  A complete uniform proof still needs either a
portal-preserving split/exchange theorem using the circuit linkages, or a
colour-gluing theorem for the genuine adhesion above.
