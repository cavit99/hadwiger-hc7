# Three boundary-full subgraphs and one defect-two subgraph do not force a `K_7` minor

**Status:** explicit barrier to an intermediate order-eight quotient claim;
separate internal audit GREEN.  This note does not concern a hypothetical
counterexample to `HC_7`.

## 1. The false claim

The following statement is false.

> Let `S` be a set of eight vertices in a graph.  Suppose that the graph
> contains four pairwise vertex-disjoint connected subgraphs, disjoint from
> `S`, of which three are adjacent to every vertex of `S` and the fourth is
> adjacent to at least six vertices of `S`.  Then the subgraph consisting of
> `S` and those four connected subgraphs contains a `K_7` minor.

The counterexample below remains inside the residual boundary class from
the order-eight three-component classification: its boundary is
three-colourable, has no clique odd-cycle transversal, and has no `K_4`
minor supported on six boundary vertices.

## 2. Construction

Let

\[
 S=\{a,a_1,a_2,b,b_1,b_2,r,s\}.
\]

On `S`, take exactly two disjoint triangles

\[
        aa_1a_2a \qquad\text{and}\qquad bb_1b_2b,
\]

with `r` and `s` isolated.  Thus

\[
                         H:=Q[S]\cong 2K_3\mathbin{\dot\cup}2K_1.
\tag{2.1}
\]

Add four further vertices `x_1,x_2,x_3,p`.  Make each `x_i` adjacent to
every vertex of `S`.  Make `p` adjacent precisely to

\[
                         S-\{a,b\}.
\tag{2.2}
\]

There are no edges among `x_1,x_2,x_3,p`, and these are all the edges of
`Q`.

The four singleton subgraphs `\{x_1\},\{x_2\},\{x_3\},\{p\}` are connected
and pairwise disjoint.  The first three are adjacent to all eight boundary
vertices, while the last misses exactly the two vertices `a,b`.

The graph `H` is three-colourable and nonbipartite.  It has no clique
odd-cycle transversal: every clique meets vertices of at most one of its
two triangle components, so the other triangle survives.  It is
`K_4`-minor-free, and therefore deleting any two boundary vertices cannot
leave a `K_4` minor.  Hence `H` satisfies all boundary-only residual
conditions used in the order-eight three-component classification.

## 3. A width-five tree decomposition

Put

\[
                         R=Q[S\cup\{p\}].
\]

The following bags form a tree decomposition of `R`:

\[
\begin{aligned}
 A_0&=\{a,a_1,a_2\},       & A_1&=\{p,a_1,a_2\},\\
 B_1&=\{p,b_1,b_2\},       & B_0&=\{b,b_1,b_2\},\\
 R_r&=\{p,r\},             & R_s&=\{p,s\}.
\end{aligned}
\tag{3.1}
\]

Join the first four bags in the path

\[
                         A_0-A_1-B_1-B_0
\tag{3.2}
\]

and attach each of `R_r,R_s` as a leaf at `A_1`.  Every edge of `R` lies
in one of these bags, and the bags containing any fixed vertex form a
connected subtree.  All bags have order at most three, so

\[
                            \operatorname{tw}(R)\le2.
\tag{3.3}
\]

Add `x_1,x_2,x_3` to every bag in (3.1).  The resulting bags cover every
edge of `Q`: each `x_i` occurs with every boundary vertex, and all old
edges were already covered.  The running-intersection property is
preserved, and every bag now has order at most six.  Therefore

\[
                            \operatorname{tw}(Q)\le5.
\tag{3.4}
\]

Treewidth is minor-monotone and `\operatorname{tw}(K_7)=6`.  Equation
(3.4) proves that `Q` has no `K_7` minor.

## 4. Exact scope

This construction disproves any order-eight completion argument that uses
only the four connected-subgraph contact sets stated in Section 1.  In
particular, a fourth connected subgraph missing at most two boundary
vertices cannot be treated as an unconditional replacement for a fourth
boundary-full component.

The graph `Q` is not a hypothetical counterexample to `HC_7`.  In
particular:

* `Q` is not seven-connected: each of `r,s` has degree four;
* `Q` is six-colourable, as already follows from its width-five tree
  decomposition;
* `Q` is not seven-contraction-critical; and
* the construction carries no operation-specific proper-minor colouring
  response or prescribed branch-set labels.

Thus the example does not refute a theorem that additionally uses
seven-connectivity, contraction-criticality, or the internal structure of
one of the four connected subgraphs.  It shows that at least one such
host-level input is indispensable.

## 5. Computational context

The research probe
[`hc7_order8_three_full_defect2_probe.py`](hc7_order8_three_full_defect2_probe.py)
tests the analogous twelve-vertex quotients over the 82 residual boundary
types.  Its exact minor search finds 62 `K_7`-free quotients, all with a
defect-two fourth vertex.  The graph above is the sparsest boundary type
in that list, with graph6 code

```text
G?`CQG
```

This finite observation motivated the construction, but the proof in
Section 3 is independent of the computation.
