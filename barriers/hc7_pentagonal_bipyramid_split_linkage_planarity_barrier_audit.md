# Independent audit of the split/linkage/planarity barrier

**Verdict: GREEN.**

This audit checks the exact revisions

- `hc7_pentagonal_bipyramid_split_linkage_planarity_barrier.md` with
  SHA-256
  `dddd2eeafd34cca51199fdbcdfa760332ab3272b071086797a4fee05eca05ec8`;
- `hc7_pentagonal_bipyramid_split_linkage_planarity_barrier_verify.py`
  with SHA-256
  `4a482657438d9a4c92b63f76d5d3bfaf190f16f5e838c8a61638446d1be9390b`.

## Construction and connectivity

The edge list in the note agrees with the verifier.  Each of the seven
label classes induces an edge, and two different classes have an edge
between them exactly when their labels are adjacent in
`C_5\vee\overline{K_2}`.

The verifier exhausts every deletion of zero, one, two, three or four
vertices and checks that the remaining graph is connected.  This proves
vertex-connectivity at least five.  Its computed minimum degree is five;
deleting the five neighbours of a degree-five vertex isolates it while
leaving other vertices, so the connectivity is exactly five.

## The two failed local mechanisms

For a two-vertex path column the only connected bipartition into two
nonempty sets is its endpoint partition.  The verifier records, for each
endpoint, all old labels contacted by that endpoint.  It checks both
orientations on every four-element subsequence of the prescribed cyclic
neighbour order.  This is exactly the four-distinct-label alternating-cut
condition, including contacts seen by both endpoints.

For each of the five adjacent rim pairs, the verifier assigns each of its
four vertices independently to the first connected set, the second
connected set, or neither.  Thus it exhausts all disjoint choices of the
two sets.  It then checks connectedness and the four prescribed portal
contacts from the adjacent-rim linkage theorem.  No feasible assignment
exists.

## Nonplanarity and the positive global model

The nine displayed paths form a subdivision of `K_{3,3}`: their ends give
the stated bipartition, every consecutive pair is an edge, and all path
interiors are mutually disjoint and avoid the six branch vertices.

The five displayed sets are pairwise disjoint and connected.  The
verifier checks an edge between every two of them.  Each contains the
whole indicated old column, so this is an anchored `K_5`-minor model with
five distinct retained labels.  Consequently the example refutes exactly
the proposed local split/linkage/planarity trichotomy, not the desired
global rooted-model conclusion.

Running

```text
python3 barriers/hc7_pentagonal_bipyramid_split_linkage_planarity_barrier_verify.py
```

returns

```text
pentagonal-bipyramid split/linkage/planarity barrier: PASS
```

## Trust boundary

This is a finite static core.  It does not assert five-chromaticity,
operation-specific proper-minor colourings, or occurrence in a
seven-contraction-critical host.  It proves that five-connectivity plus
the seven-column contact pattern cannot make one-column alternating cuts
and adjacent-pair Two Paths tests a complete structural theorem.  A valid
replacement needs a genuinely multi-column allocation outcome or an
additional dynamic hypothesis.
