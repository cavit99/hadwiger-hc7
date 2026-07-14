# Independent dependency audit: crossed-hull separating-edge exchange

**Status:** dependency audit, not a proved closure theorem.

## Verdict

The proof chain is sound through the normalized rooted path/`Y`, the bridge
support inequality, and **every clean core edge**.  The formerly live
same-parity defect is now closed by the independently audited atomic
near-full two-carrier exchange.  Consequently the remaining separating-edge
branch is exactly the fully crossed bridge hull, and it is not supplied by
any theorem currently cited in the repository.

The minimum useful new statement is now a **fully crossed carrier-or-rooted-
model lemma**: under the full atomic counterexample hypotheses, if every
edge of `T` is crossed by a literal `T`-bridge, then the thin shore must
contain two literal adjacent connected carriers whose contact lists properly
two-colour the audited frontier, unless the thin closed shore already
contains an `S`-rooted `K_5` model.  The first outcome invokes the audited
two-carrier theorem and six-colours `G`; the second gives a literal `K_7`
with the two rich packets.

Merely restating that lemma is not progress.  A proof still has to produce
the carriers by a literal bridge allocation/rerouting or produce the five
rooted bags.  Humeau--Pous supplies an uncoloured crossing/web certificate
for fixed literal terminals, but not that decoder.  Its web-composition
theorem also does not transport an equality state.  The current
four-terminal rooted-subdivision theorems neither have verified hypotheses
on this hull nor preserve the named duty pairing.

Accordingly, the proposed minimal bridge-hull induction has a valid
framework but two wholly open steps: the label-faithful crossing decoder and
the proper-minor state conversion at a crossless composition node.  Neither
may be cited as a consequence of the literature.

## 1. Exact inherited interface

The separating-edge atom has the following literal data.

1. `G` is seven-connected, `K_7`-minor-free, not six-colourable, and every
   proper minor is six-colourable.
2. There is an actual separation

   \[
     V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
     \qquad S=W\mathbin{\dot\cup}\{u\},\qquad |S|=7,
   \]

   with no `A-R` edge.  The thin shore `A` is connected and `S`-full.
   The rich shore contains two disjoint adjacent connected `S`-full
   packets.  The edge `e=zu`, with `z in A`, is the unique `A-u` edge.
3. Put `H=G[S]`.  The audited frontier is one of the following.

   * `H` is connected and bipartite.  Put `U=emptyset` and `F=H`.
   * `H=K_{1,3} dotunion K_3`.  Retain one legal triangle vertex
     `U={k}`, with `k ne u`, and put
     `F=H-U=K_{1,3} dotunion K_2`.

   In both cases every proper two-list colouring of `F` automatically
   discharges the retained duty.
4. A legally attained final trace on `G[R union S]` has two anticomplete
   equality blocks `B,C` in the unresolved duty.  Let `f` be a literal
   separating edge of their bichromatic connection, with at least one end
   in `R`.  The compressed partition

   \[
                    \Pi_0=\Pi/BC
   \]

   is exactly `I|J` or `I|J|U` and has packet demand at most two.
5. One colouring of `G-f` (equivalently `G/f`) has exact boundary state
   `Pi_0`, equal colours on the ends of `f`, and all five literal `f`-locks.
   Its old-colour lock contains a literal `B-C` subpath with all internal
   vertices in `A`.
6. In a nonsingleton atom, `A-z` is connected and meets every literal in
   `W`.  A replacement `B-C` connector may therefore be chosen with its
   internal path `Q` in `A-z`.  Adjoin a shortest `z-Q` path stopped at its
   first hit.  The resulting fixed core `T` is a literal path or subdivided
   `Y`, and `z` is a leaf.

The last replacement is geometric only.  The new `Q` need not be
bichromatic and need not occur in the colouring carrying `Pi_0` and the
five locks.  Thus `T` does **not** itself carry the localized state.

For every component `D` of `A-T`, with

\[
 X_D=N_T(D),\qquad A_D=N_S(D),
\]

seven-connectivity gives

\[
                         |X_D|+|A_D|\ge 7.             \tag{1.1}
\]

Equality makes `X_D dotunion A_D` an actual seven-boundary.  It does not
attain, inherit, or pull back any equality state.

If `f=xy` is rich-internal, every colouring of the common double
contraction `G/e/f` satisfies

\[
 z\text{ sees all five alternate colours}
 \quad\text{or}\quad
 x,y\text{ each see all five alternate colours}.      \tag{1.2}
\]

The partition induced by this colouring is not known to be `Pi_0`.
Equation (1.2) is unavailable in its present proved form when `f` is a
boundary--rich incidence edge.

## 2. What is already closed

For an edge `h=vw` of `T`, call it clean when no other `T`-bridge has
attachments on both sides of `T-h`.  A clean edge gives a literal partition

\[
                         A=C_1\mathbin{\dot\cup}C_2
\]

into nonempty connected adjacent carriers, each missing at most one
boundary literal.  Their two defects are empty or are distinct singleton
sets.

For `s in V(F)` define the literal contact list

\[
 \Lambda(s)=\{i in \{1,2\}:N_G(s)\cap C_i\ne\varnothing\}.
                                                               \tag{2.1}
\]

The audited exact two-carrier theorem closes whenever `F` has a proper
`Lambda`-list colouring.  Its former sole obstruction was:

* both carriers have singleton defects `p,q`;
* `p,q` lie in the same connected component of `F` and in the same side
  of its bipartition; and
* the two vertices are forced to opposite carrier labels.

The independently audited atomic near-full two-carrier exchange closes that
orientation as well.  In the connected bipartite frontier, contractions of
`X union (I-{p})` and `Y union J` return exactly `I|J` or
`(I-{p})|{p}|J`, both of demand at most two.  In the exceptional frontier,
the two bad defects are claw leaves and the two carriers with the untouched
boundary triangle form an `S`-rooted `K_5`.  Hence **no clean edge survives**.

If every edge of `T` is crossed, every `T` edge lies on a literal cycle in
`A`, so any two vertices of `T` have two edge-disjoint paths in `A`.  This
older conclusion alone did not imply internally vertex-disjoint paths.
The new near-full exchange also proves that the nonsingleton atomic shore
`A` is two-connected, so ordinary vertex Menger now gives two internally
vertex-disjoint paths between any one prescribed pair of `T` vertices.
This is still a one-pair statement: it gives neither a two-pair linkage nor
an assignment of either route to a frontier duty.

Finally, five pairwise disjoint connected pairwise adjacent subgraphs of
`G[A union S]`, each containing a literal member of `S`, are terminal:
the two adjacent `S`-full rich packets complete them to seven literal
`K_7` branch sets.

## 3. Minimum lemma that really closes this branch

The broad four-outcome statement in the active goal is stronger than
necessary for the separating-edge atom.  The following is the minimum
direct closure statement after the proved reductions.

> **Atomic fully crossed carrier-or-rooted-model lemma.**  Assume the full
> interface of Section 1, with `|A|>=2`, and assume every edge of `T` is
> crossed by a literal `T`-bridge.  Then at least one of the following
> holds.
>
> 1. There are disjoint nonempty connected adjacent sets
>    `C_1,C_2 subseteq A` such that every list in (2.1) is nonempty and
>    `F` has a proper `Lambda`-list colouring.
> 2. `G[A union S]` contains five pairwise disjoint connected pairwise
>    adjacent subgraphs, each containing a literal member of `S`.

No partition of all of `A` is required in item 1, and no prescribed
bridge allocation is required.  Those would be unnecessary strengthenings.
No state-pullback conclusion is required either: the audited carrier
contractions manufacture the exact clique-OCT state afresh in the original
graph, and the two full rich packets manufacture the same state on the
opposite side.

Item 1 therefore six-colours `G`.  Item 2 gives a literal `K_7`.  Under
the frozen `K_7`-minor-free hypothesis, item 2 is excluded, so item 1 must
hold.  This closes the normalized nonsingleton separating-edge atom.

This lemma is far narrower than `HC_7`, but it is still the new theorem.
Renaming “failure of item 1” as a web, a gate, or a state exchange does not
prove it.  A successful proof must exhibit the literal carriers/rooted
bags or derive them from one named proper-minor response.

## 4. Requirement/evidence table

| Requirement | Evidence currently available | Audit |
|---|---|---|
| Actual seven-separation, unique edge `zu`, and two adjacent full rich packets | Compulsory-portal bridge composition and its audit | **GREEN** in the atomic `|U|=1` cell. |
| Width-two frontier and legal `I,J,U` convention | Atomic state exchange and its audit | **GREEN**.  In the exceptional frontier `U` is a legal retained triangle vertex and duty is automatic. |
| Final blocking trace with anticomplete blocks `B,C` | Atomic state exchange | **GREEN** as a rich-side colouring; it need not avoid either packet. |
| One literal separating edge `f` | Separating-edge branch of bichromatic localization | **GREEN as a branch hypothesis**, not forced in the two-edge-disjoint alternative. |
| Exact compressed state `Pi_0` on `G-f` and `G/f` | Localization Theorem 2.1 | **GREEN** for rich-internal and boundary--rich `f`.  It is a proper-minor state, not a colouring of `G`. |
| Five locks coexist with `Pi_0` | Localization Corollary 2.2 | **GREEN**.  They may intersect and their five colours are not five boundary labels. |
| Opposite-shore `B-C` connector in that colouring | Localization Theorem 2.3 | **GREEN**.  This original connector may pass through `z`. |
| Connector avoiding `z` and rooted-leaf path/`Y` | Root-deletion normalization and audit | **GREEN for `|A|>=2`**.  The replacement is geometric, not bichromatic. |
| Bridge inequality and exact boundary at equality | Root-deletion normalization, Lemma 4.1 | **GREEN**.  No state, packet vector, or recursive orientation follows. |
| Every clean edge closes | Tree-bridge audit; exact two-carrier theorem; atomic near-full two-carrier exchange and its audit | **GREEN**.  The former same-parity defect is no longer a residue; the atomic shore is also two-connected. |
| Low internal root degree | Atomic low-root-degree closure and audit | **GREEN for connected bipartite frontiers**.  A survivor has `d_{G[A]}(z)>=3`; the exceptional frontier has separate rooted-model residues. |
| Bare cyclic atomic shore | Atomic cycle-shore closure and audit | **GREEN for `G[A]=C_n`, `n>=4`**.  This does not close a cycle torso with outside attachments; the triangle is a separate finite base. |
| Bounded carrier/rooted-model falsification | Atlas/Z3 falsifier on all biconnected thin shapes of orders 3--6, sampling 265 no-near-full-carrier contact states | **YELLOW evidence only**.  Every sample has an exact `S`-rooted `K_5`, but the search omits the full crossed hull and global kernel. |
| Fully crossed hull gives useful routing | Tree-bridge audit, Lemma 5.1; near-full exchange Corollary 3.2 | **GREEN for two internally vertex-disjoint paths joining one prescribed pair**, because `A` is now two-connected.  A two-pair linkage and duty labels remain open. |
| Common double-contraction saturation fork | Double-contraction theorem and audit | **GREEN only when `f` is rich-internal**.  Its boundary state is arbitrary. |
| Five saturated colours give five labelled portal contacts | No source | **RED: hidden palette-to-label lift.** |
| Equality boundary from (1.1) is a recursive state-carrying descent | No source | **RED.**  Legal attainment and the receiving packet vector are missing. |
| A near model is a decreasing `S1/S4` handoff | No source | **RED.**  No receiving normalization/rank is supplied. |
| Humeau--Pous crossing gives literal host paths | Generalised Two Paths Theorem, Theorem 1.5 | **GREEN after fixing pairwise distinct literal terminal occurrences.**  For a tuple longer than four, the crossing pair selected by its indices still requires a duty decoder. |
| Humeau--Pous crossless outcome gives a web | Theorem 1.5 and the paper's web-completion formulation | **GREEN only as a same-vertex edge completion.**  Added edges are not host edges. |
| Recursive parallel composition gives a literal carrier split | Humeau--Pous Proposition 2.10 | **RED as stated.**  The induced gluing path belongs to the completed web; its edges may be added, its length is unbounded, and it carries no state. |
| A host-side parallel split can be used | Humeau--Pous Proposition 4.1 | **YELLOW.**  It applies after a literal path is already known to separate the two frame arcs.  It still gives no boundary state or bounded exact-seven adhesion. |
| A current four-root subdivision theorem supplies the decoder | Hayashi--Kawarabayashi--Yoo, Theorem 1.2 | **RED.**  Its stable-root, relative `<=3`-separation, `2+2` separation, and two-neighbour hypotheses have not been verified for the hull.  Its outputs use some ordering and do not preserve both named duty groups. |
| Earlier rooted topological-minor-on-four-vertices theorem supplies the decoder | Hayashi--Kawarabayashi (2023) | **RED.**  Its terminal fan hypotheses are not established here, and a diamond/rooted `K_4` topology does not itself give the two exact-duty carriers or a rooted `K_5`. |

## 5. Exact audit of Humeau--Pous

Theorem 1.5 says that a crossless tuple of pairwise distinct literal
vertices has a same-vertex **edge completion** to a web with that tuple as
frame.  Conversely, a crossing returned by the theorem consists of literal
vertex-disjoint host paths whose interiors avoid all frame terminals.

This permits two legal uses.

1. A crossing may be decoded if every possible selected pair of tuple
   intervals has separately been proved to yield the two named carriers or
   five rooted bags.
2. In the crossless case, inserted clique cells and the rib order may be
   studied.  Completion edges must first be deleted before any asserted
   path, branch-set adjacency, or portal edge is called literal.

It does not permit the following shortcuts.

* An edge of the frame or a web-composition path may be treated as a host
  edge/path.
* A composition node may be called an actual seven-adhesion merely because
  the completed web splits there.  The shared vertex path can have
  arbitrary order and no attained state.
* A crossing of a six-terminal word such as `A B D A B D` may be assigned
  to a desired pair of duties without a case-complete literal decoder.
* A web side may inherit `Pi_0`.  The theorem is uncoloured and contains no
  proper-minor operation.

Proposition 2.10 proves that every web of frame length at least four is a
web composition along induced frame subpaths.  This is useful as an
induction **index**, but it is not a state transition.  Proposition 4.1 is
closer to the needed host geometry: when a literal path already separates
the two relevant frame arcs, it expresses the host as a parallel
composition.  The missing work is precisely to obtain a bounded literal
interface at that node and attach one legal proper-minor response to it.

Primary source checked online (version 2, 14 August 2025):
[Humeau--Pous, *On the Two Paths Theorem and the Two Disjoint Paths
Problem*](https://arxiv.org/abs/2505.16431).

## 6. Exact audit of rooted-subdivision inputs

The 2025 Hayashi--Kawarabayashi--Yoo theorem assumes four stable roots
`Z`, connected `G-Z`, no separation of order at most three isolating a
nonempty side from all four roots, no order-at-most-two separation placing
two roots on each open side, and at least two off-root neighbours at every
root.  It returns, for **some ordering**, a nondegenerate diamond, a
`K_{2,3}^+` subdivision avoiding one root, or a `K_5^-` subdivision with
two feet.

The relative bridge budget (1.1) does not verify those internal
separation hypotheses for the graph induced by the thin hull and four
chosen terminals.  Boundary support can keep `G` seven-connected while the
thin hull has a one-, two-, or three-vertex internal cut.  Moreover, the
theorem's unspecified ordering may exchange the named duty roles, and a
`K_5^-` subdivision with only two prescribed feet is not an `S`-rooted
`K_5` model.

The earlier Hayashi--Kawarabayashi four-root theorem characterizes the
absence of a diamond under terminal fan hypotheses.  Those hypotheses are
also not established on the hull, and the output is still uncoloured
rooted topology rather than an exact carrier state.

Primary sources checked online:

* [Hayashi--Kawarabayashi--Yoo, *Chasing Tripods to Obtain a Rooted
  Subdivision*](https://doi.org/10.1137/23M157082X), Theorem 1.2;
* [Hayashi--Kawarabayashi, *Rooted topological minors on four
  vertices*](https://doi.org/10.1016/j.jctb.2021.05.002).

No current rooted-subdivision result located in this audit transports an
exact equality partition or turns the five palette locks into five named
boundary-rooted bags.

## 7. Immediate circularity and legality flags

Any continuation must reject the following moves unless the missing
certificate is written explicitly.

1. **State-on-core circularity.**  The normalized `T` was obtained by a
   geometric replacement and need not occur in the `Pi_0` colouring.
2. **Palette-to-label lift.**  Five alternate colours at `z`, `x`, or `y`
   are not five prescribed boundary literals, carrier duties, or disjoint
   bags.
3. **Nonliteral completion edge.**  Web-completion and facial-triangle
   edges are not host edges.  They cannot certify adjacency or
   connectedness of a carrier.
4. **Unproved terminal decoder.**  A crossing gives only its two literal
   paths.  It must be shown that their union with named portions of `T`
   produces disjoint carriers with the recomputed lists (2.1), or five
   disjoint rooted bags.
5. **False state pullback.**  Equality in (1.1) gives an actual
   seven-boundary but no colouring attaining a paired state on it.
6. **Non-decreasing handoff.**  A smaller component `D` does not by itself
   re-enter oriented `(1,2)`: the opposite packets need not be full to the
   new `T`-vertices in the boundary, and no receiving rank is known.
7. **Boundary-incidence overreach.**  The double-contraction fork cannot be
   cited for a boundary--rich `f` in its current proved form.
8. **Rooted-topology overreach.**  A rooted `K_4`, diamond,
   `K_{2,3}^+`, or partially rooted `K_5^-` subdivision is not the five-bag
   `S`-rooted `K_5` terminal of Section 2.

## 8. Audited research decision

The next constructive proof should target the atomic fully crossed
carrier-or-rooted-model lemma, not a broader state-preserving three-gate
pullback.  Clean edges are exhausted, so the proof should spend one
mechanism on the literal crossed hull:

1. use two-connectivity and an `st`-ordering or ear step to expose a
   prefix/suffix carrier cut;
2. reduce failure of every singleton-reservoir return to two disjoint
   parity-bad boundary paths, hence four distinct literal portal labels;
3. prove a literal carrier/rooted-bag decoder for that alternating
   four-portal certificate;
4. in the crossless outcome, use web composition only to locate a literal
   host-side split; the carrier contractions, not the web, manufacture the
   exact state.

The route must be terminated if the crossless recursion generates an
unbounded family of labels or if the only output is an unlabelled web/near
model.  At present there is no legal basis for claiming that the literature
performs step 3 or step 4 automatically.
