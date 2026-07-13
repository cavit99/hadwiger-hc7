# Independent audit: nested neutral triangle rooted-model principle

## Verdict

**GREEN AS PATCHED.** Theorem 1.1 is correct. Deleting the neutral
triangle from a seven-connected graph leaves a four-connected graph; the
invoked rooted theorem is exactly Fabila-Monroy--Wood, Theorem 6; literal
neighbourhood nesting makes every rooted branch bag adjacent to all three
triangle vertices; and the cofacial alternative adds the third triangle
vertex in one face after deleting the other two.

Three exposition points were patched:

1. the proof now explicitly assumes that no four-subset of the common
   neighbourhood has a rooted model before claiming every four-subset is
   cofacial;
2. the 35-edge sharpness argument now records the relevant degrees; and
3. connectivity five of the sharpness graph is proved, rather than only
   exhibiting a five-cut.

A valid common-core weakening was added as Corollary 1.3. Mere owner-class
contact is not enough: private portals still have to be placed on the
common face to obtain the global two-apex conclusion.

## 1. Connectivity after deleting the triangle

Let `H=G-Q`. If `X` of order at most three disconnected `H`, then
`X union Q` of order at most six would disconnect `G`. Hence `H` is
four-connected. This is the standard inequality
`kappa(G-Q)>=kappa(G)-|Q|`; no undeclared connectivity is used.

Seven-connectivity also gives `d_G(q_3)>=7`. The two other triangle
vertices account for at most two neighbours, so the nested neighbourhood
`A=N_H(q_3)` has at least five distinct vertices.

## 2. Exact rooted-`K_4` input

The cited primary result is Theorem 6 of R. Fabila-Monroy and D. R. Wood,
*Rooted K4-Minors*, Electronic Journal of Combinatorics 20(2) (2013),
P64:

> For four distinct nominated vertices in a four-connected graph, either
> there is a `K_4` minor rooted at them, or the graph is planar and the four
> vertices lie on a common face.

This is precisely the form used. It is stronger than the three-connected
planar specialization and does not assume planarity in advance.

If four vertices `x_i` of `A` root bags `B_i`, literal inclusion

```text
N_H(q_3) subset N_H(q_1) intersect N_H(q_2)
```

makes each `x_i`, and hence each `B_i`, adjacent to all three singleton
triangle bags. The `B_i` are pairwise disjoint, connected and pairwise
adjacent by the rooted model; they lie in `H` and are disjoint from `Q`.
Together with the three singleton bags they are a literal seven-bag
`K_7` model. No branch set is reused.

The source originally passed too quickly from one chosen four-set to all
four-sets. The patch makes the logic explicit: if any four-subset has a
rooted model, the first outcome holds; otherwise the theorem applies to
every four-subset and makes each cofacial.

## 3. One common face and the planar extension

Once `H` is planar it is three-connected, so its plane embedding is unique
up to reflection and face choice. Fix three vertices of `A`. Every other
vertex of `A` lies with those three on a face. Distinct faces of a
three-connected plane graph share at most an edge, hence cannot share the
fixed three vertices. All of `A` therefore lies on one face.

The boundary of that face is a cycle. A new vertex can be placed in the
face and joined without crossings to any subset of its boundary vertices.
After deleting `q_1,q_2`, the complete neighbour set of `q_3` is exactly
`A`, so this draws all of `G-{q_1,q_2}`. The two apex labels are global,
not selected separately in different pieces.

## 4. Sharpness graph

The seven-vertex graph `T` described in Section 2 is a 2-tree: it starts
from a triangle and every later vertex is stacked on an existing edge.
It contains a triangle and no `K_4` minor, so its Hadwiger number is three.
For every graph `R`,

```text
eta(K_s join R) = s + eta(R).
```

The lower bound is immediate; for the upper bound, remove the at most `s`
branch bags meeting the universal clique from any clique model, leaving a
clique model in `R`. Thus `K_3 join T` has Hadwiger number six.

The independent verifier

```text
PYTHONPATH=active/runtime/deps python3 \
    archive/near_k7_nested_triangle_obstruction_verify.py
```

checks ten vertices, 35 edges, connectivity five, absence of a `K_7`
minor, and nonplanarity after every two-vertex deletion. The displayed
five-cut isolates `V`; the lower connectivity bound follows because
deleting fewer than five vertices either leaves a universal `q`, or
deletes all three `q` vertices and at most one vertex of the 2-connected
2-tree.

## 5. Cross-capacity atlas and actual gate count

The atlas command

```text
PYTHONPATH=active/runtime/deps python3 \
    archive/near_k7_exceptional_cross_split_atlas.py
```

reproduces all 480 minimal split rows and 12,960 duplicated-contact rows.
All negative minimal rows are homogeneous and have a side with at most
five owner classes. Every inclusion-maximal duplicated-contact negative
row has exactly four common owner classes; hence five common classes force
`K_7` by monotonicity.

In Corollary 3.2, owner classes are disjoint actual model pieces or
singleton labels. Therefore the external neighbourhood of `U` is the
disjoint union of one portal set per contacted nonsingleton class, the
contacted singleton vertices, and `N_V(U)`. If all are singletons its
order is at most `1+|S(U)|<=6`. In general seven-connectivity gives the
stated surplus by subtracting this baseline. The uncontacted owner class
ensures the neighbourhood is a genuine separator rather than all
remaining vertices.

## 6. Exact limit of portal-set weakening

The proof needs literal vertex-level nesting only to make every rooted bag
adjacent to `q_1,q_2`. Contact of the same *model piece* by all three
triangle vertices does not ensure that a rooted bag through a `q_3`
portal contains either other portal, and cannot replace (1.1).

The valid weakening is Corollary 1.3. If the triple common neighbourhood
has at least four vertices, then either it roots `K_4` and gives `K_7`, or
all common portals lie on one face of planar `H`. To add `q_3`, every
private `q_3` portal must also be proved to lie on that face. Thus a
spanning near-`K_7` model may replace literal nesting by:

1. a four-vertex common portal core; and
2. a separate cofaciality/rurality theorem for all private `q_3`
   attachments.

Without item 2, the two-apex conclusion is not justified. No purely
owner-class incidence weakening has been proved.
