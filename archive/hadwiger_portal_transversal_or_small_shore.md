# A label-free portal-transversal or small-shore theorem

## 1. Minimum-cut form

### Theorem 1.1 (portal transversal or small shore)

Let \(G\) be a graph, let \(S\) be a minimum vertex cut, and let \(D\) be
a component of \(G-S\). For \(s\in S\), put

\[
 P_s=N_D(s).
\]

Then precisely one of the following conclusions holds:

1. the family \((P_s:s\in S)\) has a system of distinct
   representatives; or
2. there is a nonempty \(I\subseteq S\) such that

\[
 D=\bigcup_{s\in I}P_s,
 \qquad
 |D|<|I|\le |S|.
\tag{1.1}
\]

In particular, every component \(D\) with \(|D|\ge |S|\) has an
\(S\)-indexed set of distinct portal vertices.

#### Proof

Because \(S\) is a minimum cut, it is inclusion-minimal. Hence every
vertex of \(S\) has a neighbour in every component of \(G-S\), so all
the portal sets \(P_s\) are nonempty.

Suppose that the family has no system of distinct representatives.
By Hall's theorem there is a nonempty \(I\subseteq S\) for which

\[
 U:=\bigcup_{s\in I}P_s
 \quad\hbox{satisfies}\quad
 |U|<|I|.
\tag{1.2}
\]

If \(D-U\ne\varnothing\), take a component \(C\) of \(D-U\). It has no
neighbour in \(D-(C\cup U)\). It also has no neighbour in a different
component of \(G-S\). Finally, it has no neighbour in \(I\), by the
definition of \(U\). Therefore

\[
 N_G(C)\subseteq U\cup(S-I).
\]

The right side has order

\[
 |U|+|S-I|<|I|+|S-I|=|S|.
\]

It separates \(C\) from every other component of \(G-S\), contrary to
the minimum cardinality of \(S\). Thus \(D=U\), and (1.1) follows from
(1.2). \(\square\)

## 2. Fixed-boundary connectivity form

The same proof does not require that the displayed boundary itself be
a minimum cut if ambient connectivity supplies the strict inequality.

### Theorem 2.1 (Hall-deficiency cut)

Let \(S=B\mathbin{\dot\cup}A\), and let \(D\subseteq V(G)-S\) induce a
connected subgraph. Assume that every edge from \(D\) to \(G-D\) ends
in \(S\). For
\(b\in B\), put \(P_b=N_D(b)\), and suppose every \(P_b\) is nonempty.
If these portal sets have no system of distinct representatives, then
there is a nonempty \(I\subseteq B\), with

\[
 U=\bigcup_{b\in I}P_b,\qquad |U|<|I|,
\]

such that either \(D=U\), or

\[
 U\cup(B-I)\cup A
\tag{2.1}
\]

is a vertex cut of order at most \(|B|+|A|-1\).

#### Proof

Choose a Hall-deficient set \(I\). If \(D-U\ne\varnothing\), a
component \(C\) of \(D-U\) has no neighbour outside the set in (2.1).
Its order is

\[
 |U|+|B-I|+|A|\le |B|+|A|-1.
\]

For any \(b\in I\), the vertex \(b\) lies outside both \(C\) and the set
in (2.1), and it has no neighbour in \(C\), since \(P_b\subseteq U\).
Thus (2.1) is a proper cut. \(\square\)

### Corollary 2.2

Under Theorem 2.1, if \(G\) is \((|B|+|A|)\)-connected, then either the
portal family has an SDR or

\[
 |D|<|B|.
\]

This is the form used in the \(C_6\dot\cup K_1\) laboratory: \(B\) is
the six-cycle boundary and \(A\) is the apex singleton. Thus every shore
of order at least six has six distinct portal representatives.

## 3. Degree consequence for minimal Hadwiger counterexamples

Let \(G\) be a proper-minor-minimal counterexample to \(\mathrm{HC}_t\),
so that \(\delta(G)\ge t\), and let \(S\) be a minimum cut of order
\(\kappa(G)\). If a component \(D\) is in outcome 2 of Theorem 1.1,
then \(|D|\le |S|-1\). Hence every \(x\in D\) satisfies

\[
 t\le d_G(x)\le (|D|-1)+|S|\le 2|S|-2.
\]

Consequently

\[
 |S|\ge \left\lceil\frac{t+2}{2}\right\rceil.
\tag{3.1}
\]

Equivalently, if a minimum cut has order below
\(\lceil(t+2)/2\rceil\), then every component of its complement has
an \(S\)-indexed portal transversal.

This dichotomy is uniform in \(t\). It isolates the next genuinely
structural step: turn distinct portal representatives inside a full
shore into low-loss connected block witnesses, or turn the failure of
that connection problem into a smaller, colour-gluable separator. The
exposure-weighted knitting theorem handles the latter once the witnesses
and their deletion loss are controlled.

## 4. Exact independent-set traces across a full shore

The same minimum-cut geometry gives more than contacts.

### Lemma 4.1 (full-shore exact trace)

Let \(G\) be \(t\)-contraction-critical, let \(S\) be an
inclusion-minimal vertex cut, and let \(D\) be a connected component of
\(G-S\). For every nonempty independent set \(I\subseteq S\), the graph
\(G-D\) has a proper \((t-1)\)-colouring \(c\) and a colour \(\gamma\)
such that

\[
 \{s\in S:c(s)=\gamma\}=I.
\tag{4.1}
\]

#### Proof

Every vertex of \(S\) has a neighbour in \(D\). The set \(D\cup I\) is
connected: start with connected \(D\) and attach each vertex of \(I\)
along one of its edges into \(D\). Contract \(D\cup I\) to a vertex
\(w\). This is a proper minor of \(G\), so it has a proper
\((t-1)\)-colouring. Give every vertex of \(I\) the colour of \(w\) and
delete \(D\).

The expansion is proper because \(I\) is independent, and every
neighbour outside \(D\cup I\) of a vertex in \(I\) was adjacent to
\(w\) after contraction. Moreover, every \(s\in S-I\) has a neighbour
in \(D\), so \(s\) was adjacent to \(w\) in the minor and cannot receive
its colour. This proves (4.1). \(\square\)

Thus every independent subset of a minimum adhesion occurs as an exact
single colour class from either side. This strictly strengthens abstract
colour saturation. It does not force the remaining colour classes to
agree across the two sides; that simultaneous compatibility is exactly
the block-knitting problem.

### Lemma 4.2 (boundary minor-switching)

Keep the hypotheses of Lemma 4.1 and put

\[
 Q=G[D\cup S],\qquad R=G-D.
\]

For every vertex \(x\in D\), there is a boundary colouring
\(\sigma_x:S\to[t-1]\) which extends to both \(R\) and \(Q-x\), but
does not extend to \(Q\). For every edge \(e\in E(G[D])\), there is a
boundary colouring \(\sigma_e\) which extends to both \(R\) and \(Q-e\),
but does not extend to \(Q\). In the latter extension the two ends of
\(e\) receive the same colour.

#### Proof

Colour the proper subgraph \(G-x\) with \(t-1\) colours and restrict
the colouring to \(S\). It extends to \(R\) and \(Q-x\). If the same
boundary assignment extended to \(Q\), gluing that extension to the
fixed colouring of \(R\) would colour \(G\), a contradiction.

The edge version is identical, using a proper \((t-1)\)-colouring of
\(G-e\). Its ends must have the same colour, since otherwise the
deleted edge could be restored and the colouring would already colour
\(G\). \(\square\)

Thus a counterexample shore is not merely portal-rich. Every internal
vertex and edge is essential to its boundary extension relation. Any
web or ladder outcome in a portal-splitting theorem must be tested
against this one-step state transition; ordinary connectivity and Hall
data alone do not suffice.

## 5. Limitation

An SDR is not itself a rooted clique model. The connecting subgraphs
for different boundary blocks may intersect, and a connected repair
piece may meet two portal classes at one vertex not chosen by the SDR.
The \(C_6\) portal tetrahedron is the sharp local warning. Thus the
theorem supplies a contact-or-small-shore principle, not the still
missing portal-splitting theorem.
