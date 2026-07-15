# Common-deletion dominating-five substrate

**Status:** proved and independently audited.  This is a uniform global
replacement for the failed two-colour exchange in the atomic twin seam.  It
does not yet allocate the five model bags to prescribed boundary duties.

## 1. Statement

Let `G` be a graph with `chi(G)=7` such that every proper minor of `G` is
six-colourable.  Let

\[
                         e=zu,\qquad f=dt
\]

be vertex-disjoint edges, and put

\[
                         H=G-\{e,f\},                  \tag{1.1}
\]

where the braces in (1.1) mean **edge deletion**.

### Theorem 1.1

The common deletion `H` satisfies

\[
                         5\leq \chi(H)\leq 6.          \tag{1.2}
\]

Consequently `H` has a dominating `K_5` model.  It can be normalized as

\[
                    (T_1,T_2,P,\{v\},\{w\}),          \tag{1.3}
\]

where `P` is a nonempty path and `H[P union {v,w}]` is an induced
cycle

\[
                           C=vPw v.                    \tag{1.4}
\]

Moreover, every edge `xy` of `C` can be chosen as the last two singleton
bags: for each `xy in E(C)`,

\[
                 (T_1,T_2,C-\{x,y\},\{x\},\{y\})      \tag{1.5}
\]

is a dominating `K_5` model in `H` (with the third bag interpreted as the
connected path induced by the remaining cycle vertices).

Here a dominating `K_5` model is an ordered tuple of pairwise disjoint
connected nonempty subgraphs such that every vertex of a later bag has a
neighbour in every earlier bag.

## 2. Proof

Since `H` is a proper minor obtained by edge deletions, the minimality
hypothesis gives `chi(H)<=6`.

Suppose that `H` has a colouring with at most four colours.  Give `z` a
new fifth colour and give `d` a new sixth colour, leaving all other colours
unchanged.  The two edges are vertex-disjoint.  Thus every old edge remains
proper, every edge incident with `z` has differently coloured ends, every
edge incident with `d` has differently coloured ends, and the restored
edges `zu` and `dt` are proper.  This is a six-colouring of `G`, contrary
to `chi(G)=7`.  Hence `chi(H)>=5`, proving (1.2).

By the Dominating 4-Colour Theorem of Girao, Illingworth, Mohar, Norin,
Steiner, Tamitegama, Tan, Wood and Yip, every graph with no dominating
`K_5` model is four-colourable.  Its contrapositive supplies a dominating
model

\[
                         (T_1,T_2,T_3,T_4,T_5)
\]

in `H`.

Choose `w in T_5`.  Since every vertex of `T_5` has a neighbour in `T_4`,
choose `v in T_4` adjacent to `w`.  Replacing `T_4,T_5` by the singletons
`{v},{w}` preserves every domination relation: each of `v,w` has a
neighbour in every earlier bag, and `vw` is an edge.

Both `v` and `w` have a neighbour in the connected subgraph `T_3`.
In `H[T_3 union {v,w}]-vw`, choose a shortest `v-w` path.  Its internal
vertices form a nonempty path `P` contained in `T_3`.  Shortestness makes
the path chordless in `H`; restoring `vw` therefore gives the induced cycle
(1.4) in `H`.  The two edges deleted in (1.1) may be chords in `G`, so no
inducedness claim is made in the original host.
Replace `T_3` by `P`.  Every vertex of `P` is still dominated by `T_1,T_2`,
and the end edges of the path show that `P` dominates both singleton bags.
This proves (1.3)--(1.4).

Finally let `xy` be any edge of `C`.  Deleting the adjacent vertices
`x,y` from a cycle leaves a nonempty connected path.  Every remaining cycle
vertex is dominated by `T_1,T_2`; each of `x,y` has its other cycle
neighbour in that path; and `xy` gives the last domination relation.
Thus (1.5) is a dominating `K_5` model.  \(\square\)

## 3. Why this is global rather than another local receiver

The theorem applies to **every** pair of vertex-disjoint edges in the
minimal-counterexample kernel.  It is stated in the common edge-deletion
host in which both named contraction colourings can be compared, and the
terminal edge can rotate around one literal induced cycle.  It therefore
supplies one coherent five-bag object across the separating and bypass
branches; it is not ranked by a chosen portal, lobe, colouring, or twin
boundary.

The missing implication is now an allocation theorem, not an existence
theorem:

> Given the normalized model (1.3) for the two named response edges, either
> allocate its five ordered bags label-faithfully to five required literal
> duties while preserving two reserve carriers, reproduce one exact state
> on complementary sides, extract a fixed pair from the terminal cycle, or
> return a strictly smaller member of the globally ranked exact-seven
> family.

The theorem itself does not imply any of those outcomes.  The bags may
consume both old packets and both lobes, and domination does not prescribe
which bag meets which boundary vertex.  Treating domination contacts as
labelled duties would repeat the palette-to-carrier error.

## 4. Source

The external input is Theorem 1.1 of:

António Girão, Freddie Illingworth, Bojan Mohar, Sergey Norin, Raphael
Steiner, Youri Tamitegama, Jane Tan, David R. Wood and Jung Hon Yip,
*The Dominating 4-Colour Theorem*, arXiv:2605.10112 (2026),
<https://arxiv.org/abs/2605.10112>.
