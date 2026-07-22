# Common-root rejection symmetry forces a synchronized fork

**Status:** written proof; separately audited GREEN.  This theorem does not
prove `HC_7`.

## Theorem 1 (exclusive crossing and antipodal flip-cube fork)

Let `G` be a finite simple graph such that:

1. `G` is seven-connected and `chi(G)=7`;
2. `G` has no `K_7` minor; and
3. every proper minor of `G` is six-colourable.

Let `u` have degree eight or nine, put

\[
                    X=N_G(u),\qquad H=G[X],
\]

and suppose that `G-N[u]` has exactly two components `C,D`, each adjacent
to every vertex of `X`.  For a labelled proper five-colouring `rho` of
`H`, let `R(rho)` be the set of components through which `rho` does not
extend to a proper six-colouring.  Assume that every `R(rho)` is a
singleton.

Suppose that proper five-colourings `phi,psi` agree on `X-{x}`, that

\[
 R(\phi)=\{C\},\qquad R(\psi)=\{D\},
 \qquad \phi(x)=\alpha,\qquad \psi(x)=\beta,          \tag{1.1}
\]

and that changing `x` from `alpha` to `beta` is legal.  Let

\[
                 W_0=\{x\},W_1,\ldots,W_t            \tag{1.2}
\]

be the components of `H[alpha,beta]` in `phi`.  For
`S subseteq I={0,...,t}`, let `phi_S` be obtained from `phi` by
interchanging `alpha,beta` on exactly the components indexed by `S`, and
write `r(S)` for the unique member of `R(phi_S)`.

Then all of the following hold.

1. There is a proper six-colouring `c` of `G-x`, with `c(u)=6`, such that

   \[
   \begin{array}{c|cc}
    &\alpha\text{-neighbour of }x&\beta\text{-neighbour of }x\\ \hline
   C&\text{at least one}&\text{none}\\
   D&\text{none}&\text{at least one}\\
   H-x&\text{none}&\text{none}.
   \end{array}                                          \tag{1.3}
   \]

   In this colouring, one `alpha`--`beta` component crosses from `C` to
   `D`.  A shortest such crossing path, together with `x`, is an induced
   odd cycle whose only neighbours of `x` on the cycle are its two cycle
   neighbours.

2. The rejection map is antipodally invariant:

   \[
                         r(S)=r(I-S)                    \tag{1.4}
   \]

   for every `S`.  Moreover, some cube vertex `S` has rejector-changing
   incident edges in two distinct coordinates `i,j`:

   \[
   r(S)\ne r(S\mathbin\triangle\{i\}),\qquad
   r(S)\ne r(S\mathbin\triangle\{j\}).                \tag{1.5}
   \]

3. Put `theta=phi_S`, let `E=r(S)`, and let `F` be the other exterior
   component.  Fix any extension of `theta` through `F` and consider its
   full `alpha`--`beta` components.  At least one of the following holds.

   a. The boundary components `W_i,W_j` lie in one full two-colour
      component of that single fixed extension.

   b. There are paths `P_i,P_j`, belonging to two distinct full
      two-colour components of that extension, whose open interiors lie
      in `F`.  Their endpoint pairs `f_i,f_j` are distinct nonedges of
      `H` and use disjoint pairs of the boundary components `W_k`.
      For either one of the two coordinates, an extension through `E`
      separately supplies a path `Q` whose open interior lies in `E` and
      whose endpoint pair `e` is a nonedge of `H`.  The three literal
      paths have pairwise disjoint, pairwise anticomplete open interiors.

      If repeated endpoint pairs are included only once and

      \[
                         \mathcal E=\{f_i,f_j,e\},
      \]

      then

      \[
          2\le |\mathcal E|\le3,\qquad
          K_6\not\preccurlyeq H+\mathcal E.            \tag{1.6}
      \]

      If \(|\mathcal E|=3\), this is a three-edge `K_6`-minor-free
      augmentation.  If \(|\mathcal E|=2\), the path `Q` and one of
      `P_i,P_j` have the same boundary endpoint pair but pass through
      different exterior components; the other `F`-path remains as a
      second supported nonedge.

The theorem therefore synchronizes two operated boundary components in one
fixed accepted extension.  It does not assert that the two paths obtained
separately through `E` for the two cube coordinates can be retained in one
colouring.

## 1. Exclusive contacts force an induced crossing cycle

Use the `psi`-extension through `C` and the `phi`-extension through `D`
given by the common-root exchange theorem.  Delete `x`, glue the extensions
on their common colouring of `X-{x}`, and give `u` colour six.  The two
exterior components are exhaustive and anticomplete, so this is a proper
six-colouring `c` of `G-x`.

In the extension through `C`, the boundary vertex `x` had colour `beta`.
Hence `x` has no `beta`-coloured neighbour in `C`; reverse failed lifting
supplies an `alpha`-coloured neighbour there.  Symmetrically, the extension
through `D` has no `alpha`-coloured neighbour of `x`, while forward failed
lifting supplies a `beta`-coloured neighbour.  The recolouring at `x` was
legal in both directions, so neither exchanged colour occurs on
`N_H(x)`.  Finally, `u` has colour six.  This proves (1.3).

Put

\[
 A=N_G(x)\cap C\cap c^{-1}(\alpha),\qquad
 B=N_G(x)\cap D\cap c^{-1}(\beta).                    \tag{2.1}
\]

Both sets are nonempty.  If no component of
`(G-x)[alpha,beta]` met both, interchange `alpha,beta` on the union of
all components meeting `A`.  Every `alpha`-coloured neighbour of `x`
would change to `beta`.  By (1.3), every `beta`-coloured neighbour of `x`
lies in `B`, and none of its components would be switched.  Colour
`alpha` would then be absent from `N_G(x)`, so assigning it to `x` would
six-colour `G`, a contradiction.

Choose a shortest `A`--`B` path `P` in a crossing component.  Every
neighbour of `x` on an `alpha`--`beta` path belongs to `A union B`, by
(1.3).  An internal occurrence of either set would shorten `P`.  Thus
the interior of `P` avoids all of `N_G(x)`.  The path is induced, its ends
have different colours, and hence its length is odd.  Adding the two edges
from its ends to `x` gives the asserted induced odd cycle.

## 2. Antipodal symmetry forces two changing coordinates

Let `sigma` interchange the colour names `alpha,beta` and fix the other
three names.  Palette renaming does not change extension through a fixed
exterior component.  Relative to `phi`, applying `sigma` after switching
the components in `S` switches exactly the complementary components:

\[
                         \sigma\phi_S=\phi_{I-S}.
\]

This proves (1.4).

The edge from `emptyset` to `{0}` is a rejection-cut edge by (1.1).  If
the cube had dimension one, its endpoints would be antipodal, contrary to
(1.4).  Thus `t>=1`.

Suppose every cube vertex were incident with at most one rejection-cut
edge.  Choose such an edge in coordinate `i`.  In any square containing
that edge and another coordinate `j`, the number of cut edges is even.
The two adjacent `j`-edges cannot be cut under the degree-one supposition,
so the opposite `i`-edge is cut.  Propagating through all other coordinates
shows that every edge in coordinate `i` is cut.  Every vertex is now
incident with its `i`-edge, so no edge in another coordinate is cut.  The
map `r` consequently depends only on the `i`-th coordinate.  Complementing
all coordinates changes that coordinate and would change `r`, contradicting
(1.4).  Some vertex has two changing incident coordinates, which proves
(1.5).

## 3. One accepted extension contains the fork

At the two ends of either cut edge in (1.5), the unique rejecting component
changes from `E` to `F`.  Hence `theta` extends through `F`, while switching
`W_k`, for `k=i` or `j`, does not.

Fix a `theta`-extension through `F`.  The full two-colour component meeting
`W_k` must meet some other component of `H[alpha,beta]`; otherwise switching
that one full component would extend the switched boundary colouring through
`F`.  This applies to both `W_i` and `W_j` in the same fixed extension.  If
their full components coincide, outcome 3(a) follows.

Otherwise, in each of the two full components choose a shortest path from
the operated boundary component to a different boundary component.  Its
only boundary vertices are its ends, so its open interior lies in `F`.
The two full components are disjoint.  They are also anticomplete: an edge
between them would either violate properness or join the two full
`alpha`--`beta` components.  Thus the paths `P_i,P_j` have disjoint,
anticomplete open interiors and disjoint boundary-component endpoint pairs.
Each endpoint pair is a nonedge of `H`, since an edge would join the two
corresponding components of `H[alpha,beta]`.

For one chosen `k in {i,j}`, the switched boundary colouring extends
through `E`, whereas `theta` does not.  Applying the same argument in
reverse to one such extension gives a shortest path `Q` between `W_k` and
another boundary two-colour component, with open interior in `E`.  There
are no edges between `C` and `D`, so the open interior of `Q` is disjoint
from and anticomplete to the open interiors of `P_i,P_j`.  This proves all
of the literal path assertions.

The paths can be contracted compatibly while their boundary endpoints are
retained: shared boundary endpoints are common vertices of the resulting
boundary graph, not intersections of the open interiors.  If two paths have
the same endpoint pair, the repeated added edge is retained only once.
Consequently \(H+\mathcal E\) is a minor of `G-u`.

If this augmented boundary had a `K_6` model, every one of its six branch
sets would contain a vertex of `X`.  Lifting through the displayed path
contractions and adding the singleton branch set `{u}` would give an
explicit `K_7`-minor model in `G`, a contradiction.  This proves (1.6).
Since `f_i,f_j` have disjoint boundary-component endpoint pairs, they are
distinct.  The edge `e` either differs from both, or duplicates exactly one
of them, giving the final stated alternatives.

## Exact trust boundary

The crossing odd cycle and the flip-cube fork are host-level consequences
of the exact two-full-component common-root residue.  The fork is stronger
than a collection of unrelated recolourings: both operated components are
blocked in one fixed extension through `F`.

The theorem is not terminal.  The two separately obtained `E`-side paths
may overlap arbitrarily, and even three distinct supported boundary
nonedges need not force a `K_6` minor after the paths are contracted.  Any
completion must use further literal geometry inside the exterior components,
a common boundary partition, or a strict response-preserving component
descent.

## Input

- [full exterior components force a common-root exchange](hc7_full_exterior_component_common_root_exchange.md)
