# Audit of the complete warehouse bypass and a uniform deficiency extension

## 1. Audit verdict

Theorem 1.1 and Corollary 1.2 of
`hadwiger_complete_five_warehouse_bypass.md` are correct.

For Theorem 1.1, choose a shortest path whose distinct ends are in `X`
among all such paths in the selected component of `G-C`.  Its interior
contains no vertex of `X`.  After removing its ends, the remaining `m`
vertices of `X` can be paired arbitrarily with the `m` vertices of `C`.
Complete `C-X` contact gives both the connectivity of every paired bag
and every adjacency between two paired bags.  The two parts of the path
see every paired bag through their endvertices.  All branch sets are
disjoint.  This is exactly a `K_{m+2}` model.

Deleting the `m`-set `C` from an `(m+1)`-connected graph leaves a
connected graph, so the corollary follows.

There is an important scope warning.  The same proof cannot be extended
by first finding an arbitrary matching in a noncomplete contact graph.
The two unused targets must both see every paired bag, and the path
between them must have no other target in its interior.  Connectivity
alone does not synchronize those two requirements.

## 2. Audit of the collective-contact counterexample

Let `I` be the icosahedron and let

\[
                         G_0=K_2\vee I,
\]

where the two universal adjacent vertices are `u,v`.  In the standard
NetworkX labelling put

\[
 C=N_I(0)=\{1,5,7,8,11\},\qquad
 X=\{0,2,4,6,9,10,u\}.
\]

The contact profiles inside `C` are

\[
\begin{array}{c|c}
0&1,5,7,8,11\\
2&1,8\\
4&5,11\\
6&1,5\\
9&7,8\\
10&7,11\\
u&1,5,7,8,11.
\end{array}
\]

Thus every target has a contact in `C`, but contact is not complete.
The icosahedron is planar, five-connected, and has Hadwiger number four.
Joining a universal `K_2` raises both connectivity and Hadwiger number by
two, so

\[
                       \kappa(G_0)=7,\qquad \eta(G_0)=6.
\]

The join identity for the Hadwiger number is elementary here: singleton
universal vertices extend every clique model in `I`, while in the other
direction at most two branch sets of a clique model use `u` or `v`; all
remaining branch sets form a clique model in `I`.  Hence `G_0` has no
`K_7` minor.  Deleting `u,v` leaves the planar icosahedron.  The claimed
collective-contact counterexample and its coherent two-apex description
are therefore correct.

## 3. The exterior target torso

Let `C,X` be disjoint, with

\[
                         |C|=m,\qquad |X|=m+2,
\]

and put `H=G-C`.  Define the **exterior target torso** `L=L(H,X)` on
vertex set `X` by putting `xy` in `E(L)` exactly when `H` has an
`x-y` path whose interior avoids `X`.

### Lemma 3.1 (connectivity descends to the target torso)

If `H` is connected, then `L` is connected.  If `H` is two-connected,
then `L` is two-connected.

#### Proof

Decompose any path in `H` at the vertices where it meets `X`.  Consecutive
`X`-vertices on the path are adjacent in `L`, proving connectedness.
For every `x in X`, apply the same argument in the connected graph
`H-x`; it proves that `L-x` is connected.  Since `|X|>=4`, this is
two-connectivity.  \(\square\)

Call `x in X` **complete** if it is adjacent to every vertex of `C`, and
let

\[
                 D=\{x\in X:x\text{ is not complete to }C\}.
\]

Thus `D` is the set of spatially deficient target rows.

## 4. A sharp square contact lemma

### Lemma 4.1 (subcritical deficiency pairing)

Let `A,B` be the two sides of a bipartite graph, with
`|A|=|B|=m`.  If fewer than `m` of the `m^2` possible edges are missing,
then there is a bijection `f:A->B` such that

1. `af(a)` is an edge for every `a in A`; and
2. for distinct `a,a'`, at least one of `af(a')` and `a'f(a)` is an
   edge.

#### Proof

Induct on `m`.  The claim is immediate when `m=1`.  Since fewer than
`m` edges are missing, some column `b in B` is complete to `A`.  If
there is a missing edge, choose a row `a` incident with one; otherwise
choose any row.  Delete `a,b`.  The remaining square has fewer than
`m-1` missing edges, so induction gives the required bijection there.
Set `f(a)=b`.  Every old paired bag sees the new one through its row
vertex and the complete column `b`, so property 2 is retained.  \(\square\)

The strict inequality is sharp for this certificate.  With exactly `m`
missing edges, one row can miss all `m` columns.  More generally, two
rows can have complementary missing sets partitioning the columns.  In
either case no such bijection exists.

### Lemma 4.2 (classification at equality)

If exactly `m` edges are missing in the square `A-B` and the bijection
in Lemma 4.1 does not exist, then, up to interchanging `A` and `B`,

1. every vertex of `B` is incident with exactly one missing edge; and
2. all missing edges are incident with at most two vertices of `A`.

Thus the equality obstructions are precisely a one- or two-star
partition on one side, or its transpose.

#### Proof

If the present-edge graph has no perfect matching, Hall's theorem gives
`S subseteq A` with `|N(S)|<|S|`.  If `|S|=s`, at least

\[
                         s(m-s+1)
\]

edges are missing.  This is at least `m`, with equality only for
`s=1` or `s=m`.  Equality gives respectively one empty row or one empty
column, both listed in the conclusion.

We may therefore suppose that a present perfect matching exists.  If
there is neither a complete row nor a complete column, every row and
every column is incident with exactly one missing edge.  For `m>=3`,
label those missing edges `a_i b_i` and use the cyclic bijection
`a_i -> b_{i+1}`.  It uses present edges and its directed missing-contact
pattern is one cycle of length `m`, so it has no directed two-cycle and
satisfies Lemma 4.1(2).  For `m=2` the missing matching is already one
of the listed two-star patterns.

It remains, by symmetry, that there is a complete column `b`.  If some
row `a` is incident with at least two missing edges, delete `a,b`.
The remaining `(m-1)`-square has fewer than `m-1` missing edges, so
Lemma 4.1 gives a bijection which extends by `a -> b`, a contradiction.
Hence every nonzero row has missing degree one.  If the missing edges
use at least three columns, transpose the cyclic construction in the
preceding paragraph (cycling through the nonempty column classes and
assigning all remaining rows arbitrarily) to obtain the forbidden
bijection.  Therefore the missing edges use at most two columns, which
is the transposed listed pattern.  \(\square\)

## 5. Uniform contact-or-two-apex theorem

### Theorem 5.1 (low deficiency gives a clique minor or a coherent torso)

Let `m>=2`.  Let `G` be `(m+2)`-connected, and let `C,X` be disjoint
sets with `|C|=m` and `|X|=m+2`.  Suppose that fewer than `m` edges are
missing between `C` and `X`.  With `D` and the exterior target torso
`L=L(G-C,X)` defined above, one of the following holds:

1. `G` contains a `K_{m+2}` minor; or
2. `D` is a vertex cover of the two-connected graph `L`.

In particular, if `|D|<=1`, outcome 1 always holds.  If `|D|=2`, then
either outcome 1 holds or, writing `D={p,q}`,

\[
                    K_{2,m}\subseteq L\subseteq K_2\vee\overline{K_m},
\]

where the two-vertex side is `{p,q}`.  Thus the only two-row residue is
a literal coherent two-apex exterior frame.

#### Proof

The graph `H=G-C` is two-connected: deleting one further vertex from
`H` deletes only `m+1` vertices from `G`.  Hence `L` is two-connected by
Lemma 3.1.

Suppose that `L` has an edge `uv` with `u,v notin D`.  Let `P` be a
`u-v` path in `H` whose interior avoids `X`, and put

\[
                              Y=X-\{u,v\}.
\]

Both `u` and `v` are complete to `C`.  Fewer than `m` contacts are
missing in the square `C-Y`, so Lemma 4.1 gives a bijection `f:C->Y`
with its two stated properties.  For `c in C`, put

\[
                              B_c=\{c,f(c)\}.
\]

These `m` bags are connected.  The second property of `f` makes them
pairwise adjacent.  Split `P` at any edge into two nonempty adjacent
connected sets `R,S`, with `u in R` and `v in S`.  The interior of `P`
avoids `X`, so `R,S` are disjoint from all `B_c`.  Since `u,v` are
complete to `C`, both `R` and `S` see every `B_c`.  Therefore

\[
                          (B_c:c\in C),R,S
\]

is a `K_{m+2}` model.

Consequently, if outcome 1 fails, `L` has no edge with both ends in
`X-D`; equivalently, `D` is a vertex cover of `L`.  Two-connectivity
rules out `|D|<=1`.  If `D={p,q}`, every vertex outside `D` has degree
at least two in `L` and all its neighbours lie in `D`; hence it is
adjacent to both `p` and `q`.  The displayed two-apex containment
follows.  \(\square\)

### Theorem 5.2 (equality extension)

The strict hypothesis in Theorem 5.1 can be weakened to **at most**
`m` missing contacts if a third outcome is retained:

3. exactly `m` contacts are missing and, for every edge `uv` of
   `L[X-D]`, the missing-contact graph in the square
   `C-(X-{u,v})` is one of the one-/two-star equality patterns in
   Lemma 4.2.

#### Proof

The proof of Theorem 5.1 is unchanged until a complete-complete torso
edge `uv` is selected.  All missing contacts lie in the remaining
square because `u,v` are complete.  If fewer than `m` are missing,
Lemma 4.1 closes the model.  If exactly `m` are missing, Lemma 4.2
either supplies the same bijection and closes the model, or gives
outcome 3.  If there is no complete-complete torso edge, `D` is a vertex
cover and outcome 2 holds.  \(\square\)

Under collective fullness, the equality state has a particularly clean
interpretation.  A one-column obstruction is impossible, since that
target would have no contact in `C`.  If all deficiencies occur in at
most two target rows, the only equality obstruction is therefore two
deficient targets whose missing-neighbour sets are nonempty and partition
`C`: an exact two-apex contact state.  The transposed alternative is an
exact one-/two-carrier warehouse state in which every one of the `m`
remaining targets misses exactly one of the exceptional carrier
vertices.

### Corollary 5.3 (the `HC_7` warehouse range)

In a seven-connected graph, let `|C|=5` and `|X|=7`.  If at most four
`C-X` contacts are missing, then either there is a `K_7` minor or every
clean exterior path between two complete target rows is blocked by the
deficient rows.  If the deficiencies occur in at most two target rows,
the only surviving clean-path geometry is the coherent
`K_{2,5}` two-apex frame described in Theorem 5.1.

With five missing contacts the same conclusion holds unless every
complete-complete clean exterior edge exposes one of the exact
one-/two-star contact states in Lemma 4.2.  This is a finite **state
type**, not a bound on the order or internal complexity of the carrier.

This closes an infinite spatial-deficiency family.  It does not cover
the icosahedral example, whose displayed `C-X` contact matrix has
fifteen missing entries, nor does it claim that arbitrary collective
fullness is sufficient.
