# Reserve zero rows: released-owner capacity and the exact dynamic residue

## 1. Status

This note treats **reserve consumption**, not the distinct problem in
which two rooted-extension roles use the same dark lobe.  Four protected
rooted bags and two pool bags have already been selected.  If every
reserve consumes one protected bag, release that bag.  The other three
protected bags and the two pools form a fixed `K_5` frame, while the
released material has to supply two new bags: the replacement protected
bag and the reserve.

The main theorem below shows that this is exactly a two-copy rainbow
carrier problem.  It has a uniform answer:

```text
two disjoint full carriers, hence K7,
    or one gate/cycle/3-connected torso meeting every full carrier.
```

At the torso obstruction, every off-torso lobe has a named missing frame
row and a strict portal surplus.  Proper-minor minimality supplies a
novel labelled boundary state for every operation in such a lobe.  Thus
the zero-row problem is not another unbounded collection of reserve
components.  Its exact residue is one operation-sensitive torso together
with distributed contacts in the fixed frame.

This does **not** prove `HC_7`.  In particular, it does not prove that a
novel palette state labels the five fixed model bags.  Section 5 proves
that incidence data alone cannot do so, even if the missing columns vary.

## 2. Releasing a consumed protected bag

Let

\[
                         U_1,U_2,U_3,U_4,U_5              \tag{2.1}
\]

be pairwise disjoint nonempty connected sets which are pairwise adjacent.
They are the three protected bags not being replaced and the two pool
bags.  Let `D` be a connected set disjoint from their union.  Put

\[
                         P_i=N_D(U_i)\qquad(1\le i\le5). \tag{2.2}
\]

Assume every `P_i` is nonempty.  A connected subgraph of `D` is **full**
if it meets every `P_i`.

### Theorem 2.1 (released-owner reserve theorem)

At least one of the following holds.

1. `G` contains a `K_7` minor whose first five bags are the sets in
   (2.1) and whose last two bags partition `D`.
2. In every chosen tree decomposition of `D`, some bag meets every full
   connected subgraph of `D`.  If the decomposition has adhesion at most
   `k`, every component off that bag misses one named row `P_i` and has
   at most `k` neighbours in the bag.

In a Tutte decomposition, the obstruction bag in outcome 2 is a gate of
order at most two, a cycle torso, or a 3-connected torso.

#### Proof

If there are two vertex-disjoint full connected subgraphs `A,B`, join
them by a shortest path if necessary.  Contract `A,B`, take a spanning
tree of the resulting connected graph `D`, and delete one tree edge on
the path between their images.  Lifting the two tree components gives an
adjacent connected bipartition

\[
                             D=X\mathbin{\dot\cup}Y        \tag{2.3}
\]

with `A subseteq X` and `B subseteq Y`.  Both shores remain full.  Hence

\[
                         U_1,\ldots,U_5,X,Y               \tag{2.4}
\]

are seven disjoint connected pairwise adjacent bags, a `K_7` model.

Suppose there are no two disjoint full connected subgraphs.  The
inclusion-minimal full connected subgraphs are then pairwise intersecting.
Project them to the decomposition tree.  Their traces are pairwise
intersecting subtrees, so tree Helly gives one node whose bag meets every
minimal full subgraph, and hence every full subgraph.  A component off
that bag cannot meet all five rows.  The running-intersection axiom puts
all its neighbours in the common bag inside one adhesion, proving the
last assertion.  The Tutte torso list is standard.  QED.

### Corollary 2.2 (reserve consumption is one torso)

Suppose four protected bags and two pools satisfy the hypotheses of the
biportal completion except that no disjoint reserve exists.  Suppose a
connected warehouse `D` contains one protected bag `F` and all material
which may replace `F` or form the reserve, while the other three protected
bags and two pools are disjoint from `D`.  If `D` is adjacent to each of
those five fixed bags, then either the reserve and `F` can be chosen
disjointly and give `K_7`, or all replacement/reserve capacity is
concentrated in the one torso of Theorem 2.1.

#### Proof

The five fixed bags are the frame (2.1).  A full connected subgraph of
`D` can play either of the two roles: adjacency between two selected
roles is supplied by the adjacent bipartition in (2.3).  Therefore two
disjoint full carriers are exactly a replacement and a reserve, and
(2.4) is the required completion.  If they do not exist, outcome 2 of
Theorem 2.1 applies.  QED.

The application assumes that after the fixed `K_5` frame is removed,
`D` contains **all** remaining replacement/reserve material.  If further
components remain, they must first be absorbed into `D` without touching
the fixed bags, or treated as separate warehouses.  Silently deleting
them could change which connected reserves exist.

The corollary is deliberately about the **released** protected bag.  If
one freezes all four original extensions and asks a reserve to avoid
them, one sees only the zero rows of the remaining components.  Releasing
the bag which every reserve consumes is what converts the problem into
two symmetric carrier copies.

## 3. Seven-connectivity forces a distributed owner

The torso outcome is already quantitative at vertex level.  Assume now
that `G` is seven-connected and that

\[
                  V(G)=D\mathbin{\dot\cup}U_1\mathbin{\dot\cup}
                  \cdots\mathbin{\dot\cup}U_5.              \tag{3.1}
\]

No assertion that a whole branch bag is one separator vertex is made.

### Theorem 3.1 (dark-lobe portal surplus)

Let `W` be the torso bag from Theorem 2.1 in an adhesion-at-most-two
decomposition, and let `C` be a component of `D-W`.  If `C` misses the
frame row `P_i`, then

\[
  7\le |N_G(C)|
     \le |N_D(C)\cap W|+
         \sum_{j\ne i}|N_{U_j}(C)|,                         \tag{3.2}
\]

and therefore

\[
                       \sum_{j\ne i}|N_{U_j}(C)|\ge5.       \tag{3.3}
\]

In particular some one of the four available frame bags contains at
least two distinct neighbours of `C`.

#### Proof

The missed bag `U_i` lies outside `C union N(C)`, so `N(C)` is a genuine
separator.  Seven-connectivity gives the left inequality in (3.2).
There are no vertices outside the five frame bags and `D`.  The
decomposition gives at most two neighbours in `W`, and the missed-row
condition gives no neighbour in `U_i`.  This proves the right inequality
and (3.3).  Four sets containing at least five vertices have a repeated
owner.  QED.

This is the first fact destroyed by contracting every protected bag to
one quotient vertex.  A seven-connected realization of a zero row must
have genuine portal multiplicity inside at least one owner; extra edges
between contracted reserve components cannot substitute for it.

### Corollary 3.2 (literal one-complex exactness)

Suppose instead that

\[
                         V(G)=L\mathbin{\dot\cup}D,
                         \qquad |L|=6,                       \tag{3.4}
\]

where the members of `L` are literal singleton shell labels, and the five
portal rows in Theorem 2.1 are five distinct labels in `L`.  Every
off-torso component which misses one of those five rows has

\[
                            |N_G(C)|=7.                       \tag{3.5}
\]

It sees the other five shell labels (including the sixth label), has two
actual torso attachments, and lies behind an exact seven-cut.

#### Proof

The component has at most two torso neighbours and misses at least one of
the six literal labels, so `|N(C)|<=2+5=7`.  Seven-connectivity forces
equality.  Every displayed possible neighbour is therefore present.
QED.

The repeated owner in Theorem 3.1 can itself be treated without any
case analysis of its block tree in the defect-one cell.  Assume that
`C` misses **exactly** `U_0`, and relabel a repeated owner as `U_1`.
Inside `U_1` put

\[
 A=N_{U_1}(C),\qquad R_j=N_{U_1}(U_j)
       \quad(j\in\{0,2,3,4,5\}).                       \tag{3.6}
\]

A **repair carrier** is a connected subgraph of `U_1` meeting `A` and
`R_0`.  A **retained carrier** is a connected subgraph meeting every one
of `R_0,R_2,R_3,R_4,R_5`.

### Theorem 3.3 (repeated-owner peel or one owner torso)

At least one of the following holds.

1. `G` has a `K_7` model obtained by splitting `U_1`, absorbing `C` into
   one side, and retaining the other five frame bags.
2. In every chosen tree decomposition of `G[U_1]`, one bag meets every
   repair carrier or one bag meets every retained carrier.  At adhesion
   at most `k`, each off-bag component relevant to the obstructed family
   misses a named row from (3.6) and has at most `k` neighbours in the
   bag.

In a Tutte decomposition, outcome 2 is again one gate of order at most
two, one cycle torso, or one 3-connected torso.

#### Proof

If a repair carrier `L` and retained carrier `R` are vertex-disjoint,
extend them, exactly as in the proof of Theorem 2.1, to an adjacent
connected bipartition

\[
                         U_1=X\mathbin{\dot\cup}Y,
                         \qquad L\subseteq X, R\subseteq Y. \tag{3.7}
\]

Use the seven bags

\[
                 C\cup X,quad Y,quad
                 U_0,U_2,U_3,U_4,U_5.                 \tag{3.8}
\]

The first bag is connected because `X` meets `A`.  It sees `U_0`
through the `R_0`-contact of `X`, and it sees `U_2,...,U_5` through the
old contacts of `C`; recall that `C` misses only `U_0`.  The second bag
sees all five retained frame bags by definition.  The first two bags are
adjacent by (3.7), and the retained five form a clique model.  Hence
(3.8) is a `K_7` model.

Suppose no disjoint pair exists.  Project the inclusion-minimal repair
and retained carriers to an arbitrary decomposition tree.  Every trace
from one family meets every trace from the other.  If the repair traces
are pairwise intersecting, tree Helly gives one bag meeting all of them.
Otherwise two disjoint repair traces have a joining path which every
retained trace must contain, and any node on that path meets all retained
carriers.  The standard running-intersection argument gives the adhesion
bound and the missed-row assertion.  The Tutte list follows.  QED.

The theorem makes the remaining geometry two-level but still bounded:
reserve consumption first localizes in one warehouse torso; a forced
repeated owner then either repairs the missing row or localizes in one
torso of that owner.  Arbitrary block trees on either side have
disappeared.

## 4. The operation-state carried by every real lobe

The preceding statements are geometric.  Proper-minor minimality adds an
exact dynamic relation at every actual frontier, of arbitrary order.

Let `C` be one of the components in Theorem 3.1, put `X=N_G(C)`, and let
`A=G[C union X]`, `B=G-C`.  For a boundaried graph `J` containing `X`,
write `E(J,X)` for the equality partitions of `X` induced by proper
six-colourings of `J`.

### Theorem 4.1 (zero-row operation novelty)

Assume `G` is proper-minor-minimal non-six-colourable.  For every
nonidentity deletion or contraction `mu` whose operated vertex or edge
lies wholly in `C` (so all vertices of `X` remain distinct labels), there
is a partition `Pi_mu` of `X` into at most six independent blocks such
that

\[
 \Pi_\mu\in E(A^\mu,X)\cap E(B,X),
 \qquad
 \Pi_\mu\notin E(A,X).                                \tag{4.1}
\]

Thus every internal operation moves the lobe into a state already
accepted by the unoperated opposite side.  If an unoperated lobe ever
accepts the same state, the two six-colourings glue and contradict the
choice of `G`.

#### Proof

Apply `mu` to the whole graph.  The result is a proper minor, so it has a
six-colouring.  Its equality classes on `X` give `Pi_mu`; restriction
proves the two memberships in (4.1).  If the original `A` also accepted
that partition, permute its palette so corresponding boundary blocks have
the same colours and splice it to the colouring of `B`.  The open shores
are anticomplete, so this would six-colour `G`.  QED.

For the literal case of Corollary 3.2 this is a finite exact-seven state.
For the general frame case the boundary may be larger: (3.3) explicitly
forbids pretending that four connected owner bags are four boundary
vertices.

Theorems 2.1--4.1 give the rigorous reserve-zero reduction:

```text
release one consumed protected bag
    -> K7, or one rainbow torso;
off-torso failure
    -> a repeated actual owner portal;
every faithful internal operation
    -> a novel state accepted on the opposite side.
```

The missing implication is a **model-labelled** exchange from the
repeated owner portal and (4.1) to two full carriers.  Palette blocks in
`Pi_mu` are not the five frame labels.

## 5. Why incidence enumeration cannot finish the argument

Contract the six selected bags (four protected bags and two pools) to a
clique `Q=K_6`.  Represent every free reserve component by one vertex,
and suppose that vertex has exactly one zero column, hence is adjacent to
the other five members of `Q`.  Distinct free components are pairwise
anticomplete.

### Proposition 5.1 (the zero-row book)

For an arbitrary number of free components and arbitrary choices of
their zero columns, the resulting quotient is chordal with clique number
six.  In particular it has treewidth five and no `K_7` minor.

#### Proof

Every free vertex is simplicial: its neighbourhood is one of the `K_5`
subcliques of `Q`.  Eliminate all free vertices in any order and then the
six vertices of `Q`.  This is a perfect elimination ordering and no bag
has order more than six.  Since `Q` itself is a six-clique, the clique
number is exactly six and the treewidth is five.  Treewidth is
minor-monotone, whereas `K_7` has treewidth six.  QED.

Thus neither adding more zero-row components nor making their missing
columns different changes the quotient obstruction.  The graph is a
book of `K_6` pages pasted along `K_5` subcliques.  The only information
capable of closing it is the information the quotient erased:

* multiple actual portals in one owner, forced by Theorem 3.1;
* their order/separation inside that owner; and
* the operation-state relation (4.1).

`near_k7_zero_row_incidence_probe.py` checks all 3,002 zero multisets of
orders one through eight and verifies chordality and clique number six.
The proof above is uniform and does not depend on that check.

## 6. Exact remaining theorem

The reserve branch now needs no further enumeration of free-component
incidence rows.  Its exact target is:

> **Repeated-owner operation exchange.**  In a seven-contraction-critical
> target-free graph, let `U_1,...,U_5` and `D` satisfy Theorem 2.1, and let
> `C` be an off-torso lobe with a repeated owner guaranteed by Theorem
> 3.1.  Then either the repeated portals split that owner so that `D`
> contains two disjoint full carriers, an operation state from (4.1) is
> faithful to the five model labels on the opposite side, or all portal
> occurrences of the torso and the owner admit one compatible rural disk
> expansion.

The three conclusions are respectively `K_7`, six-colour gluing, and the
coherent two-apex branch.  The first is Theorem 2.1, and the state which
the second must transport is already forced by Theorem 4.1.  What is not
proved is the alignment of that palette state with the repeated **model
owner**.  This is the same sharply identified palette-to-model gap as in
the joint-edge warehouse, now reached directly from reserve consumption.
