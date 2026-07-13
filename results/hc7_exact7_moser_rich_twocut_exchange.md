# Pure-Moser two-component low-cut exchange

**Status:** GREEN computer-assisted theorem, independently audited.  The
only finite input is the exact ten-vertex quotient enumeration in
`../archive/moser_global_2cut_verify.py`; the two exceptional quotient
states are eliminated symbolically below.

## 1. Setting and honest scope

Let `G` be a seven-connected, `K_7`-minor-free graph which is
proper-minor-minimal subject to not being six-colourable.  Thus every proper
minor of `G` is six-colourable.  Let `v` have degree seven, put

\[
                         S=N_G(v),
\]

and suppose that `H=G[S]` is the standard Moser spindle

\[
 E(H)=\{01,02,03,04,12,16,26,34,35,45,56\}.             \tag{1.1}
\]

Assume that

\[
                         G-N[v]=C_1\mathbin{\dot\cup}C_2                 \tag{1.2}
\]

has exactly two components.  This is the pure-Moser two-component cell.

### Theorem 1.1 (low-cut closure)

Neither `C_1` nor `C_2` has a cutvertex or a two-vertex cut.  Consequently,
each `C_i` of order at least four is three-connected.

The theorem applies in particular when (1.2) is the two-component branch of
the current exact-seven `(1,2)` packet setting.  The packet maxima are not
used: the statement is stronger locally and holds before one decides which
component is packet-thin or packet-rich.

It does **not** eliminate components of order one, two, or three, and it does
not treat an arbitrary exact `(1,2)` adhesion whose rich open shore itself
has two components.  Its scope is exactly (1.2).

## 2. Full attachment and the cutvertex case

Every `C_i` is `S`-full.  Indeed, if some `s in S` had no neighbour in
`C_i`, then `N_G(C_i) subseteq S-{s}` would be a separator of order at most
six; the other exterior component and `v` remain on the opposite side.

Suppose first that `z` is a cutvertex of `C_1`.  Let `D` be a component of
`C_1-z` and put `E=C_1-D`.  Then `D,E` are disjoint connected sets joined by
an edge.  Since

\[
                         N_G(D)\subseteq S\cup\{z\},
\]

seven-connectivity gives `|N_S(D)|>=6`.  Applying the same argument to a
second component of `C_1-z`, contained in `E`, gives `|N_S(E)|>=6`.  The
possible singleton boundary defects of `D,E` are distinct when both exist,
because their union is the `S`-full component `C_1`.

The four boundary triangles are

\[
                    012,\qquad034,\qquad126,\qquad345.                  \tag{2.1}
\]

For every ordered pair of distinct-or-empty singleton defects, one of these
triangles `T` and three distinct anchors `a_D,a_E,a_2 in S-T` satisfy:

* `D` contacts `a_D` and `E` contacts `a_E`;
* if the defect of `D` lies in `T`, then it is adjacent in `H` to `a_D`;
* if the defect of `E` lies in `T`, then it is adjacent in `H` to `a_E`.

This 57-case literal assertion is checked by
`../archive/moser_global_cutvertex_verify.py`.  The six sets

\[
 \{t\}\ (t\in T),\qquad D\cup\{a_D\},\qquad
 E\cup\{a_E\},\qquad C_2\cup\{a_2\}                    \tag{2.2}
\]

are then connected, disjoint, pairwise adjacent, and all meet `S`.  They
form an `S`-meeting `K_6` model in `G-v`; adjoining `{v}` gives a literal
`K_7` model.  Hence neither exterior component has a cutvertex.

## 3. Splitting an arbitrary two-cut

Suppose now that `Z={z_1,z_2}` is a two-cut of `C_1`.  By Section 2,
`C_1` has no cutvertex.  Every component of `C_1-Z` therefore has a neighbour
at both `z_1` and `z_2`: otherwise one of the two cut vertices alone would
disconnect it from the rest of `C_1`.

Choose a component `D` of `C_1-Z` and put

\[
                         A=D\cup\{z_1\},\qquad B=C_1-A.                 \tag{3.1}
\]

Then `A,B` are nonempty, disjoint, connected, and adjacent.  Connectivity
of `B` follows because it contains `z_2` and every other component of
`C_1-Z` meets `z_2`; adjacency follows from a `D-z_2` edge.

The set `N_G(D)` is contained in `S union Z`.  Another component of
`C_1-Z` remains beyond this neighbourhood, so seven-connectivity gives

\[
                         |N_S(D)|\ge5.
\]

Thus `A` has boundary defect of order at most two.  Applying the same
argument to any second component of `C_1-Z`, which lies in `B`, gives the
same conclusion for `B`.  Write

\[
                  Delta_A=S-N_S(A),\qquad Delta_B=S-N_S(B).            \tag{3.2}
\]

Since `A union B=C_1` is `S`-full,

\[
                    |\Delta_A|,|\Delta_B|\le2,
                    \qquad \Delta_A\cap\Delta_B=\varnothing.           \tag{3.3}
\]

This construction works unchanged when a component behind the cut is a
single vertex or when there are more than two components behind the cut.

## 4. Exact quotient theorem

Contract `A,B,C_2` to vertices `a,b,c`.  Retain the `ab` edge, all exact
boundary contacts prescribed by (3.2), and the Moser graph (1.1).  There
are no `ac` or `bc` edges because `C_1,C_2` are distinct components of
`G-N[v]`.

### Lemma 4.1 (ten-vertex quotient atlas)

For disjoint subsets `Delta_A,Delta_B subseteq S` of order at most two, the
ten-vertex quotient contains an `S`-meeting `K_6` model except for the two
unordered defect pairs

\[
                  \{13,24\},\qquad \{14,23\}.                           \tag{4.1}
\]

#### Finite certificate

There are 29 possible defect sets of order at most two and 260 unordered
disjoint pairs.  The dependency-free verifier
`../archive/moser_global_2cut_verify.py` enumerates, for every pair:

1. every used subset of the ten quotient vertices of order six through ten;
2. every canonical partition of that subset into six nonempty bags;
3. connectivity of every bag;
4. all fifteen bag adjacencies; and
5. literal intersection of every bag with `S`.

It finds a model for 258 pairs and asserts that (4.1) is the exact failure
list.  Replacing quotient vertices by `A,B,C_2` lifts every listed model:
bag disjointness, connectivity, all adjacencies, and literal `S`-meeting are
preserved.  Adding `{v}` therefore gives `K_7`.

It remains only to eliminate the two pairs in (4.1).

## 5. Complementary-defect state exchange

Orient the split shores so that `A` has exact defect `r` and `B` has exact
defect `e`, where

\[
                    (r,e)=(13,24)\quad\hbox{or}\quad(14,23).             \tag{5.1}
\]

In both cases `r,e` are disjoint independent pairs and

\[
 S-(r\cup e)=\{0,5,6\},\qquad 56\in E(H),\qquad05,06\notin E(H).        \tag{5.2}
\]

Put

\[
                         X=G[S\cup C_1],\qquad Y=G[S\cup C_2].
\]

### 5.1 A state returned on `X`

In `G`, contract the two disjoint connected sets

\[
                         \{v\}\cup r,
                         \qquad C_2\cup e.                              \tag{5.3}
\]

They are adjacent through the `v-e` edges.  The resulting graph is a proper
minor and hence has a six-colouring.  Delete the connector vertices `v` and
`C_2`, and expand only the independent literal pairs `r,e`.  This gives a
proper six-colouring of `X` in which `r` and `e` are distinct monochromatic
blocks.

The two contracted representatives were each adjacent to `0,5,6`, while
`5` and `6` are adjacent.  Therefore the **exact** equality partition on
`S` is one of

\[
 R_0=\{r,e,\{0\},\{5\},\{6\}\},\quad
 R_5=\{r,e,\{0,5\},\{6\}\},\quad
 R_6=\{r,e,\{0,6\},\{5\}\}.                           \tag{5.4}
\]

### 5.2 Every possible returned state is available on `Y`

Because the exact defects of `A,B` are `r,e`, respectively, the sets

\[
                          A\cup e,
                          \qquad B\cup r                                  \tag{5.5}
\]

are disjoint, connected, and adjacent.  For

\[
 I_0=\{0\},\qquad I_5=\{0,5\},\qquad I_6=\{0,6\},
\]

contract in turn

\[
                        A\cup e,\qquad B\cup r,
                        \qquad \{v\}\cup I_q.                           \tag{5.6}
\]

All three sets are disjoint and connected; their representatives are
pairwise adjacent.  When `q=0`, these representatives together with the
literal vertices `5,6` form a `K_5`.  When `q=5`, they and literal `6` form
a `K_4`; when `q=6`, they and literal `5` form a `K_4`.  The facts used are
exactly: both split shores contact `5,6`, the star representative sees them
through `v`, and `56` is an edge.

Each graph in (5.6) is a proper minor and has a six-colouring.  Delete
`A,B,v` and expand only the independent literal blocks.  The representative
clique forces the exact state `R_q` on `Y`.  Thus all three states in (5.4)
are available on `Y`.

### 5.3 Palette alignment and gluing

Choose on `Y` the state actually returned on `X`.  Equality of the exact
partitions permits a permutation of the six colours making the two
colourings agree on every literal vertex of `S`.  Since `C_1,C_2` are
anticomplete, the colourings glue to a six-colouring of `G-v`.

Only five boundary blocks occur in `R_0` and four in `R_5,R_6`; hence some
colour is absent from `S`.  Assign it to `v`.  Since `N(v)=S`, this is a
proper six-colouring of `G`, a contradiction.

The two quotient exceptions are impossible.  Lemma 4.1 and the cutvertex
argument prove Theorem 1.1. `square`

## 6. Exact contribution to the current proof spine

Inside the pure-Moser two-component branch of an actual exact `(1,2)`
adhesion, every surviving exterior component of order at least four is
three-connected.  This eliminates an infinite family of internal shore
geometries and closes the old 33 selected-trace two-cut configurations at
once.

The theorem does not extract the missing third partial carrier from a
three-connected shore, does not treat the singleton thin Moser shore, and
does not close the full `(1,2)` cell.
