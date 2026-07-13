# Independent audit: pure-Moser two-component low-cut exchange

**Verdict:** GREEN, with an explicit computer-assisted finite boundary.

## 1. Scope checked

The theorem assumes:

* `G` is seven-connected and proper-minor-minimal non-six-colourable;
* `v` has literal neighbourhood `S` of order seven;
* `G[S]` is exactly the eleven-edge Moser spindle in the stated labelling;
* `G-N[v]` has exactly two connected components.

The packet vector `(1,2)` is not used.  Thus the result applies to that
current branch but must not be quoted for an arbitrary `(1,2)` separation
whose rich open shore has two components.  It also leaves exterior
components of order at most three possible.

## 2. Cutvertex and arbitrary two-cut geometry

Every exterior component is `S`-full.  If one missed a boundary literal,
its at-most-six boundary neighbours would separate it from `v` and the
other exterior component.

For a cutvertex `z`, a component `D` of `C-z` and its complement `E=C-D`
are connected and adjacent.  Their ambient neighbourhoods are contained in
`S union {z}`.  There is another lobe beyond each relevant neighbourhood,
so seven-connectivity gives at least six literal contacts on each side.
The 57-case triangle-anchor script was rerun and returned

```text
verified 57 global cutvertex defect pairs
```

The six displayed branch sets were checked individually: anchors are
distinct and avoid the retained triangle; each anchor contacts its carrier;
an anchor repairs the sole possible carrier-to-triangle defect; the full
other exterior component creates all remaining packet adjacencies.  This is
a literal `S`-meeting `K_6`, not a colour-to-model inference.

After cutvertices are excluded, let `{z_1,z_2}` be any two-cut.  Every lobe
of `C-{z_1,z_2}` meets both cut vertices, since otherwise one cut vertex
alone disconnects that lobe.  For an arbitrary lobe `D`, the sets

```text
A = D union {z_1},
B = C-A
```

are disjoint, nonempty, connected, and adjacent.  This remains true with a
singleton lobe and with more than two lobes.  The first lobe gives at least
five `S` contacts to `A`; any second lobe gives at least five to `B`.
Fullness of `C` makes the two exact defect sets disjoint.  No hidden
two-connectivity or component-order assumption is used.

## 3. Exact quotient enumeration and lifting

The verifier uses all 29 defect sets of order zero, one, or two and all 260
unordered disjoint pairs.  Its restricted-growth labels enumerate every
partition of every used vertex subset into six nonempty bags exactly up to
bag permutation.  The terminal condition `maximum == 5` guarantees that no
bag is empty.  It then tests:

* literal intersection with `S` for all six bags;
* graph connectivity of every bag; and
* all fifteen pairwise bag adjacencies.

The script was rerun from a clean Python process and returned

```text
verified 260 global two-cut quotients; residual=2
[({1, 3}, {2, 4}), ({1, 4}, {2, 3})]
```

The search includes models using six through ten quotient vertices, so it
does not assume a spanning model.  Replacing a shore vertex in a quotient
bag by its original connected shore preserves connectivity; quotient edges
are all literal boundary contacts or the `AB` edge, so every adjacency
lifts.  Since every quotient bag meets `S`, adding `{v}` supplies the
seventh branch set.

The finite atlas remains a conventional computer-assisted input, not a
formal proof-assistant certificate.  Its implementation is dependency-free,
small, and complete by direct inspection of the enumeration, but this trust
boundary should remain visible in any publication claim.

## 4. Exceptional contraction audit

For both failures, the two defects are disjoint nonedges and their complement
is `{0,5,6}`, with exactly `56` present among that triple.

### Return on the split-component side

The sets `{v} union r` and `C_2 union e` are connected, disjoint, and
adjacent.  Their contraction is proper.  A contraction colouring is **not**
pulled back over its connector edges.  Instead `v,C_2` are deleted first,
and only the independent pairs `r,e` are expanded.  This gives a valid
colouring of `G[S union C_1]`.

The two representatives have distinct colours and each sees `0,5,6`;
`5,6` are adjacent.  Therefore there are exactly three possible equality
partitions, not merely three coarsenings: `0` is either alone, equal to `5`,
or equal to `6`.

### Matching returns on the full-component side

If `A` misses exactly `r` and `B` misses exactly `e`, then `A union e` and
`B union r` are connected: each shore contacts both vertices of the
opposite defect pair.  They are adjacent through the split-shore edge.
The third set `{v} union I_q` is a star, and the three contraction sets are
pairwise disjoint and adjacent.

For `q=0`, the three representatives and literal `5,6` were checked to be a
`K_5`.  For `q=5` or `6`, the representatives and the remaining literal are
a `K_4`.  Thus their colours are pairwise distinct and the pullbacks induce
the exact required partitions.  Again the connector vertices `A,B,v` are
deleted before independent boundary blocks are expanded.

### Gluing and the apex colour

Equal equality partitions, rather than a presumed equality of colour names,
justify a palette permutation on one side.  The two exterior components are
anticomplete, so the aligned colourings glue.  The largest returned state has
only five blocks, leaving a sixth colour absent from the literal
neighbourhood `S`.  Since `d(v)=7` and `S=N(v)`, assigning that colour to `v`
is valid.

## 5. Duplication check and conclusion

The current audited adaptive rich cut-packet theorem closes a cutvertex in
one of two rich components by extracting three carriers.  It does not close
an arbitrary two-cut and does not contain the complementary-defect state
exchange above.  The current double-triangle theorem only funnels a
near-full split to crossed pure defects.  The result audited here therefore
adds a genuine infinite-family closure in the pure-Moser two-component cell;
it is not a restatement of either current theorem.

No step identifies a palette colour with a pre-existing packet label.  The
258 ordinary cases use literal minor models; the two exceptional cases use
exact boundary partitions produced and reproduced by legal proper-minor
contractions.  Subject to the stated finite-computation trust boundary, the
theorem is GREEN.
