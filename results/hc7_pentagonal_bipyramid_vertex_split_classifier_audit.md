# Independent audit: vertex splits of the pentagonal bipyramid

**Verdict: GREEN.**

The theorem, its arbitrary two-root corollary, and the one-edge-exchange
proposition are correct with the trust boundary stated in the source.  The
finite census reproduces all reported counts.  This is an internal
mathematical audit, not external peer review.

## Audited revisions

- [`hc7_pentagonal_bipyramid_vertex_split_classifier.md`](hc7_pentagonal_bipyramid_vertex_split_classifier.md),
  SHA-256
  `ac2e367056afe2a87276c63e92278a8de2918ba371ba9825e7ac17879e318000`;
- [`hc7_pentagonal_bipyramid_vertex_split_classifier_verify.py`](hc7_pentagonal_bipyramid_vertex_split_classifier_verify.py),
  SHA-256
  `fa7f3419c66960051ae5e0723ad058e14b6216fc712156277f064d11dbef1108`.

The source was clarified before hashing to say explicitly that the
two-root orbit census identifies interchange of the two indistinguishable
added roots.  That is the equivalence relation implemented by the verifier.

## 1. Circular-word classification

Write `A=N(x_1) cap N_P(x)` and `D=N(x_2) cap N_P(x)`.  Every old neighbour
belongs to at least one set.  Marking exclusive `A`, exclusive `D`, and
common membership by `X,Y,B`, respectively, is therefore exhaustive.

The circular-order lemma is correct.

- Three `B` positions, together with any fourth position, can be assigned
  alternating `A,D,A,D` roles.
- With no `B`, absence of alternation says exactly that the `X` and `Y`
  positions are two cyclic intervals.
- With one `B`, cutting at it reduces the same assertion to two intervals
  in a linear order.
- With two `B` positions, a mixture of `X` and `Y` in either open arc gives
  an alternating quadruple.  Thus each arc is monochromatic.  If both arcs
  are nonempty and have the same mark, the two `B` endpoints and one point
  from each arc again alternate.  Hence the nonempty arcs have opposite
  marks.

These are precisely the cyclic rotations of

```text
X^r B^epsilon Y^s B^eta,
```

with `epsilon,eta` in `{0,1}`.  Conversely, in that form each clone's
incidences occupy one side of the new edge `x_1x_2`, with a common neighbour
possible only at a transition, so no alternating quadruple occurs.

As an independent exhaustive check, I generated the displayed word family
directly and compared it with all `3^4` and `3^5` words.  It contains exactly
`50` four-letter words and `82` five-letter words, and there was no mismatch
with absence of an alternating quadruple.

## 2. Planar and nonplanar sides of the split theorem

For a nonalternating word, the local-disc drawing in the proof is valid.
Place `x_1x_2` in the replacement disc, draw the `X` incidences on one side
and the `Y` incidences on the other, and draw the two incidences at a `B`
transition on opposite sides of the old radial edge.  This includes empty
exclusive blocks and adjacent transition marks.  It gives a plane drawing
of the split graph, so the graph has no `K_5` minor.

For an alternating pole split, deleting surplus clone incidences reduces
the five rim marks, up to a dihedral symmetry and clone interchange, to

```text
X,X,Y,X,Y.
```

The five displayed branch sets

```text
{q}, {c_0}, {c_1}, {x_1,c_3}, {x_2,c_2,c_4}
```

are disjoint and connected.  The pole `q` is adjacent to each other set;
`c_0c_1` is present; `c_0` and `c_1` meet the two nonsingleton sets through
the appropriate clone or consecutive rim edge; and the two nonsingleton
sets meet through `x_1x_2`.  Thus they form a `K_5`-minor model.

For a rim split, the cyclic order of the four neighbours of `c_0` is

```text
c_1,p,c_4,q.
```

An alternating assignment uses all four positions and is equivalent to
giving `x_1` the two rim neighbours and `x_2` the two poles.  The displayed
sets

```text
{p}, {c_1}, {c_2}, {q,x_2}, {c_3,c_4,x_1}
```

are again disjoint, connected, and pairwise adjacent.  Surplus incidences
can only add edges, so both explicit models lift to every original
alternating split.  This proves all three equivalent conditions in the
theorem.

I independently enumerated spanning five-part branch-set partitions of
each eight-vertex split graph and checked planarity separately.  The pole
case has `161` graphs with a `K_5` minor and `82` planar graphs; the rim case
has `31` and `50`, respectively.  These reproduce the source counts without
using the verifier's connected-mask search.

## 3. Arbitrary distribution of the two root contacts

The positive direction of the corollary is label-faithful.  Every branch
set in each explicit `K_5` model above contains an old nonsplit vertex of
`P`.  Both added roots are adjacent to every such old vertex, regardless of
which clone contact was retained.  The two singleton roots therefore join
the five sets to an explicit `K_7`-minor model.

For a nonalternating split, the ten-vertex graph is a subgraph of
`K_2 vee P_x`.  At most two branch sets of any clique-minor model can contain
the two universal vertices.  Removing those branch sets leaves a
clique-minor model in `P_x`.  Since `P_x` is planar,

```text
eta(K_2 vee P_x) <= 2 + eta(P_x) <= 6.
```

Thus no choice of the two clone-contact marks creates a `K_7` minor.  This
proves the claimed independence from the root-contact distribution.

I also independently formed the group actions rather than calling the
verifier's canonicalization routines.  With the dihedral stabilizer for a
pole split, the two commuting stabilizer involutions for a rim split, clone
interchange, and interchange of the two roots, the orbit counts are:

```text
pole: 122 total, 76 alternating, 46 nonalternating;
rim:  112 total, 52 alternating, 60 nonalternating.
```

## 4. One-edge exchanges

The orbit proof of the diagonal-flip proposition is complete.  Missing
edges have two automorphism orbits.

1. If the added edge is the pole edge `pq`, deleting a rim edge is exactly
   a facial diagonal flip.  Deleting a spoke has one stabilizer orbit, and
   the five displayed sets in the source form a `K_5` model.
2. If the added edge is the rim chord `c_0c_2`, the two facial flips delete
   `pc_1` or `qc_1`.  The old edges outside this safe orbit split into the
   five stabilizer orbits listed in the source table.  Direct inspection
   confirms that every displayed row consists of five disjoint connected,
   pairwise adjacent branch sets.  Reflection and pole interchange cover
   every edge in the relevant orbit.

Thus `P+f-e` is `K_5`-minor-free exactly for the fifteen facial flips: five
choices deleting a rim edge after adding `pq`, and ten choices deleting a
middle spoke after adding one of the five rim chords.

The two stated consequences are also correct.  Restoring the deleted rim
edge or adding any of the five rim chords to `P+pq-c_0c_1` gives a `K_5`
minor.  Adding `c_0c_2,c_0c_3` while deleting independently one of
`pc_1,qc_1` and one of `pc_4,qc_4` performs two facial flips in disjoint
face interiors (the interiors may meet only along their boundary).  All
four resulting graphs are planar.  An independent planarity and exact-minor
check confirmed all four cases.

## 5. Verifier audit

The verifier is deterministic and dependency-free.

- `has_crossing` enumerates every four-position subset in cyclic order and
  tests both clone orientations.  Alternation is invariant under cyclic
  rotation, so beginning with the least indexed chosen position loses no
  case.
- `split_graph` constructs all fifteen edges of the pentagonal bipyramid,
  removes the selected old vertex, adds the clone edge, and restores exactly
  the incidences encoded by the word.  The rim-neighbour order agrees with
  the fixed embedding.
- `exact_k5_minor` enumerates every nonempty vertex mask, retains exactly
  the connected masks, and records their full external neighbourhoods.  Its
  recursion enumerates every unordered family of five disjoint connected
  masks and accepts exactly when every pair has an edge between it.  Hence
  it is an exact branch-set test, not a bounded heuristic.
- `pole_canonical` implements the dihedral group on the rim together with
  clone interchange.  `rim_canonical` implements the independent swaps of
  the two rim neighbours and the two poles, again together with clone
  interchange.
- `rooted_canonical` applies the same spatial action, permits interchange of
  the two added roots, and applies clone interchange simultaneously to the
  split incidences and both root marks.  The coupling is essential and is
  implemented correctly.
- `is_facial_flip` recognizes exactly the fifteen cases described above:
  a rim edge opposite `pq`, or the middle spoke opposite a rim chord.
- The three census routines exhaust `3^5`, `3^4`, all two-root markings,
  and all `6*15=90` added/deleted edge pairs.  The final two loops check the
  four safe simultaneous rim flips and the six possible second contacts in
  the safe pole-edge exchange.

Running

```text
python3 results/hc7_pentagonal_bipyramid_vertex_split_classifier_verify.py
```

reproduces exactly:

```text
pole: assignments=243 k5=161 planar=82 orbits=22 planar_orbits=8
rim: assignments=81 k5=31 planar=50 orbits=20 planar_orbits=11
root-distributed pole: orbits=122 k7=76 surviving=46
root-distributed rim: orbits=112 k7=52 surviving=60
one-edge exchanges=90: diagonal-flip criterion PASS
simultaneous safe rim flips=4: all K5-free
pole safe exchange plus second contact=6: all K5
pentagonal-bipyramid vertex-split classification: PASS
```

Two trust-boundary details are worth making explicit.  The supplied script
uses the proved alternating-word criterion when it labels the two-root
orbits `k7`; it does not separately enumerate seven branch sets.  Likewise,
the simultaneous-flip loop checks absence of a `K_5` minor, while planarity
comes from the direct facial-flip construction.  Neither point is circular
in the written theorem, whose proofs are independent of the census.

## 6. Scope not proved

The result classifies an eight-vertex contact graph obtained by splitting
one quotient vertex.  It does not prove that a connected branch set in the
host can be split into the two required connected pieces, preserve selected
first edges or colouring responses, or expose an order-seven separation
when such a split fails.  It therefore supplies an exact terminal quotient
criterion, not the missing host-level exchange theorem.
