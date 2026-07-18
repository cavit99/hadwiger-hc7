# Exact independent-block traces do not synchronize the new seven-boundary

**Status:** written finite response-language barrier; deterministic verifier
included; separate audit pending.  This is not a counterexample to `HC_7`.
It isolates the precise information missing after the Kempe-fan theorem
returns an exact order-seven separation.

The accompanying checker is
[`hc7_exact7_paired_block_trace_parity_barrier_verify.py`](hc7_exact7_paired_block_trace_parity_barrier_verify.py).

## 1. Boundary and the returned partition

Let

\[
 S=\{j_0,b,r\}\mathbin{\dot\cup}
   \{j_1,z_1,z_2\}\mathbin{\dot\cup}\{q\},
\]

and let

\[
 H=K_3[\{j_0,b,r\}]\mathbin{\dot\cup}
   K_3[\{j_1,z_1,z_2\}]\mathbin{\dot\cup}K_1[\{q\}].       \tag{1.1}
\]

Thus

\[
 J\cup\{q\}=\{j_0,j_1,q\},\qquad \{b,z_1\}
\]

are disjoint independent sets.  The partition

\[
 \Pi_*=
 \bigl\{\{j_0,j_1,q\},\{b,z_1\},\{r\},\{z_2\}\bigr\}       \tag{1.2}
\]

is a proper four-block equality partition of `H`.  It has exactly the two
monochromatic boundary subsets supplied by the exact-seven outcome of the
Kempe-fan theorem.

Let `Omega` be all partitions of `S` into at most six nonempty independent
blocks of `H`.  Split it into

\[
 \mathcal E_{\rm even}=\{\Pi\in\Omega:|\Pi|\text{ is even}\},
 \qquad
 \mathcal E_{\rm odd}=\{\Pi\in\Omega:|\Pi|\text{ is odd}\}. \tag{1.3}
\]

The two families are disjoint and `Pi_*` belongs to the even family.

## 2. Strengthened trace-completeness

### Theorem 2.1

For every nonempty independent set `I` of `H`, each family in (1.3)
contains a partition having `I` as an exact block.

More strongly, if `I_1,I_2` are disjoint nonempty independent sets, each
family contains a partition having both `I_1` and `I_2` as two specified
exact blocks.

Consequently all independent-set star-contraction responses, and even all
responses that prescribe two disjoint independent blocks simultaneously,
are consistent with two disjoint opposite boundary languages.  In
particular these responses do not force the concrete partition (1.2) on
the opposite closed shore.

### Proof

Use either one prescribed independent block or two disjoint prescribed
independent blocks, and write their union as `U`.  An independent set of
`H` contains at most one vertex of each displayed triangle.  After removing
at most two such blocks, at least one vertex remains in each triangle.
Therefore

\[
                              H-U
\]

is nonempty, is not complete, and has chromatic number at most three.

Take an optimal partition of `H-U` into `k` independent blocks.  Since the
residual graph is not complete, some block has at least two vertices.
Splitting that block gives another proper partition with `k+1` blocks.
After adjoining the one or two prescribed exact blocks, the two resulting
partitions have opposite block-count parity.  Both use at most six blocks,
because

\[
                 k\le3,\qquad 2+(k+1)\le6.               \tag{2.1}
\]

Thus the relevant exact-block cylinder meets both parity families.  This
proves both assertions. \(\square\)

For the two blocks occurring in (1.2), the obstruction is especially
transparent.  The even response leaves `r,z_2` as two singleton blocks,
whereas the odd response merges the independent pair `\{r,z_2\}`.  Both
responses preserve the two prescribed large blocks, but the full boundary
partitions remain different.

## 3. The two-packet quotient is also `K_7`-minor-free

Add two nonadjacent vertices `p_L,p_R`, each adjacent to every vertex of
`S`.  This is the quotient obtained by contracting one boundary-full
connected subgraph in each open shore.  Call the resulting graph `Q`.

One has

\[
                         |Q|=9,\qquad \omega(Q)=4.         \tag{3.1}
\]

Indeed `omega(H)=3`, and a clique uses at most one of `p_L,p_R`.  If `Q`
had a `K_7`-minor model, its seven branch sets would use at most nine
vertices.  At most two branch sets could then be nonsingletons, so at least
five branch sets would be singleton vertices.  Those five vertices would
form a `K_5` subgraph, contradicting (3.1).  Hence

\[
                              K_7\not\preccurlyeq Q.       \tag{3.2}
\]

Thus neither the exact trace data nor the static minor obtained from the
two full connected shores detects a contradiction.

## 4. Exact consequence and positive residual

The barrier decisively refutes the following inference from **static
summaries alone**:

\[
 \begin{gathered}
 \text{two disjoint abstract response languages, one containing (1.2),}\
 \text{both meeting every one- and two-block exact-trace cylinder,}\
 \text{and a `K_7`-minor-free two-packet quotient}
 \end{gathered}
\quad\Longrightarrow\quad
 \mathcal E_{\rm even}\cap\mathcal E_{\rm odd}\ne\varnothing
 \text{ or }K_7\preccurlyeq Q.                          \tag{4.1}
\]

It remains possible that the full host hypotheses force a contradiction.
This does **not** refute the corresponding theorem for two actual shores in
one host.  The parity families are abstract response languages; they are
not asserted to be the two extension languages of one seven-connected,
seven-chromatic, `K_7`-minor-free graph whose every proper minor is
six-colourable.  A positive theorem must use a coupled proper-minor
transition away from the contracted full shore, or literal labelled
branch-set geometry.  Repeating independent-set trace queries cannot
suffice.

There is one complete positive subcase.  Since (1.2) proves
`chi(G[S])<=4`, the audited split-boundary synchronization theorem applies:
if the actual graph `G[S]` is split, the two closed shores have a common
boundary equality partition and six-colour `G`.  Therefore every live
exact-seven outcome of the Kempe-fan theorem has a **nonsplit** boundary,
and the next operation must use host-level data beyond exact-block traces.

## 5. Verification and dependencies

Run

```text
python3 barriers/hc7_exact7_paired_block_trace_parity_barrier_verify.py
```

The checker enumerates all proper at-most-six-block partitions, all
nonempty independent sets, and all disjoint pairs of them.  It also checks
the target partition and (3.1).

- [three Kempe connections give a packing or an exact-seven boundary](../results/hc7_kempe_fan_or_exact_seven_boundary.md)
- [split-boundary colour synchronization](../results/hc7_split_boundary_synchronization.md)
