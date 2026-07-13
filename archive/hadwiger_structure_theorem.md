# Structural Graph Theory and Hadwiger’s Conjecture

## Approach family: Graph Minors Structure Theorem, tree-decompositions, clique-sums

**Verdict (Outcome B).** The Robertson–Seymour Graph Minors Structure Theorem yields a finite chromatic bound for every fixed \(K_t\)-minor-free class, by assembling colourings of nearly-embeddable torsos along clique-sums. It does **not** yield the Hadwiger bound \(\chi\le t-1\).

The **exact obstruction** is isolated below: after clique-sum assembly is shown to be colouring-safe, Hadwiger reduces entirely to \((t-1)\)-colouring nearly-embeddable pieces; elementary colouring of those pieces incurs an **apex additive gap** of size \(|A|\) (and secondary **vortex-depth** and **Heawood** costs) that the structure theorem’s parameters do not close, and that cannot be upgraded to a Hadwiger-parameter reduction without universal joins or a recolouring theorem comparable in strength to Hadwiger itself.

All structural colouring lemmas used in the assembly are proved in full. Classical external inputs are named and not reproved (Four Colour Theorem, Heawood’s theorem, Robertson–Seymour structure theorem).

---

## 1. Definitions and statement of Hadwiger

### 1.1. Minors and colouring

**Definition 1.1 (Minor).** A graph \(H\) is a *minor* of a graph \(G\) if \(H\) can be obtained from a subgraph of \(G\) by contracting edges. Equivalently: there exist pairwise disjoint nonempty connected *branch sets* \(B_v\subseteq V(G)\) for \(v\in V(H)\) such that for every edge \(uv\in E(H)\) there is an edge of \(G\) with one end in \(B_u\) and one end in \(B_v\).

**Definition 1.2 (Hadwiger number).** The *Hadwiger number* \(h(G)\) is the largest integer \(t\) such that \(K_t\) is a minor of \(G\).

**Conjecture 1.3 (Hadwiger).** For every graph \(G\),
\[
\chi(G)\le h(G).
\]
Equivalently: every graph with no \(K_t\) minor is \((t-1)\)-colourable.

Write \(\mathcal{F}_t\) for the class of graphs with no \(K_t\) minor.

**Remark 1.4 (Known cases, orientation only).** Cases \(t\le 6\) are settled. This note concerns the general structural attack, not small-\(t\) case analysis.

### 1.2. Tree-decompositions, torsos, clique-sums

**Definition 1.5 (Tree-decomposition).** A *tree-decomposition* of \(G\) is a pair \((T,\mathcal{B})\) where \(T\) is a tree and \(\mathcal{B}=(B_x)_{x\in V(T)}\) is a family of bags \(B_x\subseteq V(G)\) such that:
1. \(\bigcup_x B_x=V(G)\);
2. every edge of \(G\) is contained in some bag;
3. for every \(v\in V(G)\), the nodes \(\{x:v\in B_x\}\) induce a connected subtree of \(T\).

The *adhesion* of an edge \(xy\in E(T)\) is \(B_x\cap B_y\).

**Definition 1.6 (Torso).** Given \((T,\mathcal{B})\) and \(x\in V(T)\), the *torso* \(\tau(B_x)\) is the graph on vertex set \(B_x\) obtained from \(G[B_x]\) by making every adhesion \(B_x\cap B_y\) (over neighbours \(y\) of \(x\) in \(T\)) into a clique.

**Definition 1.7 (Clique-sum).** A *\(k\)-clique-sum* of graphs \(G_1,G_2\) is any graph obtained by identifying a \(k\)-clique of \(G_1\) with a \(k\)-clique of \(G_2\) and then optionally deleting any subset of the edges of the shared clique.

**Fact 1.8.** Graphs admitting a tree-decomposition with clique adhesions are precisely the graphs built by iterated clique-sums from their torsos (up to optional deletion of adhesion edges). We use both languages interchangeably.

### 1.3. Surfaces, vortices, near-embeddability

**Definition 1.9 (Euler genus).** The *Euler genus* \(\mathrm{eg}(\Sigma)\) is \(2h\) for the orientable surface of genus \(h\), and \(k\) for the non-orientable surface with \(k\) crosscaps.

**Definition 1.10 (Vortex of depth \(\theta\)).** Let \(\Omega=(v_1,\ldots,v_m)\) be a cyclically ordered vertex set (a *society*). A *vortex of depth at most \(\theta\)* for \(\Omega\) is a graph \(H\) with \(\Omega\subseteq V(H)\) together with a path-decomposition \((X_1,\ldots,X_m)\) of \(H\) such that \(v_i\in X_i\) and \(|X_i|\le\theta\) for every \(i\).

(Different authors shift “depth/width” by one; only that \(\theta\in\mathbb{Z}_{\ge 0}\) is a fixed parameter matters below.)

**Definition 1.11 (\((a,g,p,\theta)\)-nearly embeddable graph).** A graph \(G\) is *\((a,g,p,\theta)\)-nearly embeddable* if there exists an *apex set* \(A\subseteq V(G)\) with \(|A|\le a\) such that
\[
G-A \;=\; G_0 \cup H_1 \cup \cdots \cup H_p,
\]
where:
1. \(G_0\) is embedded in a surface \(\Sigma\) with \(\mathrm{eg}(\Sigma)\le g\);
2. \(\Omega_1,\ldots,\Omega_p\) are vertex sets of (at most) \(p\) facial societies of this embedding;
3. each \(H_i\) is a vortex of depth \(\le\theta\) for \(\Omega_i\), with \(V(H_i)\cap V(G_0)=V(\Omega_i)\);
4. the sets \(V(H_i)\setminus V(\Omega_i)\) (\(i=1,\ldots,p\)) are pairwise disjoint.

Vertices of \(A\) may have arbitrary neighbourhoods in \(G\). (Minor variations in bookkeeping across references affect only constant functions in the bounds below.)

### 1.4. The structure theorem (external input)

**Theorem 1.12 (Robertson–Seymour Structure Theorem, qualitative form).** For every integer \(t\ge 1\) there exist integers \(a,g,p,\theta,k\ge 0\) such that every graph \(G\in\mathcal{F}_t\) admits a tree-decomposition in which every adhesion has size at most \(k\), every adhesion is a clique in the incident torsos, and every torso is \((a,g,p,\theta)\)-nearly embeddable.

Equivalently: every \(G\in\mathcal{F}_t\) is built by clique-sums of adhesion \(\le k\) from \((a,g,p,\theta)\)-nearly embeddable graphs.

We treat Theorem 1.12 as a black box and analyse what colouring information pure structural arguments can extract from it.

---

## 2. Clique-sum colouring (complete proofs)

### 2.1. Single clique-sum

**Lemma 2.1 (Clique-sum colouring).** Let \(m\ge 1\). Let \(G_1,G_2\) satisfy \(\chi(G_i)\le m\). Let \(G\) be a clique-sum of \(G_1\) and \(G_2\) along a clique of size \(k\le m\). Then \(\chi(G)\le m\).

**Proof.** Let \(C\) be the shared vertex set, \(|C|=k\le m\). Fix proper colourings \(c_i:V(G_i)\to\{1,\ldots,m\}\) for \(i=1,2\). Since \(C\) is a clique in each \(G_i\) (before optional edge deletion), each restriction \(c_i|_C\) is injective.

Hence there is a permutation \(\pi\) of \(\{1,\ldots,m\}\) with \(\pi\circ c_2(v)=c_1(v)\) for all \(v\in C\) (extend the partial matching on the image of \(C\) arbitrarily). Define \(c:V(G)\to\{1,\ldots,m\}\) by
\[
c(v)=
\begin{cases}
c_1(v) & \text{if }v\in V(G_1),\\
\pi\bigl(c_2(v)\bigr) & \text{if }v\in V(G_2)\setminus C.
\end{cases}
\]
This is well-defined on \(C\), proper on every edge of \(G_1\) and of \(G_2\), and every edge of \(G\) is an edge of \(G_1\) or of \(G_2\). ∎

**Remark 2.2.** Optional deletion of shared-clique edges cannot increase \(\chi\). If \(k>m\), the hypotheses \(\chi(G_i)\le m\) already fail.

### 2.2. Tree assembly

**Lemma 2.3 (Tree assembly of colourings).** Let \(m\ge 1\). Suppose \(G\) admits a tree-decomposition \((T,\mathcal{B})\) such that:
1. every adhesion has size at most \(m\) and is a clique in both incident torsos;
2. every torso \(\tau(B_x)\) satisfies \(\chi(\tau(B_x))\le m\).

Then \(\chi(G)\le m\).

**Proof.** Induction on \(|V(T)|\). If \(|V(T)|=1\), then \(G\) is a subgraph of the unique torso, so \(\chi(G)\le m\).

If \(|V(T)|\ge 2\), let \(\ell\) be a leaf of \(T\) adjacent to \(r\), and set \(C:=B_\ell\cap B_r\) (so \(|C|\le m\) and \(C\) is a clique in \(\tau(B_\ell)\)). Let \(G_\ell:=G[B_\ell]\) and let \(G'\) be obtained from \(G\) by deleting \(B_\ell\setminus C\). The restricted bags on \(T-\ell\) form a tree-decomposition of \(G'\) whose torsos are subgraphs of the original torsos, hence are \(m\)-colourable. By induction, \(\chi(G')\le m\). Also \(\chi(G_\ell)\le\chi(\tau(B_\ell))\le m\). The graph \(G\) is a clique-sum of \(G'\) and \(G_\ell\) along \(C\). Lemma 2.1 yields \(\chi(G)\le m\). ∎

**Corollary 2.4.** If every member of a family \(\mathcal{H}\) is \(m\)-colourable and \(G\) is obtained from members of \(\mathcal{H}\) by clique-sums along cliques of size \(\le m\), then \(\chi(G)\le m\).

**Moral.** Clique-sums are colouring-safe. Under Theorem 1.12, the entire burden of Hadwiger is to \((t-1)\)-colour the nearly-embeddable torsos.

---

## 3. Colouring building blocks for nearly-embeddable graphs

### 3.1. Bounded treewidth / pathwidth

**Lemma 3.1.** If \(\mathrm{tw}(G)\le w\), then \(\chi(G)\le w+1\). In particular, every vortex of depth \(\le\theta\) satisfies \(\chi\le\theta\).

**Proof.** A graph of treewidth \(\le w\) is a subgraph of a chordal graph \(G^*\) with \(\omega(G^*)\le w+1\) (add edges within bags of a width-\(w\) tree-decomposition). Chordal graphs are perfect, so \(\chi(G)\le\chi(G^*)=\omega(G^*)\le w+1\).

Alternatively: every graph of treewidth \(\le w\) is \(w\)-degenerate, so greedy colouring uses at most \(w+1\) colours.

A vortex of depth \(\le\theta\) has a path-decomposition with bags of size \(\le\theta\), hence treewidth \(\le\theta-1\), hence \(\chi\le\theta\). ∎

**Lemma 3.2 (Vortex interior).** If \(H\) is a vortex of depth \(\le\theta\) for a society \(\Omega\), then \(H-V(\Omega)\) has treewidth \(\le\theta-1\) (delete \(V(\Omega)\) from every bag) and \(\chi(H-V(\Omega))\le\theta\).

**Proof.** Immediate from the path-decomposition and Lemma 3.1. ∎

### 3.2. Surface-embedded graphs (classical external bound)

**Theorem 3.3 (Heawood; planar case = Four Colour Theorem).** Let \(G\) be embeddable in a surface of Euler genus \(g\). Then \(\chi(G)\le H^*(g)\), where
\[
H^*(g):=
\begin{cases}
4 & \text{if }g=0,\\[4pt]
\Bigl\lfloor\dfrac{7+\sqrt{1+24g}}{2}\Bigr\rfloor & \text{if }g\ge 1.
\end{cases}
\]

For \(g\ge 1\), the bound follows from Euler’s formula: every simple graph on the surface has a vertex of degree at most \(H^*(g)-1\), hence is \((H^*(g)-1)\)-degenerate (Appendix A). For \(g=0\), the elementary Euler argument gives only \(5\)-colourability; the sharp bound \(4\) is the Four Colour Theorem. Replacing \(4\) by \(5\) throughout would not change the obstruction analysis below.

### 3.3. Sheet plus vortices: product bound

**Lemma 3.4 (One vortex: product bound).** Let \(G_0\) be embedded in Euler genus \(\le g\), let \(H\) be a vortex of depth \(\le\theta\) for a facial society \(\Omega\) of \(G_0\), with \(V(H)\cap V(G_0)=V(\Omega)\), and set \(G:=G_0\cup H\). Then
\[
\chi(G)\le H^*(g)\cdot\theta.
\]

**Proof.** By Theorem 3.3, fix a proper colouring \(c_0:V(G_0)\to\{1,\ldots,H^*(g)\}\). By Lemma 3.1, fix a proper colouring \(c_H:V(H)\to\{1,\ldots,\theta\}\). Define
\[
c:V(G)\to\{1,\ldots,H^*(g)\}\times\{1,\ldots,\theta\}
\]
by
\[
c(v)=
\begin{cases}
\bigl(c_0(v),\,c_H(v)\bigr) & \text{if }v\in V(\Omega),\\
\bigl(1,\,c_H(v)\bigr) & \text{if }v\in V(H)\setminus V(\Omega),\\
\bigl(c_0(v),\,1\bigr) & \text{if }v\in V(G_0)\setminus V(\Omega).
\end{cases}
\]
- If \(e\in E(G_0)\), the first coordinates of its ends differ.
- If \(e\in E(H)\), the second coordinates of its ends differ.
- Every edge of \(G\) lies in \(E(G_0)\) or in \(E(H)\).

Hence \(c\) is a proper colouring, and the palette has cardinality \(H^*(g)\cdot\theta\). ∎

**Remark 3.5 (Why a product, not a casual sum).** A disjoint-palette attempt “colour \(G_0\) with \(H^*(g)\) colours and vortex interiors with \(\theta\) fresh colours” fails to control edges of \(H\) that have **both** ends on \(\Omega\) but are absent from \(G_0\) (society chords carried by the vortex): those edges are monochromatic-risk under a pure \(G_0\)-colouring. The product handles them through \(c_H\). (Under extra modeling hypotheses that every society edge of \(G\) already lies in \(G_0\), a sum bound \(H^*(g)+\theta\) is available via Lemma 3.2; see Remark 3.11. Both bounds are finite and both overshoot \(t-1\) for large RS parameters.)

**Proposition 3.6 (Several vortices: product bound).** Let \(G_0\) be embedded in Euler genus \(\le g\), and let \(H_1,\ldots,H_p\) be vortices of depth \(\le\theta\) for facial societies \(\Omega_1,\ldots,\Omega_p\), with interiors \(V(H_i)\setminus V(\Omega_i)\) pairwise disjoint. Assume the societies are pairwise vertex-disjoint (Remark 3.7). Set \(G:=G_0\cup H_1\cup\cdots\cup H_p\). Then
\[
\chi(G)\le H^*(g)\cdot\theta.
\]

**Proof.** Fix \(c_0:V(G_0)\to\{1,\ldots,H^*(g)\}\) proper. For each \(i\), fix \(c_i:V(H_i)\to\{1,\ldots,\theta\}\) proper (Lemma 3.1). Define \(c\) with values in \(\{1,\ldots,H^*(g)\}\times\{1,\ldots,\theta\}\) by
\[
c(v)=
\begin{cases}
\bigl(c_0(v),\,c_i(v)\bigr) & \text{if }v\in V(\Omega_i)\text{ for (unique) }i,\\
\bigl(c_0(v),\,1\bigr) & \text{if }v\in V(G_0)\setminus\bigcup_i V(\Omega_i),\\
\bigl(1,\,c_i(v)\bigr) & \text{if }v\in V(H_i)\setminus V(\Omega_i).
\end{cases}
\]
Edges of \(G_0\) differ in the first coordinate; edges of each \(H_i\) differ in the second. ∎

**Remark 3.7 (Disjoint societies).** If societies share vertices, one may: (i) move shared vertices into the apex set (increasing \(a\) by at most the number of shared vertices, still a function of the structure parameters); or (ii) refine the embedding/society choice. Either way the colouring bound remains of the form \(a'+H^*(g)\cdot\theta\) with \(a'\) still a function of \(t\) only. We assume disjoint societies for notational cleanliness.

### 3.4. Apex vertices

**Proposition 3.8 (Apex additive bound).** For any graph \(G\) and any \(A\subseteq V(G)\),
\[
\chi(G)\le\chi(G-A)+|A|.
\]

**Proof.** Colour \(G-A\) properly with \(\chi(G-A)\) colours; assign each vertex of \(A\) a distinct fresh colour. Edges within \(A\) and edges from \(A\) to \(G-A\) are then proper. ∎

**Proposition 3.9 (Apex greedy refinement).** If \(A=\{a_1,\ldots,a_r\}\) and each \(a_j\) has at most \(d\) neighbours in \(V(G-A)\cup\{a_1,\ldots,a_{j-1}\}\), then
\[
\chi(G)\le\max\bigl(\chi(G-A),\,d+1\bigr).
\]

**Proof.** Colour \(G-A\), then greedy-colour \(a_1,\ldots,a_r\) in order. ∎

The structure theorem provides **no** degree bound on apices, so only Proposition 3.8 applies in general.

### 3.5. Combined bound for nearly-embeddable graphs

**Theorem 3.10 (Elementary colouring of nearly-embeddable graphs).** Every \((a,g,p,\theta)\)-nearly embeddable graph \(G\) satisfies
\[
\chi(G)\le a+H^*(g)\cdot\theta.
\]

**Proof.** Let \(A\) be an apex set as in Definition 1.11, \(|A|\le a\), and write \(G-A=G_0\cup H_1\cup\cdots\cup H_p\). By Proposition 3.6,
\[
\chi(G-A)\le H^*(g)\cdot\theta.
\]
By Proposition 3.8,
\[
\chi(G)\le\chi(G-A)+|A|\le a+H^*(g)\cdot\theta.
\]
∎

**Remark 3.11 (Optional sum form).** If every edge of each \(H_i\) with both ends in \(\Omega_i\) already belongs to \(G_0\), then one may colour \(G_0\) with \(H^*(g)\) colours and all vortex interiors \(\bigcup_i\bigl(V(H_i)\setminus V(\Omega_i)\bigr)\) with a single disjoint palette of \(\theta\) colours (Lemma 3.2; interiors are pairwise non-adjacent across vortices), obtaining \(\chi(G-A)\le H^*(g)+\theta\) and \(\chi(G)\le a+H^*(g)+\theta\). The obstruction analysis is unchanged under either bound.

---

## 4. Assembly: what the structure theorem gives for \(\chi\)

**Theorem 4.1 (Finite \(\chi\)-bound for \(\mathcal{F}_t\) via structure).** Let \(t\ge 1\), and let \(a,g,p,\theta,k\) be as in Theorem 1.12. Set
\[
m(t):=\max\bigl(k,\; a+H^*(g)\cdot\theta\bigr).
\]
Then every \(G\in\mathcal{F}_t\) satisfies \(\chi(G)\le m(t)\).

**Proof.** By Theorem 1.12, \(G\) has a tree-decomposition with adhesions of size \(\le k\) that are cliques in the torsos, and with every torso \((a,g,p,\theta)\)-nearly embeddable. Theorem 3.10 gives \(\chi(\tau)\le a+H^*(g)\cdot\theta\le m(t)\) for every torso \(\tau\). Lemma 2.3 yields \(\chi(G)\le m(t)\). ∎

**Corollary 4.2.** For each fixed \(t\), \(\chi\) is bounded on \(\mathcal{F}_t\).

**Remark 4.3 (Comparison with degeneracy).** Kostochka and Thomason proved that average degree \(\ge c\,t\sqrt{\log t}\) forces a \(K_t\) minor. Hence every \(G\in\mathcal{F}_t\) is \(O(t\sqrt{\log t})\)-degenerate and
\[
\chi(G)=O\bigl(t\sqrt{\log t}\bigr).
\]
Theorem 4.1 recovers only *some* finite \(m(t)\); classical Graph Minors parameters are enormous. Structure-based colouring as above does not improve the Kostochka–Thomason order and does not reach \(t-1\).

**Remark 4.4 (Adhesion size).** For \(G\in\mathcal{F}_t\), no adhesion that is a clique can have size \(\ge t\) (else \(K_t\subseteq G\)). Thus one may take \(k\le t-1\), and
\[
m(t)=\max\bigl(t-1,\; a+H^*(g)\cdot\theta\bigr).
\]
Hadwiger requires the second term to be \(\le t-1\) as well.

---

## 5. Exact obstruction to a structure-theoretic proof of Hadwiger

### 5.1. Formal reduction: clique-sums are not the problem

**Proposition 5.1 (Clique-sums are Hadwiger-safe).** Suppose every \((a,g,p,\theta)\)-nearly embeddable torso arising in Theorem 1.12 for \(\mathcal{F}_t\) is \((t-1)\)-colourable. Then every \(G\in\mathcal{F}_t\) is \((t-1)\)-colourable.

**Proof.** Adhesions have size \(\le t-1\) (Remark 4.4). Apply Lemma 2.3 with \(m=t-1\). ∎

**Corollary 5.2 (Core reduced problem).** Under Theorem 1.12, Hadwiger’s conjecture for \(\mathcal{F}_t\) is equivalent to:
> every \((a,g,p,\theta)\)-nearly embeddable graph in \(\mathcal{F}_t\) (with the structure parameters of \(t\)) is \((t-1)\)-colourable.

### 5.2. Primary obstruction: the apex additive gap

**Definition 5.3 (Apex additive gap).** For \(A\subseteq V(G)\), set
\[
\gamma(G,A):=\chi(G)-\chi(G-A).
\]
Proposition 3.8 says \(\gamma(G,A)\le|A|\).

**Proposition 5.4 (Additive bound is tight without minor hypotheses).** For all integers \(a\ge 0\) and \(s\ge 1\), the complete graph \(G=K_{s+a}\) with \(A\) any \(a\)-set of vertices satisfies \(\chi(G-A)=s\) and \(\gamma(G,A)=a\).

**Proof.** Immediate. ∎

Such examples have huge clique minors. The structural question is whether, for apex sets produced by Theorem 1.12 inside \(\mathcal{F}_t\), one still has \(\gamma(G,A)\) large, or whether minor-exclusion forces \(\chi(G-A)+\gamma(G,A)\le t-1\).

**Proposition 5.5 (What minor-exclusion gives for vertex deletion).** Let \(G\in\mathcal{F}_t\) and \(A\subseteq V(G)\). Then \(G-A\in\mathcal{F}_t\), and
\[
h(G)\le h(G-A)+|A|.
\]

**Proof.** Deleting one vertex drops the Hadwiger number by at most \(1\): if \(K_r\) is a minor of \(G\) and \(v\in V(G)\), then \(G-v\) has a \(K_{r-1}\) minor (discard the branch set meeting \(v\), or shorten it). Iterate over \(A\). Minors of \(G-A\) are minors of \(G\), so \(G-A\in\mathcal{F}_t\). ∎

This does **not** improve the Hadwiger target for \(G-A\): one still only knows \(h(G-A)\le t-1\).

**Proposition 5.6 (Universal apex clique — the missing reduction).** Suppose \(G\in\mathcal{F}_t\), \(A\subseteq V(G)\), \(G[A]\) is complete, and every vertex of \(A\) is adjacent to every vertex of \(V(G)\setminus A\). Then \(G-A\in\mathcal{F}_{t-|A|}\). Consequently, if Hadwiger holds for \(\mathcal{F}_{t-|A|}\), then \(\chi(G-A)\le t-|A|-1\), and Proposition 3.8 yields
\[
\chi(G)\le(t-|A|-1)+|A|=t-1.
\]

**Proof.** A \(K_{t-|A|}\) minor in \(G-A\), together with the \(|A|\) singleton branch sets of \(A\) (pairwise adjacent and universal to \(G-A\)), would form a \(K_t\) minor in \(G\). ∎

**Exact failure of Proposition 5.6 in the RS setting.** The apex set in Definition 1.11 / Theorem 1.12 is **not** guaranteed to be a clique, nor to be complete to \(G-A\). Apices exist only to remove topological obstacles to embedding; their neighbourhoods may be arbitrary. One cannot spend \(|A|\) colours and drop the Hadwiger parameter by \(|A|\).

**Proposition 5.7 (Extension obstruction).** Let \(s=t-1\). Suppose \(G-A\) is properly \(s\)-coloured and \(v\in A\). This colouring extends to \(v\) if and only if \(N_G(v)\) misses at least one colour. If for every \(s\)-colouring of \(G-A\) some apex meets all \(s\) colours, extension fails and one needs a new colour or a recolouring of \(G-A\).

Neither Theorem 1.12 nor the elementary vortex/sheet analysis provides a Kempe-chain or recolouring lemma for arbitrary apex attachments to a bounded-genus graph with vortices. In Wagner’s \(K_5\)-minor-free theory and in the Four Colour Theorem, recolouring works because the non-apex part is planar (or one of finitely many base graphs) with tightly controlled attachments. For general nearly-embeddable torsos, no such theorem is known; proving one is comparable in difficulty to Hadwiger for that class.

### 5.3. Secondary obstruction: vortex-depth gap

Elementary colouring pays a factor (or summand) of \(\theta\) for vortices (Lemma 3.4, Theorem 3.10). Hadwiger allows only \(t-1\) colours globally.

**Proposition 5.8.** A vortex \(H\) of depth \(\theta\) inside a graph \(G\in\mathcal{F}_t\) satisfies \(H\in\mathcal{F}_t\) and \(\chi(H)\le\theta\) (Lemma 3.1). If \(\theta\le t-1\), the treewidth bound already gives \(\chi(H)\le t-1\). If \(\theta>t-1\), the treewidth bound exceeds the Hadwiger target, and improving it to \(t-1\) is again a Hadwiger-type statement for a pathwidth-bounded subclass of \(\mathcal{F}_t\).

Even when \(\theta\le t-1\), the difficulty is not colouring vortices in isolation but controlling the **joint** colouring with the sheet under a global palette of \(t-1\) colours (the product bound uses \(H^*(g)\cdot\theta\) colours).

### 5.4. Tertiary obstruction: Heawood vs minor-free surface colouring

**Proposition 5.9.** For a graph \(G_0\) embedded in genus \(g\), Heawood gives \(\chi(G_0)\le H^*(g)\). If \(G_0\in\mathcal{F}_t\), Hadwiger wants \(\chi(G_0)\le t-1\). Whenever the structure theorem returns \(g\) with \(H^*(g)>t-1\), using Heawood without minor-exclusion overshoots.

The chromatic number of *\(K_t\)-minor-free* graphs on a fixed surface may be smaller than \(H^*(g)\), but bounding it by \(t-1\) is a restricted form of Hadwiger and is not supplied by Theorem 1.12. (For \(g=0\) and \(t\ge 5\), the Four Colour Theorem gives \(\chi\le 4\le t-1\), so the pure planar sheet is fine; the overshoot appears for large structure genus and for the apex/vortex package.)

### 5.5. Parameter failure

**Proposition 5.10.** Hadwiger via Theorem 4.1 would require
\[
a(t)+H^*\bigl(g(t)\bigr)\cdot\theta(t)\;\le\; t-1.
\]
No known proof of a structure theorem for large \(t\) achieves this. The parameters in classical Graph Minors proofs are vastly larger than \(t\). Even optimistically replacing the product by a sum (Remark 3.11), one still needs \(a+H^*(g)+\theta\le t-1\), which is equally unavailable for large \(t\).

### 5.6. Statement of the exact obstruction

**Theorem 5.11 (Exact obstruction).** Assume Theorem 1.12. Then:

1. **Clique-sums are not an obstruction.** Hadwiger for \(\mathcal{F}_t\) reduces exactly to \((t-1)\)-colourability of the nearly-embeddable torsos (Proposition 5.1).

2. **Elementary colouring of torsos overshoots.** The only general bound proved by composition is
   \[
   \chi\le a+H^*(g)\cdot\theta
   \]
   (Theorem 3.10), which is not \(\le t-1\) for known parameters (Proposition 5.10).

3. **Primary structural gap — apex additivity.** Paying \(|A|\) colours for apices (Proposition 3.8) cannot be converted into a Hadwiger-parameter drop of \(|A|\) without universal joins from a clique of apices (Proposition 5.6), which RS apices do not have. No elementary extension/recolouring lemma closes \(\gamma(G,A)\) under mere membership in \(\mathcal{F}_t\).

4. **Secondary gaps — vortices and Heawood.** Vortex depth contributes a multiplicative (or additive) \(\theta\) cost; Heawood contributes \(H^*(g)\) without using minor-exclusion on the sheet.

5. **No free lunch from \(\mathcal{F}_t\).** Deleting apices does not improve the excluded-minor parameter below \(t\) (Proposition 5.5), so induction on \(t\) does not fire.

---

## 6. Partial positive lemmas (extra hypotheses that would finish the proof)

**Lemma 6.1 (Controlled universal apices).** Let \(G\in\mathcal{F}_t\) be \((a,g,p,\theta)\)-nearly embeddable with apex set \(A\), \(|A|\le a\), such that \(G[A]\) is complete and every vertex of \(A\) is adjacent to all of \(V(G)\setminus A\). Suppose every \((0,g,p,\theta)\)-nearly embeddable graph in \(\mathcal{F}_{t-a}\) is \((t-a-1)\)-colourable. Then \(\chi(G)\le t-1\).

**Proof.** Proposition 5.6 and Proposition 3.8. ∎

**Lemma 6.2 (Bounded-degree apices).** Let \(G\in\mathcal{F}_t\) be nearly embeddable with apex set \(A\). If \(\chi(G-A)\le t-1\) and every vertex of \(A\) has degree \(\le t-2\) in \(G\), then \(\chi(G)\le t-1\).

**Proof.** Colour \(G-A\) with \(t-1\) colours; greedy-extend across \(A\). ∎

**Lemma 6.3 (Parameter regime where elementary methods suffice).** If \(a+H^*(g)\cdot\theta\le t-1\), then every \((a,g,p,\theta)\)-nearly embeddable graph (minor-free or not) satisfies \(\chi\le t-1\) by Theorem 3.10. Combined with Lemma 2.3 and Theorem 1.12, Hadwiger would follow.

**Remark 6.4.** No known structure theorem places parameters in the regime of Lemma 6.3 for large \(t\). Degeneracy methods are likewise capped at \(O(t\sqrt{\log t})\) (Appendix B).

**Proposition 6.5 (Why \(t=5\) works: no apices/vortices).** Wagner’s theorem: every \(G\in\mathcal{F}_5\) is a clique-sum of planar graphs and copies of \(V_8\). Planar graphs are \(4\)-colourable (4CT); \(V_8\) is \(3\)-colourable; adhesions have size \(\le 3\). Lemma 2.3 gives \(\chi\le 4\). The pieces are *truly* embeddable (or tiny), not nearly embeddable — so the apex/vortex gaps never open.

**Proposition 6.6 (Why \(t=6\) is special).** Robertson–Seymour–Thomas showed Hadwiger for \(t=6\) is equivalent to the Four Colour Theorem by a dedicated structural reduction, not by feeding general RS parameters into Theorem 3.10.

---

## 7. Summary of proved statements

| Statement | Status |
|-----------|--------|
| Lemma 2.1: clique-sums preserve \(m\)-colourability | **Proved** |
| Lemma 2.3: tree assembly of torso colourings | **Proved** |
| Lemma 3.1: \(\mathrm{tw}\le w\Rightarrow\chi\le w+1\); vortices \(\chi\le\theta\) | **Proved** |
| Theorem 3.3: Heawood / 4CT | **External** |
| Lemma 3.4 / Prop. 3.6: sheet + vortices \(\Rightarrow\chi\le H^*(g)\cdot\theta\) | **Proved** |
| Prop. 3.8: apex additive bound | **Proved** |
| Theorem 3.10: nearly embeddable \(\Rightarrow\chi\le a+H^*(g)\cdot\theta\) | **Proved** |
| Theorem 4.1: \(\mathcal{F}_t\) has \(\chi\le m(t)<\infty\) via RS | **Proved** from Thm 1.12 + above |
| \(\chi\le t-1\) for \(\mathcal{F}_t\) via this route | **Not proved** |
| Exact obstruction | **Apex additive gap** (+ vortex depth, Heawood); clique-sums safe |

---

## 8. Conclusion

The Graph Minors Structure Theorem **does** organise \(K_t\)-minor-free graphs as clique-sums of nearly-embeddable pieces, and clique-sums **do** preserve colouring bounds (Lemmas 2.1–2.3). Elementary colouring of nearly-embeddable graphs **does** give a finite bound \(a+H^*(g)\cdot\theta\) (Theorem 3.10), hence \(\chi\) is bounded on each \(\mathcal{F}_t\) (Theorem 4.1).

This is **not** a proof of Hadwiger. The method fails exactly at colouring nearly-embeddable torsos with \(t-1\) colours. The elementary theory’s dominant defect is the **apex additive gap**: \(\chi(G)\le\chi(G-A)+|A|\) costs a full \(|A|\) colours, while the reduction that would justify that cost (universal apex clique, Proposition 5.6) is not provided by the structure theorem. Secondary defects are vortex-depth and Heawood overshoot. Closing the gaps requires either unrealistically small structure parameters or a deep recolouring/extension theorem under no-\(K_t\)-minor, essentially as hard as Hadwiger itself.

**Outcome B.** Partial structural colouring theory fully proved; Hadwiger not obtained; exact obstruction identified as the apex/vortex (“nearly”) package in the structure theorem.

---

## Appendix A. Euler degeneracy for Heawood (\(g\ge 1\))

**Lemma A.1 (sketch).** Let \(G\) be a simple graph embedded in a surface of Euler genus \(g\ge 1\), with \(n\) vertices, \(m\) edges, and \(f\) faces. Euler’s formula gives \(n-m+f\ge 2-g\) (in the Euler-genus convention). If every face has length at least \(3\), then \(2m\ge 3f\). Eliminating \(f\) yields \(m\le 3n+O(g)\). Hence the average degree is at most \(6+O(g/n)\), and every such graph has a vertex of degree at most \(H^*(g)-1\). Therefore \(G\) is \((H^*(g)-1)\)-degenerate and \(\chi(G)\le H^*(g)\).

(The planar case \(g=0\) by the same method gives \(\chi\le 5\); sharpness \(4\) is 4CT.)

## Appendix B. Kostochka–Thomason vs Hadwiger

**Theorem B.1 (Kostochka; Thomason).** There exists \(c>0\) such that every graph of average degree at least \(c\,t\sqrt{\log t}\) has a \(K_t\) minor.

**Corollary B.2.** Every \(G\in\mathcal{F}_t\) has a vertex of degree \(O(t\sqrt{\log t})\), hence \(\chi(G)=O(t\sqrt{\log t})\).

This is best possible among *degeneracy* bounds: there exist graphs of average degree \(\Omega(t\sqrt{\log t})\) with no \(K_t\) minor. Those graphs need not require \(\Omega(t\sqrt{\log t})\) colours; Hadwiger predicts they are still \((t-1)\)-colourable. Degeneracy and elementary structure-colouring both stop short of \(t-1\) for the same qualitative reason: they do not exploit global recolouring structure beyond local degree or local surface/vortex data.

---

*End of note.*
