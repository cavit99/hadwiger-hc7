# Internal audit of the asymmetric order-eight shore split

**Audit status:** GREEN.

**Audit date:** 2026-07-16

**Audited file:** `hc7_star_order_eight_asymmetric_shore_split.md`

**Audited SHA-256:**
`0baaf36d9d3064eaa20e4f142c1aa69742758ba24774dc05e0f5adbd0e22adfb`

The mathematical content is identical to the GREEN revision with hash
`421b71fb4eea0b569411d455c27f93e98c74a06616c5d9ee93bb1c0056c06ff8`;
the only subsequent changes were the standard-language title, filename, and
status metadata linking this audit.

This is a separate internal audit, not external peer review.  It supersedes
the provisional audit of the earlier, stronger-hypothesis draft.

## Verdict

Theorem 1 and Corollary 2 are correct under their stated hypotheses.  The
sharper theorem uses only the asymmetric contact sets specified for `P`
and `Q`, the boundary incidences of `e,f`, and fullness of the opposite
shore.  All seven branch sets are disjoint and connected, and all 21
required branch-set adjacencies have literal witnesses.

The result is an exact order-eight specialization of packet-lifting
mechanisms already present in the repository, but the asymmetric
five-contact/three-contact split and its seven displayed bags are not
duplicated verbatim by an existing result located in the repository.

## Branch-set audit

Write

\[
 X=P\cup\{x\},\qquad Y=Q\cup V(e),\qquad Z=B,
 \qquad F=V(f),\qquad R=\{r_1,r_2,r_3\}.
\]

The seven bags are `X,Y,Z,F,{r_1},{r_2},{r_3}`.

They are pairwise disjoint because `P,Q` are disjoint subsets of `A`,
`A` and `B` are disjoint from the literal boundary `S`, and the displayed
parts of `S` are disjoint.  The bags `P,Q,B` are connected.  A `P-x` edge
connects `X`; a `Q-e` edge connects `Q` to the connected edge `e` and
hence connects `Y`.  The remaining bags are an edge or singletons.

The 21 pairwise adjacencies are:

| Pair class | Number | Literal witness |
|---|---:|---|
| `X-Y` | 1 | a `Q-x` edge |
| `X-Z` | 1 | a `B-x` edge |
| `X-F` | 1 | a `P-f` edge |
| `X-{r_i}` | 3 | a `P-r_i` edge for each `i` |
| `Y-Z` | 1 | a `B-e` edge |
| `Y-F` | 1 | a `Q-f` edge |
| `Y-{r_i}` | 3 | collective adjacency of `e` to each `r_i` |
| `Z-F` | 1 | a `B-f` edge |
| `Z-{r_i}` | 3 | a `B-r_i` edge for each `i` |
| `F-{r_i}` | 3 | collective adjacency of `f` to each `r_i` |
| `{r_i}-{r_j}` | 3 | the clique edges of `R` |

The counts sum to 21.  No edge between `P` and `Q`, or between the two
open shores, is assumed or used.  The proof correctly uses `V(e)` rather
than contacts from `Q` to obtain all three `Y-R` adjacencies.  Fullness of
`B` at the two literal endpoints of `e` supplies `Y-Z` despite the
anticompleteness of `A` and `B`.

## Corollary audit

Under the cited exact order-eight hypotheses, the two components of
`G-S` are anticomplete connected open shores and each is adjacent to every
literal boundary vertex.  If one shore contained two disjoint boundary-full
connected subgraphs, either assignment to `P,Q` satisfies the weaker
asymmetric hypotheses of Theorem 1.  Taking the other component as `B`
would therefore produce a `K_7` minor.  Thus each packing number is at most
one.  Each whole component is itself boundary-full and connected, so each
packing number is exactly one.

## Duplication and scope

The closest existing results are:

1. `results/hc7_exact_seven_packet_packing.md`, especially its
   packet-plus-clique lift, which controls a literal boundary of order
   seven.  It does not directly imply this order-eight construction,
   because here the boundary has eight vertices and the `K_7` model uses
   the special triangle/two-edge/singleton decomposition.
2. `archive/hadwiger_reserve_zero_row_capacity_state_exchange.md`,
   Theorem 2.1, where two disjoint connected subgraphs meeting five fixed
   branch-set rows complete a fixed `K_5` frame.  It uses the same general
   two-carrier mechanism, but its interface and branch bags differ.
3. `results/hc7_exact7_named_model_packet_orientation.md`, Theorem 4.1,
   which combines five pre-existing branch bags with two full packets.
   Again the mechanism overlaps, but it assumes a named five-bag model
   rather than deriving the bags from this exact boundary.

An exact repository search found no earlier occurrence of the displayed
`P union {x}, Q union V(e), B, V(f), R` construction or of its asymmetric
contact hypotheses.  It is therefore best regarded as a correct new
specialization and explicit branch-set construction, not a new general
packet principle.

The theorem proves an asymmetric shore-split exclusion and, as a
corollary, boundary-full packing number one.  It does not produce a bounded
transversal, a removable `e`--`f` path, a small portal separator,
compatible boundary colourings, or a repair of the spanning near-`K_7`
model's missing adjacency.
