# Near-\(K_7\) with exactly two complex bags

## Status

This note gives two rigorous outputs for the first nontrivial near-clique
cell.

1. A sharp connectivity-only counterexample: \(K_2\vee I\) has a spanning
   \(K_7^-\)-model with **exactly two** non-singleton bags.  Thus even this
   restricted cell cannot be closed by seven-connectivity and portal counts.
2. A portal-distribution subcase in which the desired split-versus-two-apex
   dichotomy follows from the Niu--Zhang three-clique theorem.

The general two-complex-bag cell remains open and must use
contraction-critical state exchange (or an equivalent chromatic input).

## 1. Exact two-complex-bag counterexample

Let \(I\) be the icosahedron with vertices

\[
 t,b,u_0,\ldots,u_4,w_0,\ldots,w_4
\]

(subscripts modulo five) and edges

\[
 tu_i,\quad bw_i,\quad u_iu_{i+1},\quad w_iw_{i+1},
 \quad u_iw_i,\quad u_iw_{i-1}.
\]

Let \(G=K_2\vee I\), and call the two universal vertices \(p,q\).

### Proposition 1.1

The graph \(G\) is seven-connected, has minimum degree seven, is
\(K_7\)-minor-free and two-apex, and has the following spanning
\(K_7^-\)-model with exactly two non-singleton bags:

\[
\begin{aligned}
 X_1&=\{t\},&X_2&=\{u_0\},&X_3&=\{u_1\},\\
 X_4&=\{u_2\},&X_5&=\{p\},\\
 D&=\{b,u_3,w_2,w_0\},
 &E&=\{u_4,w_1,w_3,w_4,q\}.
\end{aligned}
\]

The only nonadjacent pair of bags is \(X_2X_4\).

#### Proof

The icosahedron is five-connected, five-regular, planar, and has a
\(K_4\)-minor.  Consequently

\[
 \kappa(G)=2+5=7,\qquad \delta(G)=7,\qquad
 \eta(G)=2+\eta(I)=6.
\]

The equality for the Hadwiger number follows because adjoining one universal
vertex raises the Hadwiger number by exactly one.  Deleting \(p,q\) leaves
the planar graph \(I\), so \(G\) is two-apex.

The bag \(D\) is connected through the edges
\(bw_0,bw_2,w_2u_3\).  The bag \(E\) is connected because it contains the
universal vertex \(q\).  The five singleton vertices induce \(K_5\) minus
the edge \(u_0u_2\): the vertex \(t\) meets \(u_0,u_1,u_2\), the upper
cycle supplies \(u_0u_1,u_1u_2\), and \(p\) is universal.

Both \(D\) and \(E\) meet every singleton bag.  For \(D\), use respectively
\(tu_3,u_0w_0,u_1w_0,u_2w_2\), and universality of \(p\).  For \(E\), use
\(tu_4,u_0w_4,u_1w_1,u_2w_1\), and again universality of \(p\).
Finally \(D\) and \(E\) are adjacent, for example through \(bw_3\).
Thus all bag pairs except \(\{u_0\},\{u_2\}\) are adjacent. \(\square\)

Since \(\eta(G)=6\), no branch-set split or exchange on this model can
produce \(K_7\).  Notice that \(D\) even has a cutvertex.  The failure of
the one-complex-bag cut argument is visible exactly: components behind that
cut can acquire seven neighbours by concentrating several of them inside
\(E\), without meeting all five singleton labels.

Also \(G\) is six-colourable: four-colour the planar graph \(I\) and give
\(p,q\) two fresh colours.  Hence it is not seven-contraction-critical.
This makes the missing hypothesis exact, not cosmetic.

### Proposition 1.2 (the same obstruction for \(K_7^{\vee}\))

The same graph has a spanning \(K_7^{\vee}\)-model with exactly two
non-singleton bags:

\[
 \{t\},\quad\{b\},\quad\{u_0\},\quad\{p\},\quad\{q\},
 \quad D'=\{u_1,w_0\},
 \quad E'=\{u_2,u_3,u_4,w_1,w_2,w_3,w_4\}.
\]

The only nonadjacent pairs are

\[
 \{b\}\{t\}\quad\hbox{and}\quad \{b\}\{u_0\}.
\]

#### Proof

Among the five singleton bags, \(b\) is nonadjacent to \(t,u_0\), while
all other pairs are edges: \(tu_0\) is an icosahedral edge and \(p,q\)
are universal.  The edge \(u_1w_0\) connects \(D'\), and the upper and
lower paths together with their cross-edges connect \(E'\).  The bag
\(D'\) meets \(t,b,u_0\) through \(u_1,w_0\), and \(E'\) meets them
through \(u_2,w_1,w_4\), respectively.  Universality supplies the
contacts to \(p,q\), and \(u_1u_2\) joins \(D'\) to \(E'\).  Thus the
two displayed pairs are exactly the deficient pairs. \(\square\)

Propositions 1.1 and 1.2 show that the required chromatic input is needed
for both normalized near-clique types, already with exactly two complex
bags.

## 2. A three-clique portal distribution that forces split or two-apex

We use the following established theorem of Niu and Zhang.

> **Three-clique apex theorem (the \(k=5\) case).**  Let \(G\) be a
> seven-connected non-two-apex graph.  If \(G\) contains three 5-cliques
> \(L_1,L_2,L_3\) with
> \(|L_i\cap L_j|\le3\) for every \(i\ne j\), then \(G\) contains a
> \(K_7\)-minor.

This is Theorem 1.10 of J. Niu and C.-Q. Zhang, *Cliques, minors and apex
graphs*, Discrete Math. 309 (2009), 4095--4107.

### Theorem 2.1 (distributed triangle portals)

Let \(G\) be seven-connected and suppose it has a spanning
\(K_7^-\)-model

\[
 (\{a\},\{c\},\{q_1\},\{q_2\},\{q_3\},D,E),
\]

where \(ac\) is the unique non-required pair.  Suppose there are vertices

\[
 d_a,d_0\in D,\qquad e_c,e_0\in E
\]

such that

1. \(d_a\ne d_0\) and \(e_c\ne e_0\);
2. \(d_a\) is adjacent to \(a,q_1,q_2,q_3\);
3. \(e_c\) is adjacent to \(c,q_1,q_2,q_3\);
4. both \(d_0,e_0\) are adjacent to each of \(q_1,q_2,q_3\); and
5. \(d_0e_0\in E(G)\).

Then \(G\) contains a \(K_7\)-minor or \(G\) is two-apex.

#### Proof

The following are 5-cliques:

\[
\begin{aligned}
 L_1&=\{d_a,a,q_1,q_2,q_3\},\\
 L_2&=\{e_c,c,q_1,q_2,q_3\},\\
 L_3&=\{d_0,e_0,q_1,q_2,q_3\}.
\end{aligned}
\]

The singleton vertices \(q_1,q_2,q_3\) form a triangle because they are
three unaffected singleton bags of the near-clique.  All remaining edges
inside the displayed sets are precisely the portal edges assumed above.
The distinctness assumptions give

\[
 L_i\cap L_j=\{q_1,q_2,q_3\}
 \quad(i\ne j).
\]

If \(G\) is not two-apex, the three-clique apex theorem supplies a
\(K_7\)-minor.  This proves the dichotomy. \(\square\)

### Corollary 2.2 (application to an HC7 counterexample)

The portal pattern in Theorem 2.1 cannot occur in a hypothetical
minor-minimal counterexample to \(HC_7\).  Such a graph is not two-apex,
because deleting two apex vertices, four-colouring the planar remainder,
and using two fresh colours would give a six-colouring.

### Theorem 2.3 (common-triangle portal core)

Keep the five singleton bags

\[
 \{a\},\{c\},\{q_1\},\{q_2\},\{q_3\}
\]

of a spanning two-complex-bag \(K_7^-\)-model, and put
\(T=\{q_1,q_2,q_3\}\).  Let

\[
 Z=\bigcap_{i=1}^3N_G(q_i)-(T\cup\{a,c\}).
\]

Suppose \(G[Z]\) contains an edge \(xy\), and each of

\[
 N_G(a)\cap (Z-\{x,y\}),
 \qquad N_G(c)\cap (Z-\{x,y\})
\]

has order at least two.  Then \(G\) contains a \(K_7\)-minor or is
two-apex.

#### Proof

Choose distinct vertices

\[
 z_a\in N(a)\cap(Z-\{x,y\}),
 \qquad z_c\in N(c)\cap(Z-\{x,y\}).
\]

This is possible because each of the two candidate sets has at least two
vertices.  Then

\[
 T\cup\{a,z_a\},\qquad
 T\cup\{c,z_c\},\qquad
 T\cup\{x,y\}
\]

are three 5-cliques.  Their pairwise intersections are exactly \(T\).
Apply the Niu--Zhang theorem as in Theorem 2.1. \(\square\)

### Corollary 2.4 (complete common triangle)

Suppose the common singleton triangle \(T\) is complete to
\(D\cup E\).  Then \(G\) contains a \(K_7\)-minor or is two-apex.

#### Proof

There is an edge \(xy\) between \(D\) and \(E\), and its ends belong to
\(Z\).  The vertices \(a,c\) each have three neighbours in the singleton
boundary, namely the vertices of \(T\).  Minimum degree seven gives at
least four neighbours in \(D\cup E\).  After deleting \(x,y\), at least
two candidates remain for each of \(z_a,z_c\), so Theorem 2.3 applies.
\(\square\)

In a hypothetical \(HC_7\) counterexample, Corollary 2.4 gives an atomic
exclusion: in every exactly-two-complex-bag \(K_7^-\)-model with singleton
deficient pair, at least one common-triangle edge to the complex union must
be absent.  Thus the residual is a genuine portal-distribution defect, not
merely a failure of a bag split.

### Lemma 2.5 (triangle-core matching bound)

Let \(G\) be a seven-connected, non-two-apex, \(K_7\)-minor-free graph,
and let \(T\) be any triangle.  Write

\[
 C(T)=\bigcap_{t\in T}N_G(t)-T
\]

for its common-neighbour set.  Then

\[
 \nu\bigl(G[C(T)]\bigr)\le2.
\]

Consequently all edges in the common-neighbour core \(G[C(T)]\) have
a vertex cover of order at most four.

#### Proof

Three independent edges \(e_1,e_2,e_3\) in the common-neighbour core
would make \(T\cup e_i\), \(1\le i\le3\), three 5-cliques with pairwise
intersection exactly \(T\).  The Niu--Zhang theorem would give a
\(K_7\)-minor.  Thus a maximum matching has at most two edges.  Its set of
ends is a vertex cover, proving the second assertion. \(\square\)

This is a model-independent bounded-portal-core theorem: every triangle in
a hypothetical \(HC_7\) counterexample has all edges among its common
neighbours concentrated at four vertices.

### Theorem 2.6 (dominating-triangle split-versus-two-apex theorem)

Let \(G\) be a seven-connected graph on at least nine vertices and let
\(T\) be a triangle complete to \(V(G)-T\).  Then \(G\) contains a
\(K_7\)-minor or \(G\) is two-apex.

#### Proof

Assume that \(G\) is not two-apex and has no \(K_7\)-minor, and put
\(H=G-T\).

If \(H\) has a matching \(e_1,e_2,e_3\) of order three, then the three
sets

\[
 T\cup e_1,\qquad T\cup e_2,\qquad T\cup e_3
\]

are 5-cliques whose pairwise intersections are exactly \(T\).  The
Niu--Zhang theorem gives a \(K_7\)-minor, a contradiction.  Hence a
maximum matching \(M\) of \(H\) has order at most two.

Let \(X\) be the set of ends of \(M\).  By maximality, \(X\) is a vertex
cover of \(H\), so \(H-X\) is independent.  Since \(|H|\ge6\) and
\(|X|\le4\), it contains distinct vertices \(u,v\).  Deleting
\(T\cup X\) separates \(u\) from \(v\).  Seven-connectivity forces
\(|T\cup X|\ge7\), and therefore \(|M|=2\).  Write

\[
 M=\{x_1x_2,x_3x_4\}.
\]

Every neighbour of \(u\) or \(v\) lies in \(T\cup X\), a set of order
seven.  Minimum degree seven therefore makes each of \(u,v\) complete to
\(T\cup X\).  Now

\[
 \{u,x_1\},\quad \{v,x_2\},\quad \{x_3\},\quad \{x_4\}
\]

are four pairwise adjacent connected branch sets: the last pair is
adjacent by the matching edge \(x_3x_4\), and all other required edges are
supplied by \(u\) or \(v\).  Thus they form a \(K_4\)-model in \(H\).
The three singleton vertices of the dominating triangle \(T\) upgrade it
to a \(K_7\)-model, again a contradiction. \(\square\)

This theorem is independent of the Moser labels and of any selected
near-clique model.  Corollary 2.4 is its immediate application when the
common singleton triangle is complete to both complex bags (the two
deficient singleton vertices already see that triangle).

### Theorem 2.7 (near-dominating \(K_4\) lemma)

Let \(G\) have minimum degree at least seven.  Suppose \(T\) is a
4-clique, \(a\notin T\), and

\[
 U=V(G)-(T\cup\{a\})
\]

is nonempty and connected.  If \(T\) is complete to \(U\), then \(G\)
contains a \(K_7\)-minor.

#### Proof

If \(G[U]\) contains a cycle, that cycle has a \(K_3\)-minor.  Since every
vertex of \(T\) is adjacent to every vertex of \(U\), the four singleton
bags of \(T\) together with the three cycle branch sets form a
\(K_7\)-model.

Otherwise \(G[U]\) is a tree.  A leaf of this tree has at most one
neighbour in \(U\), four in \(T\), and one at \(a\), so its degree in
\(G\) is at most six, contrary to the minimum-degree hypothesis.
\(\square\)

### Corollary 2.8 (complete common \(K_4\) in the \(K_7^{\vee}\) cell)

Consider a spanning exactly-two-complex-bag \(K_7^{\vee}\)-model with
singleton bags

\[
 \{a\},\{b\},\{c\},\{q_1\},\{q_2\}
\]

and deficient pairs \(ab,ac\).  If the 4-clique
\(T=\{b,c,q_1,q_2\}\) is complete to both complex bags \(D,E\), then
\(G\) contains a \(K_7\)-minor.

Indeed, \(U=D\cup E\) is connected because the two model bags are
adjacent, and Theorem 2.7 applies.  Thus the \(K_7^{\vee}\) residual, like
the \(K_7^-\) residual, must contain a genuine missing portal edge from
its common singleton clique into a complex bag.

### Theorem 2.9 (root-avoiding triangle-core concentration)

Let (G) be seven-connected, (K_7)-minor-free, and non-two-apex.  Let
(T) be a triangle, and let (a,c) be nonadjacent vertices outside (T)
which are complete to (T).  Put

\[
R=C(T)-\{a,c\}.
\]

Then (G[R]) has matching number at most two.  Moreover, if
(M=\{x_1x_2,x_3x_4\}) is a matching of order two in (G[R]), then

\[
N(a)\cap(R-V(M))=N(c)\cap(R-V(M))=\varnothing.  \tag{2.2}
\]

Consequently, in a two-complex-bag (K_7^-)-model, if the vertices complete
to the common singleton triangle contain two independent edges avoiding the
deficient singleton pair, every triangle-complete portal from either
deficient singleton is concentrated on the four ends of those edges.  At
least one deficient singleton then has a complex-bag neighbour which misses
the common triangle.

#### Proof

Three independent edges in (G[R]) would give three 5-cliques (T\cup e)
with pairwise intersection exactly (T).  The Niu--Zhang theorem would give
a (K_7)-minor or make (G) two-apex.  Hence the matching number is at most
two.

Suppose (z\in N(a)\cap(R-V(M))).  The three sets

\[
T\cup\{x_1,x_2\},\qquad
T\cup\{x_3,x_4\},\qquad
T\cup\{a,z\}
\]

are 5-cliques whose pairwise intersections are exactly (T).  This again
contradicts the Niu--Zhang theorem.  The argument for (c) is identical,
proving (2.2).

In the near-(K_7) model, each of (a,c) already has the three neighbours
of (T), is nonadjacent to the other, and has degree at least seven.  Thus
each has at least four neighbours in the complex union.  If both had four
triangle-complete neighbours, (2.2) would make both adjacent to all four
ends of (M).  Taking one matching edge for the third clique and distinct
ends of the other edge for the (a)- and (c)-cliques gives the three
5-cliques of Theorem 2.3, again a contradiction.  Hence at least one of
(a,c) has at most three triangle-complete complex neighbours and therefore
has a complex neighbour missing a vertex of (T). \(\square\)

### Theorem 2.10 (rooted-triangle frame dichotomy)

Let \(G\) be seven-connected and \(K_7\)-minor-free, let
\(T=\{q_1,q_2,q_3\}\) be a triangle, and let \(a,c\notin T\) be
distinct vertices complete to \(T\).  Suppose that there are two further
distinct vertices

\[
 d,e\in C(T)-\{a,c\}.
\]

Put \(J=G-T\).  Then \(J\) is planar and has a face \(F\) whose boundary
contains every vertex of \(C(T)\).  In particular, if \(G\) is not
two-apex, then each \(q_i\) has a neighbour in
\(V(J)-V(F)\), and every such off-face neighbour misses at least one of
the other two vertices of \(T\).

#### Proof

The graph \(J\) is four-connected: deleting fewer than four vertices from
\(J\), together with the three vertices of \(T\), deletes fewer than seven
vertices from \(G\).

Apply the rooted-\(K_4\) theorem of Fabila-Monroy and Wood to
\(J\) with roots \(a,c,d,e\).  If \(J\) has a rooted \(K_4\)-model at
these vertices, its four bags, together with the three singleton bags
\(\{q_1\},\{q_2\},\{q_3\}\), form a \(K_7\)-model: every rooted bag
contains a vertex complete to \(T\).  This is excluded.  The alternative
in the rooted-\(K_4\) theorem says that \(J\) is planar and that
\(a,c,d,e\) lie on one face, say \(F\).

The embedding of the four-connected planar graph \(J\) is unique up to
reflection.  Let \(z\in C(T)-\{a,c,d,e\}\).  Apply the same theorem to
the roots \(a,c,d,z\).  Again the rooted-minor outcome gives a
\(K_7\)-model, so these four vertices lie on one face \(F_z\) in the
same plane embedding.  If \(F_z\ne F\), the two distinct facial
boundaries share the three vertices \(a,c,d\), whereas two distinct
faces of a three-connected plane graph meet in at most one vertex or one
edge.  Thus \(F_z=F\).  This proves that all of \(C(T)\) lies on
\(F\).

Finally suppose that all neighbours of some \(q_i\) in \(J\) lie on
\(F\).  Place \(q_i\) in the face \(F\) and draw its incident edges
inside that face.  This gives a plane drawing of \(J+q_i\), so deleting
the other two vertices of \(T\) makes \(G\) planar.  Thus \(G\) is
two-apex.  In the non-two-apex case every \(q_i\) consequently has an
off-face neighbour.  Such a vertex is not in \(C(T)\), and hence misses
at least one of the other two triangle vertices. \(\square\)

Theorem 2.10 needs only two triangle-complete complex vertices; it is
therefore substantially stronger as a structural reduction than the
matching hypothesis in Theorem 2.9.  It identifies the exact planar-web
residue rather than asserting an unjustified bag split.

### Corollary 2.11 (curvature exports six degree-seven vertices)

In the setting of Theorem 2.10, assume additionally that
\(\delta(G)\ge7\).  With \(F\) chosen as the outer face of \(J\), every
triangulation \(J^+\) of the bounded faces has at least six interior
vertices \(x\) satisfying

\[
 d_{J^+}(x)=d_J(x)=5,\qquad
 |N_G(x)\cap T|=2,\qquad d_G(x)=7.                 \tag{2.3}
\]

#### Proof

Every boundary vertex has \(J^+\)-degree at least four because \(J\) is
four-connected.  An interior vertex is not in \(C(T)\), by Theorem 2.10,
and therefore has at most two neighbours in \(T\).  Minimum degree seven
gives

\[
 d_{J^+}(x)\ge d_J(x)\ge7-|N_T(x)|\ge5
 \qquad(x\in\operatorname{int}J^+).               \tag{2.4}
\]

The triangulated-disk identity is

\[
 \sum_{x\in\operatorname{int}J^+}(6-d_{J^+}(x))
 +\sum_{x\in V(F)}(4-d_{J^+}(x))=6.               \tag{2.5}
\]

Boundary terms are nonpositive, and an interior term is positive only
when the corresponding degree is five, in which case it equals one.
Thus at least six interior vertices have \(J^+\)-degree five.  Equality
throughout (2.4) at each such vertex gives
\(d_J(x)=5\), \(|N_T(x)|=2\), and \(d_G(x)=7\), proving (2.3).
\(\square\)

The curvature conclusion is useful for arbitrary minimum-degree-seven
graphs.  In the chromatic setting it can be replaced by a complete closure.

### Corollary 2.12 (global triangle-common-neighbour cap)

Let \(G\) be seven-connected, seven-chromatic and \(K_7\)-minor-free.
For every triangle \(T\),

\[
                         |C(T)|\le3.               \tag{2.6}
\]

In particular, if two named vertices \(a,c\) are already complete to
\(T\), at most one further vertex is complete to \(T\).  Hence in a
two-complex-bag \(K_7^-\)-model, at most one vertex of the complex union
is complete to the common singleton triangle.

#### Proof

If four common neighbours \(a,c,d,e\) existed, Theorem 2.10 would make
\(J=G-T\) planar and put every common neighbour of \(T\) on one face.
The cofacial palette-recycling theorem in
`hadwiger_planar_triangle_palette_recycling.md` then six-colours \(G\):
four-colour an auxiliary planar graph obtained by placing a vertex in that
face, recycle the auxiliary vertex's colour on one member of \(T\), and
split its independent colour class between two fresh colours according to
which of the other two triangle vertices each member misses.  This
contradicts \(\chi(G)=7\). \(\square\)

Thus the entire high common-portal branch is closed.  The surviving
two-complex-bag cell is genuinely distributed: the three triangle labels
are carried at different internal vertices, apart from at most one common
portal.  No degree-seven Moser classification is needed for this closure.

### Corollary 2.13 (degree amplification in the distributed core)

Under the hypotheses of Corollary 2.12, put \(J=G-T\).  Every vertex
outside \(C(T)\) has degree at least five in \(J\); in particular, at
most three vertices of \(J\) can have degree four.

#### Proof

Every other vertex misses at least one member of \(T\), so it has at most
two neighbours in \(T\).  Seven-connectivity gives minimum degree at
least seven in \(G\), and hence

\[
                         d_J(x)\ge7-2=5.
\]

\(\square\)

This degree amplification removes the smallest planar vertex-splitting
counterarchitectures: any degree-four core vertex would itself be a second
additional common neighbour of \(T\), returning to the closed branch of
Corollary 2.12.

## 3. Minimal two-bag transfer and defect amplification

The next lemma isolates what seven-connectivity does provide when a complex
bag has a cutvertex.

### Lemma 3.1 (charged cut components)

Fix five singleton bags \(S\) in a spanning \(K_7^-\)- or
\(K_7^{\vee}\)-model whose two remaining, unaffected bags are \(D,E\).
Among all such spanning models of the same near-clique type
with these singleton bags fixed, choose one minimizing

\[
 \min\{|D|,|E|\},
\]

and label the smaller bag \(D\).  If \(x\) is a cutvertex of \(G[D]\),
then every component \(P\) of \(G[D-x]\) is the unique \(D\)-side carrier
of at least one singleton label: there is an \(s_P\in S\) such that

\[
 N_G(s_P)\cap D\subseteq P.
\]

The labels \(s_P\) belonging to distinct components are distinct.
Consequently \(G[D-x]\) has at most five components.

#### Proof

First, every component \(P\) of \(G[D-x]\) has a neighbour in \(E\).
Otherwise

\[
 N_G(P)\subseteq \{x\}\cup S,
\]

a set of order six, while another component of \(G[D-x]\) lies beyond
that set.  This contradicts seven-connectivity.

Suppose that \(P\) carries no singleton label uniquely.  Put

\[
 D'=D-P,\qquad E'=E\cup P.
\]

The set \(D'\) is connected: it is \(x\) together with all other
components of \(G[D-x]\).  The set \(E'\) is connected by the first
paragraph.  The old edge from \(P\) to \(x\) makes \(D'\) adjacent to
\(E'\).  By the supposition, \(D'\) retains a neighbour at every singleton
bag, while \(E'\) retains all its old adjacencies.  Hence replacing
\((D,E)\) by \((D',E')\) gives another spanning model of the same type.
But

\[
 \min\{|D'|,|E'|\}\le |D'|<|D|
 =\min\{|D|,|E|\},
\]

contrary to the choice of the model.  Thus the claimed label \(s_P\)
exists.

One singleton label cannot charge two distinct components: its set of
neighbours in \(D\) is nonempty and cannot be contained in two disjoint
sets.  The final assertion follows because \(|S|=5\). \(\square\)

### Lemma 3.2 (defect amplification into the opposite bag)

In the setting of Lemma 3.1, let \(r\) be the number of components of
\(G[D-x]\).  Then every such component \(P\) has at least \(r\) distinct
neighbours in \(E\).

More generally, if \(m(P)\) singleton labels in \(S\) have no neighbour
in \(P\), then

\[
 |N_G(P)\cap E|\ge m(P)+1.
\]

#### Proof

Since

\[
 N_G(P)\subseteq \{x\}\cup
 \bigl(S\cap N_G(P)\bigr)\cup
 \bigl(E\cap N_G(P)\bigr),
\]

seven-connectivity gives

\[
 7\le |N_G(P)|
 \le 1+(5-m(P))+|N_G(P)\cap E|.
\]

This proves the general inequality.  The \(r-1\) charge labels belonging
to the other components have no neighbour in \(P\), so
\(m(P)\ge r-1\), giving the first assertion. \(\square\)

### Lemma 3.3 (two-bag peel certificate)

Consider a spanning \(K_7^-\)-model

\[
 (\{a\},\{c\},\{q_1\},\{q_2\},\{q_3\},D,E),
\]

where \(ac\) is the deficient pair.  Suppose there are partitions

\[
 D=P\mathbin{\dot\cup}R,
 \qquad E=Z\mathbin{\dot\cup}W
\]

into nonempty connected sets such that

1. \(P\) is adjacent to \(R\), to \(a\), and to \(c\);
2. \(R\) is adjacent to \(Z\);
3. \(Z\) is adjacent to \(W\);
4. \(R\cup Z\) is adjacent to each of
   \(c,q_1,q_2,q_3\);
5. \(W\) is adjacent to each of
   \(c,q_1,q_2,q_3\); and
6. \(W\) is adjacent to \(P\) or to \(a\).

Then \(G\) contains a \(K_7\)-minor.

#### Proof

Use the seven bags

\[
 \{a\}\cup P,\quad \{c\},\quad
 \{q_1\},\{q_2\},\{q_3\},\quad R\cup Z,\quad W.
\]

The first bag is connected and meets \(c\) through \(P\), repairing the
only deficient singleton pair.  The edge \(PR\) joins it to
\(R\cup Z\), and condition 6 joins it to \(W\).  Conditions 4 and 5
supply all contacts from the last two bags to the four remaining
singletons, while \(ZW\) joins the last two bags.  All singleton pairs
other than \(ac\) were already edges of the near-clique. \(\square\)

The piece \(Z\) need not itself be a complete portal carrier.  It only
has to replace the labels lost when \(P\) is peeled from \(D\); \(R\)
and \(Z\) may share the remaining responsibilities.  This is the exact
label-preserving two-complex-bag surgery hidden by an informal instruction
to "split both bags".

### Corollary 3.4 (charge forced on every common deficient peel)

Use the minimal model of Lemma 3.1 and let \(P\) be a component of
\(D-x\), with \(R=D-P\).  Suppose \(P\) has neighbours at both \(a\)
and \(c\).  If \(G\) has no \(K_7\)-minor, then either

* \(R\) misses at least one of \(q_1,q_2,q_3\); or
* \(P\) is the unique \(D\)-side carrier of both \(a\) and \(c\).

#### Proof

Every component of \(D-x\), including \(P\) and one contained in
\(R\), has a neighbour in \(E\) by Lemma 3.1.  Hence \(R\) and \(E\)
are adjacent after the peel.  If \(R\) retains
\(c,q_1,q_2,q_3\), the one-bag split certificate (Lemma 3.1 of
`hadwiger_near_k7_split_round.md`) absorbs \(P\) into \(a\) and gives
\(K_7\).  Therefore \(R\) misses one of those four labels.  Applying the
symmetric certificate, absorbing \(P\) into \(c\), says that \(R\)
also misses one of \(a,q_1,q_2,q_3\).  If it misses no \(q_i\), it must
miss both \(a\) and \(c\), exactly the second outcome. \(\square\)

Thus a cut-side that can repair the deficient pair is not merely charged
by an arbitrary singleton: it either monopolizes a neutral triangle label,
which is precisely the input for the compensating peel \(Z\) in Lemma 3.3,
or it monopolizes both deficient roots.  The unresolved web cell is the
case in which every attempted compensating peel in \(E\) is simultaneously
locked.

Thus a minimal cut bag has a precise exchange obstruction: every cut side
is locked by a different singleton label, and the opposite complex bag
receives an \(r\)-fold portal set from every side.  For \(r\ge2\), this is
already the distributed-contact input expected by the rooted
\(K_{2,4}\)/Two-Paths web step.  The remaining, unproved step is to turn
those amplified portal sets into a label-preserving split or a two-apex
web; Proposition 1.1 shows that contraction-criticality is indispensable
there.

## 4. What remains in the two-complex-bag cell

Theorems 2.1 and 2.3 show that the useful invariant is not merely the number of
contacts but their **coincidence into triangle-complete portal vertices**.
A surviving non-two-apex model must fail at least one of the following:

* one complex bag has two distinct vertices complete to the common
  singleton triangle, one carrying a deficient endpoint;
* the other bag has the symmetric pair; or
* the two neutral triangle-complete portals are adjacent.

The counterexample in Proposition 1.1 demonstrates that this failure can
be organized by a planar two-apex core.  What is still missing is a
contraction-critical exchange lemma saying that, when the contacts are
distributed instead of coincident, an internal deletion/contraction either
creates the four vertices of Theorem 2.1 or exposes the two-shore rooted
\(K_{2,4}\)/web adhesion.  Connectivity alone cannot supply that lemma.
