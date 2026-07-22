# Audit: static reserve-rotation barrier

**Audit type:** separate internal cold audit

**Verdict:** **GREEN**

Audited barrier:
[`hc7_degree8_static_reserve_rotation_barrier.md`](hc7_degree8_static_reserve_rotation_barrier.md)

Audited source SHA-256:

```text
c7426158ae2ac183480e5e49c6daf15d869beccc6e6270a500b07a7dad6f4e35
```

## Refuted claim and construction

Let the three components of

```text
H = K_3 disjoint-union K_3 disjoint-union K_2
```

be `A,B,C`.  An independent set contains at most one vertex from each
clique, and choosing one from each gives an independent triple.  Hence
`alpha(H)=3`, and every maximum independent set has exactly one vertex in
each of `A,B,C`.

For every maximum independent triple `I`, its five-vertex complement is

```text
H-I = K_2 disjoint-union K_2 disjoint-union K_1,
```

so it has exactly two edges and eight nonedges.  Every maximum independent
triple contained in this reserve again chooses one vertex from each of its
three nonempty clique components.  It is therefore also a maximum
independent triple of `H`, and replacing `I` by any such triple leaves a
new complement of the same form.  This verifies invariance under every
allowed rotation, not merely under one selected sequence.  No iteration can
produce the four reserve edges required by the refuted claim.

## Compact boundary properties

- `H` has eight vertices and independence number three.
- Each component has degeneracy at most two, so their disjoint union is
  two-degenerate and therefore three-degenerate in the standard
  at-most-three sense.
- Selecting one edge from each of the two `K_3` components induces `2K_2`.
  Since split graphs contain no induced `2K_2`, `H` is nonsplit.
- For every two-set `Z`, every component of `H-Z` has order at most three.
  A connected minor such as `K_4` must lie within one component, and no such
  component has a `K_4` minor.  Thus `H-Z` is `K_4`-minor-free for every
  `Z`.

All hypotheses in the displayed refuted claim are consequently met, while
its eventual-four-edge conclusion fails.

## Scope

The source correctly limits the counterexample to static boundary data.
The graph is disconnected and is not claimed to occur as the neighbourhood
of the distinguished vertex in a seven-connected, seven-chromatic,
minor-minimal `K_7`-minor-free host.  It supplies neither exterior
components nor colouring-response or path-provenance data.  It therefore
does not refute the five-reserve rotation corollary, any host-level dynamic
rotation argument, or `HC_7`; it refutes only termination based on repeatedly
changing the maximum independent boundary block while discarding all such
dynamic data.

No mathematical defect or scope overstatement was found.
