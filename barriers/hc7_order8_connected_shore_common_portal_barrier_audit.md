# Independent audit: connected-shore common-portal barrier

**Audit status:** separate internal mathematical and computational audit;
**GREEN**.

**Audited source:**
[`hc7_order8_connected_shore_common_portal_barrier.md`](hc7_order8_connected_shore_common_portal_barrier.md)

**Audited source SHA-256:**
`9f41a55d13b1db389d6f534ad9a27107cfaf877e0a3bcfa30bc677489308009d`

After this audit, the source status was changed only to record the GREEN
verdict and link to this file.  No refuted statement, construction,
colouring claim, proof, or scope changed.  The resulting promoted source
SHA-256 is
`f547fb1d71448b354daff1035c77e09263b17d44d38ed7775b285ca3fabb256a`.

**Audited verifier:**
[`hc7_order8_connected_shore_common_portal_barrier_verify.py`](hc7_order8_connected_shore_common_portal_barrier_verify.py)

**Audited verifier SHA-256:**
`68d546125433a25c165618b1162e581584f4f5daefab23fac01fed7b598e810a`

During the audit, the verifier was strengthened only to assert the displayed
`K_6` witness and to derive the boundary-component orders from `EDGES`
instead of listing them.  Its graph, response search, elimination
certificate, and output did not change.

This is an internal audit, not external peer review.  The example is a
barrier to one proposed connected-shore response implication, not a
counterexample to `HC_7`.

## Verdict

The construction satisfies every hypothesis in the displayed refuted
statement, realizes the equality response, and does not realize the unequal
response.  The closed shore is exactly six-chromatic, has treewidth five,
and has no `K_7` minor.  Its stated trust boundary is exact.  No
mathematical or computational gap was found within that scope.

## 1. Construction and portal data

The eight boundary vertices split as claimed into the independent nonempty
sets `P={p1,p2,p3}` and `R={r1,r2,r3}` together with the nonadjacent roots
`d,e`.  The boundary edges are exactly two disjoint triangles

```text
d-p1-r1-d    e-p2-r2-e,
```

with `p3,r3` isolated in the boundary.  Thus there is a `P`--`R` edge, and
each root has a neighbour in both classes.

The open shore `H={a,b,c}` is a triangle complete to the boundary.  Hence
it is connected; `Q0={a}` and `Q1={b}` are disjoint connected `S`-full
subgraphs; and

```text
N(d) intersect Q1 = N(e) intersect Q1 = {b}.
```

This is exactly the singleton common-portal hypothesis, with no quotient or
implicit contact convention involved.

## 2. Exact boundary responses

For `P | R | {d,e}`, assign colours `0,1,2` to the three boundary blocks.
Both boundary triangles are proper.  Since `H` is complete to `S`, its
three vertices must and can receive the three remaining colours.  Thus the
equality response extends.

For `P | R | {d} | {e}`, the partition itself requires `d` and `e` to have
different colours.  The `P`--`R` edge separates the first two block
colours, and the neighbours of each root in both classes separate each root
colour from both block colours.  The boundary therefore uses four distinct
colours.  Every vertex of the triangle `H` is adjacent to every boundary
vertex, so extending the partition would require three further colours,
seven in total.  The unequal response cannot extend with six colours.

The verifier's canonical fixed labels lose no cases: any colouring inducing
one of the prescribed equality partitions is equivalent under a colour
permutation to the labels fixed in `extends`.  Its exhaustive `6^3`
assignments on `H` find the equality response and reject the unequal one.

## 3. Chromatic and minor bounds

The six vertices `H union {d,p1,r1}` induce a `K_6`, while the equality
response supplies a proper six-colouring.  Therefore the closed shore has
chromatic number exactly six.

The boundary `2K_3 dotcup 2K_1` has treewidth two.  Adding `a,b,c` to every
bag of a width-two boundary decomposition yields bags of order at most six,
so the closed shore has treewidth at most five.  The displayed `K_6` gives
the reverse inequality, hence its treewidth is exactly five.  Treewidth is
minor-monotone, and every graph of treewidth at most five is six-colourable.
Consequently every minor of this graph is six-colourable and a `K_7` minor
is impossible.

The direct branch-set proof is also sound.  Pairwise disjoint branch sets
meeting the three vertices of `H` number at most three.  A hypothetical
`K_7` model would therefore leave at least four branch sets wholly in the
boundary, where they would form a `K_4` minor.  Every connected boundary
branch set lies in one component, and pairwise adjacent such branch sets
must lie in the same component; no boundary component has more than three
vertices.  This is a contradiction.

## 4. Verifier check

The verifier constructs exactly the graph above, checks the boundary
partition hypotheses, universal boundary contacts, singleton portal, both
response outcomes, the displayed `K_6`, and the boundary-component orders.
Its explicit fill calculation gives the later-neighbour counts

```text
d:5 e:5 p1:4 p2:4 p3:3 r1:3 r2:3 r3:3 a:2 b:1 c:0,
```

so the recorded elimination order has width five.  This executable
certificate establishes the advertised treewidth upper bound; the derived
component orders independently support the direct branch-set proof.

The audited command

```text
python3 barriers/hc7_order8_connected_shore_common_portal_barrier_verify.py
```

returned exactly

```text
GREEN connected-shore common-portal barrier
closed shore: K3 join (2K3 plus 2K1), chromatic number 6
responses: equality=yes unequal=no
minor scope: elimination width 5; every minor is six-colourable
trust boundary: not seven-connected or contraction-critical
```

The same output and verdict were reproduced with Python hash seeds `0`,
`1`, `17`, and `12345`.

## 5. Trust boundary

Deleting the three vertices of `H` disconnects the boundary, so the example
is not seven-connected.  It is six-chromatic rather than seven-chromatic.
It is not contraction-critical: for example, deleting `p3` leaves the
displayed `K_6` and hence leaves chromatic number six.

Thus the graph does not meet the host hypotheses of a hypothetical
minor-minimal counterexample to `HC_7`.  It refutes only the direct attempt
to replace two anticomplete boundary-full components in the componentwise
completion argument by two disjoint boundary-full subgraphs inside one
connected shore.  The source claims no broader consequence.
