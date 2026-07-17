# Audit of the connected deficient-branch-set trichotomy

**Verdict:** GREEN for the exact source revision identified below.

This is an independent internal mathematical audit.  It verifies the
conditional graph-theoretic statements in the source note; it is not
external peer review and does not prove `HC_7` or a valid defect-one
descent.

## Audited revision

The audited file is
`results/hc7_connected_one_hole_trichotomy.md`.

**Source SHA-256:**
`41661424adfca51a5a1bacece72a0d98366bb5f3b6031e58e70e7b951f00303e`.

The mathematical source was read line by line at SHA-256
`137c1d0c1687a1aa3936804a13c108389faff73c2597c266361be09b70d31c39`,
including the
parameter-uniform Corollary 4.1 and the application to the rainbow-diamond
separation.  The two occurrences which distinguish adjacency from set
intersection and the two links to the promoted rainbow-diamond theorem are
already corrected in this audited revision.

After that audit, the source status line alone was changed from
"written proof draft awaiting a separate exact-file audit" to "written
proof; separate internal audit GREEN."  Replacing the current status line
by the former text reproduces the initially audited SHA-256 exactly.  No
theorem statement, hypothesis, proof, dependency, or trust-boundary text
changed, so the GREEN verdict applies to the current source revision above.

## 1. Retaining connectors and unavoidable vertices

An `r`-retaining connector exists because a finite union of paths in the
connected graph `G[U]`, all starting at `r` and ending at one chosen vertex
of every nonempty portal set, is connected and meets every portal.

For Lemma 1.1, every component of `G[U-T]` has an edge to `T`; otherwise it
would be a component of `G[U]`.  Hence `T` together with all components
other than `Y` is connected, is adjacent to `Y`, and contains all selected
portal vertices.  This proves all three conclusions, including the
connectedness of `U-Y`.

For Lemma 1.2, every component of `G[U-s]` has an edge to `s`.  Thus the
union of `s` with all components except the one containing `r` is connected
and adjacent to that remaining component.  If the component containing `r`
met every portal set, paths inside it would give an `r`-retaining connector
avoiding `s`.  Unavoidability therefore forces at least one entire portal
set into the opposite connected side.

For Lemma 1.3, membership in `Z_s` says that every path from `r` to that
vertex uses `s`, and membership in `Z_r` gives the reverse statement.  A
simple `r`--`v` path would then have an `s`--`v` suffix avoiding `r`, a
contradiction.  The two sides are disjoint.  Because every portal set is
nonempty, no portal set can be contained in both, so their lost-adjacency
sets are disjoint as claimed.

## 2. Seven-connected trichotomy

The open neighbourhood `S=N_G(A)` lies in the five sets `F_i` and separates
the nonempty connected sets `A` and `R`.  Seven-connectivity gives
`|S|>=7`.  Since `A` is adjacent to every `F_i`, seven vertices of `S` can
be selected with every `F_i` represented; one donor set contains two of
them.  Both selected vertices are literal neighbours of `A`.

The five foreign sets for the donor are `R` and the other four `F_j`.
Their portal sets in the donor are nonempty because
`R,F_1,...,F_5` are a `K_6`-minor model.

### Avoidable orientation

If `s` is avoidable from `r`, Lemma 1.1 produces connected adjacent sets
`Y` and `U-Y`, with `s` in the former, `r` in the latter, and all five
foreign adjacencies retained by `U-Y`.

If `Y` is anticomplete to `R`, then `R` lies outside
`Y union N_G(Y)`.  The displayed pair

\[
                 (Y\cup N_G(Y),\;V(G)-Y)
\]

is therefore a vertex separation with open sides containing `Y` and `R`.
The donor complement is connected by Lemma 1.1.  Seven-connectivity gives
the asserted lower bound on its boundary.

If `Y` is adjacent to `R`, the seven displayed branch sets in (2.9) are
valid.  In detail:

- `R union Y` is connected and `U-Y` is connected;
- `s` supplies the `A`--`(R union Y)` edge and `r` supplies the
  `A`--`(U-Y)` edge;
- the edge between `Y` and `U-Y` supplies the adjacency between those two
  modified foreign branch sets; and
- the retained portal contacts and the original `K_6` model supply every
  other adjacency.

They are disjoint because only the donor `U` was split and `Y` was merged
with the disjoint old branch set `R`.  Thus this is an explicit
`K_7`-minor model.  The reversed orientation is identical.

### Mutually unavoidable orientation

If both selected vertices are unavoidable in the opposite orientation,
Lemmas 1.2 and 1.3 produce two detachable connected sides with nonempty,
disjoint lost-adjacency label sets inside a universe of five labels.  One
has between one and two lost labels.  Its complement in the donor is
connected and adjacent to it.

If this chosen side is anticomplete to `R`, the same full-neighbourhood
separation argument applies.  Otherwise it can be merged with `A`: the
chosen side contains one of the selected neighbours of `A`, so the union is
connected, and its adjacency to `R` repairs the old missing model edge.
The donor complement is adjacent to this enlarged set across the donor
split.  For each foreign branch set, the donor complement loses its old
adjacency exactly when the whole corresponding portal set lies in the
moved side.  Hence it misses exactly one or two of the six core branch
sets.  Equations (2.12)--(2.13) therefore give, respectively, a labelled
`K_7^-`- or `K_7^\vee`-minor model with all missing edges incident with the
new deficient centre.  No unlisted model adjacency is assumed.

Finally, if a returned full-neighbourhood boundary has order seven and a
component of its deletion missed one boundary vertex, that component would
have external neighbourhood of order at most six.  Another component
exists by the actual-separation conclusion.  This contradicts
seven-connectivity, so the stated boundary fullness is correct.

## 3. Boundary-colouring proposition

A nontrivial deletion or contraction supported wholly in the open side
`Y` is a proper minor and leaves the opposite closed shore `G_R` unchanged.
Its six-colouring therefore restricts to a six-colouring of `G_R` with a
well-defined equality partition on the literal boundary `T`.

If that equality partition also extended to the unmodified closed shore
`G_L`, the two boundary colourings could be aligned block by block and the
resulting injection of used boundary colours extended to a permutation of
the six colour names.  No edge joins the two open shores, so the aligned
colourings would glue to a six-colouring of `G`, a contradiction.  The same
argument with proper operations in opposite open shores proves the final
sentence of Proposition 3.1.  The proposition correctly asserts only the
one-sided partition exclusion and the conditional gluing implication; it
does not assert that a common partition exists.

## 4. Parameter-uniform corollary

For Corollary 4.1, `N_G(A)` separates `A` from `R` and has order at least
`m+1`.  It meets every one of the `m-1` sets `F_i`, so an `m+1`-element
selection representing every `F_i` has two vertices in some donor.

The donor has exactly `m-1` foreign branch sets: `R` and the other
`m-2` sets `F_j`.  The avoidable case gives either the same
full-neighbourhood separation or exactly `m+1` pairwise adjacent branch
sets.  In the mutually unavoidable case, two nonempty lost-label sets are
disjoint subsets of an `(m-1)`-element universe, so one has size at most

\[
                         \left\lfloor\frac{m-1}{2}\right\rfloor.
\]

Moving that side either returns the separator or produces an `m`-branch-set
core plus one deficient centre whose missing edges are precisely those
lost labels.  The argument remains valid at the endpoint `m=3`.  The
fullness proof with an order-`m+1` boundary reduces a missed component's
neighbourhood to order at most `m`, exactly contradicting
`(m+1)`-connectivity.  Thus Corollary 4.1 is a genuine parameter-uniform
consequence of the same proof and does not introduce an unproved induction.

## 5. Rainbow-diamond application

The promoted rainbow-diamond theorem supplies:

- five connected pairwise adjacent sets
  `A_1,A_2,A_3,V_m,V_n`;
- a connected set `X` adjacent to all five;
- a connected set `V_r` adjacent to all five and anticomplete to `X`; and
- the literal containment of `N_G(X)` in those five branch sets.

These are exactly hypotheses 1--3 of Theorem 2.1 under substitution (5.3).
In a `K_7`-minor-free host, the explicit-minor alternative is excluded, so
the application returns either the actual separator or the asserted
one-/two-missing-spoke near-`K_7` model.

The source does not confuse the strict connected-subbag move with a valid
defect-one descent.  It explicitly records that a donor anchor need not
belong to a protected branch set; even when the donor is `V_m` or `V_n`, the
protected label, colour-matched path, admissible cut, and eligibility may be
lost.  It also cites the exact reversibility of a single connected-subbag
rotation as a barrier to treating proper containment in the current donor
as a global rank.

## 6. Trust boundary

The audited source proves a reusable connected-set trichotomy and its
uniform analogue.  It does **not** prove any of the following:

1. that the separator alternative has order at most seven;
2. that two proper-minor colourings attain the same equality partition on
   an order-seven boundary;
3. that the rotated near-`K_7` model re-enters the conditional defect-one
   component-contact setup;
4. that the protected labels, colour-matched path, admissible cut, or
   eligible selected components survive a rotation;
5. that connected-subbag containment is a well-founded host-level rank; or
6. that every hypothetical `HC_7` counterexample reaches the conditional
   rainbow-diamond hypotheses.

These limitations are stated explicitly in the source.  There is no
overclaim of a valid defect-one descent.

## Unresolved assumptions or gaps

None within Lemmas 1.1--1.3, Theorem 2.1, Proposition 3.1, Corollary 4.1,
or the stated rainbow-diamond application at the audited source hash.
