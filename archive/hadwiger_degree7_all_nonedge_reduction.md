# Every neighbourhood nonedge is an accessible repeated pair

This note strengthens the degree-seven reduction.  It does not close the
remaining nonseparating rooted-minor problem.

Let \(G\) be a hypothetical proper-minor-minimal counterexample to
\(\mathrm{HC}_7\), let \(d_G(v)=7\), put \(H=G-v\), and let
\(N=N_G(v)\).  Write
\[
 Q=\overline{G[N]}.
\]
Dirac's inequality gives \(\alpha(G[N])=2\), so \(Q\) is a nonempty
triangle-free graph on seven vertices.

## 1. Prescribing the repeated pair

### Lemma 1.1

For every edge \(xy\in E(Q)\), there is a proper six-colouring of \(H\)
whose repeated colour on \(N\) occurs exactly at \(x,y\), while the five
vertices of \(N-\{x,y\}\) receive the other five colours bijectively.

### Proof

Contract the connected star \(G[\{v,x,y\}]\) to a vertex \(q\), obtaining
a proper minor \(J\).  The graph \(J\) is six-colourable.  It is not
five-colourable: a five-colouring could be expanded by giving \(x,y\) the
colour of \(q\) and giving \(v\) a fresh sixth colour, contradicting
\(\chi(G)=7\).  Hence \(\chi(J)=6\).

In any six-colouring of \(J\), the five vertices
\(U=N-\{x,y\}\) avoid the colour of \(q\), because each is adjacent to
\(q\) through its old edge to \(v\).  Every other colour must occur on
\(U\): if one were absent, give \(x,y\) the colour of \(q\), give \(v\)
the absent colour, and expand to a six-colouring of \(G\).  Since
\(|U|=5\), its colours are bijective.  Restoring \(x,y\) with the colour
of \(q\) gives the asserted colouring of \(H\).  \(\square\)

Thus the accessible repeated-pair graph is not merely a matching or a
subset of \(Q\): it is all of \(Q\).

## 2. Choosing a pseudoforest five-root obstruction

For a prescribed repeated pair \(xy\), the missing-edge graph on the five
unique roots is
\[
 F=Q-\{x,y\}.                                             \tag{1}
\]
The only triangle-free graph on five vertices which is not a pseudoforest
is \(K_{2,3}\).  Indeed, two cycles in one component require at least six
edges, and equality in Mantel's bound on five vertices gives \(K_{2,3}\).

### Lemma 2.1

If \(Q-\{x,y\}\cong K_{2,3}\) for every edge \(xy\in E(Q)\), then
\(Q\cong K_{3,4}\).

### Proof

First, \(Q\) is connected.  Otherwise, for an edge \(xy\) in one
component, the five-vertex deletion graph is connected, so all other
vertices lie in one component; deleting the ends of an edge in that other
component then leaves a disconnected graph, a contradiction.

Let \(m=|E(Q)|\).  For every edge \(xy\),
\[
 6=|E(Q-\{x,y\})|=m-d(x)-d(y)+1,
\]
so
\[
 d(x)+d(y)=m-5                                           \tag{2}
\]
is constant on all edges.  In a connected graph satisfying (2), degrees
alternate along paths.  Hence the graph is either regular, or bipartite
and semiregular.

The regular case is impossible: if the common degree is \(r\), then
\(m=7r/2\), while (2) gives \(2r=m-5\), whence \(r=10/3\).

In the bipartite case let the side orders be \(p\le q\), with
\(p+q=7\), and the corresponding degrees be \(r,s\).  Then
\(pr=qs=m\) and \(r+s=m-5\).  Checking \(p=1,2,3\), the only positive
integral solution within \(r\le q,s\le p\) is
\[
 (p,q,r,s,m)=(3,4,4,3,12).
\]
Thus every possible cross-edge is present and \(Q=K_{3,4}\). \(\square\)

### Corollary 2.2

Exactly one of the following holds.

1. \(G[N]\ne K_3\cup K_4\), and one can choose a six-colouring for which
   the five-root missing-edge graph \(F\) is a pseudoforest.  The rooted
   \(K_5\) certificate can then be obtained from the structured
   Kriesell--Mohr pseudoforest theorem.
2. \(G[N]=K_3\cup K_4\).  Every repeated pair is a cross-pair and every
   corresponding five-root graph is \(K_{2,3}\).

In the second case, \(G-N[v]\) has exactly one component: there is at
least one component and at most two, while two components together with
the \(K_4\subseteq G[N]\) already give an \(N\)-meeting \(K_6\)-model.
Explicitly, if the components are \(C_1,C_2\), choose distinct
\(a_1,a_2\) in the \(K_3\)-part.  The bags
\(C_1\cup\{a_1\},C_2\cup\{a_2\}\), together with the four singleton
bags on the \(K_4\)-part, form that model.

## 3. Refined exact residual

The degree-seven problem has therefore split into two sharply different
cells:

- the **pseudoforest cell**, where one must make the cycle-with-trees
  property-\((*)\) certificate nonseparating; and
- the **single-bridge \(K_3\cup K_4\) cell**, where the sole exterior
  component must simultaneously realize the hard \(K_{2,3}\) routing
  pattern and leave a sixth branch set.

This strictly improves the earlier statement that an arbitrary repeated
pair merely existed.  It still does not prove that either certificate can
be chosen disjointly from a connector for the repeated pair.
