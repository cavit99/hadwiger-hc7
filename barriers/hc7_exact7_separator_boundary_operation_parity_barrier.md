# Boundary operations do not by themselves synchronize an exact-seven interface

**Status:** written construction; finite boundary calculations have a
deterministic verifier; separate internal audit GREEN.  This is not a
counterexample to `HC_7`.

The construction strengthens the static paired-block parity barrier.  It
shows that even vertex deletion at either of the two new separator vertices,
and deletion or contraction of every edge of the boundary graph, can be
six-colourable without making the concrete one-sided boundary partition
extend through the opposite closed shore.

The accompanying checker is
[`hc7_exact7_separator_boundary_operation_parity_barrier_verify.py`](hc7_exact7_separator_boundary_operation_parity_barrier_verify.py).

## 1. Statement

There is a finite seven-connected graph `G` with an actual separation

\[
        V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
        \qquad |S|=7,
\]

such that the open shores `L,R` are nonempty, connected, anticomplete, and
each adjacent to every vertex of `S`.  Moreover:

1. `chi(G)=7`;
2. the two closed shores have disjoint six-colouring extension languages on
   `S`;
3. one closed shore admits the concrete partition

   \[
   \Pi_*=
   \{\{j_0,j_1,q\},\{b,z_1\},\{r\},\{z_2\}\};       \tag{1.1}
   \]

4. `G-z_1` and `G-z_2` are six-colourable; and
5. for every edge `e` of `G[S]`, both `G-e` and `G/e` are six-colourable.
6. for either open shore `X` and every nonempty independent set
   `I subseteq S`, contracting the connected set `X union I` gives a
   six-colourable proper minor.
7. each amplified open shore contains seven pairwise disjoint, pairwise
   adjacent connected subgraphs, each adjacent to every vertex of `S`.

Nevertheless `Pi_*` does not extend through the opposite closed shore.
Thus none of the boundary operations in items 4--6, considered only through
the returned colouring, forces the concrete one-sided partition on that
shore.

In fact item 7 is an explicit `K_7`-minor model, so the construction is
deliberately not `K_7`-minor-free.  It is also not asserted to have every
proper minor six-colourable.  In particular, it does not control operations
internal to the amplified open shores or edges between a separator vertex
and an open shore.  Target-minor exclusion and those untested operations are
the exact host-level hypotheses still available to a positive `HC_7`
argument.

## 2. The boundary and its two parity languages

Let

\[
 S=\{j_0,b,r\}\mathbin{\dot\cup}
   \{j_1,z_1,z_2\}\mathbin{\dot\cup}\{q\}
\]

and let

\[
              H=G[S]=K_3\mathbin{\dot\cup}K_3
                         \mathbin{\dot\cup}K_1,          \tag{2.1}
\]

with the two triangles displayed in that order.  Let `Omega` be the
partitions of `S` into at most six nonempty independent blocks of `H`, and
put

\[
 \mathcal E=\{\Pi\in\Omega:|\Pi|\text{ is even}\},
 \qquad
 \mathcal O=\{\Pi\in\Omega:|\Pi|\text{ is odd}\}.       \tag{2.2}
\]

The partition (1.1) belongs to `E`.  The two families are disjoint.

For every edge `e=xy` of `H`, let

\[
             \Lambda_e=\{\{x,y\}\}
                  \cup\{\{s\}:s\in S-\{x,y\}\}.       \tag{2.3}
\]

This has six blocks.  It is not proper on `H`, but it is proper on `H-e`.
Let

\[
                         \mathcal D=\{\Lambda_e:e\in E(H)\}.          \tag{2.4}
\]

For a family of partitions below, take all labelled six-colourings whose
equality partition belongs to that family.  The resulting relation is
closed under every permutation of the six colour names.  The finite
colouring-relation realization theorem of Dvorak--Swart (Theorem 3 of
*A note on extendable sets of colorings and rooted minors*,
arXiv:2504.07764) therefore gives two `S`-boundaried graphs whose labelled
six-colouring relations are respectively

\[
                         \mathcal E\cup\mathcal D,
             \qquad     \mathcal O\cup\mathcal D.       \tag{2.5}
\]

We recall the short augmentation so that no connectivity claim is hidden.
In either realizer add an open vertex `c`, and for every `s in S` add a
fresh length-two path `s-l_s-c`.  Join `c` by a fresh length-two path to
one selected vertex of every old open-interior component.  Every old
six-colouring extends: choose a colour on `c`, and each new internal
vertex then has to avoid at most two colours.  Conversely every colouring
of the augmentation restricts to the old realizer.  Thus the relation is
unchanged, while the open interior becomes connected and full to `S`.

Now replace every open vertex `u` by an independent false-twin class
`T_u` of order seven, replace every old open edge by the complete bipartite
graph between the corresponding classes, and copy every boundary
adjacency to all members of its class.  Uniformly colouring each class
lifts every old colouring; selecting one representative of each class
recovers an old colouring from every amplified colouring.  Hence the
relation is again unchanged.

Glue the two amplified boundaried graphs along `S`, with otherwise
disjoint open interiors, and finally add all edges of `H` on `S`.  Deleting
at most six vertices leaves a member of every false-twin class and at
least one boundary vertex.  Each open side therefore remains connected,
each remaining boundary vertex still meets both sides, and the two sides
are joined through a remaining boundary vertex.  The final graph is
seven-connected.

Every member of `D` is now excluded by its identified boundary edge.
Every member of `E union O` is proper on `H`.  Hence the exact extension
relations of the two closed shores in the final graph are `E` and `O`.
They are disjoint, so `G` is not six-colourable.

The boundary is induced.  Indeed, for every nonedge `xy` of `H`, each
parity family contains a partition having `{x,y}` as an exact block (this
is the one-block instance of the verified parity-cylinder calculation).
Neither realizer can therefore contain an additional boundary edge `xy`.
The augmentation makes both open interiors connected and full to `S`, as
claimed.

The amplification also exposes the omitted minor hypothesis explicitly.
Index the seven vertices in every false-twin class as

\[
                         u^1,\ldots,u^7.
\]

For `h in {1,...,7}`, let `C_h` contain `u^h` for every vertex `u` of
the connected pre-amplification open side.  Each `C_h` is connected and
adjacent to every boundary vertex.  The sets are disjoint.  For
`h ne k`, choose any old open edge `uv`; the complete bipartite replacement
contains the edge `u^h v^k`, so `C_h` and `C_k` are adjacent.  Thus
`C_1,...,C_7` themselves are an explicit `K_7`-minor model inside either
amplified open shore.

## 3. Exact chromatic number and boundary-edge operations

Fix any edge `e=xy` of `H`.  After deleting `e` from the final graph, the
common state `Lambda_e` in (2.5) survives every other boundary edge and
extends through both closed shores.  The two extensions align and give a
proper six-colouring of `G-e` in which `x,y` have the same colour.  The
same colouring descends to `G/e`.  Thus

\[
                        \chi(G-e)\le6,
             \qquad    \chi(G/e)\le6.                   \tag{3.1}
\]

Conversely, either graph cannot be five-colourable.  A five-colouring of
`G-e` would extend to a six-colouring of `G` by giving one end of `e` a
fresh colour.  A five-colouring of `G/e` similarly lifts to `G-e` with the
ends equal and then becomes a six-colouring of `G` after recolouring one
end.  Therefore both chromatic numbers in (3.1) equal six.

In particular, deleting one fixed edge `e` proves `chi(G)<=7`: use its
six-colouring and give one endpoint a seventh colour.  Since `G` is not
six-colourable,

\[
                              \chi(G)=7.                 \tag{3.2}
\]

## 4. Deleting either new separator vertex

The partition `Pi_*` and the following odd partition have the same
restriction to `S-z_1`:

\[
 \Pi_{z_1}=
 \{\{j_0,j_1,q\},\{b\},\{r\},\{z_2\},\{z_1\}\}.       \tag{4.1}
\]

Likewise `Pi_*` and

\[
 \Pi_{z_2}=
 \{\{j_0,j_1,q\},\{b,z_1\},\{r,z_2\}\}               \tag{4.2}
\]

have the same restriction to `S-z_2`.  The merged pair in (4.2) is
independent because its vertices lie in different triangles.  Thus
`Pi_*` extends through the even shore, (4.1)--(4.2) extend through the odd
shore, and after deleting the named vertex the two restrictions align.
Consequently

\[
                        \chi(G-z_1)=\chi(G-z_2)=6.       \tag{4.3}
\]

The upper bounds follow by gluing.  The lower bounds follow from
`chi(G)=7`, since deleting one vertex lowers chromatic number by at most
one.

Yet `Pi_*` itself lies in `E` and not in `O`, so it does not extend through
the odd closed shore.  The returned colourings of the two vertex-deleted
proper minors therefore do not synchronize the original seven-vertex
boundary partition.

## 5. Shore contractions through either new vertex

Fix either open shore `X`, retain the other closed shore, and let
`I subseteq S` be a nonempty independent set.  Each of `E,O` contains a
partition having `I` as an exact block.  Choose such a colouring of the
retained closed shore.

The set `X union I` is connected because `X` is connected and full to
`S`.  Contract it to one vertex `x_I`.  Give `x_I` the common colour of
`I` and keep the selected colouring on the retained vertices.  Every
vertex of `S-I` is adjacent to `X`, and hence has a different colour from
`x_I`.  Every retained open-shore vertex adjacent to `x_I` was adjacent
to a member of `I`, since the two open shores are anticomplete, and also
has a different colour.  This is a proper six-colouring of the contracted
graph.  The contraction is proper because the retained open shore is
nonempty.

In particular, these actual contractions include independent blocks
containing `z_1` or `z_2`, such as `{b,z_1}` and `{z_2}`.  They still do
not force (1.1) on the retained shore.

Even two disjoint adjacent connected subgraphs with the desired contacts
do not fix this.  In the notation of item 7, put

\[
                         P_1=C_1,
             \qquad     P_2=C_2\cup\cdots\cup C_7.      \tag{5.1}
\]

The sets `P_1,P_2` are disjoint, connected, adjacent, boundary-full, and
together cover the amplified open shore.  Contract

\[
             P_1\cup\{j_0,j_1,q\},
       \qquad P_2\cup\{b,z_1\}.                         \tag{5.2}
\]

The odd closed-shore colouring with partition (4.2) colours the resulting
minor: give the two quotient vertices the two corresponding block colours
and keep the odd colouring on the retained shore.  Thus (5.2) forces the
two large exact blocks in an actual proper-minor colouring while still
merging `r,z_2`.

The missing conclusion is precisely the distinctness of the remaining
two singleton blocks.  Any positive two-carrier theorem must obtain that
last adjacency from `K_7`-minor exclusion and the literal path geometry,
not merely from the two carriers.

## 6. Consequence for the Kempe-fan separator branch

The exact-seven outcome of the Kempe-fan theorem supplies a concrete
one-sided partition containing the two blocks

\[
                   J\cup\{q\},\qquad \{b,z_i\}.
\]

The present construction has precisely that displayed pattern and remains
unsynchronized even after the two new separator vertices are individually
deleted and every boundary edge is individually deleted or contracted.
It follows that a positive transition cannot use only the equality
partition returned by one such operation.

What the construction deliberately omits is exactly what the active host
still has: global `K_7`-minor exclusion, proper-minor responses on edges
entering the open shores, and the literal three Kempe paths whose Menger
separator produced `z_1,z_2`.  A successful next theorem must couple one
of those paths or an incident open-shore edge operation to labelled
geometry.  Independent boundary-state queries, even locally critical ones,
cannot suffice.

## 7. Verification and dependencies

Run

```text
python3 barriers/hc7_exact7_separator_boundary_operation_parity_barrier_verify.py
```

The checker enumerates the proper boundary states, verifies `Pi_*`, the
two vertex-deletion pairs, every edge state `Lambda_e`, and the parity
exact-block property used to keep the boundary induced.

- [paired-block parity barrier](hc7_exact7_paired_block_trace_parity_barrier.md)
- [complementary-state realization barrier](hc7_state_realization_barrier.md)
- [Kempe-fan packing or exact-seven boundary](../results/hc7_kempe_fan_or_exact_seven_boundary.md)
