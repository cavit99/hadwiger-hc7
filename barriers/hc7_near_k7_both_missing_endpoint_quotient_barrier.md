# Every coarse both-missing endpoint quotient is `K_7`-minor-free

## Status

After the second-path normalization, it is tempting to classify the
endpoint bundles of the two anticomplete paths and hope that a crossed
bundle order forces `K_7`.  This is false at the quotient level in the
strongest possible form: even after adding every edge allowed by the
endpoint ownership theorem, **every** such nine-vertex quotient is
`K_7`-minor-free.

Thus the crossed-frame programme must retain internal portal order,
proper-minor equality states, or rural expansion societies.  No theorem
depending only on which endpoint bundle owns which row can close the
both-missing branch.

The finite verifier
`hc7_near_k7_both_missing_endpoint_quotient_probe.py` checks all
50 labelled endpoint allocations, but the proof below is uniform.

## 1. Maximal endpoint quotient

Let

\[
                         \mathcal R=\{C,U_1,U_2,U_3,U_4\}
\]

induce a `K_5`.  Add two disjoint edges

\[
                              a_0a_1,\qquad b_0b_1,       \tag{1.1}
\]

with no edge between an `a`-vertex and a `b`-vertex.  Give the first edge
the normalized `2+2` contacts

\[
 N_{\mathcal R}(a_0)=\{U_1,U_2\},\qquad
 N_{\mathcal R}(a_1)=\{U_3,U_4\}.                        \tag{1.2}
\]

Partition the five rows for the second edge into

\[
                 \mathcal L\mathbin{\dot\cup}\mathcal M
                    \mathbin{\dot\cup}\mathcal R'
                    =\mathcal R,                         \tag{1.3}
\]

where

\[
                  |\mathcal L|\ge2,\qquad
                  |\mathcal R'|\ge2,\qquad
                  |\mathcal M|\le1.                     \tag{1.4}
\]

Join `b_0` to every row in `mathcal L union mathcal M` and `b_1` to
every row in `mathcal R' union mathcal M`.  This is the maximal graph
consistent with the audited `2+(at most 1)+2` ownership theorem: the
single mobile row, when present, is joined to both endpoints.

Call the resulting nine-vertex graph `Q`.

## Theorem 1 (uniform quotient barrier)

For every allocation (1.3)--(1.4),

\[
                              \eta(Q)\le6.                \tag{1.5}
\]

### Proof

First observe that `mathcal R` is the unique clique of order five in
`Q`.  An `a`-endpoint sees only two row vertices.  A `b`-endpoint sees at
most three row vertices, because the opposite endpoint owns at least two
of the five rows.  A clique containing both `b_0,b_1` sees at most the one
mobile row, and there are no `a-b` edges.  Hence every clique using a path
endpoint has order at most four.

Suppose that `Q` had a `K_7` model.  The model uses between seven and nine
vertices.  Its seven pairwise adjacent branch sets therefore have total
excess

\[
              \sum_{X\text{ a branch set}}(|X|-1)\le2.  \tag{1.6}
\]

If the excess is zero, all seven branch sets are singleton vertices and
form a `K_7` subgraph, impossible.  If the excess is one, six branch sets
are singletons and form a `K_6` subgraph, again impossible because the
clique number is five.

If the excess is two, there are two possibilities.  One branch set has
order three and the other six are singletons, which again requires a
`K_6` subgraph.  Otherwise two branch sets have order two and the other
five are singletons.  The five singleton roots must be the unique
`K_5=mathcal R`.  The two order-two branch sets consequently partition
the four remaining vertices.  The only edges in the graph induced by
those four vertices are the two edges in (1.1), so connectedness forces
the two branch sets to be `{a_0,a_1}` and `{b_0,b_1}`.  These sets are
anticomplete, contradicting pairwise adjacency of the clique model.

Every case is impossible, proving (1.5).  \(\square\)

## 2. Exact implication

The theorem covers both parallel and crossed assignments of the four
neutral labels, all placements of the row `C`, and the strongest possible
two-ended use of the unique mobile row.  Therefore none of the following
coarse data can force a target minor:

* which rows are locked at the left or right endpoint of the second path;
* whether that partition crosses the fixed `2+2` partition on the first
  path; or
* whether the fifth row meets both endpoints.

The original graph may of course contain a `K_7` using vertices internal
to the five foreign bags or path societies; the quotient has deliberately
forgotten exactly that information.  A positive theorem must force one of
these finer outputs:

1. private rooted pieces inside a nonsingleton row, giving more than one
   branch-set duty;
2. matching equality partitions from proper-minor operations on opposite
   actual shores; or
3. compatible port-labelled rural expansions with one pair of actual
   apex vertices.

This is a structural barrier to further endpoint-pattern enumeration, not
a counterexample to `HC_7`.
