# Audit of the forced-path detour exchange

**Verdict:** GREEN.

**Audited source:**
`results/hc7_order8_forced_path_detour_exchange.md`

**Audited SHA-256:**
`40879088c80dfb23adc67d15be8fa95d17a0388bc5defc0820379c9b09962021`

**Promoted source SHA-256:**
`f169d0a91648d2a12073fb225e0f98f6398051839cd37b951c5aa53c2deebfa6`

The promoted revision changes only the status line and adds this audit link;
the mathematical content, dependencies, and trust boundary audited below
are unchanged.

**Audit type:** independent internal mathematical audit.  This is not
external peer review and does not prove `HC_7`.

## Detour and disjointness

The forced root path has distinct internal endpoints `v_0,v_k`, since they
lie in the disjoint lobes `L_e,L_d`.  For `i<j` with `j>=i+2`, the open
segment `K=D[v_{i+1},v_{j-1}]` is nonempty and connected.

If the internal vertices of a `v_i`--`v_j` path `W` avoid all of `D`, then

```text
D[v_0,v_i] union W union D[v_j,v_k]
```

is a simple `v_0`--`v_k` path.  Neither endpoint of `W` belongs to `K`, and
its internal vertices avoid `D`, so this rerouted path is vertex-disjoint
from `K`.  It retains the literal `d` contact at `v_0` and the literal `e`
contact at `v_k`.

## Boundary-response contraction and gluing

Take the rerouted root path, `K`, and one of `Q_0,Q_1`.  They are pairwise
disjoint connected subgraphs.  The first contacts `d,e`; the second meets
every literal portal set indexed by the selected class `B`; and the full
component contacts every vertex of the other class.  The rerouted root path
is nontrivial and can be split at any path edge into adjacent connected
pieces retaining the two root contacts.

These are exactly the hypotheses of the audited reserved-path
boundary-response theorem.  Repeating the construction with `Q_0` and
`Q_1` in opposite roles gives both response types on each individual closed
component-side.  In particular, the split response can be aligned with the
selected split-response colouring on the closed `C`-side.  Because the
three components of `G-S` are pairwise anticomplete, the aligned colourings
glue to a proper six-colouring of `G`.

If an entire component of `G[C]-V(D)` meets the selected portal class, it
is connected and disjoint from the original root path; taking it as `K`
gives the same argument without rerouting.

## Standard `D`-bridges and Corollary 2.2

Under the standard definition, the `D`-bridges consist of:

1. each component of `G[C]-V(D)` together with its incident edges to `D`;
   and
2. every chord of `D` as a trivial bridge.

Corollary 2.2 explicitly states the nontrivial component-bridge case.  A
component bridge with attachments `v_i,v_j` contains the required detour
path through its interior; its connected interior triggers the off-path
test, while its open span triggers the segment test.  A chord bridge is not
silently lost: it is covered directly by Lemma 2.1 by taking `W` to be the
chord (whose interior is empty).  Thus the positive exchange is valid for
both standard bridge types, although the corollary's displayed `A` notation
is confined to nontrivial component bridges.

## Whole-packing consequences

The source correctly refuses to infer a web or separator from failure of
the individual bridge tests.  For a smaller bipartition class `B`, its order
is at most three.  The cited unbounded reductions have the stated scopes:

- order one gives a six-colouring, an order-seven separation, or a strict
  order-eight descent;
- order two gives a six-colouring, an order-seven separation, or an
  attachment-free four-terminal web; and
- order three gives a three-portal packing, an order-seven separation, a
  component of order at most six, or a connected lobe behind at most five
  internal vertices.  Excluding the small-boundary restart leaves the
  stated positive-excess lobe.

The packing outcome in the last item closes by the same reserved-path
theorem in the present opposite-response setting.

## Trust boundary

The lemma preserves literal boundary labels: contact with a class means an
actual neighbour of every named boundary vertex.  It does not identify a
palette colour with a label.  It also does not claim that one bridge must
witness every positive packing, or that failure of the whole three-portal
packing is already a colour-compatible separator.  These limitations are
accurately stated.

Within this scope, no gap was found.
