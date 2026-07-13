# A simultaneous star forces a rooted four-clique outside its hub

## 0. Degree-free rooted-core theorem

### Theorem 0.1

Let \(G\) be non-six-colourable while every proper minor of \(G\) is
six-colourable.  Let \(vh\in E(G)\), where \(d(v)=7\).  Suppose four
common neighbours have a disjoint partition

\[
 W=I_v\mathbin{\dot\cup}I_h
\]

into two nonempty independent sets.  Put

\[
 E=N(h)-\bigl(\{v\}\cup W\bigr).
\]

Then \(|E|\ge4\), and

\[
 G-(\{v,h\}\cup W)
\]

contains a \(K_4\)-model whose four bags each contain a neighbour of
\(h\) from \(E\).  Consequently those four bags together with
\(\{h\}\) form a \(K_5\)-model.

#### Proof

Contract the two stars \(\{v\}\cup I_v\) and
\(\{h\}\cup I_h\), and six-colour the resulting proper minor \(M\).
Let the contracted vertices have colours \(\alpha\ne\beta\).  Delete
the two centres and expand only the independent leaves.  The set \(W\)
then uses just \(\alpha,\beta\).

Apart from \(h\) and \(W\), the degree-seven vertex \(v\) has only two
neighbours.  Its residual colour list therefore has order at least two.
The residual list at \(h\) must be empty: if it contained a colour, the
two lists would have distinct representatives and would extend the
colouring to \(G\).  Hence all six colours occur on

\[
 N(h)-\{v\}=W\mathbin{\dot\cup}E.                 \tag{0.1}
\]

Since \(W\) uses only \(\alpha,\beta\), every colour in
\(\Gamma=[6]-\{\alpha,\beta\}\) occurs on \(E\); in particular
\(|E|\ge4\).

Let \(J\) be the subgraph of \(M\) induced by the four colour classes
in \(\Gamma\), and put \(X=E\cap V(J)\).  Every proper four-colouring
of \(J\) uses all four colours on \(X\).  Otherwise combine that
four-colouring with the unchanged \(\alpha\)- and \(\beta\)-classes of
\(M-J\), using disjoint palettes.  This would be a six-colouring of
\(M\) in which one colour of \(\Gamma\) is absent from \(E\),
For this new colouring, repeat the preceding residual-list argument:
the list at \(v\) still has order at least two, so the list at \(h\)
must again be empty.  Equation (0.1) is then violated.

By the proved four-colour case of Holroyd's Strong Hadwiger Conjecture,
\(J\) has an \(X\)-rooted \(K_4\)-model.  Both contracted vertices have
colours outside \(\Gamma\), so the model avoids them and lifts literally
to \(G-(\{v,h\}\cup W)\).  Each bag meets \(X\subseteq E\subseteq
N(h)\), so adding the singleton \(\{h\}\) gives the asserted
\(K_5\)-model. \(\square\)

This theorem is degree-free at the hub.  The special case \(d(h)=9\)
below adds a bijective rainbow trace and complete pairwise Kempe
connectivity.

### Proposition 0.2 (uniform saturation schema)

Let \(G\) be non-\(k\)-colourable while every proper minor is
\(k\)-colourable.  Let \(uv\in E(G)\), and suppose

\[
 W=I_u\mathbin{\dot\cup}I_v\subseteq N(u)\cap N(v)
\]

for two nonempty independent sets.  If

\[
 |W|\ge d(u)-k+3,                                  \tag{0.2}
\]

then, after contracting the two stars and fixing any \(k\)-colouring,
the following hold.  If their colours are \(\alpha,\beta\), put

\[
 E_v=N(v)-(\{u\}\cup W)
\]

and let \(J\) be induced by the other \(k-2\) colour classes.  Then

1. every colour outside \(\{\alpha,\beta\}\) occurs on \(E_v\);
2. \(X=E_v\cap V(J)\) uses all \(k-2\) colours in every proper
   \((k-2)\)-colouring of \(J\); and
3. \(\chi(J)=k-2\).

If Strong Hadwiger is known for \(k-2\) colours, then \(J\) has an
\(X\)-rooted \(K_{k-2}\)-model, and adding \(\{v\}\) gives a
\(K_{k-1}\)-model.  Ordinary Hadwiger at \(k-2\) gives only an
unrooted \(K_{k-2}\)-model.

#### Proof

The list estimate from the simultaneous-star proof is

\[
 |L_u|\ge k-d(u)-1+|W|\ge2.
\]

Hence \(L_v\) must be empty in every colouring of the contracted
minor.  The set \(W\) uses only \(\alpha,\beta\), so all other colours
occur on \(E_v\).  Recolouring \(J\) with a palette disjoint from
\(\{\alpha,\beta\}\) and repeating the same list argument proves the
saturation assertion.  It also rules out a \((k-3)\)-colouring of
\(J\), while its defining colouring shows \(\chi(J)\le k-2\).
The two minor conclusions are exactly ordinary and Strong Hadwiger at
parameter \(k-2\). \(\square\)

For \(k=6\), Strong HC4 is a theorem, so Proposition 0.2 becomes an
unconditional rooted-model tool for \(HC_7\).  For larger parameters it
pinpoints the extra rooted input rather than hiding the uniform
model-meeting obstruction in a recolouring argument.

## 1. Setup

Let \(G\) be non-six-colourable while every proper minor of \(G\) is
six-colourable.  Let \(vh\in E(G)\), with

\[
 d(v)=7,\qquad d(h)=9.
\]

Suppose four common neighbours form a disjoint union

\[
 W=I_v\mathbin{\dot\cup}I_h,
\]

where \(I_v,I_h\) are nonempty independent sets.  Contract the two
disjoint stars \(\{v\}\cup I_v\) and \(\{h\}\cup I_h\) to vertices
\(z_v,z_h\), obtaining a proper minor \(M\).  Fix an arbitrary proper
six-colouring \(c\) of \(M\), and write

\[
 c(z_v)=\alpha,\qquad c(z_h)=\beta.
\]

The edge \(vh\) gives \(\alpha\ne\beta\).  Put

\[
 E=N(h)-\bigl(\{v\}\cup W\bigr).
\]

Then \(|E|=4\).

## 2. Universal rainbow trace

### Theorem 2.1

In every six-colouring \(c\) of \(M\), the four vertices of \(E\)
receive the four colours in

\[
 [6]-\{\alpha,\beta\}
\]

bijectively.  In particular no vertex of \(E\) receives \(\alpha\) or
\(\beta\).

#### Proof

Delete the two contracted centres and expand only the independent leaf
sets, colouring \(I_v\) with \(\alpha\) and \(I_h\) with \(\beta\).
This properly colours \(G-\{v,h\}\).

The four vertices of \(W\) use the two colours \(\alpha,\beta\).  Apart
from \(h\) and \(W\), the degree-seven vertex \(v\) has only two
neighbours.  Hence at most four colours occur on \(N(v)-\{h\}\), and
the residual list \(L_v\) for \(v\) has order at least two.

If the residual list \(L_h\) were nonempty, \(L_v,L_h\) would have
distinct representatives, so the expanded colouring would extend to a
six-colouring of \(G\).  Therefore \(L_h=\varnothing\): all six colours
occur on

\[
 N(h)-\{v\}=W\mathbin{\dot\cup}E.
\]

The set \(W\) already uses exactly \(\alpha,\beta\), while \(E\) has
four vertices.  Thus its colours are exactly the other four, each once.
\(\square\)

This is an equality-state conclusion, not merely the failure of the
degree-nine extension argument.

## 3. Complete bichromatic connectivity

### Theorem 3.1

For every pair \(e,f\in E\), the vertices \(e,f\) lie in the same
component of the subgraph of \(M\) induced by their two colours.

#### Proof

Write \(c(e)=\gamma\) and \(c(f)=\delta\).  These colours are distinct
and avoid \(\alpha,\beta\) by Theorem 2.1.  If \(e,f\) lay in different
\(\{\gamma,\delta\}\)-components, interchange \(\gamma,\delta\) on
the component containing \(e\).  This is another proper six-colouring
of \(M\); neither contracted vertex changes colour.  Now \(e,f\) have
the same colour, contradicting Theorem 2.1 applied to the new colouring.
\(\square\)

## 4. A rooted \(K_4\)-model outside both stars

We use the proved four-colour case of Holroyd's Strong Hadwiger
Conjecture (Martinsson--Steiner): if a graph is four-colourable and every
proper four-colouring uses all four colours on a set \(X\), then it has
an \(X\)-rooted \(K_4\)-minor.

### Theorem 4.1

The graph

\[
 G-(\{v,h\}\cup W)
\]

contains an \(E\)-rooted \(K_4\)-model.  Consequently \(G\) contains a
\(K_5\)-model consisting of \(\{h\}\) and four bags rooted at the four
vertices of \(E\).

#### Proof

In the fixed colouring \(c\), let \(J\) be the subgraph of \(M\)
induced by the four colour classes outside \(\{\alpha,\beta\}\).  It is
four-colourable and contains \(E\).

Every proper four-colouring of \(J\) uses all four colours on \(E\).
Otherwise recolour \(J\) with such a colouring, retain the original
colours \(\alpha,\beta\) on \(M-J\), and regard the two palettes as
disjoint.  This is a proper six-colouring of \(M\) in which \(E\) uses
at most three colours, contradicting Theorem 2.1.

Strong HC4 therefore supplies an \(E\)-rooted \(K_4\)-model in \(J\).
The contracted images \(z_v,z_h\) have colours \(\alpha,\beta\), so
they do not belong to \(J\); neither do the four contracted leaves when
the model is lifted.  Hence the model lifts literally to
\(G-(\{v,h\}\cup W)\).  Finally, \(h\) is adjacent to every root in
\(E\), so its singleton is adjacent to all four rooted bags. \(\square\)

## 5. Pure-Moser specialization and exact gap

If \(G[N(v)]\) is the pure Moser spindle and \(h\) is its distinguished
degree-four hub, the simultaneous-star theorem forces \(d(h)\ge9\).
At equality, \(E\) is exactly the set of four neighbours of \(h\)
outside \(N[v]\), and Theorems 2.1--4.1 apply.

The result does **not** yet give a \(K_7\)-minor.  Two further disjoint
branch sets would have to be joined to all four rooted bags and to
\(\{h\}\).  What has been gained is a genuine model-meeting theorem:
the four exterior hub neighbours are no longer merely colour-saturated
or pairwise Kempe-connected; they are roots of an actual \(K_4\)-model
that avoids both simultaneous stars.
