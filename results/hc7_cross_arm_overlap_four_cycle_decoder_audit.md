# Audit of the overlap-four five-terminal cycle decoder

## Verdict

**GREEN.**  The twelve dihedral cycle orders are complete, exactly the two
stated orders survive, the 27 survivors for either bad order are exactly
the parameterized crossed-frame language, the specialized nine-vertex
`K_7` enumeration is complete, and every quotient model lifts through the
five rooted exterior bags.

The theorem is a conditional labelled composition result.  It assumes a
five-bag rooted cycle in `G-I`; it does not extract such a cycle from the
connectivity of the exterior.

## 1. Original state space and cyclic orders

The imported eleven-support join has already passed a separate GREEN
audit.  Completing all 36 original pair variables produces 3096 distinct
labelled complements.  The common rooted-`K_4` search is performed before
any virtual cycle adjacency is introduced; it removes 2016 completions,
leaving 1080.

An undirected cyclic order on five labelled terminals is determined up to
rotation and reversal.  Fixing terminal `4` first removes rotation.  Of
the `4!` remaining orders, exactly one of an order and its reversal has
second label smaller than its last label.  Hence `canonical_cycles`
enumerates exactly `4!/2=12` orders, without omission or duplication.

Running

```text
python3 active/hc7_cross_arm_overlap_four_cycle_decoder_verify.py
```

reproduced all twelve rows.  Ten had no survivor.  The only two with
survivors were

```text
(4,5,p,6,q), (4,5,q,6,p),
```

and each had exactly 27.

## 2. Completeness of the `K_7` model search

A `K_7` model supported on at most nine labelled vertices has only four
possible bag-size profiles:

```text
1+1+1+1+1+1+1                 (support 7),
2+1+1+1+1+1+1                 (support 8),
3+1+1+1+1+1+1                 (support 9),
2+2+1+1+1+1+1                 (support 9).
```

`k7_model` enumerates these respectively as a seven-vertex clique, one
edge bag and six singleton bags, one connected triple bag and six
singleton bags, and two edge bags and five singleton bags.  In each case
it checks the singleton clique, contact of every nonsingleton bag with
every singleton, and—when applicable—contact between the two edge bags.
This is therefore an exhaustive minor-model test, not merely a search for
a convenient model shape.

As an independent cross-check, a generic set-partition verifier enumerated
all partitions of every seven-, eight-, or nine-vertex support into seven
nonempty connected bags.  There are 750 such candidate partitions before
graph tests.  On every augmented state in all twelve cycle orders, its
answer agreed with `k7_model`.

The common outcome is also certificate-producing: the imported routine
enumerates every support of order four or five, every partition into four
bags, all bag adjacencies, and all three named contacts.  Thus every good
order is closed by an explicitly checked common model or by one of the
four complete `K_7` bag profiles above.

## 3. Exact 27-state residue

For a bad order

```text
l_1,l_2,r,6,s,
```

the five virtual edges are precisely the consecutive cycle pairs.  The
four fixed defects

```text
l_1-6, l_1-r, l_2-6, l_2-s
```

are all nonconsecutive terminal pairs, so none is an artefact of clearing
a virtual edge.  The remaining defects consist of a perfect matching `M`
on `I` and one of

```text
{rs}, {u6}, {rs,u6}  with u in I.
```

There are three choices for `M`.  For a fixed matching, `{rs}` is one
state, `{u6}` gives four states, and `{rs,u6}` gives four more.  The edge
types are disjoint—fixed terminal defects, matching edges in `I`, the
root edge, and an `I-6` spoke—so all `3(1+4+4)=27` masks are distinct.

The checker finds 27 survivors and verifies that each belongs to this
27-element language.  Hence the two sets are equal: every displayed
parameter choice occurs, and no additional label pattern is hidden in
the output.  A second verifier constructed the language directly as a
set of edge masks and confirmed exact equality for both bad orders.

This is genuinely a uniform two-gate/three-tail-state certificate.  The
only free data are a matching of the symmetric four-set `I`, a possible
spoke endpoint `u`, and the three stated tail types; it is not a list of
27 unrelated labelled exceptions.

## 4. Original and virtual edge layers

All support relations and the common rooted-`K_4` test use the completed
original complement.  For a chosen cyclic order, only its five consecutive
terminal-pair bits are then cleared.  No virtual adjacency is fed back
into an irredundancy relation or a named contact.

The `K_7` enumerator runs on this quotient edge layer.  Its use of a
virtual edge is legitimate because that edge represents an actual edge
between the corresponding pair of consecutive exterior bags.  All other
queried adjacencies remain literal original edges.

## 5. Lift through the rooted terminal cycle

Let the five exterior bags be pairwise disjoint connected subgraphs of
`G-I`, rooted at the five terminals, with consecutive bags adjacent.  In
any finite quotient branch bag, replace each terminal label by its entire
rooted exterior bag and retain every local vertex from `I`.

Connectedness lifts edge by edge along a spanning tree of the quotient
branch bag:

* an original terminal-local or terminal-terminal edge remains literal
  because the root vertex belongs to its exterior bag; and
* a virtual consecutive-terminal edge is replaced by an actual edge
  between the two corresponding exterior bags.

The same argument lifts every adjacency between distinct quotient branch
bags.  Expanded bags remain disjoint because the exterior bags are
pairwise disjoint and lie in `G-I`, while distinct quotient bags use
disjoint terminal labels and local vertices.  Quotient vertices or
exterior bags omitted by the finite model are simply unused.

Thus every finite `K_7` certificate expands to seven literal connected,
pairwise adjacent branch sets in `G`, including cases in which one quotient
bag contains several consecutive terminal labels.

## 6. Trust boundary

The audit certifies the finite decoder and the exact crossed-frame
alternative.  It does not eliminate that alternative, prove that the
exterior contains a rooted five-cycle, or turn an arbitrary web into the
required cycle.  Those remain structural obligations beyond this result.
