# Full exterior components force a common-root exchange

**Status:** written proof; separately audited GREEN.  This theorem does not
prove `HC_7`.

## Theorem 1 (lower boundary or common-root exchange)

Let `G` be a finite simple graph such that:

1. `G` is seven-connected and `chi(G)=7`;
2. `G` has no `K_7` minor; and
3. every proper minor of `G` is six-colourable.

Let `u` have degree eight or nine, put `X=N_G(u)` and `H=G[X]`, and suppose
that `G-N[u]` has at least two components.  For a labelled proper
five-colouring `phi` of `H`, let `R(phi)` be the set of exterior components
through which `phi` does not extend with palette `[6]`.

Assume that every `R(phi)` is a singleton.  Then at least one of the
following holds.

1. **Lower boundary order.**  Some exterior component `E` is not adjacent
   to every vertex of `X`.  Its literal boundary `S_E=N_G(E)` satisfies

   \[
                     7\le |S_E|\le d_G(u)-1.           \tag{1.1}
   \]

   The graphs `G[E union S_E]` and `G-E` form the canonical bounded full
   separation, and component-uniform alignment supplies

   \[
    z_E\in S_E,\qquad \chi(G-\{u,z_E\})=6.             \tag{1.2}
   \]

2. **Full-component common root.**  There are exactly two exterior
   components `C,D`, both adjacent to every vertex of `X`.  The graph `H`
   is three-degenerate.  There are labelled proper five-colourings
   `phi,psi` and a vertex `x in X` such that

   \[
           R(\phi)=\{C\},\qquad R(\psi)=\{D\},          \tag{1.3}
   \]

   and `psi` is obtained from `phi` by changing only the colour of `x`.
   If that change is from `alpha` to `beta`, failed lifting gives paths

   \[
    xP_Cy_C,\qquad xP_Dy_D,                            \tag{1.4}
   \]

   with nonempty interiors respectively in `C,D`, where `xy_C,xy_D` are
   nonedges of `H`.  The paths have the same literal boundary root `x` and

   \[
                 K_6\not\preccurlyeq H+xy_C+xy_D.      \tag{1.5}
   \]

   Moreover `chi(G-x)=6`.  A specific six-colouring of `G-x` has colour
   `alpha` on a neighbour of `x` in `C`, colour `beta` on a neighbour of
   `x` in `D`, and the sixth colour on `u`.

The first outcome lowers the separator order but does not decrease the
literal component order.  The second reduces the remaining task to finding
a `K_6` model in `G-x` whose six branch sets all meet `N_G(x)`; the known
case `HC_6` gives an unrooted `K_6` model but not this rooted conclusion.

## 1. The non-full alternative

For every exterior component `E`, seven-connectivity gives
`7<=|N_G(E)|<=|X|`.  If `N_G(E) ne X`, this proves (1.1).  The separation
claim and (1.2) are exactly the separately audited component-uniform
boundary-alignment theorem.  Hence only the case in which every exterior
component is `X`-full remains.

Fix two such components `C,D` for the next two sections.

## 2. Compact `K_4` exclusion

For every two-set `Z={z_1,z_2} subseteq X`,

\[
                         K_4\not\preccurlyeq H-Z.       \tag{2.1}
\]

Otherwise let `B_1,...,B_4` be a `K_4` model in `H-Z`.  The seven sets

\[
 B_1,B_2,B_3,B_4,\quad \{u\},\quad C\cup\{z_1\},
 \quad D\cup\{z_2\}                                  \tag{2.2}
\]

are disjoint and connected.  Each of `u,C,D` is adjacent to every vertex
of `X`; the two anchored component bags meet because each component is
adjacent to the other bag's anchor.  Thus all 21 branch-set adjacencies are
present, giving a `K_7` model.  This proves (2.1).

## 3. Three-degeneracy of the boundary

Suppose an induced subgraph `F` of `H` has minimum degree at least four,
and put `h=|V(F)|`.  Contract `C,D`, retain `u`, and delete every other
vertex.  The resulting minor is `overline K_3 vee F`, with

\[
                         3h+|E(F)|                    \tag{3.1}
\]

edges on `h+3` vertices.  Mader's exact `K_7` extremal bound and
`delta(F)>=4` give opposite inequalities `|E(F)|<=2h` and
`|E(F)|>=2h`.  Hence `F` is four-regular.  It is connected: every
four-regular component has at least five vertices, while `h<=9`.

Fix an edge `xy` of `F`.  By (2.1), `J=F-{x,y}` is `K_4`-minor-free.  It
has `n=h-2` vertices and

\[
 |E(J)|=2h-7=2n-3.                                   \tag{3.2}
\]

Equality in the exact `K_4` extremal theorem makes `J` a 2-tree.  It has
at least two vertices of degree two.  Since every vertex had degree four
in `F`, a vertex has degree two in `J` exactly when it is adjacent to both
`x` and `y`.  Thus every edge of `F` has at least two common neighbours.

We classify connected four-regular graphs with that property.  Fix `v`.
Every member of `N_F(v)` has at least two neighbours in the four-vertex
graph `F[N_F(v)]`, so that graph is `C_4`, `K_4-e`, or `K_4`.

- If it is `K_4`, the component is `K_5`, because all five degrees are
  saturated.
- If it is `K_4-e`, an endpoint `a` of the missing edge has one neighbour
  outside `\{v\} union N_F(v)`.  The edge to that neighbour cannot have
  two common neighbours: `v` is not adjacent to the outside vertex, while
  the two possible common neighbours in `N_F(v)` already have degree four.
- If it is `C_4`, each cycle vertex has one outside neighbour.  For the
  edge from one cycle vertex to its outside neighbour to have two common
  neighbours, that outside vertex must meet both adjacent cycle vertices.
  Applying the same condition once more forces it to meet the opposite
  cycle vertex.  All degrees are then saturated and `F` is the octahedron
  `K_{2,2,2}`.

The `K_5` case gives a `K_7` model directly: choose two vertices
`z_1,z_2 in X-V(F)` and use the five singleton clique bags together with
`C union {z_1}` and `D union {z_2}`.  In the octahedral case, its standard
`K_4` model together with two vertices of `X-V(F)` contradicts (2.1).
Both choices are possible because `|X|>=8`.  Therefore no such `F` exists,
and `H` is three-degenerate.

## 4. Single-vertex recolouring connectivity

For completeness, all labelled proper five-colourings of a
three-degenerate graph are connected by legal single-vertex recolourings.
Induct on the number of vertices.  Delete a vertex `v` of degree at most
three and lift a recolouring sequence supplied by induction.  If a
neighbour is about to receive the current colour of `v`, at least two of
the five colours are absent from `N(v)`; first move `v` to another absent
colour.  At the end move `v` to its target colour, which is absent from its
neighbours in the target colouring.

Under the singleton-rejection hypothesis, the map sending a boundary
colouring to the unique member of `R(phi)` is nonconstant: every exterior
component occurs at its private component-deletion colouring.  Connectivity
therefore gives adjacent colourings `phi,psi` with different labels and
differing only at one vertex `x`.  If `x` changes from `alpha` to `beta`,
properness before and after the move says that `x` has no neighbour of
either colour in `H`.  Hence `{x}` is the operated component of
`H[alpha,beta]`.

The one-interchange lifting argument applied forward on the component that
accepts `phi` and in reverse on the component that accepts `psi` gives the
two paths in (1.4).  Their interiors lie in distinct exterior components,
so simultaneous contraction realizes `H+xy_C+xy_D` as a minor of `G-u`,
even if `y_C=y_D`.  A `K_6` model in the augmented graph would lift to six
bags each meeting `X`, and `{u}` would complete a `K_7` model.  This proves
(1.3)--(1.5), once the number of full components is determined.

## 5. Exactly two full exterior components

Include the singleton `{u}` among the components of `G-X`; every such
component is connected, pairwise anticomplete to the others, and adjacent
to every vertex of `X`.  Let their number be `q`.

If `q>=5` and `H` has an edge `ab`, choose five full components, leave one
unanchored, and attach four others to distinct vertices of `X-{a,b}`.
Together with `{a},{b}`, these are seven pairwise adjacent connected bags.
If `H` is edgeless, contract `u union X`, colour the resulting proper minor,
and pull back after deleting all but one exterior component.  This gives,
for every retained component, a colouring in which `X` is one boundary
colour class.  Align and glue those colourings, then give `u` another
colour.  Thus `q>=5` is impossible.

It remains possible that `q=4`.  If `H` contains a triangle, leave one
full component unanchored, attach the other three to distinct vertices of
`X` outside the triangle, and use the three triangle vertices as singleton
bags.  This is again an explicit `K_7` model.  Hence `H` is triangle-free.

Every triangle-free graph on at most nine vertices is three-colourable.
If its maximum degree is at most three, this is Brooks' theorem applied
componentwise.  Otherwise choose a vertex of degree at least four.  Its
neighbourhood is independent, and its antineighbourhood has at most four
vertices and is bipartite.  Colour the neighbourhood with one colour, the
chosen vertex with a second, and the antineighbourhood with the second and
third colours.

Split colour classes if necessary, and let
`X=S_1 dotunion S_2 dotunion S_3` be a partition into three nonempty
independent blocks.  To colour the side of one retained exterior component,
contract each of the other three full components of `G-X` together with a
different block.  The three connected images form a clique.  Six-colour
this proper minor, delete those other components, and expand the blocks.
The three block colours are distinct.  Repeat for every retained exterior
component, align the three colours, and glue; a fourth colour on `u`
six-colours `G`.  Thus `q=4` is impossible.

Since there are at least two exterior components, `q>=3`; the preceding
paragraphs give `q=3`.  Therefore `G-N[u]` has exactly the two components
`C,D`.

## 6. The exact rooted residue

Orient (1.3) so that `phi(x)=alpha` and `psi(x)=beta`.  The colouring
`psi` extends through `C`, and reverse lifting gives `xP_Cy_C`; the
neighbour of `x` on this path has colour `alpha`.  The colouring `phi`
extends through `D`, and forward lifting gives `xP_Dy_D`; the neighbour of
`x` on this path has colour `beta`.

Delete `x`, combine the `psi`-extension through `C` with the
`phi`-extension through `D`, and give `u` colour six.  The two boundary
colourings agree on `X-{x}`, and `C,D` are anticomplete, so this is a proper
six-colouring of `G-x` with the asserted contacts.  A five-colouring of
`G-x` would extend to a six-colouring of `G` by giving `x` a fresh colour.
Therefore `chi(G-x)=6`.

The established case `HC_6` supplies a `K_6` minor in `G-x`.  The proof
does not show that all six branch sets meet `N_G(x)`, so it cannot add the
singleton `{x}`.  That rooted completion is the exact remaining inference.

## Inputs

- [component-uniform boundary alignment](hc7_component_uniform_boundary_alignment.md)
- [component-deletion Kempe exchange](hc7_component_deletion_kempe_exchange.md)
- W. Mader's exact extremal bounds for `K_4` and `K_7` minors.
- The established case `HC_6` and Brooks' theorem.
