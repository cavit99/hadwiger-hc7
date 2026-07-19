# Joint persistence and exact colour responses do not force first-hit Hall allocation

**Status:** two explicit computer-assisted barriers to intermediate
palette-to-label claims, with a deterministic standard-library verifier.
Neither graph is a counterexample to `HC_7`: each contains a literal
`K_7` and is not minor-minimal.

The accompanying checker is
[`hc7_joint_pair_first_hit_hall_barrier_verify.py`](hc7_joint_pair_first_hit_hall_barrier_verify.py).

## 1. Claims refuted

Both examples have a spanning labelled `K_7`-minus-one-edge model whose
root branch set is a singleton and is not an end of the missing model
adjacency.  Two edges at that singleton may be deleted simultaneously
while the same seven branch sets retain the same labelled model.

The first example refutes the following inference without explicit use of
`K_7`-minor exclusion or global proper-minor criticality.

> If the two outer endpoints are nonadjacent and their common contraction
> gives the exact star trace, then the five alternate colours have
> first-hit representatives in five distinct foreign branch sets.

The second example refutes the corresponding critical-triangle inference.

> If the two outer endpoints are adjacent, both exclusive response
> orientations occur, and one Kempe interchange changes one orientation
> into the other, then the saturated untouched colours have first-hit
> representatives in distinct foreign branch sets.

These failures occur with connectivity eight.  Thus neither higher
connectivity, exclusion of order-seven separations, singleton-root
placement, common model preservation, nor the existence of the transition
is the missing palette-to-label mechanism.

For a fixed colouring `c` and singleton root `r`, define the support of a
colour `i` to be the set of foreign model labels whose branch set contains
an `i`-coloured neighbour of `r`.  Since the root is a singleton, every
such neighbour is already a literal first hit outside the root branch set.
The failures below are strict Hall failures in this colour--label incidence
graph.

## 2. Nonadjacent outer endpoints

### 2.1 Construction

Let `B` be the graph on `0,1,...,5` with edge set

```text
01 02 03 04 05 12 13 15 23 24 34 35 45.
```

Equivalently, its graph6 string is `E~nW`.  Add a triangle
`A3,A4,A5`, complete to `B`.  Add four more vertices

```text
p, y3, y4, y5.
```

On the graph after deleting `01` and `04`, prescribe the colouring

\[
\begin{array}{c|l}
0&0,1,4\\
1&3\\
2&2,5\\
3&A3,p,y3\\
4&A4,y4\\
5&A5,y5.
\end{array}                                                    \tag{2.1}
\]

Join `p` to every old vertex whose colour in (2.1) is not `3`.  Add
`y3,y4,y5` in that order, joining each new vertex to every already present
vertex of a different colour except `4,p`.  Finally retain the original
edges `01,04`; call the resulting graph `G`, and put

\[
                         H=G-\{01,04\}.                 \tag{2.2}
\]

The displayed assignment is a proper six-colouring of `H`.  Recolouring
`0` with a seventh colour gives a proper seven-colouring of `G`.

Use the seven branch sets

\[
\begin{array}{c|l}
R&\{0\}\\
C&\{1,2,3,5\}\\
B_0&\{4,p\}\\
A_3&\{A3\}\\
A_4&\{A4\}\\
A_5&\{A5\}\\
Y&\{y3,y4,y5\}.
\end{array}                                                   \tag{2.3}
\]

They partition the graph, are connected, and every two are adjacent
except `B_0,Y`.  Hence (2.3) is a spanning exact labelled
`K_7`-minus-one-edge model in both `G` and `H`.  Its common root label is
the singleton `R`.

The edges `01,04` are jointly deletion-persistent for this model.  After
both are deleted, `R` still meets `C` through `02,03,05` and still meets
`B_0` through `0p`.  Their outer endpoints `1,4` are nonadjacent.

### 2.2 Exact trace and Hall failure

The vertices `0,1,4` induce a connected two-edge star in `G` and have
one colour in (2.1).  Every vertex adjacent to this star but outside it
has another colour.  Thus (2.1) is exactly the expansion of a colouring
after contracting the star.  In particular,

\[
 N_G(0)\cap c^{-1}(c(0))=\{1,4\}.                     \tag{2.4}
\]

The supports of alternate colours `1` and `2` are both the singleton
set

\[
                             \{C\}.                    \tag{2.5}
\]

Indeed the colour-`1` root neighbour is `3`, while the colour-`2` root
neighbours are `2,5`, and all three lie in `C`.  The two-colour family in
(2.5) therefore has neighbourhood of order one, so no system of distinct
colour-to-label representatives exists.

The verifier exhausts every deletion of at most seven vertices and proves

\[
                         \kappa(G)=8.                    \tag{2.6}
\]

Nevertheless

\[
                       \{0,1,2,3,A3,A4,A5\}             \tag{2.7}
\]

is a literal `K_7`.

## 3. Adjacent outer endpoints

### 3.1 Construction by two response colourings

Use the vertex set

```text
v a b c1 c2 c3 c4 pA pB p1 r1 p2 r2 p3 r3.
```

Define two six-colour assignments `phi,psi` by

\[
\begin{array}{c|l}
\text{colour}&\text{vertices under }\phi\\ \hline
0&v,a,r1,r3\\
1&c1,pA,pB,p1,p2,p3\\
2&b,r2\\
3&c2\\
4&c3\\
5&c4,
\end{array}                                                   \tag{3.1}
\]

and let `psi` differ only by giving `v` colour `2`.  Let `H` contain
every edge whose endpoints have different colours in both assignments,
except that no edge is placed between

\[
                  Y_1=\{p1,r1\},\qquad Y_2=\{p2,r2\}.   \tag{3.2}
\]

Put

\[
                       G=H+va+vb.                       \tag{3.3}
\]

Both assignments properly colour `H`.  Recolouring `v` with a seventh
colour in either assignment properly colours `G`.

Use the branch sets

\[
\begin{array}{c|l}
R&\{v\}\\
A&\{a,pA\}\\
B&\{b,pB\}\\
C&\{c1,c2,c3,c4\}\\
Y_1&\{p1,r1\}\\
Y_2&\{p2,r2\}\\
Y_3&\{p3,r3\}.
\end{array}                                                   \tag{3.4}
\]

They form a spanning exact labelled `K_7`-minus-one-edge model whose
only missing branch-set adjacency is `Y_1Y_2`.  The same model remains
after deleting `va,vb`: the edges `vpA,vpB` retain the two root
adjacencies.  Thus the two displayed edges are jointly
deletion-persistent at the singleton common root.

### 3.2 Exact EP/PE transition and Hall failure

The seven vertices

\[
                        v,a,b,c1,c2,c3,c4               \tag{3.5}
\]

induce `K_7` in `G` and induce `K_7-{va,vb}` in `H`.  In every
six-colouring of that latter graph, the clique
`a,b,c1,c2,c3,c4` uses all six colours.  The vertex `v` is adjacent to
the four `c` vertices and therefore has the colour of exactly one of
`a,b`.  Hence every six-colouring of `H` has exactly one of the two
exclusive signatures `(equal,proper)` and `(proper,equal)`.  The two
assignments above witness both signatures.

In `phi`, the component containing `v` of the subgraph on colours `0,2`
is the singleton `\{v\}`.  Interchanging those colours on that component
produces `psi`.  This is therefore an actual one-step EP-to-PE Kempe
transition, not merely two unrelated response colourings.

The transition theorem saturates the colour-`0` side of this singleton
component in every untouched colour.  Nevertheless the supports of
colours `3,4,5` are all

\[
                             \{C\}:                    \tag{3.6}
\]

their only root neighbours are respectively `c2,c3,c4`.  Thus a
three-colour family has a one-label neighbourhood and Hall allocation
fails even after the transition is present.

The verifier again proves

\[
                         \kappa(G)=8.                    \tag{3.7}
\]

The set in (3.5) is the promised literal `K_7`.

## 4. Exact trust boundary

The examples deliberately satisfy a terminal outcome excluded in the
active `HC_7` branch.  Each contains a literal `K_7`, and deleting any one
of its added vertices leaves that clique, so neither graph is
minor-minimal.  They therefore do not refute a theorem that uses
`K_7`-minor exclusion and the proper-minor responses of a hypothetical
minor-minimal counterexample.

Their role is to show exactly where those hypotheses must be spent.  A
positive theorem cannot first infer an injective colour-to-label map from
the local data and invoke `K_7`-minor exclusion only afterwards.  Even at
connectivity eight, with a singleton root, a fixed spanning exact model,
joint deletion persistence, an exact contraction trace, and—when
applicable—an actual orientation-changing Kempe interchange, several
colours can have all their literal first hits in one branch set.

The weakest credible continuation is therefore terminal-aware.  A
Hall-deficient first-hit branch set must be modified using a proper-minor
response supported in that branch set, and the outcome must be one of:

1. a label-preserving split giving an explicit `K_7`-minor model;
2. a full-neighbourhood separation carrying compatible colour data; or
3. a strict host-level descent retaining the labelled model and response.

There is no stronger counterexample satisfying `K_7`-minor exclusion and
the exact universal rejection law known here: such a graph would already
occupy the unresolved `HC_7` regime.

## 5. Verification

Run from the repository root:

```text
python3 barriers/hc7_joint_pair_first_hit_hall_barrier_verify.py
```

Expected output:

```text
nonadjacent star: kappa=8, singleton rooted K7^- model, joint persistence, exact trace, Hall failure, explicit K7
adjacent triangle: kappa=8, singleton rooted K7^- model, EP/PE transition, Hall failure, explicit K7
verified joint-pair first-hit Hall barriers
```
