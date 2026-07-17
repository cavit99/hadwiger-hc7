# Normal form around a simplicial component in the defect-one branch

**Status:** written proof; separate internal audit GREEN.  This note
collects consequences of the audited component-defect and bipartite
total-contraction theorems.  It does not prove that every adjacent-pair
configuration reaches the hypotheses below, does not produce compatible
colourings across a separation, and does not prove `HC_7`.

## 1. Fixed setup

Let `G` be a seven-chromatic graph with no `K_7` minor such that every
proper minor of `G` is six-colourable.  In particular, the standard
contraction-critical connectivity theorem makes `G` seven-connected.  Use
the unique-deficiency colour-matched-path setup at one fixed cut `q`.  Thus

\[
                         C_q,\qquad U_q,\qquad \{z\}                 \tag{1.1}
\]

are three pairwise disjoint, connected, pairwise adjacent vertex sets.  The
four protected branch sets are

\[
                         \mathcal K=\{X,D_1,D_2,D_3\}.               \tag{1.2}
\]

For each \(K\in\mathcal K\), let \(\mathcal E_K(q)\) be the components of
`G[K-V(P)]` which are adjacent to all three sets in (1.1).  Equivalently,
these are the components whose valid-cut interval contains `q` and which
are adjacent to `z`.

Choose a nonempty subfamily

\[
                  \mathcal L_K\subseteq\mathcal E_K(q)
                  \qquad(K\in\mathcal K),                           \tag{1.3}
\]

and let `J` be their component-contact graph: its vertices are the selected
components, retaining their four labels, and two vertices are adjacent
exactly when their represented connected subgraphs are adjacent in `G`.
Assume

1. `J` has component defect `Delta(J)=1`; and
2. the selection (1.3) is inclusion-maximal, at this fixed path and cut,
   among selections with all four labels represented and defect one.

The audited component-defect theorem implies that `J` is a two-tree.  In
particular, `J` has a simplicial vertex `v` of degree two.  Let `L` be the
component of `G[K-V(P)]` represented by `v`, and let `M,N` be the connected
subgraphs represented by the two neighbours of `v` in `J`.  The vertices
representing `M,N` are adjacent in `J`.

The inclusion-maximality in item 2 is only a normalization at the fixed
choice of `P,q`.  It is not asserted to be a decreasing parameter under a
change of path, cut, rooted model, or proper-minor colouring.

## 2. Components omitted by an inclusion-maximal selection

For an unselected component

\[
                         W\in\mathcal E_K(q)-\mathcal L_K,           \tag{2.1}
\]

and for each `K' != K`, let `t_{K'}` be the number of connected components
of the old bichromatic graph

\[
                         J[\mathcal L_K\cup\mathcal L_{K'}]
\]

which contain a neighbour of the new quotient vertex represented by `W`.

### Proposition 2.1

Every component `W` in (2.1) satisfies

\[
                              \sum_{K'\ne K}t_{K'}\le 1.             \tag{2.2}
\]

#### Proof

Add `W` to the selected family in its own part.  Proposition 4.1 of the
component-defect theorem gives

\[
              \Delta(J+W)=\Delta(J)+2-\sum_{K'\ne K}t_{K'}
                         =3-\sum_{K'\ne K}t_{K'}.                   \tag{2.3}
\]

The augmented family still has all four labels represented and every
represented component is adjacent to the three sets in (1.1).  Since `G`
has no `K_7` minor, Theorem 2.1 of the same result gives
`Delta(J+W)>=1`; hence the sum in (2.2) is at most two.  If it were exactly
two, (2.3) would give `Delta(J+W)=1`, contradicting the assumed
inclusion-maximality.  Therefore it is at most one.  \(\square\)

The proposition counts old *bichromatic connected components*, not actual
attachment vertices.  By itself it does not prevent several contacts from
being concentrated inside one such component.

## 3. The full neighbourhood of a simplicial component

### Proposition 3.1

The pair

\[
       \bigl(L\cup N_G(L),\;V(G)-L\bigr)                         \tag{3.1}
\]

is an actual separation with two nonempty open sides.  Consequently,

\[
                              |N_G(L)|\ge 7.                        \tag{3.2}
\]

If `G` has no separation of order seven, then `|N_G(L)|>=8`.

#### Proof

All four labels are represented, so `J` has at least four vertices.  Apart
from `v` and its two neighbours there is therefore a vertex `w` of `J`.
Since `v` has degree two, `vw` is not an edge.  The connected component
represented by `w` is disjoint from `L` and has no edge to `L`.  It is thus
contained in

\[
                         V(G)-\bigl(L\cup N_G(L)\bigr),              \tag{3.3}
\]

while `L` is nonempty.  The full open neighbourhood `N_G(L)` is the
intersection in (3.1), so (3.1) is an actual separation with the required
two open sides.  Seven-connectivity proves (3.2), and excluding an
order-seven separation gives the final assertion.  \(\square\)

This proposition supplies a genuine host separation but no upper bound on
its order and no colouring on its boundary.

## 4. The local five-branch-set support and the saturated quotient

### Proposition 4.1

The five connected subgraphs

\[
                         C_q,\quad U_q,\quad\{z\},\quad M,\quad N    \tag{4.1}
\]

are pairwise disjoint and pairwise adjacent.  They are therefore the branch
sets of an explicit `K_5`-minor model.  The subgraph `L` is adjacent to all
five branch sets in (4.1), so adjoining `L` gives an explicit `K_6`-minor
model.

#### Proof

The first three sets are pairwise adjacent by the fixed path-cut setup.
Every selected component is adjacent to each of those three sets.  Finally,
the two neighbours of a simplicial vertex in a two-tree are adjacent, so
`M` and `N` are adjacent.  These are all required adjacencies.  The vertex
`v` is adjacent in `J` to the vertices represented by `M,N`, and eligibility
of `L` supplies its other three adjacencies.  \(\square\)

Let `H` be the quotient obtained by contracting each set in (1.1) and each
selected component to one vertex, deleting every other vertex, and
suppressing parallel edges.  Thus

\[
                              H=K_3\vee J,                           \tag{4.2}
\]

where `vee` denotes graph join.

### Proposition 4.2

The quotient `H` is edge-maximal among `K_7`-minor-free graphs on its
vertex set: for every nonedge `ab` of `H`, the graph `H+ab` contains a
`K_7` minor.

Let `W` be any connected subgraph of `G` disjoint from all the connected
sets contracted to form `H`.  Record the vertices of `H` whose represented
sets are adjacent to `W`.  These vertices induce a clique of order at most
five in `H`.

In particular, if `W` is an unselected eligible component as in (2.1), then
it is adjacent to at most one selected component.

#### Proof

The graph `H` is a minor of `G`, so it has no `K_7` minor.  Every nonedge of
`H` has both ends in `J`.  Since a two-tree is edge-maximal
`K_4`-minor-free, adding that edge to `J` produces a `K_4` minor.  Together
with the three singleton vertices of the joined `K_3`, its four branch
sets give a `K_7` minor in `H+ab`.  This proves edge-maximality.

Now contract `W` to a new vertex `w` at the same time as the connected sets
defining `H`, and delete all other vertices.  If two attachment vertices
`a,b` were nonadjacent in `H`, contracting the quotient edge `wa` would
produce a graph containing `H+ab` as a subgraph.  The preceding paragraph
would then give a `K_7` minor in `G`, a contradiction.  Hence the attachment
vertices form a clique.  A clique of order six together with `w` would be a
`K_7` subgraph of this quotient, so its order is at most five.

Finally, an eligible `W` is adjacent to the three vertices of the joined
`K_3`.  Its selected-component neighbours therefore form a clique of order
at most two in `J`.  If there were two, they would have different protected
labels because vertices with the same label are nonadjacent.  Each would
contribute at least one to a different summand in (2.2), contradicting
Proposition 2.1.  Thus `W` has at most one selected-component neighbour.
\(\square\)

The clique conclusion concerns contracted branch-set labels.  It neither
bounds the number of attachment vertices in `G` nor says that the full
neighbourhood of `W` is a clique in `G`.

There is nevertheless a useful simultaneous absorption consequence.  Let

\[
 \mathcal U=C_q\cup U_q\cup\{z\}
       \cup\bigcup_{K\in\mathcal K}\bigcup_{R\in\mathcal L_K}V(R)  \tag{4.3}
\]

be the union of all connected sets represented in `H`.  Let
\(\mathcal A_L\) be the set of components of \(G-\mathcal U\) which are
adjacent to `L`, and put

\[
                         L^*=L\cup\bigcup_{W\in\mathcal A_L}V(W).   \tag{4.4}
\]

### Corollary 4.3

The set `L^*` is connected and

\[
             N_G(L^*)\subseteq C_q\cup U_q\cup\{z\}\cup M\cup N. \tag{4.5}
\]

Moreover,

\[
              \bigl(L^*\cup N_G(L^*),\;V(G)-L^*\bigr)              \tag{4.6}
\]

is an actual separation with two nonempty open sides, and its order is at
least seven.

#### Proof

Every component in \(\mathcal A_L\) is connected and has an edge to `L`,
so `L^*` is connected.  For such a component `W`, its attachment clique in
`H` contains the vertex `v` represented by `L`.  Therefore all its other
attachment vertices belong to `N_H(v)`.  Since `v` has exactly two
neighbours in `J`,

\[
                         N_H(v)=\{C_q,U_q,z,M,N\},                  \tag{4.7}
\]

where the notation on the right denotes the five quotient vertices
represented by those connected subgraphs.

Distinct components of \(G-\mathcal U\) are anticomplete.  Consequently,
after every member of \(\mathcal A_L\) is absorbed simultaneously, no
outside component remains adjacent to `L^*`; and (4.7) gives (4.5).

As in Proposition 3.1, choose a selected component represented by a vertex
of `J` other than `v` and its two neighbours.  It is nonadjacent to `L`.
It is also nonadjacent to every absorbed component, because it is not among
the five quotient vertices in (4.7).  Hence it lies outside
`L^* union N_G(L^*)`, proving that (4.6) has two nonempty open sides.
Seven-connectivity gives the order bound.  \(\square\)

The right side of (4.5) is a union of five potentially large branch sets,
not a set of five vertices.  Absorption therefore gives no upper bound on
the separator order.  Also, `L^*` need no longer be a component of
`G[K-V(P)]`; in particular, it is not a replacement vertex in the original
four-labelled component-contact graph without a new proof.

## 5. The extra conclusion when the simplicial component lies in `X`

Recall that `X=A\cup B` is the connected induced bipartite subgraph from
the star--Kempe compression and that the colour-matched path meets `X` only
in one side of this bipartition.  Suppose the label of `L` is `X`.

### Proposition 5.1

If `|V(L)|=1`, Proposition 3.1 already gives a full-neighbourhood
separation.

If `|V(L)|>=2`, fix a spanning tree of `G[L]` and a six-colouring of the
proper minor `G/L`.  There is a tree edge which splits

\[
                              L=L^-\mathbin{\dot\cup}L^+             \tag{5.1}
\]

into nonempty connected adjacent sets such that each of `L^-` and `L^+`
has an outside neighbour of every colour other than the colour of the
contracted image of `L`.  For this split, one of the following holds.

1. The seven sets consisting of `L^-`, `L^+`, and the five sets in (4.1)
   form an explicit `K_7`-minor model in `G`.
2. One shore \(Y\in\{L^-,L^+\}\) is nonadjacent to one set `F` in (4.1);
   then

   \[
       \bigl(Y\cup N_G(Y),\;V(G)-Y\bigr)                           \tag{5.2}
   \]

   is an actual separation with two nonempty open sides and separator order
   at least seven.

#### Proof

The component `L` is an induced connected bipartite subgraph of `G`.
Because it is nontrivial, `G/L` is a proper minor and has a six-colouring
under the contraction-critical hypotheses of the colour-matched-path setup.
The audited bipartite bilateral full-palette theorem applied to `L`, the
chosen spanning tree, and this colouring gives (5.1), including connectedness,
adjacency, and the simultaneous five-colour exposure.

If each of `L^-` and `L^+` is adjacent to all five sets in (4.1), those five
sets are pairwise adjacent by Proposition 4.1, and the deleted tree edge
joins `L^-` to `L^+`.  The seven displayed sets are therefore pairwise
disjoint, connected, and pairwise adjacent, proving item 1.

Otherwise choose a missed set `F` and the corresponding shore `Y`.  The set
`F` is disjoint from `Y` and has no edge to it, so it lies in the second
open side of (5.2).  The first open side contains `Y`.  Hence (5.2) is an
actual separation.  Its order
is at least seven by seven-connectivity.  \(\square\)

The simultaneous five-colour exposure in Proposition 5.1 does **not**
identify those five colours with the five branch sets in (4.1).  The
neighbour witnessing a colour may lie elsewhere in `G-L`; even when it lies
in one of those branch sets, no theorem here preserves that identification
through another contraction or path exchange.  Moreover, the colouring of
`G/L` is not a colouring of either closed shore of (5.2), and the proposition
does not produce a common equality partition on its boundary.  Thus item 2
is only a raw separation, not the colour-gluing conclusion required by the
active `HC_7` target.

Proposition 5.1 is deliberately applied to the original component `L`, not
to the enlarged set `L^*` from Corollary 4.3.  The absorbed outside
components need not preserve bipartiteness.

## 6. Exact trust boundary

The proved conclusions above normalize one conditional defect-one
configuration.  They do not prove any of the following.

1. Every hypothetical counterexample has a valid four-labelled defect-one
   selection at a colour-matched-path cut.
2. A proper-minor operation preserves the fixed path, cut, four labels, or
   inclusion-maximal selection.
3. A simplicial vertex can be chosen with label `X`; Proposition 5.1 does
   not apply when its label is one of `D_1,D_2,D_3`.
4. Any separator returned above has order exactly seven.
5. The two closed shores of a returned separation admit six-colourings with
   the same boundary equality partition.
6. The quotient attachment clique records the number or placement of
   attachment vertices in `G`.
7. The normalization is a strict descent or excludes the infinite family
   `K_3\vee J` with `J` a two-tree.

The bipartite total-contraction theorem has a separate GREEN audit, but that
older audit does not identify the audited source by the current content-hash
convention.  Its mathematical use here is exactly its stated scope:
connected induced bipartite `L`, one colouring of `G/L`, and the two
connected adjacent shores with simultaneous five-colour exposure.

## 7. Dependencies

- [component-contact defect and two-tree equality](../results/hc7_component_contact_defect_theorem.md)
- [all-cut valid-interval exchange](../results/hc7_colour_matched_path_all_cut_interval_exchange.md)
- [colour-matched path component exchange](../results/hc7_colour_matched_path_component_exchange.md)
- [bipartite bilateral full-palette split](../results/hc7_near_k7_bipartite_total_contraction.md)
- [audit of the bipartite split theorem](../results/hc7_near_k7_bipartite_total_contraction_audit.md)
