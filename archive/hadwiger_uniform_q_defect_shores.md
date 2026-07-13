# Uniform \(q\)-defect shore packing

## 1. Incidence-free representatives

Let \(S_1,\ldots,S_m\) be subsets of a finite set \(N\), with
\(|S_i|\le q\).  Call distinct vertices \(x_1,\ldots,x_m\in N\)
**incidence-free representatives** if

\[
x_i\notin S_i
\]

for every \(i\), and there are no distinct \(i,j\) for which both

\[
x_i\in S_j\qquad\text{and}\qquad x_j\in S_i.
\]

### Theorem 1

If

\[
|N|\ge m+q^2,
\]

then \(S_1,\ldots,S_m\) have incidence-free representatives.

### Proof

Choose the representatives greedily in the order
\(S_1,\ldots,S_m\).  Suppose that \(x_1,\ldots,x_{i-1}\) have already
been chosen.  Put

\[
J_i=\{j<i:x_j\in S_i\},\qquad h=|J_i|.
\]

Choose \(x_i\) outside

\[
F_i=\{x_1,\ldots,x_{i-1}\}\cup S_i
       \cup\bigcup_{j\in J_i}S_j.                       \tag{1}
\]

Such a choice is unused and avoids \(S_i\).  Moreover, if \(j<i\) and
\(x_j\in S_i\), then \(j\in J_i\), so (1) ensures \(x_i\notin S_j\).
Thus no mutual incidence is created.

It remains to count the forbidden vertices.  The \(h\) distinct
representatives indexed by \(J_i\) lie in both
\(\{x_1,\ldots,x_{i-1}\}\) and \(S_i\).  Therefore

\[
\begin{aligned}
|F_i|
&\le (i-1)+q-h+hq\\
&=i-1+q+h(q-1)\\
&\le i-1+q^2\\
&\le m-1+q^2<|N|.
\end{aligned}
\]

Hence \(N-F_i\) is nonempty at every step, and the greedy construction
succeeds. \(\square\)

The overlap term \(-h\) is important: the cruder count gives
\(m+q+q^2\), while the exact count removes the full additive \(q\).

## 2. Shore-packing consequence

### Theorem 2

Let \(C_1,\ldots,C_m\) be pairwise vertex-disjoint, pairwise anticomplete
connected subgraphs of a graph \(G\), and let \(N\) be disjoint from all
of them.  Suppose each
\(C_i\) is adjacent to all but at most \(q\) vertices of \(N\).  If

\[
|N|\ge m+q^2,
\]

then \(G\) contains an \(N\)-meeting \(K_m\)-model.

### Proof

Let

\[
S_i=N-N_G(C_i).
\]

Apply Theorem 1 and take incidence-free representatives \(x_i\).
Set

\[
B_i=C_i\cup\{x_i\}.
\]

Each \(B_i\) is connected because \(x_i\notin S_i\), and the bags are
disjoint.  If \(B_i\) and \(B_j\) had no edge between them, then
\(C_i\) would miss \(x_j\) and \(C_j\) would miss \(x_i\).  Thus
\(x_j\in S_i\) and \(x_i\in S_j\), contrary to incidence-freeness.
Hence the \(B_i\) are pairwise adjacent connected bags, and each meets
\(N\). \(\square\)

In particular, if \(N=N_G(v)\) and \(m=t-1\), the additional singleton
bag \(\{v\}\) turns this model into a \(K_t\)-minor.  This advances the
uniform model-meeting obstruction whenever the available pieces are
pairwise anticomplete connected shores with bounded boundary defect.  It
does not assert that an arbitrary unrooted \(K_{t-1}\)-model has this
shore form.

## 3. The bound \(m+q\) is false

Let

\[
N=A\mathbin{\dot\cup}B,\qquad |A|=|B|=3,
\]

and take

\[
S_1=S_2=A,\qquad S_3=B.
\]

Here \(m=q=3\) and \(|N|=6=m+q\).  Any representatives for rows 1 and 2
must lie in \(B\), while a representative for row 3 must lie in \(A\).
Consequently, for each \(i\in\{1,2\}\),

\[
x_i\in S_3\qquad\text{and}\qquad x_3\in S_i.
\]

Thus every possible system of distinct valid representatives contains a
mutual incidence.  The proposed general threshold \(|N|\ge m+q\) is
therefore false already at \(q=3\).

For comparison, the special rank-two theorem proved in
hadwiger_degree8_degree9_exterior_bounds.md gives the much sharper bound
\(|N|\ge m+2\) when \(q=2\).  Its proof uses the graph structure of
two-element defects and a three-edge rotation; that mechanism does not
extend automatically to \(q\ge3\), as the example above demonstrates.
