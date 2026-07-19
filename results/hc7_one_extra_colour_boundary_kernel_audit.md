# Independent audit: one-extra-colour critical kernel

**Verdict: GREEN for the theorem as stated.**

**Audit status:** separate internal mathematical audit; this is not external
peer review.

**Audited source:** `results/hc7_one_extra_colour_boundary_kernel.md`

**Audited SHA-256:**
`6317f20d0307b00ceec9ad1290f08e81e211f2dd34a85b975400381bb08c5c07`

This audit applies only to that exact revision.  The source must be
re-audited if its mathematical content changes.

## 1. Verdict and correction history

The abstract list-critical argument, the boundary construction, the degree
identity, and the exact order-seven consequence are correct under the stated
hypotheses.

An earlier revision overstated the Cranston--Rabern classification by
suggesting that every one-root obstruction had a distinguished block in
their family `mathcal D`.  The audited revision fixes this: it invokes all
five cases of their Theorem 3.6, assigns `mathcal D` only to cases (4) and
(5)(iii), and retains the degree-two case (3) as a separate possibility.
That corrected formulation agrees with the primary source.

## 2. External inputs checked

### 2.1 Degree choosability

The proof uses the Borodin--Erdos--Rubin--Taylor characterization in the
standard contrapositive form: a connected graph which is not colourable from
some list assignment of order equal to the vertex degrees is a Gallai tree.
The hypotheses established in Theorem 1.1 are exactly those required for
this use.

### 2.2 Cranston--Rabern

The citation was checked against Daniel W. Cranston and Landon Rabern,
*Beyond Degree Choosability*, Electronic Journal of Combinatorics **24**
(2017), #P3.29, <https://doi.org/10.37236/6179>.

- Their Theorem 4.1 states, for connected `G`, that `(G,h_x)` is not
  choosable exactly when it is not Alon--Tarsi, and that the same structural
  characterization governs paintability.
- Their Theorem 3.6 gives the five structural cases for a connected pair
  `(G,h_x)` which is not Alon--Tarsi.  The degree-two/Gallai-tree-component
  case is case (3).  A distinguished block in the stretched family
  `mathcal D` occurs in cases (4) and (5)(iii), not in every case.

The audited source uses only this exact equivalence and classification.  It
does not import a stronger assertion about all exceptional blocks.

## 3. Audit of Theorem 1.1

### Connectedness and nonnegative excess

If `H` were disconnected, noncolourability of `H` would imply that one
component is noncolourable from the restricted lists.  That component is a
proper induced subgraph, contradicting vertex-minimality.  Thus `H` is
connected.

For each vertex `u`, an `L`-colouring of `H-u` exists.  If
`d_H(u)<|L(u)|`, at most `d_H(u)` colours are forbidden at `u`, so the
colouring extends.  Therefore `d_H(u)>=|L(u)|` and every displayed excess is
nonnegative.

### Use of the extra colour

Only the list at `w` is enlarged.  If an `L^+`-colouring gave `w` a colour
from `L(w)`, it would be an `L`-colouring of `H`.  Hence every
`L^+`-colouring gives `w` the new colour `theta`.

### Exhaustiveness and exclusivity

- If all excesses vanish, the degree-choosability theorem gives alternative
  1.
- If the excess profile is one at `w` and zero elsewhere, the given list
  assignment is exactly a witness that `(H,h_w)` is not choosable; the
  corrected Cranston--Rabern conclusion gives alternative 2.
- In every remaining profile, either a vertex other than `w` has positive
  excess or `w` has excess at least two.  If `w` has excess zero and
  alternative 1 fails, some other vertex has positive excess.  Thus the set
  `P` in (1.4) is nonempty.

The three alternatives have disjoint excess profiles, so the word
"exactly" is justified.

### Saturation at `w`

Every proper induced subgraph, in particular `H-w`, is `L`-colourable.  If
one colour of `L(w)` were absent from the coloured neighbourhood, assigning
it to `w` would extend the colouring to `H`.  Hence all colours in `L(w)`
occur on `N_H(w)`.

## 4. Audit of the boundary construction

The definition `S=N_G(W)` implies that no vertex of `W` is adjacent to the
far side `G-(W union S)`.  If `G[W]` were colourable from the lists in
(2.3), that colouring would glue to `c` on `G-W`: the lists exclude all
colours appearing at boundary neighbours, and the deleted edge has its
`W`-endpoint outside `G-W`.  This would six-colour `G`, a contradiction.

A vertex-minimal induced noncolourable subgraph `K` is connected by the
same component argument as above.  For `u ne w`, every edge from `u` to
`S` remains in `G-sw`, so `c(u)` is absent from the colours on its boundary
neighbours and lies in `L(u)`.  At `w`, properness of `c` on `G-sw` implies
that `s` is the only boundary neighbour of colour `theta`: every other edge
from `w` to `S` remains present.  Thus `c(w)=theta` lies in `L^+(w)`.

If `w` were outside `K`, the restriction of `c` would colour `K` from `L`.
Therefore `w` belongs to `K`, the restriction is an `L^+`-colouring, and
Theorem 1.1 applies exactly as claimed.

## 5. Audit of the degree identity

Because `K` is induced in `G[W]`, the neighbours of `u in K` split into:

1. neighbours in `K`;
2. neighbours in `W-V(K)`, counted by `sigma(u)`; and
3. neighbours in `S`.

There are no further neighbours.  Since `|L(u)|=6-q(u)` and
`d_K(u)=|L(u)|+epsilon(u)`, direct substitution gives

\[
d_G(u)=6+\varepsilon(u)+\rho(u)+\sigma(u).
\]

No inequality or unrecorded disjointness assumption is used here.

## 6. Audit of the exact-seven consequence

When the boundary partition has one repeated pair `{a,b}` and five
singleton classes, any subset of the boundary loses at most one when its
number of vertices is replaced by its number of colours.  It loses one
exactly when it contains both `a` and `b`.  This proves (4.1).

The shore-filling hypothesis gives `sigma=0`.  If `epsilon(u)=0`, the degree
identity and (4.1) give `d_G(u)<=7`; seven-connectivity gives
`d_G(u)>=7`.  Hence `d_G(u)=7` and `rho(u)=1`.

The full neighbourhood `N_G(u)` is then an actual vertex separator of order
seven.  After its deletion, `u` is isolated, while the assumed nonempty far
side remains and is anticomplete to `u`.  Thus the deletion has at least two
nonempty components.

Alternative 1 contains tight vertices.  In alternative 2,
`d_K(w)=|L(w)|+1>=1`, so connectedness supplies a neighbour `u ne w`, and
every such vertex is tight by the stated excess profile.  Both alternatives
therefore expose the asserted separator.

If no such separator is admitted, no vertex of `W` can have degree seven:
the same full-neighbourhood argument would expose one.  Thus every vertex
has degree at least eight.  Substitution into the exact identity gives
`epsilon(u)+rho(u)>=2`; combining this with (4.1) yields precisely (4.3).

## 7. Trust boundary

The proof establishes only the stated list-critical trichotomy, exact degree
identity, and order-seven-separator/positive-excess alternative.  In
particular, it does **not** establish any of the following:

- an explicit `K_7`-minor model;
- a common boundary equality partition for colourings of both closed sides
  of the returned separation;
- an identification of the five available colours or bichromatic
  components with five prescribed branch-set labels;
- that the positive-excess branch is impossible; or
- that the critical kernel fills the shore outside the explicit hypothesis
  `K=G[W]` used in Theorem 4.1.

These are genuine remaining composition obligations, not consequences of
the audited theorem.
