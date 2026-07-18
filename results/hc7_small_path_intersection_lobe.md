# A path-intersection residual has nonnegative literal separator excess

**Status:** written proof; separate internal audit in the adjacent note.
This is an unbounded
conditional theorem for the exact order-seven branch.  When a forced
boundary-to-boundary path meets one of two boundary-full connected subgraphs,
it either synchronizes the boundary colouring or forces at least as many
literal external attachments as it loses boundary contacts.  Equality is an
actual order-seven separation.  It does not prove that every first
intersection has the connected-residual form used below, and it does not
prove `HC_7`.

## 1. Setup

Let `G` be a seven-connected graph which is not six-colourable and every
proper minor of which is six-colourable.  Suppose

\[
 V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}B,
 \qquad E_G(A,B)=\varnothing,
 \qquad |S|=7,                                      \tag{1.1}
\]

where `A` and `B` are nonempty.  Write

\[
 S=D\mathbin{\dot\cup}E\mathbin{\dot\cup}\{r,z\},
 \qquad |D|=3,\quad |E|=2.                         \tag{1.2}
\]

Assume that a proper six-colouring of `G[A union S]` induces one of the
following two equality partitions on the literal boundary:

\[
 \Pi_A=D\mid E\mid\{r\}\mid\{z\},
 \qquad
 \Pi_B=D\mid E\mid\{r,z\}.                         \tag{1.3}
\]

Let `C_1,C_2` be disjoint connected subgraphs of `G[A]`, each
adjacent to every literal vertex of `S`.  Let `P` be an `r-z` path whose
internal vertices lie in `A`, and assume

\[
 V(P)\cap V(C_2)=\varnothing.                       \tag{1.4}
\]

Suppose that

\[
 T=V(P)\cap V(C_1)                                  \tag{1.5}
\]

is nonempty, and that

\[
 R=V(C_1)-T                                          \tag{1.6}
\]

is nonempty and connected.  Put

\[
                         U=N_G(R)-S                  \tag{1.7}
\]

Thus `R` is the part of the first boundary-full subgraph disjoint from the
path, and `U` is its complete set of literal neighbours outside the
seven-vertex boundary, not merely a selected set of attachments.

Define its set of lost boundary contacts by

\[
 \Lambda=\{s\in S:E_G(s,R)=\varnothing\}.           \tag{1.8}
\]

## 2. Portal allocation

### Lemma 2.1

Under (1.1)--(1.8), the following assertions hold.

1. If the boundary partition is `Pi_A` and

   \[
   \Lambda\subseteq D\cup\{r\},\quad
   \Lambda\subseteq D\cup\{z\},\quad
   \Lambda\subseteq E\cup\{r\},\quad\text{or}\quad
   \Lambda\subseteq E\cup\{z\},                   \tag{2.1}
   \]

   then `G` is six-colourable.

2. If the boundary partition is `Pi_B` and either

   \[
                  \Lambda\cap D=\varnothing
                  \quad\text{or}\quad
                  \Lambda\cap E=\varnothing,        \tag{2.2}
   \]

   then `G` is six-colourable.

#### Proof

We construct connected branch sets whose contraction reproduces the exact
partition in (1.3) on the untouched closed side `G[B union S]`.

First suppose the partition is `Pi_A`.  Consider, for example,

\[
                         \Lambda\subseteq E\cup\{r\}.               \tag{2.3}
\]

Then `R` has a neighbour at each vertex of `D` and at `z`.  Split the path
`P` at the edge immediately after the last vertex of `T`, obtaining adjacent
connected sets `P_r,P_z` with

\[
 r\in P_r,\qquad T\subseteq P_r,
 \qquad z\in P_z.                                   \tag{2.4}
\]

The four sets

\[
              R\cup D,\qquad V(C_2)\cup E,
              P_r,\qquad P_z                         \tag{2.5}
\]

are disjoint and connected.  They are pairwise adjacent:

* `R union D` meets `P_r` through an edge from `R` to `T`, and it meets
  `P_z` through its retained boundary contact at `z`;
* `C_2 union E` meets the two path sets through its contacts at `r,z`;
* the two boundary-block sets are adjacent because `C_2` has a neighbour
  at every vertex of `D`; and
* `P_r,P_z` are adjacent at the splitting edge.

Contract a spanning tree in each set in (2.5).  The four representatives
form a clique and contain, respectively, the four independent boundary
blocks `D,E,{r},{z}`.  In a six-colouring of this proper minor the four
representatives therefore have distinct colours.  Keep that colouring on
`G[B union S]`, expanding each boundary block with the colour of its
representative.  The resulting colouring has exact equality partition
`Pi_A`.  After a permutation of colour names it glues to the given
colouring of `G[A union S]`, contrary to the hypothesis on `G`.

The other three containments in (2.1) use the same construction.  If the
lost contacts lie in `E union {z}`, keep `R union D` and split immediately
before the first vertex of `T`, putting all of `T` in the `z`-side of the
path.  If they lie in `D union {r}` or `D union {z}`,
interchange the roles of `D` and `E`, assigning `R` to the `E`-block and
`C_2` to the `D`-block.

Now suppose the partition is `Pi_B`.  If `Lambda cap D` is empty, the
three sets

\[
                    R\cup D,\qquad V(C_2)\cup E,
                    V(P)                              \tag{2.6}
\]

are disjoint, connected and pairwise adjacent.  The first and third meet
through an edge from `R` to `T`; the second and third meet through a
boundary contact at `r`; and the first two meet through a contact from
`C_2` to `D`.  Their contraction forces the exact boundary partition
`D|E|{r,z}` on the untouched closed side, which glues to the given
colouring.  If `Lambda cap E` is empty, interchange `D` and `E`.  This
proves the lemma. \(\square\)

## 3. Literal separator excess

### Theorem 3.1

Under (1.1)--(1.8), necessarily all of the following hold.

1. If the boundary partition is `Pi_A`, then `Lambda` is contained in none
   of the four sets displayed in (2.1).
2. If the boundary partition is `Pi_B`, then

   \[
                         \Lambda\cap D\ne\varnothing,
                         \qquad
                         \Lambda\cap E\ne\varnothing.               \tag{3.1}
   \]

3. In either case,

   \[
                         |U|\ge|\Lambda|\ge2.          \tag{3.2}
   \]

4. The **literal separator excess**

   \[
       \varepsilon(R)=|U|-|\Lambda|
                     =|N_G(R)|-7                     \tag{3.3}
   \]

   is a nonnegative integer.  If `epsilon(R)=0`, then

   \[
                    N_G(R)=U\mathbin{\dot\cup}(S-\Lambda)           \tag{3.4}
   \]

   is the boundary of an actual nontrivial separation of order exactly
   seven.

Thus every residual which does not already return an exact order-seven
separation has positive literal separator excess.  This quantity is
measured in the host graph and is independent of a chosen quotient or
minor model.

#### Proof

If the partition is `Pi_A`, any containment in (2.1) would make `G`
six-colourable by Lemma 2.1.  Hence none occurs.  In particular
`|Lambda|>=2`, since every empty or singleton subset of `S` is contained
in at least one of the four sets in (2.1).

If the partition is `Pi_B`, Lemma 2.1 gives (3.1), which again implies
`|Lambda|>=2`.

By the definitions of `U` and `Lambda`,

\[
 |N_G(R)|=|U|+|S-\Lambda|=|U|+7-|\Lambda|.           \tag{3.5}
\]

The set `N_G(R)` separates the nonempty connected set `R` from the
nonempty opposite open side `B`.  Seven-connectivity therefore gives

\[
                              |N_G(R)|\ge7.            \tag{3.6}
\]

Equations (3.5)--(3.6) give `|U|>=|Lambda|`; together with the preceding
paragraphs this proves (3.2).  Equation (3.3) follows by rearranging
(3.5).  If `epsilon(R)=0`, then (3.4) has order seven.  Since `R` and `B`
remain in different nonempty components after deleting it, this is an
actual nontrivial order-seven separation. \(\square\)

## 4. The two-attachment corollary

### Corollary 4.1

Under (1.1)--(1.8), suppose additionally that `|U|<=2`.  Then

\[
                          |U|=|\Lambda|=2,
                          \qquad \varepsilon(R)=0,                   \tag{4.1}
\]

so (3.4) is an actual order-seven separator.  Moreover:

1. if the boundary partition is `Pi_A`, then either

   \[
                 \Lambda=\{r,z\},
                 \quad\text{or}\quad
                 \Lambda=\{d,e\}
                 \text{ for some }d\in D,e\in E;     \tag{4.2}
   \]

2. if the boundary partition is `Pi_B`, then

   \[
                 \Lambda=\{d,e\}
                 \text{ for some }d\in D,e\in E.     \tag{4.3}
   \]

In particular, if `U subseteq T`, a one-vertex path intersection is
impossible.  If `U subseteq T` and `|T|=2`, then `U=T` and the theorem
returns the exact separator in (3.4), unless Lemma 2.1 already synchronized
the boundary colouring.

#### Proof

Theorem 3.1 gives `2<=|Lambda|<=|U|<=2`, proving (4.1).  For `Pi_A`, a
direct classification of two-element subsets of

\[
                         D\mathbin{\dot\cup}E
                           \mathbin{\dot\cup}\{r,z\}                 \tag{4.4}
\]

shows that the only sets contained in none of the four sets in (2.1) are
`{r,z}` and the pairs `{d,e}` with `d in D,e in E`.  For `Pi_B`, (3.1)
and `|Lambda|=2` give exactly one member of `D` and one of `E`. \(\square\)

## 5. Exact scope

The theorem is host-level and unbounded: no order bound is imposed on
`A`, `B`, `C_1`, `C_2` or `R`.  It uses seven-connectivity only after the
branch-set contractions have forced the portal obstruction.

Its remaining gap is explicit.  A general first-entry path may meet both
boundary-full connected subgraphs, the residual part may be disconnected,
or its positive separator excess may persist under every available
rerouting.  The theorem does not show that `epsilon(R)` strictly decreases
under a further host operation.  It also does not assert that the exact
separator in (3.4) already carries compatible colourings on its two shores.

## 6. Dependencies

The proof is self-contained apart from the minor-minimal six-colourability
assumption and elementary connectivity.  Its setup is returned by the
[two-full-subgraph Kempe-compression theorem](hc7_exact7_two_full_subgraph_kempe_compression.md),
which supplies the path and the two possible high-demand equality
partitions.
