# Internal audit of the total-trace rejection-kernel theorem

**Verdict:** GREEN for Theorems 2.1, 2.2, 3.1, and 4.1, under the
explicit hypotheses in Section 1 of the source and with the non-preservation
limitations stated in Sections 4 and 5 of the source.

**Audited source:** `hc7_total_trace_rejection_kernel.md`, SHA-256

```text
1bb4fff7f050cf4349ee46d612949c8ddfc07d51d69f65f2406fc7fa6ff6b258
```

After the GREEN audit, only the source status line was changed to link this
audit.  The mathematical statement and proof are unchanged; this audit is
repinned to the resulting source hash above.

This is a separate internal mathematical audit, not external peer review.
The audit reconstructed each list-colouring and gluing argument from the
stated hypotheses and independently checked the small-boundary Kempe-class
premise used in Section 3.

## 1. Setting and extension languages

The separation data are used consistently.  The equalities

```text
N_G(A)=X-{p},    N_G(D)=X
```

imply that `A` and `D` are anticomplete.  Hence two closed-shore colourings
with the same labelled trace on `X` glue without any further compatibility
condition.

The three trace sets introduced in (1.5) are nonempty for the asserted
reasons:

- the fixed colouring `c` supplies a member of `E_A`;
- deleting the nonempty shore `A` gives a proper minor and supplies a member
  of `E_D`; and
- deleting the edge `f` gives a proper minor and supplies a member of `R_f`.

The two inclusions in (1.6) are exact.  A trace in `E_A cap E_D` would glue to
a six-colouring of `G`.  A colouring of `G-f` is unchanged on `A union X`, so
its trace belongs to `E_A`; if that trace also belonged to `E_D`, the two
closed-shore restrictions would again glue to a six-colouring of `G`.

## 2. Fixed-trace deletion and the alternate critical graph

### Theorem 2.1

The fixed-trace criterion is a direct equivalence.  If a colouring of `G-f`
agrees with `c` on `X`, its restriction to `D` avoids precisely the boundary
colours deleted in the definition of `L_c`.  Conversely an
`L_c`-colouring of `G[D]-f` is proper across every `D`--`X` edge, and it glues
to `c` because there are no `A`--`D` edges.  No palette permutation or
unlabelled partition is being substituted for the required labelled trace.

### Theorem 2.2

The vertex-minimality assertion is valid.  Every proper induced subgraph of
`G[D]-f` is contained in the corresponding proper induced subgraph of
`G[D]`, which is `L_c`-colourable by the shore-filling hypothesis; deleting
`f` cannot invalidate that colouring.  Total rejection and Theorem 2.1 then
make `G[D]-f` vertex-minimal non-`L_c`-colourable.

Deleting edges while preserving non-colourability yields a spanning
edge-minimal graph `F_f`.  Every proper subgraph of `F_f` is colourable:
a proper vertex subgraph lies in a proper induced subgraph of `G[D]-f`, and
a proper spanning subgraph lies in an edge deletion of `F_f`.  This also
proves that `F_f` is connected, since otherwise an uncolourable component
would be a proper subgraph.

The degree conclusions are correct.  Colouring `F_f-w` and extending
greedily proves

```text
d_F_f(w) >= |L_c(w)|.
```

Because `uv=f` is absent from `F_f`, each endpoint has one additional edge
in `G[D]`, which proves both inequalities in (2.3).  The conclusion is only
positive degree excess relative to these fixed lists; it does not identify
the extra incidences with prescribed boundary vertices or minor-model branch
sets.

The Gallai-forest conclusion is also valid.  For a block `B` of the subgraph
induced by tight vertices, colour `F_f-V(B)` (or take the empty colouring
when `B=F_f`).  A vertex `w` of `B` loses at most
`d_F_f(w)-d_B(w)` colours to already coloured neighbours, and therefore
retains at least `d_B(w)` colours.  The degree-choosability theorem colours
`B` unless it is a complete graph or an odd cycle.  Such a colouring would
extend to `F_f`, giving the required contradiction.

## 3. Kempe connectivity of the eight-vertex boundary

The premise at lines 184--188 is correct, but it requires both branches of
the small-boundary argument; it is not an immediate consequence of
`K_7`-minor exclusion alone.

Let `R=G[X]`.  If `R` is five-degenerate, Proposition 2.1 of Las
Vergnas--Meyniel applies: all labelled six-colourings of a
five-degenerate graph are six-Kempe equivalent.  Colourings need not use all
six palette colours.

If `R` is not five-degenerate, it contains a subgraph of minimum degree at
least six.  Such a subgraph cannot have seven vertices, because it would be
`K_7`.  It therefore has all eight vertices.  Its complementary graph has
maximum degree at most one, and hence

```text
R = K_8-M
```

for a matching `M` (possibly after restoring some edges of the minimum-degree
subgraph).  If `|M|<=1`, `R` contains a `K_7`; if `|M|=2`, contracting an
edge joining endpoints from the two missing pairs produces a `K_7` minor.
Thus `K_7`-minor exclusion forces `|M|>=3`.

Now view `K_8-M` as a complete multipartite graph whose nonsingleton parts
are the missing pairs.  A colour is confined to one part.  When the two
vertices of a missing pair have different colours, each is an isolated
component in the corresponding two-colour graph, so one Kempe interchange
makes the pair monochromatic.  After all parts are monochromatic there are
at most five parts and therefore an unused sixth colour.  This unused colour
is a buffer which changes the distinct colour assigned to each part, one
vertex at a time for a two-vertex part.  It connects every monochromatic-part
colouring to every other one; reversing the initial pair-merges reaches an
arbitrary target colouring.  Hence `Gamma_6(X)` is connected in the
exceptional branch as well.

This verifies the exact premise needed to choose the path (3.1).

## 4. The first boundary transition

The shortest-path and last-extension indices are correctly quantified.
Minimality of `k` ensures that no `r_h` with `h<k` belongs to `E_D`.
Since `r_0` belongs to `R_f subseteq E_A`, the index `i` in (3.2) exists;
its maximality ensures that every trace strictly after `r_i` and before
`r_k` lies outside both `E_A` and `E_D`.  The correction from a whole-path
claim to this suffix claim is essential and is correctly implemented.

In the consecutive case, extend `r_i` through `A` and `r_k` through `D`.
If the full two-colour component in the first closed shore met `X` only in
the operated boundary component `W`, switching it would produce exactly
`r_k` and the two closed shores would glue.  Therefore it meets another
boundary two-colour component.  A shortest first-hit path has nonempty
interior wholly in `A`; a direct boundary edge would have put the two ends
in the same boundary component.  The reverse argument in the `D`-shore is
identical, and the two interiors are disjoint because `A` and `D` are
disjoint.

In the paired-rejection case, each displayed intermediate trace is rejected
by each shore.  Extension through `Z` is equivalent to colourability of
`G[Z]` from the lists (3.3).  Choosing a vertex-minimal induced obstruction
therefore gives a nonempty connected `K_h^Z`; the degree lower bound and the
Gallai-forest statement follow by the same valid arguments checked for
Theorem 2.2.  The two alternatives are exhaustive and mutually exclusive
because they are exactly `i=k-1` and `i<=k-2`.

## 5. Theorem 4.1: strict transfer from a proper paired kernel

All three assertions of Theorem 4.1 are valid.

For a component `R_j` of `G[Z-V(K_h^Z)]`, distinct such components are
anticomplete, and every neighbour outside `R_j` lies in
`X union V(K_h^Z)`.  Its full neighbourhood separates it from the nonempty
opposite shore.  The opposite shore contains no vertex of that
neighbourhood, so this is a genuine vertex cut; seven-connectivity gives
`|N_G(R_j)|>=7`.

Because `Z-V(K_h^Z)` is nonempty, deleting it gives a proper minor and hence
a six-colouring `t`.  This colouring is defined on the full neighbourhood of
every `R_j`.  If its restriction extended through every `R_j`, choose one
extension for each component.  The components are pairwise anticomplete and
all extensions agree with `t` on every shared boundary vertex, so the
extensions glue to `t` and six-colour all of `G`.  Therefore at least one
component rejects its displayed labelled boundary trace.  This conclusion
holds for every selected six-colouring `t` of the proper minor, although only
existence is needed.

The selected component is strictly smaller than `Z` because it is disjoint
from the nonempty critical subgraph `K_h^Z`.  If its full neighbourhood `S`
has order seven, both the component and the opposite shore survive in
`G-S`, so `S` is an actual order-seven separator.  For any component `C` of
`G-S`, all neighbours of `C` outside it lie in `S`.  If `C` missed one
vertex of `S`, then `|N_G(C)|<=6`, while that missed boundary vertex survives
outside `C`; this contradicts seven-connectivity.  Thus every component of
`G-S` is adjacent to every literal vertex of `S`.

The source correctly does **not** claim that this transfer preserves
`r_h`, the original order-eight boundary, the rejected edge `f`, adjacent
Kempe moves, or any branch-set labels.  The new neighbourhood can have order
greater than eight, and when both paired kernels span their shores there is
no strict transfer.  Accordingly Theorem 4.1 is a valid host-level decrease,
not a recursive state-preserving induction.

## 6. Trust boundary

The audited note proves:

1. an exact fixed-trace deletion/list-colouring equivalence;
2. a second spanning edge-minimal list-critical obstruction with non-tight
   rejected-edge endpoints;
3. a suffix dichotomy along a shortest boundary Kempe sequence; and
4. a strict transfer to a smaller connected component when a paired kernel
   is proper.

It does not prove a `K_7`-minor model, compatible colourings across an
order-seven separator, allocation of Kempe paths to prescribed branch sets,
or a well-founded iteration preserving the original trace.  No unstated
conclusion of that kind was used in the proofs.  Within this exact scope, no
unresolved mathematical gap was found.
