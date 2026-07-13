# Independent audit: theta crossbar nonowner descent

## Verdict

**GREEN.** `hadwiger_theta_crossbar_nonowner_descent.md` correctly proves
that the packet-free shore of either theta crossbar is a singleton or
contains a proper fragment behind a nested exact seven-cut. Dirac's
neighbourhood bound excludes the singleton, so every crossbar nonowner
strictly descends. Consequently a globally minimum theta fragment owns
both crossbars.

This is a descent/same-owner reduction, not a proof that the theta type or
`HC_7` is closed. The new boundary need not be theta. The former broad
rail-median Theorem 6.5 is **RED** and is not used here: component
absorption can destroy the retained rail capacity, and centre-only portal
capture need not expose the proposed seven-cut.

## 1. Crossbar orientation and the web input

For the first crossbar,

```text
P={0,5}, Q={1,2}, R={3,4,6}.
```

The two active blocks are independent, `R` is a triangle, and the
five-block quotient is complete. The only nonautomatic witnesses are
`25` between `P,Q`, `04` from `P` to singleton `4`, and `14` from `Q`
to `4`. Cyclic-packet ownership supplies at least one packet. Complete-
quotient transfer sends the exact five-block state to the opposite shore;
two owners would make that state extend both shores and colour-glue.
Therefore the owner/nonowner orientation is genuine.

If a proper relative boundary of the nonowner has order seven, its
component is a strict nested fragment. Otherwise seven-connectivity makes
every proper relative boundary have order at least eight. The audited
set-terminal Two Paths theorem then gives a bare disk web: a substituted
triangle cell would have boundary at most `3+|R|=6`.

## 2. One- and two-separators

The unique-portal, singleton-carrier and cutvertex arguments all use the
strict relative bound correctly. A two-cut component has both cut
vertices in its neighbourhood and at least six boundary contacts.
Packet failure forces exactly two lobes with complementary defects in one
active pair; the cut pair itself misses both defective roots.

Lemma 3.2's branch bags are valid. For complementary `P` defects, absorb
one cut vertex `z` into `L_0` and use

```text
P+X_P | Q+X_Q | 3 | 4 | 6 | L_0+z | L_5.
```

The first five bags form a clique by the complete block quotient. Each
lobe sees one root of `P`, both of `Q`, and all of `R`, hence all first
five bags. The absorbed cut vertex sees `L_5`, giving the last adjacency.
The `Q`-defect case is the literal swap. No branch-set overlap is hidden.

Thus an atomic nonsingleton nonowner is a three-connected bare web.

## 3. Curvature and cofaciality

After triangulating bounded faces, an outer web vertex has shore degree at
least three. An interior vertex sees none of the four active roots and at
most the three roots in `R`; the strict singleton boundary inequality
therefore gives shore degree at least five. Every positive disk-curvature
term is one and occurs at a common neighbour of `R`; an outer positive
vertex additionally sees one root of each active pair. Total positive
curvature is at least six.

If four common-`R` vertices were not cofacial, the standard rooted-`K_4`
theorem in the three-connected planar web, together with the singleton
triangle `R`, would give `K_7`. Hence every four are cofacial. Fixing three
and using that two faces of a three-connected plane graph share at most an
edge puts all such vertices on one face. If it were not the outer face, a
fan triangulation would leave at most two interior members and at most two
outer members with positive curvature, contradicting total six. The face
is therefore the outer face, with at least six tagged degree-three
vertices.

Any two tags split a spanning tree of the web into adjacent connected
sets `W_0,W_1`. The bags

```text
P+X_P | Q+X_Q | 3 | 4 | 6 | W_0 | W_1
```

form `K_7`: each tag sees all singleton roots and one root of each packet
block. This closes the arbitrary-order atomic web.

## 4. Second crossbar, singleton, and minimum orientation

For the second crossbar use

```text
P={1,5}, Q={0,2}, R={3,4,6}.
```

The same witnesses `25,14,04` make its five-block quotient complete, so
the proof relabels exactly.

A singleton full nonowner has degree seven and neighbourhood `S`. But
`012` is independent in the theta boundary, whereas Dirac's bound for a
degree-seven vertex in a 7-contraction-critical graph gives neighbourhood
independence at most two. Thus the singleton is impossible.

If a theta shore is globally minimum among fragments behind exact
seven-cuts, it cannot be a crossbar nonowner: the descent theorem would
produce a strictly smaller fragment. It therefore owns both crossbars.
This same-owner lock is the precise remaining theta cell.

## 5. Executable certificates and scope

The independent command

```text
.venv/bin/python equality_gate_theta_singleton_triangle_descent_verify.py
```

passes the complete five-block quotient, both crossed-two-cut models, and
all sixteen possible pairs of curvature tags.

The proof deliberately does not transport theta nonedges through the new
cut. Seven disjoint paths preserve a rooted minor shell, not the induced
boundary graph. Iterating the descent therefore requires the annular
operation-state transfer relation or a new same-owner exchange theorem;
static rail geometry and boundary relabelling are insufficient.
