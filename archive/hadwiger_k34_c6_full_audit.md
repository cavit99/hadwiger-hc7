# Audit of the full six-vertex exceptional-cell certificate

## Verdict

The computer-assisted Theorem 5.1 in
hadwiger_k34_c6_human.md is correct in its stated scope.  The checker
k34_c6_full_search.py exhausts the required state space and implements
the mathematical obstruction exactly.  Its output was reproduced, and
two independent checks were also run:

1. a NetworkX graph-atlas implementation, using literal sets and
   connected components instead of the checker's bit routines, reproduced
   all counts; and
2. an explicit enumeration of all 148,995 multisets of four possible
   \(B\)-neighbourhoods for each of the 63 low-compatible states found no
   feasible no-helper state.

The theorem therefore validly excludes \(|C|=6\) in the exceptional
\(K_3\dot\cup K_4\) degree-seven cell, and the resulting exact bound is
\(|C|\geq 7\).

There is one integration typo, not a flaw in Theorem 5.1.  In
hadwiger_exceptional_k34_round.md, equation (6.1), currently at line 423,
still says \(|C|\geq6\).  It must say \(|C|\geq7\), consistently with
equation (5.5), the introduction, and the proved theorem.

There is also a separate scope overstatement in the list after equation
(6.1).  Item 3 is not, by itself, sufficient to eliminate the whole
remaining cell: the rooted \(K^*_{4,2}\) model in (5.3) is supplied only
when \(p+q\geq4|C|+10\).  For \(|C|\geq7\), the established lower bounds
\(p\geq24\) and \(p+2q\geq7|C|\) do not imply this threshold.  For
example, at \(|C|=7\) the numerical values \(p=24,q=13\) satisfy the
recorded lower bounds but have \(p+q=37<38\).  Item 3 is sufficient only
in the density branch where (5.3) actually supplies a model, unless a
new argument first proves the threshold in every remaining graph.

## 1. Exact finite statement being checked

The data relevant to the theorem are:

* a connected graph \(C\) on the labelled set \(\{0,\ldots,5\}\);
* three, not necessarily distinct, subsets \(R_1,R_2,R_3\subseteq V(C)\)
  of order at least four, representing the three \(A\)-neighbourhoods;
* four subsets \(S_1,\ldots,S_4\subseteq V(C)\) of order at least three,
  representing the four \(B\)-neighbourhoods; and
* the six inequalities

  \[
  d_C(x)+|\{i:x\in R_i\}|+|\{j:x\in S_j\}|\geq7.
  \]

For a balanced partition \(\{P,Q\}\), a root \(a_i\) connects \(P\) if
and only if \(R_i\) meets every component of \(C[P]\).  Indeed, the one
new vertex \(a_i\) joins all components exactly in that situation.
Thus the checker's root predicate is necessary and sufficient, including
when \(C[P]\) has one, two, or three components.

The two sides can use distinct roots precisely when their two nonempty
root lists have union of order at least two.  This is the complete
two-set system-of-distinct-representatives condition.  Duplicate
\(A\)-neighbourhoods cause no problem: the checker keeps the three
root vertices as three separately indexed entries even when their rows
are equal.

Consequently the ten A-compatible balanced partitions computed by the
checker are exactly the partitions satisfying the connectivity and
distinct-root part of Theorem 5.1.

## 2. Exhaustiveness of the \(C\)-graph orbits

There are fifteen possible edges on six labelled vertices.  The function
connected_unlabelled_graphs first tests all \(2^{15}\) edge masks and
retains the 26,704 connected labelled graphs.  It then applies all
\(6!=720\) vertex permutations to each first unseen mask and removes its
complete orbit.

The edge relabelling is correct: each input pair \(\{u,v\}\) is sent to
the sorted pair \(\{\pi(u),\pi(v)\}\), and the corresponding output bit is
set.  Connectivity is invariant under these maps, so no disconnected
mask can enter or remove a connected orbit.  Removing a whole orbit at
each step makes the resulting 112 representatives pairwise
nonisomorphic and exhaustive.

Using one representative per orbit does not quotient away necessary
\(A\)-incidence information.  After an arbitrary labelled configuration
is relabelled so that its \(C\)-graph equals the chosen representative,
its three \(A\)-rows become three of the same 22 labelled subsets which
the inner loop enumerates.  No quotient by \({\rm Aut}(C)\) is performed,
so every such image is still present.

As an independent audit, the NetworkX graph atlas contains exactly 112
connected six-vertex graph isomorphism classes, and rerunning the full
\((C,A)\) calculation over those atlas representatives gives the same
summary as the bespoke orbit constructor.

## 3. The \(A\)-multiset quotient

There are

\[
\binom64+\binom65+\binom66=22
\]

possible \(A\)-rows.  The checker enumerates the

\[
\binom{22+3-1}{3}=2024
\]

multisets of three rows using combinations with replacement.

This quotient is exact.  Permuting the three vertices of the clique \(A\)
does not change:

* the column degrees \(d_A(x)\);
* whether the two root lists have distinct representatives; or
* the existence of the final two helper bags.

Conversely, each multiset represents three actual, distinct \(A\)-vertices;
equal rows are allowed and remain separately indexed by root_set.  Thus
the multiset enumeration neither omits nor falsely identifies a relevant
state.

The total number of checked \((C,A)\)-states,

\[
112\cdot2024=226,688,
\]

is therefore correct.

## 4. Audit of the blocker reduction

### 4.1 One \(B\)-vertex forbids at most one partition

Let \(\{P,Q\}\) be a \(3+3\) partition and let
\(|N_C(b)|\geq3\).  If \(b\) misses \(P\), then
\(N_C(b)\subseteq Q\); both sets have order at least and at most three,
respectively, so \(N_C(b)=Q\).  Similarly, missing \(Q\) forces
\(N_C(b)=P\).

Thus a \(B\)-vertex forbids a partition only when its neighbourhood is
exactly one side, and that exact three-set determines one unordered
partition.  A \(B\)-row of order four, five, or six forbids none.

It follows immediately that five A-compatible partitions cannot all be
forbidden by four \(B\)-vertices.

### 4.2 The blocker injection is valid

Suppose there are \(q\leq4\) A-compatible partitions and no helper.
Every one of those \(q\) partitions must be forbidden.  Since one
\(B\)-vertex cannot forbid two different unordered partitions, one can
choose \(q\) distinct blocking vertices, one for each partition.  Their
neighbourhoods are forced to be one of the two sides of their respective
partitions.  The checker's \(2^q\) orientation loop lists exactly all
possibilities for those forced rows.  Assigning the oriented partitions
to named \(B\)-vertices is unnecessary because the four \(B\)-vertices
are symmetric and only their column sum is used.

### 4.3 Completing the remaining \(B\)-rows is a safe maximum

After the \(q\) forced exact-three rows are selected, replace each of the
remaining \(4-q\) \(B\)-rows by \(V(C)\).  This adds one to every
coordinate for each remaining row, so it simultaneously maximizes all
six \(B\)-degrees.  It does not unblock any A-compatible partition:
the selected exact rows still block all \(q\) of them.

Accordingly, every genuine no-helper configuration satisfying the degree
conditions yields an orientation for which

\[
\min_x\bigl(d_C(x)+d_A(x)+(4-q)
 +|\{r:x\in T_r\}|-7\bigr)\geq0.
\]

The checker's best_minimum_slack is exactly the maximum of this quantity
over all orientations.  A negative value for every low-compatible state
therefore rules out all genuine \(B\)-configurations.

In fact, the relaxation is exact for existence, not merely necessary:
if some orientation with the complete residual rows had nonnegative
slack, those very four rows would be a legal \(B\)-configuration of
minimum row size three which blocks all compatible partitions and
satisfies all degree inequalities.

## 5. Line-by-line checker predicates

The principal implementation points all agree with the proof.

* PARTITIONS fixes vertex \(0\) on one side and chooses two of the other
  five vertices.  Its ten entries represent every unordered \(3+3\)
  partition exactly once.
* components computes exactly the connected components of the induced
  subgraph on a side.
* root_set sets bit \(i\) precisely when the \(i\)-th \(A\)-row meets
  every one of those components.
* compatible_partitions applies the exact two-list SDR test.
* The first degree filter discards a state only when even four
  \(B\)-vertices complete to \(C\) leave some total degree below seven.
  It is therefore a valid necessary filter.
* For \(q\leq4\), exact_b_rows contains one oriented side for each
  compatible partition, and b_degree adds the \(4-q\) complete rows.
* feasible_states receives a state exactly when the maximized minimum
  degree slack is nonnegative.  The final assertion that this list is
  empty is the desired finite conclusion; the hard-coded summary is an
  additional regression check, not the logical source of emptiness.

The root predicate was also compared for every representative graph,
every balanced side, and every possible \(A\)-row against literal
connectivity of the augmented NetworkX graph \(C[P]+\{a\}\).  Every
comparison agreed.

## 6. Reproduced and independent output

Running

    python3 k34_c6_full_search.py

completed successfully and printed:

    connected unlabelled C graphs: 112
    A-neighbourhood multisets per graph: 2024
    degree-possible C/A states: 186354
    states with at most four A-compatible partitions: 63
      (e(C), q, best minimum degree slack)=(5, 4, -3): 2
      (e(C), q, best minimum degree slack)=(5, 4, -2): 2
      (e(C), q, best minimum degree slack)=(6, 2, -1): 4
      (e(C), q, best minimum degree slack)=(6, 4, -3): 4
      (e(C), q, best minimum degree slack)=(6, 4, -2): 19
      (e(C), q, best minimum degree slack)=(7, 2, -1): 2
      (e(C), q, best minimum degree slack)=(7, 4, -2): 22
      (e(C), q, best minimum degree slack)=(8, 4, -2): 7
      (e(C), q, best minimum degree slack)=(9, 4, -2): 1
    degree-feasible no-helper states: 0
    certificate verified

An independent implementation based on the NetworkX graph atlas and
ordinary set operations reproduced

\[
(112,\ 226688,\ 186354,\ 63,\ 0)
\]

and the same nine-entry slack distribution.

Finally, all

\[
\binom{42+4-1}{4}=148,995
\]

multisets of four \(B\)-rows of order at least three were explicitly
enumerated for each of the 63 low-compatible states.  A row of order
three was marked as blocking its unique partition, rows of larger order
as blocking none, and the six true degree inequalities were tested
directly.  This independent test again found zero feasible no-helper
states.  It does not use the complete-row relaxation.

## 7. Transfer to the HC7 exceptional cell

All hypotheses of Theorem 5.1 follow from the exceptional-cell package
when \(|C|=6\):

1. \(C=G-N[v]\) is the sole exterior component, hence is connected.
2. For \(a\in A\), the only neighbours outside \(C\) are \(v\) and the
   other two vertices of the \(K_3\).  Since \(\delta(G)\geq7\),
   \(|N_C(a)|\geq4\).
3. For \(b\in B\), the only neighbours outside \(C\) are \(v\) and the
   other three vertices of the \(K_4\).  Hence
   \(|N_C(b)|\geq3\).
4. A vertex \(x\in C\) is not adjacent to \(v\), and there are no vertices
   outside \(C\cup N\cup\{v\}\).  Therefore

   \[
   d_G(x)=d_C(x)+d_A(x)+d_B(x)\geq7.
   \]

Let the theorem return \(C=P\dot\cup Q\) and distinct roots
\(a_i,a_j\).  The bags

\[
J_1=P\cup\{a_i\},\qquad J_2=Q\cup\{a_j\}
\]

are disjoint and connected.  They are adjacent through the clique edge
\(a_i a_j\).  For every \(b\in B\), the condition that \(P,Q\) meet
\(N_C(b)\) gives an edge from the singleton bag \(\{b\}\) to each helper.
The four \(B\)-singletons are pairwise adjacent because \(G[B]=K_4\).
Thus \(J_1,J_2\), together with those four singleton bags, form six
pairwise adjacent branch sets.  Every one meets \(N(v)\), so the disjoint
singleton \(\{v\}\) is adjacent to all six.  This is a valid \(K_7\)-model.

No branch set is reused, and the proof does not require an edge between
\(P\) and \(Q\).

Combining this exclusion of \(|C|=6\) with the previous elementary
\(|C|\geq6\) reduction gives exactly

\[
|C|\geq7.
\]

## 8. Exact scope and remaining gap

The certified result is confined to the exceptional
\(K_3\dot\cup K_4\) neighbourhood at a degree-seven vertex and to an
exterior component of order exactly six.  It is a genuine strengthening:
all six-vertex incidence patterns satisfying the original lower bounds
are covered, not only the earlier equality case \(e(C)=9\).

It does not eliminate exceptional configurations with \(|C|\geq7\), does
not resolve the two-side portal lock, and does not prove HC7.  The
integration note should therefore retain its stated residual, with the
correction \(|C|\geq6\to|C|\geq7\) in equation (6.1).  Its third proposed
closing route should also be qualified as applying only under
\(p+q\geq4|C|+10\), or supplemented by a proof that every residual graph
meets that density threshold.
