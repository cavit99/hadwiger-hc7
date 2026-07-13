# Exact-trace marked states at the order-eight web gate

## 1. The reference trace

Assume the setting of
`hadwiger_order8_tight_hall_palette_exchange.md`.  Thus

\[
 N(v)=S=\{c_0,\ldots,c_5,z\},
\]

`c_0c_1` is a missing boundary edge, `x` is their common exterior
portal, and the hard defect is

\[
                         a\in\{c_3,c_4\}.           \tag{1.1}
\]

Let

\[
 B=\{x,p,q\}\cup(S-\{c_1,a\})                    \tag{1.2}
\]

be the exact order-eight gate, and let `K` be the component on its open
side.

Contract the independent star on `v,c_0,c_1`, colour the proper minor,
and expand it in `G-v`.  Denote the resulting exact-trace six-colouring
by `c`.  Then

* `c_0,c_1` have one common colour `rho`; and
* the five vertices `S-{c_0,c_1}` have five distinct private colours.

Write `theta=c(a)`.  The old-boundary part of `B` has exactly five
colours, and `theta` is the unique trace colour missing there:

\[
 |c(S\cap B)|=5,
 \qquad
 [6]-c(S\cap B)=\{\theta\}.                       \tag{1.3}
\]

## 2. Exact orientation of a partition-preserving transition

### Lemma 2.1 (neighbourhood-free transitions change every boundary partition)

The following statement is parameter-uniform.  Let `G` be non-`r`-
colourable, let `H=G-v`, and let `(A,D)` be a separation of `H` with
adhesion `X`.  Suppose

\[
                         N(v)\cap(A-X)=\varnothing. \tag{2.1}
\]

Let `e` have at least one endpoint in `A-X` and both endpoints in `A`,
let `c` be any `r`-colouring of `H`, and let `d` be any `r`-colouring
of `G-e`.  Then

\[
                         \Pi_X(d)\ne\Pi_X(c).       \tag{2.2}
\]

### Proof

Assume the partitions agree and apply Theorem 3.1 of
`hadwiger_all_trace_transition_gate.md`.

If `d` is unpinned at `X`, that theorem gives

\[
 [r]-c(X)\subseteq c(N(v)\cap(A-X))=\varnothing.
\]

Hence `c(X)` uses all `r` colours.  Equality of partitions says that
`d(X)` also uses all `r` colours, so the colour `d(v)` occurs on `X`.
This contradicts unpinnedness.

If `d` is pinned, let `Q` be its marked block and let `delta` be the
`c`-colour of `Q`.  The pinned clause of the same theorem gives a vertex
`n in N(v) cap A` of colour `delta` under `c`.  By (2.1), `n in X`, so
`n` belongs to the `delta` block `Q` of `Pi_X(c)`.  Equality of the
partitions gives `d(n)=d(v)`, contradicting the edge `vn`, which is still
present in `G-e`.  Both cases are impossible.  QED.

### Corollary 2.2 (every internal order-eight operation changes the trace)

Let `e` have at least one endpoint in `K` and both endpoints in `K union B`,
and let `d` be a six-colouring of `G-e`.  Suppose

\[
                         \Pi_B(d)=\Pi_B(c).         \tag{2.3}
\]

Then no such `d` exists.

### Proof

Apply Lemma 2.1 to `A=K union B` and `X=B`.  The open component `K`
contains no vertex of `N(v)=S`.  QED.

Thus every faithful deletion on the hard web side changes the equality
partition of the entire order-eight gate.  This is stronger than merely
saying that its marked state differs from the state of an opposite
transition.

## 3. Interaction with crossed marked states

### Lemma 3.1 (absolute novelty on the web side)

For every edge `e_K` supported on the open `K` side and every colouring
`d_K` of `G-e_K`,

\[
                         \Pi_B(d_K)\ne\Pi_B(c).     \tag{3.1}
\]

If `e_O` is an edge on the opposite open side and `d_O` is a colouring
of `G-e_O`, then additionally

\[
                         \sigma_B(d_K)\ne\sigma_B(d_O).       \tag{3.2}
\]

### Proof

Equation (3.1) is Corollary 2.2.  Equation (3.2) is Theorem 1.1 of
`hadwiger_fixed_model_transition_gate.md`.  QED.

Thus the web side has **absolute partition novelty** relative to every
honest colouring of `G-v`, not merely marked-state disagreement with one
chosen opposite transition.  Crossed-state disjointness constrains the
new states pairwise, but it does not force one of them to return to the
reference partition.

## 4. A graph-realizable obstruction to a state-only closure

The transition diamond in
`hadwiger_boundary_state_diamond_counterexample.md` realizes precisely
the remaining partition-changing behavior.

Take its parameters

\[
                         r=6,\qquad h=5,
 \qquad q=r-h+2=3.                                \tag{4.1}

Its adhesion consists of a rainbow `K_5`, say
`R=C union {a,b}`, and one portal shadow `p`.  The two original shores
force the two distinct five-block states

\[
                         p=a,\qquad p=b,            \tag{4.2}

while every faithful operation on one shore admits the state forced by
the other.  Operations on both shores admit the six-block fresh state.

Choose the reference partition `Pi` to be the state `p=a`.  Every
faithful operation on that shore changes `Pi` to `p=b`; no operation
preserves the reference partition.  Opposite operation states remain
distinct, and a two-sided operation moves to the third, six-block state.
Thus absolute partition novelty and crossed-state disjointness can coexist
without any return state.

Nevertheless the two original shores have no common state.  Attaching a
four-leaf star through a new hub to the portal shadow gives four distinct
portal representatives with the exact alternating Two Paths obstruction:
both prescribed pair paths use the hub.  The leaves impose no additional
colour restriction, so the transition diamond is unchanged.

This augmented graph is deliberately not seven-connected and is not a
candidate `HC_7` counterexample.  It proves the narrower negative result:

> absolute partition novelty, proper-minor transition states, crossed
> marked-state disjointness, and an actual labelled Two Paths web do not
> by themselves force either a common state or the second protected
> column.

Therefore a valid closure must use the seven-connected full-gate geometry
to break the diamond.  Repeating the finite-state argument without that
geometric step cannot work.

## 5. Remaining high-connectivity theorem

For either web in (3.6) of
`hadwiger_order8_tight_hall_palette_exchange.md`, it is enough to prove:

> In a seven-connected realization of the full exact order-eight gate,
> some internal web edge is either linkage-relevant (its operation supplies
> the second protected column), trace-neutral (contradicting Corollary
> 2.2), or lies behind a separator which descends to the nested exact-seven
> state.

The diamond shows why persistent partition change must be converted into
an actual low-order web separation before high connectivity can be
invoked.  The state algebra alone will not supply the contradiction.
