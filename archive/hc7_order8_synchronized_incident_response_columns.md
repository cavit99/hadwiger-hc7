# Synchronized incident-edge responses in a seven-column system

**Archive note:** unaudited frozen order-eight draft retained for provenance;
it is not part of the current proof spine.

**Status:** written draft awaiting separate audit.  This is an unbounded
host-level reduction inside the two-component boundary-of-order-eight
branch.  It does not prove the response-coupling theorem or `HC_7`.

## 1. Setting

Let `G` be a seven-connected graph such that

\[
 \chi(G)=7,
 \qquad \chi(M)\le 6\text{ for every proper minor }M\text{ of }G.
 \tag{1.1}
\]

Let `S` be an eight-vertex set for which `G-S` has exactly two components
`C,D`, each adjacent to every literal vertex of `S`.  Fix

\[
 p\in S,\qquad v\in C\cap N_G(p),\qquad
 w\in D\cap N_G(p),                                  \tag{1.2}
\]

and put

\[
 e=pv,\qquad f=pw,\qquad H=G-\{e,f\}.                \tag{1.3}
\]

The two braces in (1.3) mean edge deletion.  The vertices `v,w` are
nonadjacent because they belong to distinct components of `G-S`.

We use the audited prescribed-omission theorem: seven prescribed non-`p`
edges at either centre can be routed disjointly to all seven vertices of
`S-{p}`, unless a nonempty proper connected subset of that open component
has full neighbourhood of order seven or eight.  The order-seven outcome
is an actual exact-seven response, while the order-eight outcome is a
strict generic response-side descent for one of the prescribed edges.

## 2. The incident-edge Kempe cover

### Theorem 2.1 (one double-contraction colouring controls both roots)

There is a proper six-colouring `c` of `H` and a colour `alpha` such that

\[
                         c(p)=c(v)=c(w)=\alpha.        \tag{2.1}
\]

For every colour `beta` different from `alpha`, the component containing
`p` of

\[
                         H[c^{-1}(\{\alpha,\beta\})]  \tag{2.2}
\]

contains at least one of `v,w`.

#### Proof

Contract both incident edges `pv,pw`.  Their union is connected and has
no further internal edge, because `vw` is absent.  A six-colouring of the
proper minor expands to the colouring (2.1) of `H`.

Fix `beta`.  Suppose that the component in (2.2) containing `p` contains
neither `v` nor `w`.  Interchange `alpha,beta` on the union of the
components containing `v` and `w`; if those two vertices lie in one
component, interchange on that one component.  This is a union of whole
bichromatic components disjoint from the component of `p`, so the result
is a proper colouring of `H`.  It leaves `p` with colour `alpha` and gives
both `v,w` colour `beta`.  Restoring `pv,pw` would then six-colour `G`, a
contradiction.  Hence (2.2) contains `v` or `w`.  \(\square\)

Call `beta` **`v`-locked** when `p,v` lie in one component of (2.2), and
**`w`-locked** when `p,w` do.  A colour may have both properties.  For
each lock choose a path to `p`; its first edge at the relevant centre has
a `beta`-coloured other end.  The first edges belonging to distinct
alternate colours are therefore distinct.

## 3. One common column system preserves every locked first edge

### Theorem 3.1 (synchronized marked columns)

At least one of the following holds.

1. A nonempty connected proper subset of `C` or `D` has full neighbourhood
   of order seven, or it gives a strict generic order-eight response-side
   descent for a prescribed crossing edge.
2. There are seven pairwise vertex-disjoint connected subgraphs

   \[
                          L_s\qquad(s\in S-\{p\})     \tag{3.1}
   \]

   disjoint from the adjacent connected root sets

   \[
                          R_C=\{v,p\},\qquad R_D=\{w\}, \tag{3.2}
   \]

   such that `s in L_s` and each root set is adjacent to every `L_s`.
   Moreover, every first edge selected after Theorem 2.1 is the first edge
   of the appropriate shore limb of exactly one column.  Thus the same
   colouring `c` marks a set `M_C` of `v`-columns and a set `M_D` of
   `w`-columns with

   \[
                         |M_C|+|M_D|\ge5,
              \qquad\max\{|M_C|,|M_D|\}\ge3.         \tag{3.3}
   \]

   Every alternate colour labels a mark at at least one root, and the
   colour labels are injective on either root.  No assertion identifies a
   colour with the boundary label `s`; in particular, the union
   `M_C union M_D` need not contain five columns.

#### Proof

If `d_G(v)=7`, the singleton `{v}` has full neighbourhood of order seven.
The component `D` lies outside `N_G[v]`, so this is an actual separation.
Thus, outside outcome 1, `d_G(v)>=8`; symmetrically `d_G(w)>=8`.

At `v`, take the distinct first edges of all `v`-locks.  There are at most
five.  Pad them to seven distinct incident edges other than `pv`.  None of
the seven padded edges has boundary end `p`.  Apply the prescribed-omission
theorem with omitted vertex `p`.  Its separator outcome is outcome 1 here;
otherwise it gives seven paths beginning with the prescribed edges and
ending bijectively at `S-{p}`.  Apply the same argument at `w`.

For `s in S-{p}`, let `P_s^C,P_s^D` be the two paths ending at `s`, and
put

\[
                    L_s=(P_s^C-v)\cup(P_s^D-w).       \tag{3.4}
\]

The columns are connected through their distinct common boundary ends and
are pairwise disjoint.  The first edges make the two root sets adjacent to
every column, while `pw` makes the roots adjacent.  Every selected lock
edge was prescribed and hence remains the first edge of its unique limb.
 Finally, Theorem 2.1 says that every one of the five alternate colours
 locks at least one root.  Counting a colour twice when it locks both roots
 gives the first inequality in (3.3), and the second follows by the
 pigeonhole principle.  \(\square\)

### Corollary 3.2

If the column-contact graph on `S-{p}` contains a `K_5` minor, the two root
sets and five unions of columns give an explicit `K_7`-minor model.  Hence
that contact graph is `K_5`-minor-free in a surviving host.

This is the existing paired-column decoder applied to the synchronized
system above.

### Proposition 3.3 (five marked columns on each side)

There is a possibly different paired seven-column system for which exactly
five columns on the `C` side and exactly five columns on the `D` side have
operation-critical first edges.  Consequently at least three columns are
marked on both sides.

The two sets of five marks come from the one-edge colourings of `G-e` and
`G-f`, respectively.  Their palette names are unrelated; only their
literal first edges and common boundary columns are synchronized.

#### Proof

Take a six-colouring of `G-e`.  Its endpoints `p,v` have one colour
`alpha`.  For every other colour `beta`, the `alpha,beta` component
containing `v` contains `p`; otherwise a Kempe interchange would make `e`
proper and six-colour `G`.  Choose the first edge at `v` of one such path
for each of the five alternate colours.  These five edges are distinct and
different from `e`.  Outside the separator/descent outcome of Theorem 3.1,
`d_G(v)>=8`, so pad them to seven edges different from `e` and apply the
prescribed-omission theorem with omitted vertex `p`.  This gives a fan to
all of `S-{p}` with five marked limbs.

Apply the symmetric construction to a six-colouring of `G-f` at `w`, and
pair the two fans through their common literal ends as in (3.4).  Each set
of five marked limbs therefore marks a five-subset of the same seven
columns.  Two five-subsets of a seven-set intersect in at least three
members.  No comparison of the two palettes was used.  \(\square\)

## 4. The exact noncommuting-switch contact

Fix two distinct alternate colours `beta,gamma`.  Say that `beta` is
**`v`-exclusive** when the `alpha,beta` component of `p` contains `w` but
not `v`.  Let `A_beta` be the component containing `v`.  Define
**`w`-exclusive** and `B_gamma` symmetrically.

### Theorem 4.1 (exclusive response components must touch)

If `beta` is `v`-exclusive and `gamma` is `w`-exclusive, then
`beta ne gamma` and precisely one of the following literal interactions
occurs.

1. `A_beta` and `B_gamma` intersect; every common vertex has colour
   `alpha`.
2. The two components are disjoint and an edge joins a `beta`-coloured
   vertex of `A_beta` to a `gamma`-coloured vertex of `B_gamma`.

In particular, disjoint exclusive components cannot be anticomplete.

#### Proof

The same alternate colour cannot be exclusive in the two opposite
directions: its component containing `p` cannot contain `w` but not `v`
and simultaneously contain `v` but not `w`.  Hence `beta ne gamma`.

If the components meet, a common vertex has a colour in
`{alpha,beta} cap {alpha,gamma}={alpha}`, proving outcome 1.

Assume they are disjoint.  Properness excludes an `alpha-alpha` edge.
An edge from an `alpha`-vertex of `A_beta` to a `gamma`-vertex of
`B_gamma` would put that alpha vertex in the `alpha,gamma` component
`B_gamma`, contrary to disjointness.  Symmetrically there is no
`beta-alpha` edge.  Thus every edge between the two components is a
`beta-gamma` edge.

If there were no such edge, interchange `alpha,beta` on `A_beta` and
`alpha,gamma` on `B_gamma`.  The two components are anticomplete, so the
interchanges commute and preserve properness.  The vertex `p` remains
alpha, while `v` becomes beta and `w` becomes gamma.  Restoring both
deleted edges then gives a six-colouring of `G`, a contradiction.  This
proves outcome 2.  \(\square\)

## 5. Equality partitions and the clean-contact exchange

Let `c_beta` be obtained by interchanging `alpha,beta` on `A_beta`, and
let `c_gamma` be obtained by interchanging `alpha,gamma` on `B_gamma`.
The colouring `c_beta` has `(e,f)=(proper,equal)`, so it extends to a
proper colouring of `G-f`; in particular its equality partition `Pi_C`
on `S` is legal on the intact closed `C`-shore.  Symmetrically the equality
partition `Pi_D` of `c_gamma` is legal on the intact closed `D`-shore.

### Proposition 5.1 (partition separation)

One has

\[
                              \Pi_C\ne\Pi_D.           \tag{5.1}
\]

#### Proof

If the partitions were equal, a permutation of the six colour names would
align `c_beta` on `G[C\cup S]` with `c_gamma` on `G[D\cup S]`.  The two
open components are anticomplete.  Gluing the two restrictions would give
a proper six-colouring of `G`, a contradiction.  \(\square\)

The next elementary observation identifies exactly when the touch in
Theorem 4.1 really is a new column contact.

### Proposition 5.2 (clean connector absorption)

Let `L_s,L_t` be distinct columns in a system from Theorem 3.1.  Suppose
there is an `L_s`--`L_t` path `Q` whose internal vertices avoid both root
sets and every column.  If `L_s,L_t` are not adjacent, the column system
can be changed, without changing any boundary label or root adjacency, so
that they are adjacent: add all internal vertices of `Q` to `L_s` except
the last endpoint in `L_t`.

Consequently, an exclusive-component touch either supplies a new literal
column contact whenever it contains such a clean connector between the
two marked columns, or it is blocked by a root or by a third column.

#### Proof

The enlarged `L_s` remains connected and disjoint from all other columns
and both roots.  The last edge of `Q` supplies the new adjacency to
`L_t`; every old column and root adjacency remains.  \(\square\)

## 6. Exact contribution and remaining obstruction

Theorems 2.1--4.1 use one double-contraction colouring throughout.  They do
not pool colours or contact graphs from unrelated response systems.  They
prove that all five alternate colours are represented by marked first
edges in one synchronized seven-column system and that opposite exclusive
switches have a literal
noncommutation witness.  Proposition 5.1 records the exact equality
partition incompatibility rather than merely different colour names.

What is not proved is that the touch in Theorem 4.1 has a clean connector
as in Proposition 5.2.  Its paths can return through `v` or `w`, or meet
one or more other columns before joining the two marked columns.  The
seven-connected `K_2`-join-planar shadow shows that one additional
unlabelled column contact would not be terminal in any event.  The missing
theorem must allocate a coherent family of these operation-specific
touches to a `K_5` minor in one literal column system, or turn a blocked
touch into an exact order-seven compatible partition or a strict
selected-response descent.

## 7. Dependencies

- the prescribed-omission theorem at an eight-vertex boundary;
- the paired-column `K_5`-minor decoder; and
- ordinary Kempe interchange on a whole bichromatic component.
