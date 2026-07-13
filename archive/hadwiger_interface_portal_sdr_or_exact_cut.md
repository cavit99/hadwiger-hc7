# A \(k+1\)-interface has distinct portals or an exact \(k\)-cut

### Theorem 1 (portal SDR-or-cut)

Let \(G\) be \(k\)-connected. Let \(R\) be a nonempty connected vertex
set whose external neighbourhood is contained in a set \(I\) of order
\(k+1\), and assume every vertex of \(I\) has a neighbour in \(R\).
If

\[
                         |R|\ge k+1,
\]

then at least one of the following conclusions holds:

1. the \(k+1\) portal sets
   \[
                     P_s=N_R(s)\qquad(s\in I)
   \]
   have a system of distinct representatives; or
2. a nonempty connected proper subset of \(R\) lies behind an exact
   \(k\)-cut.

#### Proof

Suppose Hall's condition fails. There is a nonempty set \(J\subseteq I\)
such that

\[
             U:=\bigcup_{s\in J}P_s,\qquad |U|\le |J|-1.          \tag{1.1}
\]

Because \(|R|\ge k+1=|I|\ge|J|>|U|\), the set \(R-U\) is nonempty.
Let \(D\) be one of its components. By the definition of \(U\), no
vertex of \(D\) is adjacent to a member of \(J\). All neighbours of
\(D\) outside \(R\) lie in \(I\), while its neighbours in \(R-D\)
lie in \(U\). Hence

\[
                         N_G(D)\subseteq U\cup(I-J).              \tag{1.2}
\]

The right side has order at most

\[
             (|J|-1)+(k+1-|J|)=k.                               \tag{1.3}
\]

It is a genuine separator: \(D\) is on one side and every member of
\(J\) is on the other. \(k\)-connectivity forces equality throughout
(1.2)--(1.3). Thus \(N_G(D)\) is an exact \(k\)-cut. Since
\(U\ne R\), the connected set \(D\) is a proper subset of \(R\).
\(\square\)

### Corollary 2 (double-Moser body)

In the cut-irreducible double-Moser endpoint, if the eight-interface
body \(R\) has order at least eight, its eight interface portal classes
have distinct representatives.

This is label-free and scales with the connectivity. It supplies the
terminal normalization needed before applying a generalized Two Paths
or rooted-biclique theorem; any Hall obstruction is already one of the
exact adhesions allowed by the structural descent.
