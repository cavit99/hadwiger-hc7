# The Hajós drop-edge barrier in the five-chromatic leaf branch

**Status:** explicit falsifier of any kernel-only unrooted-model lift.  The
construction and all chromatic equalities are checked by
`hc7_leaf_drop_hajos_barrier_verify.py`.

This note tests the five-chromatic branch of the leaf-rooted drop theorem.
It shows that the regenerated `K_5` model avoiding the drop edge cannot, by
itself, yield a `K_7`.  Any valid continuation must use attachment data from
the ambient seven-connected graph, or export a labelled near-`K_7` handoff.

## 1. Construction

Take two copies of `K_6`.  In the first use vertices

\[
                        \{a,u,l_1,l_2,l_3,l_4\},
\]

delete `au`, and in the second use

\[
                        \{a,v,r_1,r_2,r_3,r_4\},
\]

delete `av`.  The two displayed vertices called `a` are identified.  Add
the edge

\[
                              e=uv.
\]

Call the resulting Hajós join `C`.

## 2. It realizes every equality in the five-chromatic branch

The graph `C` is six-chromatic.  Indeed, in every five-colouring of the
left `K_6-au`, the nonadjacent vertices `a,u` must share the fifth colour.
Similarly `a,v` must share one colour on the right.  This conflicts with
the edge `uv`.  A six-colouring is immediate.

Moreover

\[
 \chi(C/uv)=\chi(C-u)=\chi(C-v)=\chi(C-\{u,v\})=5. \tag{2.1}
\]

For the last equality, `C-{u,v}` is exactly two copies of `K_5` sharing
the vertex `a`.  Thus the branch contains a literal `K_5` avoiding both
ends of the drop edge, not merely an abstract `HC_5` model.

After contracting `uv` to `w`, both `a union L` and `a union R` are
literal `K_5` subgraphs, while `w` is nonadjacent to `a` and complete to
`L union R`; colour `a,w` alike and use the other four colours on each of
the two four-cliques.  This proves the first equality in (2.1).  The two
vertex-deletion equalities follow by the same five-colour alignment.

The construction is the ordinary Hajós join of two six-critical graphs;
in particular it is six-critical.  The verifier independently checks
vertex-criticality, which is all that the leaf-rooted critical kernel uses.

## 3. Nevertheless it has no `K_7` minor

There is a tree decomposition with three bags

\[
 \{a,u,l_1,l_2,l_3,l_4\}
 \;--\;
 \{a,u,v\}
 \;--\;
 \{a,v,r_1,r_2,r_3,r_4\}.                           \tag{3.1}
\]

Every edge is covered and the bags containing any fixed vertex form a
connected subtree.  The largest bag has order six, so `tw(C)<=5`.  Since
treewidth is minor-monotone and `tw(K_7)=6`, the graph `C` has no `K_7`
minor.

Consequently the implication

\[
 \begin{gathered}
 C\text{ six-critical},\quad uv\in E(C),\\
 \chi(C/uv)=\chi(C-u)=\chi(C-v)=
 \chi(C-\{u,v\})=5,\\
 C-\{u,v\}\succcurlyeq K_5
 \end{gathered}
 \quad\Longrightarrow\quad C\succcurlyeq K_7
\]

is false in its strongest possible local form.

## 4. What seven-connectivity can legitimately add

The barrier also identifies the correct ambient output.  Suppose the
eleven displayed vertices occur literally in a seven-connected host `G`
with all displayed edges.  Delete `X={a,u,v}`.  By four-connectivity of
`G-X`, Menger gives four vertex-disjoint paths joining the four-set `L` to
the four-set `R`, using every vertex of both sets after truncation.

The four path vertex sets are pairwise adjacent: their `L` endpoints lie
in one four-clique.  Each path bag is adjacent to each of `a,u,v`; use the
`L` endpoint for `a,u` and the `R` endpoint for `v`.  Together with the
three singleton bags `{a},{u},{v}`, these paths form a labelled
`K_7^vee` model whose only missing bag adjacencies are `au` and `av`.

Thus global connectivity repairs the local Hajós join exactly up to the
normalized one-centre/two-hole near-clique.  It does not repair either
missing adjacency automatically.  This is an admissible S1 handoff, not a
literal `K_7` conclusion.

## 5. Exact consequence for the active spine

In the branch `chi(C-{u,v})=5`, the regenerated unrooted `K_5` is not the
next proof object.  The next proof must retain at least one of:

1. the attachments of `C` to the rest of the pre-contraction host;
2. a separator of the five-chromatic residue and the paths forced around
   it by seven-connectivity; or
3. a labelled `K_7^vee` model with the two missing rows tied to the literal
   leaf `u` and the contracted carrier `v`.

Discarding those labels reduces the branch to the counterexample above.
