# Audit of the eight-connected order bound

**Audited file:** `hc7_eight_connected_order_bound.md`
**Original audited SHA-256:**
`09fa807c7812c957c3fddb9a70c697b536e449307d76036f6dd99a2b12f0eec7`
**Promoted-candidate SHA-256:**
`8c862a302617f75e178bc2517ca0327891d2f45c58b8a8c4d1a157a89a26c4d3`
**Final promoted SHA-256:**
`6360ede972a3d12d403ad0fb204736743e866adbcd3bb589a9778bf55ef2d69b`
**Audit date:** 2026-07-17
**Verdict:** **GREEN.**  The promoted-candidate revision applies the three
source and scope repairs required by the first audit and makes no change to
the mathematical argument.

The final promoted copy differs from the re-audited candidate only in its
status paragraph and removal of a link to an unused exploratory solver.
The theorem statement and proof are unchanged.

## 1. Audited conclusion

The following conclusion is proved at the audited revision:

> Every eight-connected graph with no `K_7` minor has at least seventeen
> vertices.

The elementary complement lemma used in the proof is also correct:

> There is no seven-regular graph on sixteen vertices in which every
> nonadjacent pair has at least four common neighbours.

No computational claim is needed for either result.

## 2. External inputs

### 2.1 Mader's extremal bound

The numerical statement used in the proof is correct: a simple
`K_7`-minor-free graph on `n >= 7` vertices has at most `5n-15` edges.
Equivalently, `5n-14` edges force a `K_7` minor.  This is the `p=7` case of
Mader's theorem.

The bibliography in Section 6 of the original audited draft combined an
incorrect title with volume `172`.  The promoted candidate now gives the
correct source for the exact `p <= 7` theorem:

> W. Mader, *Homomorphiesätze für Graphen*, Math. Ann. **178** (1968),
> 154--168, DOI `10.1007/BF01350657`.

This exactly repairs the source defect.  The superseded coordinates also did
not correctly identify Mader's separate 1967 paper (which is in volume 174).

### 2.2 Jørgensen's equality classification

The scope quoted in Section 2 agrees with the established classification:
the `K_7`-minor-free graphs with `5n-15` edges are the 5-clique-sums
(5-cockades) of edge-maximal 2-apex graphs, together with
`K_{2,2,2,3}`.  The cited primary source is:

> L. K. Jørgensen, *Extremal graphs for contractions to K7*, Ars Combin.
> **25C** (1988), 133--148.

The consequences drawn from the classification are valid:

- a nontrivial 5-clique-sum has a vertex cut of order five;
- `K_{2,2,2,3}` has connectivity six (and order nine);
- an edge-maximal 2-apex graph has minimum degree at most seven unless its
  order is at most eight, in which case it is not eight-connected either.

For the last point, fix an apex set of size at most two.  When the planar
remainder has at least seven vertices it has a vertex of degree at most five,
and that vertex has degree at most seven in the original graph.  This proves
Lemma 2.1: an eight-connected `K_7`-minor-free graph has at most
`5n-16` edges.

### 2.3 Bounds used only in Section 5

The numerical checks there are correct: on fourteen vertices,
`K_6`-minor-free graphs have at most `4n-10=46` edges, and
`K_5`-minor-free graphs have at most `3n-6=36` edges.  The promoted candidate
now identifies these as the `p=6` and `p=5` cases of the correctly cited
Mader theorem.

## 3. Line-by-line audit of the complement lemma

Fixing `v`, the sets have the asserted sizes: `|A|=7` and `|B|=8`.
For `b in B`, the common neighbours of `v` and `b` all lie in `A`, so
`|N(b) intersect A| >= 4` and `d_F(b) <= 3`.

If `a=|E(L)|`, then each `x in A` has `6-d_L(x)` neighbours in `B`.
Consequently

```text
e(A,B)=42-2a,
2e(F)=56-e(A,B)=14+2a,
e(F)=7+a.
```

Since every `F`-degree is at most three, `e(F)<=12`, hence `a<=5`.

The proof that `L` has no isolated vertex is correct.  Such a vertex `x`
would have six neighbours and two nonneighbours in `B`; for either chosen
nonneighbour `b`, all common neighbours of `x,b` would have to lie among the
at most three `F`-neighbours of `b`.  Thus `a>=4`.

When `a=4`, positivity of all seven `L`-degrees and degree sum eight forces
degree sequence `(2,1,1,1,1,1,1)`.  Equation (3.2) gives `F`-degree sum 22,
and the upper bound three leaves exactly the two listed possibilities:

- `(3,3,3,3,3,3,3,1)`; or
- `(3,3,3,3,3,3,2,2)`.

For every `b in B`, regularity gives
`|A-N(b)|=d_F(b)`.  If `x` is one of those nonneighbours, then a common
neighbour of `x,b` is either an `L`-neighbour of `x` or an `F`-neighbour of
`b`, so

```text
4 <= |N(x) intersect N(b)| <= d_L(x)+d_F(b).
```

An `F`-degree-one vertex would require an `L`-degree at least three.  An
`F`-degree-two vertex has two distinct nonneighbours in `A`, both of which
would have to be the unique `L`-degree-two vertex.  Both alternatives are
impossible.  Hence `a` is not four.

The original choice of `v` was arbitrary, so `a=5` at every vertex.  Thus
every vertex is incident with exactly five triangles.  The triangle-incidence
sum would be `16*5=80`, which cannot equal three times an integer.  This
correctly completes the complement lemma.

## 4. Audit of the order-sixteen exclusion

Eight-connectivity gives `m>=4n`; Lemma 2.1 gives `m<=5n-16`; hence
`n>=16`.  If `n=16`, equality throughout gives `m=64` and eight-regularity.

For an edge `xy` lying in `t` triangles, simplification after contraction
removes the edge `xy` and one duplicate from each of the `t` common
neighbours, so

```text
|E(G/xy)|=64-1-t=63-t.
```

Mader's order-fifteen bound is 60, and therefore `t>=3`.

If `t=3`, then `G/xy` is an equality graph.  Contracting an edge in an
eight-connected graph leaves a seven-connected graph: a separator of order
at most six in the contraction lifts to one of order at most seven in the
original graph.  Jørgensen's nontrivial 5-sums and exceptional graph are
therefore excluded, leaving an edge-maximal 2-apex graph.

At order fifteen, the 2-apex edge bound is

```text
(3*13-6) + 2*13 + 1 = 60.
```

Equality forces the two apex vertices to be adjacent and universal and the
thirteen-vertex planar remainder to be a triangulation.  The contracted
vertex has degree `8+8-2-3=11`, so it is not an apex.  Each universal apex
lifts to a vertex adjacent to all thirteen unchanged vertices and to at
least one endpoint of the contracted edge, hence has degree at least
fourteen in `G`, contradicting eight-regularity.  Thus every edge lies in at
least four triangles.

The complement of `G` is seven-regular.  For an edge `xy` of `G` (a
nonedge of the complement), the two common-neighbour counts in `G` and its
complement are equal:

```text
|N_G(x) intersect N_G(y)|
 = 14-|N_H(x) union N_H(y)|
 = |N_H(x) intersect N_H(y)|.
```

The complement lemma now gives the required contradiction.  Therefore the
inference `n>=17` is valid.

## 5. Computation and novelty check

The audit did not rely on computation.  A supplemental direct Z3 feasibility
check of the sixteen-vertex complement formulation was attempted but did not
finish within the allotted run, so it has no evidentiary status.

A targeted literature search located the Mader and Jørgensen extremal inputs
and later summaries of their equality cases, but did not locate the stated
order-seventeen corollary or the `(16,7,4)` complement lemma.  This is not a
novelty proof.  The result should be described as a new deduction in this
repository unless and until a broader literature review establishes priority.

## 6. Promoted-candidate revision check

Comparison with the original audited revision confirms that the candidate:

1. replaces the incorrect Mader reference with the 1968 Math. Ann. 178
   source above;
2. replaces the broad phrase “all of the model-theoretic conditions” by the
   exact conclusions proved from the edge counts: a `K_6` minor after
   deleting an adjacent pair and a `K_5` minor after deleting any pair, with
   an explicit warning that no colouring, rooting, or label-preserving
   conclusion follows; and
3. attributes the exact `K_5`, `K_6`, and `K_7` edge bounds to the `p=5,6,7`
   cases of Mader's theorem.

Apart from the title/status wording needed to record this audit, those are
the only changes.  The theorem statement, complement lemma, extremal
equality argument, and order-sixteen contradiction are mathematically
unchanged.  The promoted-candidate hash above is therefore audited
**GREEN**.
