# Boundary-full connected subgraphs make row traces monochromatic

**Status:** written proof; separate internal audit GREEN.  This theorem combines
proper-minor colourings with the five-row reflection theorem.  It gives a
structural sufficient condition for closing a returned separation and
identifies an exact obstruction when that condition fails.  It does not
prove that the obstruction is absent in every degree-seven configuration.

## 1. Setup

Let `G` be a graph which is not six-colourable and every proper minor of
which is six-colourable.  Let

\[
       V(G)=L\mathbin{\dot\cup}T\mathbin{\dot\cup}R,
       \qquad E_G(L,R)=\varnothing,                            \tag{1.1}
\]

where both open sides are nonempty.  Fix `a in T`.  Suppose that
`G[R union T]-a` contains five pairwise disjoint connected subgraphs

\[
                             Q_1,\ldots,Q_5                     \tag{1.2}
\]

which are pairwise adjacent and satisfy

\[
 T\subseteq\{a\}\cup\bigcup_{i=1}^5V(Q_i),
 \qquad E_G(a,Q_i)\ne\varnothing\quad(1\le i\le5).             \tag{1.3}
\]

Put

\[
                              I_i=T\cap V(Q_i).                 \tag{1.4}
\]

A connected subgraph `P subseteq L` is **`T`-full** if it is adjacent to
every literal vertex of `T`.

Define the **row-trace conflict graph** `K_T` on the indices for which
`|I_i|>=2` by putting `ij in E(K_T)` precisely when an edge of `G[T]`
joins a vertex of `I_i` to a vertex of `I_j`.  Singleton row traces need
no connected subgraph to make them monochromatic, so they are deliberately
absent from `K_T`.  This definition is used only when every individual
`I_i` is independent.

## 2. Reflection using boundary-full connected subgraphs

### Theorem 2.1

Assume that each nonempty `I_i` is independent.  Suppose that `L` contains
`k` pairwise vertex-disjoint `T`-full connected subgraphs and

\[
                              \chi(K_T)\le k.                    \tag{2.1}
\]

If some row `Q_i` misses `T`, then `G` is six-colourable.

### Proof

Let `P_1,...,P_k` be the disjoint `T`-full connected subgraphs.  Properly
colour `K_T` with at most `k` colours.  For each used colour `h`, put

\[
                   J_h=\bigcup\{I_i:i\text{ has colour }h\}.    \tag{2.2}
\]

Each `J_h` is independent: its constituent sets are independent by
hypothesis, and the colouring of `K_T` excludes every edge between two
constituent sets assigned the same colour.  The nonempty sets `J_h` are
pairwise disjoint because the rows are disjoint.

If there is no used colour, then every row trace is a singleton or empty.
Delete any vertex of the nonempty open side `L`, colour the resulting
proper minor, and restrict its colouring to the unchanged graph
`G[R union T]`.  Every row trace is automatically monochromatic, and the
assumed boundary-free row supplies the second reflection hypothesis.  The
five-row reflection theorem applies immediately.  We may therefore assume
below that some `J_h` is nonempty.

For every used colour `h`, the set

\[
                              X_h=P_h\cup J_h                   \tag{2.3}
\]

is connected.  Indeed, `P_h` is connected and has a neighbour at every
literal vertex of `J_h`.  The sets `X_h` are pairwise disjoint.  They are
also pairwise adjacent: if `h ne ell`, choose any `t in J_ell`; fullness
gives an edge from `P_h` to `t subseteq X_ell`.  Finally each `X_h` is
adjacent to `a`, again by fullness.

Contract a spanning tree of every `G[X_h]`.  This produces a proper minor,
because some `J_h` is nonempty and the corresponding `X_h` contains an
edge between `P_h` and `J_h`.  Take a proper six-colouring of the minor.

The contracted representatives are pairwise adjacent and each is adjacent
to `a`, so they receive pairwise distinct colours, all different from the
colour of `a`.  Keep the minor colouring on every unchanged vertex of
`(R union T)-bigcup_h J_h`, and give every literal vertex of `J_h` the
colour of the representative of `X_h`.  This is a proper colouring of
`G[R union T]`: each `J_h` is independent; every edge from `J_h` to an
unchanged vertex of `(R union T)-bigcup_h J_h` survived at the contracted
representative; and different sets `J_h` receive distinct colours.  Call
the resulting colouring `psi`.

For every `i`, a nonsingleton trace `I_i` is contained in one `J_h` and is
therefore monochromatic in `psi`; singleton and empty traces have the same
property automatically.  The assumed boundary-free row supplies
the second alternative in the five-row reflection theorem.  That theorem
reflects the equality partition of `psi` through the opposite shore and
glues the two six-colourings, contrary to the hypothesis on `G`.
\(\square\)

## 3. Consequences in a `K_7`-minor-free host

### Lemma 3.1 (one row must miss the boundary)

Assume in addition that `L` contains a `T`-full connected subgraph and
that `G` has no `K_7` minor.  Then `I_i` is empty for some `i`.

### Proof

If every `I_i` were nonempty, let `P subseteq L` be `T`-full.  The seven
sets

\[
                         P,\quad\{a\},\quad Q_1,\ldots,Q_5     \tag{3.1}
\]

would be disjoint and connected.  The five rows are pairwise adjacent;
`a` is adjacent to each row by (1.3); `P` is adjacent to `a` and to each
row through a vertex of its nonempty trace `I_i`.  Hence (3.1) is an
explicit `K_7`-minor model, a contradiction.  \(\square\)

### Corollary 3.2 (conflict-capacity obstruction)

Under the hypotheses of Lemma 3.1, let `nu_L(T)` be the maximum number of
pairwise disjoint `T`-full connected subgraphs in `L`.  If every nonempty
row trace is independent, then

\[
                              \chi(K_T)>\nu_L(T).                \tag{3.2}
\]

In particular:

1. if the union of all nonempty row traces is independent, then `G` is
   six-colourable;
2. if `L` contains two disjoint `T`-full connected subgraphs, then every
   surviving independent-trace conflict graph is nonbipartite; and
3. if at most one row has more than one boundary vertex and its trace is
   independent, then `G` is six-colourable.

### Proof

Lemma 3.1 supplies a boundary-free row.  If (3.2) failed, Theorem 2.1 with
`k=nu_L(T)` would six-colour `G`.

For item 1, `K_T` is edgeless and one full connected subgraph suffices.
For item 2, a bipartite conflict graph has chromatic number at most two.
For item 3, `K_T` has at most one vertex and hence chromatic number at most
one; apply Theorem 2.1.  \(\square\)

## 4. Exact remaining obstruction

For a connected full open side, the unresolved row-multicolouring event is
therefore not arbitrary.  At least one of the following must hold:

1. some literal row trace `T intersect Q_i` contains an edge, so no proper
   colouring can make that trace monochromatic; or
2. the independent row traces have a conflict graph whose chromatic number
   is larger than the number of disjoint `T`-full connected subgraphs on
   the opposite shore.

This is a host-level obstruction.  It uses an actual proper minor to
manufacture the far-shore colouring, and every contracted set contains a
literal full connected subgraph plus independent boundary vertices.  It
does not infer that case 1 yields a branch-set split, or that the conflict
graph in case 2 has a fixed two-vertex transversal.  Those are the next
dynamic steps.

## 5. Dependencies

- [five-row reflection across a separation](../results/hc7_five_row_separator_reflection.md)
