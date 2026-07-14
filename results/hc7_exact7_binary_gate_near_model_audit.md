# Independent audit: binary two-gates force a labelled near model

**Verdict:** GREEN, with one non-substantive proof-order clarification.

**Audited source:**
`results/hc7_exact7_binary_gate_near_model.md`

**Source SHA-256:**
The mathematical body audited before promotion had SHA-256
`d2156727f58df4343bd0f2cc7d430a9f294f2b1ea7d38aed9b1f1eeb6df81352`.
Promotion changed only the status line and file location; the promoted source
hash is
`b1dce70c3b0b5c607828daf3ffd8364a6ccc2c8b5ef43e9a6effa46b6a28e33a`.

The audit checks the two incidence lemmas, every displayed branch-set
adjacency in Theorem 2.1, and the use of seven-connectivity and the prior
low-internal-degree handoff in Theorem 3.1.  It treats `K_7^vee` only as
a labelled near-model handoff, not as a `K_7` contradiction.

## 1. Lemma 1.1

Assume that `C` is independent and that no repairable edge exists.  After
contracting the components of `T-C`, the incidence graph `B` is indeed a
bipartite tree.  At a component `K`, different `C-K` incidence edges have
different endpoints in `K`: otherwise one endpoint would have two
neighbours in `C`, and either incident edge would be repairable.  This
justifies `|K| >= d_B(K)`.

Summing gives

`|D_X union D_Y| >= |C|+k-1`.

The bounds `|D_X union D_Y| <= 4` and `|C| >= 3` leave only `k <= 2`,
and equality forces the displayed orders when `k=2`.  A degree-three
component node would then correspond to a three-vertex path whose middle
attachment and its two component neighbours all lie in one defect set,
contradicting the defect bound two.  Thus the two components both have
order and incidence degree two, and expansion makes `T` a path.

When `k=1`, the four-vertex component is a path or claw.  A path has at
most two possible attachment vertices under the no-repair condition.  In
a claw, all three attachments would have to be leaves; each leaf and the
common centre would have to lie in one of the two disjoint defect sets.
No two leaves can then share a defect set of order two, so three leaves
cannot be assigned.  This exhausts the case.

As an independent finite check, all `14,287` labelled non-path trees on
seven vertices were generated from Pruefer words.  For each tree, all
`519` ordered disjoint defect pairs with each defect of order at most two
were tested.  No counterexample to Lemma 1.1 occurred.

## 2. Lemma 1.2

If `C` is independent in `K_{1,3} dotcup K_3`, it contains at most one
triangle vertex and hence at least two claw vertices.  Those two claw
vertices must be leaves.  The claw centre lies in one defect set and has
two distinct common neighbours in `C`; either centre-leaf edge is
repairable using the other leaf.  Exhaustive checking of the same `519`
defect pairs found no exception.

## 3. Theorem 2.1: common-edge construction

The defect sets are disjoint because the two supports cover `S`.  They
have order at most two, and hence the common support `C` has order at
least three.

In the common-edge case, deleting `r,s,t` leaves at least two possible
anchors in each support.  Two sets of order at least two admit distinct
representatives `a,b`.  The bags in (2.2) are disjoint and connected.
The first four bags form a clique: `X-Y` and `P-Q` are assumed literal
adjacencies, while the distinct anchors join each of `X,Y` to both full
packets.  Each of these four bags sees all three common literals.  Of the
last three pairs, `rs` is literal, so only `rt` and `st` can be missing;
they have the common endpoint `{t}`.

## 4. Theorem 2.1: repair construction

Suppose the repairable edge has `f in D_X`.  Then `f` belongs to the
support of `Y`, since the defects are disjoint, and the repairing vertex
`a` belongs to the support of `X`.  The choice of `w` is valid because
`|C| >= 3`; the choice of `b` is valid because among the three literals
outside the forbidden four-set, `Y` can miss at most two.

All seven bags in (2.6) are disjoint and connected.  The first four again
form a clique.  Both nearly-full carriers contact `u,w`; `Y` contacts
`f`; and `X union {a}` contacts `f` through the literal edge `af`.  The
two full packets contact every singleton.  Among the three singletons,
`uf` is literal, `uw` is absent because `C` is independent, and `fw` is
arbitrary.  Thus the only possible missing pairs are `uw,fw`, both at
`{w}`.  No quotient or completion edge is used.

Applying Lemma 1.1 to a spanning non-path tree of `H` is legitimate:
independence in `H` implies independence in the tree, while every tree
edge used by the repair is a literal edge of `H`.

## 5. Theorem 3.1

The prior low-internal-degree handoff supplies the needed dichotomy.  If
`L-Z` has at least three components, that result already gives the
labelled near model.  Otherwise a two-cut has exactly two lobes `D,E`.
The draft says this correctly but compresses the proof order into “first
disposes ... we may therefore assume”; no additional hypothesis is being
silently imposed.

Cutvertex-freeness makes each lobe adjacent to both gate vertices.  Hence
`D union {p}` and `E union {q}` are disjoint, connected, and adjacent.
For either lobe, its open neighbourhood is exactly its boundary support
plus the two gate vertices.  This set separates the lobe from the
nonempty rich shore, so seven-connectivity forces boundary support at
least five.  Their supports cover `S` because their union is the
`S`-full thin packet.

In the connected frontier, the three prescribed edges at `c` form a
star forest and can be extended to a spanning tree.  That tree contains
a vertex of degree three, so it is not a path.  In the disconnected
frontier, the input is exactly `K_{1,3} dotcup K_3`.  Theorem 2.1 applies
in both cases.

## 6. Scope and clarification

The proof is conditional on the stated connected-rich frontier package,
including the adjacent full packets and the prior low-internal-degree
handoff.  Within that package it eliminates every two-cut of the thin
packet and therefore proves the three-connectivity conclusion in
Corollary 3.2.

For maximum readability, a promoted version could begin the proof of
Theorem 3.1 with the explicit sentence “If `L-Z` has at least three
components, invoke the previous handoff; hence assume exactly two.”  This
is a presentation clarification only, not a mathematical gap.
