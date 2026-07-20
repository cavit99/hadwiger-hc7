# Contraction-critical responses at a non-triangle edge of the boundary forest

**Status:** written proof; [separately audited GREEN](hc7_order8_forest_edge_response_localization_audit.md).  This is an
unbounded conditional response lemma.  It does not prove `HC_7`.

## 1. Setting

Let

\[
 V(G)=E\mathbin{\dot\cup}D\mathbin{\dot\cup}
       R_0\mathbin{\dot\cup}R_1\mathbin{\dot\cup}S,
 \qquad S=\{d,e\}\mathbin{\dot\cup}F,
 \qquad |F|=6.                                           \tag{1.1}
\]

Assume that `E,D,R_0,R_1` are nonempty connected vertex sets.  Suppose
`d,e` are nonadjacent and that there are four distinct vertices
`x_d,y_d,x_e,y_e` in `F` for which

\[
                 d x_d y_d d,
             \qquad e x_e y_e e                       \tag{1.2}
\]

are triangles.  Assume the normalized conclusion of the GREEN-audited
[cycle-completion theorem](../results/hc7_adjacent_full_pair_cycle_completion.md):

\[
 G[F]\text{ is a forest},\qquad
 N_G(d)\cap S=\{x_d,y_d\},\qquad
 N_G(e)\cap S=\{x_e,y_e\}.                            \tag{1.3}
\]

The four sets in (1.1) partition `V(G)-S`; their contact and adjacency
properties are not needed for the lemma below, only their literal identities.

Finally assume

\[
 \chi(G)=7,qquad
 \chi(M)\le6\text{ for every proper minor }M\text{ of }G.            \tag{1.4}
\]

## 2. Five bichromatic responses must leave the boundary

### Theorem 2.1 (forest-edge response localization)

Let

\[
             xy\in E(G[F])-\{x_dy_d,x_ey_e\}.          \tag{2.1}
\]

Every proper six-colouring `c` of `G-xy` has

\[
                              c(x)=c(y)=\alpha.         \tag{2.2}
\]

All six colours occur.  For each of the five other colours `beta`, the
subgraph induced by colours `\{alpha,beta\}` contains an `x`--`y` path
`P_beta`.  Every such path has an internal vertex outside `S`.

Orient each `P_beta` from `x` to `y`, and let

\[
 \lambda(\beta)\in\{E,D,R_0,R_1\}                     \tag{2.3}
\]

be the unique part containing its first vertex outside `S`.  Then
`lambda` is not injective.  More precisely, there are distinct alternate
colours `beta,gamma` such that both paths first leave `S` into the same
named part.  The two paths can intersect only at vertices coloured
`alpha`; in particular, if their first outside vertices coincide, that
common vertex has colour `alpha`.

#### Proof

The graph `G-xy` is a proper minor and hence is six-colourable.  If the
ends of the deleted edge had different colours, restoring `xy` would give a
proper six-colouring of `G`.  This proves (2.2).

Moreover `\chi(G-xy)=6`.  Otherwise a colouring of `G-xy` with at most five
colours could be extended to a six-colouring of `G` by assigning one end of
`xy` one new colour.  Thus every proper six-colouring under consideration
uses all six colours.

Fix an alternate colour `beta`.  If `x,y` belonged to different components
of the `alpha`--`beta` subgraph, interchange those two colours on the
component containing `x`.  The resulting colouring is proper, gives `x,y`
different colours, and remains proper after restoring `xy`.  This would
six-colour `G`, a contradiction.  Hence an `x`--`y` path `P_beta` exists in
that bichromatic subgraph.

Because `G[F]` is a forest, deleting `xy` puts `x,y` in different
components of `G[F]-xy`.  By (2.1), the edge `x_dy_d` remains present, so
the two neighbours of `d` in `S` lie in one component of `G[F]-xy`.
Adding `d` therefore does not join two components of that graph.  The same
argument applies to `e` and the retained edge `x_ey_e`; the roots have no
other neighbours in `S` by (1.3), and `de` is absent.  It follows that
`x,y` remain disconnected in `G[S]-xy`.  Every `P_beta` consequently has
an internal vertex outside `S`.

The four named sets partition `V(G)-S`, so the first outside vertex of each
path determines (2.3).  There are five alternate colours and four named
parts; the pigeonhole principle gives distinct `beta,gamma` with
`lambda(beta)=lambda(gamma)`.

Finally a vertex common to `P_beta` and `P_gamma` has a colour in both
`\{alpha,beta\}` and `\{alpha,gamma\}`.  Since `beta` and `gamma` are
distinct, its colour is `alpha`.  This proves the last assertion. \(\square\)

## 3. Exact gain and trust boundary

The static two-rooted-triangle forest normal form is already GREEN-audited;
this note adds the first operation-specific consequence of every additional
forest edge.  Deleting that edge yields five colour-indexed paths which must
leave the literal boundary, and two of them first enter the same one of the
four named connected sets.

This first-hit collision is not yet a connected-set split.  The two paths
may share `alpha`-coloured vertices, may leave and re-enter the named part,
and need not preserve the other branch-set contacts after a rerouting.  The
theorem therefore does not produce a `K_7`-minor model, a compatible
order-seven separation, or a strict response-preserving descent.  When

\[
                       E(G[F])=\{x_dy_d,x_ey_e\},       \tag{3.1}
\]

there is no non-triangle forest edge to which the theorem applies.

The remaining host-level problem is precisely to use contraction-critical
responses inside the repeated first-hit part to obtain a label-preserving
split, or else to expose a full neighbourhood of order seven with a common
boundary equality partition.

## 4. Dependency

- [Cycle completion from two connected shores, especially Corollaries 3.2
  and 3.5](../results/hc7_adjacent_full_pair_cycle_completion.md).
