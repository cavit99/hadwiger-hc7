# A persistent model edge either preserves or rejects a fixed boundary trace

**Status:** written proof; separate internal audit GREEN in
[`hc7_persistent_edge_fixed_trace_alignment_audit.md`](hc7_persistent_edge_fixed_trace_alignment_audit.md).

This note isolates the exact point at which a deletion-persistent edge of a
labelled near-complete minor model can be coupled to a list-critical
obstruction on one side of a separation.  The conclusion is a binary
alternative: either the edge deletion admits the prescribed boundary
colouring and the edge belongs to every obstruction for that colouring, or
no colouring of the edge deletion has that boundary trace.  It does not
construct a clique minor or synchronize two shores.

## 1. Setting

Let `q>=2`, and let

\[
                  V(G)=A\mathbin{\dot\cup}X\mathbin{\dot\cup}D,
                                                               \tag{1.1}
\]

where there is no edge between `A` and `D`.  Let `c` be a proper
`q`-colouring of `G[A union X]`.  For every `w in D`, define

\[
             L_c(w)=[q]-c(N_G(w)\cap X).                \tag{1.2}
\]

Thus a proper colouring of `G[D]` from the lists `L_c` is exactly a proper
colouring which glues to `c` across `X`.

Let `f=uv in E(G[D])`, and suppose `G-f` has a proper `q`-colouring.  Write

\[
 \mathcal R_f(X)={\psi|_X:\psi\text{ is a proper }q\text{-colouring of }G-f\}
                                                               \tag{1.3}
\]

for its labelled boundary-response set.

## 2. Fixed-trace alignment

### Theorem 2.1

Exactly one of the following alternatives holds.

1. \(c|_X\notin\mathcal R_f(X)\).  Thus every proper `q`-colouring of
   `G-f` rejects the prescribed labelled boundary trace.
2. \(c|_X\in\mathcal R_f(X)\).  Then `G[D]-f` is `L_c`-colourable, and all
   of the following hold:

   a. every induced non-`L_c`-colourable subgraph `K` of `G[D]` contains
      both `u,v` and the edge `f`;
   b. every spanning subgraph `F` of an induced non-`L_c`-colourable
      subgraph which is itself non-`L_c`-colourable and edge-minimal with
      that property contains `f`;
   c. if `G` is not `q`-colourable, the ends of `f` have the same colour
      in every proper `q`-colouring of `G-f` whose boundary trace is
      `c|_X`.

Consequently, in alternative 2 a deletion-persistent model edge lying in
`G[D]` is a genuine edge of every fixed-trace list-critical obstruction on
that shore.  In alternative 1, its whole proper-minor response language is
disjoint from the chosen trace.

#### Proof

The two alternatives in the first sentence are complementary.  Suppose
alternative 2 holds, and choose a proper `q`-colouring `psi` of `G-f` with

\[
                             \psi|_X=c|_X.              \tag{2.1}
\]

For every `w in D`, properness of `psi` implies that `psi(w)` is absent
from the colours on \(N_G(w)\cap X\).  Equation (2.1) therefore gives

\[
                             \psi(w)\in L_c(w).          \tag{2.2}
\]

Hence `psi|_D` is an `L_c`-colouring of `G[D]-f`.

Let `K` be an induced non-`L_c`-colourable subgraph of `G[D]`.  If `f`
were not an edge of `K`, then `K` would be a subgraph of `G[D]-f`, and the
restriction of `psi` would `L_c`-colour it, a contradiction.  Since `K` is
induced, containing `f=uv` as an edge is equivalent to containing both
ends.  This proves part 2a.

Let `F` be as in part 2b.  If `f` were absent from `F`, then `F` would
again be a subgraph of `G[D]-f` and would inherit the `L_c`-colouring
`psi|_D`, contrary to its definition.  Thus \(f\in E(F)\).

Finally suppose that `G` is not `q`-colourable.  In any proper
`q`-colouring of `G-f`, the ends of `f` must have the same colour;
otherwise restoring `f` would give a proper `q`-colouring of `G`.  This
proves part 2c. \(\square\)

## 3. Exact scope

The theorem is label-preserving at the boundary: membership in
\(\mathcal R_f(X)\) means equality of the labelled trace, not equality only
up to a permutation of colour names.

The theorem does not prove that a persistent model edge lies in the chosen
shore, shares a vertex with a prescribed boundary edge, or admits the
fixed trace.  Those are alignment hypotheses for the next structural
theorem.  It also does not identify palette colours with branch-set labels,
make the fixed-trace Kempe paths disjoint, construct a `K_7` minor, or
produce a colour-compatible order-seven separation.

## 4. Dependencies

- [boundary list-criticality](hc7_boundary_list_critical_transfer.md), for
  the fixed-trace obstruction to which the theorem is intended to apply;
- [single-portal amplification](hc7_single_portal_amplification.md), for a
  deletion-persistent edge in a spanning labelled near-`K_7` model.
