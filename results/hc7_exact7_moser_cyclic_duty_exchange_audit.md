# Independent hostile audit: Moser cyclic attained-duty exchange

Audited files:

- `results/hc7_exact7_moser_cyclic_duty_exchange.md`;
- `results/hc7_exact7_moser_alternating_cycle_probe.py`.

## Verdict

**GREEN.**  The normalized exact state, the reduction to eight literal
orientations, the three symmetry orbits, and both displayed literal
`K_7` models are correct.  The theorem closes every packet containing an
actual cycle through the six selected duty portals except the single orbit
represented by

\[
                         2,4,5,3,1,0.
\]

The conclusion is exactly local to that hypothesis.  It does not say that
the exceptional orbit is `K_7`-minor-free, and it does not turn an arbitrary
multi-attachment bridge into the required six-portal cycle.

## 1. Normalized state and attained duties

For the displayed Moser edge set, each of

\[
 A=\{2,3\},\qquad B=\{1,4\},\qquad D=\{0,5\}
\]

is independent, so
`Pi={A,B,D,{6}}` is a proper equality partition.  Its only singleton block
is `{6}`, hence `C={6}` is the required maximum singleton clique and

\[
                    d_H(\Pi)=4-1=3.
\]

The literal neighbourhood of `6` in the Moser boundary is `{1,2,5}`.  It
therefore meets `A`, `B`, and `D`, respectively at `2`, `1`, and `5`.
Consequently no retained singleton is added to any of the three duties:

\[
             D_{\Pi,C}(A)=A,\qquad
             D_{\Pi,C}(B)=B,\qquad
             D_{\Pi,C}(D)=D.
\]

Thus a cycle arc containing both selected portals of one displayed pair
really is a carrier for that exact attained duty; the proof does not replace
duty by an unconditional support count.

## 2. Cyclic reduction and all eight orientations

For two pairs of distinct marked vertices on a cycle, failure to alternate
is equivalent to the existence of vertex-disjoint cycle arcs joining the
two respective pairs.  The two arcs may be extended through the two
remaining open cycle intervals until a cycle edge has one end in each arc.
They remain disjoint, connected, and adjacent.  Hence the audited
attained-duty split theorem applies with the other full rich packet funding
the third duty.

If every two of the three duty pairs alternate, the two occurrences of
each duty are antipodal in the six-term cyclic word.  Starting at an `A`
portal and choosing the direction in which `B` precedes `D` gives

\[
                         A,B,D,A,B,D.
\]

No arbitrary permutation of the literal duties is needed for this
normalization; rotation and reversal suffice with the fixed names.

Writing a flip bit for the choice of the first literal in each of
`A,B,D` gives exactly eight orders.  Direct application of cycle rotation,
reversal, and

\[
                       \varphi=(1\ 2)(3\ 4)
\]

gives the following complete operation table.  Here `rot r` means rotate
the transformed six-tuple left by `r` positions.

| flip | representative | operation |
|---|---|---|
| `000` | `000` | identity |
| `001` | `000` | `phi`, reverse, `rot 4` |
| `110` | `000` | `phi`, reverse, `rot 1` |
| `111` | `000` | `rot 3` |
| `010` | `010` | identity |
| `101` | `010` | `rot 3` |
| `011` | `011` | identity |
| `100` | `011` | `rot 3` |

The map `phi` preserves every edge in the displayed Moser edge set, fixes
`0,5,6`, and interchanges the two blocks `A,B`.  It is used only as a
literal relabelling of the local certificate: it need not extend to an
automorphism of the ambient graph.  Fullness of all three packets and the
existence of the correspondingly relabelled portal edges are invariant
under that local relabelling.

This proves that the table in the theorem contains every literal
orientation and that its two exceptional flips form exactly one orbit.

## 3. Literal audit of the first `K_7` model

For order `(2,1,0,3,4,5)`, take

\[
 X=x_1Zx_4,\qquad Y=x_5Zx_0
\]

on the two complementary cycle arcs used in the proof.  Thus `X` contains
portals for `1,0,3,4`, while `Y` contains portals for `5,2`.  The seven bags
are

\[
 \{0\},\ \{3\},\ \{4\},\ X\cup\{1\},\
 Y\cup\{2,5\},\ P',\ Q\cup\{6\}.
\]

They are pairwise disjoint.  Each arc bag is connected through the portal
edge incident with each boundary vertex it absorbs; `P'` and `Q` are
connected packets, and `Q union {6}` is connected because `Q` is `S`-full.

All 21 required bag adjacencies split into the following exhaustive groups:

1. The three singleton bags form a triangle by `03,04,34`.
2. Each singleton sees `X union {1}` through the selected `0`, `3`, and `4`
   portal edges: three adjacencies.
3. Each singleton sees `Y union {2,5}` through `02,35,45`: three
   adjacencies.
4. The two arc bags see one another across either cut edge of the cycle.
5. Each of the five core bags contains a literal boundary vertex, so the
   `S`-full packet `P'` sees all five: five adjacencies.
6. The `S`-full packet `Q` likewise makes `Q union {6}` adjacent to all
   five core bags: five adjacencies.
7. Finally `P'` sees the literal `6` in the last bag: one adjacency.

The count is `3+3+3+1+5+5+1=21`, with no edge between the two open shores
being assumed.

## 4. Literal audit of the second `K_7` model

For order `(2,4,0,3,1,5)`, `X` contains portals for `2,4,0,3` and `Y`
contains portals for `1,5`.  The bags are

\[
 \{0\},\ \{3\},\ \{4\},\ X\cup\{2\},\
 Y\cup\{1,5\},\ P',\ Q\cup\{6\}.
\]

Connectivity and disjointness are identical to the first model.  The same
21-adjacency decomposition applies: the singleton triangle is unchanged;
the three singleton--`X` edges are supplied by the `0,3,4` portals; the
three singleton--`Y` edges are `01,35,45`; the two arc bags meet across a
cycle cut edge; fullness supplies the two groups of five adjacencies; and
the literal edge from `6` to `P'` supplies the last adjacency.

Thus both displayed models are literal models, not quotient models, and
they use the other rich packet and the thin packet in exactly the legal
way.  The branch bag `P'` is disjoint from the cycle packet `P`; the bag
`Q union {6}` is disjoint from both and repairs the otherwise absent
`P'--Q` shore adjacency through the literal vertex `6`.

## 5. Verifier coverage

The verifier builds exactly the 13-vertex local host consisting of the
seven Moser boundary vertices and a private six-cycle.  Portal vertex
`7+i` has the literal edge to `order[i]`.  For each of the eight flip
vectors it then:

- tries every boundary anchor;
- enumerates every nonempty connected vertex subset avoiding that anchor
  and containing at least one literal boundary vertex;
- exhaustively backtracks over five pairwise disjoint such subsets; and
- checks every pair of chosen subsets for a literal host edge.

Such a rooted `K_5` lifts with the two unused full packets: absorb the
reserved anchor into the thin packet, use the other rich packet as the
seventh bag, and use fullness for all core contacts and for the edge from
the other rich packet to the anchor.  Conversely, the script claims only
failure of this particular rooted-core search in the two exceptional
orientations; it does not claim absence of every possible ambient `K_7`
model.

An independent run completed with exit code zero and returned certificates
for flips

\[
 000,001,010,101,110,111
\]

and `None` exactly for `011,100`, followed by
`CERTIFIED six cyclic Moser orientations lift through two packets`.
Inspection of `connected_masks`, `neighbourhood`, and the ordered
backtracking shows that this is exhaustive on the stated 13-vertex host;
the neighbourhood test is safe because candidate masks are already
required to be disjoint.

## 6. Infinite-family scope

The proof uses only the two arcs of an actual cycle through the six
distinct selected portals.  Subdividing its edges merely lengthens those
arcs.  Chords, attached bridges, and unused packet vertices only add edges
or vertices and can be ignored.  Therefore the extension to every packet
containing such a cycle is exact.

The final bridge sentence must retain its stated hypothesis: a bridge and
a portal-tree path are covered only when their union supplies an actual
cycle through all six selected duty portals.  The result does not assert
that every multi-attachment bridge has this property.
