# Double-forced vertices create a two-block boundary-state jump

## Status

This is the exact proper-minor transition supplied by the audited
double-singleton rural state.  It is uniform in the palette size.  It
does not yet force a collision with an operation in the opposite shore.

## Theorem 1 (two-block state exclusion)

Let `G` be proper-minor-minimal non-`q`-colourable.  Let `K` be a
connected vertex set, put `S=N_G(K)`, and let `c` be a `q`-colouring of
the proper total contraction `G/K`.  Write `z` for the contraction image
and `alpha=c(z)`.

Suppose distinct vertices `x,y in K` each have boundary neighbours in
all `q-1` colours different from `alpha`:

\[
 c(N_G(x)\cap S)=c(N_G(y)\cap S)
                =\{1,\ldots,q\}-\{\alpha\}.             \tag{1.1}
\]

Let `K=X dotunion Y` be any partition into nonempty connected sets with
an `XY` edge, where `x in X`, `y in Y`, and at least one of `X,Y` has
order at least two.  Contract `X` and `Y` separately, obtaining adjacent
vertices `a,b` in a proper minor `M` of `G`.

Then `M` is `q`-colourable, but no `q`-colouring of `M` induces on the
labelled boundary `S` the same equality partition as `c`.

### Proof

The separate contractions perform at least one edge contraction, so `M`
is a proper minor and has a `q`-colouring.

The vertices in `N_G(x) cap S` witness all `q-1` non-`alpha` colour
blocks of `c|S`; no member of `S` has colour `alpha`, because every
member is adjacent to `z`.  Hence `c|S` has exactly `q-1` equality
blocks.  The same is witnessed at `y`.

Suppose a `q`-colouring `d` of `M` induced the same labelled equality
partition on `S`.  Permute its palette so that `d` and `c` agree on
`S`.  The contracted vertex `a` is adjacent to the old boundary
neighbours of `x`, one in each of the `q-1` colours other than `alpha`.
Thus `d(a)=alpha`.  Similarly `d(b)=alpha`.  But `a,b` are adjacent
through an old `XY` edge, contradicting properness of `d`.  \(\square\)

### Corollary 2 (all tree cuts on a forced pair jump state)

Let `T` be a spanning tree of `K`.  Every edge on the `x-y` path of `T`
whose deletion has a side of order at least two gives, by contracting its
two tree sides, a proper two-block minor whose boundary-state family
excludes the total-contraction partition of `c`.

The theorem is stronger than saying that `c|_{G-K}` itself does not
extend: even recolouring the two contracted blocks cannot preserve the
old labelled boundary partition.

## Exact missing composition

All cuts in Corollary 2 are operations on the same side of the adhesion.
State exclusion alone does not produce a six-colouring.  A terminating
argument must still do one of the following:

1. produce the old partition from a proper operation in the opposite
   open shore and apply the audited crossed-state splice;
2. use two nested cuts to colour complementary uncontracted parts and
   glue across an actual internal separator; or
3. show that persistent avoidance of the old partition is precisely one
   globally compatible rural expansion.

Extra edges between the two tree sides are harmless for Theorem 1 but
make option 2 nontrivial; contracting the sides does not turn those edges
into a one-edge adhesion in the original graph.
