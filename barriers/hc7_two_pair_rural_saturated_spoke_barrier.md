# A saturated-response rural two-pair barrier

**Status:** explicit computer-checked barrier to an intermediate claim.  It
is not a counterexample to `HC_7`: the graph is six-colourable and hence is
not seven-contraction-critical.

The deterministic certificate is
[`hc7_two_pair_rural_saturated_spoke_barrier_verify.py`](hc7_two_pair_rural_saturated_spoke_barrier_verify.py).

## 1. Construction

Start with the nineteen-vertex graph in
[the almost-universal two-apex barrier](hc7_two_pair_rural_almost_universal_apex_barrier.md).
Thus `P` is the five-connected planar triangulated pentagonal tube, `p,q`
are adjacent added vertices, `p` is adjacent to every vertex of `P` except
`u=(1,0)`, and `q` is adjacent to every vertex of `P` except `v=(1,4)`.
The singleton open shore is

\[
                              L=\{x\},\qquad x=(0,0).
\]

Delete the two further edges

\[
                         p(1,1),\qquad q(1,3).           \tag{1.1}
\]

Call the resulting graph `G`.  An exhaustive test of the possible single
additional apex--tube edge deletions identified these two complementary
repairs: either one repairs one of the two missing saturated spoke
responses, while both together repair both and preserve the entire rural
five-subgraph geometry.

## 2. The host-level geometry survives

The checker verifies the following literal assertions.

1. `G` is seven-connected.
2. `G` is `K_7`-minor-free.  Indeed, deleting `p,q` leaves the planar graph
   `P`; at most two branch sets of a proposed `K_7` model can contain those
   two vertices, leaving an impossible `K_5` model in `P`.
3. `T=N_G(x)` has order seven, `G-T` has the singleton component `L` and a
   nonempty connected opposite shore, and both independent pairs

   \[
                 I=\{p,(1,0)\},\qquad J=\{q,(1,4)\}
   \]

   retain the alternating-wheel disk obstruction.  In particular, there
   are no vertex-disjoint `I`- and `J`-connectors through `L`.
4. The five connected, pairwise disjoint, pairwise adjacent subgraphs from
   the original certificate retain the exact traces

   \[
                     I,\quad J,\quad\{s\},\quad\{t\},
                     \quad\varnothing.
   \]
5. No pair among the three omitted boundary labels meets every `K_5`
   subgraph.  The three explicit `K_5` subgraphs from the original
   certificate use none of the edges deleted in (1.1).

Thus this is not merely an abstract response shell: it retains the exact
seven-boundary, the rural two-pair obstruction, the five named opposite-
shore subgraphs, seven-connectivity and global `K_7`-minor exclusion.

## 3. Every incident contraction has a saturated response

For every neighbour `s` of `x`, the certificate gives a proper
six-colouring of

\[
                              G-xs                            \tag{3.1}
\]

in which `x` and `s` have the same colour.  Equivalently, it is a proper
six-colouring of `G/xs` pulled back to the two original endpoints.
Moreover, both `x` and `s` see every one of the five other colours.  Hence
the certificate realizes, simultaneously for all seven spokes, the exact
endpoint-saturation conclusion usually extracted from one selected
proper-minor colouring in a seven-chromatic critical graph.

The colourings are stored literally in the checker.  No colouring solver
is trusted for this assertion: the checker verifies every undeleted edge
and both five-colour neighbourhood sets directly.

## 4. Statement refuted and exact trust boundary

The construction refutes any implication of the form

> the exact rural two-pair/five-subgraph geometry, seven-connectivity,
> `K_7`-minor exclusion, and the existence of a fully endpoint-saturated
> contraction response for every edge from the singleton shore force the
> missing linkage, a `K_7` minor, or a two-vertex transversal chosen from
> the three omitted boundary labels.

The graph remains six-colourable.  A colouring of `G` restricts, after any
spoke deletion, to a colouring in which the two spoke endpoints have
different colours.  Thus the certificate deliberately fails the
**universal nonextension law** of a critical host:

\[
  \text{every six-colouring of }G-xs\text{ gives }x,s
  \text{ the same colour}.                              \tag{4.1}
\]

It also has the coherent global terminal pair `p,q`, and a global
six-colouring supplies a common boundary partition.  It therefore does
not refute the full terminal disjunction sought in the `HC_7` programme.

The sharp methodological conclusion is nevertheless stronger than the
previous barrier: even a separately selected saturated response for
**every** relevant proper contraction is only existential data.  A
positive reserved-cycle or contact-diversification theorem must compare
complete response languages in the common host, spend the fact that no
response extends across its deleted edge, or recognize the common
partition/global terminal.  Choosing one favourable response for each
operation cannot suffice.

## 5. Verification

Run from the repository root:

```bash
PYTHONPATH=active/runtime/deps python3 \
  barriers/hc7_two_pair_rural_saturated_spoke_barrier_verify.py
```

Expected output:

```text
host: 7-connected and K7-minor-free by the two-apex argument
disk: exact seven-boundary and alternating two-pair obstruction
rows: all five named traces and adjacencies remain valid
transversal: no pair among the three omitted labels hits every K5
responses: every spoke has a fully endpoint-saturated 6-colouring
criticality gap: the host itself still has a proper 6-colouring
```
