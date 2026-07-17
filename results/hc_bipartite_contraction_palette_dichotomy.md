# Palette dichotomy after contracting an induced bipartite subgraph

**Status:** written proof; separate internal audit GREEN.

This note proves a uniform colouring-space lemma.  Its hypotheses concern a
minor-minimal `k`-chromatic graph and an induced connected bipartite
subgraph.  The conclusion is a bichromatic rotation or a literal graph
separation.  It does not by itself construct a clique minor.

## 1. Statement

Let `k >= 3`, and let `G` be a `k`-chromatic graph such that every proper
minor of `G` is `(k-1)`-colourable.  Let

\[
                  Q=G[W]
\]

be a connected bipartite induced subgraph with at least two vertices and
fixed bipartition `(A,B)`.  Thus `A` and `B` are both nonempty independent
sets.  Contract all of `Q` to one vertex `q`, and put

\[
                  R=G-W.
\]

### Theorem 1.1 (contraction palette and common support)

The following assertions hold.

1. `chi(G/Q)=k-1`.
2. Let `psi` be any proper `(k-1)`-colouring of `G/Q`, and put
   `gamma=psi(q)`.  For every other colour `delta`, each of the two sets
   `A,B` has a neighbour in `R` coloured `delta`.
3. Fix `delta != gamma`.  In the subgraph

   \[
       R[\psi^{-1}(\{\gamma,\delta\})],                 \tag{1.1}
   \]

   at least one component contains a `delta`-coloured neighbour of `A`
   and a `delta`-coloured neighbour of `B`.

Here and below, saying that `A` has a neighbour means that some vertex of
`A` has such a neighbour.  No assertion is made about every individual
vertex of `A` or `B`.

For the fixed colour `delta`, let `C_delta` be the set of components of
(1.1) which contain a `delta`-coloured neighbour of at least one of
`A,B`.  Call a member of `C_delta` **common** if it contains such a
neighbour of both sides.

### Theorem 1.2 (concentrated/diffuse support dichotomy)

Exactly one of the following alternatives holds.

1. **Concentrated support.**  The set `C_delta` consists of a single
   common component `K_delta`.  Interchanging `gamma` and `delta` on
   `K_delta`, and changing the colour of the contracted vertex `q` from
   `gamma` to `delta`, gives another proper `(k-1)`-colouring of `G/Q`.
   In that colouring, `delta` is the unique colour absent from the
   external neighbourhood of each of `A,B`, while every other colour
   occurs in both external neighbourhoods.

   Moreover, for every colour

   \[
                  theta notin \{gamma,delta\},
   \]

   some vertex of `K_delta` coloured `delta` in the original colouring
   `psi` has a `theta`-coloured neighbour in `R-K_delta`.

2. **Diffuse support.**  There is a common component `K` and a distinct
   member of `C_delta`.  Then `N_G(K)` is the boundary of the actual
   vertex-set separation `(X,Y)` given by

   \[
       X=K\cup N_G(K),\qquad Y=V(G)-K,                 \tag{1.2}
   \]

   whose two open sides are nonempty.  Write
   `N_R(K)=N_G(K) cap R` and `N_Q(K)=N_G(K) cap W`.  More precisely,

   \[
       N_G(K)=N_R(K)\mathbin{\dot\cup}N_Q(K),           \tag{1.3}
   \]

   where every vertex of `N_R(K)` has a colour outside
   `{gamma,delta}`, the set `N_Q(K)` meets both `A` and `B`, and every
   edge from `Q` to `K` ends on the `delta`-coloured side of `K`.

   Consequently, if `G` is `ell`-connected, then

   \[
                         |N_G(K)| >= ell.              \tag{1.4}
   \]

The dichotomy is exhaustive because Theorem 1.1 supplies a common
component: either it is the only member of `C_delta`, or another support
component exists.

## 2. Proof of the palette assertions

Because `Q` is connected and has at least two vertices, contracting it to
`q` produces a proper minor.  Hence

\[
                         \chi(G/Q)\le k-1.             \tag{2.1}
\]

Suppose that `G/Q` had a colouring with at most `k-2` colours, and let
`gamma` be the colour of `q`.  Restrict this colouring to `R`.  No vertex
of `R` adjacent to `Q` has colour `gamma`.  Give every vertex of `A` the
colour `gamma`, and give every vertex of `B` one new colour.  The induced
subgraph `G[W]` is bipartite with bipartition `(A,B)`, so this is a proper
colouring of `G` with at most `k-1` colours, a contradiction.  Together
with (2.1), this proves Theorem 1.1(1).

Now fix a proper `(k-1)`-colouring `psi` of `G/Q` and write
`gamma=psi(q)`.  Again, no external neighbour of `Q` has colour `gamma`.
Suppose, for example, that `A` had no external neighbour of some colour
`delta != gamma`.  On `R`, keep the colouring `psi`; give all of `A`
colour `delta` and all of `B` colour `gamma`.  There is no monochromatic
edge from `A` to `R` by the assumption, none from `B` to `R` because the
contracted vertex had colour `gamma`, and every edge of `G[W]` joins
`A` to `B`.  This is a `(k-1)`-colouring of `G`, a contradiction.  The
same argument with `A,B` interchanged proves Theorem 1.1(2).

Fix `delta != gamma`.  Suppose that no component of (1.1) is common.
Interchange `gamma,delta` on the union of all components which contain a
`delta`-coloured neighbour of `A`.  After this Kempe change, `A` has no
external neighbour of colour `delta`: all its old `delta`-neighbours were
changed, and it originally had no `gamma`-neighbour.  The set `B` has no
external neighbour of colour `gamma`: it originally had none, and no
switched component contains a `delta`-neighbour of `B`, by the assumed
absence of a common component.  Colouring `A` with `delta` and `B` with
`gamma` now extends the changed colouring of `R` to a `(k-1)`-colouring
of `G`, a contradiction.  This proves Theorem 1.1(3).

## 3. Proof of the dichotomy

Assume first that `C_delta={K_delta}`.  Every `delta`-coloured external
neighbour of either side lies in `K_delta`, and no external neighbour of
either side has colour `gamma`.  Interchange `gamma,delta` on
`K_delta`.  Both sides now have an external neighbour of colour `gamma`
because `K_delta` is common, and neither has one of colour `delta`.
Changing `q` from `gamma` to `delta` therefore gives a proper colouring
of `G/Q`.  The other colours were not changed and occur in the external
neighbourhood of both sides by Theorem 1.1(2).  This proves the rotation
assertion.

Let `theta` be outside `{gamma,delta}`.  Suppose that no
`delta`-coloured vertex of `K_delta` has a `theta`-coloured neighbour in
`R`.  Recolour every `delta`-coloured vertex of `K_delta` with `theta`.
This remains proper: the recoloured vertices form an independent set and
none has a neighbour of its new colour.  All `delta`-coloured neighbours
of `Q` have now disappeared, while `Q` still has no external
`gamma`-neighbour.  Colour `A` with `gamma` and `B` with `delta`.  This
again gives a `(k-1)`-colouring of `G`, a contradiction.  Thus the stated
`theta`-contact exists.  It lies in `R-K_delta`, since `K_delta` uses only
`gamma,delta`.

Now let `K` be a common member of `C_delta`, and suppose that a distinct
member `K'` of `C_delta` exists.  Choose a `delta`-coloured external
neighbour `x` of `A` or `B` in `K'`.  Distinct components of (1.1) are
anticomplete, so

\[
                         x notin K\cup N_G(K).         \tag{3.1}
\]

The component `K` is nonempty and connected, and all its neighbours lie
in `N_G(K)`.  Therefore (1.2) is a separation with nonempty open sides:
one contains `K`, and the other contains `x`.

Every neighbour of `K` in `R` has a colour outside `{gamma,delta}`;
otherwise it would belong to the same component of (1.1).  No vertex of
`Q` is adjacent to a `gamma`-coloured vertex of `R`, because `q` has
colour `gamma` in `G/Q`.  Hence every edge from `Q` to `K` ends at a
`delta`-coloured vertex.  Finally, commonness says precisely that
`N_Q(K)` meets both `A` and `B`.  This proves (1.3) and all the stated
colour structure.  The connectivity bound (1.4) is immediate.

## 4. A useful one-sided refinement

The support families met by `A` and `B` need not be identical.  Suppose a
component `L` of (1.1) contains a `delta`-neighbour of `A` but none of
`B`.  Then `A` must have a `delta`-neighbour in another bichromatic
component.  Indeed, otherwise switching `gamma,delta` on `L`, colouring
`A` with `delta`, and colouring `B` with `gamma` would `(k-1)`-colour
`G`.  It follows, exactly as above, that `N_G(L)` is an actual separator.
Here

\[
                  \varnothing\ne N_Q(L)\subseteq A,
\]

every member of `N_R(L)` has a colour outside `{gamma,delta}`, and the
opposite open side contains the second support component.  The symmetric
statement holds with `A,B` interchanged.

## 5. Sharp hypotheses and small cases

The nontriviality of `Q` is essential.  If `Q` is a singleton, then
`G/Q=G` and its chromatic number is `k`, not `k-1`.

The induced-bipartite requirement is also essential in exactly the place
where the colouring is expanded from `R` to `Q`.  It can be weakened to:
`G[W]` is bipartite with the displayed bipartition, while `Q` is any
connected spanning subgraph of `G[W]`.  It cannot be replaced merely by
the assertion that some connected bipartite subgraph on `W` has been
selected.  For example, in `G=K_k`, take a three-vertex path as a
non-induced bipartite subgraph.  Contracting its three vertices produces
`K_{k-2}`, not a graph of chromatic number `k-1`.

When `Q` is one edge, `A` and `B` are singletons and the theorem is exactly
the adjacent-pair palette/support dichotomy.  For `k=2`, the only relevant
minor-minimal graph is `K_2`; contracting its unique edge gives `K_1`, and
there is no second palette colour to which the support assertions apply.
The restriction `k>=3` avoids this vacuous exceptional case.

## 6. Label-preserving use inside a clique-minor branch set

Let `(F_1,...,F_m)` be a labelled clique-minor model and suppose that
`Q` lies inside one branch set `F_i`.  Contracting `Q` does not merge two
model labels: the image of `F_i` is still connected, every adjacency from
`F_i` to another branch set survives, and all other labelled branch sets
are unchanged.  Thus the contraction, and every palette rotation in
Theorem 1.2, are label-preserving at the level of the existing unsplit
model.

The two bipartition classes retain additional, literal attachment data:
the common bichromatic component in Theorem 1.1 is adjacent to both `A`
and `B`, while the diffuse alternative records the exact vertices of `Q`
in the separator.  This can be used as input to a later branch-set
rerouting or split theorem without forgetting which original model branch
set was contracted.

There is an important limit.  Neither `A` nor `B` need be connected, and
the common bichromatic component may intersect several existing branch
sets.  The theorem therefore does not itself split `F_i` into two valid
branch sets, preserve all prescribed branch-set adjacencies after such a
split, or produce a larger clique minor.  Those are separate labelled
routing obligations.
