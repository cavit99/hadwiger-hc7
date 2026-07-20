# Independent audit of the opposite single-vertex flip theorem

## Verdict and audited revision

**Verdict: GREEN.**

This audit checks the complete source file
[`hc7_order9_opposite_single_vertex_flip.md`](hc7_order9_opposite_single_vertex_flip.md)
at SHA-256

```text
4388a3c1fc27f3e490db43df191ac1871eec729525c0b5d11933a5dde63209d7
```

The glued colouring of `G-b`, saturation of `N_G(b)`, exact shore
allocation of the two relevant colours, the two forced bichromatic paths
and their parities, the common-host component lemma and odd cycle, the
order-seven/eight/full-boundary corollary, and the palette-drop
normalization are correct.

## 1. Gluing after deleting the operated vertex

The boundary colourings `phi,psi` agree on `B-{b}`.  On that set the
restrictions of `alpha` and `beta` therefore agree as labelled colourings.
The `A` part of `beta` and the `D` part of `alpha` retain all their proper
edges to `B-{b}`, and there are no `A-D` edges.  The displayed assignment
is consequently a proper `q`-colouring `c` of all of `G-b`.

If a colour were absent from `c(N_G(b))`, assigning it to `b` would extend
`c` to a proper `q`-colouring of `G`, contrary to the hypothesis.  Thus
every colour occurs on a neighbour of `b`.

In `alpha`, the vertex `b` has colour `i`, so no neighbour of `b` in
`D union (B-{b})` has colour `i`.  Since `c` equals `alpha` there, every
`i`-coloured neighbour under `c` lies in `A`.  Saturation makes that set
nonempty.  The symmetric argument using `beta(b)=j` puts every
`j`-coloured neighbour in `D` and again proves nonemptiness.  This verifies
both inclusions and the exact opposite-shore allocation in (2.2).

## 2. The two shore paths and parity

Under `alpha`, colour `j` is absent from the boundary and `b` has colour
`i`.  Every other boundary vertex of colour `i` lies in `C` and is
nonadjacent to `b`, because `phi` is proper.  Hence `{b}` is a component of
the boundary `i`--`j` graph.  If its full two-colour component in the
`D`-closed side met no other boundary vertex, switching that full component
would change the boundary trace exactly from `phi` to `psi`, contradicting
the assumed rejection of `psi` by that shore.  It must meet `C`.

A shortest path from `b` to its first later boundary vertex therefore has
all internal vertices in `D`; this gives `P_D`.  The identical reverse
argument starts from `beta`, in which `b` has colour `j`.  Although the
colour on `b` is reversed, its nonadjacency to `C` was already forced by
the proper colouring `phi`, so `{b}` is again a singleton boundary
two-colour component.  This yields `P_A` with internal vertices in `A`.

This also proves `C` is nonempty.  Each path has a nonempty interior,
because `b` has no edge to `C`, and the two interiors are disjoint because
they lie in the disjoint open shores.  Under `beta`, the ends of `P_A`
have colours `j,i`, so its length is odd.  Under `alpha`, both ends of
`P_D` have colour `i`, so its length is even.  These parity statements use
the alternating colours along a proper bichromatic path and have the
orientations claimed in the source.

## 3. Common-host component and odd cycle

Fix any two colours `r,s` in the proper colouring `c` of `G-b`.  Suppose no
`r`--`s` component contains both an `r`-coloured and an `s`-coloured
neighbour of `b`.  Switch all components containing an `r`-coloured
neighbour.  Such components contain no `s`-coloured neighbour by the
supposition.  Every old `r`-neighbour changes to `s`, and no old
`s`-neighbour changes to `r`.  Colour `r` is now absent from `N_G(b)`, so
`b` can be coloured `r`, contradicting non-`q`-colourability.  The
component lemma is therefore valid.

Apply it to `i,j`.  By the exact allocation from Section 1, the two selected
neighbours lie respectively in `A` and `D`.  Any path between them in
`G-b` must meet `B-{b}` because `A,D` are anticomplete.  It is an
`i`--`j` path.  On `B-{b}`, the glued colouring equals `phi`; colour `j`
is absent there, and the vertices of colour `i` are exactly `C`.  Hence
every boundary vertex on the path belongs to `C`.

The endpoint colours differ, so a simple bichromatic path between them has
odd length.  Adding `b` and its two endpoint edges gives a simple odd cycle
through `b`, with the asserted shore placement and boundary intersection.
If `C={x}`, the two earlier shore paths have exactly the common endpoints
`b,x` and otherwise disjoint vertices.  Their union is a cycle of length
odd plus even, hence odd, and meets the boundary exactly in `{b,x}`.

## 4. Order-nine full-neighbourhood response

For each shore path, its nonempty connected interior lies in a component
`Q_Z` of `G-B`.  Its full neighbourhood is contained in `B`.  The opposite
open shore is nonempty and lies outside `Q_Z union N_G(Q_Z)`, so this full
neighbourhood is the boundary of an actual separation, rather than merely
a local attachment set.  Seven-connectivity gives the lower bound seven;
`|B|=9` gives the upper bound nine.

Orders seven and eight are the claimed actual separations.  At order nine,
containment in the nine-vertex boundary is equality, so the connected
component `Q_Z` is adjacent to every literal boundary vertex.  The two
supporting components are distinct because one lies in `A` and the other
in `D`.

No connectedness or boundary fullness of the entire open shores is silently
assumed in this argument.

## 5. Palette-drop normalization and orientation

Only the two interchanged colours can change their global occurrence.  If
`theta` uses all `q` colours but `theta'` uses fewer, one of `i,j`
disappears.  Suppose it is `j`.  Every old `j`-vertex must lie in the
switched component `K`; otherwise it remains `j`.  No old `i`-vertex can
lie in `K`, because it would become `j`.  Thus every vertex of `K` had the
same old colour `j`.  A colour class is independent, whereas `K` is
connected, so `K` is a singleton `{b}` and was the entire old `j` colour
class.

The old colour `i` existed because `theta` was full, and no old `i`-vertex
was switched.  Therefore one remains outside `K`.  Reversing the step
recolours `b` from `i` to the previously unused colour `j`, exactly matching
the normalization (1.2), with a nonempty set `C` of other `i`-vertices.

The final application is correctly conditional on the two traces being
owned by opposite shores.  Full-trace ownership alone does not assign the
non-full endpoint to a shore, and the source does not claim that it does.
When opposite ownership is available, reversing the palette-dropping step
orients `phi,psi` as in Theorem 2.1 and all its conclusions follow.

## 6. Trust boundary

The theorem begins only after two boundary traces one literal recolouring
apart have been found and are known to extend opposite closed shores.  It
does not prove the existence of such a pair.  The two forced shore paths
need not have distinct remote boundary ends, need not align with named
minor-model branch sets, and need not split into the two vertex-disjoint
crossing edges required by stronger direct-entry results.

An order-seven or order-eight separator returned by the corollary carries
the obstructed transition, not a common complete boundary colouring.  Two
boundary-full components in the order-nine outcome are anticomplete and
are not automatically adjacent branch sets.  The result therefore does
not itself give a compatible colouring, a strict state-preserving descent,
or an explicit `K_7`-minor model.
