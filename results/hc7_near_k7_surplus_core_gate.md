# Surplus roots: transferable components or canonical portal gates

## Status

This attacks the three obstructions left by the surplus-root transfer
theorem without enumerating portal orders.  Inside a neutral donor, retain
one protected adhesion root and one literal portal to every other clique
bag.  Any surplus root outside this connected row core either lies in a
piece transferable to a twin, or lies behind an actual order-at-least-
seven adhesion missing at least one twin.  If a surplus root cannot be
excluded from any row core, it canonically defines a detachable gate
which owns an entire foreign-row portal class.

Thus “portal locked” has an exact graph-theoretic meaning: it is either a
nested adhesion or a multi-owner cut gate.  This is uniform in the clique
order.  The theorem does not yet show that all such gates have one global
plane expansion.

## 1. Retained row cores

Let `F_1,...,F_m` be a clique model and fix one donor bag `U=F_i`.
For every `j!=i`, let

\[
                     P_j=N_U(F_j)                         \tag{1.1}
\]

be its nonempty literal portal set.  Let `R subset U` be a nonempty set
of marked roots and choose one protected root `r in R`.

A **retained row core** is a connected set `T subseteq U` containing `r`
and meeting every `P_j`.

### Lemma 1 (components outside a row core have no monopoly)

Let `T` be a retained row core and let `K` be a component of `G[U-T]`.
Then `K` and `U-K` are connected and

\[
                           \Omega_U(K)=\varnothing.       \tag{1.2}
\]

Consequently, if `K` contains a surplus root and has an edge to a target
bag `F_j`, it is transferable from `U` to `F_j` in the sense of the
surplus-root transfer theorem.

### Proof

The component `K` is connected.  Every component of `U-T` has an edge to
the connected set `T`, since `U` is connected.  Hence `U-K`, consisting
of `T` and all the other components attached to it, is connected.

For every row `F_j`, the core contains a member of `P_j`; therefore
`U-K` retains an actual `U-F_j` edge.  No row is monopolized by `K`,
proving (1.2).  If `K` meets `F_j`, all three transfer conditions hold.
\(\square\)

### Lemma 2 (a non-target outside component exposes an adhesion)

Use the exact-seven `HC_7` frame with twin targets `B,C`, and let `K` be
a component outside a retained row core which contains a surplus root.
If `K` is anticomplete to at least one of `B,C`, then `N_G(K)` is an actual vertex
separator of order at least seven.  If its order is seven, every boundary
vertex is full to every component of `G-N_G(K)`.

### Proof

The connected nonempty set `K` lies on one side.  Any twin bag missed by
`K` is disjoint from `K union N_G(K)` and supplies a nonempty far side.
Hence `N_G(K)` is an actual separator.  Seven-connectivity gives its order.
At equality, the standard minimum-cut argument applies: if one cut
vertex missed one component, deleting the other six would separate that
component. \(\square\)

Combining Lemmas 1--2 gives a complete conclusion for every surplus root
outside a chosen row core: it either meets both twins and transfers freely
to either one, or it exposes a nested faithful adhesion.

## 2. Avoidable roots and unavoidable gates

Call a surplus root `s in R-{r}` **core-avoidable** if some retained row
core avoids `s`, and **core-unavoidable** otherwise.  This definition is
made separately for each root; no cardinal-minimal core is assumed.

If `s` is core-avoidable, choose a core `T_s` avoiding it and let `K_s`
be the component of `U-T_s` containing `s`.  Lemmas 1--2 give the exact
alternative:

* if `K_s` meets `B` or `C`, it is freely transferable to every twin it
  meets; or
* if it misses either twin, it exposes an actual nested adhesion.

### Theorem 3 (canonical gate at an unavoidable surplus root)

Let `s in R-{r}` be core-unavoidable.  Let `C_s` be the component of
`G[U-s]` containing `r`, and put

\[
                         Z_s=U-C_s.                       \tag{2.2}

Then:

1. `Z_s` and `C_s` are nonempty connected sets and `s in Z_s`;
2. some row portal set `P_j` is disjoint from `C_s`; equivalently
   `j in Omega_U(Z_s)`; and
3. `Z_s` is a canonical detachable surplus-root gate.  If it is
   transferable to `B` or `C`, the surplus-root exchange applies.
   Otherwise, for every twin target met by `Z_s`, its monopoly set
   contains a different row as well.

### Proof

Every component of `U-s` other than `C_s` has a neighbour at `s`, since
`U` is connected.  Therefore their union with `s`, which is exactly
`Z_s`, is connected.  The complement `C_s` is connected by definition,
and `r in C_s`, so both parts are nonempty.

Suppose `C_s` met every portal set `P_j`.  A connected subgraph of
`G[C_s]` containing `r` and one chosen vertex of every `P_j` would be a
retained row core avoiding `s`, contrary to core-unavoidability.  Hence
some `P_j` is disjoint from `C_s`; all its vertices lie in `Z_s`, so
`j in Omega_U(Z_s)`.

The first two items make `Z_s` detachable and root-containing.  Its
transferability to a met target `H` is exactly
`Omega_U(Z_s) subseteq {H}`.  Since the monopoly set is nonempty, failure
for a met twin means that it contains a row other than that twin. \(\square\)

## 3. Matching consequence at the exact-seven frame

For each neutral donor choose a protected root.  Every one of the three
surplus roots of the seven-adhesion now has one of three certified
statuses:

1. it is core-avoidable and its outside component meets both twins, hence
   is freely transferable to either one;
2. it is core-avoidable and its outside component misses a twin, exposing
   an actual nested adhesion; or
3. it is core-unavoidable and has the canonical multi-owner gate
   `Z_s` of Theorem 3.

If two status-1 pieces in distinct donors have distinct twin targets,
the audited surplus-root transfer gives `K_7`.  Thus, after descending
through every status-2 exact adhesion, a target-free state has a precise
Hall obstruction: all freely transferable roots have one common target,
and every remaining root is carried by a detachable gate owning at least
one non-target row.

This replaces the vague phrase “bad portal placement” by literal
detachable pieces and actual monopoly sets.  A proper-minor state theorem
can now operate on either side of each gate.  What is still missing is
the dynamic statement that a family of such multi-owner gates produces
matching equality partitions on opposite shores, or that all gates have
one coherent rural expansion with the same two apex vertices.

## 4. Deficiency rotation at a multi-owner gate

There is a further label-preserving output when a canonical gate meets
both twins.  Retain the exact-seven frame and write `U` for its donor,
`Z` for a detachable surplus-root gate, and `W=U-Z`.  Let `X` be the
connected path-side envelope.  Thus a marked vertex of `Z` has an edge
to `X`, while `X` already meets every neutral bag.

### Theorem 4 (gate-to-centre deficiency rotation)

Exactly one of the following holds.

1. `Z` is anticomplete to at least one of `B,C`; then `N_G(Z)` is an
   actual separator of order at least seven (full at exact order seven).
2. `Z` meets both `B,C`.  Put
   
   \[
                         A'=X\cup Z.                     \tag{4.1}
   \]
   
   Then the six bags other than `W` form a clique model, `W` is adjacent
   to `A'`, and the only old rows which may be anticomplete to `W` are
   those in `Omega_U(Z)`.  Consequently:
   
   * `Omega_U(Z)=empty` gives a literal `K_7` model;
   * `|Omega_U(Z)|=1` gives a labelled `K_7^-` model; and
   * `|Omega_U(Z)|=2` gives a labelled `K_7^vee` model,
   
   in each case with the residual donor `W` as the new deficient centre.
   If `|Omega_U(Z)|>=3`, the gate is a certified three-row warehouse.

### Proof

If `Z` misses, say, `C`, the whole connected bag `C` lies outside
`Z union N_G(Z)`.  The nonempty connected set `Z` is on the other side,
so its open neighbourhood is an actual separator.  Connectivity and
exact-order fullness follow as in Lemma 2.

Now suppose `Z` meets both twins.  The set `A'` is connected through the
edge from its marked root to `X`.  It meets `B,C` through `Z`; it meets
every neutral bag other than `U` through the old path core in `X`; and it
meets `W` through an edge across the connected split `Z|W`.

Regard `W` as the new centre.  The six foreign bags are `A'`, the two
twins, and the three neutral bags other than `U`.  They are pairwise
adjacent: `A'` meets all five old foreign rows as just checked, and the
other five retain their old clique-model edges.  The residual `W` is
connected and meets `A'` through the cut edge.  For an old foreign row
`F`, it loses its `U-F` adjacency exactly when all `U-F` portal endpoints
lay in `Z`, namely when `F in Omega_U(Z)`.  These are the only potentially
missing spokes at the new centre.  The four conclusions follow from the
size of this labelled missing star. \(\square\)

The theorem is a genuine exchange rather than a quotient inference: all
vertices of `Z` move once into one connected branch bag, the residual
donor remains connected, and every claimed adjacency is a literal old
edge or the gate cut edge.  It says that a portal-locked surplus root can
avoid both an adhesion and a nearer clique model only by owning at least
three full row classes.

## 5. Opposite roots eliminate the three-row warehouse

The last warehouse alternative cannot persist after reversing the
protected and surplus roots.

### Lemma 5 (opposite canonical gates are disjoint)

Let `U` be connected and let `r,s` be distinct vertices.  Let `C_s` be
the component of `U-s` containing `r` and `C_r` the component of `U-r`
containing `s`.  Put

\[
                         Z_s=U-C_s,\qquad Z_r=U-C_r.      \tag{5.1}
\]

Then `Z_s cap Z_r=empty`.

### Proof

Suppose `v` belonged to both gates.  Since `v notin C_s`, every
`r-v` path uses `s`.  Take a simple `r-v` path; its suffix from `s` to
`v` avoids `r`.  But `v notin C_r` says that every `s-v` path uses `r`,
a contradiction. \(\square\)

### Theorem 6 (two-root warehouse discharge)

Retain the exact-seven donor setting, and let `r,s` be any two marked
roots in one neutral donor `U`.  Protect `r` and classify `s` by the row
core theorem; then reverse their roles.  At least one of the following
holds:

1. a core-avoidable, monopoly-free surplus-root component is transferable
   to a twin;
2. an actual order-at-least-seven nested adhesion is exposed (full at
   exact order seven); or
3. a gate-to-centre deficiency rotation produces `K_7`, `K_7^-`, or a
   labelled `K_7^vee` model.

In particular, “one donor contains all surplus roots in a three-row
warehouse” is not a fourth outcome.

### Proof

If one root is core-avoidable relative to the other, its component
outside an avoiding core is monopoly-free.  It transfers to every twin
it meets by Lemma 1, and if it misses either twin, Lemma 2 exposes the
actual adhesion.  In the no-adhesion branch it therefore meets both and
is transferable to either.  This is outcome 1 or 2.

Suppose instead that each root is core-unavoidable relative to the other.
Theorem 3 gives the two canonical gates `Z_s,Z_r`, each with a nonempty
monopoly set.  Lemma 5 makes the gates disjoint.  Monopoly sets of
disjoint detachable parts are disjoint: one nonempty literal portal set
cannot be contained in two disjoint vertex sets.  Only the five foreign
row labels of `U` are available, so

\[
           |\Omega_U(Z_s)|+|\Omega_U(Z_r)|\le5.          \tag{5.2}
\]

At least one gate, say `Z`, therefore owns at most two rows.  If `Z`
misses a twin, Theorem 4 gives the actual adhesion.  If it meets both
twins, Theorem 4 rotates the model and gives `K_7`, `K_7^-`, or
`K_7^vee` according as its monopoly order is zero, one, or two.  (The
order is nonzero in the core-unavoidable branch.)  This is outcome 2 or
3. \(\square\)

Theorem 6 is the promised attack on confined surplus roots.  It works for
every selected pair of roots in a donor, including the `4+1+1+1`
distribution: no matter how many surplus roots lie in that one bag, any
chosen pair either augments, descends to an actual adhesion, or rotates
to a new near-clique centre with at most two missing spokes.

### Corollary 7 (two surplus donors close)

In the exact-seven frame, suppose surplus roots occur in at least two
distinct neutral donors.  Then at least one of the following holds:

1. `G` contains a `K_7` minor;
2. an actual nested separator of order at least seven is exposed (full
   at exact order seven); or
3. a labelled deficiency rotation gives `K_7^-` or `K_7^vee` with a new
   deficient centre.

Consequently, after excluding descent and rotation, the only exact-seven
root distribution is `4+1+1+1`.

### Proof

Choose two donors and in each choose a pair consisting of one protected
and one surplus root.  Apply Theorem 6.  If either donor gives outcome 2
or 3, the corresponding conclusion holds.  Otherwise each gives a
core-avoidable component.  By the strengthened Lemma 2, absence of an
actual adhesion forces that component to meet both twins.  Lemma 1 makes
it transferable to either twin.

The two components lie in distinct old donor bags and are therefore
disjoint.  Assign one to `B` and one to `C`; each donor complement retains
its protected root and all foreign-row contacts.  If the two residual
donors are adjacent, the corrected two-target surplus-root exchange
yields an `S`-meeting `K_6`, and the full path-side envelope supplies the
seventh branch set.  If they are anticomplete, the open neighbourhood of
either connected residual donor is an actual separator with the other
residual donor on a far side.  This is outcome 2. \(\square\)

The distributions `2+2+2+1` and `3+2+1+1` are therefore discharged
uniformly.  No enumeration of which neutral row contains which boundary
vertex is needed.

## 6. Uniform scope

Nothing in Lemma 1 or Theorem 3 uses seven, two twins, or a planar
embedding.  For a clique-model bag with any finite family of literal row
portals, surplus roots outside a connected transversal core are
monopoly-free transferable pieces; roots unavoidable in every core are
cutvertices separating the protected root from an entire portal family.
This is a uniform rooted-model augmentation principle.  Seven-connectivity
enters only when a target-free outside component is converted into an
order-at-least-seven actual adhesion.
