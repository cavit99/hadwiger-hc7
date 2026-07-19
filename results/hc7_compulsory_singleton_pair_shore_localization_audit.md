# Independent audit of shore localization for a compulsory singleton pair

**Verdict: GREEN.**

This is a separate internal mathematical audit of the complete source file
[`hc7_compulsory_singleton_pair_shore_localization.md`](hc7_compulsory_singleton_pair_shore_localization.md)
at SHA-256

```text
6f0373f5186142ba89fd26ba9ea40d21d973ecb72caea7f3b5f972669d767ec5
```

The pre-promotion source SHA-256 was

```text
76ba73c230ada451a644aca390ce8a77c09b96a6b80949e2414502c4ac8704af
```

Promotion changed only the opening status paragraph, replacing the pending
audit marker by a link to this GREEN audit.  The hypotheses, both localization
alternatives, the exceptional multiplicity classification, the reflected
completion theorem, and all trust-boundary statements are unchanged.  This
audit therefore binds the same mathematical revision at its promoted path
and current hash.

The repaired source explicitly assumes that every proper minor of `G` is
six-colourable.  That hypothesis is essential for its invocation of exact
response reflection.  The source also explicitly assumes `ab in E(G)`,
which is used only to join the two labelled paths in the exceptional
placement.  No unresolved gap was found in either theorem at this revision.

## 1. Dependencies and orientation

The Hall-theoretic input is the separately audited two-response
compulsory-label theorem.  In the centre placement it supplies:

* boundary vertices `a,x_A` in branch set `A` and `b,x_B` in branch set
  `B`;
* distinct untouched colours on `x_A,x_B`;
* the three possible boundary-label multiplicity patterns
  `(2,2,1,1,1)`, `(2,2,2,1)`, and `(3,2,1,1)`; and
* a boundary colour partition with one block of order two and five
  singleton blocks.

For Theorem 3.1, the separation is oriented with open shores `R` and `D`.
The equality `S=N_G(D)` implies that there are no `D`--`R` edges.  The
response colouring restricted to `G[R union S]` is proper because its only
two deleted edges are `va,vb`, both between `D` and `S`.  The newly stated
proper-minor hypothesis is exactly the remaining assumption required by
the audited exact-response-reflection theorem.

## 2. Exceptional label-count classification

The vertices `a,b` use the two operated colours and are singleton blocks.
The vertices `x_A,x_B` use distinct untouched colours, so at most one can
belong to the unique two-vertex block `I`.

If a singleton among `x_A,x_B` belongs to an operated label of multiplicity
two, that label has exactly the two boundary vertices asserted in conclusion
1.  This covers both operated labels in the first two multiplicity patterns,
and also covers the `(3,2,1,1)` pattern unless the tripled label is one of
`A,B` and the vertex in the other, doubled label lies in `I`.

Consequently, failure of conclusion 1 forces, up to symmetry:

```text
A has multiplicity three,
B has multiplicity two,
x_A is a singleton block,
x_B lies in I.
```

The four untouched-colour representatives consist of `x_A,x_B` and two
vertices of two further distinct labels.  Together with `a,b`, these account
for six boundary vertices.  The seventh vertex is the third occurrence of
label `A`.  Since `x_B` is already in the unique repeated-colour block, that
seventh vertex is its other member.  Naming it `y_A` gives exactly

```text
S cap A = {a,x_A,y_A},
S cap B = {b,x_B},
I = {x_B,y_A}.
```

Thus the crossed `(3,2,1,1)` placement is exhaustive and is incompatible
with conclusion 1.  The two alternatives in Theorem 2.1 are mutually
exclusive and exhaustive; the statement does not claim uniqueness of the
choice of label when conclusion 1 holds.

## 3. Localization of the labelled paths

In conclusion 1, the relevant branch set `L` is connected and has exactly
the two boundary vertices `p,x_L`.  A shortest `p`--`x_L` path in `G[L]`
therefore has no internal boundary vertex.  Its internal vertices, when
nonempty, form a connected subgraph of `G-S` and hence lie in one component
of `G-S`.

That component cannot be `D`.  If the first internal vertex `w` lay in
`D`, then `pw` would survive in the common-deletion graph: the only deleted
edge incident with `p` is `pv`, while `v` lies in the disjoint singleton
root branch set and hence cannot be a vertex of the path in `L`.  Both `p`
and `w` have one of the two switched colours.  The surviving edge `pw`
would therefore place `p` in the same bichromatic component `D`, contrary
to the centre placement.  The internal component is consequently contained
in `R`.

The exceptional placement admits two paths by the same argument:

* because `S cap B={b,x_B}`, a shortest `b`--`x_B` path in branch set `B`
  has all internal vertices in `R`;
* in branch set `A`, a shortest path from `a` to the set `{x_A,y_A}` stops
  at the first of those two boundary vertices and therefore has no internal
  boundary vertex; the common-deletion component argument again puts all
  internal vertices in `R`.

The two paths are vertex-disjoint because the labelled branch sets `A,B`
are disjoint.  Their `a` and `b` ends are adjacent by the separately assumed
edge `ab`.  This proves exactly the strengthened exceptional conclusion; it
does not assert any additional cross-contact between their interiors.

## 4. Carrier-system reflection for `r=1,2`

Suppose first that `px` is an edge.  The clique `U` has order `5-r`, avoids
`x`, contains `p`, and every other vertex of `U` is adjacent to `x`.
Therefore `U union {x}` is a clique of `6-r` singleton blocks.  Since `Pi`
has six blocks, exactly `r` blocks remain.  Assigning one of the pairwise
disjoint boundary-full connected subgraphs `F_i` to each remaining block
gives the required partition-specific carrier system relative to
`U union {x}`.

If `px` is not an edge, the internal vertex set `Z` of the path is a
nonempty connected subgraph of `R`, disjoint from every `F_i`.  Assign `Z`
to the singleton block `{x}`.  The set `Z union {x}` is connected, is
adjacent to `p` through the first path edge, and is adjacent to every member
of `U-{p}` through the stipulated boundary edges at `x`.

The block count is exact:

```text
6 - |U| - 1 = r.
```

For `r=1`, the only further block is `I`.  For `r=2`, the further blocks are
`I` and the one singleton block outside `U union {x}`.  Boundary fullness of
the `F_i` makes each assigned block union connected, supplies all pairwise
adjacencies among assigned unions, supplies their adjacencies to
`Z union {x}`, and supplies all their adjacencies to `U`.  Hence the stated
`r+1` connected subgraphs satisfy every carrier-system condition.

The exact-response-reflection theorem can now be applied on the `R` shore:
the explicit proper-minor hypothesis supplies the six-colouring after the
carrier contractions.  It returns a proper colouring of `G[D union S]`
with exactly the same boundary partition.  A permutation of colour names
then aligns it with the already proper colouring of `G[R union S]`, and the
two shore colourings glue.

## 5. Trust boundary

The audited source proves a host-level localization of the compulsory
same-label pair and a sufficient, partition-specific reflection criterion.
It does **not** prove any of the following:

* that conclusion 1 always holds rather than the crossed tripled-label
  alternative;
* that the localized path avoids a maximum family of boundary-full
  connected subgraphs;
* that the clique `U` or the required contacts from `x` always exist;
* that the two paths in the exceptional placement themselves form a
  carrier system or an explicit `K_7`-minor model;
* that an order-seven separator with a common boundary partition or a
  strict label-preserving descent always follows; or
* that `HC_7` is proved.

Within the exact centre-placement, Hall-core, proper-minor-colourability,
critical-triangle edge, and carrier-system hypotheses stated in the source,
the conclusions are valid.
