# Cold audit of the five-root/six-terminal carrier theorem

## Verdict

**GREEN.**  The theorem in
[`hc7_four_connected_five_good_terminal_carrier.md`](hc7_four_connected_five_good_terminal_carrier.md)
follows from the audited four-connected clique-or-fan theorem, and both
positions of the sixth terminal are handled by literal peripheral-cycle
bags.

## Checks

Apply the source theorem to the five-set `W`.  Its rooted-`K_4` outcome is
exactly the first outcome here.  In the other outcome one facial cycle `C`
contains all five roots, and `R=H-V(C)` is nonempty, connected, and meets
every vertex of `C`.

If `b in C`, cutting `C` at all six terminals gives six disjoint rooted
cycle bags.  Enlarging any prescribed bag by `R` makes it universal and
leaves the other five bags in path order.  If `b notin C`, then `b in R`;
the five boundary-arc bags form a cycle and the single bag `R` is a
`b`-rooted universal bag.  This gives `K_1 join C_5`, hence the claimed
`K_1 join P_5` after ignoring one rim edge.

The composition corollary uses only the four roots in `W` and the three
singleton vertices of `I`.  Thus it remains valid if either omitted
terminal was absorbed by one of the four rooted bags.  Every cross contact
is supplied by the literal root in `W`, not by an assumed clean model.

The theorem does **not** prescribe the hub/path labels of the rooted fan;
the source file records this correctly as a decoder obligation.
