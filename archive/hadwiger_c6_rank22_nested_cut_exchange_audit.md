# Independent audit: rank-two pole orientation and exact-cut descent

## Verdict

**GREEN.**  Lemmas 2.1--2.4 and 3.1--3.2, together with Corollaries
3.3--3.4 in `hadwiger_c6_rank22_nested_cut_exchange.md`, are valid under
their stated canonical contact rows.  The result is a genuine arbitrary-
order labelled rerouting/descent theorem.  It does not close the whole
`C6 dotunion K1` cell because the high-owner shore need not be the globally
minimum old shore.

## 1. No R-torso hypothesis is hidden

Let `A` be any component of `D-{p,q}`, where `D` is two-connected.  Both
poles meet `A`; otherwise the other pole is a cutvertex.  In

\[
                     D[A\cup\{p,q\}]+pq
\]

deleting an internal vertex leaves every remaining component incident
with at least one pole, and the virtual edge joins the poles.  Deleting a
pole leaves connected `A` attached to the other pole.  Hence this completed
bridge is two-connected regardless of its SPQR node type.

Two-set Menger therefore gives two disjoint paths from the two distinct
portal representatives to the two poles in some order.  Shortening at the
first pole removes every possible use of the virtual edge.  Equal orders on
the two anticomplete interiors glue at `p` and `q` to the forbidden
antipodal linkage.  This proves the unique opposite bits in Lemma 2.1.
The two pin implications in Lemma 2.2 then follow by adjoining the named
pole incidences to those literal paths.

## 2. Four-class Hall and rooted completion

For a Hall-deficient subfamily of `r` among the four `A`-portal classes,
its union has order at most `r-1`.  A component outside that union has all
neighbours in the union, the two poles, `z`, and the `4-r` omitted cycle
labels: at most six vertices.  Seven-connectivity therefore forces the
whole side to equal the deficient union and have order at most three.

If the completed bridge has the four-rooted `K4`, a virtual `pq` use
expands through connected `B`: add an entire `p-q` path to one branch bag,
or split it at an edge between the two branch bags.  Attaching boundary
roots `c0,c2,c3,c5`, and then adding the bags `H`, `{z}`, and `{c1,c4}`,
gives seven literal clique bags.  The pair `c1c4` is a boundary edge and
dominates the four selected roots in the complement-of-`C6` boundary.

## 3. Uniform two-gate descent and both nested cuts

Theorem 3.0 is valid at arbitrary connectivity `k`.  The two poles meet
both interiors by two-connectivity of the old shore.  A row of order
`k-2`, together with the poles, is therefore the exact neighbourhood of
its interior.  The two old boundary vertices outside that row attach to
the opposite interior by hypothesis and to the old full shore, making the
new far side connected.  Old boundary cut vertices see the full shore and
the poles see the opposite interior, so both new shores are full.  No
property of the `C6` labels is used in this step.

The canonical rows give

\[
N(A)=\{p,q,c_0,c_2,c_3,c_5,z\},\qquad
N(B)=\{p,q,c_1,c_2,c_4,c_5,z\}.
\]

For the first cut the other component is connected through
`B,c1,c4,H`; for the second it is connected through `A,c0,c3,H`.
The poles meet both interiors, and every retained old boundary vertex sees
the old full shore.  Thus both cuts have order seven and both sides are
full.  Since `|A|+|B|=|D|-2`, the smaller is at most `(|D|-2)/2`.

## 4. Minimum-fragment scope

If `D` is globally minimum among exact-seven fragments, either nested cut
contradicts minimality.  This does **not** follow merely because the other
old shore `H` is globally minimum: frame ownership can select the larger
shore as high owner.  In that orientation global minimality only gives

\[
                       |D|\ge 2|H|+2.
\]

Accordingly the theorem supplies exactly the “smaller exact adhesion”
outcome requested of a simultaneous-web exchange, but further state
transport is still needed when the high owner is the larger old shore.

## 5. Audit of transverse capacity and operation states

### Verdict

**GREEN AS PATCHED.**  Lemmas 5.1 and 5.2 are correct.  The source now
explicitly says that the two deletion witnesses may induce the same boundary
equality partition; no distinction or mutual incompatibility of
`Pi_0,Pi_1` follows.  The state-strictness and Kempe-switch part is a direct
specialization of `hadwiger_bad_split_interface_exchange.md`, while the
capacity bound and simultaneous transverse placement are new to the
canonical rank-two geometry.

### Degree and interface count

For a pole `p`, the canonical row permits old-boundary neighbours only in
`{c2,c5,z}`, exactly `3-r_p` of them.  There are no edges from `p` to the
old opposite shore.  Its remaining neighbours lie in `A`, `B`, and possibly
at `q`, so

\[
d_A(p)+d_B(p)+(3-r_p)+\epsilon=d_G(p)\ge7.
\]

This is precisely (5.5), and the analogous inequality for `q` gives

\[
m_0+m_1=d_A(p)+d_B(p)+d_A(q)+d_B(q)+2\epsilon
        \ge8+r_p+r_q.
\]

There are no omitted `A-B` interface edges: `A,B` are different components
of `D-{p,q}`.  Hence (5.2) counts each interface exactly.

Both poles meet both components by two-connectivity.  In allocation zero,
one edge of `p-B` and one of `q-A` are vertex-disjoint; in allocation one,
one edge of `p-A` and one of `q-B` are vertex-disjoint.  Thus both interfaces
really contain a two-matching, not merely two edges.  If all four shared
contacts in (5.4) existed, the two opposite pin patterns of Lemma 2.2 would
both hold.  Therefore `r_p+r_q>=1`, and integrality of the displayed sum
puts at least five edges in one interface.

### Geometry-preserving deletions

Choose `e0` in `p-B` and `e1` in `p-A`.  They are distinct.  Deleting `e0`
does not alter either induced piece `A+p` or `B+q`; an edge of `q-A`
remains across the split.  Deleting `e1` analogously leaves an edge of
`q-B`.  Since deleted edges have no boundary endpoint, both contact rows
remain exactly `S-M1` and `S-M0`, and their union still covers `S`.

### Strict states and Kempe alternative

Proper-minor minimality gives a six-colouring of each `G-e_i`.  The two ends
of `e_i` must share one colour, or the edge could be restored.  Restriction
to `S` is realized by both the operated shore and the unchanged opposite
shore.  If the same labelled equality partition extended over the original
shore, a palette permutation would align the two boundary colourings and
six-colour `G`; hence each witness is strict against `D`.

For another colour `gamma`, take the two endpoint components in the
`alpha_i/gamma` subgraph of `G[D]-e_i`.  If they differ and one has no
`alpha_i`- or `gamma`-coloured neighbour in `S`, switching that entire
component preserves every boundary edge and allows `e_i` to be restored.
Thus either there is an internal bichromatic endpoint path or both endpoint
components are boundary-anchored.  This is exactly the already-audited
bad-split interface exchange.

### Novelty boundary

Section 5 materially advances the *static canonical package* by proving the
sum bound (5.3), a two-matching in both transverse allocations, an interface
of order at least five, and two geometry-preserving deletions placed on
opposite sides of the same pole.  It does not establish a new colouring-
state exchange theorem beyond `hadwiger_bad_split_interface_exchange.md`:
strictness and the Kempe dichotomy are inherited verbatim, and there is no
proved relation between the two resulting states.  The remaining advance
must compare or compose `Pi_0` and `Pi_1`, rather than merely produce them.

## 6. Audit of the coupled star and six-gate localization

### Verdict

**GREEN AS PATCHED.**  Lemmas 5.3--5.5 are correct.  The source was patched
to distinguish neighbours in the operated graph from the two deleted star
edges, and to say explicitly that the alpha “warehouse” is only a set of at
most three vertices—not a three-route or three-representative capacity
statement.  The anchors in Lemma 5.5 are palette-labelled, not portal-
labelled, and therefore do not yet activate Lemma 2.4.

### Coupled star lock

The leaves `a in A` and `b in B` are nonadjacent because `A,B` are distinct
components of `D-{p,q}`.  Contracting `pa,pb` gives a proper minor; expanding
a six-colouring deletes exactly those two edges and makes `p,a,b` one colour
`alpha`.  Every vertex outside the contracted star adjacent to any star
vertex is adjacent to its image in the minor and therefore avoids `alpha`.

For each other colour, switching both leaf components when neither contains
`p` restores both deleted edges, proving support through at least one leaf.
For colours supported exclusively on opposite leaves, simultaneous switches
are proper unless the two unsupported components share an alpha vertex or
have a beta-gamma cross-edge.  The exclusive sets partition the only possible
failure of a common supporting leaf: if one exclusive set is empty, the
opposite leaf supports all five palettes; if both are nonempty, the complete
cross-interaction follows pair by pair.

### Localization at the six-gate adhesions

The exact neighbourhoods are

\[
N_G(A)=\{p\}\dot\cup T_A,qquad
N_G(B)=\{p\}\dot\cup T_B.
\]

For `beta in E_B`, the full Kempe component `K_beta(a)` contains `a` but
not `p`.  If it also misses `T_A`, it cannot leave `A`: every first exit
would be a vertex of `{p} union T_A` in the same component.  The symmetric
statement holds for `K_gamma(b)`.  If failures occurred on both sides, the
two selected components would lie in anticomplete `A,B`, contradicting the
coupled cross-interaction.  Therefore one entire exclusive family meets its
named six-vertex gate.  This localizes one side of the grid; it does not put
all interaction vertices or both exclusive families into one adhesion.

### Palette anchors and the alpha bound

Every gate vertex in `K_beta(a)` has colour `alpha` or `beta`.  If it has
colour `beta`, different palettes automatically give distinct gate vertices.
Otherwise the component meets `Z_alpha`.

Among the old boundary vertices of `T_A`, `z` is universal.  On
`{c0,c2,c3,c5}` the only missing edges are `c0c5` and `c2c3`, so an
independent colour class has order at most two; the additional vertex `q`
raises this by at most one.  Hence `|Z_alpha|<=3`.  The symmetric `T_B`
calculation is identical.

The bound controls only the cardinality of the shared alpha gate.  Many
different bichromatic components may meet the same alpha vertex, and the
colour-labelled representatives need not represent distinct portal classes.
Accordingly Lemma 5.5 supplies neither a colourful rooted `K4` nor a
capacity-three linkage without an additional palette-to-portal alignment
theorem.
