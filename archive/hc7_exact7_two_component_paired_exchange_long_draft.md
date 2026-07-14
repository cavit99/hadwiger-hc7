# Two-component paired-state exchange

**Status:** archived and superseded by
`../results/hc7_exact7_two_component_paired_trichotomy.md`.  The overall
reflect-or-`S1` conclusion is proved there by a shorter argument.  This
long draft's auxiliary Lemma 4.2 mishandles the impossible `|A|=0,4`
branch and must not be cited as written.

The target is to extend the uniform three-connected component theorem to a
whole two-component rich shore without enumerating boundary graphs.

## 1. Setup and the exact carrier criterion

Let `G` be seven-connected and suppose every proper minor of `G` is
six-colourable.  Let

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad
 S=\{c,a_1,t_1,a_2,t_2,a_3,t_3\}
\]

be an actual separation with both open shores nonempty.  Suppose a legal
operation in the closed `L`-shore attains

\[
 \Pi=\{B_1,B_2,B_3,\{c\}\},\qquad B_i=\{a_i,t_i\},
\tag{1.1}
\]

where each `B_i` is independent, every two distinct blocks `B_i,B_j` have a
literal edge between them, and `c` has a literal neighbour in every `B_i`.
Assume this is the oriented `(1,2)` packet cell: the open `L`-shore has
packet number one, while `G[R]` has exactly two connected components `C,Q`.
Seven-connectivity makes every open-shore component `S`-full.  It follows
in particular that `G[L]` is connected, and `C,Q` are the two rich full
packets.

### Lemma 1.1 (two carriers in one component suffice)

If `C` contains disjoint connected subgraphs `X,Y` and distinct indices
`i,j` such that

\[
             B_i\subseteq N_S(X),\qquad B_j\subseteq N_S(Y),
\tag{1.2}
\]

then `Pi` reflects.

#### Proof

Assign `Q` to the third block `B_k`.  The three sets

\[
              X\cup B_i,\qquad Y\cup B_j,\qquad Q\cup B_k
\]

are connected and disjoint.  Literal inter-block edges make their three
representatives pairwise adjacent, and the named `c-B_r` edges join each to
`c`.  Contracting the three sets gives a proper minor with a `K_4` indexed
exactly by the blocks of `Pi`.  Its six-colouring pulls back to the untouched
closed `L`-shore with exact state `Pi`; palette alignment with the already
attained colouring glues the shores.  \(\square\)

For a connected carrier `X`, write

\[
 \Delta(X)=S-N_S(X),\qquad
 A(X)=\{i\in\{1,2,3\}:B_i\cap\Delta(X)=\varnothing\}.
\tag{1.3}
\]

Thus `A(X)` is exactly the set of duties that `X` can fund in Lemma 1.1.

## 2. Uniform low-complexity closures

### Lemma 2.1 (a cutvertex reflects)

If `C` has a cutvertex, then `Pi` reflects.

#### Proof

Let `z` be a cutvertex, let `D` be a component of `C-z`, and put
`E=C-D`.  Both are nonempty and connected.  Since

\[
                         N_G(D)\subseteq S\cup\{z\},
\]

and the old opposite shore and `Q` survive beyond this neighbourhood,
seven-connectivity gives `|N_S(D)|>=6`.  Applying the same argument to a
second component of `C-z`, contained in `E`, gives `|N_S(E)|>=6`.
Consequently `|Delta(D)|,|Delta(E)|<=1`.  Each of `A(D),A(E)` has order at
least two, so these two subsets of a three-set have distinct
representatives.  Lemma 1.1 applies.  \(\square\)

### Lemma 2.2 (components of order two or three reflect)

If `2<=|C|<=3`, then `Pi` reflects.

#### Proof

If `C=xy`, then `N_G(x) subseteq S union {y}` and symmetrically for `y`.
Seven-connectivity gives `|N_S(x)|,|N_S(y)|>=6`; hence both availability
sets have order at least two and Lemma 1.1 applies.

Let `|C|=3`.  A noncomplete connected graph has a cutvertex, so Lemma 2.1
handles it.  It remains that `C=xyz` is a triangle.  Put
`Delta_v=Delta({v})`.  The neighbourhood of each vertex is contained in
`S` together with the other two triangle vertices, so

\[
                         |\Delta_v|\le2.                \tag{2.1}
\]

Fullness of `C` says

\[
                   \Delta_x\cap\Delta_y\cap\Delta_z=\varnothing.
\tag{2.2}
\]

For a split `x | yz`, the two availability sets are

\[
 A(\{x\}),\qquad
 A(\{y,z\}),quad
 \Delta(\{y,z\})=\Delta_y\cap\Delta_z.                \tag{2.3}
\]

Both are nonempty.  If they have no distinct representatives, both are the
same singleton.  Then `Delta_x` meets two duties, while
`Delta_y intersect Delta_z` meets those same two duties.  By (2.1), the last
intersection has two elements and forces `Delta_y=Delta_z`.  If every one
of the three splits failed, cycling this argument would give
`Delta_x=Delta_y=Delta_z` with two elements, contradicting (2.2).  Some
split therefore has distinct duty representatives, and Lemma 1.1 applies.
\(\square\)

### Lemma 2.3 (a three-connected component reflects)

If `C` is three-connected, then `Pi` reflects.

#### Proof

This is the audited uniform paired-state curvature theorem, with `Q` as the
disjoint full packet.  \(\square\)

Thus a surviving nonsingleton component is two-connected but not
three-connected.

If both rich components are singletons, they are nonadjacent open twins
with common neighbourhood `S`.  A six-colouring of the proper minor obtained
by deleting either one extends to it with the colour of the other.  Hence at
least one rich component is nonsingleton.

## 3. Exact complementary lock at a two-cut

Let `Z={x,y}` be a two-cut of such a component `C`, and let `D` be a
component of `C-Z`.  Since `C` has no cutvertex, every component of `C-Z`
has a neighbour at both `x` and `y`.  Put

\[
                       X=D\cup\{x\},\qquad Y=C-X.       \tag{3.1}
\]

The sets `X,Y` are nonempty, connected, disjoint, and adjacent.  The
separator bound applied to `D` and to a second component of `C-Z` gives

\[
              |\Delta(X)|,|\Delta(Y)|\le2,qquad
              \Delta(X)\cap\Delta(Y)=\varnothing.      \tag{3.2}
\]

If `A(X),A(Y)` have distinct representatives, Lemma 1.1 reflects.  Hence a
nonreflecting split has, after renaming duties,

\[
 \Delta(X)=\{a_1,a_2\},\qquad
 \Delta(Y)=\{t_1,t_2\},\qquad
 A(X)=A(Y)=\{3\}.                                      \tag{3.3}
\]

Indeed, two nonempty subsets of a three-set fail to have distinct
representatives only when their union is one singleton.  A defect of order
at most two leaves only duty `3` precisely when it contains one literal
from each of `B_1,B_2`; disjointness gives the complementary endpoints in
(3.3).

Now swap the two cut vertices and use

\[
                       X'=D\cup\{y\},\qquad Y'=C-X'.    \tag{3.4}
\]

The raw lobe `D` misses exactly `a_1,a_2`, so nonreflection forces
`Delta(X')={a_1,a_2}`.  It follows that `y` misses both labels.  Applying
the same argument to `Y'` shows that `x` misses `t_1,t_2`.  The original
split already gives the reverse two statements.  Therefore

\[
 N_S(x)\cap(B_1\cup B_2)
 =N_S(y)\cap(B_1\cup B_2)=\varnothing.                 \tag{3.5}
\]

Moreover the raw lobe has the exact neighbourhood

\[
 N_G(D)=\{x,y\}\cup(S-\{a_1,a_2\}).                   \tag{3.6}
\]

Thus

\[
             S_D=\{x,y\}\cup(S-\{a_1,a_2\})          \tag{3.7}
\]

is a new literal seven-boundary.  The old attained colouring restricts to
a legally attained exact state on `S_D`: the proper operation that returned
`Pi` lies wholly in the new opposite closed shore and touches no vertex of
`D`; its valid pullback restricts to `D union S_D`.  It may have used old
boundary vertices which are still in `S_D`, so no claim that the new state
has paired-triangle form is made.

There are exactly two components of `C-Z`.  Indeed, apply (3.3) to a lobe
`D_1`.  Every other lobe is contained in the complementary carrier and
therefore misses its two-label defect.  Applying (3.3) to a second lobe
`D_2` forces its defect to be that complementary pair.  A third lobe would
then have to miss both complementary pairs: it lies in the complement of
`D_1` and in the complement of `D_2`.  This contradicts the bound of two on
its defect.  Write the two lobes as `D,E`.  Then, in the normalization
(3.3),

\[
 \Delta(D)=\{a_1,a_2\},\qquad
 \Delta(E)=\{t_1,t_2\},\qquad
 N_S(\{x,y\})\subseteq\{c,a_3,t_3\}.                  \tag{3.8}
\]

Consequently the two exact seven-boundaries

\[
 \{x,y\}\cup(S-\{a_1,a_2\}),\qquad
 \{x,y\}\cup(S-\{t_1,t_2\})                          \tag{3.9}
\]

overlap in the five literal vertices `x,y,c,a_3,t_3`.  This overlap is the
state-transition interface, not merely another support pattern.

## 4. A forced bichromatic crossing

Let `phi` be the colouring of the closed rich shore returned by the legal
operation which attained `Pi`.  Write `alpha,beta` for the colours of
`B_1,B_2`, respectively, and put

\[
 K=\{a_1,t_2\},\qquad K'=\{t_1,a_2\}.                \tag{4.1}
\]

### Lemma 4.1 (diagonal Kempe separation reflects)

If no `alpha-beta` Kempe component of `phi` meets both `K` and `K'`, then
`G` is six-colourable.

#### Proof

Swap `alpha` and `beta` on the union of all `alpha-beta` components meeting
`K`.  The hypothesis says that this union misses `K'`.  The resulting
proper colouring `phi'` therefore induces on `S` the exact state

\[
 \Pi'=\bigl\{\{a_1,a_2\},\{t_1,t_2\},B_3,\{c\}\bigr\}.
\tag{4.2}
\]

Use the two-pole split

\[
 X=D\cup\{x\},\qquad Y=E\cup\{y\}.                  \tag{4.3}
\]

The sets `X,Y` are disjoint, connected, and adjacent: each raw lobe has a
neighbour at each pole.  Equations (3.5) and (3.8) give

\[
 \Delta(X)=\{a_1,a_2\},\qquad
 \Delta(Y)=\{t_1,t_2\}.                             \tag{4.4}
\]

Consequently the three disjoint sets

\[
 Y\cup\{a_1,a_2\},\qquad
 X\cup\{t_1,t_2\},\qquad
 Q\cup B_3                                             \tag{4.5}
\]

are connected.  The first two are adjacent through `X-Y`; the third is
adjacent to both because `Q` is `S`-full.  Each is adjacent to `c`: the raw
lobes `D,E` both meet `c`, and `Q` meets `c`.  Contracting (4.5) thus gives
a proper minor containing a literal `K_4` indexed by the four blocks of
`Pi'`.  Every six-colouring of this minor expands to a colouring of the
closed thin shore inducing exactly `Pi'`.  Align it with `phi'` and glue.
\(\square\)

Thus every survivor has an `alpha-beta` Kempe component meeting both
diagonal sets in (4.1).  This conclusion permits a path through `Q`; it
does not yet give a path inside `C`, two disjoint carriers, or a reflected
state.

The preceding swap admits a sharper state-level formulation.  Put

\[
 U=B_1\cup B_2,quad P=\{a_1,a_2\},\quad
 \bar P=\{t_1,t_2\}.                                \tag{4.6}
\]

### Lemma 4.2 (only the two mixed matchings can survive)

Suppose a proper colouring of the closed rich shore agrees with `Pi` on
`B_3 union {c}`, uses only `alpha,beta` on `U`, and has `alpha`-class
`A subseteq U`.  Unless the unordered partition

\[
                         A\mid(U-A)                  \tag{4.7}
\]

is either the original matching `B_1|B_2` or the crossed matching

\[
             \{a_1,t_2\}\mid\{t_1,a_2\},            \tag{4.8}
\]

the colouring glues to a six-colouring of `G`.

#### Proof

If `|A|` is zero or four, `U` is one equality block.  The two connected
sets `C union U` and `Q union B_3`, together with `c`, form a `K_3` model:
the original paired state supplies a literal `U-B_3` edge and fullness
supplies both `c` adjacencies.  Contracting the two sets returns exactly
this three-block state on the closed thin shore.

Suppose `|A|` is one or three, and let `u` be the singleton block and `W`
the triple block.  If `u in P`, use `Y` for `u` and `X` for `B_3`; if
`u in bar P`, reverse those assignments.  Thus

\[
 Q\cup W,\qquad Y\cup\{u\},\qquad X\cup B_3
\tag{4.9}
\]

or its `X,Y` reversal are three disjoint connected sets.  The two lobe
carriers are adjacent, while `Q` is full to the boundary vertices in the
other two sets.  All three meet `c`.  They therefore form, with `c`, a
`K_4` indexed by the four equality blocks.

Finally let `|A|=2`.  Up to complementation there are exactly three
partitions of `U` into pairs.  Two are (4.7)--(4.8).  The third is
`P|bar P`, which reflects by the branch sets in (4.5).  In each case the
corresponding rich-side contractions are proper and their clique images
force the exact boundary state, so palette alignment finishes.  \(\square\)

### Corollary 4.3 (Kempe trace dichotomy)

In a surviving configuration, the `alpha-beta` Kempe components which meet
`U` have one of exactly two terminal-trace patterns:

1. one component has trace `U`; or
2. two components have traces `P` and `bar P`.

#### Proof

The nonempty traces of those components partition `U`.  Swap any one such
component with trace `T`.  Before the swap the `alpha`-class is `B_1`, and
after it the class is `B_1 symmetric-difference T`.  Lemma 4.2 says that
this class must
be one side of the original or crossed matching.  Hence

\[
 T\in\{U,P,\bar P\}.                                 \tag{4.10}
\]

Disjoint nonempty members of this family can partition `U` only as `U` or
as `P,bar P`.  \(\square\)

The second outcome is a reversible matching rotation, not a strict
descent.  The first is a single four-terminal Kempe component.  Either may
use `Q`, so the dichotomy alone does not close the lock.

## 5. Three-shore state synchronization

The two-cut lock has one further uniform closure which does not select a
six-colouring in advance.

### Lemma 5.1 (two carriers synchronize three shores)

Let `G-S` have at least three connected components, all `S`-full.  Suppose
one component `C` contains disjoint adjacent connected carriers `X,Y`.  Let
`I,J` be disjoint nonempty independent subsets of `S` such that

\[
 I\subseteq N_S(X),\qquad J\subseteq N_S(Y),           \tag{5.1}
\]

and put `W=S-(I union J)`.  If `|W|=3`, `G[W]` has an edge, and

\[
                         W\subseteq N_S(X)\cap N_S(Y), \tag{5.2}
\]

then `G` is six-colourable.

#### Proof

Choose two other components `A,Q`.  Contract the disjoint connected sets
`A union I` and `Q union J`.  Their
images are adjacent, and fullness makes each image adjacent to every
literal vertex of `W`.  Six-colour this proper minor, restrict to the
untouched closed `C`-shore, and expand `I,J`.  The exact boundary state is

\[
                         \Sigma=I\mid J\mid\Theta,      \tag{5.3}
\]

where `Theta` is the proper equality partition induced on `W`.  The edge
in `G[W]` makes `Theta` have either two or three blocks.

We reproduce this actual state on every other closed component-side.  Fix a
component `R ne C` and choose a full component `F` different from both
`C,R`; this is possible because there are at least three components.  Use
the carriers `X union I`, `Y union J`, and `F`.

If `Theta` has two blocks, one is an independent pair `K` and the other is
a singleton `{w}`.  Contract the available full component together with
`K` and retain `w`.  The resulting four representatives are a clique:
`X,Y` are adjacent, fullness supplies the adjacencies of the third
representative, and (5.2) supplies both carrier-to-`w` adjacencies.

If `Theta` has three singleton blocks, choose an edge `uv` of `G[W]`,
contract the available full component with the third vertex of `W`, and
retain `u,v`.  The five representatives are a clique by adjacency of
`X,Y`, fullness, (5.2), and the literal edge `uv`.

Thus a proper-minor colouring gives the exact same state `Sigma` on the
closed `R`-side for every component `R ne C`.  Permute all palettes to
agree blockwise on `S`.  The components of `G-S` are pairwise anticomplete,
so these component-side colourings and the original closed `C`-side
colouring glue to a six-colouring of `G`.  \(\square\)

In the complementary lock, `G-S` has at least three full components: `C`,
`Q`, and a component of the nonempty old opposite shore.  Take

\[
 I=\bar P=\{t_1,t_2\},\qquad J=P=\{a_1,a_2\},
 \qquad W=B_3\cup\{c\}.                               \tag{5.4}
\]

The carriers `X,Y` in (4.3) fund `bar P,P`, respectively, and both contact
all of `W`.  The named `c-B_3` adjacency gives an edge in `G[W]`.
Consequently Lemma 5.1 yields the sharp necessary condition

\[
              a_1a_2\in E(G)\quad\hbox{or}\quad
              t_1t_2\in E(G).                          \tag{5.5}
\]

Thus the reversible matching state is not the whole obstruction: a
surviving lock must also contain a literal edge in at least one of its two
complementary defect pairs.

## 6. Further bichromatic locks

Let `gamma` be the colour of `B_3` in `phi`.

### Lemma 6.1 (the original pairs are Kempe-connected to `B_3`)

The vertices `a_1,t_1` lie in one `alpha-gamma` Kempe component of `phi`,
and `a_2,t_2` lie in one `beta-gamma` Kempe component.

#### Proof

Suppose the `alpha-gamma` component containing `a_1` misses `t_1`, and
swap its two colours.  The two resulting equality blocks on
`B_1 union B_3` separate `a_1` from `t_1`.  The block containing `a_1`
is a subset of `{a_1,a_3,t_3}` and is therefore fully contacted by `Y`;
the block containing `t_1` is a subset of `{t_1,a_3,t_3}` and is fully
contacted by `X`.  Assign `Q` to the unchanged block `B_2`.

The three carrier sets are connected and disjoint.  The first two are
adjacent through `X-Y`, `Q` is full to both other boundary blocks, and all
three carriers contact `c`.  Their contractions therefore force on the
closed thin shore exactly the Kempe-swapped four-block state.  It aligns
with the swapped colouring `phi'` and glues, a contradiction.  The
`beta-gamma` argument is symmetric.  \(\square\)

This gives two label-faithful bichromatic connections, but either can use a
literal vertex of `B_3`; they are not yet disjoint reserved carriers.

## 7. Complementary-lock near-model handoff

Within the frozen 129-boundary residual, a separate reorientation theorem
closes the case in which one rich component is a singleton.  Under the
abstract paired-state hypotheses of this note alone, that conclusion is not
claimed.  The only nonsingleton obstruction left by Sections 2--6 is the
complementary two-lobe lock (3.3)--(3.9), with one of the two Kempe trace
patterns in Corollary 4.3, at least one defect-pair edge from (5.5), and
the two additional Kempe connections in Lemma 6.1.

Merely descending to `S_D` is not a closure: its opposite shore need not
contain two full `S_D`-packets, and the colours of `x,y` need not produce a
paired-triangle state.

The transition is in fact already forced by the full actual `(1,2)` cell;
descending to `S_D` is unnecessary.  Choose `r in B_3` adjacent to `c` and
write `B_3-{r}={s}`.  The seven sets

\[
 D\cup\{x\},\quad E\cup\{y\},\quad
 L\cup B_1,\quad Q\cup B_2,\quad
 \{c\},\quad\{r\},\quad\{s\}                         \tag{7.1}
\]

are disjoint and connected.  The first four form a clique: the lobe bags
are adjacent across the two-cut, their four packet adjacencies use
`t_1,t_2,a_1,a_2`, and fullness joins the two packet bags.  Each of the
first four sees `c,r,s`, while `cr` is literal.  Thus the only possibly
missing pairs are `sc,sr`; they share the singleton centre `s`.  Equation
(7.1) is a spanning labelled `K_7^vee` model.

The audited both-missing and singleton one-hole near-model trichotomies now
give a literal `K_7`, an actual separator, or a labelled deficiency rotation
whose new centre is a proper connected part of one of the first four bags.
This is exactly the `S1` handoff required by the proof spine.  Source:
`../results/hc7_exact7_complementary_lock_near_k7_handoff.md`.

Consequently every two-component rich shore under the attained
paired-triangle hypotheses either reflects, is immediately six-colourable,
or enters the normalized `S1` near-model/adhesion system.  The remaining
global obligation is termination and composition of that system, not a
further two-lobe portal case.
