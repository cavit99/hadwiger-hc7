# Cold audit of the size-three marked Mader branch closure

**Verdict:** GREEN.

Audited source:
[`hc7_three_split_marked_mader_branch_closure.md`](hc7_three_split_marked_mader_branch_closure.md).

Source SHA-256:

```text
a2aab8482bd10039882e058f7f297989e19f97a6316aaeb2095622f070da8dfc
```

The minimal-contraction inheritance, path-packing alternative, Mader
obstruction, row-vector dichotomy, all seven values of `|W|`, and every
predecessor-dependent decoder have been checked end to end.  No row vector
or certificate type is omitted.

## 1. Minimal bad contraction inheritance

The three six-vertex model supports are pairwise disjoint.  Their split
edges therefore form a matching.  Contracting all three turns the four
singleton bags and each contracted edge bag into three pairwise disjoint
literal `K_5` cliques

\[
                         L_i=Q_i\cup\{z_i\}.
\]

Since the quotient is a minor of the `K_7`-minor-free graph `G`, it is
also `K_7`-minor-free.

The cited minimal-bad-contraction theorem applies exactly.  It gives:

* six-connectivity of `H`;
* every separator of order at most six has order six and contains all
  three contracted images; and
* for each `a`, the quotient obtained by leaving only `e_a` uncontracted
  is seven-connected.

The last item is not an additional assumption: contracting the other two
edges is a proper subset of the inclusion-minimal bad set.  These are
precisely the one-edge predecessors required by the balanced-three and
balanced-four/five decoders.  Vertex-disjoint supports also supply the
matching and disjoint endpoint hypotheses in those decoders.

## 2. Packing alternative

After shortening, each good path has two ends in two distinct named
cliques and no internal named-clique vertex.  Seven vertex-disjoint good
paths are seven disjoint connected branch bags.

Every good path has one of the three label pairs `12,13,23`.  Any two such
pairs intersect.  At a common label, disjointness of the paths gives two
distinct endpoint vertices in the corresponding literal clique, hence a
literal edge between the bags.  Thus all twenty-one branch-bag pairs are
adjacent.  A `K_7` model in the quotient expands to one in `G`.

Consequently absence of that packing legitimately invokes the
Robertson--Seymour--Thomas/Mader obstruction.  Choosing maximum `|W|` and
then maximum cell count is the same extremal choice used by the cited cut
reduction and balanced-cell decoders.  The budget gives

\[
                              0\le w=|W|\le6.
\]

## 3. Exhaustive row arithmetic

The marked cut reduction supplies disjoint rows satisfying

\[
 |B_i|\ge5-w,
 \qquad
 \sum_i|B_i|\le3(6-w).                         \tag{3.1}
\]

For `w<=5`, if every integer row order were at least `6-w`, the sum bound
would force all three orders to equal `6-w`.  Hence failure of balance
forces some row to have the only lower integer value `5-w`.  This is
exactly the deficient row used in the two unbalanced-collapse theorems.

For `w=6`, the sum upper bound itself forces every row to have order zero;
there is no separate unbalanced vector.  The source correctly treats this
case before invoking the `w<=5` dichotomy.

Thus the certificate space is partitioned as follows.

| `w` | Balanced discharge | Unbalanced discharge |
|---:|---|---|
| 0, 1 | low-`W` branch-set decoder in the marked cut reduction | low-`W` capacity closure |
| 2 | literal balanced-two decoder | unbalanced-row collapse |
| 3 | one-split balanced-three predecessor decoder | unbalanced-row collapse |
| 4, 5 | uniform one-split predecessor decoder | unbalanced-row collapse |
| 6 | marked six-cell exclusion | impossible already from (3.1) |

This table covers all integers from zero through six.

## 4. Scope of every cited discharge

### `w=6`

The cut-reduction theorem applies under six-connectivity,
`K_7`-minor-freeness, three disjoint marked cliques, and the all-marks
six-cut law, all inherited in Section 1.  Its binary-cut and cell-gateway
argument excludes this branch without predecessor data.

### Balanced `w=0,1`

The same reduction proves the balanced-cell incidence and literal
seven-bag decoder.  It uses only the marked quotient hypotheses already
available.

### Unbalanced `w=0,1`

The hash-pinned low-`W` audit checks that its capacity theorem needs only
the Mader budget, source rows and cell boundary axioms, six-connectivity,
and the marked-cut law.  It permits budget slack and proves `m<=2` before
the row/cell order contradiction.  No predecessor assumption is missing.

### Unbalanced `2<=w<=5`

The audited deficient-row collapse uses exactly (3.1), source row
separations, row disjointness, clique placement, and the marked-cut law.
It forces balance, contradicting the branch designation.

### Balanced `w=2`

The balanced-two theorem uses the exact normal form derived by the cut
reduction and constructs a literal `K_7` in `H`.  It requires no split
predecessor.

### Balanced `w=3,4,5`

The cut reduction supplies the exact balanced matrices, all three marks
in `W`, and all row tails.  The local lemmas inside the cited balanced-cell
decoders then derive connected large cells and full row packets from that
same maximal certificate.
For each supported mark, the graph `H_a` in the composition source is the
same seven-connected one-edge predecessor appearing in the decoder
statements.  The matching hypothesis holds.  The balanced-three decoder
therefore repairs its unique near-model defect, and the uniform
balanced-four/five decoder uses its clean row and one endpoint split.
Both produce literal `K_7` models in a minor of `G`.

## 5. Exact conclusion and boundary

Each certificate alternative either directly gives a `K_7` model in `H`
or in a one-edge predecessor, or is arithmetically impossible.  Every such
model is a minor of `G`, contradicting the standing exclusion.  Therefore
all three split edges cannot themselves be an inclusion-minimal bad
contraction set.

The composition does not address an inclusion-minimal bad set of order
two.  An order-one set still returns only the previously audited
exact-seven handoff.  The theorem also assumes the initial three
vertex-disjoint six-vertex models and therefore does not prove the global
support-six theorem or `HC_7`.
