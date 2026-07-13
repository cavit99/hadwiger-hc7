# Rainbow Helly cores in bounded-adhesion decompositions

## 1. A general decomposition theorem

Let `D` be a connected graph with nonempty portal sets
`P_1,...,P_s`.  A connected subgraph is **rainbow** if it meets every
portal set.  Say that `D` is **indecomposable** if it contains no two
vertex-disjoint rainbow connected subgraphs.  By Lemma 2.1 of
`hadwiger_rainbow_block_helly_core.md`, this is equivalent to the absence
of a connected adjacent bipartition whose two sides are rainbow.

Let `(T,(V_t)_{t in V(T)})` be a tree decomposition of `D`.  Its
adhesion is the maximum order of `V_t cap V_u` over edges `tu` of `T`.

### Theorem 1.1 (rainbow torso--Helly core)

If `D` is indecomposable, there is a node `z in V(T)` such that every
rainbow connected subgraph of `D` meets `V_z`.

If the decomposition has adhesion at most `k`, then every component `C`
of `D-V_z`

1. misses at least one portal class; and
2. has at most `k` neighbours in `V_z`.

#### Proof

Let `mathcal F` be the finite family of inclusion-minimal rainbow
connected subgraphs.  No two members are disjoint.  For `K in mathcal F`,
put

\[
       T(K)=\{t in V(T):V_t cap V(K) ne emptyset\}.
\]

This is a subtree of `T`.  Indeed the bags containing one fixed vertex
form a subtree, and the subtrees belonging to the vertices of a connected
graph `K` meet successively across bags containing its edges.  If
`K,L in mathcal F` intersect at a vertex `x`, every bag-subtree containing
`x` witnesses `T(K) cap T(L) ne emptyset`.  Hence the family
`{T(K):K in mathcal F}` is pairwise intersecting.  The Helly property for
subtrees of a tree gives a node `z` common to all of them.

Every rainbow connected subgraph contains an inclusion-minimal rainbow
connected subgraph, so it meets `V_z`.  A component of `D-V_z` is
therefore not rainbow, proving item 1.

Every vertex outside `V_z` has its bag-subtree wholly in one component of
`T-z`.  Bag-subtrees of adjacent vertices intersect, so connectedness of
`C` puts all bags meeting `C` in one component `T'` of `T-z`.  Let `u`
be the neighbour of `z` in `T'`.  The running-intersection axiom implies
that every edge from `C` to `V_z` has its `V_z` endpoint in
`V_z cap V_u`: otherwise the bags containing that endpoint could not
connect a bag containing the edge to `z`.  Thus

\[
                       N_D(C) cap V_z subseteq V_z cap V_u,
\]

which has order at most `k`.  QED.

## 2. The Tutte-core trichotomy

Use the standard Tutte decomposition of a connected graph, combining
the block decomposition with the 2-separation decomposition of every
2-connected block.  It has adhesion at most two and its nontrivial
torsos are of three kinds: 3-connected torsos, cycle torsos, and bond or
edge torsos of order at most two.

### Corollary 2.1 (gate, cycle, or 3-connected rainbow core)

Every indecomposable rooted carrier has a torso bag `B` meeting every
rainbow connected subgraph such that one of the following holds.

1. `|B|<=2` (a one/two-vertex gate);
2. the torso on `B` is a cycle; or
3. the torso on `B` is 3-connected.

Every component outside `B` is portal-dark and has at most two neighbours
in `B`.

The torso contains virtual edges in the usual sense; those edges record
the two-vertex adhesions and are not asserted to be literal edges of
`D`.  Any rooted-minor construction using a virtual edge must expand it
through its named bridge before it is lifted to `D`.

## 3. Why this is the right web interface

The corollary eliminates arbitrary block trees and arbitrary chains of
2-separations simultaneously.

* In the gate outcome, the faithful combined-carrier cut lemma applies
  unless a dark lobe straddles both quotient shores.
* In the cycle outcome, all portal and shore attachments have one cyclic
  order.  Alternation can be tested by the Two Paths theorem without a
  further decomposition.
* In the 3-connected outcome, the rooted-`K_4` theorem gives a rooted
  model unless the relevant four marks occur in one planar cofacial
  order.  The latter is precisely a rural/web state.

What remains is not another decomposition theorem.  It is the labelled
selection statement which chooses four marks so that a rooted `K_4` (or
a crossing in the cycle torso) expands to two disjoint rainbow carriers
or to the rooted two-pool frame completion.  Failure of every such
selection must then be shown to make the cofacial orders globally
compatible.  The theorem above guarantees that this selection problem is
confined to one torso and that every omitted lobe has a named portal
defect and an adhesion of order at most two.

## 4. Audit boundary

The common object is a **bag**, not a common vertex.  Pairwise
intersection of connected subgraphs does not have the Helly property in
an arbitrary graph; Helly is used only after projecting them to the
decomposition tree.  The theorem also does not turn virtual torso edges
into real edges.  Both qualifications are essential when branch sets are
lifted.
