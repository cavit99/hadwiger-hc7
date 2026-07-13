# The atomic order-eight curvature argument has one sharp wheel obstruction

## 1. Purpose

This note tests the hard rows of
`hadwiger_order8_tight_hall_palette_exchange.md` against the transported
atomic-web/curvature proof from
`hadwiger_singleton_triangle_exact7_transport.md`.

The test has a definitive negative answer.  Even after all of the following
are imposed simultaneously,

* the full eight-vertex gate;
* absence of a proper nested exact seven-cut;
* a three-connected bare Two Paths web whose disk core is triangulated;
* the literal `C6+z`, common-portal, and opposite-shore edges used by the
  conservative order-eight quotient; and
* absence of the required two protected columns,

there is a `K7`-minor-free static quotient.  It is a four-rim wheel with a
cyclic active-root incidence and a two-lobe distribution of the two gate
poles.  Thus disk curvature alone cannot close the connected order-eight
web.  The remaining step really must use a proper-minor transition or an
edge operation which destroys this cyclic state.

The construction is label-free up to the final embedding in the hard row.

## 2. The abstract atomic wheel

Let

\[
 B=A\mathbin{\dot\cup}C\mathbin{\dot\cup}R,
 \qquad |A|=|C|=2,\quad |R|=4,
\]

where

\[
 A=\{a_0,a_1\},\qquad C=\{d_0,d_1\},\qquad
 R=\{r,s,p,q\}.
\]

Let `K` be the wheel with rim

\[
                    v_0v_1v_2v_3v_0
\]

and hub `h`.  Give the rim the active contacts

\[
\begin{array}{c|c}
v_0& a_0,d_1\\
v_1& d_1,a_1\\
v_2& a_1,d_0\\
v_3& d_0,a_0
\end{array}                                                   \tag{2.1}
\]

and the neutral contacts

\[
\begin{array}{c|c}
v_0,v_1&r,s,p\\
v_2,v_3&r,s,q\\
h&r,s,p,q.
\end{array}                                                   \tag{2.2}
\]

Thus every rim vertex has five boundary neighbours and the hub has four.
Every vertex of `K` has total degree eight in `K union B`.

### Lemma 2.1 (strict relative eight-boundary)

For every nonempty proper `Y subsetneq K`,

\[
 |(N_K(Y)-Y)\mathbin{\dot\cup}N_B(Y)|\ge 8.                  \tag{2.3}
\]

In particular, no part of this wheel lies behind a relative boundary of
order seven.

### Proof

Put `X=Y cap {v0,v1,v2,v3}`.  First suppose `h in Y`.  The four neutral
labels belong to `N_B(Y)`.  If `X` is empty, the four rim vertices belong
to `N_K(Y)`, giving equality in (2.3).  Otherwise `|X|<=3`.  The active
labels met by `X` are the edges of the four-cycle of labels

\[
                   a_0d_1a_1d_0a_0
\]

incident with `X`.  Their number is two for `|X|=1`, at least three for
`|X|=2`, and four for `|X|=3`.  The `4-|X|` omitted rim vertices also
belong to `N_K(Y)`.  The resulting totals are at least nine.

Now suppose `h notin Y`, so `Y=X` is a nonempty rim set.  Its internal
boundary consists of `h` and the outside neighbours of `X` on the rim.
Its boundary contacts consist of `r,s`, the active label-edges incident
with `X`, and at least one of `p,q` (both if `X` meets both half-rims).
For a singleton these contributions are respectively `3,2,2,1`, giving
eight.  For two adjacent, two opposite, three, or four rim vertices the
totals are respectively at least `9,11,10,9`.  This proves (2.3). QED.

### Lemma 2.2 (bare crossed disk web)

`K` has no packet consisting of disjoint connected carriers for
`(a0,a1)` and `(d0,d1)`.  After the four active labels are added as
set-terminals, their incidences and the rim form the outer cycle

\[
 a_0v_0d_1v_1a_1v_2d_0v_3a_0.                              \tag{2.4}
\]

Together with the four rim edges and the four hub spokes this is a
triangulated disk.  Hence the planar core is saturated relative to its
fixed outer society: there is no missing internal face edge or clique
insertion hidden by the web theorem.

### Proof

The two terminal pairs alternate on the boundary of the disk in (2.4).
Two disjoint carriers would give two disjoint arcs joining alternating
boundary pairs, contrary to the Jordan curve theorem.  Every bounded
face of the displayed disk is a triangle, proving the final assertion.
This is deliberately only saturation of the disk core with the outer
society fixed; it is not a claim that adding an arbitrary edge between
two artificial terminals creates the prescribed linkage. QED.

The curvature identity is sharp here.  Each rim vertex has outer
curvature one and the hub has interior curvature two, so the total is

\[
                         4\cdot1+2=6.                       \tag{2.5}
\]

Thus none of the curvature is hidden in a clique insertion or a low
adhesion.

## 3. Embedding in the hard `alpha=c3` row

Use the notation of the order-eight note and put

\[
 (a_0,a_1)=(x,c_2),\qquad (d_0,d_1)=(c_4,c_5),
 \qquad (r,s)=(c_0,z).                                     \tag{3.1}
\]

The two remaining neutral gate vertices are the old two-cut poles `p,q`.
Let `H` denote the conservative opposite full-shore vertex.  Define `Q`
as follows.

1. On `c0,...,c5,z,H,x` take exactly the quotient edges used by
   `order8_tight_hall_quotient_probe.py`: the complement-of-cycle graph
   on the `ci`, the universal boundary vertex `z`, the vertex `H` full to
   the seven old boundary vertices, and the two edges `xc0,xc1`.
2. Add the wheel `K` and exactly the contacts (2.1)--(2.2), interpreted
   by (3.1).
3. Add no other edge incident with `p` or `q`.

Then

\[
        N_Q(K)=\{x,p,q,c_0,c_2,c_4,c_5,z\},                \tag{3.2}
\]

which is the full exact order-eight gate in the hard row.  The old labels
`c1,c3` are precisely the two old-boundary labels missed by `K`.

### Theorem 3.1 (the conservative quotient is `K7`-minor-free)

The graph `Q` has no `K7` minor.

### Proof

Delete `c0,z`.  The remaining graph is planar.  One planar rotation is
listed below; consecutive neighbours are in clockwise order.

```
c1: c3 c5 x c4 H
c2: H c4 v2 v1 c5
c3: c1 H c5
c4: v3 v2 c2 H c1
c5: c2 v1 v0 c1 c3 H
x : v0 v3 c1
v0: v1 p h v3 x c5
H : c3 c1 c4 c2 c5
v2: c4 v3 q h v1 c2
v1: c5 c2 v2 h p v0
v3: x v0 h q v2 c4
h : q v3 v0 p v1 v2
p : h v0 v1
q : v2 v3 h
```

The corresponding faces are triangles except for
`c1-x-v3-c4` and `c1-c5-v0-x`; direct traversal of the rotation gives
each edge twice and Euler's identity.  Hence this is a combinatorial
plane embedding.

Finally, every 2-apex graph is `K7`-minor-free.  Indeed, in a putative
seven-branch-set model, deleting the two apex vertices destroys at most
two branch sets, leaving a `K5` minor in a planar graph.  This is
impossible.  Apply this with the apex pair `c0,z`. QED.

## 4. Exact consequence for the curvature programme

The transported singleton-triangle proof used a three-vertex clique of
neutral tags.  Every positive-curvature vertex met all three tags, so a
rooted `K4` or two separated positive vertices immediately completed the
fixed clique frame.

At order eight the neutral set has four vertices and, crucially, two are
the unlabelled poles `p,q`.  The wheel above distributes them over two
overlapping half-rims while keeping `c0,z` universal.  This simultaneously

* pays the strict relative-boundary inequality;
* preserves the alternating active-root order;
* prevents the two protected columns; and
* keeps the conservative quotient 2-apex.

Therefore the following hoped-for statement is false:

> strict relative boundary at least eight plus a bare triangulated hard Two Paths
> web forces a `K7` minor (or a nested exact seven-cut).

The counterarchitecture is static, not a contraction-critical graph.  It
does not satisfy the proper-minor transition requirements.  Its value is
that it identifies the exact remaining dynamic target:

> A faithful operation in a minor-minimal counterexample must break the
> cyclic incidence
> `a0-d1-a1-d0-a0` or the two-pole half-rim distribution
> `p | q`; otherwise the operated state remains the same 2-apex wheel.

Equivalently, the connected hard order-eight case has reached the same
capacity--state obstruction as the exact two-lobe hub: a four-cycle of
active portal classes crossed by a two-state pole orientation.  Curvature
does not distinguish the two states.  A valid closure must use the exact
trace change or crossed-operation theorem to reverse one orientation,
which then creates the two protected columns of Lemma 3.1 in the
order-eight note.

## 5. Verification

`order8_atomic_wheel_counterarchitecture_verify.py` independently checks

* all thirty nonempty proper subsets in (2.3);
* absence of the two-packet by enumerating connected carriers;
* fullness of the exact eight-gate; and
* planarity after deleting `c0,z`.

The mathematical proof of `K7`-minor-freeness is the 2-apex argument in
Theorem 3.1; it does not depend on a minor-search solver.
