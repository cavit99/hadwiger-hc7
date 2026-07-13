# Adversarial audit: flat full-host matching dichotomy

## Verdict

**GREEN, strengthened during audit.**

Theorem 2.1 is a correct arbitrary-order colour-or-minor theorem for the
literal two-layer host.  Its alternating-reachability model, homogeneous
type cases, arbitrary optional contacts, and connected-shore lift all
check.  For actual paired carriers, Theorem 2.3 now gives the stronger
minimum-cover rooted completion requested in the research programme: the
branch set containing `a` can be built from one side of the minimum cover
while `{b,c}` remains reserved.

## 1. Colouring branches

If the cross-nonedge graph `M` has a perfect matching, pairing matched
nonadjacent `X,Y` vertices uses `n` carrier colours.  The two fresh colours
on `a,b` and `c` are valid because `ab` is absent.  Optional boundary
contacts cannot spoil this: no carrier uses either fresh colour.

If `nu(M)=n-1`, a maximum matching leaves one vertex in each layer.
Matched pairs use `n-1` colours and the two exposed vertices use distinct
colours, for `n+1` core colours.  When the exposed `X` vertex has type
zero, its forced nonedge to `c` permits `c` to reuse its singleton colour
and `a,b` to use the final fresh colour.  Dually, an exposed type-one `Y`
vertex permits `b` to reuse its colour and `a,c` to share the fresh one.
These are the only reused boundary--core pairs, and both are forced
nonedges, so all optional contacts allowed by the theorem remain safe.

## 2. Co-rank at least two

A minimum vertex cover `C` of `M` has order `nu(M)`.  Its complement in
the two clique layers contains no cross-nonedge and is therefore a literal
clique in the host.  If `nu<=n-2`, this clique has at least `n+2`
vertices.  The connected bag `{b,c}` touches every `X` vertex through
`b` and every `Y` vertex through `c`, yielding `K_{n+3}`.  Extra edges only
help.

## 3. Alternating co-rank-one model

Fix a maximum matching of order `n-1`, start at its unmatched `X` vertex,
and traverse nonmatching edges from `X` to `Y` and matching edges back.
Let the reachable sets be `Z_X,Z_Y`.  Flipping an even alternating path
to any member of `Z_X` leaves that member unmatched, so failure of every
favourable exposed state forces all of `Z_X` to have type one.

The standard Konig cover

\[
 C=(X-Z_X)\cup Z_Y
\]

has order `n-1`; consequently

\[
 K=Z_X\cup(Y-Z_Y)
\]

is a literal clique of order `n+1`.  If all types were one, the unmatched
`Y` vertex would itself be a favourable exposed state.  Thus a type-zero
index `r` exists outside `Z_X`.

The original general-host model is valid:

\[
 A'={a,b,x_r},\qquad C'={c}.
\]

`A'` is connected; it meets `Z_X` through the `X` clique and meets
`Y-Z_Y` through `b` at type zero and `a` at type one.  The vertex `c`
meets all `Y` vertices and all reachable `X` vertices, whose types are
one.  The edge `bc` joins the two extra bags.

## 4. Stronger reserved-connector completion

For literal carriers, every diagonal `x_i y_i` is an actual edge.  This
gives a more faithful rooted model.  Put

\[
 R={a}\cup(X-Z_X),\qquad W={b,c}.
\]

The set `R` is connected because `X-Z_X` is a clique containing the
type-zero vertex `x_r`, which sees `a`.  It meets every member of `Z_X`
through the `X` clique.  For `y_j in Y-Z_Y`:

* if `t_j=1`, the row edge `ay_j` joins it to `R`;
* if `t_j=0`, then `x_j notin Z_X`, and the paired diagonal edge
  `x_jy_j` joins it to `R`.

The reserved bag `W` is connected, universal to the clique `K`, and meets
`R` through `bx_r`.  Thus the singleton bags of `K`, together with
`R,W`, are a `K_{n+3}` model.  This is an exact uniform answer to the
minimum-cover rooted-completion question; there is no two-apex residue in
the literal cell.

The diagonal assumption is sharp.  For type word `0001` and

\[
 E(M)=\{x_0y_0,x_0y_3,x_1y_0,x_1y_1,x_2y_0\},
\]

the matching `x_0y_3,x_1y_1,x_2y_0` has `Z_X={x_3}`, `Z_Y=emptyset`, but
`{a,x_0,x_1,x_2}` misses `y_0`.  The general model using `b` still works.

## 5. Connected shores

Replacing vertices by connected shores preserves the proof whenever the
two labelled families are pairwise adjacent.  A cover complement becomes
a family of pairwise adjacent connected branch sets.  In the corank-one
case, if paired shores `X_i,Y_i` also touch, then

\[
 R={a}\cup\bigcup_{X_i\notin Z_X}X_i
\]

is connected and the diagonal argument above applies shore-for-shore.
Without paired contact, the more general bags `X_r union {a,b}` and
`{c}` remain valid.  The nonminor outcomes are exactly perfect transport
or a maximum transport exposing a type-zero `X` shore or type-one `Y`
shore; an internal carrier theorem is still needed to compose those
states into a colouring.

## 6. Computation

`near_k7_operation_state_dichotomy_probe.py` exhausts all sixteen type
words and all `4096` diagonal-free cross-nonedge relations for `n=4`.  It
now validates both the original model and the reserved-connector model,
and validates every colouring after simultaneously adding all optional
boundary contacts.  It reports:

```text
relations checked: 65536
outcomes: {'perfect-colour': 22896, 'corank-minor': 9616,
           'exposed-colour': 30384, 'alternating-minor': 2640}
```

The verifier also checks the explicit missing-diagonal sharpness example.

