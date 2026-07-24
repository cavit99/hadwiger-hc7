# Internal audit: order-eight near-full census and three-colourful-set route

**Verdict:** **GREEN within the stated diagnostic scope.**

This is an internal audit, not external peer review.  It checks the following
exact revisions:

| file | SHA-256 |
|---|---|
| `hc7_p2_nearfull_bipartition_census.py` | `20308f71f9b010d286db480c23227e78d724ef94b9583fe7fe679d464f250f65` |
| `hc7_p2_nearfull_bipartition_census.md` | `e160ef08ccc29e54126f206c60ec71c55f568f68a21b0618b02c0a6205d09fc8` |
| `hc7_three_colourful_sets_route_assessment.md` | `381a9c8749c8b20013ab0a119cbaed2aad6a203639499f43956c66b63bb65069` |

## 1. Finite census

I reran the program with Python 3.14.6 and nauty 2.9.3.  Its asserted output
was reproduced exactly:

```text
graphs=12346
eligible_graphs=10460
eligible_instances=469852 by_miss_count={0: 10460, 1: 117796, 2: 341596}
incompatible_instances=209246 by_miss_count={0: 2514, 1: 39742, 2: 166990}
k4_minor_free_eligible_graphs=1116
k4_minor_free_eligible_instances=18844 by_miss_count={0: 1116, 1: 6446, 2: 11282}
k4_minor_free_incompatible_instances=520 by_miss_count={0: 0, 1: 0, 2: 520}
```

The implementation matches the finite universe stated in the companion
note.  It:

1. enumerates the 12,346 unlabelled order-eight graph representatives from
   `geng -q 8`;
2. retains precisely those representatives with independence number at most
   four and chromatic number at most four;
3. enumerates every proper surjective five-colouring as a five-block
   restricted-growth partition;
4. permits a non-full miss precisely when it lies in a non-singleton block
   of one such colouring, requires two non-full misses to be distinct, and
   then applies the two displayed deletion-independence tests;
5. searches every deletion set of order zero, one, or two and every
   componentwise orientation of the remaining bipartite graph; and
6. tests exactly the endpoint-avoidance and nonempty-class conditions stated
   in the note.

The recursive deletion/contraction `K_4`-minor test was also compared on all
12,346 representatives with the independent connected-branch-set search in
`hc7_order8_k4minor_oct_certificate.py`; there were zero disagreements.

Accordingly, `520` is the exact count for the implemented marked static
universe.  The note correctly says that it is a count of ordered marked pairs
on chosen unlabelled representatives, not an orbit count or a labelled-graph
count.

## 2. Literature route

The three-set incidence requirement is exactly a rainbow `K_4` colorful
minor after annotating vertices by membership in the three sets: each of the
four branch sets must contain all three annotations.

The cited primary statements were checked directly:

- Martinsson--Steiner, Theorem 1.3, gives one `S`-rooted `K_4` minor when
  `chi(R)=4` and `S` is colourful.  Applying it separately to three sets does
  not synchronize the three models.
- Fabila-Monroy--Wood, Theorem 6, gives the rooted-`K_4`/planar-common-face
  dichotomy for four nominated vertices in a four-connected graph.  The
  proposed `R` is five-connected, but the theorem controls four nominated
  vertices, not twelve set-incidence requirements.
- Protopapas--Thilikos--Wiederrecht, full-version Theorem 3.1, assumes a
  specified `K_k` minor with
  `k >= floor(3qt/2)+t` and returns either a rainbow `K_t` or a set of order
  at most `qt-1` whose clique-model-big component is restricted.  Thus
  `(q,t)=(3,4)` requires `k>=22` and permits order 11, while `(2,4)` requires
  `k>=16` and permits order 7.  The route assessment states these constants
  and the hypothesis mismatch correctly.

## 3. Trust boundary

Neither document proves an unbounded host-graph theorem.  In particular,
the census does not prove that any of its 520 marked configurations is
realizable by an operated shore, nor that host geometry eliminates them.
The literature assessment does not supply operation provenance, a strict
same-host component descent, or an exact-seven response.  Its conclusion is
only that the cited standard theorems do not presently close the desired
three-annotation synchronization step.
