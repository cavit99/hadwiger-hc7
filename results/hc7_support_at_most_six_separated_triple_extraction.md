# Separated triples of small `K_5`-model supports

**Status:** proved and independently audited.  This is a global extraction
theorem.  It does not compose the three returned models into a `K_7`.

## 1. Definitions and statement

For a graph `G`, let `S_{<=6}(G)` be the family of vertex sets which occur as
the union of the five branch sets of a `K_5` minor model using at most six
vertices.  Every member has order five or six.  A five-element member is the
vertex set of a literal `K_5`; a six-element member has bag-size multiset

\[
                           (2,1,1,1,1).                 \tag{1.1}
\]

For a set family `F`, let `tau(F)` be its vertex-transversal number.  Call
two sets `A,B`, each of order five or six, **near-identical** when

\[
             |A\cap B|\ge \max\{|A|,|B|\}-1.          \tag{1.2}
\]

Thus two five-sets are near-identical when they meet in at least four
vertices; a five-set and a six-set are near-identical precisely when the
five-set is contained in the six-set; and two six-sets are near-identical
when they meet in at least five vertices.

### Theorem 1.1 (small-support separated triple)

Let `G` be a seven-connected graph with no `K_7` minor, and let
`F` be any subfamily of `S_{<=6}(G)`.  If

\[
                              \tau(F)>2,                \tag{1.3}
\]

then there are three members `A_1,A_2,A_3` of `F` such that

\[
 |A_i\cap A_j|\le \max\{|A_i|,|A_j|\}-2
                    \qquad(1\le i<j\le3).              \tag{1.4}
\]

Equivalently, their pairwise intersection bounds are

\[
\begin{array}{c|c}
(|A_i|,|A_j|)&|A_i\cap A_j|\\ \hline
(5,5)&\le3,\\
(5,6)&\le4,\\
(6,6)&\le4.
\end{array}                                             \tag{1.5}
\]

Every six-element support in the conclusion has four singleton bags
forming a `K_4` and one two-vertex edge-bag.  Hence Theorem 1.1 reduces the
set-system half of the support-six problem to three controlled decorated
models.

### Corollary 1.2 (irredundant decorated witnesses)

If `tau(S_{<=6}(G))>2`, the three supports in Theorem 1.1 may be chosen so
that no six-element support contains a literal `K_5`.  For every selected
six-element support, write its edge-bag as `xy` and its singleton `K_4` as
`Q`.  Then each of

\[
 D_x=\{q\in Q:xq\notin E(G)\},\qquad
 D_y=\{q\in Q:yq\notin E(G)\}
\]

is nonempty, the two sets are disjoint, and, up to interchanging `x,y`,
their orders and the number of common contacts have one of the four forms

\[
                    (1,1,2),\ (1,2,1),\ (1,3,0),\ (2,2,0). \tag{1.6}
\]

#### Proof

Take `F=S_{<=6}(G)` and delete every six-set which contains a five-element
member.  This does not change the transversal number: a vertex set meeting
the contained five-set automatically meets its six-element superset.
Apply Theorem 1.1 to the remaining family.

For a selected six-support, every singleton row is adjacent to the edge-
bag, so `D_x` and `D_y` are disjoint.  If either were empty, that endpoint
together with `Q` would be a literal `K_5` contained in the support,
contrary to the reduction.  The two nonempty disjoint subsets of the
four-set `Q`, together with their common-contact complement, have exactly
the four size patterns in (1.6). \(\square\)

## 2. Classification of pairwise near-identical families

### Lemma 2.1

Let `C` be a family of sets, each of order five or six, in which every two
members are near-identical.  At least one of the following holds.

1. The members of `C` have a common vertex.
2. For some six-set `U`, the family contains every five-set `U-{u}` with
   `u in U`; every member of `C` is either `U` or one of these five-sets.
3. For some seven-set `U`, the family consists of all seven six-sets
   `U-{u}` with `u in U`.

In particular, `tau(C)<=2`.

#### Proof

First suppose that `C` contains two distinct five-sets.  Write them as

\[
                    A=X\cup\{a\},\qquad
                    B=X\cup\{b\},\qquad |X|=4,         \tag{2.1}
\]

where `a` and `b` are distinct and outside `X`.  The five-element members
of `C` form a pairwise four-intersecting five-uniform family.  Relative to
`A,B`, any further five-set either contains `X`, or has the form

\[
                    (X-\{x\})\cup\{a,b\}
                         \quad(x\in X).                 \tag{2.2}
\]

Indeed, if it omits `x in X`, meeting both sets in (2.1) in at least four
vertices forces all five vertices displayed in (2.2).

A set of the form (2.2) meets a set `X union {c}`, with
`c notin {a,b}`, in only three vertices.  Consequently either all
five-element members contain `X`, or they are all contained in

\[
                              U=X\cup\{a,b\}.           \tag{2.3}
\]

Every six-element member of `C` must contain both `A` and `B`, by the
mixed-size case of (1.2), and hence it must equal `U`.  In the first
alternative every member has the four-set `X` in common.  In the second,
all members are `U` or five-subsets of `U`.  If their total intersection is
empty, then for each `u in U` some member omits `u`; the unique five-subset
of `U` doing so is `U-{u}`.  Thus all six such five-sets occur, giving
outcome 2.

If `C` has exactly one five-element member `A`, then every six-element
member contains `A`, so the total intersection contains `A`.  It remains
to consider a six-uniform family.

Choose distinct `A,B in C` and write

\[
                    A=X\cup\{a\},\qquad
                    B=X\cup\{b\},\qquad |X|=5.         \tag{2.4}
\]

Every further member either contains `X`, or, after omitting some
`x in X`, is forced to equal

\[
                    (X-\{x\})\cup\{a,b\}.             \tag{2.5}
\]

A member of (2.5) meets `X union {c}` in only four vertices when
`c notin {a,b}`.  Hence either all members contain `X`, or all are
contained in the seven-set `X union {a,b}`.  In the latter case, empty
total intersection forces the omission of every one of the seven
vertices, and therefore forces all seven six-subsets.  This is outcome 3.
The singleton-family case is immediate.

Outcomes 2 and 3 are met by any two vertices of `U`, while outcome 1 has
a one-vertex transversal.  This proves the last assertion. \(\square\)

## 3. The abstract extraction dichotomy

### Lemma 3.1

Let `F` be a family of sets of order five or six with `tau(F)>2`.  Then
either

1. `F` contains three members which are pairwise not near-identical; or
2. `F` is the disjoint union of two pairwise near-identical subfamilies,
   and at least one of those subfamilies is one of the full families in
   outcome 2 or 3 of Lemma 2.1.

#### Proof

By Lemma 2.1, the whole family cannot be pairwise near-identical.  Choose
members `A,B` which are not near-identical.  Suppose that outcome 1 fails.
Then every `C in F` is near-identical to `A` or to `B`; otherwise
`A,B,C` would give outcome 1.

We first claim

\[
                              |A\cap B|\le1.            \tag{3.1}
\]

If two vertices `p,q` lay in `A intersect B`, every set near-identical to
`A` would contain at least one of `p,q`: in all four size combinations in
(1.2), such a set omits at most one literal vertex of `A`.  The same is
true for sets near-identical to `B`.  Thus `{p,q}` would meet all of `F`,
contrary to `tau(F)>2`.

No member can be near-identical to both seeds.  Indeed, if `C` were, then
inside `C` the sets `C intersect A` and `C intersect B` would intersect in
at least three vertices (the minimum occurs when all three sets have order
five).  This would contradict (3.1).  Therefore the families

\[
\begin{aligned}
 F_A&=\{C\in F:C\text{ is near-identical to }A\},\\
 F_B&=\{C\in F:C\text{ is near-identical to }B\}
\end{aligned}                                           \tag{3.2}
\]

are a disjoint partition of `F`.

Each part is pairwise near-identical.  To see this for `F_A`, observe that
any member `C` near-identical to `A` satisfies

\[
                              |B\cap C|\le2.            \tag{3.3}
\]

For equal sizes, `C` differs from `A` by at most one element; if
`|A|=5,|C|=6`, then `C` is `A` plus one element; and if
`|A|=6,|C|=5`, then `C` is a subset of `A`.  Equation (3.1) gives (3.3)
in every case.  If two members `C,D in F_A` were not near-identical,
then `B,C,D` would be pairwise not near-identical, contrary to the failure
of outcome 1.  The proof for `F_B` is symmetric.

If both subfamilies in (3.2) had a common vertex, one chosen vertex from
each common intersection would meet all of `F` (or one vertex would do so
if the choices coincided).  Hence one cluster has empty total intersection.
Lemma 2.1 identifies it as one of the two full families. \(\square\)

## 4. Full near-identical families force `K_7`

### Lemma 4.1 (six-vertex full family)

Let `G` contain a six-set `U` such that every `U-{u}` is the support of a
five-vertex `K_5` model.  Then `G[U]` is a literal `K_6`.

#### Proof

A `K_5` model on five vertices has five singleton branch sets, so each
`G[U-{u}]` is a literal `K_5`.  Given two vertices `x,y in U`, choose
`u in U-{x,y}`.  The clique `G[U-{u}]` contains the edge `xy`.  Thus all
pairs in `U` are adjacent. \(\square\)

### Lemma 4.2 (seven-vertex full family)

Let `J` be a graph on seven vertices.  If `J-v` has a spanning `K_5`
model for every vertex `v`, then `J` has a spanning `K_6` model.

#### Proof

Put `D=overline J`.  A spanning `K_5` model in a six-vertex graph implies
that its complement is a disjoint union of at most two nontrivial stars
and isolated vertices.  Indeed, the four singleton bags are
independent in the complement, the endpoints of the edge-bag are
nonadjacent there, and no singleton is adjacent in the complement to both
endpoints.  Only this forward implication is used here; the complement
`K_{1,5}` shows that its converse would be false for a *spanning* model.

Thus `D-v` is a union of at most two star components for every `v`.  If a
component of `D` were not a star, it would contain a triangle or a path
with three edges.  This obstruction uses at most four vertices and would
remain after deleting one of the other three vertices, a contradiction.
Hence every component of `D` is a star.

If `D` had three nontrivial components, choose one edge from each.  These
three independent edges use six vertices; deleting the seventh leaves
three nontrivial components, again a contradiction.  Therefore `D` has at
most two nontrivial star components.

If there are two, their centres are adjacent in `J`, the other five
vertices form a clique, and every one of those five sees at least one
centre in `J`.  The centre-edge is a two-vertex bag of a spanning `K_6`
model.  If there is one star with centre `x` and it has all six other
vertices as leaves, deleting a leaf gives a complement `K_{1,5}`; its
original graph is `K_5` plus an isolated vertex and has no spanning
`K_5` model, contrary to the hypothesis.  Otherwise choose a complement-
isolated vertex `y`; the edge `xy` in `J`, together with the other five
singleton vertices, gives the same model.  With no complement edge, `J`
is complete. \(\square\)

### Lemma 4.3 (small `K_6` models lift)

If a seven-connected graph contains a `K_6` model supported on at most
seven vertices, then it contains a `K_7` minor.

#### Proof

Let `W` be the support.  If `|W|<=6`, then `G-W` is connected.  Every
literal vertex of `W` has a neighbour outside `W`, since the minimum degree
is at least seven and there are at most five other vertices in `W`.
Therefore `G-W` is a seventh branch set adjacent to all six model bags.

Suppose `|W|=7`.  The graph has at least eight vertices, so `G-W` has a
component `C`.  Its neighbourhood is contained in `W`.  If it had order
at most six, deleting that neighbourhood would separate `C` from a vertex
of `W` outside the neighbourhood, contrary to seven-connectivity.  Hence
`N(C)=W`, and `C` is again a seventh branch set adjacent to all six bags.
\(\square\)

## 5. Proof of Theorem 1.1

Apply Lemma 3.1 to `F`.  If its first outcome holds, its three
members satisfy (1.4).

In the second outcome, a full six-vertex family gives a literal `K_6` by
Lemma 4.1, while a full seven-vertex family gives a `K_6` model supported
on seven vertices by Lemma 4.2.  Lemma 4.3 turns either conclusion into a
`K_7` minor, contrary to the hypothesis.  Therefore only the first outcome
is possible. \(\square\)

## 6. Exact trust boundary

Theorem 1.1 closes the purely set-system extraction half of the first
support-six rung.  It also removes the incompatibility between separate
two-covers of the literal and exact-six subfamilies: the theorem applies to
their union directly.

It does **not** prove `tau(S_{<=6}(G))<=2`.  The missing statement is a
graph-minor composition theorem for the three returned models.  Existing
three-clique theorems handle the `(5,5,5)` case, but a six-element support
has a split edge whose contraction can lower connectivity or merge a named
row of another model.  The intersection bounds alone do not align those
split edges with the other branch sets.  No such alignment is asserted
here.
