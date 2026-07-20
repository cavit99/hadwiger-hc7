# A two-column allocation certificate for pentagonal-bipyramid expansions

**Archive note:** unaudited precursor to the promoted two-column absorption
result; retained for provenance and not part of the current proof spine.

**Status:** active draft with a written proof; independent audit pending.

This note isolates the global mechanism in the fourteen-vertex
pentagonal-bipyramid counterexample to the local path-split dichotomy.  Two
columns that are individually harmless can be divided simultaneously and
allocated to two other columns, repairing all three missing adjacencies of
an anchored five-bag model.

## 1. Setup

Let `P=C_5\vee\overline {K_2}` have poles `a,b` and rim cycle

\[
                         c_0c_1c_2c_3c_4c_0.
\]

Suppose a graph contains pairwise disjoint connected subgraphs

\[
                  R_0,R_1,(L_x:x\in V(P))
\]

such that:

1. `R_0,R_1` are adjacent;
2. each `R_i` is adjacent to every `L_x`; and
3. two columns `L_x,L_y` are adjacent exactly when `xy` is an edge of `P`.

No connectivity, planarity, or order assumption is made on the host beyond
these displayed branch sets.

## 2. The allocation theorem

### Theorem 2.1 (two-column simultaneous allocation)

Assume there are disjoint vertex sets

\[
                         X,Y\subseteq V(L_a\cup L_{c_0})
\]

such that

\[
\begin{aligned}
 H_1&=L_{c_1}\cup X, & H_2&=L_{c_2}\cup Y
\end{aligned}
\]

are connected, and

\[
 E(H_1,L_{c_3}),\quad E(H_1,L_{c_4}),\quad
 E(H_2,L_{c_4})                                      \tag{2.1}
\]

are all nonempty.  Then

\[
 R_0,\ R_1,\ L_b,\ H_1,\ H_2,\ L_{c_3},\ L_{c_4}    \tag{2.2}
\]

are branch sets of an explicit `K_7`-minor model.

The same conclusion holds after interchanging the poles, cyclically
relabelling the rim, or reversing its orientation.

#### Proof

The seven sets in (2.2) are pairwise disjoint.  The two allocated sets
`X,Y` lie in the omitted columns `L_a\cup L_{c_0}`, are disjoint from one
another, and are disjoint from the five whole anchor columns in (2.2).
They are connected by hypothesis after being adjoined to `L_{c_1}` and
`L_{c_2}`.  All other displayed sets were connected in the setup.

It remains to check adjacency among the five nonroot sets.  The pole column
`L_b` is adjacent to all four rim columns.  Among the rim anchors,

\[
 L_{c_1}L_{c_2},\qquad L_{c_2}L_{c_3},\qquad
 L_{c_3}L_{c_4}
\]

are inherited quotient contacts.  The only three absent contacts among
the four-vertex rim path are

\[
 c_1c_3,\qquad c_1c_4,\qquad c_2c_4.
\]

They are supplied, respectively, by the three edges in (2.1).  Thus

\[
                         L_b,H_1,H_2,L_{c_3},L_{c_4}
\]

form a `K_5`-minor model.  Each of these five bags contains a whole old
column, so both `R_0` and `R_1` are adjacent to all five.  The two roots are
adjacent to one another.  This proves (2.2). \(\square\)

## 3. Exact realization in the fourteen-vertex obstruction

Use poles `a=0,b=1` and rim `c_0,...,c_4=2,...,6`.  Each column is the
edge

\[
                         L_i=\{(i,0),(i,1)\}.
\]

In the explicit counterexample, take

\[
 X=\{(0,1),(2,0)\},\qquad
 Y=\{(0,0),(2,1)\}.                                  \tag{3.1}
\]

The edge `(0,1)(2,0)` makes `X` connected and `(0,0)(2,1)` makes `Y`
connected.  Moreover:

* `X` contacts `L_3,L_5,L_6`;
* `Y` contacts `L_4,L_6`.

Theorem 2.1 therefore returns the five anchored bags

\[
 L_1,\quad L_3\cup X,\quad L_4\cup Y,\quad L_5,\quad L_6,
\]

which are exactly the distributed `K_5` model found by the finite search.
The model is invisible to every test that splits only one column at a time:
both omitted columns contribute to both allocated bags.

## 4. Sharpness and role

For the fixed anchor choice

\[
                         b,c_1,c_2,c_3,c_4,
\]

the three contacts in (2.1) are exactly the three quotient nonedges that
must be repaired.  Thus none can simply be dropped while retaining the
same seven branch sets.  The theorem is a sufficient allocation
certificate, not a claim that every five-connected nonplanar expansion
contains such `X,Y`.

Its use in the live programme is to replace one-column path tests by a
global search for two disjoint connected allocations in the union of one
pole column and one adjacent rim column.  Failure of that allocation is the
appropriate place to seek a separator or a compatible planar embedding.
