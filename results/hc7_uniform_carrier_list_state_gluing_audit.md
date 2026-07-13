# Independent audit: uniform carrier-list state gluing

## Verdict

**GREEN.**  Theorem 1.1 is valid for every `k>=2`, every
`1<=q<=k-1`, and every nonempty finite boundary `S`.  Both shore
contractions are proper minors, both expansions are proper colourings,
the induced equality partition on the literal boundary is exact, and the
two states can be aligned by a permutation of the full `(k-1)`-colour
palette.  The limiting case `(k,q)=(2,1)` causes no exception.

The packet-side notation silently relabels the selected packets so that
the packet assigned to `I_i` is called `P_i`.  This is harmless because
the original `q` packets are pairwise disjoint and every packet is
`S`-full; it should merely be read as an injective assignment followed by
reindexing.

## 1. Parameters and the carrier-side minor

Let

\[
                         I_i=\phi^{-1}(i).
\]

Because `phi` is a proper colouring of `G[S]`, each `I_i` is independent.
The list condition says that every `s in I_i` has a literal neighbour in
`C_i`.  Thus

\[
                         A_i=C_i\cup I_i
\]

is connected, including when `I_i` is empty.  The `A_i` are pairwise
disjoint and cover `L union S`.

The simultaneous contraction is a **proper** minor.  There are `q`
nonempty carriers and `S` is nonempty, so

\[
                 |L\cup S|\ge q+1.
\]

Consequently at least one of the `q` sets `A_i` has at least two vertices,
and contracting all connected `A_i` strictly reduces the vertex count.
Strong contraction-criticality therefore supplies a `(k-1)`-colouring.

The images `a_1,...,a_q` form a clique, since every pair of carriers is
adjacent.  The numerical hypothesis `q<=k-1` is exactly compatible with
this clique in a `(k-1)`-colouring, and it forces distinct colours on all
the `a_i`, in particular on the images associated with nonempty boundary
blocks.

After restriction to `R` and expansion over `S`, every possible edge is
proper:

* an edge within one `I_i` does not exist;
* an edge between `I_i` and `I_j` has differently coloured endpoints
  because `a_i a_j` is an edge;
* every original edge from `s in I_i` to `R` is represented by an edge
  from `a_i` to the same vertex after contraction; and
* edges internal to `R` retain the minor colouring.

Hence this side properly colours `G[R union S]`.  Distinct nonempty
`I_i` receive distinct colours, while all members of one `I_i` receive
the same colour, so the induced equality partition is **exactly** the
family of nonempty `I_i`.

## 2. Packet assignment and packet-side minor

Let `r` be the number of nonempty `I_i`.  Since `S` is nonempty,

\[
                         1\le r\le q.
\]

There are `q` pairwise disjoint packets, so the `r` nonempty blocks can
be assigned distinct packets.  Relabel the assigned packets by their
block indices.  For every nonempty block,

\[
                         D_i=P_i\cup I_i
\]

is connected: `P_i` is connected and every literal vertex of `I_i` has
a neighbour in `P_i` by `S`-fullness.  It is nontrivial because both
`P_i` and `I_i` are nonempty and lie in disjoint parts of the vertex
partition.  The `D_i` are pairwise disjoint.  Thus contracting them
strictly lowers the vertex count and again produces a proper minor.

For distinct nonempty blocks `I_i,I_j`, choose any `s in I_j`.
`S`-fullness gives an edge from `P_i` to `s`, hence an edge between the
contracted images `d_i,d_j`.  All `d_i` therefore form a clique and get
pairwise distinct colours.

Restrict the minor colouring to `L` and expand each literal `I_i` with
the colour of `d_i`.  Independence handles edges within a block, the
clique of contracted images handles boundary edges between blocks, and
every original `sL` edge became a `d_iL` edge.  Edges internal to `L`
retain their minor colours.  This properly colours `G[L union S]` and
again induces exactly the nonempty `I_i` as its boundary equality
partition.  Empty blocks require neither a packet nor a contracted
image.

## 3. Palette permutation and gluing

Each shore colouring uses exactly `r` pairwise distinct colours on the
`r` boundary blocks.  Mapping the colour of each block on one shore to
the colour of the same block on the other gives a bijection between two
`r`-element subsets of the `(k-1)`-element palette.  Since

\[
                         r\le q\le k-1,
\]

this partial bijection extends to a permutation of the whole palette.
After applying it to one closed-shore colouring, the two colourings agree
at every literal vertex of `S`.  There are no `LR` edges, so they glue to
a proper `(k-1)`-colouring of all of `G`.

No step depends on `|S|` except that `S` be nonempty.  Large blocks and
empty palette classes are both handled explicitly.

## 4. Edge case `(k,q)=(2,1)`

Here the palette has one colour and `phi:S -> {1}` can be proper only
when `G[S]` is independent.  There is one nonempty boundary block
`I_1=S`.

On the carrier side, `C_1 union S` is nontrivial and connected, so its
contraction is a proper minor and the expansion gives a one-colouring of
`G[R union S]`.  On the packet side, `P_1 union S` is nontrivial and
connected, giving the matching one-colouring of `G[L union S]`.  The
unique block colour is already aligned; the permutation group of the
one-colour palette is trivial.  Gluing gives a one-colouring of `G`, the
required contradiction.  Thus the proof does not tacitly require
`k>=3` or `q>=2`.

## 5. Relation to the audited exact-seven result

At `(k,q)=(7,3)` and `|S|=7`, the proof specializes line for line to the
audited exact-seven spanning-triangle list-state theorem.  The present
statement is a genuine parameter-uniform formulation of the same
contraction-and-gluing mechanism; it does not add a geometric existence
claim for the carrier partition or the list-colouring.
