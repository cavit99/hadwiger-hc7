# Independent audit: crossed-frame disk barrier

Audited file:
`barriers/hc7_exact7_crossed_frame_disk_barrier.md`.

## Verdict

**GREEN.**  The note is a local structural barrier only.  It does not
construct a seven-connected contraction-critical graph and does not claim
to refute the exact `HC_7` conversion.

## Literal obstruction

The present graph on

\[
                         U=\{0,2,4,5,6\}
\]

is the cycle `0 2 6 5 4 0`, while its missing edges form
`0 5 2 4 6 0`.  Two disjoint edges of the missing cycle have alternating
ends in the present-cycle order.  Exact traces ensure that an end-to-end
path in each of the two disjoint connected frame blocks has no internal
vertex in `U`; the two paths are vertex-disjoint.  The Jordan-curve
argument therefore excludes a disk drawing with the literal present cycle
as boundary.  A cycle with two disjoint chords joining alternating ends is
exactly a rooted subdivision of `K_4`, so the second assertion of Lemma
1.1 is also correct.

## Small certificate

In `H_0`, the blocks `0-p-5`, `2-q-4`, and `{6}` are connected, disjoint,
and pairwise adjacent through literal present-cycle edges.  The graph has
seven vertices but is not complete, so it has no `K_7` minor: seven
nonempty branch sets would all have to be singletons.  After adding
`w-ell-p`, the displayed `w`-carrier contacts only the first named block,
and `{w,0,5}` is independent.  The enlarged graph has eleven edges; every
`K_7` model needs at least one distinct host edge for each of its 21 pairs
of branch sets, so it remains `K_7`-minor-free.  Thus the rooted `K_4`
topology alone gives no second decoration contact.

## Spanning rural certificate

The supplied verifier was rerun independently and returned all three
GREEN checks.  Direct inspection also confirms:

* the wheel carrier is three-connected with trace `{0,5}`;
* `X={2,m,4,6}` and `Y={ell}` are connected and anticomplete;
* the nonroot portal sets are exactly
  `{q1,q2,q3}` and `{p1,p2,p3,p4,p5}`;
* contracting `X,Y` gives the stated planar quotient; and
* `W={w,ell}` supports only the carrier decoration.

The explicit bags and tree edges in
`barriers/hc7_exact7_crossed_frame_disk_barrier_verify.py` satisfy the
vertex-cover, edge-cover, and running-intersection axioms of a tree
decomposition, and the largest bag has order six.  Hence the host has
treewidth at most five and cannot contain `K_7`, whose treewidth is six,
as a minor.

## Scope

The certificate deliberately lacks seven-connectivity and
contraction-criticality.  It proves exactly that a planar contracted
two-pole quotient, large disjoint portal sets, and the supported crossed
frame do not statically imply a `U`-boundary disk page, a literal `K_7`, or
a second attained decoration.  The source's conclusion that a positive
proof must spend a proper-minor transition or further global labelled
geometry is therefore justified.
