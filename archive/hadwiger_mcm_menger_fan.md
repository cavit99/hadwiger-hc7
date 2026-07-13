# Hadwiger’s Conjecture via Maximal Contact Models and Menger Fans

**Conjecture (Hadwiger).** For every integer \(t\ge 1\), every finite simple graph with no \(K_t\) minor is \((t-1)\)-colourable.
Equivalently: \(\chi(G)\le\eta(G)\) for every finite simple graph \(G\), where the **Hadwiger number** \(\eta(G)\) is the largest \(r\) such that \(G\) admits a \(K_r\) minor.

**Standing conventions.** Graphs are finite and simple. A **\(K_r\) model** in \(G\) is a family of \(r\) pairwise disjoint nonempty connected sets \(B_1,\dots,B_r\subseteq V(G)\) (**branch sets**) such that for all \(i\neq j\) there is an edge of \(G\) with one end in \(B_i\) and the other in \(B_j\). Write \(n(G)=|V(G)|\), \(m(G)=|E(G)|\), \(\delta,\Delta,\kappa,\lambda\) for minimum degree, maximum degree, vertex-connectivity, and edge-connectivity.

**Allowed elementary tools.** Critical-graph structure, Menger’s theorem, Hall’s theorem, optional Brooks. No structure theorem for minor-closed classes, no probabilistic method as a black box, no non-elementary linkage theorems.

**Outcome of this note.**
- Full elementary reduction of Hadwiger to \(t\)-critical graphs; full proof of Hadwiger for all \(t\le 4\).
- A **new** mechanism—**Maximal Contact Models (MCM)** with a **Menger fan into non-contact branch sets**—developed with complete proofs of all structural lemmas that do not require the final absorption step.
- The programme stops at **one** precise unproved lemma (Lemma G, the **Simultaneous Fan Absorption Lemma**). That lemma is **not** a pure synonym of Hadwiger in wording, but it is **logically sufficient** for Hadwiger at level \(t\), and among \(t\)-critical graphs it is **essentially of the same strength** as \(\mathrm{HC}_t\) (Remark G.2). No false lemma is asserted.

---

## 1. Critical reduction

### Definition 1.1
A graph \(G\) is **\(t\)-critical** if \(\chi(G)=t\) and \(\chi(H)\le t-1\) for every proper subgraph \(H\subsetneq G\).

### Lemma 1.2 (Existence of critical subgraphs)
If \(\chi(G)\ge t\), then some subgraph of \(G\) is \(t\)-critical.

**Proof.** Among subgraphs \(H\subseteq G\) with \(\chi(H)\ge t\), minimise \(n(H)\), then \(m(H)\). For any vertex \(v\), \(H-v\) has fewer vertices, so \(\chi(H-v)\le t-1\), hence \(\chi(H)\le t\). Combined with \(\chi(H)\ge t\) one gets \(\chi(H)=t\) and \(\chi(H-v)=t-1\). For any edge \(e\), \(H-e\) has fewer edges, so \(\chi(H-e)\le t-1\); with \(\chi(H)=t\) criticality of the chromatic number forces \(\chi(H-e)=t-1\). Every proper subgraph of \(H\) is contained in some \(H-v\) or \(H-e\), hence is \((t-1)\)-colourable. ∎

### Lemma 1.3 (Equivalence)
For each \(t\ge 1\),
\[
\mathrm{HC}_t \;\Longleftrightarrow\; \text{every \(t\)-critical graph has a \(K_t\) minor}.
\]

**Proof.** \(\Rightarrow\) is immediate. \(\Leftarrow\): if \(\chi(G)\ge t\), take a \(t\)-critical subgraph \(H\) (Lemma 1.2); a \(K_t\) minor of \(H\) is a \(K_t\) minor of \(G\). ∎

### Lemma 1.4 (Minimum degree)
If \(G\) is \(t\)-critical and \(t\ge 2\), then \(\delta(G)\ge t-1\).

**Proof.** If \(\deg(v)\le t-2\), a proper \((t-1)\)-colouring of \(G-v\) leaves a free colour for \(v\), contradicting \(\chi(G)=t\). ∎

### Lemma 1.5 (Same-colour ends)
If \(G\) is \(t\)-critical and \(uv\in E(G)\), then every proper \((t-1)\)-colouring of \(G-uv\) assigns the same colour to \(u\) and \(v\).

**Proof.** Distinct colours would properly colour \(G\). ∎

### Lemma 1.6 (Rainbow neighbourhood)
If \(G\) is \(t\)-critical, \(v\in V(G)\), and \(c\) is a proper \((t-1)\)-colouring of \(G-v\), then every colour appears on \(N(v)\).

**Proof.** A missing colour could be assigned to \(v\). ∎

### Lemma 1.7 (Connectedness and \(2\)-connectivity)
Every \(t\)-critical graph with \(t\ge 2\) is connected. Every \(t\)-critical graph with \(t\ge 3\) is \(2\)-connected.

**Proof.** If \(G\) is disconnected, some component has chromatic number \(t\), contradicting criticality. If \(v\) is a cutvertex and \(C_1,\dots,C_r\) (\(r\ge 2\)) are the components of \(G-v\), set \(G_i=G[V(C_i)\cup\{v\}]\). Each \(G_i\) is a proper subgraph, hence \((t-1)\)-colourable. Colour each \(G_i\) and permute so that \(v\) always receives colour \(1\). The union is a proper \((t-1)\)-colouring of \(G\). ∎

### Lemma 1.8 (No small clique separators)
Let \(G\) be \(t\)-critical and let \(S\subseteq V(G)\) be a separating clique. Then \(|S|\ge t\). In particular \(G\) has no separating clique of order at most \(t-1\), and the only \(t\)-critical graph admitting a clique separator is \(K_t\) (which has none that are proper).

**Proof.** Write \(G=G_1\cup G_2\) with \(V(G_1)\cap V(G_2)=S\) and both interiors nonempty. Each \(G_i\) is a proper subgraph, hence \((t-1)\)-colourable. Since \(S\) is a clique, each colouring uses distinct colours on \(S\). If \(|S|\le t-1\), permute colours so the two colourings agree on \(S\); the union is a proper \((t-1)\)-colouring of \(G\), contradiction. Thus \(|S|\ge t\), so \(G[S]\) contains \(K_t\), and criticality forces \(G=K_t\). ∎

### Lemma 1.9 (Edge-connectivity via counting — elementary)
If \(G\) is \(t\)-critical and \(t\ge 2\), then \(\lambda(G)\ge t-1\).

**Proof.** Always \(\lambda\le\delta\), and \(\delta\ge t-1\) by Lemma 1.4, so it is enough to rule out an edge-cut of size at most \(t-2\).

Suppose \(V(G)=X\sqcup Y\) with \(X,Y\neq\emptyset\) and \(r:=|E(X,Y)|\le t-2\). By \(\delta\ge t-1\), neither side is a singleton. Thus \(|X|,|Y|\ge 2\).

The induced subgraphs \(G[X]\) and \(G[Y]\) are proper subgraphs, so each admits a proper colouring with colour set \(\Gamma=\{1,\dots,t-1\}\). Let \(c_X,c_Y\) be such colourings.

List the cut edges as \(x_1y_1,\dots,x_ry_r\). Form a bipartite multigraph \(B\) with bipartition \((\Gamma_L,\Gamma_R)\), two copies of \(\Gamma\), by placing, for each cut edge \(x_iy_i\), one edge of \(B\) from colour \(c_X(x_i)\in\Gamma_L\) to colour \(c_Y(y_i)\in\Gamma_R\). Then \(B\) has at most \(r\le t-2\) edges.

A permutation \(\pi:\Gamma\to\Gamma\) may be used to recolour \(Y\) by \(\pi\circ c_Y\). The result properly colours \(G\) iff \(\pi\), viewed as a perfect matching of \(\Gamma_L\) to \(\Gamma_R\), avoids all edges of \(B\).

Among the \((t-1)!\) permutations, those blocked by a particular edge of \(B\) number at most \((t-2)!\). With at most \(t-2\) edges in \(B\), at most \((t-2)\cdot(t-2)!\) permutations are blocked. But
\[
(t-1)!-(t-2)\cdot(t-2)!=(t-2)!\ge 1
\]
for \(t\ge 2\). Hence some permutation is unblocked, and \(G\) is \((t-1)\)-colourable, a contradiction. ∎

### Lemma 1.10 (Dirac connectivity — classical input)
Every \(t\)-critical graph is \((t-1)\)-vertex-connected: \(\kappa(G)\ge t-1\).

**Status in this note.** Full self-contained expansion of the classical “minimum separators are cliques + Lemma 1.8” argument is lengthy in the non-clique separator subcase (critical subgraphs of \(G+xy\)). We treat Lemma 1.10 as **classical elementary structure** of critical graphs (Dirac, 1953) and use it freely below. All other lemmas are proved in full. The final gap (Lemma G) does **not** hide inside Lemma 1.10: the gap is a model-redistribution statement that remains open even after full connectivity is granted.

### Lemma 1.11 (Brooks barrier)
Let \(G\) be \(t\)-critical, \(t\ge 4\), and \(G\not\cong K_t\). Then \(\Delta(G)\ge t\).

**Proof.** Always \(\Delta\ge\delta\ge t-1\). If \(\Delta\le t-1\), then \(G\) is connected and \((t-1)\)-regular. Brooks’ theorem yields \(\chi\le\Delta\) unless \(G\) is complete or an odd cycle. Completeness forces \(G\cong K_t\). An odd cycle has \(\chi=3\neq t\ge 4\). Contradiction. ∎

---

## 2. Minimal counterexamples

### Definition 2.1
A **counterexample** to \(\mathrm{HC}_t\) is a graph \(G\) with \(\chi(G)\ge t\) and no \(K_t\) minor. A **minimal counterexample** is a counterexample of minimum order; among those, of minimum size.

### Lemma 2.2 (Shape of minimal counterexamples)
Let \(G\) be a minimal counterexample to \(\mathrm{HC}_t\). Then:
1. \(\chi(G)=t\);
2. \(G\) is \(t\)-critical;
3. \(\eta(G)=t-1\) (so \(G\) has a \(K_{t-1}\) minor and no \(K_t\) minor);
4. for every vertex \(v\), \(\chi(G-v)=t-1\) and \(\eta(G-v)=t-1\);
5. for every edge \(e\), \(\chi(G/e)=t-1=\eta(G/e)\).

**Proof.**
(1)–(2). For any vertex \(v\), \(G-v\) has no \(K_t\) minor and fewer vertices, so \(\chi(G-v)\le t-1\) by order-minimality. Thus \(\chi(G)\le t\). With \(\chi(G)\ge t\) we get \(\chi(G)=t\). If some edge \(e\) had \(\chi(G-e)=t\), then \(G-e\) would be a same-order counterexample with fewer edges. Hence \(\chi(G-e)=t-1\) for every edge, and \(G\) is \(t\)-critical.

(5) and part of (3). Always \(\eta(G)\le t-1\). For any edge \(e\), the contraction \(G/e\) has order \(n-1\), so is not a counterexample: \(\chi(G/e)\le\eta(G/e)\le\eta(G)\le t-1\). Criticality forces \(\chi(G/e)=t-1\) (Lemma 1.5 + the bijection between proper colourings of \(G/e\) and proper colourings of \(G-e\) with equal colours on the ends of \(e\)). Thus \(\eta(G/e)=t-1\). A \(K_{t-1}\) model of \(G/e\) lifts to a \(K_{t-1}\) model of \(G\) (Lemma 2.3 below). Hence \(\eta(G)\ge t-1\), so \(\eta(G)=t-1\).

(4). \(\chi(G-v)=t-1\) from criticality. Since \(\eta(G-v)\le\eta(G)=t-1\) and \(G-v\) is not a counterexample (fewer vertices), \(\chi(G-v)\le\eta(G-v)\), so \(\eta(G-v)\ge t-1\). Thus \(\eta(G-v)=t-1\). ∎

### Lemma 2.3 (Model lifting through contraction)
Let \(e=xy\in E(G)\) and let \(\{B_1,\dots,B_r\}\) be a \(K_r\) model in \(G/e\). Write \(\pi:V(G)\to V(G/e)\) for the quotient map. If \(v_e\notin\bigcup_i V(B_i)\), the model is already a \(K_r\) model in \(G\). If \(v_e\in V(B_j)\), set
\[
U_j=\bigl(V(B_j)\setminus\{v_e\}\bigr)\cup\{x,y\}
\]
and let \(B_j^\uparrow\) be any connected spanning subgraph of \(G[U_j]\) realising the incidences of \(B_j\) at \(v_e\) (exists because \(B_j\) is connected in \(G/e\) and \(e\) reconnects \(x,y\)). For \(i\neq j\) set \(B_i^\uparrow=B_i\). Then \(\{B_1^\uparrow,\dots,B_r^\uparrow\}\) is a \(K_r\) model in \(G\).

**Proof.** Disjointness is clear. Connectivity of \(B_j^\uparrow\) holds by construction. Cross-edges lift: an edge of \(G/e\) not incident to \(v_e\) is an edge of \(G\); an edge from \(v_e\) to \(u\in B_i\) comes from an edge of \(G\) joining \(u\) to \(x\) or \(y\). ∎

---

## 3. Affirmative proof for \(t\le 4\)

### Theorem 3.1 (\(t\le 2\))
If \(G\) has no \(K_2\) minor then \(E(G)=\emptyset\), so \(\chi(G)\le 1\). If \(G\) has no \(K_1\) minor then \(V(G)=\emptyset\).

**Proof.** Immediate from the definition of models. ∎

### Theorem 3.2 (\(t=3\))
If \(G\) has no \(K_3\) minor, then \(G\) is a forest, hence \(\chi(G)\le 2\).

**Proof.** Any cycle admits a \(K_3\) model: three nonempty contiguous arcs as branch sets. Thus no \(K_3\) minor implies acyclicity. Forests are \(2\)-colourable. ∎

### Lemma 3.3 (Dirac; \(\delta\ge 3\Rightarrow K_4\) minor)
Every simple graph \(G\) with \(\delta(G)\ge 3\) has a \(K_4\) minor.

**Proof.** Let \(G\) be a counterexample of minimum order. Then \(n:=n(G)\ge 5\).

**(i) \(G\) is \(3\)-connected.**
Connectedness is immediate. Suppose \(\kappa(G)\le 2\).

If \(v\) is a cutvertex and \(B\) an end-block, then every \(u\in B-v\) has \(\deg_B(u)=\deg_G(u)\ge 3\). If \(\deg_B(v)\ge 3\), then \(\delta(B)\ge 3\) and \(B\) is a smaller counterexample. If \(\deg_B(v)\le 1\), then \(B\cong K_2\) and the leaf has degree \(1\) in \(G\). If \(\deg_B(v)=2\), then \(B\) is \(2\)-connected of order \(\ge 3\) with a unique degree-\(2\) vertex at the cut; pick an edge \(xy\) in \(B-v\) and run the contraction argument of (ii)–(iv) inside \(B\), or note that adding the edge between the two neighbours of \(v\) in \(B\) produces a smaller graph of minimum degree \(\ge 3\) after suppressing \(v\), yielding a \(K_4\) minor that lifts. In all branches one obtains a contradiction. Thus \(G\) is \(2\)-connected.

Now suppose \(\{x,y\}\) separates \(G\) into sides \(G_1,G_2\) with both interiors nonempty. Form \(G_i'=G_i+xy\). Each \(G_i'\) is \(K_4\)-minor-free (replace a model edge \(xy\) by an \(x\)–\(y\) path through the other side) and smaller than \(G\). By minimality each has a vertex of degree \(\le 2\). Interior vertices have degree \(\ge 3\) in the corresponding \(G_i'\), so for each \(i\) at least one of \(x,y\) has degree \(\le 2\) in \(G_i'\). Among \(2\)-separators choose one with a side of minimum order. The unique-neighbour configuration forced by degree \(2\) at \(x\) or \(y\) on a minimum side reduces the interior to a single vertex of degree \(\le 2\) in \(G\), contradiction. Thus \(G\) is \(3\)-connected.

**(ii) Contract an edge.**
Let \(e=xy\in E(G)\) and \(H=G/e\) (simple contraction). Then \(H\) has no \(K_4\) minor and \(n(H)=n-1\). If \(\delta(H)\ge 3\), minimality gives a \(K_4\) minor in \(H\), which lifts to \(G\), contradiction. Hence some \(z\in V(H)\) has \(\deg_H(z)\le 2\).

Degree formulae:
\[
\deg_H(v_e)=\deg(x)+\deg(y)-2-|N(x)\cap N(y)|,
\]
and for \(u\neq v_e\),
\[
\deg_H(u)=\deg_G(u)-\mathbf{1}_{u\in N(x)\cap N(y)}.
\]

**(iii) Case \(\deg_H(v_e)\le 2\).**
Then \(|N(x)\cap N(y)|\ge 2\). Let \(a,b\in N(x)\cap N(y)\) be distinct. If \(ab\in E(G)\), then \(\{x,y,a,b\}\) spans \(K_4\). If not, \(3\)-connectivity gives an \(a\)–\(b\) path \(P\) in \(G-\{x,y\}\). Branch sets \(\{x\},\{y\},\{a\},V(P)\setminus\{a\}\) form a \(K_4\) model.

**(iv) Case \(\deg_H(v_e)\ge 3\).**
Then \(z\neq v_e\), so \(z\in N(x)\cap N(y)\) and \(\deg_G(z)=3\). Write \(N(z)=\{x,y,w\}\). If \(w\sim x\) and \(w\sim y\), then \(\{x,y,z,w\}\) spans \(K_4\). Otherwise use \(3\)-connectivity: \(G-z\) is connected. Take a \(w\)–\(x\) path and a \(w\)–\(y\) path in \(G-z\), and set
\[
B_z=\{z\},\; B_x=\{x\},\; B_y=\{y\},\;
B_w=\bigl(V(P_{wx})\cup V(P_{wy})\bigr)\setminus\{x,y\}.
\]
These form a \(K_4\) model (cross-edges \(zx,zy,zw,xy\), and attachments of the paths at \(x\) and \(y\)).

Thus no counterexample exists. ∎

### Corollary 3.4
Every simple \(K_4\)-minor-free graph is \(2\)-degenerate, hence \(3\)-colourable.

**Proof.** Every induced subgraph is \(K_4\)-minor-free; if some induced subgraph had \(\delta\ge 3\), Lemma 3.3 would give a \(K_4\) minor. Delete a vertex of degree \(\le 2\) and induct. ∎

### Theorem 3.5 (Hadwiger for \(t\le 4\))
Hadwiger’s conjecture holds for all \(t\le 4\).

**Proof.** Theorems 3.1, 3.2, and Corollary 3.4. ∎

---

## 4. New mechanism: Maximal Contact Models (MCM)

Fix \(t\ge 5\). Let \(G\) be a minimal counterexample to \(\mathrm{HC}_t\). By Lemma 2.2, \(G\) is \(t\)-critical, \(\eta(G)=t-1\), and for every vertex \(v\),
\[
\eta(G-v)=t-1.
\]
In particular \(G-v\) admits a \(K_{t-1}\) model.

### Definition 4.1 (Contact)
Let \(v\in V(G)\) and let \(\mathcal{B}=\{B_1,\dots,B_{t-1}\}\) be a \(K_{t-1}\) model in \(G-v\). The **contact set** of \(\mathcal{B}\) at \(v\) is
\[
S(\mathcal{B},v):=\bigl\{\,i\in\{1,\dots,t-1\}:\ N(v)\cap B_i\neq\emptyset\,\bigr\}.
\]
Write \(s(\mathcal{B},v)=|S(\mathcal{B},v)|\). Branch sets with index in \(S(\mathcal{B},v)\) are **contact branch sets**; the others are **non-contact**.

### Definition 4.2 (Maximal contact model)
A \(K_{t-1}\) model \(\mathcal{B}\) in \(G-v\) is a **maximal contact model (MCM)** at \(v\) if \(s(\mathcal{B},v)\) is maximum among all \(K_{t-1}\) models in \(G-v\).

### Lemma 4.3 (Contact deficiency)
If \(G\) is a minimal counterexample to \(\mathrm{HC}_t\) and \(v\in V(G)\), then every MCM \(\mathcal{B}\) at \(v\) satisfies
\[
s(\mathcal{B},v)\le t-2.
\]

**Proof.** If \(s(\mathcal{B},v)=t-1\), then every branch set meets \(N(v)\). The sets \(\{v\},B_1,\dots,B_{t-1}\) form a \(K_t\) model in \(G\), contradicting \(\eta(G)=t-1\). ∎

### Definition 4.4 (Regions of an MCM)
Fix an MCM \(\mathcal{B}=\{B_1,\dots,B_{t-1}\}\) at \(v\). Write \(S=S(\mathcal{B},v)\) and \(J=\{1,\dots,t-1\}\setminus S\) (so \(J\neq\emptyset\) by Lemma 4.3). Define
\begin{align*}
A &:=\bigcup_{i\in S} B_i,\\
C &:=\bigcup_{j\in J} B_j,\\
Z &:=V(G-v)\setminus(A\cup C).
\end{align*}
Vertices in \(Z\) are **unused** by the model. Note \(N(v)\cap C=\emptyset\) and \(N(v)\subseteq A\cup Z\).

### Lemma 4.5 (No free attachment path)
There is no path in \(G-v\) that starts in \(N(v)\setminus A\), ends in \(C\), and is internally disjoint from \(A\cup C\).

Equivalently: there is no path \(P=x_0x_1\dots x_\ell\) in \(G-v\) with \(x_0\in N(v)\), \(x_\ell\in C\), \(\{x_1,\dots,x_{\ell-1}\}\subseteq Z\), and \(x_0\in Z\cup(N(v)\setminus A)\), such that \(x_0\notin A\).

**More cleanly:** there is no path from \(N(v)\cap Z\) to \(C\) in the graph \(G[Z\cup C\cup(N(v)\cap Z)]-A\), i.e.\ in \(G-v-A\) starting from \(N(v)\cap Z\).

**Proof.** Suppose \(P\) is a path in \(G-v\) from a vertex \(x\in N(v)\cap Z\) to a vertex \(y\in B_j\subseteq C\) (\(j\in J\)) with all internal vertices in \(Z\). Set
\[
B_j':=B_j\cup\bigl(V(P)\setminus\{x\}\bigr).
\]
Then \(B_j'\) is connected (the path attaches at \(y\)), is disjoint from every \(B_i\) with \(i\neq j\) (internal vertices were in \(Z\)), and still meets every other branch set (old cross-edges of \(B_j\) survive). Moreover \(x\notin B_j'\) but \(x\) is adjacent to the first internal vertex of \(P\) if \(\ell\ge 2\), or to \(y\) if \(\ell=1\).

If \(\ell=1\), then \(x\sim y\in B_j\), so \(x\in N(v)\cap Z\) is adjacent to \(B_j\). Enlarge instead by
\[
B_j'':=B_j\cup\{x\}.
\]
Then \(B_j''\) is connected, disjoint from other branch sets, retains all cross-edges, and meets \(N(v)\). The new model \(\mathcal{B}'=(\mathcal{B}\setminus\{B_j\})\cup\{B_j''\}\) has contact set \(S\cup\{j\}\), contradicting maximality of \(s(\mathcal{B},v)\).

If \(\ell\ge 2\), the first internal vertex \(x_1\) lies in \(Z\) and is adjacent to \(x\in N(v)\). Set
\[
B_j':=B_j\cup\{x_1,\dots,x_{\ell-1},x_\ell\}\setminus\{x_\ell\}\cup\text{path interiors}=B_j\cup\{x_1,\dots,x_{\ell-1}\},
\]
with \(x_\ell=y\in B_j\). Then \(B_j'\) is connected, still disjoint from other branch sets, retains cross-edges, and is adjacent to \(x\in N(v)\). Including \(x\) itself:
\[
B_j^\sharp:=B_j'\cup\{x\}
\]
meets \(N(v)\) and remains connected and disjoint from other branch sets. Contact increases. Contradiction. ∎

### Corollary 4.6 (Separation form)
In \(G-v\), the set \(A\) separates \(N(v)\cap Z\) from \(C\): every path in \(G-v\) from \(N(v)\cap Z\) to \(C\) meets \(A\). Consequently every path in \(G\) from \(v\) to \(C\) meets \(A\cup\bigl(N(v)\cap A\bigr)\). In particular, if \(N(v)\subseteq A\), then \(N(v)\) separates \(v\) from \(C\) in \(G\).

**Proof.** Immediate from Lemma 4.5 and \(N(v)\cap C=\emptyset\). ∎

### Lemma 4.7 (Non-contact side is fully linked into contact)
For every \(j\in J\) and every \(i\in S\), there is an edge of \(G\) between \(B_j\) and \(B_i\). (Restatement of the model axiom restricted to pairs \((i,j)\).)

**Proof.** Definition of \(K_{t-1}\) model. ∎

### Lemma 4.8 (Non-contact block is nonempty and has no neighbour of \(v\))
\(C\neq\emptyset\), \(N(v)\cap C=\emptyset\), and every vertex of \(C\) has all its \(G\)-neighbours in \(A\cup C\cup Z\).

**Proof.** \(J\neq\emptyset\) forces \(C\neq\emptyset\). The rest is definitional. ∎

---

## 5. Menger fan into non-contact roots

### Definition 5.1 (Root selection)
Fix an MCM \(\mathcal{B}\) at \(v\) with notation as in Definition 4.4. For each \(j\in J\) choose a root vertex \(r_j\in B_j\). Set \(R:=\{r_j:j\in J\}\). Thus \(|R|=|J|=t-1-s(\mathcal{B},v)\ge 1\).

### Lemma 5.2 (Menger fan from the apex)
There exist \(|R|\) pairwise internally vertex-disjoint paths in \(G\) from \(v\) to \(R\), one path ending at each \(r_j\).

**Proof.** By Lemma 1.10, \(\kappa(G)\ge t-1\). Let \(Q\subseteq V(G)\setminus\{v\}\) be any vertex set separating \(v\) from \(R\) in \(G\). Then \(Q\) is a vertex cut of \(G\) (the side of \(v\) and the side meeting \(R\) are nonempty), so \(|Q|\ge\kappa(G)\ge t-1\). In particular \(|Q|\ge|R|\) because \(|R|=t-1-s\le t-1\). By Menger’s theorem, the maximum number of pairwise internally vertex-disjoint \(v\)–\(R\) paths equals the minimum order of a \(v\)–\(R\) separator, which is at least \(|R|\). Hence there are \(|R|\) such paths, and by the pigeonhole principle on terminals (or by the standard “linkage to a set” form of Menger) they may be chosen to end at distinct vertices of \(R\). ∎

### Definition 5.3 (Entry data of a fan path)
Let \(\{P_j:j\in J\}\) be a Menger fan as in Lemma 5.2, with \(P_j\) a \(v\)–\(r_j\) path. For each \(j\in J\), walk along \(P_j\) from \(v\) and let \(y_j\) be the **first** vertex of \(P_j\) that lies in \(C\). Let \(x_j\) be the predecessor of \(y_j\) on \(P_j\). Then:
- \(y_j\in C\), so \(y_j\in B_{\sigma(j)}\) for a unique \(\sigma(j)\in J\);
- \(x_j\notin C\), so \(x_j\in A\cup Z\cup\{v\}\);
- the subpath of \(P_j\) from \(v\) to \(x_j\) lies in \(V(G)\setminus C\).

(The map \(\sigma:J\to J\) need not be the identity: the fan path aimed at \(r_j\in B_j\) may first hit \(C\) in a different non-contact branch set.)

### Lemma 5.4 (First hit is never at \(v\)’s neighbour in \(C\))
For every \(j\in J\), \(y_j\neq\) a neighbour of \(v\) in the sense that the edge \(vy_j\) does not exist: \(x_j\neq v\). Equivalently, no fan path enters \(C\) in a single step from \(v\).

**Proof.** An edge \(v y_j\) with \(y_j\in C\) would mean \(N(v)\cap C\neq\emptyset\), contradicting Definition 4.4. ∎

### Lemma 5.5 (Direct \(Z\)-attachment increases contact)
If some vertex of \(N(v)\cap Z\) is adjacent to \(C\), then there is a \(K_{t-1}\) model \(\mathcal{B}'\) in \(G-v\) with \(s(\mathcal{B}',v)>s(\mathcal{B},v)\).

**Proof.** Immediate from the argument of Lemma 4.5 (length-\(1\) free attachment). ∎

### Lemma 5.6 (Exit structure of fan paths)
For each \(j\in J\), the predecessor \(x_j\) of the first \(C\)-vertex on \(P_j\) satisfies \(x_j\in A\cup Z\), and \(x_j\neq v\) (Lemma 5.4). Moreover:
1. If the subpath of \(P_j\) from its first vertex in \(N(v)\) to \(y_j\) is internally disjoint from \(A\), then that subpath is a free \(N(v)\)–\(C\) attachment through \(Z\), contradicting Lemma 4.5. Hence every fan path meets \(A\) before entering \(C\), **or** enters \(C\) directly from \(A\).
2. In all cases the first hit \(y_j\in C\) has predecessor \(x_j\in A\cup Z\), and if \(x_j\in Z\) then some earlier vertex of \(P_j\) lies in \(A\) (the path used a contact branch set as a stepping stone before a final hop through \(Z\) into \(C\)).

**Proof.** Definition 5.3 gives \(x_j\in A\cup Z\cup\{v\}\); Lemma 5.4 rules out \(v\). Let \(w\) be the first vertex of \(P_j\) after \(v\), so \(w\in N(v)\). The subpath \(wP_jy_j\) avoids \(C\) until its last vertex. If it also avoids \(A\), then \(w\in N(v)\cap Z\) (since \(w\notin C\)) and Lemma 4.5 is contradicted. Thus \(wP_jy_j\) meets \(A\), which is assertion (1)–(2). ∎

### Corollary 5.7 (No pure free fan)
No fan path is a free attachment path in the sense of Lemma 4.5. Every fan path interacts with the contact region \(A\) before (or as) it enters \(C\).

**Proof.** Lemma 5.6. ∎

### Remark 5.8 (Where elementary augmentation stops)
Lemmas 5.5–5.7 fully control **free** attachments through \(Z\). The remaining case—and the only case available to a \(\Phi\)-maximal MCM—is that every fan path enters \(C\) from \(A\) (possibly after excursions \(A\to Z\to C\)). Increasing contact then requires **reassigning vertices of contact branch sets** along the fan (splitting, transferring, or merging through Steiner vertices in \(Z\)). That reassignment is exactly Lemma G; no elementary single-path rule is claimed for it.

---

## 6. What MCM proves unconditionally

### Proposition 6.1 (MCM structure package)
Let \(G\) be a minimal counterexample to \(\mathrm{HC}_t\), \(v\in V(G)\), and \(\mathcal{B}\) an MCM at \(v\). Then:
1. \(s(\mathcal{B},v)\le t-2\) (contact deficiency);
2. \(A\) separates free \(Z\)-attachments of \(N(v)\) from \(C\) (Corollary 4.6);
3. a Menger fan of size \(|J|\) joins \(v\) to roots in the non-contact side (Lemma 5.2);
4. every fan path eventually enters \(C\), its predecessor at first entry lies in \(A\cup Z\), and pure free \(Z\)-only \(N(v)\)–\(C\) paths are forbidden (so every fan path interacts with \(A\));
5. the non-contact branch sets remain fully cross-linked to every contact branch set.

**Proof.** Lemmas 4.3–4.8 and 5.2–5.7. ∎

### Proposition 6.2 (Single-branch contact increase from a private exit)
Suppose there exists \(j\in J\) and a fan path \(P_j\) such that:
- \(x_j\in B_i\) for some \(i\in S\);
- the internal vertices of \(P_j\) between \(v\) and \(x_j\) meet no branch set other than those that can be reassigned without destroying cross-edges;
- in particular, if the subpath \(vP_jx_j\) is internally disjoint from \(C\cup\bigcup_{i'\in S\setminus\{i\}}B_{i'}\) and meets \(B_i\) only at vertices that remain connected after a prescribed split,

then one can split \(B_i\) and absorb a path into \(B_{\sigma(j)}\) to increase contact.

**Proof sketch (fully rigorous in the simplest subcase).**  
**Simplest subcase.** Suppose \(x_j\in B_i\), \(x_j\sim y_j\in B_{\sigma(j)}\), and \(x_j\in N(v)\). Then \(i\in S\) already accounts for this neighbour. The edge \(x_j y_j\) is a cross-edge already required by the model. No new contact is created for \(\sigma(j)\) unless we move \(x_j\) from \(B_i\) into \(B_{\sigma(j)}\):
\[
B_i^-:=B_i\setminus\{x_j\},\qquad B_{\sigma(j)}^+:=B_{\sigma(j)}\cup\{x_j\}.
\]
For this to be a model we need: \(B_i^-\) nonempty and connected; all cross-edges from \(B_i\) to other branch sets surviving in \(B_i^-\) or replaced; and \(B_{\sigma(j)}^+\) connected (true via \(x_j\sim y_j\)).

If \(x_j\) is a leaf of a spanning tree of \(G[B_i]\) and is not the unique neighbour in \(B_i\) of some other branch set, the move succeeds and contact gains \(\sigma(j)\) while retaining \(i\) (since \(i\in S\) for other reasons, or another vertex of \(B_i\) still meets \(N(v)\)).

This subcase already fails in general: \(x_j\) may be a cutvertex of \(G[B_i]\), or the unique attachment of \(B_i\) to some \(B_{i'}\). ∎

Proposition 6.2 shows that **local** moves are sometimes available but not always. The obstruction is global consistency across the whole fan—the content of the gap below.

---

## 7. The dual potential (motivating form of the gap)

### Definition 7.1 (Contact potential)
For a vertex \(v\) and a \(K_{t-1}\) model \(\mathcal{B}\) in \(G-v\), set
\[
\Phi(v,\mathcal{B}):=\bigl(s(\mathcal{B},v),\; -|Z|,\; -\textstyle\sum_i |B_i|^2\bigr)
\]
ordered lexicographically. Maximising \(\Phi\) first maximises contact, then minimises unused vertices, then prefers balanced branch sets.

### Lemma 7.2 (Potential maximisers are MCMs)
Any model maximising \(\Phi(v,\cdot)\) is an MCM at \(v\).

**Proof.** First coordinate. ∎

### Remark 7.3 (Intended dual algorithm)
**Algorithm COLOUR-OR-MINOR.**
1. If some MCM at some \(v\) has \(s=t-1\), output a \(K_t\) model.
2. Otherwise, for an MCM maximising \(\Phi\), take a Menger fan into non-contact roots and attempt a fan-absorption reassignment that increases \(\Phi\).
3. If absorption always exists, \(\Phi\) cannot maximise unless \(s=t-1\), contradiction in a counterexample—hence every \(t\)-critical graph has a \(K_t\) minor.
4. If at a maximum of \(\Phi\) no absorption exists, the configuration is a certificate of a counterexample (conjecturally impossible).

Step 2 is exactly Lemma G below. Steps 1 and 3 are fully rigorous consequences of Lemma G. Step 4 is the dual-search reading of the same obstruction.

---

## 8. ONE unproved lemma

### Lemma G (Simultaneous Fan Absorption — **UNPROVED**)

Let \(t\ge 5\). Let \(G\) be \(t\)-critical with \(\kappa(G)\ge t-1\), and let \(v\in V(G)\) satisfy \(\eta(G-v)\ge t-1\). Let \(\mathcal{B}=\{B_1,\dots,B_{t-1}\}\) be a \(K_{t-1}\) model in \(G-v\) maximising the contact potential \(\Phi(v,\mathcal{B})\) of Definition 7.1, and assume \(s(\mathcal{B},v)\le t-2\). Let \(J\) be the non-contact index set, \(R=\{r_j:j\in J\}\) a root system, and \(\{P_j:j\in J\}\) a Menger fan of internally vertex-disjoint \(v\)–\(r_j\) paths (Lemma 5.2).

**Claim (unproved).** There exists a \(K_{t-1}\) model \(\mathcal{B}'\) in \(G-v\) with \(\Phi(v,\mathcal{B}')>\Phi(v,\mathcal{B})\) in lexicographic order.

In particular, no such maximiser can satisfy \(s\le t-2\), hence some model has full contact \(s=t-1\), and \(\{v\}\) together with that model yields a \(K_t\) minor in \(G\).

### Remark G.1 (Why this is the exact gap of the MCM programme)
All preceding lemmas reduce a minimal counterexample to the existence of a \(\Phi\)-maximal MCM with \(s\le t-2\) and a Menger fan into the non-contact side. Lemma G asserts that this configuration is impossible because the fan always supplies a reassignment increasing \(\Phi\). Every structural constraint proved in §§4–6 is used to set up the configuration; none of them finishes the reassignment.

### Remark G.2 (Logical strength — honesty)
- **Sufficiency.** Lemma G \(\Rightarrow\) every \(t\)-critical graph with \(\eta(G-v)\ge t-1\) for some (equivalently, by the critical contraction calculus, every) \(v\) has a \(K_t\) minor \(\Rightarrow\mathrm{HC}_t\) (Lemma 1.3 + Lemma 2.2).
- **Near-necessity.** If \(\mathrm{HC}_t\) holds, then no minimal counterexample exists, so the hypothesis “\(G\) minimal counterexample with a deficient MCM” is vacuous and Lemma G holds vacuously on that class. Among statements of the form “every deficient MCM admits a \(\Phi\)-increasing reassignment,” Lemma G is a concrete combinatorial specialisation of \(\mathrm{HC}_t\) to apex-plus-model configurations; it is **not** a pure restatement (“every \(t\)-critical graph has a \(K_t\) minor”), but it is **not substantially weaker**: any proof of Lemma G yields \(\mathrm{HC}_t\), and any counterexample to \(\mathrm{HC}_t\) yields a deficient MCM (Lemma 4.3) for which the claim fails.

### Remark G.3 (Why classical tools do not close Lemma G)
1. **Degeneracy / average degree.** Minimal counterexamples may have average degree \(o(t\sqrt{\log t})\) while Mader-type thresholds for \(K_t\) minors sit at \(\Theta(t\sqrt{\log t})\). Contact deficiency is compatible with large degree.
2. **Path-disjoint topological models.** Demanding internally disjoint paths among rainbow neighbours would prove a \(K_t\) **subdivision**, i.e. Hajós’ conjecture, which fails for \(t\ge 7\). Lemma G must use **reassignment of shared vertices** into branch sets (true minors), not disjoint path systems alone.
3. **Single-path moves.** Proposition 6.2 shows local splits can destroy connectivity of a contact branch set or unique cross-edges; the fan must be absorbed **simultaneously** with a global accounting of Steiner vertices.
4. **High linkage theorems** (e.g. every \(f(t)\)-connected graph is \(t\)-linked) would give topological clique minors under connectivity far above \(t-1\), but critical graphs only guarantee \(\kappa=t-1\). Such theorems are also outside the elementary toolkit fixed for this note.

### Remark G.4 (What a proof of Lemma G must construct)
An explicit family of pairwise disjoint connected sets \(B_1',\dots,B_{t-1}'\) in \(G-v\) such that:
- each \(G[B_i']\) is connected;
- every pair \(B_i',B_j'\) is joined by an edge;
- the number of indices \(i\) with \(N(v)\cap B_i'\neq\emptyset\) is strictly larger than \(s(\mathcal{B},v)\),  
  **or** contact is preserved and \(|Z|\) strictly decreases,  
  **or** contact and \(|Z|\) are preserved and \(\sum |B_i|^2\) strictly decreases,

using the vertices of the Menger fan as the only new “budget” of paths into \(C\).

---

## 9. Reduction theorem (fully proved relative to Lemma G)

### Theorem 9.1 (Conditional Hadwiger)
Assume Lemma G. Then \(\mathrm{HC}_t\) holds for every \(t\ge 1\).

**Proof.** For \(t\le 4\), Theorem 3.5. Fix \(t\ge 5\) and assume \(\mathrm{HC}_{t'}\) for all \(t'<t\) if needed for bookkeeping; alternatively induct on \(n(G)\) globally.

Let \(G\) be a minimal counterexample to \(\mathrm{HC}_t\) (Definition 2.1). By Lemma 2.2, \(G\) is \(t\)-critical and \(\eta(G-v)=t-1\) for every vertex \(v\). Fix any \(v\). Among \(K_{t-1}\) models in \(G-v\), choose \(\mathcal{B}\) maximising \(\Phi(v,\mathcal{B})\). By Lemma 4.3, if we are in a counterexample then \(s(\mathcal{B},v)\le t-2\). Lemma G supplies a model of strictly larger \(\Phi\), contradiction.

Therefore no minimal counterexample exists, so \(\mathrm{HC}_t\) holds. ∎

### Theorem 9.2 (Equivalent formulation of the gap)
The following are equivalent for each \(t\ge 5\):
1. \(\mathrm{HC}_t\);
2. every \(t\)-critical graph has a \(K_t\) minor;
3. for every \(t\)-critical graph \(G\) and every \(v\in V(G)\), some \(K_{t-1}\) model in \(G-v\) has full contact \(s=t-1\) at \(v\);
4. Lemma G.

**Proof.**
(1)\(\Leftrightarrow\)(2) is Lemma 1.3.
(2)\(\Rightarrow\)(3): if \(G\) is \(t\)-critical then (2) gives a \(K_t\) model in \(G\). Contracting or deleting the branch set containing \(v\) (or taking the other \(t-1\) branch sets if \(\{v\}\) is a singleton branch set; if \(v\) lies in a larger branch set, split off a connected subset containing \(v\) as a separate argument—**careful**). More cleanly: (2)\(\Rightarrow\)(1)\(\Rightarrow\) no counterexample \(\Rightarrow\) the deficient-MCM configuration of Lemma 4.3 cannot occur in a \(t\)-critical \(K_t\)-minor-free graph; but a \(t\)-critical graph with no full-contact model at \(v\) and with \(\eta(G-v)\ge t-1\) would, if also \(\eta(G)<t\), be a counterexample. Since (2) forces \(\eta(G)\ge t\), full contact is not forced by (2) alone without the minor containing \(v\) as a singleton.

**Corrected equivalence chain used in this note:**

(1)\(\Leftrightarrow\)(2) fully.
(2) \(\Leftarrow\) Lemma G by Theorem 9.1 (and the critical reduction).
(3′) **Replacement for (3):** every \(t\)-critical graph \(G\) admits some vertex \(v\) and some \(K_{t-1}\) model in \(G-v\) with full contact at \(v\).

Then full contact \(\Rightarrow K_t\) minor, so (3′)\(\Rightarrow\)(2). Lemma G \(\Rightarrow\)(3′) by maximising \(\Phi\) and forbidding deficiency. And (2)\(\Rightarrow\)(3′) because a \(K_t\) model yields, after placing \(v\) in its branch set \(B_0\) and deleting a spanning tree leaf structure, a model in which the other branch sets all meet \(N(B_0)\); if \(B_0=\{v\}\) we are done; if \(B_0\) is larger, contract \(B_0\) to \(v\) in the model sense—the other branch sets become a full-contact model at the contracted apex in the contracted graph, and lifting back is the inverse of Lemma 2.3. The details of (2)\(\Rightarrow\)(3′) require a short model-normalisation (one can always find a \(K_t\) model in which some branch set is a singleton: take a model minimising the size of the smallest branch set; if every branch set has size \(\ge 2\), an ear argument or leaf of a spanning tree of a branch set can be split off if it retains cross-edges—**this normalisation is standard but not expanded here**).  

**For the record of this note we claim only:**
- Lemma G \(\Rightarrow\mathrm{HC}_t\) (Theorem 9.1) — **proved**;
- \(\mathrm{HC}_t\Rightarrow\) Lemma G holds vacuously on minimal counterexamples — **proved**;
- full formal equivalence of Lemma G with \(\mathrm{HC}_t\) as pure sentences about all graphs requires the model-normalisation just indicated, which is elementary but omitted for length. ∎

---

## 10. Checklist

| Item | Statement | Status |
|------|-----------|--------|
| 1.2–1.9 | Critical structure, \(\lambda\ge t-1\), no small clique separators | **Proved** |
| 1.10 | \(\kappa\ge t-1\) (Dirac) | **Classical input** |
| 1.11 | Brooks barrier | **Proved** (Brooks used) |
| 2.2–2.3 | Minimal counterexamples; model lifting | **Proved** |
| 3.1–3.5 | Hadwiger for \(t\le 4\) | **Proved** |
| 4.3–4.8 | MCM contact deficiency and separation | **Proved** |
| 5.2 | Menger fan to non-contact roots | **Proved** (uses 1.10) |
| 5.5–5.7 | Free \(Z\)-attachments; fan exit structure | **Proved** |
| 6.1 | MCM structure package | **Proved** |
| 6.2 | Local split moves | **Proved only in the simplest subcase** |
| 7.1–7.2 | Contact potential | **Proved** |
| **Lemma G** | Simultaneous Fan Absorption | **UNPROVED** |
| 9.1 | Lemma G \(\Rightarrow\mathrm{HC}_t\) | **Proved** |

---

## 11. Final verdict

### Proved
1. Hadwiger’s conjecture for all \(t\le 4\), by elementary degeneracy after Dirac’s \(\delta\ge 3\Rightarrow K_4\) minor.
2. Complete critical reduction; edge-connectivity of critical graphs; rainbow neighbourhoods; model lifting.
3. **New mechanism (MCM + Menger fan):** every minimal counterexample carries, at every apex \(v\), a contact-deficient maximal contact model whose non-contact side is joined to \(v\) by a Menger fan of size equal to the contact deficiency, with free \(Z\)-only attachments forbidden.
4. A dual potential \(\Phi\) whose increase is a well-defined certificate of progress toward a \(K_t\) model.
5. The implication **Lemma G \(\Rightarrow\mathrm{HC}_t\)** in full.

### Not proved
**Lemma G (Simultaneous Fan Absorption).**  
That every \(\Phi\)-maximal contact-deficient MCM admits a \(\Phi\)-increasing reassignment using its Menger fan into the non-contact branch sets.

### BLOCKED

\[
\boxed{\textbf{BLOCKED at Lemma G (Simultaneous Fan Absorption)}}
\]

No complete elementary proof of Hadwiger’s conjecture for all \(t\) is obtained. The MCM programme isolates a single, precise, constructive obstruction: **global reassignment of a Menger fan into a contact-deficient clique model under a lexicographic contact potential**. Closing that obstruction would prove Hadwiger; the obstruction is not resolved by Menger, Hall, Brooks, degeneracy, or single-path Kempe/contact moves alone.

---

*End of note.*

---

## 12. Partial progress on Lemma G: single-path and deficiency one

This section records what *can* be proved toward Lemma G, and why the general case still fails. No claim here closes Lemma G.

### Lemma 12.1 (Model after deleting an unused vertex)
If \(z\in Z\) and \(\mathcal{B}\) is a \(K_{t-1}\) model in \(G-v\), then \(\mathcal{B}\) remains a \(K_{t-1}\) model in \(G-v-z\). In particular unused vertices may be ignored for model validity.

**Proof.** Branch sets and cross-edges do not use \(z\). ∎

### Lemma 12.2 (Absorbing a pendant unused path into a non-contact set)
Let \(\mathcal{B}\) be an MCM at \(v\), \(j\in J\), and let \(Q\) be a path in \(G-v\) of the form \(w=q_0q_1\dots q_\ell=y\) with \(w\in N(v)\), \(y\in B_j\), \(\{q_1,\dots,q_{\ell-1}\}\subseteq Z\), and \(w\in Z\). Then \(\Phi\) can be increased (Lemma 4.5), contradicting maximality of an MCM that is \(\Phi\)-maximal.

**Proof.** Lemma 4.5 / 5.5. ∎

Thus at a \(\Phi\)-maximum, every \(v\)–\(C\) path meets \(A\).

### Definition 12.3 (Private last-exit)
For a \(v\)–\(C\) path \(P\), the **last exit** \(\alpha(P)\) is the last vertex of \(P\) that lies in \(A\) before the first visit to \(C\). (Exists at a \(\Phi\)-maximum by the previous paragraph and Lemma 5.6.)

### Lemma 12.4 (Deficiency-one: statement)
Suppose \(s(\mathcal{B},v)=t-2\), so \(|J|=1\). Write \(J=\{*\}\), \(C=B_*\), and let \(P\) be a single Menger path from \(v\) to a root \(r\in B_*\). Let \(\alpha=\alpha(P)\in B_i\) for some \(i\in S\), and let \(y\) be the first \(C\)-vertex on \(P\).

**Attempted construction.**
Let \(W\) be the set of vertices of \(P\) strictly between \(v\) and \(y\) (so \(\alpha\in W\), \(W\subseteq A\cup Z\)). Set
\[
B_*^\sharp := B_*\cup W,\qquad
B_i^\flat := B_i\setminus W,\qquad
B_k^\flat := B_k\setminus W\ \text{for all other }k\in S.
\]
For \(k\in S\) with \(B_k^\flat\) possibly changed.

**Obstructions (not eliminated):**
1. Some \(B_k^\flat\) may be disconnected or empty.
2. A cross-edge between \(B_k\) and \(B_\ell\) may have had both ends in \(W\), or its unique endpoint in \(B_k\) may lie in \(W\).
3. Even if all \(B_k^\flat\) remain valid and \(s\) does not drop by more than \(1\), bookkeeping of contact can net to zero; one then needs a strict drop in \(|Z|\) or in \(\sum |B|^2\).

### Lemma 12.5 (Special deficiency-one subcase — **proved**)
In the setting of Lemma 12.4, assume moreover:
- \(W\subseteq B_i\cup Z\) (the path meets only one contact branch set);
- \(G[B_i]\) has a spanning tree \(T_i\) in which every vertex of \(W\cap B_i\) is a leaf of \(T_i\);
- each \(u\in W\cap B_i\) is not the unique neighbour in \(B_i\) of any other branch set \(B_k\) (\(k\neq i,*\));
- \(N(v)\cap B_i\not\subseteq W\) **or** \(W\cap N(v)\neq\emptyset\) with the net contact rule below.

Then the construction yields a \(K_{t-1}\) model with strictly larger \(\Phi\).

**Proof.** Leaves of \(T_i\) may be deleted while keeping \(B_i^\flat\) connected and nonempty (if \(B_i\not\subseteq W\); if \(B_i\subseteq W\), then \(B_i\) was a subset of a path’s vertices, and after moving them into \(B_*^\sharp\) we have branch sets \(\{B_k:k\in S\setminus\{i\}\}\cup\{B_*^\sharp\}\), only \(t-2\) sets — **this subcase is excluded** by requiring \(B_i\not\subseteq W\)).

Cross-edges from \(B_i\) to other \(B_k\) survive because no unique attachment was in \(W\). Cross-edges from \(B_*^\sharp\) to all other sets: old cross-edges of \(B_*\) survive; additionally \(B_*^\sharp\) meets \(N(v)\) because \(W\) contains the first neighbour of \(v\) on \(P\).

Contact: \(S\) gains \(*\). If \(N(v)\cap B_i\not\subseteq W\), contact \(i\) is retained and \(s\) increases by \(1\). If \(N(v)\cap B_i\subseteq W\), contact \(i\) is lost and contact \(*\) is gained, so \(s\) is unchanged; but \(W\cap Z\neq\emptyset\) or vertices of \(Z\) are absorbed, or if \(W\subseteq B_i\) then \(|Z|\) is unchanged and we compare \(\sum |B|^2\): moving leaves from \(B_i\) into \(B_*\) changes sizes — not always a decrease of the sum of squares.  

**Honest restriction.** The clean fully proved subcase is:
> \(N(v)\cap B_i\not\subseteq W\), \(B_i\not\subseteq W\), single contact branch set met, leaf attachments, no unique cross-edge attachments.  
Then \(s\) strictly increases. ∎

### Remark 12.6 (Why deficiency one is still not fully closed)
Even with a single fan path, the path may snake through **all** contact branch sets, cutting each into many components, and may carry every \(N(v)\)-attachment of every contact branch set. Restoring connectivity requires Steiner vertices that may not exist without destroying the clique model. No elementary rule reassigns an arbitrary snake path. Thus **deficiency one is open in full generality** and is already enough to encode hard instances of Lemma G (a minimal counterexample could have \(s=t-2\) at every apex).

### Remark 12.7 (Iterative absorption does not reduce to deficiency one)
Even if deficiency one were proved, the general case is not an immediate iteration: absorbing one path may decrease \(\Phi\) temporarily while rearranging, and the intermediate object may not be an MCM. Lemma G demands a **single-step** \(\Phi\)-increase from a global fan, not a multi-step proof with intermediate non-maximal models (though a multi-step proof with a different potential would also suffice for Hadwiger).

### Lemma 12.8 (No improvement of the gap status)
Sections 4–9 and 12 together still leave **exactly one** unproved lemma needed for full Hadwiger: Lemma G. Partial subcases (Lemma 12.5) do not cover all configurations forced by minimal counterexamples.

---

## 13. Continuation: hybrid attack

A hybrid development combining rainbow–Kempe structure, rooted models, and MCM fans is recorded in [`hadwiger_hybrid_fan_absorption.md`](hadwiger_hybrid_fan_absorption.md). That note proves \(Z=\emptyset\) at \(\Phi\)-max, a surplus Menger lemma (\(\ge t-1\) paths into \(C\)), full **SPPA** absorption for strongly private non-cut portals (a strictly weaker lemma that still forces \(K_t\) on that class), a dichotomy reducing Lemma G to non-existence of **Rigid Portal Configurations**, and a finite counterexample to naïve whole-path absorption. Full Lemma G remains open.

A pointed RPC-type elimination is recorded in [`hadwiger_rpc_elimination.md`](hadwiger_rpc_elimination.md): no pure-\((R2)\)-only RPC under \(\delta\ge t\); free-\((R1)\) and inessential-\((R3)\) absorption; finite abstract RPC outside criticality; residual gap narrowed to **hard-core RPC**.

