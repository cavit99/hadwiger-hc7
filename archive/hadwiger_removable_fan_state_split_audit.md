# Independent audit of the removable-fan closure

## Verdict

**GREEN, conditional on the explicitly imported reserved-Moser setting in
Section 7.**  The computations reproduce, the quotient search is exhaustive,
and the lifts, Dirac repairs, and exact-cut assertions are sound.

For a standalone statement of Theorem 7.2, “the full reserved Moser two-shore
setting” must explicitly include the hypotheses used by the bilateral web
theorem: the two connected shores are anticomplete components behind the
displayed boundary, the displayed sets cover the graph, the side-specific
exposure sets are exactly the reserved ones, both shores are full to the five
root labels, and the established lower bound on shore order is available.
This is an imported-hypothesis clarification, not a mathematical defect in the
current application.

## 1. Independent replay

Compiling with

```text
c++ -std=c++20 -O2 moser_mixed_fan_crossing_verify.cpp
```

and running both modes reproduces

```text
checked 280 mixed-fan/opposite-crossing quotients; negative 8
checked 5000 three-fan/opposite-crossing quotients; negative 0
checked 120 remaining-pair/opposite-crossing quotients; negative 32 in profile types 02/13 13/24
```

The separate certificate replay prints

```text
verified 200 atomic fan/full-split K7 certificates
```

Thus all fifteen unordered pairs of the five ordinary profiles are covered:
five equal pairs by the 200 archived certificates, seven distinct singleton-
collision pairs by the 280-cell atlas, and the remaining three distinct pairs
by the 120-cell atlas.

## 2. Profile and frame mapping

The abstract-to-physical map

```text
(0,1,2,3,4) -> (0,5,2,4,6)
```

sends the five abstract present pairs

```text
02,03,13,14,24
```

to the five edges of the physical present cycle on
`U={0,2,4,5,6}`.  The program's order

```text
0,2,6,5,4
```

enumerates exactly the five frames formed by two disjoint edges of the
physical missing cycle.  For each frame, the four demanded labels are fixed
on the two carriers and the remaining root, `b`, and `w` are assigned in all
`2^3` ways.  Hence the covering-split enumeration is complete.

The ordinary/triple dichotomy is valid here: all five frames are crossless,
the simultaneous bare-web/portal-overlap result applies, and a removable fan
vertex has exactly three shore neighbours.  Relative seven-connectivity then
rules out root-profile sizes zero and one; an ordinary vertex has a present-
edge root profile and both reserved contacts, while every other possibility is
a triple lock.

## 3. Minor solver and lifting

For `n<=15`, `uint16_t` represents every vertex subset.  The C++ solver
enumerates every nonempty connected subset.  Its recursive candidate list is,
inductively, disjoint from and adjacent to every previously chosen bag; sorting
the subsets and taking only later candidates loses no unordered seven-tuple.
Consequently both its positive and negative answers are exhaustive.

Every helper vertex has a legitimate connected preimage:

* the fan vertices are singleton bags;
* the common body is the connected complement of the selected fan interval;
* the two crossing carriers extend to an adjacent connected bipartition of the
  opposite full shore; and
* all boundary and apex vertices are singleton bags.

Fullness supplies every conservative body or carrier contact used by the
quotient.  Surplus incidences may be deleted, so every computed model lifts.
The outer-corner edges are not used by the quotient certificates; they only
help certify the usual removable-fan geometry.

## 4. Dirac repairs

An ordinary fan vertex has degree exactly seven.  Dirac's contraction-critical
bound therefore gives `alpha(N(x))<=2`.

* For `P14`, the physical boundary neighbours are `{a,5,6,w}`.  Since
  `{a,5,w}` would be independent unless `aw` or `5w` is present, one of those
  two actual boundary edges is forced.  Each repairs all eight sparse cells.
* For `P13`, the physical boundary neighbours are `{a,4,5,w}`, with `45` the
  only edge among `{a,4,5}`.  Either `aw` is present, or both `4w` and `5w`
  are forced by the two independent-triple exclusions.  Both alternatives
  repair every one of the 32 sparse cells.

These are monotone additions of edges proved to occur in the original graph,
not hypothetical quotient edges.

## 5. Exact cuts and the bilateral alternative

For a triple lock with shield `s`, `D-x` is nonempty and connected and has
internal boundary `{x}`.  It has no `s`-contact.  Relative seven-connectivity
forces contacts with all other six boundary labels, proving

```text
N_G(D-x) = {x} union (L-{s}).
```

The opposite shore proves this is genuinely a cut.  For a one-vertex ordinary
fan, its three shore neighbours and four boundary neighbours are exactly its
seven neighbours, and the opposite shore again makes that neighbourhood a
genuine seven-cut.

If the fan has at least two vertices, any two consecutive vertices have a
connected common remainder by the interval-split lemma.  If the opposite shore
has a crossed frame, Theorem 6.2 applies.  If it has no crossed frame, the
current shore is already all-crossless by the Section 7 hypotheses, so the
bilateral all-crossless web theorem applies and six-colours the graph.  No
stronger connectivity than seven-connectivity is used.

