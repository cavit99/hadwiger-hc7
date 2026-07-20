# Surjective partition connectivity on a four-chromatic order-eight boundary

**Status:** written computer-assisted theorem; separate internal audit GREEN
in
[`hc7_order8_surjective_partition_connectivity_audit.md`](hc7_order8_surjective_partition_connectivity_audit.md).
This is a finite boundary theorem.  Its host corollary removes the paired
rejection-kernel outcome only when the eight-vertex residual is
four-chromatic; it does not prove `HC_7`.

## 1. The colour-name quotient

Let `H` be a graph of order eight.  Define `Q_5^sur(H)` as follows.
Its vertices are the proper partitions of `V(H)` into five nonempty
independent blocks.  Two partitions are adjacent when one can be obtained
from the other by moving one literal vertex from a nonsingleton block to a
different existing block, with all five resulting blocks still independent
and nonempty.

Equivalently, `Q_5^sur(H)` is the quotient by global permutations of the
five colour names of the graph of proper surjective labelled five-colourings
under one-vertex recolourings which remain surjective.  The quotient matters:
global colour permutations can interchange distinct connected components of
the labelled recolouring graph.

## 2. Finite connectivity theorem

### Theorem 2.1

If

\[
 |V(H)|=8,\qquad \chi(H)\ge4,\qquad K_5\not\preccurlyeq H,
\tag{2.1}
\]

then `Q_5^sur(H)` is nonempty and connected.

### Computer-assisted proof

The deterministic verifier enumerates all `12,346` unlabelled simple
graphs of order eight with `geng -q 8`.  It tests three-colourability by
exact backtracking.  For every graph which is not three-colourable it
enumerates all `S(8,5)=1,050` canonical five-block partitions, retains the
proper ones, and forms exactly the adjacency relation in Section 1.

There are `6,322` graphs which are not three-colourable.  For `236` of
them the partition graph does not have exactly one connected component;
this count includes `89` graphs for which it is empty.  The verifier tests
each of those `236` graphs for a `K_5` minor by enumerating every choice of
five nonempty, disjoint, connected branch sets, with unused vertices
allowed.  Every one contains a `K_5` minor.  Hence no graph satisfying
(2.1) is among the `236`, proving the theorem.

The positive control `G?aN~w` is not three-colourable and its partition
graph has components of orders `27,37`; the verifier confirms that it has
a `K_5` minor.  The low-chromatic sharpness control `K_{2,6}` (graph6
`G??F~w`) has partition-graph components of orders `65,90`.  Thus the
chromatic hypothesis cannot simply be deleted.

Run

```sh
PYTHONPATH=active/runtime/deps python3 results/hc7_order8_surjective_partition_connectivity_verify.py
```

with `geng` from nauty on `PATH`.  The final line is

```text
PASS order8_K5_minor_free_chromatic_at_least_four_partition_graph_connected
```

## 3. Opposite invariant languages meet in one move

### Theorem 3.1

Let `H` satisfy (2.1), and let `E_A,E_D` be nonempty, disjoint sets of
proper labelled five-colourings of `H`.  Assume:

1. each set is invariant under every permutation of the five colour names;
2. every surjective proper five-colouring belongs to exactly one of
   `E_A,E_D`.

Then some colouring in `E_A` and some colouring in `E_D` differ at exactly
one literal vertex.

#### Proof

Suppose no such pair exists.  Choose `c_A in E_A`.  Since `H` is not
three-colourable, `c_A` uses either four or five colours.  If it uses four,
one of its four colour classes contains at least two vertices.  Recolour one
vertex of that class with the unused fifth colour.  The move is proper, the
old class remains nonempty, and the resulting colouring `f_A` is
surjective.  It cannot belong to `E_D`, since then `c_A f_A` would be the
forbidden one-edge pair.  Thus `f_A in E_A`.  If `c_A` was already
surjective, put `f_A=c_A`.  The same argument gives a surjective
`f_D in E_D`.

By colour-permutation invariance, ownership of a surjective colouring
depends only on its equality partition.  The two partitions induced by
`f_A,f_D` therefore have opposite ownership.  Theorem 2.1 gives a path
between them in `Q_5^sur(H)`.  Somewhere on that path two adjacent
partitions have opposite ownership.  Label their five blocks consistently
across the one moved vertex.  This lifts the quotient edge to proper
surjective labelled five-colourings differing at that one vertex.  Their
membership is unchanged by the chosen colour names, contradicting the
supposition.  \(\square\)

### Remark 3.2 (the local two-step pattern is real but not shortest)

The conclusion is global over the extension languages; it does not say
that every displayed two-step path can be commuted locally.  For example,
let `H` be the odd wheel with rim `0,...,6` in cyclic order and hub `7`.
The three proper five-colourings

```text
c0 = (4,1,0,1,0,1,2,3)
c1 = (0,1,0,1,0,1,2,3)
c2 = (0,4,0,1,0,1,2,3)
```

form a full--four--full two-step path.  The two operated vertices `0,1`
are adjacent, so the two insertions of the missing colour `4` cannot be
commuted.  Theorem 3.1 says instead that, if `c0,c2` were assigned to
opposite invariant full-trace owners, connectedness of the whole
partition quotient would expose a different ownership-changing edge.
Thus the local adjacent-hole pattern may exist, but cannot be globally
shortest between the live shore languages.

## 4. Order-nine host corollary and trust boundary

Let an order-nine boundary be written as the disjoint union of an exact
root class `{d}` and an eight-vertex residual `H`.  In the two connected,
boundary-full, anticomplete-shore setting, the two shore-extension
languages are invariant under permutations of the five non-root colours.
In the one-sided maximum-palette alternative, every surjective residual
trace extends through exactly one shore.  If `H` is four-chromatic and
`K_5`-minor-free, Theorem 3.1 therefore gives oppositely extendable traces
which differ at one literal boundary vertex.

Consequently the shortest-path branch has length one: the paired
four-colour rejection-kernel outcome cannot occur in this four-chromatic
residual.  The audited one-transition theorem then supplies the corresponding
shore-internal bichromatic obstruction paths.  In a seven-connected host,
the component of either open shore supporting such a path has its full
neighbourhood contained in the order-nine boundary, so its boundary has
order seven, eight or nine; order nine means that component is adjacent to
every literal boundary vertex.

This does **not** align the remote path ends with five inherited
minor-model branch sets.  It does not make an order-seven separator carry a
common boundary colouring, split a boundary-full shore component, construct
a `K_7`-minor model, or close the three-colourable residual.  Existing
quotient barriers show that bichromatic paths and even stronger ordered
path data need not repair a labelled near-clique model without the remaining
host-level contraction-critical geometry.

## 5. Dependencies

- exact `K_5` branch-set minor detection and nauty enumeration, implemented
  in the adjacent verifier;
- the [maximum boundary-palette alternative](../results/hc7_order9_maximum_boundary_palette.md)
  for full-trace ownership in the host application;
- the host-level one-transition consequence of the
  [four-or-five-colour reconfiguration theorem](../results/hc7_order8_full_five_colour_reconfiguration.md)
  and its [incidence-cycle composition law](../results/hc7_two_shore_kempe_incidence_cycle.md).
