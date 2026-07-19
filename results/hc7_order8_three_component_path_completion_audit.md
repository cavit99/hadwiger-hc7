# Independent audit: completing two path-component configurations at an order-eight boundary

**Verdict:** **GREEN** for Lemma 1.1, Theorem 2.1, Corollary 2.2,
Lemma 3.1, and Corollary 3.2 at the exact revision below.  This is a
separate internal audit, not external peer review.  The result closes only
the path configurations stated in the source and does not prove `HC_7`.

## Audited revision

- theorem note:
  [`hc7_order8_three_component_path_completion.md`](hc7_order8_three_component_path_completion.md)
- theorem SHA-256:

  ```text
  a9e4e17e5a66fc9767388f7983607cce9b68393a83189f2e6aad4583f96a4570
  ```

The complete theorem note was checked line by line.  An earlier audit found
two statement-scope omissions: the anchors in Lemma 3.1 were not explicitly
typed as vertices of `S`, and Corollary 3.2 did not explicitly assume the two
additional `S`-full components required by Lemma 3.1.  Both omissions are
repaired in the pinned revision.  No mathematical claim below relies on the
finite probe.

This is a promotion re-pin of the previously GREEN source revision at
SHA-256

```text
4e52f378f4db873b95017a6e9a877e1f9ff07593af81482db4751391bee4a09a
```

The note moved from `active/` to `results/`; its status and repository-relative
links were adjusted accordingly.  A line-by-line comparison confirms that
the statements and proofs of Lemma 1.1, Theorem 2.1, Corollary 2.2,
Lemma 3.1, and Corollary 3.2, together with their trust boundary, are
mathematically unchanged.  The finite paragraph still records only the
previously audited `4,458/4,592` positive certificates and 134 uncovered
choices, and draws no conclusion from the uncovered choices.

## 1. Odd-cycle construction

Two vertex-disjoint odd cycles in an eight-vertex set have orders `(3,3)` or
`(3,5)`.  At most one contains the prescribed vertex `d`, so one of order
three or five avoids it.  The displayed three branch sets on a five-cycle

```text
{c_0}, {c_1,c_2}, {c_3,c_4}
```

are nonempty, connected, pairwise disjoint, and pairwise adjacent through
the three cycle edges `c_0c_1`, `c_2c_3`, and `c_4c_0`.  A triangle supplies
the same model by singleton branch sets.

The anchor count is exact enough for all later uses.  The chosen cycle has
at most five vertices, so its complement in `S` has at least three vertices.
Because the cycle avoids `d`, that complement contains `d` and at least two
further distinct vertices.  Thus the choices `x_0,x_1` used later are always
available and avoid both the cycle model and `d`.

## 2. Internal shared portal

For Theorem 2.1, the seven displayed branch sets are

```text
Q_0+x_0, Q_1+x_1, L, R+v, M_1, M_2, M_3.
```

They are pairwise disjoint.  The four connected subgraphs outside `S` are
pairwise disjoint by hypothesis; `v` lies outside them and outside `S`; the
anchors are distinct vertices of `S` outside the odd cycle; and the three
cycle branch sets partition that cycle.  Each displayed set is connected:
`S`-fullness connects `x_i` to `Q_i`, and the prescribed edge from `v` into
`R` connects `R+v`.

Every required adjacency has a literal source:

- `Q_0+x_0` meets `Q_1+x_1` through an edge from `Q_0` to `x_1`;
- either anchored full component meets `L` through its anchor, because both
  anchors differ from `d`;
- an anchor different from `e` has a neighbour in `R`, while an anchor equal
  to `e` is adjacent to `v`;
- `L` meets `R+v` through the prescribed edge from `v` into `L`;
- each `Q_i` meets every `M_j` by `S`-fullness;
- `L` meets every `M_j` because the whole odd cycle avoids `d`;
- `R+v` meets every `M_j`, with `R` supplying all boundary vertices other
  than possibly `e` and `v` supplying `e`; and
- the three `M_j` are pairwise adjacent by the `K_3` model.

Hence the construction is an explicit `K_7`-minor model, with no duplicated
portal or implicit quotient vertex.

In Corollary 2.2, `0<q<m` makes both tails nonempty.  The audited
overlapping-interval normal form gives

```text
P[0,q-1] adjacent to S-{d},
P[q+1,m] adjacent to S-{e},
```

unless the corresponding full neighbourhood already has order seven.  The
shared vertex `p_q` is adjacent to `d,e` and to both tails.  The two other
components are `S`-full by the boundary-full hypothesis.  These are exactly
the hypotheses of Theorem 2.1.

## 3. Strict reversal

Lemma 3.1 uses an honest disjoint path cut rather than the overlapping
three-subpath presentation.  Its seven branch sets are

```text
Q_0+x_0, Q_1+x_1, A, B, M_1, M_2, M_3.
```

Disjointness and connectivity follow exactly as in the shared-portal
construction, with `A,B` disjoint and connected by hypothesis.  The two
anchored full components are adjacent to each other through either opposite
anchor and to both `A` and `B` through their own anchors, since each anchor
avoids both `d` and `e`.  The edge between `A` and `B` is assumed literally.

For each `M_j`, condition

```text
M_j-{d} nonempty and M_j-{e} nonempty
```

is exactly sufficient: `A` has an edge to a vertex of `M_j` different from
`d`, while `B` has an edge to a possibly different vertex of `M_j` different
from `e`.  The full components meet every `M_j`, and the `M_j` are pairwise
adjacent.  Thus all 21 adjacencies of the seven-set model are present.

For Corollary 3.2, if `b<=k<a`, then

```text
A=P[0,k] contains P[0,b],
B=P[k+1,m] contains P[a,m].
```

The one-defect contacts of the two tails therefore persist in `A,B`.
The sets are nonempty, connected, disjoint, and adjacent through
`p_kp_{k+1}`.  The revised statement explicitly supplies the two other
`S`-full components `Q_0,Q_1`, so all hypotheses of Lemma 3.1 are present.

## 4. Dependency audit

The source uses the audited
[overlapping-interval path normal form](../results/hc7_order8_overlapping_interval_normal_form.md)
only for the literal tail contacts and the alternative in which a tail has
an actual order-seven full neighbourhood.  It does not import the unlabelled
rooted-minor conclusions of that note.

The audited
[three-component boundary classification](../results/hc7_order8_three_component_boundary_classification.md)
is used only to assert that each of the 82 surviving boundary graphs contains
two vertex-disjoint odd cycles.  No boundary colouring returned by a proper
minor is inferred from that finite classification.

## 5. Finite probe

The adjacent probe was rerun at SHA-256

```text
b80b497a56db5c30c12ae7db11c6fd025676d52c54cc6f4377573383d57d87d5
```

using

```text
geng -q 8 | python3 active/hc7_order8_shared_portal_quotient_probe.py
```

It reproduced:

```text
boundaries=82
shared_portal_models=4592/4592
strict_reversal_boundary_certificates=4458/4592
strict_reversal_uncovered=134
```

For every reported positive certificate, the probe checks nonemptiness,
disjointness, connectivity, and all pairwise adjacencies of the seven branch
sets.  This computation is falsification and reproducibility support only.
The proofs in Sections 1--3 are unbounded and independent of it, and no
conclusion is drawn about the 134 uncovered strict-reversal choices.

## 6. Exact trust boundary

The GREEN verdict does **not** establish:

1. a shared-portal completion when the shared vertex is an endpoint of the
   path;
2. the boundary model and anchors in Lemma 3.1 for every strict reversal;
3. a disjoint branch-set construction obtained by duplicating either of the
   two overlap vertices in the original strict-reversal normal form;
4. a compatible six-colouring of the two closed shores of any returned
   order-seven separation;
5. either path completion when only one other component of `G-S` is
   available;
6. an extension from an induced path component to a component having
   off-path vertices; or
7. `HC_7`.

Subject to these explicit limitations, every stated theorem and corollary in
the pinned source is correct.
