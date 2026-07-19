# Two entrance-edge ordered paths or an order-seven separation

**Status:** written proof; separate internal audit GREEN in
[`hc7_entrance_edge_ordered_two_path_or_order7_audit.md`](hc7_entrance_edge_ordered_two_path_or_order7_audit.md).

This note gives a sharp host-level replacement for the false assertion that
seven-connectivity alone forces two arbitrary ordered three-vertex paths.
It preserves two nominated entrance edges exactly.  It does not construct
two arbitrary three-terminal Steiner subgraphs, and the returned separation
does not automatically carry compatible closed-shore colourings.

## Theorem 1 (entrance-edge ordered-two-path alternative)

Let `G` be a seven-connected graph.  Let

\[
                 x_0,x_1,x_2,y_0,y_1,y_2
\]

be six distinct vertices such that

\[
                         x_0x_1,y_0y_1\in E(G).        \tag{1.1}
\]

At least one of the following holds.

1. There are vertex-disjoint paths `P_x,P_y` such that `P_x` starts with
   the edge `x_0x_1` and ends at `x_2`, while `P_y` starts with the edge
   `y_0y_1` and ends at `y_2`.  Thus the two paths encounter the nominated
   triples in the orders

   \[
                          x_0,x_1,x_2
             \quad\hbox{and}\quad y_0,y_1,y_2.         \tag{1.2}
   \]
2. The graph `G` has an actual separation of order seven whose boundary
   contains `x_0,y_0`.

In outcome 2 every component of the complement of the boundary is adjacent
to every literal boundary vertex.

### Proof

Put

\[
                            J=G-\{x_0,y_0\}.            \tag{1.3}
\]

Deleting two vertices from a seven-connected graph leaves a five-connected
graph.  Hence `J` is five-connected.

If `|V(J)|=6`, then `|V(G)|=8`; seven-connectivity makes `G=K_8`, and the
two required paths can be chosen directly.  We may therefore assume
`|V(J)|>=7`.

Suppose first that `J` is six-connected.  Jung's two-linkage theorem says
that every six-connected graph is two-linked.  Apply it in `J` to

\[
                             (x_1,x_2),\qquad(y_1,y_2). \tag{1.4}
\]

It gives vertex-disjoint paths `Q_x,Q_y` joining the nominated pairs.
Since `x_0,y_0` do not belong to `J`, adjoining `x_0x_1` to `Q_x` and
`y_0y_1` to `Q_y` gives outcome 1.

It remains that `J` is not six-connected.  Since `J` is five-connected
and has at least seven vertices, there is a separation

\[
                        V(J)=A\mathbin{\dot\cup}T
                                  \mathbin{\dot\cup}B,
              \qquad |T|=5,\quad A,B\ne\varnothing,   \tag{1.5}
\]

with no `A`--`B` edge.  Then

\[
                            S=T\cup\{x_0,y_0\}          \tag{1.6}
\]

has order seven.  Deleting `S` from `G` leaves nonempty vertices in both
`A` and `B`, with no edge between the two sets, so `S` is the boundary of
an actual order-seven separation.

Finally let `C` be a component of `G-S`.  If `C` missed some member `s` of
`S`, then

\[
                              N_G(C)\subseteq S-\{s\},
\]

giving a vertex cut of order at most six.  This contradicts
seven-connectivity.  Hence every such component is adjacent to every
literal member of `S`. \(\square\)

## Corollary 2 (one prescribed routing demand)

Suppose a branch-set exchange or a selected proper-minor response has
already supplied two vertex-disjoint literal entrance edges `x_0x_1` and
`y_0y_1`.  Let `x_2,y_2` be two further vertices such that

\[
                   x_0,x_1,x_2,y_0,y_1,y_2
\]

are pairwise distinct.  If the intended exchange requires only one ordered
continuation from each entrance edge to `x_2,y_2`, then Theorem 1 either
supplies both continuations simultaneously or returns an actual full
order-seven boundary containing the two outside ends `x_0,y_0`.

Thus an obstruction involving one prescribed continuation per entrance
edge is a two-linkage problem after deleting the outside ends; it is not a
new colour-allocation problem.  In an `HC_7` application, however, the
order-seven outcome is terminal only after operation-specific proper-minor
colourings are shown to induce one common complete equality partition on
that literal boundary.

## Trust boundary for two-demand connected subgraphs

Theorem 1 must not be read as a theorem about two arbitrary connected
subgraphs each required to meet three terminal sets.

1. Each output is a **path** with one fixed initial edge and one nominated
   terminal vertex.  The theorem does not allocate two independently
   prescribed terminal labels beyond that ordered triple.
2. The two paths are disjoint.  They do not model two connected subgraphs
   which may branch internally to meet several demand sets.
3. The theorem preserves literal vertices, not ownership by five inherited
   branch sets.  It supplies no rainbow first-hit allocation.
4. The returned order-seven separation is structural.  It does not retain
   a selected boundary equality partition, a list-critical kernel, or a
   boundary-labelled near-`K_7` model unless those facts are proved
   separately.
5. The result uses no `K_7`-minor exclusion and no contraction-critical
   colouring response.  Those hypotheses must be spent in the subsequent
   model construction or colouring-gluing step.

The adjacent barrier
[`hc7_p3_union_p3_linkage_barrier.md`](../barriers/hc7_p3_union_p3_linkage_barrier.md)
shows that the separation outcome cannot be omitted even when `G` is
`K_7`-minor-free.

## External input

The linkage input is Jung's theorem that every six-connected graph is
two-linked:

> H. A. Jung, “Eine Verallgemeinerung des n-fachen Zusammenhangs für
> Graphen,” *Mathematische Annalen* **187** (1970), 95--103.

A convenient traceable modern restatement is Theorem 1.1 of C. Stephens
and D. Ye, “Connectivity for Kite-Linked Graphs,” arXiv:1912.02873, which
states the six-connected two-linkage theorem and cites Jung as its original
source.
