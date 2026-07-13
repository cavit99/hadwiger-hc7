# One-hole models sit strictly above the two-hole centre floor

## Status

This gives the missing global orientation in the branch where a
`K_7^-` minor exists.  Let `mu` be the least deficient-centre order among
all labelled near-`K_7` models with at most two missing centre spokes.  If
`mu>=2`, every one-hole model has centre order at least `mu+1`.

Consequently every minimum-level state is genuinely two-hole, and a
rotation from a minimum two-hole state to a one-hole state strictly raises
centre order.  This does not orient two-hole-to-two-hole single-gate
involutions; those remain the robust web exchange.

## Theorem 1 (one-hole height gap)

Let `G` be `K_7`-minor-free and contain a labelled `K_7^-` model, written
as a missing-star model

\[
                         A,B,F_1,\ldots,F_5,              \tag{1.1}
\]

where the six foreign bags `B,F_1,...,F_5` form a `K_6` model, `A` is
anticomplete to `B`, and `A` meets every `F_i`.

Let

\[
 mu=\min\{|C|:C\text{ is the deficient centre of a labelled model
 with at most two missing centre spokes}\}.              \tag{1.2}
\]

If `mu>=2`, then every one-hole model satisfies

\[
                              |A|\ge mu+1.                \tag{1.3}
\]

### Proof

Among all labelled one-hole models choose one whose deficient centre `A`
has minimum order.  It is enough to show that this minimum is at least
`mu+1`.

For a nonempty proper set `Y subset A` such that both `G[Y]` and
`G[A-Y]` are connected, let

\[
 \Omega_A(Y)=\{i:\text{every }A-F_i\text{ model edge has its
                         }A\text{-end in }Y\}.            \tag{1.4}
\]

Every such detachable set owns at least two of the five required rows.
Indeed, if it owns none, delete it from `A`.  If it owns exactly one row
`F_i`, move it into `F_i`; an edge across `Y|(A-Y)` restores the
centre--`F_i` spoke, while all other required spokes survive in `A-Y`.
The old missing spoke to `B` is unchanged.  Either move gives a smaller
one-hole centre, contrary to the choice of `A`.

Fix a spanning tree of `G[A]`.  Every leaf singleton is detachable, and
monopoly sets of distinct leaves are disjoint.  Since each uses at least
two of only five row labels, the tree has at most two leaves.  If
`|A|>=2`, it has exactly two and is a path.  The same holds for every
spanning tree.  Hence `G[A]` has maximum degree at most two.  A cycle is
impossible, because every singleton of a cycle is detachable and three
vertices would require six disjoint row labels.  Thus `G[A]` is an
induced path.

Let `x,y` be its endpoints.  Their disjoint monopoly sets each have order
at least two and together use at most five labels.  Therefore one endpoint,
say `x`, has monopoly order exactly two:

\[
                         \Omega_A(\{x\})=\{i,j\}.         \tag{1.5}
\]

Delete `x` from the centre and absorb it into `F_i`.  The enlarged row is
connected through an `xF_i` edge, and the endpoint path edge restores its
adjacency to the residual centre `A-x`.  Every required row other than
`F_j` retains a portal in `A-x`; the only missing centre spokes are now
the old row `B` and `F_j`.  Hence this is a labelled `K_7^vee` model with
centre order `|A|-1`.

If the one-hole-minimal centre were a singleton, (1.2) would give
`mu=1`, contrary to the hypothesis.  Thus the path argument applies and

\[
                            mu\le |A|-1,                  \tag{1.6}
\]

which proves (1.3) for the minimum one-hole model and therefore for every
one-hole model. \(\square\)

## Corollary 2 (orientation of mixed rotations)

Assume `mu>=2`.  In the near-model rotation graph:

1. every state with centre order `mu` has exactly two missing spokes;
2. any rotation from such a state to a one-hole state has new centre order
   at least `mu+1`; and
3. the inverse rotation is a strict centre-order descent back toward the
   two-hole floor.

Thus a one-hole state cannot lie on a balanced minimum-level rotation
cycle.  The balanced `K_2`-join-icosahedron example has `mu=1` and is
therefore exactly outside this conclusion.

## Corollary 3 (safe fixed-frame singleton continuation at the floor)

In a target-free single-gate rotation walk at centre level `mu>=2`, let a
singleton gate take a two-hole centre of order `mu` to a one-hole centre.
A second pivot through that enlarged old centre must do one of the
following:

* return through the inverse gate;
* use a nonsingleton gate;
* use a different singleton gate and leave a centre of order `mu`, which
  must have two holes; or
* pivot through another foreign bag, thereby changing the five-row frame.

Indeed, the enlarged old centre has order `mu+1`; removing a different
singleton leaves order `mu`.  Theorem 1 excludes one hole at that order,
and target-freeness excludes zero holes.  This conclusion does not identify
the second singleton with the separately defined endpoint-shadow move;
that identification requires its own portal hypotheses.

This is the appropriate directed supplement to the single-gate involution
theorem: mixed-deficiency edges have a height orientation, while pure
two-hole edges must be quotiented as web exchanges.

## Uniform form

For `s` foreign rows with one old missing spoke and allowance of two, the
same proof works whenever a minimum one-hole path has an endpoint owning
exactly two required rows.  With `s=6`, there are five required rows and
two disjoint endpoint bundles of order at least two, forcing such an
endpoint.  This is the sharp numerical reason for the one-level gap at
`K_7`.
