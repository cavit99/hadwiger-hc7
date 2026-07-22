# Component-uniform boundary alignment at a low-degree vertex

**Status:** written proof; computer-assisted finite classification;
separately audited GREEN.  This theorem does not prove `HC_7`.

## Theorem 1 (component-uniform boundary alignment)

Let `G` be a finite simple graph such that:

1. `G` is seven-connected and `chi(G)=7`;
2. `G` has no `K_7` minor; and
3. every proper minor of `G` is six-colourable.

Let `u` be any vertex with

\[
                         7\le d_G(u)\le9.                \tag{1.1}
\]

For every component `D` of `G-N[u]`, put `S_D=N_G(D)`.  Then there is a
vertex

\[
 z_D\in S_D\subseteq N(u)
 \quad\hbox{such that}\quad
                         \chi(G-\{u,z_D\})=6.            \tag{1.2}
\]

Thus the edge-deletion response can be chosen independently for every
literal anti-neighbourhood component at the same low-degree vertex `u`.

## 1. Two local inputs

We use the following local-completion statement proved and separately
audited in Section 3 of the
[low-degree alignment theorem](hc7_low_degree_adjacent_pair_alignment.md).

### Prior local-completion lemma

Let `d` belong to `{7,8,9}`.  Let `H` have `d` vertices and minimum degree
at least five.  Add a vertex `u` complete to `H`, and a vertex `c`
nonadjacent to `u` and adjacent to at least seven vertices of `H`.  Then the
resulting graph has a `K_7` minor.

For degree seven this follows from Mader's exact extremal bound.  The
degree-eight equality cases have the explicit models displayed in the
source theorem.  The three degree-nine equality regimes are certified by
the separately audited
[degree-nine verifier](hc7_degree9_pole_verifier.md).

Only one new finite classification is needed.

### Lemma 2 (exceptional marked nine-vertex quotients)

Let `H` be a graph on nine vertices, let `S` be a seven-vertex subset, and
put `T=V(H)-S`.  Suppose

\[
             d_H(s)\ge5\quad(s\in S),
             \qquad 18\le |E(H)|\le22.                 \tag{1.3}
\]

Add one vertex `c` adjacent exactly to `S`.  Then `H+c` has a `K_6`-minor
model whose six branch sets all meet `V(H)`, apart from the following two
marked graphs.

Write

\[
 S=A\mathbin{\dot\cup}B\mathbin{\dot\cup}\{r\},
 \qquad
 A=\{a_1,a_2,a_3\},\quad B=\{b_1,b_2,b_3\},
 \qquad T=\{a,b\}.                                    \tag{1.4}
\]

In `H_-`, the sets `A` and `B` are triangles, the only edges between them
are the matching edges `a_i b_i`, the vertex `r` is complete to `A union B`,
the vertex `a` is complete exactly to `A`, and `b` is complete exactly to
`B`.  There are no other edges.  The second exception is

\[
                              H_+=H_-+br.               \tag{1.5}
\]

The graph6 encodings with the marked set `T={3,4}` are respectively
`HQjVRjf` and `HQjVRjv`.

#### Computer verification

The retained verifier is
[hc7_component_uniform_alignment_verifier.py](hc7_component_uniform_alignment_verifier.py).
It uses `geng` to enumerate every unlabelled nine-vertex graph in each
edge layer and then considers every marked two-set `T`.  A mark is retained
exactly when every vertex of `S` has degree at least five.

For every retained mark, the verifier enumerates every subset of `V(H)`
of order at least six, every partition of that subset into six nonempty
branch sets, and every choice to omit `c` or put it in one branch set.  It
checks branch-set connectedness and all fifteen pairwise adjacencies.  This
is exhaustive: in the required rooted model every branch set contains an
`H`-vertex, unused `H`-vertices are allowed, and `c` is either unused or
belongs to exactly one branch set.

The exhaustive counts are:

| `|E(H)|` | unlabelled `H` | retained marked pairs `(H,T)` | exceptions |
|---:|---:|---:|---:|
| 18 | 34,040 | 2 | 0 |
| 19 | 32,403 | 26 | 0 |
| 20 | 27,987 | 236 | 0 |
| 21 | 21,933 | 1,270 | 1 |
| 22 | 15,615 | 4,379 | 1 |

Thus 5,913 marked pairs are checked.  The two exceptional outputs are
exactly (1.4)--(1.5).  The verifier emits deterministic hashes of the graph
catalogue, all positive certificates, and the two residual marks, and it
independently validates every model returned by its search.

## 2. Double-critical boundary vertices

Fix a component `D` of `G-N[u]` and put

\[
 H=G[N(u)],\qquad S=N_G(D),\qquad T=V(H)-S.             \tag{2.1}
\]

Every neighbour of `D` outside `D` lies in `N(u)`, and `S` separates `D`
from `u`.  Seven-connectivity therefore gives

\[
                      7\le |S|\le d_G(u)\le9.          \tag{2.2}
\]

Suppose, for a contradiction, that (1.2) fails for this component.  For
every `s in S`, proper-minor minimality and `chi(G)=7` give

\[
                          \chi(G-\{u,s\})=5.            \tag{2.3}
\]

Fix a five-colouring of `G-{u,s}`.  Every colour occurs on a common
neighbour of `u` and `s`.  Indeed, if colour `i` did not, recolour every
colour-`i` neighbour of `u` with one new sixth colour, give `u` colour `i`,
and give `s` the new colour.  The recoloured vertices form an independent
set and none is adjacent to `s`, so this would six-colour `G`.

The five common neighbours have five different colours.  Hence

\[
                          d_H(s)\ge5\quad(s\in S).       \tag{2.4}
\]

Contract `D` to a vertex `c`.  It is nonadjacent to `u` and adjacent
exactly to `S`.  If `T` is empty, (2.4) and the prior local-completion lemma
already give a `K_7` minor.  It remains to consider one or two vertices in
`T`.

## 3. One vertex outside the component boundary

Suppose `T={x}`.  If `d_H(x)>=5`, apply the prior local-completion lemma.
We may therefore assume

\[
                              r:=d_H(x)\le4.             \tag{3.1}
\]

The vertex `x` has a neighbour outside `N[u]`: otherwise
`d_G(x)=1+r<=5`, contrary to seven-connectivity.  Choose a component `E`
of `G-N[u]` met by `x`.  Since `x` does not belong to `S=N_G(D)`, the
components `D` and `E` are distinct.  Seven-connectivity gives

\[
                           |N_G(E)|\ge7.                 \tag{3.2}
\]

Put `K=H-x`.  If `d_G(u)=8`, then `|S|=7` and

\[
 2|E(K)|+r=\sum_{s\in S}d_H(s)\ge35,
 \qquad |E(K)|\ge16.                                   \tag{3.3}
\]

Contract `D` and `E` separately and delete `x`.  The resulting ten-vertex
minor has at least

\[
              7+|E(K)|+7+6\ge36>5\cdot10-15           \tag{3.4}
\]

edges: the four terms count the `u-S` edges, the edges of `K`, the `D-S`
edges, and at least six surviving `E-S` edges.  Mader's exact bound gives a
`K_7` minor.

If `d_G(u)=9`, then `|S|=8` and

\[
                  2|E(K)|+r\ge40.                      \tag{3.5}
\]

When `|E(K)|>=19`, the analogous eleven-vertex minor has at least

\[
              8+|E(K)|+8+6\ge41>5\cdot11-15           \tag{3.6}
\]

edges.  Otherwise (3.1) and (3.5) force `r=4` and `|E(K)|=18`.  Before
deleting `x`, the twelve-vertex quotient obtained by contracting `D` and
`E` has at least

\[
             9+(18+4)+8+7=46>5\cdot12-15              \tag{3.7}
\]

edges.  Mader's bound again gives a `K_7` minor.

## 4. Two vertices outside the component boundary

Now `d_G(u)=9`, `|S|=7`, and `T={a,b}`.  If both `a` and `b` have degree at
least five in `H`, use the prior local-completion lemma.  Otherwise choose
a low vertex, say `a`.  As above, `a` meets a component `E_a` of
`G-N[u]` distinct from `D`.

Equation (2.4) gives `|E(H)|>=18`.  If `|E(H)|>=23`, contract `D` and
`E_a` separately.  The resulting twelve-vertex minor has at least

\[
                9+23+7+7=46>5\cdot12-15               \tag{4.1}
\]

edges and hence contains `K_7`.

It remains that `18<=|E(H)|<=22`.  Apply Lemma 2.  If `H+c` has the rooted
`K_6` model, lift `c` back to the connected component `D`.  Every branch
set meets `H=N(u)`, so the singleton branch set `{u}` is adjacent to all
six and completes an explicit `K_7`-minor model in `G`.

We are left with `H_-` or `H_+`.  In both graphs the two vertices `a,b`
outside `S` have degree at most four in `H`, so choose components `E_a,E_b`
of `G-N[u]` met by them.  Both differ from `D`.

If `E_a` and `E_b` are distinct, contract each of the connected sets

\[
                         E_a\cup\{a\},\qquad E_b\cup\{b\}.  \tag{4.2}
\]

Together with the seven vertices of `S`, the two contracted vertices form
a nine-vertex neighbourhood graph `H'` of `u`.  No degree of a vertex of
`S` decreases, because the two old vertices remain distinct after the
contractions.  Each new vertex has at least six neighbours: its support
component had at least seven boundary neighbours, one of which was the
absorbed low vertex.  Thus `delta(H')>=5`.  The contracted vertex `c` from
`D` is still adjacent exactly to the seven vertices of `S`, so the prior
degree-nine local-completion lemma gives a `K_7` minor.

If `E_a=E_b=E`, contract the connected set

\[
                              E\cup\{a,b\}              \tag{4.3}
\]

to one vertex `w`.  This gives an eight-vertex neighbourhood graph `H''`
on `S union {w}` for `u`.  In each exceptional graph the `S`-neighbourhoods
of `a` and `b` are disjoint: they are respectively `A` and `B`, with the
possible additional neighbour `r` belonging only to `b`.  Consequently no
degree in `S` decreases when `a,b` are identified.  The vertex `w` is
adjacent to `A union B`, so it has degree at least six.  Therefore
`delta(H'')>=5`.  Again `c` is adjacent to all seven vertices of `S`, and
the prior degree-eight local-completion lemma gives a `K_7` minor.

Every case contradicts the hypothesis that `G` has no `K_7` minor.  Hence
(1.2) holds for the arbitrary component `D`, proving Theorem 1.

## 5. Consequence for bounded-interface descent

For every component `D` choose `z_D` as in Theorem 1 and put

\[
 A_D=G[D\cup S_D],\qquad B_D=G-D.                      \tag{5.1}
\]

The existing bounded-interface proofs now apply at every `D`: `(A_D,B_D)`
is a full separation of order seven through nine, its boundary is
four-colourable, and every nonempty independent boundary set occurs as an
exact colour block on either closed shore.

Moreover `G-uz_D` is six-colourable.  In every such colouring `u` and
`z_D` have the same colour, since otherwise it would colour `G`; that colour
is absent from `S_D-{z_D}` because `u` is adjacent to every other boundary
vertex.  Thus each component has its own literal named singleton response.

Consequently, if a bridge argument at a selected component `C` returns an
actual component `D` with `|D|<|C|`, it is a strict same-form restart using
the newly declared edge `uz_D`.  It is no longer necessary to prove that
the old vertex `z_C` belongs to `N_G(D)`.  This removes the response-label
obstruction but does not itself force a smaller component, a common
boundary partition, or a `K_7` model.
