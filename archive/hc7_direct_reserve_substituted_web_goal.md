# Parent target: direct-reserve substituted-web decoder

**Status:** open parent target.  Its gate geometry is discharged to the
[literal normal-form programme](hc7_literal_first_c_reduction_lift_goal.md);
the immediate child is the
[twin-seam double-lock exchange](hc7_atomic_twin_seam_double_lock_exchange_goal.md).

## Strategic decision

This file records the sole surviving **rural-disk** parent of the
atomic four-root decoder.  It is now a clean rooted-web exchange problem,
not a general equality-state pullback and not a static portal census.

The linkage child of the parent decoder remains open but is frozen during
this attempt.  Proving the double-lock theorem closes the symmetric rural
gate family and returns it either terminally or through a genuinely ranked
near-`K_7`/exact-seven interface.  It does not by itself prove `HC_7`.

## Frozen direct-reserve frame

Use the actual separation

\[
 V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad S=W\mathbin{\dot\cup}\{u\},\qquad |S|=7,
\]

with these audited properties.

1. `G` is seven-connected, strongly seven-contraction-critical and
   `K_7`-minor-free; every proper minor is six-colourable.
2. There is no `A-R` edge.  The rich shore `R` contains two disjoint,
   adjacent, connected `S`-full packets.
3. `zu` is the unique `A-u` edge, `|A|>=3`, and `A-z` is connected and
   `W`-full.
4. The parity obstruction consists of one nontrivial boundary path
   `P:p--q` and one literal boundary edge `xy`, with four distinct ends.
5. The original rural diamond misses the `p-q` pair.  The path `P` repairs
   it; `xy` is the sole direct reserve.

The direct edge satisfies

\[
                       x,y\in W,\qquad zx,zy\notin E(G).
\]

For every legal endpoint `r in {p,q} cap W`, reorienting the same graph as

\[
 A'=A-z,qquad S'=W\cup\{z\},\qquad R'=R\cup\{u\}
\]

is a literal seven-separation.  The one-root substitution theorem gives a
`{z,x,y,r}`-rooted `K_4^-` in

\[
                         J_r=G[A\cup\{x,y,r\}]
\]

which avoids the other old root and the interior of `P`.

## New obstruction theorem

The substituted host has only two possibilities:

1. `J_r` contains a literal `{z,x,y,r}`-rooted `K_4`; or
2. the literal graph `J_r` has a planar embedding with `z,x,y,r` on one
   face.

This follows from the full Fabila-Monroy--Wood rooted-`K_4`
characterisation.  Rooted internal four-connectivity removes every fill
clique, the direct edge `xy` and the degree of `z` remove obstruction
classes `A,B,C,E,F`, and only the clean class-`D` web remains.  Completion
edges and fill vertices are not host objects.

Sources:

- [closed-shore rooted connectivity](../results/hc7_closed_shore_rooted_connectivity.md)
  and [audit](../results/hc7_closed_shore_rooted_connectivity_audit.md);
- [reserved-connector near-model theorem](../results/hc7_rural_reserved_connector_near_k7.md)
  and [audit](../results/hc7_rural_reserved_connector_near_k7_audit.md);
- [one-root substitution](../results/hc7_direct_reserve_one_root_substitution.md)
  and [audit](../results/hc7_direct_reserve_one_root_substitution_audit.md);
- [exact substituted-host obstruction](../results/hc7_direct_reserve_rooted_k4_obstruction.md)
  and [audit](../results/hc7_direct_reserve_rooted_k4_obstruction_audit.md).

## Exact labelled output

The useful near-model certificate must repair two distinct deficiencies:
the substituted diamond may be missing one adjacency, and its `z`-rooted
bag lies in `A`, so the two `R`-packets need not contact it.

An **anchored five-bag certificate** consists of:

- a repaired `{z,x,y,r}`-rooted `K_4` model with bags
  `B_z,B_x,B_y,B_r`;
- two disjoint nonempty connected sets `D,C`, disjoint from those bags;
- each of `D,C` contains a literal vertex of `S`;
- `D` is adjacent to `B_z`; and
- `C` is adjacent to at least two of
  `B_z union D,B_x,B_y,B_r`.

After replacing `B_z` by `B_z union D`, the four clique bags, `C`, and the
two rich packets form a labelled `K_7^vee`: packet fullness supplies every
packet edge to the five `S`-meeting bags, and the only possible missing
pairs are at most two pairs incident with `C`.  Three or four contacts from
`C` upgrade this to `K_7^-` or `K_7`.

The component of `G[S-{x,y,r}]` containing `u` is always a disjoint
connected candidate contacting `B_z` through `uz` and at least one of the
three other rooted bags.  This is not yet the whole certificate: using it
as `C` still requires a disjoint `S`-anchor `D` for `B_z`, while using it as
`D` still requires a separate two-contact connector.

## Target theorem

### Direct-reserve substituted-web decoder

Every frozen direct-reserve frame has at least one of the following literal
outcomes.

1. **Terminal:** a `K_7` model or two adjacent duty-faithful carriers to
   which the audited adaptive return applies, giving a global
   six-colouring.
2. **Anchored near-model:** an anchored five-bag certificate, hence the
   labelled `K_7^vee` above with its named deficient centre and rows.
3. **Certified equality gate:** an actual seven-adhesion whose receiving
   shore carries either a legally attained reflectable state or a named
   one-/two-hole near-model certificate already accepted by `S1`.

A clean disk, a smaller naked adhesion, a changed boundary partition, or an
arbitrary unlabelled near-model is not an outcome.

## Constructive mechanism

Choose the direct-reserve frame with minimum active-shore order.  Among all
legal root substitutions, rooted models and reduced portal trees, maximize
lexicographically:

1. whether the rooted-diamond defect is repaired without using the proposed
   anchor/connector;
2. whether the `z`-bag has a disjoint `S`-anchor;
3. the number of repaired bags contacted by the remaining connector; and
4. the negative total size of the repair and reduced portal trees.

Then prove a **crossing-or-return exchange**.

1. A bridge crossing the four-root facial order must decode into a rooted
   `K_4` repair, the missing anchor/connector contact, or two literal
   adaptive carriers.
2. If every bridge is confined, use the recursive parallel composition of
   the clean web to find the first composition seam separating an omitted
   `W`-portal from its duty.
3. A seam of lifted order at most six contradicts seven-connectivity.  At
   order seven it is useful only if the boundary map includes the exact
   receiving state or named near-model required in outcome 3.
4. Compare every legal choice of `r`.  A bridge internal to one substituted
   web can become an omitted-root bridge for another.  If one endpoint of
   `P` is `u`, the edge `uz` supplies the compulsory anchor side and the
   proof must split the remaining connector instead.
5. Every nonterminal rerouting must strictly improve the declared finite
   signature.  A reversible cycle with constant signature falsifies this
   mechanism.

Humeau--Pous web composition is used only to organize the crossless system;
its completion edges are never treated as literal edges.  Proper-minor
colouring is invoked only after literal carriers or the certified equality
gate have been constructed.

## Adversarial boundary

The following failures are now explicit.

- A rooted `K_4^-`, direct `xy`, nontrivial bad path, unique `zu`, full
  `A-z`, all relative seven-cut inequalities, and a connector with two
  contacts still need not give a rooted `K_4`.  The solver-free
  [clean-web barrier](../barriers/hc7_direct_reserve_rooted_k4_web_barrier.md)
  and its [independent audit](../barriers/hc7_direct_reserve_rooted_k4_web_barrier_audit.md)
  verify such a host.  It already exits through adaptive carriers, so it
  supports the crossing-or-return theorem while refuting the rooted-`K_4`
  shortcut.
- A fixed rooted `K_4` plus arbitrary portal assignments does not force a
  fifth bag: all 3,860 path-pair assignments survive the static quotient
  probe.
- The two rich packets are `S`-full, but `z notin S` and there is no `A-R`
  edge.  They do **not** automatically contact the substituted `z`-bag.
- A blocked rotation need not give a cut of order at most six; a genuine
  exact-seven interface may persist.  That interface must carry receiving
  data.
- Boundary colour-extension language alone cannot force the rooted model.
  Literal bridges and the universal proper-minor response are essential.

## Literature decision

The online review located no theorem which supplies this decoder.

- Fabila-Monroy--Wood gives the exact six-class rooted-`K_4` obstruction;
  it is used to reduce the negative branch to one clean cofacial web.
- Humeau--Pous gives a constructive crossing/web dichotomy and recursive
  parallel composition, but no packet labels or exact colour-state transfer.
- Norin--Totschnig records the rooted-diamond consequence used at entry.
- Kriesell's nonseparating `K_4` subdivision does not preserve four roots.
- Generic knittedness and rooted-`C_5` results require connectivity well
  above seven here.
- Dvorak--Swart shows why an abstract boundary-colouring language is too
  flexible to replace the literal exchange.

Thus the selected theorem is a genuinely new uniform rooted-model
principle, but confined to the exact direct-reserve atom rather than a
restatement of `HC_7`.

## Success condition

Success requires a complete proof of all three target outcomes and an
independent audit of every branch set, packet adjacency, anchor/connector
split, web seam and lifted separator order.  Further labelled casework or a
bare cofacial embedding is not success.
