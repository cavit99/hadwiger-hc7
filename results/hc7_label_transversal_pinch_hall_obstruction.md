# Hall obstruction at a label-transversal critical pinch

**Status:** written proof; separate internal audit GREEN in
[`hc7_label_transversal_pinch_hall_obstruction_audit.md`](hc7_label_transversal_pinch_hall_obstruction_audit.md).
This theorem gives the exact unbounded residue at the label-transversal
order-seven outcome of the two-owner portal-linkage theorem.  It does not
prove that the retained labelled branch-set remnants form connected
supports, and it does not prove `HC_7`.

## 1. Setting

Let `G` be seven-connected and `K_7`-minor-free, with

\[
 \chi(G)=7,
 \qquad\text{and every proper minor and proper edge-deleted subgraph of
 }G\text{ six-colourable}.                              \tag{1.1}
\]

Suppose a spanning labelled `K_7`-minus-one-edge model has a branch set
`U`, and that a nonempty connected set `L subseteq U` satisfies

\[
 S=N_G(L),\qquad |S|=7,                                 \tag{1.2}
\]

where `S` consists of one vertex `s in U` and one literal vertex from each
of the other six branch sets.  Assume that the retained part of `U` is
nonempty and lies outside `L union S`.  Thus, with

\[
 R=V(G)-(L\cup S),                                      \tag{1.3}
\]

the sets `L,S,R` form an actual two-shore separation and `R` is nonempty.
Fix an edge `s ell` with `ell in L`.

Take a proper six-colouring of `G-s ell`, and let `Pi` be its equality
partition on the literal boundary `S`.  The critical-pinch theorem gives

\[
 \Pi\in\operatorname{Ext}(G[R\cup S],S)
      \setminus\operatorname{Ext}(G[L\cup S],S).        \tag{1.4}
\]

In particular, `Pi` is a legal partition on the intact `R`-side, but not
on the intact `L`-side.

Let `r` be the maximum number of pairwise vertex-disjoint connected
subgraphs of `G[R]` which are adjacent to every literal vertex of `S`.
Choose such subgraphs `P_1,...,P_r`.

Let `W_1,...,W_t` be any further pairwise vertex-disjoint connected
subgraphs in

\[
                  R-\bigcup_{j=1}^rV(P_j),             \tag{1.5}
\]

and assume that the `W_k` are pairwise adjacent.  The family may consist
of connected pieces of the six retained labelled branch sets, but no such
connectivity or adjacency is assumed merely from the labels.

Choose a maximum clique `Q` in the graph induced by the singleton blocks
of `Pi`, and list every block not represented by `Q` as

\[
                         B_1,\ldots,B_d.                \tag{1.6}
\]

For each such block put

\[
 D_Q(B_i)=B_i\cup
   \{q\in Q:E_G(q,B_i)=\varnothing\}.                  \tag{1.7}
\]

Form a bipartite graph with right side `{B_1,...,B_d}` and left side
`{W_1,...,W_t}` by joining `W_k` to `B_i` exactly when `W_k` has a
neighbour at every literal vertex of `D_Q(B_i)`.

## 2. Exact Hall-deficient normal form

### Theorem 2.1

In the setting above,

\[
                              r\in\{1,2\}.              \tag{2.1}
\]

Moreover, for every permitted family `W_1,...,W_t` and every permitted
maximum singleton clique `Q`, there is a nonempty set

\[
                     X\subseteq\{B_1,\ldots,B_d\}       \tag{2.2}
\]

such that

\[
              r+|N_{\{W_1,\ldots,W_t\}}(X)|<|X|.       \tag{2.3}
\]

Consequently

\[
 d>r,qquad |X|\ge r+1,qquad
 |N_{\{W_1,\ldots,W_t\}}(X)|\le |X|-r-1.              \tag{2.4}
\]

In the two sharp lowest-demand cases the conclusion is especially rigid.

1. If `(r,d)=(2,3)`, no `W_k` meets the complete duty set (1.7) of any
   one of the three blocks.
2. If `(r,d)=(1,2)`, no `W_k` meets the complete duty set of either block.

Thus the critical-pinch partition reflects through the displayed
connected supports if and only if the associated incidence graph, after
adjoining the `r` universal full supports, has a matching saturating all
`B_i`.  In a hypothetical counterexample this matching never exists.

### Proof

Every component of `G-S` is adjacent to every vertex of `S`.  Indeed, its
neighbourhood is contained in `S`, and omission of one boundary vertex
would give a separator of order at most six between that component and the
nonempty opposite shore.  In particular, `L` itself is an `S`-full
connected subgraph and `r>=1`.

If `r>=3`, then `L` and three disjoint `S`-full connected subgraphs in
`R` satisfy the adaptive `(1,3)` exact-seven reflection theorem.  It gives
an explicit `K_7`-minor model or a proper six-colouring of `G`, contrary
to the hypotheses.  Hence (2.1) holds.

Adjoin to the displayed incidence graph one universal left vertex for
each `P_j`.  Suppose that the resulting graph has a matching saturating
all blocks `B_i`.  Apply the transported-partition Hall reflection theorem
with its coloured open side equal to `R` and its opposite open side equal
to `L`.  Equation (1.4) supplies the required proper colouring of the
closed `R`-side with exact boundary partition `Pi`; the matched connected
subgraphs supply its partition-specific supports.  The theorem therefore
produces a proper colouring of the closed `L`-side inducing exactly `Pi`.
The two colourings align on `S` and glue, contradicting `chi(G)=7`.

Thus no saturating matching exists.  Hall's theorem gives a nonempty
block family `X` whose full left neighbourhood has order below `|X|`.
Every one of the `r` vertices representing a full support belongs to that
neighbourhood, and its remaining members are exactly
`N_{\{W_1,...,W_t\}}(X)`.  This is (2.3), and (2.4) follows.

If `d=r+1`, applying (2.3) shows that `X` must have order `r+1` and have
no neighbour among the `W_k`: a smaller `X` already has the `r` universal
neighbours.  Hence no `W_k` is eligible for any block.  Substituting
`(r,d)=(2,3)` and `(1,2)` proves the two final assertions. `\square`

## 3. What the six labels do not supply

The label-transversal boundary does not itself add an edge to the Hall
incidence graph.  After deleting the one boundary representative of a
branch set,

* its retained part may be empty or disconnected;
* an old adjacency between two model branch sets may have used one of the
  deleted boundary representatives; and
* even a connected retained piece need not meet every literal vertex of
  any duty set (1.7).

Therefore a retained labelled piece may be used as a `W_k` only after its
connectedness, disjointness, pairwise adjacency and complete duty contacts
have been checked literally.  The five bichromatic entrance paths from
the critical-pinch theorem lie in the `L`-side up to their first boundary
vertices.  They are consequently on the wrong open shore for reflecting
the legal `R`-side partition in (1.4).

The theorem leaves an exact operation-specific residue: a Hall-deficient
family of boundary blocks together with labelled pieces which miss the
corresponding complete duties.  Closing it requires new host geometry or a
different proper-minor response; neither the seven labels nor the five
Kempe entrances alone supply that conclusion.

## 4. Dependencies

- [critical-pinch boundary response](hc7_near_k7_critical_pinch_state.md)
- [adaptive `(1,3)` exact-seven reflection](hc7_exact7_adaptive_packet_reflection.md)
- [transported-partition Hall reflection](hc7_transported_partition_hall_reflection.md)
- [two-owner portal-linkage transfer](hc7_multi_owner_portal_linkage_transfer.md)
