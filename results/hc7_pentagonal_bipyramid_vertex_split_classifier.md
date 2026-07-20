# Vertex splits of the pentagonal bipyramid

**Status:** written proof; separate internal audit.  This is a finite
quotient theorem about the seven-vertex pentagonal bipyramid.  It does not
assert that a quotient split can be lifted to a label-preserving split of
branch sets in the host graph.

## Theorem

Let `P=C_5\vee\overline {K_2}` be the pentagonal bipyramid, with its unique
plane embedding.  Split a vertex `x` into adjacent vertices `x_1,x_2`.
For every old neighbour `s` of `x`, retain at least one of `sx_1,sx_2`;
both may be retained.  Let `P_x` be the resulting eight-vertex graph.

List the old neighbours of `x` in their cyclic order around `x`.  Then the
following are equivalent.

1. `P_x` has a `K_5` minor.
2. There are four distinct old neighbours `a,b,c,d`, in this cyclic order,
   such that

   ```text
   ax_1, cx_1, bx_2, dx_2
   ```

   are edges (or the same statement with `x_1,x_2` interchanged).
3. The split cannot be drawn inside a small disc replacing `x` in the
   fixed plane embedding of `P`.

Equivalently, write `X`, `Y`, or `B` at an old neighbour according as it
is adjacent only to `x_1`, only to `x_2`, or to both.  The `K_5`-minor-free
splits are exactly the cyclic words of the form

```text
                 X^r B^epsilon Y^s B^eta,
```

where `r,s>=0` and `epsilon,eta` belong to `{0,1}` (empty blocks are
allowed).  Thus the surviving splits are precisely the planar vertex
splits.

## Proof

Put `A=N(x_1)\cap N_P(x)` and `D=N(x_2)\cap N_P(x)`.  By hypothesis
`A\cup D=N_P(x)`.

We first record the elementary circular-order fact used below.  Two subsets
`A,D` covering a cyclically ordered set have no alternating quadruple

```text
                 a,d,a',d'
```

with `a,a' in A` and `d,d' in D` if and only if their membership word has
the displayed form `X^r B^epsilon Y^s B^eta`.

Indeed, three common elements already supply an alternating quadruple after
assigning their two possible roles and using any fourth element.  With no
common element, the assertion says exactly that the two parts each form one
cyclic interval.  With one common element, cut the cyclic order there; the
two exclusive sets must be intervals in the resulting linear order.  With
two common elements, each of the two open arcs between them must be
monochromatic.  If both arcs are nonempty, their colours must differ, since
otherwise the two common ends and one vertex from each arc alternate.
These alternatives give precisely the stated word.  The converse is
immediate by reading that word around the circle.

Suppose first that there is no alternating quadruple.  The word form lets
us replace `x`, inside a sufficiently small disc, by the edge `x_1x_2`:
the `X`-edges leave on one side, the `Y`-edges on the other, and a `B`
neighbour can occur only at either transition.  At such a transition the
two edges to the common neighbour can be drawn on the two sides of the old
edge.  Hence `P_x` is planar and has no `K_5` minor.

Now suppose an alternating quadruple exists.  When `x` is a pole, its five
old neighbours are the rim vertices.  Delete, only for purposes of taking a
subgraph, one of the two clone incidences at every common neighbour.  Choose
the incidence at the fifth rim vertex so that, after cyclic relabelling and
possibly interchanging the clones, the five incidences read

```text
                 X, X, Y, X, Y
```

on rim vertices `c_0,c_1,c_2,c_3,c_4`.  If `q` is the other pole, the five
sets

```text
 {q},  {c_0},  {c_1},  {x_1,c_3},  {x_2,c_2,c_4}
```

are pairwise disjoint connected branch sets of a `K_5` model.  The first
set contacts every other through a rim vertex; consecutive singleton rim
vertices contact; each singleton contacts the appropriate clone bag; and
the last two bags contact through `x_1x_2`.

When `x=c_0` is a rim vertex, its old neighbours occur alternately as a
rim neighbour, a pole, the other rim neighbour, and the other pole.  An
alternating quadruple uses all four of them.  After relabelling, let `x_1`
retain the edges to `c_1,c_4` and let `x_2` retain the edges to the poles
`p,q`.  Then

```text
 {p},  {c_1},  {c_2},  {q,x_2},  {c_3,c_4,x_1}
```

are the branch sets of a `K_5` model.  Every edge needed by either displayed
model is present in the original split, since we obtained the canonical
incidence pattern only by deleting surplus clone incidences.  This proves
the equivalence.  \(\square\)

## Exhaustive check

The dependency-free script
[`hc7_pentagonal_bipyramid_vertex_split_classifier_verify.py`](hc7_pentagonal_bipyramid_vertex_split_classifier_verify.py)
checks every one of the `3^5+3^4=324` labelled splits by exact branch-set
enumeration.  It also quotients by the stabilizer of the split vertex and
clone interchange.  In the two-root census it additionally identifies the
interchange of the two indistinguishable added roots.  Its output is:

```text
pole: assignments=243 k5=161 planar=82 orbits=22 planar_orbits=8
rim: assignments=81 k5=31 planar=50 orbits=20 planar_orbits=11
root-distributed pole: orbits=122 k7=76 surviving=46
root-distributed rim: orbits=112 k7=52 surviving=60
one-edge exchanges=90: diagonal-flip criterion PASS
simultaneous safe rim flips=4: all K5-free
pole safe exchange plus second contact=6: all K5
pentagonal-bipyramid vertex-split classification: PASS
```

The computation is corroborative; the theorem above has a direct proof.

## Adding the two fixed roots

### Corollary (arbitrary root-contact distribution)

Let `r_0r_1` be an edge, make both roots adjacent to every old vertex of
`P`, and then split `x` as in the theorem.  For each root, retain its old
contact with at least one of `x_1,x_2`, arbitrarily.  The resulting
ten-vertex quotient has a `K_7` minor if and only if the split incidence
word has an alternating quadruple.

#### Proof

In the alternating case, every branch set in either explicit `K_5` model
above contains an old, nonsplit vertex of `P`.  Both roots are therefore
adjacent to every one of the five branch sets, independently of their
contacts with the clones.  The two singleton roots complete a `K_7` model.

In the nonalternating case the split graph `P_x` is planar, so it has no
`K_5` minor.  The quotient with arbitrary root contacts is a subgraph of
`K_2\vee P_x`.  Any clique-minor model in `K_2\vee P_x` has at most two
branch sets meeting the two universal vertices; deleting those branch sets
leaves a clique-minor model in `P_x`.  Hence

```text
                 eta(K_2 vee P_x) <= 2+eta(P_x) <= 6,
```

and the quotient has no `K_7` minor.  \(\square\)

Thus a loss of one or both clone-to-root contacts never changes the split
classification.  The exact orbit census, including the two root-contact
marks and allowing interchange of the two roots, has `76` `K_7`-positive
and `46` surviving pole-split orbits, and `52` positive and `60` surviving
rim-split orbits.

## One-edge exchanges

The same quotient has a second exact finite rule.  Let `f` be a missing
edge of `P` and `e` an old edge.

### Proposition (diagonal-flip criterion)

The graph `P+f-e` is `K_5`-minor-free if and only if `e` and `f` are the
opposite diagonals of the quadrilateral formed by two facial triangles of
`P`.  In that case the exchange is a planar diagonal flip.  Every other
one-edge loss is tolerated: `P+f-e` still has a `K_5` minor.

#### Proof

There are two orbits of missing edges.

If `f=pq` joins the poles, it is the opposite diagonal to each rim edge.
Deleting a rim edge is therefore planar.  Every spoke is equivalent under
the stabilizer of `pq`; for `e=pc_0`, a `K_5` model is

```text
 {p}, {q}, {c_1}, {c_2}, {c_0,c_3,c_4}.
```

If `f=c_0c_2` is a rim chord, its planar flips delete exactly `pc_1` or
`qc_1`.  The remaining old edges have the following stabilizer orbits; one
representative model is displayed in each row.

| deleted edge `e` | five branch sets in `P+c_0c_2-e` |
|---|---|
| `c_0c_1` (also `c_1c_2`) | `{p}`, `{c_0}`, `{c_2}`, `{q,c_1}`, `{c_3,c_4}` |
| `c_0c_4` (also `c_2c_3`) | `{p}`, `{c_0}`, `{c_1}`, `{c_2}`, `{q,c_3}` |
| `pc_0` (a spoke at `c_0` or `c_2`) | `{p}`, `{c_1}`, `{c_2}`, `{q,c_3}`, `{c_0,c_4}` |
| `c_3c_4` | `{p}`, `{c_0}`, `{c_1}`, `{c_2}`, `{q,c_3}` |
| `pc_3` (a spoke at `c_3` or `c_4`) | `{p}`, `{c_0}`, `{c_1}`, `{c_2}`, `{q,c_4}` |

Pole interchange and reflection in the stabilizer supply every edge in
each displayed orbit.  The two omitted middle spokes are exactly the two
planar flips.  This proves the proposition.  \(\square\)

Two consequences delimit what simultaneous response edges can do.

1. Starting with `P+pq-c_0c_1`, **any** further missing contact (restoring
   `c_0c_1` or adding any rim chord) creates a `K_5` minor.
2. The analogous assertion is false for two rim-chord responses.  Add both
   `c_0c_2,c_0c_3` and independently delete one of `pc_1,qc_1` and one of
   `pc_4,qc_4`.  All four resulting graphs are planar: they are obtained
   from `P` by two independent facial diagonal flips.  Hence none contains
   a `K_5` minor.

## Trust boundary

The theorem says that a **quotient** split of a pentagonal-bipyramid column
which has crossing attachment classes creates a `K_5` minor in the split
contact graph.  Together with two fixed root branch sets this would lift to
a `K_7` model.  It does not prove that a literal connected column admits the
required split, that the two pieces retain prescribed first edges, or that
a failed split exposes a small separator of the host graph.
