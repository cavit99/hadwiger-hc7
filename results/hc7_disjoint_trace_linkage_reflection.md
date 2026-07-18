# Disjoint trace linkages make every row trace monochromatic

**Status:** written proof; separate internal audit GREEN.  This theorem is
parameter-uniform.  It replaces boundary-full connected subgraphs by
connected subgraphs tailored to the individual boundary traces.  It does not
prove that the required disjoint linkage exists.

## 1. Setup

Let `G` be a graph which is not six-colourable and every proper minor of
which is six-colourable.  Let

\[
       V(G)=L\mathbin{\dot\cup}T\mathbin{\dot\cup}R,
       \qquad E_G(L,R)=\varnothing,
\]

where both open sides are nonempty.  Fix `a in T`.  Suppose that
`G[R union T]-a` contains five pairwise disjoint connected subgraphs

\[
                         Q_1,\ldots,Q_5
\]

which are pairwise adjacent, each is adjacent to `a`, and

\[
             T\subseteq\{a\}\cup\bigcup_{i=1}^5V(Q_i).
\]

Put `I_i=T intersect V(Q_i)` and assume that some `I_i` is empty.

## 2. Simultaneous trace-linkage theorem

### Theorem 2.1

Assume that every nonempty `I_i` is independent.  For each index `i` with
`|I_i|>=2`, suppose there is a connected subgraph

\[
                         X_i\subseteq G[L\cup I_i]
\]

containing every vertex of `I_i`, and suppose that the subgraphs `X_i` are
pairwise vertex-disjoint.  Then `G` is six-colourable.

### Proof

First suppose there is at least one nonsingleton trace.  Contract a spanning
tree of every `X_i`.  The contractions are simultaneous because the sets
`X_i` are pairwise disjoint.  They produce a proper minor: a connected graph
containing two distinct vertices has an edge, so at least one edge is
contracted.  Proper-minor criticality gives a proper six-colouring of the
resulting graph.

For each contracted set `X_i`, let `x_i` be its representative.  Define a
colouring `psi` of the unchanged far closed shore `G[R union T]` as follows.
Every vertex outside the nonsingleton traces keeps its colour from the minor,
and every literal vertex of `I_i` receives the colour of `x_i`.

This is proper.  Each `I_i` is independent.  If an edge joins `I_i` to
`I_j`, then the contraction representatives `x_i,x_j` are adjacent in the
minor and hence have different colours.  If an edge joins a vertex of `I_i`
to an unchanged vertex of `G[R union T]`, the corresponding edge from `x_i`
survives in the minor, so its ends again have different colours.  All other
edges are unchanged.

Thus every row trace is monochromatic in `psi`: the nonsingleton traces by
construction, and the singleton and empty traces automatically.  The
boundary-free row supplies the second alternative in the five-row reflection
theorem.  That theorem reflects the equality partition of `psi` through the
opposite shore and glues the two six-colourings, contradicting the hypothesis
that `G` is not six-colourable.

If there is no nonsingleton trace, delete any vertex of the nonempty side
`L`, colour the resulting proper minor and restrict the colouring to
`G[R union T]`.  Every trace is already monochromatic, so the same reflection
argument applies.  \(\square\)

## 3. The first two-pair consequence

### Corollary 3.1

Suppose the only nonsingleton row traces are two disjoint independent pairs

\[
                         I=\{x_1,x_2\},\qquad
                         J=\{y_1,y_2\}.
\]

If `G[L union I union J]` contains vertex-disjoint paths joining `x_1` to
`x_2` and `y_1` to `y_2`, then `G` is six-colourable.

### Proof

Trim each path at its first and last named endpoint.  Its internal vertices
then lie in `L`; the two paths are connected subgraphs of the form required
by Theorem 2.1.  \(\square\)

Consequently a non-six-colourable instance with these two pair traces has no
such linkage.  Assume additionally that `G` is seven-connected and `|T|=7`.
The closed-shore rooted-connectivity theorem says that

\[
                   (G[L\cup I\cup J], I\cup J)
\]

is internally four-connected.  Fabila-Monroy and Wood's Two Paths lemma
first puts this graph in a web with frame
`(x_1,y_1,x_2,y_2)`, up to reversal.  Any actual vertex in an attachment
behind a facial triangle would be separated from all four roots by at most
three vertices, contrary to rooted internal four-connectivity.  Every such
attachment is therefore empty of actual vertices.  Removing the auxiliary
completion edges leaves a disc embedding of the literal host graph with the
four roots in the displayed alternating order.  Completion edges are not
treated as host edges.

## 4. Trust boundary

- The theorem requires one pairwise disjoint connected subgraph for every
  nonsingleton trace.  Intersecting paths cannot simply be contracted, since
  that may identify boundary vertices joined by an edge.
- The theorem does not construct a linkage from Kempe connectivity.
- The disc alternative in Corollary 3.1 is not terminal.  The three omitted
  boundary vertices and the five named far-side subgraphs must still be used
  to produce an explicit `K_7` model, a common boundary partition, a fixed
  two-vertex `K_5`-model transversal, or a strict host-level reduction.

## 5. Dependencies

- [five-row separator reflection](hc7_five_row_separator_reflection.md)
- [closed-shore rooted connectivity](hc7_closed_shore_rooted_connectivity.md)

The web implication uses Lemma 2 of R. Fabila-Monroy and D. R. Wood,
*Rooted `K_4`-Minors*, Electronic Journal of Combinatorics 20(2) (2013),
P64, <https://doi.org/10.37236/3098>.
