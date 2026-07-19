# A bounded check of one tight `C_5` endpoint

**Status:** deterministic bounded computation; mechanism evidence only.  This
does not prove the unbounded Gallai-tree endpoint theorem, does not exhaust
all four-colour boundary graphs, and does not prove `HC_7`.

## Family tested

The host has the vertex partition

\[
 \{\ell\}\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad |S|=7,
\]

where:

- `S=s_0...s_6s_0` is an induced `C_7`;
- `R=r_0...r_4r_0` is an induced `C_5`;
- `ell` is adjacent to every vertex of `S` and to no vertex of `R`;
- there are no other edges except the enumerated `S-R` edges.

The boundary has the proper four-colouring

\[
 (c(s_0),\ldots,c(s_6))=(0,1,0,2,1,3,2).              \tag{1}
\]

The simultaneous-contraction trace is normalized by deleting

\[
 s_0r_0,\qquad s_1r_2,                                  \tag{2}
\]

and assigning

\[
 (c(r_0),\ldots,c(r_4))=(0,4,1,5,4),\qquad c(\ell)=4.  \tag{3}
\]

For each `r_i`, its `S`-neighbourhood:

1. has order at least five;
2. meets all four colour classes in (1); and
3. contains no boundary vertex of colour `c(r_i)`, except that `r_0` has
   `s_0` as its unique such neighbour and `r_2` has `s_1` as its unique
   such neighbour.

Thus (3) is a proper six-colouring after deleting the two edges in (2), and
it is the expansion of a proper colouring after simultaneously contracting
those two vertex-disjoint edges.  The boundary lists of all vertices of
`R` are the common two-element list `{4,5}`.  Every vertex of `R` has total
degree at least seven.  The check additionally requires both connected
subgraphs

\[
 R[\{r_0,r_1\}],\qquad R[\{r_2,r_3,r_4\}]
\]

to be adjacent to every literal vertex of `S`.

## Exhaustion and exact minor test

There are respectively `5,19,5,19,19` allowed boundary-neighbourhoods for
`r_0,...,r_4`, hence `171475` attachment tuples.  The deterministic check
obtains:

```text
normalized C5 tight-endpoint family
attachment tuples: 171475
two S-full arcs: 85536
minimum degree at least seven: 647
seven-connected: 647
edge-minimal seven-connected tuples: 234
every edge-minimal tuple has a K7 minor: yes
therefore every seven-connected tuple has a K7 minor: yes
```

All `234` edge-minimal seven-connected tuples have `29` `S-R` edges.  Every
one of the `647` seven-connected tuples contains one of them as a spanning
subgraph with the same fixed cycle edges.  It is therefore enough to test
the minimal tuples.

The `K_7`-minor test is exact.  In a connected graph, any clique-minor model
can be enlarged to a spanning model.  Contracting the connected branch sets
then produces a graph containing `K_7`.  Conversely, any contraction
sequence ending at a graph containing `K_7` gives a minor model.  The script
exhausts the possible edge contractions, with memoization used only to
reduce running time.

Run:

```bash
PYTHONPATH=active/runtime/deps \
  python3 archive/hc7_gallai_c5_tight_endpoint_bounded_check.py
```

## Interpretation

This normalized family is the smallest natural realization of the proposed
all-tight endpoint with an odd-cycle open shore, two disjoint boundary-full
connected subgraphs, an exact four-colour boundary trace, and a common
two-element list on the odd cycle.  No seven-connected `K_7`-minor-free
example survives.

The computation is positive evidence for using seven-connectivity to break
the tight odd-cycle endpoint.  Its trust boundary is important: the
boundary graph was fixed to one `C_7`, the shore was fixed to `C_5`, and the
two boundary-full subgraphs were fixed to the displayed arcs.  A proof must
still handle arbitrary boundary graphs of chromatic number at most four,
arbitrary Gallai trees (including clique blocks and block trees), and other
placements of the two marked edges.
