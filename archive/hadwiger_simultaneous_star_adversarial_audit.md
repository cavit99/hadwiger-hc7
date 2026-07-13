# Adversarial audit: simultaneous-star contraction

## Verdict

**GREEN.**  The label-free simultaneous-star argument is valid.  It does
not lift a colouring through a contraction in the invalid sense: the two
star centres are deleted before the leaves are expanded, and the only
vertices expanded with a common colour form prescribed independent sets.

## 1. General two-centre theorem

### Theorem 1.1

Let every proper minor of a non-\(k\)-colourable graph \(G\) be
\(k\)-colourable.  Let \(uv\in E(G)\), and let

\[
 I_u,I_v\subseteq N(u)\cap N(v)
\]

be disjoint, nonempty independent sets.  Put
\(m=|I_u|+|I_v|\), \(d_u=d(u)\), and \(d_v=d(v)\).

If \(d_u=d_v=d\), then

\[
                         m\le d-k+2.              \tag{1.1}
\]

If \(d_u\ne d_v\), then

\[
                         m\le\max\{d_u,d_v\}-k+1.\tag{1.2}
\]

#### Proof

Contract the two vertex-disjoint connected stars
\(\{u\}\cup I_u\) and \(\{v\}\cup I_v\) to \(z_u,z_v\).
The resulting graph is a proper minor, since both leaf sets are nonempty.
Moreover \(z_uz_v\) is an edge, inherited from \(uv\).  In a
\(k\)-colouring of the minor write

\[
 c(z_u)=\alpha,\qquad c(z_v)=\beta;qquad \alpha\ne\beta.
\]

Delete \(u,v\), expand every vertex of \(I_u\) with colour \(\alpha\),
and expand every vertex of \(I_v\) with colour \(\beta\).  This is a
proper colouring of \(G-\{u,v\}\).  There is no edge inside either
monochromatic leaf set.  An edge from a leaf to any vertex outside its
own contraction set was represented in the minor; an edge between the
two leaf sets was represented by \(z_uz_v\), whose ends have distinct
colours.

Let

\[
 L_u=[k]\setminus c(N(u)-\{v\}),\qquad
 L_v=[k]\setminus c(N(v)-\{u\}).
\]

All \(m\) selected common neighbours use only \(\alpha,\beta\).
The other \(d_u-1-m\) neighbours of \(u\), apart from \(v\), use at
most that many further colours.  Consequently

\[
 |L_u|\ge k-(2+d_u-1-m)=k-d_u-1+m,               \tag{1.3}
\]

and analogously \(|L_v|\ge k-d_v-1+m\).

If \(d_u=d_v=d\) and \(m\ge d-k+3\), both lists have at least two
members.  They have distinct representatives, which colour \(u,v\)
and contradict the choice of \(G\).  This proves (1.1).

If, say, \(d_u<d_v\) and \(m\ge d_v-k+2\), then
\(|L_v|\ge1\), while

\[
 |L_u|\ge d_v-d_u+1\ge2.
\]

Again the two lists have distinct representatives: choose the colour of
the singleton list first if necessary, then a different colour from the
list of order at least two.  This proves (1.2). \(\square\)

For \(k=6\) and \(d_u=d_v=7\), four common neighbours split into two
independent pairs would violate (1.1).  This proves the proposed
label-free lemma.

## 2. The local independence bound needs no external theorem

### Lemma 2.1

Under the minor-minimality hypothesis of Theorem 1.1, if \(d(w)=k+1\),
then \(\alpha(G[N(w)])\le2\).

#### Proof

If \(S\subseteq N(w)\) were an independent triple, contract the
connected star \(\{w\}\cup S\), colour the proper minor, delete \(w\),
and expand only \(S\) with the colour of the contracted vertex.  This
properly colours \(G-w\).  The triple uses one colour and the other
\(k-2\) neighbours of \(w\) use at most \(k-2\) further colours.
Thus at most \(k-1\) colours occur on \(N(w)\), and a missing colour
colours \(w\), a contradiction. \(\square\)

## 3. The connectivity-to-minor step

### Lemma 3.1

If a seven-connected graph contains a \(K_6\) subgraph, then it
contains a \(K_7\) minor.

#### Proof

Let \(Q\) be the six-clique.  A seven-connected graph has at least
eight vertices, and deletion of the six vertices of \(Q\) leaves a
nonempty connected graph \(R\).  Every \(q\in Q\) has a neighbour in
\(R\): otherwise \(d(q)=5\), contradicting seven-connectivity (or,
equivalently, \(Q-\{q\}\) separates \(q\) from \(R\)).  Contract
\(R\) to one branch set and retain the six vertices of \(Q\) as
singleton branch sets. \(\square\)

## 4. Sharp common-neighbour consequence available from this method

### Theorem 4.1

Let \(G\) be seven-connected and \(K_7\)-minor-free, not
six-colourable, with every proper minor six-colourable.  If \(uv\) is
an edge, \(d(u)=7\), and \(d(v)\le8\), then, for
\(C=N(u)\cap N(v)\),

\[
                         |C|\le4.                 \tag{4.1}
\]

All nonedges of \(G[C]\) share a common end.  If \(|C|=4\), there is
at least one such nonedge; equivalently, \(G[C]\) consists of a
triangle and a fourth vertex which is not complete to that triangle.

#### Proof

The minimum degree is at least seven.  If two nonedges of \(G[C]\)
were vertex-disjoint, their four ends would split into two independent
pairs.  Theorem 1.1 excludes this both when \(d(v)=7\), by (1.1), and
when \(d(v)=8\), by (1.2).  Hence the complement \(J=\overline{G[C]}\)
has matching number at most one.

By Lemma 2.1, \(J\) is triangle-free.  A triangle-free graph of
matching number at most one is a star together with isolated vertices:
after choosing two intersecting edges, any edge not through their common
end would either be disjoint from one or complete a triangle.
Thus all nonedges in \(G[C]\) share one vertex \(r\) (with the empty
family allowed).

If \(|C|\ge5\), then \(C-\{r\}\) contains a four-clique (when the
nonedge family is empty, choose \(r\) arbitrarily).  Together with \(u,v\),
this is a \(K_6\), contrary to Lemma 3.1 and the exclusion of a
\(K_7\) minor.  Hence (4.1) holds.  If \(|C|=4\) and there is no
nonedge, \(G[\{u,v\}\cup C]\) itself is \(K_6\), the same
contradiction.  The remaining description follows. \(\square\)

### Corollary 4.2 (pure-Moser hub escalation)

If \(d(v)=7\) and \(G[N(v)]\) is the pure Moser spindle with edges

\[
 \{01,02,03,04,12,16,26,34,35,45,56\},
\]

then the vertex labelled \(0\) has degree at least nine in \(G\).

#### Proof

The vertices \(v,0\) have the four common neighbours \(1,2,3,4\),
partitioned into the independent pairs \(\{1,3\}\) and \(\{2,4\}\).
If \(d(0)=7\), (1.1) bounds this set by three.  If \(d(0)\ne7\) and
\(d(0)\le8\), (1.2) bounds it by
\(\max\{7,d(0)\}-6+1\le3\).  Both are contradictions. \(\square\)

### Theorem 4.3 (uniform conditional overlap theorem)

Let \(t\ge5\).  Suppose \(G\) is \(t\)-connected and
\(K_t\)-minor-free, is not \((t-1)\)-colourable, and every proper
minor is \((t-1)\)-colourable.  If \(uv\in E(G)\), \(d(u)=t\), and
\(d(v)\le t+1\), then

\[
 |N(u)\cap N(v)|\le t-3.                          \tag{4.2}
\]

The nonedges induced by the common neighbours all share one end.  If
equality holds in (4.2), this nonedge family is nonempty.

#### Proof

Use Theorem 1.1 with \(k=t-1\).  Since \(G\) is \(t\)-connected,
\(d(v)\ge t\).  If \(d(v)=t\), (1.1) excludes four common vertices
partitioned into two independent pairs; if \(d(v)=t+1\), (1.2) does
the same.  Hence the complement on the common set has matching number
at most one.  Lemma 2.1 applied at \(u\) makes that complement
triangle-free, so it is a star plus isolated vertices.

A \(t\)-connected, \(K_t\)-minor-free graph contains no
\(K_{t-1}\) subgraph.  Indeed, deletion of such a clique leaves a
nonempty connected remainder, every clique vertex has a neighbour in
that remainder, and contracting the remainder gives \(K_t\).

If the common set had at least \(t-2\) vertices, deleting the centre
of its complement star would leave a clique on at least \(t-3\)
vertices; together with \(u,v\), this contains \(K_{t-1}\).  This
proves (4.2).  At equality, an empty complement would make
\(\{u,v\}\) together with all \(t-3\) common vertices a
\(K_{t-1}\), so at least one nonedge is present. \(\square\)

### Theorem 4.4 (exact degree-nine rainbow trace)

Let \(G\) be non-six-colourable while every proper minor is
six-colourable.  Let \(vh\in E(G)\), where \(d(v)=7\) and \(d(h)=9\).
Suppose four common neighbours split into disjoint independent pairs

\[
 W=I_v\mathbin{\dot\cup}I_h,\qquad |I_v|=|I_h|=2.
\]

Contract \(\{v\}\cup I_v\) and \(\{h\}\cup I_h\), and consider
**any** six-colouring of the resulting minor.  If the two contracted
vertices have colours \(\alpha,\beta\), then the four vertices

\[
 E=N(h)\setminus(\{v\}\cup W)
\]

are coloured bijectively by the four colours outside
\(\{\alpha,\beta\}\).

#### Proof

Delete the two centres and expand the two independent pairs as in
Theorem 1.1.  The list available at \(v\) has order at least

\[
 6-7-1+4=2.
\]

If the list at \(h\) were nonempty, these two lists would have distinct
representatives and would colour \(v,h\), a contradiction.  Therefore
the list at \(h\) is empty: every one of the six colours appears on
\(N(h)-\{v\}=W\cup E\).

The set \(W\) uses exactly \(\alpha,\beta\).  Since \(|E|=4\), the
four vertices of \(E\) must use all four remaining colours, each
exactly once. \(\square\)

For the pure-Moser hub of Corollary 4.2, when its degree is exactly
nine the set \(E\) is precisely its four neighbours outside
\(N[v]\).  Thus the first degree allowed by the inequality comes with
a rigid universal rainbow state, rather than with no information.

### Corollary 4.5 (complete Kempe coupling at degree nine)

In every colouring considered in Theorem 4.4, for each distinct
\(e,f\in E\), the vertices \(e,f\) lie in the same component of the
subgraph induced by their two colours.

#### Proof

Otherwise interchange those two colours on the bichromatic component
containing \(e\).  This produces another proper colouring of the same
contracted minor.  The two contracted vertices are unaffected because
their colours are \(\alpha,\beta\), outside the two colours being
switched.  The new colouring gives \(e,f\) the same colour, contrary
to Theorem 4.4, which applies to every colouring of that minor.
\(\square\)

Thus the four external neighbours of a degree-nine pure-Moser hub form
a rainbow four-root system with all six bichromatic root pairs
connected, entirely inside the four residual colour classes.

### Theorem 4.6 (rooted four-clique core at degree nine)

Retain the setting and a colouring of Theorem 4.4.  Let \(J\) be the
subgraph of the contracted minor induced by the four colour classes
outside \(\{\alpha,\beta\}\).  Then every proper four-colouring of
\(J\) uses all four colours on \(E\).  Consequently, by the proved
four-colour case of Holroyd's Strong Hadwiger Conjecture, \(J\)
contains an \(E\)-rooted \(K_4\)-model.

#### Proof

Suppose a four-colouring of \(J\) used at most three colours on \(E\).
Keep the two omitted original colour classes as independent sets and
give them two distinct fresh colours.  The fresh palette is disjoint
from the four-colouring palette, so this extends to a proper
six-colouring of the whole contracted minor.  The two contracted
vertices lie in the two restored classes and receive the two fresh
colours, whereas \(E\) uses at most three of the other four.  This
contradicts Theorem 4.4.  Thus \(E\) is four-saturating in \(J\), and
Strong \(\mathrm{HC}_4\) gives the rooted model. \(\square\)

The model avoids both contracted colour classes, so in particular it
avoids the contracted vertices.  It therefore lifts without any bag
surgery to \(G-(\{v,h\}\cup W)\).  Adding the singleton bag
\(\{h\}\), which is adjacent to every root in \(E\), produces a
\(K_5\)-model.  This does not by itself give a \(K_7\)-model: two
further pairwise adjacent branch sets meeting all four rooted bags are
still required.

## 5. Exact limit of the deduction

The method does **not** rule out the equality case \(|C|=4\) in
Theorem 4.1.  There the four common neighbours may induce
\(K_4\) minus a nonempty star.  The three vertices away from the star
centre, together with \(u,v\), form a \(K_5\), not a \(K_6\).
Seven-connectivity alone does not supply the two labelled outside branch
sets needed to extend that \(K_5\) to a \(K_7\) minor.  Claiming more
from the present argument would silently assume the unresolved
portal-splitting step.

There is also an exact degree-nine barrier.  On an edge joining a
degree-seven vertex to a degree-nine vertex, Theorem 1.1 with \(k=6\)
only forbids a selected common set of order at least five.  Lemma 2.1,
however, says that every independent set in the degree-seven
neighbourhood has order at most two.  Hence the union of the two
independent leaf sets used by this method has order at most four.  The
quantitative simultaneous-star inequality is therefore automatic on a
degree-seven/degree-nine edge and gives no further *numerical*
restriction.

In particular, Corollary 4.2 is sharp **for this argument**: it escalates
the pure-Moser hub to degree at least nine, but does not exclude degree
nine, although Theorem 4.4 records its exact residual colouring state.
Excluding that equality would require an additional constraint on
the colours of the four neighbours outside the selected pairs (for
example, a portal/contact or cross-trace relation).  No such constraint
has been proved here.
