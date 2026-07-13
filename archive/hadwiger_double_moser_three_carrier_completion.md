# A third root-rich carrier repairs split-negative double-Moser bodies

## 1. Setting

Use the overlapping pure-Moser notation

\[
H_1=\{x_1,x_2\},\qquad H_2=\{x_3,x_4\}.
\]

The old outer vertex \(a\) sees \(H_1\), the old outer vertex \(b\)
sees \(H_2\), the new outer vertex \(q\) sees \(H_1\), and the new
outer vertex \(p\) sees \(H_2\).  The two degree-seven centres are
\(u,v\).

The connected-split atlas is not a complete structural invariant.  This
note gives the missing direct-minor outcome: two old-to-new carriers plus
one root-rich third carrier form a \(K_7\)-minor even when every covering
split is atlas-negative.

## 2. The three-carrier certificate

### Lemma 2.1 (root-rich third carrier)

Suppose the common exterior \(C\) contains three pairwise disjoint
connected sets \(A_0,B_0,Z\) such that

\[
a\in A_0,\qquad b\in B_0,
\]

\[
E(A_0,p)\ne\varnothing,\qquad E(B_0,q)\ne\varnothing,             \tag{2.1}
\]

and

\[
                         |N_X(Z)|\ge3.                            \tag{2.2}
\]

Then \(G\) contains a \(K_7\)-minor.

#### Proof

Choose three roots met by \(Z\).  They contain one of the two literal
edges; call that edge \(yz\), and call the third root \(h\).  Use the
seven branch sets

\[
\{u\},\quad \{v\},\quad \{y\},\quad \{z\},\quad
A_0\cup\{p\},\quad B_0\cup\{q\},\quad Z\cup\{h\}.                 \tag{2.3}
\]

They are disjoint and connected by (2.1)--(2.2).  The first four form
a clique through \(uv\), the two stars, and the literal edge \(yz\).

The bag \(A_0\cup\{p\}\) sees \(u\) through \(p\), sees \(v\) through
\(a\), and sees both \(y,z\): through \(a\) when \(yz=H_1\), and
through \(p\) when \(yz=H_2\).  Similarly, \(B_0\cup\{q\}\) sees
\(u\) through \(q\), sees \(v\) through \(b\), and sees \(y,z\):
through \(q\) when \(yz=H_1\), and through \(b\) when \(yz=H_2\).
The bag \(Z\cup\{h\}\) sees \(u,v,y,z\) through its three root
contacts.

The two old-to-new bags see one another through \(ab\) (and also through
\(pq\)).  If \(h\in H_2\), then \(A_0\cup\{p\}\) sees
\(Z\cup\{h\}\) through \(ph\), while \(B_0\cup\{q\}\) sees it
through \(bh\).  If \(h\in H_1\), use \(ah\) and \(qh\),
respectively.  Thus every pair of bags in (2.3) is adjacent.
\(\square\)

There is a symmetric version obtained by interchanging \(H_1,H_2\) and
the two centre frames.  The important point is that the third carrier
need not belong to either side of a positive connected split.

## 3. A globally seven-connected split-negative architecture

The following fourteen-vertex graph proves that

\[
\text{seven-connectivity}+\text{full eight-interface}
\not\Longrightarrow \text{a quotient-positive connected split}. \tag{3.1}
\]

Take \(R=\{r_0,r_1,r_2,r_3\}\).  In addition to the fixed double-Moser
edges, give the six vertices of \(C=\{a,b\}\cup R\) the following
neighbours in \(C\cup\{v,x_1,x_2,x_3,x_4,p,q\}\):

\[
\begin{array}{c|l}
a&b,p,r_0,r_1,v,x_1,x_2\\
b&a,p,q,r_1,v,x_3,x_4\\
r_0&a,p,q,r_1,r_2,r_3,x_1\\
r_1&a,b,p,q,r_0,r_3,x_3\\
r_2&p,q,r_0,r_3,x_1,x_2,x_4\\
r_3&q,r_0,r_1,r_2,x_2,x_3,x_4
\end{array}                                                       \tag{3.2}
\]

### Proposition 3.1 (exact role of the architecture)

The graph in (3.2) has all of the following properties.

1. It is seven-connected.
2. Every nonempty proper \(Y\subset C\) satisfies

   \[
   |N_C(Y)-Y|+|N_{\{v,x_1,x_2,x_3,x_4,p,q\}}(Y)|\ge7.
   \]

3. Every covering partition \(C=C_A\dot\cup C_B\) with
   \(b\in C_A\), \(a\in C_B\), and both sides connected has one of the
   ten quotient-negative contact states from the singleton split atlas.
4. Nevertheless it has the \(K_7\)-model

   \[
   \{u\},\ \{v\},\ \{x_1\},\ \{x_2\},\
   \{a,p\},\ \{b,q\},\ \{x_4,r_2\}.                              \tag{3.3}
   \]

#### Verification

The script double_moser_one_body_counterarchitecture_verify.py is a
dependency-free direct replay.  It checks all \(6476\) deletions of at
most six vertices, all \(62\) relative shore subsets, every connected
covering split, and every bag adjacency in (3.3).  It prints

~~~text
vertex deletions checked: 6476
relative shore subsets checked: 62
connected atlas-negative covering splits checked: 5
three-carrier K7 model: verified
~~~

No graph-minor oracle is used.  \(\square\)

The architecture is therefore not a counterexample to the desired
\(K_7\)-conclusion.  It is a counterexample to the narrower strategy
that insists on finding a quotient-positive two-way split first.

## 4. Correct structural target

The one-body theorem must have at least four outcomes:

1. a quotient-positive connected \(a\)-\(b\) split;
2. a third carrier meeting any three of the four root portal classes,
   as in Lemma 2.1;
3. a direct crossed-web \(K_7\)-certificate such as the crossed
   four-cycle frame; or
4. an exact seven-cut (equivalently, the bounded-interface side of the
   web dichotomy).

Thus the next linkage theorem should not merely return two disjoint
\(A\)-to-\(P\) paths.  After choosing those paths it must inspect the
components of their complement.  A component meeting three root portal
classes as in (2.2) closes immediately; if no such component exists, the attachment
order is the data from which a two-apex web or an exact seven-cut must be
extracted.

This is a genuine structural shift from contact enumeration to
three-carrier versus web geometry.

## 5. Attachment pressure on every surviving bridge

The preceding shift has a useful quantitative consequence.

### Lemma 5.1 (four-attachment bridge pressure)

Let \(Q_a,Q_b\subseteq C\) be disjoint connected carriers with
\(a\in Q_a\), \(b\in Q_b\), where \(Q_a\) meets \(p\) and \(Q_b\)
meets \(q\).  Let \(Z\) be a component of

\[
                         C-(Q_a\cup Q_b).
\]

If \(G\) has neither a \(K_7\)-minor nor an exact seven-cut, then

\[
|N_X(Z)|\le2,\qquad
|N_{Q_a\cup Q_b}(Z)|\ge4.                         \tag{5.1}
\]

#### Proof

If \(|N_X(Z)|\ge3\), Lemma 2.1 applied to \(Q_a,Q_b,Z\) gives a
\(K_7\)-minor.  Hence the first inequality holds.

Distinct components of \(C-(Q_a\cup Q_b)\) are anticomplete.  Vertices
of \(Z\subseteq R\) have no neighbour in \(\{u,v\}\).  Therefore

\[
N_G(Z)=N_{Q_a\cup Q_b}(Z)\mathbin{\dot\cup}
       N_X(Z)\mathbin{\dot\cup}N_{\{p,q\}}(Z).       \tag{5.2}
\]

This is a genuine separator because \(u\) lies on the other side.
Seven-connectivity gives order at least seven; if its order were exactly
seven, it would be the excluded exact seven-cut.  Thus its order is at
least eight.  Since the last two terms in (5.2) have orders at most two
each, the carrier-attachment set has order at least four. \(\square\)

Thus every nonclosed component is a stable, highly attached bridge of
the two-carrier system.  The remaining theorem is no longer a vague
portal-splitting assertion: it must show that a family of
four-or-more-attachment bridges either contains a crossed frame that
lifts to one of the direct \(K_7\) certificates, or admits a Two Paths
web ordering whose facial separators expose an exact seven-cut.
