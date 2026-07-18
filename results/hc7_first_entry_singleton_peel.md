# A first-entry vertex can be peeled from a degree-eight exterior component

**Status:** written proof; separate internal audit.  This is a host-level
reduction for the three-path branch.  It preserves the literal neighbour
labels retained by the residual component.  Its order-seven outcome carries
one proper-minor colouring on the opposite closed side, but it does not prove
that the same boundary partition extends through both closed sides.

## 1. Setup

Let `G` be seven-connected, let `v` be a vertex of degree eight, and let
`D` be a component of `G-N_G[v]`.  Put

\[
                         S=N_G(D)\subseteq N_G(v).
\tag{1.1}
\]

Assume that there is a vertex outside `D union S`; the vertex `v` itself
has this property.  Seven-connectivity gives

\[
                          7\le |S|\le8.                 \tag{1.2}
\]

Fix `y in D` such that `D-y` is nonempty and connected.  Define the set of
neighbour labels monopolized by `y` inside `D` by

\[
 \Lambda_D(y)=\{s\in S:N_G(s)\cap D=\{y\}\}.          \tag{1.3}
\]

Thus the labels of `S` still contacted by `D-y` are exactly
`S-\Lambda_D(y)`.

## 2. Singleton peel or exact order-seven boundary

### Theorem 2.1

Exactly one of the following two numerical alternatives holds, and the
corresponding structural conclusion follows.

1. If

   \[
                    |S-\Lambda_D(y)|\ge7,              \tag{2.1}
   \]

   then `D-y` is a connected subgraph retaining at least seven of the eight
   literal neighbour labels in `N_G(v)`.
2. If

   \[
                    |S-\Lambda_D(y)|\le6,              \tag{2.2}
   \]

   then

   \[
             N_G(D-y)=\{y\}\mathbin{\dot\cup}
                        (S-\Lambda_D(y))               \tag{2.3}
   \]

   is the boundary of an actual nontrivial order-seven separation.

In particular, when `D` is two-connected the theorem applies to every
vertex `y in D`.  If a connected named subgraph `P` outside `D` has an edge
to `y`, then in outcome 1 the replacement

\[
                         P\longmapsto P\cup\{y\},
       \qquad           D\longmapsto D-y               \tag{2.4}
\]

is a label-preserving singleton peel: the enlarged set is connected, the
residual set is connected and retains at least seven neighbour labels, and
all old adjacencies of `P` survive.

#### Proof

Because `D` is a component of `G-N_G[v]`, every neighbour outside `D` of a
vertex of `D-y` belongs to `S`, except that deleting `y` makes `y` itself a
possible new boundary vertex.  Conversely, every member of
`S-\Lambda_D(y)` has a neighbour in `D-y`.  Since `D` is connected, `y`
has a neighbour in the nonempty set `D-y`.  Therefore

\[
       N_G(D-y)=
          \{y\}\mathbin{\dot\cup}(S-\Lambda_D(y)).   \tag{2.5}
\]

The set `D-y` is connected and nonempty by hypothesis.

If (2.1) holds, the first conclusion is just the definition of
`\Lambda_D(y)`.  The assertions about (2.4) follow because the stipulated
edge joins `y` to `P`, while deleting `y` does not alter any vertex or edge
of `P`.

Suppose instead that (2.2) holds.  The right side of (2.5) has order at
most seven.  The connected set `D-y` is separated from `v`: no vertex of
`G-N_G[v]`, and hence no vertex of `D-y`, is adjacent to `v`.  Thus
`N_G(D-y)` is the boundary of a genuine nontrivial separation.  By
seven-connectivity it has order at least seven.  Hence it has order exactly
seven (and necessarily `|S-\Lambda_D(y)|=6`), proving (2.3).  \(\square\)

## 3. The concrete proper-minor colouring at the returned boundary

Assume now that every proper minor of `G` is six-colourable, and let

\[
                         T'=N_G(D-y)                    \tag{3.1}
\]

be the order-seven boundary in outcome 2.

### Proposition 3.1

If `|D-y|>=2`, contracting a spanning tree of `D-y` gives a proper minor
whose six-colouring restricts to a proper colouring of the unchanged
closed side `G-(D-y)`.  On the literal boundary `T'` this colouring uses at
most five colours.

#### Proof

Contract the connected set `D-y` to a vertex `d`.  This is a proper minor.
Every member of `T'=N_G(D-y)` is adjacent to `d` in the minor, so no member
of `T'` receives the colour of `d`.  Restricting the minor colouring to the
unchanged vertices gives the claimed proper colouring of `G-(D-y)` and
uses at most the other five colours on `T'`.  \(\square\)

This is only a one-sided boundary partition.  The theorem does not show
that it extends through `G[(D-y) union T']`.  Let `x` be the predecessor of
`y` on a clean first-entry path.  Then `x in S`, but

\[
                 x\in T'\quad\Longleftrightarrow\quad
                 x\notin\Lambda_D(y);                    \tag{3.2}
\]

only `y` is guaranteed to belong to `T'`.  Nevertheless, the edge `xy`
lies entirely in the unchanged closed side `G-(D-y)`.  If, as in the active
counterexample, `G` is not six-colourable, a six-colouring after deleting
`xy` makes `x,y` equal (otherwise it would colour `G`), and a colouring
after contracting `xy` likewise cannot be pulled back across the restored
literal edge.  Thus neither one-edge operation by itself supplies the
missing proper colouring of the original closed side.

## 4. Application and exact remaining condition

### 4.1 Clean first entry

Let `P_0,P_1,P_2,C_0,...,C_4` be the fixed connected subgraphs used by the
cyclic contact-allocation theorem, and suppose that they are pairwise
disjoint and disjoint from `D`.  In this application, assume that `D` lies
in the open shore `R` and that the paths considered below lie in the far
closed shore `G[R union T]`.  Fix `s in {0,1,2}`.  A path `R_s` from `P_s`
to a vertex `y in D` is a **clean first-entry path** when

1. `R_s-y` is disjoint from `D`;
2. every internal vertex of `R_s` is disjoint from all the other fixed
   subgraphs; and
3. `y` is the first vertex of `D` on the path.

The direct-entry case, in which `R_s` consists of one edge from `P_s` to
`y`, is the simplest example.  Merely taking the first vertex of
`Q_0 cap D` is not enough: the preceding segment may already have entered
`Q_I`, `Q_J`, or another one of the fixed far-side subgraphs.  Nor is
merely taking the first vertex of `D` enough unless the prefix avoids those
fixed subgraphs.

If `R_s` is clean, replace

\[
       P_s\longmapsto P_s\cup V(R_s),
       \qquad D\longmapsto D-y.                       \tag{4.1}
\]

The enlarged `P_s` is connected, keeps all of its old adjacencies and is
disjoint from every other named subgraph.  Only the final vertex `y` is
removed from `D`; all other vertices of the prefix were already outside
`D`.  Consequently Theorem 2.1 applies without any hidden overlap.

### 4.2 Corollary to the cyclic incidence theorem

Assume that outcome 1 of Theorem 2.1 holds for a clean entry, so that the
residual `D-y` retains at least seven of the eight degree-eight neighbour
labels.  Form the bipartite nonadjacency graph between
`{P_0,P_1,P_2}` and `{C_0,...,C_4}` after (4.1).  Then each of the following
is a complete local incidence outcome in the sense already proved by the
cyclic incidence theorem.

1. If the nonadjacency graph is a matching of order at most two, `G`
   contains an explicit `K_7`-minor model.
2. If every nonadjacency is incident with `C_4` and `D-y` is adjacent to
   each of `P_0,P_1,P_2,C_0,C_1,C_2,C_3`, `G` contains an explicit
   `K_7`-minor model.  In particular, this applies when the only neighbour
   label (if any) lost at `y` belongs to `C_4`.
3. If `P_s` is anticomplete to some rooted set `C_i`, `0<=i<=3`, then the
   enlarged `P_s` meets the open shore through `R_s`.  The rooted-corner
   theorem therefore gives either an actual order-seven separation or a
   strict decrease in the order of a literal full-neighbourhood separator,
   retaining the named root `u_i` and the named missed subgraph `P_s`.

There is one small overlap between items 1--3 which is useful below.  In
normalized pattern `B` with `s=1`, item 3 applies if the enlarged `P_1`
remains anticomplete to `C_3`.  If the peel instead repairs `P_1C_3`, the
remaining nonadjacencies are contained in

\[
                         \{P_0C_0,P_0C_1\}.              \tag{4.2}
\]

Put `D'=D-y`, and let `O` be the possible unique member of
`{P_0,P_1,P_2,C_0,...,C_4}` not adjacent to `D'`.  The following seven-set
families are explicit `K_7`-minor models (the entry `O=none` means that no
named set is missed):

\[
\begin{array}{c|l}
O&\text{seven branch sets}\\
\hline
none,C_0,C_1,C_2&
 \{v\}\cup P_0,\ D',\ P_1,\ P_2,\
 C_0\cup C_1\cup C_2,\ C_3,\ C_4;\\
P_0&
 \{v\},\ D'\cup P_1,\ P_0,\ P_2,\
 C_0\cup C_1\cup C_2,\ C_3,\ C_4;\\
P_1,P_2&
 \{v\},\ D'\cup P_0,\ P_1,\ P_2,\
 C_0\cup C_1\cup C_2,\ C_3,\ C_4;\\
C_3&
 \{v\}\cup P_0,\ D',\ P_1,\ P_2,\
 C_0\cup C_1,\ C_2\cup C_3,\ C_4;\\
C_4&
 \{v\}\cup P_0,\ D',\ P_1,\ P_2,\
 C_0\cup C_1\cup C_4,\ C_2,\ C_3.
\end{array}                                               \tag{4.3}
\]

Every displayed union is connected.  The composite `C`-sets are three
pairwise adjacent cyclic arcs, while the only possible missing contacts
from `P_0` are to `C_0,C_1`; in (4.3) those contacts are supplied through
`v` or through `D'`.  This verifies the one pattern-`B` case not covered
directly by items 1--3.

Thus, in each normalized contact pattern, the clean singleton peel resolves
the local incidence alternative whenever its owner `P_s` is one of the
rows incident with a rooted missing adjacency.  In the notation of the four
normalized patterns this means

\[
\begin{array}{c|c}
 A& s=0,\\
 B& s\in\{0,1\},\\
 C& s\in\{0,1\},\\
 D& s=0.
\end{array}                                             \tag{4.4}
\]

The strict rooted-corner decrease in item 3 preserves the named root `u_i`
and the missed subgraph `P_s`, but it is not yet the label-preserving descent
required by the active `HC_7` proof spine: the other paired trace, the five
cyclic connected sets, the selected boundary-edge response and a common
boundary partition need not survive.  It therefore resolves this local
incidence subproblem without by itself closing the global branch.

The assertion is not that the boundary-edge Kempe theorem always selects
one of these owners.  Its three paths start at the vertex determined by
the obstructing boundary edge; in patterns `A` and `D`, for example, that
vertex may be `b_1` or `b_2` while every rooted incidence defect belongs to
`b_0`.

### 4.3 Exact live collision

There are two equivalent descriptions of the remaining label problem.

* The clean path belongs to a row `P_s` with no rooted missing incidence,
  while the row which owns the missing incidence has no clean path into the
  detachable part of the boundary-free subgraph.
* Before the selected Kempe path reaches `D`, its prefix first meets a
  different fixed far-side subgraph (`Q_I`, `Q_J`, or another singleton-
  trace row).  Absorbing that prefix into its source would overlap the hit
  row; absorbing it into the hit row would move the source trace or merge
  two named rows.

In either form, the off-pole edge response supplies a boundary matching of
order two or three and five bichromatic locks, but it does not identify a
palette colour with the owner of the rooted incidence.  This is the exact
contact-transfer statement still missing.

What is not yet automatic is the label required by the missing
boundary-to-sector incidence.  A singleton `y` is adjacent to the selected
`b`-subgraph, but need not be adjacent to whichever of the other two
boundary-rooted subgraphs owns the unresolved incidence.  Extending the
singleton to a connector inside the boundary-free subgraph destroys the
proof of (2.3): for a connected set `X`, the elementary bound becomes

\[
       N_G(D-X)\subseteq X\cup
          \bigl(S-\Lambda_D(X)\bigr),                 \tag{4.5}
\]

and its right side can have order greater than seven.  A completion
therefore needs one of the following precise extra facts:

1. the selected `b`-subgraph is itself the rooted subgraph in the
   unresolved missing incidence;
2. the first-entry vertex is also adjacent to that rooted subgraph; or
3. a proper-minor response moves the required contact to the singleton
   `y`, rather than merely supplying another unlabelled connector.

The atomic compulsory-portal results do not provide item 3 here.  They
require a connected boundary-full thin shore with a unique portal and an
opposite shore containing two disjoint boundary-full connected subgraphs;
none of those hypotheses follows from the present three-path setup.

There is also an important order distinction in the unique-portal input.
For a live boundary-full component behind an **order-seven** boundary,
two-connectivity and the audited unique-portal lemma imply
`Lambda_D(y)=emptyset` for every `y`: one unique boundary portal would
already return another actual order-seven separation.  For the present
degree-eight component, however, `|N(D)|` can be eight.  The same argument
only implies

\[
                         |\Lambda_D(y)|\le1             \tag{4.6}
\]

in a branch in which a new order-seven separation has been excluded.
Indeed two monopolized labels invoke Theorem 2.1(2), while one monopolized
label can leave an order-eight boundary.  Treating (4.6) as emptiness would
silently confuse the two interfaces.

## 5. Sharp local obstruction to replacing the singleton by a connector

The following finite graph shows that the singleton theorem cannot simply
be applied to a shortest connector from the selected `b`-subgraph to an
arbitrary second named subgraph.

Let

\[
 D=G[\{p,y_1,y_2,y_3\}]\cong K_4
\]

and let

\[
 S=\{b,i,a,t_1,t_2,t_3,t_4,t_5\}.
\]

Join `b` and `i` to each `y_k`; join `a` only to `p`; join `t_k` only to
`y_k` for `1<=k<=3`; and join each of `t_4,t_5` to all three vertices
`y_1,y_2,y_3`.  Add a vertex `v` adjacent precisely to all eight vertices
of `S`.  There are no other edges.  Then `D` is a three-connected component
of `G-N[v]`, it contacts all eight labels, and

\[
                    b y_k i\qquad(1\le k\le3)          \tag{5.1}
\]

are three `b`--`i` paths disjoint outside their terminals.  No vertex of
`D` contacts all eight labels.

Every connected subgraph `X subsetneq D` which is adjacent to both `b` and
`a` contains `p` and at least one `y_k`.  If it contains exactly `k` of the
three `y`-vertices, where `1<=k<=2`, then `D-X` is connected but contacts
exactly `7-k<=6` labels.  Moreover

\[
                         |N_G(D-X)|
                  =(1+k)+(7-k)=8.                     \tag{5.2}
\]

Thus no such connector leaves a seven-contact residual and none produces
a separator of order below eight.  The three first-entry vertices and
three-connectivity alone do not extend Theorem 2.1 from one vertex to a
connector.

This graph is only a sharpness example for that local geometric inference.
It is not seven-connected, is not asserted to be contraction-critical, and
is not a counterexample to `HC_7`.  It identifies exactly what a positive
first-entry theorem must add: a proper-minor response has to transfer the
second named contact to one first-entry vertex, or force compatible
colouring data at an order-seven boundary.  Path existence and internal
connectivity cannot perform that transfer.
