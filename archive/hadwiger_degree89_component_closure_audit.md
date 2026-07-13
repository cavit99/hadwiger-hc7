# Audit of the degree-eight and degree-nine maximal-component closures

## Verdict

**GREEN**, with the explicit computational trust boundary in Section 7.

The following two statements are supported by correct graph-theoretic
reductions and by certificate verifiers whose complete advertised test
suites passed in this audit.

* In a proper-minor-minimal counterexample to \(HC_7\), a degree-eight
  vertex has at most two exterior components.
* In such a counterexample, a degree-nine vertex has at most three exterior
  components.

The audit covered

* `hadwiger_degree8_three_component_closure.md`;
* `degree8_three_shore_verify.py` and its three certificate files;
* `hadwiger_degree9_four_component_closure.md`;
* `degree9_four_shore_verify.py` and its twenty-three certificate files;
* the quotient-to-host lift;
* every proper-minor contraction used for color gluing; and
* the prior component bounds on which the final “at most” conclusions
  depend.

Neither result eliminates the remaining one- and two-component degree-eight
cells or the remaining one-, two-, and three-component degree-nine cells.
They are substantive infinite-family closures, not a proof of \(HC_7\).

## 1. Reduction to one- and two-defect shores

Let \(N=N_G(v)\).  When \(G-N[v]\) has at least two components, the
external neighborhood of each component \(C\) is contained in \(N\) and
separates \(C\) from \(v\).  Seven-connectivity therefore gives

\[
                         |N_G(C)|\ge 7.                 \tag{1.1}
\]

Thus a shore at a degree-eight vertex misses at most one member of \(N\),
and a shore at a degree-nine vertex misses at most two.  Replacing a full
shore by a one-miss shore, or enlarging a miss set to order two, only
deletes shore-boundary edges.  Every model or usable anchor found in the
weakened quotient remains valid in the original graph.

Dirac's neighborhood inequality gives, respectively,

\[
       \alpha(G[N])\le3\qquad\hbox{and}\qquad
       \alpha(G[N])\le4.                                \tag{1.2}
\]

The only external structural inputs here are the established facts that a
proper-minor-minimal \(HC_7\) counterexample is seven-contraction-critical
and that a noncomplete seven-contraction-critical graph is seven-connected.

## 2. Finite symmetry coverage

### Degree eight

Three singleton misses have exactly three equality patterns under boundary
and shore permutations:

\[
                         000,\qquad001,\qquad012.        \tag{2.1}
\]

These are exactly the three certificate inputs.  No incidence pattern is
lost by this quotient: an ordered triple of singleton labels is determined,
up to the allowed permutations, by whether it has one, two, or three
distinct values.

### Degree nine

The four two-element miss sets are the four edges of a loopless
multigraph.  Parallel edges are allowed.  Relabeling the boundary and the
four shores is exactly multigraph isomorphism with unlabeled edges.

The verifier's incremental canonical generator returns twenty-three
types.  This count and the actual list were checked independently by a
different enumeration:

1. generate all 1,657 restricted-growth set partitions of eight labeled
   half-edges in which the two ends of no edge lie in one block;
2. canonicalize under all \(4!\) edge permutations and all \(2^4\)
   endpoint flips; and
3. add isolated boundary vertices to reach boundary order nine.

This gives exactly twenty-three orbits, and their canonical incidence
structures agree with `MISS_TYPES` in the verifier.  Thus the finite
degree-nine run covers every multiset of four loopless two-element miss
sets, including parallel misses and unused boundary vertices.

## 3. Boolean encoding audit

For degree eight, the seventy clauses indexed by four-subsets of \(N\)
say exactly that every four-set spans an edge, i.e.
\(\alpha(A)\le3\).  For degree nine, the 126 clauses indexed by five-sets
say exactly \(\alpha(A)\le4\).

The anchor encodings are exact.

* Independence is the conjunction of the negations of every same-block
  boundary edge.
* A shore-block union is connected precisely when the artificially enlarged
  miss set is disjoint from its assigned independent block.
* Two shore-block unions are adjacent if one shore meets the opposite
  block, or, when neither does, if a boundary edge crosses the two blocks.
* The singleton \(w\) is adjacent to a shore-block union either through the
  shore or through a boundary edge into that block.
* The assignment is allowed to depend on the retained side, and both
  verifiers quantify the assignment permutations separately for each side.

The symmetry reductions inside the partition enumerators are also valid:
the star block \(S\) is distinguished, while the other shore blocks are
interchangeable because every assignment permutation is tested.  The
singleton \(w\), when present, remains distinguished.

For every listed quotient model, the verifier checks:

1. six nonempty, pairwise disjoint bags;
2. a boundary vertex in every bag;
3. a crossing edge for every nontrivial bipartition of every bag; and
4. a crossing edge for every pair of bags.

Item 3 is equivalent to bag connectedness.  Quotient boundary edges are
Boolean variables, shore-boundary edges are the fixed miss constants, and
shore-shore edges are false.  Hence `model_expression` and `model_formula`
encode exactly an \(N\)-meeting \(K_6\)-model in the weakened quotient.

The degree-nine prose additionally says that every model has four bags of
the form \(C_i\cup\{x_i\}\) and two singleton boundary bags.  The verifier
does not assert this special form, but an independent decoding of all 423
current templates confirmed it: every template contains each of the four
shore vertices once, paired with one distinct boundary representative,
and contains two further distinct singleton representatives.  This special
form is not needed for the lift—the general checked model formula already
suffices—but the advertised strengthening is true for the present files.

## 4. Quotient-model lift

Let \(B\) be a quotient branch set.  Replace every shore vertex
\(c_i\in B\) by the entire connected component \(C_i\).  Call the result
\(\widehat B\).

Disjoint quotient bags lift to disjoint host bags because the exterior
components are disjoint.  A spanning tree of the connected quotient bag
lifts edge by edge: a shore-boundary quotient edge represents an actual
edge from the corresponding component to that boundary vertex, and every
component is connected.  Pairwise bag adjacencies lift for the same reason.
Every lifted bag still contains a member of \(N\).

Thus the six quotient bags lift to an \(N\)-meeting \(K_6\)-model in
\(G-v\).  Since \(v\) is adjacent to every member of \(N\), the singleton
\(\{v\}\) meets all six bags and gives a \(K_7\)-model.  Ignored extra
shore-boundary edges cannot invalidate this lift.

## 5. Proper-minor coloring and expansion

The color-gluing argument uses the following valid elementary operation.
For a retained component \(C_i\), contract

\[
 \{v\}\cup S
\]

and each assigned set \(C_j\cup T_j\) on the other shores.  These sets are
pairwise disjoint and connected: the first is a star, and every member of
an independent block \(T_j\) is adjacent to its assigned shore because
the miss set is disjoint from that block.  At least the star contraction
reduces the graph, so the result is a proper minor and has a six-coloring.

The contracted images form the claimed clique.  The star image sees every
other image through an edge from \(v\).  The remaining clique adjacencies
are exactly the anchor conditions encoded by the verifier.  When \(w\) is
present, its required adjacencies are encoded as well.

To recover a coloring of \(G[N\cup C_i]\), delete the exterior vertices
belonging to the contracted other shores, delete \(v\), and give every
boundary vertex in a contracted block the color of that block's image.
This expansion is proper:

* every expanded block is independent; and
* every original edge from the block to a retained vertex or another block
  became an edge incident with the corresponding contracted image, so the
  minor coloring already assigned different colors.

Because the contracted images form a clique, the prescribed boundary
blocks receive distinct colors.  A permutation of six colors aligns these
block colors over all retained sides.  The exterior components are pairwise
anticomplete, so the aligned side colorings glue.

In the degree-eight three-anchor case only three colors occur on \(N\); in
the four-anchor case only four occur.  In the degree-nine four- and
five-anchor cases only four and five occur, respectively.  In each case a
six-color absent from \(N\) is available for \(v\), contradicting
\(\chi(G)=7\).

No step identifies nonadjacent vertices, assumes a coloring survives an
arbitrary contraction, or contracts a disconnected shore-block union.

## 6. Verification runs

The complete degree-eight run produced:

```text
degree8_three_shore_certificate_0.txt verified UNSAT with 141 model templates
degree8_three_shore_certificate_1.txt verified UNSAT with 183 model templates
degree8_three_shore_certificate_2.txt verified UNSAT with 98 model templates
```

The degree-nine run was split into parallel index groups.  Every index
\(0,1,\ldots,22\) returned `verified UNSAT`; the template counts were

\[
10,13,15,15,13,14,13,21,13,18,22,24,17,18,20,20,26,20,23,
25,19,17,27,                                             \tag{6.1}
\]

which sum to 423 and agree with the prose and certificate files.  The
largest certificate types, 16 and 22, were among the successful runs.

The discovery programs were not imported.  The verifiers parsed only the
certificate data and reconstructed the graph formulas themselves.

## 7. Formal trust boundary

The finite proof currently trusts:

1. the ordinary CPython execution and `ast.literal_eval` parsing;
2. the audited verifier source implementing the formulas described above;
3. Z3 and its Python bindings; and
4. the supplied certificate-template files.

The text files are model-template lists, not proof-producing UNSAT traces.
The verifier asks Z3 to prove the residual formulas unsatisfiable.  No DRAT,
LRAT, or proof-assistant certificate is exported, so a fully formalized
version would need a proof-producing CNF translation and checked UNSAT
proofs (or a theorem-assistant reconstruction).

Within that stated boundary, both maximal-component closures are correct.
The independent half-edge orbit enumeration, direct decoding of all 423
degree-nine model templates, exact quotient lift, and hand audit of every
color contraction remove the main risks of an incomplete symmetry class,
a malformed model, or an invalid coloring expansion.
