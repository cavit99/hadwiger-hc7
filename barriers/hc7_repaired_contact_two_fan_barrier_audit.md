# Independent audit: repaired-contact two-fan barrier

## Audit identity

- barrier statement:
  `barriers/hc7_repaired_contact_two_fan_barrier.md`
- audited statement SHA-256:
  `af1d21098dda6cfc8be63df1a0a6ff159933daa8ce07a295cbcdde82579ef478`
- verifier:
  `barriers/hc7_repaired_contact_two_fan_barrier.py`
- audited verifier SHA-256:
  `a0e32dedc4d1b48a618966464f1204990a6dd0b3032c1d7fcbdfcee28c65c11a`
- imported exact detector:
  `results/hc7_disjoint_k6minus_six_terminal_crossing_decoder.py`
- imported detector SHA-256:
  `02a37655bb2c3e4ef2a5b125deecaac41431530e7cfe5a921616406e45095b81`

## Verdict

**GREEN.**  The displayed construction is an infinite family of
`K_7`-minor-free graphs for every integer `k>=1`, in each of the seven
listed parameter choices.  For `k>=5`, both outside singleton components
have exactly `k+2>=7` distinct neighbours on the linkage skeleton.  In six
of the seven choices both components attach to at least two distinct
linkage paths; the seventh choice is correctly retained only as a symmetry
case.  The completed-core checks are exact, and the written triangle
clique-sum argument proves the unbounded conclusion without extrapolating
from the finite replay.

The statement refuted is exactly the local attachment-count implication in
Section 3.  These graphs are neither seven-connected nor
seven-contraction-critical, so they are not counterexamples to `HC_7` and
do not refute any proposed theorem that uses the full minimal-counterexample
hypotheses.

This is an independent internal audit, not external peer review.  No source
or verifier content was changed during the audit.

## 1. Reconstruction of the family

The imported normalized graph has twelve distinct vertices and six
pairwise vertex-disjoint linkage edges

\[
 a_0b_0, a_1b_1, a_2b_2, a_3p, xq, yr.
\]

The verifier fixes the first selected linkage path as `P0=a0b0`, which is
legitimate under the simultaneous symmetry of `P0,P1,P2`.  In every listed
case the second selected path is one of `P3,P4,P5`, so the two selected
paths are distinct.  Replacing each selected edge by a path with `k`
internal vertices therefore gives two disjoint sets of exactly `k`
internal vertices.

The new vertices `c,d` are distinct and nonadjacent.  After deleting the
linkage skeleton they are two singleton components.  Their skeleton
neighbourhoods are exactly

\[
 N_\Sigma(c)=\{a_3,x\}\mathbin{\dot\cup}I_0,
 \qquad
 N_\Sigma(d)=\{y,z\}\mathbin{\dot\cup}I_j,
\]

where `I0` and `Ij` are the two sets of internal subdivision vertices.
The two displayed fixed vertices are distinct and are not internal
subdivision vertices.  Thus both neighbourhoods have exactly `k+2`
vertices, proving the claimed threshold at `k>=5`.

The component containing `c` attaches to `P0,P3,P4` in every row.  The
paths met by the component containing `d` are as follows:

| `z` | selected path | linkage paths met by `d` |
|---|---|---|
| `p` | `P3` | `P3,P5` |
| `p` | `P5` | `P3,P5` |
| `q` | `P4` | `P4,P5` |
| `q` | `P5` | `P4,P5` |
| `r` | `P3` | `P3,P5` |
| `r` | `P4` | `P4,P5` |
| `r` | `P5` | `P5` |

Consequently the first six rows satisfy the asserted two-path stability
incidence for both outside components.  The final row does not, and the
source explicitly does not claim that it does.

In all seven rows, `a3-c-x` and `y-d-z` are paths.  Their internal vertices
are outside the linkage skeleton and the two paths are internally disjoint.
Hence they have exactly the repaired-contact interpretation asserted in the
barrier.

## 2. Completed cores and exact finite verification

For each row the completed core restores the two selected linkage edges,
adds `c,d`, joins each centre to both endpoints of its selected linkage
edge, and retains the four fixed contact edges.  This is precisely what
`completed_core` constructs.  Endpoint coincidences cause only duplicate
set insertions: for example, when `z=p` and the selected path is `P3`, the
edge `dp` is both a fixed contact and a triangle edge.  No required edge is
lost and no unintended vertex identification occurs.

I ran the verifier from the repository root.  It terminated without an
assertion and printed exactly

```text
completed_cores 7
finite_family_replay 49
GREEN: all two-fan cores and replay members are K7-minor-free
```

Thus it checks all seven fourteen-vertex completed cores and all lengths
`1,...,7` in every family.  The output is deterministic: the script has no
random input, and set iteration can affect only search order, not the three
fixed output lines.

As an independent implementation cross-check, I converted each completed
core to NetworkX and ran
`results/hc7_disjoint_k6minus_support6_linkage_classifier.py`'s separately
promoted low-degree/exact branch-set detector.  It also returned `False` on
all seven cores.

## 3. Correctness and completeness of the imported detector

For a graph of order at most twelve, seven nonempty branch sets force at
least `14-n` singleton branch sets.  The imported detector iterates over
every possible exact number of singleton bags from seven down to that
minimum.  It tests every singleton clique, enumerates every connected
nonsingleton candidate adjacent to all singleton bags, and recursively
chooses every possible family of pairwise disjoint and pairwise adjacent
candidates.  Unused vertices are permitted.  The candidate-size bound only
reserves two vertices for every other nonsingleton branch set, so it cannot
discard a valid model.

Above twelve vertices the detector chooses a vertex `v` of degree below
six and uses the exact recurrence

\[
 K_7\preccurlyeq H
 \Longleftrightarrow
 K_7\preccurlyeq H-v
 \quad\text{or}\quad
 K_7\preccurlyeq H/vw\text{ for some }w\in N_H(v).
\]

The forward implication holds because `v` cannot be a singleton branch
set of a `K_7` model: such a bag would require six distinct neighbours.  If
`v` lies in a nonsingleton connected bag, that bag contains an incident
edge `vw`, which may be contracted.  The reverse implication is immediate
from minor transitivity.  The deletion, contraction and normalization
routines remove loops, preserve all other adjacencies, and strictly reduce
the order.  The verifier's successful assertion-bearing replay also checks
that every graph above order twelve reached in these calls has a vertex of
degree below six, the explicit precondition enforced by the detector.

Therefore every negative finite answer used here is exact.  The detector
is not being treated as an oracle outside the domain on which its asserted
low-degree recurrence is available.

## 4. Uniform clique-sum proof

Fix one completed core.  For the first selected linkage edge `uv`, add the
subdivided `u`--`v` path and all edges from its centre `c` to the internal
vertices while retaining the triangle `cuv`.  This summand is a wheel:
its rim is the subdivided path together with `uv`, and `c` is adjacent to
every rim vertex.  It is planar and hence `K_7`-minor-free.  The wheel and
the completed core meet exactly in the clique `\{c,u,v\}`.  The same
construction with `d` and the other selected edge gives a second planar
wheel whose adhesion triangle is disjoint from the first one.

It remains to justify that a `K_7` model cannot straddle either triangle
clique-sum.  At most three of its pairwise disjoint branch sets can meet an
adhesion triangle.  Every other branch set lies in one open side, and
branch sets cannot occur in both open sides because opposite open sides
have no edge between them.  Hence all branch sets avoiding the adhesion lie
on one side.  Restrict each adhesion-meeting bag to that side together with
the adhesion vertices it contains.  These restricted bags remain
connected because the adhesion is a clique; they remain pairwise adjacent
for the same reason, and every adjacency to a bag avoiding the adhesion was
already on the chosen side.  This would give a `K_7` model in one summand.
Thus a triangle clique-sum of two `K_7`-minor-free graphs is
`K_7`-minor-free.

Applying this argument twice shows that the supergraph formed from the
completed core and the two wheels has no `K_7` minor for every `k>=1`.
The graph in Section 1 is a subgraph of this supergraph: delete each direct
selected linkage edge and any added centre--endpoint triangle edge that is
not already one of the required fixed contacts.  When a fixed contact and
a triangle edge coincide, retain it.  Since taking a subgraph cannot create
a minor, every displayed family member is `K_7`-minor-free.  This proves
the infinite claim independently of the seven-length computational replay.

## 5. Exact scope

The construction disproves the following implication after stripping away
all other hypotheses:

> two disjoint outside components supplying the two named repaired-contact
> paths, each with at least seven (or arbitrarily many) distinct skeleton
> attachments, force a `K_7` minor.

The six robust rows further disprove the same implication after requiring
each component to meet at least two distinct linkage paths.  They show that
large attachment cardinality and stable-bridge incidence do not by
themselves overcome a fan concentrated behind a triangle.

The construction does **not** establish any of the following:

- a seven-connected graph with this obstruction;
- a seven-contraction-critical graph with this obstruction;
- a counterexample to `HC_7`;
- failure of a theorem using the additional edges forced by minimum degree
  or contraction-critical colouring transitions; or
- failure of a conclusion that allows a global fixed two-vertex
  transversal instead of demanding a local `K_7` model.

The source states these limitations accurately.
