# Singleton one-hole rooted exchange

## Status

This closes the singleton deficient bag as a *terminal configuration*.
It does not prove `HC_7`: its non-target outputs are an actual adhesion or
another labelled near-`K_7` model.  The point is that the one-missing state
now belongs to the same finite deficiency-rotation system as the audited
both-missing seven-root state; it no longer requires a separate
foreign-bag singletonization theorem.

The argument is label-preserving and uses literal portal vertices.  It is
also the one-target analogue of the seven-root trichotomy.

## Theorem 1 (singleton one-hole trichotomy)

Let `G` be seven-connected.  Let

\[
                 \{a\},B,U_1,U_2,U_3,U_4,U_5             \tag{1.1}
\]

be pairwise disjoint connected branch sets such that:

1. `B,U_1,...,U_5` form a `K_6` model;
2. `a` is anticomplete to `B`; and
3. `a` has a neighbour in every `U_i`.

Assume every neighbour of `a` lies in the displayed six foreign bags.
(In particular this holds for a spanning model.)  Then at least one of
the following occurs.

1. `G` contains a `K_7` minor.
2. There is a nonempty connected set `Y` contained properly in one
   `U_i` such that `N_G(Y)` is an actual separator of order at least
   seven.  If its order is seven, it is full to every component of
   `G-N_G(Y)`.
3. There is a labelled `K_7^-` or `K_7^vee` model whose deficient centre
   is a proper nonempty connected subset of one old neutral bag `U_i`.

### Proof

Seven-connectivity gives `d_G(a)>=7`.  All neighbours of `a` lie in the
five neutral bags, because `aB` is absent.  Choose seven distinct
neighbours of `a`, including at least one in every `U_i`.  Some donor
bag `U`, therefore, contains two selected roots `r,s`.

For every foreign row

\[
                  F\in\{B,U_1,\ldots,U_5\}-\{U\},        \tag{1.2}
\]

let `P_F=N_U(F)`, and protect `r`.  A retained row core is a connected
set in `U` containing `r` and meeting every `P_F`.

Suppose first that some retained row core `T` avoids `s`, and let `Y` be
the component of `U-T` containing `s`.  The row-core lemma gives that
`Y` and `U-Y` are connected and that `U-Y` retains an edge to every row
in (1.2).  If `Y` misses `B`, then the whole connected bag `B` lies
outside `Y union N_G(Y)`.  Thus `N_G(Y)` is an actual separator.  It has
order at least seven, and the standard minimum-cut argument gives
fullness when its order is seven.  This is outcome 2.

If instead `Y` meets `B`, perform the literal transfer

\[
                      B'=B\cup Y,\qquad U'=U-Y.           \tag{1.3}
\]

The enlarged target `B'` is connected through a `YB` edge.  The donor
residual `U'` is connected, retains every old foreign-row contact, and
is adjacent to `B'` through an edge across the connected split
`Y|U'`.  The selected root `s` gives the edge `aB'`, while the protected
root `r` gives `aU'`.  The vertex `a` retains its old edge to every
other neutral bag.  Hence

\[
                      \{a\},B',U',\{U_i:U_i\ne U\}       \tag{1.4}
\]

are seven pairwise adjacent connected branch sets, giving outcome 1.

It remains that `s` is unavoidable in every retained row core based at
`r`.  Now protect `s` and test `r`.  If `r` is avoidable in this reverse
orientation, let `Y` be its component outside a retained core.  The same
row-core lemma makes `Y` monopoly-free with connected complement.  If it
misses `B`, its open neighbourhood is an actual separator; if it meets
`B`, transfer it into `B`.  The moved root `r`, the protected root `s`,
and the five old row adjacencies then give exactly the same literal
`K_7` model as in (1.3)--(1.4), with the root names reversed.

Thus only the case in which each root is unavoidable relative to the
other remains.  The opposite-root gate theorem gives two disjoint
canonical gates, and their monopoly sets are disjoint subsets of the
five row labels in (1.2).  Consequently one orientation has a detachable
gate `Z` with

\[
             1\le |\Omega_U(Z)|\le2,\qquad
             W=U-Z\text{ connected},                    \tag{1.5}
\]

where `Z` contains one selected `a`-neighbour and `W` contains the
other.  If `Z` misses `B`, the same argument as above makes `N_G(Z)` an
actual separator and gives outcome 2.

Suppose `Z` meets `B`.  Put

\[
                          A'=\{a\}\cup Z.                 \tag{1.6}
\]

This is connected through the selected `aZ` edge.  Regard `W` as a new
deficient centre.  The six foreign bags are

\[
                       A',B,\{U_i:U_i\ne U\}.             \tag{1.7}
\]

They form a clique model.  Indeed `A'B` is supplied by the `ZB` edge;
`A'` meets every untouched neutral row through the old edges at `a`;
and the other five rows retain their old clique-model edges.  The centre
`W` meets `A'` through an edge across `Z|W`.  For a row `F` in (1.2),
the only possible loss of the old `UF` edge is exactly
`F in Omega_U(Z)`.  Thus the new centre has one or two missing spokes.
The first case is a labelled `K_7^-` and the second a labelled
`K_7^vee`, giving outcome 3.  (An empty monopoly set would instead give
outcome 1.)

In every non-target branch the displayed near side `Y` or new centre
`W` is a proper nonempty connected subset of the old donor `U`.  This
proves the theorem. \(\square\)

## Corollary 2 (closure of the normalized one-missing path cell)

In a target-free deficient-first normalized near-`K_7` model, coherent
transport which repairs exactly one twin forces the deficient path core
to be a singleton by the endpoint-shadow theorem.  After making the
model spanning, Theorem 1 applies.  Consequently the entire one-missing
normalization cell has only two live outputs:

* a faithful actual adhesion; or
* a labelled deficiency rotation to a proper part of one old foreign
  bag.

It is not an additional terminal case.  Together with the uniform
seven-root trichotomy, both the one-hole and two-hole normalized cells
now feed the same rotation/adhesion composition problem.

## Uniform form

The proof uses the numerical coincidence

\[
                 |N(a)|\ge7>5=\text{number of contacted rows}. \tag{3.1}
\]

More generally, let a singleton centre miss one row of a `K_m` foreign
model and meet the other `m-1` rows.  If it has at least `m+1` literal
neighbours in those rows, one donor contains two roots.  Opposite-root
gates in that donor have disjoint monopoly sets among the `m-1` other
foreign rows, so one has monopoly order at most
`floor((m-1)/2)`.  The same proof gives a target clique, an actual
adhesion, or a rotated missing star of that order.  The case `m=6` is
exactly the threshold at which the rotated deficiency remains at most
two.
