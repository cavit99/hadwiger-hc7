# Exact-seven sparse-gate median exchange

## 1. Scope

Assume the literal exact-seven `(1,3)` setting

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad |S|=7,
\]

with no `LR` edges and three pairwise disjoint `S`-full packets in
`R`.  Assume `L` is three-connected.  Let

\[
                         T=\{t_1,t_2,t_3\}
\]

be a literal three-cut for which `L-T` has exactly two components
`C,D`.  This note gives a literal construction for the sparse-gate
residue left by `hc7_exact7_two_lobe_gate_exchange.md`.

The point is that a nontrivial lobe supplies three *labelled arms* at
the gate.  A minimal connector for those arms is either a rooted
triangle, a three-arm `Y`, or a path with one named median.  A literal
gate edge repairs exactly the missing leaf--leaf adjacency of the last
two forms.

## 2. Three labelled arms

For a lobe `K` of order at least three, the forbidden-label portal
matching lemma supplies distinct vertices

\[
                 x_1,x_2,x_3\in K
\]

and distinct labels `s_1,s_2,s_3 in S`, with `x_i s_i` literal edges.
The lobe-to-gate linkage lemma supplies three vertex-disjoint paths
`Q_1,Q_2,Q_3` in `G[K union T]`, after permuting indices, such that

\[
              x_i\in Q_i,\qquad t_i\in Q_i,
              \qquad Q_i\cap T=\{t_i\}.                 \tag{2.1}
\]

Put `A_i=Q_i-t_i`.  The `A_i` are nonempty, pairwise disjoint,
connected subgraphs of `K`, and `A_i` has an edge to `t_i`.

### Lemma 2.1 (three-terminal connector normal form)

Let `K` be connected and let `A_1,A_2,A_3` be disjoint nonempty
connected subgraphs.  At least one of the following holds.

1. `K` contains three disjoint connected pairwise adjacent sets
   `W_i`, with `A_i subseteq W_i`.
2. There is an index `m` and three disjoint connected sets `W_i`, with
   `A_i subseteq W_i`, whose literal adjacency graph is the path with
   middle vertex `W_m`.

Moreover, if a minimal connector of the three contracted sets has a
degree-three Steiner vertex, outcome 2 can be realized with *any*
prescribed value of `m`.

#### Proof

Contract each `A_i` to a named vertex `a_i`; loops may be discarded.
If the contracted graph contains an `\{a_1,a_2,a_3\}`-rooted `K_3`
model, lift its three bags and uncontract the `A_i`.  This is outcome 1.

Otherwise take an inclusion-minimal connected subgraph containing the
three named vertices and then an edge-minimal one.  It is a tree.  Its
minimal subtree joining `a_1,a_2,a_3` has one of two forms.

* One named vertex, say `a_m`, lies on the path between the other two.
  Cut the two path edges incident with the `a_m`-piece and assign every
  unused hanging subtree arbitrarily to the piece at which it attaches.
  The three resulting connected bags have adjacency path centred at
  `a_m`.
* There is one degree-three Steiner vertex `z`, with three internally
  disjoint arms to the named vertices.  For any prescribed `m`, assign
  `z` and its `a_m` arm to the `m`-bag, and assign the other two arms to
  their terminal bags.  The `m`-bag is adjacent to both other bags and
  those other bags are not required to be adjacent.

Lifting contractions gives the asserted sets in `K`.  Extra vertices
of `K` are irrelevant; the branch bags need not span the lobe. `square`

The first outcome is retained separately because it already gives all
three carrier adjacencies and uses no gate edge.

## 3. The median repair

### Theorem 3.1 (literal sparse-gate median exchange)

Let `K` be one of `C,D`, of order at least three, and let `J` be the
other lobe.  Choose the labelled linkage (2.1), and apply Lemma 2.1 to
its `K`-parts.

If either

1. outcome 1 of Lemma 2.1 occurs; or
2. outcome 2 occurs with median `m`, and either the two leaf gate
   vertices are joined by a literal edge of `G[T]` **or** their two
   chosen boundary representatives are joined by a literal edge of
   `G[S]`,

then `G` contains a literal `K_7` minor.

#### Proof

Let `W_i` be the three connector bags and put

\[
                         B_i=W_i\cup\{t_i\}.
                                                               \tag{3.1}
\]

Here the part of `Q_i` from `A_i` to `t_i` is included in `W_i` before
adjoining `t_i`; equivalently enlarge `W_i` by all unused vertices of
`Q_i-t_i`.  The three `B_i` are disjoint and connected.  Each contains
the literal portal `x_i`, so `s_i` is a representative for `B_i`.

In outcome 1 the `B_i` are pairwise adjacent already inside `K`.  In
outcome 2, the connector gives the two median--leaf adjacencies.  If the
leaf gate vertices are adjacent, their literal edge gives the third
adjacency before anchoring.  Otherwise the hypothesis gives the literal
edge between the two leaf representatives in `S`; after adjoining those
representatives to their carrier bags, that edge gives the third
adjacency.

The other lobe `J` is connected and is adjacent to every `B_i`, because
it has a neighbour at every literal gate vertex `t_i`.  Also
`|N_S(J)|>=4`.  Choose

\[
                    s_0\in N_S(J)-\{s_1,s_2,s_3\}.       \tag{3.2}
\]

Thus, after enlarging each of `J,B_1,B_2,B_3` by its representative, the
four resulting bags are pairwise adjacent and connected.  Anchor the
three disjoint full packets in `R`
at the other three vertices of `S`.  Packet fullness supplies every
remaining adjacency, giving seven literal clique branch sets. `square`

No virtual edge of the web triangle is used in this construction.

## 4. Consequences for the sparse literal gate

Since `|L|>=8`, one of the two lobes has order at least three, so the
theorem always has a candidate lobe.

### Corollary 4.1 (one-edge gate)

Suppose `G[T]` has the unique literal edge `t_1t_2`.  The configuration
closes whenever, for some labelled three-arm linkage in either lobe,

* the contracted lobe contains a rooted `K_3` model on the three arm
  roots; or
* it has a degree-three Steiner connector; or
* it has path form with median `t_3`.

Consequently a survivor has the following uniform orientation property:
for every such choice for which the contracted lobe has no rooted
`K_3` model,
every minimal connector is a path whose median is one of `t_1,t_2`, and
the representatives on its two leaf arms are nonadjacent in `G[S]`.

### Corollary 4.2 (two-edge path with unlabelled middle)

Suppose `G[T]` is the path `t_1t_2t_3`.  The earlier middle-portal
theorem closes the case `N_S(t_2) ne emptyset`.  If the middle is
unlabelled, Theorem 3.1 still closes whenever the contracted lobe has a
rooted `K_3` model on the three arm roots, a minimal connector has a
degree-three Steiner vertex, or a path connector has median `t_1` or
`t_3`.

Thus the exact residual is not an arbitrary path-gate lobe.  For every
labelled three-arm linkage in every order-at-least-three lobe, every
minimal connector is a path with the same literal middle `t_2`, and the
two leaf representatives are nonadjacent in `G[S]`.

### Corollary 4.3 (edgeless gate)

If `G[T]` is edgeless, a rooted-`K_3` model in the lobe after contracting
the three arm sets closes the cell.  A Steiner-`Y` also closes whenever
the three chosen labels
contain an edge: choose as median the arm opposite that edge.  For a path
connector, its two leaf representatives must be nonadjacent.  Hence every
labelled three-arm system in a surviving lobe is rooted-triangle-free
after its three arm sets are contracted and obeys this exact label-order
restriction.

The last alternatives in Corollaries 4.1--4.3 are genuine
width-two/Watkins--Mesner inputs.  In the one-edge and two-edge gate
cases, every `Y` connector and every incompatible path median has been
eliminated by an explicit literal model.  In the edgeless-gate case a
`Y` connector may remain when its three chosen labels are independent;
the proved restriction there is instead the rooted-triangle exclusion
and the leaf-label nonadjacency condition.  What remains to close is to
show that the common median orientation in the nonempty-gate cases
either breaks under a portal exchange or yields a faithful proper-minor
state, and to exploit the weaker label-order certificate in the
edgeless case.  This note does not infer a common equality state merely
from the median orientation.
