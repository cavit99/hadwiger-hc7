# Barrier to statically enriched Mader delta-matroid exchange

**Status:** written counterexample with a separate GREEN internal audit in
[`hc7_labelled_mader_delta_enrichment_barrier_audit.md`](hc7_labelled_mader_delta_enrichment_barrier_audit.md).
This note does not satisfy the
hypotheses of a hypothetical counterexample to `HC_7`, does not refute
`HC_7`, and does not rule out a new invariant that couples path witnesses
to the host graph.

## 1. Scope

Let a Mader network consist of a graph `H`, a terminal set `T`, and a
partition of `T`.  A Mader path has endpoints in different parts of the
partition and has no internal terminal.  The feasible endpoint sets of
pairwise vertex-disjoint Mader paths form a linearly representable
delta-matroid.

This note proves four limitations.

1. Even when a network contains a labelled six-vertex `K_5` model, the
   corresponding contracted `K_5`, and a prescribed replacement path for
   its two-vertex branch set, symmetric exchange between the split and
   contracted endpoint systems may have no graph-realizable outcome.
2. A fixed twist does not remove this obstruction.  A direct sum, or a
   delta-sum on disjoint ground sets, with a static auxiliary delta-matroid
   does not remove it either.
3. Any invariant obtained only from the Mader endpoint delta-matroid by
   fixed twists, minors, projections, or combinations with fixed auxiliary
   systems cannot recover edges and paths to which the endpoint system is
   insensitive.
4. Delta-matroid parity imposed only on endpoint sets does not prescribe
   which terminal pairs are joined by the paths.

Here **static** means that the same auxiliary feasible set is attached to
the two endpoint sets being compared.  The result does not concern a new
coupled representation in which auxiliary elements encode the actual path
witnesses and change together with them.

## 2. A labelled split-`K_5` example

### Proposition 2.1 (only the mixed exchange is feasible)

There is a graph with a labelled six-vertex `K_5` model, a labelled
contraction edge, and a replacement path for that edge, for which two
feasible endpoint sets in the split and contracted Mader networks have no
symmetric exchange that belongs to either graph-realizable contraction
slice.

### Construction

Let

\[
 Q=\{q_1,q_2,q_3,q_4\},\qquad
 A=Q\cup\{x,y\},\qquad B=\{b_1,b_2\}.
\]

The terminals are `A union B`, with terminal partition `A | B`.  Add one
nonterminal vertex `u`.  The edge set consists of

\[
 \binom Q2\;\cup\;\{xy\}\;\cup\;\{xq:q\in Q\}
 \;\cup\;\{xb_1,yb_2,xu,uy\}.                         \tag{2.1}
\]

Thus the four singleton branch sets `q_1,...,q_4` and the two-vertex
branch set `\{x,y\}` form a labelled `K_5`-minor model.  Contracting `xy`
to `z` makes `Q union \{z\}` a `K_5` subgraph.  After deleting `xy`, the
path `x-u-y` is a prescribed replacement path for the two-vertex branch
set.

Use the common representation of the split and contracted Mader endpoint
systems, with the projected element

\[
                         z=\alpha x+\beta y,            \tag{2.2}
\]

where `alpha,beta` are algebraically independent.  A graph-realizable
split restriction retains `x,y` and omits `z`; a graph-realizable
contracted restriction retains `z` and omits `x,y`.

In the split network,

\[
                         F=\{x,y,b_1,b_2\}              \tag{2.3}
\]

is feasible, witnessed by the disjoint one-edge paths `xb_1` and `yb_2`.
In the contracted network,

\[
                         C=\{z,b_1\}                    \tag{2.4}
\]

is feasible, witnessed by `zb_1`.

### Proof

The symmetric difference of (2.3) and (2.4) is

\[
                         F\mathbin\triangle C
                              =\{x,y,z,b_2\}.           \tag{2.5}
\]

Apply symmetric exchange to `F` at `x`.  The possible second elements in
(2.5) give the following sets:

\[
\begin{array}{c|c|c}
v & F\mathbin\triangle\{x,v\} & \text{conclusion}\\
\hline
x & \{y,b_1,b_2\} & \text{infeasible: odd order},\\
y & \{b_1,b_2\} & \text{infeasible: both terminals lie in }B,\\
b_2 & \{y,b_1\} & \text{infeasible: there is no Mader }y\text{--}b_1
                       \text{ path},\\
z & \{y,z,b_1,b_2\} & \text{feasible, but in neither graph slice}.
\end{array}                                                   \tag{2.6}
\]

For the last row, the projected element `z` lifts through `x`, recovering
the two paths witnessing `F`.  The resulting set contains both an old
terminal `y` and the projected terminal `z`, so it is not an endpoint set
of either the split network or the contracted network.

The extra labelled structure in (2.1) does not change this calculation.
An edge with both ends in the terminal part `A` cannot lie in a Mader
path.  Nor can a Mader path use `x-u-y`: because `u` has degree two, such
a path contains both `x` and `y`; it either has same-part endpoints or has
an internal terminal.  Finally, the apparent walk `y-u-x-b_1` is not a
Mader path because `x` is an internal terminal.  Hence the third row of
(2.6) remains infeasible.  This proves the proposition. \(\square\)

### Corollary 2.2 (the legal union is not a delta-matroid)

Let `D*` be the common represented endpoint delta-matroid, and retain only
its feasible sets contained either in the split ground set or in the
contracted ground set.  This retained family is not a delta-matroid.

### Proof

The sets `F,C` belong to the retained family, while (2.6) shows that the
symmetric exchange axiom fails for `F,C,x`. \(\square\)

This is the exact obstruction to treating the all-or-nothing contraction
choice as a parity filter and then applying ordinary delta-matroid
exchange inside the filtered solutions.

## 3. Three labelled models and static enrichments

### Proposition 3.1 (three-copy form)

Take three vertex-disjoint copies of the construction in Section 2, with
labelled edges `x_i y_i`, labelled four-cliques `Q_i`, and replacement
paths `x_i-u_i-y_i`.  The graph has three vertex-disjoint labelled
six-vertex `K_5` models and the three corresponding contracted `K_5`
subgraphs.  In the common endpoint representation for all subsets of the
three contractions, the obstruction of Proposition 2.1 persists.

### Proof

Use `F` and `C` from one copy and the same feasible endpoint set, for
example the empty set, in each of the other two copies.  The symmetric
difference is confined to the first copy, so (2.6) applies unchanged.
\(\square\)

The three-copy graph is deliberately disconnected and is not asserted to
be an `HC_7` counterexample.  It shows that the presence of exactly three
labelled split models does not repair the formal exchange law.

### Proposition 3.2 (fixed twists and static direct sums)

The obstruction in Proposition 2.1 survives each of the following.

1. Apply one fixed twist to the common endpoint delta-matroid and twist the
   definition of the two legal slices by the same set.
2. Take a direct sum with any auxiliary delta-matroid on a disjoint ground
   set and attach the same auxiliary feasible set to `F` and `C`.
3. Take the delta-sum with such a disjoint static auxiliary system.  On
   disjoint ground sets this has the same setwise effect on the selected
   feasible sets as the direct sum.

### Proof

For a fixed twist set `X`, the two compared sets become `F triangle X`
and `C triangle X`.  Their symmetric difference is still `F triangle C`,
and

\[
 (F\mathbin\triangle X)\mathbin\triangle\{x,v\}
   =(F\mathbin\triangle\{x,v\})\mathbin\triangle X.  \tag{3.1}
\]

Thus feasibility and legality of every candidate correspond bijectively
to the four rows of (2.6).

For a direct sum, let `R` be the same auxiliary feasible set attached to
both endpoint sets.  Then

\[
 (F\cup R)\mathbin\triangle(C\cup R)=F\mathbin\triangle C. \tag{3.2}
\]

The symmetric exchange axiom therefore permits no auxiliary element as
the second exchanged element.  Feasibility in the auxiliary factor stays
fixed at `R`, and the endpoint factor is exactly (2.6).  The disjoint
delta-sum case is identical. \(\square\)

In particular, a graphic matroid or another edge-label structure placed
in a separate direct-sum factor may record the four-clique and replacement
path as static data, but it does not couple those data to the path packing
used by the endpoint exchange.

## 4. Endpoint-derived operations cannot recover hidden labels

### Proposition 4.1 (information loss)

There are pairs of labelled networks having the same Mader endpoint
delta-matroid such that one has the designated internal four-clique, or
the designated same-part replacement path, and the other does not.
Consequently, no invariant that is a function only of the Mader endpoint
delta-matroid can retain those properties.  This includes invariants
obtained by any fixed sequence of twists, deletions, contractions,
projections, unions, or delta-sums with auxiliary systems that do not
themselves contain the missing host information.

### Proof

Starting from (2.1), delete one edge of `Q`, or delete the two edges of
`x-u-y`.  Deleting an edge of `Q` changes only an edge whose two ends are
terminals in the same part.  No Mader path can use such an edge.  As shown
in the proof of Proposition 2.1, no Mader path can use either edge of the
degree-two same-part path `x-u-y`.  The feasible endpoint family is
therefore unchanged, although the indicated labelled property changes.

A fixed operation applied to identical input delta-matroids has identical
output.  Hence endpoint-derived minors and projections cannot reconstruct
the lost property.  If an operation deletes or contracts one of the
distinguished endpoint labels themselves, it has discarded rather than
preserved the labelled split-model problem. \(\square\)

This proposition does not say that a coupled auxiliary representation is
impossible.  It says that the coupling cannot be manufactured from the
endpoint delta-matroid after the same-part information has been discarded.

## 5. Endpoint parity does not prescribe path pairing

### Proposition 5.1 (four-cycle pairing obstruction)

There is a graph for which a feasible Mader endpoint set is a union of two
prescribed parity blocks although no path packing realizes the pairing
specified by those blocks.

### Proof

Let the graph be the cycle

\[
                         1-2-3-4-1,
\]

and make all four vertices terminals in four singleton terminal parts.
The endpoint set `\{1,2,3,4\}` is feasible, witnessed by the disjoint
edges `12` and `34`.  It is a union of the prescribed parity blocks

\[
                         \{1,3\},\qquad\{2,4\}.        \tag{5.1}
\]

However, there are no vertex-disjoint paths joining `1` to `3` and `2` to
`4`: every `1`--`3` path on the cycle contains `2` or `4`, an endpoint of
the other required path.  Thus parity of the endpoint set constrains which
terminals occur, not which terminal pairs are joined. \(\square\)

Linear delta-matroid parity algorithms therefore do not, without an
additional witness-level encoding, supply the same-model pairings required
by the labelled minor construction.

## 6. Consequence for the support-six programme

The common Mader representation remains useful for comparing endpoint
feasibility before and after terminal-edge contractions.  The results above
show that the following additions do not by themselves turn that comparison
into the required labelled exchange:

- a fixed twist or endpoint-derived minor/projection;
- an all-or-nothing filter retaining only graph-realizable contraction
  slices;
- a separate graphic or label delta-matroid attached by direct sum or
  disjoint delta-sum; or
- parity blocks imposed only on endpoint sets.

What remains unruled out is a genuinely coupled object whose feasible
elements retain actual path pairings, path interiors, and branch-set
adjacencies, together with a new exchange theorem using seven-connectivity,
contraction-critical colouring data, or `K_7`-minor exclusion.  The present
counterexamples also do not rule out a graph-specific theorem showing that
the mixed exchange can always be normalized in the exact `HC_7` host.

The external algebraic background is Wahlström, *Representative set
statements for delta-matroids and the Mader delta-matroid*,
arXiv:2306.03605, for the Mader endpoint representation; Geelen, Iwata and
Murota, *The linear delta-matroid parity problem*, J. Combin. Theory Ser. B
88 (2003), 377--398; and Koana and Wahlström, *Faster algorithms on linear
delta-matroids*, arXiv:2402.11596, for projected linear delta-matroids and
parity operations.  No theorem from those papers is claimed to assert the
failed labelled exchange considered here.
