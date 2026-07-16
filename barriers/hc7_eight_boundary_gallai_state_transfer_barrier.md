# Gallai--Edmonds data and two named edge transitions do not align boundary colourings

**Status:** written barrier proof.  This is not a counterexample to
Hadwiger's Conjecture.  The constructed graph is not asserted to be
`K_7`-minor-free or strongly contraction-critical.

This note tests the weakest state-transfer proposal suggested by the
canonical Gallai--Edmonds barrier on an eight-vertex boundary.  It shows
that the full canonical decomposition, two named boundary edges, exact
one- and two-edge deletion/contraction responses, seven-connectivity, and
the target-free two-shore quotient still do not force a common proper
boundary colouring.  A positive theorem must additionally use global
`K_7`-minor exclusion, proper-minor transitions beyond the two named
edges, or the specified minor-model branch sets.

## 1. Statement

There is a finite graph `G` with a separation

\[
             V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R
\]

and two vertex-disjoint edges `e,f` of `G[S]` such that:

1. `|S|=8`, the open shores `L,R` are nonempty and connected, there is no
   `L`--`R` edge, and every vertex of `S` has a neighbour in each shore;
2. `G` is seven-connected and `chi(G)=7`;
3. writing `J=G[S]`, one has `J=K_{3,5}` and
   `I_2\vee J=K_{2,3,5}` has no `K_7` minor;
4. for `F=\overline J`, the Gallai--Edmonds decomposition is

   \[
                         D=S,\qquad A=C=\varnothing;
   \]

5. each of

   \[
       G-e,\quad G-f,\quad G-\{e,f\},\quad
       G/e,\quad G/f,\quad G/e/f
   \]

   is six-colourable; and
6. nevertheless, no equality partition of `S` induced by a proper
   six-colouring extends through both closed shores while retaining all
   edges of `J`.

Both shores may additionally be required to admit, for every nonempty
independent set `X` of `J`, a six-colouring in which `X` is exactly one
boundary colour class.

## 2. Two disjoint boundary extension languages

Write the parts of `J=K_{3,5}` as

\[
 U=\{u_1,u_2,u_3\},\qquad
 W=\{w_1,w_2,w_3,w_4,w_5\},
\]

and choose the disjoint named edges

\[
                         e=u_1w_1,qquad f=u_2w_2.       \tag{2.1}
\]

Let `Omega_6(J)` be the equality partitions of `S` into at most six
independent sets of `J`.  Split it into

\[
 \mathcal E=\{\Pi\in\Omega_6(J):|\Pi|\text{ is even}\},\qquad
 \mathcal O=\{\Pi\in\Omega_6(J):|\Pi|\text{ is odd}\}. \tag{2.2}
\]

These two families are disjoint.  Define three further partitions:

\[
\begin{aligned}
 \Pi_e={}&
 \{u_1,w_1\}\mid\{u_2,u_3\}\mid\{w_2,w_3,w_4,w_5\},\\
 \Pi_f={}&
 \{u_2,w_2\}\mid\{u_1,u_3\}\mid\{w_1,w_3,w_4,w_5\},\\
 \Pi_{ef}={}&
 \{u_1,w_1\}\mid\{u_2,w_2\}\mid\{u_3\}
                  \mid\{w_3,w_4,w_5\}.
                                                               \tag{2.3}
\end{aligned}
\]

The first is proper on `J-e`, the second on `J-f`, and the third on
`J-{e,f}`.  Set

\[
 \mathcal R_L=\mathcal E\cup\{\Pi_e,\Pi_f,\Pi_{ef}\},\qquad
 \mathcal R_R=\mathcal O\cup\{\Pi_e,\Pi_f,\Pi_{ef}\}. \tag{2.4}
\]

For each family in (2.4), take all labelled six-colourings whose equality
partition belongs to that family.  The resulting sets of colourings are
closed under permutation of the six colours.  The exact colouring-relation
realization theorem of Dvorak--Swart therefore gives two finite
`S`-boundaried graphs whose exact boundary extension relations are
`\mathcal R_L` and `\mathcal R_R`, respectively.

Apply the connected-full augmentation from
[`hc7_state_realization_barrier.md`](hc7_state_realization_barrier.md) to
each side.  It preserves the exact extension relation, makes each open
interior connected, and gives every boundary vertex a neighbour in that
interior.  Glue the two realizers along their common labelled boundary and
add every edge of `J` on `S`.

Neither realizer already contains the boundary edge `e` or `f`: the
extension relation of each contains a partition equating the ends of each
named edge, which would be impossible if that edge were present.  Thus the
subsequent deletion of `e` or `f` really removes the corresponding added
boundary constraint.

Adding `J` filters the left extension relation to `\mathcal E` and the
right relation to `\mathcal O`: each partition in (2.2) is proper on `J`,
whereas every partition in (2.3) equates the ends of `e` or `f`.
Consequently the two closed shores have no common proper boundary state,
so the glued graph is not six-colourable.

## 3. The named proper-minor responses all exist

Deleting `e` from the glued graph makes `\Pi_e` proper on the boundary,
and that partition belongs to both relations in (2.4).  The two shore
colourings therefore glue to a six-colouring of `G-e`.  Similarly,
`\Pi_f` six-colours `G-f`, and `\Pi_{ef}` six-colours `G-{e,f}`.

In the colouring associated with `\Pi_e`, the ends of `e` have the same
colour.  It consequently descends to a six-colouring of `G/e`.  The
symmetric assertion holds for `G/f`, and `\Pi_{ef}` descends through both
contractions to six-colour `G/e/f`.  Thus every graph listed in item 5 of
Section 1 is genuinely six-colourable.

Since `G-e` is six-colourable, adding the edge `e` and assigning one end a
fresh colour gives `chi(G)<=7`.  The absence of a common six-colour state
gives `chi(G)>6`; hence `chi(G)=7`.

The augmentation can be followed by the false-twin amplification proved
in Theorem 3.1 of the cited realization barrier.  Use twin classes of
order seven.  The two extension relations remain unchanged and the glued
graph becomes seven-connected.  Adding the boundary edges of `J` cannot
lower connectivity.  This establishes items 1, 2, 5, and 6 simultaneously.

## 4. Exact independent-block responses

Let `X` be a nonempty independent set of `J`; it lies wholly in `U` or
wholly in `W`.

If `X subseteq U`, use `X` as one block, use `U-X` as one block when it is
nonempty, and use all of `W` as one block.  Splitting the nonempty
five-set `W` into two blocks changes the parity of the number of blocks.
Thus both `\mathcal E` and `\mathcal O` contain a partition in which `X`
is exactly one block.  If `X subseteq W`, the same argument splits the
three-set `U`.  Every displayed partition has at most four blocks.

Hence both closed shores answer every exact independent-block query even
though their complete proper extension languages are disjoint.

## 5. Gallai--Edmonds decomposition and quotient exclusion

The complement of `J=K_{3,5}` is

\[
                         F=K_3\mathbin{\dot\cup}K_5.   \tag{5.1}
\]

Every vertex of either odd clique is missed by some maximum matching, so
`D=S` and `A=C=\varnothing`.  This is the full canonical decomposition,
not merely a noncanonical Tutte witness.

Contracting each open shore to one vertex gives the quotient

\[
                         I_2\vee J=K_{2,3,5}.          \tag{5.2}
\]

It has a tree decomposition of width five: take the five vertices outside
the largest part in every bag and add one vertex of the largest part to
each bag.  Therefore (5.2) has no `K_7` minor.

## 6. Exact scope

The construction proves that none of the following static data, even in
combination, aligns the two shore languages:

- the full canonical Gallai--Edmonds decomposition `(D,A,C)`;
- a target-free contracted two-shore quotient;
- two named disjoint boundary edges;
- exact one-edge and double-edge deletion/contraction colourings;
- exact independent-block responses on both sides;
- connected full shores; and
- seven-connectivity and exact chromatic number seven.

The constructed host is **not** asserted to be `K_7`-minor-free, and not
every proper minor is asserted to be six-colourable.  Proving both of
those properties would produce a counterexample to `HC_7`, so they cannot
be discarded as technical details.  In the actual support-six residue,
the next positive theorem must use at least one of:

1. global `K_7`-minor exclusion inside the uncontracted shores;
2. colouring transitions for internal shore operations supplied by full
   contraction-criticality; or
3. the four specified singleton branch sets belonging to each named
   six-vertex `K_5` model.

Gallai--Edmonds theory remains a useful canonical boundary descriptor,
but it supplies no state-transfer mechanism on its own.

## 7. Trust boundary

The only non-elementary input is the exact colouring-relation realization
theorem of Dvorak--Swart, together with the elementary connected-full and
false-twin augmentations already proved in the cited repository barrier.
No finite search or unbounded computational inference is used here.
