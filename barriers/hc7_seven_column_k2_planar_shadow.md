# A seven-column planar shadow of the order-eight response interface

**Status:** explicit finite barrier to geometry-only and selected-fan
augmentations; deterministic verifier in
[`hc7_seven_column_k2_planar_shadow_verify.py`](hc7_seven_column_k2_planar_shadow_verify.py).
This graph is six-colourable and has order-seven separations.  It is not a
counterexample to the response-coupling target or to `HC_7`.

## 1. The inference ruled out

The following host-level data do not, by themselves, force a `K_7` minor
or a `K_5` minor in the seven-column contact graph:

1. seven-connectivity and `K_7`-minor exclusion;
2. an eight-vertex boundary whose complement has exactly two connected
   components, each adjacent to every boundary vertex;
3. an all-boundary fan from a centre in each component, with one common
   boundary limb prescribed to be a direct edge; and
4. the resulting seven literal paired columns dominated by two adjacent
   root branch sets.

The same two incident root edges also have proper six-colourings with all
three positive signatures `(equal,equal)`, `(equal,proper)` and
`(proper,equal)`.

The example realizes all this data with column-contact graph

\[
                         K_1\vee C_6.                 \tag{1.1}
\]

Thus it also rules out any proposed augmentation which uses only the
number of columns, their common two-root domination, or ordinary
seven-connectivity.  A positive theorem must use the operation-specific
nonextension of boundary colourings, or an equivalent dynamic consequence
of non-six-colourability.

## 2. The planar core and the host

Let `I` be the icosahedral graph.  Subdivide every edge `ij` once, calling
the new vertex `m_ij`.  In each old facial triangle `ijk`, add the central
triangle on `m_ij,m_jk,m_ik`.  Call the resulting forty-two-vertex planar
triangulation `P`.  It is five-connected.

Add adjacent vertices `a,b`, each complete to `P`, and put

\[
                              G=K_2\vee P.             \tag{2.1}
\]

The graph `G` is seven-connected.  It has no `K_7` minor: after discarding
the at most two branch sets containing `a,b`, a putative `K_7` model would
leave a `K_5` model in the planar graph `P`.

Every minor of `G` is six-colourable.  Indeed, after deleting the images
of the at most two branch sets containing `a,b`, what remains is a minor
of `P` and is planar.  Four colours for that planar part and two fresh
colours for the exceptional images suffice.

Use the standard NetworkX labelling of `I` and put

\[
                             x=m_{01},\qquad
 S=N_G(x).                                             \tag{2.2}
\]

The vertex `x` has six neighbours in `P`, so `|S|=8`.  The graph `G-S`
has exactly two components,

\[
                    C=\{x\},\qquad D=P-N_P[x].         \tag{2.3}
\]

Both are adjacent to every literal vertex of `S`.

## 3. Two all-boundary fans and the columns

Take the common boundary vertex `p=a`, the centre `x` in `C`, and

\[
                              w=m_{10,11}\in D.         \tag{3.1}
\]

The fan from `x` consists of its eight incident edges.  The verifier checks
the following eight paths from `w`; subscripts on midpoint vertices are
unordered.

\[
\begin{array}{c|l}
1&w,10,m_{3,10},3,m_{2,3},2,m_{1,2},1\\
0&w,11,m_{0,11},0\\
m_{1,5}&w,m_{4,10},4,m_{4,5},5,m_{1,5}\\
m_{0,5}&w,m_{4,11},m_{5,11},m_{0,5}\\
m_{1,8}&w,m_{7,10},7,m_{7,8},8,m_{1,8}\\
m_{0,8}&w,m_{7,11},m_{0,7},m_{0,8}\\
a&w,a\\
b&w,b.
\end{array}                                            \tag{3.2}
\]

Their only common vertex is `w`, their other ends are the eight distinct
members of `S`, and their interiors lie in `D`.

For `s in S-{a}`, join the tail of the direct `x-s` limb to the tail of
the `w-s` limb through their common endpoint `s`; call the resulting
connected subgraph `L_s`.  The sets

\[
                       \{x,a\},\quad\{w\},\quad
                       L_s\ (s\in S-\{a\})             \tag{3.3}
\]

are pairwise disjoint.  The first two are adjacent and each is adjacent to
all seven columns.  Direct inspection gives exactly the following contacts
among the columns:

* `L_b` is adjacent to all other columns; and
* the other six columns form the cycle

\[
       0,m_{0,5},m_{1,5},1,m_{1,8},m_{0,8},0.          \tag{3.4}
\]

Hence the column-contact graph is (1.1), which has no `K_5` minor.
It is not even one contact short of the terminal minor: after adding any
single missing column edge, deleting the universal vertex leaves a cycle
with one chord, a two-clique-sum of two cycles and hence a
`K_4`-minor-free graph.  Thus `K_1` joined to it remains
`K_5`-minor-free.  A proof which obtains only one new unlabelled column
contact from one proper-minor response still does not close this shadow.

Put `e=ax` and `f=aw`.  Contracting the connected set `\{a,x,w\}`
produces two adjacent universal vertices (its contraction image and `b`)
over the planar graph `P-\{x,w\}`.  A six-colouring of that proper minor
expands to a colouring of `G-\{e,f\}` with signature `(equal,equal)`.
Contracting only `e`, respectively only `f`, gives the signatures
`(equal,proper)` and `(proper,equal)`.  Finally, four-colour `P` and give
`a,b` two fresh colours to obtain `(proper,proper)` in `G` itself.

Thus even the paired columns and all three positive two-edge responses do
not replace the universal rejection of `(proper,proper)`.

## 4. Exact trust boundary

The construction is stronger than an abstract contact tableau: the
boundary, complementary components, fans, paths and columns all live in
one seven-connected `K_7`-minor-free graph.  It nevertheless omits the two
inputs which can still drive the active theorem:

* `G` is six-colourable (colour the planar core with four colours and give
  `a,b` two new colours), so it has no exclusive intact-shore response and
  admits the forbidden fourth signature (although all its proper minors
  also satisfy the required six-colourability bound);
* old degree-five vertices of the icosahedron have degree seven in `G`, so
  `G` has genuine order-seven separations and (2.2) is not a minimum
  positive-excess interface.

Accordingly this is not a full-hypothesis falsifier.  Producing such a
falsifier would itself produce a counterexample to `HC_7`.  The barrier
instead establishes that the complete operation-specific rejection family
and the minimum-interface hypothesis cannot be replaced by stronger static
fan geometry.
