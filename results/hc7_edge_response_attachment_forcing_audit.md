# Independent audit of attachment forcing from proper-minor colourings

**Verdict:** GREEN for the exact source revision audited.

## Audited revision and scope

- source file: `hc7_edge_response_attachment_forcing.md`
- current source SHA-256:
  `b51e6653200f54d4fb0bb950ddd98f49c7be46a0b8ff9d696ad2b241c4267862`
- original audited revision SHA-256:
  `378334b7e351d0b8b625a346e20ca2f17316ffe934fceaef919525dfdbeecb2c`

The current source differs from the original audited revision only at line 3:
the pre-audit status `written proof draft awaiting an exact-file audit` was
replaced by `written proof; separate internal audit GREEN`.  Mechanically
restoring the former status text reproduces the original audited SHA-256
exactly.  No setup, theorem, proof, example, HC7 application, dependency, or
trust-boundary text changed.  The GREEN verdict therefore rebinds to the
current source hash above.

This audit checks every statement in Sections 2--5, Example 3.2, and the
application and trust-boundary claims in Sections 6--8.  It does not audit the
three external HC7 dependencies as new theorems, and it does not promote the
conditional application to a proof of `HC_7`.

## 1. Setup and operation bookkeeping

The setup is sufficient for all displayed extensions.  Because the operated
edge `xy` lies in `Q`, neither deletion nor contraction changes the vertices
of the induced bipartite subgraph `X`.  In the contraction case the quotient
vertex `w` has precisely the union of the outside neighbourhoods of `x,y`,
with loops and parallel edges suppressed in the usual simple-graph minor.
Thus `S_m,T_m` record exactly the quotient vertices which can conflict with a
constant colour on `A` or `B`.

No connectivity or domination hypothesis is used in Sections 2--4.  The
stronger assumptions are introduced only where they are needed in Section 5.

## 2. Theorem 2.1: deletion and contraction extensions

### Edge deletion

If `c` is absent from `psi(T_m)`, giving `B` colour `c` and `A` the fresh
colour `q` is proper on `G-e`:

- `psi` is proper on `Q-e`;
- no neighbour of `B` in `Q` has colour `c`;
- colour `q` is absent from `Q`; and
- every edge of the induced bipartite graph `X` has one end in each class.

The ends of the deleted edge must then have one common colour `alpha`, since
otherwise the edge can be restored.  If an endpoint misses any colour
`beta != alpha` in its neighbourhood, recolouring only that endpoint with
`beta` and restoring `xy` remains proper.  This contradicts `chi(G)>q`.
Taking `beta=q` forces both endpoints to meet `A`.  Interchanging `A,B`
proves the second assertion.  The proof uses no hidden assumption that `psi`
uses every colour.

### Edge contraction

The same constant extension is proper on `G/e`.  To expand `w`, retain its
colour `alpha` on one original endpoint and put the fresh colour `q` on the
other.  If, for example, `x` has no neighbour in `A`, then no old neighbour
of `x` has colour `q`; every neighbour of `y` other than `x` is represented
as a neighbour of `w` and hence has colour different from `alpha`.  The edge
`xy` has differently coloured ends.  This would properly `q`-colour `G`.
The symmetric expansion treats `y`, and exchanging the bipartition classes
treats attachment to `B`.

This verifies that the conclusion concerns both *original* endpoints even
though the response colouring has only the quotient vertex `w`.

## 3. Proposition 2.2: endpoint saturation

The saturation argument is valid for all colours in the displayed
`q`-colouring, not merely for the fresh colour.  In the contraction case, if
`x` has no neighbour of colour `beta != alpha`, assign `beta` to `x` and
`alpha` to `y`.  The first colour is safe by the assumed absence; the second
is safe because every old neighbour of `y` other than `x` was a neighbour of
`w`; and `xy` is proper because `beta != alpha`.  Reversing the endpoints
proves the statement for `y`.

The source correctly limits this to palette saturation in one extension.  It
does not infer that a witnessing neighbour belongs to a prescribed minor
branch set.

## 4. Theorem 3.1 and Example 3.2

A common missing colour first invokes Theorem 2.1 on both sides.  Since each
endpoint then meets both `A` and `B`, an endpoint coloured `c` would itself
belong to `S_m` and `T_m`, contradicting the common-hole hypothesis.  Hence
`psi(x)=psi(y)=alpha != c`.

In the first extension, if `x,y` were in different `alpha`--`q` Kempe
components, swapping the two colours on the component containing `x` would
separate their colours and permit restoration of `xy`.  Therefore an
`x`--`y` alternating path exists.  Its `q`-vertices lie in `A`, and, because
`alpha != c`, its `alpha`-vertices are exactly vertices of
`psi^{-1}(alpha)` in `Q`.  The exchanged extension gives the corresponding
path through `B`.

The two paths have no common edge: every edge of one has its non-`alpha` end
in `A`, while every edge of the other has that end in disjoint `B`.  Their
common vertices are therefore `alpha`-vertices.  Taking the first return of
the first path to the second path yields two internally disjoint, edge-disjoint
subpaths with the same `alpha`-coloured ends, and hence a cycle.  This proves
the stated local-cycle conclusion without claiming that its two ends are
`x,y`.

Example 3.2 checks exactly.  The induced graph on `A union B` has edges
`ab,ad,cd`, hence is the path `b-a-d-c`, and every one of `r,s,t` meets both
bipartition classes.  In each `K_4` minus the named missing edge, the missing
edge ends must receive the same colour in a three-colouring.  The two copies
therefore force `r=s=t`, contradicting `st`.  After deleting `st`, the two
relevant bichromatic graphs are paths, so their unique endpoint paths are
`s-a-r-c-t` and `s-b-r-d-t`.  They share the internal vertex `r`, providing
the claimed counterexample to an `x`--`y` lens.

## 5. Theorem 4.1: vertex deletion

The vertex analogue uses the same proper extension on `G-v`.  If `v` misses
`A`, the fresh colour can be assigned to `v`; if it misses `B`, the symmetric
extension applies.  More generally, any colour absent from the neighbourhood
of `v` in the displayed colouring can be assigned to `v`, so the final
palette-saturation observation is also correct.

## 6. Proposition 5.1 and Theorem 5.2

Domination gives each vertex of `Q` exactly one of the three stated types.
If a connected subgraph has both one-sided types but no two-sided vertex, a
path between the types contains a first edge across the type change.  This is
the complete trichotomy; it does not require the connected subgraph to be
induced.

The full-palette conclusions follow with the orientations stated in the
source:

- for an `A`-only--`B`-only edge, a hole on either attachment set contradicts
  the type of one endpoint;
- for two `A`-only endpoints, a hole on `S_m` would force both endpoints to
  meet `B`; and
- the `B`-only case is symmetric.

The chromatic equality after either edge operation is also valid.  Since `X`
is connected and dominates `Q_m`, contracting all of `X` produces exactly
`K_1 join Q_m`.  This is a proper minor of `G`, so it is `q`-colourable and
`chi(Q_m)<=q-1=p`.  A colouring of `Q_m` with at most `p-1` colours, regarded
as a colouring with palette `[p]`, has an unused colour on every attachment
set and contradicts the already proved fullness.  Thus `chi(Q_m)=p`.

For a one-sided singleton, Theorem 4.1 gives the same fullness after vertex
deletion, while contraction of the unchanged connected dominating `X` gives
the same chromatic upper bound.  Hence `chi(Q-v)=p` as claimed.

## 7. Counterexample search

As a falsification aid, I exhaustively enumerated all simple graphs on four
through six vertices with singleton nonempty bipartition classes at `q=3`.
Among graphs with chromatic number greater than three, the scan checked
63,918 proper edge-response colourings, including 1,202 common-hole deletion
responses, and 44,130 vertex responses.  Restricting to the connected,
dominating, minor-critical hypotheses checked 144 applicable edge-operation
palette-equality responses and 192 one-sided singleton responses.  No
counterexample occurred.  The scan was auxiliary only; the GREEN verdict
rests on the written arguments above.

The sharp failure sought by the audit is already present in Example 3.2:
the two alternating paths need not be internally disjoint.  Dropping the
connectivity or domination hypotheses also invalidates the join argument for
the chromatic equalities, which is why those hypotheses are correctly confined
to Section 5.

## 8. HC7 application and trust boundary

The specialization `q=6,p=5` is consistent with a seven-chromatic graph all
of whose proper minors are six-colourable.  For a connected component lying
in one of the protected subgraphs `D_i subseteq Q`, Proposition 5.1 gives
exactly the three listed cases.  A non-singleton one-sided component contains
an internal edge, and a singleton is covered separately by Theorem 4.1.

The source does not turn a colour class into a labelled branch set, does not
claim two endpoint-rooted Kempe paths after contraction, and does not obtain
a bounded or colour-compatible separator.  It also explicitly excludes the
unsupported inference that every lifted simplicial component lies in `Q`,
since the protected bipartite subgraph `X` remains another possible label.
The six limitations in Section 7 and the seven nonterminal observations in
Section 6 match the actual logical boundary of Sections 2--5.

## Unresolved assumptions or gaps

None within the stated attachment-forcing, local-cycle, trichotomy, and
chromatic-equality results.  Their use in the HC7 programme remains
conditional on the cited connected-bipartite compression and defect-one
setup, and the source correctly records that this conditional input does not
prove `HC_7`.
