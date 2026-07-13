# Uniform carrier-list state gluing

## 1. Theorem

Let `k>=2`, and let `G` be strongly `k`-contraction-critical:

\[
 \chi(G)=k,
 \qquad\text{and every proper minor of }G\text{ is }(k-1)\text{-colourable}.
\]

Suppose

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R
\]

with `S` nonempty, `L,R` nonempty, and no `LR` edges.  Fix
`1<=q<=k-1`, and assume:

1. `R` contains `q` pairwise vertex-disjoint connected subgraphs
   `P_1,...,P_q`, each **`S`-full** (every literal vertex of `S` has a
   neighbour in every `P_i`); and
2. `L` has a spanning partition
   `L=C_1 dotunion ... dotunion C_q` into nonempty connected, pairwise
   adjacent carriers.

For `s in S`, define

\[
 \Lambda(s)=\{i\in[q]:N_L(s)\cap C_i\ne\varnothing\}.
\]

### Theorem 1.1 (uniform carrier-list synchronization)

If `G[S]` has a proper list-colouring

\[
 \phi:S\longrightarrow[q],\qquad \phi(s)\in\Lambda(s),
\]

then `G` is `(k-1)`-colourable, a contradiction.

Thus a counterexample can retain such opposite packet/carrier systems only
if the literal boundary contact lists are not properly colourable from the
carrier palette.

## 2. Carrier-side state

Put `I_i=phi^{-1}(i)` and `A_i=C_i union I_i`.  Every `I_i` is independent,
and every one of its vertices has a literal neighbour in `C_i`; hence the
`A_i` are disjoint connected sets.  Contract all `A_i`.

This is a proper minor.  Indeed, the `q` sets cover the nonempty set `S`
as well as `L`, so at least one contains at least two vertices.  Its images
`a_1,...,a_q` form a clique because the carriers are pairwise adjacent.
The minor therefore has a `(k-1)`-colouring in which the images belonging
to distinct nonempty `I_i` have distinct colours.

Restrict this colouring to `R`, and give every literal `s in I_i` the
colour of `a_i`.  The result properly colours `G[R union S]`: independence
handles edges within a block, the clique of images handles edges between
blocks, and every original `sR` edge became an `a_iR` edge.  The equality
partition induced on `S` is exactly the family of nonempty `I_i`.

## 3. Packet-side state

Assign a distinct packet to every nonempty `I_i` and contract

\[
                         D_i=P_i\cup I_i.
\]

These sets are disjoint, connected, and nontrivial.  Their images form a
clique: for `i ne j`, fullness of `P_i` supplies an edge from `P_i` to every
literal member of the nonempty set `I_j`.  A `(k-1)`-colouring of this
proper minor, restricted to `L` and expanded over each `I_i`, therefore
properly colours `G[L union S]` and induces the same exact equality
partition on `S`.

Empty colour classes use no packet.

## 4. Gluing

The nonempty boundary blocks use pairwise distinct colours on each closed
shore.  The resulting bijection between the two sets of block colours
extends to a permutation of the `(k-1)`-colour palette.  After applying
that permutation on one side, the two colourings agree at every literal
vertex of `S`.  Since there are no `LR` edges, they glue to a proper
`(k-1)`-colouring of `G`. `square`

## 5. Exact scope

At `(k,q)=(7,3)` this contains the audited exact-seven spanning-triangle
list-state theorem.  The result is a uniform palette-to-labelled-carrier
principle: it manufactures the same equality state by literal contractions
on opposite shores and never identifies old colour names with model-bag
labels.

It does **not** assert that an appropriate carrier partition or list
colouring exists.  In the live exact-seven branch, that geometric existence
problem is precisely the crossed block-terminal web obstruction.
