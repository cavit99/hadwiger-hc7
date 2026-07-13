# Unit-bag linkage, weighted cuts, and the colouring-gluing obstruction

## Status

This note strengthens the target-slot/Rado formulation by allowing the
bags of a fixed clique model to act as unit-capacity objects.  The resulting
linkage theorem is exact and has a very short Menger proof.

It also gives two necessary audits.

* A cut in the unit-bag quotient is not automatically a vertex separator
  of the same order in the original graph, and contracting a nontrivial
  bag is not a colour-preserving operation.
* After rooting one portal set, a cut for the second portal set depends on
  the chosen absorption.  Bag rotations can destroy that cut.  A valid
  two-set theorem must optimize over all first-stage rootings.

Thus the unit-bag cut is the correct **minor/model** obstruction, but an
additional boundary-colouring signature is required before it becomes a
colour-gluable adhesion.

## 1. Contracted unit-bag network

Let `K` be a graph and let

\[
                        \mathcal B=(B_1,\ldots,B_m)
\]

be pairwise disjoint connected sets.  Contract every `B_i` to one vertex
`b_i`, and call the resulting graph `bar K`.  Put

\[
                         R=\{b_1,\ldots,b_m\}.
\]

For `X subseteq V(K)`, define its image

\[
 \bar X=(X-\bigcup_iB_i)\ \cup\
         \{b_i:X\cap B_i\ne\varnothing\}.              \tag{1.1}
\]

Paths of length zero are allowed.  Let `nu_X(mathcal B)` be the maximum
number of pairwise vertex-disjoint `bar X`--`R` paths in `bar K`.

### Theorem 1.1 (exact unit-bag rooting criterion)

The following are equivalent.

1. There are pairwise disjoint connected sets
   `B_i subseteq C_i` such that every `C_i` meets `X`.
2. `nu_X(mathcal B)=m`.

If the `B_i` are the bags of a clique model, the `C_i` in item 1 retain
every old interbag adjacency and hence form an `X`-rooted clique model.

#### Proof

Assume item 1.  Inside each connected `C_i`, choose a path from a vertex
of `X cap C_i` to `B_i`, and stop it at its first vertex in `B_i`.
The `m` paths are vertex-disjoint because the `C_i` are disjoint.  After
contracting each old bag they give `m` disjoint `bar X`--`R` paths.

Conversely, take `m` disjoint `bar X`--`R` paths in `bar K`.  There are
exactly `m` target vertices in `R`.  Every path contains at least its
target, so no path can contain two vertices of `R`: otherwise the `m`
disjoint paths would collectively contain at least `m+1` distinct target
vertices.  It follows also that a path starting at a source `b_i in R`
is the length-zero path at `b_i`.

Every nontrivial path therefore starts at a vertex of `X` outside all old
bags, avoids all contracted bag vertices until its final vertex `b_i`,
and ends at a different bag from every other path.  Lift its final edge
to an actual edge entering `B_i` and absorb the lifted path into `B_i`.
The lifted paths are mutually disjoint and avoid all nonterminal old
bags.  The resulting `C_i` have the required properties.  \(\square\)

### Corollary 1.2 (weighted model cut)

Exactly one of the following holds.

1. all bags can be made to meet `X`; or
2. there is an `bar X`--`R` vertex separator `S` in `bar K` with
   `|S|<m`.

The second alternative follows from the set version of vertex-Menger.
Writing

\[
 S=S_0\mathbin{\dot\cup}\{b_i:i\in I\},
                                                        \tag{1.2}
\]

the certificate consists in the original graph of the ordinary vertices
`S_0` together with the whole labelled bags `B_i` for `i in I`, each bag
having unit **model capacity**.

This formulation already permits every apparent traversal through another
model bag.  Such a traversal uses that bag's contracted vertex and hence
its unit capacity.  In a successful `m`-linkage no path actually traverses
a bag: the target-count argument in Theorem 1.1 forces every bag vertex
to occur exactly once, as an endpoint.

## 2. Two portal sets and the rotation quantifier

Let `X,Y subseteq V(K)`.  Write `mathfrak R_X(mathcal B)` for the family
of all models obtainable from `mathcal B` by disjoint path absorption in
which every bag meets `X`.

### Theorem 2.1 (exact sequential birooting criterion)

There is a path-absorption enlargement of `mathcal B` every bag of which
meets both `X` and `Y` if and only if

\[
 \nu_X(\mathcal B)=m
 \quad\hbox{and}\quad
 \max_{\mathcal C\in\mathfrak R_X(\mathcal B)}
                   \nu_Y(\mathcal C)=m.                \tag{2.1}
\]

#### Proof

The reverse implication follows by performing the two successful
absorptions in order.  The second absorption only enlarges bags, so it
does not remove their existing `X` vertices.

For the forward implication, let `D_i` be final disjoint connected bags
meeting `X,Y` and containing `B_i`.  Within each `D_i`, choose first an
`X`--`B_i` path.  These paths give some member
`mathcal C in mathfrak R_X(mathcal B)`.  Still within each `D_i`, choose a
path from `Y cap D_i` to the first-stage bag `C_i`, stopping at its first
contact with `C_i`.  These second-stage paths are disjoint across `i`.
Thus the corresponding `Y` capacity is `m`.  \(\square\)

Consequently, if `nu_X<m`, Menger gives a first-stage weighted cut.  If
`nu_X=m` but no birooted enlargement exists, then **every** first-stage
`X`-rooting has a second-stage weighted cut.  A cut obtained from one
arbitrary greedy rooting is not a canonical obstruction.

## 3. Explicit bag-rotation counterexample

The dependence on the first-stage absorption is real, already for two
singleton model bags.

Start with adjacent bags `B_1={b_1}`, `B_2={b_2}`.  Add vertices

\[
                    x_1,x_2,y_1,y_2,p,q
\]

and the following edges (besides `b_1b_2`):

\[
\begin{aligned}
 &x_1p,\ pb_1,\ x_1q,\ qb_1,\ x_2b_2,\\
 &y_1b_1,\ y_2p,\ pb_2.
\end{aligned}                                           \tag{3.1}
\]

Take `X={x_1,x_2}` and `Y={y_1,y_2}`.

There are two relevant `X`-rootings.

* **Bad rooting:** absorb `x_1-p-b_1` into `B_1` and `x_2-b_2` into
  `B_2`.  Both `Y` vertices can now reach the first enlarged bag, but any
  route from `y_2` to the second uses `p`, which already belongs to the
  first bag.  In the unit-bag quotient the first enlarged bag is a
  separator of capacity one, so `nu_Y=1`.
* **Good rotation:** instead absorb `x_1-q-b_1` and `x_2-b_2`.  The
  vertex `p` remains free.  The disjoint paths `y_1-b_1` and
  `y_2-p-b_2` now root both bags at `Y`, so `nu_Y=2`.

Thus the bad cut is destroyed by rotating the first path from `p` to
`q`.  Any proof which fixes one arbitrary first-stage linkage and treats
its second-stage cut as invariant is invalid.

## 4. Why a unit-bag cut is not yet colour-gluable

The weighted certificate (1.2) is exact for branch-set surgery, but the
unit weight of a whole bag is not a colour-boundary size.

Contracting a connected bag to `b_i` and colouring `b_i` with one colour
does not give a colouring of the original bag: the bag may contain edges
and may require several colours.  Equivalently, replacing `b_i` in a
quotient separator by the vertices of `B_i` can increase its order from
one to arbitrarily many.

The bad rooting in Section 3 is already a literal example.  Its unit cut
is the enlarged bag

\[
                         \{x_1,p,b_1\},
\]

which contains the path edges `x_1p,pb_1`.  The quotient treats it as one
separator vertex, but it cannot be assigned one colour on expansion.
Nor is there a general reason that one actual vertex of this path has all
of the external separation responsibilities of the whole bag after more
portals are added.

The gap can be arbitrarily large.  Let one model bag `B` induce
`K_{n,n}` with bipartition `L={l_1,...,l_n}` and
`R={r_1,...,r_n}`.  Add sources `x_i` with the single attachment
`x_i l_i`, and add a second singleton model bag `{c}` adjacent to every
`r_i`.  (Thus `B` and `{c}` are adjacent model bags.)  In the unit-bag
quotient, the single vertex `b` obtained from `B` is a unit cut between
the sources and `c`.  Inside the original bag, however, every separator
between the `L`-portals and the `R`-portals has order at least `n`, by
the `n` disjoint edges `l_i r_i` (or directly by Menger).  Hence a
unit-bag cut can require unbounded actual adhesion when lifted.

Therefore the implication

\[
 \text{unit-bag Menger cut}
 \quad\Longrightarrow\quad
 \text{same-order colour-gluable adhesion}
                                                        \tag{4.1}
\]

is false without an additional bag-interface hypothesis.

Sufficient hypotheses include, for example:

1. every cut bag is a singleton;
2. every cut bag has a specified single gate through which all relevant
   external paths, including passages to other cut bags, pass; or
3. the cut bag comes with a proved finite boundary-colouring signature
   and a gluing theorem preserving that signature.

The third item is the genuine general target.  It must record enough of
the bag's internal colouring to expand quotient colourings, while the
linkage theorem records only unit branch-set capacity.

### Lemma 4.1 (exact lift through the combined cut-bag society)

Let `S=S_0 dotcup {b_i:i in I}` be a unit-bag separator in `bar K`.
Choose a separation `(bar A,bar C)` of `bar K-S` with the surviving
sources in `bar A` and the surviving target bags in `bar C` (components
containing neither may be assigned arbitrarily).

Let

\[
                         D=K[\bigcup_{i\in I}B_i]
\]

include **all** edges between the cut bags.  Let `P^A` consist of the
vertices of `D` having a neighbour whose quotient image lies in `bar A`,
together with every source vertex in `X cap V(D)`.  Let `P^C` be the
vertices of `D` having a neighbour whose quotient image lies in `bar C`.
Suppose `Z_D subseteq V(D)` separates
`P^A-Z_D` from `P^C-Z_D` in `D`.  Then

\[
                         Z=S_0\cup Z_D                  \tag{4.2}
\]

is an ordinary vertex separator in `K` between the lifted `bar A` and
`bar C` sides.  Its order is

\[
                         |S_0|+|Z_D|.                   \tag{4.3}
\]

#### Proof

Lift every quotient vertex outside the cut bags to its original vertex or
bag side.  If a path in `K-Z` crossed from the lifted `bar A` side to the
lifted `bar C` side, its quotient trace could not cross outside `S`, by
the definition of `(bar A,bar C)`.  Consider the portion between the last
visit to the lifted `bar A` side and the first subsequent visit to the
lifted `bar C` side.  After deleting ordinary cut vertices `S_0`, this
portion starts in, or enters, the union of cut bags through `P^A-Z_D`,
travels through
`D-Z_D` (possibly using edges between several different cut bags), and
leaves through `P^C-Z_D`.  This contradicts the defining separation
property of `Z_D`.  \(\square\)

In particular, if the **combined** cut-bag society has a portal separator
of order at most `|I|`, then the unit-bag cut lifts to an ordinary
separator of no larger order.  More generally, (4.3) gives the correct
cost of the lift.  This is the precise repair of the false implication
(4.1): one must pay for a separator in the union of the cut bags, with all
interbag edges retained.

It is not enough to find one gate independently in each bag.  The cut
bags of a clique model are mutually adjacent, and an `A`-portal in one bag
may reach a `C`-portal in another through an interbag edge while avoiding
all per-bag portal separators.  Any proposed bag-by-bag lifting argument
must explicitly audit these rotations.

Even after (4.2) is obtained, colour gluing still requires compatible
colour states on the actual adhesion `Z`.  Lemma 4.1 supplies a genuine
vertex separator; it does not silently prove that its two side colourings
can be permuted to agree.

## 5. Consequence for bipartite compression

In the `(r-2)` slice of a bipartite compression, assume an unrooted
`K_{r-2}` model is already available.  Theorems 1.1 and 2.1 give the exact
two-parity outcome:

* either path absorption makes every clique bag meet both parity portal
  sets; or
* after optimizing over all rotations of the first absorption, every
  candidate has a weighted cut of order `<r-2` consisting of ordinary
  vertices and whole labelled clique bags.

This is stronger and cleaner than treating individual portal vertices as
independent target slots.  It still does not finish the uniform proof:
one must convert a rotation-stable weighted cut into either a genuine
small adhesion with compatible colour states or a label-preserving split
of one of its nontrivial bags.

That conversion is exactly where portal order, protected Steiner cores,
and finite-boundary criticality must enter.  It cannot be obtained from
Menger or from contraction alone.

## 6. Audit boundaries

1. Paths of length zero handle bags already meeting the portal set.
2. In a full `m`-linkage, target counting forbids every internal traversal
   of a model bag; this is why lifting is legal.
3. The bags are treated as indivisible unit-capacity objects.  Splitting a
   bag is a different operation and requires its own theorem.
4. The second-stage cut is quantified over all first-stage rotations, not
   one greedy choice.
5. Unit model capacity is not unit colouring capacity.  No colouring is
   lifted through a nontrivial contraction.
6. The theorem preserves all old clique adjacencies because it only
   enlarges disjoint connected bags.
