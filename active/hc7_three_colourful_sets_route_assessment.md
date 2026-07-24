# Three colourful sets: literature and route assessment

**Status:** active literature assessment; checked in the separate GREEN
[internal audit](hc7_p2_nearfull_bipartition_census_audit.md).  There is no
new theorem and no claim that `HC_7` is proved.  The constants below were
checked against the cited full-version source.

## Proposed host statement

Let `Q` be eight-connected, let `p,v,d` induce a triangle, and put

\[
 R=Q-\{p,v,d\},\qquad
 A=N_R(p),\quad B=N_R(v),\quad U=N_R(d).
\]

Suppose `chi(R)=4` and each of `A,B,U` is colourful in the graph-colouring
sense: every proper four-colouring of `R` uses all four colours on each set.
The desired conclusion is one `K_4`-minor model
`(L_1,L_2,L_3,L_4)` in `R` such that

\[
 L_i\cap A\ne\varnothing,\qquad
 L_i\cap B\ne\varnothing,\qquad
 L_i\cap U\ne\varnothing
 \quad (i=1,2,3,4).                                  \tag{1}
\]

The four branch sets together with the singleton roots `{p},{v},{d}` would
be an explicit `K_7`-minor model in `Q`.

## What the standard rooted results give

Martinsson--Steiner, Theorem 1.3, proves that a colourful set in a
four-chromatic graph roots a `K_4` minor.  Applied separately, it gives an
`A`-rooted, a `B`-rooted, and a `U`-rooted model.  It does not synchronize
them into the single model required by (1).

Fabila-Monroy--Wood, Theorem 6, characterizes a `K_4` minor rooted at four
prescribed vertices of a four-connected graph, with the planar common-face
exception.  Deleting the three roots from eight-connected `Q` does leave
`R` five-connected.  The theorem nevertheless assigns only one prescribed
vertex to each branch set; (1) imposes twelve set-incidence requirements.
Colourfulness provides no common four-vertex transversal that turns those
requirements into this theorem's hypotheses.

## Exact Colorful Minors formulation

Annotate each vertex by whichever of `A,B,U` contain it.  In the terminology
of Protopapas--Thilikos--Wiederrecht, condition (1) is exactly a rainbow
`K_4` colorful minor with

\[
 q=3,\qquad t=4.
\]

Their full-version Theorem 3.1 starts from a specified `K_k`-minor model and
requires

\[
 k\ge\left\lfloor\frac32qt\right\rfloor+t.
\]

At the present parameters this is `k >= 22`.  The alternatives are a
rainbow `K_4`, or a set of order at most

\[
 qt-1=11
\]

such that the component big with respect to the starting clique model
misses at least one annotation.

This theorem is not applicable here:

1. the hypotheses supply an ordinary `K_4` minor in `R`, not a
   `K_22` minor;
2. eight-connectivity of `Q` gives five-connectivity of `R`, not the
   missing clique minor; and
3. even under a hypothetical application, a separator of order at most
   eleven is not the required exact-seven response and carries neither the
   named edge-deletion operation nor a strict literal-component descent.

There is one numerically suggestive but presently unavailable variant.  If
the three duties could first be reduced, with full provenance, to two
annotations, then `q=2,t=4` would give separator order at most seven.
However, Theorem 3.1 would still require a `K_16` minor, and no justified
two-annotation compression or such clique model is available.  This is not
a current proof route.

## Verdict

No cited theorem supplies the simultaneous three-rooted model or the
required strict exact-seven alternative.  The literature does clarify the
shape of the missing mechanism: it is a genuine multi-annotation
synchronization theorem.  In the current programme, eight-connectivity and
the named operation provenance must provide substantially more than the
abstract fact that `A,B,U` are individually colourful.

## Primary sources

- A. Martinsson and R. Steiner,
  [*Strengthening Hadwiger's conjecture for 4- and 5-chromatic graphs*](https://doi.org/10.1016/j.jctb.2023.08.009),
  Journal of Combinatorial Theory, Series B 164 (2024), 1--16,
  Theorem 1.3.
- R. Fabila-Monroy and D. R. Wood,
  [*Rooted `K_4`-Minors*](https://doi.org/10.37236/3476),
  Electronic Journal of Combinatorics 20(2) (2013), P64, Theorem 6.
- E. Protopapas, D. M. Thilikos and S. Wiederrecht,
  [*Colorful Minors*](https://arxiv.org/abs/2507.10467),
  full version, Theorem 3.1; conference version in ICALP 2026,
  [DOI 10.4230/LIPIcs.ICALP.2026.149](https://doi.org/10.4230/LIPIcs.ICALP.2026.149).
