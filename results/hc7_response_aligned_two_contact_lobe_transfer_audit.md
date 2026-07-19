# Independent audit: response-aligned transfer from two contacts

**Verdict:** **GREEN** for the exact source revision identified below.

This is a separate internal mathematical audit, not external peer review.
It checks Theorem 2.1, Lemma 3.1 and Corollary 3.2, including every branch-set
adjacency, the preservation of the only permitted missing pair, the fixed
literal boundary partition and response kernel, and the root-preserving
extremal argument.

## Audited revision

The audited source is
`results/hc7_response_aligned_two_contact_lobe_transfer.md`.

**Source SHA-256:**

```text
ec3f24c3d7de083542603bf05716c62b0ce0c1b5e9e705538c26e691cc1047dd
```

The only change from the audited `c049fb86...` revision is the source's
status line and link to this audit; no mathematical content changed.

## 1. Initial model and the owner set

The seven original branch sets are a spanning labelled
`K_7`-minus-one-edge model whose only possible missing pair is `X,Y`.
The two displayed edges join the fixed kernel `Z subseteq D` to two
distinct vertices of `U`.  After relabelling, `c_2u_2` enters `W` and
`c_1u_1` enters `U-W`.  This remains valid when `c_1=c_2`; only the two
`U`-ends are required to be distinct.

For a branch set

```text
R in {X,Y,F_1,F_2,F_3},
```

membership in `Omega(W)` means exactly that `U-W` has no edge to `R`.
Because the old model has a `U`--`R` edge and `U` is the disjoint union of
`W` and `U-W`, every member of `Omega(W)` is adjacent to `W`.  This
justifies the connectedness claim when such an `R` absorbs `W`.

The set `D` is deliberately absent from `Omega(W)`: the edge `c_1u_1`
always preserves the `D`--`(U-W)` adjacency.  No other model branch set is
omitted from the definition.

## 2. Empty owner set

When `Omega(W)` is empty, the proposed branch sets are

```text
X, Y, D union W, U-W, F_1, F_2, F_3.
```

They are nonempty, pairwise disjoint, and spanning.  The enlarged `D`
branch set is connected through `c_2u_2`; `U-W` is connected by hypothesis.
The edge `c_1u_1` joins these two new branch sets.

For each of `X,Y,F_1,F_2,F_3`, the old adjacency to `U` has an edge with
its `U`-end in `U-W`, precisely because `Omega(W)` is empty.  All old
adjacencies from `D` persist after enlarging it, and every pair not involving
the two changed branch sets is untouched.  Hence the only pair which may
remain nonadjacent is still `X,Y`.

The root `r_U` remains in `U-W`, and every other root remains in its old
branch set, which is either unchanged or enlarged.  Since `W` is nonempty,
the new `U` branch set is strictly smaller.

## 3. One owner

Suppose `Omega(W)={R}`.  The replacements are

```text
R' = R union W,
U' = U-W.
```

The set `R'` is connected because `R` is connected, `W` is connected, and
the owner-set observation gives an edge between them.  The set `U'` is
connected by hypothesis.  Since `G[U]` is connected and `W,U-W` are both
nonempty, some edge joins the two sides; after the transfer this edge gives
the `R'`--`U'` adjacency.  Independently, `c_1u_1` gives the required
`D`--`U'` adjacency.

For every other member `R_0` of `X,Y,F_1,F_2,F_3`, nonmembership in
`Omega(W)` preserves an edge from `U'` to `R_0`.  Enlarging `R` cannot
destroy any old adjacency, and no other pair changes.

If `R=F_k`, the result is therefore the same labelled
`K_7`-minus-one-edge model with possible missing pair `X,Y`.  If `R=X`,
the enlarged set `X union W` either meets `Y`, completing all pairs and
giving a `K_7` model, or is anticomplete to `Y`, in which case `X,Y`
remains the sole possible missing pair.  The case `R=Y` is symmetric.

Again, no root is lost.  A root belonging to a branch set other than `U`
stays in that old set when it is enlarged, while `r_U notin W` remains in
`U'`.

## 4. Literal response data

The transfer changes only which branch set owns each vertex of `W`.  It
does not delete, contract, or add a graph edge, change the fixed literal
boundary, or recolour a vertex.  Therefore the selected equality partition
`Pi` is literally the same object before and after the transfer.

The connected kernel `Z` remains inside the branch set labelled `D`:

* in the empty-owner case, `D` is enlarged to `D union W`; and
* in the one-owner case, `D` is unchanged.

Thus the theorem preserves exactly the response data it claims.  It does
not claim that every other path-cut or component-contact datum survives.

## 5. Existence of a root-free connected split

Lemma 3.1 is valid.  In a spanning tree of `G[U]`, every edge of the unique
`u_1`--`u_2` path separates those endpoints.  The prescribed root lies in
exactly one of the two resulting tree components, so the other component
is nonempty, root-free, and contains exactly one nominated endpoint.  Both
it and its complement induce connected subgraphs of `G[U]`, since each
contains the corresponding component tree.  This also covers the cases
`r_U=u_1` and `r_U=u_2`.

Thus the source no longer merely assumes that some admissible split exists:
the two distinct `U`-endpoints force at least one such split in every
connected branch set `U`.

## 6. Minimum-order corollary

The minimisation in Corollary 3.2 is over a finite nonempty family of
spanning labelled models in the fixed graph, with fixed labels, roots,
partition and kernel.  Hence a minimum `|U|` exists.

Every connected bipartition separating `u_1,u_2` has one side not
containing `r_U`; orienting that side as `W` and relabelling the two contact
edges supplies all hypotheses (1.3).  If `|Omega(W)|<=1`, Theorem 2.1
gives either a `K_7` model, contrary to the corollary's host hypothesis, or
a compatible model with the proper subset `U-W` as its `U` branch set,
contrary to minimality.  The new model need not retain the two contact
edges, and the source correctly does not require it to do so.

Thus every admissible root-free connected and co-connected side separating
the two persistent endpoints owns at least two of the five listed model
adjacencies.  Applying this conclusion to the split supplied by Lemma 3.1
proves the stronger final assertion: at least one actual multi-owner piece
exists in every minimum compatible `K_7`-minor-free model.  The new model
used for the minimality contradiction need not retain the two contact
edges, exactly as the source states.

## 7. Exact trust boundary

No gap was found in the stated transfer theorem, split lemma, or corollary.
The result does not show that a proper-minor colouring releases an owned
adjacency and does not align a palette colour with a named branch set.  It
also preserves only the fixed
literal partition, kernel, labels and roots explicitly stated; it does not
claim to preserve a full colour-matched-path component selection or its
component defect.

These limitations are all recorded in the source and remain open research
obligations rather than defects in the proved statement.
