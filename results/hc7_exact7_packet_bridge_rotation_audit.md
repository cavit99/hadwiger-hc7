# Independent audit: portal-preserving packet-bridge rotation

**Status:** GREEN after two necessary scope corrections: the bridge is
required to lie in the rich open shore, and the replaced open subpath is
required to be nonempty.

## 1. Scope and packet skeleton

The tree rotation in Lemma 2.1 is elementary and does not require the full
counterexample hypotheses.  The support conclusion uses the audited
defect-two reflection theorem and therefore applies only in the hard
exact-seven `(nu_L,nu_R)=(1,2)` cell with two rich-side full packets, a thin
full packet, and the stated contraction-critical hypotheses.

The selected tree is now explicitly inclusion-minimal among trees containing
the chosen portal witnesses.  Consequently every leaf is a selected portal
witness.  If there are `k` distinct selected witnesses, then there are at
most `k-2` unselected vertices of degree at least three.  Thus the skeleton
has at most `2k-2 <= 12` vertices when `k>=2` (and one vertex when `k=1`).
Selected degree-two portal witnesses remain skeleton vertices by definition.
It follows that the segments are genuinely a bounded terminal system, even
though their lengths are unbounded.

The bridge must be a subgraph of the same rich open shore.  Merely requiring
it to be disjoint from the two packet trees would have allowed it to use the
literal boundary or the opposite shore, invalidating the later reflection
interpretation.  The theorem text has been patched accordingly.

## 2. Existence of the rerouting path

Let `x,y` be distinct attachments.  Choose neighbours `x'` and `y'` of
`x,y` in connected `K`, and a path in `K` from `x'` to `y'`; after shortening
if necessary, adjoining the two attachment edges gives a simple `x-y` path
`Q` whose internal vertices all lie in `K`.  This remains true if `x'=y'`.
Other attachments of `K` to the tree and ambient chords do not enter the
chosen subgraph `Q` and cause no problem.

The original statement allowed the internal vertex set `W` of `xTy` to be
empty.  In that case the edge `xy` remains in `T-W`, and adjoining the
alternative path `Q` creates a cycle.  This was a real endpoint exception.
Lemma 2.1 now assumes `W` is nonempty.  Corollary 2.2 is unaffected: among
three distinct attachments on one segment, the middle attachment lies
strictly between the two extreme ones, so their open subpath is nonempty.

## 3. Tree and portal preservation

Because the nonempty open subpath `W` has no skeleton vertex, all its
vertices have degree two in `T`, and no selected portal witness lies in it.
Deleting `W` therefore leaves exactly two tree components, one containing
`x` and one containing `y`.  The path `Q` joins these components, and its
interior is disjoint from the old tree, so

\[
 T'=(T-W)\cup Q
\]

is connected and acyclic.

Every selected witness `p(s)` survives in `T'`, hence `T'` remains
`S`-full.  Its only new vertices lie in `K`, which is disjoint from `P_2`.
Thus `T'` and `P_2` are still disjoint connected full packets.  This argument
does not assume that `x,y` are skeleton vertices; they may be internal
vertices of the same segment.  Ambient chords do not matter because packet
branch sets are allowed to be non-induced connected subgraphs.

## 4. The freed carrier and adaptive reflection

The vertex set `W` induces the old internal path, so it is nonempty and
connected.  It is disjoint from `T'`: the retained old tree omits `W`, and
the replacement path has interior in `K`, which was disjoint from `T`.
It is also disjoint from `P_2`.  Extra ambient edges from `W` to either new
packet do not destroy vertex-disjointness.

If `W` contacts at least five literal vertices of `S`, then its defect has
order at most two.  The correct quantifier order is

```text
geometry determines D(W)
  -> choose the maximal independent block I(H,D(W))
  -> contract I with the opposite thin full packet
  -> receive an arbitrary exact demand-three state
  -> assign that actual state to T', P_2, W.
```

This is exactly Theorem 2.2 of the audited connected-rich carrier package.
No block assignment is fixed before the minor colouring is returned.
Therefore a surviving rotation must indeed satisfy `|N_S(W)| <= 4`.

## 5. Reversibility and edge cases

After the rotation, the freed internal path `W` is a connected packet bridge
of `T'` with attachments `x,y`.  Conversely, every internal vertex of `Q`
has degree two in the tree `T'` and is not a selected portal witness.  The
open `x-y` subpath of `T'` is therefore portal-free, and replacing it by the
old `x-W-y` path restores exactly the original tree `T`.

This remains valid when the original bridge has further attachments to `T`,
when `W` has further ambient attachments after it is freed, or when `Q` has
ambient chords: the rotation is an operation on the explicitly selected
tree and path subgraphs.  Its inverse does not assert that these are induced
subgraphs.

The low-support bound is not needed for algebraic reversibility; it records
why a non-closing rotation survives the defect-two theorem.  Lemma 2.1 does
not prove that a sequence of such rotations terminates, yields a common
state, or has a rural embedding.  Section 3 correctly leaves that global
composition theorem open.
