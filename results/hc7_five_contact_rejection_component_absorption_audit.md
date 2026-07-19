# Independent audit of five-contact rejection-component absorption

**Verdict:** GREEN for Theorem 2.1 and Corollary 3.1 at the exact source
revision identified below.

**Audited source:** `hc7_five_contact_rejection_component_absorption.md`,
SHA-256

```text
8dda06118dbf82a516ce32c50b2be4bf6647b39dcfe9ff395810689d6ff18500
```

The GREEN audit was performed on source revision
`452dfbf4c19ab869f4e2088adcf5c7b17227e235558078a227911be589e56a22`.
The source was then moved from `active/` to `results/` and only its status
line was changed to link this audit.  The theorem statement and proof are
unchanged; the displayed hash pins the promoted source.

This is a separate internal mathematical audit, not external peer review.
It reconstructs every component reassignment, every adjacency of the
explicit `K_7`-minor model, the actual-separation assertion, the strict
common-branch-set descent, the shortest-path equality case, and the paired
rejection-kernel corollary.  No palette colour is identified with a model
label.

## 1. Hypotheses and fixed invariants

The source starts with a partition

\[
              \{x\},B,U,H_1,H_2,H_3,H_4
\]

of `V(G)` into nonempty connected sets.  They form a labelled
`K_7`-minus-one-edge model whose only missing adjacency is `xB`.  Hence:

1. `x` is anticomplete to `B` and adjacent to each of
   `U,H_1,H_2,H_3,H_4`;
2. the six nonsingleton-labelled branch sets are mutually adjacent except
   for no required `xB` edge; and
3. because the model is spanning, every vertex considered later already
   belongs to exactly one displayed branch set.

The connected proper set `Q subsetneq U` has literal edges to `B` and to
each `H_i`.  These five contacts are the only label-sensitive input to the
absorption argument.

## 2. Construction of the replacement set `U_0`

If `Q` is adjacent to `x`, then `U_0=Q` is nonempty, connected, and a proper
subset of `U`.  It is adjacent to `x,B,H_1,H_2,H_3,H_4` by definition and
the five-contact hypothesis.

Suppose instead that `Q` is anticomplete to `x`.  Since `G[U]` is connected
and `U` has an edge to `x`, a path from the set `Q` to `x` exists in
`G[U union {x}]`.  Choose one with minimum length and stop at its first
vertex in `Q` when read from `x`; it has the form

\[
                     q p_1\cdots p_kx,
       \qquad q\in Q,\quad p_1,\ldots,p_k\in U-Q.
\]

Thus `U_0=Q union {p_1,...,p_k}` is connected.  It retains all five foreign
contacts through `Q` and is adjacent to `x` through `p_kx`.  Consequently

\[
              \{x\},B,U_0,H_1,H_2,H_3,H_4
\]

already forms a labelled, though not necessarily spanning,
`K_7`-minus-one-edge model.  Replacing `U` by `U_0` introduces no new
missing labelled adjacency.

## 3. The equality case `U_0=U`

If `U_0=U`, the direct definition `U_0=Q` is impossible because `Q` is a
proper subset.  Hence the shortest-path construction applies, `Q` is
anticomplete to `x`, and

\[
                         U-Q=\{p_1,\ldots,p_k\}.
\]

Each asserted forbidden shortcut follows directly from path minimality:

- an edge from any vertex of `Q` to `p_j`, for `j>=2`, replaces the initial
  segment through `p_1,...,p_{j-1}`;
- an edge `xp_j`, for `j<k`, replaces the terminal segment through
  `p_{j+1},...,p_k`; and
- an edge `p_ip_j` with `i+1<j` skips the nonempty interval between them.

The reverse ordering is the same last case after interchanging `i,j`.
Consecutive path edges are present, so the displayed vertices induce a
path.  Since they are all of `U-Q`, outcome 4 accurately says that the
entire old material outside `Q` is one induced shortest connector.  The
argument does not assert that `Q` has only one neighbour on that connector;
additional `Q-p_1` edges are harmless and are not excluded by the theorem.

## 4. Components outside a proper `U_0`

Now assume `U_0 subsetneq U` and let `R_1,...,R_m` be the components of
`G[U-U_0]`.  Every component has an edge to `U_0`: otherwise connectedness
of `G[U]` would fail.  Distinct components are anticomplete by their
definition.  These two facts justify processing and reassigning the
components independently.

### 4.1 Assignment to an `H_i`

If a component `R` has an edge to `H_i`, assigning all of `R` to `H_i`
preserves disjointness and makes `H_i union R` connected.  Possible extra
edges from `R` to `x`, `B`, `U_0`, or other `H_j` do not destroy a minor
model.  In particular, even when `R` is adjacent to `x`, it is not assigned
to `B`, so the unique missing pair `xB` remains absent.

If several components are assigned to the same `H_i`, each has its own
edge to the old connected `H_i`.  Their union with `H_i` is therefore
connected even though the components are pairwise anticomplete.

### 4.2 Assignment to `B`

Suppose `R` has no edge to any `H_i` but has an edge to `B`.  When `R` is
anticomplete to `x`, the union `B union R` is connected and remains
anticomplete to `x`.  Assigning `R` to `B` therefore preserves both the
branch-set connectivity and the sole missing labelled adjacency.

### 4.3 The explicit `K_7` model

In the preceding case, suppose instead that `R` also has an edge to `x`.
The seven proposed branch sets are

\[
              \{x\},\quad B\cup R,\quad U_0,
              \quad H_1,H_2,H_3,H_4.
\]

They are pairwise disjoint because `R subseteq U-U_0`, and each is
connected: `B union R` uses an `R-B` edge, while the others were already
connected.  Every pair is adjacent:

- `{x}` meets `B union R` through an `x-R` edge, meets `U_0` by the
  construction in Section 2, and meets every `H_i` in the original model;
- `B union R` meets `U_0` through the retained `B-Q` edge, and meets every
  `H_i` through the original `B-H_i` adjacencies;
- `U_0` meets every `H_i` through a retained `Q-H_i` edge; and
- the four `H_i` are pairwise adjacent in the original model.

Thus the displayed sets are an explicit `K_7`-minor model.  Omitted
components of `U-U_0` do not matter because a minor model need not span.

### 4.4 The full-neighbourhood separation

Finally suppose `R` has no edge to `B` or to any `H_i`.  By the spanning
partition, every neighbour outside the old branch set `U` lies in
`{x},B,H_1,...,H_4`.  The latter five possibilities have just been
excluded.  Inside `U`, a neighbour of `R` lies either in `U_0`, in `R`, or
in another component of `G[U-U_0]`; the last possibility is excluded by
the component definition.  Therefore its external neighbourhood satisfies

\[
                              N_G(R)\subseteq U_0\cup\{x\}.
\]

The connected set `R` is nonempty.  The nonempty old branch set `B`
survives outside `R union N_G(R)`, because `R` has no edge to `B`.  Hence
`G-N_G(R)` has a component containing `R` and a distinct nonempty side
containing a vertex of `B`.  This is an actual separation, not merely a
quotient boundary.  Seven-connectivity then gives `|N_G(R)|>=7`.

## 5. Simultaneous absorption and strict descent

Assume neither the explicit-minor outcome nor the full-neighbourhood
outcome occurred.  Every component of `U-U_0` has therefore received one
of the permitted assignments.  Enlarge each old branch set by all
components assigned to it.

The resulting seven sets are disjoint and span `G`, because the processed
components partition `U-U_0`.  Each enlarged set is connected through its
old branch set.  Their required adjacencies are preserved as follows:

- old edges retain every adjacency among `B,H_1,...,H_4`;
- the five contacts from `Q subseteq U_0` retain all adjacencies from `U_0`
  to `B',H'_1,...,H'_4`;
- old edges retain the adjacencies from `x` to every `H'_i`, and the
  construction retains `xU_0`; and
- `x` is anticomplete to `B'`, because it was anticomplete to old `B` and
  only `x`-anticomplete components were assigned there.

Thus the new sets form a spanning labelled `K_7`-minus-one-edge model with
the same labels, the same singleton `{x}`, and exactly the same missing
pair.  Since this part of the proof assumes `U_0 subsetneq U`, the host-level
quantity `|U|` strictly decreases.  No auxiliary quotient size or path
length is being mistaken for the decreasing parameter.

## 6. The paired rejection-kernel corollary

The cited strict-transfer theorem supplies a nonempty connected component
`Q` of `G[U-V(K)]` with `|Q|<|U|` and a rejected colouring trace on its
literal full neighbourhood.  Because the nonempty kernel `K` is disjoint
from `Q`, `Q` is a proper subset of `U`.  Under the additional five-contact
hypothesis, all assumptions of Theorem 2.1 hold.

The four theorem outcomes translate exactly to the four corollary outcomes:

1. the explicit `K_7` model is unchanged;
2. `Q subseteq U_0`, and the replacement common branch set has strictly
   smaller order than old `U`;
3. the returned component `R subseteq U-U_0` is a connected subgraph of the
   old common branch set and has its full neighbourhood contained in
   `U_0 union {x}`; and
4. old `U-Q` is precisely the induced shortest connector.

The host graph, the vertex set of `Q`, its induced subgraph, and its full
neighbourhood are unchanged by branch-set reassignment.  Therefore the
rejected trace attached to `Q` remains valid in outcomes 2--4.  This is
trace preservation in the same graph, not a claim that palette colours now
identify the new model labels.

For the last assertion, `K subseteq U-Q`.  In outcome 4, `G[U-Q]` is an
induced path.  Since `K` is itself an induced connected subgraph of `G[U]`,
its vertex set induces a connected subgraph of that path and hence a path
(including the one-vertex degenerate case).  The contrapositive proves that
a nonpath `K` excludes outcome 4.

## 7. Trust boundary

The proof does not supply the five-contact hypothesis for an arbitrary
component returned by strict transfer.  It gives only the lower bound seven
on the full-neighbourhood separator, not order exactly seven or compatible
closed-shore colourings.  It also leaves the shortest-connector equality
case when the paired kernel is a path.  The audit found no inference beyond
these stated limits.
