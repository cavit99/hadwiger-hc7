# Retracted: proposed unrestricted Tutte stabilization of packet skeletons

**Status:** retracted from the proof spine.  The theorem stated below was
claimed with hypotheses that are too broad.  It must not be cited as a
result, and neither Theorem 2.1 nor its corollaries are established.

The valid result that survives is the local, explicitly verified rotation
lemma in `results/hc7_exact7_packet_bridge_rotation.md`.

## 0. Retraction reason

The paraphrase of Tutte's stable-bridge theorem used below omitted a
necessary qualification on the path system and/or on which bridges are
stabilized.  In particular, the asserted arbitrary-tree application cannot
be inferred from the quoted statement.

A diagnostic small example is `K_4` with a path system consisting of one
edge `xy`, regarded as its sole segment.  No conclusion saying that **all**
bridges have attachments on two distinct segments is even syntactically
possible: there is only one segment.  If the replacement `x-y` path is
spanning, every unused chord is a trivial bridge attached on that segment;
if it is not spanning, the remaining component gives a bridge attached on
that segment.  Thus the formulation in Section 1 cannot support the
conclusion claimed in Theorem 2.1.

This example does not decide the narrower standard version concerning
only nontrivial bridges of a suitable multi-path system.  It does show that
the portal-tree globalization below requires a new, precisely sourced
special theorem.  Until such a theorem is supplied and its one-path,
two-path, and disconnected-system edge cases are checked, this file is a
record of a blocked approach only.

## 1. Former external-theorem paraphrase (not accepted)

Tutte's stable-bridge theorem, in the form stated as Theorem 1.1 of
Paul Wollan, *Bridges in Highly Connected Graphs*, SIAM J. Discrete Math.
24 (2010), 1731--1741, DOI `10.1137/070710214`, says:

Let `F` be a subgraph of a 3-connected graph, let the chosen branch set
contain every vertex of `F` of degree at least three, and let its segments
be the internally disjoint paths between consecutive branch vertices.
The segments can be rerouted, preserving the two endpoints of every
segment, so that every bridge of the rerouted subgraph is 2-stable; that
is, no one segment contains all attachments of a bridge.

The formulation permits the segments to share branch endpoints, but not
internal vertices.  It does not require the segment union to be connected.

Primary source:
`https://webdoc.sub.gwdg.de/ebook/serien/e/hbm/hbm299.pdf`.

## 2. Former packet application (retracted)

### Retracted Claim 2.1 (simultaneous portal-preserving stabilization)

Let `R` be a 3-connected open shore containing two disjoint `S`-full
packets.  In each packet choose one literal portal witness `p_i(s)` for
every `s in S`, and choose a nontrivial minimal tree `T_i` containing its
distinct selected witnesses.  Then there are two disjoint `S`-full trees
`T'_1,T'_2` with the same labelled skeleton vertices and the same abstract
tree skeletons such that every bridge of

\[
                              T'_1\cup T'_2
\]

in `R` has attachments on at least two distinct skeleton segments.

#### Proof

Let `F=T_1 union T_2`.  In each tree declare as branch vertices every
selected portal witness, every tree vertex of degree at least three, and
every leaf.  Minimality already makes each leaf a selected witness, but
including leaves explicitly removes any endpoint ambiguity.  The resulting
segments are nontrivial paths, internally disjoint across both trees, and
their union is `F`.

Apply Tutte's theorem in the ambient 3-connected graph `R`.  It returns one
path for each old segment with the same two endpoints, and all returned
paths are internally disjoint.  Since endpoints belonging to the two old
trees are distinct, the returned paths preserve the two abstract tree
components rather than joining them.  Their unions `T'_1,T'_2` are
therefore disjoint subdivisions of the original tree skeletons.

Every selected `p_i(s)` is a fixed segment endpoint, so it remains in
`T'_i`.  Hence both new trees are still `S`-full.  Finally, 2-stability is
exactly the assertion that no bridge has all its attachments on one
segment. `square`

### Retracted Corollary 2.2 (bounded stable society)

Each packet tree has at most twelve skeleton vertices and eleven segments.
After Tutte stabilization, every bridge is incident with at least two of
the at most twenty-two labelled segments.  In the audited hard exact-seven
cell, the three-attachment theorem independently gives at least three
distinct packet attachment vertices for every nontrivial complementary
component.

Thus, whenever the rich shore itself is 3-connected, the reversible
one-segment rotations are globally eliminated by a standard theorem.  The
remaining bridge system is a bounded-segment society suitable for the
Two-Paths/web dichotomy.

## 3. Former pure-Moser consequence (retracted)

The audited pure-Moser two-component low-cut theorem proves that every
exterior component of order at least four is 3-connected.  Apply Tutte's
theorem separately inside any such component to a nontrivial minimal tree
through seven selected boundary portal witnesses.  Every resulting bridge
inside that component is 2-stable.  No three-attachment conclusion is
claimed for a single tree: if one bridge contains every vertex outside two
tree attachments, those two attachments need not be a separator.

This removes the one-segment portal-drift obstruction from the
three-connected pure-Moser residue.  It does not itself create the rooted
`K_5` model or reserved connector; bridges may still attach across two or
more skeleton segments in a rural pattern.

## 4. Scope barriers

1. The theorem requires the **ambient shore graph itself** to be
   3-connected.  Seven-connectivity of the whole graph does not imply this.
   It cannot be applied directly to the general connected rich shore, whose
   surviving cutvertices merely have two lobes.
2. A singleton portal tree has no nontrivial segment.  It is a separate
   tiny-core case unless it can first be extended disjointly to a nontrivial
   tree.
3. Two-stability means attachments meet two segments, not that the bridge
   supplies two disjoint paths, contacts five boundary literals, or meets
   both packet trees.
4. Tutte stabilization supplies existence, not a monotone descent through
   the local rotation graph.  Its value is precisely that, in a
   3-connected ambient shore, it bypasses the need to prove such descent.
