# Counterexample to the connected attachment-tree equality corollary

**Status:** written counterexample to the connected-tree interpretation;
separately internally audited in
[`kawarabayashi_yu_forest_extremal_structure_counterexample_audit.md`](kawarabayashi_yu_forest_extremal_structure_counterexample_audit.md).

This note concerns a proposed connected-tree application of Theorem 5 in
Kawarabayashi--Yu,
*Connectivities for k-knitted graphs and for minimal counterexamples to
Hadwiger's Conjecture*,
[arXiv:2606.01586v2](https://arxiv.org/abs/2606.01586) (4 June 2026).
It does not challenge the strict reduction in their Theorem 4.  Because
the published statement is phrased for a "forest" rather than a connected
tree, this note does not claim a counterexample to that literal wording;
it shows that the connected corollary needed by the present project does
not follow.  It is not a counterexample to any statement about Hadwiger's
Conjecture.

## The claimed extremal conclusion

Under the useful connected interpretation, the cited theorem asserts the
following.  Let `T` be a tree containing a boundary set `P`, with every
leaf of `T` in `P`, and let `w` be outside `T` with

\[
                         |N(w)\cap V(T)|=|P|+1.             \tag{1}
\]

If there is no connected tree through `P union {w}` having fewer vertices
than `T`, then `T` is a subdivided star with a centre of degree `|P|`, and
the neighbours of `w` in `T` are that centre and all of its immediate
neighbours.

If the phrase "forest spanning `P`" instead permits arbitrary disconnected
forests, the connected consequence does not follow.  In the example below,
the edges `wa,wc` together with the isolated vertices `b,d` give a
five-vertex forest through `P union {w}` whose degree-one leaves lie in
`P`; the same remains true if isolated vertices are also called leaves.
Thus connectedness, or an equivalent requirement preserving the boundary
partition, is necessary for the statement to have the intended content.

## Counterexample

Let `T` have vertices

\[
                         z_1,z_2,a,b,c,d
\]

and edges

\[
              z_1z_2,\ z_1a,\ z_1b,\ z_2c,\ z_2d.          \tag{2}
\]

Take

\[
                         P=\{a,b,c,d\}.
\]

Thus the leaves of `T` are exactly `P`; `T` is a double star and has six
vertices.  Add a vertex `w` with neighbourhood in `T`

\[
                   N(w)\cap V(T)=\{z_1,z_2,a,c,d\}.         \tag{3}
\]

Equation (1) holds because both sides equal five.

Every connected subgraph containing `P union {w}` must also contain
`z_1`: within the graph induced by `V(T) union {w}`, the boundary vertex
`b` has the unique neighbour `z_1`.  Hence every such connected subgraph
has at least the six vertices

\[
                         P\cup\{w,z_1\}.                    \tag{4}
\]

The lower bound is attained.  The five edges

\[
                         wa,\ az_1,\ z_1b,\ wc,\ wd          \tag{5}
\]

form a six-vertex tree containing `P union {w}` whose leaves are in `P`.
Consequently there is no strictly smaller connected replacement tree.

However, `T` has maximum degree three.  It is not a subdivision of a star
with four leaves and a degree-four centre.  The asserted extremal
conclusion therefore fails.

## Exact scope

The strict threshold remains valid: if an outside vertex has at least
`|P|+2` neighbours in a tree minimally spanning `P`, a direct shortest-path
argument produces a smaller replacement tree.  The counterexample shows
only that lowering the threshold by one does not leave a unique
subdivided-star equality case.  Any attachment-tree descent used in this
repository must retain a broader tight family.
