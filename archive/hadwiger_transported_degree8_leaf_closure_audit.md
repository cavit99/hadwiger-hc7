# Adversarial audit: transported degree-eight leaf closure

## Verdict

**GREEN, conditional on the previously audited `C6+K1` two-piece atlas,
minimum-counterexample degree/connectivity facts, and the audited theorem
that a degree-eight vertex has at most two exterior components.**

The sole-exterior family is eliminated rigorously modulo the explicitly
stated finite-computation trust boundary.  The two-exterior relay packing,
the `|P|=4` closure, and the classification of the remaining clique rows
are also correct.  They leave, rather than solve, the locked-relay and
antipodal-three-clique states.

One sentence in Section 5 originally said that the *only* repair was a
private `Y_Q` relay.  A vertex `p in P` can also be adjacent to other
already committed vertices of `P`.  The statement needed by the argument
is that every available repair lies in `P union Y_Q`, and that at least one
lies in `Y_Q`.  The source note has been corrected accordingly; none of
the proved closures used the stronger wording.

## 1. Transported setup and clique classification

For a tight hub leaf,

\[
 U=P\dot\cup\{w\}\dot\cup\{y_s:s\in S-P\},
 \qquad |U|=8,
\]

and `D-u` is full to `S`.  Applying the singleton/full-body row of the
two-piece atlas to `u | (D-u)` gives

\[
 P\subseteq T_0\cup\{z\},\quad
 P\subseteq T_1\cup\{z\},\quad\hbox{or}\quad
 P\subseteq M_i\cup\{z\}.
\]

Each displayed container is a clique: `T_0,T_1` are the two prism
triangles, `M_i` is a prism edge, and `z` is universal.  Hence `P` is a
clique and `|P|<=4`.

These are also enough for the claimed no-four-clique classification.
Every four-clique of the old boundary is `T_0 union {z}` or
`T_1 union {z}`.  If `P` is in neither but is in `M_i union {z}`, it must
contain both endpoints of `M_i`; conversely such an antipodal pair cannot
lie in either prism-triangle four-clique.  Thus the only non-four-clique
row is precisely the antipodal clique `M_i union {z}` (with `P` containing
`M_i`).

## 2. Literal degree bounds when the residual shore is empty

When `R` is empty, all vertices of `G` lie in the old shores and boundary,
so the outside-neighbour counts used in Lemma 2.1 are exact.

* `w` has no neighbour in `H` because the old shores are anticomplete, and
  none in `S-P` because `N_D(s)={y_s}`.  There are no residual `D`
  vertices.  Its only neighbour outside `U` is therefore `u`, giving
  `d_{G[U]}(w)=d_G(w)-1>=6`.
* A private relay `y_s` has no neighbour in `H`; its only old-boundary
  neighbour outside `U` is `s`, since every other `t in S-P` has unique
  `D`-portal `y_t`; and there are no residual `D` vertices.  Its outside
  neighbours are exactly `u,s`, giving `d_{G[U]}(y_s)=d_G(y_s)-2>=5`.
* Fullness of `D-u` at each `p in P`, together with
  `D-u=\{w\} union \{y_s:s in S-P\}` in this case, supplies the required
  neighbour of `p` in `U-P`.
* Dirac's neighbourhood inequality at the degree-eight vertex `u` gives
  `alpha(G[U])<=8-7+2=3`.

No unlisted planarity, stronger connectivity, or adjacency assumption is
used here.

## 3. Independent audit of the finite one-shore verifier

The verifier was run successfully on 13 July 2026 and printed

```text
p=0 verified UNSAT with 3234 exhaustive model templates
p=1 verified UNSAT with 3234 exhaustive model templates
p=2 verified UNSAT with 3234 exhaustive model templates
p=3 verified UNSAT with 3234 exhaustive model templates
p=4 verified UNSAT with 3234 exhaustive model templates
```

Its encoding was checked as follows.

1. The 28 Boolean variables are exactly the edges of the eight-vertex
   boundary.  Requiring an edge in every four-set is equivalent to
   `alpha(A)<=3`.
2. The pseudo-Boolean constraints correctly encode degree at least six
   for `w=7` and degree at least five for each private relay
   `p,...,6`.  The representative clause for each `P` vertex ranges
   exactly over `Y union {w}`.
3. The contracted helper has fixed adjacency to every boundary vertex
   except `w`, exactly as `N_U(F)=U-{w}`.
4. Every boundary-meeting six-bag model in a nine-vertex graph selects
   six, seven, or eight boundary vertices and partitions them into six
   nonempty traces.  The count is
   \[
      {8\choose6}S(6,6)+{8\choose7}S(7,6)+S(8,6)
      =28+168+266=462.
   \]
   The sole helper is either unused or belongs to exactly one of the six
   bags, giving `462*7=3234` templates.  Thus no possible placement of
   the helper or omission of a boundary vertex is lost.
5. For each bag, the cut constraints are equivalent to connectedness;
   the fifteen pair constraints are exactly pairwise bag adjacency.
   Negating every template therefore states precisely that no
   boundary-meeting `K_6` model exists.

The UNSAT results prove the finite lemma relative to Z3/Python.  The note
correctly discloses that no independently checkable DRAT/LRAT certificate
has been exported.

The lift is sound: expanding the helper to the connected component `F`
preserves every required adjacency, and every one of the six bags meets
`U`.  Consequently the singleton `{u}` is adjacent to all six bags and
forms a seventh branch bag.

## 4. Relay-packing lift with two exterior components

Let `T` be an old-boundary four-clique containing `P`, `Q=T-P`, and use
the notation of Section 4.

* `A=F-Q` is connected because it contains the connected full shore `H`,
  and each remaining old-boundary vertex in `S-T` attaches to `H`.
* `B_q={q,y_q}` is connected by the private-portal edge.  The four bags
  indexed by `P union Q` are pairwise adjacent through the clique `T`.
* `A` is adjacent to every base bag through the full contacts of `H` with
  `T`; after adjoining `a in Y_0`, it meets the new boundary `U`.
* If the defect of `R` is not a base trace, choose distinct
  `a,b in Y_0` avoiding it.  Then `R union {b}` is connected,
  `A union {a}` and `R union {b}` are adjacent through an `R-a` edge,
  and both are adjacent to all four base bags.
* If `R` misses `y_q`, then `y_q` has only `u,q` outside `U`.  Thus
  `d_{G[U]}(y_q)>=5`.  There are only three other committed `U` traces,
  so `y_q` has a neighbour `b in Y_0 union {w}`.  The bag
  `R union {b}` uses `b-y_q` to repair exactly the missing base-bag
  adjacency.  The same construction works when the missed trace is
  `p in P` and the stated neighbour `b` exists.

The two added bags are disjoint, connected, meet `U`, adjacent to each
other, and adjacent to all four base bags.  This checks both bag
connectedness and every required interbag adjacency after lifting; no
edge between the two exterior components is assumed.

## 5. The four-contact row and exact residue

If `|P|=4`, then `T=P` and `Q` is empty.  When `R` misses `p in P`,
fullness of `D-u` cannot be witnessed in `R`; because `w` and all private
relays are exactly `Y_0 union {w}`, it supplies the neighbour required by
Lemma 4.1.  All other possible defects fall under its first case.  Hence
the `|P|=4` row closes.

In the remaining locked state, `R` misses `p in P` and `p` has no
neighbour in `Y_0 union {w}`.  Fullness of `D-u`, plus the missing
`R-p` adjacency, forces a neighbour in `Y_Q`.  Every possible literal
repair in `U` belongs to `P union Y_Q`, whose members are already the
four required boundary traces.  This establishes the claimed residue,
but does not by itself exclude it.

## 6. Exact scope

The proved advance is an infinite-family closure: the sole-exterior
transported degree-eight cell is impossible for exterior components of
arbitrary size, and the two-exterior `|P|=4` row is impossible.  The note
does **not** prove the proposed one-extra-bag relay web theorem, the
locked-relay state, the antipodal-three-clique row, or all of `HC_7`.
