# Three-packet boundary-core handoff

**Status:** proved and independently audited.

This note gives a label-free near-`K_7` lift from an actual exact-seven
adhesion.  Its boundary hypothesis is a connected core of order at most two
which dominates an edged triple.  The open shores and their packet interiors
may have arbitrary order.

## 1. The boundary-core lift

Let

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad |S|=7,
\tag{1.1}
\]

be a separation: `L,R` are nonempty and anticomplete.  Suppose there are
three pairwise vertex-disjoint connected `S`-full subgraphs

\[
                         P_L\subseteq L,
              \qquad P_1,P_2\subseteq R,
\tag{1.2}
\]

and that `P_1` and `P_2` are adjacent.  Put `H=G[S]`.

### Theorem 1.1 (connected-core handoff)

Suppose there are disjoint sets `D,T subseteq S` such that

1. `1<=|D|<=2` and `H[D]` is connected;
2. `|T|=3` and `H[T]` contains an edge; and
3. every member of `T` has a neighbour in `D`.

Then `G` contains seven disjoint connected branch sets for which at most
two pairs are nonadjacent, and any two nonadjacent pairs have a common
branch set.  In particular, `G` contains a labelled `K_7^vee` minor.

### Proof

First let `D={d}`.  Write

\[
                         S-(D\cup T)=\{x_0,x_1,x_2\}.
\]

Use the seven branch sets

\[
 P_L\cup\{x_0\},\quad P_1\cup\{x_1\},\quad
 P_2\cup\{x_2\},\quad \{d\},\quad \{t\}\ (t\in T).
\tag{1.3}
\]

They are disjoint and connected.  The three packet bags are pairwise
adjacent: `P_1-P_2` is an assumed literal edge, while `P_L+x_0` meets each
rich packet through that packet's contact with `x_0`.  Every packet bag is
adjacent to every one of the last four bags by `S`-fullness.  The bag
`{d}` is adjacent to all three `T`-bags by domination.  Among the three
`T`-bags at least one pair is adjacent; hence the only possible missing
pairs in (1.3) are the other two pairs inside `T`, and they share the
remaining `T`-bag.

Now let `D={d_0,d_1}`, where `d_0d_1` is an edge, and write

\[
                         S-(D\cup T)=\{x_0,x_1\}.
\]

Use

\[
 P_L\cup\{x_0\},\quad P_1\cup\{x_1\},\quad P_2,
 \quad D,\quad \{t\}\ (t\in T).
\tag{1.4}
\]

Again the packet bags are pairwise adjacent: `P_1-P_2` is literal,
`P_L+x_0` meets both rich packets at `x_0`, and all three packet bags meet
the four boundary bags by fullness.  The set `D` is connected and is
adjacent to every `T`-bag by domination.  As before, the edge in `H[T]`
leaves at most two missing pairs, both incident with the third `T`-bag.
Thus (1.4) has the required near-clique adjacency pattern. \(\square\)

No completion edge, quotient edge, or palette-to-label identification is
used in the proof.  Every displayed adjacency is a literal edge of `G`.

## 2. Connected-rich exact-seven consequence

### Lemma 2.1 (make the rich packets adjacent)

If `G[R]` is connected and contains two disjoint connected `S`-full
packets, then it contains two such packets which are adjacent.

### Proof

Choose a shortest path from the first packet to the second.  Its internal
vertices avoid both packets.  Add all internal vertices, and the path edge
incident with the first packet, to the first packet, stopping before the
endpoint in the second packet.  The enlarged first packet remains
connected, full, and disjoint from the second, and the last path edge joins
them. \(\square\)

### Corollary 2.2

In an actual `(1,2)` exact-seven adhesion whose rich open shore is
connected, Theorem 1.1 applies whenever the boundary has the displayed
core and triple.

### Proof

Every component of either open shore is `S`-full.  Since the thin shore has
packet number one, it has only one component, which supplies `P_L`.
Apply Lemma 2.1 to the two rich packets and then Theorem 1.1. \(\square\)

## 3. Exact scope

The theorem is an unbounded structural handoff, but it is not a terminal
proof of `HC_7`: an arbitrary labelled `K_7^vee` model still requires the
audited `S1` normalization/composition machinery.  Nor does failure of the
boundary-core condition imply one specific boundary graph without the
separate frozen adaptive-residual hypotheses.

In the attained paired-triangle laboratory, exhaustive diagnostics show
that the boundary-core condition handles 392 of the 512 minimal literal
edge choices.  After imposing the frozen connected-rich adaptive residue,
the maximal failures form four sparse series-parallel boundary types.  That
finite observation is a guide to the remaining portal/state exchange; it
is not used in Theorem 1.1.
