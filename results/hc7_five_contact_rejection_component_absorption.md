# Absorbing a five-contact rejection component into a labelled near-complete model

**Status:** written proof; separate internal audit GREEN in
[`hc7_five_contact_rejection_component_absorption_audit.md`](hc7_five_contact_rejection_component_absorption_audit.md).

This note gives a label-preserving model reduction for the proper-kernel
branch of total boundary-trace rejection.  A connected proper part of one
common branch set which retains the other five nonprotected model contacts
can replace that branch set.  Components omitted by the replacement can be
reassigned to unchanged foreign branch sets.  Failure of that reassignment
either constructs a `K_7`-minor model or exposes the full neighbourhood of
a connected subgraph.  The only remaining model-local equality case is a
shortest connector from the retained component to the protected singleton.

The operation changes no edge and contracts no vertex.  Thus any rejected
boundary trace carried by the retained component remains a trace in the
same host graph.  The theorem does not prove that a component returned by
the total-rejection kernel has the five required model contacts, and it
does not make the separator outcome colour-compatible.

## 1. Labelled setting

Let `G` be a seven-connected graph.  Suppose its vertex set is partitioned
into seven nonempty connected branch sets

\[
                 \{x\},\ B,\ U,\ H_1,H_2,H_3,H_4,                \tag{1.1}
\]

which form a spanning labelled `K_7`-minus-one-edge model.  Its unique
missing adjacency is `xB`.  Thus `x` is adjacent to `U` and to every
`H_i`, the set `B` is adjacent to `U` and to every `H_i`, and the five
common branch sets `U,H_1,H_2,H_3,H_4` are pairwise adjacent.

Let `Q` be a nonempty proper connected subset of `U` satisfying

\[
                  E_G(Q,B)\ne\varnothing,
       \qquad     E_G(Q,H_i)\ne\varnothing\quad(1\le i\le4).     \tag{1.2}
\]

No assumption is made initially about an edge from `Q` to `x`.

If `Q` is adjacent to `x`, put

\[
                              U_0=Q.                              \tag{1.3}
\]

Otherwise choose a shortest path from `Q` to `x` in
`G[U\cup\{x\}]`.  Write it as

\[
                         q p_1p_2\cdots p_k x,
       \qquad q\in Q,\quad p_1,\ldots,p_k\in U-Q,                \tag{1.4}
\]

and put

\[
                       U_0=Q\cup\{p_1,\ldots,p_k\}.              \tag{1.5}
\]

Such a path exists because `G[U]` is connected and `U` is adjacent to
`x`.

## 2. Component absorption

### Theorem 2.1 (five-contact absorption or a full-neighbourhood obstruction)

In the setting above, at least one of the following holds.

1. `G` contains a `K_7` minor, with branch sets described explicitly in
   the proof.
2. There is a spanning labelled `K_7`-minus-one-edge model

   \[
                  \{x\},\ B',\ U_0,\ H'_1,H'_2,H'_3,H'_4        \tag{2.1}
   \]

   with the same branch-set labels, the same protected singleton `{x}`,
   and the same unique missing adjacency `xB'`, such that

   \[
                              |U_0|<|U|.                          \tag{2.2}
   \]

3. Some component `R` of `G[U-U_0]` has

   \[
                         N_G(R)\subseteq U_0\cup\{x\}.           \tag{2.3}
   \]

   Consequently `N_G(R)` is the boundary of an actual separation with
   two nonempty open sides and

   \[
                              |N_G(R)|\ge7.                       \tag{2.4}
   \]

4. The equality `U_0=U` holds.  Necessarily `Q` is anticomplete to `x`,
   and

   \[
                              U-Q=\{p_1,\ldots,p_k\}.             \tag{2.5}
   \]

   Moreover the connector in (1.4) has no shortcut:

   \[
   \begin{aligned}
      E_G(Q,p_j)&=\varnothing &&(2\le j\le k),\\
      xp_j&\notin E(G)       &&(1\le j<k),\\
      p_ip_j&\notin E(G)     &&(|i-j|\ge2).
   \end{aligned}                                                   \tag{2.6}
   \]

   Thus the entire old material outside `Q` is one induced shortest
   connector from `Q` to the protected singleton.

Outcome 2 is a strict host-level descent: the graph is fixed, all seven
label names are retained, and the order of the common branch set carrying
`Q` strictly decreases.

#### Proof

The set `U_0` is nonempty and connected.  It is adjacent to `B` and to
every `H_i` through `Q`, by (1.2), and it is adjacent to `x` either through
an old `Q-x` edge or through the last edge `p_kx` of (1.4).  Therefore

\[
                    \{x\},\ B,\ U_0,\ H_1,H_2,H_3,H_4             \tag{2.7}
\]

is already a labelled `K_7`-minus-one-edge model.  It need not yet be
spanning.

Suppose first that `U_0=U`.  The definition (1.3) cannot apply because
`Q` is a proper subset of `U`.  Hence `Q` is anticomplete to `x`, and
(1.4)--(1.5) give (2.5).  A `Q-p_j` edge for `j>=2`, an edge `xp_j` for
`j<k`, or a chord `p_ip_j` with `|i-j|>=2` would shorten the path (1.4).
This proves (2.6) and outcome 4.

It remains to suppose that `U_0` is a proper subset of `U`.  Let

\[
                           R_1,\ldots,R_m                           \tag{2.8}
\]

be the components of `G[U-U_0]`.  Each `R_j` has an edge to `U_0`,
because `G[U]` is connected.  Different `R_j` are anticomplete.

Process one component `R=R_j` as follows.

* If `R` has an edge to some `H_i`, assign all vertices of `R` to that
  branch set `H_i`.
* Suppose `R` has no edge to any `H_i` but has an edge to `B`.  If `R`
  is anticomplete to `x`, assign all vertices of `R` to `B`.  If `R` is
  also adjacent to `x`, then

  \[
                    \{x\},\quad B\cup R,\quad U_0,
                    \quad H_1,H_2,H_3,H_4                         \tag{2.9}
  \]

  are seven branch sets of a `K_7`-minor model.  Indeed, `B\cup R` is
  connected through an `R-B` edge; it is adjacent to `x` through an
  `x-R` edge and to `U_0` through the old `B-Q` edge; `U_0` is adjacent
  to `x`, `B`, and every `H_i`; and every remaining adjacency is inherited
  from (1.1).  This is outcome 1.
* Suppose finally that `R` has no edge to `B` or to any `H_i`.  Since the
  model (1.1) is spanning and the sets in (2.8) are distinct components
  of `G[U-U_0]`, every neighbour of `R` lies in `U_0\cup\{x\}`.  This is
  (2.3).  The connected set `R` is nonempty, while the nonempty branch set
  `B` lies outside `R\cup N_G(R)`.  Hence its full neighbourhood is the
  boundary of an actual separation.  Seven-connectivity proves (2.4),
  giving outcome 3.

Assume that neither outcome 1 nor outcome 3 occurred.  Enlarge each
`H_i` by all components assigned to it, and enlarge `B` by all components
assigned to `B`; call the resulting sets `H'_i` and `B'`.  Every enlarged
set is connected because each assigned component has an edge to its target
old branch set.  The sets are pairwise disjoint, and together with `{x}`
and `U_0` they partition `V(G)`.

All old adjacencies among `B,H_1,...,H_4` survive.  The edges from `Q` to
`B,H_1,...,H_4` give every required adjacency from `U_0` to the enlarged
foreign branch sets.  The old edges from `x` to each `H_i` survive, and
`x` is adjacent to `U_0` by construction.  Finally `x` is anticomplete to
`B'`: it was anticomplete to `B`, and a component was assigned to `B`
only when it was anticomplete to `x`.  Thus (2.1) is the same labelled
near-complete model with its same unique missing pair.  Since `U_0` is a
proper subset of `U`, (2.2) holds.  This is outcome 2. \(\square\)

## 3. Application to a proper paired rejection kernel

The following corollary states exactly what Theorem 2.1 adds to the
total-rejection reduction.

### Corollary 3.1 (label-preserving transfer from a proper kernel)

Assume in addition that `G` satisfies

\[
 \chi(G)=7,\qquad K_7\npreccurlyeq G,
 \qquad\text{and every proper minor of }G\text{ is six-colourable}. \tag{3.1}
\]

Suppose the full shore called `D` in the total boundary-trace rejection
theorem is exactly the common branch set `U` in (1.1).  Let `K` be one of
the proper connected induced list-critical subgraphs returned in the
paired-rejection alternative, and let `Q` be a component of `G[U-V(K)]`
selected by the strict-transfer theorem.  Assume that (1.2) holds.

Then either:

1. `G` has a `K_7` minor;
2. the same rejected connected component `Q` is contained in a common
   branch set of a spanning labelled `K_7`-minus-one-edge model with the
   same protected singleton and all the same labels, and that common
   branch set has order strictly smaller than `U`;
3. a connected subgraph of the old common branch set has a full
   neighbourhood of order at least seven contained in the new common
   branch set together with `{x}`; or
4. `U-Q` is the shortest protected-singleton connector in (2.5)--(2.6).

The rejected trace on `N_G(Q)` is unchanged in outcomes 2--4, because the
proof merely reallocates vertices among branch sets of the same graph.

If the critical subgraph `K` is not a path (a singleton is allowed as a
degenerate path), then outcome 4 is impossible.  Consequently every such
nonpath proper kernel yields one of outcomes 1--3, and outcome 2 is a
strict label-preserving descent.

#### Proof

The strict-transfer theorem makes `Q` a nonempty connected proper subset
of `U`.  Its rejection certificate is a statement about the unchanged
induced subgraph on `Q` and its literal full neighbourhood.  Theorem 2.1
therefore applies directly, and branch-set reassignment cannot alter that
certificate.

For the final assertion, `K` is disjoint from `Q` and hence lies in
`U-Q`.  In outcome 4, equations (2.5)--(2.6) say that `G[U-Q]` is an
induced path.  Since `K` is connected and induced in `G[U]`, its induced
subgraph is a connected induced subgraph of that path, and is therefore
itself a path.  The contrapositive proves the claim. \(\square\)

## 4. Exact trust boundary

The theorem proves a strict, label-preserving model descent without
identifying palette colours with model labels.  Its five-contact hypothesis
is literal: the selected component itself must meet `B` and each of the
four other common branch sets.

It does **not** prove that an arbitrary component returned by a proper
paired rejection kernel satisfies (1.2).  It also does not bound the
separator in outcome 3 above by seven, furnish compatible colourings of
its two closed shores, or eliminate the shortest protected-singleton
connector in outcome 4 when the critical kernel is a path.  Those are the
precise residuals after the branch-set absorption mechanism.

## 5. Dependencies

- [total rejection of a fixed boundary trace](../results/hc7_total_trace_rejection_kernel.md),
  for the proper paired kernel and its smaller rejected component;
- the definition of a spanning labelled `K_7`-minus-one-edge model.
