# A boundary-aligned low-degree adjacent pair

**Status:** written proof; separate internal audit GREEN.  This strengthens the audited
low-degree adjacent-pair theorem by forcing the second pole to lie on one
of the bounded anti-neighbourhood boundaries.  It does not prove `HC_7` or
synchronize the two closed-shore colourings.

## Theorem 1 (boundary-edge alignment)

Let `G` be a finite simple graph such that:

1. `G` is seven-connected and `chi(G)=7`;
2. `G` has no `K_7` minor; and
3. every proper minor of `G` is six-colourable.

Assume the established case `HC_6`.  Then there are a vertex `u`, a
component `C` of `G-N[u]`, and a vertex

\[
                         z\in N_G(C)\subseteq N(u)                 \tag{1.1}
\]

such that

\[
                7\le d_G(u)\le9,
        \qquad \chi(G-\{u,z\})=6.                                \tag{1.2}
\]

Put `S=N_G(C)`,

\[
                 A=G[C\cup S],\qquad B=G-C.                       \tag{1.3}
\]

Then `7<=|S|<=d_G(u)<=9`, both open sides contain a connected
subgraph adjacent to every vertex of `S`, and `uz` is an edge of `B`
with `z` on the common boundary `S`.

For a graph `Y` containing `S`, write `E(Y,S)` for the equality
partitions of `S` induced by proper six-colourings of `Y`; colour names are
discarded.

Moreover, every proper six-colouring `phi` of `G-uz` has the following
properties.  For some colour `alpha`,

\[
                         \phi(u)=\phi(z)=\alpha,                   \tag{1.4}
\]

no vertex of `S-\{z\}` has colour `alpha`, and the restriction of `phi`
to `A` is a proper six-colouring whose equality partition on `S` has
`\{z\}` as an exact singleton colour block.  If `Pi_phi` denotes this
partition, then

\[
            \Pi_\phi\in E(A,S),\qquad
            \Pi_\phi\notin E(B,S),                              \tag{1.5}
\]

while `Pi_phi` is induced on `S` by the colouring `phi|B-uz`.  The
particular colouring `phi|B` fails to colour the original opposite shore
only at the boundary edge `uz`.

## 1. At least seven neighbours of `u` meet the exterior

By the exact extremal bound for `K_7`-minor-free graphs, the average
degree of `G` is strictly below ten.  Seven-connectivity therefore gives
a vertex `u` with

\[
                              7\le d_G(u)\le9.                     \tag{1.6}
\]

The standard universal-vertex argument shows that `u` is not universal:
otherwise `chi(G-u)=6`, `HC_6` gives a `K_6` minor in `G-u`, and the
singleton branch set `\{u\}` completes it to a `K_7` minor.  Hence
`G-N[u]` is nonempty.

Let

\[
 T=\{x\in N(u):N(x)\cap (V(G)-N[u])\ne\varnothing\},
 \qquad R=N(u)-T.                                                  \tag{1.7}
\]

Every vertex of `R` has no neighbour outside `N[u]`.  The set `T`
separates the nonempty set `\{u\}\cup R` from `G-N[u]`: all neighbours
of `u` outside `R` lie in `T`, and by definition no vertex of `R` has a
neighbour in the exterior.  Seven-connectivity therefore gives

\[
                                  |T|\ge7.                         \tag{1.8}
\]

## 2. Some exterior-contacting neighbour is non-double-critical

We claim that some `z in T` satisfies

\[
                              \chi(G-\{u,z\})=6.                   \tag{2.1}
\]

Suppose not.  Deleting two vertices lowers chromatic number by at most
two, and every proper minor is six-colourable, so

\[
                         \chi(G-\{u,x\})=5
                         \quad\hbox{for every }x\in T.             \tag{2.2}
\]

Put `H=G[N(u)]`.  The standard common-neighbour recolouring argument
applied to (2.2) gives

\[
                              d_H(x)\ge5\quad(x\in T).             \tag{2.3}
\]

For completeness, fix a five-colouring of `G-\{u,x\}`.  Every one of
its five colours occurs on a common neighbour of `u` and `x`; otherwise
recolour all neighbours of `u` in a missing common-neighbour colour with
one new sixth colour, give `u` the old colour and `x` the new colour.  The
recoloured vertices are independent and none is adjacent to `x`, so this
would six-colour `G`.  The five common neighbours lie in `N(u)`, proving
(2.3).

If `x in R`, then every neighbour of `x` lies in `N[u]`.  Since
seven-connectivity gives `d_G(x)>=7` and `x` is adjacent to `u`,

\[
                              d_H(x)=d_G(x)-1\ge6.                 \tag{2.4}
\]

Equations (2.3)--(2.4) imply

\[
                                  \delta(H)\ge5.                   \tag{2.5}
\]

The audited degree-`7/8/9` local completion used in the proof of the
low-degree adjacent-pair theorem now applies verbatim.  Choose any
component `D` of `G-N[u]`, contract it to a vertex `c`, and retain
`\{u\}\cup V(H)\cup\{c\}`.  Seven-connectivity gives
`|N(c)\cap V(H)|=|N_G(D)|>=7`.  Under (2.5):

- for `d_G(u)=7`, the resulting nine-vertex minor has more than the
  extremal number of edges for a `K_7`-minor-free graph;
- for `d_G(u)=8`, the equality cases reduce to complements
  `C_8`, `C_4 dotunion C_4`, or `C_3 dotunion C_5`, each with the
  explicit audited `K_6` model in `H+c`; and
- for `d_G(u)=9`, the separately audited finite local-completion theorem
  gives a `K_6` model in `H+c` meeting `H`.

In each case the singleton `\{u\}` completes the `K_6` model to a
`K_7` model.  This contradiction proves (2.1).

Since `z in T`, it has a neighbour in `G-N[u]`.  Let `C` be the component
containing such a neighbour.  Then `z in N_G(C)=S`, which proves the
alignment (1.1).  The already audited bounded-separation argument gives
`S subseteq N(u)` and `7<=|S|<=d_G(u)<=9`; `C` is connected and full
to `S`, while the singleton `\{u\}` on the opposite side is full to `S`.

## 3. The exact singleton boundary transition

The edge deletion `G-uz` is a proper minor and hence has a proper
six-colouring `phi`.  Its ends must have the same colour: if
`phi(u) ne phi(z)`, restoring `uz` would give a six-colouring of `G`.
Write their common colour as `alpha`.

Every vertex of `S-\{z\}` remains adjacent to `u` in `G-uz`, so none has
colour `alpha`.  The graph `A=G[C\cup S]` does not contain `u`, and hence
does not contain the deleted edge `uz`.  Therefore `phi|A` is already a
proper colouring of the original `A`, and `\{z\}` is exactly its
`alpha`-coloured block on `S`.

On the opposite side, `phi|B` becomes improper only when the single edge
`uz` is restored.  Hence `Pi_phi` is induced by a proper colouring of
`B-uz`.  It cannot extend through the original `B`: if it did, permute
the colours of that extension to agree with `phi|A` on every block of
`Pi_phi` and glue the two colourings across `S`.  This would six-colour
`G`.  Thus (1.5) holds and the final assertion follows.

### Corollary 3.1 (the degree-seven trace)

If `d_G(u)=7`, then `S=N(u)`, and the equality partition induced by
`phi` on `S` has exactly the form

\[
                    \{z\}\mid\{a,b\}\mid
                    \{s_1\}\mid\{s_2\}\mid\{s_3\}\mid\{s_4\},   \tag{3.1}
\]

where `ab` is a nonedge of `G[S]`.

#### Proof

The inclusions and bounds already proved give
`7<=|S|<=d_G(u)=7`, hence `S=N(u)`.  In a six-colouring of `G-uz`, the
vertex `u` has a neighbour in every colour different from `alpha`;
otherwise recolouring `u` with a missing colour would make the restored
edge proper and six-colour `G`.  Its neighbours other than `z` are the
six vertices of `S-\{z\}`.  All five non-`alpha` colours therefore occur
there.  Exactly one occurs twice and the other four occur once.  The two
vertices receiving the repeated colour are nonadjacent because `phi` is
proper on `G-uz` and the only deleted edge is `uz`.  This proves (3.1).

### Corollary 3.2 (matching-state normalization at degree seven)

Continue to assume `d_G(u)=7`, and put

\[
                              F=\overline{G[S]}.
\]

For `Y in \{A,B\}`, let `M_z(Y)` consist of the matchings `M` in
`F-z` for which the partition

\[
                 \{z\}\mid\{xy:xy\in M\}\mid
                 \{\{v\}:v\in S-(\{z\}\cup V(M))\}               \tag{3.2}
\]

belongs to `E(Y,S)`.  Then

\[
 M_z(A)\ne\varnothing,\qquad M_z(B)\ne\varnothing,\qquad
 M_z(A)\cap M_z(B)=\varnothing,                                  \tag{3.3}
\]

every matching in either family has order one, two, or three, and
`M_z(A)` contains the one-edge matching `\{ab\}` from Corollary 3.1.

#### Proof

The contraction-critical neighbourhood bound gives
`alpha(G[S])<=2`, so every colour block has order at most two.  A proper
boundary partition with singleton block `\{z\}` is therefore encoded by
a matching of `F-z`.  Since it has at most six blocks on seven vertices,
that matching is nonempty, and it has order at most three.

Corollary 3.1 supplies `\{ab\} in M_z(A)`.  To see that `M_z(B)` is
nonempty, contract the connected set `C\cup\{z\}`.  Fullness of `C` makes
the contracted vertex adjacent to every member of `S-\{z\}`.  Expanding
`z` with its colour and restricting a six-colouring of this proper minor
to `B` gives a proper colouring in which `\{z\}` is an exact boundary
block.  Finally, a common matching would give the same equality partition
on both closed shores; aligning colour names and gluing would six-colour
`G`.  Thus the two families are disjoint.

## 4. Exact contribution and remaining gap

The theorem aligns three objects at one low-degree vertex:

1. the non-double-critical adjacent-pair palette and linkage framework;
2. an actual full separation of order seven, eight, or nine; and
3. a boundary singleton trace whose unique obstruction on the opposite
   shore is the named edge `uz`.

It does not align the remaining blocks of that trace with a proper
six-colouring of `B`.  The next positive theorem must use the five
edge-critical Kempe connections or the five disjoint palette paths to
repair `uz`, produce an explicit `K_7`-minor model, or return a strictly
smaller full separation with preserved boundary-colouring data.

## Inputs

- the audited low-degree adjacent-pair and bounded-separation theorem;
- the separately audited degree-nine local-completion theorem;
- the exact extremal bound for `K_7` minors;
- the established case `HC_6`; and
- the standard five-common-neighbour consequence for a double-critical
  edge, whose elementary recolouring proof is included above.
