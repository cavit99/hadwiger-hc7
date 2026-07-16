# One full external bridge does not repair the bad six-link quotient

**Status:** computer-assisted finite barrier, with a deterministic
dependency-free classifier.  The computation concerns one fixed
12-vertex quotient and is not a counterexample to the seven-connected
host theorem.

## 1. The fixed quotient

Let `Q` have vertex set `{0,...,11}`.  On `{0,...,5}` take:

- a `K_4` on `{0,1,2,3}`;
- the edge `4-5`;
- the contacts `0-4`, `1-4`, `2-4`, and `3-5`.

These six vertices support a normalized `K_5` model with edge branch set
`{4,5}`.  On `{6,...,11}` take `K_6` minus the edge `10-11`.  Finally add
the matching

\[
 0\!-\!6,\quad1\!-\!7,\quad2\!-\!8,\quad
 3\!-\!10,\quad4\!-\!11,\quad5\!-\!9.             \tag{1.1}
\]

The archived
[quotient probe](../archive/hc7_disjoint_k6minus_support6_quotient_probe.py)
independently verifies that `Q` has no `K_7` minor.  It is the bad
matching quotient showing that six arbitrary disjoint linking paths do
not suffice.

Add one new vertex `w`, representing a connected external bridge after
contraction, and let its neighbourhood in `Q` be `T`.

## 2. Exact classification above the connectivity threshold

The statement

> every attachment set `T` of order at least seven makes `Q+w` contain a
> `K_7` minor

is false.  In fact, among attachment sets of order at least seven,
`Q+w` has no `K_7` minor exactly when `T` is contained in one of

\[
 \begin{aligned}
 T_p&=\{0,1,2,3,6,7,8,10\},\\
 T_q&=\{0,1,2,4,6,7,8,11\}.
 \end{aligned}                                      \tag{2.1}
\]

Both displayed eight-sets are inclusion-maximal nonrepairing attachment
sets.  A smallest counterexample at the seven-connectivity threshold is

\[
                         T=\{0,1,2,3,6,7,8\}.        \tag{2.2}
\]

Consequently every attachment set of order at least nine repairs the
quotient, but order seven alone does not.

## 3. Exhaustive certificate scheme

The verifier
[`hc7_disjoint_k6minus_external_bridge_classifier.py`](hc7_disjoint_k6minus_external_bridge_classifier.py)
does not invoke a generic minor solver.  It enumerates all unordered
collections of six pairwise disjoint, connected and pairwise adjacent
branch sets in `Q`.  There are 2,260 such collections, giving 1,642
distinct attachment constraint systems.

For one collection, let `U` be the vertices of `Q` outside its six branch
sets.  In a spanning seven-branch model of `Q+w`, the seventh branch set
is `U union {w}`.  This branch set is connected exactly when `T` meets
every component of `Q[U]`.  It is adjacent to another branch set `B`
unless `Q` has no edge from `U` to `B`; in that exceptional case `T` must
meet `B`.  These conditions are both necessary and sufficient.

Every minor model can be enlarged to a spanning model because `Q+w` is
connected.  Thus the enumeration covers every `K_7` model.  Evaluating
the resulting constraint systems on all `2^12` attachment sets gives:

```text
six_branch_collections 2260
attachment_constraint_types 1642
repairing_attachment_sets 3352
nonrepairing_attachment_sets 744
maximal_nonrepairing_with_at_least_seven_attachments
[(0, 1, 2, 3, 6, 7, 8, 10), (0, 1, 2, 4, 6, 7, 8, 11)]
smallest_seven_attachment_counterexample (0, 1, 2, 3, 6, 7, 8)
```

Run from the repository root with:

```sh
python3 barriers/hc7_disjoint_k6minus_external_bridge_classifier.py
```

As an independent check using the original connected-branch-set minor
verifier, both (2.2) and `T_p` returned `False` for `K_7`-minor existence.

## 4. Opposite exceptional types compose

Although either exceptional frame can survive alone, one component of
each type cannot.  More precisely, let `w_p,w_q` be distinct new vertices
with no edge required between them.  Suppose

\[
 \begin{aligned}
 7\le |N_Q(w_p)|,&\qquad N_Q(w_p)\subseteq T_p,\\
 7\le |N_Q(w_q)|,&\qquad N_Q(w_q)\subseteq T_q.
 \end{aligned}                                      \tag{4.1}
\]

Then `Q+w_p+w_q` contains a `K_7` minor.  The conclusion remains true if
`w_pw_q` is added.

There are nine possible neighbourhoods on each side: the full eight-set
and its eight seven-subsets.  The verifier checks all 81 ordered
mixed-type pairs twice, with and without `w_pw_q`, and finds no exception.
Its exhaustive model search has two parts.  If the two new vertices lie
in one branch set, it enumerates the six other branch sets in `Q`.  If
they lie in different branch sets, it enumerates the five other branch
sets and every partition of the unused vertices of `Q` between the two
new branch sets.  Thus it covers every spanning model and hence every
minor model.

For the two maximal frames, a particularly short certificate consists of
the branch sets

\[
 \{0\},\ \{1\},\ \{2\},\ \{3\},\ \{4,5\},\
 \{6,9,w_p\},\ \{7,10,w_q\}.                        \tag{4.2}
\]

They are connected and pairwise adjacent directly from (1.1) and the
definitions of `T_p,T_q`.

This gives the following finite structural corollary **only for a literal
copy of the 12-vertex quotient**.  Let `H` contain twelve distinct
vertices spanning all the displayed edges of `Q`, and let the components
of `H-V(Q)` be nonempty and each have at least seven distinct neighbours
among those twelve literal vertices.  If `H` has no `K_7` minor, every
component has the same exceptional type.  Hence, for one choice
\(T_*\in\{T_p,T_q\}\), the union `R` of all exterior components satisfies

\[
                              N_Q(R)\subseteq T_*.
\]

Consequently \((R\cup T_*,Q)\) is an actual separation of order eight in
this literal-quotient graph.

The distinct-neighbour hypothesis is automatic from seven-connectivity
when these twelve vertices are literal vertices of the host and the
objects under consideration are components of their deletion.  It is
**not** automatic for the quotient obtained by contracting six nontrivial
linking paths: seven distinct first-hit vertices may collapse to fewer
than seven quotient vertices.  Therefore the order-eight separation
conclusion must not be transferred to the expanded host without a proved
injective first-hit normalization (or an equivalent label-preserving
lifting argument).

## 5. Exact implication

One contracted external component with seven distinct attachments does
not close the rigid disjoint-support configuration.  Any host-level proof
must use more than the cardinality of its attachment set.  It must either
exclude the two labelled exceptional frames in (2.1), exploit the
order-eight separation forced by Section 4 in the literal quotient, or
use critical-colouring information absent from the quotient.  For a
general expanded six-linkage, the first-hit injectivity gap remains.
