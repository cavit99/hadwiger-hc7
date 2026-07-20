# The two-vertex path-column laboratory is four-colourable

**Status:** computer-assisted finite result; separately audited **GREEN** in
[`hc7_pentagonal_bipyramid_two_vertex_path_census_audit.md`](hc7_pentagonal_bipyramid_two_vertex_path_census_audit.md).

## Theorem

Let `P` be the pentagonal bipyramid, with poles `0,1` and cyclic rim
`2,3,4,5,6`.  Let `F` have fourteen vertices

\[
                         \{x_0,x_1:x\in V(P)\}.
\]

Assume:

1. every \(x_0x_1\) is an edge and these are the only edges within a
   two-vertex column;
2. two columns have at least one edge between them exactly when their
   labels are adjacent in `P`;
3. `F` is five-connected;
4. no internal column edge has a four-distinct-label alternating attachment
   pattern in the plane rotation of `P`; and
5. all five adjacent-rim linkage instances from
   `hc7_pentagonal_bipyramid_adjacent_rim_linkage.md` are negative.

Then `F` is four-colourable.

This is a finite theorem about the first repeated-contact path-column
laboratory.  It is not an unbounded expansion theorem and does not prove
`HC_7`.

## Verification method

The verifier represents the sixty possible intercolumn edges by Boolean
variables.  It imposes:

- a nonempty edge bundle on every edge of `P`;
- minimum degree at least five (a redundant consequence of
  five-connectivity);
- all no-alternation constraints; and
- the failure of every adjacent-rim linkage, by enumerating the two
  vertex-disjoint simple paths on the four vertices in the relevant pair
  of columns.

It then uses two sound counterexample-guided cuts.

### Connectivity cut

If a candidate has a vertex cut `S` of order below five and `D` is a
component of `F-S`, every five-connected graph must contain an edge from
`D` to `V(F)-(S union D)`.  The verifier adds the disjunction of all allowed
such edges.  This can exclude no five-connected graph.

### Colouring cut

If a five-connected candidate has a proper four-colouring `c`, any graph
for which `c` is not proper must contain an allowed edge whose ends have
the same `c`-colour.  The verifier adds the disjunction of all such edges.
Every non-four-colourable graph satisfies this disjunction, so this cut can
exclude no counterexample to the theorem.

The process terminates with an exact `unsat` answer.  Therefore no graph
satisfying hypotheses 1--5 is non-four-colourable.

Run:

```bash
python3 results/hc7_pentagonal_bipyramid_two_vertex_path_census_verify.py
```

Expected final output:

```text
pentagonal-bipyramid two-vertex path census: PASS
```

## Trust boundary

The verifier does not bound larger path or tree columns.  It does not
replace five-connectivity by minimum degree: connectivity is checked
exactly, and the minimum-degree constraints only accelerate the search.
It also does not infer planarity; the conclusion is the exact colouring
statement needed by the spanning-root application.
