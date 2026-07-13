# Audit of the seven-vertex exceptional cell and a deletion route for order eight

This note audits the claimed finite “kappa-only” elimination of the
exceptional (K_3\dot\cup K_4) neighbourhood when \(|C|=7\).  It also
records what the rooted-density route gives before that finite result is
used, and a conceptual deletion reduction for \(|C|=8\).

The mathematical encoding below is sound.  The all-UNSAT computation has
now been independently rerun with preserved machine-readable records for
all six shards, verified final counts and digests, and hashes of the exact
frozen scripts.  The finite order-seven lemma is therefore installed as a
computer-assisted result.

## 1. The finite lemma encoded by the 853-type search

Let (A,B,C) be pairwise disjoint, with

\[
 |A|=3,qquad |B|=4,qquad |C|=7,
\]

where (A) and (B) are cliques and are anticomplete to one another.
Assume:

1. (C) is connected;
2. every (a\in A) has at least four neighbours in (C), and every
   (b\in B) has at least three;
3. for every nonempty (X\subseteq C), its external neighbourhood in
   (A\cup B\cup C) has order at least seven.

The finite claim tested by `k34_c7_kappaonly_parallel.py` is:

> There are disjoint connected sets (J_1,J_2\subseteq A\cup C), each
> meeting (A), such that every (b\in B) has a neighbour in each
> (J_i).

Such sets are exactly the two helpers of Lemma 1.1 in
`hadwiger_exceptional_k34_round.md`; together with the four singleton
bags on (B) and then \(\{v\}\), they give a (K_7)-minor.

Condition 3 is necessary in the original graph: for nonempty
(X\subseteq C), the set (N_G(X)) separates (X) from (v), and
seven-connectivity gives \(|N_G(X)|\ge7\).  Since (v) has no neighbour
in (C), this is precisely the displayed condition.

## 2. Adversarial audit of the encoding

The fixed-(C) routine `solve_graph` in `k34_c7_sparse_fixed.py`, called
with `enforce_sparse=False` and `enforce_dirac=False`, correctly encodes
the preceding lemma.

* Coverage: the NetworkX atlas contains exactly 853 connected unlabelled
  graphs on seven vertices.  Fixing one representative is harmless,
  because all (A)- and (B)-incidences remain free.
* Boundary rows: the pseudo-Boolean row bounds are exactly four on each
  (A)-row and three on each (B)-row.
* Kappa shores: for every one of the 127 nonempty masks (X\subseteq C),
  the fixed (C)-boundary is counted once and each boundary vertex in
  (A\cup B) is represented by one Boolean OR.  The imposed lower bound
  is therefore exactly \(|N(X)|\ge7\), not an edge-count surrogate.
* Helper connectivity: for (P\subseteq C) and nonempty (R\subseteq A),
  the set (P\cup R) is connected exactly when every component of
  (C[P]) has a neighbour in (R), since (A[R]) is a clique.
* (B)-completeness: because (A) is anticomplete to (B), a helper is
  adjacent to every singleton (B)-bag exactly when (P) meets every
  (B)-row.
* Disjointness: the solver quantifies over disjoint nonempty (C)-masks
  and disjoint nonempty (A)-root masks.  Thus helpers using two (A)
  vertices are included; it is not merely a singleton-root search.
* Symmetry: sorting the three (A)-row codes and four (B)-row codes only
  factors permutations inside the two cliques and loses no state.

No mathematical underconstraint or overconstraint was found in this
reduction.  The independently certified outcome

\[
 853\text{ UNSAT},\qquad0\text{ SAT},\qquad0\text{ UNKNOWN}
\]

eliminates **all** \(|C|=7\) exceptional cells.  It is stronger than the sparse density
split and does not use Dirac's neighbourhood condition or the rooted
(K^*_{4,2}) density theorem.

Expected counts and digests hard-coded into a script are not themselves
evidence that a run occurred.  Here that caveat is discharged by the
independently generated records described below.

### Logic status versus run-evidence status

The two statuses should not be conflated.

* **Encoding logic audited:** the reduction from the finite lemma to the
  853 fixed-(C) solver instances is certified by the checks above.
* **Full run evidence certified and archived:** six independently rerun
  shard records cover all 853 indices, contain no SAT or UNKNOWN result,
  and merge to the expected global digest.  The frozen file hashes are

  ```text
  k34_c7_sparse_fixed.py
  aea1de233d30568694208458ea44a415c64f6c7637531c4438299f69b572a5fb

  k34_c7_kappaonly_parallel.py
  36231bad721c4f2ab66c1e92cfbcafc771ffabad66875fdee160dfa0088f0e0a
  ```

Before the full rerun, the exact fixed-(C) solver was also spot-checked on
atlas indices \(0,1,100,300,500,700,852\), spanning 6 through 21 edges.
All seven instances returned UNSAT with no timeout.

### Preserved run certificate

The separate recorder k34_c7_kappaonly_record.py imports the frozen worker
without duplicating its SAT constraints.  It asserts both frozen source
hashes, reruns one atlas shard, records every
\((\text{index},\text{graph6},\text{status})\) triple, and checks the
original expected shard count and digest before writing JSON.

The six archived files contain respectively

\[
143,\ 142,\ 142,\ 142,\ 142,\ 142
\]

UNSAT records and no SAT or UNKNOWN record.  Their graph-ID/status digests
are, in shard order:

    88bd85f9d81e547408ee9ccb5a18eb1c3ad9705e183ae2bdc81c3999e07cb136
    fe51bf49c4239069592a28b04edbc2c88d96500cfbd200d3fbd12088be9fac68
    c2190fb67ce2035a602128e028690a75c39d6bf24d67b26a28e699f059a8c8b5
    01ea845a80461d583d95bf23213fb0b8d8344c2832c3092587191b7d4ec834b4
    6aef5ce8017afb1120a0bad7c7a67ec334753430b7d11b961d8ec3397b41764c
    26383fc75f1e08e833a28eb6da083ec08555e9856a45b9084bbd550f2054e452

The merge routine independently asserts 853 distinct indices
\(0,\ldots,852\), compares every graph6 code with the atlas list, checks
that every status is UNSAT, and writes
k34_c7_kappaonly_merged.json.  Its global graph-ID/status digest is

    fe854344e1c75336fa01d6bab426e1456e28a2f59ad46c9315dc82c11e72a946

and the merged JSON file itself has SHA-256

    42c8f27265aa92c8dbdcfdb19499f440b2e2bf2301f4744f9258f3d2043d9dc5

The recorded environment is Python 3.14.3, NetworkX 3.6.1, and
Z3 4.15.4.  A second independent parse of the six JSON files reproduced
all counts, source hashes, atlas codes, and the global digest.  The root
agent additionally reran the original frozen shard 0 directly and obtained
143 UNSAT with its expected digest and success assertion.

## 3. What the dense rooted-model route says independently

Suppose instead that one only uses (p+q\ge38), so the rooted density
theorem supplies a (B)-rooted (K^*_{4,2})-model in (G-v).  Its four
root bags contain all four vertices of (B).  Hence any helper which does
not meet (A) is wholly contained in (C); call it deficient.

Two elementary size facts are valid.

### Lemma 3.1 (large deficient helper)

If a deficient helper (J\subseteq C) has at least four vertices, then
every vertex of (A) has a neighbour in (J).

#### Proof

Every (a\in A) has at least four neighbours in the seven-set (C), and
\(|J|\ge4\).  Thus (N_C(a)\cap J\ne\emptyset\). \(\square\)

Consequently, if exactly one helper is deficient, has order at least four,
and some (A)-vertex is unused by the six model bags, that vertex can be
absorbed into the deficient helper and the model extends with (v) to a
(K_7)-model.

### Lemma 3.2 (small-helper alternative)

If both helpers are deficient, then one has order at most three.

#### Proof

They are disjoint subsets of the seven-set (C). \(\square\)

Thus a rooted-model proof which does not use the finite helper lemma must
resolve one of two locks:

1. a deficient helper on at most three (C)-vertices; or
2. exactly one deficient helper of order at least four, with all three
   (A)-vertices already trapped in other model bags (and non-removable
   without destroying connectivity or a required model contact).

The rooted density theorem alone does not remove either lock.  In
particular, the fact that a large deficient helper is adjacent to every
(A)-vertex does not authorize moving an (A)-vertex out of another bag.

## 4. A conceptual order-eight reduction

Assume the seven-vertex finite lemma has been certified.  Let now
\(|C|=8\).  Call (x\in C) **deletable** if:

1. (C-x) is connected;
2. every (a\in A) still has at least four neighbours in (C-x), and
   every (b\in B) still has at least three; and
3. for every nonempty (X\subseteq C-x),
   \[
      |N_G(X)-\{x\}|\ge7.                            \tag{4.1}
   \]

### Lemma 4.1 (deletion to the certified order-seven cell)

If (C) contains a deletable vertex, then (G) has a (K_7)-minor.

#### Proof

Apply the seven-vertex finite lemma to (C-x), with the same (A,B).
Condition 1 gives connectedness, condition 2 gives the row bounds, and
(4.1) gives all 127 external-boundary inequalities after (x) is
deleted.  The resulting two helpers avoid (x) and are also helpers in
the original graph. \(\square\)

This gives an exact description of how the **deletion-to-order-seven
argument** can fail at order eight, not a sufficient characterization of
counterexamples.  In a counterexample, every non-cutvertex (x) of (C)
must be protected by at least one of:

* an (A)-row of order exactly four containing (x);
* a (B)-row of order exactly three containing (x); or
* a nonempty tight shore (X\subseteq C-x) with
  \(|N_G(X)|=7\) and (x\in N_G(X)).

Indeed, for a non-cutvertex, condition 1 in the definition of deletability
already holds.  If an (A)-row falls below four after deleting (x), its
original order was at least four, so it had order exactly four and
contained (x); the (B)-case is identical with three in place of four.  If
(4.1) fails for some (X), seven-connectivity gives
\(|N_G(X)|\geq7\).  Since deleting one vertex can reduce this boundary by
at most one, failure is possible exactly when
\(|N_G(X)|=7\) and (x\in N_G(X)).  Conversely, each of the three displayed
conditions makes the corresponding deletability requirement fail.  Thus
the list is an if-and-only-if description of nondeletability for a fixed
non-cutvertex.

The last item includes the singleton obstruction caused by an adjacent
degree-seven (C)-vertex.  Since every connected graph has at least two
non-cutvertices, the order-eight problem has become a covering/uncrossing
problem for tight rows and tight seven-boundary shores, rather than a new
unstructured helper search.  This covering condition is necessary but is
not asserted to be sufficient for avoiding two helpers or a (K_7)-minor.

A simple high-slack corollary is immediate: if every (A)-row has order
at least five, every (B)-row has order at least four, and every nonempty
proper (X\subseteq C) has \(|N_G(X)|\ge8\), then any non-cutvertex of
(C) is deletable, and the (K_7)-minor follows.
