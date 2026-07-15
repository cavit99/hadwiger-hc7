# Audit: six-terminal kernel closure of order-six overlap three

## Verdict

**GREEN** for
[`../active/hc7_overlap_three_six_terminal_kernel_verify.py`](../active/hc7_overlap_three_six_terminal_kernel_verify.py).
The terminal-kernel reduction, finite quantifiers, exact carrier census,
minor detector, and branch-set lift are correct.  The verifier closes all
`140` noncommon state orbits (weight `7,878`) of the normalized
arm-order-six, overlap-three cell.  This includes the `110` orbits that
survived the earlier direct decomposition test and the `30` orbits that
already had a direct quotient `K_7` certificate.

The optional generic-detector crosscheck and the separate structural
generator both corroborate the main certificate; see Section 7.

## 1. Connectivity and terminal reduction

Put `H=G-I`, where `|I|=3`.  Seven-connectivity of `G` makes `H`
four-connected.  For any reserved terminal `r`, the graph `H-r` is
three-connected.

Apply the audited terminal-legal contraction theorem in `H-r` to the other
six terminal labels.  It returns a spanning, three-connected,
terminal-irreducible rooted minor `M` with

```text
6 <= |V(M)| <= 6+floor(6/4)=7.
```

The process uses contractions only.  Thus the six protected terminals lie
in six distinct rooted bags, every vertex of `H-r` belongs to exactly one
kernel bag, and the reserved terminal is outside every bag.

## 2. Order-six kernels

When `|M|=6`, its vertex set is exactly the six roots and its bag-adjacency
graph is an arbitrary labelled three-connected graph.  Edge monotonicity
allows deletion down to an edge-minimal spanning three-connected graph.

The verifier independently enumerates all `2^15` labelled six-vertex
graphs.  It finds exactly

```text
142 edge-minimal three-connected carriers:
 70 with 9 edges,
 72 with 10 edges.
```

Testing every one is therefore exhaustive for the order-six branch.

## 3. Order-seven kernels

Let `x` be the sole nonterminal kernel vertex.  Every edge incident with
`x` is terminal-legal, so irreducibility says that no such edge is
contractible.  Wu's theorem consequently supplies at least four neighbours
of `x` that have degree three.  The verifier uses this only as a necessary
fast filter and then checks directly that:

* the seven-vertex graph is three-connected; and
* contracting `x` into any adjacent terminal does not leave a
  three-connected graph.

It enumerates every labelled graph satisfying those exact conditions and
obtains `780` kernels.  An independent `geng`/NetworkX census gives the
same four unlabelled rooted types:

1. a terminal `C_6` with universal extra vertex;
2. a terminal `C_6` with one opposite chord, where the extra vertex sees
   the other four rim vertices and zero, one, or both chord ends.

Their labelled multiplicities sum to

```text
60 + 180 + 360 + 180 = 780.
```

For composition it is legitimate to contract the extra bag into any
adjacent terminal bag, even though that contraction need not preserve
three-connectivity.  The union is connected through their kernel edge, the
chosen root remains in the merged bag, and all other rooted bags remain
disjoint.  For each of the `780` possible kernels the verifier requires at
least one adjacent owner that produces `K_7`.  This is exactly the safe
quantifier.

## 4. Finite quantifiers

For a fixed noncommon boundary state the code proves

```text
there exists a reserved r such that
  every order-six kernel closes, and
  for every order-seven kernel
    some adjacent owner of the extra bag closes.
```

This matches the graph argument.  The reserved label may be selected from
the known boundary state before applying the terminal-kernel theorem; the
resulting kernel and the useful owner are then selected existentially from
the actual `H-r` contraction.

The replay reports

```text
closed orbits = 140 of 140,
closed weight = 7878 of 7878.
```

The weighted distribution of the number of valid reserved terminals is

```text
one:153, two:180, three:513, four:513,
five:3798, six:1416, seven:1305.
```

Thus the finite certificate does not depend on the earlier split between
directly closed and formerly live orbits.

## 5. Exact `K_7` detector

A `K_7` model on ten quotient vertices has at least four singleton branch
sets, because seven nonempty bags use at most ten vertices.  The verifier
therefore exhausts exactly four cases:

* seven singleton bags;
* six singleton bags and one connected bag;
* five singleton bags and two connected bags; or
* four singleton bags and three two-vertex bags using all remaining six
  vertices.

In every case it checks the singleton clique, internal connectivity, all
contacts with the singleton core, and all contacts among nonsingleton bags.
Unused quotient vertices are allowed in the first three cases.  Hence the
detector is complete, not a heuristic.

## 6. Literal lift

The finite quotient contains the three singleton vertices of `I`, the
reserved singleton `r`, and the six rooted kernel bags after the optional
extra-bag contraction.  Original edges are used only through their literal
terminal endpoints.  Kernel edges are actual adjacencies between rooted
bags and are added only after the nine support relations have been joined.

Replacing every terminal quotient vertex by its rooted preimage bag
preserves connectivity, disjointness and every quotient adjacency.  No
omitted-terminal absorption occurs: after reserving `r`, all other six
exterior terminals are protected roots.

## 7. Independent corroboration

[`../active/hc7_six_terminal_kernel_composition_probe.py`](../active/hc7_six_terminal_kernel_composition_probe.py)
now generates all three opposite pairs of every labelled terminal cycle
and returns the correct `780` order-seven masks.  This independently
matches the direct `2^21` enumeration used by the main verifier.

Running the main verifier with `--crosscheck` also compares its specialized
ten-object `K_7` detector with the generic branch-partition search on
`8,204` deterministic compositions.  All answers agree, with digest

```text
b831df578ec60a78b49328ae7b0a8e9fa806b05b8e0210bd93325b3a692845ca.
```

## 8. Scope

This proves the normalized irredundant arm-order-six, overlap-three cell.
It does not by itself prove `HC_7`; a global invocation must still verify
that the upstream support reduction lands in exactly this cell and must
combine it with the already closed overlap/order alternatives.
