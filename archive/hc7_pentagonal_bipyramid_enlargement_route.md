# Hegde--Thomas enlargements of the pentagonal bipyramid

**Archive note:** this exploratory route was superseded by the tracked
paired-rooted target and is retained for provenance.

**Status:** active structural route; exact finite probe completed, relative
model-alignment theorem open.

This note tests whether the nonplanar five-connected seven-column core can
be handled by the enlargement theorem of Hegde and Thomas rather than by
further local linkage cases.

## 1. External structural input

Let

\[
                         P=C_5\vee\overline{K_2}.
\]

The graph `P` is four-connected, planar and is not the prism.  Hence it is
weakly four-connected in the terminology of Hegde--Thomas.  If `F` is
five-connected and nonplanar and contains `P` as a minor, Theorem 1.2 of

> R. Hegde and R. Thomas, *Non-Embeddable Extensions of Embedded Minors*,
> Journal of Combinatorial Theory, Series B **131** (2018), 55--84,
> Theorem 1.2, [arXiv:1401.2973](https://arxiv.org/abs/1401.2973)

implies that `F` has a minor isomorphic to an `i`-enlargement of `P` for
some `i in {1,...,7}`.

Every peripheral cycle of `P` is a triangle.  Enlargement types 2, 4, 6
and 7 require four distinct cyclic vertices, or a nonadjacent pair on one
peripheral cycle, and therefore have no instance for `P`.  The only
possibilities are:

1. adding an edge between two nonconfluent old vertices;
2. a nonconforming split of one old vertex (type 3); or
3. the double-split-plus-jump operation on one old edge (type 5).

## 2. Exact finite probe

The deterministic script

```text
python3 active/pb_hte_enlargement_probe.py
```

enumerates all labelled instances using the unique plane rotation system
of `P`.  It finds

```text
type 1:  6
type 3: 15
type 5: 50
```

and no instances of types 2, 4, 6 or 7.  An exhaustive connected-mask
search checks clique-minor branch sets and a separate matching check
records which old PB labels occur in distinct bags.

Every one of the 71 enlargements has a `K_5`-minor model whose five bags
admit representatives from five distinct old PB label fibres.  This is
only an abstract labelled-minor statement.

A stronger check requires each representative bag to contain the *whole*
fibre of its assigned old label.  It succeeds for every type-1 and type-3
instance and for every rim--rim type-5 instance, but fails for 20 of the 40
pole--rim type-5 instances.  Thus even inside the finite enlargement graph,
five distinct label intersections cannot automatically be upgraded to five
whole retained old branch sets.

## 3. Exact trust gap

Hegde--Thomas Theorem 1.2 is not stated relative to a prescribed minor
model.  Its conclusion is that `F` has *some* minor isomorphic to an
enlargement of `P`.  The proof passes through a topological model of a
conforming expansion, permits a replacement subdivision in its structural
theorem, and later contracts or changes the conforming expansion.  It does
not preserve:

- the seven specified spanning columns in the current HC7 configuration;
- the literal neighbours of the two external root branch sets;
- whole old columns inside the branch sets of the enlargement minor; or
- a prescribed matching between enlargement labels and root contacts.

Consequently the theorem plus the finite probe gives an unrooted `K_5`
minor in `F`, but not yet five branch sets each adjacent to both external
roots.  The latter is what would lift to the required `K_7` model.

The 20 pole--rim type-5 failures show that this is not a wording issue.  A
proof must use either the extra five-connectivity of the host beyond the
weakly four-connected enlargement, or the operation-specific colouring
responses, to repair the lost whole-label contacts.

## 4. Focused next theorem

A useful relative theorem would be the following.

> **Relative enlargement alignment target.**  Let a five-connected
> nonplanar graph be partitioned into seven connected spanning columns with
> contact graph `P`, and let two disjoint adjacent external branch sets be
> adjacent to every column.  Then either the graph has a `K_5`-minor model
> whose five bags each retain a whole distinct old column, or the original
> column model exposes an order-at-most-four separation that lifts to the
> required host separation.

The enlargement theorem is a plausible engine for this target, not a proof
of it.  A first finite structural subproblem is to analyze the 20 exceptional
pole--rim type-5 enlargements: five-connectivity of the host must supply an
additional bridge across a small separation of the enlargement, and the
new bridge should either repair a whole-label `K_5` model or reroute the
prescribed PB model.  This keeps the remaining work global and
label-preserving rather than reopening the five local Two Paths cases.
