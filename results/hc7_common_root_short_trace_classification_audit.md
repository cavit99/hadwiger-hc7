# Audit: low-degree common-root short-trace classification

**Audit type:** separate internal cold audit

**Verdict:** **GREEN**

Audited theorem:
[`hc7_common_root_short_trace_classification.md`](hc7_common_root_short_trace_classification.md)

Audited source SHA-256:

```text
dc57ab0da71b46cf0e6e878f0f0612aa7ed2698b5227a527a806ec9091a83670
```

## Checked scope

The proof was checked from the imported common-root hypotheses, including
all quantifiers over the fixed `F`-extension and separately chosen
`E`-extensions.

- Maximum independent sets chosen inside the distinct boundary
  `alpha`--`beta` components have independent union.  This proves the
  summed bound and the degree-eight/nine trace limits.  In the four-trace
  equality case, each connected bipartite trace has independence number
  one and is therefore `K_1` or `K_2`.
- The full-component multigraph has one edge per boundary trace.  A
  nonparallel cycle through the operated edge therefore uses exactly four
  edges, forcing degree nine and the two transverse two-by-two partitions.
- In Theorem 2, if the operated traces occupy distinct fixed `F`-blocks,
  both blocks have order at least two and exhaust the four labels.  For
  every separately chosen `E`-extension, the operated edge lies either in
  the unique parallel pair with its fixed mate or in the exact transverse
  four-cycle.  At degree eight, the common fixed block is either exactly
  `{i,j}`, forcing that same bilateral pair in every corresponding
  `E`-extension, or it contains all three traces, which are all `K_1` or
  `K_2`.
- In the four-cycle geometry, shortest carrier paths have nonempty open
  interiors in their named shores.  Same-shore full components and the two
  exterior components give the required disjointness and anticompleteness.
  Boundary paths inside the four disjoint traces consequently form a
  simple cycle.
- The odd-cycle parity is correct.  Endpoint phases cancel around the four
  boundary paths and four carrier paths; the two shore colourings differ
  on exactly the operated trace, producing exactly one phase reversal.
- Connectivity of each exterior component supplies a shortest path between
  its two same-shore sectors.  Its interior avoids the cycle.  The two
  resulting paths are vertex-disjoint and their four ends alternate.
  This is a subdivision of `K_4`.  Splitting its rim and chord paths assigns
  one distinct boundary trace to each of four disjoint connected branch
  sets, so the model is `X`-meeting; adding `{u}` validly gives `K_5`.
- In Theorem 4, dimensions two and three are handled exhaustively.  If
  neither endpoint of the original coordinate-zero cut edge had a second
  cut edge, the displayed noncut equalities and antipodal invariance would
  equate the rejectors at the two ends of the original cut.  Thus one
  endpoint has changing coordinates `0,j`.  Switching coordinate zero
  preserves the literal set `W_0={x}`, so Theorem 2 gives exactly the
  stated bilateral or atomic alternatives with the named root retained.
- In Theorem 5, a choice of one vertex from each atomic trace is independent
  because distinct boundary two-colour components are anticomplete.  Its
  order attains the neighbourhood independence bound, and its complement
  in `X` consequently has order five.
- Contracting the star on `{u} union I` is a proper minor.  Expansion deletes
  exactly the edges `ui` with `i in I`.  If the five remaining boundary
  vertices used at most four further colours, a colour absent from `X`
  could be assigned to `u`, restoring those edges and six-colouring `G`.
  Hence the remaining five vertices use the five other colours singly.
  Deleting `u` gives the asserted one colouring through both exterior
  components.
- On a closed shore containing `u`, the colour of `u` is absent from `X`.
  An exact `I`-block therefore leaves at most four colours for the five
  vertices of `R`, forcing a monochromatic boundary nonedge.  This proves
  the claimed obstruction to the five-singleton partition on that shore.
- For Theorem 5(5), the two chord ends of the topological `K_4` lie in the
  open-shore sectors.  Each rim arc therefore contains its corresponding
  boundary subpath in `W_r`; cutting that arc just after the selected
  representative assigns the four representatives to four distinct
  connected branch sets without changing the model.

No hidden synchronization of the separately chosen `E`-extensions is used.

## Dependencies and nonterminal boundary

No internal proof gap was found.  The result remains conditional on the
cited, separately audited synchronized flip-cube theorem, alternating-cycle
theorem, and low-degree neighbourhood independence bound.  The proper-minor
colouring in Theorem 5 also uses the full contraction-critical hypothesis,
not merely the displayed boundary geometry.

The theorem does not produce a common complete boundary partition, align a
proper-minor response with the displayed branch sets, construct a `K_7`
minor, give a strict same-host descent, close the common-root branch, or
prove `HC_7`.  The bilateral component may contain additional boundary
traces, and the four-cycle construction yields only an `X`-meeting `K_4`
model (`K_5` after adding `u`).  The common five-singleton colouring is a
colouring of `G-u`; it is not a common boundary partition on either closed
shore containing `u`, and it does not reserve a seventh branch set after a
rooted model is built.
