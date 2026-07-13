# Finite-order falsification bound for the static two-apex candidate

## Status

An exhaustive exact certificate proves that the proposed static
counterexample

\[
 \kappa(G)\ge7,\quad K_7^\vee\preceq G,\quad
 K_7\npreceq G,\quad G\text{ not two-apex}                   \tag{0.1}
\]

has at least eleven vertices.  In fact the stronger statement holds:

> Every seven-connected graph on at most ten vertices contains a
> `K_7` minor.

The certificate is
`hc7_near_k7_static_candidate_order10_verify.py`.  It does not assume
the `K_7^vee` or non-two-apex conditions.

## 1. Exhaustive classification

Let `8<=n<=10` and let `G` be seven-connected on `n` vertices.  Put
`H=overline G`.  Since `delta(G)>=7`,

\[
                         \Delta(H)\le n-8\le2.              \tag{1.1}
\]

For `n=8`, `H` is edgeless.  For `n=9`, it is a matching plus isolated
vertices.  For `n=10`, every component of `H` is a path or a cycle.
Consequently the isomorphism type of `H` is exactly a multiset

\[
                         \{P_{a_1},\ldots,P_{a_s},
                           C_{b_1},\ldots,C_{b_t}\}          \tag{1.2}
\]

whose orders sum to `n` (with cycles of order at least three).  This is
a complete, duplication-free classification of the possible complements.

The verifier generates all multisets (1.2), discards those violating the
degree bound in (1.1), complements them, and computes vertex connectivity
exactly.  The resulting counts are:

\[
\begin{array}{c|c|c}
n&\text{complement types satisfying (1.1)}&
       \text{types with }\kappa(G)\ge7\\ \hline
8&1&1\\
9&5&5\\
10&106&87.
\end{array}                                                \tag{1.3}
\]

## 2. Exact minor certificate

For each of the 93 surviving types, the verifier enumerates every
nonempty connected vertex subset as a possible branch set.  It joins two
candidate sets precisely when they are disjoint and have an edge between
them, and performs an exhaustive clique search for seven mutually
compatible candidates.

The connected-subset enumeration is complete.  A branch set in a
seven-bag model on `n` vertices has order at most `n-6`; the verifier
uses exactly this safe bound.  For every surviving complement type it
finds seven pairwise compatible connected sets and then independently
rechecks:

1. nonemptiness and connectedness of every bag;
2. pairwise disjointness; and
3. at least one original edge between every pair of bags.

No random generation, planarity heuristic, chromatic test, or unproved
minor oracle is used.

### Theorem 2.1

Every seven-connected graph of order at most ten has a `K_7` minor.

#### Proof

The degree bound (1.1) and the path/cycle classification make the
generator exhaustive up to isomorphism.  The exact branch-set verifier
returns and rechecks a `K_7` model for every type satisfying
seven-connectivity.  The counts (1.3) exhaust all orders at which such a
graph can occur.  \(\square\)

## 3. Consequence for the static candidate

Any counterexample to

\[
  \text{7-connected}+K_7^\vee\text{-minor}+K_7\text{-minor-free}
     \Longrightarrow\text{two-apex}                         \tag{3.1}
\]

has order at least eleven.  The same lower bound applies to the
7-contraction-critical strengthening.

This is only a finite-order exclusion, not evidence that (3.1) is true.
At order eleven the complement can have degree three, so path/cycle
classification no longer suffices.

