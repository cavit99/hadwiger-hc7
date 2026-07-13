# Infinite-family closures in the sole-exterior pure-Moser cell

## 1. Setup

Let $G$ be seven-connected, let $v\in V(G)$, and suppose

$$
N=N_G(v)=\{0,1,2,3,4,5,6\}
$$

induces the pure Moser spindle

$$
E(M)=\{01,02,03,04,12,16,26,34,35,45,56\}.
$$

Suppose $C=G-N[v]$ is the sole exterior component. Then $C$ is
connected and $N_G(C)=N$. This note proves that $C$ cannot be a tree if
$G$ is $K_7$-minor-free. The proof closes two infinite classes:
branching exteriors and path exteriors of arbitrary order.

## 2. Three one-defect shores

### Lemma 2.1 (Moser triangle assignment)

Let $D_1,D_2,D_3\subseteq N$, with $|D_i|\le1$. There are a triangle
$T\subseteq V(M)$ and distinct anchors

$$
x_i\in N-T-D_i\qquad(i=1,2,3)
$$

such that:

1. for $i\ne j$, it is not the case that both $x_i\in D_j$ and
   $x_j\in D_i$; and
2. if $t\in T\cap D_i$, then $tx_i\in E(M)$.

#### Proof

The four triangles of $M$ are

$$
012,\qquad034,\qquad126,\qquad345.
$$

There are eight possible sets $D_i$, including the empty set. For each
of the $8^3=512$ ordered triples, test the four triangles and the at most
$4\cdot3\cdot2=24$ ordered anchor triples outside it. The direct verifier
`moser_one_component_infinite_verify.py` checks exactly the two displayed
conditions and finds a witness in every case. No graph-minor oracle is
used in this finite check. $\square$

### Theorem 2.2 (no branching cutvertex)

If a vertex $z\in C$ has at least three components in $C-z$, then $G$
contains a $K_7$-minor.

#### Proof

Choose three components $A_1,A_2,A_3$ of $C-z$. They are connected,
pairwise anticomplete, and

$$
N_G(A_i)\subseteq N\cup\{z\}.
$$

Seven-connectivity therefore gives $|N_N(A_i)|\ge6$. Put
$D_i=N-N_N(A_i)$, so $|D_i|\le1$. Apply Lemma 2.1 and set

$$
B_i=A_i\cup\{x_i\}.
$$

Each $B_i$ is connected. For $i\ne j$, the two shores are anticomplete,
but condition 1 ensures that at least one of $A_ix_j$ and $A_jx_i$ is
present. Hence $B_i,B_j$ are adjacent. Every $B_i$ is adjacent to each
singleton $\{t\}$, $t\in T$: this is immediate unless $t\in D_i$, and
condition 2 supplies the anchor edge in that case. Thus

$$
B_1,B_2,B_3,\quad \{t\}\ (t\in T)
$$

are six disjoint, connected, pairwise adjacent bags, all meeting $N$.
Together with $\{v\}$ they form a $K_7$-model. $\square$

Consequently every cutvertex of a surviving exterior has exactly two
components behind it.

## 3. Six shores in a path

### Lemma 3.1 (path representative lemma, computer-assisted)

Let $S_1,\ldots,S_6\subseteq N$, where $|N|=7$, such that

$$
|S_1|,|S_6|\le1,\qquad
|S_i|\le2\ (2\le i\le5),\qquad
\bigcap_{i=1}^6S_i=\varnothing.
$$

Then there are distinct $x_1,\ldots,x_6\in N$ with $x_i\notin S_i$
such that, whenever $|i-j|\ge2$, it is not the case that both

$$
x_i\in S_j\quad\hbox{and}\quad x_j\in S_i.
$$

#### Certificates

It is enough to check maximal defect systems. Indeed, enlarge the two
endpoint defects to singletons and the four internal defects to pairs. If
the two endpoint singletons are distinct, their intersection is already
empty. If they are the same singleton $\{a\}$, the original
empty-intersection condition supplies an internal defect omitting $a$;
enlarge that defect while continuing to omit $a$. Thus the enlarged six
sets still have empty intersection. A representative valid for the
enlarged sets is valid for the original sets.

There are two normal forms under permutations of $N$:

1. endpoint defects $\{0\},\{1\}$ and four arbitrary pairs; and
2. endpoint defects $\{0\},\{0\}$ and four pairs not all containing $0$.

The direct verifier enumerates all pair sequences and quotients only by
boundary relabelings fixing the normalized endpoint labels. This leaves
3158 orbits in the distinct-end case and 686 in the equal-end case. It
finds and checks a valid injection for every orbit.

As an independent redundant check, the verifier also introduces the 42
Boolean membership variables $s_{i,x}$, imposes the displayed cardinality
and empty-intersection conditions, and asks for a set system for which
every injection

$$
(x_1,\ldots,x_6):[6]\hookrightarrow N
$$

is invalid. There are $7P6=5040$ injections. For each injection its
invalidity clause says either $x_i\in S_i$ for some $i$, or a
nonconsecutive pair is mutually incident. Z3 returns `unsat`. Both
exhaustive checks are reconstructed, rather than loaded from an archived
result, by `moser_one_component_infinite_verify.py`. $\square$

### Theorem 3.2 (six-shore path packing)

Let $A_1,\ldots,A_6$ be disjoint connected subgraphs outside a
seven-vertex set $N$. Suppose consecutive shores are adjacent,
nonconsecutive shores are anticomplete, and, with

$$
S_i=N-N_N(A_i),
$$

the hypotheses of Lemma 3.1 hold. Then the graph contains an
$N$-meeting $K_6$-model.

#### Proof

Take representatives $x_i$ from Lemma 3.1 and put
$B_i=A_i\cup\{x_i\}$. The bags are disjoint and connected. Consecutive
bags are adjacent through the shore edge. If $|i-j|\ge2$, the shores are
anticomplete, but the representative condition ensures that at least one
of $A_ix_j,A_jx_i$ is present. Thus the six bags are pairwise adjacent
and all meet $N$. $\square$

Unlike the earlier anticomplete-shore theorem, Theorem 3.2 permits a
path of interactions among the shores and works at the tight boundary
size seven.

### Theorem 3.3 (no path exterior of order at least six)

If $G[C]$ is a path and $|C|\ge6$, then $G$ contains a $K_7$-minor.

#### Proof

Partition the path, in its linear order, into six nonempty consecutive
subpaths $A_1,\ldots,A_6$. Put $S_i=N-N_N(A_i)$.

For $i=1,6$, the external neighbourhood of $A_i$ is contained in
$N_N(A_i)$ plus one path vertex. For $2\le i\le5$, it is contained in
$N_N(A_i)$ plus two path vertices. Each such neighbourhood separates
$A_i$ in $G$, so seven-connectivity gives

$$
|S_1|,|S_6|\le1,\qquad |S_i|\le2\quad(2\le i\le5).
$$

Moreover, $N_G(C)=N$, so $\bigcap_iS_i=\varnothing$. The six subpaths
satisfy Theorem 3.2 and therefore give an $N$-meeting $K_6$-model.
Adding $\{v\}$ gives a $K_7$-model. $\square$

## 4. Infinite-family consequence

### Corollary 4.1 (the exterior contains a cycle)

In the sole-exterior pure-Moser cell of a hypothetical minimal
counterexample, $C$ is not a tree.

#### Proof

The certified order-four and order-five theorems already give
$|C|\ge6$. If a tree $C$ has a vertex of degree at least three,
Theorem 2.2 applies. Otherwise the connected tree is a path, and
Theorem 3.3 applies. $\square$

This is a non-enumerative closure of every tree exterior, of arbitrary
order. It does not eliminate exteriors containing a cycle. In a
surviving exterior, every cutvertex has precisely two components behind
it, and at least one nontrivial 2-connected block remains.

## 5. Reproduction

Run

```text
PYTHONPATH=.deps python3 moser_one_component_infinite_verify.py
```

The expected output is

```text
branching cases verified: 512
path maximal-system orbits verified directly: 3158 distinct-end + 686 equal-end
path injections excluded in counterexample encoding: 5040
path representative counterexample formula: UNSAT
```
