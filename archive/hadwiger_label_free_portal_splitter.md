# A label-free portal splitter with exact critical-state exchange

## 1. Portal patterns

Let \(D\) be a graph and \(L\) a disjoint labelled boundary such that every
neighbour of \(D\) lies in \(D\cup L\). For \(\lambda\in L\), put

\[
 P_\lambda=N_D(\lambda).
\]

A portal-linkage pattern consists of an integer \(m\), label demands
\(R_1,\ldots,R_m\subseteq L\), and an optional graph \(F\) on
\(\{1,\ldots,m\}\). It is realized in \(D\) if there are pairwise disjoint
nonempty connected sets \(B_1,\ldots,B_m\subseteq D\) such that

\[
 B_i\cap P_\lambda\ne\varnothing
 \quad(\lambda\in R_i),
\tag{1.1}
\]

and \(B_i,B_j\) are adjacent whenever \(ij\in E(F)\). Disjoint path
demands, frame crossings, rooted partial clique models, and prescribed shore
splittings all fit this definition.

Let \(\mathfrak F\) be any finite family of such patterns. Say that \(D\)
is \(\mathfrak F\)-free if it realizes none of them.

### Lemma 1.1 (contraction closure)

If \(D\) is \(\mathfrak F\)-free and \(e\in E(D)\), then \(D/e\), with
portal rows united at the contracted vertex, is \(\mathfrak F\)-free.

### Proof

Let \(z\) be the contracted vertex and suppose a pattern is realized in
\(D/e\) by \(B'_1,\ldots,B'_m\). Pairwise disjointness means that at most
one set contains \(z\). Sets avoiding \(z\) lift unchanged and avoid both
ends of \(e\). In the unique set containing \(z\), replace \(z\) by both
ends of \(e\). The replacement is connected; every incident edge and every
portal contact at \(z\) lifts to at least one endpoint; and every demanded
cross-edge between branch sets also lifts. The lifted sets realize the same
pattern in \(D\), a contradiction. \(\square\)

The proof applies to any contraction-closed collection of rooted
connected-support certificates, even when it is packaged without the
explicit pattern notation.

## 2. Relative connectivity

For every nonempty proper \(X\subsetneq D\), put

\[
 \phi_D(X)=|N_D(X)-X|+|N_L(X)|.
\]

Call \(D\) relatively \(k\)-connected if \(\phi_D(X)\ge k\) for every
such \(X\), and full if \(N_L(D)=L\).

### Lemma 2.1 (exact contraction defect)

Let \(xy\in E(D)\). Contraction preserves fullness. If \(D/xy\) is not
relatively \(k\)-connected, then there is a nonempty proper set
\(Y\subseteq D-\{x,y\}\) such that

\[
 \phi_D(Y)=k,\qquad x,y\in N_D(Y).
\tag{2.1}
\]

The corresponding boundary in \(D/xy\) has order \(k-1\).

### Proof

A violating set containing the contracted vertex has a preimage containing
both \(x,y\) and exactly the same external boundary, a contradiction. A
violating set avoiding the contracted vertex is a set
\(Y\subseteq D-\{x,y\}\). Its boundary is unchanged unless it sees both
ends of the edge, in which case two distinct boundary vertices merge and
the order falls by exactly one. This gives (2.1). \(\square\)

## 3. Label-free splitter theorem

### Theorem 3.1 (portal splitter)

Let \(D\) be a simple three-connected, full, relatively
\(k\)-connected, \(\mathfrak F\)-free boundaried graph with
\(|D|\ge5\). Then one of the following holds.

1. There is an edge \(xy\) such that the simplification of \(D/xy\) is
   three-connected, full, relatively \(k\)-connected, and
   \(\mathfrak F\)-free.
2. There is a three-connectivity-preserving contractible edge \(xy\) and a
   tight witness \(Y\) satisfying (2.1).

If relative \(k\)-connectivity comes from a \(k\)-connected ambient graph,
then in outcome 2 every component of \(D[Y]\) is a full shore for an exact
order-\(k\) boundary.

### Proof

Tutte's contractible-edge theorem supplies an edge \(xy\) whose contraction
is three-connected, since a three-connected graph on more than four
vertices has such an edge. Lemma 1.1 preserves every forbidden portal
pattern, and row union preserves fullness. If relative
\(k\)-connectivity survives, outcome 1 holds. Otherwise Lemma 2.1 gives
outcome 2.

For a component \(K\) of \(D[Y]\), its external neighbourhood is contained
in the order-\(k\) boundary certified by (2.1). Ambient
\(k\)-connectivity forces it to meet all \(k\) boundary vertices; otherwise
at most \(k-1\) vertices separate \(K\). \(\square\)

Neither the number of labels, the demand graph, nor the target clique size
enters this theorem.

## 4. What minor-criticality adds

Let \(G\) be \(r\)-minor-critical: \(G\) is not \(r\)-colourable and
every proper minor is. Suppose \(D\) is a nonempty side with boundary
\(L\), so \(N_G(D)\subseteq D\cup L\). Let
\(\mathcal E_r(D,L)\) denote the labelled \(r\)-colourings of \(L\)
which extend to \(G[D\cup L]\). Equality partitions may be used after
quotienting by palette permutations.

### Theorem 4.1 (exact state exchange)

For every internal edge \(xy\in E(D)\),

\[
 \mathcal E_r(D/xy,L)-\mathcal E_r(D,L)\ne\varnothing.
\tag{4.1}
\]

Thus an internal contraction cannot preserve the boundary extension family
of a side of an \(r\)-minor-critical graph.

### Proof

Colour the proper minor \(G/xy\) with \(r\) colours and restrict the
colouring to \(L\), obtaining
\(\psi\in\mathcal E_r(D/xy,L)\). If
\(\psi\in\mathcal E_r(D,L)\), use an extension over the original \(D\)
and keep the minor colouring on \(G-D\). They agree label by label on
\(L\), and no edge joins \(D\) to \(G-(D\cup L)\), so they glue to an
\(r\)-colouring of \(G\), a contradiction. \(\square\)

### Corollary 4.2 (structural exchange dichotomy)

Under the simultaneous hypotheses of Theorems 3.1 and 4.1, either an exact
order-\(k\) boundary is exposed, or a contraction preserves
three-connectivity, relative \(k\)-connectivity, fullness, and all
forbidden portal obstructions while creating a genuinely new exact
boundary-colouring state.

This is what the splitter buys in a minor-critical graph. A particular
application must classify the new state or show that the exact
order-\(k\) boundary can be glued, knitted, or pumped.

## 5. Why arbitrary contraction-chain pumping is invalid

The state exchange (4.1) applies to a one-step minor of the original
critical graph. After contracting once, the whole graph is already an
\(r\)-colourable proper minor. For a chain

\[
 D=D_0\to D_1\to\cdots\to D_s,
\]

an equality

\[
 \mathcal E_r(D_i,L)=\mathcal E_r(D_j,L)
 \qquad(0<i<j)
\]

does not colour the original graph unless the repeated family also equals
\(\mathcal E_r(D_0,L)\). Hence finiteness of the state universe does not
bound an arbitrary contraction chain.

Finite-state pumping is valid for nested annuli or laminar sides retained
simultaneously inside the original graph: equal states at two boundaries,
together with clean label-preserving connectors through the region between
them, let one delete that region while preserving the original outer side.
That retained-shell hypothesis is absent from a sequence of quotient
graphs and cannot be omitted.

