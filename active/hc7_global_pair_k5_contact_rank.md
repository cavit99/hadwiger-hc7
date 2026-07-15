# Global adjacent-pair `K_5` contact rank

**Status:** the extremal normalization and first-hit lock below are proved.
The labelled cross-pair exchange is open.  This note is a global invariant
check, not a proof of `HC_7` and not a ranked receiver theorem.

## 1. Why every adjacent pair has a five-row model

Let `G` be a hypothetical minimal `HC_7` counterexample.  For every two
vertices `p,q`,

\[
                         \chi(G-\{p,q\})\ge 5.             \tag{1.1}
\]

Indeed, a four-colouring of `G-{p,q}`, followed by two fresh colours on
`p,q`, would six-colour `G`.  Hadwiger's conjecture at parameter five
therefore gives a `K_5` model in `G-{p,q}`.

For an edge `pq` and a five-row model

\[
                  \mathcal M=(F_1,\ldots,F_5)
                         \quad\hbox{in }G-\{p,q\},          \tag{1.2}
\]

put

\[
 C_p=\{i:p\sim F_i\},\qquad C_q=\{i:q\sim F_i\},          \tag{1.3}
\]

and define its contact profile by

\[
 \lambda(pq,\mathcal M)=
 \left(|C_p\cap C_q|,\ |C_p\cup C_q|,
       -\sum_{i=1}^5|F_i|\right).                         \tag{1.4}
\]

Choose `(pq,mathcal M)` lexicographically maximal over all adjacent pairs
and all their `K_5` models.  This is a genuine graph-global choice: the
family is finite and no local gate orientation enters its definition.
The third coordinate is only a tie-breaker; Section 4 explains why it is
not yet a rewrite rank.

Since `pq` is literal, five common rows would make

\[
                  \{p\},\{q\},F_1,\ldots,F_5
\]

a `K_7` model.  Hence, in the target-free branch,

\[
                         |C_p\cap C_q|\le4.               \tag{1.5}
\]

## 2. The global first-hit lock

### Lemma 2.1 (contact-maximal first hits are old contacts)

Let `(pq,mathcal M)` maximize the first two coordinates of (1.4), either
for the fixed pair `pq` or globally.  Let `P` be a `p-q` path in `G-pq`,
and put `U=F_1 union ... union F_5`.

If `P` meets `U`, let `x` be its first vertex in `U` from the `p` end and
`y` its first vertex in `U` from the `q` end.  If

\[
                         x\in F_i,\qquad y\in F_j,
\]

then

\[
                         i\in C_p,\qquad j\in C_q.        \tag{2.1}
\]

In particular, if `i=j`, then that row is already common:

\[
                              i\in C_p\cap C_q.           \tag{2.2}
\]

If `P` avoids `U`, let `K` be the component of

\[
                         (G-\{p,q\})-U
\]

containing the internal vertices of `P`.  Every model row adjacent to
`K` is already a common-contact row.

### Proof

Suppose first that `P` meets `U`.  The initial `p-x` segment before `x`
has no model vertex, and the corresponding terminal `y-q` segment before
`q` has no model vertex.  If `i ne j`, add the internal vertices of the
first segment to `F_i` and those of the second to `F_j`.  The enlarged
rows are connected, disjoint, and retain every old row adjacency.  They
give another `K_5` model avoiding `p,q`, now with the literal contacts
`p-F_i` and `q-F_j`.

If `i=j`, add both exterior end segments to that one row.  Their union
with `F_i` is connected and disjoint from every other row, so this again
is a valid five-row model and it gives both pole contacts to `F_i`.

No old contact is lost in either construction.  If `p` did not already
contact `F_i`, the new contact would either increase the number of common
rows (when `q` contacts `F_i`) or increase the union contact (when it does
not).  Both contradict lexicographic maximality.  Thus `i in C_p`; the
argument at the other end is symmetric.  The same-row conclusion follows.

Now suppose `P` avoids `U`.  The graph `G-{p,q}` is connected, so `K` has
an edge to at least one model row.  For any row `F_i` adjacent to `K`,
replace it by `F_i union K`.  This remains a connected row and preserves
the five-row clique model.  The first and last edges of `P` make both
`p` and `q` adjacent to the enlarged row.  If `F_i` were not already
common, the joint-contact coordinate would increase.  Hence every such
attachment row is common.  \(\square\)

The proof is label-faithful.  It moves literal exterior path segments into
literal model rows; it never identifies a palette colour with a row.

## 3. Six simultaneous locked channels

Deleting one edge from a seven-connected graph leaves a six-connected
graph.  Thus `G-pq` has six internally vertex-disjoint `p-q` paths.
Applying Lemma 2.1 to all six gives the following exact consequence.

### Corollary 3.1

There are six internally disjoint literal channels through `G-pq`.  Every
channel which meets the selected model first meets, from its two ends, a
row already contacted by the corresponding pole.  The six first-hit
vertices, among the channels which meet the model, are distinct on either
end.  A channel avoiding the model lies in an exterior component all of
whose model attachment rows are common contacts.

In particular, if all six channels meet the model, some `p`-contact row
receives at least

\[
                         \left\lceil 6/|C_p|\right\rceil
\]

pairwise internally disjoint `p`-to-row end segments, and symmetrically at
`q`.

This is a global **row-duty lock**, not a row split.  Several channels may
end at different vertices of one row while every foreign-row duty of that
row remains behind one bottleneck.

## 4. Why the profile is not yet a transition rank

The rooted four-pole theorem for disjoint edges `pq` and `dt` gives a
literal `K_4` model rooted at `p,q,d,t` in the common edge-deleted host.
It does not give a labelled transition from the selected `pq` model to a
`K_5` model avoiding `d,t`.

There are two equivalent forms of the missing reservation.

1. To extend the four rooted bags directly, one needs a fifth connected
   set disjoint from, and adjacent to, all four bags.  The rooted theorem
   reserves no such row; its bags may meet all five old model rows and both
   full packets.
2. To exchange the pole pair, if `d,t` occupy distinct old rows one would
   retain three old rows and replace the two discarded rows by disjoint
   `p`- and `q`-rooted carriers.  If they occupy one old row one would
   retain four rows and insert one connected `p,q` carrier.  The rooted
   `K_4` supplies neither the required disjointness from the retained rows
   nor their five labelled adjacencies.

Consequently the rooted core currently defines no target pair/model to
which (1.4) can be compared.  Even when a first-hit absorption leaves the
first two coordinates unchanged, it enlarges rather than shrinks the
model, so the third coordinate of (1.4) gives no orientation.  Reversible
row rotations may therefore remain inside one maximal profile.

The adjacent two-apex icosahedron barrier in
`../barriers/hc7_same_row_split_two_apex_icosahedron.md` is the exact
guardrail: contact-maximal distinct first hits can remain in one locked
row without a five-duty split.  That graph is discharged by its coherent
fixed pair, not by a strict contact increase.  Thus the next valid global
statement has to prove

\[
 \text{reserved labelled row exchange}
 \quad\text{or}\quad
 \text{one coherent fixed pair},                         \tag{4.1}
\]

not another contact inequality.

## 5. Why the general rooted-`X` theorem does not supply the reservation

Bohme--Harant--Kriesell--Mohr--Schmidt prove that
`kappa_G(X)>=4` yields a four-connected `X`-minor preserving every member
of `X` in a distinct bag.  It does not close (4.1).

* Applied to `X=S` in the whole graph, its contractions need not be
  confined to one open shore.  Both old packets may be consumed, so no
  opposite closed side remains intact for an exact-state pullback.
* The internally rooted connectivity of a closed shore is not the
  hypothesis `kappa_J(S)>=4`.  For example, take `S` to induce a seven-
  vertex path and add one vertex adjacent to every member of `S`.  Every
  root-free fragment needs all seven roots in its boundary, but deleting
  the added vertex and a middle path vertex separates members of `S`.
  Thus the two notions can differ already at orders seven and two.
* After obtaining a four-connected `S`-minor, an ordinary rooted-`K_4`
  model at four chosen roots may delete or absorb the other three roots.
  The theorem contains no group-preserving or packet-reserving clause.

Accordingly that literature gives a useful rooted connectivity reduction,
but not the literal fifth-row reservation needed by the global contact
rank.

## 6. Exact status

The maximization (1.4) is a well-founded **selection principle**, and
Lemma 2.1 is its complete automatic consequence for first-hit paths.  It
does not yet orient the atomic twin-seam rewrite system: the globally
maximizing edge need not be the compulsory seam edge, while restricting
the maximum to seam-eligible edges is not known to be closed under the
`dt` exchange.

Therefore rooted-core allocation currently yields only the locked
alternative in (4.1).  Promoting it as a ranked receiver would be
circular.  A future proof may cite Lemma 2.1 to freeze the contact profile,
but it must spend the proper-minor response or a labelled row exchange to
turn that frozen profile into the coherent fixed-pair terminal.

## 7. The avoided-pair theorem is the endgame, not a backup lemma

The natural global statement is

> every seven-connected `K_7`-minor-free graph containing a
> `K_7^vee` minor has a pair `P` such that `G-P` is
> `K_5`-minor-free.

No counterexample to this statement was found.  The standard
`K_2 vee`-icosahedron guardrail satisfies it: the two universal vertices
are such a pair.  An exhaustive small-order check is vacuous but clean.
For every graph through order eleven, complements of maximum degree at
most `n-8` cover every possible host of minimum degree seven; every host
which was seven-connected already contained a literal `K_7` minor.  The
exact avoided-pair checker
`hc7_avoided_pair_falsifier.py` returned, by order,

\[
\begin{array}{c|r|r}
n&\text{seven-connected hosts}&\text{hosts with }K_7\\ \hline
8&1&1\\
9&5&5\\
10&87&87\\
11&9940&9940.
\end{array}
\]

This finite check is only falsification evidence.

The proposed theorem is already `HC_7`-strength.  A minimal counterexample
is seven-connected, is `K_7`-minor-free, and the known near-clique theorem
gives it a `K_7^vee` minor.  If `G-P` were `K_5`-minor-free, known `HC_5`
would four-colour `G-P`; two fresh colours on `P` would six-colour `G`.
Thus proving the avoided-pair theorem closes `HC_7` immediately.

The reserved-fifth-row obstruction in Section 4 is necessary but is not,
by itself, the whole global gap.  In the two-apex icosahedron, many
nonterminal pairs have a `K_5` model after their deletion and can lie at
the maximal contact profile, while only the hidden apex pair is terminal.
Even a faithful local exchange may therefore move between wrong pairs at
equal profile.  One must additionally prove sink coherence: all neutral
rechoices in a terminal component expose the same literal pair, or a
proper-minor state leaves that component.  Without that composition
statement, “reserved fifth row” remains another local allocation theorem
rather than the avoided-pair endgame.
