# Cold audit of the `|W|=3` one-mark decoder

**Verdict: GREEN.**  The one-mark four-linkage, the two labelled
`K_7^-` models, the terminal-row decoder, and the closure of tails of order
at most two in
[`hc7_marked_three_clique_w3_one_mark_decoder.md`](hc7_marked_three_clique_w3_one_mark_decoder.md)
are correct.  The three-vertex packet at the end is only a local
guardrail, as stated.

## Linkage and near-model

Deleting two marks from the six-connected host leaves a four-connected
graph.  After taking trivial paths on `I=Q cap B`, both residual terminal
sets in Lemma 2.1 have order `4-|I|`, so set-Menger gives paths with
distinct starts and ends.  A nontrivial path starts in `Q-B subseteq P`;
the only exits from `P` after the other two marks are deleted are precisely
the target vertices.  Shortening at the first target therefore leaves all
internal vertices in `P`.

Absorbing the three `B`-ending paths into their distinct large cells
preserves disjointness and connectedness.  Their initial roots, and the
fourth root left in `R_c`, lie in the literal clique `Q`.  This supplies
all mutual cell/root adjacencies.  The endpoint edge to `z_c` gives
`R_c-D_c`; no argument supplies `R_c-D_d`, and the note correctly lists
that as the sole possible missing edge.

## Terminal row and small tails

If three vertices of `Q` lie in `B`, they form one vertex in each large
cell.  Their clique edges make the three connected cell bags pairwise
adjacent.  The remaining `Q` vertex lies in `P`, so the packet contacts all
three cells, both other marked row bags, and `z_i`.  This is a literal
seven-bag model.

If `|P|=2` and `|Q cap B|=2`, write `P={q,q'}` and let `u_3` be the sole
non-`Q` boundary vertex.  Each of `q,q'` has the four fixed clique
neighbours consisting of the other packet vertex, `z_i`, and the two
members of `Q cap B`.  Its entire possible neighbour set has three further
vertices `z_a,z_b,u_3`.  If it missed either outside mark, minimum degree
six would force the other mark and `u_3`, making its neighbourhood a
six-cut that omits the missed mark.  Thus both packet vertices see both
outside marks.  Fullness gives an edge from at least one, say `q`, to
`u_3`.

The two trivial roots and `q` form a literal triangle in `Q`, so absorbing
`q` into the third cell makes the three cells pairwise adjacent.  The
reserved singleton `q'` contacts the first two cells through the clique,
the third through `q'q`, both outside row bags through its marked edges,
and `z_i` through the named clique.  Together with the standard remaining
bags this verifies all twenty-one adjacencies.  Therefore every live tail
has order at least three.

## Guardrail and scope

In the displayed three-vertex local packet, any three-root
terminalization uses two of `q_1,q_2,q_3` for the two nontrivial boundary
ends, leaving the third as the reserved root.  By construction no such
root sees both outside marks.  This correctly refutes a proof based only
on the stated local incidence.  It is not asserted to be six-connected,
`K_7`-minor-free, or a counterexample to the marked theorem.

The exact audited residue is simultaneous compatibility for tails of
order at least three.  The note does not close the balanced `|W|=3` cell.
