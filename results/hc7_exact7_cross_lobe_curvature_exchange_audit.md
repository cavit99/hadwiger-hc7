# Independent audit: cross-lobe curvature exchange

Audited file: `hc7_exact7_cross_lobe_curvature_exchange.md`.

## Verdict

**GREEN.**  The six-label circle bound, the planar-curvature contradiction,
and the exact-seven cross-lobe application are valid as stated.  The audit
covered arbitrary shared portal vertices; it did not assume that portal
sets are disjoint beyond what the proof derives.

The exact promoted proof version checked in this audit has SHA-256

```text
69ec0f6104af79412d26f5910f8f47167a2dfdee78e2080629ac78400e03dcaf
```

Theorems 1.1 and 2.1 and Corollary 3.1 were reread line by line at this
exact hash, including every endpoint coincidence, the charging injection,
the Euler inequality, and the exact-state reflection application.

## 1. Circular confinement

The proof first derives `P_i cap P_{i+3}=empty`.  A common vertex would
itself fund duty `i`; because the six selected representatives are
distinct, one of the other two selected duty paths avoids that vertex.
This ordering is essential: it excludes `v=x_{i+3}` before the subsequent
four-endpoint alternation argument.

For `v in P_i`, comparison with each of the two other duties confines `v`
to two closed arcs.  Their intersection is exactly the selected
`x_{i-1}-x_{i+1}` sector through `x_i`.  Endpoint coincidences with the
other duty are harmless because those endpoints already lie on the stated
closed arc.  Thus an open selected gap carries only its two adjacent
labels, while a selected representative can carry only its own label and
the two adjacent labels.

## 2. Adjacent-overlap charging

If two distinct vertices belonged to both adjacent portal sets `P_i` and
`P_{i+1}`, swap their duty roles.  In cyclic order

```text
u, v, x_(i+3), x_(i+4),
```

the `v-x_(i+3)` and `x_(i+4)-u` arcs are disjoint and fund the two
different duties.  Hence each adjacent pair of portal sets overlaps in at
most one vertex.

Every incidence above the first at a vertex is charged to one adjacent
portal-set pair containing that vertex.  At a selected vertex its own label
is mandatory, so each extra adjacent label receives a different charge.
There are six adjacent pairs and each is charged at most once.  Adding at
most one base incidence per cycle vertex gives the exact upper bound

\[
                          \sum_v\lambda(v)\le |F|+6.
\]

## 3. Curvature calculation

Taking the common face `F` as the outer face is legitimate.  If `I` is the
set of other vertices, Euler's formula and the inner-face length bound give

\[
 \sum_{v\in I}(6-d_C(v))+
 \sum_{v\in F}(4-d_C(v))\ge6.
\]

Every interior vertex has no boundary neighbour among the six duty labels,
and at most the singleton `c` remains.  Minimum degree seven therefore
gives `d_C(v)>=6` on `I`, so the facial curvature sum is at least six.
For a facial vertex, `c` contributes at most one boundary edge, whence
`lambda(v)>=6-d_C(v)`.  Summation yields

\[
                          \sum_v\lambda(v)\ge2|F|+6,
\]

contradicting the circle bound.

## 4. Exact-seven hypotheses

The audited common-face theorem supplies a plane three-connected component
whose complete six portal sets lie on one facial cycle.  Its order-five
exclusion and Hall lemma supply six distinct portal representatives; full
nonreflection forces their duty word to be `A B D A B D` and forbids every
two disjoint duty carriers, including facial subpaths.  The frozen
minimal-counterexample kernel supplies minimum degree seven.  These are
exactly the hypotheses of the curvature theorem, so the attained state
must reflect.

## 5. Independent finite falsification audit

As a check on shared-portal edge cases, an independent solver encoded every
nonempty proper cyclic interval as a possible carrier, an arbitrary
six-label incidence relation, and an ordered SDR.  For cycle orders
`6,...,12`, it found exact maxima

```text
12, 13, 14, 15, 16, 17, 18,
```

equal to `|F|+6` in every case.  A second endpoint-alternation encoding
independently made the threshold `|F|+7` unsatisfiable.  These computations
are corroboration only; the theorem rests on the preceding elementary
proof.

## Trust boundary

The theorem closes the cross-lobe one-sibling support family.  It does not
apply when only two of the three duty-pair failures are known, and it does
not close the distinct single-missing-duty family retained by the
Hall-and-duty funnel.
