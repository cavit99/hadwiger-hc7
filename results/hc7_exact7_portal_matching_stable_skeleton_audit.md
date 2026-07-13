# Independent audit: Tutte stabilization of portal skeletons

**Status:** the unrestricted finite-witness claim is **RED**.  The corrected
pure-Moser exterior-component application below is **GREEN**.  In particular,
the application is justified by a separator-matching lemma that forces at
least four distinct portal witnesses, and hence at least three segments.

**Duplication note.**  The separator--component matching lemma below was
already proved in this repository as Theorem 1.1 of
`results/hc7_exact7_portal_rooted_k4.md` (using Hall deficiency rather than
Konig's vertex-cover form).  The new contribution here is the stable-tree
application, not the portal-matching statement itself.

## 1. Exact external input

For a subgraph `F` of a graph `C`, fix a set `X` of branch vertices containing
every vertex of `F` of degree at least three.  The segments are the nontrivial
paths between consecutive members of `X`.  An `F`-bridge is either

* an edge outside `F` with both ends in `F`, or
* a component of `C-V(F)`, together with all of its edges to `F`.

Its attachments are its vertices in `F`.  A bridge is 2-stable when no one
segment contains all of its attachments.  This is the precise formulation:
when segments share a branch endpoint, merely saying that the attachments
"meet two segments" is weaker and is not equivalent.

The stable-bridges theorem used here is Tutte's theorem as stated in Paul
Wollan, *Bridges in Highly Connected Graphs*, SIAM J. Discrete Math. 24
(2010), 1731--1741, Theorem 1.1, DOI `10.1137/070710214`: in a 3-connected
ambient graph, a segment system can be rerouted with the same segment
endpoints so that every bridge of the rerouted system is 2-stable.  We use
only the path-system specialization with **at least three segments**.  In
that formulation a path system consists of paths that may share common
endpoints but have no other common vertices; the returned equivalent path
system has the same endpoint pair for each indexed path.

The allowance of shared endpoints is essential here and is part of the
segment formulation: distinct segments of a tree meet at their common
skeleton endpoint.  Since the returned paths are again a path system, no
new internal intersection or unintended shared endpoint is introduced.
There is no requirement that a declared branch vertex have degree at least
two: the branch set must contain all degree-at-least-three vertices and may
also contain leaves and degree-two vertices.  We declare all tree leaves and
all selected degree-two witnesses, so the listed segments cover the whole
tree.

## 2. Why the unrestricted claim is false

Take `C=K_4`, choose adjacent vertices `u,v`, let the witness set be
`W={u,v}`, and let `T=uv`.  This is an inclusion-minimal tree containing the
distinct witnesses and it has one skeleton segment.

Any rerouting with the same abstract tree is a `u-v` path `T*`.  The graph
`K_4` is not itself a path, so `T*` has an ambient bridge: if `T*` is
spanning, an unused edge is a trivial bridge; if it is not spanning, an
off-path component gives a nontrivial bridge.  Every attachment of every
such bridge lies on the sole segment.  Thus not every bridge can be
2-stable.

This is the smallest possible ambient counterexample, since `K_4` is the
smallest 3-connected simple graph.  A singleton skeleton has no segment and
the stated bridge condition is vacuous, but the named path-system theorem
does not apply and it supplies no geometric information there.  The genuine
failure begins with one segment.

## 3. Separator incidence forces distinct portals

### Lemma 3.1 (separator--component matching)

Let `G` be `k`-connected, let `S` have order `k`, and let `C` be a component
of `G-S`.  Suppose that

\[
                 V(G)\setminus (S\cup V(C))\ne\varnothing.
\]

In the bipartite graph consisting of the literal edges between `S` and
`C`, there is a matching of order

\[
                         \min\{k,|C|\}.
\]

#### Proof

Suppose the maximum matching has order
`r<min{k,|C|}`.  By Konig's theorem the incidence graph has a vertex cover
`A union B`, where `A subseteq S`, `B subseteq V(C)`, and
`|A|+|B|=r`.

The inequality `r<|C|` leaves a vertex of `C-B`; take a component `D` of
`C-B`.  Since `A union B` covers every `S-C` edge, `D` has no neighbour in
`S-A`.  Since `C` is a component of `G-S`, it has no neighbour outside
`S union C`.  Therefore `A union B` separates `D` from the assumed nonempty
far side.  But `|A union B|=r<k`, contradicting `k`-connectivity. `square`

The same separation argument, applied to `N_G(C) subseteq S`, also gives
`N_G(C)=S`.  Hence every literal member of `S` has a portal in `C`, not only
the four or more vertices saturated by the matching.

## 4. Corrected portal-stabilization theorem

### Theorem 4.1 (stable portal tree behind a full separator)

Let `G,S,C` satisfy Lemma 3.1, assume `|C|>=4`, and assume that the graph
`G[C]` is 3-connected.  Then one can choose a portal witness

\[
                    p(s)\in N_G(s)\cap V(C)\qquad(s\in S)
\]

and a tree `T* subseteq G[C]` containing all selected witnesses such that:

1. `T*` is a subdivision of the same abstract tree as an inclusion-minimal
   tree through the selected witnesses; and
2. the attachment set of every `T*`-bridge in `G[C]` is not contained in
   any one skeleton segment.

Here every selected witness, including a selected degree-two vertex, is
declared to be a skeleton vertex.

#### Proof

Lemma 3.1 supplies four independent incidence edges

\[
                        s_i p_i\quad (1\le i\le4),
\]

with the `s_i` distinct and the `p_i` distinct.  Set `p(s_i)=p_i`.  Since
`N_G(C)=S`, choose an arbitrary portal witness in `C` for every remaining
member of `S`.  The set of distinct selected witnesses therefore has order
at least four.

Let `T` be an inclusion-minimal tree in `G[C]` containing the distinct
selected witnesses.  Declare every witness and every vertex of `T` of
degree different from two to be a skeleton vertex.  Suppressing the open
degree-two, nonwitness subpaths gives an abstract tree on at least four
skeleton vertices, hence at least three skeleton edges.  Those edges
correspond exactly to at least three nontrivial, pairwise internally
disjoint segments of `T`.

Apply Tutte's stable-bridges theorem in the 3-connected ambient graph
`G[C]`.  It returns one path for every segment, with the same two endpoints,
and the returned paths form a path system.  Their endpoint-incidence graph
is the same abstract tree, so their union `T*` is a subdivision of that
tree.  Every selected portal witness was declared a segment endpoint and
therefore remains in `T*`.  Thus `T*` is still `S`-full.

The theorem also says that every bridge is 2-stable.  This includes trivial
edge bridges, so an ambient chord with both ends on one segment is not an
exception.  If there are no bridges the conclusion is simply vacuous.
`square`

## 5. Exact HC7 application and composition verdict

In the pure-Moser setting take `S=N_G(v)`.  For an exterior component `C`
of `G-N_G[v]`, the vertex `v` itself lies on the far side of the separation
`(S,C)`.  Thus Lemma 3.1 applies in the 7-connected graph `G`.  The audited
Moser low-cut theorem says that every such exterior component of order at
least four is 3-connected.  Theorem 4.1 therefore applies to every
order-at-least-four exterior component.

This genuinely eliminates, in one simultaneous rerouting, every bridge
whose attachments are confined to one segment of the selected portal tree.
It therefore supplies the desired global replacement for repeated local
one-segment rotations **inside that component**.  If another full packet
lies in a different exterior component, disjointness is automatic because
the rerouting remains in `C`.

It does not prove that the stable bridges form a rooted `K_5`, a reserved
connector, or a nonrural crossing.  A bridge may still attach to two or more
segments in a web-like pattern.

For two packet trees lying in the **same** 3-connected ambient shore, every
object whose disjointness must be preserved has to be included in the one
path system before applying Tutte.  If the combined forest has at least
three segments, preservation of indexed endpoints makes the returned union
a subdivision of the same two-component abstract forest, so the two packet
trees remain disjoint.  The theorem cannot be applied only to the first
tree and then assumed to avoid a reserved second tree.

Accordingly, the unrestricted simultaneous statement recorded in
`../barriers/hc7_exact7_tutte_single_segment_barrier.md` would need an explicit
"at least three combined segments" hypothesis unless a separate incidence
argument supplies it.  Lemma 3.1 supplies that hypothesis for an actual
pure-Moser exterior component, but not for an arbitrary selected packet
subgraph of a rich shore.
