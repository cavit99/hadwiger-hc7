# Exact-seven boundary rooted-model trichotomy

## 1. Uniform seven-boundary theorem

Let `F` be a triangle-free graph on a literal seven-set `S`.  Give every
`s in S` a nonempty contact list

\[
                       \Lambda(s)\subseteq\{1,2,3\},
\]

and assume every palette symbol has support at least four:

\[
              |\{s:q\in\Lambda(s)\}|\ge4
                         \qquad(q=1,2,3).                \tag{1.1}
\]

Form `Q(F,Lambda)` by adjoining a carrier triangle `c_1c_2c_3` and the
incidence edge `sc_q` precisely when `q in Lambda(s)`.  An anchored `K_4`
means four disjoint connected pairwise adjacent bags in `Q` which together
use exactly four vertices of `S`, one per bag.

### Theorem 1.1 (colour, rooted model, or one-block state)

At least one of the following holds.

1. `F` is properly list-colourable from `Lambda`.
2. `Q(F,Lambda)` has an anchored `K_4`.
3. There is a literal edge `pq in E(F)` such that

\[
                         S-\{p,q\}\quad\hbox{is independent}. \tag{1.2}
\]

Outcome 3 is exactly an admissible one-block equality partition:
`I=S-{p,q}` is an independent set of order five, while `{p}` and `{q}`
are singleton blocks whose two literal anchors are adjacent.  Thus the
partition is

\[
                         I\mid\{p\}\mid\{q\}.           \tag{1.3}
\]

This is a rooted-model principle, not a classification of Moser labels or
block-chain positions.  Its finite boundary order is essential.

## 2. Exhaustive proof and certificate

The proof is a complete finite enumeration implemented in
`hc7_exact7_raw_list_no_k4_search.py`.  The encoding is as follows.

1. `networkx.graph_atlas_g()` supplies one representative of every
   unlabelled simple graph on seven vertices.  Retaining the triangle-free
   representatives gives 107 graphs, including disconnected graphs.
2. Boolean variable `x_{s,q}` records `q in Lambda(s)`.  Nonemptiness is
   `Or_q x_{s,q}` and (1.1) is a cardinality-at-least-four constraint for
   each `q`.
3. For every proper ordinary three-colouring `phi` of `F`, the clause

\[
                      \bigvee_{s\in S}\neg x_{s,\phi(s)} \tag{2.1}
\]

   says that `phi` is not a list-colouring.  Imposing (2.1) for every
   proper `phi` is exactly the negation of outcome 1.
4. For each of the `binom(7,4)` choices of four boundary roots, assign each
   of the three carrier vertices to one of the four rooted bags or leave it
   unused.  These `5^3` assignments exhaust anchored models: a bag contains
   its one boundary root and an arbitrary subset of the three carrier
   vertices.  Its connectivity says either that it is a singleton root or
   that the root sees at least one assigned carrier; two carrier-bearing
   bags are adjacent through the carrier triangle, and every other bag pair
   is checked by a literal boundary edge or incidence variable.  Negating
   every successful conjunction is exactly the negation of outcome 2.

The solver enumerates every assignment satisfying items 2--4, not merely one
model per graph.  Across all 107 graphs it returns exactly 150 assignments,
supported on only three unlabelled boundary graphs:

| boundary graph | assignments |
|---|---:|
| `K_2 dotunion 5K_1` | 60 |
| `P_3 dotunion 4K_1` | 84 |
| `P_4 dotunion 3K_1` | 6 |

The merged machine-readable catalogue is
`hc7_exact7_raw_list_no_k4_catalogue.json`.  The independent propagation
check records that every returned assignment has exactly two raw singleton
lists, no full list, and reaches a unit conflict; these diagnostics are not
needed for Theorem 1.1.

There is also a deterministic non-SAT verifier
`hc7_exact7_raw_list_no_k4_verify.py`.  It handles the raw-list boundary
adversarially as follows.  The audited full-list completion proves outcome 2
whenever a raw list is `123`.  If every raw list is a pair, the audited
pair-bicycle completion proves outcome 1 or 2.  It therefore remains to
enumerate the nonfull assignments having a singleton.  Exactly 9,450
labelled assignments satisfy (1.1).  On all 107 atlas graphs, exact unit
propagation followed by residual backtracking finds 194,706 uncolourable
states.  The independent four-root/three-carrier search finds an anchored
`K_4` in 194,556 of them.  For each of the remaining 150 states the verifier
directly asserts, before any orbit grouping, that some edge `pq` has
independent complement.  The number of failures of outcome 3 is zero.

Up to a boundary-graph automorphism and a palette permutation, the 150
states form exactly four orbits.  Writing only the nonisolated path in its
linear order gives the complete countercatalogue to the false dichotomy
“list-colourable or anchored `K_4`”:

| type | boundary graph | lists on the nonisolated path | lists on the isolated vertices |
|---|---|---|---|
| `A` | `K_2 dotunion 5K_1` | `3,3` | `3 x 12, 1 x 13, 1 x 23` |
| `B` | `P_3 dotunion 4K_1` | `1,1,13` | `1 x 12, 3 x 23` |
| `C` | `P_3 dotunion 4K_1` | `1,13,3` | `2 x 12, 2 x 23` |
| `D` | `P_4 dotunion 3K_1` | `23,2,2,12` | `3 x 13` |

Every colour has support exactly four in each row.  Types `A,B,D` have a
literal equal-singleton conflict edge.  Type `C` is the necessary sharp
exception to that shortcut: forcing colour `1` at one end of the path forces
colour `3` at its middle and conflicts with the colour-`3` singleton at the
other end.

Each of the three displayed graphs has a literal edge whose endpoints cover
all of its edges: take the unique edge of `K_2`, either edge incident with
the middle vertex of `P_3`, and the middle edge of `P_4`.  Deleting its two
ends leaves an independent five-set.  Thus every assignment left after
negating outcomes 1 and 2 satisfies outcome 3.  This proves Theorem 1.1.
`square`

The companion proof in `hc7_exact7_forced_path_completion.md` explains why
the 150 residual assignments are unit-path conflicts rather than stable
pair-list bicycles; the present enumeration additionally proves that their
underlying boundary graph always exposes the admissible one-block state.

## 3. Literal lift in the exact `(1,3)` cell

Return to an exact-seven `(1,3)` separation.  Suppose the thin shore has a
spanning partition into three connected pairwise adjacent carriers
`C_1,C_2,C_3`, each contacting at least four literal boundary vertices, and
let (1.1) be their raw contact lists.

* In outcome 1, the audited spanning-triangle list-state theorem contracts
  the three independent colour blocks into the selected carriers on one
  side and into three full packets on the other.  The two proper-minor
  six-colourings induce the same literal boundary partition and glue.
* In outcome 2, replace each `c_q` by `C_q`.  The four anchored bags lift
  literally.  Anchor the three opposite full packets at the remaining
  boundary vertices.  The six anchored-bag edges, twelve mixed packet edges,
  and three packet--packet edges give all `6+12+3=21` adjacencies of a
  literal `K_7` model.
* In outcome 3, put `I=S-{p,q}` and choose one connected `S`-full packet
  `P_L` in the left open shore and one `P_R` in the right open shore.
  Contract `P_L union I` in a proper minor.  The contracted vertex is
  adjacent to both literal vertices `p,q` by packet fullness, and `pq` is a
  literal edge, so these three vertices form a triangle in the minor.  A
  six-colouring, restricted to the right shore and expanded by giving every
  vertex of the independent set `I` the contracted colour, therefore induces
  exactly the equality partition (1.3).  Contracting `P_R union I`
  symmetrically gives a colouring of the left shore with the same exact
  partition.  Permute the three distinct block colours on one side and glue;
  there are no edges between the open shores.  Only one full packet on each
  side is used.

Hence the assumed spanning three-carrier state cannot occur in a
hypothetical counterexample.

## 4. Closure of the rank-two block-chain branch

The audited block-chain list exchange starts from a gate-rooted triangle of
portal rank two in one lobe.  If the other lobe has a cutvertex, every
noncrossed duty split already gives a literal `K_7`; every surviving cut has
one global crossed orientation.  At each such cut the three carriers in
(6.1) of that theorem span the thin shore and each has at least four literal
boundary contacts.

Theorem 1.1 and Section 3 therefore close every one of those states.  We
obtain the following infinite-family conclusion.

### Corollary 4.1 (rank-two cut-lobe closure)

In the exact-seven `(1,3)` two-lobe setting, suppose one lobe has a spanning
gate-rooted triangle of literal portal rank two.  If the opposite lobe has a
cutvertex, then `G` has a literal `K_7` minor or is six-colourable.

Thus a target-free rank-two pair of lobes is two-connected on the lobe used
for the block exchange.  This closes all multi-block and bridge-block chains
at once; no forced-bicycle transport remains in that branch.

The corollary does not handle maximum rooted-triangle portal rank one, nor a
pair of genuinely two-connected lobes.  Those are the exact remaining
portal-rank cells.
