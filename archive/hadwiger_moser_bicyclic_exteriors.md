# Elimination of every bicyclic sole exterior behind a Moser boundary

## 1. Six-shore packing

Let $N=\{0,1,2,3,4,5,6\}$ induce the pure Moser spindle.

### Theorem 1.1 (bicyclic shore packing, computer-assisted)

Let $Q$ be any simple connected graph on six vertices with seven edges.
Let $A_1,\ldots,A_6$ be disjoint connected shores representing every
edge of $Q$. Suppose

$$
|N-N_N(A_i)|\le d_Q(i)
$$

for each $i$, and suppose the shores collectively see every vertex of
$N$. Then the graph contains an $N$-meeting $K_6$-model.

#### Proof certificate

There are nineteen unlabelled connected seven-edge graphs on six
vertices. For each, contract the shores to helpers. The 42 optional
helper-boundary incidences satisfy row lower bounds $7-d_Q(i)$ and full
column coverage.

The archive contains 28,575 explicit six-bag models over the nineteen
types. Each record lists only optional incidences needed for its bag
trees and pairwise adjacencies. `moser_bicyclic_shore_verify.py`
independently enumerates all nineteen graph-atlas types, checks every
model using only its recorded edges, reconstructs every Boolean system,
and verifies all nineteen as `unsat`. Expanding helpers back to connected
shores proves the theorem. $\square$

## 2. Safe contraction to six shores

Write the cyclomatic number of a connected graph as

$$
\rho(C)=|E(C)|-|V(C)|+1.
$$

### Lemma 2.1 (nontriangle edge)

If $C$ is a simple connected bicyclic graph of order greater than six,
then $C$ has an edge contained in no triangle.

#### Proof

Suppose every edge lies in a triangle. Then there is no bridge. The
cycle ranks of the nontrivial blocks sum to two.

If there are two cyclic blocks, each has cycle rank one and hence is a
cycle. Since all its edges lie in triangles, each block is a triangle.
The two triangles meet at one cutvertex, so $|C|=5$.

Otherwise $C$ is one 2-connected block of cycle rank two. An ear
decomposition consists of an initial cycle and one additional ear, so
$C$ is a theta graph: three internally disjoint paths between two
vertices. For every edge to lie in a triangle, the three path lengths
must be $1,2,2$; hence $C$ is the diamond $K_4-e$ and has order four.
Both alternatives contradict $|C|>6$. $\square$

### Lemma 2.2 (six-part bicyclic quotient)

Every simple connected bicyclic graph $C$ of order at least six has a
partition into six nonempty connected parts whose contraction is a
simple connected seven-edge graph $Q$. Between any two parts there is
at most one edge of $C$.

#### Proof

While more than six vertices remain, use Lemma 2.1 and contract an edge
in no triangle. Its endpoints have no common neighbour, so the contraction
creates no parallel edge and deletes exactly one edge and one vertex.
It therefore preserves simplicity, connectivity, and cyclomatic number
two. At six vertices the quotient has seven edges. The inverse images are
connected; because no contraction created or suppressed a parallel edge,
two final parts have at most one cross-edge. $\square$

## 3. Infinite-family closure

### Theorem 3.1 (no bicyclic sole exterior)

Let $G$ be seven-connected, let $d_G(v)=7$, suppose $G[N(v)]$ is the
pure Moser spindle, and let $C=G-N[v]$ be the sole exterior component.
If $C$ is bicyclic, then $G$ contains a $K_7$-minor.

#### Proof

Existing certificates give $|C|\ge6$. Take the partition and quotient
$Q$ from Lemma 2.2. A part $A_i$ has neighbours in other parts at at
most $d_Q(i)$ vertices. Therefore

$$
N_G(A_i)\subseteq N_N(A_i)\cup X_i,
\qquad |X_i|\le d_Q(i).
$$

This is a separator, so seven-connectivity gives the defect bound in
Theorem 1.1. The six parts collectively see all of $N$ because
$N_G(C)=N$. Theorem 1.1 gives an $N$-meeting $K_6$-model; add $\{v\}$.
$\square$

## 4. New residual

The tree, unicyclic, and bicyclic closures now imply that every surviving
sole exterior satisfies

$$
\rho(C)\ge3,
\qquad\text{equivalently}\qquad
|E(C)|\ge |V(C)|+2.
$$

The next residual family is tricyclic. The theorem does not yet control
arbitrarily dense or highly entangled 2-connected exteriors.

## 5. Reproduction

```text
PYTHONPATH=.deps python3 moser_bicyclic_shore_probe.py
PYTHONPATH=.deps python3 moser_bicyclic_shore_verify.py
```

Expected replay:

```text
verified 19 bicyclic quotient types and 28575 K6 model clauses
all bicyclic-shore counterexample formulas: UNSAT
```

