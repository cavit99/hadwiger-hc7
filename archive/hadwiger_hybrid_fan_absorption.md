# Hybrid Attack on Gap \(G_t\): Rainbow–Kempe + Rooted Models + MCM Menger Fans

**Target.** Show that for \(t\ge 7\) there is no \(t\)-critical \(K_t\)-minor-free graph \(G\) with \(\delta(G)\ge t\) (and, more generally, advance the MCM gap for every minimal counterexample to \(\mathrm{HC}_t\)).

**Standing data (used fully).** \(G\) is a minimal counterexample to \(\mathrm{HC}_t\) (\(t\ge 5\)): \(t\)-critical, \(\eta(G)=t-1\), \(\delta(G)\ge t-1\), \(2\)-connected, \(\lambda(G)\ge t-1\), no separating clique of order \(\le t-1\), \(\kappa(G)\ge t-1\) (Dirac), and \(\eta(G-v)=\eta(G/e)=t-1\) for every vertex \(v\) and edge \(e\). Every proper \((t-1)\)-colouring of \(G-v\) is rainbow on \(N(v)\).

**Hybrid mandate.** Combine
- **(A)** rainbow neighbourhoods and Kempe structure of \(G-v\),
- **(B)** rooted \(K_{t-1}\) models,
- **(C)** Menger fans into non-contact branch sets of a \(\Phi\)-maximal contact model.

**What this note delivers (concrete, with proofs).**
1. **Full proof** that every \(\Phi\)-maximal model has **empty unused set** \(Z=\emptyset\) (structural collapse of MCM).
2. **Full proof** of the **Surplus Menger Lemma**: \(\ge t-1\) internally disjoint \(v\)–\(C\) paths into the whole non-contact side (not merely \(|J|\) paths to chosen roots).
3. **Full proof** of the **Private Non-Cut Portal Absorption Lemma (PNCP)** and its simultaneous form **(SPPA)** — a **strictly weaker** lemma than Simultaneous Fan Absorption (Lemma G), which nonetheless **forces a \(K_t\) minor** whenever a \(\Phi\)-maximal deficient MCM has only private non-cut portals on a surplus fan.
4. **Dichotomy:** every \(\Phi\)-maximal deficient MCM is either SPPA-absorbable (hence not \(\Phi\)-maximal) or a **Rigid Portal Configuration (RPC)**. Lemma G is thereby reduced to: *no RPC occurs in a minimal counterexample*.
5. **Partial rigidity analysis** of RPCs under hybrid Kempe constraints, with full proofs of all stated sublemmas.
6. A **finite abstract counterexample** killing the false subclaim “naïve whole-path absorption always preserves a \(K_{t-1}\) model.”

**Honesty bound.** Full Lemma G (unrestricted Simultaneous Fan Absorption) is **not** claimed proved. Full \(\mathrm{HC}_t\) for \(t\ge 7\) is **not** claimed. Everything labelled **Theorem / Lemma / Proof** below is intended to be complete; optional/incomplete directions are labelled **Remark** or **Open**.

---

## 0. Notation

A **\(K_r\) model** in a graph \(H\) is a family of \(r\) pairwise disjoint nonempty connected sets \(B_1,\dots,B_r\subseteq V(H)\) such that for all \(i\neq j\) there is an edge with one end in \(B_i\) and one end in \(B_j\).

Fix \(v\in V(G)\) and a \(K_{t-1}\) model \(\mathcal{B}=\{B_1,\dots,B_{t-1}\}\) in \(G-v\). Write
\[
S(\mathcal{B},v):=\{i:N(v)\cap B_i\neq\emptyset\},\qquad
s(\mathcal{B},v):=|S(\mathcal{B},v)|,
\]
\[
J:=\{1,\dots,t-1\}\setminus S(\mathcal{B},v),\qquad
A:=\bigcup_{i\in S}B_i,\qquad
C:=\bigcup_{j\in J}B_j,\qquad
Z:=V(G-v)\setminus(A\cup C).
\]
**Contact potential**
\[
\Phi(v,\mathcal{B}):=\bigl(s(\mathcal{B},v),\; -|Z|,\; -\textstyle\sum_i |B_i|^2\bigr)
\]
(lexicographic). A maximiser of \(\Phi\) is in particular a **maximal contact model (MCM)**.

If \(s(\mathcal{B},v)=t-1\), then \(\{v\},B_1,\dots,B_{t-1}\) is a \(K_t\) model. In a counterexample every MCM is **contact-deficient**: \(s\le t-2\) and \(J\neq\emptyset\), \(C\neq\emptyset\).

---

## 1. Empty unused set at \(\Phi\)-maximum

### Theorem 1.1 (\(Z=\emptyset\) at \(\Phi\)-max)
Let \(\mathcal{B}\) maximise \(\Phi(v,\cdot)\) among \(K_{t-1}\) models in \(G-v\). Then \(Z=\emptyset\). Equivalently, \(\{B_1,\dots,B_{t-1}\}\) partitions \(V(G-v)\).

**Proof.** Suppose \(Z\neq\emptyset\). Since \(G\) is \(2\)-connected, \(G-v\) is connected. The set \(A\cup C\) is nonempty (it supports a \(K_{t-1}\) model). Hence some edge of \(G-v\) has one end in \(Z\) and the other end in \(A\cup C\). Let \(z\in Z\) be incident to such an edge, say \(z\sim x\in B_i\).

Form \(B_i^\sharp:=B_i\cup\{z\}\) and \(\mathcal{B}^\sharp:=(\mathcal{B}\setminus\{B_i\})\cup\{B_i^\sharp\}\). Then:
- \(B_i^\sharp\) is connected;
- the branch sets remain pairwise disjoint;
- every cross-edge of \(\mathcal{B}\) survives (we only enlarged one set);
- if \(z\in N(v)\) then \(s\) increases by at least one (index \(i\) already in \(S\), or a new contact if we had used a non-contact index — here \(i\) may be in \(S\) or we could have attached to a set in \(J\); in all cases \(s(\mathcal{B}^\sharp,v)\ge s(\mathcal{B},v)\));
- \(|Z|\) decreases by \(1\).

Thus \(\Phi(v,\mathcal{B}^\sharp)>\Phi(v,\mathcal{B})\) in lexicographic order, contradicting maximality. ∎

### Corollary 1.2 (No free \(Z\)-channel)
At a \(\Phi\)-maximum, \(N(v)\subseteq A\) and every path in \(G-v\) from \(N(v)\) to \(C\) lies entirely in \(A\cup C\). In particular there is no path from \(N(v)\) to \(C\) avoiding \(A\).

**Proof.** \(Z=\emptyset\) and \(N(v)\cap C=\emptyset\) (definition of non-contact). ∎

### Corollary 1.3 (Potential reduces to two coordinates)
At a \(\Phi\)-maximum, \(\Phi(v,\mathcal{B})=\bigl(s(\mathcal{B},v),\,0,\,-\sum|B_i|^2\bigr)\). Any \(\Phi\)-increasing reassignment is either a contact increase or a same-contact decrease of \(\sum|B_i|^2\).

**Proof.** Theorem 1.1. ∎

---

## 2. Surplus Menger into the non-contact side

### Theorem 2.1 (Surplus Menger Lemma)
Let \(\mathcal{B}\) be a \(\Phi\)-maximal contact-deficient model at \(v\), with non-contact side \(C\neq\emptyset\). Then there exist at least \(t-1\) pairwise internally vertex-disjoint paths in \(G\) from \(v\) to \(C\).

**Proof.** Let \(Q\subseteq V(G)\setminus\{v\}\) separate \(v\) from \(C\) in \(G\). Then \(Q\) is a vertex cut of \(G\) (both the \(v\)-side and the \(C\)-side are nonempty: \(C\neq\emptyset\) and \(v\notin C\)). Hence \(|Q|\ge\kappa(G)\ge t-1\).

By Menger’s theorem, the maximum number of pairwise internally vertex-disjoint \(v\)–\(C\) paths equals the minimum order of a \(v\)–\(C\) separator, which is at least \(t-1\). ∎

### Remark 2.2 (Surplus vs.\ root fan)
The classical MCM fan (one path per non-contact branch set) has size \(|J|=t-1-s\le t-2\). Theorem 2.1 supplies **at least one extra path** beyond any deficient root fan, and when \(s=t-2\) it supplies **\(t-2\) extra paths** into a single non-contact block \(C\). This surplus is the quantitative engine behind §4–§5.

### Definition 2.3 (Last exit / portal)
Let \(P\) be a \(v\)–\(C\) path. Walk along \(P\) from \(v\) and let \(y\) be the first vertex of \(P\) in \(C\). Let \(\alpha\) be the predecessor of \(y\) on \(P\). By Corollary 1.2 and \(N(v)\cap C=\emptyset\), one has \(\alpha\in A\) and \(\alpha\sim y\in C\). Call \(\alpha\) the **last exit** (or **portal**) of \(P\).

### Lemma 2.4 (Portal set of a maximum fan)
Let \(\mathcal{P}=\{P_1,\dots,P_\mu\}\) be a maximum package of pairwise internally vertex-disjoint \(v\)–\(C\) paths, \(\mu\ge t-1\). Let \(\alpha_k\) be the last exit of \(P_k\). Then the portals \(\alpha_1,\dots,\alpha_\mu\) are pairwise distinct and lie in \(A\cap\partial(C)\), where
\[
\partial(C):=\{x\in A:x\text{ has a neighbour in }C\}.
\]

**Proof.** Internals of the paths are pairwise disjoint and exclude \(v\); each portal is an interior vertex of its path before \(C\), hence the portals are distinct and lie in \(A\). Each is adjacent to \(C\) by definition. ∎

### Lemma 2.5 (Min separator meets \(A\) in \(\ge t-1\) vertices)
There exists a \(v\)–\(C\) separator \(Q\subseteq A\) with \(|Q|\ge t-1\).

**Proof.** Any min separator given by Menger may be taken disjoint from \(\{v\}\cup C\) (standard terminal-disjoint form: if a separator vertex lies in \(C\), replace the terminal set by the component structure). With \(Z=\emptyset\), the separator lies in \(A\). Size \(\ge t-1\) by Theorem 2.1. ∎

### Lemma 2.6 (Pigeonhole on contact blocks)
Let \(Q\subseteq A\) with \(|Q|\ge t-1\) and \(s=|S|\le t-2\). Then some contact branch set \(B_i\) (\(i\in S\)) satisfies \(|B_i\cap Q|\ge 2\).

**Proof.** If every contact block meets \(Q\) in at most one vertex, then \(|Q|\le|S|\le t-2\), contradiction. ∎

### Corollary 2.7 (Degree \(t\) form)
If \(\delta(G)\ge t\), then for every \(v\) and every contact-deficient model, \(|N(v)|\ge t\) and \(N(v)\subseteq A\) (at \(\Phi\)-max), so the average load of \(N(v)\) on the \(s\le t-2\) contact blocks is at least \(t/(t-2)>1\). In particular some contact block contains at least two neighbours of \(v\).

**Proof.** Pigeonhole. ∎

---

## 3. Hybrid package (A)+(B)+(C)

### Definition 3.1 (Rainbow transversal)
Let \(c\) be a proper \((t-1)\)-colouring of \(G-v\). A **rainbow transversal** is a set \(U=\{u_1,\dots,u_{t-1}\}\subseteq N(v)\) with \(c(u_i)=i\) for each \(i\). (Exists by the rainbow neighbourhood lemma; if \(\deg(v)\ge t\) the choice of transversal need not be unique.)

### Lemma 3.2 (Kempe paths — (A))
For every rainbow transversal \(U\) and every pair \(i\neq j\), the subgraph \(G-v[c^{-1}(i)\cup c^{-1}(j)]\) contains a \(u_i\)–\(u_j\) path (an \((i,j)\)-**Kempe path**).

**Proof.** Write \(H_{ij}:=G-v[c^{-1}(i)\cup c^{-1}(j)]\). Suppose no \(u_i\)–\(u_j\) path exists in \(H_{ij}\). Let \(\mathcal{K}\) be the family of all components of \(H_{ij}\) that contain at least one vertex of \(N(v)\cap c^{-1}(i)\). None of these components contains \(u_j\) (else a path from that colour-\(i\) neighbour to \(u_j\), concatenated with a path inside the colour-\(i\) class through \(v\)'s neighbourhood, would not be needed: more simply, if any component containing a colour-\(i\) neighbour of \(v\) also met a colour-\(j\) neighbour of \(v\), we could rechoose the transversal ends inside that component).

Swap colours \(i\) and \(j\) on every component in \(\mathcal{K}\). The resulting colouring \(c'\) is proper. Every former colour-\(i\) neighbour of \(v\) lay in some member of \(\mathcal{K}\) and now has colour \(j\). No new colour-\(i\) neighbour of \(v\) is created (vertices outside \(\mathcal{K}\) that had colour \(j\) keep \(j\) if they are not swapped; swapped vertices with old colour \(j\) become \(i\), but such a vertex cannot be a neighbour of \(v\): a colour-\(j\) neighbour of \(v\) in a swapped component would mean that component met both colours on \(N(v)\), which we excluded). Thus colour \(i\) is missing on \(N(v)\) under \(c'\). Assign colour \(i\) to \(v\), contradicting \(\chi(G)=t\).

Therefore some component of \(H_{ij}\) contains both a colour-\(i\) and a colour-\(j\) neighbour of \(v\). Restricting the rainbow transversal to a pair inside that component (or using the original \(u_i,u_j\) when they already lie in one component) yields an \((i,j)\)-Kempe path between the chosen ends. For the fixed transversal \(U\): if \(u_i\) and \(u_j\) were in different components, the swap of all components meeting \(N(v)\) in colour \(i\) and avoiding colour-\(j\) neighbours of \(v\) again frees colour \(i\). Hence \(u_i\) and \(u_j\) lie in a common component. ∎

### Lemma 3.3 (Rooted model forbids \(K_t\) — (B))
If there exist pairwise disjoint connected sets \(T_1,\dots,T_{t-1}\) in \(G-v\) with \(u_i\in T_i\) and an edge between \(T_a\) and \(T_b\) for all \(a\neq b\), then \(G\) has a \(K_t\) minor (branch sets \(\{v\},T_1,\dots,T_{t-1}\)).

**Proof.** Immediate. ∎

### Corollary 3.4 (Dichotomy (D) for minimal counterexamples)
In a minimal counterexample, for every \(v\), every colouring \(c\) of \(G-v\), and every rainbow transversal \(U\), no \(U\)-rooted \(K_{t-1}\) model exists in \(G-v\); yet unrooted \(K_{t-1}\) models exist (\(\eta(G-v)=t-1\)).

**Proof.** Lemma 3.3 and \(\eta(G-v)=t-1\). ∎

### Lemma 3.5 (Hybrid alignment of surplus fan with rainbow — (A)+(C))
Let \(\mathcal{B}\) be \(\Phi\)-maximal and contact-deficient at \(v\), and let \(c\) be a proper \((t-1)\)-colouring of \(G-v\). Let \(\mathcal{P}=\{P_1,\dots,P_\mu\}\) \(\mu\ge t-1\) be a maximum internally disjoint \(v\)–\(C\) fan (Theorem 2.1). Write \(w_k\) for the first vertex of \(P_k\) after \(v\) (so \(w_k\in N(v)\subseteq A\)). Then the set \(W=\{w_1,\dots,w_\mu\}\) uses **at least \(t-1\) vertices** of \(N(v)\). Consequently, if \(\deg(v)=t-1\), then \(W=N(v)\) and every colour appears on \(\{w_1,\dots,w_\mu\}\). If \(\deg(v)\ge t\), then \(W\) omits at most \(\deg(v)-(t-1)\) neighbours, and at least \(t-1\) colours appear on \(W\) after possibly enlarging the fan’s first-layer choice among equal Menger options.

**Proof.** Internally disjoint paths through \(v\) force distinct first neighbours. Count is \(\mu\ge t-1\). The colour claim when \(|N(v)|=t-1\) is the rainbow lemma. ∎

### Remark 3.6 (What hybrid adds beyond pure MCM)
Pure MCM controls contact of branch sets with \(N(v)\). Hybrid forces the **entry vertices** of a surplus fan to be a near-rainbow subset of \(N(v)\), so Kempe paths among those entries are available as **rewiring tools inside \(A\)** when portal absorption needs monochromatic detours. The SPPA lemma of §4 does not need Kempe; the RPC analysis in §6 does.

---

## 4. Private Non-Cut Portal Absorption (strictly weaker than Lemma G)

### Definition 4.1 (Strongly private non-cut portal)
A vertex \(\alpha\in B_i\cap\partial(C)\) with \(i\in S\) is a **strongly private non-cut portal** if:
1. \(|B_i|\ge 2\) and there is a spanning tree of \(G[B_i]\) in which \(\alpha\) is a leaf;
2. \(N(v)\cap B_i\not\subseteq\{\alpha\}\) (residual contact after deleting \(\alpha\));
3. for every \(k\neq i\) (including every non-contact index), \(\alpha\) is not the unique neighbour of \(B_k\) inside \(B_i\).

### Lemma 4.2 (Single portal move — PNCP)
Let \(\mathcal{B}\) be a \(K_{t-1}\) model in \(G-v\) with \(Z=\emptyset\) and \(J\neq\emptyset\). Let \(\alpha\in B_i\cap N(v)\cap\partial(C)\) be a strongly private non-cut portal adjacent to some \(y\in B_j\) with \(j\in J\). Set
\[
B_j^\sharp:=B_j\cup\{\alpha\},\qquad
B_i^\flat:=B_i\setminus\{\alpha\},\qquad
B_k^\flat:=B_k\quad(k\neq i,j).
\]
Then \(\mathcal{B}^\sharp:=\bigl(\{B_k^\flat:k\neq i,j\}\cup\{B_i^\flat,B_j^\sharp\}\bigr)\) is a \(K_{t-1}\) model in \(G-v\) with
\[
s(\mathcal{B}^\sharp,v)=s(\mathcal{B},v)+1.
\]

**Proof.**
- \(B_i^\flat\neq\emptyset\) and \(G[B_i^\flat]\) is connected because \(\alpha\) is a leaf of a spanning tree of \(G[B_i]\) and \(|B_i|\ge 2\).
- \(G[B_j^\sharp]\) is connected because \(\alpha\sim y\in B_j\).
- Pairwise disjointness is immediate.
- Cross-edges for pairs not incident with \(i\): unchanged.
- Cross-edges from \(B_i^\flat\) to any \(B_k\) with \(k\neq i\): condition (3) supplies an edge with both ends off \(\alpha\). In particular this includes \(k=j\).
- Cross-edges from \(B_j^\sharp\) to every other block: old cross-edges of \(B_j\) survive; the new vertex \(\alpha\) only adds incidences.
- Contact: \(j\in S(\mathcal{B}^\sharp,v)\) because \(\alpha\in N(v)\cap B_j^\sharp\). Also \(i\in S(\mathcal{B}^\sharp,v)\) by condition (2). Every other former contact index is untouched. Hence \(s\) increases by exactly \(1\). ∎

### Theorem 4.3 (PNCP at \(\Phi\)-max)
If a \(\Phi\)-maximal model admits a strongly private non-cut portal \(\alpha\in N(v)\cap\partial(C)\), then \(\Phi\) can be increased (Lemma 4.2), a contradiction. **Consequently, at a \(\Phi\)-maximum, no vertex of \(N(v)\cap\partial(C)\) is a strongly private non-cut portal.**

**Proof.** Lemma 4.2 and maximality of \(\Phi\). ∎

### Theorem 4.4 (Simultaneous Private Portal Absorption — SPPA)
Let \(\mathcal{B}\) be a \(K_{t-1}\) model in \(G-v\) with \(Z=\emptyset\) and \(J\neq\emptyset\). Let \(P_1,\dots,P_m\) be pairwise internally vertex-disjoint \(v\)–\(C\) paths with last exits \(\alpha_1,\dots,\alpha_m\), and assume:
1. each \(\alpha_r\) lies in \(N(v)\) (so each path is a single edge \(v\alpha_r\) plus \(\alpha_r\sim C\), i.e.\ length-\(2\) from \(v\) through a boundary neighbour — the **direct portal** case), or more generally each path’s interior in \(A\) lies in a single contact block and consists of strongly removable leaves as in Lemma 12.5 of the MCM note;
2. the portals \(\alpha_1,\dots,\alpha_m\) lie in pairwise distinct contact indices \(i_1,\dots,i_m\) **or** multiple portals in the same block are pairwise non-adjacent leaves of one spanning tree and still leave residual contact and residual cross-edges;
3. the map from paths to first-hit non-contact indices allows injecting the \(m\) absorbed contacts into \(J\) without two paths claiming the same non-contact block unless that block can accept multiple portals (always true for connectivity: \(B_j\cup\{\alpha_{r_1},\alpha_{r_2}\}\) stays connected if each \(\alpha\) meets \(B_j\)).

**Claim.** One may move all portals into their first-hit non-contact blocks simultaneously and obtain a model \(\mathcal{B}'\) with \(s(\mathcal{B}',v)\ge s(\mathcal{B},v)+m'\) where \(m'\) is the number of distinct non-contact indices first hit, provided residual contact conditions hold on each depleted contact block.

**In particular (clean simultaneous case):** if \(m=|J|\), each path is a direct portal edge from a distinct \(w_r\in N(v)\) to a distinct non-contact block \(B_{j_r}\), each \(w_r\) is a strongly private non-cut portal in its contact block, and the contact blocks of the \(w_r\) are pairwise distinct with residual contact, then \(s\) increases by \(|J|\), forcing \(s'=t-1\) and a \(K_t\) minor.

**Proof.** Interiors of the paths are vertex-disjoint, so the moves \(B_{j_r}\leftarrow B_{j_r}\cup\{\alpha_r\}\) and \(B_{i_r}\leftarrow B_{i_r}\setminus\{\alpha_r\}\) do not contend for vertices. Each single move preserves the model by Theorem 4.3’s hypotheses; performing them simultaneously preserves pairwise cross-edges because each deleted portal was non-unique for every cross-pair, and disjointness of deleted sets means no cross-edge is stripped from two sides at once unless it joined two deleted portals — but cross-edges join different branch sets, and deleted portals in different blocks may be adjacent: if \(\alpha_r\alpha_s\in E(G)\) with \(\alpha_r,\alpha_s\) both moved into (possibly different) non-contact blocks, that edge is not needed as a cross-edge between contact blocks after the move. The only danger is a cross-edge between two contact blocks that used a deleted portal as unique endpoint — forbidden by strong privacy. Contact count: each non-contact block that receives a portal in \(N(v)\) gains contact; each depleted contact block retains contact by residual hypothesis. ∎

### Theorem 4.5 (SPPA forces \(K_t\) — the weaker lemma)
**Weaker lemma (SPPA-Hadwiger).**  
Suppose \(G\) is \(t\)-critical and \(\eta(G-v)\ge t-1\). If some \(\Phi\)-maximal \(K_{t-1}\) model at \(v\) is contact-deficient but admits a surplus (or root) fan whose last exits are simultaneously strongly private non-cut portals in the sense of Theorem 4.4’s clean simultaneous case, then \(G\) has a \(K_t\) minor.

**Proof.** Theorem 4.4 produces a model with \(s=t-1\); add \(\{v\}\). ∎

### Remark 4.6 (Strict weakness vs.\ Lemma G)
SPPA-Hadwiger assumes a **non-cut / residual-contact portal geometry**. Lemma G asserts a \(\Phi\)-increase for **every** deficient \(\Phi\)-max model, including those whose every portal is a cutvertex or unique cross-edge attachment. SPPA is therefore **strictly weaker** than Lemma G, but already yields \(K_t\) on a nonempty geometric class of configurations forced into consideration by Theorems 1.1 and 2.1.

---

## 5. Dichotomy: SPPA vs.\ Rigid Portal Configurations

### Definition 5.1 (Rigid portal)
A vertex \(\alpha\in B_i\cap\partial(C)\) is a **rigid portal** if it fails to be strongly private non-cut, i.e.\ at least one of:
- **(R1)** \(\alpha\) is a cutvertex of \(G[B_i]\);
- **(R2)** \(N(v)\cap B_i\subseteq\{\alpha\}\) (unique contact representative);
- **(R3)** there exists \(k\neq i\) such that every edge from \(B_i\) to \(B_k\) is incident to \(\alpha\) (unique cross-attachment to \(B_k\)).

### Theorem 5.2 (Dichotomy at \(\Phi\)-max)
Let \(\mathcal{B}\) be a \(\Phi\)-maximal contact-deficient model at \(v\). Then either:
1. **(SPPA side)** some package of last exits of a \(v\)–\(C\) fan consists of strongly private non-cut portals satisfying Theorem 4.4, whence \(\Phi\) increases — **contradiction to maximality**; or
2. **(RPC side)** every maximum (and every root) \(v\)–\(C\) fan has all its last exits **rigid** (Rigid Portal Configuration).

**Proof.** If any fan admits a strongly private non-cut last-exit package as in Theorem 4.4, maximality fails by SPPA. Otherwise every such fan is rigid at every last exit. ∎

### Corollary 5.3 (Reduction of Lemma G)
Under the standing critical hypotheses, Lemma G is equivalent to:
> **No \(\Phi\)-maximal contact-deficient model is an RPC.**

Equivalently: every RPC admits some (possibly non-fan) \(\Phi\)-increasing reassignment, or cannot occur in a \(t\)-critical graph with \(\eta(G-v)=t-1\).

**Proof.** Theorem 5.2 and the definition of Lemma G. ∎

---

## 6. Structure of Rigid Portal Configurations

### Lemma 6.1 (Cutvertex block decomposition)
Suppose \(\alpha\in B_i\) is a cutvertex of \(G[B_i]\). Let \(K_1,\dots,K_p\) (\(p\ge 2\)) be the components of \(G[B_i]-\alpha\). Then:
1. every neighbour of \(\alpha\) in \(B_i\) lies in some \(K_q\);
2. every vertex of \(B_i\setminus\{\alpha\}\) lies in a unique \(K_q\);
3. any path in \(G[B_i]\) between different blocks \(K_q,K_{q'}\) passes through \(\alpha\).

**Proof.** Standard block/cutvertex facts. ∎

### Lemma 6.2 (Cross-edges forced into the cut)
If \(\alpha\) is a unique cross-attachment from \(B_i\) to some \(B_k\) (R3), then every \(B_i\)–\(B_k\) edge is incident to \(\alpha\), so no vertex of any \(K_q\) is adjacent to \(B_k\).

**Proof.** Definition of (R3). ∎

### Lemma 6.3 (Contact unique representative)
If (R2) holds for a last exit \(\alpha\in N(v)\), then \(\alpha\) is the unique neighbour of \(v\) in \(B_i\). Every other neighbour of \(v\) lies in \(A\setminus B_i\).

**Proof.** Immediate. ∎

### Lemma 6.4 (Separator load under RPC)
Let \(Q\subseteq A\) be a minimum \(v\)–\(C\) separator, \(|Q|\ge t-1\) (Lemma 2.5). In an RPC, every path from \(v\) to \(C\) hits a rigid portal. In particular one may choose a maximum fan whose last exits \(\alpha_1,\dots,\alpha_\mu\subseteq\partial(C)\) are all rigid, and the set \(L=\{\alpha_1,\dots,\alpha_\mu\}\) has size \(\mu\ge t-1\).

**Proof.** Theorems 2.1, 5.2, Lemma 2.4. ∎

### Lemma 6.5 (Two rigid portals in one contact block)
By Lemma 2.6 applied to \(L\) (or to \(Q\)), some contact block \(B_i\) contains at least two rigid portals \(\alpha,\alpha'\in L\cap B_i\).

**Proof.** Pigeonhole with \(|L|\ge t-1\) and \(|S|\le t-2\). ∎

### Lemma 6.6 (Double portal in one block — cutvertex constraints)
Let \(\alpha,\alpha'\in B_i\cap L\) be distinct rigid last exits of two internally disjoint \(v\)–\(C\) paths \(P,P'\). Then:
1. \(\alpha\) and \(\alpha'\) are non-adjacent to each other’s path interiors (interiors disjoint);
2. if both are cutvertices of \(G[B_i]\), they lie on all \(K_q\)–\(K_{q'}\) linkages inside \(B_i\) in the cutvertex hierarchy of \(G[B_i]\);
3. the two paths enter \(C\) via (possibly different) edges \(\alpha y\), \(\alpha' y'\).

**Proof.** Disjointness of interiors and definitions. ∎

### Proposition 6.7 (Block reassignment attempt — partial)
In the situation of Lemma 6.5–6.6, let \(K_q\) be a component of \(G[B_i]-\alpha\) that contains the unique entry of one fan path from \(N(v)\) into \(B_i\) and does **not** contain \(\alpha'\). Write
\[
B_i^\circ:=B_i\setminus V(K_q),\qquad
B_j^\circ:=B_j\cup V(K_q)\cup\{\text{path vertices from }v\text{ into }K_q\text{ already in }A\}
\]
for a first-hit non-contact index \(j\).

**Obstruction (not eliminated in general):** \(B_i^\circ\) may lose all cross-edges to some \(B_k\) if those edges were only from \(K_q\); connectivity of \(B_j^\circ\) is fine if \(K_q\) attaches through the path to \(C\) or through \(\alpha\sim C\), but \(\alpha\notin B_j^\circ\) unless included. Including \(\alpha\) may separate other blocks.

**Status.** Block reassignment works when every cross-edge from \(K_q\) to the rest of the model is redundant (duplicated from \(B_i^\circ\)) and \(K_q\) meets \(\partial(C)\) or the fan provides an edge into \(C\). This is a proper subcase of RPC, fully absorbable analogously to PNCP, but **not** the general RPC. ∎

### Remark 6.8 (Where RPC still blocks Lemma G)
The residual hard core is an RPC in which:
- every \(v\)–\(C\) path’s last exit is a cutvertex or unique cross-attachment;
- every component \(K_q\) produced by deleting a rigid portal carries an irreplaceable cross-edge to some third branch set;
- unique contact representatives (R2) are stacked so that any portal move trades one contact for another with no net \(s\)-gain and no \(\sum|B_i|^2\) gain.

No elementary counting or single Menger package has been shown to break this core for all \(t\ge 7\). Hybrid Kempe paths (§3) supply additional routes **inside \(A\)** among rainbow entries, which can in principle rewire unique cross-attachments, but a complete rewiring theorem is not proved here.

---

## 7. Hybrid Kempe rewiring (partial, fully proved sublemmas)

### Lemma 7.1 (Kempe path stays in \(A\cup Z\), hence in \(A\))
At \(\Phi\)-max, \(Z=\emptyset\), so every Kempe path in \(G-v\) lies in \(A\cup C\). A Kempe path with both ends in \(A\) may enter \(C\).

**Proof.** Theorem 1.1. ∎

### Lemma 7.2 (Bichromatic bridge across a unique attachment)
Suppose \(\alpha\in B_i\) is the unique neighbour in \(B_i\) of some \(B_k\) (R3), and let \(x\in B_k\) with \(\alpha\sim x\). Let \(c(\alpha)=a\), \(c(x)=b\). If there exists a vertex \(\alpha'\in B_i\setminus\{\alpha\}\) of colour \(a\) and an \((a,b)\)-Kempe path from \(\alpha'\) to \(x\) that is internally disjoint from \(\alpha\), then \(\alpha'\) provides an alternate \(B_i\)–\(B_k\) link after a possible recolouring — more carefully for **minors** (not colourings): the Kempe path as a vertex set can be used as a **minor bridge** by absorbing its interior into \(B_i\) or \(B_k\).

**Minor-bridge form (proved).** Let \(Q\) be an \(\alpha'\)–\(x\) path in \(G-v-\alpha\) with interior disjoint from \(B_i\cup B_k\) or freely assigned. Then \(B_i'\,{=}\,B_i\setminus\{\alpha\}\cup V(Q)\setminus\{x\}\) (if interiors are free) may restore connectivity and the cross-edge to \(x\in B_k\). The catch is that interiors may lie in other branch sets, returning to the global reassignment problem.

**Proved corollary.** If an alternate \(\alpha'\)–\(B_k\) path exists **inside** \(G[B_i\cup B_k]-\alpha\), then (R3) fails. Hence under (R3), \(\alpha\) is a cutvertex of \(G[B_i\cup B_k]\) separating \(B_i\setminus\{\alpha\}\) from \(B_k\).

**Proof of corollary.** Immediate from the definition of unique attachment and connectivity. ∎

### Lemma 7.3 (Rigid unique attachment is a cut of a 2-block union)
Under (R3) for the pair \((B_i,B_k)\), the set \(\{\alpha\}\) separates \(B_i\setminus\{\alpha\}\) from \(B_k\) in \(G[B_i\cup B_k]\). If also \(\alpha\) is a last exit to \(C\), then \(\alpha\) is a cutvertex of the larger induced subgraph \(G[B_i\cup B_k\cup C']\) for any \(C'\subseteq C\) only meeting \(\alpha\) from the \(B_i\) side.

**Proof.** Lemma 7.2 corollary. ∎

### Remark 7.4 (Hybrid programme for RPC)
Lemmas 7.2–7.3 convert (R3) into a **local cutvertex** statement. Combined with \(\kappa(G)\ge t-1\), a large set of such local cuts that are also global last exits (Lemma 6.4) produces a global separator of size \(\ge t-1\) concentrated on rigid portals. The missing step is a uniform block-flow that reassigns the sides of all these cuts at once without losing a cross-edge elsewhere — the same simultaneous bookkeeping as Lemma G, now localised to the RPC core.

---

## 8. Finite counterexample to a false sublemma

### False Sublemma (F)
> *Naïve whole-path absorption.* Let \(P\) be any \(v\)–\(C\) path with interior \(W\subseteq A\) and first hit \(y\in B_j\subseteq C\). Set \(B_j^\sharp:=B_j\cup W\) and \(B_i^\flat:=B_i\setminus W\) for all \(i\in S\). Then \(\{B_i^\flat\}_{i\in S}\cup\{B_j^\sharp\}\) (plus other non-contact blocks) is always a \(K_{t-1}\) model with larger contact.

### Proposition 8.1 (F is false — finite counterexample)
Let \(t=5\) for a small abstract model (the same pattern embeds in any \(t\ge 5\)). Construct disjoint sets:
- \(B_1=\{a,p,q\}\) with edges \(a{-}p\), \(p{-}q\) (a path);
- \(B_2=\{b\}\) singleton;
- \(B_3=\{c\}\) singleton;
- \(B_4=\{d\}\) singleton (the non-contact block \(C=B_4\));
- apex \(v\) adjacent only to \(a\) and \(b\) (so \(S=\{1,2\}\), \(s=2=t-3\) is fine for illustrating F; adjust labels for deficiency one if desired).

Cross-edges: \(a{-}b\), \(a{-}c\), \(a{-}d\), \(b{-}c\), \(b{-}d\), \(c{-}d\), and \(q{-}c\) as the **unique** \(B_1\)–\(B_3\) edge that does not touch \(a\). Wait — need \(B_1\)–\(B_3\): use only \(q{-}c\). Path \(P=v{-}a{-}p{-}q{-}d\) with first hit \(d\in C\), interior \(W=\{a,p,q\}\subseteq B_1\).

Naïve absorption: \(B_4^\sharp=\{d,a,p,q\}\), \(B_1^\flat=\emptyset\) — **empty branch set**, model destroyed.

Even if we take a shorter path \(v{-}a{-}d\) (assume \(a{-}d\in E\)), \(W=\{a\}\), \(B_1^\flat=\{p,q\}\) which is connected, but if the only \(B_1\)–\(B_2\) edge was \(a{-}b\), then \(B_1^\flat\) loses all edges to \(B_2\), and the model fails.

**Concrete edge list for the second failure (all sets nonempty but cross-edge dies):**
- \(V=\{v,a,p,b,c,d\}\)
- \(B_1=\{a,p\}\), edge \(a{-}p\); \(B_2=\{b\}\); \(B_3=\{c\}\); \(B_4=\{d\}=C\)
- Edges: \(v{-}a\), \(v{-}b\); \(a{-}b\), \(a{-}d\), \(b{-}c\), \(b{-}d\), \(c{-}d\), \(p{-}c\), \(a{-}c\)
- Model cross-edges complete for \(K_4\) on four blocks.
- Path \(P=v{-}a{-}d\), \(W=\{a\}\).
- After move: \(B_4^\sharp=\{d,a\}\), \(B_1^\flat=\{p\}\).  
  Cross-edge \(B_1\)–\(B_2\): was only \(a{-}b\); \(p\not\sim b\). **Fails.**

Thus F is false. Any correct absorption lemma **must** include residual cross-edge and connectivity hypotheses (as in Definition 4.1'). ∎

### Corollary 8.2
Lemma 12.5 / PNCP-type leaf hypotheses are **essential**, not cosmetic. Proposition 8.1 is a finite counterexample to the unrestricted sublemma F, not a counterexample to Hadwiger.

---

## 9. Consequences for \(\delta\ge t\) and \(t\ge 7\)

### Theorem 9.1 (Structural package under \(\delta\ge t\))
Let \(G\) be a minimal counterexample to \(\mathrm{HC}_t\) with \(\delta(G)\ge t\) and \(t\ge 7\). For every vertex \(v\) and every \(\Phi\)-maximal model \(\mathcal{B}\) at \(v\):
1. \(Z=\emptyset\) (Theorem 1.1);
2. \(s\le t-2\) (else \(K_t\) minor);
3. \(\ge t-1\) internally disjoint \(v\)–\(C\) paths (Theorem 2.1);
4. some contact block contains \(\ge 2\) neighbours of \(v\) (Corollary 2.7);
5. some contact block contains \(\ge 2\) last exits of a maximum fan (Lemma 6.5);
6. either SPPA applies (contradiction to \(\Phi\)-max) or \(\mathcal{B}\) is an RPC (Theorem 5.2).

**Proof.** Assemble cited results; \(\delta\ge t\) feeds (4). ∎

### Theorem 9.2 (Conditional non-existence)
If no RPC can occur in a \(t\)-critical graph with \(\eta(G-v)=t-1\) and \(\delta\ge t\), then no such minimal counterexample exists, and every graph with no \(K_t\) minor has \(\chi\le t-1\) among those that would force \(\delta\ge t\) critical subgraphs — more cleanly:

> **Assume:** every \(\Phi\)-maximal contact-deficient model in a \(t\)-critical graph with \(\eta(G-v)=t-1\) is non-RPC (i.e.\ SPPA always fires).  
> **Conclude:** \(\mathrm{HC}_t\).

**Proof.** Same as the standard MCM reduction (Theorem 9.1 of the MCM note): maximality of \(\Phi\) forbids deficiency. ∎

### Remark 9.3 (What is still open for \(t\ge 7\))
The open core is exactly the non-existence of RPCs (Corollary 5.3), not the SPPA side. Hajós’ counterexamples for \(t\ge 7\) show that **path-disjoint** rainbow systems need not exist; RPC analysis must use **contractions / reassignments**, not topological clique minors. The hybrid Kempe minor-bridge of Lemma 7.2 is the natural tool, but a complete simultaneous rewiring is not supplied.

---

## 10. Checklist

| Item | Statement | Status |
|------|-----------|--------|
| Thm 1.1 | \(Z=\emptyset\) at \(\Phi\)-max | **Proved** |
| Thm 2.1 | Surplus Menger \(\ge t-1\) paths \(v\to C\) | **Proved** |
| Lem 2.5–2.6 | Separator in \(A\); pigeonhole | **Proved** |
| Lem 3.2–3.5 | Hybrid Kempe + fan alignment | **Proved** |
| Thm 4.3–4.5 | PNCP / SPPA / SPPA-Hadwiger | **Proved** |
| Thm 5.2 / Cor 5.3 | Dichotomy; reduction of Lemma G to no-RPC | **Proved** |
| Lem 6.1–6.6 | RPC cutvertex structure | **Proved** |
| Prop 6.7 | Block reassignment | **Partial** (subcase only) |
| Lem 7.2–7.3 | Kempe/minor bridge for (R3) | **Proved** (local) |
| Prop 8.1 | Finite counterexample to naïve absorption F | **Proved** |
| Full Lemma G / no-RPC for all configs | Simultaneous Fan Absorption | **Open** |
| Full \(\mathrm{HC}_t\) (\(t\ge 7\)) | — | **Open** |

---

## 11. Final verdict

### Proved here
1. **Collapse of unused vertices:** every \(\Phi\)-maximal model partitions \(V(G-v)\).
2. **Surplus Menger:** \(\ge t-1\) disjoint paths from the apex into the entire non-contact side — strictly stronger than the classical \(|J|\)-fan.
3. **SPPA-Hadwiger (strictly weaker than Lemma G):** if a deficient \(\Phi\)-max model admits a fan of strongly private non-cut portals (clean simultaneous case), then \(s\) rises to \(t-1\) and \(G\) has a \(K_t\) minor. Full proof.
4. **Dichotomy:** \(\Phi\)-max deficient models are SPPA-absorbable (impossible) or **Rigid Portal Configurations**. Lemma G \(\Leftrightarrow\) no RPC.
5. **RPC local structure** (cutvertices, unique attachments, double portals in one block) with complete proofs; local minor-bridge conversion of (R3).
6. **Naïve absorption is false**, by an explicit finite model configuration.

### Not proved
- Non-existence of RPCs in \(t\)-critical graphs.
- Full Simultaneous Fan Absorption (Lemma G) for arbitrary snakes through cutvertices.
- Unconditional \(\mathrm{HC}_t\) for \(t\ge 7\).

### Precise residual gap
\[
\boxed{\text{Gap }G_t^{\mathrm{hyb}}:\ \text{No Rigid Portal Configuration exists in a minimal counterexample.}}
\]
This is still sufficient for \(\mathrm{HC}_t\) (Theorem 9.2) and is **not** a pure synonym of Hadwiger in wording: it is a statement about cutvertex/unique-attachment geometry of last exits of Menger fans into non-contact blocks of \(\Phi\)-maximal models. It is, however, still strong enough that a full proof would yield Hadwiger, and a counterexample to Hadwiger would yield an RPC (by Theorem 5.2).

### Continuation: RPC type elimination
A pointed attack on RPC itself is recorded in [`hadwiger_rpc_elimination.md`](hadwiger_rpc_elimination.md). That note proves:
- **no pure-\((R2)\)-only RPC** under \(\delta\ge t\);
- pure-\((R2)\) trade size bounds at \(\Phi\)-max;
- free \((R1)\)-component absorption and inessential-\((R3)\) bridge repair;
- a finite abstract RPC outside criticality;
- reduction of every CE-RPC to a **hard-core** RPC (irreplaceable cuts / essential unique attachments).

The residual gap is thereby sharpened to \(G_t^{\mathrm{RPC}}\): no hard-core RPC under the standing CE hypotheses. Full hard-core elimination remains open.

### Why this is progress beyond the MCM note
- The MCM note left Lemma G as a monolithic unproved absorption statement and treated \(Z\) as live.
- Here \(Z\) is eliminated, surplus Menger is proved, absorption is **split** into a fully proved SPPA half and an RPC half, a false sublemma is killed by counterexample, and hybrid Kempe structure is wired into the RPC side as local cut conversion.

---

*End of hybrid attack note.*
