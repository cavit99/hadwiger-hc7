# Terminal-edge contraction in a Mader delta-matroid

**Status:** proved and independently internally audited in
[`hc7_mader_terminal_contraction_projection_audit.md`](hc7_mader_terminal_contraction_projection_audit.md).
This note gives a common linear representation for the Mader endpoint
systems of a graph and the quotients obtained by contracting specified
terminal edges.  It does not yet prove the support-height exchange or
`HC_7`.

## 1. Mader endpoint systems

Let `G` be a graph, let `T` be a set of terminals, and let
`\mathcal T` be a partition of `T`.  A `\mathcal T`-path has its endpoints
in different parts of `\mathcal T` and has no internal terminal.  A set
`S\subseteq T` is **feasible** when `G` has a collection of pairwise
vertex-disjoint `\mathcal T`-paths whose endpoint set is exactly `S`.

Wahlström proves that the feasible subsets of `T` form a linearly
representable delta-matroid.  The result below identifies the exact effect
of contracting an edge whose endpoints are terminals in the same part.

## 2. The graph operation

### Theorem 2.1 (terminal-edge contraction projection)

Let `xy` be an edge of `G` with `x,y\in T` in the same part of
`\mathcal T`.  Contract `xy` to a vertex `z`, put

\[
 T'=(T-\{x,y\})\cup\{z\},
\]

and replace `x,y` by `z` in their part of the terminal partition.  Let
`D` and `D'` be the Mader endpoint delta-matroids of the original and
contracted networks.  For every `R\subseteq T'`:

1. if `z\notin R`, then `R` is feasible in `D'` if and only if `R` is
   feasible in `D`; and
2. if `z\in R`, then `R` is feasible in `D'` if and only if at least one
   of

   \[
      (R-\{z\})\cup\{x\},\qquad
      (R-\{z\})\cup\{y\}
   \]

   is feasible in `D`.

#### Proof

Suppose first that `z\notin R`.  Every path in a packing with endpoint
set `R` in the contracted network avoids `z`, because `z` is a terminal
and is not one of the endpoints.  The same paths therefore exist in
`G-\{x,y\}`.  Conversely, a packing in the original network with endpoint
set `R` avoids both unused terminals `x,y`; it survives the contraction
unchanged.

Now suppose that `z\in R`.  Exactly one path in a corresponding packing
has endpoint `z`.  Its unique incident path edge at `z` is the image of an
edge incident with `x` or with `y`.  Replace the endpoint `z` by that
endpoint of `xy`.  All other paths avoid `z`, and hence lift while avoiding
both `x` and `y`.  This gives one of the two displayed feasible sets in
the original network.

Conversely, a packing using exactly one of `x,y` as an endpoint avoids the
other one, since every unused terminal is forbidden as an internal vertex.
Contracting `xy` therefore maps the unique path ending at `x` or `y` to a
path ending at `z`, without creating an intersection with another path.
This proves both directions.  \(\square\)

## 3. Linear representation

The preceding operation has an explicit representation that does not
require recomputing the Mader delta-matroid.

### Theorem 3.1 (two-to-one skew-matrix projection)

Let an even delta-matroid `D` on ground set `E` be directly represented by
a skew-symmetric matrix `A` over a field `\mathbb F`.  Fix distinct
`x,y\in E`, introduce a new element `z`, and work over the rational-function
extension `\mathbb F(\alpha,\beta)`, where `\alpha,\beta` are algebraically
independent.

After ordering `x,y` before the other elements, define a skew-symmetric
matrix `B` on `(E-\{x,y\})\cup\{z\}` by

\[
 B[u,v]=A[u,v]
 \quad(u,v\not=z),
 \qquad
 B[z,u]=\alpha A[x,u]+\beta A[y,u].                 \tag{3.1}
\]

Then `B` directly represents the set system in Theorem 2.1: a set not
containing `z` is feasible precisely when it was feasible in `D`, while a
set `U\cup\{z\}` is feasible precisely when at least one of
`U\cup\{x\}` and `U\cup\{y\}` is feasible in `D`.

#### Proof

For a set not containing `z`, the corresponding principal submatrix of
`B` is the identical principal submatrix of `A`.

Consider `U\cup\{z\}`.  If its order is odd, its skew-symmetric principal
matrix is singular, and the two comparison sets also have odd order.  If
its order is even, expand the Pfaffian along the first row and column,
which is indexed by `z`.  With `x,y,z` placed before the common ordering
of `U`, multilinearity gives

\[
 \operatorname{Pf} B[U\cup\{z\}]
   =\alpha\,\operatorname{Pf} A[U\cup\{x\}]
    +\beta\,\operatorname{Pf} A[U\cup\{y\}].          \tag{3.2}
\]

The two coefficients lie in the original field (or its existing
representation extension), while `\alpha,\beta` are algebraically
independent.  Hence the right-hand side is nonzero exactly when at least
one coefficient is nonzero.  A skew-symmetric even-order matrix is
nonsingular exactly when its Pfaffian is nonzero.  This proves the claimed
feasibility rule.  \(\square\)

### Corollary 3.2 (one master representation for several contractions)

Let `x_i y_i` (`i\in I`) be pairwise vertex-disjoint edges, with the two
ends of each edge lying in one terminal part.  Starting from one direct
representation `A`, adjoin, for every `i`, a new row and column `z_i`
equal to an independent generic linear combination

\[
       z_i=\alpha_i x_i+\beta_i y_i.                  \tag{3.3}
\]

Retain the original rows and columns as well.  For every subset
`J\subseteq I`, the principal-matrix slice which

- retains `z_i` and omits `x_i,y_i` for `i\in J`; and
- retains `x_i,y_i` and omits `z_i` for `i\notin J`

represents the Mader endpoint system of the quotient obtained by
contracting exactly the edges indexed by `J`.

#### Proof

Apply Theorems 2.1 and 3.1 successively.  The contractions commute.  In
the master matrix, an entry between two new elements is the corresponding
bilinear combination of the four old entries.  Every choice of one old
endpoint for each new element has a distinct monomial in the independent
variables, so the Pfaffian is nonzero exactly when at least one lifted
endpoint choice is feasible.  \(\square\)

## 4. Exact contribution to the `HC_7` programme

For three disjoint six-vertex `K_5` models, take all model vertices as
terminals and partition them by model.  Corollary 3.2 puts the Mader
endpoint systems of the fully split graph, the three one-split
predecessors, and the fully contracted three-clique quotient into slices
of one represented even delta-matroid.  It therefore removes one genuine
formal obstruction: these endpoint systems need not be treated as
unrelated black boxes.

What remains is not automatic symmetric exchange.  A legal slice imposes
an all-or-nothing choice at every triple `\{x_i,y_i,z_i\}`.  An arbitrary
delta-matroid exchange may select both an old endpoint and its projected
element, or may move to a slice that does not correspond to any graph in
the contraction chain.  Moreover:

- endpoint feasibility records neither the pairing of endpoints nor the
  internal vertices of the paths;
- the paths used in the common edge-deletion argument join two terminals
  in the same model, whereas a Mader path joins different terminal parts;
- palette and Kempe-component information is absent; and
- the already proved three-edge minimal-contraction closure means that the
  immediate live application is the two-edge/eight-boundary residue, not
  a reproof of the closed branch.

The next algebraic target is therefore the following deliberately narrow
question.

> **Slice-preserving exchange target.**  Under the graph-specific
> seven-connectivity, contraction-criticality, and `K_7`-minor exclusion
> hypotheses, does symmetric exchange between feasible sets in two legal
> slices yield a feasible set in a third legal slice, or a principal-rank
> obstruction whose graph interpretation is a model-preserving
> order-seven separation?

A negative answer with no additional graph structure terminates the
delta-matroid route.  A positive answer would supply the first common
label-preserving exchange language for the split predecessors.

## 5. Source and trust boundary

The external input is Magnus Wahlström, *Representative set statements for
delta-matroids and the Mader delta-matroid*, arXiv:2306.03605v2 (2025),
especially the linear representability theorem for Mader endpoint sets.

Theorems 2.1 and 3.1 above are new deductions in this repository and have
passed a separate internal audit.  That audit is not external peer review.
The theorems do not assert the slice-preserving exchange target and do not
prove a new case of Hadwiger's Conjecture.
