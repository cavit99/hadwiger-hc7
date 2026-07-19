# Audit of the exact-seven crossing three-response barrier

**Verdict:** **GREEN** for the exact source and verifier revisions recorded
below.

This is an independent internal audit, not external peer review.  It checks a
finite counterarchitecture to an intermediate inference.  It does not certify
a counterexample to Hadwiger's conjecture; the constructed graph deliberately
has a `K_7` minor and is not minor-minimal among non-six-colourable graphs.

## Audited revisions

- theorem source:
  `archive/hc7_exact7_crossing_three_chamber_barrier.md`
- source SHA-256:
  `b029098adeab64280da30f55af85dac3beea3a984d74ce896ea964d600ddd73c`

The source differs from the originally audited revision only in the
documented verifier invocation after this superseded package was moved to
`archive/`; the graph, theorem statement, and verifier are unchanged.
- deterministic verifier:
  `archive/hc7_exact7_crossing_three_chamber_barrier_verify.py`
- verifier SHA-256:
  `7291d12005e4f344ddab8250e7d2faea626b8e3bc81e279f3206748d5bb02164`

The verifier was run from the repository root and produced exactly the output
stated in the source.

## Audit method

The graph was reconstructed independently from the displayed edge list.  In
addition to reading the proof and verifier line by line, the audit used a
separate exhaustive backtracking check for vertex cuts, colourings, connected
boundary-full subgraphs, their packing number, and the displayed minor
models.  The independent check did not call the verifier's graph or colouring
helpers.

The exhaustive check found:

- the first vertex cuts have order seven;
- the full graph is not five- or six-colourable and is seven-colourable;
- the boundary is not three-colourable and is four-colourable;
- every one of `G-e`, `G-f`, `G-{e,f}`, `G/e`, `G/f`, and `G/e/f` is
  six-colourable but not five-colourable;
- modulo permutations of the six colours, `G-{e,f}` has twelve colourings,
  all with the one claimed boundary partition and exactly the three claimed
  endpoint-equality signatures; and
- the two open shores have boundary-full packing numbers two and one.

## Claim-by-claim reconstruction

### 1. Separation and connectivity

The displayed sets `A`, `S`, and `B={ell}` are nonempty where required,
partition the vertex set, and there is no `A-B` edge.  The neighbourhood of
`ell` is exactly the seven-set `S`, so deleting `S` separates `ell` from the
connected set `A`.

Let `W=T union {w_0,w_1}`.  The set `W` is connected, has five vertices, and
is complete to the ten-vertex core `J`.  The core `J` is two-connected: an
independent cut-vertex check finds none, and this also follows directly from
the two diamond subgraphs and their two independent routes through `c,d`.
After deleting at most six vertices, if both `J` and `W` remain, their complete
join connects the remainder.  All of `J` cannot have been deleted.  If all
five vertices of `W` were deleted, at most one vertex was deleted from the
two-connected `J`.  Thus this fifteen-vertex subgraph remains connected.
If `ell` remains, one of its seven neighbours also remains.  Consequently no
set of at most six vertices disconnects `G`, while `S` does, and therefore
`kappa(G)=7`.

### 2. Chromatic numbers

In a proper three-colouring of either diamond, the two ends of its missing
edge receive the same colour.  Hence a three-colouring of the full core `J`
would induce a three-colouring of a `K_4` on the effective vertices
`a,b,c,d`, which is impossible.  An explicit four-colouring exists, so
`chi(J)=4`.

The subgraph `T vee J` therefore has chromatic number seven.  Conversely,
colour `J` with four colours, use three new colours on `T`, give both `w_i`
the colour of `t_0`, and give `ell` a core colour absent from `b,d`.  This is a
seven-colouring, proving `chi(G)=7`.

On the boundary, `b,t_0,t_1,t_2` induce a `K_4`.  The proposed colouring with
`b,d` equal, `T` rainbow, and `w_0,w_1` equal to `t_0` is proper.  Thus
`chi(G[S])=4`.

### 3. Boundary-full packing numbers

Every vertex of `A` is adjacent to the five boundary vertices in
`T union {w_0,w_1}`.  A connected boundary-full subgraph of `A` must also
meet both

```text
{a,pb,qb}       and       {c,ap,bp},
```

the respective sets of neighbours in `A` of `b` and `d`.  Every path in
`G[A]` between these portal sets meets `{ap,bp}`.  Hence at most two such
connected subgraphs can be disjoint.  The disjoint connected sets
`{a,pa,ap}` and `{pb,bp}` are both boundary-full, so `nu_A=2`.  The singleton
`{ell}` is boundary-full, giving `nu_B=1`.

The independent exhaustive enumeration found 36 connected boundary-full
subsets of `A` and confirmed that their maximum disjoint packing has order
two.

### 4. The three response types

After deleting `e=ab` and `f=cd`, the two diamond equalities reduce the
three-colouring constraints on `a,b,c,d` to those of `K_{2,2}`.  If `a,b`
receive distinct colours, both `c,d` must receive the third colour; the
symmetric assertion also holds.  Therefore the possible endpoint signatures
are exactly

```text
EE, EP, PE,
```

and `PP` is impossible.  All three displayed signatures have explicit
three-colourings.  The edge `bp d`, together with the forced equality
`b=bp`, shows that `b` and `d` differ in every such colouring.

The literal clique on `T union {a,pa,qa}` is a `K_6` in the common response
host.  Hence every six-colouring uses three colours on `T` and three disjoint
colours on the core.  Each `w_i`, being complete to the core and adjacent to
`t_1,t_2`, must receive the colour of `t_0`; `b,d` receive two different core
colours; and `ell` receives the remaining core colour.  Thus every response,
not merely the specifically constructed responses, induces exactly

```text
{{t0,w0,w1},{t1},{t2},{b},{d}}
```

on the literal boundary.

Colourings of `G/e` are equivalent to colourings of `G-e` in which `a,b`
are equal, and similarly for `f`.  The three signatures therefore supply
six-colourings of both single-edge deletions, both single-edge contractions,
and the double contraction.  The displayed `K_6` survives each operation
(with the contracted vertex replacing `a` when needed), so none of these
graphs is five-colourable.  Their chromatic number is exactly six.

### 5. Demand and shore compatibility

The singleton blocks of the boundary partition induce `K_4-bd`, whose clique
number is three.  Under the stated full-subgraph-demand definition, the
demand is consequently `5-3=2`, which is strictly larger than `nu_B=1`.

The closed singleton shore extends the five boundary blocks by assigning the
sixth colour to `ell`.  The intact other closed shore contains the
seven-chromatic subgraph `T vee J`, so it rejects every six-colouring and in
particular rejects the selected partition.

### 6. Explicit minor models

The claimed `K_6` is a literal clique in the common response host.  The seven
sets

```text
{t0}, {t1}, {t2}, {a,pa,ap}, {b,pb,bp}, {c}, {d}
```

are pairwise disjoint and connected.  The first three are mutually adjacent
and complete to the four core branch sets.  Among the latter four, the six
required adjacencies are supplied respectively by `ab`, `ap-c`, `ap-d`,
`bp-c`, `bp-d`, and `cd`.  They therefore form the stated `K_7`-minor model.

Deleting `ell` leaves `T vee J`, which remains seven-chromatic.  This proves
both advertised failures of the global hypotheses used in the active
minimal-counterexample programme.

## Verifier audit

The verifier faithfully constructs the graph from the displayed definition.
It exhaustively checks every deletion set of order at most six, the displayed
order-seven cut, connected boundary-full subsets and their packing number,
the core colouring signatures, the unique lifted boundary partition,
boundary chromatic number, demand, the response `K_6`, shore rejection, and
all branch-set conditions for the `K_7` model.

The verifier derives rather than explicitly constructs the contraction
responses, and it constructs lifted host colourings rather than enumerating
all host colourings.  These are not gaps: the quotient-colouring equivalence
and the `K_6` palette argument above prove the two implications, and the
independent enumeration checked them directly.

## Exact scope and trust boundary

The construction proves that the following local information is jointly
insufficient for common-partition closure:

- an actual order-seven interface with connected boundary-full shores;
- packing vector `(2,1)`;
- a four-colourable boundary and excessive partition demand;
- two disjoint same-shore crossing edges;
- all three non-`PP` proper-minor response signatures; and
- agreement of every response on one literal boundary partition.

It does **not** show that either omitted global hypothesis is individually
necessary.  It shows only that additional global information is necessary.
In the active `HC_7` programme, the available information includes
`K_7`-minor exclusion and six-colourability of every proper minor.

There are no unresolved mathematical assumptions within this stated finite
scope.  The barrier does not refute a theorem retaining the full hypotheses
of a hypothetical minor-minimal `HC_7` counterexample.
