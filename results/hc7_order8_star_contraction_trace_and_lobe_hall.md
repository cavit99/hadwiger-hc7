# Star-contraction traces and the three-support Hall obstruction

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_star_contraction_trace_and_lobe_hall_audit.md`](hc7_order8_star_contraction_trace_and_lobe_hall_audit.md).
This is a conditional
theorem inside the ordered positive-boundary-excess interface.  It does not
prove `HC_7`.

## 1. Setting

Retain the setting and notation of the audited
[contact-concentration theorem](../results/hc7_order8_rooted_partition_contact_concentration.md).
Thus

\[
 B=(S-\{e\})\mathbin{\dot\cup}W=N_G(E),\qquad |W|\ge2,
\]

`G-B` has exactly the two components `E,C`, and `C` contains adjacent
connected subgraphs `P_0,P_1` which are each adjacent to every vertex of
`S`.  Every proper minor of `G` is six-colourable, while `G` itself is not.

For a boundary colouring `Sigma`, choose a maximum clique `U` among its
singleton blocks.  If `C_1,...,C_t` are the remaining blocks, write

\[
 D_U(C_i)=C_i\cup\{u\in U:E_G(u,C_i)=\varnothing\}
\tag{1.1}
\]

for their required boundary sets.

## 2. Every independent set is an exact star-contraction trace

### Lemma 2.0 (the contraction colour is absent from the boundary)

If `|E|\ge2`, there is a response partition on `B` with at most five
blocks.  If additionally `|W|=2`, one may choose such a partition with
demand at most four.

#### Proof

Contract a spanning tree of `E` to one vertex `a`.  The hypothesis
`|E|\ge2` makes this a proper minor, which therefore has a six-colouring.
The vertex `a` is adjacent to every literal vertex of `B=N_G(E)`,
so its colour is absent from `B`.  Restricting to `G[C\cup B]` gives a
boundary partition with at most five blocks.  As in Theorem 2.1 below, that
partition is rejected by the intact `E`-side, or else the two colourings
glue.

When `|W|=2`, the boundary has order nine.  A partition of nine vertices
into five nonempty blocks has a singleton block; partitions with fewer
blocks already have demand at most four.  Thus a maximum clique among the
singleton blocks has order at least one in the only remaining case, and
the demand is at most `5-1=4`. \(\square\)

### Theorem 2.1

For every nonempty independent set `I` of `G[B]`, there is a proper
six-colouring of `G[C\cup B]` in which `I` is one exact equality block:
all vertices of `I` have one colour and no vertex of `B-I` has that colour.
Its equality partition on `B` is rejected by the intact graph
`G[E\cup B]`.

In particular, every `v\in B` can be made an exact singleton block.  Also,
because `d` is anticomplete to `W`, every set

\[
                         \{d\}\cup J                 \tag{2.1}
\]

with `J` independent in `G[W]` is an exact block of such a response.

#### Proof

The graph induced by `E\cup I` is connected: `E` is connected and every
literal vertex of `B=N_G(E)` has a neighbour in `E`.  Contract a spanning
tree of `G[E\cup I]` to one vertex `a`.  This is a proper minor, so it has a
proper six-colouring.

Discard the interior of `E`, retain the colouring on `C\cup(B-I)`, and give
each literal member of `I` the colour of `a`.  This expansion is proper.
There is no edge inside `I`; and every edge from `I` to a retained vertex
became incident with `a` in the minor.  Moreover, `a` is adjacent to every
vertex of `B-I`, through an edge from that vertex to `E`.  Hence the colour
of `I` occurs nowhere else on `B`.

If the resulting equality partition extended through the intact graph
`G[E\cup B]`, align the two boundary colourings by a permutation of the six
colour names and glue across `B`.  The components `E,C` of `G-B` are
anticomplete, so this would six-colour `G`, a contradiction.  Thus the
partition is rejected by the intact `E`-side.

Finally `W\subseteq D`, while `D` has no neighbour at `d`; hence `d` is
anticomplete to `W`, proving the last assertion. \(\square\)

Theorem 2.1 and the contact-concentration theorem imply that every one of
these responses has demand at least two.  At demand two, both required
boundary sets meet `W`.

### Proposition 2.2 (block-count descent or colour-indexed paths)

Assume, as in the live forest normal form, that

\[
 N_G(d)\cap B=\{x_d,y_d\},
 \qquad de\notin E(G).                                \tag{2.2}
\]

Take the exact-singleton response from Theorem 2.1 with `I=\{d\}`, and let
`k` be the number of its boundary blocks.  Then at least one of the
following holds.

1. A Kempe exchange gives another partition which extends through the
   `C`-side, is rejected by the intact `E`-side, and has `k-1` blocks.
2. For every boundary block other than `\{d\}` and the at most two blocks
   containing `x_d,y_d`, there is a bichromatic path from `d` to that block
   whose internal vertices lie outside `B` and whose first internal vertex
   lies in `R`.

Consequently, in outcome 2 there are at least `k-3` paths indexed by
distinct alternate colours.  Two paths with different alternate colours
can intersect only at vertices having the colour of `d`.

#### Proof

Let `alpha` be the colour of `d`, and let `C_i` be a boundary block which
contains neither `x_d` nor `y_d`.  Equation (2.2) says that `d` has no
boundary edge to `C_i`.  Apply the two-block Kempe exchange to the singleton
block `\{d\}` and `C_i`.  Either the exchange merges exactly these two
blocks, leaving every other boundary block fixed, or a shortest
`alpha`--`c(C_i)` path joins `d` to `C_i` and has all internal vertices
outside `B`.

The merged colouring remains a proper colouring of `G[C\cup B]`.  If its
new boundary partition extended through `G[E\cup B]`, boundary alignment
would six-colour `G`; hence it is another rejected response, now with one
fewer block.  This is outcome 1.

If no selected block gives outcome 1, take all the resulting paths.  Their
internal vertices lie in `C`.  The vertex `d` has no neighbour in `D-W`
because `D` misses `d`, and it has no edge to `e` in the live ordered
interface.  Since `C=(D-W)\dot\cup\{e\}\dot\cup R`, the first internal
vertex of every path lies in `R`.  The path may later pass through `e` into
`D-W`; no stronger localization is asserted.

The blocks containing `x_d,y_d` are distinct because `x_dy_d` is an edge.
There are therefore at least `k-3` selected blocks.  Paths belonging to
distinct alternate colours have colour sets `\{alpha,beta\}` and
`\{alpha,gamma\}`; every common vertex consequently has colour `alpha`.
\(\square\)

## 3. A sharper three-support criterion when `D-W` is nonempty

Assume now that the sole surviving nonempty-lobe outcome of the
contact-concentration theorem holds:

\[
                         Z=D-W\ne\varnothing,
 \qquad N_G(Z)=(S-\{d\})\mathbin{\dot\cup}W.          \tag{3.1}
\]

Also assume explicitly that

\[
                              de\notin E(G).           \tag{3.2}
\]

This is an additional hypothesis from the live ordered interface; it is
not part of the self-contained statement of the contact-concentration
theorem.

Put

\[
                            H=Z\cup\{e\}.             \tag{3.3}
\]

### Theorem 3.1

The three subgraphs `P_0,P_1,H` are pairwise vertex-disjoint, connected and
pairwise adjacent.  Their exact contacts with `B` are

\[
 N_G(P_i)\cap B=B-W\quad(i=0,1),
 \qquad N_G(H)\cap B=B-\{d\}.                        \tag{3.4}
\]

Let `Sigma` be any boundary partition on `B` which extends through the
`C`-side and is rejected by the intact `E`-side.  If its demand `t` is at
most three, then at least one of the following holds:

1. some required set `D_U(C_i)` contains both `d` and a member of `W`;
2. at least two required sets meet `W`; or
3. `t=3` and all three required sets contain `d`.

Equivalently, if none of 1--3 holds, the three displayed connected
subgraphs reproduce `Sigma` through the opposite shore, and the resulting
colourings glue to a six-colouring of `G`.

#### Proof

The set `H` is connected because `Z` is connected and is full to `e` by
(3.1).  The subgraphs `P_0,P_1` are adjacent by hypothesis, and each is
adjacent to `H` through an edge to the literal vertex `e` in `H`.  They are
pairwise disjoint because `Z\subseteq L`, `e\in S`, and `P_0,P_1\subseteq
R`.

There are no `L`--`R` edges.  Thus each `P_i` misses every member of `W`
and, by boundary fullness to `S`, has exactly the first contact set in
(3.4).  The set `Z` is full to `(S-\{d\})\cup W`.  Neither `Z` nor `e` is
adjacent to `d`, so `H` has exactly the second contact set in (3.4).

Apply the transported-partition Hall reflection theorem with the three
pairwise adjacent connected supports `P_0,P_1,H`.  A required set which
avoids `W` is eligible at each `P_i`; a required set which avoids `d` is
eligible at `H`.  Therefore:

* a required set meeting both `W` and `d` has no eligible support;
* two required sets meeting `W` compete for the sole support `H`; and
* three required sets containing `d` compete for the two supports
  `P_0,P_1`.

These give alternatives 1--3.  Conversely, assume none occurs.  At most
one required set meets `W`; assign it to `H` (it avoids `d` by failure of
1).  Every remaining required set avoids `W`, and there are at most two of
them unless all three required sets contain `d`, which is excluded by 3.
Assign those sets injectively to `P_0,P_1`; if one of them avoids `d`, it
could instead be assigned to the unused `H`, so the same conclusion also
covers the case of three required sets and no `W`-meeting set.  This is a
saturating matching.  Hall reflection reproduces `Sigma` on the intact
opposite shore, and boundary alignment then six-colours `G`, contrary to
the standing hypothesis. \(\square\)

## 4. Sharp static obstruction to star traces alone

Theorem 3.1 does not close the response.  The following nine-vertex
boundary tableau satisfies the exact star trace and the unresolved first
alternative.

Let

\[
 B=\{d,a,b,c,f,p,q,w_0,w_1\}
\]

and give `G[B]` exactly the edges

\[
                         da,\ db,\ ab,\ cf.           \tag{4.1}
\]

Thus `dabd` is one rooted triangle and the six vertices
`a,b,c,f,p,q` induce the forest `ab\mathbin{\dot\cup}cf` plus two isolated
vertices.  Put `W=\{w_0,w_1\}`.  The partition

\[
 \{d,w_0\}\ \bigm|\ \{a,c,p,w_1\}\ \bigm|\ \{b,f,q\}               \tag{4.2}
\]

has three independent nonsingleton blocks.  Its singleton clique is empty,
so its demand is three and its required sets are exactly the three blocks.
The first required set contains both `d` and `W`; the second also meets
`W`.  Hence neither the two rooted connected parts of the
contact-concentration theorem nor the three primitive supports of Theorem
3.1 have a saturating matching.  The first block is an admissible exact
trace block of the kind forced by Theorem 2.1 for `I=\{d,w_0\}`; the
theorem does not assert that the other two blocks of (4.2) occur in a
particular host colouring.

This tableau is not asserted to be the boundary language of a
seven-connected contraction-critical host.  It proves the narrower and
necessary point: exact independent-set star traces, forest structure on
`S-\{d,e\}`, and the available support-contact sets do not by themselves
force reflection.  A closure theorem must use transitions between
operation-specific colourings or additional labelled branch-set geometry.

## 5. What the minimal-contraction forest gives in this normal form

Let

\[
 A_1=R_0,\quad A_2=R_1,\quad
 A_3=E\cup\{d\},\quad A_4=D\cup\{e\}                 \tag{5.1}
\]

be the four spanning branch sets supplied by the contact-concentration
theorem and its forest corollary.  Contract a spanning tree of each `A_i`.
The resulting minor is exactly

\[
                              K_4\vee G[F],            \tag{5.2}
\]

where `F=S-\{d,e\}` and `G[F]` is a forest.  If `c` is the number of
components of `G[F]`, contracting all forest edges gives

\[
                              K_4\vee I_c,             \tag{5.3}
\]

which is five-colourable.

### Proposition 5.1

Inside the already contracted graph (5.2), `E(G[F])` is inclusion-minimal
among edge subsets whose contraction gives a five-colourable graph.  For
every forest edge `xy`, contracting all other forest edges leaves exactly

\[
                         K_4\vee(K_2\mathbin{\dot\cup}I_{c-1}).       \tag{5.4}
\]

The quotient (5.4) visibly contains an explicit rooted `K_6`: its four
`K_4` vertices and the two ends of its `K_2`.  On lifting, these are the
four branch sets (5.1) and the two connected sides of the component of
`G[F]-xy`.  Independently, the minimal-contraction cut-saturation theorem
says that both ends of that `K_2` see every one of the four other colours.
Its stronger critical-image corollary is not being invoked.

#### Proof

For `J\subseteq E(G[F])`, the quotient of (5.2) by `J` is

\[
                         K_4\vee(G[F]/J).
\]

If `J=E(G[F])`, the second factor is the independent set `I_c`, so the
chromatic number is five.  If `J` is proper, a forest edge remains between
two distinct contraction classes.  The second factor is then bipartite but
not independent, so the join has chromatic number six.  This proves
minimality.  Leaving the one edge `xy` uncontracted turns its tree component
into `K_2` and every other tree component into one isolated vertex, proving
(5.4).  Lifting its evident `K_6` gives the stated branch sets. \(\square\)

This observation does not apply the saturation theorem to internal edges
of the original four branch sets.  If one chooses an inclusion-minimal
subset of the **combined** bag trees and boundary forest which makes a
quotient five-colourable, the terminal quotient need not remain the exact
graph (5.3); omitted bag-tree edges leave additional vertices and destroy
the four named quotient colours.  Exact quotient structure and chromatic
minimality cannot be assumed simultaneously without another argument.

Nor does the evident star split of `A_3` provide the seventh branch set.
The two connected sides `E` and `\{d\}` have complementary losses:

\[
 E\not\sim R_0,R_1,
 \qquad
 \{d\}\not\sim D\cup\{e\}.                           \tag{5.5}
\]

Consequently the boundary-edge `K_6` in Proposition 5.1 still requires a
label-preserving split of one of the four spanning branch sets.  The
one-sided ownership of `W` does not supply that split by itself.

## 6. Trust boundary

Theorem 2.1 gives the complete exact-block family supplied by contracting
`E` together with chosen boundary vertices.  Theorem 3.1 is a genuine
strengthening in the nonempty `T`-full-lobe case: every rejected response
of demand at most three has one of three explicit literal concentration
patterns.

The result does not show that a star-contraction response has demand at most
three, does not eliminate the displayed concentration patterns, and says
nothing stronger when `D-W` is empty.  In particular it does not produce a
common boundary partition, an explicit `K_7`-minor model, or a strict
response-preserving descent.

## 7. Dependencies

- [rooted-partition contact concentration](../results/hc7_order8_rooted_partition_contact_concentration.md)
- [transported-partition Hall reflection](../results/hc7_transported_partition_hall_reflection.md)
- [minimal contraction-forest saturation](../results/hc7_minimal_contraction_forest_saturation.md)
