# Audit: singleton-gate holonomy

## Verdict

**GREEN.**  The theorem is a genuine two-step composition result, but its
scope is one fixed five-row frame and two single connected gates.  It does
not exclude cycles which change a fixed row, use a nonsingleton gate, or
use the concentrated two-piece exchange.

## Checks

1. The second donor is exactly `A'=A union Z`.  For a label in the first
   missing set `D`, `A` is wholly anticomplete to that row.  Thus every
   donor portal for a common label `D cap E` lies in `Z`.
2. A legal second gate must meet every row currently missed by `W`, so it
   contains one of those old-gate portal vertices.  This proves literal
   intersection, not merely equality of quotient labels.
3. Absence of a `K_7^-` minor makes two consecutive two-element missing
   sets intersect by the audited pair-overlap theorem.  No assumption
   about which label is common is made.
4. If `Z,Y` are singletons, their nonempty intersection makes them the
   same actual vertex.  Removing it from `A union Z` and adding it back to
   `W` restores the exact old bags.  The involution theorem restores the
   exact old missing set.
5. The theorem does not claim that a nonsingleton next gate contains all
   of `Z`; it contains a literal old-gate portal for each common label.
   Nor does it constrain a next pivot whose donor is one of the fixed
   rows, because that move changes the five-row frame.
6. The result is compatible with coherent two-apex examples and with the
   previously exhibited `K_2`-join-icosahedron inverse pair: that example
   is a `K_7^-` state and the displayed second move is precisely the
   inverse.

