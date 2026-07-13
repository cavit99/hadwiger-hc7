# The mobile-path exchange in the exact `K_3\vee C_4` carrier

## Status

This note combines the audited total-contraction state with the literal
geometry of a lex-minimal six-duty path row.  It proves three things.

1. A repeated mobile portal class gives a **rooted bilateral five-colour
   state** on an internal subpath, not merely an unrooted poor edge.
2. The six foreign bags have five literal pairwise adjacent carriers after
   merging any rim edge.  At a balanced cut, two label-exact repair packets
   therefore give a literal `K_7`, with all seven branch sets displayed.
3. The audited two-portal support theorem composes with this construction
   when its four distinct protected terminals (or flexible-attachment
   hypotheses) and the required disjoint helpers are present.  Failure is
   then the exact cutvertex/degenerate-gate output of that theorem.

This closes the whole infinite family in which the two missing carrier
contacts have such a protected two-packet support.  It does **not** infer
that support from palette colours.  The final section gives a smallest static
label-incidence witness showing why that inference would be invalid; that
witness is not an `HC_7` counterexample.

## 1. Exact carrier and the rooted total-contraction split

Let

\[
             R,S,T,U_0,U_1,U_2,U_3                         \tag{1.1}
\]

be pairwise disjoint connected bags.  The first three are the common rows,
the four `U_i` occur cyclically, and every pair is adjacent except

\[
                         U_0U_2,\qquad U_1U_3.              \tag{1.2}
\]

Assume that `G` is proper-minor-minimal non-six-colourable and that

\[
                         G[R]=r_0r_1\cdots r_n              \tag{1.3}
\]

is an induced path.  A duty is one of the six foreign bags in (1.1).  The
endpoint `r_0` owns every duty all of whose `R`-ends equal `r_0`, and
similarly for `r_n`.  In the lex-minimal path cell, the two owner sets are
disjoint, have order at least two, and at most two duties are mobile.

For a foreign bag `Q`, write

\[
                         P_Q=N_R(Q).                        \tag{1.4}
\]

### Theorem 1 (rooted bilateral mobile state)

Let `Q` be a mobile duty and let `r_i,r_j in P_Q` with `i<j`.  Put

\[
                         X=G[r_i,\ldots,r_j].               \tag{1.5}
\]

Contract `X` to a vertex `z`, and take any six-colouring `c` of `G/X`.
If `alpha=c(z)`, then some edge `r_kr_{k+1}` with `i<=k<j` splits `X`
into the two path intervals

\[
 X^- =\{r_i,\ldots,r_k\},\qquad
 X^+ =\{r_{k+1},\ldots,r_j\},                              \tag{1.6}
\]

such that

\[
 c(N_G(X^-)-X)=c(N_G(X^+)-X)
                 =\{1,\ldots,6\}-\{\alpha\}.              \tag{1.7}
\]

Both shores have a literal edge to the **same old bag `Q`**.  Moreover,
if `|X|>=3`, the one-block state `c|N(X)` is excluded from the boundary
state family of the proper minor which contracts `X^-` and `X^+`
separately.

#### Proof

The induced subgraph `X` is a connected bipartite graph with at least two
vertices.  Lemma 2.1 of the audited total-contraction theorem says that
`G/X` is six-chromatic, so the selected colouring exists.  Apply its
Theorem 2.2 with the path itself as spanning tree.  It gives (1.6)--(1.7).

Every edge of the path separates its two ends.  Hence `r_i in X^-` and
`r_j in X^+`.  Since both lie in `P_Q`, each shore has an actual edge to
the unchanged connected bag `Q`.  Corollary 2.5 of the same audited theorem
is exactly the final marked-boundary assertion.  \(\square\)

The point of choosing an internal repeated portal class is that the roots
of the poor split are now literal.  If `i>0` and `j<n`, no endpoint-owned
duty has an edge to a vertex of `X`; all direct labelled contacts of `X`
are through the one or two mobile bags.  The five secondary colours in
(1.7), however, may also be witnessed through `R`-private bridges.  They
are not foreign-bag labels.

## 2. The literal five-carrier frame

The foreign quotient on

\[
                         S,T,U_0,U_1,U_2,U_3               \tag{2.1}
\]

is `K_2\vee C_4`.  For every `h` modulo four, put

\[
 W_h=U_h\cup U_{h+1},\qquad
 \mathcal K_h=\{S,T,W_h,U_{h+2},U_{h+3}\}.                 \tag{2.2}
\]

### Lemma 2 (rim-edge `K_5` carrier)

The five members of `mathcal K_h` are disjoint, connected and pairwise
adjacent.

#### Proof

The rim edge `U_hU_{h+1}` makes `W_h` connected.  The common rows `S,T`
are adjacent to each other and to every rim bag.  Contracting one edge of
a four-cycle produces a triangle: explicitly, `W_h` meets `U_{h+2}`
through `U_{h+1}U_{h+2}`, meets `U_{h+3}` through `U_hU_{h+3}`, and
`U_{h+2}U_{h+3}` is a rim edge.  Thus the last three bags form a triangle
and both common rows are complete to it.  \(\square\)

### Theorem 3 (two-packet mobile-path completion)

Let an edge of `R` split the whole path into nonempty connected adjacent
shores `L,R'`.  Fix `h`, and suppose each shore has a literal edge to at
least four of the five carriers in `mathcal K_h`.  Suppose its unique
missed carrier is `K_L` for `L` and `K_R` for `R'` (the two missed
carriers are allowed to coincide).

If there are disjoint connected sets `Z_L,Z_R`, disjoint from the path and
from all five carriers, such that

\[
       Z_L\sim L,K_L,\qquad Z_R\sim R',K_R,                \tag{2.3}
\]

then `G` contains a literal `K_7` minor.

The assertion remains true when one shore misses no carrier: take its
packet empty and leave that shore unchanged.

#### Proof

Enlarge the shores to

\[
                         L^+=L\cup Z_L,\qquad
                         R^+=R'\cup Z_R.                   \tag{2.4}
\]

They are connected, disjoint and adjacent through the old path-cut edge.
By hypothesis and (2.3), each enlarged shore is adjacent to every member
of `mathcal K_h`.  Lemma 2 says that those five members are connected,
disjoint and pairwise adjacent.  Therefore

\[
                         L^+,R^+,\mathcal K_h              \tag{2.5}
\]

are seven disjoint connected pairwise adjacent branch sets.  \(\square\)

This is the exact label-preserving carrier conversion needed at a balanced
path cut.  In the sharp `2+2+2` owner cell, a particularly useful instance
occurs when the merged rim edge `U_hU_{h+1}` has one endpoint owned at each
end of `R`, both mobile duties meet both shores, and the unmerged owner at
each end is the unique carrier missed by the opposite shore.  Then (2.3)
asks for exactly two packets, one in each direction.

## 3. Composition with protected two-portal supports

The next corollary records a genuine infinite-family closure rather than
renaming the packet condition.  Its hypotheses are exactly those returned
by the audited protected-support theorem.

### Corollary 4 (protected support closes the balanced path)

Keep Theorem 3.  Suppose `Z` is a connected old exterior piece, disjoint
from the path and all five carriers, with four distinct vertices

\[
                         l,r,x,y\in Z,                     \tag{3.1}
\]

where `l` meets `L`, `r` meets `R'`, and `x,y` meet `K_L,K_R`,
respectively.  If `Z` contains disjoint paths joining `l` to `x` and `r`
to `y`, then `G` has a `K_7` minor.

More generally the pairing of `x,y` is immaterial when each has an edge to
both missed carriers.

Put

\[
 A=N_Z(L),\quad B=N_Z(R'),\quad P=N_Z(K_L),\quad Q=N_Z(K_R).
                                                               \tag{3.2}
\]

If `Z` is 4-connected and these four whole portal sets are nonempty and
pairwise disjoint, the set-rooted Two Paths theorem gives either disjoint
`A-P` and `B-Q` paths, hence the literal `K_7` above, or a planar connector
with all four whole portal sets on one facial cycle in alternating block
order `A,Q,P,B`, up to reflection.

There is also a protected common-carrier version.  Assume an old exterior
support `K` has four distinct terminals `l,r,x,y` (or satisfies the exact
flexible-attachment hypotheses of Theorem 3 of the audited two-portal
support exchange), where `l,r` attach to opposite path shores and `x,y`
attach to the common missed carrier.  Assume every helper used for the
other missed carrier is pairwise disjoint, avoids `K`, the path, and all
five carriers, and already attaches to its assigned path shore and missed
carrier.  Then Theorems 1 and 3 of that audited exchange give either the
two protected paths, which combine with the helpers and yield `K_7`, or
one exact cutvertex portal arm/degenerate side gate.

#### Proof

Take the two paths in `Z` as `Z_L,Z_R`.  Their `l,r` ends have literal
edges to the path shores and their `x,y` ends have literal edges to the
assigned missed carriers, so Theorem 3 applies.

For (3.2), apply the set-rooted rural-order theorem to the four nonempty,
pairwise disjoint whole attachment sets.  In its crossed outcome the two
paths are again the packets of Theorem 3; its other outcome is the stated
facial block order.  The final assertion imports exactly the protected or
flexible construction, including its disjoint-helper hypotheses, from
Theorems 1 and 3 of the two-portal support exchange and then applies
Theorem 3 here.  Its failure outcomes are the stated cutvertex portal arm
and concentrated literal gate.  \(\square\)

Thus arbitrary size of the support is gone.  A surviving balanced path is
not a further portal-mask family: it has one alternating rural page, one
literal cutvertex arm, or one degenerate gate.  The one-block/two-block
state in Theorem 1 lives on the actual boundary of that same path interval,
so an operation on an opposite open shore with the same marked partition
would six-colour `G` by the audited crossed-state splice.

## 4. Why the five-colour state alone does not create the packets

It is essential not to replace the last geometric sentence by a
palette-to-label assertion.  The following smallest quotient witness makes
the failure explicit.

Take the six foreign vertices `0,...,5`, with `0,1` forming `K_2` and
`2,3,4,5` forming the rim `C_4`.  Add the induced path

\[
                         p_0p_1\cdots p_6.                \tag{4.1}
\]

Let `p_0` own `0,1`, let `p_6` own `2,3`, and let the mobile contacts be

\[
 N_R(4)=\{p_1,p_2,p_3,p_4\},\qquad N_R(5)=\{p_5\}.       \tag{4.2}
\]

There are no other edges.  This graph has no `K_7` minor, and the displayed
path is label-preserving minimal: no nonempty proper connected subpath can
serve as the common row while the six old labelled foreign bags are only
enlarged by removed path vertices.

#### Proof

There are thirteen vertices.  The following eight bags, joined in the
displayed tree order, are a tree decomposition (path vertices are written
as `p_i`):

\[
\begin{array}{lll}
A=\{0,1,3,4,5,p_5\},&
B=\{0,1,2,3,5,p_5\},& A-B,\\
C=\{0,1,4,p_1,p_5\},& A-C,\\
D=\{2,3,p_5,p_6\},&B-D,\\
E=\{0,1,p_0,p_1\},&C-E,\\
F=\{4,p_1,p_4,p_5\},&C-F,\\
H=\{4,p_1,p_3,p_4\},&F-H,\\
I=\{4,p_1,p_2,p_3\},&H-I.
\end{array}                                               \tag{4.3}
\]

Every graph edge is contained in one displayed bag, and the bags
containing any fixed vertex form a connected subtree of the displayed
tree.  Its largest bags have order six, so the graph has treewidth at most
five.  Since treewidth is minor-monotone and `tw(K_7)=6`, it has no `K_7`
minor.

For label-preserving minimality, the retained row must contain `p_0`.
Indeed `p_0` is the only path vertex adjacent to either old label `0` or
old label `1`.  If a nonempty connected retained subpath omits `p_0`, its
component towards `p_0` has only one edge back to the retained subpath.
After all removed prefix vertices are assigned to old foreign bags, that
one cut edge can restore the retained-row adjacency to at most one of the
two distinct labels `0,1`; the other required duty is lost.  The same
argument at the other end forces `p_6`, using the two old labels `2,3`.
A connected subset of the induced path containing both ends contains every
`p_i`.  Hence the displayed row cannot be shortened in the permitted
label-preserving comparison.  \(\square\)

The script `hc7_mobile_path_probe.py` independently checks both assertions
by connected-branch-set and labelled-assignment search.

This witness is deliberately low-connected and is not contraction-critical.
It does **not** refute the desired `HC_7` exchange.  It does show precisely
what the total-contraction state does not supply: a palette witness in a
nonsingleton foreign carrier is not a connected packet to that carrier.
The actual `HC_7` hypotheses must be spent on the rural/cutvertex/degenerate
outputs of Corollary 4, or on a matching proper-minor state from the opposite
open shore.  The positive theorems above ensure that no further bounded or
unbounded support enumeration is needed once either physical mechanism is
present.
