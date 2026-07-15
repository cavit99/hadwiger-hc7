# The two-apex icosahedron is a sharp same-row split barrier

**Status:** explicit, independently checkable barrier to every
geometry-only same-row split.  It is not a counterexample to the intended
split-or-terminal theorem: the displayed graph has a literal fixed-pair
terminal.

## 1. The graph

Let `I` be the icosahedral graph.  Use vertices

\[
 T,B,U_0,\ldots,U_4,L_0,\ldots,L_4
\]

and, with subscripts modulo five, the edges

\[
 TU_i,\quad BL_i,\quad U_iU_{i+1},\quad L_iL_{i+1},
 \quad U_iL_i,\quad U_iL_{i-1}.
\tag{1.1}
\]

Add adjacent universal vertices `a,b`, and put

\[
                         J=K_2\mathbin\vee I.
\tag{1.2}
\]

Set

\[
                         z=T,\qquad u=U_0.
\tag{1.3}
\]

The graph `J` is seven-connected.  Indeed, if at least one of `a,b`
survives a deletion, it joins all remaining vertices; if both are deleted
with at most six vertices in total, at most four vertices were deleted
from the five-connected icosahedron.  Conversely, deleting `a,b` and the
five neighbours of one icosahedral vertex isolates that vertex.

The graph has no `K_7` minor.  In any clique model, at most two branch
sets contain `a,b`.  Deleting those branch sets from a hypothetical
`K_7` model would leave five branch sets forming a `K_5` minor in the
planar graph `I`, which is impossible.

## 2. A spanning, balanced `K_6` model avoiding the poles

In `J-{z,u}` take the six bags

\[
\begin{array}{lll}
 F_h=\{U_3,U_4\}, &F_1=\{L_0,L_4\},&F_2=\{U_1,U_2\},\\
 F_3=\{L_1,L_2\},&F_4=\{a,L_3\},&F_5=\{b,B\}.
\end{array}
\tag{2.1}
\]

They are connected, pairwise disjoint, pairwise adjacent, and partition
`V(J)-{z,u}`.  Thus this is a spanning `K_6` model.  Every bag has order
two.  Since the graph being modelled has twelve vertices, no spanning
six-bag model can have a smaller maximum bag size, smaller sum of squared
bag sizes, or a lexicographically smaller sorted size vector.

For a model `M`, write `C_z,C_u` for the rows contacted by `z,u`.  The
model (2.1) has

\[
                  |C_z\cup C_u|=5,qquad |C_z|+|C_u|=9.
\tag{2.2}
\]

These values are maximal, in this order, among all `K_6` models in
`J-{z,u}`.  One short exhaustive verification is supplied beside this
note.  The reason it is enough to enumerate four disjoint connected
branch sets in `I-{z,u}` is structural: the two universal vertices must
belong to distinct branch sets, since otherwise the other five branch
sets would give a `K_5` minor in the planar icosahedron.  Removing the two
universal-containing bags leaves a `K_4` model in `I-{z,u}`.  The checker
enumerates all 696 connected nonempty subsets and all 4,645 such `K_4`
models; their maximum base-row contact profile is `(3,5)`, which becomes
`(5,9)` after restoring the two universally contacted rows.

Thus the obstruction is not removed by the natural instructions
“maximize two-pole row contact, then minimize the spanning bag sizes.”

## 3. Literal same-row first hits and failure of the split

The six-cycle

\[
 L_2-U_3-z-u-U_4-L_3-L_2                         \tag{3.1}
\]

has named edges

\[
 e=zu,qquad f=L_2L_3.
\]

Deleting `e` from the complementary `L_2-L_3` path gives two end
segments whose first model hits are the distinct vertices `U_3,U_4` of
the same row `F_h`.

The five foreign-row portal sets in `F_h` are

\[
\begin{array}{c|ccccc}
  &F_1&F_2&F_3&F_4&F_5\\ \hline
 N_{F_h}(F_i)&\{U_4\}&\{U_3\}&\{U_3\}
                         &\{U_3,U_4\}&\{U_3,U_4\}.
\end{array}                                                   \tag{3.2}
\]

Any connected subset of `F_h` meeting all five foreign rows must contain
both `U_3` and `U_4`.  Consequently there do not exist disjoint connected
sets `X_z,X_u subseteq F_h` which both retain all five foreign-row duties,
even though `z` and `u` have the required distinct first hits.

This falsifies the direct same-row split under all of the following:

* seven-connectivity;
* `K_7`-minor-freeness;
* a literal cycle through the two named edges;
* a spanning `K_6` model avoiding the poles;
* absolute balance/minimality of its bag sizes; and
* maximum natural two-pole row-contact profile.

## 4. Why this is the right barrier, not a negative answer

The pair `{a,b}` is a valid fixed-pair terminal:

\[
                            J-\{a,b\}=I
\]

is planar and hence `K_5`-minor-free.  Moreover `J` is six-colourable,
so it is not a seven-contraction-critical host.

Therefore the example does **not** falsify the desired model-relative
dichotomy

\[
 \text{row split}\quad\text{or}\quad
 \text{proper-minor state/strict receiver}\quad\text{or}\quad
 \text{fixed-pair terminal}.
\]

It identifies the exact hypothesis boundary.  Portal trees, spanning
normalization, contact maximality and bag-size minimality cannot be the
engine.  A proof must use either the universal proper-minor response of
the contraction-critical kernel or the global exclusion of a fixed
two-apex pair.  The example is the canonical two-apex outcome that such a
proof is supposed to detect.

