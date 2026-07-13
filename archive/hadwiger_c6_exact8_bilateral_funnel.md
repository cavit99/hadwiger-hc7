# The forced exact-eight gate is bilateral and carries a rooted `K_4`

## 1. Setting

Let

\[
 S=W\mathbin{\dot\cup}\{z\},\qquad
 \overline{G[S]}=C_6\mathbin{\dot\cup}K_1,
\]

so `G[W]` is the triangular prism and `z` is complete to `W`.  Let `D`
be the minimum all-full-deletion exact-seven shore and `H` an opposite
component full to `S`.  By the forced-three-cut theorem, a three-cut

\[
                         T=\{t_1,t_2,t_3\}
\]

of `D` has exactly two lobes `C_1,C_2`.  Put

\[
                         A_i=S-N_S(C_i).
\]

At least one `A_i` has order two.  Fix such an index, write

\[
 C=C_i,\qquad A=A_i,\qquad B=S-A,
 \quad X=T\mathbin{\dot\cup}B.
\]

Then `N_G(C)=X` and `|X|=8`.

## 2. The opposite side is one full shore

### Theorem 2.1 (bilateral exact-eight funnel)

The graph `G-X` has exactly two components.  One is `C`; the other,
denoted `R`, is connected and full to all eight vertices of `X`.
Consequently the forced order-eight adhesion has two full sides.

### Proof

The two-lobe polarity theorem gives

\[
                         A_1\cap A_2=\varnothing.       \tag{2.1}
\]

Hence the other lobe `C_{3-i}` contacts both members of `A`.  Since it is
adjacent to every member of `T`, the set

\[
                         H\cup A\cup C_{3-i}           \tag{2.2}
\]

is connected.  It is adjacent to every member of `T` through the other
lobe and to every member of `B` through the old full shore `H`.

Every component of `G-S` other than `D` is full to `S`; after `B` is
deleted it joins (2.2) through either member of `A`.  There are no further
lobes of `D-T`.  (In the standard two-shore formulation the only old
opposite component is `H`; if the cut has been obtained from a larger
presentation, every additional old component joins in the same way.)
Thus every vertex outside `C\cup X` belongs to the one component `R`
containing (2.2).  The preceding literal contacts show that `R` is full to
`X`.  The lobe `C` is full to `X` because `X=N_G(C)`.
QED.

No assertion that an individual vertex of either shore is complete to
`X` is used here; fullness is collective.

## 3. The five old gate vertices contain a `K_4` minor

### Lemma 3.1 (boundary `K_4` core)

The graph `G[B]` contains a `K_4` minor.  More precisely, the defect pair
`A` is either the two neighbours `N_{C_6}(w)` of a cycle vertex in the
missing six-cycle, or one of the three antipodal pairs of that cycle.

* In the first case `W-A` contains one of the two triangles of the
  triangular prism, so that triangle together with `z` is a literal
  `K_4`.
* In the antipodal case `G[W-A]` is a four-cycle.  Contracting one of its
  edges gives a `K_3` minor, and adjoining the universal vertex `z` gives
  a `K_4` minor in `B`.

### Proof

The four-polarity theorem for the two lobes says that every order-two
coordinate is of one of the two displayed types.  The two branch models
then follow directly from the complement-of-cycle boundary.  QED.

## 4. Exact rooted completion target

The previous facts isolate the remaining geometry without referring to
the Moser labels.

### Lemma 4.1 (single-reserve completion)

If there is a vertex `x in X` for which `G[X-x]` contains a `K_5` model,
then `G` contains a `K_7` minor.

### Proof

Let `Q_1,...,Q_5` be the five bags of the model in `X-x`.  Use

\[
                         C,\qquad R\cup\{x\},
                         \qquad Q_1,\ldots,Q_5.       \tag{4.1}
\]

The second bag is connected because `R` is full to `X`.  The first two
bags are adjacent through an edge from `C` to `x`.  Each of them is
adjacent to every `Q_j`, again by fullness to `X`.  The seven bags are
otherwise disjoint, so (4.1) is a `K_7` model.  QED.

Consequently a target-free gate satisfies

\[
                         \eta(G[X-x])\le4
                         \qquad\text{for every }x\in X. \tag{4.2}
\]

In particular, for each `i=1,2,3`, the seven-vertex graph
`G[B union (T-\{t_i\})]` is `K_5`-minor-free.  This is the genuine
simultaneous three-choice failure; two unused cut vertices are not
required.  By the already established `HC_5`, all three of these
seven-vertex graphs are four-colourable.

### Lemma 4.2 (reserved-three-root completion)

Let `F_1,...,F_4` be a `K_4` model in `G[B]`.  Suppose that, after
permuting `T`, the graph `G[B\cup\{t_3\}]` has a `K_5` model

\[
                         F'_1,F'_2,F'_3,F'_4,P
\]

such that `P` contains `t_3` and the other two cut vertices `t_1,t_2`
are unused.  Then `G` contains a `K_7` minor.

### Proof

Use the seven bags

\[
              C\cup\{t_1\},\quad R\cup\{t_2\},\quad
              P,\quad F'_1,F'_2,F'_3,F'_4.          \tag{4.3}
\]

The first two bags are connected because both shores are full to `X`.
They are adjacent through either of the literal edges from `C` to `t_2`
or from `R` to `t_1`.  Each is adjacent to every one of the last five
bags through the fullness of its shore to `X`.  The last five bags form
the assumed `K_5` model.  All bags are disjoint by construction.  Thus
(4.3) is a `K_7` model.  QED.

The target-free residue is therefore exact:

> for each cut vertex `t_i`, even the boundary enlarged by the other two
> cut vertices remains `K_5`-minor-free.

This is a simultaneous rooted-extension failure across a bilateral full
eight-adhesion.  Static fullness alone does not eliminate it: the three
cut vertices may have no edges to `B`.  The missing input must use the
proper-minor transition states (or a model-clean allocation theorem), not
another contact-incidence count.

### Exact sharpness check

The dependency-free verifier `c6_threecut_forced_quotient_probe.py`
contracts the two lobes and the old opposite shore, keeps the three cut
vertices as distinct vertices adjacent to both lobe helpers, and retains
only the forced old-boundary contacts.  An exact connected-branch-set
search returns `negative` for all four polarity orbits of the two-lobe
theorem.  Thus even the literal three-vertex adhesion, as opposed to its
contraction to one complementary shore, does not close statically.

The smaller verifier `c6_exact8_rooted_k5_row_probe.py` also identifies
the precise one-vertex repairs of the boundary core.  In the neighbour-pair
case `B` is `K_5` minus two adjacent edges; a cut vertex roots a `K_5`
exactly above the upward closure of two minimal contact rows (the three
vertices consisting of the deficient vertex and its two nonneighbours, or
all four vertices of the literal `K_4`).  In the antipodal case `B` is
`K_5` minus two independent edges; every minimal repairing row has order
four.  These calculations are diagnostics only.  They show why a single
extra contact cannot prove the transition theorem and are not used as a
positive lemma.

## 5. Scope

Theorem 2.1 and Lemmas 3.1--4.2 do not prove `HC_7`.  They replace the
arbitrary exact-eight alternative by one precise uniform rooted-model
problem:

\[
 \boxed{\text{two full sides}+\text{one reserved root}
        +\text{a boundary }K_4
        \Longrightarrow
        \text{rooted }K_5\text{ or compatible minor state}.}
\]

Any affirmative transition theorem of this form closes the minimum
`C_6\dot\cup K_1` atom and is directly reusable in the arbitrary
near-`K_7` route.
