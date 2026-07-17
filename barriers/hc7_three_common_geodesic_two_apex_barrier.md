# A seven-connected barrier at the three-common-branch-set profile

**Status:** explicit computer-assisted barrier; separate internal audit
GREEN.

This example shows that the exact contact profile and all of the static
buffer-colour linkage data in the current adjacent-pair frontier do **not**
force a contact-increasing change of a spanning `K_6` model or a `K_7`
minor.  The order-seven-separation or fixed-pair conclusion is essential.

The example is not a counterexample to `HC_7`: it is six-colourable and
has a natural pair whose deletion is planar.

## 1. The planar graph

Start with the icosahedral triangulation `I`.  Subdivide every edge once,
and in every original facial triangle join its three subdivision vertices.
Call the resulting frequency-two triangulation `T`.  It has 42 vertices;
the twelve original vertices have degree five and the thirty subdivision
vertices have degree six.

Fix an original face with vertices `a,b,c`.  Write

\[
 z=m_{ab},\qquad u=m_{bc},\qquad w=m_{ca}
\]

for its three subdivision vertices, and put

\[
                         P=T-zw.                       \tag{1.1}
\]

The edge `zu` remains present.  Its only common neighbour in `P` is the
original vertex `b`: before deleting `zw` its two common neighbours were
`b,w`.

The adjacent verifier exhaustively checks that `P` remains
five-connected.  This is the only finite-search assertion in the
construction.  Planarity follows directly from the facial subdivision
construction and edge deletion.

Now add two adjacent vertices `s,t`, each complete to `P`, and let

\[
                         G=K_2\mathbin\vee P.           \tag{1.2}
\]

Then `G` is seven-connected.  Indeed, if at least one of `s,t` remains
after deleting at most six vertices, that universal vertex connects the
remainder.  If both are deleted, at most four vertices of the
five-connected graph `P` were also deleted.  Conversely, `z` has five
neighbours in `P`, so `N_G(z)` is an order-seven separator isolating `z`.

The graph has no `K_7` minor.  Removing from a hypothetical seven-bag
model the at most two bags containing `s,t` would leave at least five
pairwise adjacent branch sets in the planar graph `P`, a `K_5` minor.
This is impossible.

## 2. The spanning `K_6` model

The verifier uses the standard integer labelling of the icosahedron given
in its source.  In that labelling

\[
 z=12,\qquad u=18,\qquad w=14,\qquad b=1,
\]

and the two added universal vertices are `42,43`.  In `G-{z,u}` take the
following six branch sets:

\[
\begin{aligned}
 C_1={}&\{42\},\\
 C_2={}&\{43\},\\
 C_3={}&\{1\},\\
 F_z={}&\{0,4,8,9,10,11,13,15,16,20,24,25,27,28,29,30,
          31,33,34,36,37,38,39,40,41\},\\
 F_u={}&\{5,6,7,14,19,22,23,26,32,35\},\\
 F_0={}&\{2,3,17,21\}.
\end{aligned}                                           \tag{2.1}
\]

They partition `V(G)-{z,u}`, are connected, and are pairwise adjacent.
The pole contacts are exactly

\[
\begin{array}{c|cccccc}
       &C_1&C_2&C_3&F_z&F_u&F_0\\ \hline
 z     &1&1&1&1&0&0\\
 u     &1&1&1&0&1&0.
\end{array}                                             \tag{2.2}
\]

Moreover, in each common-contact branch set the two pole-neighbourhoods
are the same singleton.  In the three noncommon branch sets the literal
neighbour sets are

\[
 N(z)\cap F_z=\{0,16,20\},\qquad
 N(u)\cap F_u=\{5,14,19,32\},\qquad
 N(\{z,u\})\cap F_0=\varnothing.                       \tag{2.3}
\]

Thus (2.1) realizes exactly the three-common-branch-set normal form, not
the previously known four-common-row two-apex example.

## 3. Full static colouring and linkage data

Delete the edge `zu`.  A proper four-colouring of the copy of `P-zu`
has colour classes

\[
\begin{array}{c|l}
0&10,12,13,17,18,21,25,33,36,37,39\\
1&2,15,16,19,26,28,29,34,35,40\\
2&0,5,6,20,23,27,30,31,38,41\\
3&1,3,4,7,8,9,11,14,22,24,32.
\end{array}                                             \tag{3.1}
\]

Give `s,t` two new colours.  This is a proper six-colouring of `G-zu`
in which both poles have colour zero.  Colour zero occurs in
`G-{z,u}` and is anticomplete there to both poles.  Each pole sees every
one of the other five colours.  The three common singleton portals have
the two universal-vertex colours and colour three, while each exclusive
branch set supplies pole-neighbours of colours one and two.

For each of the five nonbuffer colours, the two poles lie in the same
two-colour component.  For the two universal-vertex colours this is the
length-two path through the corresponding universal vertex.  The verifier
checks the other three induced two-colour components directly.

The exclusive branch sets also have the required two-linkage.  With the
selected colour-one and colour-two endpoints, two disjoint paths are

\[
       16-20-1-19,
       \qquad
       0-14-5.                                         \tag{3.2}
\]

Their endpoint sets are respectively contained in `F_z` and `F_u` and
use both selected colours at each end.  As in the general theorem, their
interiors need not stay within named branch sets or preserve colours.

## 4. Exact falsification boundary

The graph satisfies all of the following simultaneously:

1. seven-connectivity and `K_7`-minor-freeness;
2. an adjacent pole pair whose deletion has a spanning `K_6` model;
3. the exact three-common-singleton contact profile;
4. a nonempty buffer colour, five saturated pole colours, and every
   buffer/nonbuffer Kempe connection;
5. two disjoint paths between two-colour endpoint sets in the exclusive
   branch sets; and
6. absence of a contact-increasing transfer from (2.1).

Every proper minor of this particular graph is six-colourable, but this
does not follow merely from the six-colourability of `G` (chromatic number
is not minor-monotone).  Instead, every contraction-only minor of
`K_2 vee P` has the form `K_r vee P'`, where `r<=2` and `P'` is planar:
contracting inside `P` preserves planarity, contracting an edge incident
with a universal vertex only absorbs a planar vertex into the universal
clique, and contracting `st` reduces its order.  An arbitrary minor is a
subgraph of such a contraction-only minor.  The Four-Colour Theorem
therefore gives the asserted six-colouring.

In fact `G-{z,u}` is exactly six-chromatic.  The planar graph
`P-{z,u}` contains the odd wheel with centre `10` and rim

\[
                         16,20,24,28,31,
\]

so it is four-chromatic; joining the universal edge `{s,t}` raises the
chromatic number by two.  Thus what the example lacks is specifically
`chi(G)=7`, and therefore the requirement that proper-minor colourings be
compulsory responses which cannot extend back to `G`.

For item 6, such a transfer would make the pair `{z,u}` contact all six
branch sets of a spanning `K_6` model.  The pair together with those six
sets would then be a `K_7` model, contradicting the proved
`K_7`-minor-freeness.  The same reasoning excludes any proposed clean
branch-set split whose asserted conclusion is a `K_7` model.

What survives is exactly the permitted structural alternative:

\[
 |N_G(z)|=7,
 \qquad
 G-N_G(z)\text{ is disconnected},                     \tag{4.1}
\]

and the fixed pair `{s,t}` leaves the planar graph `P`.

Consequently, no proof of the current three-common-branch-set milestone
can derive the model improvement from connectivity, the static
six-colouring, Kempe connectivity, and the two-linkage alone.  It must
use seven-chromaticity and the resulting forced proper-minor transitions
to align the order-seven separator (or to identify the coherent fixed
pair).

## 5. Verification

Run

```bash
python3 barriers/hc7_three_common_geodesic_two_apex_verify.py
```

The script is dependency-free.  It reconstructs the graph, exhaustively
checks five-connectivity of `P`, and checks the model, contact profile,
colouring, Kempe connections, two displayed paths, and order-seven
separator.
