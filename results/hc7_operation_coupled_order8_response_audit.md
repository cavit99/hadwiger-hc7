# Internal audit: operation-coupled responses at a boundary-full eight-separation

**Verdict:** GREEN for the exact source revision

```text
be8fc118ab832ff9a24057873c815805539c0ab7cb1e4996c4d81202cf72b268
```

of
[`hc7_operation_coupled_order8_response.md`](hc7_operation_coupled_order8_response.md).
This is a separate internal audit, not external peer review.  Relative to
the exact revision checked line by line, the pinned revision changes only
the opening status line to link this audit; its mathematical content is
identical.

## 1. Scope checked

The audit checked the full source, including:

1. the legal/rejected orientation of the edge-deletion response on the
   operated component and all unchanged components;
2. the transported-partition demand and Hall-deficiency deductions;
3. the exact-block Kempe tree for two and three complementary components;
4. the use of the prescribed-first-edge fan theorem and its literal
   order-seven cut geometry;
5. the construction of the opposite-shore colouring with the same exact
   block at the returned order-seven boundary;
6. the order-independent signature-change argument there; and
7. the exact-seven packing-number and Hall conclusions in both orientations.

## 2. Audit findings

### The asymmetric response is correctly oriented

A six-colouring of `G-e` restricts to every unchanged component-side.  If
the same labelled boundary colouring also extended through the operated
component with `e` restored, the component-side colourings would glue to a
six-colouring of `G`.  Hence its extension set is exactly the set of far
components.

The transported-partition theorem applies to every block not represented
by the selected singleton clique, including singleton blocks outside that
clique.  The source defines the corresponding duty sets and counts the
actual full supports in the Hall inequality.  A saturating matching would
reproduce the rejected equality partition on the operated side and give the
same forbidden gluing.

### The exact-block Kempe trees are valid

The boundary degeneracy theorem makes the exact-block five-colour space
connected after a named colour is fixed exactly on the independent block.
For two components, the operated response and the contraction response have
opposite extension signatures.  For three components, the source uses the
operated response as the anchor omitting `C_0` and the two contractions as
the anchors omitting `C_1` and `C_2`.  Thus every extension bit changes on
the finite tree.  The signature-change lemma gives a literal bichromatic
path in the named component whenever its bit changes; it does not assert
that the different changes occur on one move.

### The fan-or-separation geometry is preserved literally

Criticality of the deleted edge supplies one two-colour path for each of
the five alternate colours.  Different colour pairs share only vertices of
the common endpoint colour and share no edge.  The prescribed-first-edge
theorem therefore returns either the clean five-path fan or sets
`I,Z,A` satisfying

\[
 N_G(A)=(X-I)\mathbin{\dot\cup}\{v\}
             \mathbin{\dot\cup}Z,
 \qquad |N_G(A)|=7.
\]

The selected colouring is proper on this closed side, and its exact common
colour block contains `v` and a vertex of `Z`.

### The opposite exact-block response and packing conclusions are valid

Contracting a spanning tree of `A` together with the independent exact
block produces a proper minor.  Boundary fullness makes that block exact
when the minor colouring is pulled back only to the opposite shore.  If the
two complete equality partitions differ, exact-block Kempe connectivity and
the elementary signature-change proof give operation-specific obstruction
paths in both orientations.

The exact-seven packing theorem leaves only `(1,1)`, `(1,2)`, and `(1,3)`.
The separately audited adaptive reflection theorem excludes `(1,3)` under
the present hypotheses.  Hence the maximum number of disjoint
boundary-full connected supports on either oriented shore is one or two.
With a fixed maximum family and the explicitly defined duty incidence,
failure of a Hall matching is necessary; otherwise transported reflection
would again glue the two shore colourings.

## 3. Trust boundary

The theorem proves one uniform operation-specific normal form for both the
two- and three-component order-eight interfaces.  It provides asymmetric
boundary responses, non-simultaneous literal Kempe obstruction paths, and a
clean-fan-or-exact-seven alternative with bilateral Hall certificates.

It does **not**:

- identify palette colours with inherited minor-model branch-set labels;
- preserve a connected residual subgraph after allocating the fan;
- make the different Kempe transitions simultaneous;
- produce one complete equality partition on both shores; or
- prove `HC_7`.

No unresolved assumption remains inside the stated theorem.  The open step
is the label- and residual-preserving allocation or the compatible
exact-seven gluing asserted in its trust boundary.
