# Independent audit: first-hit rank under a label-preserving branch-set transfer

**Verdict:** **GREEN** for the exact source revision below.

This is a separate internal mathematical audit, not external peer review.  It
checks the path extension, disjointness, literal first-hit condition, response
data preserved by the underlying transfer, and the extremal corollary.

## Audited revision

The audited source is
`results/hc7_first_hit_rank_preserving_branch_set_transfer.md`.

**Source SHA-256:**

```text
8012e097021736357c2b91445f209c39b69dda58cfc3fa7ed7ddc3695be6290a
```

## 1. Definition and unchanged paths

The ranked set contains `U` but not `D`.  Hence a first-hit path whose
terminal label is not `U` avoids every vertex of `U`, including `W`.  Such
paths are unchanged when `W` is reassigned.  The designated vertices on the
fixed response subgraph `Z` are unchanged, and the transfer changes no host
edge or vertex.

There is at most one path with terminal label `U`, because terminal labels
in a ranked family are distinct.  If this path ends in `U-W`, it too is
unchanged.

## 2. Replacement of the path ending in `W`

Suppose the `U`-path ends in `W`, and let `p` be its designated port.  The
underlying transfer has a preserved edge `c_1u_1` with `c_1 in Z` and
`u_1 in U-W`.  Connectedness of `Z` gives a `p-c_1` path inside `Z`.
Appending `c_1u_1` produces a path whose only vertex outside `Z` is its
terminal in the new `U` branch set.

The relaxed rank deliberately permits path overlap inside `Z`.  Every
other path avoided the old ranked set `U`, so it avoids `u_1`; disjointness
outside `Z` is therefore preserved.  The replacement uses the same
designated port and first meets a ranked branch set at `u_1`.  This
argument is independent of whether `W` is absorbed by `D`, by an unranked
owner, or by a ranked owner.  Hence every nonterminal transfer allowed by
the underlying theorem preserves the rank.

## 3. Compatibility and extremality

The audited underlying transfer theorem preserves the fixed graph, boundary
partition, response subgraph `Z`, designated roots, and branch-set labels.
It either constructs a `K_7`-minor model or replaces `U` by the proper
connected subset `U-W`.  Thus the new model belongs to the same finite
compatibility class used in Corollary 2.2.

If the class was chosen first to maximize the first-hit rank, the theorem's
nondecrease forces the transferred rank to equal that maximum.  The strict
decrease of `|U|` then contradicts the secondary minimum.  The corollary is
therefore well founded in the fixed finite host.

## 4. Trust boundary

The result concerns the relaxed connected-kernel rank stated in the source.
It does not preserve the stricter Rado--gammoid rank in which paths must be
vertex-disjoint inside `Z`: two internally disjoint port-to-contact paths
inside `Z` need not exist.  That stricter assertion is neither stated nor
used.

The remaining owner obstruction has order at least two.  The underlying
transfer cannot move such a piece to one owner while retaining every other
named branch-set adjacency.  The theorem does not release either owned
adjacency, synchronize a colouring on a new separator, or prove `HC_7`.

No mathematical error or unstated use of connectivity was found.
