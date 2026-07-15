# A global two-vertex transversal for literal `K_5` subgraphs

## Status

The theorem below is proved from an elementary five-set lemma and the
published clique--minor theorem of Niu and Zhang.  It is a global result for
all seven-connected `K_7`-minor-free graphs; it does not use contraction
criticality or a selected near model.

It concerns **literal `K_5` subgraphs only**.  It does not say that deleting
the returned pair destroys every `K_5` minor, and therefore does not prove
the global model-transversal target or `HC_7`.

## 1. The elementary clique-family lemma

For a family `F` of sets, write `tau(F)` for the minimum order of a set
meeting every member of `F`.

### Lemma 1.1

Let `F` be the family of vertex sets of all literal `K_5` subgraphs of a
graph `G`.  If `G` has no literal `K_6` and

\[
                              \tau(F)>2,
\]

then `F` contains three members `L_1,L_2,L_3` such that

\[
                     |L_i\cap L_j|\leq 3
                     \qquad(1\leq i<j\leq3).             \tag{1.1}
\]

#### Proof

We first record a fact about a pairwise four-intersecting subfamily
`A` of `F`.  If all members of `A` are equal, they plainly have a
common vertex.  Otherwise choose distinct `A,B` in `A`.  Their intersection
has order four, so write

\[
                         A=X\cup\{a\},\qquad
                         B=X\cup\{b\},\qquad |X|=4.       \tag{1.2}
\]

If `ab` is an edge, then `X\cup\{a,b\}` induces a literal `K_6`: all
edges except possibly `ab` already lie in `A` or `B`.  This is excluded.
Hence `ab` is not an edge.

Let `C` belong to `A`.  It meets each of `A,B` in at least four vertices.
If some `x\in X` were absent from `C`, those two inequalities would force

\[
                         (X-\{x\})\cup\{a,b\}\subseteq C.
\]

The set on the left has order five, so equality holds; but then the clique
`C` contains the nonedge `ab`, a contradiction.  Thus every member of `A`
contains all of `X`.  We have proved:

> Every pairwise four-intersecting family of literal `K_5` subgraphs in a
> `K_6`-subgraph-free graph has a common vertex.                 \(\tag{1.3}\)

Now suppose that (1.1) fails.  If every two members of `F` meet in at
least four vertices, (1.3) gives `tau(F)=1`, contrary to the hypothesis.
Choose, therefore, `A,B` in `F` with

\[
                              |A\cap B|\leq3.             \tag{1.4}
\]

For every `C` in `F`, failure of (1.1) for the triple `A,B,C` says that

\[
                         |C\cap A|\geq4
                         \quad\hbox{or}\quad
                         |C\cap B|\geq4.                 \tag{1.5}
\]

If `|A\cap B|\geq2`, choose distinct `x,y\in A\cap B`.  A five-set meeting
`A` in at least four vertices misses at most one member of `A`, so it meets
`{x,y}`; the same is true with `B` in place of `A`.  By (1.5), `{x,y}`
meets every member of `F`, contradicting `tau(F)>2`.

It remains that

\[
                              |A\cap B|\leq1.             \tag{1.6}
\]

Partition `F` into

\[
 \begin{aligned}
  F_A&=\{C\in F:|C\cap A|\geq4\},\\
  F_B&=\{C\in F:|C\cap B|\geq4\}.
 \end{aligned}                                           \tag{1.7}
\]

Equation (1.5) says these families cover `F`.  They are disjoint: a
five-set cannot contain at least four vertices of each of two five-sets
whose intersection has order at most one.

If `C\in F_A`, then (1.6) gives `|C\cap B|\leq2`: at least four vertices of
`C` lie in `A`, at most one of those lies in `B`, and only one further
vertex is available.  Consequently, if two members `C,D in F_A` met in at
most three vertices, the three cliques `B,C,D` would satisfy (1.1), a
contradiction.  Thus `F_A` is pairwise four-intersecting.  Symmetrically,
so is `F_B`.

By (1.3), some vertex `x` belongs to every member of `F_A`, and some
vertex `y` belongs to every member of `F_B`.  Then `\{x,y\}` meets all of
`F`, again contradicting `tau(F)>2`.  This final contradiction proves the
lemma. \(\square\)

## 2. The global theorem

### Theorem 2.1 (literal-`K_5` transversal)

Every seven-connected graph `G` satisfies at least one of the following:

1. `G` contains a `K_7` minor;
2. there is a set `X\subseteq V(G)` of order at most two which meets every
   literal `K_5` subgraph of `G`.

#### Published input

Niu and Zhang prove the following theorem.

> If `k\geq2` and a `(k+2)`-connected non-`(k-3)`-apex graph contains three
> `k`-cliques `L_1,L_2,L_3` with
> `|L_i\cap L_j|\leq k-2` for all distinct `i,j`, then it contains a
> `K_{k+2}` minor.

This is Theorem 1.10 of Jianbing Niu and Cun-Quan Zhang,
*Cliques, minors and apex graphs*, Discrete Mathematics 309 (2009),
4095--4107, DOI
[`10.1016/j.disc.2008.12.009`](https://doi.org/10.1016/j.disc.2008.12.009).
An author-hosted copy is available
[here](https://math.wvu.edu/~cqzhang/Publication-files/my-paper/DM-2009-Apex.pdf).

#### Proof

Suppose that `G` has no `K_7` minor and that no set of order at most two
meets every literal `K_5`.

First, `G` has no literal `K_6`.  If `L` were a six-vertex clique, then
seven-connectivity would make `G-L` nonempty and connected.  Also every
vertex of `L` has a neighbour in `G-L`: its degree is at least seven but
it has only five neighbours in `L`.  Contracting the connected graph
`G-L` to one bag, together with the six singleton vertices of `L`, gives
a literal `K_7` model, contrary to the assumption.

Lemma 1.1 now supplies three literal `K_5` subgraphs
`L_1,L_2,L_3` satisfying

\[
                              |L_i\cap L_j|\leq3
                              \quad(i\ne j).              \tag{2.1}
\]

Moreover `G` is not two-apex.  Indeed, if `G-X` were planar for some
`|X|\leq2`, then every literal `K_5` would meet `X`, because a planar graph
contains no `K_5` subgraph.  This contradicts the assumed absence of a
two-vertex transversal.

Apply the Niu--Zhang theorem with `k=5`.  The graph is seven-connected,
non-two-apex, and has the three cliques (2.1), so it has a `K_7` minor.
This contradiction proves the theorem. \(\square\)

## 3. Consequence for the support potential

For a vertex pair `P`, let

\[
 \mu(P)=\min\{|V(M)|:M\text{ is a `K_5` minor model in }G-P\}, \tag{3.1}
\]

with `mu(P)=infinity` if no such model exists.

### Corollary 3.1

If `G` is seven-connected and `K_7`-minor-free, some pair `P` satisfies

\[
                              \mu(P)\geq6.                \tag{3.2}
\]

#### Proof

Choose the transversal `X` from Theorem 2.1 and, if necessary, enlarge it
to a two-vertex set `P`.  Then `G-P` has no literal `K_5`.  A five-bag
`K_5` model has support order five exactly when every bag is a singleton,
that is, exactly when it is a literal `K_5` subgraph.  Hence every model
in `G-P` has support at least six, or no such model exists. \(\square\)

## 4. Exact trust boundary

Theorem 2.1 is a genuine global theorem and Corollary 3.1 removes the
support-five level from a globally `mu`-maximal pair.  It does **not**
produce either of the conclusions needed to finish `HC_7`:

* the returned pair need not meet a `K_5` model whose support has order
  six or more;
* `G-P` need not be `K_5`-minor-free or planar;
* the theorem gives no exchange increasing `mu` from a finite value; and
* it does not orient reversible near-`K_7` rotations.

Thus the next support levels, beginning with six-vertex `K_5` models, are
the exact remaining model-transversal problem rather than a cosmetic
extension of this argument.
