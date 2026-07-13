# State-forcing columns: the exact gammoid theorem and the warehouse obstruction

## 1. Colourful vertex columns

Let `H` be a graph, let `T` be a set of `m` target vertices, and let
`S_1,...,S_m` be nonempty sets disjoint from `T`.  A **colourful
`S`--`T` linkage** consists of `m` pairwise vertex-disjoint paths, with
one path starting in each `S_i` and with their other ends the `m`
distinct vertices of `T`.

For `X subseteq V(H)-T`, let

\[
 rho_T(X)=\max\{|mathcal P|:mathcal P\text{ is a family of disjoint
 paths from distinct vertices of }X\text{ to distinct vertices of }T\}.
                                                               \tag{1.1}
\]

### Theorem 1.1 (Rado--Perfect colourful linkage)

A colourful `S`--`T` linkage exists if and only if

\[
       rho_T\left(\bigcup_{i in I}S_i\right)\ge |I|
       \qquad\text{for every }I subseteq [m].                  \tag{1.2}
\]

If no colourful linkage exists, there is a nonempty `I subseteq[m]`
and a vertex set `Z` of order less than `|I|` meeting every path from
`union_{i in I}S_i` to `T`.

#### Proof

On the ground set `S=union_i S_i`, declare `X subseteq S` independent
when `X` can be linked by `|X|` disjoint paths to distinct vertices of
`T`.  These independent sets form the strict gammoid presented by
`H` with sink set `T`.  The exchange axiom is Perfect's linkage theorem;
equivalently it follows from the ordinary augmenting-path proof after
splitting every graph vertex into a capacity-one in/out pair.

Rado's matroidal transversal theorem says that this gammoid has an
independent transversal of `S_1,...,S_m` exactly when

\[
             r\left(\bigcup_{i in I}S_i\right)\ge |I|
             \quad(I subseteq[m]).
\]

Its rank is `rho_T`, proving the equivalence.  If (1.2) fails, choose
`I` with `rho_T(union_{i in I}S_i)<|I|`.  The vertex form of Menger's
theorem supplies a separator `Z` of order equal to this linkage number,
and hence less than `|I|`.  QED.

### Corollary 1.2 (four-connected colourful columns)

Let `m=4`, suppose `H` is four-connected, and assume

\[
             \left|\bigcup_{i in I}S_i\right|\ge |I|
             \qquad(I subseteq[4]).                             \tag{1.3}
\]

Then a colourful linkage to any four-vertex target set `T` disjoint from
the source sets exists.

#### Proof

If (1.2) failed for a nonempty `I`, Theorem 1.1 would give a separator
`Z` of order less than `|I|<=4`.  Condition (1.3) and `|T|=4` imply that
vertices of both `union_{i in I}S_i` and `T` survive outside `Z`; hence
`H-Z` is disconnected.  This contradicts four-connectivity.  QED.

In particular, four pairwise disjoint nonempty portal-vertex families
always have the required transversal linkage.  If `H=G-Q`, `|Q|=3`,
and the separator outcome of Theorem 1.1 occurs, then `Q union Z` is a
cut of `G` of order at most six, provided the two displayed sides are
nonempty.  Thus the vertex-family version has exactly the lift required
by seven-connectivity.

### Corollary 1.3 (named target families)

Let `T_1,...,T_m` be target families rather than fixed target vertices.
Adjoin a new protected terminal `tau_j` adjacent to every vertex of `T_j`,
and use `T^*={tau_1,...,tau_m}` as the sink set in Theorem 1.1.  A
colourful linkage to `T^*`, with the artificial last edges deleted, is
exactly a family of disjoint paths using one source family and one target
family each (in an arbitrary bijection).

Thus Theorem 1.1 remains exact for two-sided named portal families after
this leaf transformation.  A deficient-rank separator which avoids the
artificial leaves is an actual separator of `H`; one containing a leaf
records concentration in that target family and needs a separate
faithful-lift argument.  This is the target-side analogue of the
protected warehouse in the next section.

## 2. Protected state carriers

State forcing usually belongs not to one vertex but to a whole connected
extension which must stay in one eventual branch bag.  This changes the
capacity problem.

Let `C_1,...,C_m` be pairwise disjoint connected vertex sets, disjoint
from `T`.  A **protected column system** is a family of disjoint connected
sets `B_i` such that

\[
                    C_i subseteq B_i,
        \qquad |B_i cap T|=1,                                  \tag{2.1}
\]

and the `m` target vertices occurring in (2.1) are distinct.

Contract every `C_i` to a vertex `c_i`, obtaining `bar H`, and put
`C={c_1,...,c_m}`.

### Theorem 2.1 (exact protected-column dichotomy)

The following two statements are equivalent.

1. `H` has a protected column system.
2. `bar H` has `m` disjoint `C`--`T` paths.

If these fail, Menger gives a set `Z subseteq V(bar H)` of order at most
`m-1` meeting every `C`--`T` path.  Its full inverse image

\[
 Z^uparrow=(Z-C)\;union\!
           \bigcup_{c_i in Z}C_i                               \tag{2.2}
\]

separates the corresponding sides in `H`.  In particular:

* if `Z cap C=emptyset`, then `Z^uparrow=Z` is an actual separator of
  order at most `m-1` in `H`;
* if `Z` contains a contracted carrier vertex, its lift may be large.
  The carrier is a capacity-one **warehouse**, not a small graph
  separator.

#### Proof

Given (1), choose inside each connected `B_i/C_i` a path from `c_i` to
its target; the paths are disjoint.  Conversely, lift disjoint paths in
`bar H`: the path beginning at `c_i`, together with all of `C_i`, is a
connected bag, and different lifted bags are disjoint.  This proves the
equivalence.

If the linkage has order below `m`, Menger supplies `Z`.  Contraction
maps every path in `H-Z^uparrow` to a `C`--`T` path in `bar H-Z`, so
the full inverse image separates.  Formula (2.2) gives the two stated
cases.  QED.

For `m=4`, Theorem 2.1 is the exact form of the desired
column-or-three-cut statement.  The cut lifts with the neutral triangle
only when its Menger certificate avoids the contracted protected
carriers.  Four-connectivity of the uncontracted graph does not force
that avoidance.

## 3. A sharp four-connected target-free counterexample

### Proposition 3.1 (the warehouse obstruction)

There is a four-connected `K_7`-minor-free graph `H`, four disjoint
connected protected sets `C_1,...,C_4`, and four targets `T`, such that

1. the vertex-family linkage of Corollary 1.2 exists; but
2. no protected column system exists; and
3. the minimum obstruction after contracting the protected sets is one
   contracted carrier vertex, not a separator of order at most three in
   `H`.

#### Construction and proof

Let `W={w_1,w_2,w_3,w_4}` induce `K_4`.  Let

\[
              L={a_1,a_2,a_3},\qquad
              T={t_1,t_2,t_3,t_4}
\]

be independent and anticomplete to one another, and join every vertex
of `L union T` to every vertex of `W`.  Thus

\[
                         H=K_4 vee overline{K_7}.                \tag{3.1}
\]

Put

\[
              C_i={a_i}\quad(1<=i<=3),\qquad C_4=W.             \tag{3.2}
\]

The graph is four-connected: after any three vertex deletions at least
one vertex of `W` remains, and it is adjacent to every remaining vertex
outside `W`; the remaining part of `W` is a clique.  It is
`K_7`-minor-free.  Indeed it is chordal with maximal cliques
`W union {x}`, `x in L union T`, so it has treewidth four.  Since
treewidth is minor-monotone and `tw(K_6)=5`, it has no `K_6` minor, a
fortiori no `K_7` minor.

If only one representative of `C_4` must be retained, there are four
disjoint paths

\[
 a_iw_it_i\quad(1<=i<=3),\qquad w_4t_4.                         \tag{3.3}
\]

Thus ordinary Menger, and even the colourful gammoid theorem, sees full
rank four.

On the other hand, a protected bag containing `C_4` contains all of
`W`.  Every path from an `a_i` to any target meets `W`.  Hence none of
the other three protected bags can reach a target disjointly from the
`C_4` bag.  No protected column system exists.

After contracting `W` to `c_4`, the graph relevant to the sources and
targets is a star with centre `c_4`; the one-vertex Menger separator is
`{c_4}`.  Its inverse image is the four-vertex set `W`, exactly the
minimum cut of `H`.  There is no separator of order at most three in
`H`.  QED.

This example is not a counterexample to `HC_7`; it is a counterexample
to the proposed connectivity-only column-selection implication.  It is
already `K_7`-minor-free, so target-minor exclusion does not repair the
implication.

## 4. What vertex-criticality removes

The warehouse example deliberately uses false twins.  Vertex-criticality
forbids this exact static lock.

### Lemma 4.1 (critical anti-domination)

In a vertex-critical graph, if `u,v` are distinct nonadjacent vertices,
then neither `N(u) subseteq N(v)` nor `N(v) subseteq N(u)` holds.
Consequently there are private distinguishing neighbours

\[
                 x in N(u)-N(v),\qquad
                 y in N(v)-N(u).                               \tag{4.1}
\]

#### Proof

Suppose `N(u) subseteq N(v)`.  Colour `G-u` with one fewer colour than
`G`, which is possible by vertex-criticality.  Give `u` the colour of
`v`.  Since `u,v` are nonadjacent and every neighbour of `u` is a
neighbour of `v`, this remains proper, contradicting the chromatic
number of `G`.  The other containment is symmetric.  QED.

In (3.1), all vertices outside `W` have the same neighbourhood `W`, so
Lemma 4.1 excludes the construction inside a critical host.  More
generally, when a contracted state carrier occurs in every small
Menger certificate, Lemma 4.1 forces private contacts distinguishing
locally parallel portal vertices.  To finish the near-`K_7` application
one must show that these private contacts either bypass the warehouse in
the protected-column gammoid or create the labelled rooted model.  That
last implication uses contraction-critical state data; it does not
follow from four-connectivity or `K_7`-minor exclusion alone.
