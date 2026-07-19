# Density closure for a tight single-block shore

**Status:** written proof; audit pending.  This is a consequence of the
single-block outcome in
[`hc7_direct_entry_tight_gallai_shore.md`](hc7_direct_entry_tight_gallai_shore.md).
It reduces that unbounded outcome to an order-seven singleton-side
separation or to a shore of order at most nine.  It does not settle the
remaining bounded shores or the Gallai block-chain outcome, and it does not
prove `HC_7`.

## Theorem 1 (single-block density closure)

Let `G` be a seven-connected graph with no `K_7` minor and let

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad |S|=7,\qquad E_G(L,R)=\varnothing,             \tag{1.1}
\]

where `L,R` are nonempty.  Let `psi` be a six-colouring of a subgraph of
`G` obtained by deleting two specified edges from `S` to `R`, and define

\[
 A(v)=[6]\setminus
 \{\psi(s):s\in N_G(v)\cap S\}.                       \tag{1.2}
\]

Assume that:

1. `G[R]` is connected and not `A`-colourable;
2. `d_{G[R]}(v)=|A(v)|` for every `v in R`;
3. at most four colours occur on `S` under `psi`; and
4. `G[R]` consists of one block.

Then one of the following holds.

1. Some vertex `v in R` has `|N_G(v)|=7`; hence `N_G(v)` is the boundary
   of an actual order-seven separation with singleton open side `{v}`.
2. `G[R]` is a complete graph of order between three and six.
3. `G[R]` is an odd cycle of order at most nine.

### Proof

The degree-choosability theorem applied to the uncolourable degree-sized
list assignment says that the sole block is a complete graph or an odd
cycle.

Suppose first that it is a complete graph of order `r`.  If `r=1`,
tightness gives an empty list, so the sole vertex sees all six colours on
`S`; this is already incompatible with the four-colour boundary hypothesis.
The case `r=2` is excluded exactly as in the endblock argument: a vertex of
internal degree one would have a singleton list and would therefore see five
distinct colours on `S`, although `psi|S` uses at most four.  Thus `r>=3`.
Since `G` has no `K_7` minor, necessarily `r<=6`.  This is outcome 2.

Now let `G[R]` be an odd cycle of order `n`.  Every vertex has internal
degree two.  Tightness and (1.2) imply that every vertex sees exactly four
distinct boundary colours.  Seven-connectivity gives

\[
  7\le d_G(v)=2+|N_G(v)\cap S|,
\]

so every cycle vertex has at least five neighbours in `S`.  If equality
holds for some `v`, then `d_G(v)=7`.  Its full neighbourhood separates the
singleton `{v}` from the nonempty set `L`, proving outcome 1.

It remains to consider the case in which every cycle vertex has at least
six neighbours in `S`.  Choose a component `D` of `G[L]`.  Its neighbourhood
is contained in `S`; seven-connectivity and `|S|=7` imply
`N_G(D)=S`.  Contract `D` to one vertex `ell`, delete the other vertices of
`L`, and retain all vertices in `S union R`.  The resulting minor `H` has
`n+8` vertices.  It contains:

- the `n` cycle edges in `R`;
- the seven edges from `ell` to `S`; and
- at least `6n` edges between `R` and `S`.

Consequently

\[
                         |E(H)|\ge 7n+7.               \tag{1.3}
\]

The sharp Mader edge bound for `K_7` minors gives

\[
 |E(H)|\le 5|V(H)|-15=5n+25.                          \tag{1.4}
\]

Combining (1.3) and (1.4) yields `2n<=18`, hence `n<=9`.  This is outcome
3.  \(\square\)

## Trust boundary

The density argument is host-level and applies to odd cycles of arbitrary
length; it is not a finite-search inference.  The residual odd cycles have
orders `3,5,7,9` (with the triangle already covered by the complete-graph
outcome).  The theorem does not assert that the order-seven separation has
compatible proper colourings on its two closed sides.  It also says nothing
about the unbounded path of Gallai blocks left by the preceding theorem.

## External input

The extremal inequality used above is W. Mader,
*Homomorphiesätze für Graphen*, Math. Ann. **178** (1968), 154--168:
for `p<=7`, a simple `K_p`-minor-free graph on `N` vertices has at most
`(p-2)N-binom(p-1,2)` edges.  Its `p=7` instance is `5N-15`.
