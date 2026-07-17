# Audit of pairwise-connected-union transfer

**Verdict:** GREEN for the exact draft revision identified below.

## Audited revision

The audited file is
`results/hc7_response_collision_quasi_transfer.md`.

**Source SHA-256:**
`684c6f1c9dcabc47a098a4e0e8d8d68f476f977c0d679137fda1adb5b104ed0e`.

The mathematical source was audited at SHA-256
`b35bf4f6aee4dafc31f8998acd42428c9f90c2c1ad01fc2a1978ad0de51517ca`.
The promoted revision changes only the status line from “awaiting a
separate internal audit” to “separate internal audit GREEN”; restoring the
former line reproduces the audited hash exactly.  No theorem statement,
hypothesis, proof, or scope qualification changed.

The verdict covers the pairwise-connected-union lemma, the weak transfer
theorem, Corollaries 3.1--3.3, the induced near-complete model,
supported-centre preservation, and the extremal normalization in
Propositions 4.1--4.2.  It does not promote the draft to `results/`, assert
novelty relative to the literature, or strengthen the returned separation
beyond what the source states.

## 1. Component-count calculation

For seven pairwise disjoint nonempty sets `B_1,...,B_7`, pairwise
connectedness of the induced unions gives

\[
  r_{ij}=\operatorname{cc}(G[B_i\cup B_j])=1
  \quad(i<j).
\]

Hence the sum of the twenty-one pair counts is `21`.  If
`n=sum_i cc(G[B_i])`, nonemptiness gives `n>=7`, and therefore

\[
                              21\le n+14.
\]

This is exactly the hypothesis of the separately audited component-count
density lemma.  Contracting the individual components is legitimate even
when an original `B_i` is disconnected.  Lemma 1.1 is therefore correct.

## 2. Componentwise transfer

Let `D` be a component of `G[C-T]`.  Because `G[C]` is connected and `T`
is nonempty, `D` has an edge to `T`: different components of `G[C-T]`
have no edge between them, so every first edge leaving `D` on a path in
`G[C]` has its other end in `T`.

If `D` met all five fixed sets, then

\[
                  W\cup T,\quad D,\quad F_1,\ldots,F_5
\]

would be seven disjoint connected pairwise adjacent sets.  The
`(W union T)-D` adjacency is the edge just found; `W union T` meets each
`F_i` through `W` or, for an index missed by `W`, through the assumed
contact from `T`; and all other adjacencies are hypotheses.  These sets
would be an explicit `K_7`-minor model.  Hence in a `K_7`-minor-free host
every component `D` misses at least one `F_i`, and summing one missed
incidence per component proves `M>= k`.

If instead a component `Y` of `G[C-T]` misses `F_i`, then the nonempty set
`F_i` lies outside `Y union N_G(Y)`.  Thus

\[
             (Y\cup N_G(Y),\;V(G)-Y)
\]

is an actual separation with both open sides nonempty.  Seven-connectivity
gives the lower bound on its order.  When the order is seven, a component
of the complement which missed one boundary vertex would be separated from
another complement component by at most six vertices; the stated fullness
conclusion follows.

## 3. Rotation application

In Corollary 3.1, every missed fixed set has a nonempty portal set in `Z`.
Connectivity of `Z` permits a connected subgraph `T` containing the unique
`W-Z` attachment vertex and one selected portal for each missed set.  The
edge at that attachment makes `T` adjacent to `W`.  Since the old centre
`A` is nonempty and disjoint from `Z`, this `T` is a proper subset of
`C=A union Z`.  All hypotheses of Theorem 2.1 are therefore satisfied.

Corollaries 3.2 and 3.3 are valid substitutions into that result.  In
particular, the reversible near-complete-model outcome is replaced by an
explicit `K_7`-minor model or by the full neighbourhood of a named
connected residual component.  The complement of one residual component
inside `C` is connected because it is `T` together with the other
components, each adjacent to `T`.

## 4. Induced near-complete model and preserved support

The component `D_A` containing the old connected centre `A` contains all
of `A`.  Therefore it meets each of the four old fixed branch sets.  It is
adjacent to `W union T` through `T`; and `W union T` meets the five fixed
sets as above.  Thus

\[
             D_A,\quad W\cup T,\quad R,\quad F_j\ (j\ne i)
\]

has every branch-set adjacency except possibly `D_A-R`.  If that final
adjacency existed, the sets would form a `K_7` model.  In a
`K_7`-minor-free host it is absent, proving Proposition 4.1's labelled
`K_7^-` model.  The assertion that `(A union Z)-D_A` is connected is the
same `T`-plus-components argument checked above.

If `D_A,D_2,...,D_k` are the components outside `T`, the old and new model
orders differ by

\[
                       \sum_{a=2}^k |D_a|.
\]

All fixed and `W` vertices cancel; `A union Z` is partitioned by `T` and
the displayed components.  Hence a globally minimum-order old model
forces `k=1`, provided that old model belongs to the declared globally
normalized class.  No tie-break by the number of missing adjacencies is
used: both the old and replacement models already belong to the supported
one-missing-adjacency class.  The actual secondary extremization, used only
after Proposition 4.2 verifies preservation of that class, is to maximize
the order of the deficient centre among minimum-model-order configurations.

For Proposition 4.2, let `O` be the vertices outside the old seven branch
sets and put all vertices of `Z` which have a neighbour in `O` into `T`.
The old support hypothesis makes `A` anticomplete to `O`, and the definition
of `E_Z` makes `D_A intersect Z` anticomplete to `O`.  Within the old branch
sets, every possible neighbour of `D_A` is accounted for as follows:

- `D_A` is anticomplete to `R` by Proposition 4.1;
- distinct components of `(A union Z)-T` are anticomplete;
- neighbours in `T` or the residual donor `W` lie in the new branch set
  `W union T`; and
- neighbours in the four unchanged branch sets lie in the other four new
  met branch sets.

There are no omitted old donor vertices, since the old donor is exactly
`Z dotcup W`.  Therefore

\[
 N_G(D_A)\subseteq (W\cup T)\cup\bigcup_{j\ne i}F_j,
\]

and the replacement genuinely remains in the same supported
one-missing-adjacency class.  No hidden outside vertex or relabelling gap
occurs.

## 5. Extremal normalization

Choose a supported configuration of minimum model order and, subject to
that, maximum centre order.  For the replacement obtained using a connected
`T` which contains `s`, all selected lost-portal vertices, and `E_Z`, the
model-order difference remains

\[
                       \sum_{a=2}^k |D_a|.
\]

Proposition 4.2 puts the replacement in the same normalized class, so
minimum model order forces `k=1`.  Then the only component outside `T` is
`D_A=A union (Z-T)`, whence

\[
                       |D_A|=|A|+|Z-T|.
\]

The replacement has equal model order.  Maximum centre order therefore
forces `Z-T` empty, or `T=Z`.  Because `T` was chosen inclusion-minimal
among connected subsets containing the named finite terminal set, `Z` is a
vertex-minimal connector for exactly that set.  This is a valid
well-founded normalization.  It does not orient the remaining equality
case, in which the operation simply reverses the connector transfer.

## 6. Exact scope and strategic caveat

The source states its limitations correctly:

- the returned boundary may have order greater than seven;
- the two closed shores need not induce a common boundary equality
  partition;
- the residual component need not re-enter the complete defect-one
  configuration; and
- the extremal argument normalizes the supported one-missing-adjacency
  class, but does not align that class with the globally minimum lifted
  simplicial component in the separate defect-one setup.

Moreover, the original connected deficient-branch-set setup already has a
raw separator `N_G(A)` of order at least seven.  The new mathematical gain
is therefore the pairwise-connected-union transfer and the localization of
failure to a component of `C-T`, not the bare existence of some unbounded
separator.  Nothing in the audited argument closes the remaining
order-seven colour-gluing problem.

## Unresolved assumptions or gaps

None for the exact statements at the audited hash.
