# Minimal bad split contractions and the multi-component closure

**Status:** proved and independently audited.

This note treats an inclusion-minimal simultaneous contraction of split
edges belonging to vertex-disjoint six-vertex `K_5` models.  It proves the
exact six-cut assertion and closes every excess-eight or excess-nine cut
having at least three quotient components by displaying seven literal
branch sets.

The sole residue left by this argument is a six-cut with exactly two
components.  No conclusion about that residue is asserted here.

## 1. Setup

Let `G` be a seven-connected graph containing three pairwise
vertex-disjoint six-vertex `K_5` models

\[
 M_i=Q_i\mathbin{\dot\cup}\{x_i,y_i\},\qquad i=1,2,3,
\]

where `Q_i` is the literal four-clique formed by the singleton bags and
`x_i y_i` is the two-vertex bag.  The three split edges form a matching.

Let `F` be a nonempty inclusion-minimal subset of these split edges such
that

\[
                         H=G/F
\]

is not seven-connected.  Put `m=|F|`, and write `z_i` for the image of an
edge `x_i y_i in F`.  Thus every quotient obtained by contracting a proper
subset of `F` is seven-connected.

For `x_i y_i in F`, the image

\[
                         L_i=Q_i\cup\{z_i\}
\]

is a literal `K_5` in `H`.

## 2. The minimal bad quotient has one exact kind of cut

### Theorem 2.1 (minimal bad cut)

Assume that `H` has no `K_7` minor.  Then `H` is six-connected.  Every
separator `T` of `H` of order at most six has all of the following
properties.

1. `|T|=6`.
2. `z_i in T` for every `x_i y_i in F`.
3. Every component of `H-T` has neighbourhood exactly `T`.
4. Put

   \[
    T^+=(T-\{z_i:x_i y_i\in F\})
          \cup\bigcup_{x_i y_i\in F}\{x_i,y_i\}.
   \]

   The components of `G-T^+` are the literal expansions of the
   components of `H-T`, and every vertex of `T^+` has a neighbour in every
   one of them.

In particular

\[
                         |T^+|=6+m.                    \tag{2.1}
\]

### Proof

Fix `x_i y_i in F` and let

\[
                         H_i=G/(F-\{x_i y_i\}).
\]

By inclusion-minimality, `H_i` is seven-connected and `H=H_i/x_i y_i`.

Let `U` be any separator of `H` of order at most six.  We first prove that
`z_i in U`.  If `z_i notin U`, it belongs to one component `C` of `H-U`.
Splitting `z_i` back into the adjacent vertices `x_i,y_i` only replaces a
vertex of `C` by a connected edge.  Every neighbour of either endpoint
outside `U` maps to a neighbour of `z_i` and hence also lies in `C`.
Therefore the split cannot join `C` to another component of `H-U`, and
`U` would separate the seven-connected graph `H_i`, a contradiction.
Thus every contracted image belongs to `U`.

Replace `z_i` in `U` by `x_i,y_i`.  The set

\[
                 U_i=(U-\{z_i\})\cup\{x_i,y_i\}       \tag{2.2}
\]

separates `H_i` and has order `|U|+1`.  Seven-connectivity of `H_i`
therefore gives `|U|+1>=7`.  Hence every separator of `H` of order at most
six has order exactly six.  The same argument applied to a hypothetical
separator of order at most five proves that none exists, so `H` is
six-connected.  (If `H` had seven vertices, six-connectivity would make
it `K_7`, contrary to the hypothesis.)

Now fix a six-separator `T`.  A component `C` of `H-T` has
`N_H(C) subseteq T`.  Since another component exists, `N_H(C)` is a
separator.  Six-connectivity gives `|N_H(C)|>=6`, and hence

\[
                             N_H(C)=T.                  \tag{2.3}
\]

Expanding all hit contraction images gives a bijection between the
components of `H-T` and those of `G-T^+`: splitting a boundary image
changes no vertex outside the boundary and creates no edge between two
old components.

It remains to prove the final, individual contact assertion.  In `H_i`,
the set

\[
                  T_i=(T-\{z_i\})\cup\{x_i,y_i\}
\]

is an actual seven-boundary with the same open components.  Each such
component has neighbourhood all of `T_i`, because `H_i` is
seven-connected.  Thus it has a neighbour of each of `x_i` and `y_i`.
Doing this for every edge of `F`, and using (2.3) for the ordinary members
of `T`, proves that every literal atom of `T^+` has a neighbour in every
expanded component.  Formula (2.1) is immediate.  \(\square\)

### Corollary 2.2 (the exact excess types)

If `m=1`, the expansion is already an actual seven-boundary and preserves
the one contracted named carrier.  It need not preserve every uncontracted
support-six carrier.  If `m=2` or `m=3`, its order is respectively eight
or nine.  Thus minimal bad simultaneous contractions never produce the
`(5,3)` order-eight type from the general trimming theorem; their only
excess types are

\[
                         (|T|,m)=(6,2),(6,3).           \tag{2.4}
\]

## 3. A fan rooted at the surviving core

We use the following elementary rooted-fan fact.

### Lemma 3.1 (forbidden-set fan)

Let `J` be `k`-connected, let `A,B` be disjoint vertex sets with
`|A|=r`, `|B|>=r`, and let `D` be disjoint from `A union B`.  If

\[
                         r+|D|\le k,
\]

then `J-D` contains `r` pairwise vertex-disjoint `A-B` paths, using every
vertex of `A` and distinct vertices of `B`.

### Proof

The graph `J-D` is `(k-|D|)`-connected and hence at least
`r`-connected.  If fewer than `r` disjoint `A-B` paths existed, the
set version of Menger's theorem would give a set `X` of order below `r`
meeting every `A-B` path.  Since both `A-X` and `B-X` are nonempty,
`J-(D union X)` would be disconnected, contrary to
`r`-connectivity of `J-D`.  \(\square\)

### Lemma 3.2 (a quotient clique cannot lie in the cut)

If `G` has no `K_7` minor, then for every `x_i y_i in F`,

\[
                             Q_i-T\ne\varnothing.       \tag{3.1}
\]

### Proof

Otherwise the literal clique `L_i=Q_i union {z_i}` of order five lies in
the six-set `T`.  Choose two components `C,D` of `H-T` and let
`w` be the one vertex of `T-L_i`.  The seven sets

\[
             \{v\}\ (v\in L_i),\qquad C\cup\{w\},\qquad D
\]

are connected and pairwise adjacent.  Indeed, both components are
`T`-full by (2.3), and `w` joins the last two bags.  They form a `K_7`
model in `H`, which expands to one in `G`.  \(\square\)

## 4. Three quotient components force `K_7`

### Theorem 4.1 (multi-component excess closure)

Suppose `m>=2`.  If `H-T` has at least three components, then `G`
contains a `K_7` minor.

### Proof

Fix an edge `x_i y_i in F`.  Put

\[
 R=Q_i\cap T,\qquad K=Q_i-T,
 \qquad r=|K|=4-|R|.
\]

By Lemma 3.2, `r>=1`.  Since `L_i-T` is a clique, all vertices of `K`
belong to one component `C` of `H-T`, viewed also as its expanded
component in `G-T^+`.  Choose two other components `D,E`.

Apply Lemma 3.1 in `G` with

\[
 A=K,qquad
 B=T^+-(R\cup\{x_i,y_i\}),qquad
 D_0=R\cup\{x_i,y_i\}.
\]

Here `|D_0|=|R|+2=6-r`, so `r+|D_0|=6<=7`; and

\[
 |B|=(6+m)-(6-r)=m+r>=r.
\]

We obtain `r` disjoint paths from the vertices of `K` to distinct
vertices of `B`.  Truncate every path at its first vertex of `T^+`.
Before that first hit it lies in `C`, because `C` is a component of
`G-T^+`.  Denote these truncated paths by `P_q` for `q in K`.

The following four bags are pairwise disjoint and pairwise adjacent:

\[
                  V(P_q)\quad(q\in K),
                  \qquad \{q\}\quad(q\in R).          \tag{4.1}
\]

They are disjoint by the fan construction, and their adjacency follows
from the literal clique `Q_i`, since every bag in (4.1) contains its named
vertex of `Q_i`.  They use four distinct boundary vertices: the endpoints
of the fan paths and the literal members of `R`.  None is `x_i` or `y_i`.

Use the fifth bag

\[
                              \{x_i,y_i\}.              \tag{4.2}
\]

It is connected and adjacent to every bag in (4.1), because it is the
fifth branch bag of the original model `M_i`.

The bags in (4.1) and (4.2) use exactly six vertices of `T^+`.  Since
`|T^+|=6+m>=8`, choose

\[
 w\in T^+-\left(\{x_i,y_i\}\cup
            \bigcup_{q\in Q_i}(B_q\cap T^+)\right),
\]

where `B_q` denotes the corresponding bag in (4.1).  Finally take

\[
                              D\cup\{w\},\qquad E.      \tag{4.3}
\]

The first set in (4.3) is connected because `w` has a neighbour in `D`.
It is adjacent to `E` because `w` also has a neighbour in `E`.  Each set
in (4.3) is adjacent to every bag in (4.1), using the distinct boundary
vertex contained in that bag, and to (4.2), using the individual endpoint
contacts from Theorem 2.1.  Consequently the four bags in (4.1), the one
bag in (4.2), and the two bags in (4.3) are seven pairwise disjoint,
pairwise adjacent connected subgraphs.  They are a literal `K_7` model.
\(\square\)

## 5. Exact remaining residue

Combining Theorems 2.1 and 4.1 gives the following audit-ready reduction.

### Corollary 5.1

For a nonempty inclusion-minimal bad contraction set `F`:

1. `m=1` gives an actual seven-separation preserving the contracted
   named carrier;
2. `m=2,3` and at least three quotient components give a literal `K_7`;
3. if neither conclusion occurs, then `m in {2,3}`, the unique relevant
   quotient obstruction is a six-cut containing every contracted image,
   and deleting that cut leaves exactly two components.  In the original
   graph every atom of the expanded eight- or nine-set has a neighbour in
   each component.

The last two-component alternative is not closed here.  Trimming one or
two atoms is impossible by the displayed individual contacts.  Closing it
requires either a labelled split of one of the two components, a
proper-minor state transfer, or a direct `K_7` construction using two
normalized cores.  Merely repeating the component-fullness argument gives
only six branch sets and is insufficient.
