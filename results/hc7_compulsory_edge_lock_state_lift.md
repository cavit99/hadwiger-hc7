# Lifting a compulsory-edge state through one rich lock bridge

**Status:** proved and independently audited.

This note couples one legal colouring of `G-zu` to a deletion/contraction
state of a literal rich-side edge.  It does not identify that edge with the
independently chosen edge in the earlier final-two-duty trace.

## 1. Setup

Let

\[
 V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}R
\]

be the frozen atomic separation, with no `A-R` edge.  Assume explicitly,
as part of that frozen setup, that `A` is connected and `S`-full: every
literal vertex of `S` has a neighbour in `A`.  Let

\[
                         e=zu,\qquad z\in A,\quad u\in S
\]

be the unique compulsory portal edge.  Assume `G` is not six-colourable
and every proper minor is six-colourable.

Fix a proper six-colouring `phi` of `G-e`.  Necessarily

\[
                         \phi(z)=\phi(u)=\alpha.        \tag{1.1}
\]

For a colour `beta != alpha`, let `K` be the `alpha-beta` component of
`G-e` containing `z` and `u`; its existence is the audited compulsory-edge
Kempe lock.  Suppose `f=xy` is a bridge of `K` separating `z` from `u`,
and suppose `f` is either rich-internal or boundary--rich:

\[
       x,y\in R,qquad\hbox{or}\qquad
       |\{x,y\}\cap R|=|\{x,y\}\cap S|=1.             \tag{1.2}
\]

Let `X` be the vertex set of the component of `K-f` containing `z`, and
put

\[
                         T=X\cap S.                    \tag{1.3}
\]

Let `Pi` be the exact equality partition of `S` under `phi`.

## 2. The coupled deletion/contraction state

### Lemma 2.1 (lock-bridge state lift)

Interchanging `alpha,beta` on `X` produces a proper six-colouring `psi`
of `G-f`.  Its two ends `x,y` have the same colour, so `psi` also descends
to a proper six-colouring of `G/f` (retaining the literal boundary label
when `f` is boundary--rich).

On the literal boundary, `psi` is obtained from `phi` by toggling exactly
the vertices of `T` between `alpha` and `beta`; every other boundary
colour is unchanged.

#### Proof

The set `X` is one component of the `alpha-beta` graph after deleting the
bridge `f`.  Hence swapping its two colours preserves every edge of
`G-{e,f}`.  The vertex `z` changes from `alpha` to `beta`, while `u` stays
`alpha`, so restoring `e` is proper.  Before the swap the two ends of `f`
had the distinct colours `alpha,beta`; exactly one end lies in `X`, so
after the swap they have the same colour.  Thus only `f` remains improper,
which proves both the `G-f` colouring and its descent to `G/f`.

The swap changes a boundary vertex exactly when it lies in `X`; this is
precisely (1.3).  `square`

## 3. Exact reproduction or a rich blocking path

Let

\[
                  H_R=G[R\cup S]
\]

with the colouring inherited from `phi`.  This is an intact rich
closed-shore colouring, because the missing edge `e` has its other end in
`A`.  Consider the `alpha-beta` components of `H_R`.

### Theorem 3.1 (same-state lift or literal rich crossing)

Exactly one of the following mechanisms occurs.

1. `T` is a union of the boundary traces of `alpha-beta` components of
   `H_R`.  Swapping precisely those components gives an intact rich-shore
   colouring which agrees on every literal member of `S` with
   `psi|G[A\cup S]`.  Consequently `G` is six-colourable.
2. There is an `alpha-beta` path `P` in `H_R`, with one end in `T`, the
   other in `S-T`, all internal vertices in `R`, and `f in E(P)`.

In a hypothetical counterexample only item 2 can occur.  Thus one legal
`G-e` state, the coupled legal `G-f`/`G/f` state of Lemma 2.1, and the
literal rich path through `f` coexist in one two-colour transition.

#### Proof

If no `alpha-beta` component of `H_R` meets both `T` and `S-T`, then `T`
is a union of component boundary traces: swap every component which meets
`T`.  Components with empty boundary trace may be left unchanged.  On
`S`, this toggles exactly `T`, so the resulting intact rich-shore
colouring agrees literally with `psi` on `S`.

Condition (1.2) puts `f` outside the induced thin closed shore.  Therefore
`psi|G[A\cup S]` colours that shore intact, including the restored edge
`e`.  The two shore colourings agree on `S`, and there is no `A-R` edge,
so they glue to a proper six-colouring of `G`.  This proves item 1.

Otherwise some `alpha-beta` component of `H_R` meets both `T` and
`S-T`.  Choose a shortest path in that component between the two boundary
sets.  No internal vertex lies in `S`, since such a vertex belongs to one
of the two sets and would shorten the path.  Hence all internal vertices
lie in `R`.

Every vertex of `T` lies in the `z`-side `X` of `K-f`.  The other endpoint
of the path is connected to it by `alpha-beta` edges of `G-e`, so it also
lies in `K`; because it is not in `T=X\cap S`, it lies in the `u`-side of
`K-f`.  Since `f` is the sole edge of `K` between those two components,
the path contains `f`.  This is item 2.  The alternatives are exhaustive,
and item 1 is impossible when `G` is not six-colourable.  `square`

### Corollary 3.2 (the lifted state has demand at least two)

Let `Pi'` be the exact boundary partition under `psi`.  If

\[
                       d_{G[S]}(\Pi')\le1,
\]

then `G` contains a literal `K_7` model or is six-colourable.  Hence in a
hypothetical counterexample every lifted state has packet demand at least
two.

#### Proof

The connected thin shore `A` is an `S`-full packet.  Apply the audited
exact packet-reflection lemma with `q=1` to `Pi'`, contracting on the thin
closed shore.  It either displays a literal `K_7`, or produces an intact
rich closed-shore colouring with exact boundary partition `Pi'`.

In the latter case, `f` lies outside the induced thin closed shore by
(1.2), so `psi|G[A\cup S]` is an intact thin colouring with the same
exact partition.  Align the palettes and glue, six-colouring `G`.
`square`

## 4. Exact scope and remaining obstruction

The theorem is the missing legal coupling at one lock bridge:

\[
 \boxed{
  \text{one state of }G-zu
  \longrightarrow
  \text{one explicitly related state of }G-f\text{ and }G/f
  \longrightarrow
  \text{common state or a literal rich path through }f.}
\]

It avoids comparing unrelated extension languages.  It also proves that
the rich path is not an arbitrary geometric replacement: its colours,
boundary trace, and edge `f` are all carried by the same transition.

The remaining theorem-strength obstruction is precise.  One must either:

* choose a compulsory lock whose rich bridge `f` is compatible with the
  separating edge localized in the final-two-duty trace; or
* use the path in item 2 together with the `z`-side trace `T` and the
  saturated bridge fan to construct the audited adjacent carriers, a
  strict state-carrying exact-seven descent, or a normalized labelled
  `S1/S4` handoff.

The lemma does not assert that every compulsory lock has a rich-side
bridge.  If all five locks are edge-nonseparable on the rich side, their
two-route structure is a separate branching residue.  Nor does the lemma
assert that its dynamically selected `f` equals an independently selected
trace-blocking edge.

### Corollary 4.1 (exact compatibility test for the localized trace edge)

Let `f` be the rich-internal or boundary--rich separating edge returned by
the audited final-two-duty localization theorem.  If some legal colouring
of `G-e` and some alternative colour make this same literal `f` a bridge
separating `z,u` in the corresponding compulsory lock, then that one
colouring and the dynamically constructed legal `G-f`/`G/f` state satisfy
Theorem 3.1.  This state need not equal the independently localized
`Pi/BC` state.
In particular, either `G` is six-colourable or there is a literal
two-colour boundary-to-boundary path through the named trace edge `f`, with
all internal vertices in `R`, in the same `G-e` state.

Thus failure to couple the two audited constructions has an exact finite
meaning: for every legal `G-e` state and every one of its five compulsory
locks, the named localized edge is absent from the lock or is not a
`z-u`-separating bridge.  An argument that claims the states intersect must
discharge precisely this compatibility condition.
