# Independent audit: twin-seam stable-stem barrier

**Status:** GREEN for the exact mechanism barrier stated in
[`hc7_twin_seam_stable_stem_barrier.md`](hc7_twin_seam_stable_stem_barrier.md).
This is not an `HC_7` counterexample and does not falsify the active
terminal-disjunctive twin-seam theorem.

## 1. Audited artifacts

The audit used these exact inputs:

```text
d60e9a6356f6ea9a42ac928cabc1666d4dd9b7b242e8303ecfd1885c808de063  barriers/hc7_twin_seam_stable_stem_barrier.md
827f488fb2e1cfe3f0bc28ba1ae58a7b08a2d564e248cf67353a6eb5c280fd88  active/hc7_twin_seam_stable_stem_probe.py
```

The verifier was run with Python 3.14.3 and NetworkX 3.6.1.  Its output was

```text
GREEN twin_seam_stable_stem
separating_packet_numbers (1, 1, 1, 1)
bypass_packet_numbers (1, 1, 1, 1)
orders 23 100
connectivity 7; matched_carriers_D=0; matched_carriers_E=0
six_colourable=true; explicit_K7_model=true
```

The separating host has 23 vertices and 100 edges.  The bypass host adds
only `q-i2`, and hence has 101 edges.

## 2. Literal regions and separations

The vertex sets in the program are pairwise disjoint and exhaust the host:

\[
 A=Z\mathbin{\dot\cup}D\mathbin{\dot\cup}E,
 \qquad S=I\mathbin{\dot\cup}A_0\mathbin{\dot\cup}B_0,
 \qquad R=\{r_1,r_2\}.
\]

Thus `|A|=14`, `|S|=7`, `|R|=2`, and `|G|=23`.  Direct component and
neighbourhood checks, performed independently of the verifier's packet
helpers, give the following in both variants.

* `G-S` has exactly the components `A` and `R`, each with external
  neighbourhood exactly `S`.
* `G-Omega_D` has exactly the components
  `D` and `B_D=E union B_0 union R`, each with external neighbourhood
  exactly `Omega_D`.
* `G-Omega_E` has exactly the components
  `E` and `B_E=D union A_0 union R`, each with external neighbourhood
  exactly `Omega_E`.

Consequently the old boundary and both twin boundaries are literal actual
seven-separations, not quotient boundaries.  The induced old boundary
`G[S]` is connected and bipartite.  The induced graph `G[A]` is connected
after deletion of any one of its vertices, so it is biconnected.  There is
no `A-R` edge, and `zu` is the unique edge from `A` to `u`.

The original packet vector is also genuinely `(1,2)`: every `S`-full
packet in `A` contains `z`, because `z` is the unique `A`-neighbour of
`u`, while `r1` and `r2` are disjoint singleton `S`-full packets.  This
does **not** assert that `A` is globally minimum over all members of
`mathcal F_12(G)`; that global rank is not part of the barrier.

## 3. Connectivity and packet numbers

NetworkX returns vertex-connectivity seven and minimum degree seven.  This
was independently checked by exhaustive deletion of every vertex set of
order at most six: the remainder is connected in both variants.  Conversely
`p` has degree seven, and deleting `N(p)` isolates `p`, so the connectivity
is exactly seven rather than merely at least seven.

The four residual packet numbers admit a direct proof which does not depend
on subset enumeration:

* every `Omega_D`-full packet in `D` contains `d1`, since `d1` is the only
  `D`-neighbour of `p`;
* every `Omega_D`-full packet in `B_D` contains `e1`, since `e1` is the
  only `B_D`-neighbour of `q`;
* every `Omega_E`-full packet in `E` contains `e1`, since `e1` is the only
  `E`-neighbour of `q`;
* every `Omega_E`-full packet in `B_E` contains `d1`, since `d1` is the
  only `B_E`-neighbour of `p`.

Each whole open shore is connected and full, so each packing number is at
least one.  The compulsory vertices above prevent two disjoint packets.
Therefore the exact vector is `(1,1,1,1)` in both hosts.

Independent exhaustive connected-subset enumeration agrees.  The numbers
of full connected subsets in the four listed shores are respectively

```text
16, 265, 16, 310,
```

and the maximum disjoint packing has order one in every case.

The helper `packet_number` searches only orders three, two and one.  This
is sufficient for the asserted value one: any packing of larger order
contains a packing of order two.  No conclusion in this certificate relies
on distinguishing packet number three from a larger value.

## 4. Colourings, locks and response bundle

An independent edge-conflict check gives this exact table in both variants:

| displayed colouring | monochromatic host edges |
|---|---|
| `PHI` | `zu` only |
| selected `G/f` response | `qd` only |
| equal/equal colouring | `zu` and `qd` only |
| proper/proper colouring | none |

Thus `PHI` expands a colouring of `G/e`, the selected response expands a
colouring of `G/f`, the equal/equal colouring descends through both named
contractions, and the proper/proper colouring is a literal six-colouring
of the whole graph.

The `PHI` boundary partitions are

```text
Omega_D: {a1,i1,q} | {a2,i2,i3,p}
Omega_E: {b,i2,i3,p} | {i1,q,u}.
```

For the separating response they become

```text
Omega_D: {a1,i1,p} | {a2,i2,i3,q}
Omega_E: {b,i2,i3,q} | {i1,p,u},
```

and for the bypass response they become

```text
Omega_D: {a1,i2,i3} | {a2} | {i1,p} | {q}
Omega_E: {b} | {i1,p} | {i2,i3} | {q} | {u}.
```

Hence both named responses disagree with `PHI` on both literal twin
boundaries, exactly as claimed.  No stronger state-alignment assertion is
being inferred.

In the separating host, the `0-1` graph of `G-e` under `PHI` contains
`z,u` in one component and contains `f=qd`.  Deleting `f` splits that
component into

```text
{p,q,z}
{a1,a2,b,d,i1,i2,i3,u}.
```

Swapping precisely the first component gives the displayed separating
response.  In that response the path

```text
d-a1-b-u-z-p-q
```

is a literal alternating `1-0` path through `e` and avoiding `f`.
For `j=2,3,4,5`, the four paths `d-xj-q` are literal alternating
`1-j` paths, avoid both named edges, and have mutually disjoint internal
vertices.  This is the full five-rung separating response bundle.

In the bypass host, deletion of `f` leaves the literal `PHI`-bichromatic
path

```text
z-p-q-i2-u
```

inside `G-{e,f}`.  Its colours are `0,1,0,1,0`.  The displayed `G/f`
response has `c_f(z)=PHI(z)=0` and `c_f(u)=1`, so this is the exact
response-matched `0-1` lock selected by that response.

## 5. Failure of sharp matched carriers

For a `D`-carrier contained in `D union {a_i}`, neither `a1` nor `a2` is
adjacent to a gate.  Meeting `p` therefore forces the carrier to contain
the unique `D`-portal `d1`.  Two carriers matched to the two distinct
members of `A_0` consequently cannot be disjoint.

Symmetrically, neither member of `B_0` is adjacent to a gate, and meeting
`q` forces every `E union {b_i}` carrier to contain the unique `E`-portal
`e1`.  Hence no sharp matched pair exists in `E`.  Exhaustive enumeration
of every connected candidate in the verifier agrees with this direct
compulsory-vertex argument.

The added edge `q-i2` lies entirely between the gate and the common old
boundary.  It changes neither compulsory lobe portal and therefore does
not affect this conclusion or any residual packet number.

## 6. Literal `K_7` certificate

The seven displayed bags are nonempty and pairwise disjoint.  Connected
spanning edge sets inside them are:

```text
B1: d-i1, d-x4, i1-r1
B2: singleton u
B3: e1-i2
B4: singleton b
B5: d1-i3, i3-y2, y2-y5
B6: a1-r2, a1-x3
B7: a2-x2, p-q, p-y3, q-x2, q-x5, y3-y4, y3-z.
```

One literal edge witnessing each of the 21 interbag adjacencies is:

```text
B1-B2 r1-u       B1-B3 i1-e1      B2-B3 u-i2
B1-B4 r1-b       B2-B4 u-b        B3-B4 e1-b
B1-B5 i1-y2      B2-B5 u-i3       B3-B5 i2-y2
B4-B5 b-y2       B1-B6 d-a1       B2-B6 u-r2
B3-B6 i2-x3      B4-B6 b-a1       B5-B6 d1-a1
B1-B7 i1-y3      B2-B7 u-z        B3-B7 e1-y3
B4-B7 b-y3       B5-B7 y2-y3      B6-B7 a1-x2.
```

Therefore these are literal `K_7` branch sets already in the separating
host, and hence also in its one-edge extension.

## 7. Verifier micro-audit

The executable was read line by line.  Its helper contracts are as follows.

* `build` has one boolean input and deterministically creates the fixed
  simple graph.  The only variant effect is adding `q-i2`; all region,
  boundary and named-edge constants are immutable module data.
* `proper_off` checks every host edge and permits equality only on the
  explicitly omitted edge set.  Both omitted named edges are independently
  verified to exist.  Every displayed colouring has exactly the full
  23-vertex key set.
* `exact_partition` groups literal boundary vertices by colour and sorts
  only for canonical comparison; it neither merges labels nor reasons
  modulo a boundary automorphism.
* `external_neighbourhood` computes the literal open neighbourhood of a
  supplied vertex set.  It is used only on `D,E`; independent component
  checks above verify the stronger actual-separation statements.
* `connected_full_packets` enumerates every nonempty subset of the finite
  shore, tests induced connectivity, then tests one literal contact for
  every boundary vertex.  `packet_number` tests pairwise vertex-disjointness.
* `matched_gate_carriers` separately enumerates every connected set in
  `D union {a_i}` or `E union {b_i}` containing its named seed, then tests
  literal adjacency to both gates.  Combining candidates requires distinct
  seeds and disjoint vertex sets, exactly matching the falsified extraction
  claim.
* `check_clique_model` checks nonemptiness, pairwise disjointness, induced
  connectivity of every bag and a literal host edge for every bag pair.
* `verify` checks the region invariants before the colouring assertions,
  reconstructs the exact selected lock in `G-e`, checks the appropriate
  separating or bypass branch, then checks packet numbers, carrier failure
  and the terminal model.  It makes no mutation shared between the two
  calls to `verify`.

The main implementation risks were a wrong closed-shore complement, a
nonliteral boundary identification, a colouring which silently omitted a
vertex, a truncated packet search, and a quotient rather than literal
minor certificate.  The explicit checks above eliminate each risk for
these two fixed hosts.

## 8. Exact safe conclusion

The certificate refutes only this geometry-only implication:

> twin exact-seven boundaries, residual vector `(1,1)/(1,1)`, seven
> connectivity, crossed named responses, an equal/equal state, and either
> the separating five-rung response bundle or a response-matched bypass
> force a sharp matched lobe-carrier pair.

It does not satisfy the terminal-free kernel.  Both hosts are visibly
six-colourable and contain the literal `K_7` model above.  They therefore
fail non-six-colourability, strong seven-contraction-criticality and
`K_7`-minor-freeness.  Nor does the audit assert the global
`mathcal F_12(G)` shore-minimality used to rank a strict handoff.

Accordingly this is **not** a counterexample to the active twin-seam
double-lock exchange theorem.  It proves that the response bundle or
bypass alone cannot perform literal gate-stem shortening.  Any valid
decoder must spend one of the hypotheses absent here: the forbidden
proper/proper state, the terminal `K_7`/fixed-pair alternative, or a valid
strictly ranked state-carrying handoff.
