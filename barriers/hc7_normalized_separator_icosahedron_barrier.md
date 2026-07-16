# Sharp normalized-separator example

**Status:** explicit counterexample to a connectivity-only intermediate
claim, with a deterministic verifier. It is not a counterexample to
`HC_7` or to the singleton-root completion-or-separation target.

## Refuted claim

Seven-connectivity, a spanning singleton-root `K_7`-minus-one-edge model,
and the normalized dominating-model separator produced by the low-colour
absorption theorem do not force that separator to have order five.

## Construction

Let `I` be the icosahedral graph with the labelling used by
`results/hc7_join_near_clique_dichotomy_verify.py`, and put

`G=K_2 join I`,

with universal vertices `p,q`. Take roots `a=0,b=2`. The following is a
spanning `K_7`-minus-one-edge model whose unique missing pair is the first
two singleton branch sets:

`{0}, {2}, {p}, {q}, {1,3,4,5,6}, {7,8}, {9,10,11}`.

In `J=G-{0,2}`, put

`T_1={4}`, `T_2={p,q}`, `T_3={3,6,5}`, `v=11`, `w=10`.

Then

`C=3-6-5-11-10-3`

is the induced neighbourhood cycle of vertex `4`, and
`(T_1,T_2,T_3,{v},{w})` is a normalized dominating `K_5` model. The set

`S=T_2 union V(C)={p,q,3,5,6,10,11}`

has order seven. For the internal root-to-root path `X={8}` coming from
`0-8-2`, the set `S` separates `X` from `T_1` in `J`. In fact `S` itself is
an actual order-seven separator of `G`.

The graph `G` is seven-connected. It is `K_7`-minor-free because `I` is
planar and

`eta(K_2 join I)=2+eta(I)<=6`.

Thus the example realizes the `(7,0)` equality case of the weighted
boundary order

`|S|+|R_E|=7`.

## Missing critical hypothesis

The construction is six-colourable. One four-colouring of `I` has classes

`{0,2,4}`, `{1,3,7}`, `{5,8,10}`, `{6,9,11}`,

and `p,q` receive two fresh colours. In the restriction to `J`, both roots
miss the first colour on their neighbourhoods. Hence the universal
two-root colouring cover forced by strong seven-contraction-criticality is
absent.

The example therefore fixes the trust boundary precisely: the normalized
separator and connectivity can reach weighted order seven, but that is the
permitted terminal separation. Any compression above the terminal value
must use a proper-minor colouring transition, not static domination alone.
