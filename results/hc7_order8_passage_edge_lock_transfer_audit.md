# Independent audit: passage-edge lock transfer

**Verdict:** **GREEN.**

**Audited source:**
[`hc7_order8_passage_edge_lock_transfer.md`](hc7_order8_passage_edge_lock_transfer.md)

**Source SHA-256:**

```text
127b2fec273bb40de24f0e57485ebc58c8fcbda8da6dfcf33b242e141140d570
```

The promoted revision differs from the audited mathematical source only in
its status line and adjacent-audit link; the theorem statement and proof are
unchanged.

This is a separate internal mathematical audit of the complete source:
Theorem 2.1, Propositions 3.1 and 3.2, the cited separator and linkage
inputs, and the stated limitations.  It is not external peer review.

## 1. One-edge lock transfer

Let `H` be the `alpha,beta` component containing `d,e`, and let `f=uv`
lie on an `alpha,beta` `d`--`e` path.  The two alternatives in Theorem
2.1 are exhaustive.

If `H-f` still connects `d,e`, a shortest such path has no internal
boundary vertex: `beta` is absent from `S`, and the only
`alpha`-coloured boundary vertices are `d,e`.  Its interior therefore lies
in `L`, so the assumed ordered-crossing theorem applies literally.

Otherwise `f` separates `d,e` in `H`.  Swapping `alpha,beta` on the
component of `H-f` containing `d` is a valid Kempe interchange after
deleting `f`.  No `alpha,beta` edge leaves that component, including to a
vertex outside `H`, because `H` was the complete bichromatic component
before the deletion.  The swap changes `d` but not `e` and leaves `X,Y`
unchanged, so it gives exactly the split boundary partition.  Aligning its
four boundary-block colours with the given opposite-shore colouring is
legitimate, and the anticompleteness of the two open shores makes the
gluing proper.

Exactly one endpoint of `f` is swapped.  Its two old colours were
`alpha,beta`, so the endpoints become equal and the colouring descends to
`G/f`.

For an arbitrary six-colouring of `G-f`, the endpoints must be equal;
otherwise restoring `f` would six-colour `G`.  If they were separated in
one of the corresponding two-colour subgraphs, swapping the component of
one endpoint would make `f` proper, giving the same contradiction.  Hence
the universal five-colour lock and the neighbour-saturation conclusion are
both valid.  This also proves the stated obstruction to a single Kempe
interchange.

## 2. The two-edge equality signatures

For two vertex-disjoint edges, contracting precisely any nonempty subset
gives a proper minor.  In a six-colouring of that minor, each contracted
edge expands to an equal pair while every uncontracted marked edge remains
a proper edge.  This gives exactly

```text
(=,=), (=,different), (different,=).
```

An all-different colouring of the common deletion would remain proper
after restoring both edges and would six-colour `G`, so the fourth
signature is absent.

The connectivity and separator conclusions in Proposition 3.1 are the
two-edge specialization of the separately GREEN-audited matching-deletion
separator budget.  It yields `kappa(J)>=5` when `G` is seven-connected.
At an order-five separation, both deleted matching edges cross.  With

```text
f_1=a_1b_1, f_2=a_2b_2,
a_1,a_2 in A, b_1,b_2 in B,
```

the set `T union {b_1,a_2}` has order seven, meets both restored crossing
edges, and leaves `a_1,b_2` on distinct nonempty sides.  It is therefore
an actual order-seven separator of `G`.  The revised source explicitly
scopes this conclusion to seven-connected `G`; no small-open-side endpoint
choice is being assumed.

If `J` is six-connected, Jung's theorem, in the Stephens--Ye Theorem 1.1
form, makes it two-linked.  Applying it to each pairing of the four
distinct edge endpoints supplies all three linkages.  Fabila-Monroy--Wood,
Theorem 8, then gives the claimed endpoint-rooted `K_4` minor.  The theorem
numbers and hypotheses are used at their valid scopes.

## 3. The untouched edge in Proposition 3.2

For distinct private colours `beta_i,beta_j`, perform the
`alpha,beta_i` interchange on the `d`-component after deleting `f_i`.
The endpoints of `f_j` initially have colours `alpha,beta_j` in some
order.  Its `beta_j` endpoint cannot change, and its `alpha` endpoint
either stays `alpha` or changes to `beta_i`.  Both possibilities remain
different from `beta_j`.  Thus the retained edge `f_j` stays proper.

The interchange consequently gives the signature with exactly `f_i`
equal and still induces the literal split partition on `S`.  Reversing the
roles gives the other one-equal signature with the same literal boundary
partition.  Contracting both edges gives the all-equal signature, and the
all-different signature is excluded exactly as in Proposition 3.1.

## 4. Trust boundary

The source correctly stops at an endpoint-rooted `K_4` or an actual
order-seven separator.  It does not claim that the rooted branch sets
respect the two named deficient connected subgraphs, that the new
seven-vertex separator receives one common boundary partition from both
closed shores, or that the static rooted model alone produces a `K_7`
minor.  The cited width-five barrier is used only to reject that stronger
static implication.

No unresolved mathematical gap remains within the stated scope.
