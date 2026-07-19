# First-hit rank under a label-preserving branch-set transfer

**Status:** written proof; separate internal audit GREEN in
[`hc7_first_hit_rank_preserving_branch_set_transfer_audit.md`](hc7_first_hit_rank_preserving_branch_set_transfer_audit.md).
This theorem
isolates the exact part of the two-contact branch-set transfer on which the
labelled first-hit rank is monotone.  It does not prove `HC_7`.

## 1. Setting

Use the spanning labelled `K_7`-minus-one-edge model

\[
                 X,\ Y,\ D,\ U,\ F_1,\ F_2,\ F_3
\]

and the two-contact transfer setting of
[`hc7_response_aligned_two_contact_lobe_transfer.md`](../results/hc7_response_aligned_two_contact_lobe_transfer.md).
Thus `Z subseteq D` is a fixed connected response subgraph, `P subseteq Z`
is a set of permitted source ports, and `U=W dotcup U'`, where `W,U'` are
nonempty and connected and `U'` contains the prescribed root of `U`.

Fix a set `L` of ranked labels chosen from

\[
                  \{X,Y,U,F_1,F_2,F_3\},
              \qquad U\in L.                           \tag{1.1}
\]

For a compatible labelled model `M`, let `lambda(M)` be the maximum number
of paths with the following properties:

1. each path has a designated port in `P` on `Z`, the designated ports are
   distinct, and the paths are pairwise vertex-disjoint outside `Z`;
2. their other ends lie in branch sets with different labels in `L`; and
3. each path meets the union of the ranked branch sets only in its terminal
   vertex.

Thus every terminal vertex is a literal first model-bag hit.  This
is a relaxed connected-kernel rank: the paths may overlap arbitrarily inside
`Z`, and a designated port need not be their only vertex in `Z` or `P`.
It is not the stricter Rado--gammoid rank in which the paths are
vertex-disjoint everywhere.

The transfer theorem replaces `U` by `U'=U-W`.  If the owner set is empty,
it adds `W` to `D`.  If the owner set is `{R}`, it adds `W` to `R`.

## 2. Rank-preservation theorem

### Theorem 2.1

Assume that the two-contact transfer has a nonterminal
`K_7`-minus-one-edge outcome.  Thus the owner set of `W` has order at most
one.  Then the transferred model `M'` satisfies

\[
                         \lambda(M')\ge\lambda(M).      \tag{2.1}
\]

The selected boundary partition, response subgraph, prescribed roots and
all branch-set labels are the same objects preserved by the underlying
transfer theorem.

#### Proof

Choose a first-hit path family of order `lambda(M)`.  Every path whose
terminal label is different from `U` avoids all of `U`, and hence avoids
`W`.  Those paths remain valid and mutually disjoint after the transfer.

If the family has no path with terminal label `U`, this already proves
(2.1).  Otherwise let `Q` be that unique path.  If its terminal vertex lies
in `U'`, then `Q` also survives unchanged.

It remains that `Q` ends at a vertex of `W`.  Let `p` be its designated
port.  The transfer setting includes the edge `c_1u_1`, where
`c_1 in Z` and `u_1 in U'`.  Since `Z` is connected, choose a `p-c_1`
path inside `Z` and append the edge `c_1u_1`.

This replacement may meet other paths inside `Z`, which is permitted by
the definition of `lambda`; outside `Z` it consists only of the new
terminal vertex `u_1`.  Every other path avoided the old ranked branch set
`U`, and hence avoids `u_1`.  The replacement first meets a ranked branch
set at its final vertex in `U'`, uses the same designated port as `Q`, and
does not depend on which branch set, if any, absorbs `W`.  Replacing `Q` by
this path gives a valid family of the same order in `M'`, proving (2.1).
\(\square\)

### Corollary 2.2

Among all compatible models in the fixed host, first maximize `lambda` and,
subject to that, minimize `|U|`.  If the host has no `K_7` minor, then no
nonterminal transfer with owner set of order at most one is possible.

#### Proof

The transfer theorem gives an explicit `K_7` model or a compatible model
with `U'` a proper subset of `U`.  The first conclusion is excluded.  By
Theorem 2.1 the second model has first-hit rank at least the chosen maximum,
and hence equal to it, but has smaller `U`.  This contradicts the secondary
choice. \(\square\)

## 3. Exact remaining obstruction

The shared response subgraph removes the apparent source-port collision:
paths are allowed to overlap inside `Z`, while the persistent edge
`c_1u_1` supplies a new one-vertex tail into the reduced branch set.  Thus
even a ranked unique owner cannot lower `lambda`.

Consequently, after maximizing `lambda` and then minimizing `|U|`, every
root-free connected and co-connected split of `U` which separates the two
persistent contact endpoints has at least two owners.  This is the exact
remaining model-local obstruction.  Moving such a piece to one owner would
destroy an adjacency to another owner, so the two-contact transfer theorem
does not produce a compatible model.  Eliminating this multi-owner case
requires a label-preserving split which restores one owned adjacency, an
explicit `K_7`-minor model, or a colour-compatible full-neighbourhood
separation.  The present rank theorem supplies none of those conclusions.
