# Independent audit: critical-edge double saturation

## Verdict

**GREEN.**  All four conclusions hold for every `k>=4`.  The theorem is a
reduction to a doubly rooted clique-model problem, not a solution of that
problem.

## Checks

1. In the fixed `(k-1)`-colouring of `G-sw`, the endpoints have the same
   colour, or the deleted edge can be restored.  Because this colouring
   is proper, its colour class `C_0` is independent in `G-sw`; consequently
   the only possible edge of `G[C_0]` is the restored edge `sw`.
2. The restriction to `H=G-C_0` uses at most `k-2` colours.  If `H` used
   at most `k-3`, colour `C_0-{s}` with one fresh colour and `s` with a
   second.  The class `C_0-{s}` is independent in `G`, and `sw` has
   differently coloured ends.  This is a proper `(k-1)`-colouring of
   `G`, so `chi(H)=k-2`.
3. If `H+s` had a `(k-2)`-colouring, one fresh colour on `C_0-{s}` would
   colour `G` with `k-1` colours.  The only restored same-`C_0` edge is
   `sw`, and its endpoint `s` uses an old colour while `w` uses the fresh
   one.  The symmetric argument applies to `H+w`.  The original colouring
   supplies the matching upper bounds, so both chromatic numbers equal
   `k-1`.
4. If a `(k-2)`-colouring of `H` omitted a colour on `S=N_H(s)`, assigning
   that colour to `s` would colour `H+s`, contradicting item 3.  Thus `S`
   is saturated in every such colouring; likewise `T`.
5. In the model lift, singleton bags `{s}` and `{w}` are disjoint from the
   model in `H`, adjacent through the literal edge `sw`, and each has a
   literal edge to every branch set through its `S` or `T` contact.  With
   the `k-2` pairwise adjacent connected bags of the rooted model, these
   are exactly `k` valid branch sets.

No connectivity, minor-criticality, or near-clique geometry is used in
this reduction.  Such extra structure is necessarily part of any theorem
that forces the required doubly rooted model.
