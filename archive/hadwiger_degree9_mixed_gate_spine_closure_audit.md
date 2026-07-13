# Adversarial audit: the mixed complementary/same-bag gate

## Verdict

Theorem 3.1 and Corollary 3.2 of
`hadwiger_degree9_mixed_gate_spine_closure.md` are **GREEN** under the
globally minimized balanced spanning-model hypotheses.  The proof works
with two outer portals and therefore includes exact portal equality.

The key point is that the failed two-path outcome is not left as a web
or separator case: it gives a rooted-model exchange which strictly
improves the already chosen tertiary potential.

## 1. Portal-count audit

For the complementary left gate, seven-connectivity gives at least
three portals from the root component (K) into (R_5cup R_0).
The audited ordinary-bag theorem gives

\[
                         |N_{R_0}(K)|\leq1.
\]

Therefore at least two portals lie in (R_5).  In the mixed cell the
root component (J) of (R_5-5) is anticomplete to (L_6), so both
portals lie in (C=R_5-J).  This proves (|A|\geq2), exactly the
source multiplicity required by the flexible-start lemma.  No strict
surplus assumption is used.

The old (R_5L_0)-adjacency has its (R_5)-endpoint in (C), since
(J\not\sim L_0).  Hence (B=N_C(L_0)) is nonempty.

## 2. Linkage branch

Apply the flexible-start lemma in (C) to source set (A) and target
classes (B,{5}).  In its linkage outcome the paths have distinct
starts in (A) and distinct terminal vertices.  This remains valid if
(5\in A), (A\cap B\ne\varnothing), or (5\in B): order-one paths
are permitted, while distinctness makes the two path subgraphs
disjoint.

Extending the two paths gives connected sides (X,Y) with

\[
 X\sim K,L_0,\qquad Y\sim K,\qquad5\in Y.
\]

Adding (J) to (Y) preserves disjointness and connectivity because
every component of (R_5-5), including (J), has an edge to (5).
Now (r_5,5\in Y), so the already audited outer two-sided closure
applies.

The stronger split certificate in Lemma 2.1 also covers the unused
orientation (r_5\in X,5\in Y).  Its seven displayed bags were checked
directly by `degree9_mixed_gate_spine_closure_verify.py`: all bags are
connected and disjoint, and all twenty-one adjacencies are present using
only the stated conservative contacts.

## 3. Bottleneck branch

If the linkage fails, one vertex (q\in C) meets every
(A)-to-((B\cup{5})) path.  Since (|A|\geq2), the set
(A-\{q\}) is nonempty.  Let (U) be a component of (C-q)
meeting it.

Connectedness of (U) proves

\[
                         U\cap B=\varnothing,\qquad5\notin U:
\]

otherwise an (A)-to-(B) or (A)-to-(5) path inside (U)
would avoid (q).  This argument also covers target/source overlap.

The exchange

\[
                 (L_6,R_5)\longmapsto(L_6\cup U,R_5-U)
\]

is valid:

* (U\sim K) connects the enlarged left bag;
* (C-U) is (q) plus the other components of (C-q), so it is
  connected and contains (5);
* (J) joins the residue through (5), so (R_5-U) is connected;
* an edge (Uq) keeps the two changed bags adjacent;
* a member of (B) retained outside (U) keeps the (R_5L_0)
  edge;
* (J\sim R_0) keeps the (R_5R_0) edge;
* roots and the literal vertices (5,6) stay in their prescribed
  bags.

Thus the move remains in the full globally optimized balanced family,
keeps the first two potential coordinates, and decreases (|R_5|) by
(|U|>0).  This is a contradiction.  There is no hidden assumption
that (U) is anticomplete to (R_0); contacts gained by enlarging
(L_6) do not invalidate a clique model.

## 4. Combination audit

The gate classification is exhaustive.  If the left gate is
complementary, the right gate is either:

1. same-bag, closed by Theorem 3.1; or
2. complementary, closed by the independently audited direct model in
   `hadwiger_degree9_opposite_gate_closure.md`.

Therefore no complementary left gate survives.  The symmetric argument
excludes a complementary right gate.  The only attachment cell not
eliminated by these two infinite-family theorems is the bilateral
same-bag cell.
