# The block--Helly core of an indecomposable rooted carrier

## 1. Purpose

The `Q`-full quotient reduction leaves connected carrier parts which
cannot be split into two connected `Q`-full pieces.  A tree carrier has a
universal rainbow gate by the subtree Helly property.  This note extends
that conclusion to an arbitrary connected carrier: either there is still
a universal gate vertex, or all rainbow complexity is concentrated in
one 2-connected block and every lobe outside that block is portal-dark.

The statement is independent of `HC_7`, the number of portal classes,
and the sizes of those classes.

## 2. Disjoint transversals are exactly connected covering splits

Let `D` be a connected graph and let

\[
                         P_1,\ldots,P_s\subseteq V(D)
\]

be nonempty portal sets.  A connected subgraph is **rainbow** when it
meets every `P_i`.

### Lemma 2.1 (extension of two disjoint rainbows)

If `D` contains two vertex-disjoint rainbow connected subgraphs, then
`V(D)` has a bipartition into two nonempty connected adjacent rainbow
sets.

#### Proof

Contract the two rainbow subgraphs, take a spanning tree of the resulting
connected graph, and delete an edge on the path between the two
contraction vertices.  The two tree components lift to the desired
partition.  Each contains one of the original rainbow subgraphs.  QED.

Thus a carrier is indecomposable precisely when it contains no two
vertex-disjoint rainbow connected subgraphs.

## 3. The block--Helly dichotomy

Use the standard block--cut tree `T_D`: its nodes are the cutvertices and
blocks of `D`, with incidence as edges.  Bridges are allowed as two-vertex
blocks.  For a connected subgraph `K` of `D`, let `tau(K)` be the minimal
subtree of `T_D` traversed by `K`.  Concretely, it contains the block node
of every edge of `K`, the unique block node of every non-cutvertex of
`K`, and every cutvertex node used by `K`.

### Theorem 3.1 (rainbow block--Helly core)

Assume `D` is portal-indecomposable.  At least one of the following
structural conclusions holds; if the first fails, the second holds.

1. There is a vertex `x in D` contained in every rainbow connected
   subgraph of `D`.
2. There is a block `B` of order at least three which meets every rainbow
   connected subgraph of `D`.

In outcome 2, every component `C` of `D-V(B)` has exactly one neighbour
in `B`, and `C` misses at least one portal class.

#### Proof

Let `mathcal F` be the finite family of inclusion-minimal rainbow
connected subgraphs.  It is nonempty.  By indecomposability and Lemma
2.1, any two members of `mathcal F` intersect.  Therefore their projected
subtrees `tau(K)` are pairwise intersecting.  Subtrees of a tree have the
Helly property, so all `tau(K)` contain one common node `z` of `T_D`.

If `z` is the node of a cutvertex `x`, then every `K in mathcal F`
contains `x`: a connected subgraph whose block--cut trace uses the
cutvertex node must traverse the actual vertex.  Every rainbow connected
subgraph contains an inclusion-minimal member of `mathcal F`, so `x`
lies in every such subgraph.  This is outcome 1.

Suppose instead that `z` is a block node `B`.  Every member of
`mathcal F` meets the actual block `B`, and hence so does every rainbow
connected subgraph.  If `B` is an isolated one-vertex block, its unique
vertex belongs to every member of `mathcal F`, giving outcome 1.  If `B`
is a bridge `uv`, no two traces can be
`{u}` and `{v}`: the bridge separates the corresponding two sides of
`D`, so the two connected subgraphs would be disjoint, contrary to
pairwise intersection.  Hence the nonempty traces in `{u,v}` are
pairwise intersecting and have a common endpoint.  That endpoint lies in
every member of `mathcal F`, which gives outcome 1.  Thus, when outcome 1
is unavailable, `B` has order at least three and is 2-connected.

A component `C` of `D-V(B)` attaches to `B`, since `D` is connected.  It
cannot attach at two distinct vertices of `B`: a path through `C`
between two such attachments, together with two internally disjoint
paths in the 2-connected block, would place vertices of `C` in the same
block as `B`, contradicting maximality of the block.  Hence it has one
attachment.  Finally `C` cannot itself be rainbow, because it is a
connected subgraph disjoint from `B`, while every rainbow connected
subgraph meets `B`.  Thus it misses a portal class.  QED.

### Corollary 3.2 (`Q`-full carriers)

Let `Q` be a clique and let the portal sets be the neighbours in `D` of
the vertices of `Q`.  A maximally refined `Q`-full carrier has either a
universal `Q`-rainbow gate vertex or a single 2-connected block meeting
every connected `Q`-full subgraph.  In the latter case all components
hanging off the block are `Q`-dark and attach at single cutvertices.

## 4. Consequence for the carrier-lifting programme

The one/two-carrier adhesion is therefore not an arbitrary unbounded
network.  After the literal gate branch is handled by the faithful cut
lift, every carrier has one 2-connected **rainbow core block** with only
single-attachment dark lobes.  All left/right shore incidences and portal
classes can be recorded on that block by marking either their literal
core vertices or the cutvertices carrying the corresponding lobes.

The generalized Two Paths Theorem can now be applied to a tuple of these
marked core vertices.  It gives either a crossing in the 2-connected
core or a web completion.  The remaining theorem-strength step is
labelled: prove that a crossing supplies two disjoint rainbow carriers
(or a rooted Hall frame), while a web completion places all marks of one
neutral class on a common outer boundary.  The present theorem does not
assert that step, but it removes every unbounded block-tree alternative
before it is attempted.

The interface with the Two Paths Theorem can be stated exactly.  Call a
cyclic tuple `Z` of distinct marked vertices of the core block
**rainbow-forcing** when every crossing of `Z` (two disjoint paths joining
alternating pairs of entries) can be enlarged, using the named portal
lobes, to two disjoint rainbow connected subgraphs of `D`.

### Corollary 4.1 (crossing or web, with labels isolated)

If `D` is indecomposable and `Z` is rainbow-forcing, then the core block
is a spanning subgraph of a web with frame `Z`.

#### Proof

A crossing would contradict indecomposability by the definition of
rainbow-forcing and Lemma 2.1.  Hence `Z` is crossless.  The generalized
Two Paths Theorem says that a graph with a crossless tuple embeds in a
web having that tuple as its frame.  QED.

Here “crossless” and “web” are used in the same-vertex generalized-tuple
sense of that theorem: the core is a spanning subgraph of a web
completion, and an edge added by the completion is not asserted to be an
edge of `D`.

This corollary deliberately does not declare an arbitrary portal tuple
rainbow-forcing.  Establishing that property from strict surplus or
proper-minor state exchange is the exact label-preserving rerouting
lemma still required.

## 5. Audit boundary

The conclusion is a block, not necessarily a common vertex.  The three
edges of a triangle give the standard pairwise-intersecting family with
no common vertex, so outcome 2 is genuinely necessary.  Nor does the
theorem assert that an arbitrary crossing of four marked vertices
preserves all portal classes.  That label-preservation issue is exactly
the residual rooted-model problem.
