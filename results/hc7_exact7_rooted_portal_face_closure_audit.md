# Independent audit: exact-seven rooted portal-face closure

## Verdict

**GREEN AS PATCHED.**  The four-connected closure, the planar
three-connected curvature statement, and the three-cyclic-arc literal
`K_7` construction are correct.  These results eliminate every
four-connected thin shore and every planar three-connected thin shore in
the exact-seven `(1,3)` packet cell.

The original nonplanar Proposition 6.3 was not correct as written.  The
rooted-web theorem puts the graph inside a web as a **spanning
subgraph**; a facial triangle of the web rib need not be a literal
triangle in the original shore.  The source has been patched to retain
the valid three-vertex gate and to make the Hall-deficient conclusion
conditional on that gate inducing a literal triangle.

## 1. Literal branch-set lift

Given four distinct portal vertices `x_i` matched to four distinct
literal labels `s_i`, a rooted `K_4` model `B_i` in `L` gives the four
bags `B_i union {s_i}`.  The three remaining labels `r_j` anchor the
three disjoint full packets as `P_j union {r_j}`.

All 21 adjacencies are literal:

* six among the rooted bags come from the rooted `K_4`;
* three among packet bags come from one packet contacting the other
  bag's boundary anchor;
* twelve mixed adjacencies come from packet fullness at each `s_i`.

The bags are disjoint because `L`, `S`, and `R` are disjoint and the
seven anchors are distinct.  No colour class, virtual edge, or
contracted boundary label is used.

## 2. Hall rank and occurrence coverage

For `A subseteq S`, `1 <= |A| <= 4`, let

```text
U = union_{s in A} N_L(s).
```

If `|U| <= |A|-1`, then `|U| <= 3`.  A three- or four-connected `L`
has at least four or five vertices respectively, so `L-U` is nonempty.
Deleting `U union (S-A)`, of order at most six, separates a component of
`L-U` from the nonempty opposite shore: it cannot meet `A` by the
definition of `U`, cannot meet `R`, and all of `S-A` was deleted.  Thus
the rank-four Hall inequality is valid.

For a fixed incidence `sx`, delete label `s` and portal vertex `x`.  If
the residual matching number were at most two, Konig's theorem would
give a cover `U_0 union W_0` of order at most two.  Four labels can be
chosen outside `U_0`; all their portal neighbours lie in
`W_0 union {x}`, a set of order at most three, contradicting the preceding
rank inequality.  Hence **every individual literal portal occurrence**
extends to a matched four-set.  Overlapping portal sets cause no
duplication.

This agrees with, and slightly repackages, the stronger maximum-matching
theorem in `hc7_exact7_portal_rooted_k4.md`.  The latter proves a
matching of order `min{7,|L|}`; the present proof explicitly records the
fixed-incidence extension needed below.

## 3. Matroid facial propagation

The four-element partial transversals are the bases of the rank-four
truncation of the portal transversal matroid.  Its basis graph is
connected by one-element exchanges, so consecutive bases share three
actual portal vertices, not merely three labels.

Fabila-Monroy--Wood Theorem 6 gives, for each basis in a
four-connected `L`, either a rooted `K_4` or a planar embedding with the
four roots cofacial.  The first outcome lifts by Section 1.  In the
second, four-connectivity implies three-connectivity and hence a unique
plane embedding.  Two distinct faces of a three-connected simple plane
graph share at most two vertices.  Faces assigned to consecutive bases
therefore coincide, and occurrence coverage puts every vertex of
`N_L(S)` on one face.

For a planar three-connected `L`, Fabila-Monroy--Wood Theorem 9 supplies
the same cofacial alternative.  The identical basis propagation is
valid there as well.

## 4. Four-connected planar degree contradiction

In the fixed plane embedding, the common portal face has a simple facial
cycle because `L` is three-connected.  Let its length be `f`, let `h`
be the number of off-face vertices, and let `m=|E(L)|`.  This cycle need
not be induced; the outer-face Euler bound remains

```text
m <= 3(f+h) - 3 - f,
2m <= 4f + 6h - 6.
```

Every face vertex has `L`-degree at least four.  An off-face vertex has
no neighbour in `S`, since every literal portal is on the face, and no
neighbour in `R`, since there are no cross-shore edges.  Seven-connectivity
therefore makes its entire degree internal to `L` and at least seven.
Thus

```text
4f + 7h <= 2m <= 4f + 6h - 6,
```

an impossibility.  The argument also covers `h=0` and all smallest
four-connected orders (which are at least five).

## 5. Planar three-connected closure

For a planar three-connected shore, put

```text
e = sum_{z off F} (d_L(z)-7).
```

The same external-neighbour argument gives `e>=0`; Euler and the exact
degree sum yield

```text
sum_{x on F}(4-d_L(x)) >= h+6+e.
```

Since every face vertex has degree at least three, separating the
degree-three contribution from the negative contributions of degrees at
least five gives exactly Proposition 6.1.  The case `h=0` would make the
three-connected graph outerplanar, contradicting the standard
degree-at-most-two property, so there are at least `h+6>=7`
degree-three face vertices.  Each has at least four distinct literal
neighbours in `S`, because its three `L`-neighbours plus all boundary
neighbours account for a total degree at least seven.

Counting those incidences chooses a label `q` adjacent to at least four
such vertices.  Choose three in cyclic order.  Removing one cycle edge
from each of the three intervening intervals partitions the facial cycle
into three nonempty, disjoint, connected arcs `X_i`, one through each
chosen vertex; the three removed interface edges make the arcs pairwise
adjacent.

After deleting `q`, each chosen vertex has at least three available
labels.  Three sets each of order at least three automatically satisfy
Hall, so distinct `s_1,s_2,s_3` exist.  The bags

```text
X_i union {s_i}       (i=1,2,3),
{q},
P_j union {r_j}       (j=1,2,3)
```

are disjoint and connected.  Their 21 adjacencies consist of three arc
interfaces, three `q`--arc portal edges, three packet--packet
adjacencies, nine packet--arc contacts, and three packet--`q` contacts.
Thus Corollary 6.2 is a literal `K_7`, not merely a quotient model.

## 6. The nonplanar web overreach and its repair

Fabila-Monroy--Wood Theorem 8 says that a three-connected graph with no
rooted `K_4` is a spanning subgraph of a web.  A cell lies behind the
three vertices of a facial triangle in the web rib, and
three-connectivity ensures that all three gate vertices contact the
cell component.  This proves a literal three-vertex gate `T` with
`N_L(K)=T`, but does **not** prove that `L[T]` is a triangle.

The distinction is real.  Let the web rib be the wheel with outer cycle
`a b c d a` and hub `u`.  Add a two-vertex cell `{x,y}` at the facial
triangle `{a,b,u}`.  In the spanning subgraph keep

```text
ab, bc, cd, da, ub, uc, ud, xy,
x-a, x-b, x-u, y-a, y-b, y-u,
```

but delete `ua`.  It is three-connected: after deleting any two
vertices, if one of `x,y` remains then it still reaches at least one of
`a,b,u`, and every surviving component of the rib meets that triple;
if both are deleted, the remaining rib is connected.  It is nonplanar
(it contains a subdivision of `K_{3,3}` with sides `{a,b,u}` and
`{x,y,d}`, subdividing the `bd` edge at `c`).  Being a spanning subgraph
of the `(a,b,c,d)`-web, it has no `K_4` rooted at `a,b,c,d`.  Its cell
component `{x,y}` has literal neighbourhood `{a,b,u}`, which is not a
triangle.  No literal triangle separates a component disjoint from all
four nominated roots.  This falsifies the archived lemma in precisely
the form originally invoked by Proposition 6.3.

The patched Proposition 6.3 keeps the valid consequences:

* the gate has exactly three literal vertices;
* seven-connectivity gives `|N_S(K)|>=4`;
* **if** the gate induces a triangle and the four sets
  `N_S(K),N_S(t_1),N_S(t_2),N_S(t_3)` have an SDR, four carrier bags plus
  the three rich packet bags form a literal `K_7`;
* conditional on a literal triangle, failure of the SDR localizes by
  Hall entirely among the three gate portal sets, since every subfamily
  containing `N_S(K)` has union order at least four.

For a nonclique gate, the missing gate edge is an additional live
obstruction; palette or web completion edges may not be used as literal
branch-set adjacencies.

## 7. Exact promoted content and remaining gap

The independently safe theorem package is:

1. every four-connected thin shore in the `(1,3)` exact-seven packet
   cell gives a literal `K_7`;
2. every planar three-connected thin shore in that cell gives a literal
   `K_7`;
3. every surviving three-connected thin shore is nonplanar and exposes
   a component behind a literal three-vertex gate, with at least four
   boundary labels on the component side;
4. if that gate is a clique, its remaining obstruction is the stated
   Hall-deficient gate pattern.

The unresolved nonplanar branch must repair a missing gate edge or build
the four carriers without assuming that web-completion edges belong to
`L`.
