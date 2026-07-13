# Independent adversarial audit: uniform palette-haven dichotomy

## Verdict

**GREEN for Theorems 2.1, 2.3, 4.1, 5.1 and the substantive HC7
connectivity consequence; AMBER for the note as written.**  The palette
permutation, both haven constructions, the endpoint-inclusive Menger
argument, and the Rado transversal are valid.  The minimum polarized
adhesion really has both shores full.  I found no counterexample or
quantifier failure in those results.

There is, however, one false assertion in Corollary 5.2: an exact trace
from Lemma 3.1 need not have `mu=1`.  If the contracted independent set
`I` is a singleton, all `r` colours are private on `N`, so `mu=0`.
For example, take `G=K_{r+1}`, `v` any vertex, and contract the edge from
`v` to the sole member of `I`.  The intended orientation conclusion
survives unchanged after replacing `mu(c)=mu(d)=1` by
`mu(c),mu(d)<=1`; equality holds when both repeated blocks are
nontrivial.

## 1. The shore permutation (Theorem 2.1)

Let `F=[r]-c(X)`.  Applying one permutation of `F` throughout `D` and
fixing every colour in `c(X)` is legitimate:

* internal edges of `D` remain proper by bijectivity;
* a `D-X` edge remains proper because a permutation fixing a boundary
  colour cannot send a different colour to it; and
* no edge joins the two open shores.

For `P,Q subseteq F`, the minimum of `|pi(P) union Q|` is
`max(|P|,|Q|)`: inject the smaller set into the larger and extend the
injection to a permutation.  If neither shore contains all of `F`, this
maximum is strictly below `|F|`, so the hybrid neighbourhood palette
omits a colour.  This proves the stated dichotomy, including empty-shore
and repeated-colour cases.

## 2. Private roots and haven nesting

The uniqueness-on-`N` hypothesis is used in exactly the right place.
If two private roots whose colours are absent from `c(X)` lie in
different components of `H-X`, separating one component from the union
of the others makes each shore miss the other root's unique
neighbourhood colour.  This contradicts Theorem 2.1.

For `|X|<h`, some private colour is absent from `c(X)`, so the selected
component is nonempty.  If `X subseteq Y`, a private colour absent from
`c(Y)` supplies a common root in both selected components; the
`H-Y` component is contained in the corresponding `H-X` component.
Thus (2.7) is a genuine haven nesting law, not merely a pairwise
connectivity statement.  The count `h>=2r-|N|` is also exact.

## 3. Model haven, Menger, and Rado (Theorem 4.1)

For `|X|<r`, at most `|X|` disjoint model bags meet `X`.  Every two
untouched bags retain a direct interbag edge, hence lie in one component
of `H-X`.  This gives the model haven and its nesting.

In the nonpolarized case, suppose a prescribed subfamily of `j<=h`
bags cannot be reached by `j` vertex-disjoint paths from `U_c`.  The
set form of Menger gives an `U_c`--target hitting set `X` with
`|X|<j`.  This remains valid when source and target sets overlap and
when the cut contains endpoints.  Since `|X|<j`, one target bag is
disjoint from `X`; since `|X|<h`, one private root is outside `X` in
the colour-haven component.  Haven equality gives an `X`-avoiding path
between them, contradicting the hitting property.

Those inequalities are precisely Rado's conditions for the family of
bag vertex sets in the (undirected) strict gammoid defined by linkage
from `U_c`.  Representatives supplied by Rado are distinct because
the bags are disjoint.  When `j=h`, the `h` disjoint source endpoints
must be all of `U_c`.  Hence the claimed path transversal is valid.
It is not, and the source correctly does not call it, a cleaned rooted
clique model.

## 4. Minimum polarized adhesion (Lemma 4.3)

The conclusion is valid, although the phrase "interchanging the two
havens" compresses a point worth spelling out.  If `x in X` has no
neighbour in `C=beta_c(X)`, restoring only `x` cannot merge `C` with
another component of `H-X`.  Haven nesting therefore gives
`beta_c(X-{x})=C`, while the model haven contains `M` and cannot reach
`C` through `x`.  This contradicts minimum cardinality of `X`.

The model-side argument is analogous but must account for a model bag
which becomes untouched after `x` is restored.  Such a bag cannot join
`M` to `x` unless `x` has a neighbour in the `H-X` component `M`:
delete `x` from a bag path from `x` toward an old untouched bag; the
first neighbour of `x` lies in the same `H-X` component as that old
bag.  Thus if `x` misses `M`, restoring it leaves `M` unmerged, and the
two havens again differ at `X-{x}`.  Therefore every adhesion vertex
meets both shores and `N_H(C)=X=N_H(M)`.

## 5. HC7 connectivity consequence

If `H` is `h`-connected, a polarized pair would be two distinct
components of `H-X` for `|X|<h`, impossible.  In a seven-connected
hypothetical minimal HC7 counterexample, deleting `v` leaves a
six-connected graph: any cut of order at most five in `G-v`, together
with `v`, would be a cut of order at most six in `G`.  Since the actual
private-colour count at degrees seven, eight, and nine is at most six
and at least five, four, and three respectively, six-connectivity kills
the polarized branch and gives the stated prescribed-bag linkage ranks.

This consequence also tacitly uses the already-established `HC_6` to
obtain a `K_6` model in `G-v`; that dependency should be stated next to
the table in a standalone presentation.

## 6. Opposite-orientation gluing (Theorem 5.1)

The same equality partition on `X` is exactly enough to align the two
restrictions by one global palette permutation.  This permutation does
not change private/nonprivate status or the underlying haven component.

For a colouring whose haven points into `E`, every private colour not
used on `X` has its unique occurrence on `N` in `E`, so it is absent
from `N cap D`.  Consequently the hybrid using that colouring on `D`
and the other colouring on `E` uses at most

`|c(X)| + mu(c) + mu(d)`

colours on `N`.  If this is below `r`, the omitted colour extends to
`v`, a contradiction.  Theorem 5.1 is therefore sound.

The repair to Corollary 5.2 is:

> For exact traces from Lemma 3.1, `mu<=1`; it equals one precisely
> when the contracted block has at least two vertices.  Hence two such
> traces with `|c(X)|<=r-3` still cannot have opposite orientations.

## 7. Minor repairs and exact remaining limitation

* In Corollary 4.5, the sentence citing `(4.6)` for roots avoiding the
  model should cite hypothesis `(4.7)`.
* The reference after Corollary 4.6 to "Corollary 4.3" appears to mean
  the connectivity/path-transversal consequence, Corollary 4.4.
* Lemma 3.1's star contraction is proper in its stated setting because
  non-`r`-colourability forces `|N|>=r`, hence (3.1) forces `I` to be
  nonempty.  Adding this one-line observation would remove ambiguity.

The unresolved issue remains exactly label-preserving model cleaning:
the gammoid paths can first enter unintended bags.  Truncation yields
contacts or a double-hit certificate, but neither by itself supplies a
legal split preserving every old clique-bag adjacency.  Nothing in this
audit upgrades the theorem to an `N(v)`-meeting `K_r` model.
