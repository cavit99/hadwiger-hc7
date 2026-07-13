# Rooted `K_5`: reserved connector or a full model separator

**Status:** proved and independently audited.

This is the first uniform rooted-model principle on the sole-exterior
`HC_7` spine.  It is stated without Moser labels; the pure-Moser trace is an
immediate instance.

## 1. Exact setting

Let `G` be seven-connected, not six-colourable, and suppose every proper
minor of `G` is six-colourable.  Let `v` have degree seven and write

\[
 N(v)=\{a,b\}\mathbin{\dot\cup}U,
 \qquad |U|=5,
\]

where `ab` is a nonedge.  Put `H=G-v`.  Assume:

1. contracting the connected star on `{v,a,b}` gives the exact trace in
   which `a,b` share one colour and the five roots in `U` have five distinct
   other colours;
2. the corresponding Kempe system supplies a rooted `K_5` model
   `B=(B_u:u in U)` in `H-{a,b}`; and
3. `{a,b}` jointly dominates `U`: for every `u in U`, at least one of
   `au,bu` is an edge.

The exact trace and domination assumptions are automatic in the pure-Moser
degree-seven cell.  The rooted model follows from the audited five-root
Kempe theorem because the missing-edge graph on `U` is a cycle.

## 2. The dichotomy

### Theorem 2.1

Under the hypotheses above, one of the following holds.

1. `G` contains a literal `K_7` minor.
2. If `W=union_{u in U} B_u`, then there is an inclusion-minimal
   `a-b` separator

   \[
                        Z\subseteq W,
                        \qquad |Z|\ge6,              \tag{2.1}
   \]

   such that the components `R_a,R_b` of `H-Z` containing `a,b` are both
   full to the literal separator `Z`.  Moreover some rooted bag contains
   at least two vertices of `Z`.

### Proof

If `a,b` lie in one component of `H-W`, choose an `a-b` path `P` in that
component.  The path is disjoint from all five rooted bags.  For every root
`u`, one of `a,b` is adjacent to `u`, so `P` is adjacent to `B_u`.  Hence

\[
                         P,B_u\ (u\in U)
\]

are six disjoint connected pairwise adjacent branch sets in `H`.  The
singleton `{v}` sees `P` through `a,b` and sees every `B_u` through its
root.  These are seven literal `K_7` branch sets.

Otherwise `W` separates `a` from `b`.  Choose an inclusion-minimal
`a-b` separator `Z subseteq W`.  Seven-connectivity of `G` makes `H`
six-connected, so `|Z|>=6`.

For every `z in Z`, minimality supplies an `a-b` path meeting `Z` exactly
at `z`.  The two portions of that path show that `z` has a neighbour in
each of `R_a,R_b`.  Conversely, a component of `H-Z` has no external
neighbour outside `Z`.  Thus

\[
                         N_H(R_a)=N_H(R_b)=Z.          \tag{2.2}
\]

Finally, `Z` is distributed over the five pairwise disjoint rooted bags.
Since it has at least six vertices, one bag contains at least two of them.
This proves outcome 2. `square`

## 3. Pure-Moser instantiation

For the standard Moser boundary take

\[
 a=1,\qquad b=3,\qquad U=\{0,2,4,5,6\}.
\]

Contracting `{v,1,3}` forces the exact six-colour trace: if a colour were
absent on `N(v)`, it would colour `v`.  A Kempe swap separating any missing
pair of roots would again make one colour absent on `N(v)`, so every
missing-cycle pair is bichromatically connected.  The five-root theorem
therefore yields the required rooted `K_5`.  Finally
`alpha(G[N(v)])<=2` implies joint domination, since otherwise
`{1,3,u}` would be independent.

Thus every sole-exterior pure-Moser survivor either already contains
`K_7`, or has the full separator (2.1)--(2.2) inside an actual rooted model.

## 4. Trust boundary

The theorem does not say that `|Z|=6`, that `Z` contains the literal roots,
or that `Z=U union {w}`.  Nor does a double hit automatically split its bag
label-faithfully.  Those are precisely the bridge/Tutte tasks that remain.
The gain is that the obstruction is now an actual full separator carried by
five named rooted bags, rather than an abstract failure of a nonseparating
rooted minor.
