# Independent audit: three Kempe locks on a merged-root shore

**Verdict:** **GREEN** for Theorem 2.1 and its stated trust boundary.  This
is a separate internal mathematical audit, not external peer review.  The
result does not prove `HC_7`.

## Audited revision

This audit checks the complete source file
[`hc7_merged_root_three_kempe_locks.md`](hc7_merged_root_three_kempe_locks.md)
at SHA-256

```text
9892dc5ef5fbb173033471fa54d90f9d3ad34db3edc69c9f98c0a7a3c36ff130
```

The status-only promoted revision has SHA-256

```text
2705b68b8452fd8642601ed48f93c84db98e313be46c12c3f4f7ba85cd94cd41
```

It changes only the status paragraph to link this audit; the theorem,
proof, dependencies, and trust boundary are unchanged.

The source was split from the previously GREEN-audited combined draft, but
the theorem and its proof were also rechecked independently below.  No
unresolved mathematical assumption or gap remains at this revision.

## 1. Exact response and quantifier

The merged boundary partition

```text
X | Y | {d,e}
```

uses three pairwise distinct colours `xi,eta,alpha`.  Consequently exactly
three of the six palette colours are absent from the literal boundary; these
are the distinct colours `beta_1,beta_2,beta_3` in (2.1).

The setting assumes existence of a merged-root colouring and nonexistence
of **any** closed-`L`-shore colouring inducing

```text
X | Y | {d} | {e}.
```

This is precisely the singleton merged response used from the audited
opposite-response theorem.  Theorem 2.1 correctly starts with an arbitrary
merged-root colouring `c`, so its three conclusions hold simultaneously in
every such fixed colouring, not merely in three separately selected
colourings.

The split source omits the earlier assumption that each of `d,e` has a
neighbour in both `X,Y`.  That assumption is needed upstream to obtain the
opposite-response normal form, but it is not used by this conditional Kempe
theorem once the exact response is assumed.  Its omission does not enlarge
the conclusion beyond what the proof establishes.

## 2. Kempe interchange and internal localization

Fix a boundary-absent colour `beta_i`.  If `d,e` lay in different
`alpha`--`beta_i` components, interchanging those colours on the component
containing `d` would preserve properness.  It changes `d` to `beta_i`, keeps
`e` at `alpha`, and changes no vertex of `X union Y`, whose colours are
`xi,eta`.  The resulting four boundary blocks have four distinct colours
and therefore induce exactly the forbidden split-root partition.  This
contradiction proves the claimed component connection for every `i`.

On the literal boundary, only `d,e` have colour `alpha` and no vertex has
colour `beta_i`.  A shortest `d`--`e` path in the common two-colour
component therefore has no internal boundary vertex.  Since it lies in
`G[L union S]`, every internal vertex lies in `L`.  Properness makes the path
alternate between its two colours, so its first and last internal vertices
have colour `beta_i`; this proves the endpoint-neighbour assertions.

For distinct indices `i,j`, every common vertex of `P_i,P_j` has a colour
in

```text
{alpha,beta_i} intersect {alpha,beta_j} = {alpha}.
```

This proves the exact intersection restriction.  It supplies no internal
disjointness, distinct first-hit, or separator conclusion.

## 3. Split preservation, provenance, and scope

The split retains all proved content of the merged-response portion of the
combined draft: the exact three locks, their common fixed colouring,
internal-shore localization, endpoint saturation, and pairwise intersection
rule.  It deliberately omits the former diagnostic crossing corollary,
whose extra two-piece cover is not supplied on the live merged shore, and it
contains none of the logically independent cycle-completion hypotheses.

The live connected opposite-response interface genuinely reaches this
theorem on its merged closed shore.  The theorem remains only a local
constraint: it does not locate the paths in named minor-model branch sets,
produce a common boundary response, or return an order-seven separation.

The swap mechanism is a specialization of the GREEN-audited general
merged-pair carrier in
[`../archive/hadwiger_two_block_full_shore_state.md`](../archive/hadwiger_two_block_full_shore_state.md).
The promoted result is useful because it records, self-containedly and in
the live notation, the exact three absent colours, simultaneous endpoint
saturation, and intersection rule.  Its proof uses no external theorem.

Subject to the stated trust boundary, the source is GREEN at the pinned
hash.

## Status-only promotion

After this audit, only the source status line was changed to link this
GREEN audit.  The promoted source has SHA-256

```text
2705b68b8452fd8642601ed48f93c84db98e313be46c12c3f4f7ba85cd94cd41
```

No theorem statement, proof, dependency, or trust-boundary text changed.
