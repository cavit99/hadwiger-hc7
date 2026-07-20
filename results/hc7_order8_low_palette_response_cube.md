# Low-palette boundary colourings give a coupled response cube

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_low_palette_response_cube_audit.md`](hc7_order8_low_palette_response_cube_audit.md).
This theorem
reduces the three-colour boundary residual to simultaneous bichromatic paths
in both open shores.  It does not prove `HC_7`.

## 1. Setting

Let

\[
 V(G)=A\mathbin{\dot\cup}B\mathbin{\dot\cup}D,
 \qquad E_G(A,D)=\varnothing,
\tag{1.1}
\]

where `A,D` are nonempty.  Fix a nonempty independent set
`I\subseteq B`,
give it one fixed sixth colour, and put `H=G[B-I]`.  Let `E_A,E_D` be the
disjoint sets of labelled proper five-colourings of `H` whose corresponding
exact-`I` boundary colourings extend through the two closed shores.

Assume:

1. `E_A,E_D` are nonempty and invariant under every permutation of the
   five colour names;
2. every surjective proper five-colouring of `H` belongs to exactly one of
   `E_A,E_D`; and
3. `E_A` contains no colouring using four or five colours.

Choose `c\in E_A` with maximum palette order `p`.  Then `p\le3`.

## 2. The response cube

### Theorem 2.1

Assume `|H|=8`.  Choose `5-p` distinct vertices

\[
                              x_1,\ldots,x_{5-p}       \tag{2.1}
\]

from the colour classes of `c` so that every original colour class remains
nonempty after all selected vertices are removed.  Assign the `5-p` unused
colours bijectively to these vertices.  For
`J\subseteq[5-p]`, let `c_J` be obtained from `c` by making exactly those
recolourings indexed by `J`.

The vertices in (2.1) can always be chosen, and every `c_J` is proper with

\[
                         |\operatorname{pal}(c_J)|=p+|J|. \tag{2.2}
\]

Let `J` be inclusion-minimal and nonempty subject to `c_J in E_D`.  Such a
set exists.  Then exactly one of the following holds.

1. `|J|=1`, and `c,c_J` are oppositely extendable boundary colourings
   differing at one literal vertex.
2. `|J|\ge2`, and every colouring `c_K` with
   `\varnothing\ne K\subsetneq J` is rejected by both closed shores.

In outcome 2, for every `i in J` there are two paths `P_i^A,P_i^D` with
the following properties.  If `a_i=c(x_i)` and `b_i` is the new colour
assigned to `x_i`, then

* `P_i^A` joins `x_i` to another literal vertex of the original boundary
  colour class `c^{-1}(a_i)`, has nonempty interior in `A`, and uses only
  colours `a_i,b_i` in one fixed extension of `c` through the `A`-shore;
* `P_i^D` has the same boundary-end description, has nonempty interior in
  `D`, and uses only colours `a_i,b_i` in one fixed extension of `c_J`
  through the `D`-shore.

#### Proof

The total number of vertices available beyond one representative of each
old colour class is `8-p`, which is at least `5-p`.  This proves that the
selection in (2.1) exists.  Each new colour is absent from `H`, distinct
selected vertices receive distinct new colours, and every old colour
retains a representative.  Hence all `c_J` are proper and (2.2) holds.

The top colouring `c_[5-p]` is surjective.  It cannot belong to `E_A` by
hypothesis 3, so exact surjective ownership puts it in `E_D`.  A minimal
nonempty `J` therefore exists.  If `|J|=1`, outcome 1 holds.

Let `|J|\ge2` and take `\varnothing\ne K\subsetneq J`.  Minimality excludes
`c_K` from `E_D`.  Its palette is larger than the maximum palette `p` of a
colouring in `E_A`, so it is not in `E_A` either.  This proves the rejection
claim.

Fix an extension of `c` through `A\cup B`.  In its full
`a_i`--`b_i` component containing `x_i`, suppose no other boundary vertex
of colour `a_i` occurs.  The new colour `b_i` is absent from the boundary,
so interchanging the two colours on that component changes the boundary
trace from `c` to exactly `c_{\{i\}}`.  This contradicts rejection of that
trace.  A shortest route from `x_i` to the first other boundary vertex in
the component gives `P_i^A` with all internal vertices in `A`.

Now fix an extension of `c_J` through `D\cup B`.  The same argument,
with the interchange reversed at `x_i`, would produce `c_{J-\{i\}}` unless
the full component met another original boundary vertex of colour `a_i`.
That trace is rejected by the minimality conclusion above.  Stopping at
the first other boundary vertex gives `P_i^D` with interior in `D`.
This proves the theorem. \(\square\)

## 3. The three-chromatic square

### Corollary 3.1

Suppose `\chi(H)=3`.  Then `p=3`, and Theorem 2.1 gives two selected
vertices `x,y` and a square

\[
                         c,\quad c_x,\quad c_y,\quad c_{xy}. \tag{3.1}
\]

Either `c_x` or `c_y` is an oppositely extendable one-vertex transition,
or both are four-colour boundary traces rejected by both shores.  In the
latter case both shores contain the two path systems from Theorem 2.1.

If `x,y` are chosen from distinct repeated colour classes of `c`, then the
two paths in each shore are vertex-disjoint: their two colour pairs are
disjoint.  Such a choice fails only when the three colour-class orders of
`c` are `(6,1,1)`.  In particular, an additional bound `\alpha(H)\le4`
guarantees the disjoint choice.

#### Proof

A proper colouring of the three-chromatic graph uses at least three
colours, so maximality and hypothesis 3 give `p=3`.  The top of the cube
therefore has two coordinates.  Theorem 2.1 gives the first assertion.

When `x,y` come from distinct old colour classes, the pairs
`{a_x,b_x}` and `{a_y,b_y}` are disjoint.  In either fixed shore colouring,
the corresponding bichromatic subgraphs, and hence the selected paths, are
vertex-disjoint.  Two different repeated colour classes permit such a
choice.  If there is only one repeated class, the other two classes are
singletons and the class orders sum to eight, giving `(6,1,1)`.
The independence bound excludes a colour class of order six. \(\square\)

## 4. Exact scope

The theorem gives a finite-dimensional, operation-labelled replacement for
an unspecified low-palette transition.  It does not show that either
intermediate four-colour trace extends, align the path endpoints with named
minor branch sets, or force the two paths in different shores to share
remote ends.  The next positive theorem must use seven-connectivity, global
`K_7`-minor exclusion or full proper-minor criticality to turn this coupled
path geometry into an explicit `K_7`-minor model, a colour-compatible
order-seven separation or a strict host-level descent.
