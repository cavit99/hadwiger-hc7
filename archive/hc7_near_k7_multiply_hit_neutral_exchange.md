# Multiply-hit neutral rows: a sacrificial split or one rooted torso

## Status

This note combines the both-missing neutral separator with the normalized
second path.  It does **not** close the both-missing branch.  It proves two
uniform facts which remove the arbitrary internal neutral bag from the next
step.

1. A suitable pair of disjoint rooted carriers inside a multiply-hit neutral
   bag gives a literal `K_7` model by sacrificing that neutral row.
   If the carriers do not exist, every carrier of one of the two exact roles
   is concentrated in one bag of any tree decomposition.  In a Tutte
   decomposition the whole failure is therefore one gate, cycle torso, or
   3-connected torso, with every off-torso lobe missing a named literal row.
2. The `2+(at most 1)+2` portal structure of the minimized twin path forces a
   sharp load dichotomy.  Either some multiply-hit neutral row is locked to
   one actual endpoint of the twin path, or the sole mobile neutral row
   contains at least four vertices of the ambient separator and each of the
   other three neutral rows contains exactly one.

Thus the multiply-hit conclusion is not merely another portal count.  The
remaining geometry is one of two rooted torso cells: a two-portal neutral
society with one fixed external twin root, or a four-portal neutral society
carrying the unique mobile twin row.

## 1. The exact sacrificial-row split

Let

\[
                 B,C,R_1,R_2,R_3,U                         \tag{1.1}
\]

be pairwise disjoint connected pairwise adjacent bags.  Let `X` be a
connected set disjoint from them such that

\[
 E(X,B\cup C)=\varnothing,
 \qquad E(X,R_i)\ne\varnothing\ (1\le i\le3),
 \qquad E(X,U)\ne\varnothing .                            \tag{1.2}
\]

For `Y in {X,B,C,R_1,R_2,R_3}`, put

\[
                 P_Y=N_U(Y).                               \tag{1.3}
\]

All six portal sets are nonempty.  Call a connected subgraph of `G[U]`

* an **entry carrier** if it meets `P_X,P_B,P_C`; and
* a **retained carrier** if it meets
  `P_B,P_C,P_{R_1},P_{R_2},P_{R_3}`.

### Theorem 1.1 (sacrificial neutral-row completion)

If `G[U]` contains vertex-disjoint entry and retained carriers, then `G`
contains a `K_7` minor.

#### Proof

Let `L,R` be disjoint carriers of the two types.  If they are not adjacent,
take a shortest `L`--`R` path in connected `G[U]` and add its internal
vertices to `L`.  Contract `L` and `R`, extend an edge between their images
to a spanning tree, and delete that tree edge.  Lifting the two tree
components gives a bipartition

\[
                         U=U_L\mathbin{\dot\cup}U_R          \tag{1.4}
\]

into nonempty connected adjacent sets containing `L,R`, respectively.

Use the seven branch sets

\[
       X\cup U_L,\quad U_R,\quad B,\quad C,\quad
       R_1,\quad R_2,\quad R_3.                             \tag{1.5}
\]

The first set is connected through the `P_X` contact of `L`.  It sees
`B,C` through `L` and sees every `R_i` through the old edges from `X`.
The set `U_R` sees all five retained foreign rows through `R`.  The first
two sets are adjacent by (1.4), and the five unchanged foreign rows are
pairwise adjacent by hypothesis.  Hence (1.5) is a `K_7` model.  \(\square\)

The asymmetry in the two carrier types is exact.  The entry shore does not
need internal `U-R_i` contacts because the connected envelope `X` already
supplies them.  The residual shore must retain all five foreign-row duties.

## 2. Failure is one rooted torso

### Theorem 2.1 (entry/retained bi-Helly core)

Let `(T,(V_t)_{t\in V(T)})` be any tree decomposition of `G[U]`.  At least
one of the following holds.

1. `G` contains a `K_7` minor by Theorem 1.1.
2. Some node `z` has the property that every entry carrier meets `V_z`.
3. Some node `z` has the property that every retained carrier meets `V_z`.

If the decomposition has adhesion at most `k`, then in outcome 2 or 3 every
component of `G[U]-V_z` misses at least one named portal set required by
the concentrated carrier type and has at most `k` neighbours in `V_z`.

#### Proof

Take the finite families of inclusion-minimal entry and retained carriers.
If a cross-pair is disjoint, Theorem 1.1 applies.  Otherwise every entry
carrier meets every retained carrier.

For a connected subgraph `K`, the set of decomposition nodes whose bags
meet `K` is a subtree of `T`.  If the trace subtrees of the entry carriers
are pairwise intersecting, subtree Helly gives one node common to all of
them.  If two entry traces are disjoint, every retained trace meets both
and therefore contains the path between them; any node of that path is
common to all retained traces.  This proves outcomes 2 and 3.  Every
nonminimal carrier contains a minimal one, so the conclusion holds for all
carriers.

A component outside the common bag cannot meet all named portal sets of
the concentrated type, since it would itself contain such a carrier
avoiding the bag.  The running-intersection property puts all of its
neighbours in the common bag into the first adhesion toward that component,
which has order at most `k`.  \(\square\)

### Corollary 2.2 (one rooted neutral torso)

Use the Tutte decomposition of `G[U]`.  In a `K_7`-minor-free host, one
gate of order at most two, one cycle torso, or one 3-connected torso meets
every carrier of one exact role.  Every off-torso lobe has an adhesion of
order at most two and misses a named member of

\[
       \{X,B,C\}
       \quad\hbox{or}\quad
       \{B,C,R_1,R_2,R_3\},                                \tag{2.1}
\]

according to the concentrated role.

Virtual torso edges in this conclusion are not literal host edges.  The
next exchange must expand their named lobes, or use a faithful proper-minor
state on the lifted adhesion.

## 3. The second path forces a sharp separator-load dichotomy

Return to the both-missing near-`K_7` model

\[
                      A,B,C,U_1,U_2,U_3,U_4.               \tag{3.1}
\]

Let `X` be the full envelope of `A` and

\[
             S=N_G(X)\subseteq U_1\cup U_2\cup U_3\cup U_4,
             \qquad |S|\ge7.                               \tag{3.2}
\]

Put `s_i=|S\cap U_i|`.  Since `A subseteq X` has an old model edge to
each `U_i`,

\[
                             s_i\ge1.                       \tag{3.3}
\]

Fix `A` and minimize the twin `B`, as in the audited second-path theorem.
If `B` is nonsingleton, write

\[
                            B=b_0\cdots b_n.                \tag{3.4}
\]

A row `Y in {C,U_1,U_2,U_3,U_4}` is **endpoint-locked** when every
`B-Y` edge has its `B`-end at `b_0` or every such edge has its `B`-end
at `b_n`.  The endpoint-ownership theorem says that at least two rows are
locked at each endpoint and that at most one row is not endpoint-locked.

### Theorem 3.1 (locked multiply-hit or four-hit mobile row)

If `B` is nonsingleton, at least one of the following alternatives needed
for the next stage holds.  More precisely, if outcome 1 fails, outcome 2
holds.

1. Some neutral row `U_i` has `s_i>=2` and is endpoint-locked.  Hence all
   occurrences of the `B-U_i` portal class in the expansion society of
   `U_i` attach to one fixed actual external vertex `b_0` or `b_n`.
2. There is a unique non-endpoint-locked row, it is a neutral row `U_*`,
   and

   \[
                   |S\cap U_*|=|S|-3\ge4,\qquad
                   |S\cap U_i|=1\quad(U_i\ne U_*).          \tag{3.5}
   \]

   Moreover `C` is endpoint-locked and the two endpoint monopoly sets
   have order exactly two each.  Thus this is the literal `2+1+2` cell,
   with `U_*` as its sole mobile row.

In either case, some one endpoint of `B` locks at least two distinct
neutral rows.  Hence two neutral expansion societies have their entire
`B`-portal classes rooted at the same actual vertex of `G`.

#### Proof

Suppose outcome 1 fails.  Every endpoint-locked neutral row then has
`s_i=1`.  If all four neutral rows were endpoint-locked, (3.3) would give
`|S|=4`, contrary to (3.2).  Hence some neutral row `U_*` is not
endpoint-locked.  There is at most one such row among all five row labels,
so `U_*` is unique and the other three neutral rows are endpoint-locked.
They each have load one, and (3.5) follows by summing the four disjoint
parts of `S`.

The only row outside the two endpoint monopoly sets is now `U_*`.
Consequently `C` belongs to an endpoint set.  Those two disjoint sets
have order at least two and together use exactly the other four labels,
so each has order exactly two.

For the final assertion, at most one of the five row labels is not locked
at an endpoint.  Therefore at least three of the four neutral labels are
endpoint-locked.  Distributing those labels between two endpoints puts at
least two at one endpoint.  Endpoint ownership means literally that every
edge from `B` to either of the corresponding neutral bags has its `B`-end
at this same endpoint.  \(\square\)

### Corollary 3.2 (the exact multiply-hit neutral residue)

Apply Theorem 2.1 to a multiply-hit neutral row.

* If `B` is a singleton, its `U`-portal class already has one fixed actual
  external root.
* In outcome 1 of Theorem 3.1, choose the locked multiply-hit row.  Its
  neutral society has at least two actual `X` portals and one fixed actual
  endpoint root for the entire `B` portal class.
* In outcome 2, choose `U_*`.  Its neutral society has at least four actual
  `X` portals and carries the unique mobile `B` portal class.

Unless Theorem 1.1 gives `K_7`, all entry carriers or all retained
carriers of the selected society are concentrated in one gate, cycle, or
3-connected torso.  This is the complete nonenumerative output of the
multiply-hit separator plus the second path.

The remaining theorem is now genuinely rooted and local: in the locked
cell, use two `X` roots and the fixed external endpoint root to split the
torso or align a full adhesion state; in the mobile cell, use the four
`X` roots to obtain the corresponding rooted model or one rural face.
Two portal vertices by themselves still do not justify splitting the old
neutral bag.

## 4. Uniform form

Theorem 1.1 is not specific to seven.  If a missing-star carrier `X`
already contacts `r` retained clique rows, and one additional clique row
`U` can be split into

* an entry shore supplying every still-missing row to `X`, and
* a residual shore retaining all other clique-row duties,

then sacrificing `U` increases the clique model by one branch set.  The
cross-Helly proof of Theorem 2.1 works for arbitrary finite lists of entry
and retained portal classes.  Its obstruction is always one rooted torso,
not an unbounded enumeration of the carrier vertices.
