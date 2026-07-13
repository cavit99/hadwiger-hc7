# Candidate apex pairs and the unrooted `TK_5` test

## Status

This note tests the proposed use of Kelmans--Seymour on deletions of
natural model-edge endpoint pairs.  It proves a necessary condition on any
global two-apex pair and shows why an arbitrary unrooted `TK_5` does not
complete the near model.

The viable pair must consist of **bag-killing vertices in two distinct
foreign bags**.  In particular the endpoints of the normalized deficient
path can never be the apex pair.

## 1. The untouched foreign `K_6`

Let

\[
                       A,B,C,U_1,U_2,U_3,U_4              \tag{1.1}
\]

be a spanning labelled `K_7^vee` model with only `AB,AC` unprescribed.
Then

\[
                         B,C,U_1,U_2,U_3,U_4              \tag{1.2}
\]

are six pairwise adjacent connected bags: they form a `K_6` model without
using any vertex of `A`.

### Lemma 1.1 (where a global apex pair must lie)

If `G-{p,q}` is planar, then `p,q` lie in two distinct bags of (1.2).

#### Proof

If neither deleted vertex lies in a bag of (1.2), all six bags survive in
`G-{p,q}`, which therefore contains a `K_6` minor and is not planar.

If only one bag of (1.2) meets `{p,q}`—this includes the case in which
both deleted vertices lie in the same foreign bag—the other five bags are
untouched and still form a `K_5` model.  Again the remainder is nonplanar.
Thus the pair meets two distinct foreign bags.  \(\square\)

This is only a necessary condition.  Deleting one vertex from a
nonsingleton bag may leave a connected fragment retaining all old roles;
then five old bags can still survive after a realignment.  A successful
pair must therefore be essential, or **bag-killing**, in both of its bags.

### Corollary 1.2 (the deficient path is never the apex pair)

No vertex of `A` belongs to a two-apex pair of `G` relative to the model
(1.1).  In particular, the two endpoints obtained in
`../results/hc7_near_k7_deficient_path_normalization.md` cannot be the pair
whose deletion is planar.

## 2. Exact limit of the `TK_5` alternative

Since `G` is seven-connected, `G-{p,q}` is five-connected for every pair.
If it is nonplanar, the Kelmans--Seymour theorem gives a subdivision of
`K_5` in that deletion.

### Proposition 2.1 (an unrooted `TK_5` does not combine automatically)

The existence of that subdivision does not, by itself, combine with the
near model to give a `K_7` minor.

#### Proof

To add `{p}` and `{q}` as two further branch bags to the five branch bags
of the subdivision, each deleted vertex would have to be adjacent to all
five bags and the two singleton bags would have to be adjacent to one
another.  A general model-edge endpoint supplies none of these rooted
conditions.  Absorbing paths from `p,q` into the subdivision can consume
the old near-model bags or make two proposed branch sets intersect.

Alternatively, retaining old foreign bags and using the subdivision as a
repair requires prescribed branch vertices in the portal sets of those
bags.  Kelmans--Seymour is unrooted and gives no such prescription.
Thus the asserted combination is exactly an additional rooted-linkage
theorem, not a consequence of the `TK_5` output.  \(\square\)

The standard test graph `K_2 vee I`, with `I` the icosahedron, displays
the issue concretely.  It has many natural endpoint pairs whose deletion
is nonplanar and hence contains a `TK_5`; the coherent pair is the two
universal singleton vertices.  The displayed deficient vertices of a
near model are not that pair.  This graph is not seven-critical, so it is
a falsifier of the unconditional combination step, not of the desired
critical theorem.

## 3. Viable reformulation

The only noncircular use of the candidate-pair test is therefore:

> Select vertices `p,q` in two distinct foreign bags and prove, from
> lexicographic model minimality plus contraction-critical operation
> states, that either they kill those two bag roles and `G-{p,q}` has one
> coherent planar expansion, or a `TK_5` can be chosen with its five
> branch vertices in specified surviving portal classes.

The first outcome is the required global pair.  The second is a genuinely
rooted strengthening and would give a label-faithful `K_7`.  Without the
bag-killing and rooted clauses, the proposed `TK_5` mechanism stops at an
unproved global theorem.
