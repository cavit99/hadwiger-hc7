# Adversarial audit of the exposure-weighted knitting argument

## Verdict

The component-exposure refinement, the hybrid full-shore/knitting theorem,
and the component bound (m\le 2q-1) are mathematically valid.  The descent
also gives a strictly smaller cut whenever the current cut has knitting
weight below (t+1).  Two wording limitations must be kept explicit:

1. the descended cut need not be a subset of the old cut and successive cuts
   need not be laminar; and
2. after preconnected witnesses have been deleted, a relative separator does
   not automatically lift at exposure cost—the full deleted witness vertex
   set may have to be paid for.

Neither point invalidates a stated numerical theorem, but both matter in any
attempt to iterate the hybrid construction.

## 1. Component exposure and the hybrid theorem

Let (S) be a minimum cut and (D) a component of (G-S).  Minimum
cardinality makes (S) inclusion-minimal, so every (s\in S) has a neighbour
in every component (D).  Otherwise (S-s) still separates (D) from a
second component.  This justifies every use of (D\cup P_i) as a connected
block witness.

For (H_A=G[A_0\cup U]) and (x\in A_0), there are no edges from (A_0) to
another component of (G-S), and (S=U\dot\cup K).  Hence the claimed
degree calculation is in fact the exact identity

\[
 d_{H_A}(x)=d_G(x)-|N_G(x)\cap K|.
\]

If ((C,D)) is a proper relative separation of ((H_A,U)), oriented with
(U\subseteq C), then its far side is contained in (A_0).  Every escape
from (D-C) in (G) meets

\[
 (C\cap D)\cup K.
\]

The two sets are disjoint because (C\cap D\subseteq A_0\cup U) and
(K\cap(A_0\cup U)=\varnothing).  Thus the lifted cut has order

\[
 |C\cap D|+|K|<|U|+|K|=|S|,
\]

and the opposite selected component certifies that both sides are nonempty.
This verifies the most delicate step in Theorem 2.1.

The knitted family in (A_0\cup U) is disjoint from all fixed families
(A_i\cup P_i): the shore components are distinct and (F\cap U=\varnothing).
The same is true on the (B)-side.  Grouping whole components then gives a
proper separation with common boundary (S), so exact-state gluing applies.
No complete bipartite adjacency between blocks is being assumed; the one
witnessing boundary edge per block pair survives the contractions.

## 2. Component count

For (q\ge1), if (m\ge2q), take (I=[q]) and (U=\varnothing).  Assign a
different full component to each of the (q) blocks on each of two sides.
This gives the two disjoint block realizations and hence a colouring.  Thus

\[
 m\le2q-1.
\]

For (q=0), the displayed numerical bound should not be read literally as
(m\le-1).  Rather, the complete quotient consists only of singleton
blocks, so (G[S]) is a clique and exact-state gluing rules out the cut
outright.  This is already stated in the source note, but it is worth keeping
separate from the formula.

In Corollary 2.3, the cleanest quantifier is: choose the two globally
least-exposed components for (A_0,B_0), and choose any other (2|I|)
components for the fixed blocks.  The hypothesis (m\ge2(|I|+1)) is exactly
what makes this possible.  With that reading, (2.4) and its consequence
(|S|+7|U|\ge t+1) are valid.

## 3. Preconnected witnesses

Theorem 2.4 is valid as a conditional gluing theorem.  The deletion loss

\[
 \Delta_Z=\max_{x\in H_Z-U}(d_G(x)-d_{H_Z}(x))
\]

counts every edge lost on deleting the singleton set and the fixed witness
vertices, so (d_{H_Z}(x)\ge t-\Delta_Z) is correct.  The assumptions that
the witnesses are pairwise disjoint and avoid (U) ensure that the knitted
residual family can simply be adjoined.

There is, however, no exposure-cost lifting statement here.  If a relative
separator (X) occurs in (H_Z=G[Z]-W_Z), its lift to (G) is generally

\[
 X\cup W_Z,
\]

not (X) plus only the boundary neighbourhood exposed by (W_Z).  The set
(W_Z) can be arbitrarily large.  Therefore Theorem 2.4 may be used for
gluing when the residual is inseparable, but a separator outcome cannot be
fed into Proposition 3.1 without a further portal-peeling lemma.

## 4. What the descent really proves

For the unpeeled graph (G[A]-R), a relative separator (W) lifts to

\[
 S'=W\cup R,
\]

and (|S'|<|S|).  Repeating whenever the new cut has weight below (t+1)
must terminate, solely because the cut order is a strictly decreasing
nonnegative integer.  The terminal cut has knitting weight at least (t+1).

But normally (W\subseteq A-S), so (S'=W\cup R) is not a subset of (S).
The construction nests a *separated region* for that one step; it does not
produce nested separator vertex sets.  A later minimum-side choice can cross
an earlier one.  Thus Proposition 3.1 is a **strict-order descent**, not yet a
laminar-decomposition theorem.  Any use of a global tree or holonomy argument
still needs an uncrossing proof.

## 5. Weakest portal-splitting target consistent with the tetrahedron

The tetrahedral portal system in
`hadwiger_c6_portal_tetrahedron_obstruction.md` shows that no statement based
only on two-connectivity, frame ownership, and abstract portal sets can force
six coherent roots.  It even survives every coarse two-piece atlas test.  The
missing lemma must explicitly use degree loss or a liftable separator.

A minimally strong label-free target is the following.

> **Low-loss split-or-lift lemma.**  Let (Z) be one side of a separation in
> a minor-minimal counterexample, and let \(\Pi\) be a complete-quotient
> independent partition of its boundary.  For a prescribed family (I) of
> blocks, either
>
> 1. there are pairwise disjoint connected witnesses (F_i^Z), (i\in I),
>    avoiding the unresolved terminal set (U), such that their deletion
>    loss is the actual local exposure and the residual pair ((H_Z,U)) is
>    relatively (|U|)-inseparable; or
> 2. a proper residual relative separator lifts to a cut smaller than the
>    current boundary after charging only the separator's boundary footprint;
>    or
> 3. some vertex has total degree at most (t-1).

Outcome 1 is exactly the hypothesis needed by Theorem 2.4.  Outcome 2 is
exactly what is needed by strict-order descent.  Outcome 3 is essential: the
portal tetrahedron realizes it sharply with degree six when (t=7), and is a
counterexample if that outcome is omitted.

This is weaker than demanding a coherent rooted clique model: it asks only
for enough low-loss block witnesses to reduce the knitting core, and it
allows the two genuine obstruction mechanisms—liftable separators and low
degree.  What remains unproved is the portal-peeling assertion that one of
these three outcomes always occurs.
