# Independent audit of the one-tree attachment-set classification

**Status:** separate internal audit GREEN, 21 July 2026.

This is an internal mathematical audit, not external peer review.

## Revision audited

- result:
  [`hc7_partial_loss_attachment_set_classification.md`](hc7_partial_loss_attachment_set_classification.md)
- exact SHA-256:
  `328ac9bac738d4df60df6b1268e9a49b42924d5b507515a607551c69b2486eb5`

The mathematical content was audited at SHA-256
`6a11110f65742be219f4b1cd789ef3be3ae6763eb9893e6f2defea1af4bfb5b1`.
The only subsequent source edit changed its status line from audit pending
to audit GREEN.  Reversing exactly that substitution independently
reproduced the mathematical-content hash, and the final hash above was
independently reproduced with `shasum -a 256`.

The two directly invoked inputs were checked against their adjacent GREEN
audits:

- the attachment-hull theorem at SHA-256
  `faa777f7645cd3afcaa81c41338a12ec8b82f9e2b28a80a136c195b97a4afad2`;
- the clean three-arm theorem at SHA-256
  `6071c020cb7aa9fa2c963c13718a02db2b29a218fa742d924b460d540a5fc869`.

## Verdict

GREEN.  Every stated conclusion follows under the displayed hypotheses.
In particular, the comparison alternative is exact, the order-seven case
really has an opposite full component, the clean-support criterion uses
literal contacts only, and the join construction realizes every prescribed
common-leaf attachment family at an inclusion-minimal first connectivity
loss.

There are no unresolved assumptions or mathematical gaps.  One sentence in
the proof of Theorem 3.1 compresses the case in which the connected
attachment set under consideration is `A_C`; check 3 below supplies the
immediate missing case distinction without strengthening any hypothesis or
altering the argument.

## Checks performed

1. For a finite nontrivial tree, its minimal spanning subtree is the whole
   tree exactly when the selected set contains every leaf.  Necessity follows
   by deleting an unselected leaf from a purported minimal subtree.
   Conversely, each side of every deleted tree edge contains an original
   leaf, so a connected subgraph containing all leaves contains every edge.
   Thus the attachment-hull input is exactly the common-leaf condition
   `A_C=L union X_C`, with no hidden convexity or interval conclusion.

2. Choose `A_C` inclusion-minimal.  If some other `A_D` contains it, the
   host-neighbourhood identity `S_C=O union A_C` and fullness of every lifted
   component to `O` make `D` full to `S_C`.  Otherwise minimality excludes
   `A_D proper-subset A_C`, while the assumed failure excludes
   `A_C subseteq A_D`; hence every other set is incomparable with `A_C`.
   Since all attachment sets contain `L`, witnesses to both strict
   differences are internal vertices of `R`.  The same identities prove the
   advertised equivalence between `S_C`-fullness of a specified component
   `D` and `A_C subseteq A_D`.

3. In the antichain alternative no attachment set induces a connected
   subgraph of `R`.  For `D != C`, connectedness plus full hull would force
   `A_D=V(R)`, contradicting `A_C not-subseteq A_D`.  If instead `A_C` were
   connected, then `A_C=V(R)`.  There is another lifted component because
   `T` is a separator; its attachment set is a subset of `V(R)`, and
   inclusion-minimality of `A_C` rules out a proper subset.  It would
   therefore equal `A_C`, again giving the forbidden comparison.  This
   verifies the source's explicit claim that the conclusion includes
   `A_C` itself.

4. Since `O` has five vertices and is disjoint from `A_C`, the boundary
   `S_C` has order seven exactly when `|A_C|=2`.  Every nontrivial tree has at
   least two leaves, all of which lie in `A_C`; equality therefore means
   precisely that `R` is a path and `A_C` is its two-end leaf set.  Every
   other attachment set then contains `A_C`, so every other lifted component
   is full to `S_C`.  Removing `S_C=N_G(C)` separates the nonempty component
   `C` from at least one other lifted component, making this a literal host
   separator rather than a quotient boundary.  Proposition 3.1 of the
   attachment-hull theorem then gives the two exact-block responses under
   the separately stated strong contraction-critical hypothesis.

5. In Proposition 4.1, `x in O` is adjacent to the selected lifted component
   `C`, so `X=G[V(C) union {x}]` is connected.  The disjointness hypothesis
   makes `X` meet the fixed subdivision exactly in `x`.  Every leaf of `R`
   is a literal neighbour of `C`; hence a matching of three distinct leaves
   on the subdivision to the clean roots `e,f,g` is a submatching of the
   clean attachment graph for `X`.  The audited clean three-arm theorem
   therefore gives the displayed `K_7` model.  Contraposition and Hall's
   theorem give exactly the stated matching-number and deficiency
   conclusions.  No leaf outside the subdivision is assigned a support.

6. For Theorem 5.1, let `H` consist of `R`, the independent vertices `c_i`,
   and the prescribed incidence edges.  It is two-connected.  Deleting a
   `c_i` leaves the connected tree with every remaining `c_j` attached.
   After deleting a tree vertex `r`, every component of `R-r` contains an
   original leaf; any surviving `c_i` sees every such component because
   `L subseteq A_i`, and the other `c_j` retain a surviving leaf neighbour.
   The assumptions `m>=2` and nontriviality of `R` cover all small cases.

7. The join `G=K_5 join H` is seven-connected: after deletion of at most six
   vertices, either a universal vertex of the `K_5` remains, or all five
   have been deleted and at most one vertex was deleted from the
   two-connected graph `H`.  Contracting all tree edges gives exactly
   `K_5 join K_{1,m}`.  Its set consisting of the five clique vertices and
   the star centre is a six-cut, while deletion of at most five vertices
   leaves either a universal clique vertex or the whole star.  Thus the
   quotient is six-connected but not seven-connected, and its open
   components are the singleton `c_i` with literal attachment sets exactly
   `A_i`.

8. For every proper edge subset `F'` of `E(R)`, the quotient tree
   `R'=R/F'` is nontrivial.  Each edge of `R'` comes from an uncontracted
   original edge.  Because every `A_i` contains all original leaves, it
   meets both sides of that edge; contractions cannot identify its two
   sides.  Consequently the image `A_i'` spans all of `R'` and contains
   every leaf of `R'`.  Repeating check 6 makes the corresponding `H'`
   two-connected, and `G/F'=K_5 join H'` is seven-connected by check 7.
   This verifies the all-proper-edge-subsets quantifier, not merely a chosen
   contraction order.  The selected forest has `R` as its unique nontrivial
   component.

9. The example with a Sperner family genuinely yields arbitrarily large
   incomparable attachment families.  It is correctly fenced off from the
   `K_7`-minor-free setting: the five join vertices together with the two
   ends of any tree edge induce a `K_7` subgraph.  Thus it proves only that
   seven-connectivity and first-loss minimality cannot eliminate the
   antichain residue by themselves.

## Trust boundary

The classification is restricted to a first loss with one nontrivial tree
fibre and to a selected inclusion-minimal attachment set.  The realization
theorem deliberately constructs graphs containing `K_7`; it does not show
that the antichain residue occurs in a `K_7`-minor-free or
contraction-critical host.  A Hall-deficient clean-support pattern remains
neither a bounded response interface nor a strict same-form reduction.
