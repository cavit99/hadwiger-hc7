# A static transition barrier at the shifted order-eight separation

**Status:** written counterexample to overbroad intermediate claims, with a
deterministic finite verifier.  This is not a counterexample to `HC_7`.
The graph is `K_7`-minor-free and has two connected boundary-full open
sides, but it is not seven-connected or contraction-critical.

## 1. What the example disproves

There is a graph `G` with an eight-vertex separator `T` and open sides
`L,R` such that:

1. `L` and `R` are connected, anticomplete to one another, and each is
   adjacent to every vertex of `T`;
2. the closed `L`-side contains a `K_5`-minor model whose minimum possible
   support order is six;
3. `G` has treewidth at most five and hence has no `K_7` minor;
4. `R` is the edge `pq`; and
5. deleting or contracting `pq` creates four different new equality
   partitions on `T`.

Thus boundary fullness, `K_7`-minor exclusion, a named support-six model,
and simultaneous deletion/contraction responses at one internal edge do
not select a unique boundary partition or a unique equality block.  A
positive shifted-separation theorem must use seven-connectivity or the
global compatibility conditions supplied by full contraction-criticality.

## 2. The graph

Let

\[
                 T=\{v,x,r_1,r_2,a,b,c,d\}.           \tag{2.1}
\]

On `T`, take the theta graph

\[
 r_1r_2,\ r_1b,\ ba,\ ar_2,\ r_1d,\ dc,\ cr_2        \tag{2.2}
\]

and add the three edges

\[
                              va,\ vr_1,\ vd.          \tag{2.3}
\]

The left open side is

\[
                              L=\{s,u_1,u_2\}.         \tag{2.4}
\]

Make `s` adjacent to every vertex of `T`, add `su_1,u_1u_2`, and make
each `u_i` adjacent to `a,r_1,d`.

The right open side is the edge

\[
                              R=\{p,q\},\qquad pq\in E(G),       \tag{2.5}
\]

with boundary neighbourhoods

\[
\begin{aligned}
 N_T(p)&=\{v,x,r_1,c,d\},\\
 N_T(q)&=\{r_1,r_2,a,b,c\}.
\end{aligned}                                                   \tag{2.6}
\]

There are no other edges.  Both open sides are connected and boundary
full: `s` sees all of `T`, while the two sets in (2.6) have union `T`.

## 3. The support-six model and minor exclusion

The five sets

\[
                 \{u_1\},\quad\{u_2\},\quad\{r_1\},\quad\{d\},
                 \quad\{v,a\}                         \tag{3.1}
\]

are branch sets of a `K_5`-minor model.  The first four vertices form a
clique.  The last set is connected through `va`, meets the two `u_i`
through `a`, and meets `r_1,d` through `v`.

The graph has no `K_5` subgraph.  In particular, a `K_5`-minor model
cannot have support order five, so (3.1) has minimum possible support order
six.  This can also be seen directly from the maximal cliques, all of
which have order at most four; the verifier checks this exhaustively.

For the stronger `K_7` exclusion, the following eight bags form a tree
decomposition:

\[
\begin{array}{ll}
B_0=\{a,c,p,q,r_1,s\},        &B_1=\{a,c,d,p,r_1,s\},\\
B_2=\{a,c,q,r_1,r_2,s\},     &B_3=\{a,b,q,r_1,s\},\\
B_4=\{p,s,x\},               &B_5=\{a,d,p,r_1,s,v\},\\
B_6=\{a,d,r_1,s,u_1\},       &B_7=\{a,d,r_1,u_1,u_2\}.
\end{array}                                                    \tag{3.2}
\]

Its decomposition tree has edges

\[
       01,\ 02,\ 03,\ 04,\ 15,\ 16,\ 67.             \tag{3.3}
\]

Every graph edge is covered and the bags containing each vertex induce a
connected subtree.  The maximum bag order is six, so `tw(G)\le5`.
Treewidth is minor-monotone and `tw(K_7)=6`; hence `G` has no `K_7`
minor.

## 4. Exact six-colour boundary languages

For a graph containing `T`, let `Ext_6` denote the equality partitions of
`T` induced by its proper six-colourings.  Let `J=G[T]`.

The closed left side has the exact extension language

\[
 \mathcal L={\Pi:\Pi\text{ is a proper partition of }J
                  \text{ into at most five blocks}\}.           \tag{4.1}
\]

Indeed, the vertex `s` is adjacent to all of `T`, so a boundary colouring
uses at most five colours.  Conversely, give `s` an unused sixth colour.
The vertices `u_1,u_2` both see only the three boundary colours on
`\{a,r_1,d\}`; among those vertices only `r_1d` is an edge.  After also
avoiding the colour of `s` at `u_1`, two distinct available colours can
always be assigned to `u_1,u_2`.  Thus every partition in (4.1) extends.

There are exactly

\[
                              |\mathcal L|=358          \tag{4.2}
\]

such labelled equality partitions.

For a fixed colouring belonging to `\mathcal L`, the vertices `p,q` can
be coloured precisely when they have two distinct available colours.  All
but four members of `\mathcal L` have this property.  The four exceptions
are

\[
\begin{array}{lllll}
 vr_2&|xa&|r_1&|bd&|c,\\
 vr_2&|xb&|r_1&|ad&|c,\\
 vb&|xr_2&|r_1&|ad&|c,\\
 vb&|xa&|r_1&|r_2d&|c.
\end{array}                                                    \tag{4.3}
\]

In each row, both `p` and `q` have the same unique available sixth colour,
so the edge `pq` prevents extension.  The exact language table is therefore

| graph | exact boundary language | order |
|---|---|---:|
| `G` | `\mathcal L` minus the four rows in (4.3) | 354 |
| `G-pq` | `\mathcal L` | 358 |
| `G/pq` | `\mathcal L` | 358 |
| `G-R` | `\mathcal L` | 358 |
| `G/R` | `\mathcal L` | 358 |

For `G-pq`, the two endpoints may share their unique available colour.
For `G/pq`, the contracted vertex is complete to `T` and may receive the
unused sixth colour.  Deleting or contracting the whole component gives
the last two rows for the same reasons.

The four-state jump in (4.3) is the minimal useful certificate: even an
internal edge for which both deletion and contraction unlock compatible
boundary colourings need not determine one returned state.

## 5. Exact scope

This graph deliberately fails the hypotheses that still carry real force
in a hypothetical minimal `HC_7` counterexample.  It is only
two-connected, is six-colourable, and is not contraction-critical.  It
therefore does not refute a theorem that combines seven-connectivity,
global incompatibility of the two closed-side extension languages, and
responses to every proper minor.

It does show that none of those hypotheses can be replaced merely by:

- two connected boundary-full sides;
- global `K_7`-minor exclusion;
- a minimum-support-six `K_5` model on one closed side; and
- one internal edge whose deletion and contraction both enlarge the
  boundary extension language.

The verifier
[`hc7_shifted_order8_static_transition_barrier_verify.py`](hc7_shifted_order8_static_transition_barrier_verify.py)
checks the graph, model, tree decomposition, all `4,111` boundary
partitions into at most six blocks, the exact counts above, and the four
exceptional partitions.
