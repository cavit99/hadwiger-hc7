# Boundary-crossing persistent edges give a strict one-extra-colour descent

**Status:** written proof; separate internal audit GREEN in
[`hc7_boundary_crossing_persistent_edge_reduction_audit.md`](hc7_boundary_crossing_persistent_edge_reduction_audit.md).

This note treats the case in which the deletion-persistent model edge
aligned at a critical boundary vertex crosses the boundary of the full
shore.  Two useful structures coexist in this case.

First, the critical edge and the persistent edge form a two-edge star whose
leaves are nonadjacent.  A colouring after contracting that star therefore
gives the audited bichromatic saturation-or-bypass alternative.  Second,
any colouring after deleting the persistent boundary edge makes the full
shore colourable after adding one colour to the list of exactly one vertex.
The induced vertex-minimal list obstruction is itself a connected component
behind its full neighbourhood.  If it is a proper part of the old shore,
this is a strict component-order descent which retains the same persistent
edge and the exact one-sided boundary partition.

Thus the boundary-crossing case does not merely fall outside the internal
fixed-trace argument.  It either descends strictly, exposes an order-seven
or order-eight singleton-side separation, or reaches a shore-filling
one-extra-colour critical graph with an explicit positive-excess normal
form.  The last normal form is not eliminated here, and the theorem does
not prove `HC_7`.

## 1. Setting

Let `G` be a graph satisfying

\[
 \chi(G)=7,\qquad \kappa(G)\ge 7,\qquad
 K_7\npreccurlyeq G,
 \qquad\text{and every proper minor of }G\text{ is six-colourable}.
                                                               \tag{1.1}
\]

Suppose

\[
                   V(G)=A\mathbin{\dot\cup}X
                            \mathbin{\dot\cup}D,                \tag{1.2}
\]

where `A,D` are nonempty and connected, `|X|=8`, there is no edge
between `A` and `D`, and, for some `p in X`,

\[
                         N_G(A)=X-\{p\},
 \qquad                   N_G(D)=X.                              \tag{1.3}
\]

Assume also that

\[
                    \{x\},\ B,\ R,\ H_1,H_2,H_3,H_4             \tag{1.4}
\]

is a spanning labelled `K_7`-minus-one-edge model: the seven displayed
sets are pairwise disjoint nonempty connected sets which partition
`V(G)`, every two are adjacent except `\{x\}` and `B`, and those two
sets are anticomplete.  Choose

\[
                    x,u\in X,\qquad v\in D\cap R,
 \qquad              g=xv,\qquad f=uv,                           \tag{1.5}
\]

where `x ne u`, `u in B`, and both displayed pairs are edges.  Assume that
`f` is deletion-persistent for the model (1.4): after deleting `f`, the
same seven sets still form the same labelled near-clique model.  In
particular, another edge realizes the required `B-R` adjacency.

The anticompleteness of the unique deficient pair gives

\[
                              xu\notin E(G).                       \tag{1.6}
\]

The hypotheses arise after applying the protected-singleton rooted
persistence theorem and then taking its boundary-crossing case with the
persistent edge ending in the branch set deficient from `\{x\}`.

## 2. The simultaneous two-edge colouring

### Proposition 2.1 (saturation or a boundary-to-boundary bypass)

There is a proper six-colouring `kappa` of `G-\{g,f\}` satisfying

\[
                         \kappa(x)=\kappa(v)=\kappa(u).            \tag{2.1}
\]

In this colouring, one of the following holds.

1. One of the pairs `xv,uv` lies in one bichromatic component for each
   of the five alternate colours.
2. The graph

   \[
                         (G-\{g,f\})-v                              \tag{2.2}
   \]

   contains an `x-u` path.  More precisely, the path is contained in the
   union of two named bichromatic components and at most one edge between
   them.  Interchanging colours on the component containing `x` gives a
   proper six-colouring of `G-f`, while the symmetric interchange at `u`
   gives a proper six-colouring of `G-g`.

In either alternative, the colouring after deleting `f` coexists with the
unchanged spanning labelled model (1.4).

#### Proof

Contract both edges of the two-edge tree `x-v-u`.  The resulting proper
minor is six-colourable.  Expand the contraction vertex over `x,v,u`.
Equation (1.6) says that the only host edges among those three vertices are
the two deleted edges, so the expansion is a proper colouring of
`G-\{g,f\}` and gives (2.1).

Apply the audited shared-interface bichromatic-bypass theorem to the
incident edges `vx,vu`, with centre `v` and leaves `x,u`.  Its hypotheses
are exactly (1.1), (1.6), and the simultaneous-contraction colouring just
constructed.  The two alternatives and the two one-edge response
colourings are its conclusions.  Persistence of `f` is independent of the
colouring and says that the same labelled model remains present in `G-f`.
\(\square\)

## 3. The one-extra-colour kernel

Fix a proper six-colouring `psi` of `G-f`.  In outcome 2 of Proposition
2.1 one may, and will, take the colouring obtained by the named component
interchange there.  Put

\[
                         \theta=\psi(u)=\psi(v).                   \tag{3.1}
\]

The equality is forced: otherwise restoring `f` would six-colour `G`.
For `z in D`, define

\[
                  L(z)=[6]-\psi(N_G(z)\cap X).                    \tag{3.2}
\]

### Theorem 3.1 (strict one-extra-colour full-neighbourhood descent)

The graph `G[D]` is not `L`-colourable.  It has a connected induced
vertex-minimal non-`L`-colourable subgraph `K` such that

\[
                              v\in V(K),                           \tag{3.3}
\]

and `psi|K` colours `K` from the lists

\[
 L^+(v)=L(v)\cup\{\theta\},\qquad
 L^+(z)=L(z)\quad(z\ne v).                                      \tag{3.4}
\]

Put

\[
               S=N_G(V(K)),\qquad
               C=G[V(K)\cup S],\qquad O=G-V(K),                 \tag{3.5}
\]

and let `Pi` be the equality partition of `S` induced by `psi`.  Then:

1. `(C,O)` is an actual separation with two nonempty open sides;
2. `u in S`, and `f=uv` is the only edge on which `psi|C` can fail to
   be proper;
3. one has the exact response orientation

   \[
       \Pi\in \operatorname{Ext}(C-f,S)
                  \cap\operatorname{Ext}(O,S)
                  \setminus\operatorname{Ext}(C,S);              \tag{3.6}
   \]

4. `|S|>=7`; and
5. if `K ne G[D]`, then

   \[
                              |V(K)|<|D|,                          \tag{3.7}
   \]

   so (3.5) is a strict full-neighbourhood descent which retains the same
   boundary-crossing edge `f`, its exact response partition `Pi`, and the
   global deletion-persistent model in `G-f`.

#### Proof

The restriction of `psi` to `G[A\cup X]` is proper, because the only
deleted edge `f` has its other end in `D`.  If `G[D]` had an
`L`-colouring, it would glue to this restriction across `X`; the list
definition would make every `D-X` edge proper, including `f`.  This would
six-colour `G`, a contradiction.  Choose an induced non-`L`-colourable
subgraph with a minimum vertex set and call it `K`.  It is connected.

For `z ne v`, every edge from `z` to `X` is present in `G-f`, so
`psi(z) in L(z)`.  At `v`, the only absent boundary edge is `vu`.  Thus
`u` is the only boundary neighbour of `v` coloured `theta`, and
`psi(v)=theta` belongs to `L^+(v)`.  If `v` were absent from `K`, then
`psi|K` would be an `L`-colouring of `K`.  This is impossible, so (3.3)
and (3.4) follow.

The set `K` is a connected subset of `D`.  Its full neighbourhood `S`
separates it from the nonempty set `A`, because there is no edge from `D`
to `A`.  This proves item 1.  Since `v in K` and `uv` is an edge, `u in S`.
Every edge other than `f` is properly coloured by `psi`, which proves
item 2.

The restriction to `C-f` and the restriction to `O` are proper and induce
the same labelled partition `Pi` on `S`.  If `Pi` also extended through
`C`, permute the six colour names of that extension to agree literally
with `psi|O` on every block of `Pi`, and glue the two colourings.  This
would six-colour `G`.  Hence (3.6) holds.

The full neighbourhood `S` is a vertex separator.  Seven-connectivity
gives `|S|>=7`, proving item 4.  Finally, if `K` is a proper induced
subgraph of `G[D]`, then its vertex set is a proper subset of `D`, which
is (3.7).  No graph operation has been performed: the persistent labelled
model remains a model of `G-f`, while (3.6) retains the exact single-edge
response at the smaller component.  \(\square\)

The point of (3.6) is stronger than a fresh rejected trace on an unrelated
component.  The old persistent edge remains the only failed edge on the
new closed side, and the opposite closed side already supplies the exact
same labelled boundary partition.

## 4. The shore-filling normal form

It remains to record the exact endpoint when `K=G[D]`.  For `z in D`, put

\[
\begin{aligned}
 q(z)&=|\psi(N_G(z)\cap X)|,\\
 \rho(z)&=|N_G(z)\cap X|-q(z),\\
 \varepsilon(z)&=d_{G[D]}(z)-|L(z)|.
\end{aligned}                                                     \tag{4.1}
\]

### Theorem 4.1 (shore-filling trichotomy and low-degree descent)

Assume `K=G[D]`.  Then

\[
                 d_G(z)=6+\varepsilon(z)+\rho(z)
                         \qquad(z\in D).                         \tag{4.2}
\]

The one-extra-colour trichotomy applies to `G[D],L,v`.  Thus exactly one
of the following holds.

1. Every vertex is tight (`epsilon=0`), and `G[D]` is a Gallai tree.
2. `epsilon(v)=1`, every other vertex is tight, and `(G[D],h_v)` belongs
   to the exceptional class in Cranston--Rabern, Theorems 4.1 and 3.6.
3. The positive-excess set specified in the one-extra-colour theorem is
   nonempty.

In addition, if some `z in D` satisfies

\[
                         \varepsilon(z)+\rho(z)\le2,              \tag{4.3}
\]

then `N_G(z)` is the boundary of an actual separation of order seven or
eight.  Its `z`-side is the singleton `\{z\}`.  If `|D|>1`, this is a
strict component-order descent from the old shore `D`.

Consequently, after excluding the explicit `K_7` conclusion and every
strict full-neighbourhood descent above, the boundary-crossing case has
the following sharp normal form:

\[
                    K=G[D],\qquad
                    \varepsilon(z)+\rho(z)\ge3
                    \quad\text{for every }z\in D.                \tag{4.4}
\]

In particular, every tight vertex then has at least three repeated
boundary-colour occurrences among its literal neighbours, and every
vertex of `D` has degree at least nine.  If `D=\{v\}`, condition (4.3)
always holds, so the only singleton-shore endpoint is an order-seven or
order-eight separation rather than the high-excess normal form.

#### Proof

Because `K=D`, there are no neighbours in `D-V(K)`.  Also
`|L(z)|=6-q(z)`.  Hence

\[
\begin{aligned}
 d_G(z)
   &=d_{G[D]}(z)+|N_G(z)\cap X|\\
   &=6-q(z)+\varepsilon(z)+q(z)+\rho(z),
\end{aligned}
\]

which is (4.2).  The three structural alternatives are Theorem 1.1 of the
audited one-extra-colour critical-kernel theorem, applied using Theorem
3.1.

Suppose (4.3) holds.  Equation (4.2) gives `d_G(z)<=8`, while
seven-connectivity gives `d_G(z)>=7`.  The set `N_G(z)` separates `z`
from every vertex of the nonempty set `A`, because `z in D` and `A` is
anticomplete to `D`.  Thus it is the boundary of an actual order-seven or
order-eight separation.  Its component on the `z`-side is the singleton
`\{z\}`; this has smaller order than `D` whenever `|D|>1`.

If no strict descent and no singleton endpoint occurs, (4.3) fails for
every vertex, which is exactly (4.4).  Equation (4.2) then gives degree at
least nine.  A tight vertex has `epsilon=0`, so (4.4) gives
`rho>=3`.

Finally suppose `D=\{v\}`.  Vertex-minimal noncolourability and (3.4)
force `L(v)=varnothing`, for otherwise the singleton would be
`L`-colourable.  Hence `q(v)=6`, `epsilon(v)=0`, and

\[
        \rho(v)=|N_G(v)\cap X|-6\le |X|-6=2.
\]

Thus (4.3) holds.  \(\square\)

## 5. Exact gain and remaining gap

The theorem closes, by a genuine component-order decrease, every
boundary-crossing instance in which the one-extra-colour critical kernel
is a proper part of the full shore.  In the shore-filling branch it also
removes every instance having a vertex with
`epsilon+rho<=2`, including every singleton shore.  These are unbounded
families, not finite boundary cases.

The surviving graph is much more rigid: the full shore itself is
vertex-minimal for one-extra-colour list criticality, it satisfies one of
the three standard list-critical structures, and every vertex has
`epsilon+rho>=3`.  Simultaneously, Proposition 2.1 supplies either a
five-colour-saturated named model edge or a three-colour boundary-to-
boundary bypass in one common two-edge-deletion colouring.

What is not proved is that the strict descent preserves a useful placement
of all seven model branch sets relative to the new boundary.  Nor does the
high-excess shore-filling normal form allocate the five palette colours to
the four named common branch sets.  A completion must use that literal
contact geometry to produce an explicit `K_7`-minor model or a compatible
order-seven boundary partition.

## 6. Dependencies

- [rooted persistent incident model edges](hc7_rooted_persistent_model_edge.md)
- [one-extra-colour critical kernel](hc7_one_extra_colour_boundary_kernel.md)
- [bichromatic saturation or a bypass at two incident critical edges](hc7_shared_interface_bichromatic_bypass.md)
