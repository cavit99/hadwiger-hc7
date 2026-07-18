# A universal obstructing-edge response need not diversify named first hits

**Status:** explicit finite barrier with a deterministic verifier.  This
graph is seven-connected and has the exact configuration of five named
connected subgraphs and five cyclic connected subgraphs below.  It is not a
counterexample to `HC_7`: it contains a literal `K_7` and is not
minor-minimal.

The accompanying checker is
[`hc7_degree8_blocker_first_hit_concentration_barrier_verify.py`](hc7_degree8_blocker_first_hit_concentration_barrier_verify.py).

## 1. Principle refuted

The following inference is false without using `K_7`-minor exclusion or
proper-minor responses away from the selected edge:

> In the degree-eight obstructing-edge configuration, suppose the host is
> seven-connected, the obstruction is one edge `g`, every six-colouring of
> `G-g` gives its ends the same colour, and those ends are joined in every
> two-colour subgraph required by edge criticality.  Then the colours absent
> from the seven-vertex boundary have paths whose first internal vertices
> lie in different named far-side connected subgraphs.

The construction has three absent colours, but every corresponding path
first enters the same boundary-free named subgraph.

## 2. Construction

Start with the complete six-partite graph with parts

\[
\begin{aligned}
 A&=\{b,i_0,i_1,a_J\},&
 K&=\{q,j_0,j_1,k_I\},\\
 C&=\{r\},&D&=\{d\},&E&=\{e\},&F&=\{f\}.
\end{aligned}                                                    \tag{2.1}
\]

Add the single edge

\[
                              g=bi_0.                    \tag{2.2}
\]

Put

\[
 T=\{b,i_0,i_1,q,j_0,j_1,r\},
 \qquad
 R=\{a_J,k_I,d,e,f\}.                                  \tag{2.3}
\]

Add five new vertices `x_0,...,x_4`.  They induce the cycle

\[
                   x_0x_1x_2x_3x_4x_0,                 \tag{2.4}
\]

and every `x_s` is adjacent to every vertex of `T`.  There are no edges
from `L={x_0,...,x_4}` to `R`.  This completes the definition of `G`.

The set `T` is an actual order-seven separator.  The two open sides `L`
and `R` are connected.

## 3. The five named far-side connected subgraphs

Let

\[
 I=\{i_0,i_1\},\qquad J=\{j_0,j_1\},
 \qquad B=\{b,q,r\}.                                   \tag{3.1}
\]

With distinguished boundary vertex `r`, define

\[
\begin{aligned}
 Q_I&=\{i_0,i_1,k_I\},&
 Q_J&=\{j_0,j_1,a_J\},\\
 Q_b&=\{b\},& Q_q&=\{q\},& Q_0&=\{d,e,f\}.
\end{aligned}                                           \tag{3.2}
\]

These five subgraphs are connected, pairwise vertex-disjoint and pairwise
adjacent.  Each is adjacent to `r`; they cover `T-{r}`; and their boundary
traces are

\[
                         I,\quad J,\quad\{b\},\quad
                         \{q\},\quad\varnothing.        \tag{3.3}
\]

Thus `Q_0` is the named boundary-free connected subgraph.

On the other side, put

\[
\begin{aligned}
 C_0&=G[\{i_0,x_0\}],&C_1&=G[\{j_0,x_1\}],\\
 C_2&=G[\{i_1,x_2\}],&C_3&=G[\{j_1,x_3\}],&
 C_4&=G[\{x_4\}].
\end{aligned}                                           \tag{3.4}
\]

They are disjoint connected subgraphs with the four required singleton
root traces followed by an empty trace, and consecutive subgraphs are
adjacent cyclically.  The vertex `b` contacts `C_0,C_2`, the vertex `q`
contacts `C_1,C_3`, and

\[
 E_G(\{b\},I)=\{bi_0\},\qquad J\cup\{q\}\text{ is independent}. \tag{3.5}
\]

The two connected supports are adjacent through `x_0x_1`.

## 4. Universal nonextension at the obstructing edge

Delete `g`.  Colour the six parts in (2.1) with six distinct colours,
labelled `0,...,5` in the displayed order.  Extend this colouring to `L`
by

\[
       c(x_0),c(x_1),c(x_2),c(x_3),c(x_4)=3,4,3,4,5.   \tag{4.1}
\]

This is a proper six-colouring of `G-g`: the cycle is properly coloured,
every vertex of `L` sees only the boundary colours `0,1,2`, and `L` is
anticomplete to `R`.

More strongly, every six-colouring of `G-g` gives `b` and `i_0` the same
colour.  Indeed, the complete six-partite subgraph has six nonempty parts.
A colour cannot occur in two different parts, so a six-colouring assigns
exactly one colour to each part and is constant on every part.  Thus the
obstructing edge has the universal nonextension property, not merely one
selected favourable response.

Both ends of `g` see every one of the five other colours.  For each such
colour, its two-colour subgraph contains the complete bipartite core between
part `A` and the corresponding other core part, and therefore connects `b`
to `i_0`.  This realizes all the ordinary
edge-critical Kempe locks in every six-colouring of `G-g`.

## 5. Exact concentration of the three absent colours

The boundary `T` uses only the colours of `A,K,C`.  Its three absent
colours are the colours of `D,E,F`.  In the far closed shore, the only
vertex of each absent colour is respectively `d,e,f`.  Consequently every
simple two-colour path from `b` to `I` in (G[R\cup T]-g) for one of these
three colours has length two and has internal vertex `d`, `e`, or `f`.

All three internal vertices belong to the same named connected subgraph
`Q_0`.
Hence even universal nonextension, endpoint saturation, seven-connectivity,
five pairwise adjacent named subgraphs and the cyclic left-side supports do
not produce an injective first-hit assignment.

## 6. Seven-connectivity and exact trust boundary

The complete six-partite core has twelve vertices and largest part of
order four, so its vertex connectivity is eight.  If at most six vertices
are deleted from `G`, that core remains connected.  Every surviving
vertex of `L` still has a neighbour in the seven-set `T`, and hence joins
the surviving core.  Therefore `G` is seven-connected.

The seven vertices

\[
                       \{b,i_0,q,r,d,e,f\}              \tag{6.1}
\]

induce a `K_7`: the only two selected vertices in one multipartite class
are `b,i_0`, and (2.2) supplies their edge.  Deleting, for example, `x_0`
leaves this `K_7`, so `G` is also not minor-minimal among non-six-colourable
graphs.

Those are essential exclusions, not cosmetic shortcomings.  A
seven-connected, seven-chromatic, `K_7`-minor-free version of this barrier
would itself be a counterexample to `HC_7`.  The valid conclusion is
therefore narrow but decisive for the next proof step: first-hit diversity
cannot be deduced before explicitly using `K_7`-minor exclusion or a
proper-minor operation away from the obstructing edge.

## 7. Warning about a minimal seven-portal tree

A fixed inclusion-minimal tree spanning seven labelled contacts does not
by itself repair the problem.  Take a star with centre `z` and seven
leaves, with label `s` adjacent only at the leaf assigned to `s`.  The
whole star is the unique connected subgraph of the tree meeting all seven
labels.  Any connected repair using its centre, or any one of its leaves,
therefore leaves no disjoint seven-contact residual.

Subtrees of a tree do have the Helly property.  Thus, **if** each
Kempe-path intersection with a fixed contact tree is connected, their
tree traces yield two disjoint traces or one common tree vertex.  But the
common vertex need not separate the host: an additional path using other
colours may bypass it without changing any of the selected two-colour
subgraphs.  A positive tree-based theorem needs redundant labelled
contacts or a completeness theorem for all bridges attached to the tree;
inclusion-minimality alone is insufficient.
