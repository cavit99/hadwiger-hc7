# A minimal contraction bag in a regenerated `K_6` model

**Status:** written proof; separate internal audit in
[`hc7_contracted_edge_k6_model_normalization_audit.md`](hc7_contracted_edge_k6_model_normalization_audit.md).

This note gives a uniform model normalization for every edge of a
hypothetical minor-minimal counterexample to `HC_7`.  It supplies a genuine
finite descent inside the branch set containing the contracted edge.  It
also shows that unused vertices cannot provide the clean external repair
needed to split that branch set.  Nothing here proves `HC_7`.

## 1. Setting

Let `G` be seven-connected and satisfy

\[
 \chi(G)=7,\qquad K_7\not\preccurlyeq G,
 \qquad\text{and every proper minor of }G\text{ is six-colourable}. \tag{1.1}
\]

Fix an edge `e=pv`, put `H=G/e`, and denote the contraction image by `x`.

### Theorem 1.1 (minimal contraction-bag normalization)

There is an `x`-rooted labelled `K_6`-minor model

\[
                         (D,B_1,\ldots,B_5)              \tag{1.2}
\]

in `H` with the following properties.  Put

\[
                 U=D\cup B_1\cup\cdots\cup B_5.         \tag{1.3}
\]

1. `chi(H)=6` and `H` is six-connected.
2. If `Z` is a nonempty subset of `D-{x}` for which both `H[Z]` and
   `H[D-Z]` are connected, then

   \[
      \left|\{i:E_H(D-Z,B_i)=\varnothing\}\right|\ge2.  \tag{1.4}
   \]

3. `H[D-x]` has at most two components.  Each component contains every
   `D`--`B_i` edge for at least two values of `i`, and the corresponding
   label sets are disjoint for distinct components.
4. Every component `Q` of `H-U` satisfies `N_H(Q) subseteq D` and
   `|N_H(Q)|>=6`.  If equality holds, then `x in N_H(Q)` and

   \[
      (N_H(Q)-\{x\})\cup\{p,v\}                         \tag{1.5}
   \]

   is an actual order-seven boundary in `G`; every complementary component
   is adjacent to every literal vertex of that boundary.
5. The lift

   \[
                 D^\uparrow=(D-\{x\})\cup\{p,v\}        \tag{1.6}
   \]

   is connected.  It has a partition into connected adjacent sets
   `A,W`, with `p in A` and `v in W`.  If both sets are adjacent to every
   `B_i`, then

   \[
                         A,W,B_1,\ldots,B_5             \tag{1.7}
   \]

   is an explicit `K_7`-minor model.  Otherwise the full neighbourhood of
   a deficient side is an actual separator of order at least seven.
6. No connected subgraph disjoint from the lifted model can repair a
   missing adjacency from one side of (1.6) to a `B_i`: every such connected
   subgraph is anticomplete to all five `B_i`.

The model in (1.2) is chosen by minimizing `|D|` and, subject to that,
maximizing `|U|`.

## 2. Chromatic number and connectivity after contraction

The graph `H` is a proper minor, so `chi(H)<=6`.  If `H` had a proper
five-colouring, expand `x` over `p,v`, keep `p` in the colour of `x`, and
give `v` a fresh sixth colour.  This is a proper six-colouring of `G`, a
contradiction.  Hence

\[
                              \chi(H)=6.                 \tag{2.1}
\]

Suppose `S` separates `H` and `|S|<=5`.  If `x notin S`, the same set
separates `G`: the two preimages of `x` remain in the one component of
`H-S` containing `x`, and no other component has an edge to either of them.
If `x in S`, replace `x` by `p,v`; this gives a separator of `G` of order at
most six.  Both alternatives contradict seven-connectivity.  Thus `H` is
six-connected.

Known `HC_6`, applied to (2.1), gives a `K_6` model in `H`.  The graph `H`
is connected.  If `x` is outside the model, take a shortest path from `x`
to its union and absorb that path into the first branch set it meets.  This
gives an `x`-rooted model.  Among all labelled `x`-rooted models choose one
minimizing `|D|`, where `x in D`, and then maximizing the order of the union
`U`.  This proves item 1 and defines the extremal model used below.

## 3. Detachable pieces carry at least two labels

Let `Z` satisfy item 2 and put

\[
             \Lambda(Z)=\{i:E_H(D-Z,B_i)=\varnothing\}. \tag{3.1}
\]

If `Lambda(Z)` is empty, replace `D` by `D-Z`.  This remains connected,
contains `x`, and is adjacent to every other branch set, contradicting the
minimum choice of `|D|`.

If `Lambda(Z)={j}`, then every old `D`--`B_j` edge has its end in `Z`, so
`B_j union Z` is connected.  Connectivity of `D` supplies an edge between
`Z` and `D-Z`; this keeps `D-Z` adjacent to the enlarged `B_j`.  The old
`B_j` supplies all adjacencies from the enlarged branch set to the other
four `B_i`, while the definition of `Lambda(Z)` preserves every adjacency
from `D-Z` to those four sets.  Thus

\[
            (D-Z,B_1,\ldots,B_j\cup Z,\ldots,B_5)       \tag{3.2}
\]

is another `x`-rooted `K_6` model with a smaller root branch set, again a
contradiction.  This proves (1.4).

Let `K` be a component of `H[D-x]`.  Since `H[D]` is connected, `K` is
adjacent to `x`, and `D-K` is connected.  Hence (1.4) applies to `K`.
Moreover, if `i in Lambda(K)`, then every `D`--`B_i` edge has its end in
`K`.  The monopoly label sets `Lambda(K)` of distinct components are
therefore disjoint.  Each has order at least two and there are only five
labels.  This proves item 3.

## 4. Components outside the extremal model

Let `Q` be a component of `H-U`.  If `Q` has a neighbour in some `B_i`,
absorb all of `Q` into that branch set.  This preserves the labelled
`K_6` model, leaves `D` unchanged and strictly enlarges `U`, contrary to
the secondary extremal choice.  Therefore

\[
                              N_H(Q)\subseteq D.          \tag{4.1}
\]

Six-connectivity gives `|N_H(Q)|>=6`.  Suppose equality holds.  If
`x notin N_H(Q)`, the same six vertices separate `Q` in `G`, contrary to
seven-connectivity.  Hence `x in N_H(Q)`.  In `G`,

\[
 N_G(Q)\subseteq (N_H(Q)-\{x\})\cup\{p,v\},             \tag{4.2}
\]

whose right side has order seven.  The set separates `Q` from the five
nonempty branch sets, so seven-connectivity forces equality in (4.2).
This proves (1.5).  If a component behind this seven-boundary missed one
boundary vertex, its full neighbourhood would have order at most six and
would separate it from another component.  Thus every complementary
component is boundary-full.  Item 4 follows.

## 5. Lifting and splitting the contraction bag

Replace `x` in `D` by `p,v`.  Every component of `H[D-x]` has a neighbour
in at least one of `p,v`, and the edge `pv` joins the two possible
attachment sides.  Hence `D^uparrow` is connected.  Choose a spanning tree
of `G[D^uparrow]` containing `pv` and delete that tree edge.  Its two vertex
sets `A,W` are connected, adjacent, partition `D^uparrow`, and contain
`p,v`, respectively.

If each side is adjacent to every `B_i`, the seven sets in (1.7) are
pairwise disjoint, connected and pairwise adjacent.  They form a `K_7`
model.  Otherwise, suppose `W` misses `B_j`.  Then `N_G(W)` separates the
nonempty connected set `W` from the nonempty branch set `B_j`, so its order
is at least seven.  The same argument applies if `A` is deficient.  This
proves item 5.

Finally, any connected subgraph disjoint from the lifted model corresponds
to a connected set in `H-U`, and hence lies in one component `Q`.  By
(4.1) it is anticomplete to every `B_i`.  It therefore cannot restore any
missing adjacency from `A` or `W` to a named branch set.  This proves item
6.

## 6. Exact scope

The theorem gives a strict descent whenever a detachable root-bag piece
carries at most one named adjacency.  Its residual root bag is a singleton,
or has one or two components after deletion of `x`, each monopolizing at
least two labels.

The theorem does **not** upper-bound the neighbourhood of a deficient split
side.  It also shows why spanning absorption is not a repair mechanism:
vertices left outside the extremal model have no contact with the five
foreign branch sets.  Any successful continuation must repartition one or
more named branch sets, reselect the model, or use a proper-minor colouring
response to force an exact order-seven boundary.  Palette colours do not
identify the five labels.  The no-repair conclusion concerns a connected
subgraph wholly outside `U`; it does not exclude a construction combining
an outside component with vertices reassigned from `D`.

## 7. Dependencies

- Hadwiger's Conjecture for `t=6`.
- [prescribed spokes or a coloured exact-seven separator](hc7_order8_prescribed_spoke_reduction.md),
  used only as motivation for the remaining alignment problem.
