# Independent internal audit of the degree-eight common-root star response

**Verdict:** **GREEN** for the exact source revision

```text
9ef4d2aa63b125ff6e4cd7186ddacd64755d6cb0011123401f84810dcd1f80c3
```

of
[`hc7_degree8_common_root_star_response.md`](hc7_degree8_common_root_star_response.md).
This is a separate internal audit, not external peer review.

## Checked scope

- The retained trace has `W_0={x}`.  Recolouring `x` across the selected
  rejection-cut edge shows that each opposite-shore leaf set is nonempty:
  otherwise the rejected boundary colouring would extend.  Each leaf set
  is independent in its shore colouring, and the two exterior components
  are anticomplete, so the subgraph induced by the root and all leaves is
  exactly a star.
- Recolouring the root in `c_F` or `c_E` creates precisely the corresponding
  deleted star-edge conflicts and gives the stated aligned boundary trace.
  The two shore colourings glue, and the boundary-absent sixth colour is
  available for `u`.  Contracting the whole induced star is a proper-minor
  operation whose expansion deletes exactly its star edges, proving the
  third response signature.  A response proper on both edge sets would
  six-colour `G`.
- Inclusion-minimal aligned deletion sets exist.  For every such set and
  every aligned colouring, each deleted edge is monochromatic: otherwise
  restoring that edge contradicts inclusion-minimality.  This verifies the
  universal quantifier in the multi-edge outcome.
- In the singleton case, the components of `G-X` are exactly `{u},E,F`, all
  full to the eight-vertex boundary.  The selected edge joins `x in X` to
  its named exterior component, and the aligned colouring is a colouring
  of its one-edge deletion.  These are exactly the hypotheses of the cited
  clean-fan-or-generic-restart theorem.  The selected deleted edge chooses
  the response; it is not asserted to be one of the five preserved fan
  first edges.

## Dependencies and nonterminal limits

The proof depends on the full contraction-critical host hypotheses, the
retained-root conclusion of the common-root short-trace classification,
and the audited order-eight clean-fan-or-generic-restart theorem.  No
additional synchronization of the two shore extensions is assumed.

The result does not allocate the clean fan to distinct minor-model labels,
resolve the multi-edge minimal obstruction, produce a common complete
boundary partition, construct a `K_7`-minor model, or prove `HC_7`.  The
generic exact-seven output is a smaller response shore but still enters an
open terminal-decoding problem.

The status-only promotion of the audited source has hash

```text
a732fe236dd247070425edd7c19c744934e49dca378555055f468120fc98be94
```

and makes no mathematical change to the revision audited above.
