# Independent audit: eight-terminal rooted-carrier trichotomy

## Verdict

**GREEN.**  The proof of
[`hc7_eight_terminal_rooted_carrier_trichotomy.md`](hc7_eight_terminal_rooted_carrier_trichotomy.md)
is valid as stated: every eight prescribed vertices in a simple
three-connected graph root a `C_8`, a `K_{3,5}`, or the stated graph `F_8`.
The result is independent of `HC_7`.

The audit checked the published inputs, every suppressed-multigraph case in
Lemma 3.1, the contraction criterion used there, and the lift through the
terminal-legal contraction sequence.  The deterministic census was rerun as
secondary evidence; it is not a premise of the proof.

## 1. Published inputs and terminal kernel

Wu's published theorem has exactly the strength used: in a simple
three-connected graph of order at least five, a vertex incident with no
contractible edge has at least four degree-three neighbours, each incident
with exactly two contractible edges.  The already audited terminal-kernel
argument therefore gives an irreducible rooted minor with at most

```text
floor(8/4)=2
```

nonterminals.  The charge sets of distinct nonterminals are disjoint because
a shared charged terminal would have its two terminal-terminal contractible
edges and two distinct nonterminal neighbours despite having degree three.

The Chvatal--Erdos and Moon--Moser statements are also used with their correct
hypotheses.  In particular, the balanced bipartite graph in Lemma 2.1 has
parts of order four, and every opposite nonedge has degree sum at least five.

## 2. Order-eight base

If the graph is non-Hamiltonian, Chvatal--Erdos gives an independent set of
order at least four, while minimum degree three bounds its order by five.
The independence-five case gives a literal spanning `K_{3,5}`.

In the independence-four case, let `I` be the independent four-set and `B`
its complement.  If every member of `B` has at least two neighbours in `I`,
Moon--Moser gives a spanning cycle.  Otherwise choose `b_0` with at most one
such neighbour.

* If it has none, minimum degree makes `b_0` complete to the other three
  members of `B`, while every member of `I` is complete to those same three;
  this is a spanning `K_{3,5}`.
* If its sole neighbour in `I` is `i_0`, then `i_0` and `b_0` each miss at
  most one of the remaining three vertices.  They cannot miss the same one:
  deleting the other two would isolate the edge `i_0b_0`.  Thus the two
  possible missing cross-edges are independent.  Deleting zero, one, or two
  suitable extra cross-edges leaves exactly the displayed `F_8`.

The labelled counts are correct.  The automorphism groups of `C_8`,
`K_{3,5}`, and `F_8` have orders `16`, `3!5!=720`, and `12`, respectively,
giving `2520`, `56`, and `3360` masks.  Their edge counts are `8`, `15`, and
`14`, so the three mask families are disjoint.

## 3. One-nonterminal kernel

Let `x` be the nonterminal and `H=M-x`.  The graph `H` is two-connected.
Wu's four degree-three neighbours of `x` have degree two in `H`, so if `D`
is the degree-two set and `B=V(H)-D`, then `|D|>=4` and `|B|<=4`.

When `B` is nonempty, each component of `H[D]` is a path with distinct ends
in `B`: a repeated end would be a cutvertex.  Suppression gives the stated
loopless multigraph `K`; its positive weights sum to `8-|B|`, and a Hamilton
cycle of `H` is exactly a spanning cycle of `K` containing every positive
edge.  If `|B|=1`, deleting its sole vertex leaves one path, whose two ends
both return to it and force its degree to be two, a contradiction.  Thus the
suppression proof loses no small case.

### The contraction escape

For an edge `uv` in a simple three-connected graph of order at least five,
`uv` is contractible exactly when deleting both ends leaves a two-connected
graph.  One direction follows by deleting the contracted vertex; in the
other, a cut of order at most two in the contraction either lifts to the
original graph or contains the contracted vertex and contradicts
two-connectivity after deleting `u,v`.

Consequently, if a positive suppressed edge `ab` has weight one, with
internal vertex `z`, and `K-ab` is two-connected, then `H-z` is
two-connected.  Three-connectivity of `M` forces `xz`: after deleting `a,b`,
the vertex `z` would otherwise be isolated.  The edge `xz` would then be
contractible.  This proves the key prohibition (3.4).

### Exhaustion by the number of branch vertices

* **Two branch vertices.**  A multigraph cycle here means two distinct
  parallel routes.  With at most two positive routes, choose those routes
  and obtain a Hamilton cycle.  With at least three positive routes, each is
  removable, hence has weight at least two.  The weight budget six leaves
  exactly three weight-two routes, plus at most one zero route.  This is
  `Theta_{3,3,3}`.
* **Three branch vertices.**  The underlying graph is a triangle.  A failure
  of a positive-spanning triangle requires two positive parallel routes on
  one pair.  They consume at least four of the five weight units.  Minimum
  degree three at the third vertex forces a positive route in another
  parallel class; it has weight one and is removable, contradicting (3.4).
* **Four branch vertices, underlying `C_4`.**  Every vertex lies on a
  parallel class.  The marked parallel classes contain a matching covering
  all four vertices.  Choosing a positive route on each matched pair consumes
  the full weight budget as two weight-two routes.  The expanded four-cycle
  through them is Hamiltonian.
* **Four branch vertices, underlying `K_4-e`.**  Each of the two nonadjacent
  degree-two tips lies on a parallel class.  Positive routes selected from
  those two distinct classes are removable and hence each has weight at least
  two.  They exhaust the budget and lie on a common spanning four-cycle.
* **Four branch vertices, underlying `K_4`.**  Every positive route is
  removable, so at most two exist.  One route, or two on distinct pairs, lies
  on a spanning four-cycle.  The only residue is two parallel weight-two
  routes on one pair, with all other pairs represented by zero edges.

In that last residue all four internal route vertices are adjacent to `x`.
Deleting the common route ends forces `x` to see one of the other two branch
vertices, say `r`.  But `H-r` is two-connected, making `xr` contractible.
This eliminates the residue.

In the sole theta exception, deleting the two displayed neighbours of each
internal route vertex forces `x` to see all six internal vertices.  Both
cycles (3.5) and (3.6) are literal.  Relabelling the three paths covers every
one of the six possible owners.

## 4. Two nonterminals and rooted lifting

The two disjoint Wu charge sets each have at least four elements and lie in
the eight terminals, so they partition the terminal set.  Every terminal has
degree three, with exactly one nonterminal neighbour and exactly two terminal
neighbours.  Deleting the two nonterminals leaves a connected two-regular
graph, hence `C_8`.

Terminal-legal contraction never identifies two roots.  Expanding the
contraction sequence preserves bag connectivity, disjointness, every literal
root, and every required carrier adjacency.  In the theta exception the sole
nonterminal bag is merged into one adjacent terminal bag, so every lifted bag
still contains exactly one literal terminal.  In the two-nonterminal branch
the nonterminal bags may simply be deleted.

## 5. Independent finite replay and scope

The standard-library/nauty verifier was rerun and reported

```text
carrier_counts 2520 56 3360 5936
order8 (2589, 2388, 18, {15: 1, 14: 2, 13: 11, 12: 4}, ...)
order9 (84242, 80890, 97, 6, 97, ...)
PASS
```

The theorem deliberately forgets contacts of the one- and two-nonterminal
kernels.  A bare rooted `C_8` is not, by itself, a decoder for the active
overlap-one composition cell.  Any such application must verify all `5936`
labelled carrier masks or retain the exact kernel contact data.  This audit
does not promote a palette-to-label lift or claim closure of `HC_7`.
