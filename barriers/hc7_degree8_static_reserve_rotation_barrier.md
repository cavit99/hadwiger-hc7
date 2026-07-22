# Static reserve rotation need not escape the sparse five-reserve case

**Status:** barrier/counterexample to an intermediate claim; written proof;
separate internal audit: GREEN.  This is not a counterexample to `HC_7`.

## 1. Refuted claim

The following boundary-only continuation of the
[five-reserve rotation](../results/hc7_common_root_five_reserve_kempe_packet.md#corollary-33-maximum-independent-reserve-rotation)
is false.

> Let `H` be an eight-vertex nonsplit, three-degenerate graph with
> `alpha(H)=3` such that `H-Z` has no `K_4` minor for every two-set `Z`.
> If `I` is a maximum independent triple and `H-I` has at most three edges,
> then repeated replacement of `I` by a maximum independent triple inside
> the current five-vertex reserve must eventually produce a reserve with at
> least four edges.

A reserve with at least four edges has at most six nonedges and therefore
enters the proved six-demand rooted-`K_5` conversion.  The claim would make
static reserve rotation a terminating strategy.

## 2. Counterexample

Let

\[
                         H=K_3\mathbin{\dot\cup}K_3
                              \mathbin{\dot\cup}K_2.   \tag{2.1}
\]

Then `alpha(H)=3`, and every maximum independent set contains exactly one
vertex from each of the three components.  For every such triple `I`,

\[
                         H-I=K_2\mathbin{\dot\cup}K_2
                                  \mathbin{\dot\cup}K_1. \tag{2.2}
\]

Thus every five-vertex reserve has exactly two edges and eight nonedges.
It contains maximum independent triples—choose one vertex from each
component again—but every resulting rotation has the same form (2.2).
Even allowing every possible maximum-independent-set rotation never
reaches a reserve with at least four edges.

The compact boundary hypotheses also hold.  The graph is
three-degenerate.  It is nonsplit because it contains an induced `2K_2`.
For every two-set `Z`, each component of `H-Z` has at most three vertices;
no component, and hence no disjoint union of them, has a `K_4` minor.

This proves the counterexample.  \(\square\)

## 3. Exact scope

The example is boundary-only and disconnected.  It is not asserted to be
the neighbourhood of a vertex in a seven-connected, seven-chromatic,
minor-minimal `K_7`-minor-free graph, and it carries no exterior-shore
colouring language.  It refutes only a proof that repeatedly rotates the
maximum independent boundary block while remembering no dynamic shore or
proper-minor response data.

Consequently the live concentrated-reserve argument must use the literal
exclusive paths, the matching-swap responses, or the labelled near-`K_7`
model.  Further static rotation is not a well-founded descent.
