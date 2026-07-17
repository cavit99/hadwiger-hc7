# A labelled near-`K_7` model and the internal-edge colouring fork

**Status:** written proof; separate internal audit GREEN.

This note works inside the conditional defect-one branch of the current
`HC_7` programme.  It proves that every simplicial component of the
two-tree component-contact graph belongs to a labelled `K_7`-minor model
with one missing adjacency.  It then gives the exact chromatic response to
an edge inside that component and an explicit sufficient condition which
repairs the missing adjacency.

The note does not align colour classes with the named branch sets, does not
prove an order-seven upper bound for a returned separation, and does not
prove `HC_7`.

## 1. Conditional setup

Let `G` be seven-chromatic, let every proper minor of `G` be
six-colourable, and assume that `G` has no `K_7` minor.  Use the setup of
the audited component-defect theorem at a fixed valid cut.  Thus

\[
                  A_1=C_q,\qquad A_2=U_q,\qquad A_3=\{z\}
                                                                    \tag{1.1}
\]

are three pairwise disjoint, connected, pairwise adjacent branch sets, and
`J` is a four-partite component-contact graph with all four parts nonempty.
Assume that `J` is a two-tree.  Let `l` be a simplicial vertex of `J`, let
its two neighbours be `m,n`, and denote their represented connected
subgraphs of `G` by `L,M,N`, respectively.

All represented components are disjoint from the three branch sets in
(1.1), are mutually disjoint, and are adjacent to every set in (1.1).  An
edge of `J` records an actual edge between the represented connected
subgraphs.

## 2. The labelled near-complete model

### Theorem 2.1 (clique-tree anchoring)

There is a vertex `r` of `J-l` adjacent to both `m,n`.  If `R` denotes its
represented connected subgraph, then

\[
                         A_1,A_2,A_3,M,N,R                         \tag{2.1}
\]

are the branch sets of an explicit `K_6`-minor model disjoint from `L`.
Moreover,

\[
                         A_1,A_2,A_3,M,N,L,R                       \tag{2.2}
\]

are the branch sets of a `K_7^-`-minor model whose only missing required
adjacency is between `L` and `R`.

Here `K_7^-` denotes `K_7` with one edge deleted.

#### Proof

A two-tree is obtained from a triangle by repeatedly adding a new vertex
on an existing edge.  Deleting a simplicial degree-two vertex from a
two-tree of order at least four leaves a two-tree.  The edge `mn` belongs
to a triangle of that remaining two-tree: if `l` was added on `mn`, this
edge already belonged to a triangle before `l` was added; if `l` was a
vertex of the initial triangle, its having degree two forces all later
vertices to have been added in the two-tree on the edge opposite `l`, and
that edge again lies in a triangle not using `l`.  Hence a vertex `r` as
claimed exists.

The three sets in (1.1) are pairwise adjacent.  Each of `M,N,R` is adjacent
to all three, and the triangle `mnr` in `J` supplies the three adjacencies
among `M,N,R`.  This proves (2.1).  The simplicial vertex `l` is adjacent
to `m,n`, and its represented subgraph `L` is adjacent to every set in
(1.1).  Thus all pairs in (2.2) are adjacent except possibly `L,R`, proving
the second assertion.  If `L` and `R` were adjacent, the seven displayed
sets would already be a `K_7`-minor model, contrary to the host assumption.
\(\square\)

The fixed model (2.1) survives every deletion or contraction supported
inside `L`.  This is a label-preserving fact about a displayed model, not a
chromatic lower bound for the graph left after the operation.

## 3. The exact response to an internal edge

Let `xy` be an edge of `G[L]`, and put

\[
                              H=G-\{x,y\}.                         \tag{3.1}
\]

For a colouring `phi` of `H`, let

\[
 M_x(\phi)=[6]-\phi(N_G(x)-\{y\}),\qquad
 M_y(\phi)=[6]-\phi(N_G(y)-\{x\}).                               \tag{3.2}
\]

### Theorem 3.1 (five-or-six edge fork)

For every edge `xy` of `G[L]`,

\[
                  \chi(G/xy)=6,\qquad 5\le \chi(H)\le6.           \tag{3.3}
\]

Exactly one of the following chromatic cases occurs.

1. **Five-colour case.**  The edge `xy` is double-critical:
   `chi(H)=5`.  In every proper five-colouring of `H`, each colour occurs
   on a common neighbour of `x,y`.  More strongly, for every nonempty
   ordered list of distinct colours
   `j_1,...,j_s` there is an `x`--`y` path whose internal vertices have,
   in order, colours `j_1,...,j_s`.
2. **Six-colour case.**  One has `chi(H)=6`.  Every proper six-colouring
   `phi` of `H` satisfies at least one of the following three alternatives:

   \[
      M_x(\phi)=\varnothing;qquad M_y(\phi)=\varnothing;qquad
      M_x(\phi)=M_y(\phi)=\{\alpha\}.                             \tag{3.4}
   \]

   At least one six-colouring realizes the common-singleton alternative in
   (3.4).

#### Proof

Every graph in (3.3) is a proper minor or subgraph obtained by vertex
deletion, so the upper bounds are six.  If `G/xy` had a five-colouring,
retain the contracted vertex's colour on `x` and give `y` a fresh sixth
colour.  This would six-colour `G`, a contradiction.  Thus
`chi(G/xy)=6`.  If `H` had a four-colouring, give `x,y` two distinct fresh
colours; this would again six-colour `G`.  Hence (3.3) holds.

Suppose first that `H` has a five-colouring `phi`.  Extend it to `G-xy` by
giving both `x,y` a fresh sixth colour.  Let
`pi=(6,j_1,...,j_s)` be the cyclic permutation of the displayed colours,
fixing the other colours.  Direct every edge `uv` from `u` to `v` whenever
the colour of `v` is `pi` applied to the colour of `u`, and let `W` be the
set reachable from `x` by directed paths.  If `y` were not in `W`, applying
`pi` to the colours of all vertices in `W` would remain proper: a newly
monochromatic edge crossing from `W` to its complement would itself be the
next directed step and would put its outside end in `W`.  The recolouring
would give `x` a colour different from the unchanged colour `6` on `y`, so
restoring `xy` would six-colour `G`.

Therefore `y` is reachable.  Take a shortest directed `x`--`y` path.  Its
colours follow the cycle `6,j_1,...,j_s,6`.  The only vertices coloured `6`
are `x,y`, so this path cannot complete the colour cycle before reaching
`y`; hence its internal colours are exactly `j_1,...,j_s` in that order.
The case `s=1` says precisely that every colour class contains a common
neighbour of `x,y`.

Suppose now that `H` is six-chromatic and let `phi` be a six-colouring.
If distinct colours `a in M_x(phi)` and `b in M_y(phi)` existed, assigning
`a` to `x` and `b` to `y` would six-colour `G`.  Thus the two missing sets
have no distinct representatives, which is equivalent to (3.4).

Finally, restrict a six-colouring of `G/xy` to `H`, and let `alpha` be the
colour of the contracted vertex.  It is absent from both endpoint
neighbourhoods.  No second colour can be absent at either endpoint, since
that colour and `alpha` could be assigned to the two ends in the suitable
order.  Hence both missing sets equal `{alpha}`.  \(\square\)

The generalized Kempe-chain argument in the five-colour case is the local
edge version of Proposition 3.3 of Kawarabayashi--Pedersen--Toft,
*Double-critical graphs and complete minors*, Electronic Journal of
Combinatorics 17 (2010), R87.  Its proof above uses only that the selected
edge is double-critical; it does not assume that every edge of `G` is
double-critical.

## 4. A literal label-alignment condition which repairs the model

Write

\[
                         B_1=A_1,\ B_2=A_2,\ B_3=A_3,
                         \ B_4=M,\ B_5=N.                        \tag{4.1}
\]

These are the five common branch sets of the near-complete model (2.2).

### Theorem 4.1 (common-neighbour repair)

Suppose `xy` is an edge of a spanning tree `T` of `G[L]`.  If

\[
                  N_G(x)\cap N_G(y)\cap B_i\ne\varnothing
                         \qquad(1\le i\le5),                       \tag{4.2}
\]

then the graph `G` contains an explicit `K_7`-minor model.

#### Proof

Delete `xy` from `T`, and let `L_x,L_y` be the vertex sets of the two
resulting tree components containing `x,y`, respectively.  They are
nonempty, disjoint, connected, and adjacent through `xy`.  For each `i`,
choose a vertex `w_i` in the intersection in (4.2).  Since the branch sets
`B_i` are disjoint, the chosen vertices are distinct.  The edge `xw_i`
makes `L_x` adjacent to `B_i`, while `yw_i` makes `L_y` adjacent to `B_i`.
The five sets `B_i` are pairwise adjacent.  Consequently

\[
                           L_x,L_y,B_1,B_2,B_3,B_4,B_5             \tag{4.3}
\]

are seven pairwise disjoint, connected, pairwise adjacent branch sets.
They are the required `K_7`-minor model.  \(\square\)

### Corollary 4.2 (exact obstruction in the five-colour case)

If `G` has no `K_7` minor and `xy` is a double-critical edge of a spanning
tree of `G[L]`, then every five-colouring of `G-{x,y}` has all five colours
on the common neighbourhood of `x,y`, but at least one named branch set
in (4.1) contains no common neighbour of `x,y`.

Thus the uncoloured path existence and the colour saturation are complete;
the missing assertion is their alignment with the five literal branch-set
labels.

## 5. What this theorem changes, and what it does not

Theorems 2.1--4.1 give a finite, operation-specific fork at every internal
edge of `L`.

- The old unrooted-minor regeneration step is redundant: the fixed
  `K_6` model (2.1) already avoids all of `L`.
- In the five-colour case, ordered generalized Kempe paths exist for every
  colour sequence.  A `K_7` follows as soon as their one-colour witnesses
  occupy the five named common branch sets.
- In the six-colour case, the exact missing-colour cover and a canonical
  common-hole colouring are available.

Neither alternative currently preserves or replaces the original
colour-matched path, its valid cut, the four protected labels, and the
defect-one component selection.  In particular, the theorem does not prove
that an internal operation yields a smaller eligible component in the
original graph.

The remaining positive theorem must use the `K_7`-minor exclusion and the
literal placement of the colour witnesses to prove one of the following:

1. a repair satisfying (4.2), possibly after a label-preserving rerouting;
2. a full-neighbourhood separation of order exactly seven with compatible
   closed-shore six-colourings; or
3. another complete valid defect-one configuration in the same host with a
   strictly smaller lifted simplicial component.

Palette data alone cannot supply this conclusion: it does not identify a
colour class with a fixed minor branch set.

## 6. Dependencies

- [component-contact defect and its two-tree equality case](../results/hc7_component_contact_defect_theorem.md)
- [normal form around a simplicial component](../results/hc7_defect_one_simplicial_normalization.md)
- Kawarabayashi, Pedersen and Toft, Proposition 3.3 in the paper cited
  after Theorem 3.1.
