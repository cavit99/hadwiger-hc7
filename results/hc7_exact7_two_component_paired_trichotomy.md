# Two-component paired-state trichotomy

**Status:** proved and independently audited.

This theorem closes an unbounded exact-seven family.  When the rich shore
has two components and the thin side has legally attained the paired-
triangle state, the state either reflects, the graph is already
six-colourable, or the configuration supplies a spanning labelled
`K_7^vee` model and enters the normalized near-model spine.

No boundary census, component-order bound, Kempe trace, or portal ordering
is used.

## 1. Setup

Let `G` be seven-connected and suppose every proper minor of `G` is
six-colourable.  Let

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad S=\{c,a_1,t_1,a_2,t_2,a_3,t_3\}               \tag{1.1}
\]

be an actual separation with both open shores nonempty.  Put

\[
                         B_i=\{a_i,t_i\}\quad(i=1,2,3).
\]

Assume:

1. the open shore `L` has packet number one;
2. `G[R]` has exactly two components;
3. a legal proper-minor operation supported in the closed `L`-shore
   attains the exact boundary state

   \[
                \Pi=\{B_1,B_2,B_3,\{c\}\};            \tag{1.2}
   \]

4. every `B_i` is independent, every two distinct `B_i,B_j` have a
   literal edge between them, and `c` has a literal neighbour in every
   `B_i`.

Seven-connectivity makes every component of either open shore `S`-full.
The packet-number-one hypothesis therefore makes `G[L]` connected.  Write
the two connected full components of `G[R]` as `C,Q`, choosing `C`
nonsingleton whenever one exists.

### Theorem 1.1

At least one of the following holds:

1. `G` is six-colourable; or
2. `G` has a spanning labelled `K_7^vee` model with a singleton deficient
   centre.

In the second outcome, the audited near-model trichotomies give a literal
`K_7`, an actual separator, or a labelled deficiency rotation into a proper
connected part of one of the four nonsingleton model bags.

## 2. Reflection and availability

For a connected set `X subseteq C`, put

\[
 \Delta(X)=S-N_S(X),\qquad
 A(X)=\{i:B_i\cap\Delta(X)=\varnothing\}.              \tag{2.1}
\]

Thus `A(X)` is the set of paired duties which `X` funds.

### Lemma 2.1 (two adjacent carriers reflect)

Suppose `X,Y subseteq C` are disjoint connected adjacent sets and
`i in A(X)`, `j in A(Y)` are distinct.  Then `G` is six-colourable.

### Proof

Let `k` be the third duty.  Contract the three disjoint connected sets

\[
              X\cup B_i,\qquad Y\cup B_j,\qquad Q\cup B_k. \tag{2.2}
\]

The first two representatives are adjacent through `X-Y`; fullness of `Q`
joins its representative to the other two.  The literal `c-B_h` edge makes
each representative adjacent to the retained singleton `c`.  Thus the four
representatives form a clique indexed exactly by the blocks of `Pi`.

The contraction is proper, so a six-colouring pulls back to the untouched
closed `L`-shore with exact state `Pi`.  Aligning its block colours with the
legally attained colouring on the closed `R`-shore gives a six-colouring of
`G`.  \(\square\)

## 3. Low-complexity components

### Lemma 3.1 (cutvertex)

If `C` has a cutvertex, then `G` is six-colourable.

### Proof

Let `z` be a cutvertex, let `D` be a component of `C-z`, and put `E=C-D`.
Both `D` and `E` are connected and adjacent.  The set

\[
                              S\cup\{z\}
\]

separates `D` from the nonempty old opposite shore.  Seven-connectivity
therefore gives `|N_S(D)|>=6`.  Applying the same argument to a second
component of `C-z`, which is contained in `E`, gives `|N_S(E)|>=6`.
Consequently each of `A(D),A(E)` has order at least two.  Two subsets of a
three-set of order at least two have distinct representatives, so Lemma 2.1
applies.  \(\square\)

### Lemma 3.2 (orders two and three)

If `2<=|C|<=3`, then `G` is six-colourable.

### Proof

For `C=xy`, seven-connectivity applied at each vertex gives
`|N_S(x)|,|N_S(y)|>=6`; hence `A(x),A(y)` have distinct representatives.

Let `|C|=3`.  If `C` is not a triangle it has a cutvertex.  Otherwise write
`C=xyz` and put `Delta_v=Delta({v})`.  Since every vertex has only the two
other triangle vertices outside `S`, seven-connectivity gives

\[
                    |\Delta_v|\le2,\qquad
                    \Delta_x\cap\Delta_y\cap\Delta_z=\varnothing. \tag{3.1}
\]

For a split `x | yz`, failure of distinct duty representatives means that
both availability sets are the same singleton.  Hence `Delta_x` meets the
other two duties, while `Delta_y intersect Delta_z` meets the same two.
The order bound in (3.1) forces `Delta_y=Delta_z`.  If all three splits
failed, cycling the argument would give
`Delta_x=Delta_y=Delta_z`, contradicting (3.1).  Some split therefore
reflects by Lemma 2.1.  \(\square\)

### Lemma 3.3 (three-connected component)

If `C` is three-connected, then `G` is six-colourable.

### Proof

This is the audited uniform paired-state curvature-reflection theorem, with
`Q` as the disjoint full packet.  \(\square\)

If both components of `G[R]` are singletons, they are nonadjacent open
twins with common neighbourhood `S`.  A six-colouring of the proper minor
obtained by deleting one extends to it with the colour of the other.  Thus
outcome 1 holds.  We may consequently assume that the selected `C` is
nonsingleton.  Lemmas 3.1--3.3 leave only the case in which `C` is
two-connected but not three-connected.

## 4. A two-cut gives reflection or a near model

Choose a two-cut `Z={x,y}` of `C` and a component `D` of `C-Z`.  Since `C`
has no cutvertex, every component of `C-Z` has a neighbour at both poles.
Put

\[
                         X=D\cup\{x\},\qquad Y=C-X.     \tag{4.1}
\]

The sets `X,Y` are disjoint, connected, and adjacent.  The neighbourhood
of the raw lobe `D` is contained in `S union Z`; seven-connectivity gives
`|N_S(D)|>=5`, and hence

\[
                              |\Delta(X)|\le2.          \tag{4.2}
\]

A second component of `C-Z` lies in `Y` and gives the symmetric bound
`|Delta(Y)|<=2`.  Since `C` is `S`-full,

\[
                         \Delta(X)\cap\Delta(Y)=\varnothing. \tag{4.3}
\]

Both availability sets are nonempty.  If they have distinct
representatives, Lemma 2.1 gives outcome 1.  Otherwise two nonempty subsets
of a three-set with no system of distinct representatives are the same
singleton.  Renaming duties, let

\[
                         A(X)=A(Y)=\{3\}.              \tag{4.4}
\]

The two-element defect bound now forces each defect to contain one literal
from each of `B_1,B_2`.  Disjointness (4.3) makes the choices complementary.
Relabeling the two ends inside each paired block gives

\[
             \Delta(X)=\{a_1,a_2\},\qquad
             \Delta(Y)=\{t_1,t_2\}.                   \tag{4.5}
\]

Choose `r in B_3` adjacent to `c` and write `B_3-{r}={s}`.  The seven sets

\[
 X,\quad Y,\quad L\cup B_1,\quad Q\cup B_2,
 \quad\{c\},\quad\{r\},\quad\{s\}                   \tag{4.6}
\]

are disjoint, connected, and span `G`.  The first four form a clique:
`X-Y` is literal; (4.5) gives the four cross contacts through
`t_1,t_2,a_1,a_2`; and fullness joins the two packet bags.  Every one of
the first four sees `c,r,s`, while `cr` is literal.  Thus the only possibly
missing pairs are `sc,sr`, which share the singleton bag `{s}`.  Equation
(4.6) is a spanning labelled `K_7^vee` model, proving outcome 2.

The standardized near-model trichotomy conclusion in Theorem 1.1 is now
exactly Corollary 2.2 of
`hc7_exact7_complementary_lock_near_k7_handoff.md`.  \(\square\)

## 5. Exact scope

The theorem eliminates the entire two-**component** rich-shore branch for
the attained paired-triangle state, either terminally or by a label-faithful
`S1` handoff.  It does not handle two full packets interlaced inside one
connected rich component, an arbitrary attained demand-three state, packet
vector `(1,1)`, or termination of the global near-model rotation system.
