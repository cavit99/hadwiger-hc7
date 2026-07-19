# A two--three linkage reduction for three boundary portal sets

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_three_portal_two_three_reduction_audit.md`](hc7_order8_three_portal_two_three_reduction_audit.md).
This is an unbounded structural reduction for one connected component
behind an order-eight boundary.  It does not prove `HC_7` and does not turn
the separation it returns into compatible closed-shore colourings.

## 1. Setting

Let `G` be a seven-connected graph, let `S` be a set of eight vertices, and
let `Q` be a component of `G-S`.  Assume that `G-S` has a component other
than `Q` and that

\[
                              N_G(Q)=S.                 \tag{1.1}
\]

Fix five distinct boundary vertices

\[
                         d,e,x_1,x_2,x_3\in S.          \tag{1.2}
\]

For `s in S`, write

\[
                         P_s=N_G(s)\cap V(Q).           \tag{1.3}
\]

All five displayed portal sets are nonempty by (1.1).  A **three-portal
packing** in `Q` is a pair of vertex-disjoint connected subgraphs `D,T`
such that

1. `D` contains a nontrivial path with one end in `P_d` and the other in
   `P_e`; and
2. `T` meets each of `P_{x_1},P_{x_2},P_{x_3}`.

This is exactly the positive configuration required by Corollary 2.2 of
the reserved-path boundary-response theorem when
`X={x_1,x_2,x_3}`.

## 2. The five-terminal completion

For five distinct vertices

\[
                  a_i\in P_{x_i}\quad(i=1,2,3),
                  \qquad b_d\in P_d,\quad b_e\in P_e, \tag{2.1}
\]

let `H^+` be the graph obtained from `G[Q]` by adding the seven possible
virtual edges

\[
                  b_db_e,\qquad a_i b_d,\ a_i b_e
                              \quad(i=1,2,3).           \tag{2.2}
\]

The edges in (2.2) are used only to test connectivity.  They are never
treated as edges of `G`.

### Theorem 2.1 (portal packing or a confined lobe)

At least one of the following holds.

1. `Q` contains a three-portal packing.
2. `G` has an actual separation of order seven.
3. `|V(Q)|<=6`.
4. The five displayed portal sets have distinct representatives as in
   (2.1), and the corresponding completion `H^+` has a separation of
   order at most five.  More precisely, there are a set

   \[
                              K\subseteq V(Q),
                         \qquad |K|\le5,               \tag{2.3}
   \]

   and a nonempty connected proper set `C subsetneq V(Q)` such that

   \[
                      N_{G[Q]}(C)\subseteq K,
       \qquad N_G(C)=N_{G[Q]}(C)\mathbin{\dot\cup}(N_G(C)\cap S). \tag{2.4}
   \]

   The set `N_G(C)` is the boundary of an actual separation.  If outcome 2
   does not hold, then

   \[
                          |N_G(C)|\ge8.                 \tag{2.5}
   \]

   The completed-graph separation can be chosen with one of the following
   two terminal forms:

   - `C` contains none of the five nominated vertices in (2.1); or
   - `b_d,b_e` belong to `K`, and nominated vertices from
     `{a_1,a_2,a_3}-K` occur in components on both sides of `K`.

#### Proof

First consider the five portal sets indexed by

\[
                 I_0=\{d,e,x_1,x_2,x_3\}.             \tag{2.6}
\]

Suppose they have no system of distinct representatives.  Hall's theorem
gives a nonempty set \(I\subseteq I_0\) such that, on putting

\[
                         Z=\bigcup_{s\in I}P_s,
\]

one has

\[
                            |Z|\le |I|-1.              \tag{2.7}

\]

If `Q-Z` is nonempty, let `C` be any component of `Q-Z`.  A boundary
vertex indexed by `I` has no neighbour in `C`, while every neighbour of
`C` inside `Q` belongs to `Z`.  Consequently

\[
             N_G(C)\subseteq Z\cup(S-I),
       \qquad |N_G(C)|\le(|I|-1)+(8-|I|)=7.            \tag{2.8}

\]

The set on the left is a genuine separator: `C` is nonempty, and a
component of `G-S` different from `Q` lies outside
\(C\cup N_G(C)\).
Seven-connectivity forces equality in (2.8), so outcome 2 holds.

If `Q-Z` is empty, then

\[
                         |V(Q)|=|Z|\le |I|-1\le4,      \tag{2.9}

\]

and outcome 3 holds.  We may therefore assume that the five distinct
representatives in (2.1) exist.

Suppose `H^+` is six-connected.  Apply Xie's two--three linkage theorem to
the terminal triple `{a_1,a_2,a_3}` and the terminal pair `{b_d,b_e}`.
It gives vertex-disjoint connected subgraphs `T,D` of the original graph
`G[Q]` such that

\[
                \{a_1,a_2,a_3\}\subseteq V(T),
             \qquad \{b_d,b_e\}\subseteq V(D).        \tag{2.10}

\]

The connected graph `D` contains a `b_d`--`b_e` path.  Its ends are
distinct, so this path is nontrivial.  Thus `D,T` form a three-portal
packing and outcome 1 holds.

Assume next that `H^+` is not six-connected.  If `|V(Q)|<=6`, outcome 3
holds.  Otherwise a separation of `H^+` has a separator `K` of order at
most five and two nonempty open sides.

We recall the elementary shape of this separation.  If both open sides
contain nominated terminals, neither `b_d` nor `b_e` can survive outside
`K`.  Indeed, the virtual edge `b_db_e` and all six virtual edges between
the pair and the triple would then place every surviving nominated terminal
on the same open side.  Hence

\[
                            b_d,b_e\in K,               \tag{2.11}

\]

and surviving members of `{a_1,a_2,a_3}` occur on both open sides.  If
only one open side contains nominated terminals, the other is
terminal-free.

In the latter case take a component `C` of the terminal-free open side.  In
the former case take a component containing a surviving `a_i` on either
open side.  In both cases `C` is a nonempty connected proper subset of
`Q`.  No original edge of `G[Q]` joins `C` to
\(Q-(C\cup K)\), so

\[
                            N_{G[Q]}(C)\subseteq K.     \tag{2.12}

\]

As `Q` is a component of `G-S`, all remaining neighbours of `C` lie in
`S`, proving (2.4).  A vertex in the other open side and the component of
`G-S` different from `Q` show that `N_G(C)` is an actual separation
boundary.  Seven-connectivity gives `|N_G(C)|>=7`; equality is outcome 2,
and otherwise (2.5) holds.  The terminal description follows from the
choice of `C` and (2.11).  This proves the theorem. \(\square\)

## 3. The minimum-positive-excess consequence

The preceding theorem becomes sharper in the minor-minimal `HC_7` setting.

### Corollary 3.1 (positive-excess five-cut residue)

In addition to the hypotheses of Theorem 2.1, assume

\[
 \chi(G)=7,\qquad K_7\not\preccurlyeq G,
 \qquad \chi(M)\le6\text{ for every proper minor }M\text{ of }G. \tag{3.1}

\]

Suppose that there is no three-portal packing, no actual order-seven
separation, `|V(Q)|>=7`, and no strict order-eight lobe descent supplied by
the small-boundary lobe theorem.  Then outcome 4 of Theorem 2.1 gives `K,C`
such that

\[
             |K|\le5,\qquad N_{G[Q]}(C)\subseteq K,
             \qquad |N_G(C)|\ge9.                     \tag{3.2}

\]

In particular,

\[
                   |N_G(C)\cap S|
                       \ge 9-|N_{G[Q]}(C)|
                       \ge 9-|K|.                     \tag{3.3}

\]

Thus the unsolved case is a connected lobe behind at most five internal
vertices which has positive boundary excess: it meets at least
`9-|K|` of the eight literal boundary vertices.  Its completed-separation
terminal form is one of the two forms in Theorem 2.1.

Moreover, for every edge `uv` with `u in C` and `v in N_G(C)`, every
proper six-colouring of `G-uv` assigns the same colour to `u` and `v`.

#### Proof

Theorem 2.1 supplies `K,C`.  If `|N_G(C)|=8`, the hypotheses of the
small-boundary lobe theorem hold for the proper connected subset `C` of
`Q`, because

\[
       |N_{G[Q]}(C)|+|N_G(C)\cap S|=|N_G(C)|=8.        \tag{3.4}

\]

That theorem returns an order-seven separation or a strict order-eight
descent, both excluded here.  Equation (2.5) and integrality therefore give
`|N_G(C)|>=9`, and (3.3) follows from (2.4).

Finally `G-uv` is a proper minor and hence has a proper six-colouring.  If
one such colouring gave `u,v` different colours, restoring `uv` would
six-colour `G`, contrary to (3.1). \(\square\)

## 4. Exact remaining target and trust boundary

The theorem converts the three-portal problem into a standard
two--three-linkage test and, on failure, into one confined positive-excess
lobe.  It also handles every failure of five distinct portal representatives
except a component of order at most four.

It does **not** eliminate the small component in outcome 3.  It does not
show that a positive-excess lobe creates a `K_7` minor, and it does not turn
the equal-endpoint edge responses in Corollary 3.1 into five prescribed
branch-set contacts.  Most importantly, an order-seven separation returned
above is structural only: no complete equality partition has yet been
shown to extend through both intact closed shores.

Accordingly the next strictly smaller target is the following.  In the
opposite-response setting, use the selected proper-minor colouring response
to prove that a positive-excess lobe satisfying (3.2)--(3.3) either

1. supplies a three-portal packing;
2. gives an explicit `K_7`-minor model; or
3. exposes an order-seven boundary with one complete equality partition
   extending through both closed shores.

This target includes the terminal shape of Theorem 2.1 and the literal
equal-endpoint responses; it is strictly more structured than the original
arbitrary connected component `Q`.

## 5. External and internal inputs

- Shijie Xie, *6-Connected Graphs Are Two-Three Linked*, PhD dissertation,
  Georgia Institute of Technology (2019), Theorem 1.2.1: the five-terminal
  completion in (2.2) being six-connected yields the two disjoint connected
  subgraphs in (2.10).
- the small-boundary lobe descent, only for Corollary 3.1;
- Hall's theorem and elementary separation facts.
