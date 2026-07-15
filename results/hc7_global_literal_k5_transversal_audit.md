# Audit of the global literal-`K_5` transversal theorem

## Verdict

**GREEN.**  The proof in
[`hc7_global_literal_k5_transversal.md`](hc7_global_literal_k5_transversal.md)
is correct as stated.  Its conclusion concerns literal `K_5` subgraphs, not
`K_5` minor models; the theorem file preserves that distinction throughout.

## 1. Audit of Lemma 1.1

Let `A,B` be distinct five-vertex cliques in a pairwise
four-intersecting family.  Their intersection has order exactly four, so

\[
 A=X\cup\{a\},\qquad B=X\cup\{b\},\qquad |X|=4.
\]

All pairs in `X union {a,b}` except possibly `ab` are edges.  Hence `ab`
would complete a literal `K_6`, and the exclusion of a literal `K_6` implies
that `ab` is a nonedge.

For any further clique `C`, if `x in X` were absent from `C`, the two
inequalities `|C cap A|>=4` and `|C cap B|>=4` would force the five-set

\[
 (X-\{x\})\cup\{a,b\}
\]

to equal `C`.  This is impossible because it contains the nonedge `ab`.
Thus every member contains `X`, proving the asserted common-vertex property
(in fact, a common four-set).  The all-equal case is immediate.

Now assume no three members have all three pairwise intersections of order at
most three.  If the full family is pairwise four-intersecting, the preceding
argument gives a one-vertex transversal.  Otherwise choose `A,B` with
`|A cap B|<=3`.  Every member `C` must satisfy

\[
 |C\cap A|\ge4\quad\hbox{or}\quad |C\cap B|\ge4,
\]

because `A,B,C` would otherwise be the forbidden triple.

The remaining cases are exhaustive:

* If `2<=|A cap B|<=3`, any two vertices of `A cap B` meet every five-set
  having at least four vertices in `A` or at least four in `B`.  They are a
  two-vertex transversal.
* If `|A cap B|<=1`, the subfamilies `F_A,F_B` defined in the proof cover the
  family and are disjoint: a five-set cannot contain four vertices from each
  of two five-sets whose intersection has order at most one.  Each member of
  `F_A` meets `B` in at most two vertices.  Therefore two members of `F_A`
  cannot meet in at most three vertices, since together with `B` they would
  form the forbidden triple.  Thus `F_A` is pairwise four-intersecting; the
  same holds for `F_B`.  Both are nonempty (`A in F_A` and `B in F_B`), so
  their respective common vertices form a transversal of order at most two.

Every alternative contradicts `tau(F)>2`, so Lemma 1.1 is valid.

## 2. Audit of Theorem 2.1

In a seven-connected graph, deleting the six vertices of a literal `K_6`
leaves a nonempty connected graph.  Every clique vertex has degree at least
seven and only five neighbours inside the clique, so it has a neighbour in
that connected remainder.  The remainder is therefore one connected branch
set adjacent to all six singleton clique branch sets.  These seven branch
sets form a literal `K_7` minor model.  No unstated disjointness or contraction
assumption is used.

Under the contrary assumptions of Theorem 2.1, Lemma 1.1 consequently applies
and returns three literal five-cliques with pairwise intersections at most
three.

The absence of a two-vertex transversal also implies that the graph is not
two-apex: if deleting at most two vertices left a planar graph, every literal
`K_5` would meet the deleted set.

Niu and Zhang's Theorem 1.10 states that a `(k+2)`-connected,
non-`(k-3)`-apex graph containing three literal `k`-cliques with pairwise
intersections at most `k-2` has a `K_(k+2)` minor.  Substitution of `k=5`
gives exactly:

* seven-connectivity;
* non-two-apexness; and
* three literal `K_5` subgraphs with pairwise intersections at most three.

Thus its use is exact and yields the required `K_7` minor.

## 3. Audit of Corollary 3.1

For a `K_7`-minor-free graph, Theorem 2.1 supplies a set `X` of order at most
two meeting every literal `K_5`; enlarging it to a two-set `P` preserves this
property.  A `K_5` minor model has five nonempty disjoint bags.  Its support
has order five if and only if all five bags are singletons, and their required
pairwise adjacencies then induce a literal `K_5`.  Since `G-P` has no such
subgraph, every surviving model has support order at least six, or no model
exists and `mu(P)=infinity`.  Therefore `mu(P)>=6` is correct.

## 4. Trust boundary

The proof does not show that the returned pair intersects every nonliteral
`K_5` model.  In particular, it neither proves `tau_(K_5)(G)<=2` for minor
models nor supplies a strict exchange above support order five.  The theorem
is nevertheless a valid global elimination of the support-five level.
