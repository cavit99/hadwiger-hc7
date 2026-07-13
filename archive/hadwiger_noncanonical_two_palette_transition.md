# Noncanonical two-palette states at an operated carrier edge

## 1. Setup

Use the flat rigid edge-carrier host from
`hadwiger_seven_view_state_cocycle_exchange.md`.  After switching by the
state word, the carrier vertices are

\[
             X=\{x_1,\ldots,x_n\},\qquad
             Y=\{y_1,\ldots,y_n\},                 \tag{1.1}
\]

and both `X` and `Y` induce `K_n`.  There are `n+2` colours.  The exact
boundary rows are

\[
\begin{array}{c|cc}
t_i&x_i&y_i\\ \hline
0&a,b&b,c,\\
1&b,c&a,c.
\end{array}                                         \tag{1.2}
\]

In addition, rigidity gives the forced nonedges

\[
             c x_i\notin E\quad(t_i=0),
       \qquad b y_i\notin E\quad(t_i=1).            \tag{1.3}
\]

Thus `b` is complete to `X`, `c` is complete to `Y`, a type-zero `x_i`
is the unique kind of `X` vertex which may miss `c`, and a type-one `y_i`
is the unique kind of `Y` vertex which may miss `b`.

Let `e=x_r y_s` be an actual cross-layer edge.  Six-colour `F-e`; in the
general notation below this is an `(n+2)`-colouring.  If `F` is
edge-critical, the ends of `e` have the same colour in every such
colouring.

## 2. Palette distance

Let `Gamma` be the colour set, and put

\[
 P=c(X),\qquad Q=c(Y),\qquad
 O_X=\Gamma-P,\qquad O_Y=\Gamma-Q.                 \tag{2.1}
\]

Both layers are cliques, so

\[
 |P|=|Q|=n,qquad |O_X|=|O_Y|=2.                   \tag{2.2}
\]

Define the palette distance

\[
 d=|O_X-O_Y|=|O_Y-O_X|\in\{0,1,2\}.               \tag{2.3}
\]

Every colour in `P intersect Q` occurs once on each layer.  The two
vertices carrying it are nonadjacent in `F-e`; these pairs form a matching
of order `n-d` in the cross-nonedge relation of `F-e`.

### Theorem 2.1 (complete noncanonical palette classification)

Let `beta=c(b)` and `gamma=c(c)`.  Then `beta in O_X`,
`gamma in O_Y`, and `beta != gamma`.  Moreover:

1. If `d=0`, then `O_X=O_Y={beta,gamma}`.  The common-colour pairs give
   a perfect matching between the two layers.  After retaining the carrier
   palette, one may recolour `a` with the fresh colour of `b`; hence this is
   the canonical separated-palette state even if the displayed colouring
   originally gave `a` a different colour.
2. If `d=1`, write

   \[
   O_X=\{rho,sigma\},\qquad O_Y=\{rho,tau\}.        \tag{2.4}
   \]

   The colour `sigma` occurs on a unique `Y` vertex and `tau` on a unique
   `X` vertex.  At least one of the following holds:

   * `b` has colour `sigma`, and that unique `Y` vertex is a type-one
     `y_i` (the `p` shore missing `b`);
   * `c` has colour `tau`, and that unique `X` vertex is a type-zero
     `x_j` (the `p` shore missing `c`).

   The common-colour pairs give a cross-nonedge matching of order `n-1`.
3. If `d=2`, the colour of `b` is unique to the `Y` palette and occurs on
   a type-one `p` shore, while the colour of `c` is unique to the `X`
   palette and occurs on a type-zero `p` shore.  The common-colour pairs
   give a cross-nonedge matching of order `n-2`.

If the operated edge ends have a common colour, their pair is one edge of
the matching in every case.

#### Proof

The vertex `b` is complete to `X`, so its colour is absent from `P` and
belongs to `O_X`.  Similarly `c` is complete to `Y`, so its colour lies
in `O_Y`.  The edge `bc` makes the two colours distinct.

For `d=0`, the omitted pairs agree.  Since they already contain the two
distinct colours of `b,c`, they are exactly `{beta,gamma}`.

For `d=1`, the only possibilities for the distinct pair
`(beta,gamma)` are

\[
       (sigma,tau),\quad(sigma,rho),\quad(rho,tau). \tag{2.5}
\]

Thus `beta=sigma` or `gamma=tau`.  The colour `sigma` is absent from `X`
but not from `Y`, so it occurs exactly once on the `Y` clique.  If it is
the colour of `b`, that vertex is nonadjacent to `b`; (1.2)--(1.3) force
it to be a type-one `y_i`.  The assertion for `tau` and `c` is symmetric.

For `d=2`, the omitted pairs are disjoint.  Hence every colour of `O_X`
occurs uniquely on `Y`, and every colour of `O_Y` occurs uniquely on `X`.
Apply the same boundary-row argument to `beta` and `gamma`.

Finally `|P intersect Q|=n-d`, and properness pairs equal colours only
across cross-nonedges.  If the operated ends have equal colour, their pair
is among these common-colour pairs. \(\square\)

## 3. Exact canonicalization target

Let `M` be the cross-nonedge graph of the unoperated host.  Deleting
`e=x_r y_s` adds the single allowed pair `r_Ls_R`, so the colour matching
in Theorem 2.1 lies in `M+e` and contains `e`.

* At distance zero it is already a perfect matching: the deletion state
  is canonical.
* At distance one it is one augmentation short, and exposes at least one
  boundary-reusable `p` shore.
* At distance two it is two augmentations short, and exposes one `p` shore
  of each type.

If the displayed matching augments to a perfect matching in `M+e`, the
deletion colouring can be canonicalized without changing the operated
minor.  If some perfect matching avoids `e`, it lies in `M` and gives an
`(n+2)`-colouring of the original host.

Therefore the remaining edge-cell operation lemma is now finite in
**deficiency**, not in carrier order:

> Starting from the edge-critical common-colour pair, a distance-one or
> distance-two Dulmage--Mendelsohn obstruction containing the exposed `p`
> shores either has an alternating augmentation, or those shores and the
> connected bag `{b,c}` yield the labelled `K_{n+3}` rerouting.

The static Hall-defect example in the cocycle note shows that one cannot
delete the words “edge-critical common-colour pair.”  Theorem 2.1 supplies
the exact operated state which that final augmentation theorem must use.

There is also an unconditional way to force such a state in the
minor-critical edge cell.  Theorem 6.4 of the cocycle note proves that if
deleting every internal carrier edge admitted a distance-zero canonical
colouring in the same switched frame, then the original cross-nonedge
relation would already have a perfect matching.  Consequently:

### Corollary 3.1 (a noncanonical operated carrier is unavoidable)

Let the flat edge-carrier host be minor-critical and suppose its
cross-nonedge relation has no perfect matching.  Then some internal
carrier edge `x_i y_i` has a proper-minor colouring of palette distance
one or two.  Its ends have a common colour, and the colouring exposes the
`p` shore or shores stated in Theorem 2.1.

#### Proof

Minor-criticality colours the deletion of every internal carrier edge,
and edge-criticality makes its two ends equal.  If every deletion had a
distance-zero colouring, those colourings would be canonical and Theorem
6.4 would give a perfect matching in the original relation.  Hence one
deletion has positive palette distance; Theorem 2.1 applies. \(\square\)

Thus positive palette distance is not merely a possible residue.  It is
forced whenever static gluing fails.  The sole missing step in the exact
edge cell is to convert this forced distance-one/two operated state into
an alternating augmentation or the labelled clique minor.
