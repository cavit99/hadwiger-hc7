# Independent audit: reserved cycle or a separator of order at most two

## Verdict and audited revision

**GREEN.**  The theorem is correct at the stated scope.  Fournier's theorem
is applied to the full five-set `C` in the literal graph `K`; the alternative
separator lifts to an actual order-seven full-neighbourhood separation with
the asserted count.  The colouring paragraph supplies only a one-sided
boundary partition and correctly leaves synchronization open.

This audit checks
`results/hc7_reserved_cycle_or_two_cut.md` at SHA-256

```text
8f9cd1d6a76c868a200b3d5504584980d054bf8bb43d880fcbf360a9f3938495
```

No finite computation is used in this theorem.

## 1. Literal setup and the reserved component

The five-set `C=N_H(v)` and the three-set `B` partition the degree-eight
neighbourhood of `v`.  Since `D` is a component of `G-N_G[v]`, every external
neighbour of `D` lies in `N_G(v)=B dotcup C`; in particular, `D` is disjoint
from the residue

\[
                    K=G-(D\cup B\cup\{v\}).
\]

All five vertices of `C` survive in `K`.  In the contraction-critical
application, Dirac's neighbourhood-independence inequality at a degree-eight
vertex of a seven-contraction-critical graph gives

\[
                         \alpha(G[C])\le3.
\]

Only this inherited inequality on the induced five-set is used.

## 2. Fournier's cyclability theorem

The exact accessible statement is Theorem 7 of R. J. Gould, *A look at
cycles containing specified elements of a graph*, Discrete Mathematics 309
(2009), 6299--6311: if a graph `F` is two-connected and `Y subseteq V(F)`
satisfies

\[
                         \alpha(F[Y])\le\kappa(F),
\]

then one cycle of `F` contains every vertex of `Y`.  Gould attributes this
result to I. Fournier's 1985 thesis.  The same statement is recorded as
Theorem D by A. Saito and T. Yamashita, *Cycles within specified distance
from each vertex*, Discrete Mathematics 278 (2004), 219--226.

If `K` is `k`-connected for some `k>=2` and
`alpha(G[C])<=k`, then `alpha(K[C])=alpha(G[C])<=k<=kappa(K)`, so all
hypotheses hold with `F=K` and `Y=C`.  In particular they hold when `K` is
three-connected, because the setup supplies `alpha(G[C])<=3`.

On the resulting cycle, removing one edge from each arc between consecutive
members of `C` leaves five nonempty, pairwise disjoint paths.  Each path
contains exactly one nominated member of `C`, and the five removed edges give
the asserted cyclic adjacencies.  This construction does not prescribe the
cyclic order of `C`, nor does the theorem claim that it does.

## 3. The seven-contact count

The cycle and its five connected sectors lie in `K`, hence avoid `D`, `B`,
and `v`.  The external neighbourhood of `D` is contained in the eight-set
`B dotcup C`.  It separates `D` from the surviving vertex `v`, so
seven-connectivity gives

\[
                    7\le |N_G(D)|\le |B\cup C|=8.
\]

Each member of `B` is its own label and each member of `C` lies in a
different cycle sector.  Thus the map from boundary neighbours of `D` to the
eight labels is injective, and `D` is adjacent to at least seven labels.  No
edge between `D` and a cycle sector is inferred from collective fullness
alone: it is supplied by the corresponding literal neighbour in `C`.

## 4. Lifting a separator of `K`

Let `Z` be a separator of `K`, let `z=|Z|<=2`, and let `A` be a component of
`K-Z`.  Put `C_A=A cap C`, and let `X` be a component of `G[A-C_A]`.
Every vertex of `X` lies outside `N_G[v]`, since `K` already excludes `B`
and `v`, while all remaining neighbours of `v` are exactly `C` and have
been removed from `A`.

The component `X` has no edge to `D`: both lie in `G-N_G[v]`, and `D` is a
different component because it was deleted when `K` was formed.  Nor can
`X` meet another component of `K-Z`.  There is no edge from `X` to `v`.
Consequently

\[
                       N_G(X)\subseteq Z\cup B\cup C_A.
\]

The three sets on the right are disjoint.  If `|C_A|<=4-z`, their union has
order at most seven.  It is an actual cut because `X` is nonempty and `D`
survives on the opposite side.  Seven-connectivity therefore forces equality
in both bounds:

\[
             |C_A|=4-z,
             \qquad N_G(X)=Z\mathbin{\dot\cup}B
                                  \mathbin{\dot\cup}C_A,
             \qquad |N_G(X)|=7.
\]

Taking the two closed sides determined by this full neighbourhood gives an
actual order-seven separation with both open shores nonempty.

The contrapositive is exact: if no such separation is returned, every
component of `K-Z` containing a vertex outside `C` contains at least `5-z`
members of `C`.  Two such components would contain at least
`2(5-z)>5` distinct members of the five-set `C`, so at most one exists.

If the reserved cycle does not exist, then either `K` is disconnected, has
a cutvertex, or is two-connected with `alpha(G[C])=3`; these alternatives
provide a separator `Z` of order zero, one, or two, respectively.  A complete
`K` cannot be an exception in the last case because its induced set `C`
would have independence number one.

## 5. Proper-minor colouring at the returned boundary

When `|X|>=2`, contracting a spanning tree of `X` performs at least one edge
contraction and hence gives a proper minor.  Its image vertex is adjacent to
all seven members of `N_G(X)`.  In a six-colouring of that minor, the image
colour is therefore absent from the boundary.  Removing the image vertex
leaves a colouring of `G-X` whose equality classes partition the boundary
into at most five independent sets.  This is exactly the asserted one-sided
partition; no colouring of the `X`-side is inferred.

If `X` is a singleton `x`, then `d_G(x)=7`.  Under the expressly stated
minor-minimal counterexample hypotheses, Dirac's inequality gives
`alpha(N_G(x))<=2`.  Every six-colouring of `G-x` uses all six colours on
the seven neighbours, since otherwise it extends to `x`.  Hence its boundary
partition consists of one independent pair and five singleton blocks.  The
source correctly confines this observation to the intended
`chi(G)=7`, proper-minor-six-colourable application.

## 6. Dependencies and trust boundary

The contact-allocation conclusion in Section 3 uses the adjacent audited
degree-eight connected-set allocation theorem.  The proof of Theorem 2.1
itself does **not** use the exact-seven packet-packing theorem.  In
particular, it does not claim that the order-seven separation is colour
gluable merely because one side supplies a partition.

The result does not prove any of the following:

- the matching condition for the three boundary vertices and five sectors;
- a split of the concentrated low-cut residue;
- extension of the returned partition through both closed shores;
- a common equality partition; or
- `HC_7`.
