# Independent audit: three-packet boundary-core handoff

Audited file:
`results/hc7_exact7_three_packet_boundary_core_handoff.md`.

Audited SHA-256:
`cef65412bc4ecb094da4b9ea4fd1476ae8a65ecabd6300e89dd040127fba9f75`.

After this audit, the source's status line alone was changed from
"awaiting independent audit" to "proved and independently audited".  The
resulting SHA-256 is
`7f71d38a575a563cef44936961610cb7abdbc307e6982f0d72a098c6bead0c21`;
the mathematical text is unchanged.

**Verdict:** **GREEN.**

Both boundary-core constructions give seven literal, disjoint, connected
branch sets.  All adjacencies outside the three singleton `T`-bags are
forced, and one literal edge in `H[T]` leaves at most two missing pairs,
which share the third `T`-bag.  This is exactly the repository's
`K_7^vee` convention.  The path-extension lemma and the connected-thin-
shore inference are also valid.

## 1. The singleton core

When `D={d}`, the disjoint partition

\[
                  S=\{d\}\mathbin{\dot\cup}T
                    \mathbin{\dot\cup}\{x_0,x_1,x_2\}
\]

and the vertex-disjoint packets make all seven bags in (1.3) disjoint.
Each anchored packet bag is connected because an `S`-full connected packet
has a neighbour at its assigned anchor.

The three packet bags form a clique.  The two rich packet bags are adjacent
by hypothesis.  The thin packet bag contains `x_0`, and each rich packet
has a literal neighbour at `x_0`, supplying its other two packet-bag
adjacencies.  Every packet bag is adjacent to `{d}` and each singleton
`{t}`, `t in T`, by packet fullness.  Domination of `T` by the singleton
core gives all three edges from `{d}` to the `T`-bags.

Thus only pairs among the three `T`-bags can be absent.  If `t_0t_1` is
the required edge of `H[T]`, the only two possibly absent pairs are
`t_2t_0` and `t_2t_1`, both incident with `{t_2}`.

## 2. The two-vertex core

When `D={d_0,d_1}`, connectedness of `H[D]` is exactly the literal edge
`d_0d_1`, so `D` is a connected branch set.  Now

\[
                  S=D\mathbin{\dot\cup}T
                    \mathbin{\dot\cup}\{x_0,x_1\},
\]

which makes the seven bags in (1.4) disjoint.  The two anchored packet
bags are connected as before, and `P_2` is connected by hypothesis.

The packet-bag clique is again literal: `P_1-P_2` is assumed, while both
rich packets meet the boundary vertex `x_0` in the thin packet bag.  Every
packet bag meets the connected core `D` and all three `T`-singletons by
fullness.  For each `t in T`, the domination hypothesis supplies an edge
from `t` to at least one member of `D`; this is exactly the required
bag adjacency.  The same edge of `H[T]` leaves at most the two incident
missing pairs described above.

No adjacency between the two shores is inferred: the proof routes the
thin-to-rich packet adjacencies through literal boundary anchors.

## 3. Near-clique convention

The repository uses `K_7^vee` for `K_7` with two incident edges deleted,
and permits extra edges between branch sets.  If exactly two pairs are
absent here, the preceding checks identify their common singleton centre.
If only one or no pair is absent, the model contains a labelled
`K_7^vee` after ignoring one or two harmless extra adjacencies.  Thus the
conclusion matches the established usage and does not require induced
nonadjacency.

## 4. Adjacent-packet extension

Take a shortest path in connected `G[R]` between the two original packet
vertex sets.  Its internal vertices avoid both packets; otherwise a proper
subpath would be shorter.  Add the internal path and all its edges except
the terminal vertex in the second packet to the first packet.  The enlarged
packet is connected, remains disjoint from the second, and remains
`S`-full.  The final path edge makes the two packets adjacent.  If the
shortest path has length one, the original packets are already adjacent.
This verifies Lemma 2.1, including its zero-internal-vertex case.

## 5. Connected-rich exact-seven consequence

Behind an actual seven-adhesion in the seven-connected kernel, every
component of either open shore is `S`-full: its neighbourhood is contained
in the seven-vertex boundary and separates it from the nonempty opposite
shore.  If the packet-number-one thin shore had two components, those two
components would themselves be disjoint full packets, a contradiction.
It therefore has one connected component, which supplies `P_L`.

Packet number two on the connected rich shore supplies two disjoint full
packets.  Lemma 2.1 makes a choice of them adjacent without losing
fullness or disjointness, so every hypothesis of Theorem 1.1 holds.  This
proves Corollary 2.2 at its stated scope.

The handoff is not a terminal proof of `HC_7`; it yields the advertised
labelled near model and leaves its normalization/composition to the
existing `S1` machinery.
