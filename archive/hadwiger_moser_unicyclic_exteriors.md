# Elimination of every unicyclic sole exterior behind a Moser boundary

## 1. The finite six-shore theorem

Let $N=\{0,1,2,3,4,5,6\}$ induce the pure Moser spindle

$$
E(M)=\{01,02,03,04,12,16,26,34,35,45,56\}.
$$

### Theorem 1.1 (unicyclic shore packing, computer-assisted)

Let $Q$ be any simple connected unicyclic graph on vertices
$1,\ldots,6$. Let $A_1,\ldots,A_6$ be disjoint connected shores such
that every edge of $Q$ is represented by an edge between the corresponding
shores. Suppose

$$
|N-N_N(A_i)|\le d_Q(i)\qquad(i=1,\ldots,6)
$$

and the six shores collectively see every vertex of $N$. Then the graph
contains an $N$-meeting $K_6$-model.

Extra cross-edges between shores do not affect the conclusion.

#### Proof certificate

There are exactly thirteen unlabelled connected unicyclic graphs on six
vertices. For each type, contract the shores to six labelled helpers and
retain the fixed Moser boundary. The 42 helper-boundary incidences are
Boolean variables. Row $i$ has at least $7-d_Q(i)$ present incidences,
and every boundary column has at least one.

A lazy exact search produced, over all thirteen types, 8447 explicit
$N$-meeting $K_6$ models. Each record lists six branch sets and only the
optional incidences needed for their connectivity and pairwise adjacency.
For each quotient type, requiring at least one recorded incidence to be
absent from every model is inconsistent with the row and column
constraints.

`moser_unicyclic_shore_verify.py` independently:

1. enumerates the thirteen unlabelled graph-atlas types and checks exact
   graph6/edge-set coverage;
2. verifies the degree bounds stored for each type;
3. checks every one of the 8447 six-bag models using only fixed edges and
   its recorded optional incidences; and
4. reconstructs all thirteen Boolean systems and verifies each as
   `unsat` with Z3.

Expanding each helper to its original connected shore preserves every
verified model. $\square$

## 2. Contracting an arbitrary unicyclic exterior

### Lemma 2.1 (six connected quotient shores)

Every simple connected unicyclic graph $C$ of order at least six has a
partition into six nonempty connected sets $A_1,\ldots,A_6$ such that
contracting the sets produces a simple connected unicyclic graph $Q$.
Moreover, between two distinct parts there is at most one edge of $C$.

#### Proof

Repeatedly contract an edge while more than six vertices remain. If a
bridge exists, contract a bridge. This preserves simplicity and the
unique cycle. If no bridge exists, the graph is a cycle; since its order
is greater than six, contract a cycle edge, again leaving a simple cycle.
The process ends with a simple connected unicyclic graph on six vertices.
The inverse images of its vertices are nonempty and connected.

Every contraction used preserves simplicity, so two final parts cannot
have two distinct cross-edges. Equivalently, two such cross-edges together
with paths inside the two connected parts would form an additional cycle
(or a forbidden parallel two-cycle in the quotient). $\square$

## 3. Infinite-family closure

### Theorem 3.1 (no unicyclic sole exterior)

Let $G$ be seven-connected, let $d_G(v)=7$, suppose $G[N(v)]$ is the
pure Moser spindle, and let $C=G-N[v]$ be the sole exterior component.
If $C$ is unicyclic, then $G$ contains a $K_7$-minor.

#### Proof

The certified order-four and order-five results give $|C|\ge6$. Take the
six-part partition from Lemma 2.1 and let $Q$ be its quotient. For each
part $A_i$, its neighbours in $C-A_i$ are contained in at most
$d_Q(i)$ vertices, one on the far side of each quotient edge. Hence

$$
N_G(A_i)\subseteq N_N(A_i)\cup X_i,
\qquad |X_i|\le d_Q(i).
$$

This set separates $A_i$ from the rest of $G$. Seven-connectivity yields

$$
|N_N(A_i)|+d_Q(i)\ge7,
$$

which is precisely the defect bound in Theorem 1.1. Since
$N_G(C)=N$, the six parts collectively see every boundary vertex.
Theorem 1.1 supplies an $N$-meeting $K_6$-model in $G-v$; adding
$\{v\}$ gives a $K_7$-model. $\square$

## 4. New exact residual

Combining this theorem with the tree closure gives:

$$
|E(C)|\ge |V(C)|+1.
$$

Thus every sole-exterior pure-Moser residual has cyclomatic number at
least two. Also, every cutvertex has exactly two components behind it.
The remaining one-component obstruction begins with bicyclic exteriors,
not merely with order six.

## 5. Reproduction

Run

```text
PYTHONPATH=.deps python3 moser_unicyclic_shore_probe.py
PYTHONPATH=.deps python3 moser_unicyclic_shore_verify.py
```

The verifier prints

```text
verified 13 unicyclic quotient types and 8447 K6 model clauses
all unicyclic-shore counterexample formulas: UNSAT
```

