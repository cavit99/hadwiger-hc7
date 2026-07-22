# Independent audit: doubled-route responses and short rooted-bag cycles

**Verdict:** **GREEN**.

Audited theorem:
[`hc7_degree7_route_cycle_model_persistence.md`](hc7_degree7_route_cycle_model_persistence.md)

Audited source SHA-256:

```text
886b7b65e53cdfd8d6940a64702155293fa902085c2a11d50a415404232f7f62
```

The mathematical content was cold-read at hash
`8f022f8f8f3ac0505d1a5c4b28307da4bd4dae517c3cd02603f20b394560601d`.
The only subsequent source change was the status line linking this audit;
the final hash above was rechecked separately.

## 1. Hypothesis matching

The setup is exactly the audited degree-seven tight-pole residue.  Each
selected route-cycle edge has an end in `C`, so deleting it leaves the pole
shore and the original boundary graph intact.  The off-pole response theorem
therefore applies literally.  The fixed rooted `K_5` model lies in
`A-\{a,b\}`, which contains both route cycles.

## 2. Minimal bond response

The bond switch is valid.  The selected `K_i` is the full
`alpha_i-beta_i` component, and the bond contains every edge between its
two connected sides.  Switching one side creates no undeleted
bichromatic conflict.  Only `x_i` changes on `S`, so the new boundary
matching is exactly `\{e_0,e_i\}` and the vanished colour can be assigned
to `u`.

Every bond edge becomes monochromatic.  Equality propagates within each
component of the bond-edge graph; any other edge inside such a component
would be a monochromatic edge of `G-D`.  Hence the simultaneous contraction
claim is sound.

The minimal-response quantifiers are also exact.  If an edge of a minimal
aligned set `J` were proper in an aligned `G-J` colouring, restoring it
would align a proper subset.  For `|J|\ge2`, every singleton is a proper
subset, so every `G-h` response omits `e_0` or `e_i`.  When an endpoint
Kempe component is switched, restoring `h` again invokes this same
minimality; consequently both distinct endpoint components meet `S` and
either switch leaves the target matching family.  No stronger lock is
claimed in the common multi-edge deletion.

The common-host equality signatures are correct.  A `G-h` colouring makes
the ends of `h` equal, while every other bond edge is present and proper.
For a two-edge bond this gives the three displayed signatures; the fourth
would colour `G` after both edges were restored.

## 3. Rooted-model persistence and short cycle

Lemma 2.1 is an exact test for persistence of the same fixed bags:
deleting an outside edge changes nothing, an internal edge matters exactly
when it is a bag bridge, and a cross-bag edge matters exactly when it is
the unique contact of that pair.

If a route cycle has no persistent edge, it lies in the bag union.  Its
bag-label transitions form a connected simple Eulerian graph: repeated
use of one label pair would give two contacts and make both transition
edges persistent.  The two literal route cycles are vertex-disjoint, so
their transition graphs use disjoint edges of `K_5`.  Both have at least
three edges and together have at most ten; one therefore has three to five
edges.  A connected simple Eulerian graph in that range is exactly
`C_3,C_4` or `C_5`.

On that short trace each bag occurs in one sector.  Every sector edge is a
bag bridge, which proves uniqueness of the in-bag path and the one-vertex
attachment statement for every off-sector bag component.  The theorem
correctly leaves all nonconsecutive cross-bag contacts uncontrolled.

## 4. Unresolved dependencies and claim boundary

No internal assumption or proof gap remains.  The conclusions remain
conditional on the cited audited exact-matching, off-pole-response and
rooted-model inputs.

The theorem does not prove:

- that a persistent edge returns a matching containing `e_0,e_i`;
- that palette colours align with the five rooted-bag labels;
- that the short cycle has a crossing bridge or an order-seven interval
  separation; or
- an explicit `K_7` model, a common complete boundary partition, a strict
  descent, the degree-seven branch, or `HC_7`.
