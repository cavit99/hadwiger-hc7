# Audit: atomic four-vertex packet-path classification

**Verdict:** GREEN at frozen hashes

* note: `8bcf05d1e64bd2089301d398e3f3bcf43a2ad806d573f26c0951200b4b863d6e`;
* verifier: `8736b680c3186d93a44ea265d636f4a4e90f84dc1a9456782392a7019e41902c`.

The promoted note differs from the audited draft only in its title, status,
certificate path, and two audit-only typographical repairs: `quad` was
corrected to `\quad`, and the inaccurate phrase “four trace colours” was
replaced by “the displayed trace colouring.”  The promoted verifier differs
only in its relocated dependency path and the added assertion
`classification["with_k5"] == 0`.  No mathematical construction or search
space changed.

The verifier was rerun successfully.  Its frozen output includes

```text
vertices 12 edges 30
connectivity 3
packet_number 2 full_packets 5
blocking_path_uses_both_packet_centres True
K7_model None
K7vee_model None
K5_after_canonical_pair None
trace_legal_extensions 8192
near_free_extension_with_canonical_K5 False
```

and exactly the nine singleton triggers displayed in (3.2).

## 1. Frozen atomic interface

The boundary edges

\[
                 02,23,31,04,45,06
\]

form the stated seven-vertex tree.  Its bipartition is exactly

\[
 I=\{0,3,5\},\qquad J=B\mathbin{\dot\cup}C,
 \quad B=\{1,2\},\quad C=\{4,6\}.
\]

The thin vertex `a` is adjacent to all seven boundary vertices.  Since the
thin shore is the singleton `{a}`, `a0` is indeed its unique edge to the
compulsory literal `u=0`.

The rich induced graph is the path

\[
                         p_0-p_c-q_b-q_0.
\]

After `sparse_atomic_base()` replaces the generic star contacts, its literal
boundary rows are

\[
 N_S(p_c)=\{1\},\quad N_S(p_0)=S-\{1\},\quad
 N_S(q_b)=\{4\},\quad N_S(q_0)=S-\{4\}.
\]

Thus `P={p_c,p_0}` and `Q={q_b,q_0}` are disjoint, connected, adjacent,
and individually `S`-full.

Exhausting the fifteen nonempty subsets of the four rich vertices gives
exactly five connected full packets:

\[
 P,\quad P\cup\{q_b\},\quad Q,\quad Q\cup\{p_c\},
 \quad P\cup Q.
\]

The disjoint pair `P,Q` gives packing number at least two, while direct
inspection of this list gives packing number at most two.

## 2. Exact trace and blocking path

The displayed colouring is proper on the rich closed shore.  In the two
blocking colours, all vertices outside

\[
 B\cup C\cup\{p_c,q_b\}
\]

disappear.  There is no `B-C` boundary edge; `p_c` has the sole relevant
boundary contact `1`, `q_b` the sole relevant contact `4`, and their mutual
edge is literal.  Therefore the unique bichromatic path between the two
named blocks is

\[
                         1-p_c-q_b-4.
\]

It meets both preselected packets.  No path of these two colours confined
to either packet can join `B` to `C`.  Since the partition
`I|B|C` has no singleton blocks, its packet demand is exactly three.

## 3. Base minor exclusions

The base graph is connected, has twelve vertices and thirty edges.  The
restricted-growth partition search returns no spanning `K_7` model, no
spanning `K_7^vee` model, and—after deleting `{a,0}`—no spanning `K_5`
model.

The spanning restriction is exact here.  Both the base graph and the
canonical-pair remainder are connected.  In a connected graph, each
component outside a clique-minor model can be attached wholesale to an
adjacent branch set, extending the model until all vertices are assigned.

The partition generator enumerates every restricted-growth partition into
exactly `k` nonempty blocks.  It checks each block's graph connectivity and
every required interblock adjacency.  In near mode it tries every possible
hub, requires the other six bags to be a clique, and requires at least four
of the six hub spokes; this is exactly `K_7` with at most two missing edges
incident with one hub.  Hence all three exclusions in (2.1) are exact.

The other diagnostic claims also match the frozen graph.  A four-colouring
exists, the vertex connectivity is three, and every one of the twelve
vertices violates the degree-seven Dirac neighbourhood inequality.

## 4. Completeness of the thirteen optional edges

The frozen data are the vertex set, boundary tree, thin/rich separation,
displayed trace colouring, and three rich-path edges.  Relative to those
data, all remaining proper edges fall into the advertised thirteen choices.

* `p_c` has blocking colour `2`, so it cannot meet `C={4,6}`.  Among the
  permitted literals `I union B`, the edge `p_c1` is fixed and the four
  missing contacts are `p_c0,p_c2,p_c3,p_c5`.
* `q_b` has blocking colour `1`, so it cannot meet `B={1,2}`.  The edge
  `q_b4` is fixed and the four missing permitted contacts are
  `q_b0,q_b3,q_b5,q_b6`.
* The spare-coloured leaf `p_0` is already adjacent to every boundary
  literal except `1`, and `q_0` to every literal except `4`.  This gives
  `p_01,q_04`.
* Of the four cross-packet vertex pairs, `p_cq_b` is fixed.  The other
  three trace-proper edges are `p_0q_b,p_cq_0,p_0q_0`.

Additional boundary edges are excluded because the boundary graph is
frozen; thin-rich edges are excluded by the frozen separation; all other
rich-boundary edges are monochromatic or already present.  Thus there are
exactly thirteen independent optional edges and `2^13=8192` extensions.

## 5. Packet filtering and monotonic triggers

For each extension not already certified by a monotone trigger, the script
recomputes all connected full subsets of the four rich vertices and their
maximum disjoint packing.  States whose packet number is not two are
correctly outside Theorem 3.1 and are skipped.

Each of the nine singleton additions

\[
 p_c0,p_c2,p_c3,p_c5,
 q_b0,q_b3,q_b5,q_b6,p_0q_0
\]

has an explicit spanning seven-bag `K_7^vee` partition returned by the
exact checker.  In every returned partition, the missing interbag pairs are
either zero, one, or two pairs sharing one hub.  Adding further edges cannot
destroy connectivity or a branch-set adjacency, so every extension
containing one of these singleton triggers has the near-model outcome.

Avoiding all nine triggers leaves exactly the four edges

\[
                         p_01,q_04,p_0q_b,p_cq_0.
\]

I independently replayed all sixteen subsets.  Every one has rich packet
number exactly two, and every canonical-pair remainder is connected and has
no `K_5` minor under the exact partition search.  The classification routine
returns

```text
checked = 8192
with_k5 = 0
near_triggers = 9 singleton sets
```

so Theorem 3.1 follows.  The promoted verifier now explicitly asserts
`classification["with_k5"] == 0` in `main()`.

## 6. Exact scope of the conclusion

The result is a complete classification only of this frozen four-vertex
rich path and its thirteen trace-legal edge additions.  It proves that a
blocking path through both chosen packets need not itself escape either
packet.  Within this finite language, every extension that destroys the
canonical fixed-pair outcome contains a `K_7^vee` model.

The note correctly does not claim this for larger packets, arbitrary
width-two interiors, strongly contraction-critical responses, or the
unbounded atomic bridge cell.  Its recommendation to move next to a genuine
packet branch is therefore a scope boundary, not a theorem about all such
branches.
