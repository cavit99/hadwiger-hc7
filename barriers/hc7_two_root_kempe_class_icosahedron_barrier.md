# The two root-dominating orientations can lie in different Kempe classes

**Status:** explicit computer-assisted counterexample to an intermediate
colouring-space claim.  The deterministic standard-library checker is
[`hc7_two_root_kempe_class_icosahedron_barrier_verify.py`](hc7_two_root_kempe_class_icosahedron_barrier_verify.py).
This note does not refute the full `HC_7` colouring-space dichotomy: the
ambient graph below contains a `K_7` minor and has an actual order-seven
separation.

## 1. Claim refuted

The following data do **not** imply that two oppositely oriented
root-dominating colourings are Kempe-equivalent, or even that a colouring
making both roots colour-dominating exists:

1. a six-chromatic, `K_7`-minor-free common host `J`;
2. two nonadjacent external roots `a,b` such that every proper
   six-colouring of `J` makes at least one root adjacent to every colour
   class;
3. proper six-colourings with each of the two exclusive orientations;
4. a spanning five-branch-set `K_5` model in `J`, every branch set of which
   is adjacent to both roots;
5. seven-connectivity of the ambient graph; and
6. six-colourability after contracting **every** edge incident with either
   root.

In the example below every six-colouring has exactly one colour-dominating
root.  The Kempe reconfiguration graph has ten components: four consist
entirely of colourings in which only `a` is colour-dominating, and six
consist entirely of colourings in which only `b` is colour-dominating.
Thus there is no orientation-changing Kempe sequence, no single
orientation-changing interchange, and no intermediate colouring in which
both roots are colour-dominating.

The missing hypotheses are genuinely global: absence of a `K_7` minor or
of an actual order-seven separation, or the full proper-minor criticality
of a hypothetical counterexample.

## 2. Construction

Let `I` be the icosahedral graph on vertices `0,...,11`.  Its adjacency
lists in the labelling used here are

\[
\begin{array}{c|l@{\qquad}c|l}
0&1,5,7,8,11&1&0,2,5,6,8\\
2&1,3,6,8,9&3&2,4,6,9,10\\
4&3,5,6,10,11&5&0,1,4,6,11\\
6&1,2,3,4,5&7&0,8,9,10,11\\
8&0,1,2,7,9&9&2,3,7,8,10\\
10&3,4,7,9,11&11&0,4,5,7,10.
\end{array}                                                \tag{2.1}
\]

Add adjacent vertices `p,q`, each complete to `I`, and put

\[
                             J=K_2\vee I.                 \tag{2.2}
\]

Add nonadjacent roots `a,b`.  Both are adjacent to `p,q`, and their
neighbourhoods in `I` are

\[
 A=\{0,1,2,3,5\},\qquad B=\{2,3,4,8,11\}.                \tag{2.3}
\]

Write `F=I+{a,b}` for the graph before adjoining `p,q`, and

\[
                             G=K_2\vee F.                 \tag{2.4}
\]

The icosahedron is five-connected.  Adding a vertex with at least five
neighbours to a five-connected graph preserves five-connectivity, so `F`
is five-connected.  It follows directly that `G` is seven-connected:
after deleting at most six vertices, either one of `p,q` remains and is
universal in the surviving graph, or both are deleted and at most four
vertices were deleted from `F`.  Since `d_G(a)=7`, its connectivity is
exactly seven.

The common host `J` is six-chromatic.  It is `K_7`-minor-free: in any
putative `K_7` model, deleting the at most two branch sets containing
`p,q` would leave five pairwise adjacent connected branch sets in the
planar graph `I`, an impossible `K_5` minor.

## 3. The complete colouring-space certificate

Every six-colouring of `J` gives singleton colour classes to `p,q` and a
proper four-colouring to `I`, and conversely.  Up to permuting its four
colours, the icosahedron has exactly the following ten colourings.  Each
row lists the four independent colour classes.

| row | four colour classes in `I` | colour-dominating root |
|---:|---|:---:|
| 1 | `024 / 137 / 5 8 10 / 6 9 11` | `b` |
| 2 | `024 / 1 9 11 / 357 / 6 8 10` | `b` |
| 3 | `0 2 10 / 147 / 3 5 8 / 6 9 11` | `b` |
| 4 | `0 2 10 / 149 / 357 / 6 8 11` | `b` |
| 5 | `049 / 137 / 2 5 10 / 6 8 11` | `b` |
| 6 | `049 / 1 3 11 / 257 / 6 8 10` | `b` |
| 7 | `069 / 1 3 11 / 247 / 5 8 10` | `a` |
| 8 | `069 / 147 / 2 5 10 / 3 8 11` | `a` |
| 9 | `0 6 10 / 149 / 257 / 3 8 11` | `a` |
| 10 | `0 6 10 / 1 9 11 / 247 / 3 5 8` | `a` |

The checker exhausts all 240 labelled four-colourings and verifies this
table.  In particular, every six-colouring of `J` makes exactly one of
`a,b` adjacent to all six colour classes.

For every row, the subgraph induced by any two displayed colour classes
is connected.  A Kempe interchange between two colours of `I` therefore
only permutes two whole classes.  An interchange involving the colour of
`p` or `q` also only permutes whole colour classes, because each is
universal.  Consequently the unordered partition of `V(I)` is invariant
under every Kempe interchange in `J`.  Conversely, all palette
permutations are Kempe moves, so the ten rows are exactly the ten Kempe
components of the six-colouring reconfiguration graph.  Each component
has `6!=720` labelled colourings.

Thus the four `a`-rows and the six `b`-rows are disjoint unions of Kempe
components.  There is no row in which both roots are colour-dominating.

The same table also shows that `F` is not four-colourable: a
four-colouring of `I` cannot be extended to both roots.  Giving `a,b` one
new common colour shows `chi(F)=5`, and hence `chi(G)=7`.

## 4. The labelled minor model and the exact root-edge traces

The following five sets partition `V(J)`, are connected and pairwise
adjacent, and are each adjacent to both roots:

\[
 \{p\},\quad \{q\},\quad \{0,1,2\},\quad \{3\},\quad
 \{4,5,6,7,8,9,10,11\}.                                \tag{4.1}
\]

Thus the obstruction is present over a spanning, root-adjacent `K_5`
model, not merely over an abstract common host.

It also survives all exact root-edge probes.  For every `s in A`, the
graph `F/as` is four-colourable; for every `s in B`, the graph `F/bs` is
four-colourable.  Equivalently, for each chosen incident edge the expanded
colouring of `I` makes `s` the unique neighbour of its root in its colour,
while the other root misses a colour.  The checker verifies all ten
contractions independently.

The contractions of `ap,aq` are also six-colourable: after either
contraction the two adjacent universal vertices use two colours and
`I+b` uses four, choosing any `a`-row (in which `b` misses a colour).
The argument with the roots interchanged handles `bp,bq`.  Hence every edge incident with
`a` or `b` contracts to a six-colourable graph.  Deleting either root is
six-colourable as well, using an exclusive row of the opposite type.

## 5. Exact trust boundary

The example deliberately does **not** satisfy three hypotheses of the
intended counterexample application:

1. the ambient graph `G` is not `K_7`-minor-free (although the common host
   `J` is);
2. `G` has an actual order-seven separation; and
3. `G` is not strongly seven-contraction-critical.

Indeed, `G` has the following
explicit `K_7` model:

\[
 \{p\},\ \{q\},\ \{0,7,8,11\},\ \{a,1,2,5\},\
 \{3,9,10\},\ \{4,6\},\ \{b\}.                        \tag{5.1}
\]

Moreover

\[
                         N_G(a)=\{p,q,0,1,2,3,5\}       \tag{5.2}
\]

is an actual order-seven separator, isolating `a`.  In particular `G` is
not strongly seven-contraction-critical: the `K_7` model contracts to a
proper seven-chromatic minor.

The example therefore does not refute the proposed trichotomy

\[
 K_7\text{ minor}\quad\text{or}\quad
 \text{actual order-seven separation}\quad\text{or}\quad
 \text{two-vertex }K_5\text{-minor transversal}.
\]

It does refute the intended preliminary step if that step tries to obtain
an orientation-changing Kempe transition from universal root domination,
opposite witnesses, a root-adjacent spanning model, seven-connectivity and
all root-edge contraction colourings alone.  Any valid transition theorem
must use the absence of the first two terminal outcomes, or use proper
minor operations away from the roots in an essentially global way.

Run the certificate from the repository root with

```text
python3 barriers/hc7_two_root_kempe_class_icosahedron_barrier_verify.py
```

Its expected output is

```text
icosahedron colourings: 240 labelled, 10 unordered partitions
Kempe components in J: 10 of order 720; orientations 4 A-only + 6 B-only
ambient connectivity: 7; root a has an actual order-seven neighbourhood cut
spanning root-adjacent K5 model: verified
root-edge exact traces in I: 5 at a + 5 at b
explicit K7 model: verified
ALL CHECKS PASSED
```
