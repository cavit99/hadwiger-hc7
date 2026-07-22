# Two independent boundary triples force a nonedge on the remaining pair

**Status:** written proof; [separately audited **GREEN**](hc7_degree8_two_independent_triples_audit.md).
This theorem does not prove `HC_7`.

## 1. Setup

Let `G` be a finite simple graph such that

\[
 \chi(G)=7,
 \qquad
 \chi(M)\le 6\text{ for every proper minor }M\text{ of }G.       \tag{1.1}
\]

Let `u` have degree eight, put `X=N_G(u)`, and suppose that
`G-N_G[u]` has exactly two nonempty components `E,F`, with

\[
                         N_G(E)=N_G(F)=X.                       \tag{1.2}
\]

Suppose that

\[
                 X=I\mathbin{\dot\cup}T
                       \mathbin{\dot\cup}\{p,q\},              \tag{1.3}
\]

where `I` and `T` are independent triples.

## 2. Simultaneous contractions and opposite responses

For \(P\in\{E,F\}\), let \(\mathcal R_P\) be the set of equality types of
`p,q` induced by proper six-colourings of `G[P union X]` in which `I` and
`T` are two exact boundary colour classes.  Thus

\[
                       \mathcal R_P\subseteq\{=,\ne\}.           \tag{2.1}
\]

### Theorem 2.1

Under the setup of Section 1, both response sets are nonempty,

\[
             \varnothing\ne\mathcal R_E,\mathcal R_F,           \tag{2.2}
\]

the pair `p,q` is a nonedge, and the response sets are opposite
singletons:

\[
 \{\mathcal R_E,\mathcal R_F\}=\bigl\{\{=\},\{\ne\}\bigr\}.
                                                                    \tag{2.3}
\]

Moreover, in every colouring contributing type \(\ne\) on its shore, `p,q`
lie in one component induced by their two colours.  A shortest joining
path has open interior wholly in that open shore.

### Proof

Fix \(P\in\{E,F\}\) and let `P'` be the other component.  The two sets

\[
                    A=\{u\}\cup I,
             \qquad B_{P'}=P'\cup T                            \tag{2.4}
\]

are disjoint and connected.  The first is connected through `u`; the
second is connected because `P'` is connected and has a neighbour at every
vertex of `T`.  Contract a spanning tree of each set, to vertices `a` and
`b_{P'}`, respectively.  The resulting graph is a proper
minor, so (1.1) gives it a proper six-colouring.

Keep the colours of the surviving vertices in `P\cup\{p,q\}`, give every
vertex of `I` the colour of `a`, and give every vertex of `T` the colour of
`b_{P'}`.  This is a proper six-colouring of `G[P\cup X]`.  Indeed,
`I` and `T` are independent, and every edge incident with either set was
represented by an edge incident with the corresponding contraction
vertex.

The contraction vertices `a,b_{P'}` are adjacent through the edges from
`u` to `T`.  Each of `p,q` is adjacent to `a` through its edge to `u`, and
to `b_{P'}` because `P'` has a neighbour at each of `p,q`.  Consequently
`I,T` are distinct exact boundary colour classes, while `p,q` avoid both
of their colours.  The construction therefore contributes one type to
\(\mathcal R_P\), proving (2.2).

If the two response sets had a common type, choose one colouring of each
closed shore with that type.  Their boundary partitions would be identical:
they would be

\[
 I\mid T\mid\{p,q\}
 \quad\hbox{or}\quad
 I\mid T\mid\{p\}\mid\{q\}.                                  \tag{2.5}
\]

After a permutation of colour names, the two colourings agree on `X` and
glue to a proper six-colouring of `G-u`.  At most four colours occur on
`X`, so assign an absent colour to `u`.  This six-colours `G`, contrary to
(1.1).  Hence

\[
                         \mathcal R_E\cap\mathcal R_F=\varnothing.
                                                                    \tag{2.6}
\]

If `pq` were an edge, both nonempty response sets would be the singleton
\(\{\ne\}\), contrary to (2.6).  Thus `pq` is a nonedge.  The two nonempty,
disjoint subsets of the two-element set in (2.1) must now be the two
opposite singletons, proving (2.3).

Finally, let `P` be the shore of type \(\ne\), take any colouring counted by
\(\mathcal R_P\), and let `alpha,beta` be the distinct colours of `p,q`.  If
`p,q` lay in different `alpha`--`beta` components, interchange the two
colours on the component containing `p`.  This preserves the exact blocks
`I,T` and changes the type to `=`, contrary to (2.3).  Hence `p,q` lie in
one such component.  No other boundary vertex has colour `alpha` or
`beta`, so a shortest joining path has no internal vertex in `X`; its open
interior lies in `P`. \(\square\)

## 3. Consequence for the seven-demand degree-eight residue

### Corollary 3.1

Retain the setup of Section 1 and fix an independent triple `I\subseteq X`.
Put `R=X-I`.  Suppose

\[
                |E(G[R])|=3,
          \qquad \alpha(G[R])\le3.                              \tag{3.1}
\]

Then

\[
                              G[R]\cong P_3\mathbin{\dot\cup}K_2. \tag{3.2}
\]

### Proof

A graph on five vertices with three edges and independence number at most
three is isomorphic to one of

\[
 K_3\mathbin{\dot\cup}2K_1,
 \qquad P_4\mathbin{\dot\cup}K_1,
 \qquad P_3\mathbin{\dot\cup}K_2.                              \tag{3.3}
\]

In the first graph, take `T` to be the two isolated vertices together
with one triangle vertex.  It is an independent triple, while the two
vertices of `R-T` are adjacent.  This contradicts Theorem 2.1.

In the second graph, take `T` to be the isolated vertex together with the
two ends of the four-vertex path.  Again `T` is independent, while the two
vertices of `R-T` are adjacent.  Theorem 2.1 gives the same contradiction.
Only the third graph in (3.3) remains. \(\square\)

In the five-reserve notation, (3.1) is precisely the degree-eight case
with seven reserve nonedges.  Thus the simultaneous-contraction argument
eliminates the `P_4`-plus-isolated-vertex case without invoking a
seven-demand extension of Kriesell--Mohr's theorem, and also eliminates
the triangle-plus-two-isolated-vertices case.  It does not settle the
remaining `P_3\mathbin{\dot\cup}K_2` boundary graph.

## Exact trust boundary

The proof uses the full proper-minor six-colourability assumption twice,
once for each choice of contracted exterior component.  It also uses both
literal full components and the independence of both triples.  It does not
claim that an arbitrary seven-edge five-root demand graph has
Kriesell--Mohr property `(*)`, and it constructs no rooted `K_5` model in
the surviving `P_3\mathbin{\dot\cup}K_2` case.
