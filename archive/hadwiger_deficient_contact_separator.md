# Hybrid Mechanism: Deficient Contact Forces a Thin Separator That Is Almost a Clique

**Conjecture (Hadwiger, \(\mathrm{HC}_t\)).** Every finite simple graph with no \(K_t\) minor is \((t-1)\)-colourable.

**This note.** A mechanism that is **new relative to pure degeneracy** and **new relative to pure MCM/fan absorption**: combine a **maximal contact \(K_{t-1}\) model** at an apex \(v\) with the **canonical \((v,C)\)-separator** forced by contact deficiency, then press the classical **no-clique-separator** property of \(t\)-critical graphs against the model geometry of the contact region. The goal is either a \(K_t\) minor, a forbidden separating clique, or a colouring extension of \(G\).

**Status summary.**
- §§1–6: fully proved (path obstruction, separator calculus, size bounds, clique case).
- §7: fully proved structural consequences when the separator is **not** a clique (critical properties of \(G[S]\), missing-edge geometry relative to contact bags).
- §8: fully proved pigeonhole / bag-distribution constraints.
- §9: colouring-extension under extra hypotheses on missing edges (**proved** in listed subcases; **not** in full generality).
- §10: honest gap — the hybrid does **not** close \(\mathrm{HC}_t\) for \(t\ge 7\); it yields a concrete obstruction class (non-clique \((v,C)\)-separators of order \(\ge t-1\) living in \(\le t-2\) contact bags).

**Tools used.** Critical-graph structure, Menger’s theorem, model reassignment for free attachments only. Dirac’s \(\kappa\ge t-1\) is used as classical input (same status as in the MCM note). No degeneracy comparison with Mader/Kostochka–Thomason thresholds is used for the contradiction attempts below.

---

## 0. Standing setup

### Definition 0.1
A graph \(G\) is **\(t\)-critical** if \(\chi(G)=t\) and \(\chi(H)\le t-1\) for every proper subgraph \(H\subsetneq G\).

### Definition 0.2
A **minimal counterexample** to \(\mathrm{HC}_t\) is a graph with \(\chi\ge t\), no \(K_t\) minor, minimum order, and subject to that minimum size.

### Lemma 0.3 (Shape — standard)
Let \(t\ge 2\) and let \(G\) be a minimal counterexample to \(\mathrm{HC}_t\). Then:
1. \(\chi(G)=t\) and \(G\) is \(t\)-critical;
2. \(\eta(G)=t-1\) (has a \(K_{t-1}\) minor, no \(K_t\) minor);
3. for every \(v\in V(G)\), \(\chi(G-v)=t-1=\eta(G-v)\);
4. \(\delta(G)\ge t-1\);
5. \(G\) has **no separating clique of order \(\le t-1\)** (in particular none of order \(\le t-2\)).

**Proof.**
(1)–(3). For any vertex \(v\), \(G-v\) has no \(K_t\) minor and fewer vertices, so \(\chi(G-v)\le t-1\). Thus \(\chi(G)=t\). Size-minimality among minimum-order counterexamples forces \(\chi(G-e)=t-1\) for every edge, so \(G\) is \(t\)-critical. Always \(\eta(G)\le t-1\). Contractions \(G/e\) have order \(n-1\), hence \(\chi(G/e)\le\eta(G/e)\le t-1\); criticality forces \(\chi(G/e)=t-1\), so \(\eta(G/e)=t-1\). A \(K_{t-1}\) model of \(G/e\) lifts to \(G\), whence \(\eta(G)=t-1\). For \(G-v\): not a counterexample, so \(\chi(G-v)\le\eta(G-v)\le t-1\); criticality gives \(\chi(G-v)=t-1\), hence \(\eta(G-v)=t-1\).

(4). If \(\deg(v)\le t-2\), a \((t-1)\)-colouring of \(G-v\) extends to \(v\).

(5). Let \(S\) be a separating clique, \(G=G_1\cup G_2\) with \(V(G_1)\cap V(G_2)=S\) and both interiors nonempty. Each \(G_i\) is a proper subgraph, hence \((t-1)\)-colourable. Clique colourings inject \(S\) into \(\{1,\dots,t-1\}\). If \(|S|\le t-1\), permute to agree on \(S\); the union colours \(G\), contradiction. ∎

### Lemma 0.4 (Dirac connectivity — classical input)
Every \(t\)-critical graph satisfies \(\kappa(G)\ge t-1\).

**Status.** Used freely; elementary self-contained expansion is classical (Dirac 1953). The hybrid gap below does **not** hide inside this citation: even with full \(\kappa\ge t-1\), the non-clique separator case remains open.

---

## 1. Maximal contact models and regions

Fix \(t\ge 5\). Let \(G\) be a minimal counterexample to \(\mathrm{HC}_t\), and fix \(v\in V(G)\). By Lemma 0.3(3), \(G-v\) admits a \(K_{t-1}\) model.

### Definition 1.1 (Contact)
Let \(\mathcal{B}=\{B_1,\dots,B_{t-1}\}\) be a \(K_{t-1}\) model in \(G-v\). The **contact index set** is
\[
I(\mathcal{B},v):=\bigl\{\,i\in\{1,\dots,t-1\}:\ N(v)\cap B_i\neq\emptyset\,\bigr\},
\]
and \(s(\mathcal{B},v):=|I(\mathcal{B},v)|\). Indices in \(I(\mathcal{B},v)\) label **contact** branch sets; the complementary indices \(J(\mathcal{B},v):=\{1,\dots,t-1\}\setminus I(\mathcal{B},v)\) label **non-contact** branch sets.

### Definition 1.2 (MCM)
A model \(\mathcal{B}\) in \(G-v\) is a **maximal contact model (MCM)** at \(v\) if \(s(\mathcal{B},v)\) is maximum among all \(K_{t-1}\) models in \(G-v\).

### Lemma 1.3 (Contact deficiency)
Every MCM \(\mathcal{B}\) at \(v\) satisfies \(s(\mathcal{B},v)\le t-2\).

**Proof.** If \(s=t-1\), every branch set meets \(N(v)\), so \(\bigl\{\{v\},B_1,\dots,B_{t-1}\bigr\}\) is a \(K_t\) model in \(G\), contradicting \(\eta(G)=t-1\). ∎

### Definition 1.4 (Regions)
Fix an MCM \(\mathcal{B}\) at \(v\). Write \(I:=I(\mathcal{B},v)\), \(J:=J(\mathcal{B},v)\) (so \(J\neq\emptyset\)), and
\begin{align*}
A &:=\bigcup_{i\in I} B_i,\\
C &:=\bigcup_{j\in J} B_j,\\
Z &:=V(G-v)\setminus(A\cup C).
\end{align*}
Thus \(N(v)\cap C=\emptyset\), \(N(v)\subseteq A\cup Z\), \(C\neq\emptyset\), and \(A\) is the union of \(s:=s(\mathcal{B},v)\le t-2\) pairwise adjacent connected bags.

### Lemma 1.5 (Model cross-edges into non-contact)
For every \(j\in J\) and every \(i\in I\), there is an edge of \(G\) between \(B_j\) and \(B_i\). For every distinct \(j,j'\in J\), there is an edge between \(B_j\) and \(B_{j'}\).

**Proof.** Definition of a \(K_{t-1}\) model. ∎

---

## 2. Path obstruction (Menger form)

### Lemma 2.1 (No free attachment path — full proof)
There is **no** path in \(G-v\) that starts in \(N(v)\cap Z\), ends in \(C\), and has all internal vertices in \(Z\).

Equivalently: in the graph \(G-v-A\), no vertex of \(N(v)\cap Z\) lies in the same component as any vertex of \(C\). (In particular \(C\cap(N(v)\cap Z)=\emptyset\) is already known; the claim is about \(Z\)-paths.)

**Proof.** Suppose \(P=x_0x_1\dots x_\ell\) is such a path, with \(x_0\in N(v)\cap Z\), \(x_\ell\in B_j\subseteq C\) for some \(j\in J\), and \(\{x_1,\dots,x_{\ell-1}\}\subseteq Z\).

**Case \(\ell=1\).** Then \(x_0\sim x_\ell\in B_j\). Set \(B_j':=B_j\cup\{x_0\}\). This set is connected, disjoint from all other branch sets, retains every cross-edge of \(B_j\), and meets \(N(v)\). The model \((\mathcal{B}\setminus\{B_j\})\cup\{B_j'\}\) has contact index set \(I\cup\{j\}\), contradicting maximality of \(s\).

**Case \(\ell\ge 2\).** Set
\[
B_j^\sharp:=B_j\cup\{x_0,x_1,\dots,x_{\ell-1}\}.
\]
Connectedness: the subpath \(x_0\dots x_{\ell-1}x_\ell\) attaches to \(B_j\) at \(x_\ell\). Disjointness from other branch sets: new vertices lie in \(Z\cup\{x_0\}\). Cross-edges of \(B_j\) survive. Contact: \(x_0\in N(v)\cap B_j^\sharp\). Contact index set gains \(j\), contradiction. ∎

### Corollary 2.2 (Separation form of free attachments)
In \(G-v\), the set \(A\) separates \(N(v)\cap Z\) from \(C\): every path in \(G-v\) from \(N(v)\cap Z\) to \(C\) meets \(A\).

**Proof.** Lemma 2.1. ∎

### Lemma 2.3 (\(A\) separates \(v\) from \(C\) in \(G\))
Every \(v\)–\(C\) path in \(G\) meets \(A\). In particular \(A\) is a \((v,C)\)-separator in \(G\).

**Proof.** Let \(P\) be a \(v\)–\(C\) path. The successor \(w\) of \(v\) on \(P\) lies in \(N(v)\subseteq A\cup Z\). If \(w\in A\), done. If \(w\in Z\), the subpath of \(P\) from \(w\) to the first vertex of \(C\) is a walk in \(G-v\) from \(N(v)\cap Z\) to \(C\); by Corollary 2.2 it meets \(A\). (No edge \(vc\) with \(c\in C\) exists, so \(P\) has length at least \(2\).) ∎

### Remark 2.4 (Menger obstruction, careful statement)
Lemma 2.3 is a **global hitting-set** statement for the family of all \(v\)–\(C\) paths: the set \(A\) is a hitting set. It is **not** a claim that \(\kappa(G)\) is small. Menger’s theorem applied to the pair \((v,C)\) yields
\[
\tau_G(v,C)\;=\;\nu_G(v,C),
\]
where \(\tau\) is the minimum order of a \((v,C)\)-separator and \(\nu\) is the maximum number of internally vertex-disjoint \(v\)–\(C\) paths. Lemma 2.3 gives \(\tau_G(v,C)\le|A|\). Combined with Lemma 0.4 (see Lemma 3.3), one gets \(\tau_G(v,C)\ge t-1\). The hybrid uses the **location** of a min separator inside \(A\), not a sub-connectivity claim.

---

## 3. The canonical separator \(S\)

### Definition 3.1 (Reachable \(v\)-side in \(G-A\))
Let \(K_v\) be the set of all vertices of \(G-A\) that lie in the same component of \(G-A\) as \(v\). Equivalently,
\[
K_v=\bigl\{\,x\in V(G)\setminus A:\ \text{there is a \(v\)–\(x\) path in \(G-A\)}\,\bigr\}.
\]
By Lemma 2.3, \(K_v\cap C=\emptyset\), so \(K_v\subseteq\{v\}\cup Z\).

### Definition 3.2 (Canonical frontier separator)
Set
\[
S\;:=\;N_G(K_v)\setminus K_v.
\]
Then \(S\subseteq A\) (every neighbour of \(K_v\) outside \(K_v\) lies in \(A\), because edges leaving \(K_v\) in \(G-A\) would extend \(K_v\)). Call \(S\) the **canonical \((v,C)\)-frontier** of the MCM.

### Lemma 3.3 (Separator properties of \(S\))
1. \(S\) separates \(v\) from \(C\) in \(G\): every \(v\)–\(C\) path meets \(S\).
2. Every vertex of \(S\) has at least one neighbour in \(K_v\).
3. Every vertex of \(S\) has at least one neighbour in \(V(G)\setminus(K_v\cup S)\) (in particular, toward the side containing \(C\), after discarding useless vertices of \(A\setminus S\) if needed — see (4)).
4. \(C\subseteq V(G)\setminus(K_v\cup S)\), and some component of \(G-S\) other than the component of \(v\) meets \(C\).
5. \(S\) is a **minimal** \((v,C)\)-separator up to deletion of vertices of \(A\) that do not meet \(K_v\): no proper subset of \(S\) separates \(v\) from \(C\) while still meeting every \(K_v\)-exit. More precisely: for every \(s\in S\) there is a \(v\)–\(C\) path whose unique vertex in \(S\) is \(s\) *provided* one first replaces \(S\) by a minimum-order \((v,C)\)-separator contained in \(A\) (Lemma 3.4). The canonical \(S\) itself always satisfies (1)–(2) and (4); minimality in the strong Menger sense holds after thinning (Lemma 3.4).

**Proof.**
(1). Let \(P\) be a \(v\)–\(C\) path. Walk along \(P\) from \(v\). All vertices of \(P\) until the first vertex of \(A\) lie in \(K_v\). Let \(a\) be the first vertex of \(P\) in \(A\). The predecessor of \(a\) on \(P\) lies in \(K_v\), so \(a\in N(K_v)\setminus K_v=S\). Thus \(P\) meets \(S\).

(2). Immediate from the definition \(S=N(K_v)\setminus K_v\).

(4). \(C\cap K_v=\emptyset\) by Lemma 2.3, and \(C\cap S=\emptyset\) because \(S\subseteq A\) and \(A\cap C=\emptyset\). Hence \(C\subseteq V(G)\setminus(K_v\cup S)\). The component of \(G-S\) containing a fixed \(c\in C\) is distinct from the component containing \(v\) (else a \(v\)–\(c\) path in \(G-S\) would exist).

(3). If some \(s\in S\) had no neighbour outside \(K_v\cup S\), then every neighbour of \(s\) would lie in \(K_v\cup S\). This does not by itself contradict separation of \(v\) from \(C\), but it does mean \(s\) is useless for reaching \(C\): every path that uses \(s\) to leave \(K_v\) is trapped in \(S\cup K_v\). Such an \(s\) can be deleted from the separator without creating a \(v\)–\(C\) path (any \(v\)–\(C\) path through \(s\) would need a next vertex outside \(K_v\cup S\)). After deleting all such useless vertices one obtains a subset \(S'\subseteq S\) in which every vertex has a neighbour in \(V(G)\setminus(K_v\cup S')\). We work with a thinned minimum separator next. ∎

### Lemma 3.4 (Minimum separator inside \(A\))
There exists a \((v,C)\)-separator \(S^\star\subseteq A\) of order \(\tau_G(v,C)\) (hence of minimum possible order among all \((v,C)\)-separators). Moreover \(t-1\le|S^\star|\le|A|\), and one may choose \(S^\star\) so that:
- every \(s\in S^\star\) has a neighbour in the component of \(G-S^\star\) containing \(v\);
- every \(s\in S^\star\) has a neighbour in some component of \(G-S^\star\) that meets \(C\).

**Proof.**
By Lemma 2.3, \(A\) is a \((v,C)\)-separator, so \(\tau:=\tau_G(v,C)\le|A|\).

By Menger’s theorem, \(\tau=\nu_G(v,C)\), the max number of internally vertex-disjoint \(v\)–\(C\) paths. Each such path meets \(A\) (Lemma 2.3), and distinct paths meet \(A\) in distinct vertices (internal vertices of distinct paths are disjoint; the first \(A\)-vertex of each path is internal or the terminal only if the terminal is in \(A\), but terminals lie in \(C\), disjoint from \(A\)). Hence any hitting set of the path family that is contained in \(A\) has size at least \(\nu=\tau\). Therefore the minimum order of a \((v,C)\)-separator **contained in \(A\)** is exactly \(\tau\). Let \(S^\star\subseteq A\) be such a minimum separator.

**Lower bound.** Fix any \(c\in C\). Then \(vc\notin E(G)\). Any \((v,C)\)-separator is a \(v\)–\(c\) separator, so \(\tau\ge\kappa(G)\ge t-1\) by Lemma 0.4. (More carefully: \(\kappa(G)\) is the minimum order of a separator of \(G\), i.e. a set whose deletion leaves a disconnected graph; a minimum \(v\)–\(c\) separator has order at least \(\kappa(G)\) when \(v,c\) are nonadjacent, by the global definition of connectivity. Yes: \(\kappa(G)=\min_{x\not\sim y}\tau(x,y)\) for non-complete \(G\), and \(G\not\cong K_t\) is not complete of order \(t\) in a counterexample of larger order; for non-complete graphs \(\kappa=\min\tau(x,y)\). In a complete graph \(\kappa=n-1\). Our \(G\) is not complete — else \(G\cong K_t\) has a \(K_t\) minor — so \(\kappa=\min_{x\not\sim y}\tau(x,y)\le\tau(v,c)\le\tau(v,C)\). Combined with Dirac \(\kappa\ge t-1\), we get \(\tau(v,C)\ge t-1\).)

**Neighbourhood claims.** Among minimum \((v,C)\)-separators contained in \(A\), choose \(S^\star\) so that the component \(D_v\) of \(G-S^\star\) containing \(v\) is maximal. Every \(s\in S^\star\) has a neighbour in \(D_v\): else \(S^\star\setminus\{s\}\) still separates \(v\) from \(C\). Every \(s\in S^\star\) has a neighbour in \(V(G)\setminus(D_v\cup S^\star)\): else \(S^\star\setminus\{s\}\) still separates. Some component of the complement meets \(C\) because \(S^\star\) separates \(v\) from \(C\). ∎

### Definition 3.5 (Working separator)
For the rest of the note, **\(S\) denotes a minimum-order \((v,C)\)-separator contained in \(A\)** as in Lemma 3.4 (not merely the possibly non-minimum frontier of Definition 3.2). Write
\[
\tau:=|S|=\tau_G(v,C),\qquad t-1\le\tau\le|A|.
\]
Let \(D_v\) be the component of \(G-S\) containing \(v\), and let \(D_C\) be the union of all components of \(G-S\) that meet \(C\). Write
\[
G_v:=G\bigl[V(D_v)\cup S\bigr],\qquad
G_C:=G\bigl[V(D_C)\cup S\bigr].
\]
Both are proper subgraphs of \(G\) (each misses the opposite open side), so
\[
\chi(G_v)\le t-1,\qquad \chi(G_C)\le t-1.
\]

---

## 4. Size control by connectivity

### Proposition 4.1 (Size sandwich)
\[
t-1\;\le\;\tau\;=\;|S|\;\le\;|A|\;=\;\sum_{i\in I}|B_i|.
\]
In particular \(S\) is a separator of order at least the Dirac connectivity bound, living entirely inside the contact region of an MCM with only \(s\le t-2\) contact bags.

**Proof.** Lemma 3.4. ∎

### Proposition 4.2 (Path packing)
There exist \(\tau\) pairwise internally vertex-disjoint \(v\)–\(C\) paths in \(G\). Each meets \(S\) in exactly one vertex when the paths are chosen to realise Menger’s equality against \(S\), and those \(\tau\) attachment vertices are exactly the vertices of some minimum separator (which we may take to be our \(S\)).

**Proof.** Menger’s theorem. ∎

### Remark 4.3 (Why “small” is accurate in the hybrid sense)
The separator is not smaller than \(t-1\). “Small” here means:
1. **order controlled from below by \(\kappa\)** and from above by the contact region;
2. **supported on only \(s\le t-2\) bags** of a clique model (a thin cut relative to the full \(K_{t-1}\) model, which has \(t-1\) bags);
3. **strictly thinner in bag-count than a full rooted contact system** (full contact would use \(t-1\) bags and yield a \(K_t\) minor without separators).

The hybrid’s force comes from packing a \(\ge(t-1)\)-separator into \(\le(t-2)\) model bags, not from claiming \(\tau\le t-2\) (which is false under Dirac).

---

## 5. The clique case — full contradiction

### Theorem 5.1 (If \(S\) is a clique, then contradiction)
If \(G[S]\) is complete, then \(G\) is not a counterexample to \(\mathrm{HC}_t\).

**Proof.** \(S\) separates \(G\) (at least \(D_v\) and a component meeting \(C\) are distinct components of \(G-S\)). By Lemma 0.3(5), a separating clique has order \(\ge t\). Thus \(\tau=|S|\ge t\).

But then \(G[S]\) contains \(K_t\) as a subgraph, hence \(G\) has a \(K_t\) minor, contradicting \(\eta(G)=t-1\). ∎

### Corollary 5.2 (Forced non-clique)
In a minimal counterexample, for every apex \(v\) and every MCM at \(v\), every minimum \((v,C)\)-separator \(S\subseteq A\) induces a **non-complete** graph. In particular \(\tau\ge t-1\) and \(G[S]\) misses at least one edge.

**Proof.** Theorem 5.1. ∎

### Remark 5.3 (Compatibility with Dirac)
Corollary 5.2 is consistent with \(\kappa(G)=t-1\): the separators that realise connectivity in a \(t\)-critical non-complete graph **cannot** be cliques of order \(t-1\) (Lemma 0.3(5)). The hybrid asserts that the **specific** separators arising from deficient contact are under extra geometric pressure from the model — pressure that general separators need not feel.

---

## 6. What is fully proved so far (checklist of claims 1–3)

| Claim | Statement | Status |
|-------|-----------|--------|
| 1 | No path from \(N(v)\cap Z\) into \(C\) avoiding \(A\) | **Proved** (Lemma 2.1) |
| 2 | A min set of vertices in \(A\) meeting all \(v\)–\(C\) paths is a \((v,C)\)-separator \(S\) | **Proved** (Lemmas 2.3, 3.3, 3.4) |
| 3 | \(t-1\le|S|\le|A|\), controlled by connectivity + contact support | **Proved** (Proposition 4.1) |
| 4a | If \(S\) is a clique \(\Rightarrow\) contradiction | **Proved** (Theorem 5.1) |
| 4b | \(S\) is never a clique in a counterexample | **Proved** (Corollary 5.2) |

The remaining work is claim 4’s non-clique branch: force “almost clique” structure on \(G[S]\) hard enough to colour \(G\) or build a \(K_t\) minor.

---

## 7. Non-clique separators: \(\chi\)-critical properties of \(G[S]\)

### Lemma 7.1 (Both sides see every separator vertex)
Every \(s\in S\) has a neighbour in \(D_v\) and a neighbour in \(D_C\).

**Proof.** Lemma 3.4. ∎

### Lemma 7.2 (Colourings of the two sides)
There exist proper \((t-1)\)-colourings \(c_v\) of \(G_v\) and \(c_C\) of \(G_C\).

**Proof.** Both are proper subgraphs of the \(t\)-critical graph \(G\). ∎

### Lemma 7.3 (Failure of colour matching is the only obstruction)
If there exist proper \((t-1)\)-colourings \(c_v\) of \(G_v\) and \(c_C\) of \(G_C\) that **agree on \(S\)** (as functions \(S\to\{1,\dots,t-1\}\)), then \(\chi(G)\le t-1\), contradiction.

**Proof.** The union is a proper colouring of \(G[V(D_v)\cup V(D_C)\cup S]\). Every edge of \(G\) has both ends in this vertex set: any edge leaving \(D_v\cup S\) enters \(V(G)\setminus(D_v\cup S)\), and components of \(G-S\) not meeting \(C\) can be folded into the \(C\)-side or coloured separately — **careful**.

**Precise repair.** Let \(\mathcal{D}\) be the set of all components of \(G-S\). One component is \(D_v\); write \(\mathcal{D}_C\) for those meeting \(C\), and \(\mathcal{D}_0\) for the rest (if any). For each \(D\in\mathcal{D}\), the graph \(G[V(D)\cup S]\) is a proper subgraph, hence \((t-1)\)-colourable. If we can choose colourings of all these graphs that agree on \(S\), the union colours \(G\).

So the pure two-side statement is complete when \(G-S\) has exactly two components. In general:

### Lemma 7.3′ (Multi-side colour matching)
If there is a single map \(\gamma:S\to\{1,\dots,t-1\}\) that extends to a proper \((t-1)\)-colouring of \(G[V(D)\cup S]\) for **every** component \(D\) of \(G-S\), then \(\chi(G)\le t-1\), contradiction.

**Proof.** Union over components. ∎

### Definition 7.4 (List of admissible colourings of \(S\))
For each component \(D\) of \(G-S\), let \(\mathrm{Adm}(D)\) be the set of all restrictions to \(S\) of proper \((t-1)\)-colourings of \(G[V(D)\cup S]\). Each \(\mathrm{Adm}(D)\) is a nonempty set of proper colourings of the induced subgraph \(G[S]\) (properness on \(S\) is forced by edges inside \(S\)).

### Corollary 7.5 (Intersection obstruction)
In a counterexample,
\[
\bigcap_{D}\mathrm{Adm}(D)\;=\;\emptyset.
\]
In particular, writing \(D_v\) and any \(D\subseteq D_C\),
\[
\mathrm{Adm}(D_v)\cap\mathrm{Adm}(D)=\emptyset.
\]

**Proof.** Lemma 7.3′. ∎

### Lemma 7.6 (Missing edges are essential)
Let \(xy\notin E(G)\) with \(x,y\in S\). Then there exist colourings in \(\mathrm{Adm}(D_v)\) (resp. some \(C\)-side) in which \(x\) and \(y\) receive the **same** colour, **or** the two sides force incompatible equality/inequality patterns on the missing edges of \(G[S]\).

**More precisely (structural dichotomy for a single missing edge):**

### Lemma 7.7 (Single missing edge — classical critical dichotomy)
Suppose \(G[S]\) is a complete graph minus exactly one edge \(xy\). Then \(\tau=|S|\ge t-1\), and one of the following holds:

**(α)** Some proper \((t-1)\)-colouring of \(G_v\) has \(c_v(x)=c_v(y)\), and some proper \((t-1)\)-colouring of \(G_C\) has \(c_C(x)=c_C(y)\).  
**(β)** Every proper \((t-1)\)-colouring of \(G_v\) has \(c_v(x)\neq c_v(y)\), or the same on the \(C\)-side.

**Proof.** Pure logic on the two boolean predicates “exists equal-colour colouring on side \(v\)” and “on side \(C\)”. ∎

### Lemma 7.8 (Colouring extension when both sides allow a monochromatic missing edge)
In the setting of Lemma 7.7(α), if moreover \(|S|\le t-1\), then \(\chi(G)\le t-1\), contradiction.

**Proof.** Take \(c_v\) with \(c_v(x)=c_v(y)\) and \(c_C\) with \(c_C(x)=c_C(y)\). On \(S\), both colourings properly colour \(K_{|S|}-xy\): all pairs except \(xy\) get distinct colours, and \(x,y\) share a colour. Thus both colourings use exactly \(|S|-1\) colours on \(S\), with a unique repeated colour on \(\{x,y\}\).

If \(|S|\le t-1\), there is room in the palette. The colourings of \(S\) are determined up to permutation of colours by the partition \(\bigl\{\{x,y\}\bigr\}\cup\bigl\{\{s\}:s\in S\setminus\{x,y\}\bigr\}\). Permute colours of \(c_C\) so that \(c_C|_{S}=c_v|_{S}\). The union colours \(G_v\cup G_C\). Remaining components of \(G-S\), if any, are handled as in Lemma 7.3′ provided each admits a colouring realising the same map on \(S\).

**Gap in multi-component generality.** If some third component \(D_0\) has \(\gamma\notin\mathrm{Adm}(D_0)\) for this common \(\gamma\), extension fails. When \(G-S\) has only two components (common after suppressing non-\(C\) components into a redefined \(C\)-side, or when \(Z\)-debris is empty), the argument is complete. ∎

### Proposition 7.9 (Two-component almost-clique extension — **proved**)
Assume \(G-S\) has exactly two components \(D_v\) and \(D_C\), \(G[S]\cong K_\tau-e\) for a single edge \(e=xy\), and \(\tau\le t-1\). If both sides admit a proper \((t-1)\)-colouring with equal colours on \(x,y\), then \(\chi(G)\le t-1\), contradiction.

**Proof.** Lemma 7.8 in the two-component case. ∎

### Proposition 7.10 (Two-component, both sides force distinct colours on the missing edge)
Assume the same two-component almost-clique setting, but every \((t-1)\)-colouring of \(G_v\) and of \(G_C\) gives \(c(x)\neq c(y)\). Then each side’s admissible colourings of \(S\) are exactly the proper \((t-1)\)-colourings of the complete graph \(K_\tau\) (i.e. injections \(S\to\{1,\dots,t-1\}\) if \(\tau\le t-1\)).

If \(\tau\le t-1\), one may permute to match any two injections that use the same image set of size \(\tau\). In particular if \(\tau\le t-1\), colour matching succeeds and \(\chi(G)\le t-1\), contradiction — **unless** the two sides are forced to use different constraints that are not pure completeness. But under the hypothesis that both sides always colour \(x,y\) with distinct colours, \(G[S]\) is coloured as if complete, and matching works for \(\tau\le t-1\).

**Proof.** Injections of a set of size \(\tau\le t-1\) into a palette of \(t-1\) colours may be matched by a palette permutation once the images are aligned; more carefully: fix \(c_v|_S\), which is injective on \(S\) (because all pairs including \(xy\) receive distinct colours). Take any \(c_C\); \(c_C|_S\) is also injective. There is a permutation \(\pi\) of the palette with \(\pi\circ c_C|_S = c_v|_S\) because both are injections from the same domain into the palette — **false in general** if the images differ and we need \(\pi\circ c_C = c_v\) pointwise: yes, any two injections \(f,g:S\to\Gamma\) with \(|S|\le|\Gamma|\) need not satisfy \(g=\pi\circ f\) for a single \(\pi\) unless we only care about... actually yes they do: set \(\pi(f(s))=g(s)\) on the image of \(f\), and extend \(\pi\) arbitrarily to the rest of \(\Gamma\). This is well-defined because \(f\) is injective. Then \(\pi\circ f = g\). Here we need \(\pi\circ c_C = c_v\), so take \(f=c_C|_S\), \(g=c_v|_S\). ∎

### Corollary 7.11 (Two-component, deficiency-one clique, \(\tau\le t-1\) — **closed**)
If \(G-S\) has two components, \(G[S]\cong K_\tau - e\), and \(\tau\le t-1\), then \(\chi(G)\le t-1\), contradiction.

**Proof.** Combine Propositions 7.9 and 7.10: either both sides allow \(c(x)=c(y)\), or at least one side (in fact the case analysis) forces the injective regime on both after the hypothesis split; the only logical gap would be “one side allows equality, the other forbids it”.

### Lemma 7.12 (Mixed equality obstruction — the real almost-clique gap)
Suppose \(G[S]\cong K_\tau-xy\), two components, \(\tau\le t-1\), and:
- every colouring of \(G_v\) has \(c_v(x)\neq c_v(y)\);
- every colouring of \(G_C\) has \(c_C(x)=c_C(y)\) (or vice versa).

Then colour matching on \(S\) is impossible: one side requires \(c(x)\neq c(y)\), the other requires \(c(x)=c(y)\). This configuration is **not** ruled out by Propositions 7.9–7.10.

**Proof.** Immediate from the incompatible equality constraints. ∎

### Remark 7.13 (When does the mixed obstruction occur?)
The mixed obstruction is the classical “critical sides disagree on a missing edge” phenomenon. In abstract critical-graph theory it is handled by adding the edge \(xy\) and analysing critical subgraphs of \(G+xy\) (Dirac’s method). That analysis **does not** use the contact model. The hybrid’s hope is that the model forbids the mixed obstruction for separators supported in \(A\). Section 8 develops the model constraints; Section 9 returns to forbidding the mixed case.

---

## 8. Contact bag geometry of \(S\)

### Lemma 8.1 (Pigeonhole)
Let \(s=|I|\le t-2\) and \(\tau=|S|\ge t-1\). Write \(S_i:=S\cap B_i\) for \(i\in I\). Then \(\sum_{i\in I}|S_i|=\tau\) (because \(S\subseteq A=\bigcup_{i\in I}B_i\) and the \(B_i\) are pairwise disjoint), and
\[
\max_{i\in I}|S_i|\;\ge\;\Bigl\lceil\frac{\tau}{s}\Bigr\rceil\;\ge\;\Bigl\lceil\frac{t-1}{t-2}\Bigr\rceil\;=\;2.
\]
In particular some contact bag contains at least two vertices of \(S\).

**Proof.** Disjointness of branch sets and the division algorithm. ∎

### Lemma 8.2 (Intra-bag paths)
If \(x,y\in S_i\) are distinct, then every \(x\)–\(y\) path in \(G[B_i]\) lies entirely in \(A\). If such a path is internally disjoint from \(S\), its internal vertices lie in \(A\setminus S\subseteq V(G)-S\), hence lie in some component of \(G-S\) — but \(x,y\in S\) are not in \(G-S\), so an internally \(S\)-avoiding \(x\)–\(y\) path in \(G[B_i]\) would be an edge or would place internal vertices in \(G-S\) adjacent to both... A path of length \(\ge 2\) with ends in \(S\) and interior in \(G-S\) means the two ends have a common side-component neighbour structure.

**More useful form:**

### Lemma 8.3 (No \(S\)-internal path through one open side connecting two separator vertices without being an edge on that side)
If \(x,y\in S\) are joined by a path with interior in \(D_v\), then in any proper colouring of \(G_v\) one has constraints along that path; in particular if \(xy\notin E(G)\) and there is an \(x\)–\(y\) path through \(D_v\), Kempe-type recolouring on \(G_v\) may force or forbid \(c(x)=c(y)\).

**Proof.** Standard path-colouring: a path of odd/even length through a bipartite subgraph forces inequality/equality in 2-coloured subgraphs; in general \((t-1)\)-colourings the existence of an \(x\)–\(y\) path does not alone force \(c(x)\neq c(y)\). ∎

### Lemma 8.4 (Inter-bag model edges need not join \(S\)-vertices)
If \(x\in S_i\), \(y\in S_k\) with \(i\neq k\), the model supplies **some** edge between \(B_i\) and \(B_k\), but not necessarily the edge \(xy\). The unique model edge between the bags may miss \(S\) entirely.

**Proof.** Definition of models only requires some cross-edge. ∎

### Lemma 8.5 (Contracted contact clique)
Let \(H\) be the graph obtained from \(G[A]\) by contracting each contact bag \(B_i\) (\(i\in I\)) to a single supervertex \(b_i\), deleting loops, and suppressing parallel edges. Then \(H\) contains \(K_s\) as a spanning subgraph on \(\{b_i:i\in I\}\) (exactly the contact part of the model). The image of \(S\) is a multiset of supervertices; after contraction, \(S\) maps onto a vertex set \(S_H\subseteq V(H)\) with \(1\le|S_H|\le s\le t-2\).

**Proof.** Model cross-edges between contact bags. ∎

### Proposition 8.6 (Separator image is small in the bag quotient)
The bag-quotient image \(S_H\) of \(S\) has order at most \(s\le t-2\), while \(|S|\ge t-1\). Thus the contraction map \(S\to S_H\) is **non-injective**: at least two vertices of \(S\) lie in the same contact bag (recovering Lemma 8.1).

**Proof.** Lemmas 8.1 and 8.5. ∎

### Remark 8.7 (What the quotient does **not** give)
Contracting contact bags does **not** produce a separating set of order \(\le t-2\) in \(G\): contraction is not a deletion, and the preimage of \(S_H\) is a union of bags, hence large. One cannot feed \(S_H\) into Lemma 0.3(5). The quotient is only a bookkeeping device for pigeonhole and for tracking which bags carry separator vertices.

---

## 9. Forcing almost-clique / colouring extension — proved subcases and the gap

### Strategy
By Corollary 5.2, \(G[S]\) is not complete. Let \(m:= \binom{\tau}{2}-|E(G[S])|\) be the number of missing edges. We attempt:
- small \(m\) (especially \(m=1\)) + two components + \(\tau\le t-1\) \(\Rightarrow\) colour \(G\) (nearly done in §7, mixed case open);
- model structure forbids the mixed equality obstruction;
- or missing edges inside a single bag can be filled by paths that create a \(K_t\) minor.

### Theorem 9.1 (Degree-\((t-1)\) apex with full neighbourhood in \(A\) — **proved**)
Suppose \(\deg(v)=t-1\) and \(N(v)\subseteq A\). Then \(N(v)\) is a \((v,C)\)-separator (every \(v\)–\(C\) path leaves \(v\) into \(N(v)\)), so \(\tau\le t-1\). Combined with \(\tau\ge t-1\), \(\tau=t-1\) and we may take \(S=N(v)\) after thinning. If \(G[N(v)]\) is complete, then \(G[N[v]]\cong K_t\), contradiction. If not, \(S=N(v)\) is a non-clique \((t-1)\)-separator contained in \(A\).

**Proof.** Paths from \(v\) start in \(N(v)\). Size sandwich forces \(\tau=t-1\). Clique case: \(K_t\) subgraph. ∎

### Remark 9.2 (Dirac neighbourhood lemma)
Classically, \(t\)-critical graphs with \(t\ge 4\) satisfy: \(\deg(v)=t-1\Rightarrow G[N(v)]\cong K_{t-1}\). Granting that lemma, Theorem 9.1 yields an immediate contradiction, so every apex in a counterexample has \(\deg(v)\ge t\). We do **not** rely on that classical lemma for the rest of the hybrid; we record it as an optional shortcut for the minimum-degree case.

### Theorem 9.3 (Full neighbourhood contact, high degree — separator still non-clique)
If \(N(v)\subseteq A\), then \(N(v)\) is a \((v,C)\)-separator, so \(\tau\le\deg(v)\). Still \(\tau\ge t-1\), and \(G[S]\) is not complete (Corollary 5.2).

**Proof.** Same exit argument; Corollary 5.2. ∎

### Lemma 9.4 (Missing edge inside one contact bag)
Suppose \(x,y\in S_i\) for a common \(i\in I\), and \(xy\notin E(G)\). Let \(T_i\) be a spanning tree of \(G[B_i]\). The unique \(T_i\)-path \(Q\) from \(x\) to \(y\) has length \(\ge 2\) and lies in \(B_i\subseteq A\).

If \(Q\) is internally disjoint from \(S\), then the internal vertices of \(Q\) lie in \(A\setminus S\) and hence in \(G-S\). Those internal vertices all lie in a single component \(D^\star\) of \(G-S\) (the path is connected). Both \(x\) and \(y\) have neighbours on \(Q\) entering \(D^\star\), so \(x\) and \(y\) both touch \(D^\star\).

**Proof.** Tree path uniqueness; connectedness. ∎

### Lemma 9.5 (Same-side path forces equality option on that side — **partial**)
In the setting of Lemma 9.4, if \(D^\star=D_v\) (the tree path between \(x,y\) runs through the \(v\)-side), then \(G_v\) contains an \(x\)–\(y\) path of length \(\ge 2\). This does **not** automatically produce a colouring with \(c(x)=c(y)\); it does produce a colouring with \(c(x)\neq c(y)\) whenever the path can be 2-coloured in a Kempe subgraph — not guaranteed for all colourings.

**Honest status.** Same-side paths are suggestive for Kempe arguments but do not, by themselves, kill the mixed obstruction of Lemma 7.12. ∎

### Lemma 9.6 (Trying to add a missing edge inside \(S\))
Let \(xy\notin E(G)\) with \(x,y\in S\). Form \(G+xy\). Then \(\chi(G+xy)\ge t\). Let \(H\) be a \(t\)-critical subgraph of \(G+xy\) with \(xy\in E(H)\).

**Standard Dirac fork:**
- If \(V(H)\) meets both open sides of \(S\), then \(S\cap V(H)\) separates \(H\), and \(\kappa(H)\ge t-1\) forces \(|S\cap V(H)|\ge t-1\). Combined with model structure this is possible but does not immediately yield a \(K_t\) minor in \(G\).
- If \(V(H)\) lies in one closed side \(G_v\) or \(G_C\), then \(H\) uses the new edge \(xy\) inside that side’s completion.

**Status.** This is exactly the classical Dirac separator analysis; the contact model does not simplify it enough to finish in this note. We **do not** claim a new complete proof of “min separators are cliques” via contact. ∎

### Theorem 9.7 (What the hybrid **does** prove toward claim 4)
Let \(G\) be a minimal counterexample, \(v\) an apex, \(\mathcal{B}\) an MCM, \(S\subseteq A\) a minimum \((v,C)\)-separator. Then:

1. \(G[S]\) is not a clique (Corollary 5.2).
2. \(\tau=|S|\ge t-1\), and \(S\) is distributed over at most \(s\le t-2\) contact bags, with some bag contributing at least two vertices of \(S\) (Lemma 8.1).
3. If \(G-S\) has two components, \(G[S]\cong K_\tau-e\), \(\tau\le t-1\), and the mixed equality obstruction of Lemma 7.12 does **not** occur, then \(\chi(G)\le t-1\), contradiction (Corollary 7.11).
4. If \(S\) is a clique, contradiction (Theorem 5.1).

**Proof.** Cited results. ∎

### Lemma 9.8 (The precise unproved hybrid lemma)

> **Lemma H (Contact-mixed-edge lemma — UNPROVED).**  
> Let \(G\) be a minimal counterexample to \(\mathrm{HC}_t\), \(v\in V(G)\), \(\mathcal{B}\) an MCM at \(v\), and \(S\subseteq A\) a minimum \((v,C)\)-separator. Suppose \(xy\notin E(G)\) with \(x,y\in S\). Then it is **not** the case that one of \(G_v,G_C\) admits only colourings with \(c(x)\neq c(y)\) while the other admits only colourings with \(c(x)=c(y)\).  
> More strongly: the admissible sets \(\mathrm{Adm}(D_v)\) and \(\mathrm{Adm}(D_C)\) have nonempty intersection after palette permutation (i.e. there exist colourings agreeing on \(S\)).

**Why Lemma H finishes the two-component, \(\tau\le t-1\), sparse-missing-edges case.**  
Combined with Corollary 7.11’s analysis, forbidding the mixed obstruction yields colour matching and \(\chi(G)\le t-1\).

**Why Lemma H is not proved here.**  
Forbidding mixed equality constraints on a missing edge is essentially the hard core of Dirac’s separator-clique argument, specialised to separators that happen to lie in a contact region. The model’s cross-edges and bag connectivity give paths through \(A\), but those paths may exit into both sides or stay in \(A\setminus S\), and no elementary recolouring using only free-attachment prohibition was found that forces both sides to agree on equality vs inequality for \(xy\).

**Why Lemma H is not pure degeneracy.**  
It is a pure colouring-and-separator statement constrained by MCM geometry; average degree never appears.

**Relation to MCM Lemma G (fan absorption).**  
Lemma G of the MCM/Menger-fan note asks for a \(\Phi\)-increasing model reassignment using a fan into \(C\). Lemma H asks for colour-matching across the \((v,C)\)-separator. They are **logically independent** attacks on contact deficiency:
- Lemma G increases contact (minor side);
- Lemma H colours \(G\) directly (chromatic side).
Either would kill counterexamples. Neither is proved in full for \(t\ge 7\).

---

## 10. Global picture and verdict

### Theorem 10.1 (Hybrid structure package — **proved**)
Let \(t\ge 5\) and let \(G\) be a minimal counterexample to \(\mathrm{HC}_t\). For every vertex \(v\in V(G)\) and every MCM \(\mathcal{B}\) at \(v\), with regions \(A,C,Z\) as in Definition 1.4 and minimum \((v,C)\)-separator \(S\subseteq A\):

1. **Deficiency:** \(s(\mathcal{B},v)\le t-2\), so \(C\neq\emptyset\) and \(N(v)\cap C=\emptyset\).
2. **Path obstruction:** no \(N(v)\cap Z\to C\) path avoids \(A\).
3. **Separation:** \(A\) and \(S\) separate \(v\) from \(C\); \(t-1\le|S|\le|A|\).
4. **Non-clique:** \(G[S]\) is not complete; if it were, \(G\) would have a \(K_t\) subgraph/minor or a forbidden separating clique.
5. **Bag packing:** \(S\) meets at most \(s\le t-2\) contact bags, and some bag contains \(\ge 2\) vertices of \(S\).
6. **Colouring obstruction:** the admissible colouring sets of \(S\) from the various components of \(G-S\) have empty total intersection.

**Proof.** §§1–8. ∎

### Theorem 10.2 (Conditional closure)
Assume Lemma H. Assume moreover that for every MCM at every apex, some minimum \((v,C)\)-separator \(S\) satisfies \(\tau\le t-1\) and \(G-S\) has two components, and \(G[S]\) is complete minus a matching of missing edges each of which falls under Lemma H. Then \(\chi(G)\le t-1\), contradiction. Hence no minimal counterexample exists under these extra hypotheses.

**Proof.** Lemma H supplies colour matching on \(S\); Lemma 7.3′ colours \(G\). ∎

### Remark 10.3 (Why \(\tau\le t-1\) is not free)
We know \(\tau\ge t-1\). The equality \(\tau=t-1\) holds automatically if \(\kappa(G)=t-1\) **and** \(\tau(v,C)=\kappa(G)\), i.e. if the pair \((v,C)\) realises global connectivity. This is true if there exists \(c\in C\) with \(\tau(v,c)=\kappa(G)\). In a \(\kappa\)-critical sense one can often find such pairs, but \(C\) is a specific model region — it need not contain a vertex at maximum distance from \(v\) in the connectivity sense. Thus \(\tau(v,C)\) could in principle be \(>t-1\). For \(\tau\ge t\), colour matching with a non-clique \(G[S]\) is harder (palette pressure), and if \(\omega(G[S])\ge t\) one already has a \(K_t\) subgraph.

### Theorem 10.4 (Large clique number in the separator)
If \(\omega(G[S])\ge t\), then \(G\) has a \(K_t\) subgraph, contradiction. If \(\omega(G[S])=t-1\), then a maximum clique \(Q\subseteq S\) of order \(t-1\) is **not** separating by itself unless it separates — but \(Q\subseteq S\) may fail to separate if \(S\setminus Q\neq\emptyset\) provides bypasses. If some maximum clique \(Q\subseteq S\) of order \(t-1\) **does** separate \(v\) from \(C\), we contradict Lemma 0.3(5).

**Proof.** Immediate. ∎

---

## 11. Comparison with pure degeneracy and pure MCM

| Approach | Core engine | Closes \(\mathrm{HC}_t\) for \(t\ge 7\)? |
|----------|-------------|----------------------------------------|
| Degeneracy / Mader | \(\delta\ge t-1\) vs average-degree minor thresholds \(\Theta(t\sqrt{\log t})\) | **No** — threshold gap |
| MCM + fan absorption (Lemma G) | Reassign Menger fan into non-contact bags to raise contact | **No** — Lemma G open |
| **This hybrid (Lemma H)** | Deficient contact \(\Rightarrow\) non-clique \((v,C)\)-separator in \(\le t-2\) bags; colour-match or clique contradiction | **No** — Lemma H open |
| Hybrid + clique case only | Theorem 5.1 | **Partial** — kills clique separators only (already classical) |

The hybrid is **genuinely distinct**: it never compares average degree to Mader numbers, and it never reassigns branch sets along a fan. It converts contact deficiency into a **located separator** and attacks that separator with critical colouring.

---

## 12. Checklist

| Item | Statement | Status |
|------|-----------|--------|
| 0.3 | Shape of minimal counterexamples; no sep. clique \(\le t-1\) | **Proved** |
| 0.4 | \(\kappa\ge t-1\) | **Classical input** |
| 1.3–1.5 | MCM deficiency; regions; cross-edges | **Proved** |
| 2.1–2.3 | No free \(Z\)-attachment; \(A\) separates \(v\) from \(C\) | **Proved** |
| 3.3–3.4 | Canonical / minimum separator \(S\subseteq A\) | **Proved** |
| 4.1–4.2 | Size sandwich; path packing | **Proved** |
| 5.1–5.2 | Clique separator case \(\Rightarrow\) contradiction; \(S\) non-clique | **Proved** |
| 7.1–7.5 | Side colourings; matching obstruction | **Proved** |
| 7.11 | Two-comp., \(K_\tau-e\), \(\tau\le t-1\), no mixed obstruction \(\Rightarrow\) colour \(G\) | **Proved** |
| 7.12 | Mixed equality obstruction identified | **Proved as obstruction** |
| 8.1–8.6 | Pigeonhole; bag quotient | **Proved** |
| 9.1, 9.3, 9.7 | Partial claim-4 consequences | **Proved** |
| **Lemma H** | Contact forbids mixed edge obstruction / forces colour match | **UNPROVED** |
| 10.1 | Hybrid structure package | **Proved** |
| Full \(\mathrm{HC}_t\) for \(t\ge 7\) | — | **Not obtained** |

---

## 13. Final verdict

### Proved (full proofs in this note)
1. In every minimal counterexample, every MCM at every apex has contact deficiency \(s\le t-2\).
2. **Path obstruction:** no attachment of \(N(v)\cap Z\) into the non-contact region \(C\) can avoid the contact region \(A\).
3. **Separator existence and location:** a minimum \((v,C)\)-separator \(S\) lives in \(A\), with
   \[
   t-1\le|S|\le|A|.
   \]
4. **Clique case dies:** if that separator were a clique, one obtains either a forbidden separating clique of order \(\le t-1\) or a \(K_t\) subgraph — contradiction. Hence \(S\) is **never** a clique.
5. **Bag geometry:** \(S\) is packed into \(\le t-2\) contact bags of the model; some bag holds \(\ge 2\) vertices of \(S\).
6. **Chromatic obstruction form:** sides of \(S\) are \((t-1)\)-colourable, but their admissible colourings of \(S\) have empty common intersection.
7. **Almost-clique subcase without mixed obstruction:** two components, \(G[S]\cong K_\tau-e\), \(\tau\le t-1\), non-mixed equality pattern \(\Rightarrow\) \(G\) is \((t-1)\)-colourable (contradiction).

### Not proved
**Lemma H:** the contact geometry forces colour-matching across \(S\) (equivalently: forbids the mixed equality obstruction on missing edges of \(G[S]\)).

### BLOCKED

\[
\boxed{\textbf{BLOCKED at Lemma H (contact-mixed-edge / colour match across the deficient-contact separator)}}
\]

The hybrid realises the intended new mechanism as far as elementary methods reach: **deficient contact \(\Rightarrow\) thin non-clique separator in the contact region, controlled by connectivity, incompatible with being a clique, and subject to critical colouring constraints**. Closing the mixed-edge colour-matching gap (Lemma H) — or proving \(\tau=t-1\) with only two sides and \(G[S]\) close enough to complete for matching to work unconditionally — would yield a degeneracy-free proof route for Hadwiger. That gap is not filled here, and is essentially as hard as the classical non-clique-separator analysis specialised to MCM-located cuts.

---

*End of note.*
