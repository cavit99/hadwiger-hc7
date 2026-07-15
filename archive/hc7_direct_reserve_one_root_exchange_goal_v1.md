# Active goal: direct-reserve one-root exchange

**Status:** retracted draft.  Its proposed near-model lift omitted the fact
that the rich packets need not contact the substituted `z`-bag.  Retained
only to prevent reuse; the active replacement is
`../active/hc7_direct_reserve_substituted_web_goal.md`.

## Decision

The primary task is to close the sole surviving **rural-disk** outcome of
the atomic four-root decoder.  The linkage outcome remains a separate open
child of the parent decoder and is frozen while this narrower exchange is
tested.

This choice follows two new facts.  First, the closed thin shore regenerates
a labelled rooted diamond after one old root is replaced by the compulsory
portal `z`.  Second, exhaustive static augmentation tests show that a fixed
rooted `K_4` plus arbitrary spare portal contacts never forces the required
fifth bag.  The proof must therefore compare regenerated models and their
literal bridges; it cannot be another contact-count lemma.

Proving the target below closes an unbounded rural family by a reusable
root-exchange principle.  It does not by itself prove the linkage branch,
`S1`, or `HC_7`.

## Frozen direct-reserve frame

Use the actual separation

\[
 V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad S=W\mathbin{\dot\cup}\{u\},\qquad |S|=7,
\]

from the atomic four-root goal, with these audited properties.

1. `G` is seven-connected, strongly seven-contraction-critical and
   `K_7`-minor-free; every proper minor is six-colourable.
2. There is no `A-R` edge.  The rich shore `R` contains two disjoint,
   adjacent, connected `S`-full packets.
3. `zu` is the unique `A-u` edge, `|A|>=3`, and `A-z` is connected and
   `W`-full.
4. The two parity-bad boundary paths have four distinct roots.  Exactly one
   is a nontrivial path `P:p--q`; the other is a literal edge `xy`.
5. In the rural disk the original rooted diamond misses the `p-q` pair.
   The path `P` repairs that pair, while `xy` is the sole reserved direct
   connector.

The last description is exact: two direct bad edges cannot occur in the
rural disk, and a literal edge cannot be the missing pair of the rooted
diamond.

## Proved entry move

The direct bad edge satisfies

\[
 x,y\in W,\qquad zx,zy\notin E(G).
\]

Reorienting the same graph as

\[
 A'=A-z,\qquad S'=W\cup\{z\},\qquad R'=R\cup\{u\}
\]

gives a literal seven-separation.  For either choice

\[
 r\in \{p,q\}\cap W,
\]

the audited one-root substitution theorem regenerates in

\[
 G[(A-z)\cup\{z,x,y,r\}]
\]

a `{z,x,y,r}`-rooted `K_4^-` model.  It avoids `u`, the other endpoint of
`P`, and the interior of `P`.

Let

\[
                         D_r=P-r.
\]

Then `D_r` is a nonempty connected literal connector, disjoint from every
bag of the substituted diamond and adjacent to the bag rooted at `r`.
If the other endpoint of `P` is `u`, then `D_r` also contacts the `z`-bag
through the literal edge `uz`.

Sources:

- [closed-shore rooted connectivity](../results/hc7_closed_shore_rooted_connectivity.md)
  and its [audit](../results/hc7_closed_shore_rooted_connectivity_audit.md);
- [reserved-connector near-model theorem](../results/hc7_rural_reserved_connector_near_k7.md)
  and its [audit](../results/hc7_rural_reserved_connector_near_k7_audit.md);
- [one-root substitution](../results/hc7_direct_reserve_one_root_substitution.md)
  and its [audit](../results/hc7_direct_reserve_one_root_substitution_audit.md).

## Reduced certificate and progress signature

For each legal choice of `r`, reduce the four branch sets and a path which
repairs the diamond defect, if such a repair exists, by deleting every
inessential vertex while preserving the four root labels and disjointness
from `D_r`.

Record

\[
                  \mu=(\varepsilon,c,-\ell,-b),
\]

where:

- `epsilon=1` precisely when the missing diamond adjacency is repairable
  without using `D_r`, and is zero otherwise;
- after such a repair, `c` is the number of the four clique-model bags
  literally contacted by `D_r`;
- `ell` is the length of the shortest legal repair; and
- `b` is the total size of the reduced bags and their selected portal
  trees.

Choose the frame and certificate lexicographically maximizing `mu`, after
minimizing the active-shore order.  The signature is finite and literal;
it contains no palette-to-bag identification.

If `epsilon=1` and `c>=2`, the proof has already reached a labelled
near-`K_7`: the repaired four clique bags, `D_r`, and the two rich packets
are seven disjoint connected bags, and the only possible missing pairs are
at most two pairs incident with `D_r`.  Thus they form `K_7^vee`; three or
four contacts upgrade this to `K_7^-` or `K_7` respectively.

## Target theorem

### Direct-reserve one-root exchange theorem

Every lexicographically optimal direct-reserve frame above has at least one
of the following outcomes.

1. **Literal terminal:** a `K_7` model or two adjacent duty-faithful
   carriers to which the audited adaptive return applies, giving a global
   six-colouring.
2. **Normalized near-model handoff:** a repaired substituted diamond with
   `c>=2`, hence the labelled `K_7^vee` centered at `D_r` described above,
   together with its named deficient rows.
3. **Certified equality gate:** an actual seven-adhesion whose receiving
   shore carries either a legally attained reflectable state or a named
   one-/two-hole near-model certificate already accepted by `S1`.
4. **Strict exchange:** a legal bridge rotation or alternative root
   substitution which strictly increases `mu`.

At a globally minimal, lexicographically maximal frame, outcome 4 is
impossible.  Outcomes 1--3 close the rural cell either terminally or by a
literal, already named handoff.  A naked smaller adhesion, an arbitrary
near-`K_7` model, or a changed equality partition is not an allowed
outcome.

## Constructive proof mechanism

The next lemma to prove is a bridge exchange for the whole family of
one-root substitutions, not for one fixed model.

1. Reduce each substituted diamond to four labelled portal trees and expose
   its bridges relative to `D_r`.
2. A bridge meeting two relevant tree segments must either repair the
   missing pair, give `D_r` a second literal contact, or rotate one segment
   to increase `mu`.
3. If every bridge is confined, uncross its attachment intervals.  At most
   six literal gates contradict seven-connectivity.  Equality at seven is
   useful only when the separation is returned with the exact state or
   named near-model certificate required in outcome 3.
4. Apply this to every legal choice of `r`.  When both endpoints of `P` lie
   in `W`, compare the two substitutions: the host of each regenerated
   diamond omits the other old root, so a bridge trapped for one model is
   available as a literal external bridge for the other.  When one endpoint
   is `u`, the sole legal substitution instead starts with the second
   contact from the literal edge `uz`.
5. Use generalized-web composition only to organize a crossless bridge
   system.  A completion edge is never a host edge.  Invoke proper-minor
   colouring only after literal carriers or the certified equality gate
   have been constructed.

This is the precise model-regeneration advantage over the former static
portal programme.

## Falsification boundary

The following shortcuts have been rejected and must not be reintroduced.

- A fixed rooted `K_4` plus spare portal assignments does not force a fifth
  bag: the companion quotient probe has 3,860 surviving path-pair
  assignments and no universally closed instance.
- A blocked rotation need not expose a separator of order at most six;
  seven-connected planar-tube examples preserve a genuine seven-interface.
  Therefore outcome 3 is essential.
- Abstract boundary equality languages do not force rooted clique models.
  Minor-critical transitions and literal rooted folios are indispensable.
- A state-preserving three-gate pullback is not the current target: known
  examples can change the packet vector and destroy the paired state.

Before promoting the exchange theorem, bounded searches must enumerate the
actual regenerated diamonds and their literal bridges, not merely portal
contact masks.  Any unbounded new state alphabet or nontrivial cycle with
constant `mu` terminates this proof mechanism.

## Literature boundary checked online

- Jorgensen's rooted-diamond consequence, as recorded by Norin--Totschnig,
  supplies the regenerated `K_4^-`, but not its fifth bag.
- Fabila-Monroy--Wood characterizes rooted-`K_4` obstructions; it does not
  preserve the reserved connector or its named contacts.
- Humeau--Pous gives crossing/web structure and recursive parallel
  composition, but its completion edges are not literal host edges.
- Kriesell gives an unrooted nonseparating `K_4` subdivision in a
  four-connected graph; the four prescribed roots are not preserved.
- Knittedness and rooted-`C_5` theorems require connectivity well above
  seven in the generic setting.

No located theorem supplies the exchange outright.  The new content must
be the simultaneous, label-faithful comparison of regenerated rooted
diamonds under the exact seven-cut inequalities.

## Success condition

Success requires a complete proof of the target theorem and an independent
audit of every bag, repair path, connector contact, rotation, and separator
order.  A further portal taxonomy, a bare web embedding, or an arbitrary
near-model is not success.
