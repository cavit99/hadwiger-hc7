# Independent audit: coupled-response Hall tableau barrier

**Verdict:** **GREEN** for the exact source and verifier revisions below.

This is a separate internal mathematical and computational audit, not
external peer review.  It checks the simultaneous-switch normal form, the
boundary partitions and demands, the Hall-deficient incidence pattern, the
literal shell, the verifier, and the stated trust boundary.

## Audited revisions

Barrier source:
`barriers/hc7_order8_coupled_response_hall_tableau_barrier.md`

```text
f34e4dfaf6e59f4f0dc042268024a58732d8148fef1b95d73f559bd572688797
```

The mathematical source audited directly had SHA-256
`db5c05e20ce036edaccca22fa790371052b1a0935f10971f0498e205476f13b2`.
The final source differs only by replacing the pending-audit status with
the adjacent GREEN-audit link.  No mathematical statement, construction,
calculation, verifier reference, or trust-boundary sentence changed.

Deterministic verifier:
`barriers/hc7_order8_coupled_response_hall_tableau_barrier_verify.py`

```text
ec85ddebda9f528bc23a1978f7ff17ad936f970fa859d3485efb8847d8c4caf7
```

The verifier was run directly and returned exactly

```text
GREEN minimum coupled-response Hall tableau
```

It also compiles successfully with Python's bytecode compiler.

## 1. Simultaneous-switch normal form

The central colouring is proper on `H=G-{wu,wq}` and gives `w,u,q` colour
zero.  The `{0,i}`-component `A` through `u` excludes `w,q`, while the
`{0,j}`-component `D` through `q` excludes `w,u`.  When `A,D` are disjoint,
the only new monochromatic edges created by both Kempe interchanges have an
old `i`-coloured endpoint in `A` and an old `j`-coloured endpoint in `D`.
Both endpoints become zero.  All other cross-palette edge types remain
bichromatic, and each individual interchange is proper away from the other
component.

The bypass hypothesis supplies at least one `i`--`j` joining edge, so the
set `F` of precisely these bad edges is nonempty.  After deleting `F`, the
simultaneous assignment is proper.  The first switch changes `u` away from
zero but does not change `w`; the second changes `q` away from zero but not
`w`.  Thus `wu,wq` can both be restored.  If `F` is a singleton, this is
indeed one operation-specific edge-deletion response.  The lemma makes no
claim in the intersecting-component case and does not need one for the
displayed shell.

## 2. Boundary graph and partitions

The boundary has nine vertices, the minimum possible from
`B=(S-{e}) dotcup W`, `|S|=8`, and `|W|>=2`.  Every displayed block in the
central partition is independent under the listed boundary edges, and the
sixth colour is unused.

Switching the component whose boundary footprint is `{y_d}` merges `y_d`
with `w` and removes it from the large colour-four block, producing exactly
`Sigma_E`.  Switching the component whose boundary footprint is `{d}`
merges `d` with `w` and leaves `r` as a singleton, producing exactly
`Sigma_C`.  The partitions are visibly distinct.

For `Sigma_C`, the singleton-block vertices are exactly
`U={r,x_d,x_e}`.  The edges `rx_d,rx_e,x_dx_e` make this set a triangle, so
it is the maximum singleton clique.  There are five blocks and three clique
singletons, giving demand two.  Direct inspection of the listed boundary
edges gives

\[
 R_U(\{w,d\})=\{w,d,r,x_e\},
 \qquad
 R_U(\{y_d,y_e,x_0,y_0\})
  =\{y_d,y_e,x_0,y_0,r\}.
\]

The full support `Q_0` meets both required sets.  The support `Q_1` misses
only `r`, which belongs to both required sets, so it meets neither.  The
incidence matrix is therefore exactly

```text
[[True, True], [False, False]]
```

and Hall fails at demand two in the strongest nonisolated-right-vertex
form.  For `Sigma_E`, the singleton vertices are exactly `x_d,x_e`, which
are adjacent.  Five blocks minus a maximum singleton clique of order two
gives demand three, as stated.

## 3. Literal shell

The constructed graph has vertex partition `E dotcup B dotcup C`, with
`C=Q_0 dotcup Q_1`.  The helper paths make `E` connected and full to `B`
without adding vertices to either selected bichromatic component.  The set
`Q_1` is connected, meets every old boundary vertex in `S`, meets every
member of `B-{r}`, and misses `r`.  The set `Q_0` is connected, contains
`e`, is full to `B`, and is adjacent to `Q_1` through `pq`.  The explicit
edges at `e` give the second old boundary triangle.

After deleting `uw,qw`, the scripted assignment is proper.  The
`{0,4}`-component through `u` meets `B` exactly in `{y_d}`; the
`{0,1}`-component through `q` meets `B` exactly in `{d}`.  They are disjoint,
and the only edge with a colour-four endpoint in the first and a colour-one
endpoint in the second is `y_dd`.  Switching the first component gives a
proper colouring after restoring `uw`; switching the second does the same
after restoring `qw`.  Their boundary partitions are exactly the two
displayed partitions.

## 4. Verifier coverage

The verifier deterministically checks:

- properness of the central colouring with exactly the two selected edges
  deleted;
- connectedness and adjacency of the three constructed open-side pieces;
- every asserted `S`- and `B`-contact and the unique missed vertex `r`;
- the exact two bichromatic components, their disjointness, and their unique
  joining edge;
- properness after each one-component switch and edge restoration;
- both exact boundary equality partitions and their inequality;
- the singleton triangle, both required sets, and the complete two-by-two
  incidence matrix.

The code uses plain finite sets and breadth-first search and has no random,
network, or external-library dependency.  The statements about the second
partition's demand, minimum boundary order, and the two components of the
open graph are also immediate from the explicit construction and were
checked independently from the verifier assertions.

## 5. Trust boundary

The shell is intentionally low-connectivity and is not asserted to be
seven-chromatic, contraction-critical, or `K_7`-minor-free.  It does not
refute any theorem using those host hypotheses, any theorem converting the
failure into a separator, or any theorem using additional label-preserving
geometry.  It refutes only the algebraic inference that the common
two-edge-deletion colouring, its two component switches, a singleton joining
edge, and an exact demand-two Hall certificate must themselves synchronize
the two boundary partitions or repair the Hall obstruction.

Within that scope, the normal-form lemma, finite shell, calculations, and
verifier are correct.  No mathematical or computational error was found.
