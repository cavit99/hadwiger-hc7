# A global adjacent-pair palette frame in a hypothetical `HC_7` counterexample

**Status:** written proof; separately audited.

This note turns the adjacent-pair palette theorem from a conditional local
statement into a uniform reduction for every hypothetical minor-minimal
counterexample to `HC_7`.  It does not prove `HC_7`.

## Theorem

Let `G` be a finite graph satisfying all of the following:

1. `G` is seven-connected and `chi(G)=7`;
2. `G` has no `K_7` minor; and
3. every proper minor of `G` is six-colourable.

Then there is an edge `zu` such that, for `H=G-{z,u}`:

1. `chi(H)=6`;
2. `H` has a spanning `K_6`-minor model;
3. `G-zu` has a six-colouring in which `z,u` have one common colour
   `alpha`, the colour `alpha` occurs in `H` but is absent from both pole
   neighbourhoods, and both poles have neighbours in all other five
   colours; and
4. after choosing one neighbour of each non-`alpha` colour at each pole,
   `H` has five pairwise vertex-disjoint paths joining the two selected
   five-sets.  The colours at either end of these paths form the complete
   five-colour palette, paired by a permutation.

Relative to every spanning `K_6` model in `H`, the contact-profile
conclusions of the audited adjacent-pair palette theorem also hold.  In
particular, four branch sets contacted by both poles give an explicit
`K_7`-minor model or an actual vertex separator.  If that separator
outcome is excluded and precisely three branch sets are contacted by both
poles, the model has the exact three-common-branch-set profile stated in
Corollary 5.1 of that theorem.

## Proof

Kawarabayashi, Pedersen and Toft proved that every double-critical
seven-chromatic graph contains a `K_7` minor: see Theorem 7.1 of
*Double-critical graphs and complete minors*, Electronic Journal of
Combinatorics 17 (2010), R87.  Hence `G` is not double-critical.  There is
therefore an edge `zu` for which

\[
                       \chi(G-\{z,u\})>5.
\]

On the other hand, `G-z` is a proper minor of `G`, so it is
six-colourable.  Its induced subgraph `G-{z,u}` is therefore also
six-colourable.  Thus

\[
                       \chi(H)=6.                 \tag{1}
\]

The already established case `HC_6` gives a `K_6` minor in `H`.  Deleting
two vertices from a seven-connected graph leaves a five-connected graph,
so `H` is connected.  Starting with any `K_6`-minor model, repeatedly add
an unused vertex with a neighbour in the current model to the branch set
containing such a neighbour.  Connectivity guarantees that this process
eventually assigns every vertex of `H`, and it preserves branch-set
connectivity and all old branch-set adjacencies.  Hence the model can be
chosen spanning.

All hypotheses of the separately audited adjacent-pair palette theorem now
hold.  Its Lemma 2.1 supplies the edge-deletion colouring and the surviving
buffer colour, and its Theorem 3.1 supplies the five disjoint paths.  Its
Theorem 4.1 and Corollary 5.1 give the two final contact-profile assertions.
\(\square\)

## Exact contribution and remaining gap

The edge and palette frame are not special features of the balanced
order-eight boundary: they exist in every hypothetical minor-minimal
counterexample.  This makes the five-path palette linkage a global input
to `HC_7` research.

The result does not align the six colour classes with the six branch sets.
The five paths preserve endpoint colours only up to a permutation, and the
separator returned by a failed branch-set split has neither a proved upper
bound nor a compatible boundary colouring.  Those are the remaining
uniform rooted-model obligations.

## Primary external input

K. Kawarabayashi, A. S. Pedersen and B. Toft,
[*Double-critical graphs and complete minors*](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v17i1r87),
Electronic Journal of Combinatorics 17 (2010), R87, Theorem 7.1.
