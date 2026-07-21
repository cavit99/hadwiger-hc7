# Independent audit of the partial-loss attachment-hull theorem

**Status:** separate internal audit GREEN, 21 July 2026.

This is an internal mathematical audit, not external peer review.

## Revision audited

- result:
  [`hc7_partial_loss_attachment_hull.md`](hc7_partial_loss_attachment_hull.md)
- exact SHA-256:
  `faa777f7645cd3afcaa81c41338a12ec8b82f9e2b28a80a136c195b97a4afad2`

The mathematical content was audited at SHA-256
`976c621134662d0b9b73584e84797f71be6931aab8b94ead14a9592e5f4038c8`.
The only subsequent source edit changed its status line to record this
GREEN audit.  That status-only revision was rechecked, and the final hash
above was independently reproduced with `shasum -a 256`.

## Verdict

GREEN.  Under the stated all-proper-edge-subsets minimality, the proof
correctly lifts a six-separator through every one-edge split predecessor,
forces every component attachment set to span its entire forest tree, and
derives exactly the claimed one- and two-sided colouring responses.  The
bipartite one-tree fibre argument also correctly proves `chi(P)=6` and the
five-colour contact condition on both bipartition classes.

No unproved quotient separator is treated as a bounded host separator: the
host boundary is the literal set `O` together with the vertex-level
attachment sets `A_j(C)`.

## Checks performed

1. The setup invokes the separately audited minimal partial-loss lemma with
   edge subsets of a forest.  It gives `kappa(P)=6`, makes every nontrivial
   fibre image a member of the selected six-cut `T`, and leaves the
   components of `P-T` as literal vertex sets in `G`.  Since `P-T` has at
   least two components, `N_P(C)` is a separator contained in `T`.
   Six-connectivity therefore forces `N_P(C)=T`.
2. Expanding the fibre images cannot introduce a neighbour of `C` outside
   `O` and the fibre trees.  An ordinary member of `O` is literal and is
   adjacent to `C`; a vertex in `R_j` is adjacent to `C` exactly when it
   belongs to `A_j(C)`.  This verifies the disjoint equality

   \[
                  N_G(C)=O\mathbin{\dot\cup}\bigcup_j A_j(C).
   \]

3. For an edge `h` of `R_j`, the proper-subset predecessor
   `H_h=G/(F_0-{h})` is seven-connected.  Replacing `z_j` in `T` by the two
   images of the components of `R_j-h` gives an order-seven set `S_h`.
   Deleting it leaves exactly the old open components.  Hence
   `N_{H_h}(C)` is a separator contained in `S_h`, and seven-connectivity
   forces equality.  In particular, `C` has a host neighbour on each side
   of every forest-tree edge.
4. In a tree, a vertex set has full minimal spanning subtree exactly when
   it meets both components after every edge deletion.  Applying this to a
   leaf edge forces its singleton leaf side into `A_j(C)`.  This proves the
   hull equivalence and the common-leaf conclusion.  Host chords inside a
   fibre do not affect the argument: `R_j` here is the tree formed by the
   selected forest edges.
5. The neighbourhood formula gives
   `|N_G(C)|=6-q+sum_j |A_j(C)|`.  It is a genuine host separator because
   another lifted component remains, so seven-connectivity gives the lower
   bound seven.  In the one-tree specialization this becomes
   `|N_G(C)|=5+|A_C|` exactly.
6. For a nonempty independent set `I` in `G[S_C]`, every member of `I` has
   a neighbour in `C`; hence `G[C union I]` is connected.  Contracting it
   is a proper minor.  After a six-colouring is pulled back to `I` and
   restricted to `G-C`, every vertex of `S_C-I` avoids the contracted
   colour because it has a neighbour in `C`.  Independence makes the
   pullback proper.  Thus `I` is exactly one boundary colour class, not
   merely a monochromatic subset.
7. If another lifted component `D` satisfies
   `A_j(C) subseteq A_j(D)` for all `j`, then it is adjacent to every
   vertex of each `A_j(C)` and, from `N_P(D)=T`, to every ordinary vertex
   of `O`.  It is therefore full to `S_C`.  Contracting `D union I` and
   restricting to `G[C union S_C]` gives the reverse closed-shore response.
   The note correctly presents this containment as a sufficient extra
   condition; it does not infer it from attachment cardinalities.
8. In the one-tree case, contraction gives a proper minor `P`, so
   `chi(P)<=6`.  If `P` used at most five colours, colouring one side of the
   induced bipartite fibre with the quotient colour of `z` and the other
   with a fresh sixth colour would six-colour `G`.  Every external fibre
   neighbour avoids the colour of `z`, so all cross-boundary edges are
   proper.  This contradiction proves `chi(P)=6`.
9. Fixing a six-colouring of `P`, if either bipartition side lacked an
   external neighbour of some non-`z` colour `beta`, that side could be
   coloured `beta` and the other side with the colour of `z`.  The induced
   bipartite hypothesis handles every internal edge, while the assumed
   missing contact and quotient propriety handle every external edge.
   This again six-colours `G`, proving the asserted contact for each of the
   five other colours on both sides.

## Trust boundary

The theorem requires inclusion-minimality against every proper edge subset
of `F_0` and a chosen separator of order six in the first bad quotient.  It
does not bound the orders of the attachment sets, compare attachment sets
belonging to different lifted components, or identify tree leaves with
named endpoint supports in the atomic subdivision.

The reverse-shore exact-block response requires an actual opposite
`S_C`-full connected subgraph; the displayed attachment containment is one
sufficient way to obtain it.  The chromatic saturation theorem additionally
requires the entire induced fibre `G[V(R)]`, including host chords not in
the contraction forest, to be bipartite.  None of these conclusions alone
produces a `K_7` model, a dominating-model transversal, or a strict
same-form reduction.
