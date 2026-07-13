# Adversarial audit of the sole-exterior infinite-family closures

Audited source: `hadwiger_moser_one_component_infinite_classes.md`.

## Verdict

The branching-cutvertex theorem, six-shore path theorem, and tree-exterior
corollary are sound.  The full verifier was replayed successfully:

```text
branching cases verified: 512
path maximal-system orbits verified directly: 3158 distinct-end + 686 equal-end
path injections excluded in counterexample encoding: 5040
path representative counterexample formula: UNSAT
```

## Branching cutvertex

If \(A_i\) is a component of \(C-z\), then every neighbor outside \(A_i\)
lies in \(N\cup\{z\}\).  The set

\[
  N_N(A_i)\cup\{z\}
\]

separates \(A_i\) from another component of \(C-z\) and from \(v\).
Seven-connectivity therefore gives \(|N_N(A_i)|\ge6\), exactly the claimed
one-vertex boundary defect.

For the bags \(B_i=A_i\cup\{x_i\}\):

* \(x_i\notin D_i\) proves connectivity;
* absence of mutual incidence proves adjacency between two shore bags;
* a missed triangle vertex is joined through the anchor edge \(tx_i\);
* all anchors are distinct and outside the triangle; and
* every bag meets \(N\), so the singleton \(v\) completes the model.

No hidden assumption that \(z\) has only one neighbor in a component is
used.

## Path separator bounds

For six consecutive nonempty subpaths \(A_1,\ldots,A_6\):

* an endpoint block has at most one neighbor in \(C-A_i\);
* an internal block has at most two;
* vertices of \(C\) have no edge to \(v\), by \(C=G-N[v]\); and
* the displayed external neighborhood separates \(A_i\) from \(v\).

Thus seven-connectivity gives boundary defects at most one at the ends and
at most two internally.  Since \(N_G(C)=N\), every boundary vertex sees at
least one block, which is exactly
\(\bigcap_i S_i=\varnothing\).

## Representative encoding

The Z3 verifier uses the correct 42 membership variables and cardinality
bounds.  For each of the \(7P6=5040\) injections, its invalidity clause is

1. an assigned representative lies in its own defect; or
2. a pair of rows at distance at least two is mutually incident.

Consecutive row pairs are correctly excluded because their shores already
have a path edge.  Requiring every injection to be invalid and obtaining
`UNSAT` is precisely the negation of the representative lemma.

The independent maximal-system reduction is also valid.  Endpoint defects
can be enlarged to singletons and internal defects to pairs while preserving
empty intersection.  If the endpoint singletons differ, this is immediate;
if both equal \(\{a\}\), an original internal defect omits \(a\), and it can
be enlarged to a pair still omitting \(a\).

## Tree corollary

Earlier certified results give \(|C|\ge6\).  A connected tree with a vertex
of degree at least three is covered by the branching theorem.  A connected
tree of maximum degree at most two is a path and is covered by the
six-shore theorem.  Hence every surviving sole exterior contains a cycle.
