# Cyclic two-defect shore packing over the Moser boundary

## 1. Finite packing theorem

Let $N=\{0,1,2,3,4,5,6\}$ induce the pure Moser spindle

$$
E(M)=\{01,02,03,04,12,16,26,34,35,45,56\}.
$$

### Theorem 1.1 (computer-assisted)

Let $A_1,\ldots,A_6$ be disjoint connected subgraphs outside $N$.
Suppose:

1. $A_i$ is adjacent to $A_{i+1}$, with indices modulo six;
2. every $A_i$ is adjacent to all but at most two vertices of $N$; and
3. every vertex of $N$ is adjacent to at least one $A_i$.

Then the graph contains an $N$-meeting $K_6$-model.

Extra edges between nonconsecutive shores do not affect the conclusion.

#### Proof certificate

Contract each shore to a labelled helper $h_i$. It is enough to prove the
claim in the thirteen-vertex quotient containing the fixed Moser edges,
the six cycle edges $h_ih_{i+1}$, and the 42 optional incidences $nh_i$.

The Boolean base system says:

$$
\deg_N(h_i)\ge5\quad(i=1,\ldots,6)
$$

and, for every $n\in N$, at least one incidence $nh_i$ is present.

The certificate contains 1797 explicit six-bag models. For each model it
records only the optional incidences needed to connect its bags and make
them pairwise adjacent. A quotient avoiding an $N$-meeting $K_6$ must
omit at least one incidence from each record. Adding all 1797 resulting
clauses to the base system is unsatisfiable.

`moser_cycle_shore_verify.py` independently:

1. checks that every record has six disjoint nonempty bags meeting $N$;
2. reconstructs the graph using only the fixed edges and recorded
   incidences;
3. verifies bag connectivity and all fifteen pairwise adjacencies; and
4. reconstructs the 42-variable formula and obtains `unsat` from Z3.

Thus every allowed incidence assignment contains one of the recorded
models. Expanding each helper $h_i$ back to its connected shore preserves
connectivity and all model adjacencies, proving the theorem. $\square$

## 2. Consequences for a sole exterior

Let $G$ be seven-connected, let $d_G(v)=7$, let $G[N(v)]$ be the pure
Moser spindle, and let $C=G-N[v]$ be connected.

### Corollary 2.1 (no cycle exterior)

If $G[C]$ is a cycle, then $G$ contains a $K_7$-minor.

#### Proof

The previously certified order-four and order-five closures allow us to
assume $|C|\ge6$. Partition the cycle into six nonempty consecutive arcs
$A_1,\ldots,A_6$. Each arc has at most two neighbours in $C$ outside
itself. Since

$$
N_G(A_i)\subseteq N_N(A_i)\cup\{\text{the two adjacent cycle vertices}\},
$$

seven-connectivity gives $|N_N(A_i)|\ge5$. Moreover $N_G(C)=N$, so
the six arcs collectively see every boundary vertex. Theorem 1.1 gives
an $N$-meeting $K_6$-model in $G-v$; add $\{v\}$. $\square$

### Corollary 2.2 (long-cycle unicyclic exteriors)

Suppose $C$ is unicyclic and its unique cycle has length at least six.
Then $G$ contains a $K_7$-minor.

#### Proof

Partition the unique cycle into six nonempty consecutive arcs, and assign
every tree component of $C-E(R)$ to the arc containing its attachment
vertex on the cycle. The resulting six shores are connected and cyclically
adjacent. A shore has only the two cycle edges to the other five shores,
so seven-connectivity again gives boundary defect at most two. They cover
$C$ and hence collectively see all of $N$. Apply Theorem 1.1 and add
$\{v\}$. $\square$

## 3. Exact remaining one-component structure

Together with `hadwiger_moser_one_component_infinite_classes.md`, the new
conclusions are:

* every tree exterior is eliminated;
* every cycle exterior is eliminated;
* every cutvertex in a residual exterior has exactly two components
  behind it; and
* a unicyclic residual can only have unique cycle length three, four, or
  five.

This does not eliminate 2-connected exteriors with multiple cycles, nor
the short-core unicyclic cases with attached paths.

## 4. Reproduction

Generate and replay the certificate with

```text
PYTHONPATH=.deps python3 moser_cycle_shore_probe.py
PYTHONPATH=.deps python3 moser_cycle_shore_verify.py
```

The verifier prints

```text
verified 1797 cyclic-shore K6 model clauses
cyclic two-defect counterexample formula: UNSAT
```

