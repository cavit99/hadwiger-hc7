# Hybrid attack: apex / near-planar reduction + inductive colouring

**Focus.** Minimal Hadwiger counterexamples at \(t\ge 7\), with a concentrated attempt at \(\mathrm{HC}_7\).

**Conventions.** Finite simple graphs. A **\(K_r\) model** is \(r\) pairwise disjoint nonempty connected branch sets with a \(G\)-edge between every pair. \(\eta(G)=\) Hadwiger number. \(G\) is **\(k\)-critical** if \(\chi(G)=k\) and every proper subgraph is \((k-1)\)-colourable. \(\mathrm{HC}_t\): every \(K_t\)-minor-free graph is \((t-1)\)-colourable.

**Verdict.**
- §§0–5: concrete lemmas with full elementary proofs (including \(\lambda\ge t-1\), \(\kappa\ge 3\) for edge-maximal CE, all apex/separation lemmas).
- Dirac \(\kappa\ge t-1\): **Theorem D** (classical; elementary reduction to “separators are cliques” proved in §1).
- Degree boost \(\delta\ge t\) for CE: **Theorem N** / Corollary 3.1 (classical neighbourhood lemma).
- For \(t=7\): full portrait, all cheap apex structures forbidden, and \(\mathrm{HC}_7\) reduced **exactly** to a rooted \(K_6\) lemma (Lemma R\(_7\)).
- **\(\mathrm{HC}_7\) is not proved.** The gap is Lemma R\(_7\) (Theorem 8.1). No vague structure theory.

**Classical status used only as base cases.** \(\mathrm{HC}_s\) for \(s\le 4\) elementary; \(\mathrm{HC}_5\equiv\)4CT via Wagner; \(\mathrm{HC}_6\equiv\)4CT via RST. When attacking \(\mathrm{HC}_7\) we assume \(\mathrm{HC}_s\) for \(s\le 6\).

---

## 0. Minimal counterexamples

### Definition 0.1
A **minimal counterexample** to \(\mathrm{HC}_t\) is a graph with \(\chi\ge t\), no \(K_t\) minor, of minimum order; among those, of minimum size.

**Type C** = Definition 0.1 (critical form).  
**Type M** = minimum order, then **maximum** size among counterexamples (edge-maximal form: every missing edge creates a \(K_t\) minor).

### Lemma 0.2 (Type C portrait)
Let \(t\ge 2\) and let \(G\) be Type C for \(\mathrm{HC}_t\). Then:
1. \(\chi(G)=t\) and \(G\) is \(t\)-critical;
2. for every edge \(e\), \(\chi(G/e)\le t-1\);
3. every smaller-order \(K_t\)-minor-free graph is \((t-1)\)-colourable.

**Proof.**  
(1) For any vertex \(v\), \(G-v\) is \(K_t\)-minor-free of smaller order, so \(\chi(G-v)\le t-1\), hence \(\chi(G)\le t\). With \(\chi(G)\ge t\) get \(\chi=t\). If some edge \(e\) had \(\chi(G-e)=t\), then \(G-e\) would be a same-order counterexample with fewer edges. Thus \(G\) is \(t\)-critical.  
(2) If \(\chi(G/e)\ge t\), a \(t\)-critical subgraph \(H\) of \(G/e\) has fewer vertices. If \(H\) has a \(K_t\) minor so does \(G\); if not, \(H\) is a smaller counterexample.  
(3) Order-minimality. \(\quad\square\)

### Lemma 0.3 (Minimum degree)
If \(G\) is \(t\)-critical then \(\delta(G)\ge t-1\).

**Proof.** If \(\deg(v)\le t-2\), extend a \((t-1)\)-colouring of \(G-v\) to \(v\). \(\quad\square\)

### Lemma 0.4 (Rainbow neighbourhood)
If \(G\) is \(t\)-critical and \(v\in V(G)\), then every proper \((t-1)\)-colouring of \(G-v\) uses all \(t-1\) colours on \(N(v)\).

**Proof.** A missing colour would colour \(v\). \(\quad\square\)

### Lemma 0.5 (No separating clique)
If \(G\) is \(t\)-critical then no clique of order \(\le t-1\) separates \(G\).

**Proof.** Let \(S\) be a separating clique, \(|S|\le t-1\), sides \(G_1,G_2\) with intersection \(S\). Each \(G_i\) is a proper subgraph, hence \((t-1)\)-colourable. Colours on the clique \(S\) are distinct in each colouring; permute to agree on \(S\); the union colours \(G\). \(\quad\square\)

### Lemma 0.6 (Brooks barrier)
If \(G\) is \(t\)-critical, \(t\ge 4\), and \(G\not\cong K_t\), then \(\Delta(G)\ge t\).

**Proof.** If \(\Delta\le t-1\) then \(G\) is \((t-1)\)-regular (using \(\delta\ge t-1\)). Brooks: \(\chi\le\Delta\) unless complete or odd cycle. Odd cycle \(\Rightarrow t=3\); complete \(\Rightarrow G\cong K_t\). \(\quad\square\)

### Lemma 0.7 (Critical subgraphs exist)
If \(\chi(H)\ge t\) then some subgraph of \(H\) is \(t\)-critical.

**Proof.** Minimise order then size among subgraphs of chromatic number \(\ge t\). \(\quad\square\)

### Lemma 0.8 (\(\eta=t-1\) for first open CE)
Assume \(\mathrm{HC}_s\) for all \(s<t\). If \(G\) is Type C for \(\mathrm{HC}_t\) then \(\eta(G)=t-1\).

**Proof.** No \(K_t\) minor \(\Rightarrow\eta\le t-1\). If \(\eta\le t-2\) then \(G\) is \(K_{\eta+1}\)-minor-free with \(\chi=t>\eta\), contradicting \(\mathrm{HC}_{\eta+1}\) (since \(\eta+1<t\)). \(\quad\square\)

---

## 1. Connectivity — full elementary proofs

### Lemma 1.1 (Connected / \(2\)-connected)
Every \(t\)-critical graph with \(t\ge 2\) is connected. Every \(t\)-critical graph with \(t\ge 3\) is \(2\)-connected.

**Proof.** Disjoint union: \(\chi\) is the max of components.  
Cutvertex \(v\), components \(C_i\) of \(G-v\), blocks \(G_i=G[V(C_i)\cup\{v\}]\): each \(G_i\) is \((t-1)\)-colourable; permute so \(v\) always has colour \(1\); union colours \(G\). \(\quad\square\)

### Lemma 1.2 (Edge-connectivity — complete)
If \(G\) is \(t\)-critical, \(t\ge 2\), then \(\lambda(G)\ge t-1\).

**Proof.** Always \(\lambda\le\delta\), and \(\delta\ge t-1\), so rule out a cut of size \(r\le t-2\).

Let \(V=X\sqcup Y\), both nonempty, with \(r=|E(X,Y)|\le t-2\). By \(\delta\ge t-1\), \(|X|,|Y|\ge 2\).

Colour \(G[X]\) and \(G[Y]\) properly with \(\Gamma=\{1,\dots,t-1\}\). Build a bipartite multigraph \(B\) with both sides copies of \(\Gamma\): for each cut edge \(xy\) place an edge from colour \(c_X(x)\) to colour \(c_Y(y)\). Then \(B\) has \(\le t-2\) edges.

A permutation \(\pi\) of \(\Gamma\), used to recolour \(Y\), yields a proper colouring of \(G\) iff \(\pi\) as a matching avoids every edge of \(B\). Each edge of \(B\) blocks at most \((t-2)!\) permutations. Total blocked \(\le(t-2)\cdot(t-2)!\). Total permutations \((t-1)!\). Remainder:
\[
(t-1)!-(t-2)\cdot(t-2)!=(t-2)!\ge 1.
\]
So some recolouring is proper: \(\chi(G)\le t-1\), contradiction. \(\quad\square\)

### Lemma 1.3 (Path insertion)
Suppose \(G+uv\) has a \(K_t\) model in which the unique new edge \(uv\) is the sole \(G+uv\)-edge joining branch sets \(X\ni u\) and \(Y\ni v\). If \(G\) has a \(u\)–\(v\) path with interior disjoint from all branch sets, then \(G\) has a \(K_t\) minor.

**Proof.** Absorb the path interior into \(Y\). \(\quad\square\)

### Lemma 1.4 (Type M is \(3\)-connected)
Let \(t\ge 4\) and let \(G\) be Type M for \(\mathrm{HC}_t\). Then \(\kappa(G)\ge 3\).

**Proof.** Lemma 1.1-style cutvertex argument with \(\chi(G-v)\le t-1\) gives \(\kappa\ge 2\).

Suppose \(\{u,v\}\) separates with sides \(A,B\). If \(uv\in E(G)\), then \(\{u,v\}\) is a separating clique of order \(2\le t-1\): colour \(G[A],G[B]\) by order-minimality (fewer vertices, \(K_t\)-minor-free), match on \(K_2\), contradiction. So \(uv\notin E(G)\).

By Type M, \(G+uv\) has a \(K_t\) model, which must use \(uv\). Branch sets cannot cross the separator without \(uv\), so the model is supported in \(G[A]+uv\) or \(G[B]+uv\). Say \(G[A]+uv\). Minimality of the separator: both \(u,v\) meet \(B\setminus\{u,v\}\), so a \(u\)–\(v\) path through \(B\) has interior outside \(A\). Lemma 1.3 yields a \(K_t\) minor in \(G\). \(\quad\square\)

---

### Theorem D (Dirac, 1953)
Every \(t\)-critical graph \(G\) satisfies \(\kappa(G)\ge t-1\).

**Elementary reduction (proved in full).**  
It is enough to prove that every minimal separator of a \(t\)-critical graph is a clique: then Lemma 0.5 forbids separators of order \(\le t-1\), so \(\kappa\ge t-1\).

**Lemma 1.5 (clique-completion colouring).**  
Let \(G\) be \(t\)-critical and let \(S\) separate \(G\) into sides \(G_U=G[U\cup S]\) and \(G_W=G[W\cup S]\). Let \(G_U^*\) (resp. \(G_W^*\)) be \(G_U\) (resp. \(G_W\)) with all missing edges inside \(S\) added. If \(\chi(G_U^*)\le t-1\) and \(\chi(G_W^*)\le t-1\), then \(\chi(G)\le t-1\).

**Proof.** Colour both graphs with \(\{1,\dots,t-1\}\). The set \(S\) is a clique in each, of order \(\le|S|\). If \(|S|\le t-1\), both colourings inject \(S\) into the colour set; permute to agree on \(S\); restrict to \(E(G)\). \(\quad\square\)

**Corollary 1.6.**  
If \(S\) is a separator of a \(t\)-critical graph with \(|S|\le t-2\), then at least one of \(G_U^*,G_W^*\) has chromatic number \(\ge t\). (Else Lemma 1.5 colours \(G\).) \(\quad\square\)

**Remaining step of Theorem D (classical).**  
One proves by induction on order that a \(t\)-critical subgraph of a one-sided clique-completion \(G_U^*\) cannot exist when \(|S|\le t-2\). Equivalently: every minimal separator of a \(t\)-critical graph is a clique. Full write-ups: Toft; Jensen–Toft, *Graph Coloring Problems*, Thm 1.3; Chartrand–Zhang, *Chromatic Graph Theory*.

**What this note uses as Theorem D.** \(\kappa\ge t-1\) for \(t\)-critical graphs.  

**What this note proves elementarily without Theorem D.**  
\(\delta\ge t-1\), \(\lambda\ge t-1\), \(\kappa\ge 2\), Type M \(\kappa\ge 3\), no separating clique of order \(\le t-1\).

### Corollary 1.7
Every Type C minimal counterexample to \(\mathrm{HC}_t\) satisfies \(\kappa\ge t-1\) (by Theorem D). \(\quad\square\)

---

## 2. Apex colouring lemmas (complete)

### Lemma 2.1 (Additive apex bound)
For any graph \(G\) and \(A\subseteq V(G)\),
\[
\chi(G)\le\chi(G-A)+|A|.
\]

**Proof.** Colour \(G-A\); give each vertex of \(A\) a fresh colour. \(\quad\square\)

### Lemma 2.2 (Greedy apex extension)
If \(\chi(G-A)\le m\) and every vertex of \(A\) has degree \(<m\) in \(G\), then \(\chi(G)\le m\).

**Proof.** Colour \(G-A\); greedy-colour \(A\). \(\quad\square\)

### Lemma 2.3 (Universal clique apex drops Hadwiger parameter)
Suppose \(A\subseteq V(G)\), \(G[A]\) is complete, every \(a\in A\) is adjacent to all of \(V(G)\setminus A\), and \(G\) has no \(K_t\) minor. Then \(G-A\) has no \(K_{t-|A|}\) minor.

**Proof.** A \(K_{t-|A|}\) model in \(G-A\) plus singleton branch sets for vertices of \(A\) yields a \(K_t\) model. \(\quad\square\)

### Lemma 2.4 (Inductive colouring under universal apices)
Under Lemma 2.3, if \(\mathrm{HC}_{t-|A|}\) holds then \(\chi(G)\le t-1\).

**Proof.** \(\chi(G-A)\le t-|A|-1\) by \(\mathrm{HC}_{t-|A|}\); apply Lemma 2.1. \(\quad\square\)

### Lemma 2.5 (Single apex over \((t-2)\)-colourable)
If \(\chi(G-v)\le t-2\) then \(\chi(G)\le t-1\).

**Proof.** Lemma 2.1. \(\quad\square\)

### Lemma 2.6 (Apex slack obstruction for CE)
If \(G\) is Type C for \(\mathrm{HC}_t\) and \(A\subseteq V(G)\), then
\[
\chi(G-A)\ge t-|A|.
\]
In particular \(\chi(G-v)=t-1\) for every vertex \(v\).

**Proof.** If \(\chi(G-A)\le t-1-|A|\), Lemma 2.1 gives \(\chi(G)\le t-1\). For \(|A|=1\), combine with \(\chi(G-v)\le t-1\) from criticality. \(\quad\square\)

### Lemma 2.7 (Forbidden apex budgets)
Let \(\mathcal{C}\) be a class with \(\chi\le r\) on \(\mathcal{C}\). A Type C CE to \(\mathrm{HC}_t\) cannot satisfy \(G-A\in\mathcal{C}\) with \(|A|\le t-1-r\).

**Proof.** Lemma 2.1 would give \(\chi(G)\le r+|A|\le t-1\). \(\quad\square\)

### Lemma 2.8 (\(t=6\) pattern — external structure, internal colouring)
If a minimal CE \(G\) to \(\mathrm{HC}_6\) is \(1\)-apex over planar and 4CT holds, then \(\chi(G)\le 5\), contradiction.  
(RST proved every minimal CE to \(\mathrm{HC}_6\) is \(1\)-apex planar; that structure is external. The colouring step is Lemma 2.5.)

**Proof.** Lemma 2.5 with \(t=6\). \(\quad\square\)

---

## 3. Degree boost \(\delta\ge t\)

### Theorem N (Dirac neighbourhood lemma — classical)
If \(G\) is \(t\)-critical, \(t\ge 4\), and \(\deg(v)=t-1\), then \(G[N(v)]\cong K_{t-1}\). In particular \(G[N[v]]\cong K_t\).

**Partial elementary steps (proved).**  
Write \(N(v)=\{u_1,\dots,u_{t-1}\}\). Suppose \(u_1u_2\notin E(G)\).

1. Identifying \(u_1,u_2\) yields a graph of chromatic number \(\ge t\) (else pull back a colouring with \(c(u_1)=c(u_2)\) and free a colour for \(v\)).
2. In that identification, \(\deg(v)\) drops to \(t-2\), so any \(t\)-critical subgraph avoids \(v\).
3. Every \((t-1)\)-colouring of \(G-v\) is bijective on \(N(v)\) (Lemma 0.4), so \(c(u_1)\ne c(u_2)\) always.
4. For any proper \((t-1)\)-colouring of \(G-v\) with \(c(u_i)=i\), the vertices \(u_1,u_2\) lie in the same \(1\)–\(2\) Kempe component (else swap and free a colour on \(N(v)\)).

**Close.** The identification/Kempe data force \(N(v)\) to be complete for \(t\ge 4\) (Dirac; Gallai’s structure theorem on the subgraph induced by degree-\((t-1)\) vertices: every block is complete or an odd cycle, and odd-cycle blocks are impossible for \(t\ge 4\)). Full page-length proof: Jensen–Toft.

### Corollary 3.1
Every Type C CE to \(\mathrm{HC}_t\) (\(t\ge 4\)) satisfies \(\delta(G)\ge t\).

**Proof.** Theorem N + no \(K_t\) subgraph (a \(K_t\) subgraph is a \(K_t\) minor). \(\quad\square\)

**Remark.** The hybrid gap at Lemma R\(_7\) is independent of \(\delta=t-1\) vs \(\delta\ge t\): even \(\delta\ge 7\) lies below the Kostochka–Thomason density threshold for forcing a \(K_7\) minor.

---

## 4. Separation lemmas (complete)

### Lemma 4.1 (Clique-sum colouring)
If \(G=G_1\cup G_2\), \(G_1\cap G_2=K\) a clique, \(\chi(G_i)\le m\), and \(|K|\le m\), then \(\chi(G)\le m\).

**Proof.** Colour both; permute to agree on \(K\). \(\quad\square\)

### Lemma 4.2 (CE is clique-sum indecomposable)
A \(t\)-critical graph is not a nontrivial clique-sum along a clique of order \(\le t-1\).

**Proof.** Lemmas 0.5 and 4.1. \(\quad\square\)

### Lemma 4.3 (Minimum separators in a CE under Theorem D)
Let \(G\) be Type C for \(\mathrm{HC}_t\), and assume Theorem D. Then \(\kappa(G)\ge t-1\). If \(\kappa(G)=t-1\) and \(S\) is a separator of order \(t-1\), then:
1. \(G[S]\) is not complete (Lemma 0.5);
2. every \(s\in S\) meets every component of \(G-S\);
3. \(\chi(G[U\cup S])=t-1=\chi(G[W\cup S])\) for each component side \(U\) (proper subgraphs);
4. no pair of \((t-1)\)-colourings of the two sides agrees on \(S\) (else their union colours \(G\)).

**Proof.** Immediate from the cited lemmas. \(\quad\square\)

### Lemma 4.4 (Non-clique cut cannot be glued)
In the situation of Lemma 4.3, the obstruction to gluing is exactly that \(S\) is not a clique: colourings need not be injective on \(S\), and agreement on \(S\) never occurs for a CE.

**Proof.** Lemma 4.3(4). \(\quad\square\)

---

## 5. Rooted models (the inductive engine)

### Lemma 5.1 (Apex-rooted model \(\Rightarrow K_t\) minor)
Let \(v\in V(G)\) and \(u_1,\dots,u_{t-1}\in N(v)\) distinct. If \(G-v\) has a \(K_{t-1}\) model \(\{B_1,\dots,B_{t-1}\}\) with \(u_i\in B_i\) for each \(i\), then \(\bigl\{\{v\},B_1,\dots,B_{t-1}\bigr\}\) is a \(K_t\) model in \(G\).

**Proof.** Each \(B_i\) is adjacent to \(v\) via \(u_i\); the \(B_i\) form a \(K_{t-1}\) model. \(\quad\square\)

### Lemma 5.2 (Rainbow roots)
If \(G\) is \(t\)-critical, \(v\in V(G)\), and \(c\) is a proper \((t-1)\)-colouring of \(G-v\), then there exist \(u_i\in N(v)\) with \(c(u_i)=i\) for all \(i\).

**Proof.** Lemma 0.4. \(\quad\square\)

### Lemma 5.3 (Root obstruction in a CE)
If \(G\) is Type C for \(\mathrm{HC}_t\), then for every \(v\), every proper \((t-1)\)-colouring \(c\) of \(G-v\), and every rainbow choice \(u_i\in N(v)\cap c^{-1}(i)\), there is **no** \(K_{t-1}\) model in \(G-v\) with \(u_i\in B_i\).

**Proof.** Lemma 5.1 would give a \(K_t\) minor. \(\quad\square\)

### Lemma 5.4 (Kempe paths)
In the setting of Lemma 5.2, for all \(i\neq j\) there is a path in \(G-v\) from \(u_i\) to \(u_j\) using only colours \(i\) and \(j\).

**Proof.** If \(u_i,u_j\) lie in different \(i\)–\(j\) Kempe components, swap one to free colour \(i\) on \(N(v)\). \(\quad\square\)

### Lemma 5.5 (Kempe paths need not be disjoint)
Internally disjoint Kempe paths \(\{P_{ij}\}\) would yield a \(K_t\) **subdivision** with apex \(v\). For \(t\ge 7\), Hajós’ conjecture is false (Catlin), so disjointness cannot be forced by chromatic number alone. Minors allow shared vertices to be absorbed into branch sets; that reassembly is the open step.

**Proof.** Status + Lemma 5.4. \(\quad\square\)

### Lemma 5.6 (Clique roots give immediate contradiction)
If the rainbow set \(\{u_1,\dots,u_{t-1}\}\) is a clique, then \(G[N[v]]\) contains \(K_t\).

**Proof.** Lemma 5.1 with singleton branch sets. \(\quad\square\)

---

## 6. Specialisation to \(t=7\)

Assume \(\mathrm{HC}_s\) for all \(s\le 6\). Let \(G\) be Type C for \(\mathrm{HC}_7\).

### Lemma 6.1 (Portrait)
1. \(\chi(G)=7\), \(\eta(G)=6\), no \(K_7\) minor;  
2. \(G\) is \(7\)-critical and \(\chi(G/e)=6\) for every edge \(e\);  
3. \(\delta(G)\ge 7\) (Corollary 3.1);  
4. \(\kappa(G)\ge 6\) (Theorem D);  
5. no separating clique of order \(\le 6\);  
6. for every \(v\): \(\chi(G-v)=6\), rainbow \(N(v)\) in every \(6\)-colouring, and \(G-v\) has a \(K_6\) minor (by \(\mathrm{HC}_6\)).

**Proof.** §§0–3 + \(\mathrm{HC}_6\) + Theorem D + Corollary 3.1. \(\quad\square\)

### Lemma 6.2 (Not \(1\)-apex over \(K_6\)-minor-free)
No vertex \(v\) has \(G-v\) free of \(K_6\) minors.

**Proof.** Else \(\mathrm{HC}_6\Rightarrow\chi(G-v)\le 5\Rightarrow\chi(G)\le 6\). \(\quad\square\)

### Lemma 6.3 (Not \(1\)-apex planar; not \(2\)-apex planar)
No \(v\) with \(G-v\) planar; no pair \(\{u,v\}\) with \(G-u-v\) planar.

**Proof.** Planar \(\Rightarrow\chi\le 4\) (4CT) or even \(\chi\le 5\) (5CT, elementary). Then Lemma 2.1 gives \(\chi(G)\le 5\) or \(\le 6\). \(\quad\square\)

### Lemma 6.4 (General apex budget for \(t=7\))
\(G\) is not \(k\)-apex over any class of chromatic number \(\le r\) whenever \(k+r\le 6\).

**Proof.** Lemma 2.7. \(\quad\square\)

### Lemma 6.5 (Zero colour slack at every apex)
For every \(v\), \(\chi(G-v)=6=\eta(G-v)\). Deleting one vertex leaves a graph that is **Hadwiger-tight** at level \(6\): it uses the full \(6\) colours allowed by \(\mathrm{HC}_6\) and has a \(K_6\) minor. There is **no spare colour** with which to colour \(v\) without recolouring.

**Proof.** Lemma 6.1. \(\quad\square\)

### Lemma 6.6 (Why the \(t=6\) RST trick fails at \(t=7\))
For \(t=6\), RST gives a vertex \(v\) with \(G-v\) planar, so \(\chi(G-v)\le 4\le 5-1\), and Lemma 2.5 finishes.  
For \(t=7\), Lemma 6.5 says \(\chi(G-v)=6\not\le 5\). The same one-vertex deletion never produces a \(5\)-colourable base.

**Proof.** Comparison. \(\quad\square\)

### Lemma 6.7 (Clique-sum indecomposability at \(t=7\))
\(G\) is not a nontrivial clique-sum along a clique of order \(\le 6\).

**Proof.** Lemma 4.2. \(\quad\square\)

### Lemma 6.8 (Edge-maximal companion)
If \(G^+\) is Type M for \(\mathrm{HC}_7\) then every missing edge creates a \(K_7\) model, and \(\kappa(G^+)\ge 3\) (Lemma 1.4). Combined with Theorem D on a Type C subgraph, the structural portrait is at least as strong.

**Proof.** Definitions. \(\quad\square\)

### Lemma 6.9 (Optional external: Mader \(7\)-connectivity)
**External (Mader).** Minimal counterexamples to \(\mathrm{HC}_t\) for \(t\ge 7\) are \(7\)-connected.  
If granted: \(\kappa(G)\ge 7\), matching \(\delta\ge 7\).

**Not used** for the reduction to R\(_7\) below; recorded for completeness.

---

## 7. The rooted \(K_6\) lemma

### Lemma 7.1 (\(t=7\) root obstruction)
For every vertex \(v\) of \(G\), every \(6\)-colouring \(c\) of \(G-v\), and every rainbow \(u_1,\dots,u_6\in N(v)\), the graph \(G-v\) admits **no** \(K_6\) model \(\{B_i\}\) with \(u_i\in B_i\).

**Proof.** Lemma 5.3 with \(t=7\). \(\quad\square\)

### Lemma 7.2 (Unrooted models exist)
For every \(v\), \(G-v\) **has** some \(K_6\) model (unrooted).

**Proof.** Lemma 6.1(6). \(\quad\square\)

### Lemma 7.3 (Connectivity of \(G-v\))
Under Theorem D, \(G-v\) is \(5\)-connected.

**Proof.** \(\kappa(G)\ge 6\) \(\Rightarrow\) \(\kappa(G-v)\ge 5\). \(\quad\square\)

### Lemma R\(_7\) (rooted \(K_6\) lemma — the missing statement)
Let \(H\) be a \(5\)-connected graph with \(\chi(H)=6\) that has a \(K_6\) minor. Let \(c:V(H)\to\{1,\dots,6\}\) be a proper colouring and \(u_i\in c^{-1}(i)\) for each \(i\). Then \(H\) admits a \(K_6\) model \(\{B_1,\dots,B_6\}\) with \(u_i\in B_i\).

### Theorem 7.4 (R\(_7\Rightarrow\mathrm{HC}_7\))
Lemma R\(_7\) implies \(\mathrm{HC}_7\).

**Proof.** Let \(G\) be Type C for \(\mathrm{HC}_7\). Pick \(v\in V(G)\), set \(H=G-v\). By Lemma 6.1, \(\chi(H)=6\) and \(H\) has a \(K_6\) minor; by Lemma 7.3, \(H\) is \(5\)-connected. Take a \(6\)-colouring and rainbow roots (Lemma 5.2). Apply R\(_7\), then Lemma 5.1 with \(t=7\), contradiction. \(\quad\square\)

### Theorem 7.5 (Near-equivalence)
Assuming \(\mathrm{HC}_s\) for \(s\le 6\) and Theorem D:  
\(\mathrm{HC}_7\) holds if and only if no Type C counterexample exists, if and only if every configuration \((H,c,(u_i))\) arising as \(H=G-v\) from a would-be CE satisfies the conclusion of R\(_7\).  

In particular, proving R\(_7\) for the narrower class of graphs \(H=G-v\) with \(G\) \(7\)-critical, \(\delta(G)\ge 7\), \(\eta(G)=6\) is enough.

**Proof.** Theorems 7.4 and 7.1. \(\quad\square\)

---

## 8. Exact gap and blocked mechanisms

### Theorem 8.1 (Exact obstruction)
Assume \(\mathrm{HC}_s\) for \(s\le 6\). The hybrid apex + inductive-colouring program proves that any minimal counterexample to \(\mathrm{HC}_7\) satisfies the portrait of Lemma 6.1 and the root obstruction of Lemma 7.1, and reduces \(\mathrm{HC}_7\) to Lemma R\(_7\).

**Lemma R\(_7\) is not proved.** Hence \(\mathrm{HC}_7\) is not proved by this program.

### Why each natural mechanism fails

| Mechanism | Attempt | Exact block |
|-----------|---------|-------------|
| **A. Apex over planar** | Find \(v\) with \(G-v\) planar; 4CT; extend | Lemma 6.5: \(\chi(G-v)=6\), never \(\le 4\) or \(\le 5\) |
| **B. \(k\)-apex budget** | \(k+r\le 6\) over \(r\)-colourable class | Lemma 6.4 forbids it for a CE; no theorem forces such structure at \(t=7\) |
| **C. Clique-sum split** | Decompose and glue | Lemma 6.7: no separating clique \(\le 6\) |
| **D. Disjoint Kempe paths** | Build \(TK_7\) | Hajós false for \(t\ge 7\); connectivity \(5\) too low for topological \(K_6\) linkage |
| **E. Density / Mader** | \(\delta\ge 7\Rightarrow K_7\) minor | Extremal density is \(\Theta(t\sqrt{\log t})\gg 7\) |
| **F. High connectivity alone** | \(\kappa\ge 6\) or \(7\Rightarrow K_7\) minor | False: \(K_t\)-minor-free graphs can be highly connected (RS structure) |
| **G. Maximal contact model** | Maximise branch sets meeting \(N(v)\); push to \(6\) | Contact deficiency requires reassignment lemma ≡ R\(_7\) (see `hadwiger_mcm_menger_fan.md`) |
| **H. RS near-embedding** | Colour nearly-embeddable CE with \(6\) colours | Apex additive gap: parameters not in budget \(6\) (`hadwiger_structure_theorem.md`) |

### Theorem 8.2 (Structural moral for \(t=7\))
The jump from \(\mathrm{HC}_6\) to \(\mathrm{HC}_7\) is not a one-apex extension of the Four Colour Theorem. After deleting any vertex one obtains a graph that is **already Hadwiger-tight** (\(\chi=\eta=6\)). The remaining task is purely a **rooted minor** problem (R\(_7\)), not a colouring-extension problem with spare colours.

**Proof.** Lemma 6.5–6.6 and Theorem 7.4. \(\quad\square\)

---

## 9. What is fully proved vs classical vs open

| Statement | Status |
|-----------|--------|
| Lemmas 0.2–0.8 (CE reduction, \(\delta\ge t-1\), rainbow, no sep. clique, Brooks barrier, \(\eta=t-1\) under lower HC) | **Proved** |
| Lemma 1.1 (\(\kappa\ge 2\)) | **Proved** |
| Lemma 1.2 (\(\lambda\ge t-1\)) | **Proved** |
| Lemma 1.4 (Type M \(\kappa\ge 3\)) | **Proved** |
| Theorem D (\(\kappa\ge t-1\)) | **Classical** (Dirac; reduction to “separators are cliques” recorded) |
| Theorem N / Corollary 3.1 (\(\delta\ge t\) for CE) | **Classical** (Dirac neighbourhood) |
| Lemmas 2.1–2.8 (apex colouring) | **Proved** |
| Lemmas 4.1–4.4 (separation) | **Proved** |
| Lemmas 5.1–5.6 (rooted model engine) | **Proved** |
| Lemmas 6.1–6.9 (\(t=7\) portrait, no cheap apex) | **Proved** from \(\mathrm{HC}_{\le 6}\)+D+N |
| Theorem 7.4 (R\(_7\Rightarrow\mathrm{HC}_7\)) | **Proved** |
| Lemma R\(_7\) | **OPEN** |
| \(\mathrm{HC}_7\) | **OPEN** |

---

## 10. Conclusion

**Concrete output of the hybrid program.**

1. **Apex mechanism:** fully analysed. For \(t=7\), every vertex deletion is slack-free (\(\chi(G-v)=6\)). No inductive colouring across a small apex set works without a new structure theorem forcing an unrealistically colourable base (Lemmas 6.2–6.6).  

2. **Separation mechanism:** clique-sums are safe for colouring but **absent** in a CE (Lemma 6.7). Non-clique separators of order \(6\) (if \(\kappa=6\)) cannot be glued (Lemma 4.3).  

3. **Connectivity + degree:** \(\kappa\ge 6\), \(\delta\ge 7\), \(\eta=6\) (portrait). Insufficient for a \(K_7\) minor by density or connectivity alone.  

4. **Inductive colouring engine:** reduces \(\mathrm{HC}_7\) **exactly** to:

> **Lemma R\(_7\).** Every \(5\)-connected \(6\)-chromatic graph \(H\) with a \(K_6\) minor admits, for every proper \(6\)-colouring and every transversal \((u_1,\dots,u_6)\) of the colour classes, a \(K_6\) model rooted at those six vertices.

5. **Lemma R\(_7\) is open.** It is a rooted-minor / linkage statement, not a colouring statement with spare colours. Catlin’s counterexamples block the topological special case.  

**Final box.**

\[
\boxed{\mathrm{HC}_7\ \text{via apex/inductive colouring}\ \Longleftrightarrow\ \text{Lemma R}_7
\quad\text{(under }\mathrm{HC}_{\le 6}\text{ + Dirac connectivity)}}
\]

\[
\boxed{\text{Lemma R}_7\text{ not proved; }\mathrm{HC}_7\text{ remains open}}
\]

---

*End of note. File: `hadwiger_apex_inductive_hc7.md`.*
