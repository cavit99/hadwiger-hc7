# Four portal reductions at the aligned degree-eight interface

**Status:** written proof; separate internal audit **GREEN** in
[`hc7_degree8_four_portal_reduction_audit.md`](hc7_degree8_four_portal_reduction_audit.md).
This is a structural reduction inside the non-wheel degree-eight branch and
does not prove `HC_7`.

## 1. Setup

Retain the hypothetical-counterexample setup and notation of the audited
[two-defect component closure](hc7_degree8_two_defect_component_closure.md).
Thus

\[
 S=I\mathbin{\dot\cup}T\mathbin{\dot\cup}\{p,q\},
 \qquad |I|=|T|=3,
\]

and `G-S` has, among its components, the two boundary-full open shores
`E,F` and the singleton `{u}`.  Every root connector in either shore meets
every carrier for either `I` or `T`.  Write `c_E,c_F` for the fixed aligned
closed-shore colourings supplied by the bilateral response-cycle theorem,
and use `c_Q` for the one on shore `Q`.

For a shore \(Q\in\{E,F\}\), a block \(B\in\{I,T\}\), and a boundary
vertex `s`, put

\[
                         P_s^Q=N_G(s)\cap Q.             \tag{1.1}
\]

All five sets \(P_p^Q,P_q^Q,(P_b^Q:b\in B)\) are nonempty because `Q` is
full to `S`.

## 2. One shore and one independent block

### Theorem 2.1 (portal reduction)

For every ordered pair \((Q,B)\in\{E,F\}\times\{I,T\}\), at least one of
the following holds.

1. **Generic exact-seven response.**  The graph has a generic exact-seven
   response interface in the sense of the audited
   [generic restart theorem](hc7_generic_exact7_response_restart.md).
2. **Small shore.**  \(|Q|\le6\).
3. **Strict order-eight lobe.**  There is a nonempty connected proper set
   \(C\subsetneq Q\) such that \(|N_G(C)|=8\), every component of
   \(G-N_G(C)\) is full to `N_G(C)`, and there are exactly two or three
   such components.  Deletion of any edge from `C` to its boundary has a
   six-colouring with monochromatic ends.  This is a fresh response
   interface; it need not retain the original `p,q,I,T` operation labels.
4. **Positive-excess connected set.**  There are a set \(K\subseteq Q\)
   and a nonempty connected proper set \(C_B^Q\subsetneq Q\) such that

   \[
      R_B^Q:=N_{G[Q]}(C_B^Q)\subseteq K,
      \qquad |K|\le5,\qquad 9\le |N_G(C_B^Q)|\le13,  \tag{2.1}
   \]

   and

   \[
      |N_G(C_B^Q)\cap S|\ge9-|K|.                     \tag{2.2}
   \]

   In fact the stronger bounds

   \[
      |N_G(C_B^Q)\cap S|\ge9-|R_B^Q|,
      \qquad |S-N_G(C_B^Q)|\le |R_B^Q|-1\le4          \tag{2.3}
   \]

   hold.

   The set `N_G(C_B^Q)` is the boundary of an actual separation.  There
   are five distinct nominated representatives of the portal sets for which
   the corresponding five-terminal completion has one of the two terminal
   distributions stated in Theorem 2.1 of the audited three-portal
   reduction.  For
   every edge `xy` with \(x\in C_B^Q\) and
   \(y\in N_G(C_B^Q)\), every proper six-colouring of `G-xy` makes `x,y`
   monochromatic.  The equality partition it induces on the full separator
   `N_G(C_B^Q)`, viewed from the closed side opposite `C_B^Q`, differs from
   the restriction of the fixed aligned `Q`-shore colouring `c_Q` from the
   bilateral response-cycle theorem; equality would glue to a six-colouring
   of `G`.

### Proof

Apply the audited
[three-portal two--three reduction](hc7_order8_three_portal_two_three_reduction.md)
to the component `Q` of `G-S`, with its terminal pair `p,q` and terminal
triple `B`.  Its other-component hypothesis is witnessed by `{u}` (and also
by the opposite shore).

Its first outcome gives disjoint connected subgraphs `D,R` in `Q`, where
`D` contains a nontrivial path between a vertex of `P_p^Q` and a vertex of
`P_q^Q`, while `R` meets every `P_b^Q` for \(b\in B\).  Hence `D` is a
root connector and `R` is a `B`-carrier.  This contradicts the universal
connector--carrier intersection theorem.  The packing outcome is therefore
impossible.

The reduction's small-component outcome is item 2.  Consider any actual
order-seven separation it returns.  Its proof supplies a nonempty connected
set `A`, with \(N_G(A)\) as the seven-vertex boundary and a nonempty
opposite side.  Choose an edge `xy` from `A` to `N_G(A)`.  Minor-criticality
gives a proper six-colouring of `G-xy`; its ends are monochromatic, since
otherwise restoring `xy` would six-colour `G`.  The restriction to the
opposite closed shore induces a complete boundary equality partition which
cannot extend through the intact `A`-shore.  This is exactly a generic
exact-seven response interface, proving item 1.

Assume now that items 1--3 do not otherwise hold.  It remains to consider
the connected proper set `C` returned behind the five-terminal completion
cut.  Its full boundary has order at least eight.
If that order is eight, apply the audited
[small-boundary lobe theorem](hc7_order8_small_boundary_lobe_descent.md).
The theorem gives either another actual order-seven separation, which is
item 1 by the preceding argument, or item 3.  If the boundary has order at
least nine, put \(R_B^Q=N_{G[Q]}(C)\).  Corollary 3.1 of the three-portal
reduction gives \(R_B^Q\subseteq K\), (2.1)--(2.2), the terminal distribution,
and the forced monochromatic edge responses.  Since all neighbours of `C`
outside `Q` lie in the eight-set `S`, one also has
`|N_G(C)|<=|R_B^Q|+8<=13`; rearranging the lower bound nine gives (2.3).

Finally, compare any displayed edge-deletion colouring on the full
separator `N_G(C)`, viewed from the closed side opposite `C`, with the
restriction of the fixed aligned colouring `c_Q` of the intact `Q`-shore
to that separator.  If their equality partitions agreed, a permutation of
colour names would align them and the two closed-shore colourings would glue
to a proper six-colouring of `G`.  They therefore differ, completing item 4.
\(\square\)

### Corollary 2.2 (fourfold reduction)

Either one of items 1--3 of Theorem 2.1 holds, or one may select four
positive-excess connected sets, not necessarily distinct,

\[
                 C_I^E,\quad C_T^E,\quad C_I^F,\quad C_T^F             \tag{2.4}
\]

with the literal shore, block role, separator, terminal distribution, and
edge-deletion responses in item 4.

### Proof

Apply Theorem 2.1 to the four ordered pairs `(E,I)`, `(E,T)`, `(F,I)`, and
`(F,T)`. \(\square\)

### Corollary 2.3 (bounded minimum-excess normal form)

If item 4 of Theorem 2.1 occurs for any pair `(Q,B)`, then at least one of
the following holds.

1. The graph has a generic exact-seven response interface.
2. There is a set `X` with

   \[
                         8\le |X|\le13                 \tag{2.5}
   \]

   such that `G-X` has exactly \(m\in\{2,3\}\) components and every
   component is adjacent to every literal vertex of `X`.  Moreover, if
   \(1\le r\le m\), any `r` distinct components and any `r`-set
   \(F\subseteq X\) satisfy

   \[
              \chi(G[X-F])\le6-r,
              \qquad K_{7-r}\not\preccurlyeq G[X-F].  \tag{2.6}
   \]

   Deleting an edge between one component and `X` gives a complete equality
   partition of `X` which extends through every other component-side and is
   rejected by the intact operated component-side.

This normal form need not retain `S`, the block `B`, the aligned path, or
the original boundary operation.

### Proof

The connected set in item 4 is eligible for the audited minimum
positive-excess separator theorem and has boundary order at most thirteen.
Choose an eligible connected set with globally minimum boundary order and
write its boundary as `X`.  Thus \(8\le|X|\le13\).  The minimum-separator
theorem gives either a component with an exact order-seven full
neighbourhood, which supplies item 1 exactly as in Theorem 2.1, or exactly
two or three components full to `X`.  Its universal contraction profile
is (2.6), and its operation-specific response corollary gives the final
assertion. \(\square\)

### Corollary 2.4 (three-component tagged-lobe exit)

Let `C=C_B^Q` be a selected lobe from item 4, put

\[
        X=N_G(C),\qquad R=X\cap Q,
        \qquad M=S-X,                                  \tag{2.7}
\]

and suppose `G-X` has exactly three components, all full to `X`.  Then
`M` is nonempty, and there are disjoint adjacent connected sets in `Q`
which are both adjacent to every vertex of `S-M`.  Consequently, whenever
\(|M|\le2\), this is the one-shore common-defect pair required as one half
of the four-bag input in Section 3.

### Proof

The set `R` is nonempty: since `Q` is connected and `C` is nonempty and
proper, some edge joins `C` to `Q-C`.  If `M` were empty,
then \(S\subseteq X\) and `{u}` would be a component of `G-X`; it has no
neighbour in the nonempty set `R`, contrary to every component being full
to `X`.  Thus `M` is nonempty.

The component of `G-X` containing `u` also contains `M` and the open shore
opposite `Q`, since `u` and that shore are both adjacent to every vertex of
the nonempty set `M`.  Besides this component and `C`, let `D` be the third
component.  All vertices outside `Q` which survive deletion of `X` lie in
the component just described, so \(D\subseteq Q\).

Choose any \(r\in R\).  The sets \(C\cup\{r\}\) and `D` are disjoint and
connected.  They are adjacent because `D` is full to `X`, and both are
adjacent to every vertex of \(S-M\subseteq X\): this is the definition of
`X=N_G(C)` for the first set and fullness for `D`. \(\square\)

## 3. Correct next bifurcation

Corollary 2.2 does not by itself produce two genuinely coupled block-tagged
lobes.  In the terminal-free completed-cut form, the same connected set `C`
behind the same cut `K` may witness both the `I`- and `T`-applications: all
nominated vertices and all virtual edges lie on the other side.  The
positive-excess arithmetic, entering-edge responses and mismatch with `c_Q`
then depend only on `C,N_G(C),c_Q`, not on `B`.  The two selected witnesses
may therefore be literally identical.  Ordinary uncrossing or independent
lexicographic minimization cannot recover a block role which has vanished.

The next work should split accordingly.

1. **Block-blind minimum-boundary response coupling.**  Use Corollary 2.3.
   The first milestone is the case \(|X|=8\) in which `G-X` has exactly two
   `X`-full components, together with (2.6) and the operation-specific
   extension/rejection responses.  Prove an explicit `K_7`-minor model, one
   complete equality partition extending through both closed sides, or an
   exact-seven response on a literal connected shore strictly smaller than
   the operated `X`-full component, measured by vertex count in the unchanged
   host.
   Treat the three-component order-eight case next, then boundary orders
   nine through thirteen.  Corollary 2.4 is already a fast exit when the
   selected tagged lobe itself has the three-component normal form and
   defect at most two.
2. **Genuinely tagged split-terminal cuts.**  If both block applications
   can be selected in their split-terminal forms, use the surviving `I`-
   and `T`-representatives, rather than their labels alone, to force the two
   adjacent connected sets with one common defect of order at most two.
   The strengthened four-bag allocation then gives an explicit `K_7` model.

The finite computation is now complete only for that last allocation step.
Corollary 2.3 bounds `X`, but the two or three component interiors remain
unbounded and determine their colouring-extension languages, rooted-minor
behaviour and operation provenance.  A proof-producing exhaustive search
therefore first needs a written finite-signature replacement lemma with a
certificate lift back to the unchanged host.  Before such a lemma,
computation is useful for falsifying proposed response-coupling statements
and discovering missing signatures, not for proving the unbounded theorem.

The small-shore alternative remains open.  Likewise, the fresh exact-seven
and strict order-eight interfaces above do not preserve the original
`p,q,I,T` operation labels; they are structural reductions, not a common
boundary partition or a strict restart on a component of `G-N[u]`.

## Inputs

- [two-defect component closure and universal connector--carrier intersection](hc7_degree8_two_defect_component_closure.md)
- [three-portal two--three linkage reduction](hc7_order8_three_portal_two_three_reduction.md)
- [small-boundary lobe descent](hc7_order8_small_boundary_lobe_descent.md)
- [generic exact-seven response restart](hc7_generic_exact7_response_restart.md)
- [minimum positive-excess separator normal form](hc7_minimum_positive_separator_normal_form.md)
