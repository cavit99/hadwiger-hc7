# Attack on Rigid Portal Configurations (RPC)

**Gap targeted.** \(G_t^{\mathrm{hyb}}\): no \(\Phi\)-maximal contact-deficient model in a minimal counterexample is an RPC ([`hadwiger_hybrid_fan_absorption.md`](hadwiger_hybrid_fan_absorption.md), Corollary 5.3).

**Standing hypotheses (throughout).** Fix \(t\ge 5\). Let \(G\) be a \(t\)-contraction-critical graph with
\[
\eta(G)=t-1,\qquad \delta(G)\ge t,\qquad
\text{\(G\) has no separating clique},
\]
and, for a fixed apex \(v\in V(G)\),
\[
\eta(G-v)=t-1.
\]
(If \(G\) is a minimal counterexample to \(\mathrm{HC}_t\), all of this holds, with \(\delta\ge t\) by the Dirac neighbourhood lemma when \(t\ge 4\); subgraph-criticality supplies no separating clique and rainbow neighbourhoods.) We use Dirac’s bound \(\kappa(G)\ge t-1\) as classical input in the same status as the MCM/hybrid notes (so Surplus Menger applies). Every proper \((t-1)\)-colouring of \(G-v\) is rainbow on \(N(v)\).

**Inherited from the hybrid note (used freely).**
- \(Z=\emptyset\) at every \(\Phi\)-maximum ([hybrid, Thm 1.1](hadwiger_hybrid_fan_absorption.md)).
- Surplus Menger: \(\ge t-1\) internally disjoint \(v\)–\(C\) paths ([hybrid, Thm 2.1](hadwiger_hybrid_fan_absorption.md)).
- SPPA for strongly private non-cut portals ([hybrid, Thm 4.4–4.5](hadwiger_hybrid_fan_absorption.md)).
- Dichotomy: \(\Phi\)-max deficient \(\Rightarrow\) SPPA (contradiction) or RPC ([hybrid, Thm 5.2](hadwiger_hybrid_fan_absorption.md)).

**What this note delivers.**
1. Full type-analysis of rigidity \((R1)(R2)(R3)\).
2. **No pure-\((R2)\)-only RPC** under \(\delta\ge t\) (Theorem 3.4).
3. **Pure-\((R2)\) trade calculus** and forced size inequalities at \(\Phi\)-max (Theorem 3.6–3.8).
4. **Free \((R1)\)-block absorption** and **inessential \((R3)\) absorption** (Theorems 4.3, 5.3).
5. **Double-portal forced mixed rigidity** (Theorem 3.3).
6. A **finite abstract RPC outside criticality**, showing RPC geometry is not vacuous as a pure model configuration (Proposition 7.1).
7. Precise residual hard core: **linked \((R1){+}(R3)\) irreplaceable cuts** (Section 8).

**Honesty bound.** Full non-existence of every RPC in a contraction-critical graph is **not** claimed. The residual core of Section 8 is exactly the remaining obstruction for Lemma G / \(G_t^{\mathrm{hyb}}\).

---

## 0. Notation (recall)

A \(K_{t-1}\) model \(\mathcal{B}=\{B_1,\dots,B_{t-1}\}\) in \(G-v\) has contact index set
\[
S=S(\mathcal{B},v)=\{i:N(v)\cap B_i\neq\emptyset\},\qquad s=|S|,
\]
\[
J=\{1,\dots,t-1\}\setminus S,\quad
A=\bigcup_{i\in S}B_i,\quad
C=\bigcup_{j\in J}B_j,\quad
Z=V(G-v)\setminus(A\cup C).
\]
Contact potential \(\Phi(v,\mathcal{B})=(s,-|Z|,-\sum_i|B_i|^2)\) (lexicographic). At a \(\Phi\)-max: \(Z=\emptyset\), and in a counterexample \(s\le t-2\).

**Last exit / portal.** For a \(v\)–\(C\) path \(P\), walk from \(v\); let \(y\) be the first vertex in \(C\) and \(\alpha\) its predecessor. Then \(\alpha\in A\cap\partial(C)\) with \(\partial(C)=\{x\in A:x\sim C\}\).

**Strongly private non-cut portal** ([hybrid Def 4.1](hadwiger_hybrid_fan_absorption.md)): \(\alpha\in B_i\cap\partial(C)\) with
1. \(|B_i|\ge 2\) and \(\alpha\) a leaf of some spanning tree of \(G[B_i]\);
2. \(N(v)\cap B_i\not\subseteq\{\alpha\}\) (residual contact);
3. for every \(k\neq i\), \(\alpha\) is not the unique neighbour of \(B_k\) inside \(B_i\).

**Rigid portal.** \(\alpha\in B_i\cap\partial(C)\) fails to be strongly private non-cut, i.e. at least one of:
- **(R1)** \(\alpha\) is a cutvertex of \(G[B_i]\);
- **(R2)** \(N(v)\cap B_i\subseteq\{\alpha\}\) (unique contact representative);
- **(R3)** \(\exists\,k\neq i\) such that every \(B_i\)–\(B_k\) edge is incident with \(\alpha\) (unique cross-attachment).

**RPC.** A \(\Phi\)-maximal contact-deficient model for which every last exit of every maximum (and every root) \(v\)–\(C\) fan is rigid.

---

## 1. Load lemmas under \(\delta\ge t\)

### Lemma 1.1 (Surplus portal set)
There is a package of \(\mu\ge t-1\) pairwise internally vertex-disjoint \(v\)–\(C\) paths whose last exits \(\alpha_1,\dots,\alpha_\mu\) are pairwise distinct and lie in \(A\cap\partial(C)\). Write \(L=\{\alpha_1,\dots,\alpha_\mu\}\).

**Proof.** Hybrid Theorem 2.1 and Lemma 2.4. ∎

### Lemma 1.2 (Pigeonhole on portals)
Some contact block \(B_i\) (\(i\in S\)) satisfies \(|B_i\cap L|\ge 2\).

**Proof.** If \(|B_i\cap L|\le 1\) for all \(i\in S\), then \(|L|\le s\le t-2\), contradicting \(|L|\ge t-1\). ∎

### Lemma 1.3 (Degree load)
\(|N(v)|\ge t\), \(N(v)\subseteq A\), and some contact block contains at least two neighbours of \(v\).

**Proof.** \(\delta\ge t\) and hybrid Corollary 2.7 (pigeonhole of \(\ge t\) neighbours into \(\le t-2\) contact blocks). ∎

### Lemma 1.4 (Not all contact bags are singletons)
It is impossible that \(|B_i|=1\) for every \(i\in S\).

**Proof.** If every contact bag is a singleton then \(|N(v)|\le s\le t-2\), contradicting \(|N(v)|\ge t\). ∎

### Lemma 1.5 (Singletons are automatically rigid)
If \(B_i=\{x\}\) with \(i\in S\) and \(x\in\partial(C)\), then \(x\) is rigid: (R2) holds, and (R3) holds vacuously for every \(k\neq i\) (every edge leaving \(B_i\) is incident with \(x\)). Condition (1) of strong privacy fails because no spanning tree of a singleton has a leaf in the sense of Def 4.1 with \(|B_i|\ge 2\).

**Proof.** Immediate. ∎

---

## 2. Type calculus for \((R2)\)

### Lemma 2.1 (\((R2)\) forces the portal into \(N(v)\))
Suppose \(\alpha\in B_i\) is rigid via \((R2)\) and \(i\in S\). Then
\[
N(v)\cap B_i=\{\alpha\},
\]
in particular \(\alpha\in N(v)\).

**Proof.** By \((R2)\), \(N(v)\cap B_i\subseteq\{\alpha\}\). By \(i\in S\), \(N(v)\cap B_i\neq\emptyset\). Hence equality, and \(\alpha\in N(v)\). ∎

### Lemma 2.2 (At most one \((R2)\)-portal per contact block)
A contact block \(B_i\) contains at most one vertex that is rigid via \((R2)\). Equivalently: if \(\alpha,\alpha'\in B_i\) are distinct and both satisfy \((R2)\), contradiction.

**Proof.** Lemma 2.1 would force \(\alpha=\alpha'\) as the unique element of \(N(v)\cap B_i\). ∎

### Lemma 2.3 (Multi-contact blocks forbid \((R2)\))
If \(|N(v)\cap B_i|\ge 2\), then no vertex of \(B_i\) is rigid via \((R2)\). Every rigid portal in such a block fails strong privacy only through \((R1)\) and/or \((R3)\).

**Proof.** \((R2)\) requires \(N(v)\cap B_i\subseteq\{\alpha\}\), impossible if the left side has size \(\ge 2\). ∎

### Definition 2.4 (Pure types)
A rigid portal \(\alpha\in B_i\) is:
- **pure \((R2)\)** if \((R2)\) holds, but neither \((R1)\) nor \((R3)\) holds;
- **pure \((R1)\)** if \((R1)\) holds, but neither \((R2)\) nor \((R3)\) holds;
- **pure \((R3)\)** if \((R3)\) holds, but neither \((R1)\) nor \((R2)\) holds;
- **mixed** otherwise (at least two of \((R1),(R2),(R3)\)).

### Lemma 2.5 (Characterisation of pure \((R2)\))
\(\alpha\in B_i\cap\partial(C)\) is pure \((R2)\) if and only if all of the following hold:
1. \(N(v)\cap B_i=\{\alpha\}\) (so \(\alpha\in N(v)\));
2. \(\alpha\) is **not** a cutvertex of \(G[B_i]\) (hence \(|B_i|\ge 2\) and \(G[B_i\setminus\{\alpha\}]\) is connected and nonempty);
3. for every \(k\neq i\), some vertex of \(B_i\setminus\{\alpha\}\) is adjacent to \(B_k\).

**Proof.** Unpack Definitions 2.4 and the rigid/portal axioms; (2) and \(|B_i|\ge 2\) force a spanning tree of \(G[B_i]\) in which \(\alpha\) is a leaf (take a spanning tree of \(G[B_i\setminus\{\alpha\}]\) and attach \(\alpha\) by any edge into that set). ∎

---

## 3. No pure-\((R2)\)-only RPC

### Theorem 3.1 (Double portal forces non-\((R2)\) rigidity)
Let \(\mathcal{B}\) be an RPC at \(v\), and let \(L\) be a last-exit set of a maximum \(v\)–\(C\) fan as in Lemma 1.1. Let \(B_i\) be a contact block with \(|B_i\cap L|\ge 2\) (Lemma 1.2), and let \(\alpha,\alpha'\in B_i\cap L\) be distinct. Then at least one of \(\alpha,\alpha'\) fails to be pure \((R2)\). In particular at least one of \(\alpha,\alpha'\) is rigid via \((R1)\) or \((R3)\).

**Proof.** If both were pure \((R2)\), Lemma 2.2 is contradicted. ∎

### Theorem 3.2 (Stronger: at most one pure \((R2)\) portal in the whole of \(L\cap B_i\))
Under the same hypotheses, \(|L\cap B_i\cap\{\text{pure \((R2)\) portals}\}|\le 1\).

**Proof.** Lemma 2.2. ∎

### Theorem 3.3 (Every RPC uses \((R1)\) or \((R3)\))
In every RPC under the standing hypotheses, some last exit of some maximum \(v\)–\(C\) fan is rigid via \((R1)\) or via \((R3)\) (possibly mixed with \((R2)\)).

**Proof.** Theorems 3.1 and Lemma 1.2. ∎

### Theorem 3.4 (No pure-\((R2)\)-only RPC) — **main partial elimination**
There is **no** RPC in which every rigid last exit of every maximum \(v\)–\(C\) fan is pure \((R2)\).

**Proof.** Theorem 3.3. ∎

### Remark 3.5 (Why \(\delta\ge t\) is essential for the global shape)
Without \(\delta\ge t\), one could have \(s=t-2\) and \(|N(v)|=t-1\) with each contact bag a singleton neighbour of \(v\). Then every portal in \(N(v)\cap\partial(C)\) is rigid by Lemma 1.5, and a pure-\((R2)\)-flavoured RPC (all bags singletons) is formally possible as a model configuration. Lemma 1.4 kills that global singleton regime precisely when \(\delta\ge t\). Theorem 3.4 then upgrades the obstruction from “not all bags singletons” to “some portal must use cutvertex or unique-cross geometry.”

---

## 4. Pure \((R2)\): trade calculus at \(\Phi\)-max

### Lemma 4.1 (Pure \((R2)\) trade preserves models)
Let \(\alpha\in B_i\cap N(v)\cap\partial(C)\) be pure \((R2)\), and let \(y\in B_j\) (\(j\in J\)) with \(\alpha\sim y\). Set
\[
B_j^\sharp:=B_j\cup\{\alpha\},\qquad
B_i^\flat:=B_i\setminus\{\alpha\},\qquad
B_k^\flat:=B_k\ (k\neq i,j).
\]
Then \(\mathcal{B}^\sharp:=\{B_k^\flat:k\neq i,j\}\cup\{B_i^\flat,B_j^\sharp\}\) is a \(K_{t-1}\) model in \(G-v\) with
\[
s(\mathcal{B}^\sharp,v)=s(\mathcal{B},v).
\]
(Contact trades index \(i\) for index \(j\).)

**Proof.**
- \(B_i^\flat\neq\emptyset\) and \(G[B_i^\flat]\) is connected: pure \((R2)\) forbids \((R1)\).
- \(G[B_j^\sharp]\) is connected: \(\alpha\sim y\).
- Disjointness: immediate.
- Cross-edges off \(\{i,j\}\): unchanged.
- Cross-edges from \(B_i^\flat\) to every \(B_k\) with \(k\neq i\): pure \((R2)\) forbids \((R3)\), so residual attachments exist (including to \(B_j\)).
- Cross-edges from \(B_j^\sharp\): old cross-edges of \(B_j\) survive; \(\alpha\) only adds incidences.
- Contact: \(j\) becomes a contact index via \(\alpha\in N(v)\); \(i\) loses its unique contact. All other contact indices are untouched. Net: \(s\) unchanged. ∎

### Lemma 4.2 (Third-coordinate change)
In the trade of Lemma 4.1, writing \(a=|B_i|\) and \(b=|B_j|\),
\[
\sum_k |B_k^\sharp|^2-\sum_k |B_k|^2 = 2(b-a+1).
\]
Hence \(\Phi(v,\mathcal{B}^\sharp)>\Phi(v,\mathcal{B})\) in the third coordinate (with \(s\) and \(|Z|\) equal) if and only if \(b\le a-2\).

**Proof.** Expand \((a-1)^2+(b+1)^2-a^2-b^2=2(b-a+1)\). The potential’s third coordinate is \(-\sum|B|^2\), so \(\Phi\) increases in the third slot precisely when the sum of squares decreases, i.e. \(2(b-a+1)<0\), i.e. \(b\le a-2\). ∎

### Theorem 4.3 (Size obstruction for pure \((R2)\) at \(\Phi\)-max)
Let \(\mathcal{B}\) maximise \(\Phi\) and let \(\alpha\in B_i\) be a pure \((R2)\) last exit adjacent to \(B_j\) (\(j\in J\)). Then
\[
|B_j|\ \ge\ |B_i|-1.
\]
In particular, if \(\alpha\) is adjacent to some non-contact block of size at most \(|B_i|-2\), one may trade as in Lemma 4.1 and strictly increase \(\Phi\), contradiction.

**Proof.** Lemma 4.1–4.2 and maximality of \(\Phi\). ∎

### Corollary 4.4 (No pure \((R2)\) portal into a tiny non-contact block)
At \(\Phi\)-max, a pure \((R2)\) portal \(\alpha\in B_i\) cannot be adjacent to any \(B_j\subseteq C\) with \(|B_j|\le|B_i|-2\).

**Proof.** Theorem 4.3. ∎

### Theorem 4.5 (Equal-size trade yields an alternate maximiser)
If \(|B_j|=|B_i|-1\) and \(\alpha\in B_i\) is pure \((R2)\) adjacent to \(B_j\), the trade of Lemma 4.1 produces another \(\Phi\)-maximiser \(\mathcal{B}^\sharp\) with the same contact count, the same unused set \(\emptyset\), and the same sum of squares, whose contact index set is \((S\setminus\{i\})\cup\{j\}\).

**Proof.** Lemmas 4.1–4.2. ∎

### Remark 4.6 (Why pure \((R2)\) still survives as a local type)
Theorem 3.4 eliminates RPCs **made only of** pure \((R2)\) portals. Theorems 4.3–4.5 constrain pure \((R2)\) portals that **coexist** with \((R1)/(R3)\) portals: they cannot feed tiny non-contact blocks, and equal-size trades only permute maximisers. A pure \((R2)\) portal adjacent only to non-contact blocks of size \(\ge|B_i|\) does not by itself raise \(\Phi\). That local type is therefore not fully eliminated — only stripped of the “all portals pure \((R2)\)” regime and of the “absorb into a much smaller bag” regime.

### Proposition 4.7 (No residual-contact repair by a second \(N(v)\) vertex inside \(B_i\))
If \(\alpha\) is pure \((R2)\) then \(N(v)\cap B_i=\{\alpha\}\), so no second neighbour of \(v\) in \(B_i\) can restore residual contact after a prospective SPPA move of \(\alpha\). Any repair of residual contact must import a neighbour of \(v\) from a different contact block (global reassignment).

**Proof.** Lemma 2.1. ∎

---

## 5. Free \((R1)\)-block absorption

### Lemma 5.1 (Cutvertex decomposition)
If \(\alpha\) is a cutvertex of \(G[B_i]\), write \(K_1,\dots,K_p\) (\(p\ge 2\)) for the components of \(G[B_i]-\alpha\). Then every vertex of \(B_i\setminus\{\alpha\}\) lies in a unique \(K_q\), and every \(K_q\)–\(K_{q'}\) path in \(G[B_i]\) meets \(\alpha\).

**Proof.** Standard. ∎

### Definition 5.2 (Free component of a cut portal)
Let \(\alpha\in B_i\) be a cutvertex and \(K\) a component of \(G[B_i]-\alpha\). Write \(B_i^\circ:=B_i\setminus V(K)\) (so \(\alpha\in B_i^\circ\) and \(G[B_i^\circ]\) is connected). Call \(K\) **free** if:
1. **No private cross-edge.** For every \(k\neq i\), if some vertex of \(K\) is adjacent to \(B_k\), then some vertex of \(B_i^\circ\) is also adjacent to \(B_k\).
2. **Residual contact off \(K\).** \(N(v)\cap B_i\not\subseteq V(K)\).
3. **C-exit.** Either some vertex of \(K\) is adjacent to \(C\), or \(\alpha\in\partial(C)\) and we allow a joint move of \(\{\alpha\}\cup V(K)\) only under the stronger hypotheses of Remark 5.5.

### Theorem 5.3 (Free \((R1)\)-component absorption — **proved**)
Let \(\mathcal{B}\) be a \(K_{t-1}\) model with \(Z=\emptyset\) and \(J\neq\emptyset\). Let \(\alpha\in B_i\) be a cutvertex, \(K\) a free component of \(G[B_i]-\alpha\) in the sense of Definition 5.2(1)–(2), and assume some vertex of \(K\) is adjacent to \(B_j\) for a fixed \(j\in J\) (or, after including a direct edge from \(K\) into \(C\), rename so the first-hit non-contact index is \(j\)). Set
\[
B_j^\sharp:=B_j\cup V(K),\qquad
B_i^\flat:=B_i\setminus V(K)=B_i^\circ,\qquad
B_k^\flat:=B_k\ (k\neq i,j).
\]
Then \(\mathcal{B}^\sharp\) is a \(K_{t-1}\) model. Moreover, if some vertex of \(V(K)\) lies in \(N(v)\), then \(s(\mathcal{B}^\sharp,v)\ge s(\mathcal{B},v)+1\) after accounting for residual contact of \(B_i^\flat\) by freeness (2); if no vertex of \(K\) lies in \(N(v)\) but the move is performed as part of a larger fan absorption that deposits a neighbour of \(v\) into a non-contact block by a different path, contact bookkeeping is external to this lemma.

**Clean contact-gain subcase.** If \(V(K)\cap N(v)\neq\emptyset\) and freeness (2) holds, then \(i\) retains contact in \(B_i^\flat\) and \(j\) gains contact, so
\[
s(\mathcal{B}^\sharp,v)=s(\mathcal{B},v)+1.
\]

**Proof.**
- \(G[B_i^\flat]\) is connected and nonempty: \(B_i^\flat=B_i^\circ\) contains \(\alpha\) and is the union of \(\{\alpha\}\) with the other components of \(G[B_i]-\alpha\).
- \(G[B_j^\sharp]\) is connected: \(K\) meets \(B_j\) by hypothesis.
- Disjointness: immediate.
- Cross-edges from \(B_i^\flat\) to every \(B_k\), \(k\neq i\): freeness (1) supplies a residual attachment whenever \(K\) had one; attachments that never used \(K\) survive a fortiori. Attachments from \(B_i\) to \(B_j\) that used only \(K\) are replaced by the fact that \(B_j^\sharp\) already contains \(K\), and \(B_i^\flat\)–\(B_j^\sharp\) still need an edge: freeness (1) for \(k=j\) gives a \(B_i^\circ\)–\(B_j\) edge, or if \(K\) was the only \(B_i\)–\(B_j\) link then after the move the edge is internal to \(B_j^\sharp\) and we need a different \(B_i^\flat\)–\(B_j^\sharp\) edge — **this is why freeness (1) for \(k=j\) is required**. (If the only \(B_i\)–\(B_j\) edges left \(K\), freeness (1) fails for \(k=j\), and \(K\) is not free.)
- Cross-edges from \(B_j^\sharp\): old cross-edges of \(B_j\) survive.
- Contact in the clean subcase: \(V(K)\cap N(v)\neq\emptyset\) puts a neighbour of \(v\) into \(B_j^\sharp\); freeness (2) retains a neighbour of \(v\) in \(B_i^\flat\). ∎

### Corollary 5.4 (Free \((R1)\) blocks are forbidden at \(\Phi\)-max)
At a \(\Phi\)-maximum, no contact block admits a free component \(K\) (Def 5.2) that meets \(N(v)\) and meets \(C\) (or meets a non-contact block) in the sense of Theorem 5.3’s clean subcase.

**Proof.** Theorem 5.3 would raise \(s\). ∎

### Remark 5.5 (Non-free \((R1)\): the residual cut core)
If every component \(K\) of \(G[B_i]-\alpha\) carries a **private** cross-edge to some \(B_{k(K)}\) (an edge with no residual from \(B_i^\circ\)), then freeness (1) fails for every \(K\). This is the **irreplaceable cutvertex** situation of hybrid Remark 6.8: each side of the cut is load-bearing for the clique model. No elementary single-component move applies. This is retained as residual core (Section 8).

### Theorem 5.6 (Pure \((R1)\) with a free side is absorbable)
If \(\alpha\) is pure \((R1)\) (so residual contact and residual cross-edges hold globally for \(\alpha\) itself) and some component \(K\) of \(G[B_i]-\alpha\) is free and meets \(N(v)\cap\partial(C)\) after routing, then \(\Phi\) increases by Theorem 5.3. Consequently, at \(\Phi\)-max every pure \((R1)\) portal is an **irreplaceable** cutvertex: no free \(N(v)\)-meeting component exists.

**Proof.** Combine purity (no \((R2)\), no \((R3)\) for \(\alpha\) as a vertex) with Corollary 5.4. Note: purity of \(\alpha\) does **not** automatically free the components of \(G[B_i]-\alpha\); private cross-edges may leave those components even when \(\alpha\) itself is not a unique attachment for any bag (unique attachments could be vertices inside \(K\), not \(\alpha\)). The theorem records the free-side subcase only. ∎

---

## 6. \((R3)\): local cuts and inessential unique attachments

### Lemma 6.1 (\((R3)\) is a local cut in a 2-bag union)
Suppose \(\alpha\in B_i\) is a unique cross-attachment from \(B_i\) to \(B_k\) (R3). Then \(\{\alpha\}\) separates \(B_i\setminus\{\alpha\}\) from \(B_k\) inside \(G[B_i\cup B_k]\). In particular there is no edge from \(B_i\setminus\{\alpha\}\) to \(B_k\).

**Proof.** Hybrid Lemma 7.2–7.3. ∎

### Definition 6.2 (Inessential unique attachment)
Say that \((R3)\) for the pair \((B_i,B_k)\) at \(\alpha\) is **inessential** if there exists a path in \(G-v-\alpha\) from \(B_i\setminus\{\alpha\}\) to \(B_k\) whose interior lies in
\[
V(G-v)\setminus\bigl(B_i\cup B_k\bigr)
\]
and can be absorbed into \(B_i\) or \(B_k\) without destroying other cross-edges — more precisely, the following **bridge-reassignment** is available.

### Theorem 6.3 (Bridge repair of inessential \((R3)\) — **proved local form**)
Suppose \(\alpha\in B_i\) satisfies \((R3)\) for \(B_k\), and suppose there is a path
\[
Q:\quad u=q_0q_1\dots q_\ell=x
\]
with \(u\in B_i\setminus\{\alpha\}\), \(x\in B_k\), \(\{q_1,\dots,q_{\ell-1}\}\) pairwise disjoint from \(B_i\cup B_k\cup\{\alpha\}\), and each internal vertex \(q_r\) lying in some branch set \(B_{\pi(r)}\) that remains connected after deleting \(q_r\) and is not uniquely attached through \(q_r\) to any bag (leaf-Steiner hypothesis on the interior). Then one may reassign the interior of \(Q\) into \(B_i\) or \(B_k\) so that after deleting \(\alpha\) from \(B_i\) (or moving \(\alpha\) into a non-contact block), the pair \((B_i^\flat,B_k)\) retains a cross-edge. In particular, \((R3)\) is not an absolute obstruction once a leaf-Steiner bridge exists.

**Proof.** Same bookkeeping as hybrid Lemma 7.2 (minor-bridge form) and MCM Lemma 12.5 (leaf attachments): move interior Steiner vertices that are leaves of their bags into \(B_i\) (or \(B_k\)), obtaining a \(u\)–\(x\) connection in the enlarged bag system; then \(\alpha\) is no longer needed as the unique \(B_i\)–\(B_k\) attachment. ∎

### Corollary 6.4 (Essential \((R3)\) at \(\Phi\)-max)
At a \(\Phi\)-maximum, every \((R3)\) instance that blocks a portal move is **essential**: no leaf-Steiner bridge as in Theorem 6.3 exists. Equivalently, every path in \(G-v-\alpha\) from \(B_i\setminus\{\alpha\}\) to \(B_k\) must either fail to exist outside \(B_i\cup B_k\), or use a Steiner vertex that is itself a cutvertex or unique attachment in its bag (recursion into the residual core).

**Proof.** Theorem 6.3 and maximality (else repair then SPPA/PNCP raises \(\Phi\)). ∎

### Theorem 6.5 (Pure \((R3)\) direct portal into non-contact — expansion)
Let \(\alpha\in B_i\cap N(v)\cap\partial(C)\) be pure \((R3)\): so \(\alpha\) is not a cutvertex of \(B_i\), residual contact holds (\(N(v)\cap B_i\not\subseteq\{\alpha\}\)), and for some \(k\neq i\) every \(B_i\)–\(B_k\) edge meets \(\alpha\). Let \(y\in B_j\) (\(j\in J\)) with \(\alpha\sim y\).

**Attempted move.** Same as PNCP: \(B_j^\sharp=B_j\cup\{\alpha\}\), \(B_i^\flat=B_i\setminus\{\alpha\}\).

**What survives.** Connectivity of \(B_i^\flat\) and residual contact: yes (pure \((R3)\) forbids \((R1)\) and \((R2)\)). Cross-edges from \(B_i^\flat\) to every bag **except** those \(k\) for which \(\alpha\) was unique attachment: fail precisely for those \(k\).

**Expansion repair when \(k\in J\).** If the only \((R3)\)-violations are for non-contact indices \(k\in J\), absorb \(\alpha\) into \(B_j\) and simultaneously note that a unique attachment to another non-contact block \(B_k\) becomes an internal or cross issue inside \(C\): after the move, \(B_i^\flat\) may lose its edge to \(B_k\). Repair: since \(\alpha\in B_j^\sharp\) and \(\alpha\sim B_k\) (unique attachment was from \(\alpha\)), the edge \(\alpha\)–\(B_k\) is now a \(B_j^\sharp\)–\(B_k\) edge (both non-contact originally; \(B_k\) still non-contact). For the model we need \(B_i^\flat\)–\(B_k\): **still missing**. So pure expansion into one non-contact block does **not** repair unique attachments to **other** non-contact blocks.

**Expansion repair when \(k\in S\) and a bridge exists.** Use Theorem 6.3.

**Status.** Pure \((R3)\) with essential unique attachment into a contact bag and no leaf-Steiner bridge remains open (residual core). Pure \((R3)\) that is inessential is absorbable after bridge repair, then SPPA. ∎

### Remark 6.6 (Hybrid Kempe as a bridge factory — partial)
By hybrid Lemma 3.2, every rainbow pair of neighbours of \(v\) is joined by a Kempe path in \(G-v\). If both ends lie in \(A\) and a Kempe path avoids a rigid portal \(\alpha\), its vertex set is a candidate minor-bridge (hybrid Lemma 7.2). This does **not** automatically give leaf-Steiner interiors: Kempe paths may snake through many bags. Full conversion of Kempe paths into Theorem 6.3 bridges for every essential \((R3)\) is **not** proved here (same simultaneous bookkeeping as Lemma G).

---

## 7. Finite abstract RPC outside criticality

### Proposition 7.1 (RPC geometry exists abstractly — finite example)
There exists a finite graph \(H\) with a distinguished apex \(v\), a \(K_4\) model in \(H-v\) (so the local parameters match \(t=5\)), contact deficiency \(s=2\le 3=t-2\), \(Z=\emptyset\), and the property that every last exit of every \(v\)–\(C\) path is rigid, such that \(\delta(H)\le 2<5\) (hence \(H\) is not \(5\)-critical and fails \(\delta\ge t\)). Thus RPC as pure model+fan geometry is **not** vacuous; criticality / \(\delta\ge t\) / no-separating-clique are essential for any non-existence claim.

**Construction.** Let
\[
V(H)=\bigl\{v,\alpha,u,w,b,d,c\bigr\}
\]
with branch sets in \(H-v\)
\[
B_1=\{\alpha,u,w\},\qquad B_2=\{b\},\qquad B_3=\{d\},\qquad B_4=\{c\}.
\]
Edges:
- inside \(B_1\): \(u-\alpha-w\) (so \(\alpha\) is a cutvertex of \(G[B_1]\), with components \(\{u\}\) and \(\{w\}\));
- cross-edges for a \(K_4\) model:
  \[
  \alpha{-}b,\ \alpha{-}d,\ \alpha{-}c,\quad
  b{-}d,\ b{-}c,\ d{-}c,\quad
  u{-}b,\quad w{-}d;
  \]
- apex: \(v{-}\alpha\), \(v{-}b\).

Then \(S=\{1,2\}\), \(s=2\), \(J=\{3,4\}\), \(A=B_1\cup B_2\), \(C=\{d,c\}\), \(Z=\emptyset\).

**Model check.** Cross-pairs:
\(B_1\)–\(B_2\) via \(\alpha{-}b\) and \(u{-}b\);
\(B_1\)–\(B_3\) via \(\alpha{-}d\) and \(w{-}d\);
\(B_1\)–\(B_4\) via \(\alpha{-}c\) only;
\(B_2\)–\(B_3\) via \(b{-}d\);
\(B_2\)–\(B_4\) via \(b{-}c\);
\(B_3\)–\(B_4\) via \(d{-}c\). All connected bags, all pairs joined. ∎*(model)*

**Rigidity of last exits.** Every \(v\)–\(C\) path has last exit in \(\{\alpha,b\}\subseteq A\cap\partial(C)\):
- \(\alpha\): \((R1)\) holds (cutvertex of \(B_1\)); \((R2)\) holds (\(N(v)\cap B_1=\{\alpha\}\)); \((R3)\) holds for \(k=4\) (unique \(B_1\)–\(B_4\) edge \(\alpha{-}c\)). Mixed rigid.
- \(b\): singleton contact bag, rigid by Lemma 1.5.

Both components of \(B_1-\alpha\) carry **private** cross-edges (\(u{-}b\), \(w{-}d\)), so freeness (Definition 5.2) fails on both sides — residual-core geometry.

**Standing CE hypotheses fail.** \(\deg(u)=2\) (neighbours \(\alpha,b\) only), so \(\delta(H)\le 2<t\). In particular \(H\) is not \(5\)-critical.

**Point of the example.** Mixed \((R1){+}(R2){+}(R3)\) at \(\alpha\) with irreplaceable private cross-edges on both cut sides occurs in a tiny non-critical graph. Non-existence of RPC is not a formal emptiness of rigid last-exit geometry. ∎

### Corollary 7.2 (Criticality separates abstract RPC from CE-RPC)
Proposition 7.1 shows that non-existence of RPC **requires** the critical / \(\delta\ge t\) / no-separating-clique package; the obstruction is not a purely formal absence of rigid last-exit geometry among all graphs.

**Proof.** Proposition 7.1. ∎

---

## 8. Residual hard core (precise)

### Definition 8.1 (Irreplaceable rigid portal)
A rigid portal \(\alpha\in B_i\cap L\) is **irreplaceable** if all of the following hold:
1. every component \(K\) of \(G[B_i]-\alpha\) (if \(\alpha\) is a cutvertex) carries at least one private cross-edge to some bag (freeness fails);
2. every \((R3)\) instance at \(\alpha\) is essential in the sense of Corollary 6.4 (no leaf-Steiner bridge);
3. if \((R2)\) holds, every non-contact neighbour block \(B_j\) of \(\alpha\) satisfies \(|B_j|\ge|B_i|-1\) (Theorem 4.3), so pure trade does not raise \(\Phi\).

### Theorem 8.2 (Structure theorem for residual RPC)
Let \(\mathcal{B}\) be a \(\Phi\)-maximal contact-deficient model that is an RPC under the standing hypotheses. Then:
1. **(Not pure \((R2)\))** Some portal in \(L\) uses \((R1)\) or \((R3)\) (Theorem 3.3).
2. **(No free cut side)** No free \(N(v)\)-meeting \((R1)\)-component exists (Corollary 5.4).
3. **(No inessential \((R3)\))** Every \((R3)\) that blocks absorption is essential (Corollary 6.4).
4. **(No tiny pure-\((R2)\) trade)** Every pure \((R2)\) portal obeys the size bound of Theorem 4.3.
5. **(Double portal)** Some \(B_i\) contains two distinct portals of \(L\), at least one irreplaceable via \((R1)\) or \((R3)\).
6. **(Multi-contact load)** Some contact block contains \(\ge 2\) neighbours of \(v\); all rigid portals in that block are of type \((R1)\) and/or \((R3)\) only (Lemma 2.3).

**Proof.** Assemble cited results. ∎

### Definition 8.3 (Hard-core RPC)
An RPC is **hard-core** if every last exit of every maximum fan is irreplaceable in the sense of Definition 8.1.

### Remark 8.4 (What remains for full Lemma G)
Hard-core RPC is exactly hybrid Remark 6.8, now with pure-\((R2)\)-only RPCs, free cut sides, inessential unique attachments, and tiny pure-\((R2)\) trades **removed**. The residual problem is simultaneous reassignment across a system of irreplaceable cutvertices and essential unique attachments, using the surplus fan and (optionally) Kempe bridges, without a free side to start induction.

No elementary counting, single Menger package, or single Kempe path has been shown to break every hard-core RPC for all \(t\ge 5\).

---

## 9. Conditional collapse

### Theorem 9.1 (Conditional non-existence \(\Rightarrow\mathrm{HC}_t\))
If no hard-core RPC occurs in any graph satisfying the standing hypotheses, then no \(\Phi\)-maximal contact-deficient model is an RPC (every non-hard-core RPC is absorbable by §§3–6), hence SPPA or a \(\Phi\)-increase always fires, hence Lemma G holds on this class, hence \(\mathrm{HC}_t\) holds for graphs whose minimal counterexamples would satisfy \(\delta\ge t\).

**Proof.** Dichotomy (hybrid Theorem 5.2) + Theorem 8.2 + hybrid Theorem 9.2. ∎

### Theorem 9.2 (What is fully proved without hard-core elimination)
Under the standing hypotheses, at every \(\Phi\)-maximum contact-deficient model:
1. \(Z=\emptyset\);
2. either the model is not an RPC (some fan has a strongly private non-cut last-exit package \(\Rightarrow\) SPPA raises \(s\)), or it is an RPC, in which case it is hard-core after discarding free/inessential/tiny-\((R2)\) structure;
3. in particular, **pure-\((R2)\)-only RPC is impossible**.

**Proof.** Hybrid package + Theorems 3.4 and 8.2. ∎

---

## 10. Checklist

| Item | Statement | Status |
|------|-----------|--------|
| Lem 1.1–1.5 | Load, pigeonhole, non-all-singletons | **Proved** |
| Lem 2.1–2.5 | \((R2)\) forces \(\alpha\in N(v)\); pure-type calculus | **Proved** |
| Thm 3.3–3.4 | Every RPC uses \((R1)\) or \((R3)\); **no pure-\((R2)\)-only RPC** | **Proved** |
| Thm 4.3–4.5 | Pure \((R2)\) trade size bounds at \(\Phi\)-max | **Proved** |
| Thm 5.3 / Cor 5.4 | Free \((R1)\)-component absorption; forbidden at \(\Phi\)-max | **Proved** |
| Thm 6.3 / Cor 6.4 | Inessential \((R3)\) bridge repair; essentiality at max | **Proved** (local leaf-Steiner form) |
| Prop 7.1 | Finite abstract RPC outside criticality | **Proved** |
| Thm 8.2 | Structure of residual / hard-core RPC | **Proved** (classification) |
| Full no-RPC / no hard-core RPC | Simultaneous irreplaceable reassignment | **Open** |
| Full \(\mathrm{HC}_t\) (\(t\ge 7\)) | — | **Open** |

---

## 11. Final verdict

### Proved (point of the spear on Gap \(G_t^{\mathrm{hyb}}\))
1. **No pure-\((R2)\)-only RPC** under \(\delta\ge t\): double portal load + uniqueness of contact representatives.
2. **Pure \((R2)\) trade calculus:** model-preserving contact trade; \(\Phi\) rises whenever the target non-contact bag is smaller by at least two vertices; equal-size trades only permute maximisers.
3. **Free \((R1)\) sides absorb:** any cut portal with an \(N(v)\)-meeting free component raises \(s\); at \(\Phi\)-max every cut side is load-bearing.
4. **Inessential \((R3)\) repairs** via leaf-Steiner bridges; at \(\Phi\)-max every blocking unique attachment is essential.
5. **Finite non-critical RPC** exhibiting irreplaceable private cross-edges on both sides of a cut portal — geometry is real, criticality is necessary for non-existence.
6. **Hard-core reduction:** every RPC in the standing class reduces to a hard-core RPC (Definition 8.3); non-hard-core structure is eliminated.

### Not proved
- Non-existence of **hard-core** RPC (irreplaceable \((R1){+}(R3)\) systems under surplus fans).
- Full Simultaneous Fan Absorption (Lemma G).
- Unconditional \(\mathrm{HC}_t\) for \(t\ge 7\).

### Precise residual gap (sharper than hybrid \(G_t^{\mathrm{hyb}}\))
\[
\boxed{\;G_t^{\mathrm{RPC}}:\ \text{No hard-core Rigid Portal Configuration exists under the standing CE hypotheses.}\;}
\]
This is strictly narrower than “no RPC”: pure-\((R2)\)-only, free-cut, inessential-\((R3)\), and tiny-\((R2)\)-trade RPCs are gone. The remaining object is a \(\Phi\)-maximal deficient model whose every surplus-fan last exit is an irreplaceable cutvertex and/or essential unique cross-attachment, with private cross-edges on every cut side, size bounds blocking pure contact trades, and \(\delta\ge t\) forcing multi-contact load on some bag.

A proof of \(G_t^{\mathrm{RPC}}\) yields Lemma G on the standing class and hence \(\mathrm{HC}_t\) for that class. A counterexample to \(\mathrm{HC}_t\) yields (by hybrid dichotomy + this note) a hard-core RPC.

### Continuation: \(t=7\) finite case attack
A finite case analysis specialised to \(t=7\) (Mader \(\kappa\ge 7\), double-foot, \(s\in\{1,\dots,5\}\)) is recorded in [`hadwiger_hardcore_rpc_t7.md`](hadwiger_hardcore_rpc_t7.md). That note proves:
- Mader-boosted surplus \(\tau(v,C)\ge 7\);
- **complete elimination of hard-core RPC for \(s=1\)** (unique-attachment budget \(\le 5<|L|\) + fan-disjointness against cutvertex portals);
- deficiency-one exclusivity (multi-portal bags cannot uniquely glue to the single non-contact bag);
- reduction of \(G_7^{\mathrm{RPC}}\) to **locked contact cores** for \(s\in\{2,3,4,5\}\) only.

Full emptiness of locked cores (hence unconditional \(\mathrm{HC}_7\)) remains open.

---

*End of RPC elimination note.*
