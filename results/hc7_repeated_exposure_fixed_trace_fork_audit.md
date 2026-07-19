# Independent audit: fixed-trace alternatives for two repeated-exposure edges

**Verdict:** **GREEN.**

**Audited source:**
`results/hc7_repeated_exposure_fixed_trace_fork.md`

**Source SHA-256:**

```text
1df977201ca009336eb1393f2407d16e3258747ba55bd64f2af7be6844cd610e
```

This is a separate internal mathematical audit, not external peer review.
The audit covers Lemma 1.1, Theorem 2.1, Propositions 3.1--3.3,
Corollary 3.4, and the stated repeated-exposure application and trust
boundary.

## 1. Boundary lists and the exhaustive fork

The absence of `A`--`D` edges makes the list assignment exact.  An
`L`-colouring of `G[D]-g` glues to the fixed colouring `c` of
`G[A\cup X]`; conversely, the restriction to `D` of any colouring of
`G-g` agreeing with `c` on `X` uses only the displayed lists.  Thus the
definition of fixed-trace attainment and its whole-host formulation are
equivalent.

Lemma 1.1 is exact.  If two colourings of `X` induce the same equality
partition, the colour used on each block in one colouring may be sent to
the colour used on that block in the other.  This is a bijection between
their used palette colours and extends to a permutation of `[q]`.  Applying
the permutation globally preserves properness and makes the new colouring
agree literally with `c` on `X`.  The argument remains valid when fewer
than `q` colours occur on the boundary.  Thus fixed-trace attainment depends
only on the boundary equality partition, although later model labels do not.

The three cases in Theorem 2.1 are exhaustive and pairwise disjoint.  If a
single deletion is `L`-colourable, so is the common deletion.  Otherwise
the common deletion is either `L`-colourable or not.  If an attained edge
were absent from an induced non-`L`-colourable subgraph of `G[D]`, the
restriction of the colouring of its deletion would colour that subgraph.
The universal containment statement in alternative 1 is therefore valid,
including when both marked edges attain the trace.

## 2. Common equality and simultaneous contraction

In alternative 2, restoring `e` to an `L`-colouring of the common deletion
would colour `G[D]-f` unless the ends of `e` were equal.  Since `f` does not
attain the trace, equality is forced.  The symmetric argument forces
equality on `f`, and it applies to every colouring of the common deletion.

For disjoint marked edges, the equal-coloured endpoint pairs may be
identified independently.  For incident edges `sw,st`, their outer ends
also receive the common colour.  They cannot be adjacent, since that edge
survives in `G-\{e,f\}`.  The only edges internal to the contracted
three-vertex class are therefore the two marked edges, so the colouring
descends to the simultaneous contraction.  No unmentioned nonedge or
disjointness hypothesis is used.

## 3. Common rejection, tight vertices, and endpoint excess

In alternative 3, vertex minimality in the common edge-deletion graph gives
a connected induced non-`L`-colourable subgraph `K`.  Colouring `K-v` and
then attempting to colour `v` proves

\[
                            d_K(v)\ge |L(v)|.
\]

For a block of the subgraph induced by the tight vertices, colour the rest
of `K`.  At most `d_K(v)-d_B(v)` colours are removed from the list at a
vertex `v` of the block, leaving at least `d_B(v)` colours.  The standard
degree-choosability theorem would then colour the block unless it is a
complete graph or an odd cycle.  Hence every block is of one of these two
types and the tight-vertex subgraph is a Gallai forest.  This is exactly the
audited list-critical argument in
`results/hc7_boundary_list_critical_transfer.md`; it remains valid for
empty lists and singleton complete blocks.

Here `K` is induced in `G[D]-\{e,f\}`.  It need not be induced in the
original graph `G[D]`, because one of the two deleted edges could have both
ends in `V(K)`.  The proof and the strict-kernel conclusion use only the
former statement: when `V(K)` is a proper subset of `D`, the same lists and
the same fixed boundary trace are rejected on a strictly smaller connected
subgraph.  Adding the marked edges back on that vertex set can only preserve
noncolourability and connectedness.  The final source states the analogous
ambient-graph distinction explicitly for `K_e` and `K_f`: each is
vertex-induced in its respective edge-deleted host, and its vertex set
induces a possibly stronger noncolourable kernel in `G[D]`.

If the vertex-minimal obstruction spans `D`, deleting edges while retaining
noncolourability gives a spanning edge-minimal subgraph
`F\subseteq G[D]-\{e,f\}`.  The same one-vertex extension argument gives
`d_F(v)\ge |L(v)|`.  Each of the `m(v)` distinct marked edges incident with
`v` belongs to `G[D]` and not to `F`; consequently

\[
              d_{G[D]}(v)\ge d_F(v)+m(v)\ge |L(v)|+m(v).
\]

This also covers the shared endpoint of two incident marked edges, where
`m(v)=2`.

## 4. Paired fixed-trace critical subgraphs

Alternative 2 says that `G[D]-f` is non-`L`-colourable while deleting `e`
from it gives the colourable common deletion.  A vertex-minimal induced
obstruction `K_e` must therefore contain the edge `e`; otherwise it is a
subgraph of the common deletion.  The symmetric construction gives `K_f`,
and edge minimisation gives spanning non-`L`-colourable subgraphs `F_e,F_f`
containing their respective marked edges.

For `g\in\{e,f\}`, the restriction of any common-deletion colouring is an
`L`-colouring of `F_g-g`.  The audited locked-edge theorem therefore applies
in the local properly coloured graph formed by `F_g-g`, `X`, and the
`K_g`--`X` edges.  For every alternate colour, either the marked endpoints
are in one bichromatic component, or their two components are distinct and
both meet `X`.  Shortest first-hit paths in the latter case are disjoint,
have distinct literal boundary endpoints, and have all internal vertices in
`K_g`.  Since `F_g-g` omits both marked edges, every asserted path lies in
the common edge-deletion host.  Proposition 3.1 has the correct local, rather
than whole-host, scope.

If both `K_e` and `K_f` span `D`, the added surplus bound (3.2) is valid.
For an endpoint `v` of `e`, the spanning subgraph
`F_f\subseteq G[D]-e` satisfies `d_{F_f}(v)\ge |L(v)|`; restoring the
distinct incident edge `e` gives

\[
                         d_{G[D]}(v)\ge |L(v)|+1.
\]

The symmetric argument uses `F_e` for an endpoint belonging only to `f`.
At a common endpoint of incident marked edges either inequality suffices.
The claim is only a one-edge surplus in the common-equality branch; it is
not the two-edge `m(v)` surplus proved separately in the shore-filling
common-rejection branch.

## 5. Fixed-trace Kempe orientations for disjoint edges

In Proposition 3.2, switching either endpoint component of an unlocked
pair makes that marked edge proper.  The companion pair must remain equal;
otherwise both deleted edges could be restored and would `q`-colour `G`.
Restoring only the repaired edge therefore gives a colouring of the
opposite one-edge deletion.

If the switched component avoided `X`, that one-edge colouring would retain
the exact fixed trace and contradict nonattainment.  Hence both endpoint
components meet the literal boundary.  The stronger assertion about the
boundary equality partition is also valid.  Two colourings of `X` induce
the same equality partition exactly when a bijection between their used
colour classes maps one restriction to the other; this bijection extends to
a permutation of the full palette.  Applying that global permutation to
the whole one-edge colouring would recover `c|_X`, again contradicting
nonattainment.  The argument is valid even when not all nominal colours are
used on `X`.

The audited common-host allocation theorem applies because the additional
proper-minor hypothesis implies `chi(G)=q+1` and supplies the simultaneous
contraction colouring.  Its same-colour and distinct-colour counts give the
stated three-lock and four-lock conclusions for `q=6`.  Proposition 3.2
does not infer that different palette locks use disjoint paths or reach
different model branch sets.

## 6. Incident edges and the partial boundary footprint

For incident edges `sw,st`, the common-equality colouring meets the input of
the audited incident-edge saturation-or-bypass theorem: the outer vertices
are nonadjacent and the simultaneous contraction is a proper colourable
minor.  In the nonsaturated outcome, the theorem supplies the two stated
bichromatic components, their `w`--`t` path avoiding `s`, and the two
opposite one-edge colourings.  If either switched component avoided `X`, its
one-edge colouring would attain the fixed trace.  The same palette-permutation
argument as above proves that each switch changes the boundary equality
partition, not only its colour names.

Corollary 3.4 follows exactly.  Every switched component meets
`X_i\cup X_j`.  It cannot contain all of that set, because then the switch
would merely transpose the two complete boundary colour classes and leave
the equality partition unchanged.  Finally, an edge of the induced
`i`--`j` subgraph from `Q\cap X` to a boundary vertex of the complementary
set would put that vertex in the same bichromatic component `Q`.  Thus no
such edge exists.

The mathematical revision with hash `77bb53e2...` only clarified that
`K_e,K_f` are vertex-induced in their respective edge-deleted hosts (and
explained what happens after restoring the companion edge), and corrected
the Corollary 3.4 cross-reference to `(3.4)`.  Both changes were editorial
clarifications consistent with the audited proof.  The current source hash
`1df97720...` differs from that GREEN mathematical revision only in its
status line, which now links this audit; no mathematical content changed.

## 7. Application and exact trust boundary

The repeated-exposure interpretation uses the trichotomy only after both
marked edges have been located in the tested shore and one fixed boundary
colouring has been selected.  Alternative 1 preserves a companion model
edge; a proper common-rejection kernel is a strict order decrease with the
same trace; and alternative 2 supplies two oppositely deleted critical
subgraphs plus boundary-reaching response components.  These deductions
are exactly those proved above.

The source correctly stops before the unresolved label-allocation step.  It
does **not** prove that:

* a palette colour or a boundary first hit belongs to a prescribed one of
  the five common model branch sets;
* the local fixed-trace paths form whole-host proper-minor colourings;
* a strict kernel retains the companion edge or all inherited branch-set
  labels;
* a bare order-seven separation has compatible shore colourings; or
* any alternative alone constructs a `K_7`-minor model or proves `HC_7`.

The response-reflection endpoint additionally requires the stated
partition-specific connected-subgraph system; it is not inferred from the
existence of an order-seven separator alone.  No mathematical defect was
found within this trust boundary.
