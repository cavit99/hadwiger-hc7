# Degree-eight and degree-nine exterior-component bounds for \(\mathrm{HC}_7\)

## 1. Result

Let \(G\) be a 7-connected graph and let \(v\in V(G)\).  Put
\(N=N_G(v)\), and call the components of \(G-N[v]\) the **exterior
components at \(v\)**.

This note proves the following two concrete minor certificates.

### Theorem 1 (degree eight)

Suppose \(d(v)=8\) and
\[
\alpha(G[N])\leq 3.
\]
If \(G-N[v]\) has at least four components, then \(G\) contains a
\(K_7\)-minor.

### Theorem 2 (degree nine)

Suppose \(d(v)=9\) and \(\alpha(G[N])\le4\).  If \(G-N[v]\) has at least
five components, then \(G\) contains a \(K_7\)-minor.

Consequently, in a minor-minimal counterexample to \(\mathrm{HC}_7\), a
degree-eight vertex has at most three exterior components and a degree-nine
vertex has at most four exterior components.  The needed inequalities
\(\alpha(G[N(v)])\leq3\) and \(\alpha(G[N(v)])\leq4\), respectively, are
the two instances of Dirac's neighborhood inequality
\(\alpha(G[N(v)])\leq d(v)-7+2\).

Both theorems give the branch sets explicitly.  No coloring theorem, rooted
minor theorem, or unproved model-meeting assertion is used.

---

## 2. The common boundary observation

### Lemma 3 (large attachment)

If \(C\) is an exterior component at \(v\), then
\[
|N_G(C)|\geq7.
\]

#### Proof

Every neighbor of \(C\) outside \(C\) belongs to \(N\).  The set
\(N_G(C)\) separates the nonempty set \(C\) from \(v\).  Seven-connectivity
therefore gives \(|N_G(C)|\geq7\). \(\square\)

Thus a component at a degree-eight vertex misses at most one boundary
vertex, while a component at a degree-nine vertex misses at most two.

---

## 3. One-miss component certificates

We first prove the finite lemma that contains all of the degree-eight work.

### Lemma 4 (four one-miss shores)

Let \(A\) be a graph on an eight-element vertex set \(N\), with
\(\alpha(A)\leq3\).  Let \(C_1,\ldots,C_4\) be pairwise disjoint connected
graphs with no edges between distinct \(C_i\)'s.  Suppose that, for every
\(i\), there is a vertex \(m_i\in N\) such that
\[
N\setminus\{m_i\}\subseteq N_G(C_i).
\]
Then there is a \(K_6\)-model all six of whose branch sets meet \(N\).

#### Proof

Let \(M=\{m_1,\ldots,m_4\}\).  Since \(|N\setminus M|\ge4\) and
\(\alpha(A)\le3\), choose adjacent vertices
\(y,z\in N\setminus M\).  Put \(W=N\setminus\{y,z\}\), so \(|W|=6\).

There are distinct \(x_1,\ldots,x_4\in W\) such that \(x_i\ne m_i\) and
there is no directed 2-cycle \(x_i=m_j,x_j=m_i\).  To see this, let \(r\)
be the number of distinct missed vertices.  If \(r=1\), use any four of the
five vertices of \(W\setminus M\).  If \(r=2\), assign one row missing the
first missed vertex to the second, and assign the other three rows to three
vertices outside \(M\).  If \(r\ge3\), assign one row for each missed vertex
cyclically to the next missed vertex, and assign all remaining rows
injectively outside \(M\).  There are \(6-r\ge4-r\) vertices available for
the latter assignment.

The six sets
\[
\{y\},\quad\{z\},\quad C_i\cup\{x_i\}\quad(1\le i\le4)
\]
are connected, disjoint, pairwise adjacent, and all meet \(N\).  The only
possible failure of adjacency between two component bags would be a directed
2-cycle of the excluded kind. \(\square\)

The following slightly stronger certificate, although no longer needed for
the sharp component count in Theorem 1, is also useful.

### Lemma 5 (five one-miss shores)

Let \(A\) be a graph on an eight-element vertex set \(N\), with
\(\alpha(A)\leq3\).  Let \(C_1,\ldots,C_5\) be pairwise disjoint connected
graphs with no edges between distinct \(C_i\)'s.  Suppose that, for every
\(i\), there is a vertex \(m_i\in N\) such that
\[
N\setminus\{m_i\}\subseteq N_G(C_i).
\]
Then the graph on \(N\cup C_1\cup\cdots\cup C_5\) contains a \(K_7\)-minor.

#### Proof

Write \(M=\{m_1,\ldots,m_5\}\), as a set, and put \(r=|M|\).

First suppose either \(r\leq4\), or \(r=5\) and the three vertices of
\(N\setminus M\) are not independent.  In either case there are adjacent
vertices
\[
y,z\in N\setminus M.
\]
Indeed, when \(r\leq4\), the set \(N\setminus M\) has at least four vertices
and cannot be independent because \(\alpha(A)\leq3\).

Set \(W=N\setminus\{y,z\}\), so \(|W|=6\).  We claim that there are distinct
vertices \(x_1,\ldots,x_5\in W\) such that

1. \(x_i\ne m_i\) for every \(i\); and
2. there are no distinct \(i,j\) for which simultaneously
   \(x_i=m_j\) and \(x_j=m_i\).

Here is an explicit allocation.  If \(r=1\), use any five vertices of
\(W\setminus M\).  If \(r=2\), with \(M=\{a,b\}\), assign \(b\) to one row
whose missed vertex is \(a\), and assign the other four rows bijectively to
the four vertices of \(W\setminus\{a,b\}\).  If \(r\geq3\), cyclically order
the distinct missed vertices \(a_1,\ldots,a_r\), choose one row missing each
\(a_j\), and assign that row \(a_{j+1}\), with indices modulo \(r\).  Assign
the remaining \(5-r\) rows injectively into \(W\setminus M\), which has
\(6-r\) vertices.  A directed cycle of length at least three has no directed
2-cycle, so the two asserted properties hold.

Now take the seven branch sets
\[
\{y\},\quad \{z\},\quad C_i\cup\{x_i\}\quad(1\leq i\leq5).
\]
Each is connected because \(x_i\ne m_i\).  The singleton bags are adjacent.
They are adjacent to every other bag because neither \(y\) nor \(z\) is a
missed vertex.  Finally, two bags \(C_i\cup\{x_i\}\) and
\(C_j\cup\{x_j\}\) could fail to have a cross-edge only if
\(x_j=m_i\) and \(x_i=m_j\), which the allocation forbids.  Hence these are
the branch sets of a \(K_7\)-model.

It remains to handle \(r=5\) when
\[
T:=N\setminus M
\]
is an independent triple.  The five missed vertices are now distinct, so
label the component missing \(m\) by \(C_m\).  Every \(m\in M\) has a
neighbor in \(T\), since otherwise \(T\cup\{m\}\) would be an independent
set of order four.  Also \(A[M]\) has an edge, since \(|M|=5>\alpha(A)\).
Choose an edge \(zw\in E(A[M])\), and choose a neighbor \(y\in T\) of
\(z\).  Write
\[
T\setminus\{y\}=\{p,q\},\qquad
M\setminus\{z,w\}=\{a,b,c\}.
\]
Use the seven branch sets
\[
\{y\},\quad\{z\},\quad
C_z\cup\{w\},\quad
C_w\cup\{p\},\quad
C_a\cup\{q\},\quad
C_b\cup\{a\},\quad
C_c\cup\{b\}.
\]
All are connected.  The singleton \(y\) is adjacent to every component bag,
because \(y\notin M\).  Every component bag other than the one rooted at
\(C_z\) is adjacent to \(z\), and \(C_z\cup\{w\}\) is adjacent to \(z\)
through the edge \(wz\).  Among the five component bags, the assignment
arcs are
\[
z\to w,\qquad b\to a,\qquad c\to b,
\]
with the other two assigned vertices outside \(M\); there is no directed
2-cycle.  The same cross-edge check as above proves pairwise adjacency.
Thus these seven sets form a \(K_7\)-model. \(\square\)

### Proof of Theorem 1

Choose four exterior components.  By Lemma 3, each has at least seven
neighbors in the eight-element set \(N\).  If a component has eight
neighbors, choose an arbitrary \(m_i\) and simply ignore its edge to
\(m_i\).  Lemma 4 gives an \(N\)-meeting \(K_6\)-model in \(G-v\).  The
singleton branch set \(\{v\}\) is adjacent to all six bags and completes a
\(K_7\)-model. \(\square\)

---

## 4. A two-miss representative theorem

The degree-nine result rests on the following independent combinatorial
lemma.  Parallel edges are allowed in the auxiliary multigraph.

### Lemma 6 (incidence-free representatives)

Let \(m\geq3\), let \(F\) be a loopless multigraph with \(m\) labeled edges
on a vertex set \(X\) of order \(m+2\).  There is an injective map
\[
f:E(F)\longrightarrow X
\]
such that

1. \(f(e)\notin e\) for every edge \(e\); and
2. for no two distinct edges \(e,g\) do both \(f(e)\in g\) and
   \(f(g)\in e\) hold.

#### Proof

We induct on \(m\).

For \(m=3\), first suppose that \(F\) has an isolated vertex \(p\).  Of the
three edges, choose an edge \(e\) such that the other two edges \(g,h\)
intersect.  Such a choice exists: otherwise all three pairs of edges would be
disjoint, requiring six nonisolated vertices.  Set \(f(e)=p\).  If \(g,h\)
are parallel, assign to them the two vertices of \(X\setminus(g\cup\{p\})\).
If \(g=ab\) and \(h=ac\) with \(b\ne c\), set \(f(g)=c\) and set \(f(h)\)
equal to the unique vertex of \(X\setminus\{p,a,b,c\}\).  These assignments
have the required properties.

If \(F\) has no isolated vertex, its three edges cover all five vertices.
It is therefore a two-edge path \(ab,bc\) together with a disjoint edge
\(de\).  The assignment
\[
f(ab)=d,\qquad f(de)=c,\qquad f(bc)=a
\]
is a directed incidence cycle of length three and satisfies the conclusion.

Now let \(m\geq4\), and assume the result for \(m-1\).  If \(F\) has an
isolated vertex \(p\), remove \(p\) and any edge \(e\), apply induction, and
set \(f(e)=p\).  This creates no incidence in either direction.

We may therefore assume that \(F\) has no isolated vertex.  Its average
degree is \(2m/(m+2)<2\), so it has a vertex \(p\) of degree one.  Let its
unique incident edge be \(e=pq\).  Delete \(p\) and \(e\), and apply the
induction hypothesis to the resulting \((m-1)\)-edge multigraph on
\((m-1)+2\) vertices.  Let \(r,s\) be the two vertices not used as
representatives by the resulting map \(f'\).

If one of \(r,s\), say \(u\), can be assigned to \(e\) without creating a
2-cycle, do so.  Notice that if \(q\in\{r,s\}\), the other unused vertex
always works, because no edge has representative \(q\).  Hence the only
failure is the following configuration: \(q\notin\{r,s\}\), the unique edge
\(g\) with \(f'(g)=q\) is \(g=rs\), and both choices \(r,s\) conflict with
that same edge.

In this exceptional configuration, choose an edge \(h\ne g\) that is not
parallel to \(g\).  Such an edge exists.  Indeed, since \(m+2\geq6\), there
is a vertex outside \(\{p,q,r,s\}\), and the assumption that \(F\) has no
isolated vertices gives an incident edge \(h\), which cannot be \(pq\) or
parallel to \(rs\).  Choose
\[
u\in\{r,s\}\setminus h
\]
and put \(a=f'(h)\).  Replace the three assignments by
\[
f(e)=u,\qquad f(g)=a,\qquad f(h)=p,
\]
leaving every other assignment unchanged.

These representatives are distinct and are not incident with their assigned
edges: \(u\notin pq\), \(a\notin rs\) because \(r,s\) were unused, and
\(p\notin h\) because \(p\) has degree one.  There is no new 2-cycle with an
unchanged edge.  For \(e\), such a cycle would need an unchanged edge with
representative \(p\) or \(q\), but no such edge remains.  For \(g\), it would
need an unchanged representative in \(\{r,s\}\), but these were unused.  For
\(h\), it would need an unchanged edge incident with \(p\), and only \(e\)
is incident with \(p\).  Among the three changed edges: \(a\ne p,q\), so
\(e,g\) do not form a 2-cycle; the choice \(u\notin h\) excludes a 2-cycle
between \(e,h\); and \(a=f'(h)\notin h\) excludes one between \(g,h\).
This completes the induction. \(\square\)

### Corollary 7 (uniform two-defect shore packing)

Let \(m\ge3\), let \(N\) be a vertex set with \(|N|\ge m+2\), and let
\(C_1,\ldots,C_m\) be pairwise disjoint connected subgraphs with no edges
between distinct \(C_i\)'s.  If each \(C_i\) is adjacent to all but at most
two vertices of \(N\), then there is an \(N\)-meeting \(K_m\)-model with
branch sets
\[
C_i\cup\{x_i\}\qquad(1\le i\le m)
\]
for distinct vertices \(x_i\in N\).

#### Proof

Choose \(X\subseteq N\) with \(|X|=m+2\).  Enlarge the set of vertices of
\(X\) missed by \(C_i\), if necessary, to a two-element set \(e_i\).  Apply
Lemma 6 to the labeled multigraph with edge set \(e_1,\ldots,e_m\), and put
\(x_i=f(e_i)\).  Connectivity and disjointness are immediate.  If two bags
had no cross-edge, then both \(x_j\in e_i\) and \(x_i\in e_j\), contrary to
Lemma 6. \(\square\)

### Proof of Theorem 2

Choose five exterior components \(C_1,\ldots,C_5\).  Enlarge the set of
boundary vertices missed by each component to a two-element set
\(e_i\subseteq N\), and view \(e_1,\ldots,e_5\) as the labeled edges of a
multigraph \(F\) on the nine-element set \(N\).

If \(F\) has an isolated vertex \(y\), choose any seven-element set
\(X\subseteq N\setminus\{y\}\).  Lemma 6, applied to the five miss sets
restricted to and enlarged inside \(X\), gives five pairwise adjacent
connected bags \(C_i\cup\{x_i\}\).  All five bags are adjacent to the
singleton \(\{y\}\), because no component misses \(y\).  These six bags form
an \(N\)-meeting \(K_6\)-model, which \(\{v\}\) extends to a \(K_7\)-model.

Suppose instead that \(F\) has no isolated vertex.  Five edges have total
degree ten and cover all nine vertices.  Hence the degree sequence is
\((2,1,1,1,1,1,1,1,1)\), and
\[
F\cong P_3\mathbin{\dot\cup}3K_2.
\]
In particular, eight vertices are leaves of \(F\).  There is a leaf \(y\)
of \(F\) with a neighbor \(x\) in \(A=G[N]\) outside the unique edge
\(yz\in E(F)\) incident with \(y\).  Indeed, if every leaf had neighbors in
\(A\) only within its unique incident edge of \(F\), then every edge of
\(A\) would be an edge of \(F\).  But
\[
\alpha(F)=2+3=5,
\]
so \(A\subseteq F\) would imply \(\alpha(A)\ge5\), contrary to Dirac's
inequality \(\alpha(A)\le4\) for a degree-nine vertex.

Let \(C_i\) be the component whose enlarged miss set is \(e_i=\{y,z\}\),
and take
\[
B_i=C_i\cup\{x\}.
\]
This bag is connected, meets \(N\), and is adjacent to \(y\) through the
edge \(xy\).  Put
\[
X=N\setminus\{y,z,x\},
\]
so \(|X|=6\).  Apply Lemma 6 with \(m=4\) to the other four components,
after restricting and enlarging their miss sets inside \(X\).  This gives
four pairwise adjacent bags \(B_j=C_j\cup\{x_j\}\).  Each is adjacent to
\(B_i\), because \(x_j\notin\{y,z\}\) and hence \(C_i\) is adjacent to
\(x_j\).  Each is adjacent to \(\{y\}\), because the leaf \(y\) belongs to
no miss edge other than \(e_i\).  Therefore
\[
\{y\}, B_1,\ldots,B_5
\]
is an \(N\)-meeting \(K_6\)-model.  Adding \(\{v\}\) completes a
\(K_7\)-model. \(\square\)

---

## 5. Exact residual left by these lemmas

### Subsequent strengthening

The bounds in this section were the state before the finite-boundary
color-gluing arguments in
`hadwiger_degree8_three_component_closure.md` and
`hadwiger_degree9_four_component_closure.md`.  Those independently
verified arguments improve the conclusions to

\[
d(v)=8\Longrightarrow \#\operatorname{comp}(G-N[v])\le2,
\]

and

\[
d(v)=9\Longrightarrow \#\operatorname{comp}(G-N[v])\le3.
\]

The original bounds and proofs below remain useful as the first packing
step.

For a hypothetical minor-minimal counterexample to \(\mathrm{HC}_7\):

* at a degree-eight vertex, \(G-N[v]\) has between one and three components;
* at a degree-nine vertex, \(G-N[v]\) has between one and four components.

The lower bound of one uses the counterexample package and the already known
\(\mathrm{HC}_6\): if \(G=N[v]\), then \(v\) is universal, while
\(\chi(G-v)=6\).  Hence \(G-v\) has a \(K_6\)-minor, and adjoining the
singleton branch set \(\{v\}\) gives a \(K_7\)-minor.  The two theorems above
only need the upper bounds.

The remaining higher-degree problem is therefore no longer an unbounded
exterior-component packing problem.  It is a bounded-shore problem: at most
three almost-complete shores for degree eight, and at most four two-defect
shores for degree nine.  Closing those bounded cells still requires coloring
criticality or rooted-model surgery; the component bounds alone do not prove
\(\mathrm{HC}_7\).
