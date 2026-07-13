# Superseded second audit: portal matching and stable skeletons

**Archive note:** this independent GREEN check duplicates the fuller audit
now stored beside the theorem in `../results/`.  Lemma 1.1
and Theorem 2.1 are valid.  The result may be promoted beside its audit.

## 1. Stable-bridges source check

The relevant published formulation is the path-system version of Tutte's
stable-bridges theorem quoted as Theorem 1.1 by Wollan.  In that version:

* a path system is a set of pairwise internally disjoint paths;
* paths may share endpoints, but every common vertex must be an endpoint of
  both paths;
* the theorem assumes that the path system has order at least three; and
* it returns an equivalent path system, preserving the indexed endpoint
  pair of every path, for which no bridge has all attachments on one path.

The order-three hypothesis is the qualification missing from the earlier
retracted one-segment paraphrase.  It excludes the `K_4` one-path and
two-path diagnostics.  It is explicitly met in Theorem 2.1.

Primary publication: Paul Wollan, *Bridges in Highly Connected Graphs*,
SIAM J. Discrete Math. 24 (2010), 1731--1741,
DOI `10.1137/070710214`.

## 2. Lemma 1.1

Assume a maximum `S-C` matching has order
`r<min{k,|C|}`.  Konig's theorem gives a vertex cover
`A union B`, where `A subset S`, `B subset C`, and `|A|+|B|=r`.
Because `|B|<|C|`, a component `K` of `C-B` exists.  Its neighbours are
confined to `A union B`:

* an edge from `K` to `S-A` would be an uncovered incidence edge;
* an edge from `K` to `C-B-K` would contradict the definition of `K`; and
* an edge from `K` outside `S union C` would contradict that `C` is a
  component of `G-S`.

After deleting `A union B`, the nonempty set `K` is separated from the
assumed nonempty far shore.  The cut has order `r<k`, contradicting
`k`-connectivity.  No hidden assumption about edges inside `S` or inside
`C` is used.  The matching conclusion is therefore correct.

## 3. Theorem 2.1

With `k=7` and `|C|>=4`, Lemma 1.1 supplies four distinct boundary
vertices with four distinct witnesses in `C`.  Every remaining boundary
literal also has a neighbour in `C`: otherwise the other six vertices of
`S` separate `C` from the nonempty far shore.  Thus one can select at most
seven witnesses, at least four of them distinct.

Let `T` be a minimal tree through the distinct selected witnesses and
declare all selected witnesses and all degree-at-least-three vertices of
`T` to be skeleton vertices.  The suppressed abstract skeleton is a tree
with at least four vertices, so it has at least three segments.  These
segments form an eligible path system for the sourced theorem.

The endpoint-preserving rerouting really does preserve the abstract tree,
not only its terminal pairs.  If a returned segment passed through a
skeleton endpoint not incident with that segment, it would meet an
incident returned segment at a vertex internal to the first, contrary to
pairwise internal disjointness.  Nonincident segments cannot gain a common
vertex for the same reason.  Hence the returned union is a subdivision of
the same abstract tree.  Every selected portal witness remains a fixed
endpoint and therefore retains its literal boundary edge.  The new tree is
still `S`-full.

Finally, a tree whose leaves all lie among at most seven selected witnesses
has at most five degree-at-least-three vertices not already selected.
Thus there are at most twelve skeleton vertices and eleven segments, as
claimed.

## 4. Scope confirmation

The result requires all of the following:

1. an actual order-seven adhesion with a nonempty far shore;
2. the exterior component itself is 3-connected; and
3. at least four vertices in that component (automatic under the usual
   definition of 3-connectivity).

It yields stability only: every bridge has attachments not contained in a
single skeleton segment.  It does not yield two disjoint prescribed paths,
a support-five carrier, a rural embedding, or an `N`-meeting `K_6` model.
Those are correctly left as the next proof-spine step.
