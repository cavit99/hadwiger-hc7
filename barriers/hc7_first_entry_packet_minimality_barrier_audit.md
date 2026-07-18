# Independent audit: first-entry packet-minimality barrier

**Verdict:** **GREEN for the stated geometric refutation.**  The graph is
six-connected and `K_7`-minor-free, the displayed boundary colouring and
minimum adjacent full pair are valid, and the selected direct-entry path
has minimum possible intersection with the pair.  The construction does
not refute any theorem using the full hypothetical-counterexample
hypotheses or allowing the common boundary partition already present here.

**Audited source:**
`barriers/hc7_first_entry_packet_minimality_barrier.md`.

**Source SHA-256:**
`f731d5fec15e1734fb5ff2b465efaa71ed97fbed47670331c3abd27077ee3a28`.

**Verifier:**
`barriers/hc7_first_entry_packet_minimality_barrier_verify.py`.

**Verifier SHA-256:**
`ca0b251ff2a46a53888736fca8b02f37180b1b62e88a524b36100718a70681cf`.

## 1. Independent structural replay

The graph has twelve vertices and thirty-eight edges.  Exhaustive deletion
of vertex sets confirms that no set of order at most five disconnects it.
There are eight minimum cuts of order six; the source displays one of them,
which isolates `c1`.  Thus the connectivity is exactly six and the minimum
degree is six.

An independent connected-partition search found no `K_7` minor.  The
search enumerates canonical spanning partitions into seven nonempty
connected branch sets and tests pairwise adjacency.  Spanning is without
loss because every component outside a minor model can be absorbed along a
path into an adjacent branch set.  As a positive control, the same solver
finds a `K_6` model.

## 2. Colour and connected-subgraph checks

The colouring with equality partition

\[
 \{1,4,6\}\mid\{2,5\}\mid\{0\}\mid\{3\}
\]

is proper.  Enumeration of connected boundary-full subsets of `A` shows
that its only inclusion-minimal members are `{a1,a2}` and `{c1,c2}`.  They
are disjoint and adjacent through `a2c1`; no singleton in `A` is
boundary-full.  Their total order four is therefore minimum.

The path `0-a1-a2-3` is bichromatic and has two internal vertices.  No
vertex in `A` is adjacent to both `0` and `3`, so no bichromatic path has
only one internal vertex.  Every such path has its internal vertices in
`A=P_1 union P_2`, since no other vertex uses either endpoint colour and
`03` is absent.  The selected path consequently has minimum possible
intersection with the selected union and enters it directly.

Fresh runs of the verifier under both normal and optimized Python produced

```text
GREEN first-entry packet-minimality barrier
vertices=12 edges=38 connectivity=6 K7_minor=no
```

## 3. Exact scope

The graph is five-colourable, not seven-chromatic or
contraction-critical.  Its connectivity is six, not seven.  The boundary
has a clique odd-cycle transversal and is not one of the ten hard
absolute-demand-three graphs.  Finally, the displayed partition extends
through both closed shores.

The example therefore refutes only the claim that packet/path
lexicographic minimality automatically yields a smaller full pair at a
direct entry.  Seven-connectivity, hard-boundary structure, and a
proper-minor colouring response remain available to a positive `HC_7`
argument.
