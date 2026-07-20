# An isolated required boundary set gives literal crossing paths or descent

**Archive note:** author-checked but not independently audited; retained for
provenance and not part of the current proof spine.

**Status:** written proof; author self-check in
[`hc7_order8_isolated_required_set_crossing_or_descent_self_audit.md`](hc7_order8_isolated_required_set_crossing_or_descent_self_audit.md);
independent audit pending.  This is an unbounded lemma for one of the two
low-demand Hall forms in the positive-excess order-eight interface.  It
does not close the other Hall form or prove `HC_7`.

## 1. Literal crossing lemma

Let `G` be a seven-connected graph satisfying

\[
 \chi(G)=7,
 \qquad \chi(M)\le 6\text{ for every proper minor }M\text{ of }G.
 \tag{1.1}
\]

Let `E` be a connected set of order at least two, put

\[
                         B=N_G(E),
 \qquad                    |B|\ge9,                 \tag{1.2}
\]

and suppose that `E` is a component of `G-B`.  Suppose another component
of `G-B` contains disjoint connected sets `Q_0,Q_1`.  Let
`w_0,w_1 in B` be distinct and assume

\[
\begin{array}{c|cc}
 &w_0&w_1\\ \hline
Q_0&\text{misses}&\text{meets}\\
Q_1&\text{meets}&\text{misses}.
\end{array}                                           \tag{1.3}
\]

Here *meets* means that the displayed connected set has a literal
neighbour at the displayed vertex, and *misses* means that it has none.
A **literal `Q_1,Q_0`-labelled crossing pair** is a pair of
vertex-disjoint paths

\[
 u_0w_0q_1,
 \qquad
 u_1w_1q_0,                                           \tag{1.4}
\]

where `u_0,u_1 in E` are distinct, `q_i in Q_i`, and every displayed
adjacency is an edge of `G`.  The labels in this definition are the actual
sets `Q_0,Q_1`; they are not palette colours.

### Theorem 1.1 (crossing pair or strict response descent)

Under the hypotheses above, at least one of the following holds.

1. There is a literal `Q_1,Q_0`-labelled crossing pair.
2. There is a nonempty connected set `A subsetneq E` such that

   \[
                              |N_G(A)|=7,             \tag{1.5}
   \]

   and `N_G(A)` is the boundary of an actual separation.  Deleting an
   `A`--`N_G(A)` edge supplies a generic exact-seven response interface.
3. There is a nonempty connected set `A subsetneq E` such that

   \[
                         8\le |N_G(A)|<|B|,           \tag{1.6}
   \]

   and deleting an `A`--`N_G(A)` edge supplies a strict boundary-order
   response descent from `B`.

### Proof

For `i in {0,1}`, put

\[
                         X_i=N_G(w_i)\cap E.          \tag{1.7}
\]

Both sets are nonempty because `w_i in B=N_G(E)`.  Apply Hall's theorem
to the two-set family `X_0,X_1`.  If it has distinct representatives
`u_0 in X_0`, `u_1 in X_1`, choose

\[
 q_1\in N_G(w_0)\cap Q_1,
 \qquad
 q_0\in N_G(w_1)\cap Q_0,                            \tag{1.8}
\]

which exist by (1.3).  The six vertices displayed in (1.4) are distinct:
`u_0,u_1` are distinct vertices of `E`, `w_0,w_1` are distinct boundary
vertices, and `q_0,q_1` lie in the disjoint sets `Q_0,Q_1` in a different
component of `G-B`.  Thus the two length-two paths are vertex-disjoint,
giving outcome 1.

Suppose instead that the two-set family has no distinct representatives.
Since both sets are nonempty, the exact two-set Hall obstruction is

\[
                         X_0=X_1=\{u\}               \tag{1.9}
\]

for one vertex `u in E`.  Because `|E|>=2`, the graph `G[E-u]` has a
component `A`.  Connectedness of `G[E]` gives

\[
                         N_G(A)\cap E=\{u\}.          \tag{1.10}
\]

Every neighbour of `A` outside `E` belongs to `B`, because `E` is a
component of `G-B`.  Neither `w_0` nor `w_1` has a neighbour in `A`, by
(1.9).  Consequently

\[
 N_G(A)\subseteq \{u\}\mathbin{\dot\cup}
                         (B-\{w_0,w_1\}),
 \qquad
 |N_G(A)|\le |B|-1.                                  \tag{1.11}
\]

The boundary in (1.11) is an actual separator.  The set `A` is nonempty,
while the component of `G-B` containing `Q_0,Q_1` survives outside
`A union N_G(A)`.  Seven-connectivity and (1.11) therefore give

\[
                         7\le |N_G(A)|<|B|.           \tag{1.12}
\]

Choose an edge `xy` with `x in A` and `y in N_G(A)`; for example, one may
take an `A`--`u` edge supplied by (1.10).  By (1.1), `G-xy` has a proper
six-colouring `psi`.  Its ends have one common colour, since otherwise the
edge could be restored and `G` would be six-colourable.  The restriction
of `psi` to `G-A` is proper, and its restriction to
`G[A union N_G(A)]-xy` is proper.  The equality partition induced on
`N_G(A)` cannot extend through the intact graph
`G[A union N_G(A)]`: such an extension could be aligned, block by literal
block, with `psi|G-A` and glued to a proper six-colouring of `G`.

Thus `A,N_G(A);xy,psi` is a full-neighbourhood response side.  Equality
in the lower bound of (1.12) is outcome 2; every larger value is outcome
3. \(\square\)

## 2. Entry from the isolated required-set Hall form

Assume outcome 3 of the audited
[positive-excess normal form](../results/hc7_order8_positive_excess_frozen_outer_shore.md).
If one required boundary set is met by neither `Q_0` nor `Q_1`, that
theorem supplies distinct `w_0,w_1 in W` satisfying (1.3).  The identity

\[
                     W=N_G(E)\cap D                  \tag{2.1}
\]

makes both sets in (1.7) nonempty.  In the full ordered two--three
allocation setting, the three-distinct-first-portals lemma gives

\[
                         |N_G(d)\cap E|\ge3,          \tag{2.2}
\]

so in particular `|E|>=2`.  Also

\[
 |B|=|S-\{e\}|+|W|\ge7+2=9.                          \tag{2.3}
\]

All hypotheses of Theorem 1.1 are therefore present.  This proves, with
no identification of colours and branch-set labels, that the isolated
required-set form gives the displayed literal crossing pair or a strict
response descent, with the exact-seven case explicitly separated.

There is one additional demand observation.  Every operation-specific
partition `Sigma` in item 5 of the positive-excess normal form has
full-subgraph demand at least two.  Indeed, `G[C]` is connected and `C` is
adjacent to every literal vertex of `B`.  In the transported-partition
Hall-reflection theorem, use the whole of `C` as one boundary-full support.
A demand-one partition would reflect to the intact `E`-shore, contrary to
the rejection asserted in item 5.  Demand zero is already impossible
because `|B|>=9` and a six-colouring has at most six blocks.  Consequently,
within the stated low-demand analysis, the isolated form occurs at demand
exactly two.

## 3. Exact proof-spine consequence of the crossing pair

The crossing pair is a genuine structural gain, but it is not by itself a
`K_7`-minor model or a contact-improving repartition of `C`.

Put

\[
                       H=G[E\cup\{w_0,w_1\}].         \tag{3.1}
\]

The graph `H` is connected.  The three connected subgraphs

\[
                         H,\quad Q_0,\quad Q_1        \tag{3.2}
\]

are pairwise disjoint and pairwise adjacent: the two crossing paths give
the `H`--`Q_i` edges, while the positive-excess normal form gives a
`Q_0`--`Q_1` edge.  Each is adjacent to every literal vertex of `S-{e}`.
Together with the triangle `d x_d y_d d`, they therefore give the six
explicit pairwise adjacent branch sets

\[
                 H,\ Q_0,\ Q_1,\ \{d\},\ \{x_d\},\ \{y_d\}. \tag{3.3}
\]

This is a `K_6` model, not a `K_7` model.  The four-boundary-full-subgraphs
triangle theorem cannot be invoked because (3.2) contains only three
such subgraphs.

Nor does (1.4) add an incidence edge in the Hall-reflection graph.
Incidence is tested on `Q_0,Q_1` themselves and requires a neighbour at
**every** literal vertex of the complete required boundary set.  The new
paths lie outside `C` except for their final vertices and merely repeat
the already known cross-contacts at `w_0,w_1`; neither path proves that a
piece meets the other vertices of the required set.  Hence no existing
audited reflection or branch-set-transfer theorem accepts (1.4) alone as
its positive input.

The exact remaining positive lemma at demand two can be stated without
palette language.  Let `R_1,R_2` be the two literal required boundary
sets.  It is enough to find vertex-disjoint connected subgraphs
`H_0,H_1 subseteq C`, with `P_i subseteq H_i`, and a permutation `pi` of
`{1,2}` such that

\[
 H_i\text{ has a neighbour at every vertex of }R_{\pi(i)}
 \qquad(i=0,1).                                      \tag{3.4}
\]

Indeed, the old edge between `P_0,P_1` makes `H_0,H_1` adjacent.  Every
component of `G[C-(H_0 union H_1)]` may be absorbed into an adjacent one
of the two connected subgraphs.  This yields an adjacent connected
partition of `C` retaining (3.4) and the two protected `S`-full subgraphs.
The resulting two supports saturate the two required sets in the literal
Hall-incidence graph.  Transported-partition reflection then colours the
intact `E`-shore with the selected boundary partition, contradicting its
rejection.

Thus the missing step is a **protected two-support packing** inside `C`,
or a response-preserving separator exposed by failure of that packing.
The two length-two paths in Theorem 1.1 locate opposite literal contacts,
but do not supply the protected connected subgraphs in (3.4).

## 4. Why the second Hall form is different

The second low-demand Hall form need not supply two distinct vertices of
`W`.  Required boundary sets can overlap at singleton-clique vertices.
For example, let the maximum singleton clique contain a vertex `w in W`
which is anticomplete to each of two other colour blocks `C_1,C_2`.  Then

\[
                  w\in R_U(C_1)\cap R_U(C_2).         \tag{4.1}
\]

If `Q_0` meets both complete required sets and `Q_1` misses only `w`, the
two block vertices have combined incidence neighbourhood `{Q_0}`.  Hall
fails, neither block is isolated, and the same single literal vertex `w`
witnesses both absent incidences at `Q_1`.

This is an exact required-set incidence example, not a colour-to-label
interpretation.  It prevents extending Theorem 1.1 to the second Hall form
by simply choosing two distinct `W` witnesses.  That form requires either
an additional literal witness-separation argument or the protected
two-support packing (3.4) directly.

## 5. Dependencies and trust boundary

- [ordered two--three allocation and its three distinct first portals](../results/hc7_order8_ordered_two_three_allocation.md);
- [positive boundary excess reduces to one partitioned opposite shore](../results/hc7_order8_positive_excess_frozen_outer_shore.md); and
- [transported-partition Hall reflection](../results/hc7_transported_partition_hall_reflection.md).

Theorem 1.1 is elementary once the literal cross-witnesses are present.
It uses minor-critical six-colourability only to decorate the smaller full
neighbourhood with a selected response.  It does not use Perfect fan
augmentation: in the isolated form, the exact obstruction to two distinct
`E` feet is already the two-set Hall obstruction (1.9), and that
obstruction gives the strict descent directly.

No common equality partition on the two closed shores of the returned
separator is asserted.  No crossing path is treated as a complete required
boundary set, and no palette colour is identified with `Q_0`, `Q_1`, or a
vertex of `W`.
