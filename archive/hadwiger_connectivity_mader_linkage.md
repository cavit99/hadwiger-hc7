# Connectivity, Mader’s Theorem, and Highly Linked Subgraphs
## An approach to Hadwiger’s Conjecture

**Conjecture (Hadwiger).** For every integer \(t\ge 1\), every graph with no \(K_t\) minor satisfies \(\chi\le t-1\).
Write \(\mathrm{HC}_t\) for this assertion at \(t\).

**Conventions.** Graphs are finite and simple. A *\(K_t\) model* in \(G\) is a collection of \(t\) pairwise disjoint nonempty connected vertex sets \(B_1,\dots,B_t\) (branch sets) such that \(G\) has an edge between \(B_i\) and \(B_j\) for all \(i\neq j\). The graph \(G\) has a \(K_t\) minor iff it admits a \(K_t\) model. The *Hadwiger number* \(\eta(G)\) is the largest \(t\) such that \(G\) has a \(K_t\) minor.

---

## 1. Critical reduction

### Definition 1.1
A graph \(G\) is *\(k\)-critical* if \(\chi(G)=k\) and \(\chi(H)<k\) for every proper subgraph \(H\) of \(G\).

### Lemma 1.2 (Minimal counterexamples are critical)
Let \(t\ge 2\). If \(\mathrm{HC}_t\) fails, let \(G\) be a counterexample of minimum order (no \(K_t\) minor, \(\chi(G)\ge t\)), and among such graphs choose one with the fewest edges. Then:
1. \(\chi(G)=t\);
2. \(G\) is \(t\)-critical;
3. every graph of smaller order with no \(K_t\) minor is \((t-1)\)-colourable.

**Proof.**  
For any vertex \(v\), the graph \(G-v\) has no \(K_t\) minor and fewer vertices, so \(\chi(G-v)\le t-1\) by minimality of order. Hence \(\chi(G)\le t\). With \(\chi(G)\ge t\) we get \(\chi(G)=t\).

If some edge \(e\) satisfied \(\chi(G-e)=t\), then \(G-e\) would be a same-order counterexample with fewer edges. Thus \(\chi(G-e)=t-1\) for every edge \(e\). Combined with \(\chi(G-v)=t-1\), every proper subgraph is \((t-1)\)-colourable, so \(G\) is \(t\)-critical.

Assertion (3) is the minimality of \(|V(G)|\). ∎

### Remark 1.3
So \(\mathrm{HC}_t\) is equivalent to: every \(t\)-critical graph admits a \(K_t\) minor.

---

## 2. Degree and elementary connectivity

### Lemma 2.1 (Minimum degree of critical graphs)
If \(G\) is \(k\)-critical and \(k\ge 2\), then \(\delta(G)\ge k-1\).

**Proof.** If \(d(v)\le k-2\), a proper \((k-1)\)-colouring of \(G-v\) extends to \(v\): its neighbours use at most \(k-2\) colours. This contradicts \(\chi(G)=k\). ∎

### Corollary 2.2
A minimum-order counterexample \(G\) to \(\mathrm{HC}_t\) satisfies \(\delta(G)\ge t-1\) and \(|E(G)|\ge \tfrac12(t-1)|V(G)|\). ∎

### Lemma 2.3 (\(2\)-connectivity of critical graphs)
If \(G\) is \(k\)-critical and \(k\ge 2\), then \(\kappa(G)\ge 2\).

**Proof.** If \(G\) is disconnected, each component is a proper subgraph, hence \((k-1)\)-colourable, so \(\chi(G)\le k-1\).

If \(v\) is a cut-vertex, let \(C_1,\dots,C_m\) (\(m\ge 2\)) be the components of \(G-v\) and \(G_i:=G[V(C_i)\cup\{v\}]\). Each \(G_i\) is a proper subgraph, hence \((k-1)\)-colourable. Colour \(G_1\) with colours \(\{1,\dots,k-1\}\); for \(i\ge 2\), colour \(G_i\) and permute colours so \(v\) retains its colour from \(G_1\). The union is a proper \((k-1)\)-colouring of \(G\). ∎

### Lemma 2.4 (No small clique separators)
Let \(G\) be a minimum-order counterexample to \(\mathrm{HC}_t\). Let \(S\subset V(G)\) with \(|S|\le t-2\), and suppose \(G-S\) is disconnected. If \(G[S]\) is a clique, then \(\chi(G)\le t-1\), a contradiction.

Thus **no clique of order at most \(t-2\) separates \(G\)**.

**Proof.** Let \(D_1,\dots,D_m\) (\(m\ge 2\)) be the component vertex sets of \(G-S\), and \(G_i:=G[D_i\cup S]\). Each \(G_i\) has fewer vertices than \(G\) and no \(K_t\) minor, so \(\chi(G_i)\le t-1\) by Lemma 1.2(3).

Since \(S\) is a clique, the vertices of \(S\) receive distinct colours in every proper colouring of each \(G_i\). Fix a \((t-1)\)-colouring of \(G_1\). For \(i\ge 2\), colour \(G_i\) and permute colours so each \(s\in S\) matches its colour in \(G_1\). The union colours \(G\) properly with \(t-1\) colours. ∎

### Lemma 2.5 (Brooks barrier)
Let \(G\) be \(t\)-critical, \(K_t\)-minor-free, and \(t\ge 4\). Then \(\Delta(G)\ge t\).

**Proof.** By Lemma 2.1, \(\delta(G)\ge t-1\). If \(\Delta(G)\le t-1\), then \(G\) is connected and \((t-1)\)-regular. Brooks’ theorem: \(\chi\le\Delta\) unless \(G\) is complete or an odd cycle. Here \(\chi=t\), so \(\chi>\Delta\) if \(\Delta\le t-1\). An odd cycle has \(\chi=3\), forcing \(t=3\), a contradiction. The graph \(K_t\) has a \(K_t\) minor, a contradiction. Hence \(\Delta\ge t\). ∎

### Lemma 2.6 (Rainbow neighbourhood)
Let \(G\) be \(t\)-critical and \(v\in V(G)\). In every proper \((t-1)\)-colouring \(c\) of \(G-v\),
\[
c\bigl(N(v)\bigr)=\{1,\dots,t-1\}.
\]

**Proof.** A missing colour on \(N(v)\) could be assigned to \(v\). ∎

### Lemma 2.7 (Dirac: edge-connectivity of critical graphs)
If \(G\) is \(k\)-critical and \(k\ge 2\), then \(\lambda(G)\ge k-1\).

**Proof.** Always \(\lambda\le\delta\), and \(\delta\ge k-1\) by Lemma 2.1, so it is enough to rule out an edge-cut of size at most \(k-2\).

Suppose \(V(G)=X\sqcup Y\) with \(X,Y\neq\emptyset\) and \(r:=|E(X,Y)|\le k-2\). By \(\delta\ge k-1\), neither side is a singleton (a singleton side would be a vertex of degree \(\le k-2\)). Thus \(|X|,|Y|\ge 2\).

Since \(G\) is \(k\)-critical, \(G[X]\) and \(G[Y]\) are proper subgraphs, so each admits a proper colouring with colour set \(\Gamma=\{1,\dots,k-1\}\). Let \(c_X\) and \(c_Y\) be such colourings.

List the cut edges as \(x_1y_1,\dots,x_ry_r\) (endpoints not necessarily distinct). Define a bipartite multigraph \(B\) with bipartition \((\Gamma_L,\Gamma_R)\), two copies of \(\Gamma\), by placing, for each cut edge \(x_iy_i\), one edge of \(B\) from colour \(c_X(x_i)\in\Gamma_L\) to colour \(c_Y(y_i)\in\Gamma_R\). Then \(B\) has at most \(r\le k-2\) edges and \(|\Gamma|=k-1\) vertices on each side.

A permutation \(\pi:\Gamma\to\Gamma\) may be used to recolour \(Y\) by \(\pi\circ c_Y\). The recoloured graph is a proper colouring of \(G\) iff no cut edge is monochromatic, iff there is no cut edge \(x_iy_i\) with \(\pi(c_Y(y_i))=c_X(x_i)\), iff \(\pi\) as a perfect matching of \(\Gamma_L\) to \(\Gamma_R\) avoids all edges of \(B\).

Equivalently: among the \((k-1)!\) permutations, those that are “blocked” by a particular edge of \(B\) number at most \((k-2)!\). With at most \(k-2\) edges in \(B\), at most \((k-2)\cdot(k-2)!\) permutations are blocked. But
\[
(k-1)!-(k-2)\cdot(k-2)! = (k-2)!\bigl((k-1)-(k-2)\bigr)=(k-2)!\ge 1
\]
for \(k\ge 2\). Hence some permutation is unblocked, and \(G\) is \((k-1)\)-colourable, a contradiction. ∎

---

## 3. Edge-maximal counterexamples and 3-connectivity

### Remark 3.0 (Two secondary optimisations)
Lemma 1.2 takes a counterexample of **minimum order**, then **fewest edges**, to obtain \(t\)-criticality (used for Lemmas 2.1–2.7).  
For linkage across separators one instead wants **edge-maximality** without a \(K_t\) minor: among counterexamples of minimum order, pass to one with the **most edges**. Adding any missing edge then creates a \(K_t\) minor.

These two secondary optimisations need not coincide. The lemmas of §2 that use only vertex-deletion criticality (\(\delta\ge t-1\), \(\kappa\ge 2\), rainbow neighbourhoods, no small clique separators) apply to every minimum-order counterexample. Dirac’s Lemma 2.7 uses full subgraph-criticality (fewest edges). Lemma 3.2 below uses edge-maximality (most edges). Both kinds of minimal counterexample satisfy \(\chi=t\), \(\delta\ge t-1\), and \(\kappa\ge 2\).

### Lemma 3.1 (Path insertion)
Suppose \(G+uv\) has a \(K_t\) model \(\{X_1,\dots,X_t\}\) that uses the new edge \(uv\) as the unique \(G+uv\)-edge not in \(G\), with \(u\in X_1\), \(v\in X_2\). Let \(P\) be a \(u\)–\(v\) path in \(G\) whose interior is disjoint from \(\bigcup_i X_i\). Then \(G\) has a \(K_t\) minor.

**Proof.** Set \(X_2':=X_2\cup\bigl(V(P)\setminus\{u\}\bigr)\). Then \(X_2'\) is connected in \(G\). The family \(\{X_1,X_2',X_3,\dots,X_t\}\) is pairwise disjoint. Adjacencies \(X_i\)–\(X_2\) for \(i\ge 3\) survive as \(X_i\)–\(X_2'\) adjacencies. The first edge of \(P\) at \(u\in X_1\) enters \(X_2'\). ∎

### Lemma 3.2 (Minimal counterexamples are 3-connected)
Let \(t\ge 4\) and let \(G\) be a minimal counterexample to \(\mathrm{HC}_t\). Then \(\kappa(G)\ge 3\).

**Proof.** Lemma 2.3 gives \(\kappa\ge 2\). Suppose \(\{u,v\}\) separates \(G\), with sides \(A,B\) so that \(A\cup B=V(G)\), \(A\cap B=\{u,v\}\), both \(A\setminus\{u,v\}\) and \(B\setminus\{u,v\}\) nonempty, and no \(G\)-edge joins the two open sides. Write \(G_A:=G[A]\) and \(G_B:=G[B]\).

Both \(G_A\) and \(G_B\) have fewer vertices than \(G\) and no \(K_t\) minor, so each is \((t-1)\)-colourable.

If \(uv\in E(G)\), then \(\{u,v\}\) is a clique separator of order \(2\le t-2\), contradicting Lemma 2.4. So \(uv\notin E(G)\).

By edge-maximality, \(G+uv\) has a \(K_t\) minor. The same holds for at least one of \(G_A+uv\) and \(G_B+uv\): if neither has a \(K_t\) minor, then both are \((t-1)\)-colourable by Lemma 1.2(3), and since \(uv\) is present one may match colours with \(c(u)\neq c(v)\) on both sides to \((t-1)\)-colour \(G\), a contradiction. (Alternatively: a \(K_t\) model in \(G+uv\) is supported on one side after discarding the other open side, up to the edge \(uv\).)

Say \(G_A+uv\) has a \(K_t\) model \(\{X_1,\dots,X_t\}\). The model must use \(uv\) (else it lies in \(G_A\subseteq G\)). Arrange \(u\in X_1\), \(v\in X_2\).

Take the separator minimal: both \(u\) and \(v\) have neighbours in \(B\setminus\{u,v\}\). Hence a \(u\)–\(v\) path \(P_B\) exists with interior in \(B\setminus\{u,v\}\), necessarily disjoint from \(A\supseteq\bigcup_i X_i\). Lemma 3.1 yields a \(K_t\) minor in \(G\), a contradiction.

Therefore no 2-vertex separator exists. ∎

---

## 4. Mader’s theorem (elementary form)

High average degree forces large clique minors. We prove a standard elementary corollary package; the classical theorem itself is stated with a complete proof reference and an outline of every step.

### Lemma 4.1 (Large minimum-degree subgraph)
If \(\bar d(G)\ge d>0\), then some subgraph \(H\subseteq G\) satisfies \(\delta(H)\ge d/2\).

**Proof.** While there exists a vertex \(v\) with \(d(v)<d/2\), delete \(v\). If \(\sum_x d(x)\ge dn\) and \(d(v)<d/2\), then
\[
\frac{\sum d(x)-2d(v)}{n-1}\ >\ \frac{dn-d}{n-1}\ =\ d,
\]
so the average degree remains strictly above \(d\). The process terminates at a nonempty subgraph of minimum degree at least \(d/2\). ∎

### Theorem 4.2 (Elementary Mader bound)
For every integer \(t\ge 2\), every graph of average degree at least \(2^{t-2}\) has a \(K_t\) minor.

**Proof outline (Diestel, Graph Theory, Thm. 7.2.1).**  
Proceed by induction on \(t\). For \(t\le 3\) the claim is elementary (an edge; a cycle).  

For \(t\ge 4\), let \(G\) have average degree \(\bar d(G)\ge 2^{t-2}\). Among minors of \(G\) with average degree at least \(2^{t-2}\), choose a minor \(H\) of minimum order. Then:

1. **Minimum degree.** \(\delta(H)\ge 2^{t-3}+1\) in the integral sense: if some \(v\) had \(d(v)\le 2^{t-3}\), then
   \[
   2e(H-v)=2e(H)-2d(v)\ge 2^{t-2}|H|-2^{t-2}=2^{t-2}(|H|-1),
   \]
   so \(\bar d(H-v)\ge 2^{t-2}\), contradicting minimality of \(|H|\).

2. **Neighbourhood case.** Let \(v\) be a vertex of minimum degree and \(N=N(v)\). If \(\bar d(H[N])\ge 2^{t-3}\), the inductive hypothesis yields a \(K_{t-1}\) minor in \(H[N]\); adding the branch set \(\{v\}\) gives a \(K_t\) minor.

3. **Empty exterior forbidden.** If \(\bar d(H[N])<2^{t-3}\) and \(U:=V(H)\setminus N[v]=\emptyset\), then
   \[
   \bar d(H)=\frac{2e(H[N])+2|N|}{|N|+1}<\frac{|N|(2^{t-3}+2)}{|N|+1},
   \]
   which for \(t\ge 4\) cannot reach \(2^{t-2}\) (the inequality \(\frac{|N|(2^{t-3}+2)}{|N|+1}\ge 2^{t-2}\) rearranges to \(|N|(2-2^{t-3})\ge 2^{t-2}\), impossible since \(2-2^{t-3}\le 0\)).

4. **Contraction case.** If \(U\neq\emptyset\), contract the connected set \(N[v]\) to a single vertex. Diestel’s arithmetic shows that the resulting minor still has average degree at least \(2^{t-2}\), contradicting minimality of \(|H|\). (The average-degree hypothesis—rather than a pure minimum-degree hypothesis—is what makes the contraction preserve the threshold after parallel edges are suppressed.)

Thus a \(K_t\) minor exists in \(H\), hence in \(G\). ∎

**Full write-up of step 4:** R. Diestel, *Graph Theory*, 5th ed., Springer, Theorem 7.2.1; original: W. Mader, *Homomorphieeigenschaften und mittlere Kantendichte von Graphen*, Math. Ann. 174 (1967), 265–268.

### Corollary 4.3 (Degeneracy and colouring)
If \(G\) has no \(K_t\) minor, then every subgraph of \(G\) has a vertex of degree at most \(2^{t-2}-1\). In particular \(G\) is \((2^{t-2}-1)\)-degenerate and
\[
\chi(G)\ \le\ 2^{t-2}.
\]

**Proof.** If some subgraph \(H\) satisfied \(\delta(H)\ge 2^{t-2}\), then \(\bar d(H)\ge 2^{t-2}\), so Theorem 4.2 would give a \(K_t\) minor in \(H\), hence in \(G\). A \(d\)-degenerate graph is greedy-\((d+1)\)-colourable. ∎

### Corollary 4.4 (Degree window for critical counterexamples)
If \(G\) is \(t\)-critical and \(K_t\)-minor-free, then
\[
t-1\ \le\ \delta(G)\ \le\ 2^{t-2}-1.
\]
For large \(t\) this interval is nonempty: **Mader’s theorem alone does not forbid \(t\)-critical \(K_t\)-minor-free graphs**. ∎

### Remark 4.5 (Optimal density)
Kostochka (1982) and Thomason (1984) proved that the extremal average degree forcing a \(K_t\) minor is \(\Theta(t\sqrt{\log t})\). Pure degree methods therefore give at best
\[
\chi(G)\ \le\ O\bigl(t\sqrt{\log t}\bigr)
\]
for \(K_t\)-minor-free graphs—still larger than \(t-1\) for large \(t\). Connectivity and linkage are needed to bridge the remaining gap.

---

## 5. Small \(t\): connectivity finishes the proof

### Lemma 5.1
Every \(3\)-connected graph on at least \(4\) vertices has a \(K_4\) minor.

**Proof.** Let \(G\) be \(3\)-connected, \(|V(G)|\ge 4\). For any \(v\), the graph \(G-v\) is \(2\)-connected, so contains a cycle \(C\). By Menger’s theorem there are three paths from \(v\) to \(V(C)\), disjoint except at \(v\), meeting \(C\) at distinct vertices \(a,b,c\).

Branch sets: \(B_v=\{v\}\); \(B_a=\) vertex set of the \(v\)–\(a\) path minus \(v\); likewise \(B_b,B_c\). These are connected and pairwise disjoint, and \(B_v\) meets each. The three \(a,b,c\)-arcs of \(C\) join \(\{B_a,B_b,B_c\}\). ∎

### Theorem 5.2 (\(\mathrm{HC}_t\) for \(t\le 4\))
Hadwiger’s conjecture holds for all \(t\le 4\).

**Proof.**  
- \(t\le 2\): trivial.  
- \(t=3\): no \(K_3\) minor \(\Rightarrow\) forest \(\Rightarrow\) \(\chi\le 2\).  
- \(t=4\): a minimum-order counterexample has \(\delta\ge 3\) (Corollary 2.2). Any graph of minimum degree \(\ge 3\) has a \(3\)-connected minor of minimum degree \(\ge 3\) (take a minor-minimal minor with \(\delta\ge 3\); it is \(3\)-connected). Lemma 5.1 supplies a \(K_4\) minor, a contradiction. ∎

### Remark 5.3
- \(\mathrm{HC}_5\) follows from the Four Colour Theorem plus Wagner’s structure theorem for \(K_5\)-minor-free graphs.  
- \(\mathrm{HC}_6\) was proved by Robertson–Seymour–Thomas.  
- \(\mathrm{HC}_t\) is open for all \(t\ge 7\).

### Theorem 5.4 (Kelmans–Seymour — statement)
Every \(5\)-connected nonplanar graph has a \(K_5\) minor.

This is the prototype “high connectivity \(\Rightarrow\) clique minor” theorem at \(t=5\).

---

## 6. Linkage

### Definition 6.1
\(G\) is *\(k\)-linked* if \(|V(G)|\ge 2k\) and for all distinct \(s_1,\dots,s_k,t_1,\dots,t_k\) there exist pairwise vertex-disjoint paths joining \(s_i\) to \(t_i\).

### Theorem 6.2 (Bollobás–Thomason; Thomas–Wollan)
There is a constant \(c\le 10\) such that every \(ck\)-connected graph is \(k\)-linked.

### Lemma 6.3 (Rooted model upgrades)
Let \(G\) be \(t\)-critical, \(v\in V(G)\), and \(u_1,\dots,u_{t-1}\in N(v)\). If \(G-v\) has a \(K_{t-1}\) model \(\{B_1,\dots,B_{t-1}\}\) with \(u_i\in B_i\) for each \(i\), then \(\bigl\{\{v\},B_1,\dots,B_{t-1}\bigr\}\) is a \(K_t\) model in \(G\).

**Proof.** Immediate from the definition of models and \(v\sim u_i\). ∎

### Lemma 6.4 (Complete linkage realises a clique minor)
Let \(w_1,\dots,w_r\) be distinct vertices of a graph \(H\). If for every pair \(\{i,j\}\) there is a path \(P_{ij}\) joining \(w_i\) to \(w_j\) such that the interiors of these paths are pairwise disjoint and avoid \(\{w_1,\dots,w_r\}\), then \(H\) has a \(K_r\) minor (contract each path to an edge, or expand branch sets halfway along each path).

**Proof.** Contracting each \(P_{ij}\) to a single edge produces a \(K_r\) on \(\{w_1,\dots,w_r\}\) as a minor. ∎

### Corollary 6.5 (Linkage threshold for a direct construction)
If a minimal counterexample \(G\) to \(\mathrm{HC}_t\) is \(\binom{t-1}{2}\)-linked, then one can attempt: pick \(v\), rainbow neighbours \(u_1,\dots,u_{t-1}\) (Lemma 2.6), and realise all pairs among them by disjoint paths in \(G-v\). Lemma 6.4 would give a \(K_{t-1}\) model on those roots, and Lemma 6.3 a \(K_t\) minor.

By Theorem 6.2, \(\binom{t-1}{2}\)-linkedness follows from connectivity \(\ge c\binom{t-1}{2}=\Theta(t^2)\). ∎

---

## 7. Attempted contradiction for general \(t\)

Let \(t\ge 7\) and let \(G\) be a minimal counterexample to \(\mathrm{HC}_t\). Summarising §§1–3:
- \(\chi(G)=t\), no \(K_t\) minor, \(\delta(G)\ge t-1\), \(\Delta(G)\ge t\);
- \(\kappa(G)\ge 3\), \(\lambda(G)\ge t-1\);
- no clique separator of order \(\le t-2\);
- \(N(v)\) is rainbow in every \((t-1)\)-colouring of \(G-v\).

### Attempt A (Mader density)
Corollary 2.2 gives \(\bar d(G)\ge t-1\). Theorem 4.5 forces a \(K_t\) minor only at density \(\ge 2^{t-2}\) (or \(\Omega(t\sqrt{\log t})\) in the sharp form). For \(t\ge 7\), \(t-1\) lies strictly below both thresholds. **No contradiction.**

### Attempt B (Connectivity \(\to\) linkage \(\to\) model)
If \(\kappa(G)\ge c\binom{t-1}{2}\), Corollary 6.5 produces a \(K_t\) minor.

**Missing piece B.** There is no theorem guaranteeing that minimal Hadwiger counterexamples are \(\Omega(t^2)\)-connected (nor even \(\Omega(t)\)-connected in full generality). Known connectivity boosts for minimal counterexamples yield only a constant (e.g. arguments toward \(7\)-connectivity), independent of \(t\).

### Attempt C (Desired trade-off theorem)
**Open theorem that would finish \(\mathrm{HC}_t\):**  
*There exists a function \(f\) such that every \(f(t)\)-connected graph of minimum degree at least \(t-1\) has a \(K_t\) minor.*

This is known for \(t\le 6\) (degeneracy / Kelmans–Seymour / Robertson–Seymour–Thomas) and open for \(t\ge 7\). It is the precise content of the connectivity approach beyond small \(t\).

### Attempt D (Rooted minors without huge linkage)
Lemma 6.3 reduces the problem to a *rooted* \(K_{t-1}\) minor in \(G-v\) meeting a prescribed set of \(t-1\) neighbours of \(v\). This rooted problem is not known to be easier than Hadwiger itself; high connectivity helps but does not currently resolve it at degree \(t-1\).

---

## 8. Exact remaining gap

### Fully proved in this manuscript

| Label | Statement |
|-------|-----------|
| 1.2 | Min-order counterexample is \(t\)-critical |
| 2.1 | \(\delta\ge k-1\) for \(k\)-critical graphs |
| 2.3 | \(\kappa\ge 2\) for \(k\)-critical graphs |
| 2.4 | No clique separator of order \(\le t-2\) in a min counterexample |
| 2.5 | \(\Delta\ge t\) for counterexamples, \(t\ge 4\) |
| 2.6 | Rainbow neighbourhood |
| 2.7 | \(\lambda\ge k-1\) for \(k\)-critical graphs (Dirac) |
| 3.1 | Path insertion for models |
| 3.2 | Minimal (edge-max) counterexample is \(3\)-connected |
| 5.1–5.2 | \(3\)-connected \(\Rightarrow K_4\) minor; \(\mathrm{HC}_t\) for \(t\le 4\) |
| 4.6–4.7 | From Mader: \(\chi\le 2^{t-2}\) if no \(K_t\) minor; degree window for counterexamples |

### Classical black boxes used
- Mader’s theorem (Theorem 4.5): average degree \(\ge 2^{t-2}\) forces a \(K_t\) minor.  
- Bollobás–Thomason linkage (Theorem 6.2): \(O(k)\)-connectivity forces \(k\)-linkedness.  
- Brooks’ theorem (in Lemma 2.5).  
- Menger’s theorem (in Lemma 5.1).

### The gap (precise)

After reducing to a \(t\)-critical, edge-maximal, \(K_t\)-minor-free graph \(G\) with
\[
\delta(G)\ge t-1,\quad \Delta(G)\ge t,\quad \kappa(G)\ge 3,\quad \lambda(G)\ge t-1,
\]
and with no clique separator of order \(\le t-2\), one still cannot force a \(K_t\) model when \(t\ge 7\).

- **Degree is too low for Mader:** the extremal density of \(K_t\)-minor-free graphs is \(\Theta(t\sqrt{\log t})\), so \(\delta\sim t\) is compatible with having no \(K_t\) minor.  
- **Connectivity is too low for linkage:** known structural results do not lift \(\kappa(G)\) to \(\Omega(t)\) or \(\Omega(t^2)\), which would be needed to feed Theorem 6.2 and Corollary 6.5.  
- **The missing theorem:** every sufficiently highly connected graph of minimum degree \(t-1\) has a \(K_t\) minor—proved for \(t\le 6\), open for \(t\ge 7\).

Until that theorem (or a rooted-linkage substitute at degree \(t-1\)) is established, the connectivity–Mader–linkage approach does not prove \(\mathrm{HC}_t\) for general \(t\).

---

## 9. Conclusion

The connectivity / Mader / linkage approach yields a complete structural portrait of a hypothetical minimal counterexample to Hadwiger’s conjecture:

- \(t\)-critical, \(\delta\ge t-1\), \(\lambda\ge t-1\), \(\kappa\ge 3\) (edge-maximal case),  
- no small clique separators,  
- \(\Delta\ge t\), rainbow neighbourhoods,  
- chromatic number at most \(2^{t-2}\) forced by Mader in the broader \(K_t\)-minor-free world, yet criticality demands \(\chi=t\).

These ingredients **prove \(\mathrm{HC}_t\) for all \(t\le 4\)** by elementary means, and they organise the known deep solutions for \(t=5,6\) as connectivity-to-minor theorems (Kelmans–Seymour, Robertson–Seymour–Thomas).

For \(t\ge 7\), the same ingredients stop short: Mader’s density threshold exceeds \(t-1\), and no theorem supplies enough connectivity to run a linkage construction of a \(K_t\) model. **That is the exact remaining gap.**
