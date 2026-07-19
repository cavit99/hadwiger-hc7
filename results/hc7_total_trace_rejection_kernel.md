# Total rejection of a fixed boundary trace at an internal edge

**Status:** written proof; separate internal audit GREEN in
[`hc7_total_trace_rejection_kernel_audit.md`](hc7_total_trace_rejection_kernel_audit.md).

This note records what follows when an internal critical edge of the full
shore in an asymmetric order-eight interface admits no six-colouring with a
previously fixed boundary trace.  Total rejection has an exact list-colouring
formulation.  It produces a second spanning list-critical graph in which the
ends of the deleted edge have positive degree excess, and it gives a precise
alternative along a shortest boundary Kempe sequence: either one boundary
move is obstructed simultaneously in the two shores, or an intermediate
trace produces list-critical subgraphs in both shores.

The latter subgraphs yield a strict transfer when one is proper.  The
transfer, however, uses a fresh proper-minor colouring and need not preserve
the intermediate trace, the selected edge, or any inherited minor-model
labels.  Thus the results below are a rejection-kernel reduction, not a
state-preserving induction.  Nothing here proves `HC_7`.

## 1. Setting and extension languages

Let `G` satisfy

\[
 \chi(G)=7,\qquad \kappa(G)\ge 7,\qquad K_7\npreccurlyeq G,
 \qquad\text{and every proper minor of }G\text{ is six-colourable}.
                                                               \tag{1.1}
\]

Suppose

\[
                 V(G)=A\mathbin{\dot\cup}X\mathbin{\dot\cup}D, \tag{1.2}
\]

where `A,D` are nonempty and connected, `|X|=8`, and, for some `p in X`,

\[
                         N_G(A)=X-\{p\},
 \qquad                   N_G(D)=X.                              \tag{1.3}
\]

In particular there is no edge between `A` and `D`.  Let `c` be a proper
six-colouring of `G[A union X]` whose restriction to `X` does not extend to
`G[D union X]`.  For `w in D`, define

\[
                 L_c(w)=[6]-c(N_G(w)\cap X),                     \tag{1.4}
\]

where the right-hand side removes the set of colours occurring on the
literal boundary neighbours of `w`.

Assume throughout Sections 2 and 3 that `G[D]` is vertex-minimal subject to
not being `L_c`-colourable.  This is the shore-filling endpoint of the
boundary list-critical reduction.

Let `f=uv` be an edge of `G[D]`.  Write `E_A` and `E_D` for the sets of
proper six-colourings of `G[X]` which extend to `G[A union X]` and
`G[D union X]`, respectively.  Let

\[
 R_f=\{d|X:d\text{ is a proper six-colouring of }G-f\}.          \tag{1.5}
\]

The sets `E_A,E_D,R_f` are nonempty.  Moreover,

\[
                         E_A\cap E_D=\varnothing,
 \qquad                   R_f\subseteq E_A-E_D.                   \tag{1.6}
\]

Indeed, a common extension trace would glue to a six-colouring of `G`.
Every colouring of `G-f` restricts to a colouring of the unchanged closed
shore `G[A union X]`; if its trace also extended through the original
`D`-shore, the same gluing contradiction would result.

We say that `f` **totally rejects the fixed trace** `c|X` when no proper
six-colouring of `G-f` agrees with `c` on `X`.

## 2. Exact list-colouring criterion

### Theorem 2.1 (fixed-trace deletion criterion)

There is a proper six-colouring of `G-f` which agrees with `c` on `X` if
and only if `G[D]-f` is `L_c`-colourable.

#### Proof

Suppose first that `d` is a six-colouring of `G-f` with `d|X=c|X`.
For every `w in D`, the colour `d(w)` differs from the colour of every
boundary neighbour of `w`.  Hence `d(w) in L_c(w)`, and `d|D` is an
`L_c`-colouring of `G[D]-f`.

Conversely, let `phi` be an `L_c`-colouring of `G[D]-f`.  The definition of
the lists makes `phi union c` proper on every edge between `D` and `X`.
There are no edges between `A` and `D`, so gluing `phi` to `c` gives a
proper six-colouring of `G-f` agreeing with `c` on `X`. \(\square\)

Thus total rejection is exactly the assertion

\[
                         G[D]-f\text{ is not }L_c\text{-colourable}.
                                                               \tag{2.1}
\]

It is stronger than the original failure of `c|X` on `G[D union X]`, but
it is still a statement about one fixed trace rather than all traces in
`E_A`.

### Theorem 2.2 (alternate spanning critical graph)

Assume that `f` totally rejects `c|X`.  Then `G[D]-f` is vertex-minimal
subject to not being `L_c`-colourable.  It contains a connected spanning
subgraph `F_f`, minimal by edge inclusion subject to not being
`L_c`-colourable, with the following properties.

1. Every proper subgraph of `F_f` is `L_c`-colourable.
2. For every `w in D`,

   \[
                              d_{F_f}(w)\ge |L_c(w)|.              \tag{2.2}
   \]

3. The ends of the rejected edge have positive degree excess in the
   original shore:

   \[
       d_{G[D]}(u)\ge |L_c(u)|+1,
       \qquad
       d_{G[D]}(v)\ge |L_c(v)|+1.                                \tag{2.3}
   \]

   In particular neither endpoint is tight in `G[D]` for the lists `L_c`.
4. The subgraph of `F_f` induced by

   \[
                         \{w:d_{F_f}(w)=|L_c(w)|\}                 \tag{2.4}
   \]

   is a Gallai forest: each of its blocks is complete or an odd cycle.

#### Proof

Every proper induced subgraph of `G[D]` is `L_c`-colourable by the
shore-filling minimality assumption.  Deleting `f` cannot destroy such a
colouring, so every proper induced subgraph of `G[D]-f` is
`L_c`-colourable.  Equation (2.1) therefore makes `G[D]-f` vertex-minimal
non-`L_c`-colourable.

Delete edges from `G[D]-f` while non-`L_c`-colourability is retained.  The
result is the spanning edge-minimal graph `F_f`.  A subgraph with fewer
vertices is contained in a proper induced subgraph of `G[D]-f`, and a
proper spanning subgraph is contained in an edge deletion of `F_f`.
This proves assertion 1.  It also shows that `F_f` is connected: otherwise
one of its components would already be a non-`L_c`-colourable proper
subgraph.

Colour `F_f-w` from its lists.  If `d_{F_f}(w)<|L_c(w)|`, a colour absent
from the coloured neighbours of `w` extends the colouring to all of
`F_f`, a contradiction.  This proves (2.2).  Since `f=uv` is absent from
`F_f`,

\[
 d_{G[D]}(u)=d_{G[D]-f}(u)+1\ge d_{F_f}(u)+1\ge |L_c(u)|+1,
\]

and the same argument applies to `v`, proving (2.3).

For assertion 4, colour the complement of a block `B` of the tight-vertex
subgraph and delete from each list the colours already used on neighbours
outside `B`.  A vertex `w in B` retains at least `d_B(w)` colours.  The
degree-choosability theorem would then colour `B` unless `B` were complete
or an odd cycle; such a colouring would extend to `F_f`, contrary to its
choice. \(\square\)

The graph `F_f` is an alternate spanning obstruction, not a smaller one.
Different choices of `f` may replace one spanning edge-minimal obstruction
by another on the same vertex set.  Theorem 2.2 therefore supplies no
well-founded edge-rotation or edge-deletion induction.

## 3. The first boundary transition

Let `Gamma_6(X)` be the graph whose vertices are the proper six-colourings
of `G[X]`, with two colourings adjacent when one is obtained from the other
by interchanging two colours on one full two-colour component of `G[X]`.
Because `|X|=8` and `G[X]` has no `K_7` minor, all its proper
six-colourings belong to one Kempe class.  Thus `Gamma_6(X)` is connected.

Choose a shortest path

\[
                    r_0,r_1,\ldots,r_k                              \tag{3.1}
\]

in `Gamma_6(X)` from `R_f` to `E_D`; that is, `r_0 in R_f`, `r_k in E_D`,
and `k` is minimum.  By (1.6), `k>=1`, no internal `r_h` belongs to `E_D`,
and `r_0 in E_A`.  Put

\[
                    i=\max\{h<k:r_h\in E_A\}.                      \tag{3.2}
\]

Then every trace strictly between `r_i` and `r_k` belongs to neither
extension language.

### Theorem 3.1 (single transition or paired rejection kernels)

Exactly one of the following two alternatives occurs for the path (3.1).

1. **Consecutive transition.** `i=k-1`.  If the last move interchanges
   colours `alpha,beta` on a boundary two-colour component `W`, then there
   is an `alpha`--`beta` path with nonempty interior in `A` from `W` to a
   different boundary two-colour component, and there is such a path with
   nonempty interior in `D` for the reverse move.  The two interiors are
   disjoint.
2. **Paired rejection.** `i<=k-2`.  Every trace `r_h` with `i<h<k` is
   rejected by both shores.  For each such `h` and each `Z in {A,D}`, put

   \[
                 L_h^Z(w)=[6]-r_h(N_G(w)\cap X),\qquad w\in Z.     \tag{3.3}
   \]

   Then `G[Z]` has a connected induced subgraph `K_h^Z`, vertex-minimal
   subject to not being `L_h^Z`-colourable.  Every `w in V(K_h^Z)` obeys

   \[
                           d_{K_h^Z}(w)\ge |L_h^Z(w)|,              \tag{3.4}
   \]

   and the tight-vertex subgraph of `K_h^Z` is a Gallai forest.

#### Proof

The assertion preceding the theorem proves that every intermediate trace
after `r_i` lies outside `E_A union E_D`.  This gives the first sentence of
alternative 2.  A boundary trace extends through `Z` exactly when `G[Z]`
is colourable from the lists (3.3).  Hence each shore is not list-colourable
for each displayed intermediate trace.  Choosing a vertex-minimal induced
obstruction gives `K_h^Z`; connectivity, (3.4), and the Gallai-forest
conclusion follow by the same elementary list-critical argument as in
Theorem 2.2.

It remains to prove alternative 1.  Choose an extension of `r_i` to
`G[A union X]` and an extension of `r_k` to `G[D union X]`.  In the first
closed shore, let `C_A` be the full `alpha`--`beta` component containing
`W`.  If `C_A cap X=W`, interchange the two colours on `C_A`.  The resulting
closed-shore colouring has trace `r_k` and glues to the selected extension
through `D`, six-colouring `G`, a contradiction.  Thus `C_A` meets another
boundary two-colour component.  A shortest first-hit path has nonempty
interior entirely in `A`.

Apply the same argument in reverse to the full two-colour component in the
selected `D`-shore extension of `r_k`.  If it met `X` only in `W`, the
reverse interchange would produce `r_i` and glue to the selected
`A`-extension.  It therefore yields the required path with interior in
`D`.  The two interiors are disjoint because `A` and `D` are disjoint.
The two alternatives are mutually exclusive by their conditions on `i`.
\(\square\)

The correction in (3.2) is essential.  A shortest path from `R_f` to
`E_D` need not have every internal trace outside `E_A`.  One must take the
last trace on the path which still extends through `A`.  Only the suffix
after that trace has the dichotomy asserted above.

## 4. What a proper paired kernel transfers

### Theorem 4.1 (strict transfer without trace preservation)

Assume alternative 2 of Theorem 3.1.  Fix `h` with `i<h<k` and
`Z in {A,D}`.  If `K_h^Z` is a proper induced subgraph of `G[Z]`
(equivalently, `V(K_h^Z)` is a proper subset of `Z`), let
`R_1,...,R_m` be the components of `G[Z-V(K_h^Z)]`.  Then:

1. `|N_G(R_j)|>=7` for every `j`.
2. For a six-colouring `t` of the proper minor
   `G-(Z-V(K_h^Z))`, at least one component `R_j` rejects the trace
   `t|N_G(R_j)`.
3. Such an `R_j` is connected and satisfies `|R_j|<|Z|`.  If
   `|N_G(R_j)|=7`, its full neighbourhood is an actual order-seven
   separator, and every component behind that separator is adjacent to
   all seven of its literal vertices.

#### Proof

Every component `R_j` has all its neighbours in
`X union V(K_h^Z)`.  Its full neighbourhood separates it from the other
nonempty shore, so seven-connectivity proves assertion 1.

The deleted set `Z-V(K_h^Z)` is nonempty, so the displayed graph is a
proper minor and has a six-colouring `t`.  If `t` extended through every
component `R_j`, choose one extension for each.  The components are
pairwise anticomplete and all extensions agree with `t` on their full
neighbourhoods, so they glue to a six-colouring of `G`, a contradiction.
This proves assertion 2.

The selected component is disjoint from the nonempty `K_h^Z`, so it is
strictly smaller than `Z`.  If its full neighbourhood `S` has order seven,
then `S` is the boundary of a nontrivial separation.  Any component of
`G-S` which missed a vertex of `S` would have a neighbourhood of order at
most six, contradicting seven-connectivity.  This proves assertion 3.
\(\square\)

The strict inequality in Theorem 4.1 is a host-level decrease, but it does
not preserve the data which created it.  The proper-minor colouring `t`
need not restrict to the intermediate trace `r_h` on `X`; its new boundary
`N_G(R_j)` can have order greater than eight; and it need not preserve
`f`, the two boundary Kempe moves adjacent to the gap, or any labelled
branch sets of a pre-existing minor model.  If both paired kernels fill
their respective shores, Theorem 4.1 gives no decrease at all.

## 5. Exact preservation gap

The preceding theorems leave the following alternatives and no stronger
conclusion.

1. Total rejection of `c|X` at `f` gives an alternate spanning critical
   graph `F_f` and proves that the ends of `f` are non-tight in the
   original shore.  It does not yield a smaller obstruction.
2. The first transition from a response trace towards the opposite
   extension language either gives simultaneous two-shore Kempe paths or
   produces paired list-critical kernels.  The paths are not assigned to
   prescribed minor-model branch sets.
3. A proper paired kernel gives a smaller rejected connected subgraph, but
   only for a fresh proper-minor trace on a new boundary.  This is not a
   recursion in the original boundary transition.
4. A full paired kernel gives synchronized vertex-deletion colourings on
   its own shore, but no palette colour is thereby identified with a named
   branch set.
5. Comparing deletion and contraction of the same edge `f` cannot repair
   the gap: their full six-colouring Kempe graphs are canonically
   isomorphic, because every colouring of `G-f` gives the ends of `f` the
   same colour and identifies with a colouring of `G/f`.

Accordingly, a continuation needs an additional label-preserving theorem.
It must either align the non-tight endpoints in Theorem 2.2 with distinct
named branch sets, retain the intermediate trace through the strict
transfer of Theorem 4.1, or turn one of the resulting order-seven
separators into compatible closed-shore boundary colourings.  None of
these conclusions follows from total fixed-trace rejection alone.

## 6. Dependencies

- [boundary list-criticality and transfer to a complementary
  component](hc7_boundary_list_critical_transfer.md)
- [a single boundary Kempe transition between opposite-shore edge
  responses](hc7_opposite_shore_single_kempe_transition.md)
- [fresh-colour linkages across an exact order-seven
  separation](hc7_exact7_fresh_colour_linkage.md), Lemma 4.1
- M. Las Vergnas and H. Meyniel, *Kempe classes and the Hadwiger
  Conjecture*, J. Combin. Theory Ser. B 31 (1981), 95--104.
- P. Erdős, A. L. Rubin and H. Taylor, *Choosability in graphs*,
  Proceedings of the West Coast Conference on Combinatorics, Graph Theory
  and Computing, Congressus Numerantium 26 (1979), 125--157.
