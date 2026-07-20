# Audit of the two--three centre-component closure

**Verdict:** **GREEN**.

**Audited source:**
[`hc7_order8_two_three_centre_component_closure.md`](hc7_order8_two_three_centre_component_closure.md)
at SHA-256
`b29c5aeabe36d406b7817c851d976cad544d19f9f325aac4435ec8d86878dd69`.

**Audit class:** separate internal mathematical audit.  This is not external
peer review.

## 1. Scope

The audit checks Theorem 1.1 and its complete proof.  It checks the two
separator constructions, the use of Dirac's inequality, both boundary
allocation cases, and every adjacency in each displayed `K_7`-minor model.
It does not audit the wider order-eight programme or claim that `HC_7` is
proved.

## 2. Separator checks

If a component of `C-v` or `D-w` misses at least two vertices of the
eight-set `S`, its full neighbourhood is contained in the relevant centre
and at most six vertices of `S`.  The component itself and the opposite
open component give two nonempty sides.  Seven-connectivity therefore
forces its neighbourhood to have order exactly seven, as claimed.

In the repeated-centre-neighbour case, failure of two disjoint
`{a,b}`--`Y` paths gives a separator `Z` of order at most one.  A surviving
source lies in a component `R subseteq A_1` with

\[
 N_G(R)\subseteq \{v\}\cup M\cup\{p\}\cup Z,
\]

whose order is at most `1+4+1+1=7`.  The open component `D` witnesses the
other side, so seven-connectivity again forces an actual order-seven
separation.  The successful Menger outcome yields two paths with distinct
ends, and the connected-bipartition lemma preserves their required
connectivity and disjointness.

## 3. Repeated-neighbour minor model

For the seven branch sets in (3.4), all twenty-one adjacencies are present:

- six incidences involve the connected root bag `{v,p,w}`;
- one is the adjacency between the two parts of the connected partition of
  `A_1`;
- eight join those two parts to the four other component-derived bags via
  the common boundary vertices `x,y`; and
- six among the four remaining component-derived bags follow from the
  no-reciprocal-defect representative lemma.

All seven sets are connected and pairwise disjoint.  Thus the displayed
construction is an explicit `K_7`-minor model.

## 4. Unique-neighbour reduction

When each component contains exactly one neighbour of its centre,

\[
 d(v)=|N(v)\cap S|+2,
 \qquad
 d(w)=|N(w)\cap S|+3.
\]

The two centre-neighbours of `v` form an independent set and the three
centre-neighbours of `w` form an independent set.  Dirac's inequality
`alpha(N(x)) <= d(x)-5` therefore gives
`|N(v) cap S|>=5` and `|N(w) cap S|>=5`, hence `|V|,|W|>=4`.

If a vertex of `V union W union P` is missed by none of the five
components, the cited paired-centre decoder applies with central connected
set `G[{v,p,w}]`, five components, and a singleton boundary clique.  In the
remaining case every vertex of `K=V union W union P` occupies one of the
five defect slots, so `4<=|K|<=5`.

## 5. Boundary allocation

For `|K|=5`, the five defects are the five distinct vertices of `K`; in
particular no `B`-component misses `p`.  Two safe distinct `A`-representatives
exist in `W`.  Of the three unused values of `K`, at most two are forbidden
for the first `B`-component.  The two values outside `K` are then safe for
the other two components.

For `|K|=4`, one has `V=W=K`.

- If no `B`-component misses `p`, at most one defect is outside `K`.  If it
  exists, the four defects in `K` are pairwise distinct.  Consequently the
  three-by-three assignment of outside-`K` representatives has at most one
  forbidden incidence, and a safe bijection exists.
- If `B_0` misses `p`, it is the unique such component and the other four
  defects are exactly the four distinct vertices of `K`.  The stated two
  `A` choices, one remaining `K` choice for `B_0`, and two outside-`K`
  choices are all safe.

These arguments establish distinct representatives, root adjacency, and
the exclusion of reciprocal defect pairs in every case.

As nonessential corroboration, an independent deterministic enumeration
checked 138,240 valid canonical defect tables, including both orientations,
and found no failure.  The original raw loop count 147,840 included 9,600
redundant declarations in which the named five-set strictly contained the
actual union `V union W union P`; the filtered count 138,240 is the one
reported in the audited theorem.  The written proof is independent of this
finite check.

## 6. Final model and trust boundary

For the seven branch sets in (5.2), all twenty-one adjacencies are present:
one between the two root bags, five from each root bag to the five
component-derived bags, and ten among the component-derived bags by the
no-reciprocal-defect condition.  Connectivity and disjointness are valid.

The result is conditional on reaching the `(2,3)` centre-component count.
It neither proves that every order-eight response interface reaches this
case nor closes `(1,1)`, `(1,2)`, `(1,3)`, or `(2,2)`.  No unresolved
assumption remains inside the theorem as stated.
