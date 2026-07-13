# The \(K_{3,3}\) Kempe-routing problem

## 1. Exact formulation

Let \(K=K_{3,3}\), with bipartition

\[
L=\{1,2,3\},\qquad R=\{4,5,6\}.
\]

Let \(G\) have a proper colouring
\(\mathcal A=\{A_1,\ldots,A_6\}\), and choose roots
\(t_i\in A_i\). Assume that, for every \(i\in L,j\in R\), the
roots \(t_i,t_j\) lie in the same component of \(G[A_i\cup A_j]\).
The target is to prove that \(G\) has six pairwise disjoint connected
sets \(B_i\ni t_i\) such that \(B_i\) and \(B_j\) are adjacent whenever
\(i\in L,j\in R\). This is exactly the assertion that \(K_{3,3}\) has
Kriesell--Mohr property (*).

The work below proves a nontrivial uniform cell of this assertion and gives
an exact description of what remains.

## 2. Minimal path form

Suppose that a counterexample is chosen with
\(|V(G)|+|E(G)|\) minimum. For each \(i\in L,j\in R\), write
\(P_{ij}\) for the nontrivial component of \(G[A_i\cup A_j]\).
The standard Kriesell--Mohr reductions give:

1. \(P_{ij}\) is an induced \(t_i\)-\(t_j\) path, and all other
   vertices of \(G[A_i\cup A_j]\) are isolated in that two-colour
   graph.
2. \(G=\bigcup_{i\in L,j\in R}P_{ij}\).
3. Every vertex outside the transversal has degree at least four.

For completeness, here is the reduction proving item 3. If a non-root
vertex \(x\in A_i\) had degree two, then it lies on just one path, say
\(P_{ij}\), and its two neighbours \(y,z\) both lie in \(A_j\). Contract
the connected path \(y-x-z\) to one vertex \(w\), give \(w\) colour \(j\),
and replace the old colour-\(j\) root by \(w\) if that root was one of
\(y,z\). The path \(P_{ij}\) survives with \(y-x-z\) replaced by \(w\).
Every other required path either avoids \(y,z\), contains one of them, or
contains both; in the last two cases replacing the occurrences by \(w\)
and deleting any resulting closed subwalk leaves a path between the same
two (possibly updated) roots. Properness is preserved because every
remaining neighbour of \(y\) or \(z\) has colour different from \(j\),
while \(x\) had no other neighbours. Thus the contracted graph is a
strictly smaller witness. A rooted certificate in it lifts by replacing
\(w\), if used, by the connected set \(\{y,x,z\}\). This contradicts
minimality.

Because a non-root vertex \(x\in A_i\) is internal on each \(P_{ij}\)
that contains it, its degree in the minimal path union is

\[
d_G(x)=2\bigl|\{j:P_{ij}\ni x\}\bigr|.
\]

Consequently every non-root vertex has degree four or six. Equivalently,
it lies on exactly two or on all three of the paths belonging to its colour.

The nine paths form an **essential immersion** of \(K_{3,3}\): paths
belonging to distinct edges are edge-disjoint, and paths belonging to
nonincident edges are vertex-disjoint. The unresolved issue is precisely
whether every such *properly endpoint-coloured* essential immersion rounds
to a rooted minor.

## 3. Triple-supported root-shift theorem

Call a non-root vertex of \(A_i\) **triple-supported** if it lies on all
three paths \(P_{ij}\), \(j\) in the opposite part. Thus, in minimal
path form, triple-supported is equivalent to degree six.

### Theorem 3.1 (triple-supported shift)

Assume there is an automorphism \(\phi\) of \(K_{3,3}\) interchanging
its two bipartition classes and, for every \(i\), a triple-supported vertex
\(s_{\phi(i)}\in A_{\phi(i)}\) adjacent to \(t_i\). Then \(G\) has a
rooted \(K_{3,3}\)-certificate.

#### Proof

Delete all six old roots and put \(G'=G-T\), where
\(T=\{t_1,\ldots,t_6\}\). Use
\(T'=\{s_1,\ldots,s_6\}\) as the new transversal.

For every edge \(ij\in E(K_{3,3})\), both \(s_i\) and \(s_j\) lie on
the path \(P_{ij}\). Since they are not old roots, they lie on the
connected interior \(P_{ij}-\{t_i,t_j\}\). Hence \(i,j\) are adjacent
in the routing graph of \((G',\mathcal A|_{G'},T')\). The graph \(G'\)
is strictly smaller than \(G\), so minimality gives a rooted
\(K_{3,3}\)-certificate \((D_i)_{i=1}^6\) in \(G'\), with
\(s_i\in D_i\).

For each old label \(i\), define

\[
B_i=D_{\phi(i)}\cup\{t_i\}.
\]

The edge \(t_i s_{\phi(i)}\) makes \(B_i\) connected. The sets remain
pairwise disjoint because the old roots were deleted before the \(D_i\)
were constructed and \(\phi\) is a permutation. Finally, if
\(ij\in E(K_{3,3})\), then
\(\phi(i)\phi(j)\in E(K_{3,3})\), so \(D_{\phi(i)}\) and
\(D_{\phi(j)}\), and hence \(B_i,B_j\), are adjacent. Thus
\((B_i)\) is the required rooted certificate. \(\square\)

### Corollary 3.2 (the degree-six cell)

If every non-root vertex in a minimal path-form witness has degree six,
then the witness is not a counterexample.

#### Proof

Every \(P_{ij}\) then spans \(A_i\cup A_j\). Since it is an alternating
path with one end in each class, \(|A_i|=|A_j|\) for every edge \(ij\).
All six class sizes are therefore equal. If they equal one, the roots
already induce \(K_{3,3}\).

Otherwise choose arbitrary bijections
\(f:L\to R\) and \(g:R\to L\), and define the side-interchanging
automorphism \(\phi\) by \(\phi|_L=f\), \(\phi|_R=g\). For each
\(i\), let \(s_{\phi(i)}\) be the neighbour of \(t_i\) on
\(P_{i,\phi(i)}\). Every such vertex is a non-root and hence is
triple-supported. Theorem 3.1 applies. \(\square\)

### Corollary 3.3 (exact matching obstruction)

For an oriented cross-pair \(i\to j\), call the cell good if the neighbour
of \(t_i\) on \(P_{ij}\) is triple-supported. In a minimal counterexample,
at least one of the following two \(3\times3\) bipartite good-cell graphs
has no perfect matching:

* old roots in \(L\) to new colours in \(R\);
* old roots in \(R\) to new colours in \(L\).

Indeed, perfect matchings in both matrices combine to a side-interchanging
automorphism satisfying Theorem 3.1. Thus every surviving obstruction has
a Hall-deficient family of degree-four first portals. This is a finite
capacity state, not an arbitrary path system.

## 4. Exact finite checks completed

The program **trianglefree_six_property_search.py** exhaustively checks the
case in which every colour class has size two. For \(K_{3,3}\), each
required two-colour graph has only the minimal direct-edge or length-three
root-path possibilities. All 512 reduced local-path patterns have a rooted
certificate.

The independent program **k33_essential_immersion_search.cpp** generates
unions of nine alternating root paths on 14--18 vertices and checks the
rooted minor exactly by exhaustive connected-branch-set search. A run of
100,000 instances found no counterexample. These computations are
falsification evidence only; they are not used in Theorem 3.1.

There is also a complete exact check of the smallest pure degree-four
portal core. In that core every colour has precisely one non-root vertex
of each of its three two-element supports. Every required path therefore
has two internal vertices of each endpoint colour, and the only choices are
their two orders. There are \(2^{18}=262144\) labelled order states.
Root-preserving automorphisms of \(K_{3,3}\) reduce them to 3692 orbits.
The program **k33_pair_support_exhaustive.py** constructs every orbit and
encodes a rooted model by owner and strictly descending depth variables:

* each root has its prescribed owner and depth zero;
* every used non-root has a same-owner neighbour of smaller depth, which
  is exactly a connectivity certificate;
* every one of the nine target edges is witnessed by an ambient edge with
  the two required owners.

All 3692 instances are satisfiable, with no solver timeouts. Thus the
entire atomic all-degree-four order cell is eliminated by an independently
rerunnable exhaustive certificate search. What remains unbounded is the
multiplicity of portals with the same two-element support and mixtures with
degree-six portals.

## 5. Exact remaining gap

It remains to eliminate the Hall-deficient degree-four portal state from
Corollary 3.3. A degree-four portal in colour \(A_i\) lies on exactly two
of the three \(i\)-incident Kempe paths. Therefore the residue can be
encoded by support sets of size two, together with their orders on the nine
alternating paths.

Contact-existence alone is insufficient: several columns can be dominated
by the same colour, and their corresponding tails can interlace in that
colour class. The missing statement is an ordered portal-exchange lemma:
either these interlacings can be uncrossed into six rooted bags, or a
simultaneous root shift creates the two perfect matchings required by
Theorem 3.1. Proving that exchange closes \(K_{3,3}\); no stronger
connectivity or whole-two-colour connectedness may be assumed.
