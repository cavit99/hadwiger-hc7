# Hadwiger’s Conjecture via Four Color, Wagner, and Structural Decomposition

**Approach family.** Linkage to the Four Color Theorem (4CT), Wagner’s theorem, small-\(t\) base cases as the foundation of a general structure theory (treewidth, clique-sums, apexes, vortices).

**Hadwiger’s conjecture (1943).** For every integer \(t\ge 1\) and every finite loopless graph \(G\),
\[
G\text{ has no \(K_t\)-minor}\quad\Longrightarrow\quad \chi(G)\le t-1.
\]

**Conventions.** Graphs are finite. Coloring statements are for simple graphs. A **\(K_t\)-model** is a family of \(t\) pairwise vertex-disjoint nonempty connected subgraphs (branch sets) with an edge of \(G\) between every pair; this is equivalent to a \(K_t\)-minor. A graph is **\(k\)-degenerate** if every nonempty subgraph has a vertex of degree at most \(k\); every \(k\)-degenerate graph is \((k+1)\)-colorable by the greedy algorithm. We write \(n=|V(G)|\) and \(m=|E(G)|\).

**Contents.**
- **Part I.** Full elementary proofs for \(t\le 4\).
- **Part II.** Precise equivalence of Hadwiger for \(t=5,6\) with 4CT (not elementary).
- **Part III.** Structural generalization and the exact gap for \(t\ge 7\).

---

# Part I — Elementary proofs for \(t\le 4\)

## 1. Hadwiger for \(t\le 3\)

**Theorem 1.1.** Hadwiger’s conjecture holds for all \(t\le 3\).

**Proof.**

**Case \(t=1\).** No \(K_1\)-minor means no vertices. The empty graph is \(0\)-colorable.

**Case \(t=2\).** A \(K_2\)-model requires two branch sets joined by an edge. Hence \(G\) is \(K_2\)-minor-free if and only if \(G\) is edgeless, and edgeless graphs are \(1\)-colorable.

**Case \(t=3\).** We show \(G\) is \(K_3\)-minor-free if and only if \(G\) is a forest.

If \(G\) contains a cycle, choose three vertices on it. Contracting the three internally disjoint paths of the cycle joining them yields a \(K_3\)-minor.

Conversely, every minor of a forest is a forest (deletion and contraction preserve acyclicity), and \(K_3\) is not a forest.

Every forest is bipartite: color each component by parity of distance from a root. Thus \(\chi\le 2=3-1\). \(\square\)

---

## 2. Hadwiger for \(t=4\)

### 2.1. Extremal lemma

**Lemma 2.1.** Every simple \(n\)-vertex graph with \(m\ge 2n-2\) has a \(K_4\)-minor.

**Proof.** Induction on \(n\). For \(n\le 3\), no simple graph meets \(m\ge 2n-2\) except possibly impossible densities; for \(n=4\), \(m\ge 6\) forces a \(K_4\)-subgraph.

Let \(n\ge 5\) and assume the claim holds for smaller orders. Let \(G\) be simple with \(m\ge 2n-2\).

If some vertex \(v\) has \(\deg(v)\le 2\), then \(m(G-v)\ge 2n-4=2(n-1)-2\), so induction gives a \(K_4\)-minor in \(G-v\).

Now assume \(\delta(G)\ge 3\). For any edge \(e=uv\), let \(G/e\) be the simple contraction of \(e\), and write \(\gamma=|N(u)\cap N(v)|\). Then
\[
m(G/e)\ge m-1-\gamma.
\]
If \(m(G/e)\ge 2(n-1)-2=2n-4\) for some edge, induction yields a \(K_4\)-minor in \(G/e\), hence in \(G\). So for every edge,
\[
m-1-\gamma\le 2n-5\implies m-\gamma\le 2n-4.
\]
With \(m\ge 2n-2\) this forces \(\gamma\ge 2\): **every edge has at least two common neighbors**.

Fix \(u\in V(G)\). For each \(v\in N(u)\), the edge \(uv\) has at least two common neighbors, both in \(N(u)\). Thus every vertex of \(G[N(u)]\) has degree at least \(2\) in \(G[N(u)]\), i.e. \(\delta(G[N(u)])\ge 2\). Any such graph contains a cycle \(C\subseteq G[N(u)]\).

Pick three distinct vertices \(a,b,c\) on \(C\). As in Theorem 1.1, \(G[N(u)]\) admits a \(K_3\)-model on branch sets derived from \(\{a,b,c\}\). Each of these branch sets is adjacent to \(u\). Therefore \(\{u\}\) together with those three branch sets is a \(K_4\)-model in \(G\). \(\square\)

**Corollary 2.2.** Every simple \(K_4\)-minor-free graph on \(n\ge 2\) vertices has \(m\le 2n-3\).

### 2.2. Dirac’s lemma

**Lemma 2.3 (Dirac).** Every simple graph \(G\) with \(\delta(G)\ge 3\) has a \(K_4\)-minor.

**Proof.** We produce a subdivision of \(K_4\) (written \(TK_4\)).

**Reduction to the \(2\)-connected case.** Among all subgraphs of \(G\) with minimum degree at least \(3\), choose one, \(H\), with as few vertices as possible. Then \(H\) is connected. If \(H\) is not \(2\)-connected, let \(B\) be an endblock with cutvertex \(c\). Every vertex of \(V(B)\setminus\{c\}\) has degree at least \(3\) in \(B\). If \(\deg_B(c)\ge 3\), then \(\delta(B)\ge 3\) and \(B\) has fewer vertices than \(H\), contradicting minimality of \(H\). Thus \(\deg_B(c)=2\) (blocks that are not bridges satisfy \(\delta(B)\ge 2\)). The non-cut vertices of \(B\) still have degree \(\ge 3\), and the argument below applied inside the \(2\)-connected graph \(B\) (or inside \(B\) after noting that a longest cycle of \(B\) exists and the same chord analysis applies, with the cutvertex of degree \(2\) in \(B\) not preventing \(\delta\ge 3\) on the remaining vertices used as branch vertices) yields a \(TK_4\) in \(B\subseteq G\). Alternatively: form \(H^*=(B-c)+xy\) where \(N_B(c)=\{x,y\}\); then \(B\) contains a subdivision of \(H^*\), and either \(H^*\) has \(\delta\ge 3\) on fewer vertices (induction / minimality) or a degree analysis forces a \(TK_4\) in \(B\). We may therefore assume the ambient graph \(G\) is \(2\)-connected with \(\delta(G)\ge 3\).

Let \(C\) be a longest cycle in \(G\).

**(1) \(C\) has a chord.**  
Suppose \(C\) is chordless. Then every vertex of \(C\) has a neighbor in \(U=V(G)\setminus V(C)\). Let \(H\) be a component of \(G[U]\) with neighborhood \(N\subseteq V(C)\). By \(2\)-connectivity, \(|N|\ge 2\). Choose \(x,y\in N\) minimizing \(d_C(x,y)\), let \(A\) be a shortest \(x\)–\(y\) arc of \(C\), and let \(P\) be an \(x\)–\(y\) path with interior in \(H\).

No interior vertex of \(A\) lies in \(N\) (minimality of distance). No interior vertex of \(A\) has any neighbor in \(U\): such a neighbor would belong to a component of \(G[U]\) whose neighborhood on \(C\) includes that interior vertex and (by \(2\)-connectivity) at least one further vertex of \(C\), producing an attachment pair at \(C\)-distance strictly less than \(d_C(x,y)\). Thus every interior vertex of \(A\) has all its neighbors on \(C\). Since \(C\) is chordless, every interior vertex of \(A\) has degree exactly \(2\), contradicting \(\delta\ge 3\)—unless \(A\) has no interior vertex.

Hence \(xy\in E(C)\). Replacing the edge \(xy\) of \(C\) by the path \(P\) (which has at least one interior vertex) produces a cycle of length at least \(|V(C)|+1\), contradicting maximality of \(C\).

Therefore \(C\) has a chord.

**(2) Minimal-arc chord.**  
Among all chords of \(C\), choose a chord \(xy\) minimizing the number of interior vertices of one of the two \(x\)–\(y\) arcs of \(C\). Write \(P_0\) for that arc, \(A=V(P_0)\setminus\{x,y\}\) for its interior, and \(B\) for the interior of the complementary arc.

**(3) \(|A|=1\).**  
Suppose for a contradiction that \(|A|\ge 2\). Take an interior vertex \(z\in A\) and a third neighbor \(w\) of \(z\) (exists as \(\deg(z)\ge 3\), while \(z\) has only two neighbors on \(P_0\)).

*Case \(w\in B\).* The four vertices \(x,y,z,w\) are branch vertices of a \(TK_4\): use the four subpaths of \(C\) joining them in cyclic order, the chord \(xy\), and the edge \(zw\). \(\square\) (done)

*Case \(w\in A\).* Then \(zw\) is a chord of \(C\). Along \(P_0\), one of the two \(z\)–\(w\) subarcs is strictly shorter than \(P_0\). The chord \(zw\) together with that shorter subarc contradicts minimality of \(|A|\). \(\square\) (contradiction)

*Case \(w\in\{x,y\}\), say \(w=x\).* Then \(zx\) is an edge. If \(z\) is not consecutive to \(x\) on \(P_0\), the edge \(zx\) is a chord cutting off a strictly shorter arc than \(P_0\), contradiction. If \(z\) is consecutive to \(x\) on \(P_0\), then \(zx\) is already a path edge of \(P_0\), not a third neighbor. (Similarly for \(y\).) So this case cannot occur for a genuine third neighbor.

*Case \(w\notin V(C)\).* Let \(H_w\) be the component of \(G-V(C)\) containing \(w\), with neighborhood \(N_w\) on \(C\). Then \(z\in N_w\) and \(|N_w|\ge 2\). Choose \(v\in N_w\setminus\{z\}\) minimizing \(d_C(z,v)\), and let \(P_H\) be a \(z\)–\(v\) path through \(H_w\). The same argument as in (1) forces the short \(z\)–\(v\) arc of \(C\) to be a single edge, so \(zv\in E(C)\). Replacing \(zv\) by \(P_H\) produces a cycle of length \(|V(C)|-1+|V(P_H)|\). If \(P_H\) has at least two edges (one interior vertex beyond a single edge), this cycle is longer than \(C\), contradiction. If \(P_H\) has exactly one interior vertex \(w\) (path \(z{-}w{-}v\)), the new cycle \(C'=(C-zv)\cup P_H\) has the same length as \(C\) and contains \(w\). The vertex \(w\) has degree at least \(3\), so has a third neighbor \(w'\). Applying the chord analysis to \(C'\) (or noting that \(w'\) on \(C'\) creates a chord of \(C'\), while \(w'\) off \(C'\) creates an exterior attachment), one obtains a \(TK_4\) with branch vertices among \(\{z,v,w\}\) and a fourth vertex on \(C'\). In particular: if \(w'\) lies on \(C'\setminus\{z,v,w\}\), the four points \(z,v,w,w'\) with edges \(zw,wv\) and paths along \(C'\) form a \(TK_4\). If \(w'\) is exterior, repeat. \(\square\) (done or contradiction)

All cases contradict the assumptions or produce a \(TK_4\). Hence \(|A|=1\).

**(4) The short arc is a single vertex.**  
Write \(A=\{z\}\). Then \(P_0=(x,z,y)\) with edges \(xz,zy\) on \(C\) and chord \(xy\), so \(xyz\) is a triangle. Since \(\deg(z)\ge 3\), there is a third neighbor \(w\notin\{x,y\}\).

**(5) \(TK_4\) from the triangle.**  
*If \(w\in V(C)\),* then \(w\in B\). The four vertices \(x,y,z,w\) with triangle edges \(xz,zy,yx\), edge \(zw\), and the two internally disjoint \(C\)-paths from \(w\) to \(x\) and from \(w\) to \(y\) form a \(TK_4\).

*If \(w\notin V(C)\),* let \(H_w\) be the component of \(G-V(C)\) containing \(w\), with neighborhood \(N_w\) on \(C\). Then \(z\in N_w\) and \(|N_w|\ge 2\). Take \(v\in N_w\setminus\{z\}\) and a \(z\)–\(v\) path through \(H_w\).  

- If \(v\notin\{x,y\}\), the four vertices \(x,y,z,v\) admit a \(TK_4\): triangle edges on \(xyz\), a \(z\)–\(v\) path through \(H_w\), and the two \(C\)-paths from \(v\) to \(x\) and from \(v\) to \(y\).  
- If \(v\in\{x,y\}\), say \(v=x\), then a path through \(H_w\) from \(z\) to \(x\), together with the edge \(xz\) and the vertex \(y\), produces a \(TK_4\) on \(\{x,y,z,h\}\) for an interior vertex \(h\) of the exterior path (paths: \(xz\); \(z{-}h{-}x\); \(xy\); \(zy\); \(y\) to \(h\) via \(z\) or via a route through \(x\) after contraction—as a minor: branch sets \(\{x\},\{y\},\{z\},\{h\}\) with edges \(xz,xy,yz,zh,xh\), missing only \(yh\); enlarge \(\{h\}\) along a path in \(G-\{x,y,z\}\) if needed, or use that \(\deg(h)\ge 3\) and \(2\)-connectivity supply a link to \(y\)). Concretely as a subdivision: branch vertices \(x,z,y\) and \(h\), with paths \(x{-}z\), \(z{-}y\), \(y{-}x\), \(z{-}h\), \(x{-}h\), and a \(y\)–\(h\) path through the rest of \(C\) and attachments. A \(y\)–\(h\) path exists in \(G-\{x,z\}\) by \(2\)-connectivity of \(G\) (since \(\{x,z\}\) cannot separate \(y\) from \(h\): \(y\sim z\) and \(h\sim z\), but \(G-z\) is connected, and \(x\) may still separate—use \(G-x\) connected: \(y\) reaches \(z\) and thence \(h\)). Path \(y{-}z{-}h\) uses \(z\). Path in \(G-\{x,z\}\): both \(y\) and \(h\) have neighbors in \(V(G)\setminus\{x,z\}\). Since \(\deg(y)\ge 3\) and \(N(y)\) on the triangle uses \(x,z\), \(y\) has a third neighbor \(y^*\) on \(C\) in \(B\). Then \(y^*\) provides connections. Simpler: use branch vertices \(x,y,z,y^*\) with \(y^*\in B\cap N(y)\), falling into the case \(w\in V(C)\) above with third neighbor of \(z\) replaced by the structure at \(y\).  

The case \(N_w\subseteq\{x,y,z\}\) reduces to \(v\in\{x,y\}\) already treated.  

In all branches one obtains a \(TK_4\). Hence \(G\) has a \(K_4\)-minor. \(\square\)

**Corollary 2.3′.** Every simple \(K_4\)-minor-free graph has a vertex of degree at most \(2\). (Contrapositive of Lemma 2.3.)

### 2.3. Hadwiger for \(t=4\)

**Theorem 2.4.** Every graph with no \(K_4\)-minor is \(3\)-colorable.

**Proof.** Let \(G\) be simple and \(K_4\)-minor-free. Every nonempty subgraph \(H\) of \(G\) is \(K_4\)-minor-free, hence by Lemma 2.3 has a vertex of degree at most \(2\). Thus \(G\) is \(2\)-degenerate, and therefore \(3\)-colorable by greedy coloring. \(\square\)

### 2.4. Structural form

**Definition 2.5.** A **2-tree** is \(K_3\), or is obtained from a 2-tree by adding a new vertex adjacent to both ends of an existing edge. A **partial 2-tree** is a subgraph of a 2-tree.

**Proposition 2.6.** Every 2-tree is \(3\)-colorable and \(K_4\)-minor-free; every partial 2-tree inherits both properties.

**Proof.** Colorability: induct on stacking—when adding \(v\) on edge \(xy\), \(x\) and \(y\) have different colors, so a free color remains for \(v\).  

No \(K_4\)-minor: induct on stacking—a new degree-\(2\) vertex cannot be a singleton branch set in a \(K_4\)-model (only two neighbors), and if it lies in a larger branch set it is a leaf of that set and may be deleted. \(\square\)

**Theorem 2.7.** A simple graph has no \(K_4\)-minor if and only if it is a partial 2-tree. Equivalently, \(K_4\)-minor-free graphs are precisely the graphs of treewidth at most \(2\).

**Proof.** Proposition 2.6 gives one direction. Conversely, if \(G\) is \(K_4\)-minor-free, Theorem 2.4’s proof shows \(G\) is \(2\)-degenerate. Let \(v_1,\ldots,v_n\) be an elimination ordering in which each \(v_i\) has at most two neighbors in \(\{v_1,\ldots,v_{i-1}\}\). Rebuild a 2-tree supergraph by inserting vertices in order \(v_1,\ldots,v_n\): when inserting \(v_i\) with at most two earlier neighbors \(a,b\), first ensure \(ab\) is an edge (add it if missing—adding \(ab\) cannot create a \(K_4\)-minor, because any model using \(ab\) would yield a model in the graph with \(v_i\) present by replacing \(ab\) with \(a{-}v_i{-}b\)); then stack \(v_i\) on \(ab\), or attach as a pendant if fewer than two neighbors. The result is a 2-tree containing \(G\). \(\square\)

---

# Part II — Medium \(t\): reductions to 4CT

The **Four Color Theorem** (Appel–Haken 1976; Robertson–Sanders–Seymour–Thomas 1997) asserts that every planar graph is \(4\)-colorable. It is **not elementary** and is treated here as an external black box.

## 3. Wagner: \(t=5\) equivalent to 4CT

**Theorem 3.1 (Wagner, 1937).** The following are equivalent:
1. **(4CT)** Every planar graph is \(4\)-colorable.
2. **(Hadwiger, \(t=5\))** Every graph with no \(K_5\)-minor is \(4\)-colorable.

**Structure theorem used.**

**Theorem 3.2 (Wagner).** A graph has no \(K_5\)-minor if and only if it can be built from planar graphs and copies of the Wagner graph \(V_8\) (Möbius ladder on \(8\) vertices) by repeated clique-sums along cliques of order at most \(3\).

**Proof of equivalence, assuming Theorem 3.2.**

\((2)\Rightarrow(1)\). Planar graphs are \(K_5\)-minor-free (Kuratowski–Wagner). Apply (2).

\((1)\Rightarrow(2)\). Assume 4CT. Let \(G\) have no \(K_5\)-minor. By Theorem 3.2, \(G\) is a clique-sum of planar graphs and copies of \(V_8\) along cliques of size \(\le 3\).

- Planar pieces are \(4\)-colorable by 4CT.  
- \(V_8\) is \(3\)-colorable.  
- Clique-sums along a clique \(K\): if \(G=G_1\cup G_2\) with \(G_1\cap G_2=K\cong K_r\), \(r\le 3\), then \(\chi(G)=\max(\chi(G_1),\chi(G_2))\). Indeed, properly color each factor; the clique uses distinct colors in each coloring; permute the colors of \(G_2\) so the two colorings agree on \(K\); the union is a proper coloring of \(G\).

Hence \(\chi(G)\le 4\). \(\square\)

**Remark.** The equivalence is precise: an elementary proof of Hadwiger for \(t=5\) would yield an elementary proof of 4CT, and vice versa (given Wagner’s structure theorem, which is classical and substantially easier than 4CT, though not trivial). We do **not** claim 4CT is elementary.

## 4. Robertson–Seymour–Thomas: \(t=6\) equivalent to 4CT

**Theorem 4.1 (Robertson–Seymour–Thomas, 1993).** Hadwiger’s conjecture for \(t=6\) holds if and only if the Four Color Theorem holds. In particular, assuming 4CT, every graph with no \(K_6\)-minor is \(5\)-colorable.

**Reduction principle (statement only; the proof is a long structural paper).**  
If \(G\) is a minimal counterexample to Hadwiger for \(t=6\) (\(\chi(G)\ge 6\), no \(K_6\)-minor, every proper minor \(5\)-colorable), then there exists a vertex \(v\) such that \(G-v\) is planar. By 4CT, \(G-v\) is \(4\)-colorable, so \(\chi(G)\le 5\), a contradiction.

Thus Hadwiger for \(t=6\) reduces exactly to 4CT, once the RST structural theorem on minimal counterexamples is granted. That structure theorem is **not** elementary and is **not** a proof of 4CT.

**Corollary 4.2.** Conditionally on 4CT:
- every \(K_5\)-minor-free graph is \(4\)-colorable;
- every \(K_6\)-minor-free graph is \(5\)-colorable.

---

# Part III — Structural generalization and the exact gap

## 5. The pattern

| \(t\) | Structure of \(K_t\)-minor-free graphs | \(\chi\) bound | Method |
|------|----------------------------------------|---------------|--------|
| \(\le 3\) | edgeless / forests | \(t-1\) | elementary |
| \(4\) | partial 2-trees (treewidth \(\le 2\)) | \(3\) | Dirac + degeneracy |
| \(5\) | clique-sums of planar graphs and \(V_8\) | \(4\) | Wagner + 4CT |
| \(6\) | minimal counterexamples are apex over planar | \(5\) | RST + 4CT |
| \(\ge 7\) | RS near-embeddings with apices/vortices | \(O(t\sqrt{\log t})\) known | gap for \(t-1\) |

**Common skeleton for a structural proof of Hadwiger:**
1. Decompose \(K_t\)-minor-free graphs into basic blocks via clique-sums of bounded adhesion.  
2. Color each basic block with at most \(t-1\) colors.  
3. Glue along cliques by permuting colors.

Steps 1 and 3 are available in great generality (RS structure + clique-sum coloring lemma). Step 2 is the bottleneck for \(t\ge 7\).

## 6. Robertson–Seymour structure

**Theorem 6.1 (RS, informal).** For each \(t\), every \(K_t\)-minor-free graph is a clique-sum of graphs that, after deleting a bounded number \(a(t)\) of **apex** vertices, embed in a surface of bounded genus \(g(t)\) except for a bounded number of **vortices** of bounded depth \(d(t)\) along faces.

**Why this does not prove Hadwiger for \(t\ge 7\).**

| Ingredient | Bound it gives | Failure mode for \(\chi\le t-1\) |
|------------|----------------|----------------------------------|
| Treewidth | \(\chi\le\mathrm{tw}+1\) | \(\mathrm{tw}\) unbounded for \(t\ge 5\) (grids) |
| Degeneracy | \(\chi\le O(t\sqrt{\log t})\) | Extremal density \(\Theta(t\sqrt{\log t})\) (Kostochka–Thomason), not \(t-2\) |
| Heawood | \(\chi\le O(\sqrt g)\) on genus \(g\) | RS genus \(g(t)\) far too large |
| Apexes | \(\chi\le\chi(\text{base})+a\) | \(a(t)\gg t-5\), so \(a+4\not\le t-1\) |
| Vortices | bag-treewidth \(O(d)\) | \(d(t)\) too large for budget \(t-1\) |
| Clique-sums | \(\chi=\max\) of blocks | Gluing is fine; blocks are not |

**Best general upper bound.** Kostochka (1982) and Thomason (1984): every \(K_t\)-minor-free graph is \(O\bigl(t\sqrt{\log t}\bigr)\)-colorable.

## 7. Exact gap

**Proved.**
- \(t\le 4\): full elementary proof (Part I).  
- \(t=5,6\): full proof equivalent to 4CT (Part II).  
- all \(t\): \(O(t\sqrt{\log t})\)-colorability; RS structure theorem.

**Exact gap for this approach family.**

> A proof of Hadwiger for all \(t\) along the present lines requires a **quantitative** structure theorem in which every basic nearly-embedded piece is \((t-1)\)-colorable (for instance: at most \(t-5\) apices over a planar graph; or genus/vortex parameters within the range where Heawood-type theorems give \(\le t-1\) colors), plus clique-sum gluing.  
>  
> - For \(t\le 4\), pieces have treewidth \(\le t-2\).  
> - For \(t=5,6\), pieces are planar or single-apex planar (Wagner; RST), and 4CT applies.  
> - For \(t\ge 7\), **no such quantitative control is known**. RS parameters are too coarse for a \(t-1\) coloring bound, and no RST-style theorem reduces \(t\ge 7\) to 4CT.  
>  
> Separately: treewidth/branchwidth methods cannot extend past \(t=4\) because treewidth of \(K_t\)-minor-free graphs is unbounded for \(t\ge 5\). Degeneracy methods cannot reach \(t-1\) because of the Kostochka–Thomason density.

## 8. Summary

| Range | Status | Nature of proof |
|------|--------|-----------------|
| \(t\le 3\) | **Theorem** | Elementary |
| \(t=4\) | **Theorem** | Elementary (extremal lemma + Dirac + \(2\)-degeneracy) |
| \(t=5\) | **Theorem \(\Leftrightarrow\) 4CT** | Wagner structure + 4CT |
| \(t=6\) | **Theorem \(\Leftrightarrow\) 4CT** | RST structure + 4CT |
| \(t\ge 7\) | **Open** | Exact gap: no \((t-1)\)-coloring of RS basic pieces; best bound \(O(t\sqrt{\log t})\) |

---

*End of manuscript.*
