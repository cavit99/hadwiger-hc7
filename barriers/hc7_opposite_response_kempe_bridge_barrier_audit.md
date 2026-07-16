# Audit: exact-order-eight Kempe-bridge barrier

**Verdict:** GREEN.  The displayed graph has every property asserted in the
barrier statement.  In particular, it is seven-chromatic and exactly
eight-connected; its order-eight separation has two connected shores that
are adjacent to every boundary vertex; the common two-edge deletion has
exactly the three signatures `EE`, `EP`, and `PE`; and the two one-edge
response families have Kempe distance exactly two, not one.  The example is
only a mechanism barrier: it contains a `K_7` minor and is not minor-minimal
subject to being non-six-colourable.

**Audited revisions and SHA-256 hashes:**

- `barriers/hc7_opposite_response_kempe_bridge_barrier.md` —
  `ca51cb9deaba0a3d94bcdce94de8fd1455aa89af423d3fd48883349bfe9b973a`;
- `barriers/hc_opposite_response_transition_barrier_verify.py` —
  `9259d294a97f84955be89f018bda4e5f1aa5ecac47830b9e3f5d843163bdd227`.

The source was amended during audit only to repair mathematical typesetting,
make its two-connectivity justification explicit, and link this audit.  The
verifier was amended to choose set roots deterministically and to assert the
advertised colouring counts.

## 1. Replay and determinism

Running

```text
python3 barriers/hc_opposite_response_transition_barrier_verify.py
```

completed successfully and printed:

```text
GREEN separated opposite-response transition barrier
colourings: G-g=24, G-h=24, H=72
boundary languages: G-g={equal}, G-h={different}
common-host signatures: EE, EP, PE; PP absent
Kempe reconfiguration graph of H: one component containing both languages
shortest response-to-response Kempe distance=2, through EE
padded lift: q=6, boundary=8, connectivity=8, both shores full
padded common host contains K6; padded full host contains K7 minor
```

The same output and assertions were reproduced with `PYTHONHASHSEED=1` and
`PYTHONHASHSEED=777`.  Search ordering cannot affect the certificate: the
colouring search is exhaustive, Kempe components are traversed exhaustively,
and all formerly arbitrary set roots are now chosen by `min`.

## 2. The ten-vertex core

For each of `aa'` and `bb'`, the five displayed edges induce a copy of
`K_4` minus the edge between the nominated pair.  In every proper
three-colouring of this diamond, its adjacent vertices `p,q` have distinct
colours and both nominated nonadjacent vertices must use the third colour.
Thus `a=a'` and `b=b'` as colour equalities.

After making `c,d` adjacent to both `a',b'`, the colouring constraints on
the four effective vertices `a,b,c,d` are exactly those of a `K_4`; `g=ab`
and `h=cd` are a disjoint matching in that effective graph.  Consequently:

- the full core `J` is not three-colourable and is four-colourable;
- in `J-g`, `a=b` and hence `a'=b'`, while `c` and `d` are different;
- in `J-h`, `c=d`, while `a,b` and hence `a',b'` are different;
- deleting both edges permits precisely `EE`, `EP`, and `PE`;
- `PP` would restore a three-colouring of `J` and is impossible.

The exhaustive enumeration gives 24 labelled three-colourings of each
one-edge deletion and 72 of the common deletion, agreeing with the written
claim.  The common deletion is exactly three-chromatic because it is
three-colourable and contains the triangle `{a,p_a,q_a}`.

The displayed open shores are

```text
A0 = {a,b,p_a,q_a,p_b,q_b},   B0 = {c,d},   S0 = {a',b'}.
```

There is no `A0-B0` edge, while `g` and `h` are internal to the respective
shores.  Each diamond is two-connected.  The two diamonds are joined by
`ab` and by the two internally disjoint paths `a'cb'` and `a'db'`.
Deleting any one vertex leaves one such inter-gadget join and leaves `c,d`
attached, proving that `J` is two-connected as used later.

## 3. Kempe reconfiguration claims

The verifier constructs all standard Kempe neighbours: for each unordered
pair of colours it finds every connected component of the induced
two-colour graph and swaps that component.  The graph on all 72 labelled
three-colourings of `J_0=J-{g,h}` is one connected component.

No colouring of `J-g` is one Kempe interchange from a colouring of `J-h`.
The exhibited route has two valid interchanges.  From the `PE` colouring,
`{b,b',p_b}` is exactly one zero-one Kempe component; swapping it produces
`EE`.  In that intermediate colouring, `{d}` is exactly one one-two Kempe
component; swapping it produces `EP`.  Since the response families are
disjoint and no direct edge joins them, this length-two route proves that
their distance is exactly two.

## 4. Six-colour lift and boundary

Let `T` be the added triangle and let `W={w_0,w_1,w_2}`.  Every vertex of
`T union W` is adjacent to every vertex of `J`; every `w_i` is also adjacent
to `t_1,t_2` and not to `t_0`.  The boundary

```text
S = {a',b',t_0,t_1,t_2,w_0,w_1,w_2}
```

has order eight.  The shores `A=A0` and `B=B0` remain connected.  Direct
inspection of the edge definition shows that both shores meet every
literal boundary vertex, and that there is still no `A-B` edge.

If at most seven vertices are deleted and both `J` and `T union W` remain,
the surviving complete join is connected.  All ten vertices of `J` cannot
be deleted.  If all six vertices of `T union W` are deleted, at most one
vertex of the two-connected graph `J` is additionally deleted, so the
remainder is connected.  Hence the lift is eight-connected.  Deleting the
displayed boundary separates the two nonempty shores, so its connectivity
is exactly eight.  The verifier independently checks every vertex deletion
set of order at most seven and the displayed order-eight cut.

The induced subgraph `T join J` has chromatic number `3+4=7`, while all
`w_i` can receive the colour of `t_0`; hence the lift has chromatic number
exactly seven.  In the common deletion, `T join J_0` has chromatic number
six and contains the literal clique

```text
T union {a,p_a,q_a}.
```

Thus the common host is exactly six-chromatic and contains a literal
`K_6`.  In every six-colouring, `T` and `J_0` use disjoint three-colour
palettes.  Each `w_i`, being adjacent to all of `J_0` and to `t_1,t_2`,
must use the colour of `t_0`.  The two boundary partitions in the source
therefore follow exactly from the core equal/different relation.

An `EE` colouring of `J_0` identifies consistently across both disjoint
edges, so it descends to a six-colouring after contracting `g` and `h`.
This verifies the named double-contraction response.

A Kempe interchange using two core colours is exactly a core interchange.
For one triangle-palette colour and one core-palette colour, the complete
join puts the two whole colour classes in one Kempe component, so the swap
preserves all endpoint equality relations.  A swap between two triangle
palette colours also leaves the core signatures unchanged.  Therefore the
core's absence of a direct response-to-response interchange survives in
the six-colour lift, while the displayed two-switch route lifts unchanged.

## 5. Minor models and trust boundary

The literal `K_6` was checked above.  The seven displayed branch sets for
the full lift are connected and disjoint.  Among the four non-`T` bags:

- the first two are adjacent through `g=ab`;
- each of them contacts each singleton `{c}` and `{d}` through `a'` or
  `b'`; and
- `{c}` and `{d}` are adjacent through `h=cd`.

They therefore form a `K_4` model, and every singleton of `T` is adjacent
to every one of its bags.  This is an explicit `K_7` model.  The verifier
checks induced connectivity of each bag and every pairwise bag adjacency.

Deleting any `w_i` leaves the seven-chromatic subgraph `T join J`, so the
lift is not minor-minimal subject to being non-six-colourable.  These two
failures are stated prominently and prevent the construction from being an
`HC_7` counterexample or from refuting a terminal theorem whose conclusions
include a `K_7` minor.

The exact barrier is narrower: connectedness of the common deletion's
Kempe reconfiguration graph, even with the three proper-minor signatures,
does not itself transfer a legal one-edge response across the boundary.
Minor-minimality or `K_7`-freeness must be used to interpret an intermediate
`EE` colouring.

## 6. Relation to earlier barriers

No duplicate of this exact construction was found in the repository.  The
closest promoted barrier is the common-host odd-antihole family.  That
family has the opposite one-edge responses but **does not** admit `EE`, so
its simultaneous named double contraction is not colourable.  The present
barrier was designed precisely to retain `EE`, a legal double-contraction
response, an actual full order-eight separation, and a length-two Kempe
bridge.  It therefore blocks a strictly different transition inference.
