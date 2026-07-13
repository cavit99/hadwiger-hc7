# Two components behind the old outer edge close the double-Moser re-root

## 1. Setting

Let (G) be seven-connected.  Let (u,v) be adjacent degree-seven
vertices whose neighbourhoods are overlapping pure Moser spindles.  Use

\[
X=\{x_1,x_2,x_3,x_4\},\qquad A=\{a,b\},\qquad P=\{p,q\},
\]

and suppose

\[
N(u)=\{v\}\mathbin{\dot\cup}X\mathbin{\dot\cup}P,
\qquad
N(v)=\{u\}\mathbin{\dot\cup}X\mathbin{\dot\cup}A.       \tag{1.1}
\]

After interchanging the two literal edges if necessary, the fixed core
edges, in addition to the stars at (u) and (v), are

\[
x_1x_2, x_3x_4, ab, pq,
\]

\[
ax_1,ax_2,bx_3,bx_4,
\qquad qx_1,qx_2,px_3,px_4.                    \tag{1.2}
\]

Put

\[
W=X\mathbin{\dot\cup}P.
\]

Assume that (C=G-N[u]) is the sole exterior component, as supplied by
the singleton re-rooting.  It contains the old outer edge (ab), and

\[
N_C(v)=\{a,b\}.                                  \tag{1.3}
\]

This note proves that (C-\{a,b\}) is connected in a
(K_7)-minor-free graph.

## 2. Every component has one of nine profiles

Let (D) be a component of (C-A), and define

\[
A_D=N_A(D),\qquad S_D=W-N_W(D).                  \tag{2.1}
\]

### Lemma 2.1

Every such component satisfies

\[
1\le |A_D|\le2,
\qquad
|S_D|\le |A_D|-1.                                \tag{2.2}
\]

Hence its conservative contact profile is one of the following nine:

\[
\begin{array}{c|c|c}
\text{profile}&A_D&S_D\\ \hline
A&\{a\}&\varnothing\\
B&\{b\}&\varnothing\\
F&\{a,b\}&\varnothing\\
1,2,3,4,P,Q&\{a,b\}&
 \{x_1\},\{x_2\},\{x_3\},\{x_4\},\{p\},\{q\}
\end{array}                                      \tag{2.3}
\]

Here a component with surplus contacts may be replaced by one of the
listed conservative profiles by deleting edges.

#### Proof

The connectedness of (C) implies (A_D\ne\varnothing).  Distinct
components of (C-A) are anticomplete.  The degree-seven vertices
(u,v) have no neighbour in (D).  Therefore

\[
N_G(D)=A_D\cup N_W(D).                            \tag{2.4}
\]

The vertex (u) lies outside (D\cup N_G(D)), so (2.4) is a genuine
separator.  Seven-connectivity yields

\[
7\le |N_G(D)|=|A_D|+6-|S_D|,
\]

which is (2.2).  If (A_D) has one vertex, (S_D) is empty.  If it has
two vertices, (S_D) has order at most one.  This gives (2.3).
\(\square\)

The distinction between profiles (A,B) and (F) is essential: one
may not add a fictitious second (A)-portal to a component.

## 3. The explicit 81-profile atlas

Contract two distinct components (D_1,D_2) to labelled vertices
(r_1,r_2), and delete every contact not required by their conservative
profiles.  The following nine branch-set templates are used.  A plus
sign denotes the union inside one bag.

\[
\begin{array}{c|l}
1&u\mid x_1\mid x_2\mid v{+}x_3\mid p{+}r_1\mid q{+}r_2\mid x_4{+}a{+}b\\
2&u\mid x_1\mid x_2\mid v{+}x_3\mid q{+}r_1\mid p{+}r_2\mid x_4{+}a{+}b\\
3&u\mid x_3\mid x_4\mid v{+}x_2\mid p{+}r_1\mid q{+}r_2\mid x_1{+}a{+}b\\
4&u\mid x_3\mid x_4\mid v{+}x_1\mid q{+}r_1\mid p{+}r_2\mid x_2{+}a{+}b\\
5&u\mid x_3\mid x_4\mid v{+}x_1\mid p{+}r_1\mid q{+}r_2\mid x_2{+}a{+}b\\
6&u\mid x_1\mid x_2\mid v{+}x_4\mid p{+}r_1\mid q{+}r_2\mid x_3{+}a{+}b\\
7&u\mid x_1\mid x_2\mid v{+}x_4\mid q{+}r_1\mid p{+}r_2\mid x_3{+}a{+}b\\
8&u\mid x_3\mid x_4\mid v{+}x_2\mid q{+}r_1\mid p{+}r_2\mid x_1{+}a{+}b\\
9&v\mid x_1\mid x_2\mid u{+}x_3\mid a{+}r_1\mid b{+}r_2\mid x_4{+}p{+}q
\end{array}                                                        \tag{3.1}
\]

Rows and columns in the next table are ordered

\[
A,B,F,1,2,3,4,P,Q.
\]

The entry is the number of the valid template in (3.1).

\[
\begin{array}{c|ccccccccc}
 &A&B&F&1&2&3&4&P&Q\\ \hline
A&1&1&1&1&1&2&1&1&2\\
B&1&1&1&1&1&2&1&1&2\\
F&1&1&1&1&1&2&1&1&2\\
1&2&2&2&3&4&2&2&3&2\\
2&2&2&2&5&5&2&2&5&2\\
3&1&1&1&1&1&6&1&1&7\\
4&1&1&1&1&1&2&1&1&2\\
P&2&2&2&8&4&2&2&9&2\\
Q&1&1&1&1&1&6&1&1&9
\end{array}                                                        \tag{3.2}
\]

### Lemma 3.1 (two-component portal atlas)

For every ordered pair of profiles in (2.3), the seven bags selected by
(3.2) are disjoint, connected, and pairwise adjacent.  Hence the
conservative quotient contains a (K_7)-minor.

#### Verification

The script `double_moser_two_component_portal_atlas.py` constructs the
fixed double-Moser core, constructs each of the (9^2=81) conservative
profile pairs, selects the displayed template, and directly checks:

1. all seven bags are nonempty and pairwise disjoint;
2. every bag is connected; and
3. every pair of bags has an edge between it.

It contains no graph-minor search and no external dependency.  Its output
is

```text
explicit two-component portal profiles verified: 81/81
template usage: 1:42 2:26 3:2 4:2 5:3 6:2 7:1 8:1 9:2
```

Every contracted bag (r_i) lifts by replacing it with the original
connected component (D_i).  All quotient incidences are genuine
component-to-boundary contacts from its profile.  Therefore every one of
the 81 certificates lifts to (G).  \(\square\)

As a readable example, if (D_1) misses a root in
(\{x_1,x_2\}) and (D_2) misses a root in
(\{x_3,x_4\}), template 2 is the uniform model

\[
\{u\},\ \{x_1\},\ \{x_2\},\ \{v,x_3\},\
\{q\}\cup D_1,\ \{p\}\cup D_2,\ \{x_4,a,b\}.   \tag{3.3}
\]

Both components necessarily meet (a,b) in this case, by Lemma 2.1.

## 4. Structural closure

### Theorem 4.1

In the overlapping-pure-Moser singleton re-rooting, if \(G\) has no
\(K_7\)-minor, then

\[
             R:=C-\{a,b\}\text{ is nonempty and connected}.        \tag{4.1}
\]

#### Proof

If \(R\) were empty, the old Moser incidences would give

\[
N(a)\subseteq\{v,b,x_1,x_2,p,q\},
\]

so \(d(a)\le6\), contrary to seven-connectivity.  Thus
\(R\ne\varnothing\).  If it had two components, Lemma 2.1 would assign
each a profile in (2.3), and Lemma 3.1 would give a \(K_7\)-minor.
Additional components and surplus contacts may be deleted.  \(\square\)

The overlap also forces an order bound.

### Lemma 4.2 (the common body has order at least three)

\[
                              |R|\ge3.                             \tag{4.2}
\]

If equality holds, each of

\[
\{u,v,a,q\}\cup R,\qquad \{u,v,b,p\}\cup R                         \tag{4.3}
\]

is an exact seven-cut.

#### Proof

The set \(\{u,v,a,q\}\cup R\) separates the literal edge
\(\{x_1,x_2\}\) from the nonempty set \(\{x_3,x_4,b,p\}\).  Indeed,
the vertices \(x_1,x_2\) have no neighbours outside their literal edge
except \(u,v,a,q\) and vertices of \(R\).  Seven-connectivity therefore
gives \(4+|R|\ge7\).  Equality makes the displayed separator an exact
seven-cut.  The second assertion follows symmetrically.  \(\square\)

Equation (2.4) gives the exact remaining dichotomy.

### Corollary 4.3 (seven-cut or eight-interface body)

Either

\[
|N_G(R)|=7,                                          \tag{4.4}
\]

in which case \(N_G(R)\) is an exact seven-cut, or

\[
N_G(R)=A\cup W,\qquad |N_G(R)|=8.                   \tag{4.5}
\]

Indeed, (2.2) leaves only profile \(F\) as the order-eight case.

Thus the multi-component branch is completely closed.  A cut-irreducible
double-Moser re-root consists of the old outer edge \(ab\) together with
one connected body \(R\) that meets both \(a,b\) and all six labels of
\(W\).  The remaining problem is not another shore count: it is to split
this one eight-interface body (necessarily of order at least four after
the exact order-three cuts in (4.3) have been descended through) into the
two portal-distributed carriers
required by the cross-saturated split lemma, or to expose a new exact
seven-cut.

## 5. Scope

The theorem uses only seven-connectivity, the two exact degree-seven
Moser neighbourhoods, and the sole-exterior conclusion of the singleton
re-rooting.  It does not assume that a contracted contact can be split
inside one connected body.  That distinction is precisely why (4.5)
remains.
