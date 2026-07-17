# Audit of the five-branch-set separator-excess barrier

**Verdict:** GREEN.

**Audited source:**
[`hc7_five_bag_separator_excess_barrier.md`](./hc7_five_bag_separator_excess_barrier.md)

**Audited SHA-256:**
`0613bfb720df55cccc63182fcbf7187b5f882be0e6eb5224356e4a7f16fdd05c`

This is a separate internal mathematical audit of the exact source revision
identified above.  It is not external peer review.  The audit checked every
asserted property of the capped-antiprism family, the use of the external
Kelmans--Seymour theorem, the labelled minor model, and the stated limits of
the counterexample.

## 1. Construction, embedding, and edge count

For odd `n>=7`, the graph `H_n` has the two cap vertices `p,q`, two disjoint
`n`-cycles on the vertices `a_i` and `b_i`, and the four families of spoke
and annulus edges displayed in (2.1).

The counts are correct:

- there are `2n+2` vertices;
- the two rim cycles contribute `2n` edges;
- the two cap stars contribute `2n` edges; and
- the two annulus diagonals at every index contribute `2n` edges.

Thus `|E(H_n)|=6n=3(2n+2)-6`.  The claimed planar embedding is explicit:
the two rim cycles bound an annulus, the cross edges triangulate that
annulus, and the two cap vertices triangulate its two complementary discs.
The graph is simple for `n>=7`, so this is a planar triangulation and hence a
maximal planar graph.

## 2. Five-connectivity of `H_n`

The proof correctly exhausts the possible locations of the two cap vertices
in a set `S` of at most four deleted vertices.

### 2.1 Neither cap is deleted

All surviving `a`-vertices are joined through `p`, and all surviving
`b`-vertices are joined through `q`.  The cross edges form the alternating
cycle (2.3), of length `2n`.  A vertex cover of this cycle has order at least
`n`; since `|S|<=4<n`, a cross edge survives and joins the two cap
components.  Every surviving vertex is in one of those components, so the
remainder is connected.

### 2.2 Exactly one cap is deleted

By symmetry it is enough to delete `q` and retain `p`.  All surviving
`a`-vertices then lie in the component of `p`.  A component outside it would
contain a maximal cyclic interval `I` of surviving `b`-vertices and no
surviving `a`-neighbour.

The repaired interval count is correct in all three cases:

- If `1<=|I|<=n-2`, the two boundary `b`-vertices are distinct and deleted,
  while the interval has `|I|+1` distinct `a`-neighbours, all deleted.  This
  requires `|I|+3>=4` deletions in `S-{q}`, although at most three are
  available.
- If `|I|=n-1`, the two cyclic boundary positions coincide.  The sole
  missing `b`-vertex and all `n` distinct `a`-neighbours must nevertheless
  be deleted, requiring `n+1>3` deletions.
- If `I` is the whole `b`-cycle, all `n` `a`-vertices must be deleted.

Thus no component outside the `p`-component exists.

### 2.3 Both caps are deleted

At most two ring vertices are then deleted from the alternating cycle.  Zero
or one deletion leaves a connected path or cycle.  Two adjacent deletions
also leave one path.  Two nonadjacent deletions leave two paths, but the two
alternating-cycle neighbours of either deleted vertex are joined by an
undeleted same-rim edge; because the deleted vertices are nonadjacent, those
two neighbours survive.  That edge reconnects the paths.

No set of at most four vertices disconnects `H_n`.  Every rim vertex has
degree five, so `kappa(H_n)=5`, as asserted.

As a finite sanity check independent of the prose argument, the adjacency
definition was reconstructed directly and every vertex deletion set of
order at most four was enumerated for `n=7,9,11`; no disconnected remainder
occurred.  This computation is corroborative only and is not needed by the
written proof.

## 3. Connectivity of the join

In `G_n=K_2\vee H_n`, any surviving universal vertex connects every
remaining vertex.  Hence a vertex cut must contain both `s,t`; after those
vertices are removed, its remaining vertices must disconnect `H_n`.
Conversely, the two universal vertices together with a five-cut of `H_n`
disconnect `G_n`.  Therefore

\[
                         \kappa(G_n)=2+\kappa(H_n)=7.
\]

This also covers cuts intended to separate a universal vertex: if either
universal vertex survives, the remainder cannot be disconnected.

## 4. `K_7`-minor exclusion

Suppose a `K_7`-minor model existed.  At most two branch sets meet
`{s,t}`, even when one branch set contains both universal vertices.
Therefore at least five branch sets lie wholly in `H_n`.  Their internal
connectivity and every mutual model adjacency use only edges of `H_n`, so
they form a `K_5`-minor model in the planar graph `H_n`.  This is impossible.
Thus `G_n` has no `K_7` minor.

The argument does not silently assume that `s` and `t` lie in distinct
branch sets.  If they lie in one branch set, there are in fact at least six
branch sets wholly in `H_n`, and choosing any five gives the same
contradiction.

## 5. Chromatic number

The Four Colour Theorem gives `chi(H_n)<=4`.  The subgraph induced by `p`
and the odd `a`-cycle is an odd wheel.  In any three-colouring, the colour on
the hub `p` is unavailable on the rim, which would force the odd rim cycle
to be two-coloured.  Hence `chi(H_n)>=4`, and therefore `chi(H_n)=4`.

Chromatic number is additive under graph join.  Consequently
`chi(G_n)=chi(K_2)+chi(H_n)=2+4=6`.  The family is not seven-chromatic, as
the source explicitly records.

## 6. Edge-maximal `K_7`-minor-freeness and external input

Because `H_n` is a maximal planar graph, adding any nonedge `e` makes
`H_n+e` nonplanar.  Adding an edge cannot decrease vertex connectivity, so
`H_n+e` remains five-connected.

The source invokes Theorem 1.1 of Dawei He, Yan Wang, and Xingxing Yu,
*The Kelmans--Seymour conjecture IV: a proof*, arXiv:1612.07189.  Its exact
statement is that every five-connected nonplanar graph contains a
subdivision of `K_5`.  The hypotheses apply to `H_n+e`; a subdivision of
`K_5` supplies a `K_5` minor.

Every nonedge of `G_n` lies inside `H_n`, since `s,t` are adjacent and
universal.  Adding any such edge therefore produces a `K_5` minor in the
`H_n` part, which together with singleton branch sets `{s}` and `{t}` gives
a `K_7` minor.  Thus `G_n` is edge-maximal among `K_7`-minor-free graphs.
The source now uses precisely this term and does not conflate it with
contraction-criticality.

## 7. The labelled `K_7^-` model

Three nonempty consecutive arcs `P_1,P_2,P_3` partition the `a`-cycle.
Each is connected, and the three boundary edges of the cyclic partition
make them pairwise adjacent.  The set

\[
                         R=\{q\}\cup\{b_i:0\le i<n\}
\]

is connected.  The seven disjoint connected sets

\[
       \{s\},\ \{t\},\ P_1,\ P_2,\ P_3,\ \{p\},\ R
\]

have every model adjacency except `{p}R`:

- `s,t` are universal and adjacent to one another;
- the three arcs are pairwise adjacent;
- `p` is adjacent to every arc;
- every nonempty arc meets a cross edge into `R`; and
- `p` has no edge to `q` or any `b_i`.

This is therefore a label-faithful `K_7^-`-minor model with common `K_5`
given by `{s},{t},P_1,P_2,P_3`.

For the four-labelled component-contact graph, use anchors
`{s},{t},P_1` and the four distinct labelled vertices represented by

\[
             l=\{p\},\qquad r=R,\qquad m=P_2,\qquad n=P_3.
\]

Their contact graph is exactly `K_4-lr`: all five other edges are present
and `lr` is absent.  This diamond is a two-tree, for example by starting
with the triangle `lmn` and adding `r` on the edge `mn`.  The seven sets
cover the host, so the attachment-clique hypothesis for components outside
their union holds vacuously.

## 8. Separator order and portal claim

For `X={p}`,

\[
 N_{G_n}(X)=\{s,t\}\cup\{a_i:0\le i<n\}
             =\{s\}\cup\{t\}\cup P_1\cup P_2\cup P_3.
\]

The complement of `X\cup N(X)` is exactly the connected nonempty set `R`,
which is anticomplete to `X`.  Hence this is the required actual
five-branch-set-supported separation and has order `n+2`, unbounded with
odd `n`.

Any separation whose near open side is the singleton `{p}` must include
every neighbour of `p` in its separator.  It therefore cannot have order
seven.  Under the explicitly stated stronger preservation requirement,
retaining each of the five common branch sets in its entirety in the
separator likewise retains all `n+2` vertices.

The added portal assertion is also exact.  Every vertex of every arc
`P_i` is adjacent to `p`, and each `a_j` is adjacent to the two vertices
`b_{j-1},b_j` of `R`.  Thus the `p`-attachment and `R`-attachment vertex sets
inside each nonsingleton common branch set are both the whole branch set.
If those contacts alone permitted a label-preserving split repairing the
missing `{p}R` adjacency, the result would be a `K_7` minor, contradicting
Section 4.  The family therefore also blocks an argument based solely on
the multiplicity or distribution of those contacts.

Moving the three cyclic cut edges changes the arc partition while retaining
all of these quotient properties and the same separator.  Cyclically moving
the cuts and returning to the original partition gives the claimed rotation
cycles.  The source correctly limits the conclusion: these rotations are
not asserted to be legal contraction-critical transitions.

## 9. Exact trust boundary

The construction proves that the following data, even jointly, do not bound
the five-branch-set-supported separator:

1. seven-connectivity;
2. `K_7`-minor exclusion;
3. edge-maximality within the `K_7`-minor-free class;
4. a labelled `K_7^-` model with a named common `K_5`;
5. two anticomplete connected pole branch sets;
6. maximally distributed contacts inside the nonsingleton common branch
   sets; and
7. the outside-component attachment-clique condition.

It does **not** prove a barrier under the full hypotheses of a hypothetical
minimal counterexample.  In particular:

- `G_n` is six-chromatic, not seven-chromatic;
- it is not seven-contraction-critical;
- the model lacks the proper-minor colouring provenance of the active
  adjacent-pair programme; and
- `{s,t}` meets every `K_5`-minor model, since deleting it leaves the planar
  graph `H_n`.

Accordingly, this family is not a counterexample to `HC_7` or to the active
conditional exchange-or-gluing theorem.  It establishes only that the next
theorem must use contraction-critical colouring information or permit the
two-vertex `K_5`-minor-transversal outcome; connectivity, edge-maximal
minor exclusion, and static branch-set geometry do not suffice.

## 10. Verdict

All claims in the audited source revision are correct at the stated scope.
The earlier cyclic-interval overcount has been repaired, the preservation
condition is now unambiguous, and the closing terminology states the exact
edge-maximal property proved.  The external theorem is accurately cited
and correctly applied.

**Final verdict: GREEN.**
