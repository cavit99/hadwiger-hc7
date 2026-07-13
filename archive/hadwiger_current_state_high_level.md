# Hadwiger programme: high-level current state

## Bottom line

There is still no proof of (HC_7), and therefore no proof of Hadwiger's
Conjecture for arbitrary (t).  The programme has moved beyond raw case
enumeration: it now has several uniform, operation-sensitive lemmas and has
closed its first genuine infinite rooted-model cells.  These results have
been checked internally and adversarially in this workspace, but they have
not been externally refereed.

The decisive missing theorem remains a **dynamic labelled carrier
exchange**: turn the first extra portal or foreign-bag hit of a failed
rooted-model construction into either a label-preserving model move, a
strictly smaller Hall/capacity obstruction, or two compatible minor
colourings across an actual adhesion.

## 1. Established mathematical inputs

The programme uses the following established foundation.

* Hadwiger is known for (t\le6).
* At a least failing parameter, a proper-minor-minimal counterexample can
  be taken contraction-critical.  Writing (r=t-1), every proper minor is
  (r)-colourable, while (G) is not.
* For every vertex (v), (H=G-v) is (r)-colourable and, by induction
  at the previous parameter, contains an unrooted (K_r)-model.
* Every colour of every (r)-colouring of (H) occurs on (N(v)).
  Contracting (v) together with any independent subset of (N(v))
  produces an exact prescribed colour trace on the neighbourhood.
* Minimal counterexamples have the standard critical minimum-degree and
  connectivity properties.  For (HC_7), seven-connectivity is the key
  ambient input.

The final inductive step is exact: alter an unrooted (K_r)-model in
(H) so that every branch bag meets (N(v)).  Then the singleton
({v}) is the last branch bag of a (K_{r+1})-minor.

## 2. Genuinely new internally audited progress

### Dynamic boundary states

Static colour saturation is insufficient.  Explicit examples in the
workspace realize every independent trace, colourful nested flags, and an
unrooted clique model without the required rooted model.

The first datum which survives those examples is dynamic: for every
internal edge (e), a colouring of (G-e) creates a genuinely new
boundary equality state.  Colourings arising from proper minor operations
on opposite shores of a separation cannot induce the same marked boundary
state; if they did, their untouched restrictions would splice to colour
(G).

This crossed-splicing theorem has been proved for arbitrary
boundary-faithful minor operations, not only edge deletions.  It is the
current mechanism for converting repeated states into contradictions.

### Exact Hall circuit and genuine portal adhesion

Failure to route unused neighbourhood roots into all uncontacted model bags
has been promoted from a vague Menger obstruction to an exact gammoid
circuit.  If the circuit has order (h), its interface has order (h-1),
every proper subfamily is linkable through that same saturated interface,
and the root side is separated from the deficient bags by a genuine
adhesion

\[
                         \{v\}\cup X\cup P.
\]

In a (k)-connected host, (P) has the exact required surplus.  For
(HC_7), this forces a multiply hit accessible branch bag.  Simultaneous
root-side and far-side contractions also force a rainbow core state; the
remaining mismatch is entirely on the portal set (P).

### Root-shore portal basis

A second gammoid, whose ground elements are the individual portal vertices
rather than bag labels, has now been introduced.  Its rank is at least

\[
                         \min\{k-1,|R|\},
\]

where (R) is the set of unused neighbourhood roots.  Thus the Hall
interface (X) extends to a common linkage containing a quantified set of
individual portals.  A minimum linkage is clean at every portal endpoint.

In a co-rank-one circuit and (k\ge r+1), two clean portal carriers exist
simultaneously with the complete (X)-linkage.  Moreover the rainbow-state
colour collision can be chosen among these capacity-basis portals.  This
closes the former label-versus-colour-versus-linkage alignment gap in that
cell.

### Tree and Gallai transit bags

Crossed edge-transition states collapse an arbitrary rigid spanning tree
of a branch bag to an alternating binary path, unless there is a clean
model rotation or a first hit in a named foreign bag.  This geometric
collapse no longer requires the whole tree to be a minimal list core.

When the branch bag is its full minimal list core and the other bags are
singletons, the stronger named-colour analysis closes the cell completely.
The Gallai-block extension reduces to an alpha/delta block path; a new
leaf-carrier and opposite-owner argument eliminates that last rigid web.
This is the programme's first fully closed infinite rooted-model family.

For a co-rank-one tree bag without the full-list-core hypothesis, safe lobe
rotations give a sharp owner rule: every unprotected attachment lobe either
rotates away or wholly owns at least two deficient labels.  In (HC_7),
two portal ends consume at least four of the five deficient labels, leaving
at most one mobile label.  The tree residue is therefore a two-ended owner
corridor, an empty portal tail, or a protected-root-ended lock.

## 3. What remains provisional or computational

The detailed (HC_7) neighbourhood work remains useful as a laboratory,
but it is not a proof.

* Pure-Moser and related degree-seven configurations have been reduced
  substantially; many quotient and small-component cases were eliminated.
* Degree-eight and degree-nine exterior-component bounds and several
  shore-packing lemmas are proved, but those degree classes are not closed.
* Some finite searches enumerate boundary graphs, quotient contacts, or
  components up to a fixed order.  Their encodings and certificates have
  not been independently formalized in a proof assistant or externally
  verified.

None of these computations establishes an unbounded case by itself.  They
should be treated as conjecture generators and adversarial tests for the
uniform lemmas.

## 4. Exact (HC_7) bottleneck

The most advanced unresolved cell is now highly specific.

Start with a promoted Hall circuit and its fixed (K_6)-model.  In the
co-rank-one case, two clean root carriers split the multiply hit accessible
bag into two connected adjacent pieces.  If both pieces retain four of the
five deficient bag adjacencies, explicit branch sets give a (K_7)-minor.
Therefore every surviving split has a **two-label lock**: at least two
named model adjacencies are lost.

For a tree bag, this lock is an owner corridor with two fixed label groups
and at most one mobile label.  The remaining failures are:

1. an owner corridor whose edge transitions have not yet been synchronized;
2. an attachment-free portal tail;
3. a portal end protected by the old neighbourhood root; or
4. in a non-tree/non-singleton setting, a first carrier hit in a nontrivial
   foreign bag.

What is missing is not another path-existence statement.  It is a proof
that one of these locks necessarily yields a clean labelled rotation, a
smaller Hall circuit/contraction core, or an actual adhesion carrying the
same state from opposite faithful minor operations.

## 5. General-(t) outlook

Several of the strongest new lemmas are genuinely uniform in (r): exact
traces, Hall circuits, crossed minor splicing, the root-shore rank theorem,
binary tree collapse, and the full singleton/Gallai closure.

That is meaningful progress toward a general rooted-model principle, but
it is not yet a general Hadwiger proof.  The (HC_7) argument benefits from
(k\ge r+1), which forces portal multiplicity and two clean carriers.  For
large (t), presently available connectivity of a minimal counterexample
is much smaller relative to (r=t-1); the same counting does not guarantee
even one surplus model label.  A full proof therefore needs either:

* an ambient-lift theorem extracting additional capacity from
  minor-critical boundary states rather than raw connectivity; or
* a dynamic carrier theorem that works with fractional/deficient capacity
  and recursively shrinks the obstruction.

Thus closing (HC_7) is the credible immediate goal.  Any lemma used there
should remain label-free and parameter-uniform where possible, but claiming
that the general case is close would be unjustified.

## 6. Best next theorem target

The highest-value next statement is the following dynamic owner/carrier
exchange theorem.

> Let (G) be proper-minor-minimal non-(r)-colourable, let a promoted
> Hall circuit protect a deficient subfamily of a fixed (K_r)-model, and
> let the root-shore portal basis be chosen minimally.  If a clean split is
> blocked by a named owner corridor, empty tail, protected root, or first
> foreign-bag hit, then one of the following occurs:
>
> 1. a label-preserving rotation increases contact;
> 2. the Hall circuit, portal carrier, or contraction core strictly
>    decreases; or
> 3. two opposite boundary-faithful minor operations induce the same
>    equality partition on an actual adhesion and therefore colour (G).

For (HC_7), it is enough to prove this first for the four-fixed-label,
one-mobile-label owner corridor and its two endpoint exceptions.  Success
would close a genuinely infinite outstanding family and would supply the
first plausible bridge from the local (HC_7) laboratory to a uniform
rooted-model theorem.

## Honest assessment

The work has produced real structural mathematics and a much sharper map
of the obstruction.  It has not yet moved the accepted frontier: (HC_7)
is not proved, no complete new value of Hadwiger has been established, and
the new results still require external expert verification.  The programme
is now credible because it has a reusable dynamic mechanism and closed
infinite cells; it will become a solution only if the dynamic
owner/carrier exchange theorem is actually proved.
