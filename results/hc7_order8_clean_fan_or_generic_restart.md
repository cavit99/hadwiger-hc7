# A boundary-full order-eight response gives a clean fan or a generic exact-seven restart

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_clean_fan_or_generic_restart_audit.md`](hc7_order8_clean_fan_or_generic_restart_audit.md).

This corollary combines the audited operation-coupled order-eight theorem
with the generic exact-seven restart.  It treats the two- and
three-component cases uniformly, including all boundary types in the
three-component classification.

## 1. Setting

Use the hypotheses and notation of
[`hc7_operation_coupled_order8_response.md`](hc7_operation_coupled_order8_response.md).
Thus `X` has order eight, the components of `G-X` are

\[
                       C_0,\ldots,C_{m-1},
                       \qquad m\in\{2,3\},             \tag{1.1}
\]

every component is adjacent to every vertex of `X`, `e=pv` has
`p in X`, `v in C_0`, and `d` is a proper six-colouring of `G-e`.

## 2. Uniform alternative

### Theorem 2.1

At least one of the following holds.

1. There is a clean five-path fan retaining the five prescribed first
   edges, as in Theorem 4.1(1) of the operation-coupled order-eight
   theorem.
2. There is a generic exact-seven response interface

   \[
      \bigl(A,Y,V(G)-(A\cup Y);\,ya,c\bigr)             \tag{2.1}
   \]

   where `A` is a nonempty connected proper subset of `C_0`,
   `Y=N_G(A)`, `|Y|=7`, `ya` is any edge from `Y` to `A`, and `c` is a
   proper six-colouring of `G-ya`.  In particular,

   \[
                              |A|<|C_0|.                \tag{2.2}
   \]

#### Proof

Apply Theorem 4.1 of the operation-coupled order-eight theorem.  Its first
outcome is item 1.  In its second outcome it gives a nonempty connected
set `A subsetneq C_0` with `Y=N_G(A)` and `|Y|=7`.

Choose an edge `ya` from `Y` to `A`.  The proper minor `G-ya` has a proper
six-colouring `c`, and `c(y)=c(a)`; otherwise `c` would already be a
proper six-colouring of `G`.  The opposite open shore in (2.1) is
nonempty, since it contains every far component `C_i`, `i>0`.  Thus (2.1)
is a generic exact-seven response interface.  The proper inclusion gives
(2.2). \(\square\)

### Corollary 2.2 (minimum-shore consequence)

Let `A_0` be the connected shore of a minimum-order generic exact-seven
response interface.  If the order-eight configuration above occurs with

\[
                        C_0\subsetneq A_0,              \tag{2.3}
\]

then the clean five-path fan in Theorem 2.1(1) must exist.

#### Proof

Outcome 2 would give a generic exact-seven response shore `A` satisfying

\[
                         |A|<|C_0|<|A_0|,
\]

contrary to the choice of `A_0`. \(\square\)

## 3. Exact trust boundary

The theorem completely absorbs the order-seven output of the
operation-coupled order-eight machinery into the well-founded generic
restart.  In a minimum generic shore, every residue satisfying the setting
of Section 1 and `C_0 subsetneq A_0` therefore lies in the clean fan branch.

The fan paths may end at repeated boundary vertices and need not first
meet five different inherited branch sets.  The theorem does not preserve
a connected residual subgraph, supply the cyclic-contact allocation
hypotheses, synchronize a boundary partition, or prove `HC_7`.

## 4. Dependencies

- [operation-coupled order-eight responses](hc7_operation_coupled_order8_response.md)
- [generic exact-seven selected-response restart](hc7_generic_exact7_response_restart.md)
