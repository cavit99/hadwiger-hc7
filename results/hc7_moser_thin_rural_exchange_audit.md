# Independent audit: Moser thin-rural exchange

## Verdict

**GREEN.**  The two exceptional five-carrier frames are literal, all their
pairwise adjacencies have witnesses, the failed-orientation classification is
exhaustive, and the cutvertex, bridge, cycle, and cactus consequences use
seven-connectivity correctly.  The result closes the stated unbounded
subfamilies; it does not close the remaining 2-connected packet-thin rural
society.

## 1. Scope and inherited input

The note works only in the favourable pure-Moser crossing normalized in
`../results/hc7_moser_crossing_carrier.md`: the crossed shore supplies
vertex-disjoint external paths `P_05` and `P_24`, and the rural row duties are
the literal pairs

`A={1,4}` and `B={3,2}`.

The source theorem and its independent audit establish this normalization.
In particular the path `Q=P_24` has all internal vertices in `C_1` and avoids
`v`, `C_2`, and every boundary vertex except `2,4`.  Since `24` is not a Moser
edge, `Q` has a nonempty interior.  No stronger conclusion about an arbitrary
crossed rooted `K_4` is being used.

## 2. The `14`-defect frame

Write the five bags as

`A0={0}`, `A2={2}`, `A16={1,6}`, `A3v={3,v}`, and
`AQ=(Q-2) union {5}`.

They are disjoint.  The only shore vertices occur in `AQ`; its boundary
vertices are exactly `4,5`, while the other four bags use
`0,2,1,6,3,v`.  Connectivity of the nonsingletons follows from `16`, `3v`,
and `45`, the latter joining `5` to the `4` end of `Q-2`.

The ten pairwise contacts are:

| Pair | Witness |
|---|---|
| `A0,A2` | `02` |
| `A0,A16` | `01` |
| `A0,A3v` | `03` |
| `A0,AQ` | `04` |
| `A2,A16` | `12` or `26` |
| `A2,A3v` | `2v` |
| `A2,AQ` | the first edge of `Q` |
| `A16,A3v` | `1v` or `6v` |
| `A16,AQ` | `65` |
| `A3v,AQ` | `34`, `4v`, or `5v` |

A rural set missing at most `1` still contacts the bags at, respectively,
`0,2,6,3,4`; one missing at most `4` contacts them at `0,2,1,3,5`.
Thus both stated defect types contact all five bags literally.

## 3. The `23`-defect frame

Write the five bags as

`B0={0}`, `B4={4}`, `B35={3,5}`, `B1v={1,v}`, and
`BQ=(Q-4) union {6}`.

Connectivity uses `35`, `1v`, and `26`, which joins `6` to the `2` end of
`Q-4`.  Disjointness follows from the same boundary accounting as above.
The ten contacts are:

| Pair | Witness |
|---|---|
| `B0,B4` | `04` |
| `B0,B35` | `03` |
| `B0,B1v` | `01` |
| `B0,BQ` | `02` |
| `B4,B35` | `43` or `45` |
| `B4,B1v` | `4v` |
| `B4,BQ` | the last edge of `Q` |
| `B35,B1v` | `3v` |
| `B35,BQ` | `56` |
| `B1v,BQ` | `16` or a `v` edge |

A rural set missing at most `2` contacts `BQ` at `6`; one missing at most
`3` contacts `B35` at `5`.  The other four bag contacts are immediate from
the remaining literal boundary labels.  Lemmas 2.1 and 2.2 are therefore
correct.

## 4. Failed orientations and Theorem 3.1

For each of `X,Y`, its defect is empty or a singleton.  Full attachment of
`C_2=X dotunion Y` says the two defects are disjoint.  The two possible row
orientations are

* `D(X) cap A=empty` and `D(Y) cap B=empty`;
* `D(Y) cap A=empty` and `D(X) cap B=empty`.

If both fail, a direct two-singleton truth table leaves only

`{D(X),D(Y)}={{1},{4}}` or `{{3},{2}}`.

An empty defect, a defect outside `A union B`, or defects chosen from
different duty pairs always permit at least one orientation.  In the first
exceptional pair, the `14` frame plus `X,Y` gives seven clique bags; in the
second, the `23` frame does.  The pre-existing `X-Y` edge is exactly the last
of the 21 adjacencies.  This verifies Theorem 3.1 without a palette-to-label
step.

## 5. Connectivity consequences

If `z` is a cutvertex and `K` is a component of `C_2-z`, then

`N_G(K) subseteq N_N(K) union {z}`.

Five or fewer boundary contacts would therefore give a cut of order at most
six separating `K` from another component of `C_2-z`, from `v`, and from the
opposite shore.  Hence every such component has at least six boundary
contacts.  Taking `X=K` and `Y=C_2-K` makes both connected and adjacent, and
a second component certifies at least six contacts for `Y`.  Theorem 3.1
applies.

For a bridge `xy`, the two bridge sides have external neighbourhoods
contained in their boundary contacts plus the opposite endpoint.  The same
six-cut argument gives at least six boundary contacts on each side, including
when `C_2=K_2`.  This proves the bridge corollary.

If `C_2={x}`, then `x` and `v` are nonadjacent open twins with neighbourhood
exactly `N`.  A six-colouring of the proper minor `G-x` extends by giving `x`
the colour of `v`.  Thus the singleton exclusion is valid.  The conclusion
that a survivor has order at least three and is 2-connected follows under
the standard convention for finite simple graphs.

## 6. Cyclic defect lemma and cycle closure

The cyclic set-family lemma is correct.  If one `D_w` has size at most one,
failure of the split forces the complementary interval to have a two-element
intersection, hence every set on that interval equals the same two-set.  If
all sets have size two, choose adjacent unequal sets.  Their intersection has
size at most one, so the complementary interval consists entirely of copies
of one two-set `E`.  Applying the same argument to the next adjacent pair
shows that either the first or the second exceptional set also equals `E`.
Thus all but one set equal `E`.

As an adversarial check, all `29^4` ordered four-cycles of subsets of a
seven-set of size at most two were enumerated, and 20,000 random instances
were tested for every length from 5 through 30.  No counterexample occurred.
This computation is supplementary; the preceding hand proof is complete.

For a cycle shore, minimum degree seven and the two cycle neighbours give
at least five boundary neighbours per vertex, hence defect at most two.
Full attachment makes the total intersection empty.  In the split outcome,
the two cyclic intervals are connected adjacent pieces and the defect of a
piece is exactly the intersection of its vertex defects, so Theorem 3.1
applies.

In the exceptional outcome all vertices except `w` miss the same two labels
`a,b`.  The six-set

`{w} union (N-{a,b})`

separates the nonempty path `C_2-w` from `v`, the opposite shore, and the
rest of the graph.  There are no hidden cross-shore or `v` edges because
`C_2` is a component of `G-N[v]`.  Seven-connectivity excludes it.  Hence
all cycle shores of length at least four close.  A connected cactus with
more than one block has a cutvertex; a one-block cactus is a vertex, edge,
or cycle.  The only cactus type not covered is therefore a single triangle.

## 7. Trust boundary

The audited result eliminates every singleton, tree, bridge architecture,
cutvertex architecture, cycle of length at least four, and multi-block cactus
in this exact favourable one-duty-per-row Moser residue.  It neither proves
that a triangle shore survives nor closes a general 2-connected shore.  It
does not turn packet number one into a bounded transversal and does not apply
to a differently labelled crossing without first transporting the favourable
normalization from the source theorem.
