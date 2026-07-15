# Three split models across an exact lifted separator

## Status

Proved and independently audited.

This is the positive counterpart to the indivisible-bundle `H`-Wege
barrier.  Whenever the quotient obstruction contains an actual separator
whose bundle-weight is exactly seven, expansion gives a literal
model-preserving exact-seven handoff.  No named support can straddle its
open shores.

The statement distinguishes hit and unhit bundles.  A hit contraction
image expands to a split edge in the adhesion.  An unhit split edge remains
intact in one open-shore component.  Thus all three split edges lie in the
adhesion only in the `(4,3)` collision; this cannot be asserted in the
`(5,2)` or `(6,1)` collisions.

## 1. Setup

Let `G` contain three pairwise vertex-disjoint support-six `K_5` models
`M_i`, where

\[
                 V(M_i)=Q_i\mathbin{\dot\cup}\{x_i,y_i\},
                 \qquad i=1,2,3,
\]

`Q_i` is the set of four singleton bags and `x_i y_i` is the unique
two-vertex bag.  Put

\[
             H=G/x_1y_1/x_2y_2/x_3y_3,
\]

write `z_i` for the image of `x_i y_i`, and put

\[
                         L_i=Q_i\cup\{z_i\}.
\]

The three `L_i` are pairwise disjoint literal `K_5` cliques in `H`.
For a set `T subseteq V(H)`, define

\[
                 \rho(T)=|T\cap\{z_1,z_2,z_3\}|.
\]

Its literal expansion in `G` is

\[
 T^+=\bigl(T-\{z_1,z_2,z_3\}\bigr)
     \cup\bigcup_{z_i\in T}\{x_i,y_i\}.             \tag{1.1}
\]

Thus `|T^+|=|T|+rho(T)`.

## 2. Exact component lifting

### Lemma 2.1

Let `T` be a vertex separator of `H`.  Splitting every unhit `z_i notin T`
back into the adjacent pair `x_i,y_i` gives a bijection between the
components of `H-T` and the components of `G-T^+`.

### Proof

Fix a component `C` of `H-T`.  Replace each vertex `z_i in C` by the edge
`x_i y_i`, assigning every former edge at `z_i` to the endpoint which
realized it in `G`.  The resulting graph is connected: every former
neighbor of `z_i` is adjacent to at least one of `x_i,y_i`, and the edge
`x_i y_i` joins the two possible neighbor classes.  Repeating this for all
unhit contraction images preserves connectedness.

No edge can join the expansions of two distinct components.  Such an edge
would contract to an edge between those components in `H-T`.  Conversely,
every vertex of `G-T^+` belongs to the expansion of one component of
`H-T`.  Hence the expanded components are exactly the components of
`G-T^+`.  \(\square\)

## 3. The decoder

### Theorem 3.1 (exact bundle-separator handoff)

Let `G` be seven-connected and let `T` be a separator of `H` satisfying

\[
                         |T|+\rho(T)=7.                \tag{3.1}
\]

Then the following hold.

1. `S=T^+` is an actual seven-boundary in `G`, and every component of
   `G-S` is `S`-full.
2. For each `i`, all vertices of `M_i-S` lie in at most one component
   `C_i` of `G-S`.  Consequently the complete named carrier `V(M_i)` is
   contained in the closed shore `S union C_i`; if `M_i subseteq S`, it
   may be assigned to either shore.
3. If `z_i in T`, then the literal edge `x_i y_i` lies in `S`.  If
   `z_i notin T`, then both `x_i,y_i` lie in `C_i`, so the whole split bag
   remains intact in one open shore.
4. After any nontrivial bipartition of the components of `G-S`, the
   resulting exact-seven separation assigns each of the three named models
   wholly to one of its two closed shores.  Every hit split edge remains a
   named edge of the adhesion.

In particular, when `|T|<=6`, equality (3.1) gives exactly one of

\[
             (|T|,\rho(T))=(4,3),(5,2),(6,1).          \tag{3.2}
\]

The `(4,3)` case puts all three split edges in the adhesion; the `(5,2)`
and `(6,1)` cases put exactly the hit two or one there and preserve every
unhit model intact on a side.

### Proof

By (1.1) and (3.1), `S=T^+` has order seven.  Lemma 2.1 and the fact that
`T` is a separator show that `G-S` has at least two nonempty components.
Thus `S` is the boundary of an actual exact-seven separation.

Let `C` be a component of `G-S`.  Its neighborhood is contained in `S`.
Since another component exists, `N_G(C)` separates `C` from a nonempty
part of the graph.  Seven-connectivity gives `|N_G(C)|>=7`; hence
`N_G(C)=S`.  This proves item 1.

Fix `i`.  The set `L_i=Q_i union {z_i}` is a clique in `H`.  Therefore
all vertices of `L_i-T` lie in at most one component of `H-T`: two such
vertices in different components would retain their clique edge.  Apply
Lemma 2.1 to that component.  If `z_i in T`, its expansion
`{x_i,y_i}` belongs to `S`, while every vertex of `Q_i-T` belongs to the
one expanded component.  If `z_i notin T`, the whole edge `x_i y_i` and
every vertex of `Q_i-T` belong to that component.  Vertices of `Q_i cap T`
belong to `S` in both cases.  This proves items 2 and 3.

Finally partition the components of `G-S` into two nonempty collections.
Every `C_i` belongs to exactly one collection, while a model contained in
`S` belongs to both closed shores and may be assigned arbitrarily.  Hence
each named carrier lies wholly in one closed shore.  This proves item 4.

If `|T|<=6`, then `1<=rho(T)<=3` and (3.1) gives precisely (3.2).
\(\square\)

## 4. RST/Mader corollary

Let

\[
                 (W;Y_1,X_1,\ldots,Y_n,X_n)
\]

be a Robertson--Seymour--Thomas form of a Mader obstruction in `H`.
For every `j` such that

* `Y_j-X_j` is nonempty; and
* `V(H)-(W union Y_j)` is nonempty,

the set

\[
                              T_j=W\cup X_j            \tag{4.1}
\]

is a separator: the off-boundary condition gives no edge from
`Y_j-X_j` to the other side after deleting `T_j`.

### Corollary 4.1 (exact RST collision decoder)

Under the hypotheses of Theorem 3.1, if an active RST cell in (4.1)
satisfies

\[
                         |T_j|+\rho(T_j)=7,             \tag{4.2}
\]

then it returns the model-preserving exact-seven handoff of Theorem 3.1.
If the left side of (4.2) is at most six, its literal expansion is a cut of
`G` of order at most six, contradicting seven-connectivity.

The same conclusion applies when `W` itself is a separator and
`|W|+rho(W)=7`.  This is exactly what happens in the normalized
three-bundle bottleneck from
[`../barriers/hc7_global_indivisible_bundle_hwege_barrier.md`](../barriers/hc7_global_indivisible_bundle_hwege_barrier.md):
`(|W|,rho(W))=(4,3)` and all three named split edges enter the adhesion.

### Proof

The separator assertion preceding the corollary is immediate from the RST
off-boundary property.  Expand (4.1) literally.  Its order is
`|T_j|+rho(T_j)`, so values at most six contradict seven-connectivity and
value seven invokes Theorem 3.1.  The argument for `W` is identical once
`W` is known to be a separator.  \(\square\)

## 5. Exact remaining gap

This decoder closes every **exact** separator-side bundle collision.  It
does not prove that an arbitrary RST obstruction has an active cell (or a
separating `W`) of expanded order seven.  Two residues remain outside the
theorem:

1. every separator exposed by the obstruction has expanded order at least
   eight; or
2. the RST partition blocks good paths without any one `W` or active-cell
   separator carrying the required named transition.

Nor does the theorem orient the returned separation into a closed packet
class or preserve a colouring state.  Its contribution is prior to those
steps: all three named minor carriers survive literally, hit split edges
are named adhesion edges, and unhit models remain intact in one open
shore.

## 6. Trust boundary

The following are proved here.

* exact component correspondence under parallel split-edge expansion;
* fullness of every lifted component;
* closed-shore containment of all three named models;
* exact adhesion placement for every hit split edge; and
* the RST active-cell decoder at expanded order seven.

The theorem does **not** claim that all three split edges lie in the
adhesion unless all three contraction images lie in `T`.  It does not
convert expanded order eight or nine to order seven, and it does not close
the resulting exact-seven adhesion.
