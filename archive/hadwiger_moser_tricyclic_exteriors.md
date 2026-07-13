# Six-shore tricyclic packing and the two exceptional cores

## 1. Certified six-shore theorem

Let $N=\{0,1,2,3,4,5,6\}$ induce the pure Moser spindle.

### Theorem 1.1 (tricyclic shore packing, computer-assisted)

Let $Q$ be any simple connected graph on six vertices with eight edges.
Let $A_1,\ldots,A_6$ be disjoint connected shores representing every
edge of $Q$. For every nonempty proper $I\subset V(Q)$, suppose

$$
\left|N_N\left(\bigcup_{i\in I}A_i\right)\right|
+|\delta_Q(I)|\ge7,
$$

and suppose all six shores collectively see $N$. Then the graph contains
an $N$-meeting $K_6$-model.

#### Certificate

There are 22 unlabelled connected eight-edge graphs on six vertices.
For each type, the 42 helper-boundary incidences are constrained by all
displayed shore-union cuts. The certificate contains 64,044 explicit
six-bag models. `moser_tricyclic_shore_verify.py` independently checks
the 22 graph types, every model, every cut constraint, and all 22 final
Z3 `unsat` results. Expanding helpers to shores proves the theorem.
$\square$

The union inequalities are exactly what seven-connectivity supplies when
there is at most one edge between each pair of shores: the vertices on
the far ends of the quotient cut edges, together with the boundary
neighbours of the union, form a separator.

## 2. Safe contractions

An edge in no triangle can be contracted without creating parallel edges;
the contraction preserves simplicity and cyclomatic number.

### Lemma 2.1 (all-triangle tricyclic classification)

If a connected tricyclic graph has every edge in a triangle, then it has
order at most seven. The only order-seven possibilities are:

1. three triangles sharing one common cutvertex (graph6 `FGEFw`); and
2. a chain of three triangle blocks (graph6 `FxCX_`).

#### Proof

There are no bridges. Cycle ranks add over nontrivial blocks, so the
block-rank partition is $1+1+1$, $1+2$, or $3$.

A rank-one all-triangle block is a triangle. A rank-two 2-connected
all-triangle block is the diamond. For a rank-three 2-connected block,
the degree identity

$$
\sum_v(d(v)-2)=4
$$

and the fact that every degree-two vertex lies in a triangle bound the
order by seven, as follows. Two degree-two vertices cannot be adjacent:
their common triangle would attach to the rest only through its third
vertex, contradicting 2-connectivity. The triangle cycles belonging to
distinct degree-two vertices are therefore linearly independent, because
each contains the two incident edges unique to its degree-two vertex.
The cycle space has dimension three, so there are at most three such
vertices. The displayed excess identity gives at most four vertices of
degree at least three. Direct enumeration through order seven leaves exactly
$K_4$ and the two five-vertex 2-tree types (the three-page book and the
triangle-chain 2-tree). Thus a single rank-three block has order at most
five; a rank-two block plus a triangle has order six; and three triangle
blocks have order seven, in exactly the two stated block-tree forms.
$\square$

The small enumeration in the last paragraph can be replayed directly
from the graph atlas; it is independent of the 64,044-model certificate.

### Corollary 2.2 (exact contraction alternative)

Every connected tricyclic graph of order at least six can be contracted,
using only nontriangle edges, either to a simple six-vertex tricyclic
graph or to one of the two seven-vertex triangle cacti in Lemma 2.1.

#### Proof

While the order exceeds seven, Lemma 2.1 supplies a nontriangle edge to
contract. At order seven, contract once more unless every edge lies in a
triangle. The contraction process never creates or suppresses a parallel
edge, so inverse images form connected shores with at most one cross-edge
per quotient adjacency. $\square$

## 3. Consequence and exact residual

For a sole exterior $C$ behind the pure-Moser neighbourhood, if the
contraction alternative ends at a six-vertex quotient, seven-connectivity
gives all shore-union inequalities in Theorem 1.1. Hence that entire
tricyclic family contains a $K_7$-minor after adding $\{v\}$.

The only tricyclic exterior families not closed by this theorem are those
whose safe contraction terminates in one of the two seven-vertex
three-triangle cacti. A seven-helper version of Theorem 1.1 has not yet
been certified. Therefore one must not claim that every tricyclic exterior
is eliminated.

Combining the audited results, every remaining sole exterior either has
cyclomatic number at least four, or belongs to one of these two exact
tricyclic contraction families.

## 4. Reproduction

```text
PYTHONPATH=.deps python3 moser_tricyclic_shore_probe.py
PYTHONPATH=.deps python3 moser_tricyclic_shore_verify.py
```

Expected replay:

```text
verified 22 tricyclic quotient types and 64044 K6 model clauses
all six-shore tricyclic counterexample formulas: UNSAT
```
