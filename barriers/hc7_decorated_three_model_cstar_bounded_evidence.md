# Decorated three-model C*: bounded evidence and a closed terminal cell

**Status:** finite evidence plus one proved terminal-cell elimination.  No
counterexample to C* is known.  Nothing here proves C* in general.

Write C* for the statement under current test:

> `H` is six-connected, contains three disjoint marked `K5`s `L_i` with
> `z_i in L_i`, and every ordinary six-separator contains all
> `z_1,z_2,z_3`.  Must `H` contain a `K7` minor?

## 1. Exact bounded tests

Two independent finite families have no counterexample.

### Cross-degree two

Put arbitrary two-regular cross edges between three disjoint `K5`s.  Up
to permutations inside the cliques, such a graph is a multiset of
properly three-coloured cycles with five vertices of each colour.  There
are 504 types; 340 give a six-connected host.  Exact minor search finds a
`K7` in all 340.

This family cannot itself satisfy C*: every vertex has degree six, and
the neighbourhood of a marked vertex is a six-separator omitting that
marked vertex.  Its value is as a sharp minimum-degree stress test of the
weaker six-connected three-clique statement.

### Planar 3-tree core

Use the twelve-vertex planar 3-tree and three disjoint `K4`s from the
genuine-cell falsifier.  Add one marked vertex complete to each `K4`.
There are 27 remaining possible edges incident with a marked vertex.
The verifier symbolically covers all `2^27` supergraphs.  Every graph
either has a separator forbidden by C* or contains an explicit `K7`
model.

Reproduce with

```bash
python3 barriers/hc7_decorated_three_model_cstar_bounded_verify.py
```

This family is deliberately bounded.  It is not evidence by raw order
alone and it is not promoted as a theorem about arbitrary cores.

## 2. The KLNZ terminal `5,5,5` cell is incompatible with C*

The disjoint-clique equality residue in the published three-clique proof
has `W=emptyset` and three cells `X_1,X_2,X_3`, each of order five,
partitioning the fifteen clique vertices.  Put

\[
                         a_{ij}=|L_i\cap X_j|.
\]

The proof gives `a_ij <= 2`; every row and column sums to five.  Therefore
each row and each column is a permutation of `(2,2,1)`.

Whenever `a_ij=2`, the published separator

\[
                         C_{ij}=X_j\mathbin\triangle L_i
\]

has order six.  It contains all three marked vertices exactly when

* `z_i` is not in `X_j`, and
* the two marks belonging to the other rows are both in `X_j`.

For a fixed column `j`, this can hold for at most one row `i`: it requires
that `X_j` contain exactly two of the three marks, with `i` the omitted
row.  But the column has two entries equal to two, hence supplies two
order-six separators.  At least one misses a marked vertex, contrary to
C*.

Thus C* rigorously closes the terminal disjoint `5,5,5` equality cell.
The remaining proof obligation is not this residue; it is replacing the
earlier uses of ordinary seven-connectivity strongly enough to force the
published argument into it (or directly into a `K7`).

## 3. Boundary of the evidence

The weighted genuine-cell decoder is false; see the companion barrier.
C* survives because it retains ordinary six-connectivity and the common
three-mark property of every minimum cut.  A search over arbitrary
superedges was intentionally stopped after 2,100 sound cutting-plane
candidates (1,716 explicit `K7` witnesses and 384 forbidden-cut
witnesses): this is not an exhaustive result and is not used as evidence
beyond falsification pressure.
