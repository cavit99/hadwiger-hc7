# Exact-block Kempe transitions across two full shores

**Status:** written proof; separate internal audit GREEN in
[`hc7_two_full_shore_exact_block_kempe_transition_audit.md`](hc7_two_full_shore_exact_block_kempe_transition_audit.md).

This note gives an unbounded two-shore consequence of a
`K_5`-minor-free boundary.  It replaces the order bound in the earlier
[two-shore Kempe-distance theorem](../results/hc7_two_shore_kempe_list_dichotomy.md)
by the exact minor exclusion and, more importantly, preserves any prescribed
independent boundary set as one fixed colour class throughout the
reconfiguration.  It does not prove that the two shores admit a common
boundary colouring.

## 1. Setting and notation

Let

\[
                 V(G)=A\mathbin{\dot\cup}B\mathbin{\dot\cup}D,
                 \qquad E_G(A,D)=\varnothing,                 \tag{1.1}
\]

where `A` and `D` are nonempty and induce connected subgraphs.  Assume that
both `A` and `D` are **full to** `B`: every literal vertex of `B` has a
neighbour in each of `A` and `D`.  Suppose

1. `G` is not six-colourable;
2. every proper minor of `G` is six-colourable; and
3. `G[B]` has no `K_5` minor.

Fix a nonempty independent set `I subseteq B`.  A labelled proper
six-colouring of `G[B]` is **exact at `I`** when colour six occurs on `B`
exactly at `I`.

Let `Gamma_I(B)` be the graph whose vertices are the exact-`I` boundary
colourings.  Two colourings are adjacent when one is obtained from the other
by interchanging two colours from `{1,...,5}` on one connected component of
the corresponding two-colour subgraph of `G[B-I]`.

For an exact-`I` boundary colouring `phi`, write

\[
 \operatorname{Ext}(\phi)=
 \{A: \phi\text{ extends through }G[A\cup B]\}
 \cup
 \{D: \phi\text{ extends through }G[D\cup B]\}.       \tag{1.2}
\]

## 2. Exact-block anchors and connectivity

### Theorem 2.1

Under the hypotheses of Section 1:

1. each closed shore has a proper six-colouring exact at `I`;
2. `Gamma_I(B)` is connected; and
3. no vertex of `Gamma_I(B)` extends through both closed shores.

#### Proof

Contract the connected set `D union I` to one vertex `z`.  It is connected
because `D` is connected and every vertex of `I` has a neighbour in `D`.
The contraction gives a proper minor, so it has a proper six-colouring.
Restrict that colouring to `A union (B-I)` and give every vertex of `I` the
colour of `z`.

This pullback is proper.  The set `I` is independent.  Every vertex of
`B-I` is adjacent to `z` in the minor because `D` is full to `B`, and every
vertex of `A` having a neighbour in `I` is also adjacent to `z` in the
minor.  Thus the contraction colour occurs on the boundary exactly at `I`.
Renaming it as colour six gives the required colouring of `G[A union B]`.
Contracting `A union I` gives the symmetric colouring of `G[D union B]`.

Exact-`I` boundary colourings are in bijection with labelled proper
five-colourings of `G[B-I]`: delete `I`, or add it back in the fixed sixth
colour.  The graph `G[B-I]` is `K_5`-minor-free.  The main theorem of Las
Vergnas and Meyniel says that all labelled five-colourings of a
`K_5`-minor-free graph are Kempe equivalent.  Applied componentwise if
necessary, it makes `Gamma_I(B)` connected.

Finally, a boundary colouring extending through both closed shores would
glue, because `A` and `D` are anticomplete.  It would give a proper
six-colouring of `G`, contrary to hypothesis 1.  \(\square\)

## 3. The two-shore transition

### Theorem 3.1 (exact-block distance dichotomy)

Let

\[
                         \phi_0,\phi_1,\ldots,\phi_k    \tag{3.1}
\]

be a shortest path in `Gamma_I(B)` whose first vertex extends through the
`A`-shore and whose last vertex extends through the `D`-shore, minimized
over all choices of its endpoints.  Then `k>=1`, every colouring on the path
keeps `I` as the same exact labelled colour class, and exactly one of the
following holds.

1. **One boundary interchange.**  One has `k=1`.  Suppose the interchange
   swaps colours `alpha,beta` on a boundary two-colour component `W`.
   There is an `alpha`--`beta` path from `W` to a different boundary
   component of `G[B-I][alpha,beta]` with nonempty interior in `A`, and
   another such path, for the same colours and the same operated component
   `W`, with nonempty interior in `D`.  The two interiors are disjoint.

2. **Two list-critical shore subgraphs.**  One has `k>=2`.  Every internal
   colouring `phi_i`, `1<=i<=k-1`, extends through neither closed shore.
   Fix one such `phi_i`.  Each open shore contains a connected induced
   vertex-minimal subgraph which is not colourable from the lists left by
   `phi_i` on its literal boundary neighbours.  More precisely, if

   \[
      L_A(v)=\{1,\ldots,6\}
             -\phi_i(N_G(v)\cap B),                   \tag{3.2}
   \]

   then there is a connected induced `K_A subseteq G[A]` which is not
   `L_A`-colourable and satisfies

   \[
             d_{K_A}(v)\ge |L_A(v)|
               =6-|\phi_i(N_G(v)\cap B)|              \tag{3.3}
   \]

   for every `v in V(K_A)`.  The analogous statement holds for a disjoint
   subgraph `K_D subseteq G[D]`.

#### Proof

The endpoint sets in `Gamma_I(B)` are nonempty and disjoint by Theorem 2.1,
so (3.1) exists and `k>=1`.  Its minimality gives

\[
 \phi_i\text{ does not extend through }A\quad(i>0),
 \qquad
 \phi_i\text{ does not extend through }D\quad(i<k).   \tag{3.4}
\]

Suppose first that `k=1`.  Extend `phi_0` through `A`.  In that extension,
consider the full `alpha`--`beta` component containing the operated
boundary component `W`.  If it met no other boundary component of those two
colours, interchanging the colours on the full component would extend
`phi_1` through `A`, contrary to (3.4).  Hence it meets another boundary
component.  A shortest path from `W` to the first such component has no
internal boundary vertex, so its nonempty interior lies in `A`.  Apply the
same argument backwards to an extension of `phi_1` through `D`.  The two
path interiors are disjoint because the open shores are disjoint.  This is
outcome 1.

Now let `k>=2` and fix an internal `phi_i`.  Equation (3.4) says that it is
rejected by both shores.  Extending it through `A` is equivalent to
colouring `G[A]` from the lists (3.2).  Choose a vertex-minimal induced
subgraph `K_A` which is not colourable from those lists.  It is connected,
since otherwise one of its components is a smaller obstruction.  For
`v in V(K_A)`, colour `K_A-v` from its lists.  If
`d_{K_A}(v)<|L_A(v)|`, one colour in `L_A(v)` is absent from the coloured
neighbours of `v`, and adding `v` gives a contradiction.  This proves
(3.3).  The same construction in `D` gives `K_D`.  \(\square\)

## 4. The simplicial boundary root

Suppose additionally that `d in B` has precisely two neighbours in
`G[B]`, say `x_d,y_d`, and that `x_dy_d` is an edge.  If a separate argument
has established that `G[B]` is `K_5`-minor-free, Theorems 2.1 and 3.1 apply
with

\[
                              I=\{d\}.                 \tag{4.1}
\]

Thus both shore responses can be placed in one connected reconfiguration
space while preserving `d` as one fixed singleton colour class.  Every move
uses only the other five colours, so the named triangle
`d x_d y_d d` remains present throughout.  This is the direct application
to the enlarged-boundary configuration in which the two open shores are
full and anticomplete.

## 5. Exact gain and trust boundary

The theorem is host-level and has no bound on `|B|` or on either shore.  It
couples the two extension languages in one root-preserving Kempe space and
returns either one synchronized boundary move with a literal obstruction
path in each shore or two simultaneous list-critical shore subgraphs.

It does **not** show that the extension languages intersect.  The two
obstruction paths in outcome 1 may end in different boundary components.
The list-critical subgraphs in outcome 2 need not be boundary-full or be
components after deleting their full neighbourhoods.  Consequently the
theorem alone gives neither an explicit `K_7`-minor model nor an order-seven
separation.  The separate
[common-colouring barrier](../barriers/hc7_k5minor_boundary_full_shores_common_colouring_barrier.md)
shows that the boundary minor exclusion, the simplicial triangle vertex and
shore fullness do not by themselves force an intersection.

## 6. External input

- M. Las Vergnas and H. Meyniel, *Kempe classes and the Hadwiger
  Conjecture*, J. Combin. Theory Ser. B **31** (1981), 95--104,
  doi:10.1016/S0095-8956(81)80014-7: the main theorem states that all
  labelled five-colourings of a `K_5`-minor-free graph form one Kempe class.

## 7. Internal dependencies

- proper-minor six-colourability and the ordinary gluing argument; and
- [the general two-shore Kempe-distance proof](../results/hc7_two_shore_kempe_list_dichotomy.md),
  whose transition and list-critical arguments are reproduced here with the
  exact independent block retained.
