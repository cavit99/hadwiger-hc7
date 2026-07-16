# Independent audit: two-root Kempe orientation transition

**Verdict:** **GREEN**, with the scope guard that the transition theorem
does not itself produce the localized residual branch set `W` used in the
sufficient `K_7`-completion criterion.

**Audited source:**
[`hc7_two_root_kempe_orientation_transition.md`](hc7_two_root_kempe_orientation_transition.md).

**Audited SHA-256:**
`83d49aff3cd363765b83d111c2b52e2eec2ba545a757792f499cec9f5b9e2c9c`.

The audit was performed independently from the proof draft and checked the
exact root contacts, the recolouring argument for untouched colours, the
separator conclusion, and the localized branch-set construction.

## 1. Exact contacts

For a root `r` and a colour `delta in {alpha,beta}`, write

\[
 I_r^\delta=N_J(r)\cap V(K)\cap c^{-1}(\delta),\qquad
 O_r^\delta=(N_J(r)-V(K))\cap c^{-1}(\delta).
\]

If `lambda` is the colour lost by `a` and `gamma` the colour gained by
`b`, the claimed conditions are exactly

\[
 I_a^\lambda\ne\varnothing,\quad I_a^{\bar\lambda}=\varnothing,
 \quad O_a^\lambda=\varnothing,\quad
 O_a^{\bar\lambda}\ne\varnothing,                         \tag{1.1}
\]

and

\[
 I_b^\gamma=O_b^\gamma=\varnothing,\quad
 I_b^{\bar\gamma}\ne\varnothing,\quad
 O_b^{\bar\gamma}\ne\varnothing.                         \tag{1.2}
\]

Only the two switched colours can change at a root.  Equations (1.1) and
(1.2) are therefore both necessary and sufficient once the four stated
domination statuses are fixed.  They also prove uniqueness of the lost and
gained colours.  Contacts selected in `I_a^lambda` and
`I_b^bar(gamma)` are joined inside the connected graph `K`, giving the
claimed root-to-root path.  They can be the same vertex only in the
one-sided case `lambda=bar(gamma)`; the theorem correctly says only that
coincidence may occur.

## 2. Saturation by untouched colours

The recolouring argument is valid.  The `lambda`-coloured vertices of `K`
are independent.  If none had a neighbour of an untouched colour `theta`,
they could all be recoloured `theta`.  Equation (1.1) would make `a` miss
`lambda`, while (1.2) shows that `b` would still miss `gamma`, contradicting
the hypothesis on every `q`-colouring.  Applying the same reasoning to
`c'` and the inverse interchange proves the assertion for the original
`bar(gamma)` side.  No connectivity or minor-model label is smuggled into
this step.

## 3. Actual separator and connectivity count

Both roots meet `K`.  Every `alpha`- or `beta`-coloured vertex outside `K`
is anticomplete to `K`, by maximality of `K` as a component of the induced
two-colour graph.  In particular, the vertex supplied by
`O_a^bar(lambda)` lies outside `K union N_G(K)`.  Thus deleting `N_G(K)`
leaves the nonempty component `K` and at least one other surviving vertex,
so this is an actual separator.  Its only two vertices outside `J` are the
roots.  Hence `k`-connectivity gives

\[
                         |N_J(K)|\ge k-2.
\]

For `q=6,k=7`, the count and the four untouched-colour contacts stated in
the theorem follow.

## 4. Localized `K_7` completion

Under the additional condition in Section 2 of the source, let `r` be a
root adjacent to `W` and let `s` be the other root.  The seven sets

\[
          \{s\}\cup V(K),\quad \{r\},\quad W,
          \quad B_j\quad(j\ne i)
\]

are disjoint and connected.  The `r-K` contact joins the first two sets;
the `K-W` edge joins the first and third; the root-to-frame, residual-to-
frame, and frame-to-frame hypotheses supply every remaining pair.
Therefore they are an explicit `K_7`-minor model.

This final implication is conditional.  Neither Theorem 1.1 nor
seven-connectivity forces `K subseteq B_i`, produces `W`, or ensures that
deleting `K` preserves the five fixed branch sets.  The source states this
limitation correctly and does not claim that a higher-order transition
separator is a label-preserving split.
