# A critical edge produces a doubly saturated rooted-model instance

## Status and proof-spine role

This is a uniform, literal translation of the palette-to-carrier gap.  It
does not assert the false principle that colour saturation alone gives a
rooted clique model.  Instead it identifies exactly what a labelled
rerouting theorem would have to exploit at one critical edge.

For `HC_7`, deleting a critical edge leaves a five-chromatic induced core
with two root sets which are simultaneously saturated in every
five-colouring.  A `K_5` model meeting both root sets in every bag lifts
immediately to a literal `K_7` model.  The accompanying barrier shows that
the converse needs the ambient near-`K_7`, seven-connectivity, or
proper-minor state geometry.

## Theorem 1 (double-saturation reduction)

Let `k>=4`, let `G` be a `k`-chromatic graph, and let `sw` be an edge for
which `G-sw` is `(k-1)`-colourable.  Fix a proper `(k-1)`-colouring `c` of
`G-sw`.  The endpoints `s,w` have one common colour, say `0`.  Let `C_0`
be its colour class and put

\[
                 H=G-C_0,
 \qquad S=N_H(s),\qquad T=N_H(w).                 \tag{1.1}
\]

Then:

1. `chi(H)=k-2`;
2. `chi(H+s)=chi(H+w)=k-1`;
3. in every proper `(k-2)`-colouring of `H`, each of `S` and `T` uses all
   `k-2` colours; and
4. if `H` has a `K_{k-2}` model every branch set of which meets both `S`
   and `T`, then `G` has a `K_k` minor.

### Proof

Restoring `sw` to the fixed colouring forces `c(s)=c(w)`, since otherwise
`c` would colour `G` with `k-1` colours.  The restriction of `c` to `H`
uses at most `k-2` colours.

If `H` had a `(k-3)`-colouring, use it on `H`, give all vertices of
`C_0-{s}` one new colour, and give `s` another new colour.  This is a
proper `(k-1)`-colouring of `G`: the set `C_0` is independent in `G-sw`,
and the only edge of `G` with both ends in `C_0` is `sw`, whose ends now
have different colours.  This contradicts `chi(G)=k`.  Thus
`chi(H)=k-2`.

If `H+s` had a `(k-2)`-colouring, give `C_0-{s}` one fresh colour.  Again
the result is a proper `(k-1)`-colouring of `G`; the restored edge `sw`
joins `s` to a vertex in the fresh colour class.  Hence
`chi(H+s)=k-1`, and the argument for `H+w` is symmetric.

Now take any `(k-2)`-colouring of `H`.  If `S` omitted a colour, give `s`
that colour, contradicting `chi(H+s)=k-1`.  Thus `S` sees every colour;
the same argument applies to `T`.

Finally, let `B_1,...,B_{k-2}` be pairwise disjoint connected pairwise
adjacent branch sets in `H`, each meeting both `S` and `T`.  The
`k` branch sets

\[
                         \{s\},\ \{w\},\ B_1,\ldots,B_{k-2}
\]

are connected and disjoint.  The first two are adjacent through `sw`,
and each is adjacent to every `B_i` through the stipulated root-set
contacts.  They therefore form a literal `K_k` model.  \(\square\)

## Exact remaining use at `k=7`

At `k=7`, the theorem asks for a doubly `(S,T)`-rooted `K_5` model in the
five-chromatic graph `H`.  The state is stronger than one selected
colouring: both root sets meet every colour class in **every**
five-colouring.  It is nevertheless not sufficient by itself; see
`../barriers/hc7_double_saturation_rooted_k5_barrier.md`.

Accordingly, the live proof-spine question is the following restricted
one, not an abstract saturation conjecture:

> When `sw` is the critical pinch edge of an exact near-`K_7` rotation,
> use the five fixed row carriers and the actual adhesion state to turn
> the doubly saturated core into either the doubly rooted `K_5` above, a
> matching opposite-shore state, or the same literal two-apex pair.

