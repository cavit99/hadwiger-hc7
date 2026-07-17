# A rooted five-bag fan at one double-critical edge

**Status:** written proof; separate internal exact-file audit GREEN in
[`hc7_double_critical_edge_rooted_fan_audit.md`](hc7_double_critical_edge_rooted_fan_audit.md).
This note is local to one double-critical edge.  It constructs a labelled
`K_2 join F_5` minor, where `F_5=K_1 join P_4`; it does not construct a
`K_7` minor and does not prove `HC_7`.

## 1. Common-neighbour colour saturation

Let `G` be a seven-chromatic graph, let `xy` be an edge, and suppose

\[
                         \chi(G-\{x,y\})=5.                 \tag{1.1}
\]

Put `H=G-{x,y}` and fix a proper five-colouring
`phi:V(H) -> [5]`.  For each colour `i`, put

\[
 C_i=N_G(x)\cap N_G(y)\cap\phi^{-1}(i),
 \qquad
 C=N_G(x)\cap N_G(y).                                  \tag{1.2}
\]

### Lemma 1.1 (every colour has a common neighbour)

For every `i in [5]`, the set `C_i` is nonempty.  Consequently every
proper five-colouring of `H` uses all five colours on `C`.

#### Proof

Suppose `C_i` were empty.  Recolour every colour-`i` neighbour of `x`
with one new sixth colour, give `x` colour `i`, and give `y` the new
colour.  The recoloured vertices are pairwise nonadjacent because they had
one colour under `phi`.  None is adjacent to `y`, since otherwise it would
belong to `C_i`.  All other edges retain a proper colour pair, including
`xy`.  This gives a six-colouring of `G`, contrary to `chi(G)=7`.
\(\square\)

This is the one-colour, edge-local part of Proposition 3.3 and Corollary
3.1 of Kawarabayashi--Pedersen--Toft.  The proof above records explicitly
that no hypothesis about the other edges of `G` is used.

### Lemma 1.2 (set-valued Kempe completeness)

For every two distinct colours `i,j`, some connected component of

\[
                       H[\phi^{-1}(\{i,j\})]             \tag{1.3}
\]

meets both `C_i` and `C_j`.

#### Proof

Suppose no component in (1.3) met both sets.  Let `U` be the union of all
components of (1.3) which meet `C_i`, and interchange colours `i,j` on
`U`.  This is a proper Kempe change.  Every old colour-`i` common
neighbour lies in `U` and becomes colour `j`.  No old colour-`j` common
neighbour lies in `U`, by the supposition, and hence no common neighbour
becomes colour `i`.  The resulting proper five-colouring of `H` therefore
has no colour-`i` vertex in `C`, contradicting Lemma 1.1 applied to that
new colouring.  \(\square\)

Lemma 1.2 is deliberately set-valued: the component witnessing the pair
`i,j` may use different members of `C_i` from the components witnessing
other pairs incident with colour `i`.  It does not supply one fixed
rainbow transversal whose ten pairs all lie in the required Kempe
components.

## 2. The rooted fan minor

Write

\[
                            F_5=K_1\vee P_4,              \tag{2.1}
\]

where `vee` denotes graph join.  Thus `F_5` is a five-vertex maximal
outerplanar graph: one vertex is universal and the other four induce a
path.

### Theorem 2.1 (common-neighbour-rooted fan)

Assume in addition that `G` is seven-connected.  Choose one vertex
`c_i in C_i` for every `i in [5]`, and put

\[
                              T=\{c_1,\ldots,c_5\}.        \tag{2.2}
\]

Then `H` contains a `T`-rooted `F_5`-minor model.  Consequently `G`
contains an explicit minor model of

\[
                              K_2\vee F_5                 \tag{2.3}
\]

in which the two vertices of the `K_2` are the singleton branch sets
`{x}` and `{y}`.

#### Proof

The graph `H` is five-connected.  Indeed, a separator of `H` of order at
most four, together with `x,y`, would be a separator of `G` of order at
most six.

The five chosen vertices are distinct because they have distinct colours.
Apply the audited universal five-root fan theorem to the three-connected
graph `H` and terminal set `T`.  It gives five pairwise disjoint connected
branch sets, one containing each `c_i`, whose branch-set adjacency graph
contains `F_5`.

Every one of those branch sets is adjacent to both `x` and `y`, through
its contained common neighbour `c_i`.  The branch sets lie in `H`, so they
are disjoint from the adjacent singleton sets `{x},{y}`.  Adjoining those
two singleton branch sets therefore gives (2.3).  \(\square\)

## 3. Consequence for a private endpoint of a named near-clique model

The following location statement applies when the edge is the first edge
of the path normal form used in the conditional defect-one branch.  Let

\[
                         A_1,\ldots,A_5,L,R               \tag{3.1}
\]

be pairwise disjoint connected sets such that the `A_i` are pairwise
adjacent, each of `L,R` is adjacent to every `A_i`, and `L,R` are
anticomplete.  Suppose `G[L]` is an induced path, `x` is one endpoint and
`y` is its path neighbour.  Define

\[
 P_L(x)=\{i:N_G(A_i)\cap L=\{x\}\}.                    \tag{3.2}
\]

### Proposition 3.1 (the palette witnesses avoid private labels)

Under (1.1) and (3.1)--(3.2),

\[
 C\cap\left(L\cup R\cup\bigcup_{i\in P_L(x)}A_i\right)
 =\varnothing.                                         \tag{3.3}
\]

Moreover,

\[
                             d_G(x)\ge 6+|P_L(x)|.       \tag{3.4}
\]

In particular, if the path tuple is reduced under the five-support path
normalization, then `|P_L(x)|>=2` and `d_G(x)>=8`.

#### Proof

No member of `C` lies in `R`, because `R` is anticomplete to `L`.  No
member lies in `L`: in the induced path `G[L]`, the endpoint `x` has only
the neighbour `y`, so there is no third vertex of `L` adjacent to both.

If `i in P_L(x)`, then `y` has no neighbour in `A_i`.  Hence no vertex of
`A_i` is adjacent to both `x` and `y`, proving (3.3).

Lemma 1.1 supplies five distinct vertices in `C`.  For every
`i in P_L(x)`, choose a neighbour of `x` in `A_i`.  These chosen vertices
are distinct because the `A_i` are disjoint, and (3.3) says that they are
distinct from the five common neighbours.  Together with `y`, they give
(3.4).  The final assertion is the endpoint conclusion of the audited
five-support path normal form.  \(\square\)

If `L={x,y}` and this two-vertex path is reduced, the private-label sets
at `x` and `y` are disjoint and each has order at least two.  The same
count then gives

\[
                              |N_G(\{x,y\})|\ge9.         \tag{3.5}
\]

Thus the natural full-neighbourhood separation with open shore `{x,y}`
is not an order-seven separation in this two-vertex normal form.

## 4. Exact remaining gap

Among the four non-universal bags of the rooted `F_5` model, Theorem 2.1
guarantees only the edges of a path.  Three adjacencies among them are not
supplied.  A
`C`-meeting `K_5`-minor model in `H` would immediately give a `K_7` model
in `G` after adjoining `{x},{y}`, but neither Lemma 1.2 nor the universal
rooted-fan theorem supplies that upgrade.

In the conditional defect-one application there is also a pre-existing
named `K_6`-minor model on the five sets `A_i` and `R`.  Proposition 3.1
shows why a palette-to-label identification is unavailable: the five
edge-local common-neighbour witnesses avoid every branch set privately
owned by the endpoint `x`.  The remaining operation must therefore
compose the common-neighbour-rooted `F_5` with that named `K_6` model in a
label-preserving way, or turn failure of the composition into an exact
order-seven separation with compatible closed-shore colourings.

## 5. Dependencies

- [universal five-root fan theorem](../results/hc7_five_terminal_rooted_fan.md)
- [path normal form for the sixth branch set](../results/hc7_minimal_sixth_branch_set_path.md)
- K. Kawarabayashi, A. S. Pedersen and B. Toft,
  [*Double-critical graphs and complete minors*](https://doi.org/10.37236/359),
  Electronic Journal of Combinatorics **17** (2010), R87,
  Proposition 3.3 and Corollary 3.1.
