# A clean forced path and three boundary-full subgraphs do not force a `K_7` minor

**Status:** explicit counterexample to an intermediate claim; deterministic
certificate verifier in
[`hc7_exact7_clean_path_geometry_barrier_verify.py`](hc7_exact7_clean_path_geometry_barrier_verify.py).

## Refuted statement

The following geometry-only assertion is false:

> Let `S=M dotcup {x,y} dotcup K`, where `|M|=2`, `|K|=3`, `M` is
> independent, `K` is a clique, and `xy` is a nonedge.  Suppose an actual
> separation has one boundary-full connected subgraph on one open side and
> two disjoint boundary-full connected subgraphs on the other.  If the second
> side also contains an `x`--`y` path internally disjoint from the latter two
> subgraphs, then the host contains a `K_7` minor.

The counterexample shows that a clean path is not itself an additional
demand-set representative.  Contraction-critical colouring information is
essential.

## Construction

Let

\[
 S=\{m_1,m_2,x,y,k_1,k_2,k_3\},
\]

and put precisely the three edges of the triangle on
`K={k_1,k_2,k_3}` inside `S`.  Add vertices `d,p_1,p_2,w`.  Make each of
`d,p_1,p_2` adjacent to every vertex of `S`, add the four edges

\[
                         xw,\quad wy,\quad wp_1,\quad wp_2,
\]

and add no other edges.

Take the two open sides to be

\[
                         L=\{d\},\qquad R=\{p_1,p_2,w\}.
\]

There is no edge between `L` and `R`.  The singleton `d` is boundary-full,
the singleton subgraphs `p_1,p_2` are disjoint and boundary-full, and `R` is
connected.  The path `x-w-y` has its internal vertex disjoint from
`\{p_1,p_2\}`.  Its internal component contacts no vertex of `K`, so it does
not meet either endpoint demand set.

## No `K_7` minor

The following bags form a tree decomposition:

\[
\begin{aligned}
 C&=\{d,p_1,p_2,k_1,k_2,k_3\},\\
 B&=\{d,p_1,p_2,x,y\},\\
 W&=\{p_1,p_2,x,y,w\},\\
 I_1&=\{d,p_1,p_2,m_1\},\\
 I_2&=\{d,p_1,p_2,m_2\}.
\end{aligned}
\]

Use the decomposition-tree edges

\[
                         CB,\quad BW,\quad CI_1,\quad CI_2.
\]

Every graph edge is covered and the bags containing each vertex form a
connected subtree.  The largest bag has order six, so the graph has treewidth
at most five.  Treewidth is minor-monotone and `K_7` has treewidth six;
therefore this graph has no `K_7` minor.

## Scope not refuted

This eleven-vertex graph is neither seven-connected nor contraction-critical.
Moreover, the displayed six-block boundary partition cannot extend to a
six-colouring in which `d,p_1,p_2` are single boundary-full vertices: each is
adjacent to all six boundary colours.  Thus the example does **not** refute
the demand-set reflection theorem, the exact critical-triangle setup, or
`HC_7`.  It refutes only the shortcut from path/contact geometry to a clique
minor and explains why the proper-minor colouring response must be used.

## Verification

Run:

```text
python3 barriers/hc7_exact7_clean_path_geometry_barrier_verify.py
```

Expected output:

```text
PASS: clean-path geometry; tree decomposition width 5; no K7 minor
```
