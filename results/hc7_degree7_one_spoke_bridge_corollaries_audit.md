# Independent audit: degree-seven one-spoke bridge corollaries

## Verdict

**GREEN** at the exact source revision

```text
61ed79428d43a82043ea024e5c804f12d59f74c1082be726865d588338039d37  results/hc7_degree7_one_spoke_bridge_corollaries.md
```

The three corollaries are correct under their stated hypotheses.  They do
not repair the missing centre adjacency or prove `HC_7`.

## 1. Spanning enhancement

For the complement edge `ab` used by the aligned near-`K_7` theorem,
seven-connectivity makes `J=G-{u,a,b}` connected.  The five rooted `K_5`
bags have connected union.  Every component of their complement in `J`
has an edge to an old bag and may be assigned wholly to one such bag,
preserving disjointness, connectivity, every boundary root and every old
adjacency.  Reinserting `u,a,b` exactly as in the promoted construction
therefore gives a spanning labelled model.

Absorption may repair one of two missing centre adjacencies, changing a
two-missing-adjacency model into a one-missing-adjacency model.  Repairing
all missing adjacencies would give a forbidden `K_7` minor.  The source
correctly warns that absorbed vertices need not retain the five-colour
provenance, so spanning-bag orders are not a descent parameter.

## 2. Off-pole-shore edge response

If `h=xy` has an endpoint in `C`, deleting `h` leaves the induced closed
shore `B=G[N[u]]` unchanged.  Restriction of any six-colouring of `G-h`
to `B` therefore gives, by the exact matching-language theorem, a boundary
matching of order two or three.  The endpoints `x,y` must have one colour,
since otherwise `h` can be restored.  For every other palette colour, if
`x,y` lay in different bichromatic components, swapping the component
containing `x` would separate their colours and again permit restoration
of `h`.  This also excludes an absent alternate colour.  Expanding a
colouring of `G/h` gives a colouring of `G-h`, so the same conclusions
follow.

For a crossing edge in `E(C,S)`, the resulting bichromatic component is
global; the source correctly makes no shore-internal linkage claim.

## 3. Dual orientation

If `N_F(a)={b,x}`, triangle-freeness of `F` gives `bx in E(H)`.  The rooted
model for `ab` therefore yields the connected deficient bag
`{b} union B_x`; all other contacts are present, and a contact from `{a}`
to that bag would produce a forbidden `K_7` model.  Repeating with `ax`
gives `{x} union B_b`.  Both models retain pole `{u}`, centre `{a}`, and
the same four remaining boundary labels, while their rooted interiors need
not coincide.

## Trust boundary

The connected one-missing-adjacency trichotomy applies only to the
spanning `K_7^-` outcome, not directly to the two-missing-adjacency outcome.
Nothing here converts a first-hit collision into a labelled split, bounds
a returned separator above by seven, synchronizes boundary colourings, or
supplies a well-founded rank.  These limitations are stated correctly.

## Dependencies checked

- the promoted degree-seven aligned near-`K_7` theorem;
- the exact matching-language and proper-minor-response theorem; and
- the connected one-missing-adjacency trichotomy.

No unresolved mathematical assumption was found.
