# One-step minor transitions across a seven-vertex boundary

## 1. Setup

Let \(G\) be a proper-minor-minimal counterexample to \(\mathrm{HC}_7\),
let \(d(v)=7\), and suppose

\[
G-N[v]=C_1\mathbin{\dot\cup}C_2.
\]

Put \(L_i=G[N\cup C_i]\), where \(N=N(v)\), and let
\(\mathcal E_i\) be the matching states on \(N\) which extend to a
six-colouring of \(L_i\).  As usual,

\[
\mathcal E_1\cap\mathcal E_2
\quad\hbox{contains no state of size at least two}. \tag{1.1}
\]

The following records precisely the one-step criticality which is absent
from a purely abstract extension-family calculation.

## 2. Transition lemma

### Lemma 2.1 (every internal minor step creates an opposite state)

Fix \(i\in\{1,2\}\), write \(j=3-i\), and perform any one of the
following operations \(\mu\) on the \(C_i\)-side:

* delete a vertex of \(C_i\);
* delete or contract an edge internal to \(C_i\); or
* delete or contract an edge between \(C_i\) and \(N\), retaining the
  boundary label of its endpoint in \(N\) after contraction.

Then there is a matching state \(R\) on \(N\), with \(2\le |R|\le3\),
such that

\[
R\in\mathcal E_j,\qquad
R\notin\mathcal E_i,\qquad
R\text{ extends to }\mu(L_i). \tag{2.1}
\]

Thus each side is jointly one-step-minor-critical for a finite family of
opposite-side precolouring states.  In the pure-Moser case this target
family has at most 42 members (26 double and 16 triple matchings).

#### Proof

Apply the same operation to \(G\).  It gives a proper minor \(G'\), so
\(G'\) has a proper six-colouring \(c\).  The colour of \(v\) is absent
from \(N\), since \(v\) remains adjacent to all seven distinct boundary
vertices.  Hence at most five colours occur on \(N\).

Every colour class on \(N\) is independent in \(G[N]\).  Dirac's equality
bound gives \(\alpha(G[N])\le2\), so the non-singleton classes form a
matching state \(R\) in \(\overline{G[N]}\).  Seven boundary vertices use
at most five colours, whence \(2\le |R|\le3\).

For an internal operation, the other side \(L_j\) is unchanged.  Contracting
an edge from \(C_i\) to a boundary vertex can only add edges inside the
labelled copy of \(N\); after those extra edges are forgotten, the
restriction of \(c\) is still a proper colouring of the original \(L_j\).
Thus in every case it proves \(R\in\mathcal E_j\).  Its restriction to the
operated side proves that \(R\) extends to \(\mu(L_i)\).  Finally
\(R\notin\mathcal E_i\) follows from (1.1). \(\square\)

### Lemma 2.2 (edge-transition Kempe fan)

Let \(xy\) be an edge internal to \(C_i\), and let \(c\) be any
six-colouring of \(G-xy\).  Then

1. \(c(x)=c(y)\);
2. each of \(x,y\) has a neighbour of every other colour; and
3. for every colour \(\gamma\ne c(x)\), the vertices \(x,y\) lie in the
   same component of the subgraph of \(G-xy\) induced by
   \(\{c(x),\gamma\}\).

The boundary state of \(c\) is one of the newly created states in (2.1).

#### Proof

If \(c(x)\ne c(y)\), restoring \(xy\) gives a six-colouring of \(G\).
Thus the colours agree.  If, say, \(x\) has no neighbour of a different
colour \(\gamma\), recolour \(x\) with \(\gamma\) and restore \(xy\),
again a contradiction.  Finally, if the two endpoints lie in different
\(c(x)\)-\(\gamma\) components, swap those colours on the component
containing \(x\); this separates their colours and again permits restoring
\(xy\). \(\square\)

The colourings of \(G-xy\) and \(G/xy\) correspond: every colouring of
the deletion has equal endpoint colours by Lemma 2.2, and hence factors
through the contraction.  Thus contraction does not lose any edge witness.

## 3. Exact consequence and limitation

Lemma 2.1 is a genuine cross-boundary consequence of proper-minor
criticality.  It is not encoded by the consistent abstract certificate in
`hadwiger_moser_state_certificate.md`.  A successful finite-boundary proof
may therefore target the following sharper assertion:

> No pair of Moser-boundaried graphs can realize the archived state
> certificate while every internal vertex and edge operation creates an
> opposite-family state with the Kempe fan of Lemma 2.2.

Proving that assertion still requires graph geometry.  Lemma 2.1 alone
does not bound the size of a side, because different internal operations
may create different states and precolouring-critical graphs can be large.
