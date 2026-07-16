# Residual-component contacts in the mixed-shore support-six model

**Status:** written proof with a separate GREEN internal audit in
[`hc7_mixed_shore_component_contacts_audit.md`](hc7_mixed_shore_component_contacts_audit.md).
This theorem uses the normalized mixed-shore model from the boundary-anchor
completion theorem.  It eliminates every component of the opposite shore
which retains all required boundary contacts, and otherwise returns an
actual order-seven separation or an exact one-missing-contact form.  It does
not prove `HC_7`.

## Theorem 1.1

Let `G` be a seven-connected graph.  Let `S` be an eight-vertex separator
such that `G-S` has exactly two components `U,V`, and suppose every vertex
of `S` has a neighbour in each component.  Let `s\in S` be adjacent to
every vertex of `S-\{s\}`, and let `x\in S-\{s\}`.

Suppose `G-\{s,x\}` has a support-six `K_5`-minor model with branch sets

\[
       \{u_1\},\ldots,\{u_h\},
       \quad\{w_1\},\ldots,\{w_{4-h}\},
       \quad\{v,t\},                                   \tag{1.1}
\]

where

\[
       h\in\{2,3\},\quad u_i\in U,\quad v\in V,\quad
       t,w_j\in S-\{s,x\}.                             \tag{1.2}
\]

Let

\[
                   F_0=\{s,t,w_1,\ldots,w_{4-h}\}.    \tag{1.3}
\]

For every component `C` of `V-v`, at least one of the following holds.

1. `G` contains a `K_7` minor.
2. `N_G(C)` is the separator of an actual order-seven separation.
3. `C` is adjacent to exactly seven vertices of `S`, and the unique vertex
   of `S` not adjacent to `C` belongs to `F_0`.

Consequently, if `G` is `K_7`-minor-free and has no actual order-seven
separation, every component of `V-v` has exactly one missing boundary
contact, and that missing vertex is one of the boundary vertices already
needed by the five model branch sets or the universal vertex `s`.

### Proof

Fix a component `C` of `V-v`.  Since `V` is connected, `C` has a neighbour
at `v`.  It has no neighbour in `U` or in another component of `V-v`, and
therefore

\[
                       N_G(C)=\{v\}\cup N_S(C).        \tag{1.4}
\]

Seven-connectivity gives

\[
                              |N_S(C)|\ge6.             \tag{1.5}
\]

If equality holds, (1.4) is a separator of order seven.  Both open sides
are nonempty: one contains `C`, while the other contains `U`.  Thus outcome
2 holds.

We next prove that

\[
                         F_0\subseteq N_S(C)            \tag{1.6}
\]

implies outcome 1.  Let `A=\{u_1,\ldots,u_h\}` and delete

\[
        Z=\bigl(\{u_1,\ldots,u_h,w_1,\ldots,w_{4-h},v,t\}
                    -A\bigr)\cup\{s\}.                \tag{1.7}
\]

The displayed model has six support vertices, so

\[
                              |Z|=7-h.                  \tag{1.8}
\]

Put `T=N_S(C)-F_0`.  Under (1.5)--(1.6),

\[
       |T|\ge6-|F_0|=6-(6-h)=h.                        \tag{1.9}
\]

There are `h` pairwise vertex-disjoint `A`--`T` paths in `G-Z`.  Indeed,
otherwise Menger's theorem supplies an `A`--`T` separator `X` of order at
most `h-1`; at least one vertex remains on each side, and

\[
                  |Z\cup X|\le(7-h)+(h-1)=6,
\]

contradicting seven-connectivity.

Stop each path on its first visit to `T`.  No initial segment so obtained
meets `C`.  Indeed, a path starting in `U` can enter `C` only through a
vertex of `N_G(C)=\{v\}\cup N_S(C)`.  The vertex `v` and all vertices of
`F_0` are deleted in `Z`, while every vertex of `N_S(C)-F_0` belongs to
`T`; hence the path encounters its terminal before it can enter `C`.

Enlarge each singleton branch set `\{u_i\}` along its path to its distinct
terminal in `T`.  The five model branch sets remain connected, pairwise
disjoint, pairwise adjacent, and disjoint from `C`.  Every one is now
adjacent to `C`: the enlarged `U` branch sets through their terminals in
`T`, and the other branch sets through `t,w_j\in F_0`.  Every model branch
set is also adjacent to `s` through a boundary vertex on it, while `C` is
adjacent to `s` by (1.6).  Hence the five enlarged model branch sets,
`C`, and `\{s\}` form an explicit `K_7`-minor model.  This proves the
implication (1.6) `=>` outcome 1.

It remains to suppose outcomes 1 and 2 both fail.  Equation (1.5) and the
failure of outcome 2 give `|N_S(C)|\ge7`.  If `|N_S(C)|=8`, then (1.6)
holds and outcome 1 follows.  If `|N_S(C)|=7` but the unique missed
boundary vertex lies outside `F_0`, then (1.6) again holds.  The only
remaining possibility is outcome 3.  \(\square\)

## Exact contribution and limitation

This theorem turns the unstructured graph `V-v` into an exact alternative.
At contact order six it gives a genuine order-seven separation.  Above that
threshold, every component either completes the labelled model or misses
exactly one of the few boundary vertices whose contact is indispensable.

It does not align the missing vertex across different components, show that
`V-v` is connected, or handle the case `V=\{v\}`.  Those are the remaining
opposite-shore composition questions.  A next exchange theorem must use the
fact that different components are all joined through `v`, together with
the three exact defect patterns of the mixed-shore model; merely counting
their seven boundary contacts cannot distinguish the possible missed
vertices.
