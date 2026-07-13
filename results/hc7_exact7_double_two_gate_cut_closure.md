# Exact-seven double-two-gate cut closure

## 1. Setting

Retain the audited exact-seven `(1,3)` three-gate cell.  Thus

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad |S|=7,
\]

`R` contains three disjoint `S`-full packets, `G[S]` is triangle-free,
and a three-cut `T={t_1,t_2,t_3}` of `G[L]` has exactly two lobes `J,K`.
Each lobe is connected and meets all three gate vertices.

Suppose `z` is a cutvertex of `J` and `J-z` has exactly two components
`A,D`.  Put

\[
                         U_A=N_T(A),\qquad U_D=N_T(D).
\]

Three-connectivity of `G[L]` gives `|U_A|,|U_D|>=2`.

## 2. The closure

### Theorem 2.1 (double-two-gate cut closure)

If

\[
                         |U_A|=|U_D|=2,                 \tag{2.1}
\]

then `G` contains a literal `K_7` minor or is six-colourable.

#### Proof

First record the literal boundary capacities.  The set

\[
                         \{z\}\cup U_A\cup N_S(A)
\]

separates `A` from the nonempty opposite shore.  Seven-connectivity and
(2.1) therefore give

\[
                         |N_S(A)|\ge4.                  \tag{2.2}
\]

The same argument gives `|N_S(D)|>=4`.  Also
`T union N_S(K)` separates the opposite lobe `K`, so

\[
                         |N_S(K)|\ge4.                  \tag{2.3}
\]

Choose distinct `g_A in U_A` and `g_D in U_D`, and let `g_0` be the
remaining member of `T`.  Such a choice always exists for two two-subsets
of a three-set: if they agree, choose their two different elements; if they
differ, choose their two exclusive elements.

The three sets

\[
 C_A=A\cup\{z,g_A\},\qquad
 C_D=D\cup\{g_D\},\qquad
 C_K=K\cup\{g_0\}                                      \tag{2.4}
\]

are disjoint, connected, and span `L`.  Their three pairwise adjacencies
are literal:

* `C_AC_D` has an edge from `z` to `D`;
* `C_AC_K` has an edge from `g_A` to `K`; and
* `C_DC_K` has an edge from `g_D` to `K`.

By (2.2)--(2.3), each carrier contacts at least four literal vertices of
`S`.  Every boundary contact list is nonempty because the connected thin
shore is `S`-full.  Apply the audited exact-seven boundary rooted-model
trichotomy to the spanning carrier triangle (2.4).  Its three outcomes give,
respectively, a synchronized proper-minor state and a six-colouring, an
anchored `K_4` and hence a literal `K_7`, or the admissible one-block state
and again a six-colouring.  This proves the theorem. `square`

## 3. Rank-free consequence

### Corollary 3.1

In a hypothetical counterexample, every cutvertex `z` of either gate lobe
has exactly two deletion components and at least one of those components
meets **all three** gate vertices.

#### Proof

The audited nested-cutvertex exchange already excludes three or more
deletion components.  Each of the two remaining components meets at least
two gates.  If neither met all three, both gate supports would have order
two, contrary to Theorem 2.1. `square`

This conclusion does not use a portal-rank-two rooted triangle.  Along a
linear block chain the left gate supports are nested increasingly and the
right supports decreasingly, so every surviving cut is oriented toward at
least one full-gate side.  The theorem does not yet turn that orientation
into a support-four carrier on the full-gate side: seven-connectivity gives
only three boundary contacts there.  If one side meets two gates and the
other all three, the direct support profile is `4/3/4`; if both sides meet
all three, it is `3/3/4`.  Further portal contacts may raise these bounds,
but the present theorem does not exclude either low-support profile.
