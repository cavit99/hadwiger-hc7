# A simultaneous-star obstruction for adjacent degree-seven vertices

## 0. Label-free theorem

### Theorem 0.1 (adjacent degree-seven obstruction)

Let \(G\) be a graph which is not six-colourable but every proper minor
of \(G\) is six-colourable.  Let \(u,v\) be adjacent vertices of degree
seven.  There do not exist four distinct common neighbours

\[
        x_1,x_2,x_3,x_4\in N(u)\cap N(v)
\]

such that

\[
        x_1x_3,x_2x_4\notin E(G).                 \tag{0.1}
\]

Equivalently, the complement of the graph induced by any four common
neighbours of \(u,v\) has matching number at most one.

#### Proof

Contract the two disjoint connected stars

\[
 S_u=\{u,x_1,x_3\},\qquad S_v=\{v,x_2,x_4\}
\]

to vertices \(z_u,z_v\).  This is a proper minor.  The contracted
vertices are adjacent through the original edge \(uv\), so in a proper
six-colouring of the minor they receive distinct colours, say
\(\alpha\ne\beta\).

Delete the two star centres and expand only the leaves, assigning

\[
 c(x_1)=c(x_3)=\alpha,\qquad
 c(x_2)=c(x_4)=\beta.                              \tag{0.2}
\]

This gives a proper six-colouring of \(G-\{u,v\}\).  The only vertices
expanded with the same colour are the two independent pairs in (0.1).
Every edge from an expanded leaf to a vertex outside its contraction set
was represented in the contracted minor, and every edge between the two
sets was represented by \(z_uz_v\).

All four displayed vertices belong to \(N(u)-\{v\}\).  They use only
the two colours \(\alpha,\beta\).  Since \(d(u)=7\), there are only two
further vertices in \(N(u)-\{v\}\), and they use at most two further
colours.  Hence at most four of the six colours occur on
\(N(u)-\{v\}\), so

\[
 L_u=[6]-c(N(u)-\{v\})
\]

has order at least two.  The same argument gives \(|L_v|\ge2\).
Any two sets of order at least two have distinct representatives: choose
\(\lambda\in L_u\) and then
\(\mu\in L_v-\{\lambda\}\).  Colouring \(u\) with \(\lambda\) and
\(v\) with \(\mu\) extends (0.2) to a proper six-colouring of \(G\), a
contradiction. \(\square\)

The proof uses neither the Moser spindle nor connectivity nor exclusion
of a \(K_7\)-minor.  Its invariant is simultaneous control of two
colour traces by a single proper minor.

### Corollary 0.2

The adjacent degree-seven double pure-Moser frame described in Theorem
1.1 is impossible: its four common neighbours contain the two disjoint
nonedges \(x_1x_3\) and \(x_2x_4\).

### Corollary 0.3 (common-neighbour structure in the HC7 setting)

Let \(G\) satisfy the hypotheses of Theorem 0.1.  Suppose in addition
that \(G\) is seven-connected and \(K_7\)-minor-free.  If \(u,v\) are
adjacent degree-seven vertices, then

\[
        |N(u)\cap N(v)|\le4.                       \tag{0.3}
\]

If equality holds, the graph induced by the four common neighbours is
\(K_4\) with a nonempty star of edges deleted.  In particular, three of
the four common neighbours form a triangle and all nonedges among the
four share the remaining vertex.

#### Proof

First observe directly that every degree-seven vertex \(w\) satisfies
\(\alpha(G[N(w)])\le2\).  Otherwise take an independent triple
\(S\subseteq N(w)\), contract the connected star \(\{w\}\cup S\), and
six-colour the resulting proper minor.  Delete \(w\) and expand only
the independent leaves \(S\) monochromatically.  This properly colours
\(G-w\), and the vertices of \(N(w)\) use at most one colour on \(S\)
plus one colour on each of the other four neighbours.  A sixth colour
is therefore available for \(w\), contradicting the choice of \(G\).

Put \(C=N(u)\cap N(v)\).  Theorem 0.1 says that the graph
\(\overline{G[C]}\) has matching number at most one.  A family of
pairwise intersecting two-element sets is either a star or the three
edges of a triangle.  The triangle alternative would give an
independent triple in \(G[N(u)]\), so the nonedges of \(G[C]\) all
belong to one star.

If \(|C|\ge5\), then \(C\) contains a four-clique: if the complement
star has centre \(r\), use four vertices of \(C-\{r\}\) (and if the
complement has no edges, use any four).  Together with the adjacent vertices
\(u,v\), this is a \(K_6\) subgraph.  But a seven-connected graph
containing a \(K_6\) subgraph contains a \(K_7\) minor: after deleting
the six clique vertices the remaining graph is nonempty and connected;
each clique vertex has a neighbour in that remainder (otherwise its
degree is at most five); contract the remainder to one branch set.
This contradiction proves (0.3).

When \(|C|=4\), the same classification says that all nonedges share
one vertex.  There is at least one nonedge, since otherwise
\(G[\{u,v\}\cup C]\cong K_6\), again giving a \(K_7\) minor.  The
claimed form follows. \(\square\)

### Corollary 0.4 (mixed degree seven/eight)

In Corollary 0.3 it is enough to assume that \(d(u)=7\) and
\(d(v)\le8\).  The same bound and equality structure hold.

#### Proof

If \(\overline{G[C]}\) had two disjoint edges, their four endpoints
would split into two independent pairs in \(G\).  Theorem 3.2 excludes
this both when \(d(v)=7\) and when \(d(v)=8\).  The degree-seven star
contraction in the proof of Corollary 0.3 still gives
\(\alpha(G[N(u)])\le2\).  The rest of that proof is unchanged.
\(\square\)

## 1. Theorem

### Theorem 1.1

Let \(G\) be a graph which is not six-colourable but every proper minor
of \(G\) is six-colourable.  Then \(G\) cannot contain adjacent vertices
\(u,v\) and eight further vertices

\[
 X=\{x_1,x_2,x_3,x_4\},\qquad A=\{a,b\},\qquad P=\{p,q\}
\]

with

\[
 N(u)=\{v,x_1,x_2,x_3,x_4,p,q\},
 \qquad
 N(v)=\{u,x_1,x_2,x_3,x_4,a,b\},                 \tag{1.1}
\]

such that

\[
 x_1x_2,x_3x_4,ab,pq\in E(G),                    \tag{1.2}
\]

\[
 ax_1,ax_2,bx_3,bx_4,
 qx_1,qx_2,px_3,px_4\in E(G),                    \tag{1.3}
\]

while

\[
 x_1x_3,x_2x_4\notin E(G).                       \tag{1.4}
\]

In particular, the adjacent degree-seven double pure-Moser frame in a
proper-minor-minimal counterexample to \(\mathrm{HC}_7\) is impossible.

### Proof

Contract the two disjoint connected stars

\[
 S_u=\{u,x_1,x_3\},\qquad
 S_v=\{v,x_2,x_4\}                                \tag{1.5}
\]

to vertices \(z_u,z_v\), respectively.  The sets are connected through
their centres, are disjoint, and are adjacent through \(uv\) (as well as
through other displayed edges).  Hence \(z_uz_v\) is an edge of the
resulting proper minor \(M\).

By hypothesis, \(M\) has a proper six-colouring \(c\).  Write

\[
 c(z_u)=\alpha,\qquad c(z_v)=\beta .              \tag{1.6}
\]

Since \(z_uz_v\in E(M)\),

\[
                         \alpha\ne\beta .         \tag{1.7}
\]

Delete the two contracted centres and expand only their four leaves:

\[
 c(x_1)=c(x_3)=\alpha,
 \qquad c(x_2)=c(x_4)=\beta,                       \tag{1.8}
\]

while retaining all other colours from \(M\).  This is a proper
six-colouring of \(G-\{u,v\}\).  Indeed, each pair in (1.8) is
independent by (1.4); every edge from one of those four vertices to a
vertex outside its contraction set was represented by an edge incident
with the corresponding contracted vertex; and every edge between the two
sets was represented by \(z_uz_v\).

Both \(p\) and \(q\) avoid \(\alpha\), since they were adjacent to
\(u\in S_u\), and they avoid \(\beta\), since \(p\) is adjacent to
\(x_4\in S_v\) and \(q\) is adjacent to \(x_2\in S_v\).  Since
\(pq\in E(G)\), there are distinct colours \(\gamma,\delta\), both
different from \(\alpha,\beta\), such that

\[
                         \{c(p),c(q)\}=\{\gamma,\delta\}.       \tag{1.9}
\]

Similarly, both \(a,b\) avoid \(\beta\), because they were adjacent to
\(v\in S_v\); they avoid \(\alpha\), because \(a x_1,bx_3\in E(G)\).
The edge \(ab\) therefore gives distinct colours \(\varepsilon,\zeta\),
again outside \(\{\alpha,\beta\}\), with

\[
                         \{c(a),c(b)\}=\{\varepsilon,\zeta\}.  \tag{1.10}
\]

Use a fixed palette \(\mathcal C\) of six colours and define

\[
 L_u=\mathcal C-\{\alpha,\beta,\gamma,\delta\},
 \qquad
 L_v=\mathcal C-\{\alpha,\beta,\varepsilon,\zeta\}.           \tag{1.11}
\]

The four colours removed in each expression are distinct, so

\[
                         |L_u|=|L_v|=2.                         \tag{1.12}
\]

Choose distinct colours \(\lambda\in L_u\) and \(\mu\in L_v\).
Such a choice always exists: two sets of order two have a system of
distinct representatives (if they are equal, use their two different
members; otherwise choose a member of one outside the other and any
member of the other).

Give \(u\) colour \(\lambda\) and \(v\) colour \(\mu\).  Equation
(1.11) says that \(u\)'s colour is absent from
\(X\cup\{p,q\}=N(u)-\{v\}\), and that \(v\)'s colour is absent from
\(X\cup\{a,b\}=N(v)-\{u\}\).  The choices are distinct, so the edge
\(uv\) is also proper.  This extends (1.8) to a six-colouring of \(G\),
contrary to the hypothesis. \(\square\)

## 2. Audit of the minor operation

The proof does **not** make the invalid inference that a colouring of a
contraction lifts to the uncontracted graph.  The vertices internal to
the two contraction sets which would create monochromatic edges are
precisely the centres \(u,v\), and they are deleted before expansion.
Only the independent leaf pairs \(\{x_1,x_3\}\) and
\(\{x_2,x_4\}\) are expanded monochromatically.  The centres are then
coloured afresh from their two-element residual lists.

No information about the common exterior body, connectivity, planarity,
Kempe paths, or \(K_7\)-minor exclusion is used.  Thus Theorem 1.1
strictly dominates every portal/web subcase whose hypotheses already
include the adjacent double-Moser frame.

The dependency-free script
`double_moser_simultaneous_star_verify.py` exhausts all \(4320\)
admissible colour assignments on
\(z_u,z_v,a,b,p,q\) and independently verifies the two-list extension.

## 3. Label-free mechanism

### Lemma 3.1 (simultaneous-star list obstruction)

Let \(G\) be non-\(k\)-colourable while every proper minor of \(G\) is
\(k\)-colourable.  Let \(uv\in E(G)\), and let

\[
 I_u\subseteq N(u)-\{v\},\qquad
 I_v\subseteq N(v)-\{u\}
\]

be disjoint independent sets.  Contract the two disjoint stars
\(\{u\}\cup I_u\) and \(\{v\}\cup I_v\), colour the resulting proper
minor (assume at least one leaf set is nonempty), delete \(u,v\), and
expand \(I_u,I_v\) monochromatically.  Let
\(c\) be the resulting proper colouring of \(G-\{u,v\}\), and put

\[
 L_u=[k]-c(N(u)-\{v\}),\qquad
 L_v=[k]-c(N(v)-\{u\}).                            \tag{3.1}
\]

Then the two lists have no system of distinct representatives.
Equivalently, at least one list is empty, or

\[
                         L_u=L_v=\{\lambda\}       \tag{3.2}
\]

for some colour \(\lambda\).  In particular, it is impossible that
\(|L_u|,|L_v|\ge2\).

#### Proof

The expansion is proper for exactly the reason used in Theorem 1.1:
only independent leaf sets are expanded, after their centres have been
deleted.  If \(L_u,L_v\) had distinct representatives, assign them to
\(u,v\); this would properly colour \(G\), a contradiction.  Hall's
condition for two sets fails precisely in the two alternatives displayed
above. \(\square\)

Thus the reusable invariant is a two-centre simultaneous-star extension,
not a compatibility statement between independently chosen traces.

### Theorem 3.2 (quantitative common-neighbour form)

Let \(G\) be non-\(k\)-colourable while every proper minor of \(G\) is
\(k\)-colourable, and let \(uv\in E(G)\).  Suppose a set

\[
 W\subseteq N(u)\cap N(v)
\]

is the disjoint union of two nonempty independent sets \(I_u,I_v\).
If \(d(u)=d(v)=d\), then

\[
 |W|\le d-k+2.                                      \tag{3.3}
\]

If \(d(u)\ne d(v)\), then

\[
 |W|\le \max\{d(u),d(v)\}-k+1.                     \tag{3.4}
\]

#### Proof

Apply Lemma 3.1 using the two parts of \(W\).  In the expanded
colouring, all of \(W\) uses only the two contracted colours.  The
other \(d(u)-1-|W|\) vertices of \(N(u)-\{v\}\) use at most that many
additional colours.  Therefore

\[
 |L_u|\ge k-\bigl(2+d(u)-1-|W|\bigr)
          = k-d(u)-1+|W|.                          \tag{3.5}
\]

The analogous inequality holds for \(L_v\).  If the degrees are equal
and \(|W|\ge d-k+3\), both lists have order at least two, contradicting
Lemma 3.1.  This proves (3.3).

Now suppose, by symmetry, that \(d(u)<d(v)\).  If
\(|W|\ge d(v)-k+2\), then (3.5) gives \(|L_v|\ge1\), while

\[
 |L_u|\ge k-d(u)-1+d(v)-k+2
          =d(v)-d(u)+1\ge2.
\]

Two nonempty lists, one of order at least two, have distinct
representatives, again contradicting Lemma 3.1.  This proves (3.4).
\(\square\)

For a hypothetical minor-minimal counterexample to \(\mathrm{HC}_t\),
putting \(k=t-1\) shows uniformly that two adjacent vertices of minimum
possible degree \(t\) cannot have four common neighbours which split
into two nonempty independent sets.  At \(t=7\), adjacent degree-eight
vertices exclude such a five-vertex set, and adjacent degree-nine
vertices exclude such a six-vertex set.  The mixed-degree conclusion is
stronger than the crude two-list bound: at \(t=7\), an adjacent
degree-seven/degree-eight pair already excludes a four-vertex set of
this kind.

### Corollary 3.3 (the Moser hub has degree at least nine)

Under the hypotheses of Theorem 0.1, let \(v\) have degree seven and
suppose \(G[N(v)]\) is the pure Moser spindle with edge set

\[
 \{01,02,03,04,12,16,26,34,35,45,56\}.
\]

Then the vertex labelled \(0\) has degree at least nine in \(G\).

#### Proof

The vertices \(v,0\) are adjacent and have the four common neighbours
\(1,2,3,4\).  These split into the independent pairs
\(\{1,3\}\) and \(\{2,4\}\).  If \(d(0)=7\), Theorem 3.2 with equal
degrees, \(k=6\), and \(|W|=4\) gives the contradiction
\(4\le3\).  If \(d(0)\ne7\) and \(d(0)\le8\), its unequal-degree
conclusion gives

\[
 4\le \max\{7,d(0)\}-6+1\le3,
\]

again impossible.  Therefore \(d(0)\ge9\). \(\square\)

For the double-Moser frame, complementary cross pairs partition the four
common neighbours, and each exclusive outer edge is forced to use two
distinct colours outside the two contracted colours.  This makes both
residual lists have order exactly two, so the extension is automatic.
