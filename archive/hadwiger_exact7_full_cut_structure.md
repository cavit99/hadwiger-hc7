# Exact seven-cuts in the `HC_7` setting

## 1. Fullness is automatic

### Lemma 1.1 (components behind a minimum cut are full)

Let `G` be seven-connected and let `X` be a vertex cut of order seven.
Then every component of `G-X` has neighbourhood exactly `X`.

### Proof

For a component `C` of `G-X`, its neighbourhood is contained in `X`.
If it were a proper subset, deleting `N_G(C)` would separate `C` from
the other component(s) of `G-X` using at most six vertices, contrary to
seven-connectivity.  QED.

Thus every exact-seven cut is automatically a multi-full-shore gate; no
separate contact hypothesis is needed.

## 2. Chromatic structure of the gate

### Theorem 2.1 (four colours or the pentagonal join)

Let `G` be seven-connected and `K_7`-minor-free, and let `X` be a vertex
cut of order seven.  Then

\[
                              \chi(G[X])\le5.        \tag{2.1}
\]

If equality holds, then

\[
                              G[X]\cong K_2\vee C_5. \tag{2.2}
\]

### Proof

Choose two components of `G-X`.  By Lemma 1.1 they are connected,
anticomplete full shores.  The one-reserve full-shore lift says that

\[
                              \eta(G[X-x])\le4
                              \qquad(x\in X),        \tag{2.3}
\]

since a `K_5` model in one deletion, together with the two full shores,
would give a `K_7` model.  The already known `HC_5` makes every `X-x`
four-colourable, proving (2.1).

Suppose equality holds and let `H` be a 5-critical induced subgraph of
`G[X]`.  If `H` omitted a vertex `x` of `X`, then `H subseteq X-x`; by
`HC_5`, the five-chromatic graph `H` would contain a `K_5` minor,
contradicting (2.3).  Hence `H=G[X]`: the boundary itself is 5-critical.

Gallai's theorem applies because `|X|=7<=2(5)-2` and decomposes `G[X]`
as a nontrivial join of critical factors.  Continue decomposing every
factor to which Gallai applies.  The excess `|J|-chi(J)` is additive
under joins and has total two.  No critical graph has excess one (the
standard complement-matching argument), so exactly one terminal factor
has excess two and all other factors are complete.  A terminal
excess-two factor has chromatic number at most three, since for chromatic
number at least four its order `r+2` is at most `2r-2` and Gallai would
decompose it further.  Critical graphs of chromatic number one or two
are complete and have excess zero; the 3-critical graphs are odd cycles,
and excess two selects `C_5`.  The complete factors have total chromatic
number two and join to `K_2`.  This proves (2.2).  QED.

## 3. The pentagonal equality case is impossible

The static one-reserve lift alone does not remove `K_2 vee C_5`, because
every one-vertex deletion of this graph has Hadwiger number at most four.
The full-shore web theorem does remove it.

### Theorem 3.1 (exact-seven boundary is four-colourable)

Let `G` be seven-connected, `K_7`-minor-free, and not six-colourable, and
let `X` be a vertex cut of order seven.  Then

\[
                              \chi(G[X])\le4.        \tag{3.1}
\]

### Proof

By Theorem 2.1 it is enough to exclude

\[
                              G[X]\cong K_2\vee C_5. \tag{3.2}
\]

If `G-X` has at least three components, choose three of them
`C_1,C_2,C_3`.  They are pairwise anticomplete connected shores, each
full to `X`, by Lemma 1.1.  Write the rim of (3.2) as
`v_0v_1v_2v_3v_4v_0`, with universal vertices `a,b`.  Reserve `v_0` for
`C_2` and `v_2` for `C_3`.  The four vertices

\[
                              a,b,v_3,v_4
\]

induce a `K_4`.  The full-shore reserve lift applied to these four
singleton bags and the three bags

\[
                     C_1,\qquad C_2\cup\{v_0\},\qquad
                     C_3\cup\{v_2\}
\]

gives a `K_7` model, a contradiction.  Hence `G-X` has exactly two
components.

Now apply the full `C_5` web-closure theorem proved in
`hadwiger_c5_full_web_closure.md`.  For completeness, its dichotomy is
as follows.  Attach five artificial terminals to the five rim portal
sets in each shore.  A crossing in either shore gives an explicit
`K_7` model, using the opposite full shore as the seventh bag.  If both
terminal tuples are crossless, the generalized Two Paths Theorem gives
same-vertex five-web completions.  Any nonempty clique inserted behind a
facial triangle has at most the three facial neighbours and the two
universal boundary vertices as its ambient neighbourhood, contrary to
seven-connectivity.  Thus both completions are bare disk webs.  Gluing
the disks along their common rim proves that `G-{a,b}` is planar.  Four
colours on this planar graph and two fresh colours on the adjacent
vertices `a,b` give a six-colouring of `G`, again a contradiction.

Thus (3.2) is impossible and (3.1) follows.  QED.

The same-vertex web-completion input and every branch-set adjacency in
the crossing model were independently audited in
`hadwiger_exact7_five_defect_web_closure_audit.md`.

## 4. Exact remaining boundary problem

Every exact-seven cut in a hypothetical minimal `HC_7` counterexample
therefore has a four-colourable boundary.  The remaining task is no
longer a pentagonal rooted-model exception: it is the uniform
four-block knitted/gluing exchange across a full minimum adhesion.
