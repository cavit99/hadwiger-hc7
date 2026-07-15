# Active goal: atomic four-root linkage/disk decoder

**Status:** research target, not a proved theorem.

## Decision

Keep the exact-seven `(1,2)` programme as the primary `HC_7` engine.  The
next goal is no longer an abstract state-pullback or an unspecified
four-portal lemma.  The list obstruction has now been solved exactly by
set-Menger.  What remains is one literal geometric decoder.

The decoder must use the full atomic kernel.  Neither a static two-carrier
quotient nor two-connectivity plus a fully crossed path is sufficient.
Generalized webs organize the negative linkage branch, but their completion
edges are never host edges.

Proving this goal closes the connected-bipartite atomic separating-edge
family.  It does not by itself prove `HC_7`.

## Frozen atomic input

Use an actual separation

\[
 V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad S=W\mathbin{\dot\cup}\{u\},\qquad |S|=7,
\]

with the following audited hypotheses.

1. `G` is seven-connected, `K_7`-minor-free, not six-colourable, and every
   proper minor is six-colourable.
2. There is no `A-R` edge; `A` is connected and `S`-full.
3. `zu` is the unique edge from `A` to `u`.
4. `R` contains two disjoint adjacent connected `S`-full packets.
5. `H=G[S]` is connected and bipartite: it is a tree or a six-cycle with
   one pendant vertex.
6. Root deletion gives `A-z` connected and `W`-full.
7. Every nonsingleton surviving atom is two-connected; every clean edge of
   the normalized rooted path/`Y` core closes; a survivor has
   `d_{G[A]}(z)>=3` and is not a bare cycle.

The exceptional frontier `K_{1,3} dotunion K_3` is not part of this goal.

## Audited reduction to four literal roots

Take the canonical carriers

\[
                         X=\{z\},\qquad Y=A-z.
\]

Their literal lists on `S` satisfy

\[
 \Lambda(u)=\{X\},\qquad
 Y\in\Lambda(w)\quad(w\in W),
\]

and `X in Lambda(w)` exactly when `zw` is an edge.

If some empty or singleton clique reservoir makes `H` properly
two-list-colourable using both carrier labels, the audited adaptive
clique-reservoir theorem six-colours `G`.  Otherwise the audited
two-list/Menger dichotomy gives two vertex-disjoint parity-bad paths

\[
                  P_0:a_0\leadsto b_0,
             \qquad P_1:a_1\leadsto b_1                 \tag{1}
\]

in `H`, with four distinct literal endpoints.  Their signs are
orientation demands, not carrier names.

Seven-connectivity gives those four labels distinct literal portals in
`A`, although the safest next step is the existing artificial-root
four-port theorem.  Apply it to the ordered roots

\[
                         (a_0,a_1,b_0,b_1).              \tag{2}
\]

It returns exactly one of the following literal outcomes.

1. **Linkage:** disjoint `A`-interior paths join `a_0` to `b_0` and
   `a_1` to `b_1`.
2. **Rural disk:** `G[A union {a_0,a_1,b_0,b_1}]` has a closed-disk
   embedding with those four roots on the boundary in the order (2).

This reduction is proved.  The next theorem starts here.

## Target theorem

### Atomic four-root linkage/disk decoder

Under the frozen input and (1)--(2), both the linkage and rural-disk
outcomes yield at least one of:

1. disjoint nonempty connected adjacent sets `C_0,C_1 subseteq A` and a
   clique reservoir `U subseteq S` of order at most one such that `H-U`
   has a proper two-colouring using both labels and every label class is
   contacted by its named carrier; or
2. five pairwise disjoint connected pairwise adjacent subgraphs of
   `G[A union S]`, each containing a different literal member of `S`.

Outcome 1 invokes the audited adaptive clique-reservoir theorem.  No
carrier need contact `U`; the proper-minor response chooses the actual
returned blocks and their packet demand remains at most two.  Outcome 2,
together with the two adjacent full packets in `R`, is a literal `K_7`
model.

## Proof engine

Spend the main effort on the rural-disk branch.

1. Work only in the literal disk returned by the audited four-port theorem.
   Track the portal sets of the three unrepresented boundary labels and the
   compulsory root `z`.
2. Choose an inclusion-minimal frame interval or bridge hull which blocks
   an admissible two-carrier allocation.  If an extra portal bridge crosses
   that interval, decode the crossing into the carriers or five rooted
   bags.
3. If every extra attachment is confined, use the full relative
   seven-cut inequalities.  A confinement with at most six literal gates
   is impossible; an equality gate is an actual seven-adhesion and must be
   closed by the existing packet/reflection machinery, not merely named as
   a smaller case.
4. In the linkage branch, the two `A` paths and the two bad `H` paths alone
   are insufficient.  Use the fully crossed normalized core or a second
   portal bridge to obtain a literal second rung.  Failure of every second
   rung must produce the same rural disk or an at-most-six separator.
5. Invoke a proper-minor colouring only after the literal carriers or an
   exact actual adhesion have been identified.  Never identify a palette
   colour with a root or branch-set label.

The desired reusable sublemma is a **three-extra-label rural decoder**:
in a seven-connected four-root disk society with the remaining three
literal boundary labels attached, either an extra attachment crosses the
frame, two adjacent seed carriers exist, or the attachment gates form an
at-most-six cut.  It must be proved with the atomic portal data; an
unconditional society statement is false.

## Falsification boundary

The following shortcuts are closed.

* The canonical two-carrier quotient need not have an adaptive return or a
  rooted `K_5`; a path-frontier example remains `K_5`-minor-free after the
  carriers are contracted.  Internal shore geometry is essential.  See
  `../barriers/hc7_atomic_static_root_split_quotient_barrier.md`.
* A two-connected, noncyclic shore with a fully crossed path need not have
  the desired two-pair linkage.  Maximal outerplanar fans give the rural
  branch.
* A Humeau--Pous completion edge is not a host edge, and a web-composition
  seam is not automatically an actual seven-adhesion.
* The four orientation signs are not two pairs of carrier labels.

Exact bounded falsification is nevertheless positive: all 84 rooted
connected-bipartite frontiers against every biconnected atlas shore of
orders three through six (5,880 exhaustive instances) force an adaptive
carrier split before a rooted `K_5` clause is needed.  The rerun requires
the first and last vertices of each `st`-numbering to be literally adjacent.
This is evidence only; the search omits the global
minor-critical response and cannot replace the unbounded decoder.

## Literature boundary checked online

* Humeau--Pous gives literal crossings or a same-vertex web completion and
  a recursive parallel-composition description.  It does not decode the
  three extra boundary labels or make completion edges literal.
* Hayashi--Kawarabayashi--Yoo gives a powerful four-root subdivision
  trichotomy, but its relative-separation, stable-root, and two-neighbour
  hypotheses are not verified in this atom.
* Rooted-folio and colorful-minor theorems preserve bounded rooted or
  annotated minor data, not the adaptive boundary colouring return.
* High-connectivity knittedness applies far above connectivity seven.

No located theorem supplies the target outright.  The new work is the
label-faithful rural/linkage decoder under the exact seven-cut inequalities.

## Success condition

The goal succeeds only with a complete proof of both four-port outcomes and
an independent audit of every carrier, contraction, branch-set adjacency,
and separator order.  A further portal taxonomy, a disk embedding without a
decoder, or a smaller unlabeled adhesion is not success.

Terminate a proposed mechanism if it produces an unbounded new state
alphabet or a transition cycle with no literal carrier/rooted-model output.
Retain the target theorem and change the proof engine; do not restart a
boundary census.
