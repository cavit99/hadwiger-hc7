# Independent audit: common-row promotion

## Verdict

**GREEN.**  Theorem 1 gives a literal seven-bag `K_7` model.  Every
connectivity, disjointness and adjacency claim follows from the exact
rotation datum and the three-carrier hypotheses.  Corollary 2 is an exact
specialization with `K={p}`.  The uniform count is also correct: with `r`
fixed rows the construction has `3+(r-1)=r+2` branch sets, one more than
the old foreign `K_{r+1}` model.

The square-antiprism shared-label barrier does not falsify the theorem.
It prevents the two endpoint carriers from being disjoint before the
middle-carrier adjacency conditions are considered.

## 1. Bag-by-bag audit

The proposed branch sets are

\[
 A=X\cup L,\qquad M=F_a\cup K,\qquad B=W\cup R,
 \qquad F_i\quad(i\ne a).                              \tag{A.1}
\]

There are exactly seven: three displayed unions and the four rows other
than `F_a`.

### Disjointness and nonemptiness

In the rotation datum, `X,Z,W,F_1,...,F_5` are pairwise disjoint: `Z`
and `W` are the two disjoint parts of the old donor `U`, which is disjoint
from `X` and the rows.  The sets `L,K,R` lie in `Z` and are
pairwise vertex-disjoint.  Hence all seven sets in (A.1) are pairwise
disjoint.  Every set is nonempty by hypothesis and by the branch-set
convention for the old model.

### Connectivity

* `A` is connected because `X,L` are connected and `E(X,L)` is nonempty.
* `M` is connected because `F_a,K` are connected and `E(F_a,K)` is
  nonempty.
* `B` is connected because `W,R` are connected and `E(W,R)` is nonempty.
* Every unchanged `F_i` remains connected.

No extension of `L,K,R` to a partition of all of `Z` is needed; unused
vertices may simply be deleted when taking the minor.

## 2. Complete adjacency table

Among the three promoted bags:

* `A-M` is witnessed by the literal `L-K` edge;
* `M-B` is witnessed by the literal `K-R` edge; and
* `A-B` is witnessed by the literal `X-W` edge in the audited rotation
  datum.

For an unchanged row `F_i`, `i!=a`:

* if `i!=b`, the old centre `X` meets `F_i`; if `i=b`, the carrier `L`
  meets `F_b`.  Thus `A` meets every unchanged row;
* if `i!=c`, the new centre `W` meets `F_i`; if `i=c`, the carrier `R`
  meets `F_c`.  Thus `B` meets every unchanged row; and
* `M` meets `F_i` through the original `F_a-F_i` clique-model edge.

Finally, any two unchanged rows retain their original clique-model edge.
This checks every pair among the seven branch sets and proves Theorem 1
without a quotient or an inferred portal edge.

The assumption that `a,b,c` are distinct is used exactly here: after
removing the promoted row `F_a`, the old endpoint has only the exclusive
missing row `F_b`, while the new endpoint has only `F_c`.  The theorem is
therefore genuinely the one-common-label cell

\[
                   D\cap E=\{a\}.
\]

## 3. Singleton corollary

If `P_a={p}`, then `p` has a literal neighbour in `F_a`; hence
`K={p}` is a nonempty connected `a`-carrier.  The hypotheses that both
`L` and `R` lie in `Z-p` and are disjoint give pairwise disjointness of
`L,{p},R`.  Their respective neighbours of `p` are precisely the two
edges required in (1.3).  Their contacts with `X,F_b` and `W,F_c` are
exactly (1.2).  Thus every hypothesis of Theorem 1 holds and Corollary 2
is **GREEN**.

This corollary does not require the common singleton to be copied into
both endpoint carriers: it is used only in the middle bag
`F_a union {p}`.

## 4. Square-antiprism falsification attempt

Use the audited barrier assignment

\[
 (\alpha,\beta,p,b,c)=(0,5,1,3,6),\qquad
 D=\{p,b\},\quad E=\{p,c\},
\]

in graph6 `GQyurg`.  The quadrilateral face

\[
                         (c,\alpha,\beta,b)=(6,0,5,3)
\]

puts the ends of an `alpha-b` path and a `beta-c` path in alternating
order.  Consequently there cannot be disjoint connected endpoint
carriers `L` meeting `alpha,b` and `R` meeting `beta,c`.  In particular
there cannot be three pairwise disjoint carriers `L,{p},R` satisfying
Theorem 1.  The barrier therefore lands in the theorem's explicit failure
branch; it is not a counterexample to its conclusion.

## 5. Uniform count and scope

Retain the full rotation-datum disjointness and contact assumptions with
`r>=3` fixed clique rows and distinct labels `a,b,c`.  Promoting `F_a`
replaces that row by `F_a union K`, so the output consists of

\[
  X\cup L,\quad F_a\cup K,\quad W\cup R,
  \quad r-1\text{ unchanged rows}.
\]

The total is `r+2`.  The old foreign clique model has one donor plus the
`r` rows, hence order `r+1`; the promoted model is one order larger, as
claimed.  The same adjacency table proves it is a `K_{r+2}` model.

The uniform paragraph is correct as a parameterized restatement of
Theorem 1.  Read as a standalone theorem it must retain the inherited
conditions that all bags are disjoint, all carriers lie in the connecting
donor, the two endpoint carriers touch their respective centres, and the
middle carrier touches both endpoint carriers.  The paragraph explicitly
or contextually records these duties and makes no stronger existence
claim.

## Trust boundary

The theorem proves only the implication

\[
  \text{three specified disjoint carriers}
  \Longrightarrow K_7.
\]

It does not derive those carriers from four-connectivity, split a crossed
rural page, compose portal orders across rotations, or manufacture a
proper-minor equality-state collision.  Those remain the proof-spine gap.
