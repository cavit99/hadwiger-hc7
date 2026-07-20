# Verification-gate report and research reassessment

**Status:** point-in-time internal verification report, 20 July 2026.  This
is not a status authority, a new theorem or external peer review.  Current
status remains governed by [`RESEARCH_LEDGER.md`](../RESEARCH_LEDGER.md),
and the reconstructed case graph is
[`hc7_live_case_dag.md`](hc7_live_case_dag.md).

## 1. Purpose

This gate asked three questions before another proof campaign:

1. Is there an exhaustive live case graph from a hypothetical
   counterexample to the stated open theorem?
2. Do the load-bearing promoted results survive a fresh audit at their
   present revisions?
3. Does the resulting programme justify further work on a host-level
   response-coupling theorem, and does it support a separate partial-results
   manuscript?

## 2. Exact revisions cold-audited

The following source revisions were checked without changing their theorem
statements.

| Result | SHA-256 | Cold verdict |
|---|---|---|
| [Low-degree adjacent-pair alignment](../results/hc7_low_degree_adjacent_pair_alignment.md) | `263611a40dc7829788967250e031a3f3170e1c7a6c8c9a3fbfbb358231b1f9ca` | GREEN |
| [Bounded-interface exact-block Kempe reduction](../results/hc7_bounded_interface_exact_block_kempe_reduction.md) | `2c0db7cf9b646597f73a2b5c6fa5e4199f98ced44800b3a60f521cbbdb7372a9` | GREEN, conditional on its promoted inputs |
| [Generic exact-seven response restart](../results/hc7_generic_exact7_response_restart.md) | `e689c96686a936c27e58c2cba22d699c62ad649092eebfcdfc9c5db95a8e7b5a` | GREEN, conditional on its promoted inputs |
| [Minimum positive-excess separator normal form](../results/hc7_minimum_positive_separator_normal_form.md) | `4b6a4d7a434cb255229fcf4fe12e1393d7b0dadad27985e8528b0535d4cf64ba` | GREEN, conditional on existence of the stated eligible set |
| [Cycle-boundary completion](../results/hc7_cycle_boundary_completion.md) | `f87ddcf7e4bd33b0fc107033033d9a8ebb2f6e32533b1b9c4538c0bf4bd137db` | GREEN |
| [Large-boundary singleton-response descent](../results/hc7_large_boundary_singleton_response_descent.md) | `bce97974e2d3d543aaf9ae2f07ff13b61684ddc9cb6bdf08bacdb750c2be2c97` | GREEN, with the fresh-response qualification below |

The existing adjacent audits already pin these revisions and accurately
state their trust boundaries.  Because the cold audit found no mathematical
change or new gap in the source theorems, their audit files were not rewritten
merely to record a second internal reading.

The finite degree-nine completion was rerun over all `4,608` recorded
instances with matching catalogue and witness hashes.  The order-eight/nine
boundary-absorption census was also rerun: there were no order-eight
survivors and the sole order-nine survivor was `K_2\vee C_7`.  The relevant
enumeration and minor-checking code was inspected for incomplete generation,
unsound caching and missing minor operations; none was found.

## 3. External-input check

The exact Mader bound used throughout is correctly sourced to W. Mader,
*Homomorphiesätze für Graphen*, Math. Ann. **178** (1968), 154--168,
[EuDML record and scan](https://eudml.org/doc/161741).  Its `p=7` case is

\[
 K_7\not\preccurlyeq G\quad\Longrightarrow\quad
 |E(G)|\le5|V(G)|-15.
\]

The equality classification quoted from L. K. Jørgensen,
*Extremal graphs for contractions to K7*, Ars Combin. **25C** (1988),
133--148, was checked against its
[publisher record](https://combinatorialpress.com/ars/vol25c/) and an
independent [modern extremal-minor treatment](https://users.monash.edu/~davidwo/files/Hendrey-PhD.pdf)
citing the original theorem.
It gives the five-clique sums of edge-maximal two-apex graphs together with
`K_{2,2,2,3}`.  The repository uses it correctly:

- `K_{2,2,2,3}` has connectivity six;
- a nontrivial five-clique sum has a separator of order five; and
- one two-apex summand is six-colourable by the Four Colour Theorem plus
  two fresh colours.

Thus equality is impossible in a seven-connected seven-chromatic graph,
and the strengthened bound `|E(G)|<=5|V(G)|-16` is valid.  For
publication-level source hygiene, a library scan of Jørgensen's original
article and its exact theorem number should still be obtained.  That is a
citation-verification task, not an identified proof gap.

Martinsson--Steiner Lemma 3.1 and the Las Vergnas--Meyniel Kempe-equivalence
theorem were also compared with their primary statements.  Their hypotheses
are used exactly in the cycle-boundary and exact-block arguments.

One proposed documentation correction was rejected after this comparison.
The opening positive-excess paragraph of the ledger correctly refers to a
Kempe-change graph: it invokes the unbounded exact-block Kempe theorem.
The later order-eight theorem genuinely uses a single-vertex recolouring
graph and is described separately.  Conflating the two would introduce,
rather than repair, a scope error.

## 4. What the audited chain does and does not prove

The audited entry and exact-block reduction yield one exhaustive coarse
chain for degrees seven, eight and nine:

```text
hypothetical counterexample
  -> bounded full separation of order 7, 8 or 9
  -> operation-specific pole-free paths
  -> open pole-free bridge composition theorem.
```

The last theorem has terminal `K_7` and colour-gluing outcomes and a proposed
strict recursive outcome measured by the literal component order.  Relative
to the entry reduction it is sufficient for `HC_7`; it therefore packages
essentially the entire remaining global difficulty.

The fine exact-seven chain has one proved strict arrow: a proper
list-critical core whose full neighbourhood again has order seven returns a
strictly smaller operated shore.  It is not globally well-founded.  The
remaining nonterminal arrows are:

- a singleton shore with a surviving nonbipartite two-connected exterior;
- a minimum positive-excess boundary returning two or three boundary-full
  components;
- a fresh exact-seven response from that boundary, with no proved decrease
  from the previous shore; and
- a shore-filling positive-excess list-critical core.

The developed order-eight and order-nine analyses are conditional
descendants of this positive-excess branch.  There is no proved reduction
from every original degree-eight or degree-nine entry to those detailed
normal forms.

The large-boundary theorem likewise needs its explicit qualification.  A
proper list-critical kernel gives a smaller connected response side, but
its boundary order, trace and inherited branch-set labels are uncontrolled.
It is genuine compression, not an allowed recursive arrow in the labelled
programme until a pullback theorem restores the required data.

## 5. Reassessment

### Full-proof campaign: conditional GO

The promoted chain is mathematically coherent enough to justify one further
focused unbounded campaign.  It is not evidence that a complete proof is
near, and it does not justify more labelled residue enumeration.

The next theorem should be narrower than the global bridge-composition
statement and should test the missing mechanism directly:

> **Minimum-positive-excess response-coupling target.**  In a minimum
> generic exact-seven response interface, suppose a proper two-root
> list-critical core has a full boundary of order eight or nine and deleting
> that boundary leaves exactly two or three boundary-full components with
> the audited operation-specific exclusive responses.  Then construct an
> explicit `K_7`-minor model, produce an actual order-seven separation on
> which one complete equality partition extends through both closed shores,
> or return a strictly smaller connected generic exact-seven response shore.

The first milestone should be the two-component order-eight case.  It is an
unbounded host-level theorem, is strictly weaker than `HC_7`, and would turn
the positive-excess normal form into a genuine induction.  Even closing that
case would materially improve the programme's prospects; another static
first-hit or portal classification would not.

The campaign should stop or pivot if it produces only fresh response
interfaces without a proved rank, or if a full-host counterexample defeats
the two-component order-eight statement.  Useful outputs must explicitly do
one of: construct the minor, synchronize a complete boundary partition, or
decrease the literal connected-shore order while preserving the generic
response data.

### Partial-results manuscript: GO after one source-and-novelty gate

There is enough audited unbounded mathematics to prepare a separate
partial-results manuscript even if the full-proof campaign fails.  The
strongest coherent package is the low-degree bounded-interface entry,
cycle-boundary completion, exact-seven full-subgraph packing, and the
large-boundary density descent.  A manuscript must not present the detailed
order-eight/order-nine programme as exhaustive and must not claim novelty
until a conventional literature review and independent human proof audit
are complete.

### No-go directions

- Do not present the global pole-free bridge theorem as a near-final local
  lemma; with the entry reduction it is `HC_7`-strength.
- Do not extend raw order-eight/order-nine case catalogues without an
  audited entry arrow and strict host-level rank.
- Do not identify palette colours with inherited branch-set labels without
  literal first-hit data.
- Do not count a smaller kernel, quotient or auxiliary path as induction
  unless the returned instance preserves the declared response data.

## 6. Bottom line

The verification gate is passed in the limited sense that the principal
promoted theorems remain sound and the programme now has an honest map of
its exhaustive and nonexhaustive parts.  It fails any claim that the current
detailed reductions already form a convergent proof.  Further investment is
justified only as a focused attempt to discover the host-level
response-coupling theorem above, alongside preservation of the standalone
unbounded results for independent review and eventual publication.
