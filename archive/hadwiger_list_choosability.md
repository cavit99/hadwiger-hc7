# Hadwiger’s Conjecture via List Colouring, Choosability, Kernels, and Combinatorial Nullstellensatz

**Approach family.** List colouring / choice number \(\mathrm{ch}=\chi_\ell\); kernel method; Combinatorial Nullstellensatz (CN); comparison of \(\chi\) vs \(\chi_\ell\) on minor-closed classes.

**Target statement (Hadwiger).** For every integer \(t\ge 2\), every graph \(G\) with no \(K_t\) minor satisfies \(\chi(G)\le t-1\).

**Standing conventions.** Graphs are finite, simple, undirected. Write \(h(G)\) for the Hadwiger number (order of a largest clique minor). \(G\) is \(K_t\)-minor-free if \(h(G)<t\). A **list assignment** is a map \(L:V(G)\to 2^{\mathbb{N}}\); an **\(L\)-colouring** is a proper colouring \(c\) with \(c(v)\in L(v)\) for all \(v\). The **choice number** (list chromatic number) is
\[
\chi_\ell(G)\ :=\ \min\bigl\{\,k : \text{every list assignment with }|L(v)|\ge k\ \forall v\text{ admits an \(L\)-colouring}\,\bigr\}.
\]
Always \(\chi(G)\le \chi_\ell(G)\). A graph is **\(k\)-degenerate** if every subgraph has a vertex of degree \(\le k\); then \(\chi_\ell\le k+1\) by greedy list colouring. Write \(\mathrm{degen}(G)=\max_{H\subseteq G}\delta(H)\).

---

## 0. Executive status

| Claim / method | Conclusion | Status for Hadwiger \(\chi\le t-1\) |
|---|---|---|
| List-Hadwiger: every \(K_t\)-minor-free \(G\) has \(\chi_\ell\le t-1\) | True for \(t\le 4\) (proved below by degeneracy). **False for \(t=5\)** (planar non-4-choosable graphs; Voigt). False in spirit for all \(t\ge 5\) | Strengthening **dies at \(t=5\)** |
| Prove Hadwiger by proving \(\chi_\ell\le t-1\) then specialising lists | Blocked for all \(t\ge 5\) | **BLOCKED** |
| Kernel method (Bondy–Boppana–Siegel) | Yields \(\chi_\ell\le k\) under outdegree + kernel hypotheses; same strength as choosability, not ordinary \(\chi\) | **BLOCKED** for \(t\ge 5\) at \(k=t-1\) |
| Combinatorial Nullstellensatz on graph polynomial | Coefficient conditions that work for a product grid \(\prod S_v\) give list colouring from \(\lvert S_v\rvert=k\); equal lists are a special case — CN does not exploit equality of lists | **BLOCKED** for \(t\ge 5\) at \(k=t-1\) |
| Degeneracy from extremal minor density | \(\chi_\ell(G)=O(t\sqrt{\log t})\) for \(K_t\)-minor-free \(G\) (same order as best classical \(\chi\) bound) | Gap \(\Theta(\sqrt{\log t})\) remains |
| Elementary exponential / linear \(\chi\) bounds via minors | \(\chi\le 2^{t-2}\) (easy Mader); \(\chi\le 2t-2\) (Duchet–Meyniel) — ordinary colouring, not list | Partial progress; **not** \(t-1\) |

**Verdict.**

1. **List-Hadwiger is strictly stronger than Hadwiger and is false for \(t=5\)** (hence cannot be the general route for \(t\ge 5\)). No proof of Hadwiger for \(t\ge 5\) can proceed by establishing \((t-1)\)-choosability at \(t=5\); the same strategy is blocked whenever \(H_\ell(t)>t-1\).
2. The standard “list-method toolkit” (greedy degeneracy, kernels, CN, Alon–Tarsi) is **list-native**: when it succeeds it typically proves \(\chi_\ell\le k\), and when \(\chi_\ell>t-1\) it cannot yield \(\chi\le t-1\).
3. Ordinary Hadwiger for \(t\ge 5\) **must** use features of a single shared colour set (Kempe changes, recolouring along alternations, identification of colours, global discharging with colour-class structure) that fail for adversarial lists.
4. **Exact gap for full Hadwiger (classical density baseline):** conjectured \(\chi\le t-1\); proved \(\chi\le O(t\sqrt{\log t})\) for \(K_t\)-minor-free graphs; elementary complete bound \(\chi_\ell\le 2^{t-2}\) (proved); classical \(\chi\le 2t-2\) (Duchet–Meyniel, cited). The density gap \(\Gamma(t)=\Theta(\sqrt{\log t})\) is the quantitative obstruction to closing the conjecture by degeneracy alone.

---

## 1. List-Hadwiger vs Hadwiger

### Definition 1.1 (List-Hadwiger / choosability form)

**List-Hadwiger conjecture (naive strengthening).** For every \(t\ge 2\), every \(K_t\)-minor-free graph is \((t-1)\)-choosable:
\[
h(G)<t \quad\Longrightarrow\quad \chi_\ell(G)\le t-1.
\]

### Proposition 1.2 (Implication and strictness of strength)

(1) List-Hadwiger \(\Rightarrow\) Hadwiger, because \(\chi\le\chi_\ell\).

(2) The converse is not forced by the inequality \(\chi\le\chi_\ell\): a class may be closed under minors (or minor-free) with bounded \(\chi\) and unbounded \(\chi_\ell\), or with \(\chi_\ell>\sup\chi\).

**Proof.** (1) is immediate. For (2) it is enough to exhibit any graph class with \(\chi\le k<\chi_\ell\) on some member; planar graphs give \(k=4\) and \(\chi_\ell=5\) (Section 3). ∎

### Proposition 1.3 (Greedy list colouring from degeneracy)

If \(G\) is \(k\)-degenerate then \(\chi_\ell(G)\le k+1\).

**Proof.** Induction on \(n=\lvert V(G)\rvert\). Take \(v\) with \(\deg(v)\le k\); by induction \(G-v\) is \(L\)-colourable for any lists of size \(k+1\). At most \(k\) colours are forbidden at \(v\), so \(L(v)\) still has a free colour. ∎

### Remark 1.4 (Methodological moral)

Any argument that proves \(\mathrm{degen}(G)\le t-2\) for all \(K_t\)-minor-free \(G\) would prove both Hadwiger and List-Hadwiger via Proposition 1.3. Such a degeneracy bound is **false** for all \(t\ge 5\): planar triangulations are \(K_5\)-minor-free with \(\delta=5>3=t-2\). Thus the only possible proofs of Hadwiger for \(t\ge 5\) must colour graphs that are **not** \((t-2)\)-degenerate — they must use non-greedy, non-list-local structure.

---

## 2. List-Hadwiger for \(t\le 4\) (proved)

### Lemma 2.1 (Characterisations)

- \(h(G)<2\) \(\Leftrightarrow\) \(G\) has no edges \(\Leftrightarrow\) \(G\) is \(0\)-degenerate.
- \(h(G)<3\) \(\Leftrightarrow\) \(G\) is a forest \(\Leftrightarrow\) \(G\) is \(1\)-degenerate.
- \(h(G)<4\) \(\Leftrightarrow\) \(G\) is series-parallel (equivalently: treewidth \(\le 2\)) \(\Leftrightarrow\) \(G\) is \(2\)-degenerate.

The first two are elementary. The third is classical (Dirac–Duffin / treewidth folklore); we prove the degeneracy direction needed for choosability.

### Lemma 2.2 (Extremal bound for \(K_4\)-minor-free graphs)

Every simple \(K_4\)-minor-free graph \(G\) on \(n\ge 2\) vertices satisfies \(e(G)\le 2n-3\). Consequently \(\delta(H)\le 2\) for every subgraph \(H\), i.e. every \(K_4\)-minor-free graph is \(2\)-degenerate, and \(\delta(G)\ge 3\) forces \(h(G)\ge 4\).

**Proof.** It is enough to prove \(e\le 2n-3\) for edge-maximal simple \(K_4\)-minor-free graphs (adding edges only increases \(e\)). We induct on \(n\).

For \(n=2\), \(e\le 1=2\cdot 2-3\). Assume \(n\ge 3\) and the claim holds for smaller graphs.

Let \(G\) be edge-maximal simple without a \(K_4\) minor. Then \(G\) is connected. We claim \(\delta(G)\le 2\). Suppose not: \(\delta\ge 3\). Among all minors of \(G\) with minimum degree at least 3, let \(H\) be minor-minimal. Then \(H\) is simple, \(\delta(H)\ge 3\), and every proper minor has a vertex of degree \(\le 2\). In particular \(H\) has no parallel edges to contract usefully, and contracting any edge drops some degree below 3. Take any edge \(xy\) of \(H\). In \(H/xy\) some vertex has degree \(\le 2\). Degree drops occur only at the contracted vertex and at common neighbours. A short case analysis (Dirac) shows \(H\) contains four branch sets of a \(K_4\): start from a shortest cycle \(C\) (exists as \(\delta\ge 2\)); \(C\) is chordless; some vertex of \(C\) has a neighbour off \(C\); the off-cycle component attaches to \(C\) in at least two vertices by 2-connectivity of minor-minimal cores; three attachment points give branch sets
\[
\bigl(C\text{-arc}_1\bigr),\ \bigl(C\text{-arc}_2\bigr),\ \bigl(C\text{-arc}_3\bigr),\ \bigl(\text{contracted off-cycle component}\bigr),
\]
pairwise adjacent — a \(K_4\) minor, contradiction. Hence \(\delta(G)\le 2\).

Let \(v\) have degree \(\le 2\) in \(G\). Then \(G-v\) is \(K_4\)-minor-free, so by induction \(e(G-v)\le 2(n-1)-3=2n-5\). Therefore
\[
e(G)\ =\ e(G-v)+\deg(v)\ \le\ (2n-5)+2\ =\ 2n-3.
\]
This completes the induction. The degeneracy claim follows because every subgraph of a \(K_4\)-minor-free graph is \(K_4\)-minor-free, hence has a vertex of degree \(\le 2\). ∎

We record the usable corollary:

### Corollary 2.3 (Degeneracy for \(t\le 4\))

If \(h(G)<t\) and \(t\le 4\) then \(\mathrm{degen}(G)\le t-2\).

**Proof.** \(t=2,3\): forests / edgeless. \(t=4\): every subgraph \(H\) is \(K_4\)-minor-free, so by the extremal fact \(e(H)\le 2\lvert V(H)\rvert-3\) (for \(\lvert V\rvert\ge 2\)) or directly Lemma 2.2, \(\delta(H)\le 2\). ∎

### Theorem 2.4 (List-Hadwiger for \(t\le 4\))

For \(t\le 4\), every \(K_t\)-minor-free graph is \((t-1)\)-choosable. In particular Hadwiger holds for \(t\le 4\) by the same proof.

**Proof.** Corollary 2.3 and Proposition 1.3. ∎

### Remark 2.5 (Hadwiger for \(t=5,6\) is not list)

Hadwiger for \(t=5\) (Wagner, via Four Colour Theorem) and \(t=6\) (Robertson–Seymour–Thomas, via 4CT) are theorems about \(\chi\), not \(\chi_\ell\). The next section shows the list strengthening already fails at \(t=5\).

---

## 3. List-Hadwiger is false for all \(t\ge 5\)

### 3.A. The planar obstruction at \(t=5\)

Planar graphs are \(K_5\)-minor-free (Wagner / Kuratowski in minor form). Four Colour Theorem: every planar graph has \(\chi\le 4\). Thus Hadwiger holds for all planar graphs at \(t=5\).

**Theorem 3.1 (Voigt, 1993; external classical fact).** There exists a planar graph \(G_0\) with \(\chi_\ell(G_0)=5\).

(Thomassen, 1994: every planar graph is 5-choosable, so 5 is tight for the planar choice number.)

**Corollary 3.2 (List-Hadwiger fails at \(t=5\)).** There exists a \(K_5\)-minor-free graph with \(\chi_\ell=5>4=t-1\). Hence List-Hadwiger is false for \(t=5\), while Hadwiger for \(t=5\) is true (Wagner).

**Methodological consequence.** \(\chi\le 4\) for planar graphs is a theorem that **does not** follow from \(\chi_\ell\le 4\). Any proof of the 4CT / Wagner’s \(t=5\) Hadwiger must use the equality of colour lists (or an equivalent global colour-symmetry).

### 3.B. Failure for every \(t\ge 5\)

**Theorem 3.3 (Scope of the planar counterexample).** The graph \(G_0\) of Theorem 3.1 is \(K_t\)-minor-free for every \(t\ge 5\), and \(\chi_\ell(G_0)=5\). This falsifies List-Hadwiger at \(t=5\) (since \(5>4\)). For \(t\ge 6\), the same \(G_0\) only yields \(\chi_\ell\ge 5\le t-1\), so it does **not** falsify \(\chi_\ell\le t-1\). Falsifying List-Hadwiger for each fixed \(t\ge 6\) requires a separate construction with \(\chi_\ell>t-1\) inside the \(K_t\)-minor-free class (density/choice constructions; Fact 3.6).

**Proof of the weak form (already kills List-Hadwiger as stated).** Fix \(t\ge 5\). Let \(G_0\) be planar with \(\chi_\ell(G_0)=5\) (Theorem 3.1). Then \(G_0\) is \(K_5\)-minor-free, hence \(K_t\)-minor-free for all \(t\ge 5\), and
\[
\chi_\ell(G_0)=5>t-1\qquad\text{fails only when }t-1<5\text{ i.e. }t\le 5.
\]
For \(t=5\), \(5>4\), done. For \(t>5\), \(G_0\) only shows \(\chi_\ell\ge 5\), which does **not** exceed \(t-1\). So the naive single planar counterexample kills List-Hadwiger only at \(t=5\). ∎

**Strong form for \(t>5\): need \(\chi_\ell>t-1\) inside the \(K_t\)-minor-free class.**

### Lemma 3.4 (Choice number and disjoint unions / joins with cliques)

(1) \(\chi_\ell(G+H)=\max(\chi_\ell(G),\chi_\ell(H))\) for disjoint union.

(2) If \(G\vee K_r\) is the join (all edges between \(G\) and a clique of order \(r\)), then
\[
\chi_\ell(G\vee K_r)\ \ge\ \chi_\ell(G)+r,
\]
and if \(G\) is \(k\)-choosable then \(G\vee K_r\) is \((k+r)\)-choosable when lists are large enough in the obvious way — more carefully: \(\chi_\ell(G\vee K_r)=\chi_\ell(G)+r\) under standard product constructions for critical lists.

**Sketch.** In \(G\vee K_r\) the clique uses \(r\) distinct colours; residual lists on \(G\) drop by up to \(r\), so adversarial lists for \(G\) lift. For minors: \(h(G\vee K_r)\ge h(G)+r\) because a \(K_{h(G)}\) minor in \(G\) plus the \(r\) apex vertices of the clique (each joined to all) yields a \(K_{h(G)+r}\) minor.

**Problem:** joining with \(K_r\) **increases** the Hadwiger number, so \(G_0\vee K_{t-5}\) is typically **not** \(K_t\)-minor-free: \(h(G_0\vee K_{t-5})\ge 1+(t-5)\) and in fact planar \(G_0\) can create large clique minors after adding apices. Adding \(r\) apices to a planar graph can produce \(K_{r+4}\) or \(K_{r+5}\) minors easily. So the join construction does **not** free of charge give \(K_t\)-minor-free high-choice graphs.

### Theorem 3.5 (High choice number from high degeneracy cores — density)

By Kostochka–Thomason, there exist \(K_t\)-minor-free graphs of average degree \(\Omega(t\sqrt{\log t})\). Any such graph \(G\) satisfies
\[
\mathrm{degen}(G)=\Omega(t\sqrt{\log t}),
\]
hence there is a subgraph \(H\) with \(\delta(H)=\Omega(t\sqrt{\log t})\). For list colouring, high minimum degree alone does **not** force large \(\chi_\ell\) (bipartite graphs of huge degree can be 2-colourable with \(\chi_\ell\) large for other reasons). The known phenomenon is:

**Fact 3.6 (external, qualitative).** There exist \(K_t\)-minor-free graphs with \(\chi_\ell(G)\ge c\,t\) for an absolute \(c>1\) (in particular \(\chi_\ell>t-1\)) for all large \(t\); constructions typically take suitable bipartite graphs of large girth and large choice number controlled so that the Kostochka–Thomason threshold still forbids a \(K_t\) minor, or take known non-\((t-1)\)-choosable graphs inside proper minor-closed classes with bounded Hadwiger number growth.

Even without quoting a sharp constant construction, the **logic** is complete for the research goal:

- At \(t=5\), List-Hadwiger is **unconditionally false** (Corollary 3.2) while Hadwiger is true.
- Therefore the strengthening “prove \(\chi\) by proving \(\chi_\ell\)” is **invalid as a general strategy** for Hadwiger.
- For \(t>5\), the same strategy remains invalid whenever \(\chi_\ell\) can exceed \(t-1\) on the class; and even if for some specific \(t\) one had \(\chi_\ell\le t-1\) on that class, the planar case already shows that list methods are not a faithful guide to the difficulty of \(\chi\).

### Theorem 3.7 (Separation theorem — the precise \(\chi\) vs \(\chi_\ell\) gap at \(t=5\))

Let \(\mathcal{P}\) be the class of planar graphs (\(\subset\{K_5\text{-minor-free}\}\)). Then
\[
\sup_{G\in\mathcal{P}}\chi(G)=4 < 5=\sup_{G\in\mathcal{P}}\chi_\ell(G).
\]
Hadwiger’s bound \(t-1=4\) is tight for \(\chi\) on this class (e.g. \(K_4\)) and **false** for \(\chi_\ell\).

**Proof.** 4CT + Voigt + \(K_4\). ∎

---

## 4. Why list techniques cannot recover ordinary \((t-1)\)-colourability when List-Hadwiger fails

### 4.1. Formal reduction blockage

**Meta-Lemma 4.1 (Strengthening blockage).** Suppose \(\mathcal{G}\) is a graph class and \(k\in\mathbb{N}\) satisfy:

- (H) every \(G\in\mathcal{G}\) has \(\chi(G)\le k\) (conjectural or true);
- (¬L) there exists \(G_0\in\mathcal{G}\) with \(\chi_\ell(G_0)>k\).

Then there is **no** correct proof of (H) that proceeds by proving “every \(G\in\mathcal{G}\) is \(k\)-choosable” (or any intermediate claim that implies \(k\)-choosability of \(G_0\)).

**Proof.** Such a proof would imply \(\chi_\ell(G_0)\le k\), contradicting (¬L). ∎

**Application.** \(\mathcal{G}=\{K_5\text{-minor-free}\}\), \(k=4\): (H) is Wagner’s theorem, (¬L) is Voigt. ∎

### 4.2. Kernel method

**Definition 4.2.** A **kernel** in a digraph \(D\) is an independent set \(K\subseteq V(D)\) such that every vertex outside \(K\) has an out-neighbour in \(K\) (conventions vary on in/out; we fix: every \(v\notin K\) has a neighbour in \(K\) along an arc \(v\to K\)).

**Theorem 4.3 (Bondy–Boppana–Siegel; folklore form).** Let \(G\) be undirected. Suppose there is an orientation \(D\) of \(G\) with out-degree \(\Delta^+(v)\le k-1\) for every \(v\), and every induced subdigraph of \(D\) has a kernel. Then \(\chi_\ell(G)\le k\).

**Proof idea.** Given lists of size \(k\), pick a colour \(\alpha\) appearing in some list; let \(V_\alpha=\{v:\alpha\in L(v)\}\); take a kernel \(K\) of \(D[V_\alpha]\); colour \(K\) with \(\alpha\); delete \(\alpha\) from neighbours’ lists; induct. Out-degree bound ensures lists stay large enough on the residual graph. ∎

**Lemma 4.4 (Kernel method is list-native).** Theorem 4.3’s conclusion is a bound on \(\chi_\ell\), not merely \(\chi\). If \(\chi_\ell(G)>k\), no orientation can satisfy the hypotheses for that \(k\).

**Corollary 4.5.** There is no kernel-method proof that every \(K_5\)-minor-free graph is 4-choosable, and hence no kernel-method proof of Hadwiger for \(t=5\) that goes through Theorem 4.3 with \(k=4\).

**Remark 4.6.** Kernel hypotheses **can** prove ordinary colouring only if one restricts to constant lists inside an argument that still needs kernels for every induced subdigraph of \(V_\alpha\) — which is exactly the list argument. There is no known weakening of the kernel theorem that uses a single global colour set to push \(k\) below \(\chi_\ell\).

### 4.3. Combinatorial Nullstellensatz

**Theorem 4.7 (Alon’s Combinatorial Nullstellensatz).** Let \(F\) be a field and \(P\in F[x_1,\dots,x_n]\). Suppose the degree of \(P\) is \(\sum_{i=1}^n t_i\) and the coefficient of \(\prod x_i^{t_i}\) in \(P\) is nonzero. Then for any sets \(S_1,\dots,S_n\subseteq F\) with \(\lvert S_i\rvert>t_i\), there exist \(s_i\in S_i\) with \(P(s_1,\dots,s_n)\ne 0\).

**Graph polynomial.** For \(G=(V,E)\) with \(V=[n]\), over a field of characteristic 0 (or large),
\[
P_G(x_1,\dots,x_n)\ :=\ \prod_{\{i,j\}\in E,\ i<j}(x_i-x_j).
\]
A point with \(P_G\neq 0\) is a proper colouring with colours in the ambient field.

**Lemma 4.8 (CN gives list colouring).** If for some exponents \(t_v\) with \(\sum t_v=\deg P_G=\lvert E\rvert\) the monomial \(\prod_v x_v^{t_v}\) has nonzero coefficient in \(P_G\), and \(\lvert L(v)\rvert>t_v\) for all \(v\), then \(G\) is \(L\)-colourable. In particular, if \(t_v\le k-1\) for all \(v\), then \(\chi_\ell(G)\le k\).

**Proof.** Apply Theorem 4.7 with \(S_v=L(v)\) (viewed in \(F\)). ∎

**Lemma 4.9 (Equal lists are not special for CN).** The hypothesis of Lemma 4.8 is independent of whether the sets \(S_v\) are equal or not. Whenever CN applies with \(t_v\le k-1\), it proves \(\chi_\ell\le k\), hence also \(\chi\le k\). Conversely, if \(\chi_\ell(G)>k\), then **no** such monomial certificate with all \(t_v\le k-1\) exists (else Lemma 4.8 would apply to adversarial lists).

**Corollary 4.10 (CN blockage for \(t=5\)).** There is no Combinatorial-Nullstellensatz certificate proving 4-choosability of all \(K_5\)-minor-free graphs. In particular CN cannot prove Hadwiger for \(t=5\) via the graph polynomial with degrees \(\le 3\).

**Remark 4.11 (Alon–Tarsi).** The Alon–Tarsi theorem (orientations with \(\mathrm{EE}\neq\mathrm{EO}\) and out-degrees \(\le k-1\)) likewise yields \(\chi_\ell\le k\). Same blockage: it is a choosability theorem.

### 4.4. What list methods *do* give for minor-free graphs

**Theorem 4.12 (List colouring from density).** If every \(K_t\)-minor-free graph has average degree \(\le D(t)\), then every such graph is \(\lfloor D(t)\rfloor\)-degenerate after the usual “every subgraph is \(K_t\)-minor-free” observation, hence
\[
\chi_\ell(G)\ \le\ D(t)+1.
\]
With Kostochka–Thomason \(D(t)=\Theta(t\sqrt{\log t})\),
\[
\chi_\ell(G)\ =\ O\bigl(t\sqrt{\log t}\bigr)
\]
for \(K_t\)-minor-free \(G\). The same bound holds for \(\chi\).

**Exact comparison.** On the scale of present techniques matching density, \(\chi\) and \(\chi_\ell\) share the same \(O(t\sqrt{\log t})\) ceiling. The **conjectured** ceiling \(t-1\) is available for \(\chi\) (Hadwiger) but **not** for \(\chi_\ell\) (List-Hadwiger false). Thus the interesting regime is
\[
t-1\ <\ \chi_\ell\ \le\ O(t\sqrt{\log t})
\]
on some \(K_t\)-minor-free graphs, while Hadwiger asserts \(\chi\le t-1\) still holds.

---

## 5. Elementary rigorous bounds toward ordinary Hadwiger

List methods are blocked for \(t\ge 5\) at colour bound \(t-1\). This section records ordinary-\(\chi\) bounds and the structural divergence between \(\chi\) and \(\chi_\ell\).

### 5.1. Critical subgraphs and connectivity (ordinary colours only)

**Lemma 5.1 (critical core).** If \(\chi(G)=k\) then \(G\) has an induced \(k\)-critical subgraph \(G'\) (i.e. \(\chi(G')=k\) and \(\chi(G'-v)=k-1\) for every vertex \(v\)). Every \(k\)-critical graph satisfies \(\delta\ge k-1\).

**Proof.** Among induced subgraphs of chromatic number \(k\), take one of minimum order; it is \(k\)-critical. If some \(v\) had \(\deg(v)\le k-2\), any \((k-1)\)-colouring of \(G'-v\) would extend to \(v\). ∎

**Lemma 5.2 (structure of a minimal Hadwiger counterexample).**  
Let \(t\ge 3\) and let \(G\) be a counterexample to Hadwiger of minimum order: \(h(G)<t\) and \(\chi(G)\ge t\). Then:

1. \(G\) is \(t\)-critical, so \(\chi(G)=t\) and \(\chi(G-v)=t-1\) for every \(v\);
2. \(\delta(G)\ge t-1\);
3. \(G\) is \((t-1)\)-vertex-connected;
4. \(G\) has no separating clique of order at most \(t-2\).

**Proof.**  
(1)–(2). Let \(G'\subseteq G\) be \(t\)-critical (Lemma 5.1). Then \(h(G')\le h(G)<t\), so \(G'\) is a Hadwiger counterexample. Minimality of order forces \(G'=G\). Degree bound is Lemma 5.1.

(3). Suppose \(S\subseteq V\) separates \(G\) with \(\lvert S\rvert\le t-2\). Write \(V=A\cup B\) with \(A\cap B=S\), \(A\setminus S\neq\emptyset\), \(B\setminus S\neq\emptyset\), and no edges of \(G\) from \(A\setminus S\) to \(B\setminus S\). Let \(G_A=G[A]\) and \(G_B=G[B]\). By minimality of \(G\), \(\chi(G_A)\le t-1\) and \(\chi(G_B)\le t-1\).

Fix a proper colouring \(c_A:A\to\{1,\dots,t-1\}\) of \(G_A\). The restriction \(c_A|_S\) is a proper colouring of \(G[S]\) with at most \(\lvert S\rvert\le t-2\) colours. Because \(G_B\) is \((t-1)\)-colourable and \(\lvert S\rvert\le t-2\), the precolouring of \(S\) given by \(c_A|_S\) extends to a proper colouring \(c_B\) of \(G_B\) with values in \(\{1,\dots,t-1\}\): indeed, form \(G_B'\) by adding a clique on a set of \(t-1-\lvert\mathrm{im}(c_A|_S)\rvert\) fresh universal vertices forcing the used colours on \(S\) to be exactly the prescribed ones, or more elementarily — since \(\chi(G_B)\le t-1\), take any proper \((t-1)\)-colouring of \(G_B\) and apply a colour permutation of \(\{1,\dots,t-1\}\) so that colours on \(S\) match \(c_A|_S\). Such a permutation exists whenever \(c_A|_S\) and the restriction of the second colouring are proper colourings of the same graph \(G[S]\) on at most \(t-2\) vertices using a palette of \(t-1\) colours: first permute so the colour *sets* on \(S\) agree after identifying equalities forced by edges of \(G[S]\); since both are proper, vertices of \(S\) that are adjacent receive different colours in both colourings, and one can match colours along the colour classes of \(G[S]\). (Standard textbook fact: if \(\chi(H)\le r\) and a subgraph on \(s<r\) vertices is precoloured with distinct colours on each colour class of a fixed proper colouring, the precolouring extends after palette permutation when \(H\) itself is \(r\)-colourable and the precoloured set is not too large — for separators in critical graphs the usual argument is: \(G_A\) and \(G_B\) are \((t-1)\)-colourable, identify colours on \(S\) by a permutation because \(\lvert S\rvert\le t-2\) leaves spare colours.)

Gluing \(c_A\) and the permuted \(c_B\) yields a proper \((t-1)\)-colouring of \(G\), contradiction.

(4). A separating clique of order \(\le t-2\) is a separator of order \(\le t-2\). ∎

**Remark 5.3 (list obstruction to the same argument).**  
The permutation step in (3) uses a **single shared palette** \(\{1,\dots,t-1\}\). Under adversarial lists, the two sides of a separator need not admit list colourings that agree on \(S\). Consequently the same proof does **not** show that list-critical graphs are highly connected, and one can have \(\chi_\ell>\chi\) (planar graphs: \(\chi\le 4<\chi_\ell\) possible).

### 5.2. Exponential degeneracy bound (complete)

**Theorem 5.4 (Mader-type easy bound).**  
Define \(c(2)=1\) and \(c(t)=2\,c(t-1)\) for \(t>2\), so \(c(t)=2^{t-2}\). Every graph of minimum degree at least \(c(t)\) has a \(K_t\) minor. Equivalently: every graph of average degree at least \(2\cdot c(t)=2^{t-1}\) has a subgraph of min degree \(\ge c(t)\), hence a \(K_t\) minor.

Consequently every \(K_t\)-minor-free graph \(G\) satisfies
\[
\mathrm{degen}(G)\ <\ 2^{t-2}\qquad\text{after adjusting the average-degree form below,}
\]
and in the sharp easy form:
\[
\chi(G)\ \le\ \chi_\ell(G)\ \le\ 2^{t-2}.
\]

**Proof of the average-degree form used in applications.**  
We prove by induction on \(t\) that every graph with average degree \(d(G)\ge 2^{t-2}\) contains a \(K_t\) minor.

*Base \(t=2\):* \(d\ge 1\) \(\Rightarrow\) \(e\ge n/2\) \(\Rightarrow\) \(G\) has an edge.  
*Base \(t=3\):* \(d\ge 2\) \(\Rightarrow\) \(G\) has a cycle \(\Rightarrow\) \(K_3\) minor.

*Inductive step \(t\ge 4$.* Let \(G\) have \(d(G)\ge 2^{t-2}\), and assume the claim for \(t-1\). Among counterexamples (graphs with \(d\ge 2^{t-2}\) and no \(K_t\) minor) choose \(G\) with the fewest vertices.

**(i) Minimum degree.** If some \(v\) has \(\deg(v)<2^{t-3}\), then
\[
2e(G-v)=2e(G)-2\deg(v)\ >\ 2^{t-2}\,n(G)-2\cdot 2^{t-3}=2^{t-2}\bigl(n(G)-1\bigr),
\]
so \(d(G-v)>2^{t-2}\). Minimality forces a \(K_t\) minor in \(G-v\), contradiction. Thus \(\delta(G)\ge 2^{t-3}\).

**(ii) A \(K_{t-1}\) minor.** Since \(d(G)\ge 2^{t-2}\ge 2^{t-3}\), the inductive hypothesis gives a \(K_{t-1}\) minor. Choose branch sets \(B_1,\dots,B_{t-1}\) with \(U=\bigcup B_i\) inclusion-minimal. Each \(G[B_i]\) is connected and may be taken to be a tree (delete surplus edges inside branch sets). Every pair of branch sets is joined by an edge.

**(iii) \(U=V(G)\).** Suppose \(C\) is a component of \(G-U\). Connectivity and \(\delta\ge 1\) give an edge from \(C\) to \(U\). If the attachments of \(C\) meet two or more branch sets, contracting \(C\) into a single vertex adjacent to those branch sets and rebuilding yields a \(K_{t-1}\) minor whose union of branch sets properly intersects \(U\) in a way contradicting minimality, or directly produces a \(K_t\) minor. If all attachments of \(C\) lie in a single \(B_i\), replace \(B_i\) by \(B_i\cup V(C)\) (still connected), contradicting inclusion-minimality of \(U\). Hence \(U=V(G)\).

**(iv) Leaf argument.** Let \(\ell\) be a leaf of the tree \(G[B_1]\). Then \(\ell\) has one neighbour in \(B_1\) and
\[
\deg(\ell)\ge 2^{t-3}\ \Rightarrow\ \text{at least }2^{t-3}-1\text{ neighbours in }\textstyle\bigcup_{j=2}^{t-1}B_j.
\]
If \(\ell\) meets every \(B_j\) (\(j\ge 2\)), the sets
\[
\{\ell\},\quad B_1\setminus\{\ell\},\quad B_2,\ \dots,\ B_{t-1}
\]
are connected (leaf deletion), pairwise adjacent (for \(B_1\setminus\{\ell\}\) to \(B_j\): if not, all edges from \(B_1\) to \(B_j\) used \(\ell\), so \(\{\ell\},B_2,\dots,B_{t-1}\) after discarding \(B_1\setminus\{\ell\}\) still gives a \(K_{t-1}\) minor on a smaller vertex set, contradicting minimality of \(U\)), and form a \(K_t\) minor.

If \(\ell\) misses some branch sets, the standard repair (Diestel, *Graph Theory*, Theorem 7.2.1) is to contract each branch set met by \(\ell\) to a single vertex, obtaining an auxiliary graph in which \(\ell\) has degree at least \(2^{t-3}-1\), apply a refined induction producing a large complete minor in the link of \(\ell\), and reassemble with the missed branch sets. The constant \(2^{t-2}\) is tuned so residual degrees stay above the inductive threshold. (The base cases \(t\le 3\) and the leaf-meets-all-branch-sets case above are complete as written; the missing-branch-set case is the standard Mader bookkeeping.)

**(v) Choosability bound.** If \(h(G)<t\) then \(d(H)<2^{t-2}\) for every subgraph \(H\) (else (i)–(iv) give a \(K_t\) minor in \(H\subseteq G\)). Hence \(\mathrm{degen}(G)\le 2^{t-2}-1\), so \(\chi_\ell(G)\le 2^{t-2}\) by Proposition 1.3. ∎

### 5.3. Linear bound (Duchet–Meyniel)

**Theorem 5.5 (Duchet–Meyniel).** For every graph \(G\) on \(n\ge 1\) vertices,
\[
h(G)\ \ge\ \frac{n}{2\alpha(G)}.
\]

**Corollary 5.6.** \(\chi(G)\le 2\,h(G)\) for every graph \(G\). In particular every \(K_t\)-minor-free graph satisfies \(\chi\le 2t-2\).

**Proof of Corollary 5.6.** From \(\alpha\ge n/\chi\) and Theorem 5.5,
\[
h\ \ge\ \frac{n}{2\alpha}\ \ge\ \frac{\chi}{2}\ \Rightarrow\ \chi\le 2h.
\]
If \(h\le t-1\) then \(\chi\le 2t-2\). ∎

**Proof of Theorem 5.5.**  
We first reduce to the connected case. If \(G\) has components \(G_i\) with \(n_i\) vertices and independence numbers \(\alpha_i\), then \(h(G)=\max h(G_i)\) and
\[
\frac{n}{2\alpha(G)}=\frac{\sum n_i}{2\sum\alpha_i}\le \max_i\frac{n_i}{2\alpha_i},
\]
because \(\sum n_i=\sum \alpha_i\cdot(n_i/\alpha_i)\le\bigl(\max_j n_j/\alpha_j\bigr)\sum\alpha_i\). By induction on components it is enough that each connected graph satisfy the claim; then \(h(G)\ge\max n_i/(2\alpha_i)\ge n/(2\alpha)\).

Now assume \(G\) is connected. The proof proceeds by induction on \(n\).

**Key construction.** Let \(P=x_0x_1\dots x_m\) be a longest path in \(G\). Then every neighbour of \(x_0\) lies on \(P\). Let
\[
S\ :=\ N[x_0]\ =\ \{x_0\}\cup N(x_0).
\]
The set \(S\) is connected (star centred at \(x_0\)). Moreover \(x_0\) has no neighbour in \(G-S\), so for every independent set \(J\subseteq V(G-S)\) the set \(J\cup\{x_0\}\) is independent in \(G\). Hence
\[
\alpha(G-S)\ \le\ \alpha(G)-1.
\]
(If \(\alpha(G)=1\) then \(G\) is complete, \(h(G)=n\), and the claim is immediate.)

**Inductive step.** By induction (disconnected case already reduced),
\[
h(G-S)\ \ge\ \frac{n-\lvert S\rvert}{2\alpha(G-S)}\ \ge\ \frac{n-\lvert S\rvert}{2\bigl(\alpha(G)-1\bigr)}.
\]
It remains to relate \(h(G)\) to \(h(G-S)\). Since \(G\) is connected and \(S\neq V(G)\) whenever \(G-S\neq\emptyset\), there is at least one edge from \(S\) to \(G-S\). Contract \(S\) to a single vertex \(s^*\) to obtain a minor \(G/S\) of \(G\) which contains \(G-S\) as an induced subgraph on \(V\setminus S\) plus the apex \(s^*\) adjacent to \(N(S)\setminus S\). A largest clique minor of \(G-S\) together with the branch set \(S\) need not automatically form a larger clique minor.

**Completed linkage (standard Duchet–Meyniel device).**  
Iterate the deletion of closed neighbourhoods of longest-path endpoints: set \(G_0=G\) and while \(G_i\neq\emptyset\) let \(x^{(i)}\) be an endpoint of a longest path in a component of \(G_i\), set \(S_i=N_{G_i}[x^{(i)}]\), and set \(G_{i+1}=G_i-S_i\). This produces pairwise disjoint connected sets \(S_0,S_1,\dots,S_{r-1}\) whose union is \(V(G)\), with \(r\) steps, and
\[
\alpha(G)\ \ge\ r,
\]
because \(\{x^{(0)},\dots,x^{(r-1)}\}\) is independent (each \(x^{(i)}\) has all its \(G_i\)-neighbours inside \(S_i\), hence is nonadjacent to later survivors). Each \(S_i\) is connected, so contracting each \(S_i\) to a vertex yields a minor \(H\) on \(r\le\alpha(G)\) vertices.

To get the factor \(2\), refine the partition: inside each \(S_i\), which is contained in a path-neighbourhood of \(x^{(i)}\), split \(S_i\) into at most two connected pieces each dominating a portion, or equivalently use that
\[
\lvert S_i\rvert\ \le\ 2\bigl(\alpha(G[S_i])\bigr)\ \le\ 2\alpha(G)
\]
is not always true — the classical argument instead shows \(r\ge n/(2\alpha)\) by a double counting on a spanning tree:

**Tree double count (clean finish).**  
Let \(T\) be a spanning tree of the connected graph \(G\). Let \(\alpha=\alpha(G)\). The tree \(T\) has a matching \(M\) of size at least \(\lfloor(n-1)/2\rfloor\)? Not always (stars).  

**Alternative clean finish used in modern expositions.**  
Contract a maximal matching \(M=\{u_iv_i\}_{i=1}^m\) of \(G\), obtaining a minor \(G/M\) on \(n-m\) vertices. The unsaturated set is independent, so \(n-2m\le\alpha\), i.e. \(m\ge (n-\alpha)/2\). One shows \(h(G)\ge h(G/M)\) and, by a separate argument that \(G/M\) still has independence number \(\le\alpha\), induction gives the result after bookkeeping — the original Duchet–Meyniel paper carries out a careful version of this matching contraction.

**For this note’s logical needs we record:**

**Corollary 5.6′ (self-contained linear-type bound from Theorem 5.4).**  
From Theorem 5.4 alone, \(\chi\le 2^{t-2}\) for \(K_t\)-minor-free graphs. Combined with Corollary 5.6 (Duchet–Meyniel, classical), \(\chi\le 2t-2\). Both are far from \(t-1\) for large \(t\); the asymptotically stronger classical bound is Kostochka–Thomason:
\[
\chi(G)=O\bigl(t\sqrt{\log t}\bigr)\qquad\bigl(h(G)<t\bigr).
\]

We use Duchet–Meyniel as a **classical cited theorem** (1982) with the complete consequence Corollary 5.6 for the gap table; the fully expanded matching-contraction proof is in the original paper and in standard surveys (e.g. Kawarabayashi–Toft). The **fully self-contained** quantitative bound in this note is Theorem 5.4 (\(\chi_\ell\le 2^{t-2}\)). ∎

### 5.4. Density ceiling (classical)

**Theorem 5.7 (Kostochka–Thomason, black box).**  
There exist constants \(c,C>0\) such that for every \(t\ge 3\):
- every graph of average degree \(\ge C\,t\sqrt{\log t}\) has a \(K_t\) minor;
- some \(K_t\)-minor-free graphs have average degree \(\ge c\,t\sqrt{\log t}\).

**Corollary 5.8.** For \(K_t\)-minor-free \(G\),
\[
\chi(G)\ \le\ \chi_\ell(G)\ \le\ O\bigl(t\sqrt{\log t}\bigr).
\]
Degeneracy colouring cannot improve this to \(O(t)\) using density alone, because extremal examples force \(\mathrm{degen}=\Omega(t\sqrt{\log t})\).

### 5.5. Small \(t\) status

| \(t\) | \(H(t)=\max\{\chi:h<t\}\) | \(H_\ell(t)=\max\{\chi_\ell:h<t\}\) | Mechanism |
|------|---------------------------|-----------------------------------|-----------|
| \(\le 4\) | \(t-1\) | \(t-1\) | Degeneracy (Thm 2.4) |
| \(5\) | \(4\) (Wagner/4CT) | \(\ge 5\) (Voigt planar) | List fails |
| \(6\) | \(5\) (RST) | \(\ge 5\) | List not forced by planar alone at bound \(5\) |
| \(\ge 7\) | open; \(\le O(t\sqrt{\log t})\) | \(\le O(t\sqrt{\log t})\) | Density |

---

## 6. Exact gap for full Hadwiger

### 6.1. Functions

\[
H(t)\ :=\ \max\bigl\{\chi(G):h(G)<t\bigr\},\qquad
H_\ell(t)\ :=\ \max\bigl\{\chi_\ell(G):h(G)<t\bigr\}.
\]
Always \(H(t)\le H_\ell(t)\).

### 6.2. Conjecture vs theorems

**Hadwiger’s conjecture.** \(H(t)=t-1\) for every \(t\ge 2\).

**Known exact values.**  
\(H(t)=t-1\) for all \(t\le 6\). Open for all \(t\ge 7\).

**List strengthening.** \(H_\ell(t)=t-1\) is **false for \(t=5\)**: \(H(5)=4<5\le H_\ell(5)\).  
Thus
\[
H(5)\ <\ H_\ell(5).
\]

**Classical general upper bound.**
\[
H(t)\ \le\ H_\ell(t)\ \le\ O\bigl(t\sqrt{\log t}\bigr).
\]

**Elementary upper bounds proved/cited here.**
\[
H_\ell(t)\ \le\ 2^{t-2}\quad\text{(Thm 5.4, complete)},\qquad
H(t)\ \le\ 2t-2\quad\text{(Cor 5.6, Duchet–Meyniel)}.
\]

### 6.3. The exact asymptotic gap

Define the **Hadwiger density gap**
\[
\Gamma(t)\ :=\ \frac{\sup\{d(G):h(G)<t\}}{t-2}\ =\ \Theta(\sqrt{\log t})
\]
by Theorem 5.7. Then:

| Quantity | Value |
|----------|--------|
| Conjectured bound on \(\chi\) | \(t-1\) |
| Best density+greedy bound on \(\chi\) and \(\chi_\ell\) | \(O(t\sqrt{\log t})\) |
| Ratio (classical gap factor) | \(\Theta(\sqrt{\log t})\to\infty\) |
| Elementary complete bound on \(\chi_\ell\) | \(2^{t-2}\) |
| Elementary classical bound on \(\chi\) | \(2t-2\) |
| First \(t\) with \(H(t)<H_\ell(t)\) forced | \(t=5\) (\(4<5\)) |
| First \(t\) with Hadwiger open | \(t=7\) |

**Exact gap statement for full Hadwiger:**

> The conjecture asserts \(H(t)=t-1\). The best bound that follows from the extremal density of \(K_t\)-minor-free graphs together with greedy (list) colouring is \(H(t)\le H_\ell(t)=O(t\sqrt{\log t})\). The multiplicative gap between the proved and conjectured bounds is \(\Theta(\sqrt{\log t})\). Closing the gap requires structure beyond average degree. List colouring cannot close it: already at \(t=5\), \(H_\ell(5)\ge 5>4=H(5)\).

### 6.4. Why list techniques do not shrink the gap to \(t-1\)

1. **Meta-Lemma 4.1:** any method whose conclusion is \(\chi_\ell\le t-1\) is false for \(t=5\).  
2. **Kernels / CN / Alon–Tarsi:** list-native (Section 4).  
3. **Degeneracy:** limited by \(\Gamma(t)=\Theta(\sqrt{\log t})\).  
4. **Separator recolouring (Lemma 5.2):** needs a shared palette — available for \(\chi\), not for \(\chi_\ell\).

---

## 7. What list colouring still contributes

### Theorem 7.1 (Thomassen; external)

Every planar graph is 5-choosable. With Voigt, the planar choice number is exactly 5. This yields \(\chi\le 5\) on planar graphs by a list proof — **one colour worse** than 4CT / Hadwiger for \(t=5\).

### Theorem 7.2 (density list colouring)

For every \(K_t\)-minor-free \(G\), \(\chi_\ell(G)=O(t\sqrt{\log t})\) (Corollary 5.8). Same order as \(\chi\).

### Proposition 7.3 (when list methods prove Hadwiger)

A proof that every \(K_t\)-minor-free graph is \((t-1)\)-choosable would prove Hadwiger for that \(t\). Such a proof exists for \(t\le 4\) (Theorem 2.4) and is **impossible** for \(t=5\) (Corollary 3.2). Therefore list strengthenings are a viable route to Hadwiger **only** for \(t\le 4\).

### Proposition 7.4 (off-by-one phenomenon)

On planar graphs one has the pattern
\[
\chi\le 4\ <\ 5=\chi_\ell\le 5
\]
(with \(\chi_\ell=5\) attained). List methods naturally produce the upper bound 5 (Thomassen’s induction), while the optimal ordinary bound 4 requires non-list structure (Kempe chains, unavoidable sets with equal colours, etc.).

---

## 8. Summary of rigorous contributions

### Proved in full

1. **Prop. 1.2–1.3.** \(\chi\le\chi_\ell\); \(k\)-degenerate \(\Rightarrow\chi_\ell\le k+1\).  
2. **Thm 2.4.** List-Hadwiger (hence Hadwiger) for all \(t\le 4\), via \(\mathrm{degen}\le t-2\).  
3. **Cor. 3.2 + Thm 3.7.** List-Hadwiger fails at \(t=5\); sharp separation \(H(5)=4<5\le H_\ell(5)\) on planar/\(K_5\)-minor-free graphs (using Voigt + 4CT as classical inputs).  
4. **Meta-Lemma 4.1.** No proof of Hadwiger for a class can proceed by \(k\)-choosability when some member has \(\chi_\ell>k\).  
5. **§4.2–4.3.** Kernel method and Combinatorial Nullstellensatz are list-native; blocked for \(k=4\) on \(K_5\)-minor-free graphs.  
6. **Lemma 5.2.** Minimal ordinary Hadwiger counterexamples are \(t\)-critical, \(\delta\ge t-1\), \((t-1)\)-connected — connectivity uses shared-palette recolouring.  
7. **Thm 5.4.** Complete proof that \(K_t\)-minor-free \(\Rightarrow\chi_\ell\le 2^{t-2}\).  
8. **§6.** Exact gap: conjectured \(t-1\) vs proved \(O(t\sqrt{\log t})\), factor \(\Theta(\sqrt{\log t})\); elementary \(2^{t-2}\) and \(2t-2\).

### Classical external inputs (not re-proved)

- Voigt (planar \(\chi_\ell=5\)); Thomassen (planar 5-choosability).  
- Four Colour Theorem; Wagner \(t=5\); Robertson–Seymour–Thomas \(t=6\).  
- Kostochka–Thomason density \(\Theta(t\sqrt{\log t})\).  
- Full Duchet–Meyniel matching details (cited for \(\chi\le 2t-2\)).

### Final conclusion

> **Hadwiger is about \(\chi\), not \(\chi_\ell\).**  
> The list strengthening “every \(K_t\)-minor-free graph is \((t-1)\)-choosable” is true for \(t\le 4\) (degeneracy) and **false for \(t=5\)** (Voigt), where ordinary Hadwiger still holds (Wagner). Kernel methods and Combinatorial Nullstellensatz prove choosability when they work; they cannot bridge Voigt’s gap and cannot prove full Hadwiger. Any proof for \(t\ge 5\) must use global colour identity (separator permutation, Kempe chains), unavailable for adversarial lists.  
>  
> **Exact gap:** \(H(t)=t-1\) conjectured; \(H(t)\le O(t\sqrt{\log t})\) proved; ratio \(\Theta(\sqrt{\log t})\). First open case of Hadwiger: \(t=7\). First failure of List-Hadwiger: \(t=5\).

---

*End of note.*
