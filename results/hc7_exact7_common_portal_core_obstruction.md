# Common-portal cores in the exact-seven two-packet cell

**Status:** proved and independently audited.

This note records a label-free obstruction forced by the two adjacent full
packets in the connected-rich width-two frontier.  It does not close the
common-gate residue, but it rules out an entire uniform mechanism for
maintaining that residue: no three literal portal classes can support a
`K_4` model, and every `K_4` model supported by two literal classes has a
rigid one-bag trace for every other literal.

## 1. Setup

Let

\[
             V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
             \qquad |S|=7,
\]

be a literal separation.  Let `P,Q subseteq R` be disjoint connected
`S`-full packets with a `P-Q` edge.

For `T subseteq S`, define the common-portal core

\[
             L_T=G[\{v\in L:T\subseteq N_S(v)\}].       \tag{1.1}
\]

Thus every vertex of `L_T` is literally adjacent to every member of `T`.

## 2. Three common portals give a literal `K_7`

### Theorem 2.1 (triple-core obstruction)

Let `T={a,b,c}` consist of three distinct boundary literals.  If `L_T`
contains a `K_4` model, then `G` contains a literal `K_7` minor.

#### Proof

Let `B_1,B_2,B_3,B_4` be the four disjoint connected pairwise adjacent
branch bags in `L_T`.  Use the seven bags

\[
 B_1,B_2,B_3,B_4,qquad P\cup\{a\},\qquad
 Q\cup\{b\},\qquad\{c\}.                              \tag{2.1}
\]

They are disjoint because the `B_i` lie in `L`, the packets lie in `R`,
and the three anchors `a,b,c` are distinct literals of `S`; they are
connected because `P,Q` contact their respective anchors.  The first four
form a clique.  Each
`B_i` is adjacent to the fifth, sixth and seventh bags through its literal
edges to `a,b,c`, respectively.  The fifth and sixth bags are adjacent
through the assumed `P-Q` edge.  Fullness of `P,Q` at `c` joins each of
them to the last singleton bag.  Hence all seven bags are pairwise
adjacent.  \(\square\)

### Corollary 2.2 (uniform degeneracy)

If `G` has no `K_7` minor, then `L_T` is `K_4`-minor-free, and hence
two-degenerate, for every three-set `T subseteq S`.

#### Proof

Theorem 2.1 excludes a `K_4` model in `L_T`.  Every nonempty subgraph of a
`K_4`-minor-free graph has a vertex of degree at most two: otherwise its
minimum degree is at least three and the elementary `K_4`-minor theorem
applies.  This is exactly two-degeneracy. \(\square\)

## 3. Two common portals force one-bag traces

### Theorem 3.1 (pair-core trace obstruction)

Let `a,b` be distinct boundary literals, and let
`B_1,B_2,B_3,B_4` be a `K_4` model in `L_{\{a,b\}}`.  If some third
literal `c in S-{a,b}` has a neighbour in at least two distinct bags
`B_i`, then `G` contains a labelled `K_7^vee` minor.

#### Proof

Use the same seven bags as in (2.1).  The four `B_i` together with
`P union {a}` and `Q union {b}` form a `K_6`: common `a,b` contacts join
each rooted bag to the two packet bags, and `P-Q` supplies the remaining
packet adjacency.  The singleton `{c}` is adjacent to both packet bags by
fullness and to at least two of the four `B_i` by hypothesis.  It therefore
has at least four neighbours in the displayed `K_6`.  At most two missing
bag pairs remain: they can only be pairs `{c}B_i` among the four rooted
bags not met by `c`.  Both permitted missing pairs are therefore incident
with the single deficient bag `{c}`.  This is exactly a labelled
`K_7^vee` model. \(\square\)

### Corollary 3.2 (rigidity in a near-model-free survivor)

If `G` has no `K_7^vee` minor, then for every boundary pair `{a,b}`, every
`K_4` model in `L_{\{a,b\}}`, and every third literal
`c in S-{a,b}`, the literal `c` has neighbours in at most one of the four
branch bags.

This conclusion concerns the actual branch bags, not merely four selected
vertices.  A later rerouting argument may therefore change which bag owns
the unique possible `c`-trace; the theorem does not assert a canonical
owner across different `K_4` models.

## 4. Scope

No boundary edge, colouring state, Dirac inequality, connectivity, or
planarity is used.  The only resources are the literal separation and the
two disjoint adjacent full packets.  Consequently these obstructions apply
uniformly to every width-two frontier boundary.

They do not prove the common-gate exchange.  Their exact output is the
following finite-rank restriction on any live residue:

1. every three-label common core is two-degenerate; and
2. every `K_4` model in a two-label common core assigns every remaining
   label to at most one model bag.

Thus any counterarchitecture with internal minimum degree at least four
must obtain that degree from vertices whose portal triples vary; it cannot
hide a four-branch clique model inside one fixed triple of literal portal
classes.
