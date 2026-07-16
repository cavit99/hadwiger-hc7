# Independent audit: exact eight-terminal bundle, analytic order-ten branch

## Verdict and scope

**GREEN for Section 3 and Corollary 3.4.**  The exact order-ten
`C_8/AABBAABB` classification, its converse, and all sixteen owner-pair
quotients in
[`hc7_eight_terminal_exact_bundle.md`](hc7_eight_terminal_exact_bundle.md)
are correct.

This audit does **not** independently certify the full order-eight and
order-nine catalogue.  Those sections retain their stated computational
trust boundary.

## 1. Contraction and path-apex criteria

For an edge `uv` of a simple three-connected graph `J` of order at least
five, contracting `uv` is three-connectivity-preserving exactly when
`J-{u,v}` is two-connected.  A separator of the contraction not containing
the contracted vertex lifts to `J`; one containing it contradicts
connectivity after deleting zero or one further vertex from `J-{u,v}`.

For a path plus an apex joined to a nonempty set `W`, two-connectivity is
equivalent to both path ends lying in `W`.  If both do, the apex reconnects
the two intervals left by deletion of any path vertex.  If an end is absent,
the first attachment from that end is a cutvertex.  Both criteria are used
with graphs of the required order.

## 2. Charge sets and the exact terminal cycle

In an order-ten terminal-irreducible kernel there are two nonterminals
`x,y`.  Wu's charge sets are disjoint terminal sets of order at least four;
they therefore partition the eight terminals into two four-sets.  Every
terminal is degree three, adjacent to its charging nonterminal and to two
terminals.  It cannot also see the other nonterminal.  Thus `K[T]` is
two-regular, and three-connectivity makes it connected after deleting
`x,y`; it is exactly `C_8`.

If `xy` existed, deleting its ends would leave that cycle, so the contraction
criterion would make `xy` a terminal-legal contractible edge.  Hence the
nonterminals are nonadjacent and their terminal neighbourhoods are precisely
the complementary charge four-sets.

## 3. Cyclic word and exclusion of `AAAABBBB`

Colour the terminal cycle by the nonterminal to which each terminal is
adjacent.  For `a in A`, deletion of `x,a` leaves the path `C_8-a` plus `y`
attached exactly to the four `B` vertices.  The path-apex criterion says
`xa` would be contractible exactly when both cyclic neighbours of `a` were
in `B`.  Irreducibility therefore gives every `A` vertex an `A` neighbour;
symmetrically every `B` vertex has a `B` neighbour.

Every monochromatic cyclic run consequently has length at least two.  With
four letters of each kind, the only words are `AAAABBBB` and `AABBAABB`, up
to rotation and reversal.  In `AAAABBBB`, deleting the two endvertices of
the `A` run isolates `x` together with the two internal `A` vertices from
`y` and the `B` run.  Three-connectivity excludes it.

## 4. Converse

The normal-form `AABBAABB` graph is three-connected.  The deletion cases are
exhaustive:

* deleting both nonterminals leaves `C_8`;
* deleting one nonterminal and one terminal leaves a terminal path, with the
  other nonterminal attached to at least three vertices;
* deleting two terminals leaves at most two path components of the cycle.
  If there are two, some colour occurs in both.  Indeed, the only way no
  colour could occur in both would be one `A`-only component and one
  `B`-only component, but a monochromatic component lies within one two-run
  while the other two-run of that colour remains in the other component.
  The corresponding nonterminal joins the components.

Deleting fewer vertices is easier and leaves the graph connected.  Thus no
separator of order at most two exists.

The only terminal-legal edges are the spokes `xa` and `yb`.  Each terminal
has one same-colour cyclic neighbour, so after deleting the spoke ends the
remaining path has an end not adjacent to the surviving nonterminal.  The
path-apex criterion makes the remainder not two-connected, and the
contraction criterion makes every spoke noncontractible.  The graph is
terminal-irreducible.

## 5. Owner pairs and independent replay

For every `(w_x,w_y) in A cross B`, the bags `{x,w_x}`, `{y,w_y}` and the six
remaining terminal singletons are connected, pairwise disjoint, and contain
one terminal each.  Their quotient consists exactly of the terminal cycle
plus the two owner stars into `A` and `B`; there is no omitted `xy` edge or
cross-neighbour of either nonterminal.  All sixteen owner pairs are therefore
legal.

An independent rerun of the normal-form generator gave

```text
ordered templates       10080
owner families           5040
family sizes               {16}
template digest  78217d8621685a5839aa55172a51e3470297e6f989516c0455a4884471923418
family digest    9b0f7300357d8b8443e9ddacf5b15118859642f5c77bbfe559cab120fc182ac8
```

The factor of two is exactly interchange of the ordered nonterminals.  The
safe downstream quantifier remains: for every exact template, choose the
owner pair only after that template is known.
