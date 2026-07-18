# A multicoloured boundary carrier does not determine a labelled exchange

**Status:** explicit finite barrier with a dependency-free exhaustive
checker.  This graph is seven-connected and `K_7`-minor-free, but it is
six-colourable.  It is not a hypothetical counterexample to `HC_7`.

The certificate refutes the following static or single-response
inferences.

1. A connected subgraph meeting a separator in two or more colours must
   admit a split preserving all named clique-model adjacencies.
2. One exact, nonextendible proper-minor response with a multicoloured
   boundary intersection forces either such a split or a smaller open
   shore.
3. Merely obtaining a fully endpoint-saturated response for every edge
   from a singleton shore reproduces the universal colouring dynamics of a
   seven-chromatic critical graph.

It does **not** refute a theorem which uses every proper-minor response and
the fact that the host itself is not six-colourable.  In the displayed
graph the two universal vertices form a coherent terminal pair.

The deterministic checker is
[`hc7_multicoloured_row_response_barrier_verify.py`](hc7_multicoloured_row_response_barrier_verify.py).

## 1. The host graph

Let `I` be the icosahedral graph with poles `t,b`, upper cycle

\[
                           u_0u_1u_2u_3u_4u_0,
\]

and lower cycle

\[
                           w_0w_1w_2w_3w_4w_0.
\]

In addition to the two cycles, add

\[
 tu_i,\qquad bw_i,\qquad u_iw_i,\qquad u_iw_{i-1}
                         \quad(i\bmod 5).
\tag{1.1}
\]

Add adjacent vertices `p,q`, each complete to `I`, and put

\[
                              G=K_2\vee I.              \tag{1.2}
\]

The graph is seven-connected.  Deleting fewer than both universal
vertices leaves a universal vertex; after deleting both, at most four
vertices have been deleted from the five-connected icosahedron.  Conversely,
the two universal vertices together with the five neighbours of an
icosahedral vertex form a cut of order seven.

The graph has no `K_7` minor.  At most two branch sets of a clique-minor
model contain `p,q`; deleting those branch sets from a hypothetical
seven-branch-set model would leave at least five pairwise adjacent branch
sets wholly in the planar graph `I`, giving an impossible `K_5` minor.

Finally, `G` is six-colourable.  The neighbourhood of a pole is an odd
five-cycle, so `chi(I)>=4`; the Four Colour Theorem, or the explicit
colouring in Section 4, gives equality.  Hence

\[
                              \chi(G)=6.                 \tag{1.3}
\]

## 2. A spanning labelled near-complete model

Use the seven branch sets

\[
\begin{aligned}
 \{a\}&=\{u_3\},&
 D&=\{u_1,w_1\},\\
 U&=\{p,u_4,w_3,w_4\},&
 V_1&=\{t,u_0\},\\
 V_2&=\{u_2\},&
 V_3&=\{b,w_0,w_2\},&
 V_4&=\{q\}.
\end{aligned}                                             \tag{2.1}
\]

They are connected, pairwise disjoint, and cover `V(G)`.  Every two are
adjacent except `a,D`, which are anticomplete.  Thus (2.1) is a spanning
boundary-labelled `K_7`-minus-one-edge model.

Split the donor branch set as

\[
                Z=\{w_3\},\qquad W=\{p,u_4,w_4\}.        \tag{2.2}
\]

Both pieces are connected and adjacent to `a`, and `W` retains the root
`u_4`.  The first piece is anticomplete to `D`.  Its full neighbourhood is

\[
 T=N_G(w_3)=\{b,p,q,u_3,u_4,w_2,w_4\}.                  \tag{2.3}
\]

Deleting `T` leaves exactly two components,

\[
 \{w_3\},\qquad \{t,u_0,u_1,u_2,w_0,w_1\},              \tag{2.4}
\]

and both components are adjacent to every vertex of `T`.

Absorb the opposite donor part into the previously deficient branch set:

\[
 Q_0=D\cup W,\qquad Q_1=V_1,\quad Q_2=V_2,
 \quad Q_3=V_3,\quad Q_4=V_4.                            \tag{2.5}
\]

These five connected subgraphs are pairwise adjacent, each is adjacent to
`a`, and

\[
                 T-\{a\}\subseteq\bigcup_{i=0}^4Q_i.    \tag{2.6}
\]

Two of them have empty boundary intersection, which is permitted by the
five-subgraph separator-reflection setup.  Crucially,

\[
                Q_0\cap T=\{p,u_4,w_4\}\cong K_3.       \tag{2.7}
\]

Therefore `Q_0 cap T` uses exactly three colours in **every** proper
colouring.  This remains true after every deletion or contraction
considered below.

## 3. A nonextendible exact proper-minor response

The following is a proper six-colouring of `G-w_3`:

\[
\begin{array}{c|ccccccccccccc}
v&p&q&t&u_0&u_1&u_2&w_0&w_1&b&u_3&u_4&w_2&w_4\\ \hline
c(v)&0&1&2&3&4&5&5&3&2&3&5&4&4.
\end{array}                                               \tag{3.1}
\]

Its boundary trace uses all six colours and has the sole repeated block
`{w_2,w_4}`.  It cannot extend to `w_3`, because that vertex is adjacent
to every member of `T`.

This is a genuine connected-contraction response, not merely an arbitrary
colouring after vertex deletion: contract the path

\[
                              w_2w_3w_4                  \tag{3.2}
\]

and give its image colour `4`.  Pulling the quotient colouring back to the
untouched far shore gives (3.1).  Nevertheless (2.7) remains
multicoloured, and a split of `Q_0` preserving the other six named branch
sets would itself be a `K_7` model, impossible by Section 1.  The exposed
open shore `{w_3}` is already a singleton, so its order cannot strictly
decrease.

## 4. The full elementary-response census

The checker enumerates proper colourings once each up to a global
permutation of the six colours.  It uses restricted-growth palette names
and a deterministic saturation-degree backtracking order.  Every listed
colouring globally uses all six colours, so the number of labelled-palette
colourings is the displayed count multiplied by `6!`.

\[
\begin{array}{c|c|c|c|c}
\text{proper minor}&\text{colourings}&\text{boundary partitions}
 &\text{all six colours on }T&\text{six-block partitions}\\ \hline
G-w_3&20&10&10&5\\
G/(w_3p),\ G/(w_3q)&20&10&10&5\\
G/(w_3s),\ s\in\{b,u_3,u_4,w_2,w_4\}&8&4&6&3
\end{array}                                               \tag{4.1}
\]

Thus every one of the seven incident edge contractions has an exact
nonextendible response whose boundary uses all six colours, while every
response still has the fixed multicoloured triangle (2.7).  Expanding a
colouring of `G/(w_3s)` gives a colouring of `G-w_3s` in which the two
ends have the same colour.

The resemblance to an edge-critical response is stronger still.  For
`s=p,q`, ten contraction colourings saturate both original endpoints in
all five alternative colours; the other ten saturate only `s`.  For each
of the five icosahedral neighbours, four colourings saturate both
endpoints, two saturate only `w_3`, and two saturate only `s`.  Hence every
incident edge has at least one fully endpoint-saturated, nonextendible,
multicoloured response.

For example, deleting `w_3b` and assigning

\[
\begin{array}{c|cccccccccccccc}
v&b&p&q&t&u_0&u_1&u_2&u_3&u_4&w_0&w_1&w_2&w_3&w_4\\ \hline
c(v)&2&1&0&5&3&2&4&3&4&4&3&5&2&5
\end{array}                                               \tag{4.2}
\]

gives equal colour `2` to the deleted edge's endpoints, uses all six
colours on `T`, and makes both endpoints see every other colour.

## 5. Exact failed criticality law

The certificate satisfies all of the displayed geometric hypotheses,
proper-minor colourability, and the **existence** of a critical-looking
response for every edge incident with the singleton shore.  What it does
not satisfy is universal nonextension.

In a seven-vertex-critical graph, every proper six-colouring of `G-w_3`
uses all six colours on `N_G(w_3)`: a missing colour could otherwise be
assigned to `w_3`.  Here half of the colourings in the first line of
(4.1) use only five boundary colours.  One such colouring is obtained by
colouring the icosahedron as

\[
\begin{array}{c|cccccccccccc}
v&w_4&w_3&u_4&u_3&w_2&b&w_1&w_0&u_0&u_1&t&u_2\\ \hline
c(v)&0&1&2&0&2&3&0&1&3&2&1&3,
\end{array}                                               \tag{5.1}
\]

and assigning colours `4,5` to `p,q`.  On `T`, colour `1` is absent and
extends to `w_3`; indeed (5.1) is a proper colouring of all of `G`.

Similarly, in a non-six-colourable edge-critical host, every colouring of
`G-w_3s` with equal-coloured ends puts those ends in the same two-colour
Kempe component for every alternative colour.  Otherwise one interchange
separates their colours and restores the edge.  The displayed graph fails
this universal law for its five icosahedral spokes, even though it has the
fully saturated witnesses counted above.

This is the exact missing hypothesis.  Existence of proper-minor responses,
even one saturated response for every incident operation, is insufficient.
A positive theorem must compare the complete response languages forced by
non-six-colourability, obtain a common labelled boundary partition, or
recognize the coherent terminal pair `p,q`.

## 6. Trust boundary

- The graph is six-colourable.  In particular, it is neither
  seven-vertex-critical nor a seven-chromatic graph all of whose proper
  contractions are six-colourable.
- The pair `p,q` is a valid global terminal: deleting it leaves the planar
  icosahedron and hence no `K_5` minor.
- The two closed shores therefore do have a common boundary equality
  partition, although the particular response (3.1) is nonextendible.
- Consequently this is not a counterexample to the disjunction

  \[
  K_7\text{ minor}\quad\text{or common boundary partition}
  \quad\text{or coherent two-vertex terminal}.
  \]

- It refutes only arguments which try to obtain that disjunction from the
  geometry of one multicoloured connected subgraph, one response colouring,
  or the existence of separately selected saturated responses.
- No infinite-family claim is needed for the barrier.  The fourteen-vertex
  certificate already satisfies every static hypothesis stated above.

The strongest unconditional path conclusion from a multicoloured
intersection is much weaker: if `Q` is connected and `Q cap T` contains
two colours, choose a differently coloured pair at minimum distance in
`G[Q]`.  A shortest path between them has no internal vertex in `T`, since
such a vertex would give a shorter differently coloured pair.  The path
need not be bichromatic and does not determine a branch-set split.
