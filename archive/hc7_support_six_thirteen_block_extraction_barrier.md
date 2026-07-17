# A minimum pair-cover barrier to the four-outcome extraction list

**Status:** proved abstract decorated-family barrier, but **not a live graph
obstruction**.  It shows that a proposed four-outcome extraction theorem is
false for bare set systems.  The subsequently proved nine-vertex
support-six closure shows that no seven-connected `K_7`-minor-free graph can
realize this design with transversal number greater than two.  Retain this
note only as a warning against forgetting graph structure.

## 1. The nine-point design

Let

\[
 A=\{a_0,a_1,a_2,a_3\},\qquad
 Z=\{z_0,z_1,z_2,z_3,z_4\},\qquad X=A\dot\cup Z.
\]

Take the following thirteen triples as a block family `B`:

\[
\begin{array}{lll}
 a_0a_1a_2,&a_0a_1a_3,&a_2a_3z_0,\\[2mm]
 a_0z_0z_1,&a_0z_0z_2,&a_1z_0z_3,\\
 a_1z_0z_4,&a_1z_1z_2,&a_0z_3z_4,\\
 a_2z_1z_3,&a_2z_2z_4,&a_3z_1z_4,\\
 a_3z_2z_3.&&
\end{array}                                             \tag{1.1}
\]

For every `B in B`, let

\[
                              F_B=X-B.                 \tag{1.2}
\]

Regard each `F_B` as a formal support-six model.  Choose a four-subset
`Q_B subset F_B` and mark the complementary pair
`e_B=F_B-Q_B` as its split row.

The cores `Q_B` may be chosen pairwise distinct.  Greedily, when the
`k`-th support is decorated, fewer than thirteen cores have been used while
that support contains fifteen four-subsets.  Each decoration may also be
given any locally normalized deficiency type, for example `(1,1,2)`.
No global graph realization of those local edge prescriptions is assumed.

## 2. Exact covering properties

### Lemma 2.1

The blocks in (1.1) cover every pair of points of `X`.  Exactly three pair
incidences are repeated:

\[
                       a_0a_1,qquad a_0z_0,qquad a_1z_0.  \tag{2.1}
\]

Every other pair occurs in exactly one block.

#### Proof

The first three blocks cover all six pairs inside `A`.  The remaining ten
blocks correspond to an edge-colouring of `K_5` on `Z`:

\[
\begin{array}{c|l}
a_0&01,02,34\\
a_1&03,04,12\\
a_2&13,24\\
a_3&14,23.
\end{array}                                             \tag{2.2}
\]

Every edge of `K_5` occurs once.  At each of `z_1,z_2,z_3,z_4`, the four
incident edges receive the four different `A`-colours.  At `z_0`, colours
`a_0,a_1` occur twice and the missing colours `a_2,a_3` are supplied by
the block `a_2a_3z_0`.  This covers every `A-Z` pair and gives exactly the
repetitions in (2.1). \(\square\)

### Lemma 2.2

For `F=\{F_B:B in B\}` one has

\[
                              \tau(F)=3.                \tag{2.3}
\]

The family has no full seven-point top from the near-identical-family
classification.

#### Proof

Given a two-set `P`, Lemma 2.1 supplies a block `B` containing it, and
`F_B` is disjoint from `P`.  Thus no two-set meets every support.  On the
other hand, `\{z_0,z_1,z_2\}` is not one of the triples in (1.1).  Since
all blocks and this set have order three, it is contained in no block and
therefore meets every complementary support.  This proves (2.3).

A full seven-point top would require all seven triples through one fixed
pair as complement blocks.  By Lemma 2.1 every pair occurs at most twice,
so no such top exists. \(\square\)

### Lemma 2.3

The block family has transversal number four.  In particular, the four-set
`A` is not contained in any support `F_B`.

#### Proof

Every displayed block meets `A`, so the block transversal number is at
most four and `A` is contained in no complementary support.

The only points lying in five blocks are `a_0,a_1,z_0`; every other point
lies in four blocks.  Suppose a three-set `R` met all thirteen blocks.  If
`R` is not `\{a_0,a_1,z_0\}`, its total point--block incidence is at most
fourteen.  Each of its three pairs lies in at least one block by Lemma 2.1,
and at most one block contains all three points.  Inclusion--exclusion
therefore shows that `R` meets at most

\[
                              14-3+1=12
\]

blocks.  The exceptional set `\{a_0,a_1,z_0\}` has incidence sum fifteen,
each of its three pairs lies in two blocks, and no block contains the whole
triple, so it meets only nine blocks.  Thus no three-set, and hence no
smaller set, is a block transversal. \(\square\)

The design is minimum for these two simultaneous properties: covering
every pair by triples while having a four-point block transversal.

### Lemma 2.4 (minimality)

Any triple family on nine points which covers every pair and has a
four-point transversal has at least thirteen blocks.  The family (1.1)
attains the bound and is inclusion-minimal.

#### Proof

Twelve triples have only `36` pair incidences, exactly the number of pairs
of nine points.  If they cover every pair, each pair occurs exactly once,
so they form a Steiner triple system on nine points.

Suppose a four-set `R` met all twelve blocks.  Let `n_i` count blocks
meeting `R` in exactly `i` points.  Counting blocks, incidences with `R`,
and pairs inside `R` gives

\[
 n_1+n_2+n_3=12,qquad
 n_1+2n_2+3n_3=16,qquad
 n_2+3n_3=6.
\]

These equations force `n_3=2` and `n_2=0`.  But two distinct triples
inside a four-set share a pair, impossible in a Steiner triple system.
Hence twelve blocks cannot have a four-point transversal.

The thirteen blocks in (1.1) attain the bound.  Every displayed block
contains a pair other than the three repeated pairs in (2.1), so removing
it leaves that pair uncovered.  Thus the family is also inclusion-minimal.
\(\square\)

## 3. Failure of the proposed extraction list

### Theorem 3.1

The decorated family above has transversal number greater than two but
admits none of the following outcomes.

1. A row-compatible one-split/two-literal-clique triple.
2. Three vertex-disjoint normalized split models.
3. Three split models with one common singleton `K_4` core.
4. A nine-set whose genuine six-supports cover every four-subset.

#### Proof

There are no five-element members, so outcome 1 is unavailable.  All
supports lie in the same nine-set and have order six, so three of them
cannot be vertex-disjoint.  The cores were chosen pairwise distinct, so
outcome 3 is unavailable.  The ground set itself is the only nine-set, and
Lemma 2.3 gives a four-subset not contained in any support.  Thus outcome 4
also fails. \(\square\)

The pair meeting all literal `K_5` supports adds no abstract restriction:
this family has no literal members, so every pair has that property.  The
failure therefore persists after retaining the audited fixed-pair input.

## 4. Graph realization is now closed

The later theorem

[`../results/hc7_nine_vertex_support_six_closure.md`](../results/hc7_nine_vertex_support_six_closure.md)

classifies every graph on nine vertices whose exact six-supports have
transversal number greater than two.  Such a graph either contains a
`K_7` minor or is `complement(C_9)`.  The exceptional graph has an
`N`-meeting `K_6` model for every seven-set `N`; hence seven-connectivity
of the ambient graph supplies the seventh bag.  Consequently the design
in this note cannot survive in the active `HC_7` setting, regardless of
whether it satisfies the more local extension property below.

The remainder records the earlier, weaker mechanism because it remains a
useful example of how graph structure enters a formal support design.

## 5. The earlier graph-specific condition

The abstract obstruction has a sharply localized realization condition.
Let a graph `G` genuinely realize every `F_B` as a spanning `K_5` model,
and put

\[
                         D=\overline{G[X]}.
\]

The complement of a spanning support-six `K_5` model is a union of at most
two stars.  Hence `D[F_B]` contains neither a triangle nor a three-edge
path.

Call a four-set `R subset X` a **blocking four-set** when it meets every
block in `B`.  The following is the precise extra input needed here.

> **Blocking-`P_4` extension property.**  Whenever `D[R]` contains a
> three-edge path on a blocking four-set `R`, some genuine support-at-most-
> six `K_5` model of `G` contains all four vertices of `R`.

### Proposition 4.1

No `K_7`-minor-free graph can genuinely realize (1.1) and satisfy the
blocking-`P_4` extension property.

#### Proof

By Lemma 2.3 the block family has no transversal of order at most three.
Therefore every set of at most three vertices is disjoint from some block,
or equivalently is contained in some selected support.  It follows that
`D` has no triangle.

If `D` had a three-edge path, its four vertices could not be contained in
one of the selected supports, so they would form a blocking four-set.
The extension property would put those same four vertices in another
genuine support-at-most-six model.  But the complement on the support of
such a model cannot contain a three-edge path, a contradiction.

Thus `D` has neither a triangle nor a three-edge path.  Every component of
`D` is a star.  The complement of a star forest on nine vertices contains
a `K_7` minor by the audited four-cover composition argument.  Hence
`G[X]`, and therefore `G`, contains a `K_7` minor. \(\square\)

Consequently any genuine `K_7`-minor-free realization of this minimum
abstract barrier must expose a blocking four-set `R` such that

1. `D[R]` contains a three-edge path; and
2. no support-at-most-six `K_5` model contains `R`.

This is the graph-specific residue hidden by pair-cover arithmetic.  A
viable replacement for the false four-outcome extraction list is therefore

\[
 \boxed{\text{one of the three composition patterns, a four-cover
 terminal, or an unextendable blocking complement-}P_4.}
\]

The last alternative is suitable for a connectivity/model-regeneration
attack: it asks for an extension of one named four-vertex obstruction, not
for a further taxonomy of support intersections.
