# Endpoint allocation in type-5 pentagonal-bipyramid enlargements

**Status:** computer-assisted finite theorem; separately audited **GREEN**
in
[`hc7_pentagonal_bipyramid_type5_endpoint_allocation_audit.md`](hc7_pentagonal_bipyramid_type5_endpoint_allocation_audit.md).

This note classifies exactly when two nominated root-contact sets fail to
support a common `K_5` model in a type-5 enlargement of the pentagonal
bipyramid.  It is a finite theorem about the enlargement graph.  It does
not assert that the enlargement supplied by Hegde--Thomas preserves a
previously selected minor model.

## 1. Setup

Let

\[
                       P=C_5\vee\overline{K_2}
\]

be the pentagonal bipyramid in its unique plane embedding.  A type-5
enlargement is obtained from an edge `uv` of `P` by splitting its ends into
adjacent pairs

\[
                         u_0u_1,\qquad v_0v_1.
\]

The old edge `uv` is represented by `u_0v_0`.  Each old neighbourhood is
divided conformingly along one of the two faces incident with `uv`, and the
additional type-5 edge is `u_1v_1`.

Let `A,B` be sets of nominated vertices satisfying the following
conditions.

1. Every unsplit old vertex belongs to both `A` and `B`.
2. Each of `A,B` meets each of `\{u_0,u_1\}` and `\{v_0,v_1\}`.

A `K_5`-minor model is **paired-rooted at `(A,B)`** when each of its five
branch sets meets both `A` and `B`.

Say that `A` is **confined to the retained-edge sides** when

\[
 A\cap\{u_0,u_1\}=\{u_0\},\qquad
 A\cap\{v_0,v_1\}=\{v_0\},                             \tag{1.1}
\]

and define the same condition for `B`.

## 2. Classification theorem

### Theorem 2.1

For every type-5 enlargement `H` of `P`, exactly one of the following
alternatives is relevant.

1. `H` has a `K_5` model rooted at five unsplit old vertices.  In this
   case it has a paired-rooted `K_5` model for every admissible pair
   `(A,B)`.
2. `H` has no such five-unsplit-root model.  In this case `H` has a
   paired-rooted `K_5` model at `(A,B)` if and only if neither `A` nor `B`
   is confined to the retained-edge sides.

Thus the entire finite label obstruction is one simultaneous two-column
phenomenon: one nominated root-contact set is confined to side zero in
both split fibres.

### Proof

The finite classification is checked by
[`hc7_pentagonal_bipyramid_type5_endpoint_allocation_verify.py`](hc7_pentagonal_bipyramid_type5_endpoint_allocation_verify.py).
We describe the exhaustive search and its exact logical test.

The verifier uses the exact generator in
[`active/hc7_pentagonal_bipyramid_enlargement_probe.py`](../active/hc7_pentagonal_bipyramid_enlargement_probe.py),
which constructs the plane rotation system of `P`.  For every old
edge it enumerates every conforming split at both ends and retains exactly
the face assignments in the definition of a type-5 enlargement.  This
gives 50 labelled enlargements.

For each enlargement, it first tests whether five unsplit old vertices
root a `K_5` model.  It then considers all eighty-one choices

\[
 (I_A,I_B,J_A,J_B)\in
 \bigl\{\{0\},\{1\},\{0,1\}\bigr\}^4,                \tag{2.1}
\]

where `A` contains the vertices `u_i` for `i\in I_A` and `v_j` for
`j\in J_A`, while `B` is defined by `I_B,J_B`, in addition to the five
unsplit old vertices.  These are exactly all nonempty set-valued choices in
the two split pairs.

For each choice, the verifier enumerates every nonempty connected vertex
set which meets both nominated sets, and then every five pairwise disjoint
such sets.  It accepts exactly when all ten pairwise branch-set
adjacencies hold.  Hence the search is exhaustive over all paired-rooted
minor models, not merely over paths or prescribed contractions.

Among the 50 enlargements, 20 have no model rooted at five unsplit old
vertices.  Across all `50\cdot81=4050` endpoint-set tests, exactly 340 have no
paired-rooted model.  The verifier compares every result with the Boolean
condition

\[
 \bigl(I_A=J_A=\{0\}\bigr)\quad\text{or}\quad
 \bigl(I_B=J_B=\{0\}\bigr),                            \tag{2.2}
\]

restricted to those 20 exceptional enlargements.  It finds no mismatch.
This is exactly the condition in (1.1), proving both directions of the
classification. \(\square\)

Running the verifier prints

```text
GREEN type-5 endpoint allocation: instances=50 tests=4050 failures=340 root-trap-mismatches=0
```

## 3. Label-preserving host consequence

Suppose an actual host contains a type-5 enlargement **relative to named
connected pieces**, so that contracting those pieces produces the graph in
Section 1.  Suppose also that two disjoint adjacent connected root
subgraphs meet the pieces represented by `A` and `B`.

If alternative 1 holds, or if alternative 2 holds with neither root
confined as in (1.1), lift the paired-rooted `K_5` model through the named
connected pieces.  Its five branch sets are adjacent to both roots.  The
two roots and those five sets are therefore an explicit `K_7`-minor model.

Consequently, a `K_7`-minor-free relative type-5 configuration has one
precise residual: at least one root has no contact with the side-one piece
of either split column.  If exactly one root is confined, any
label-preserving response which gives that root a side-one contact in at
least one split column is terminal by Theorem 2.1.  If both roots are
confined, a response must free both roots (or provide an independent
terminal construction); freeing only one leaves the other obstruction.

The theorem does not prove that such a response exists.  In a nontrivial
column, many literal neighbours in the same named piece can supply high
connectivity without producing a new quotient contact.  Thus the remaining
unbounded theorem must use contraction-criticality and `K_7`-minor
exclusion to escape this simultaneous two-column confinement, or return a
compatible order-seven separation.
