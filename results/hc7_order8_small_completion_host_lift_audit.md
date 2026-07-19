# Independent audit: host lift for a small five-terminal completion

**Verdict:** **GREEN** for Theorem 2.1, Corollary 2.2,
Proposition 3.1, and the stated trust boundary.  This is a separate internal
mathematical audit, not external peer review.  The result is a conditional
host-level reduction and does not prove `HC_7`.

## Audited revision

This audit checks the complete source file
[`hc7_order8_small_completion_host_lift.md`](hc7_order8_small_completion_host_lift.md)
at SHA-256

```text
a2bb06c0c6301f5a1a5d806b3e2dd1cebb9f8c9b71fcc50e4b1fd5d30632981e
```

The promoted revision differs from the independently audited mathematical
source only in its status line and adjacent-audit link; the theorem statement
and proof are unchanged.

It also checks the normalized partition in
[`hc7_order8_ordered_two_three_allocation.md`](hc7_order8_ordered_two_three_allocation.md)
at SHA-256

```text
3f62092ab492815d5c21489e001e5732da76bc28454dac75206ba5aa61299dde
```

and the promoted small-boundary input
[`../results/hc7_order8_small_boundary_lobe_descent.md`](../results/hc7_order8_small_boundary_lobe_descent.md)
at its audited promoted SHA-256

```text
de980671b3053459e4e11845e510e5d96bb0a4f18d1a8bd50fe4b9dfae996d52
```

No unresolved mathematical gap was found at the audited revision.  During
the audit the source setting was repaired to state explicitly the named
merged-root partition used in (3.2); the hash above is the frozen revision
after that repair.

## 1. Exact host boundary

The displayed vertex partition, connectedness of `G[L]` and `G[R]`, and
absence of `L`--`R` edges make `L,R` the two components of `G-S`.
The normalized partition `L=E dotcup D` has both induced sides connected
and adjacent.  In particular `E,D` are nonempty and

```text
W = N_G(E) intersect D
```

is nonempty.

Every vertex outside `E` lies in exactly one of `D,S,R`.  There are no
`E`--`R` edges.  Exact normalization gives

```text
N_G(E) intersect S = S-{e},
```

and every remaining neighbour of `E` is, by definition, in `W subseteq D`.
The two classes are disjoint because `D` and `S` are disjoint.  Hence

```text
B = N_G(E) = (S-{e}) dotcup W
```

and `|B|=7+|W|` exactly.  No quotient edge or virtual completion edge is
used in this identity.

The set `E` is a nonempty connected proper subset of `L`; properness follows
from nonempty `D`.  The whole component `R` lies outside `E union B`, since
it is disjoint from `E,S,D` and has no edge to `E`.  Thus `B` is the full
neighbourhood of a nonempty connected side with a nonempty opposite side,
so it is an actual host separation boundary.

## 2. Applicability of the small-boundary lobe theorem

When `|W|=1`, the internal neighbours of `E` in the original component
`L` are exactly `W`, and its boundary neighbours are exactly the seven
vertices of `S-{e}`.  Therefore

```text
|N_{G[L]}(E)| + |N_G(E) intersect S| = 1+7 = 8.
```

This matches every hypothesis of the GREEN-audited small-boundary lobe
theorem:

- the host is seven-connected and satisfies the same minor-critical
  assumptions;
- `S` has order eight;
- `L` is a component of `G-S` and `R` is another component;
- `E` is a nonempty connected proper subset of `L`; and
- the displayed internal-plus-boundary neighbourhood sum is at most eight.

The invoked theorem returns exactly either an actual order-seven separation
or an order-eight boundary-full descent in which `E` is one component of
the new complement.  The descent is strict because `E subsetneq L`.

Since `W` is nonempty, the alternatives `|W|=1` and `|W|>=2` are exhaustive.
In the latter case the exact boundary identity immediately gives
`|B|>=9`, with all seven permitted literal vertices of `S` and at least two
literal vertices of `D`.  The source correctly calls this positive boundary
excess a residue, not a terminal contradiction or a decreasing parameter.

## 3. The small Xie-completion corollary

The selected completion has vertex set `E union {x_e}`.  The literal
boundary vertex `x_e` is outside `L` and hence outside `E`, so its order is
exactly `|E|+1`.  Order at most six is therefore equivalent to `|E|<=5`.
The proof of Theorem 2.1 does not use `|E|`, so all three host-boundary
alternatives remain valid in this small-order case.  Corollary 2.2 merely
removes small completion order as a qualitatively separate residue; it does
not claim that the positive-excess alternative is closed.

## 4. Edge-deletion response and colour gluing

The fixed colouring `c` is defined on `G[L union S]`.  The exact boundary
identity gives `E union B subseteq L union S`, so its restriction to
`G[E union B]` is available.

For every actual edge `uv` from `E` to `B`, the graph `G-uv` is a proper
minor and has a six-colouring.  Every such colouring gives `u,v` the same
colour: if they were different, the deleted edge could be restored and the
same colouring would properly six-colour `G`.

Now suppose an edge-deletion colouring, restricted to `G-E`, induced the
same equality partition on `B` as the fixed inner colouring.  Equality of
partitions gives a bijection between the colours used on `B`; this partial
bijection extends to a permutation of the full six-colour palette.  After
that permutation the two colourings agree vertexwise on their overlap
`B`.

The fixed colouring of `G[E union B]` covers every edge with at least one
endpoint in `E`, because `B=N_G(E)`; in particular it contains the original
edge `uv`.  The outer colouring of `G-E` covers every edge with neither
endpoint in `E`.  Their union is therefore a proper six-colouring of all of
`G`, contradicting `chi(G)=7`.  The outer equality partition must differ
from `pi_B`, exactly as Proposition 3.1 states.

The explicit assumption that `c` induces

```text
X | Y | {d,e}
```

on `S` makes its restriction to `S-{e}` exactly
`X | Y | {d}`.  The source makes no unsupported assertion about the colours
or equality classes of the additional boundary vertices in `W`.

## 5. Adversarial checks and trust boundary

I attempted to falsify the boundary and gluing arguments in the potentially
delicate placements:

- a vertex of `D` adjacent to many vertices of `E`;
- boundary vertices having additional edges within `S` or into `D`;
- `R` having arbitrary contacts with `S` or `D`;
- the edge-deletion colouring using fewer than six colours on `B`; and
- `|E|<=5` while `W` is arbitrarily large.

None invalidates the result.  The full-neighbourhood definition absorbs all
`E`--`D` contacts into `W`; additional edges not incident with `E` do not
alter `B`; the absence of `E`--`R` edges keeps `R` on the opposite side; a
partial boundary-colour bijection always extends to a permutation of six
names; and the proof never bounds `W` by the order of `E`.

The source accurately records the remaining gap.  It does not make a
positive-excess boundary into a well-founded descent, align palette colours
with the labels `P_0,P_1,A_d,A_e`, or prove that an order-seven separation
has compatible closed-shore colourings.  Within those stated limits, the
small-completion host lift is correct.
