# Cold audit: exact two-row five-colour linkage package

**Verdict:** **GREEN.**  The recolouring, exact-signature, local
double-criticality, simultaneous Kempe-lock, Menger, branch-set, prescribed
path, and augmentation-barrier claims in
[`hc7_five_colour_exact_two_row_linkage.md`](hc7_five_colour_exact_two_row_linkage.md)
are correct under the hypotheses stated there.  The note remains a partial
package: it does not augment the raw nonmonotone path to a member of a
four-linkage and therefore does not close the five-colour branch or `HC_7`.

**Audited source SHA-256:**
`83551a1447d072dd3d7a82ec59c60ea8cc565245efac9bba54a89308e8e52418`.

## 1. Exact two-row rigidity

Theorem 2.1 is correct.

* If no deleted matching row is equal, the five-colouring already colours
  `G`.  If exactly one row is equal, one endpoint can receive a fresh sixth
  colour; no other edge becomes monochromatic.
* When precisely `e` and `f` are equal, two nonadjacent endpoints chosen one
  from each row could receive the same fresh sixth colour.  This would repair
  both rows while preserving the proper third row.  Thus all four cross-edges
  exist, and together with `e` and `f` they give the claimed literal `K_4`.

Corollary 2.2 is also exact.  The displayed five-colouring restricts to
`G-x-y`, while

\[
  \chi(G)\leq \chi(G-x-y)+2
\]

gives the matching lower bound.

Lemma 2.3 is valid.  The beta-coloured neighbours of `y` form an independent
set.  If none is also adjacent to `x`, they may all receive the fresh sixth
colour, after which `y` receives beta and `x` the fresh colour.  This checks
all possible fresh-colour conflicts and contradicts seven-chromaticity.
No global double-critical hypothesis is being imported.

## 2. Simultaneous Kempe locks

Theorem 3.1 is correct, including the count of exceptional colours.

Swapping the alpha-beta component containing `a` but not `a'` makes `e`
proper and leaves `f` equal.  Theorem 2.1 therefore forces `g` to become
equal.  Exactly one endpoint of `g` must have been swapped, so its two old
colours were precisely `{alpha,beta}`.  The eta-beta argument is symmetric.

For the three colours outside `{alpha,eta}`, the fixed unordered colour pair
on `g` can equal `{alpha,beta}` for at most one beta and can equal
`{eta,beta}` for at most one beta.  Exceptions of the two different kinds
cannot coexist: equality

\[
  \{\alpha,\beta\}=\{\eta,\gamma\}
\]

would force beta to be eta and gamma to be alpha, contrary to both being
outside `{alpha,eta}`.  Hence at most one outside colour fails either lock,
and at least two satisfy both.  Lemma 2.3 then gives distinct common-contact
vertices of those two colours; their colours also show that neither lies in
the endpoint `K_4`.

## 3. All-three-equal branch

The independent-transversal assertion used in Section 4 is valid directly
from the hypotheses of this note.  An independent choice of one endpoint
from each equal row could be recoloured with one common fresh sixth colour,
repairing all three deleted edges and six-colouring `G`.

The two orientation observations are also correct.  If all row colours
coincide, properness of the colouring of `K` forbids every cross-row edge.
If two rows have one common colour and the third row another, an endpoint of
the third row which is not complete to either of the first rows has a chosen
nonneighbour in each; those three vertices form the forbidden independent
transversal.

## 4. Menger separator and literal models

Deleting the four-clique `C` from a seven-connected `G` leaves a
three-connected `H`: deleting a further set of at most two vertices deletes
at most six vertices from `G`.  Both four-clique cores remain available, so
the usual order conditions for connectivity are harmless.

Theorem 5.1 correctly applies set-Menger in `H`.

* A separator of order at most three cannot have order at most two, because
  both four-vertex terminal cliques survive and `H` is three-connected.  It
  therefore has order exactly three.  Each surviving part of a terminal
  clique lies in one component.  Adding `C` to the separator produces a
  literal seven-boundary in `G`, and the two core remainders make both open
  shores nonempty.  Boundary vertices from a core cause no problem: the full
  named model is contained in its declared closed shore.
* With four disjoint paths, truncate at the first and last core vertices.
  Distinct endpoints in each literal four-clique make every pair of path bags
  adjacent.  The support assumption gives an edge from every path bag to its
  named two-vertex bag, and the endpoint `K_4` supplies the `e-f` adjacency.
  These are six disjoint connected branch sets for `K_6`.

Theorem 5.2's seven branch sets are also correct.  If `r s` is an oriented
edge between the early `f`-contact and later `e`-contact, the prefix and
suffix are disjoint and adjacent through `rs`.  The early contact gives the
prefix its edge to `f`, the later contact gives the suffix its edge to `e`,
and their retained terminal-clique endpoints give all adjacencies to the
other three paths.  Together with the two row bags this is a literal `K_7`
model.  The stated monotone order, including the fact that there is at most
one common-contact vertex, follows immediately.

## 5. Prescribed path input

The Li--Ning--Zhang invocation in Theorem 6.1 is accurate.  Their path
theorem states that in a `k`-connected graph, fixed distinct endpoints are
joined by a path through any prescribed `k-2` further vertices (with an
additional length bound irrelevant here).  The source is Binlong Li, Bo
Ning, and Shenggui Zhang, *Long paths and cycles passing through specified
vertices under the average degree condition*, Graphs and Combinatorics 32
(2016), 279--295; arXiv:1109.4344, Theorem 4.

If the three-connected `H` has no three-cut, it is four-connected.  The
choices of `q` and `r` are distinct from `u,v` because each terminal core has
four vertices and the cores are disjoint.  On the resulting path, whichever
of `u,v` occurs first is an `f`-contact and the other is a distinct later
`e`-contact.  Conversely, an existing three-cut plus `C` is an actual
seven-boundary.  As the source says, these alternatives need not be
exclusive and the raw path is not asserted to avoid the terminal cliques or
extend to four disjoint terminal paths.

## 6. Four-connected augmentation barrier

The graph in Section 7 has the asserted proper five-colouring.  Every gate
vertex has at least three neighbours in each core.  After deleting at most
three vertices, both four-clique cores survive and at least one gate
survives.  Ordinarily that gate still meets both cores.  In the sole tight
case all three deletions remove its neighbours in one core; then all other
gates survive, and a gate of a different colour joins the surviving core
vertex to the untouched opposite core.  Thus the remainder is connected.
Deleting all four gate vertices separates the cores, so the connectivity is
exactly four.

Every path between the cores uses a gate.  Four vertex-disjoint such paths
therefore use all four gates, exactly one per path.  No path in a
four-linkage can contain both `z_2` and `z_3`, although
`x_1 z_2 z_3 y_0` is a raw nonmonotone path.  After the two equal row bags
are added as described, the `0,2`, `0,3`, `1,2`, and `1,3` Kempe components
give the four claimed row locks, while `z_2,z_3` are different-colour common
contacts.  All added edges respect the displayed colouring of the common
deletion.

This verifies precisely the claimed guardrail.  The construction is not a
strongly contraction-critical host and is not asserted to be `K_7`-minor
free, so it refutes only the attempted augmentation from connectivity,
proper colouring, and the two local Kempe locks.

## 7. Final trust boundary

No correction to the source theorem statements is required.  What is now
audited is the following partial fork:

1. an exact seven-boundary retaining the two named supports;
2. a labelled `K_6` whose nonmonotone member would split to a literal `K_7`;
3. in the four-connected residue, a raw nonmonotone path which cannot be
   augmented using the stated local data alone.

The unresolved implication must use additional global minor-critical or
`K_7`-free structure.  Treating the raw path as a member of the four-linkage
would be invalid.
