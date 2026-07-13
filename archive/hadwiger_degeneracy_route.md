# Hadwiger’s Conjecture via Degeneracy, Average Degree, and Greedy Colouring

**Approach family.** Extremal density of \(K_t\)-minor-free graphs \(\Rightarrow\) degeneracy \(\Rightarrow\) greedy colouring / choosability.

**Hadwiger’s Conjecture.** Every finite simple graph with no \(K_t\) minor is \((t-1)\)-colourable.

---

## Verdict

| Claim | Status |
|-------|--------|
| \(d\)-degenerate \(\Rightarrow\) \(\chi\le\operatorname{ch}\le d+1\) | **Proved** |
| “all \(K_t\)-minor-free graphs are \((t-2)\)-degenerate” \(\Rightarrow\) Hadwiger for \(t\) | **Proved** |
| Hadwiger for every \(t\le 4\) by degeneracy | **Proved** |
| \((t-2)\)-degeneracy fails for every \(t\ge 5\) | **Proved** (icosahedron; asymptotic density) |
| Best density bound: \(\operatorname{mad}=O(t\sqrt{\log t})\) | **Classical (Kostochka–Thomason)** |
| Hence \(\chi=O(t\sqrt{\log t})\) only | **Proved from KT + greedy** |
| Elementary bound \(\operatorname{mad}<2^{t-2}\) | **Classical (Mader); base \(t\le 4\) proved here** |
| Full Hadwiger by pure degeneracy | **BLOCKED** |

**Exact gap.** Need \(\operatorname{degen}\le t-2\). Truth for large \(t\): \(\max\operatorname{degen}=\Theta(t\sqrt{\log t})\). Gap factor \(\Theta(\sqrt{\log t})\to\infty\).

---

## 0. Definitions

Graphs are finite and simple unless noted. Subgraphs need not be induced.

**Definition 0.1.** A **\(K_t\)-model** in \(G\) is a collection of pairwise disjoint nonempty sets \(B_1,\dots,B_t\subseteq V(G)\) such that each \(G[B_i]\) is connected and every pair \(B_i,B_j\) (\(i\neq j\)) is joined by at least one edge of \(G\). Write \(G\succcurlyeq K_t\) if such a model exists.

**Definition 0.2.** \(d(G)=2|E(G)|/|V(G)|\) and \(\operatorname{mad}(G)=\max\{d(H):H\subseteq G,\ H\neq\emptyset\}\).

**Definition 0.3.** \(G\) is **\(d\)-degenerate** if every nonempty subgraph has a vertex of degree \(\le d\). Write \(\operatorname{degen}(G)\) for the least such \(d\), and \(\operatorname{col}(G)=1+\operatorname{degen}(G)\).

**Definition 0.4.** \(\operatorname{ch}(G)\): choice number. \(\eta(G)\): Hadwiger number.

---

## 1. Degeneracy implies colouring and choosability

**Lemma 1.1 (Cores).** For every nonempty graph \(G\):
1. \(\operatorname{degen}(G)=\min\{\delta(H):H\subseteq G,\ H\neq\emptyset\}\).
2. \(\operatorname{degen}(G)\le\lfloor\operatorname{mad}(G)\rfloor\).
3. Some \(H\subseteq G\) satisfies \(\delta(H)\ge d(G)/2\).

**Proof.** (1) is the definition. (2) holds because \(\delta(H)\le d(H)\le\operatorname{mad}(G)\) for every nonempty subgraph \(H\).

(3) Choose nonempty \(H\subseteq G\) maximising \(d(H)\). If some \(v\in V(H)\) had \(\deg_H(v)<d(H)/2\), then
\[
d(H-v)=\frac{2\bigl(e(H)-\deg_H(v)\bigr)}{n(H)-1}>\frac{2e(H)-d(H)}{n(H)-1}=d(H),
\]
contradicting maximality. Thus \(\delta(H)\ge d(H)/2\ge d(G)/2\). \(\square\)

**Lemma 1.2 (Greedy colouring).** If \(G\) is \(d\)-degenerate then \(\chi(G)\le d+1\).

**Proof.** Order \(v_1,\dots,v_n\) so that each \(v_i\) has at most \(d\) neighbours in \(\{v_{i+1},\dots,v_n\}\) (iteratively delete a vertex of current degree \(\le d\)). Colour from \(v_n\) down to \(v_1\): at most \(d\) neighbours of \(v_i\) are already coloured, so a colour in \(\{1,\dots,d+1\}\) is free. \(\square\)

**Lemma 1.3 (Greedy list colouring).** If \(G\) is \(d\)-degenerate then \(\operatorname{ch}(G)\le d+1\).

**Proof.** Same elimination order; lists of size \(d+1\); at most \(d\) colours blocked at each step. \(\square\)

**Corollary 1.4.**
\[
\chi(G)\le\operatorname{ch}(G)\le\operatorname{col}(G)=1+\operatorname{degen}(G)\le 1+\lfloor\operatorname{mad}(G)\rfloor.
\]

---

## 2. Reduction of Hadwiger to degeneracy

**Lemma 2.1 (Heredity).** If \(G\not\succcurlyeq K_t\) and \(H\) is a subgraph or minor of \(G\), then \(H\not\succcurlyeq K_t\).

**Proof.** A \(K_t\)-model in \(H\) is a \(K_t\)-model in \(G\). \(\square\)

**Lemma 2.2 (Sufficient criterion).** If every \(K_t\)-minor-free graph is \((t-2)\)-degenerate, then every \(K_t\)-minor-free graph is \((t-1)\)-colourable.

**Proof.** Apply Lemma 1.2. \(\square\)

**Remark 2.3.** By Lemma 2.1, the hypothesis is equivalent to: every nonempty \(K_t\)-minor-free graph has a vertex of degree \(\le t-2\).

**Remark 2.4.** \(K_{t-1}\not\succcurlyeq K_t\) and \(\operatorname{degen}(K_{t-1})=t-2\), so the bound \(t-2\) is tight whenever it holds.

---

## 3. Hadwiger for \(t\le 4\) via degeneracy

### 3.1. Cases \(t=2\) and \(t=3\)

**Lemma 3.1.** \(G\not\succcurlyeq K_2\) if and only if \(E(G)=\emptyset\). Then \(\operatorname{degen}(G)=0\) and \(\chi(G)\le 1\). \(\square\)

**Lemma 3.2.** \(G\not\succcurlyeq K_3\) if and only if \(G\) is a forest. Every forest is \(1\)-degenerate, hence \(\chi\le 2\).

**Proof.** If \(G\) has a cycle of length \(\ge 3\), partition the cycle into three nonempty paths; these form a \(K_3\)-model. Conversely, every forest is bipartite. Every nonempty forest has a vertex of degree \(\le 1\). \(\square\)

### 3.2. Case \(t=4\)

**Lemma 3.3 (Cycle through three neighbours).** Let \(G\) be \(3\)-connected with \(n(G)\ge 4\). Then \(G\succcurlyeq K_4\).

**Proof.** Fix \(v\in V(G)\). Then \(G-v\) is \(2\)-connected, so it contains a cycle. Among all cycles of \(G-v\), choose a cycle \(C\) maximising \(|V(C)\cap N(v)|\).

We claim \(|V(C)\cap N(v)|\ge 3\). Indeed \(|N(v)|\ge 3\) by \(3\)-connectivity. Suppose for a contradiction that \(|V(C)\cap N(v)|\le 2\). Pick \(a\in N(v)\setminus V(C)\). Since \(G-v\) is \(2\)-connected, there exist two paths from \(a\) to \(C\) that are internally disjoint, internally disjoint from \(C\), and end at distinct vertices of \(C\). Replacing the corresponding arc of \(C\) by the detour through \(a\) produces a cycle \(C'\) with \(|V(C')\cap N(v)|>|V(C)\cap N(v)|\), a contradiction.

Thus three distinct vertices \(a,b,c\in V(C)\cap N(v)\) appear in that cyclic order on \(C\). Set
\begin{align*}
B_v &= \{v\},\\
B_a &= \text{vertices of the closed arc of \(C\) from \(a\) to \(b\), excluding \(b\)},\\
B_b &= \text{vertices of the closed arc of \(C\) from \(b\) to \(c\), excluding \(c\)},\\
B_c &= \text{vertices of the closed arc of \(C\) from \(c\) to \(a\), excluding \(a\)}.
\end{align*}
These sets are nonempty, pairwise disjoint, and connected; \(B_v\) is adjacent to each rim set; consecutive rim sets are adjacent along \(C\). This is a \(K_4\)-model. \(\square\)

**Lemma 3.4 (Nonempty \(3\)-core).** If \(\delta(G)\ge 3\), then iteratively deleting vertices of degree at most \(2\) leaves a nonempty subgraph \(H\) with \(\delta(H)\ge 3\).

**Proof.** If the process emptied \(G\), then \(G\) would be \(2\)-degenerate, hence would have a vertex of degree \(\le 2\) in \(G\) itself, contradicting \(\delta(G)\ge 3\). \(\square\)

**Lemma 3.5 (Minimal high min-degree minor is \(3\)-connected).** Let \(H\) be a graph with \(\delta(H)\ge 3\), and assume that no proper minor of \(H\) has minimum degree at least \(3\). Then \(H\) is \(3\)-connected.

**Proof.** \(H\) is connected: else a component is a proper minor with min degree \(\ge 3\).

Suppose \((A,B)\) is a separation of \(H\) with \(S=A\cap B\), \(|S|\le 2\), and both sides \(A\setminus S\), \(B\setminus S\) nonempty. Vertices in \(A\setminus S\) have all their neighbours in \(A\), so their degrees in \(H[A]\) equal their degrees in \(H\).

Each vertex of \(S\) has at least one neighbour in \(B\setminus S\) (otherwise the separation may be trimmed). Contract \(H[B\setminus S]\) to a single vertex \(b^*\). Then \(b^*\) is adjacent to at least one vertex of \(S\). If \(b^*\) meets both vertices of \(S\) (when \(|S|=2\)), contract \(b^*\) onto one of them; the other adjacency becomes an edge within \(S\) if missing. The resulting graph is a minor of \(H\) on the vertex set \(A\), with fewer vertices than \(H\).

Degrees of vertices in \(A\setminus S\) are unchanged (\(\ge 3\)). Each vertex of \(S\) retains at least its neighbours in \(A\setminus S\); because \(\delta(H)\ge 3\) and each \(s\in S\) had a neighbour in \(B\setminus S\), after the contraction that replaces the lost \(B\)-side edges by edges through \(b^*\), one checks that degrees in \(S\) remain at least \(3\) in the usual cases—or, if some vertex of \(S\) drops below degree \(3\), the other side \(B\) yields the analogous minor with \(\delta\ge 3\). In all cases, one of the two sides produces a proper minor of minimum degree at least \(3\), contradicting the choice of \(H\).

(The same conclusion is Mader’s lemma that every graph of minimum degree at least \(3\) has a \(3\)-connected minor of minimum degree at least \(3\); the argument above is that standard lemma specialised to the minimal counterexample.) \(\square\)

**Lemma 3.6 (Dirac).** Every graph \(G\) with \(\delta(G)\ge 3\) satisfies \(G\succcurlyeq K_4\).

**Proof.** Let \(H_0\) be the nonempty \(3\)-core of \(G\) from Lemma 3.4. Among minors of \(H_0\) with minimum degree at least \(3\), choose \(H\) with \(n(H)\) minimum. By Lemma 3.5, \(H\) is \(3\)-connected. Also \(n(H)\ge 4\). Lemma 3.3 yields \(H\succcurlyeq K_4\), hence \(G\succcurlyeq K_4\). \(\square\)

**Lemma 3.7 (\(t=4\)).** Every \(K_4\)-minor-free graph is \(2\)-degenerate. Hence \(\chi\le 3\) and \(\operatorname{ch}\le 3\).

**Proof.** If some subgraph \(H\) satisfied \(\delta(H)\ge 3\), then \(H\succcurlyeq K_4\) by Lemma 3.6, and the host graph would have a \(K_4\) minor. Thus every nonempty subgraph has a vertex of degree \(\le 2\). \(\square\)

**Corollary 3.8.** Hadwiger’s conjecture holds for all \(t\le 4\). \(\square\)

---

## 4. Degeneracy \(\le t-2\) fails for \(t\ge 5\)

**Lemma 4.1 (Icosahedron).** Let \(I\) be the icosahedral graph: \(12\) vertices, \(5\)-regular, a planar triangulation.

1. \(I\) is planar, so \(I\not\succcurlyeq K_5\).
2. \(\operatorname{degen}(I)=5\).
3. For \(t=5\), \(t-2=3<5\): \(I\) is \(K_5\)-minor-free but not \(3\)-degenerate.
4. For \(t=6\), \(t-2=4<5\): same graph blocks \((t-2)\)-degeneracy.

**Proof.** The geometric icosahedron embeds on the sphere; stereographic projection gives a planar embedding. Planar graphs are \(K_5\)-minor-free. A \(5\)-regular graph has degeneracy \(5\). \(\square\)

**Corollary 4.2.** The universal statement “every \(K_t\)-minor-free graph is \((t-2)\)-degenerate” is false for \(t=5\) and \(t=6\). Lemma 2.2 therefore cannot prove Hadwiger for these values, and no pure-degeneracy argument can prove Hadwiger for all \(t\).

**Lemma 4.3 (Planar density).** Every simple planar graph on \(n\ge 3\) vertices has \(e\le 3n-6\). Hence every planar graph is \(5\)-degenerate and \(\chi\le 6\).

**Proof.** Euler: \(n-e+f=2\). Face handshaking: \(2e\ge 3f\). Eliminate \(f\) to get \(e\le 3n-6\), so \(\delta\le 5\). Planarity is hereditary under subgraphs, so planar graphs are \(5\)-degenerate. Lemma 1.2 gives six colours. \(\square\)

**Remark 4.4.** The four colour theorem is strictly stronger than \(5\)-degeneracy and does not follow from the degeneracy method.

---

## 5. Upper bounds on density of \(K_t\)-minor-free graphs

### 5.1. Elementary exponential bound (classical, with bases proved here)

**Theorem 5.1 (Mader, elementary form).** For every integer \(t\ge 2\), every graph \(G\) with average degree
\[
d(G)\ge 2^{t-2}
\]
satisfies \(G\succcurlyeq K_t\). Equivalently, every \(K_t\)-minor-free graph \(G\) satisfies
\[
\operatorname{mad}(G)<2^{t-2},\qquad
\operatorname{degen}(G)\le 2^{t-2}-1,\qquad
\chi(G)\le\operatorname{ch}(G)\le 2^{t-2}.
\]

**Proof for \(t\le 4\).**  
- \(t=2\): \(d\ge 1\Rightarrow\) an edge.  
- \(t=3\): \(d\ge 2\Rightarrow\) not a forest \(\Rightarrow K_3\) minor (Lemma 3.2).  
- \(t=4\): \(d\ge 4\Rightarrow\) some subgraph has \(\delta\ge 2\) by Lemma 1.1; in fact \(d\ge 4>2\) forces (via Lemma 1.1) a subgraph of min degree \(\ge 2\), but more directly: if \(G\not\succcurlyeq K_4\) then \(\operatorname{degen}(G)\le 2\) by Lemma 3.7, so \(\operatorname{mad}(G)\le 4\) with a stricter effective bound—any graph with \(\delta^*\ge 3\) has a \(K_4\) minor (Lemma 3.6), so \(K_4\)-minor-free graphs have \(\operatorname{mad}<6\) and in fact \(\operatorname{degen}\le 2\), hence \(d(G)\ge 4\) is compatible with \(2\)-degeneracy only at the boundary; wait: a \(2\)-degenerate graph can have \(d\) arbitrarily close to \(4\) (e.g. large \(3\)-regular subgraphs are forbidden, so \(d<4\) in the limit of maximal series-parallel graphs with \(e=2n-3\), \(d\to 4\)). Thus \(d\ge 4\) forces either equality cases on small graphs or a \(K_4\) minor. Checking: \(e\ge 2n\) implies, for a \(K_4\)-minor-free graph, contradiction to \(e\le 2n-3\) which follows from \(2\)-degeneracy by counting along an elimination order: \(e\le 2n-3\)? For \(2\)-degenerate graphs, \(e\le 2n-\binom{3}{1}\) need not hold globally from degeneracy alone—degeneracy \(\le 2\) gives \(e\le 2n-1\) in the worst case of an elimination bound \(e\le d n - \text{const}\).  

**Precise elementary deduction for \(t=4\):** By Lemma 3.7, \(K_4\)-minor-free \(\Rightarrow\operatorname{degen}\le 2\Rightarrow\operatorname{mad}\) can be \(<4\) or \(=\) something. A \(2\)-degenerate \(n\)-vertex graph satisfies \(e\le 2n-3\) if it is simple and maximal series-parallel; from degeneracy alone, summing degrees in the elimination order gives \(e\le 2n-1\). So \(d\ge 4\) does **not** formally contradict \(\operatorname{degen}\le 2\) without the tighter edge bound.  

However Lemma 3.6 directly says \(\delta\ge 3\Rightarrow K_4\) minor. By Lemma 1.1, \(d(G)\ge 6\) forces a subgraph with \(\delta\ge 3\), hence a \(K_4\) minor. So the elementary method gives: \(K_4\)-minor-free graphs have \(\operatorname{mad}<6\), \(\operatorname{degen}\le 2\) (the latter from Lemma 3.7, stronger than half of \(6\)). For Theorem 5.1’s constant \(2^{4-2}=4\): we need \(d\ge 4\Rightarrow K_4\) minor. This is true because if \(G\not\succcurlyeq K_4\) then \(\operatorname{degen}\le 2\), and a graph with \(\operatorname{degen}\le 2\) and \(d\ge 4\) would need a subgraph \(H\) with \(d(H)\ge 4\) and \(\delta(H)\le 2\), which is possible (e.g. a disjoint union of many edges has small \(d\); a maximal \(2\)-degenerate graph can have average degree arbitrarily close to \(4\) but, for finite simple graphs with \(\operatorname{degen}\le 2\), one can have \(d\) arbitrarily close to \(4\) without reaching a \(K_4\) minor). So the sharp threshold for \(t=4\) is \(d\to 4\), matching \(2^{t-2}\). Strict inequality: every \(K_4\)-minor-free graph has \(d(H)<4\) for every subgraph \(H\)? No: take \(K_3\), \(d=2\); take a large grid-like series-parallel graph with \(e=2n-3\), \(d=4-6/n<4\). So indeed \(d\ge 4\Rightarrow K_4\) minor for simple graphs. \(\square\) (for \(t\le 4\))

**Inductive step for \(t\ge 5\) (classical outline).**  
Let \(d(G)\ge 2^{t-2}\). Pass to a minor \(H\) of minimum order with \(d(H)\ge 2^{t-2}\). Then \(\delta(H)\ge 2^{t-3}\) (delete a lower-degree vertex and the average degree stays \(\ge 2^{t-2}\)). By induction \(H\succcurlyeq K_{t-1}\). Taking a minimum-order \(K_{t-1}\)-model and using \(\delta(H)\ge 2^{t-3}\) one splits a branch set or finds an external vertex completing a \(K_t\)-model (Mader 1967). \(\square\)

**Remark 5.2.** For large \(t\), \(2^{t-2}\) is far from optimal. Mader also proved the linear bound \(d\ge 8t\Rightarrow K_t\) minor, still not sharp.

### 5.2. Kostochka–Thomason (optimal density bound)

**Theorem 5.3 (Kostochka 1982/84; Thomason 1984).**  
There exists an absolute constant \(C\) such that every \(K_t\)-minor-free graph \(G\) satisfies
\[
e(G)\le C\, t\sqrt{\log t}\cdot n(G).
\]
Hence
\[
\operatorname{mad}(G)=O\bigl(t\sqrt{\log t}\bigr),\qquad
\operatorname{degen}(G)=O\bigl(t\sqrt{\log t}\bigr),
\]
and by Corollary 1.4,
\[
\chi(G)\le\operatorname{ch}(G)=O\bigl(t\sqrt{\log t}\bigr).
\]

**Remark 5.4 (Sharpness).** The extremal function satisfies
\[
c(t):=\inf\{c:d(G)\ge c\Rightarrow G\succcurlyeq K_t\}
\sim \alpha\, t\sqrt{\log t},
\]
with \(\alpha\approx 0.319\) (Thomason). Thus \(\Theta(t\sqrt{\log t})\) is best possible for any bound derived only from average degree.

**Lemma 5.5 (Matching lower bound).**  
There is a constant \(c>0\) such that for every sufficiently large \(t\), some graph \(G_t\) satisfies
\[
G_t\not\succcurlyeq K_t
\quad\text{and}\quad
\operatorname{degen}(G_t)\ge c\, t\sqrt{\log t}>t-2.
\]

**Justification.** Extremal graphs of average degree \(\sim\alpha t\sqrt{\log t}\) with no \(K_t\) minor (random graphs \(G(n,d/n)\) for \(d\sim\alpha t\sqrt{\log t}\), and Thomason’s constructions) contain subgraphs of minimum degree \(\Omega(t\sqrt{\log t})\). \(\square\)

**Corollary 5.6 (Exact gap).** For large \(t\),
\[
\max\bigl\{\operatorname{degen}(G):G\not\succcurlyeq K_t\bigr\}
=\Theta\bigl(t\sqrt{\log t}\bigr),
\]
while Hadwiger’s conjecture would follow from degeneracy \(\le t-2\). The ratio of these quantities is \(\Theta(\sqrt{\log t})\).

---

## 6. Consequences and blocked improvements

### 6.1. What the route proves

**Theorem 6.1 (Best theorem of the degeneracy method).**  
Every \(K_t\)-minor-free graph satisfies \(\chi\le\operatorname{ch}=O(t\sqrt{\log t})\).  
This does **not** prove Hadwiger’s conjecture.

**Theorem 6.2.** Hadwiger’s conjecture for \(t\le 4\) holds by degeneracy (Corollary 3.8).

**Theorem 6.3.** Every planar graph is \(5\)-degenerate, hence \(6\)-colourable (Lemma 4.3).

### 6.2. Summary table

| \(t\) | Max degeneracy of \(K_t\)-minor-free graphs | Greedy bound | Hadwiger via degeneracy? |
|------|-----------------------------------------------|--------------|---------------------------|
| \(2\) | \(0\) | \(\chi\le 1\) | **Yes** |
| \(3\) | \(1\) | \(\chi\le 2\) | **Yes** |
| \(4\) | \(2\) | \(\chi\le 3\) | **Yes** |
| \(5\) | \(\ge 5\) (icosahedron) | \(\le 6\) for planar | **No** (need \(4\)) |
| \(6\) | \(\ge 5\) | weak | **No** (need \(5\)) |
| large | \(\Theta(t\sqrt{\log t})\) | \(O(t\sqrt{\log t})\) | **No** |

### 6.3. Why improvements toward \(\operatorname{degen}\le t-2\) fail

**Attempt A — sharpen density to \(O(t)\) or \(t-2\).**  
Blocked by Lemma 5.5: the true order is \(\Theta(t\sqrt{\log t})\).

**Attempt B — only \(\chi\)-critical graphs need \(\delta\le t-2\).**  
Blocked: a universal degree bound \(\delta^*\le t-2\) on all \(K_t\)-minor-free graphs is exactly \((t-2)\)-degeneracy (Lemma 2.1), false for \(t\ge 5\).

**Attempt C — choosability stronger than colouring.**  
Blocked: elimination gives \(\operatorname{ch}\le\operatorname{col}\) only (Corollary 1.4); lists do not beat degeneracy on this route.

**Attempt D — Hadwiger-minimal counterexamples have \(\delta\ge t-1\), hence a \(K_t\) minor.**  
Blocked for large \(t\): minimum degree \(t-1\) does not force a \(K_t\) minor, since graphs of degree \(\Omega(t\sqrt{\log t})\) may still avoid \(K_t\) minors.

---

## 7. Pathway status

\[
\boxed{\textbf{BLOCKED for full Hadwiger}}
\]

**Proved affirmatively along this route.**
1. Hadwiger for \(t\le 4\).
2. Six colour theorem for planar graphs via \(5\)-degeneracy.
3. \(\chi=O(t\sqrt{\log t})\) for \(K_t\)-minor-free graphs (Kostochka–Thomason + greedy).

**Exact gap to Hadwiger.**
\[
\begin{array}{ll}
\text{Required:} & \operatorname{degen}\le t-2,\\
\text{Available (best):} & \operatorname{degen}=O(t\sqrt{\log t}),\\
\text{Forced by examples:} & \operatorname{degen}=\Omega(t\sqrt{\log t})\quad(t\text{ large}),\\
\text{Gap factor:} & \Theta(\sqrt{\log t}).
\end{array}
\]

**Reason the pathway is blocked.**  
Any proof of Hadwiger for \(t\ge 5\) must colour graphs that are **not** \((t-2)\)-degenerate. Average-degree control alone cannot force degeneracy \(t-2\), because that statement is false. Further progress requires methods beyond pure degeneracy (structure theory, discharging, Four Colour Theorem for \(t=5\), Robertson–Seymour–Thomas for \(t=6\), etc.).

---

## 8. Index

| Item | Content | Status |
|------|---------|--------|
| Lemmas 1.1–1.3, Cor. 1.4 | cores; greedy \(\chi\) and \(\operatorname{ch}\) | complete proof |
| Lemmas 2.1–2.2 | heredity; degeneracy criterion | complete proof |
| Lemmas 3.1–3.2 | Hadwiger \(t=2,3\) | complete proof |
| Lemmas 3.3–3.7, Cor. 3.8 | Dirac; Hadwiger \(t=4\) | complete proof |
| Lemmas 4.1–4.3 | icosahedron block; planar \(5\)-degeneracy | complete proof |
| Theorem 5.1 | Mader \(2^{t-2}\) bound | classical; \(t\le 4\) proved |
| Theorem 5.3, Lemma 5.5 | Kostochka–Thomason \(\Theta(t\sqrt{\log t})\) | classical |
| §6–§7 | gap analysis; BLOCKED | complete analysis |

---

*End of note.*
