# Falsification of boundary-only three-bridge closure

**Scope.**  This note tests only the proposed inference from the two-coordinate
fork to a `K_6` minor in the augmented boundary.  It does not construct a
hypothetical minor-minimal counterexample to `HC_7`, and it does not refute the
two-coordinate fork itself.

## Verdict

The proposed boundary-only closure is false, already at boundary order nine.
There is a connected graph `H` satisfying all three compact conditions, a
proper labelled colouring for which `H[alpha,beta]` has four components, and
three supported nonedges in exactly the forked pattern, but the three-edge
augmentation is still `K_4`-minor-free.  Hence it certainly has no `K_6`
minor.

Even the strongest four-edge pattern naturally suggested by the two cut
coordinates fails: two vertex-disjoint supported edges in each shore can form
crossing matchings on the same four `alpha`--`beta` components, while the
four-edge augmentation remains `K_4`-minor-free.

## 1. A connected order-nine witness

Let `V(H)={0,...,8}` and

```text
E(H) = {04,08,48, 15,18, 26,28, 37,38}.
```

Thus `048` is a triangle and `8-1-5`, `8-2-6`, `8-3-7` are three
length-two arms.  Give the boundary the proper colouring

```text
alpha : {0}
beta  : {5,6,7,8}
gamma : {1,2,3,4}.
```

The other two palette names are unused.  Then the components of
`H[alpha,beta]`, labelled so that the distinguished root component is a
singleton, are

```text
W_0={5},  W_1={0,8},  W_2={6},  W_3={7}.
```

The vertex `x=5` has no `alpha`- or `beta`-coloured neighbour, so
`W_0={x}` has the exact root form in the synchronized-fork theorem.  Regard
`W_0,W_1` as the two operated coordinates.  One fixed shore may
support the two nonedges

```text
f_0=57  between W_0 and W_3,
f_1=06  between W_1 and W_2.
```

Their four boundary endpoints are distinct, so the two supporting paths can
have disjoint interiors, exactly as in the fixed-extension alternative.  The
other shore may support

```text
e_1=87  between W_1 and W_3.
```

All three displayed pairs are nonedges of `H` and join distinct
`alpha`--`beta` components.  Paths in the two shores have disjoint,
anticomplete interiors automatically; no further boundary incidence is being
assumed.

Put

```text
H_3 = H + {06,57,87}.
```

This is the exact three-supported-edge augmentation proposed for closure.

## 2. Direct audit of the compact hypotheses

The four pairwise vertex-disjoint cliques

```text
{0,4,8}, {1,5}, {2,6}, {3,7}
```

cover `V(H)`.  Therefore every independent set has order at most four, while
`{5,6,7,8}` is independent.  Hence

```text
alpha(H)=4,
```

which is the sharp allowed bound for `d_G(u)=9`.

The graph is a triangle with trees attached, so it is two-degenerate and has
no `K_4` minor.  Consequently it is three-degenerate and, for every two-set
`Z`, `H-Z` is `K_4`-minor-free.  The displayed colouring is proper: every
edge has ends in two of the three displayed colour classes.

Thus the witness satisfies all of the compact boundary conditions in the
question, and its two operated and two target components are genuinely four
distinct components of `H[alpha,beta]`.

## 3. The three-edge augmentation does not close

The graph `H_3` is a subgraph of the four-edge graph considered below, which
is `K_4`-minor-free.  In particular

```text
K_6 is not a minor of H+{06,57,87}.
```

There is also a coarser immediate check: `H_3` has only twelve edges, whereas
six pairwise adjacent disjoint branch sets require at least one distinct host
edge for each of the fifteen unordered pairs of branch sets.

This disproves the implication

```text
compact H + forked three supported nonedges  =>  K_6 minor in H+edges.
```

The failure is not caused by repeated endpoint pairs or by overlap of the two
fixed-shore paths: `57` and `06` have disjoint endpoints and join four
different two-colour components.

## 4. Stronger crossing-square test

If one optimistically retains the second path from the other cut coordinate,
take

```text
e_0=56  between W_0 and W_2.
```

The two shore-labelled matchings are then

```text
fixed shore : {W_0W_3, W_1W_2} represented by {57,06},
other shore : {W_1W_3, W_0W_2} represented by {87,56}.
```

Within each shore the two boundary pairs have disjoint endpoints.  At the
component level their union is a crossing `K_{2,2}` cycle.  Nevertheless

```text
H_4 = H + {06,57,87,56}
```

is still `K_4`-minor-free.  A direct series-reduction certificate is:

1. eliminate `1,2,3,4`, adding respectively the fill edges `58`, `68` and
   no new edge for the last two eliminations;
2. eliminate `0`, whose remaining neighbours are `6,8` and are already
   adjacent;
3. eliminate `6` from the remaining `K_4` minus the edge `67`;
4. the residue is a triangle.

Every eliminated vertex has at most two current neighbours, so this is a
width-two elimination certificate.  Thus even two crossing, internally
disjoint shore matchings do not force a `K_4` minor, much less a `K_6`
minor.

## 5. Computational route and trust boundary

A targeted graph6 search first checked order eight and then stopped at the
first connected order-nine residue.  It filtered exactly for the independence
bound, three-degeneracy, and the two-vertex `K_4`-minor exclusions; enumerated
proper choices of the two operated colours; required four distinct
two-colour components and disjoint endpoints for the fixed-shore pair; and
tested the resulting augmentation.  It returned graph6 string

```text
H?`@?bw
```

with the edge list above.  No finite census is needed for the conclusion,
because Sections 1--4 directly verify the explicit witness.

The witness is an abstract boundary/support counterexample only.  It does not
realize the full rejection map, seven-connectivity, or the literal
minor-minimal host.  Therefore it does **not** show that the exact common-root
residue exists.  It shows that contracting the forked paths to three or even
four boundary edges discards too much information to finish the proof.

## 6. Consequence for the proof strategy

The two-coordinate fork remains a genuine synchronized invariant, but its
terminal use must retain host-level geometry inside the full shores.  Any
viable next lemma has to exploit data absent from `H+edges`, such as multiple
attachments of the literal path components, a shore separation forced by
their placement, or the universal colourfulness/criticality of the full
host.  A further classification of the boundary edge pattern alone cannot
close this residue.
