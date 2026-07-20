# Internal audit: common-colouring barrier for two full shores

**Verdict:** **GREEN** for the exact source revision identified below.

This is a separate internal mathematical audit, not external peer review.
It verifies the boundary graph, the two closed-side six-colourings, the
incompatibility of their complete extension languages, the explicit
`K_7`-minor model in the union, and the stated trust boundary.

## Audited revision

The audited source is
[`hc7_k5minor_boundary_full_shores_common_colouring_barrier.md`](hc7_k5minor_boundary_full_shores_common_colouring_barrier.md)
at SHA-256

```text
18a3f084fd92610090b8f478787a200e9c0610ee914d0eeed52c1e8833959da1
```

## 1. Boundary and shore structure

The displayed boundary edge set is the disjoint union of the triangle
`dabd`, the edge `xz`, and the isolated vertices `y,t_1,t_2,t_3`.
Consequently `d` has exactly the adjacent boundary neighbours `a,b`, and
the boundary has no `K_5` minor.

Both `L` and `R` induce copies of `K_5`, so they are connected.  No edge is
placed between them.  On the `L` side, `x,y` meet every member of `L` and
every other boundary vertex meets `l_1`; on the `R` side, `y,z` meet every
member of `R` and every other boundary vertex meets `r_1`.  Thus both shores
are adjacent to every literal boundary vertex.

## 2. The displayed six-colourings

On the `L` side, the five vertices `l_i` receive distinct colours
`1,...,5`, while `x,y` receive colour six.  Every remaining boundary
vertex is adjacent in `L` only to `l_1` and receives a colour different from
one.  The triangle `dabd` has colours `2,3,4`, and `xz` has colours `6,2`.
This is a proper six-colouring.

The symmetric check on the `R` side is identical: the vertices `r_i` use
`1,...,5`, the vertices `y,z` use six, all boundary vertices adjacent only
to `r_1` avoid one, the boundary triangle uses `2,3,4`, and `xz` uses
`2,6`.

## 3. Incompatibility is forced in every extension

In any six-colouring of the `L`-closed side, its `K_5` uses five distinct
colours.  Each of `x,y` is complete to that clique, so both must use the
unique sixth colour.  Hence every `L`-side boundary trace satisfies
`c(x)=c(y)`.

Similarly, every `R`-side boundary trace satisfies `c(y)=c(z)`.  A trace
common to both sides would therefore have `c(x)=c(z)`, contradicting the
literal boundary edge `xz`.  This proves disjointness of the two complete
extension languages, not merely failure of the two displayed colourings to
align.

## 4. Explicit `K_7`-minor model and scope

The seven sets

```text
{l_1},...,{l_5}, {x,z}, {y,r_1}
```

are pairwise disjoint and connected.  The first five are pairwise adjacent.
The set `{x,z}` meets every one of them through `x`, and `{y,r_1}` meets
every one through `y`.  The final two sets are adjacent through the edge
`zr_1`.  They therefore form an explicit `K_7`-minor model.

Accordingly the example does not satisfy `K_7`-minor exclusion and is not a
counterexample to `HC_7`.  It refutes only the stated inference from a
`K_5`-minor-free boundary, a simplicial triangle vertex, connected
anticomplete boundary-full shores, and closed-side six-colourability to a
common boundary colouring.  The source's trust boundary is exact.
