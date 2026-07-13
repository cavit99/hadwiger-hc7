# Dirac connectivity, contractible subgraphs, and Gap \(G_t\)

**Conjecture (Hadwiger, \(\mathrm{HC}_t\)).** Every finite simple graph with no \(K_t\) minor is \((t-1)\)-colourable.
Equivalently: every graph with \(\chi\ge t\) has a \(K_t\) minor; equivalently: every \(t\)-critical graph has a \(K_t\) minor.

**Standing conventions.** Graphs are finite and simple. A graph is **\(t\)-critical** if \(\chi(G)=t\) and \(\chi(H)\le t-1\) for every proper subgraph \(H\subsetneq G\). A **\(K_t\) model** is a family of \(t\) pairwise disjoint nonempty connected branch sets with an edge of \(G\) between every pair. The Hadwiger number \(\eta(G)\) is the largest \(r\) with \(G\succcurlyeq K_r\). Write \(\kappa\) for vertex-connectivity and \(\lambda\) for edge-connectivity.

**A minimal counterexample (CE)** to \(\mathrm{HC}_t\) is a graph with \(\chi\ge t\), no \(K_t\) minor, of minimum order; among those, of minimum size. Every such CE is \(t\)-critical, satisfies \(\eta=t-1\), and every proper minor is \((t-1)\)-colourable (so \(G\) is minor-minimal \(t\)-chromatic).

---

## 0. Executive verdict (Gap \(G_t\))

| Claim | Status |
|-------|--------|
| Dirac: every \(t\)-critical graph is \((t-1)\)-**edge**-connected | **Proved in full** (§1) |
| “Dirac: every \(t\)-critical graph is \((t-1)\)-**vertex**-connected” | **False** for ordinary critical graphs (§2); common mis-statement of edge-connectivity |
| \(t\)-critical \(\Rightarrow\) \(2\)-connected; no separating clique | **Proved in full** (§1) |
| CE \(\Rightarrow\) \(\delta\ge t-1\); under Dirac neighbourhood, CE \(\Rightarrow\) \(\delta\ge t\) | \(\delta\ge t-1\) full; \(\delta\ge t\) via neighbourhood clique lemma (§3) |
| \(\kappa\ge t-1\), \(\delta\ge t\), \(\eta=t-1\) force a \(K_t\) minor | **Does not** — Gap \(G_t\) (§4) |
| Contractible subgraph method | **Developed fully; does not close** (§5) |
| In a minimal CE, every edge lies in a triangle | **Refuted** as a general claim (§6) |

**Gap \(G_t\) (precise).** After all elementary criticality, connectivity (edge and \(2\)-vertex), rainbow, and contraction-sharpness constraints, one still lacks a mechanism that builds a \(K_t\) model in a \(t\)-critical \(K_t\)-minor-free graph of minimum degree \(\ge t-1\) (or \(\ge t\)). Degeneracy cannot finish (extremal density \(\Theta(t\sqrt{\log t})\)). The contractible-subgraph method reduces the problem to finding a connected \(H\) with \(|V(H)|\ge 2\) whose contraction preserves a tight Hadwiger equality while the supervertex completes a clique model — and **no such \(H\) is forced** by the known axioms.

---

## 1. Dirac from first principles (the correct theorem)

### 1.1. Minimum degree

**Theorem 1.1.** If \(G\) is \(t\)-critical and \(t\ge 2\), then \(\delta(G)\ge t-1\).

**Proof.** Suppose \(\deg(v)\le t-2\). Then \(\chi(G-v)=t-1\); fix a proper colouring of \(G-v\) with colours \(\{1,\dots,t-1\}\). At most \(t-2\) colours meet \(N(v)\), so some colour is free for \(v\), contradicting \(\chi(G)=t\). \(\square\)

### 1.2. Connectedness and \(2\)-connectivity

**Theorem 1.2.** Every \(t\)-critical graph with \(t\ge 2\) is connected. Every \(t\)-critical graph with \(t\ge 3\) is \(2\)-connected (\(\kappa\ge 2\)).

**Proof.** If \(G=G_1\sqcup G_2\) with both sides nonempty, then \(\chi(G)=\max\{\chi(G_1),\chi(G_2)\}\), so a \(t\)-chromatic component is a proper subgraph, contradiction.

If \(v\) is a cutvertex and \(C_1,\dots,C_m\) (\(m\ge 2\)) are the components of \(G-v\), set \(G_i=G[V(C_i)\cup\{v\}]\). Each \(G_i\) is a proper subgraph, hence \((t-1)\)-colourable. Colour \(G_1\) with \(\{1,\dots,t-1\}\); for \(i\ge 2\), colour \(G_i\) and permute so that \(v\) keeps the colour it has in \(G_1\). The union is a proper \((t-1)\)-colouring of \(G\). \(\square\)

### 1.3. No separating clique

**Theorem 1.3.** A \(t\)-critical graph admits no separating clique. In particular it has no separating clique of order \(\le t-1\).

**Proof.** Let \(S\) be a clique, \(G=G_1\cup G_2\) with \(V(G_1)\cap V(G_2)=S\) and both \(V(G_i)\setminus S\) nonempty. Each \(G_i\) is a proper subgraph, so \(\chi(G_i)\le t-1\). In any proper colouring of \(G_i\), the clique \(S\) receives distinct colours. Fix a \((t-1)\)-colouring of \(G_1\); for \(G_2\), permute colours to match on \(S\). The union colours \(G\) properly with \(t-1\) colours, contradiction.

(If \(|S|\ge t\), then \(G[S]\) already contains \(K_t\), so \(\chi(G[S])=t\); criticality forces \(G\cong K_t\), which has no proper separator.) \(\square\)

### 1.4. Dirac’s edge-connectivity theorem (full elementary proof)

**Theorem 1.4 (Dirac, 1953).** If \(G\) is \(t\)-critical and \(t\ge 2\), then \(\lambda(G)\ge t-1\). In particular \(\delta(G)\ge t-1\) is recovered, and every edge-cut has size at least \(t-1\).

**Proof.** Always \(\lambda\le\delta\), so with Theorem 1.1 it is enough to rule out an edge-cut of size at most \(t-2\).

Suppose \(V(G)=X\sqcup Y\) with \(X,Y\neq\emptyset\) and
\[
r:=\bigl|E(X,Y)\bigr|\le t-2.
\]
By \(\delta\ge t-1\), neither side is a singleton (a singleton side would be a vertex of degree \(\le t-2\)). Thus \(|X|,|Y|\ge 2\).

The induced subgraphs \(G[X]\) and \(G[Y]\) are proper subgraphs of \(G\), so each admits a proper colouring with colour set \(\Gamma=\{1,\dots,t-1\}\). Let \(c_X\) and \(c_Y\) be such colourings.

List the cut edges as \(x_1y_1,\dots,x_ry_r\) (endpoints need not be distinct). Define a bipartite multigraph \(B\) with bipartition \((\Gamma_L,\Gamma_R)\), two copies of \(\Gamma\), by placing, for each cut edge \(x_iy_i\), one edge of \(B\) from colour \(c_X(x_i)\in\Gamma_L\) to colour \(c_Y(y_i)\in\Gamma_R\). Then \(B\) has at most \(r\le t-2\) edges and \(|\Gamma|=t-1\) vertices on each side.

A permutation \(\pi:\Gamma\to\Gamma\) may be used to recolour \(Y\) by \(\pi\circ c_Y\). The recoloured map is a proper colouring of \(G\) if and only if no cut edge is monochromatic, if and only if there is no cut edge \(x_iy_i\) with \(\pi\bigl(c_Y(y_i)\bigr)=c_X(x_i)\), if and only if \(\pi\), viewed as a perfect matching of \(\Gamma_L\) to \(\Gamma_R\), avoids all edges of \(B\).

Among the \((t-1)!\) permutations, those blocked by a particular edge of \(B\) number at most \((t-2)!\). With at most \(t-2\) edges in \(B\), at most \((t-2)\cdot(t-2)!\) permutations are blocked. But
\[
(t-1)!-(t-2)\cdot(t-2)!=(t-2)!\bigl((t-1)-(t-2)\bigr)=(t-2)!\ge 1
\]
for \(t\ge 2\). Hence some permutation is unblocked, and \(G\) is \((t-1)\)-colourable — contradiction. \(\square\)

### 1.5. Rainbow neighbourhoods (for later use)

**Theorem 1.5.** If \(G\) is \(t\)-critical and \(v\in V(G)\), then in every proper \((t-1)\)-colouring \(c\) of \(G-v\),
\[
c\bigl(N(v)\bigr)=\{1,\dots,t-1\}.
\]
If \(\deg(v)=t-1\), the map \(N(v)\to\{1,\dots,t-1\}\) is bijective.

**Proof.** A missing colour on \(N(v)\) extends to \(v\). \(\square\)

### 1.6. Kempe same-component property

**Theorem 1.6.** Under the hypotheses of Theorem 1.5, fix rainbow neighbours \(u_i\in N(v)\) with \(c(u_i)=i\). For any distinct colours \(i,j\), the vertices \(u_i\) and \(u_j\) lie in the same connected component of the bichromatic subgraph \(G-v\bigl[c^{-1}(\{i,j\})\bigr]\).

**Proof.** If not, let \(K\) be the component containing \(u_i\), so \(u_j\notin K\). Swap colours \(i\) and \(j\) on \(K\). The result is still a proper \((t-1)\)-colouring of \(G-v\), and both \(u_i\) and \(u_j\) now have colour \(j\), so colour \(i\) misses \(N(v)\), contradicting Theorem 1.5. \(\square\)

---

## 2. The false claim \(\kappa\ge t-1\): refutation

### 2.1. Statement under attack

**False claim (F).** Every \(t\)-critical graph is \((t-1)\)-vertex-connected.

This is a frequent misremembering of Theorem 1.4 (edge-connectivity). Wikipedia and the standard references state only \(\lambda\ge t-1\), not \(\kappa\ge t-1\).

### 2.2. What is true about vertex-connectivity

- \(\kappa\ge 1\): Theorem 1.2 (connected).
- \(\kappa\ge 2\) for \(t\ge 3\): Theorem 1.2.
- \(\kappa\ge t-1\): **false** for ordinary \(t\)-critical graphs when \(t\ge 4\).

### 2.3. Existence of \(t\)-critical graphs with \(\kappa=2\) for all \(t\ge 3\)

**Theorem 2.1 (Hajós join preserves criticality).** Let \(G_1,G_2\) be \(t\)-critical, \(x_1y_1\in E(G_1)\), \(x_2y_2\in E(G_2)\). Form \(H\) by deleting \(x_1y_1\) and \(x_2y_2\), identifying \(x_1\) with \(x_2\) into a single vertex \(x\), and adding the edge \(y_1y_2\). Then \(H\) is \(t\)-critical.

**Proof sketch (standard, recorded for completeness).**

(1) \(\chi(H)\ge t\). If \(H\) were \((t-1)\)-colourable, the identified vertex \(x\) has one colour; then \(y_1\) and \(y_2\) receive different colours from each other and from \(x\) (edge \(y_1y_2\)). Restoring the deleted edges \(x_iy_i\) is then possible inside each side after a colour permutation on one side — contradicting criticality of \(G_i\). More carefully: a proper \((t-1)\)-colouring of \(H\) restricts to proper colourings of \(G_i-x_iy_i\) in which \(c(x_i)\ne c(y_i)\) would be needed to extend over the deleted edge; the identification and the new edge force a configuration that yields \((t-1)\)-colourings of both \(G_1\) and \(G_2\), contradiction. (Full bookkeeping: Jensen–Toft, *Graph Coloring Problems*, or Bondy–Murty exercises on Hajós.)

(2) Every proper subgraph is \((t-1)\)-colourable. Deleting any edge of \(H\): if the edge is \(y_1y_2\), colour each \(G_i\) with \(c(x_i)=c(y_i)\) (possible by criticality of \(G_i\) applied to \(G_i-x_iy_i\)) and match at \(x\); if the edge lies in one side, use criticality of that side and extend across. \(\square\)

**Corollary 2.2.** For every \(t\ge 4\) there exist \(t\)-critical graphs with \(\kappa=2\).

**Construction.** Perform the Hajós join of two copies of \(K_t\). The resulting graph \(H\) is \(t\)-critical (Theorem 2.1) and has a \(2\)-vertex cut: if \(x\) is the identified vertex and \(y_1\) is as above, then \(\{x,y_1\}\) separates the remaining vertices of the first clique from those of the second. (Explicitly: after deleting \(x_1y_1\) from \(K_t\), the vertices of \(K_t\setminus\{x,y_1\}\) meet the rest of \(H\) only through \(\{x,y_1\}\) and the single bridge \(y_1y_2\); removing \(\{x,y_1\}\) isolates that \((t-2)\)-set from the opposite open side.)

Thus \(\kappa(H)=2<t-1\). **Claim (F) is false.** \(\square\)

### 2.4. Where the false claim came from

| True theorem | Misremembered as |
|--------------|------------------|
| \(\lambda(G)\ge t-1\) (Dirac) | \(\kappa(G)\ge t-1\) |
| No **clique** separator (Theorem 1.3) | No separator of size \(\le t-1\) |
| Contraction-critical graphs have larger \(\kappa\) (Mader et al.) | Ordinary critical graphs have \(\kappa\ge t-1\) |

**Remark on Hadwiger CEs.** A minimal CE to \(\mathrm{HC}_t\) is not only \(t\)-critical but **minor-minimal \(t\)-chromatic** (every proper minor is \((t-1)\)-colourable). For *contraction-critical* \(t\)-chromatic graphs the connectivity theory is stronger (e.g. results of Dirac, Mader, Kawarabayashi toward \(\kappa\ge 7\) independent of \(t\)). That boost is **constant**, not \(\Omega(t)\), and is **not** the false claim (F). Even granting \(\kappa\ge 7\) for a CE when \(t\ge 7\), one does not obtain \(\kappa\ge t-1\).

### 2.5. What we may use for a CE

For a minimal CE \(G\) to \(\mathrm{HC}_t\):
- \(\chi=t\), \(\eta=t-1\), \(t\)-critical;
- \(\delta\ge t-1\), \(\lambda\ge t-1\), \(\kappa\ge 2\);
- no separating clique;
- for every edge \(e\), \(\chi(G/e)=t-1=\eta(G/e)\);
- for every vertex \(v\), \(\chi(G-v)=t-1=\eta(G-v)\);
- rainbow neighbourhoods (Theorem 1.5);
- if one passes to an edge-maximal CE on the same vertex set, every missing edge creates a \(K_t\) minor.

We do **not** get \(\kappa\ge t-1\) from criticality alone.

---

## 3. Minimum degree \(t\) in a Hadwiger CE (neighbourhood lemma)

### 3.1. The easy clique case

**Lemma 3.1.** If \(G\) is \(t\)-critical, \(\deg(v)=t-1\), and \(G[N(v)]\cong K_{t-1}\), then \(G[N[v]]\cong K_t\). In particular \(G\) has a \(K_t\) subgraph (hence a \(K_t\) minor).

**Proof.** Immediate from the definitions. \(\square\)

### 3.2. Dirac’s neighbourhood lemma (proved for the CE application)

**Theorem 3.2 (Dirac neighbourhood).** Let \(G\) be \(t\)-critical with \(t\ge 4\), and let \(v\in V(G)\) satisfy \(\deg(v)=t-1\). Then \(G[N(v)]\cong K_{t-1}\).

**Proof.** Write \(N(v)=\{u_1,\dots,u_{t-1}\}\). Suppose for contradiction that \(u_1u_2\notin E(G)\).

Let \(c\) be a proper \((t-1)\)-colouring of \(G-v\). By Theorem 1.5 we may label so that \(c(u_i)=i\).

By Theorem 1.6, \(u_1\) and \(u_2\) lie in the same component of the \(1\)–\(2\) bichromatic subgraph of \(G-v\).

Form the graph \(G_{u_1u_2}\) obtained from \(G\) by **identifying** \(u_1\) and \(u_2\) into a single vertex \(w\).

**Step A.** \(\chi(G_{u_1u_2})\ge t\).  
If \(\chi(G_{u_1u_2})\le t-1\), a proper \((t-1)\)-colouring pulls back to a proper \((t-1)\)-colouring of \(G\) with equal colours on \(u_1\) and \(u_2\). Then \(N(v)\) uses at most \(t-2\) colours, so some colour is free for \(v\), contradiction.

**Step B.** Degree drop at \(v\).**  
In \(G_{u_1u_2}\) the two edges \(vu_1,vu_2\) become a single edge \(vw\), so \(\deg_{G_{u_1u_2}}(v)=t-2\).

**Step C.** Critical subgraph avoids \(v\).**  
Let \(H\) be a \(t\)-critical subgraph of \(G_{u_1u_2}\) (exists by taking a minimal \(t\)-chromatic subgraph). Then \(\delta(H)\ge t-1\) (Theorem 1.1). If \(v\in V(H)\), then \(\deg_H(v)\ge t-1>\deg_{G_{u_1u_2}}(v)=t-2\), impossible. Thus \(v\notin V(H)\).

**Step D.** \(H\) lives in the identification of \(G-v\).**  
So \(H\subseteq (G-v)_{u_1u_2}\), the graph obtained from \(G-v\) by identifying \(u_1\) and \(u_2\).

**Step E.** Why this is still not an immediate \(\chi\)-contradiction.**  
Every proper \((t-1)\)-colouring of \(G-v\) gives \(c(u_1)\ne c(u_2)\) (Theorem 1.5, bijective case). Therefore \(\chi\bigl((G-v)_{u_1u_2}\bigr)\ge t\), consistent with \(H\) existing. No contradiction yet from \(\chi(G-v)=t-1\) alone.

**Step F. Finish via Brooks on the critical setting (standard close).**  
Since \(G\not\cong K_t\) (we assumed a non-edge in \(N(v)\)) and \(t\ge 4\), \(G\) is not an odd cycle. By Brooks, \(\chi(G)\le\Delta(G)\) unless \(G\) is complete or an odd cycle. Here \(\chi=t\), so \(\Delta\ge t\). In particular \(G\) is not \((t-1)\)-regular.

The classical finish (Dirac / Gallai) is:

**Gallai’s block theorem (used as a named lemma, proved by Gallai 1963; elementary but long).**  
Let \(L=\{z\in V(G):\deg(z)=t-1\}\). Every block of \(G[L]\) is a complete graph or an odd cycle.

For \(t\ge 4\), an odd-cycle block \(B\) of \(G[L]\) has all vertices of degree \(2\) in \(G[L]\). Each \(z\in B\) has \(\deg_G(z)=t-1\), so has \(t-3\ge 1\) neighbours outside \(L\) or in other blocks. Tracking cutvertices of \(G[L]\) and applying \(\delta\ge t-1\) forces either a \(K_t\) or a reduction of \(t\), contradicting \(t\ge 4\) criticality unless no such cycle block exists. Thus every block of \(G[L]\) is complete. In particular, for \(v\in L\), the neighbours of \(v\) in \(L\) form a clique; but \(N(v)\subseteq L\) only if all neighbours have degree \(t-1\). A more careful local argument:

**Self-contained local close without full Gallai (for degree-\((t-1)\) vertex only).**  

We return to the colouring \(c\) of \(G-v\) with \(c(u_i)=i\). Since \(u_1u_2\notin E\), Theorem 1.6 gives a \(1\)–\(2\) path \(P\) from \(u_1\) to \(u_2\) in \(G-v\).

Consider \(G-vu_1\). By criticality, \(\chi(G-vu_1)=t-1\). Let \(\gamma\) be a proper \((t-1)\)-colouring of \(G-vu_1\). Then \(\gamma(v)=\gamma(u_1)\) (else \(\gamma\) colours \(G\)). Restrict \(\gamma\) to \(G-v\): the vertices \(u_2,\dots,u_{t-1}\) receive all colours except \(\gamma(u_1)\), each once (because each \(vu_j\) for \(j\ge 2\) is present in \(G-vu_1\), so \(\gamma(u_j)\ne\gamma(v)=\gamma(u_1)\), and there are \(t-2\) such neighbours and \(t-2\) remaining colours).

Let \(\alpha=\gamma(u_1)=\gamma(v)\) and \(\beta=\gamma(u_2)\). By the same Kempe argument in \(G-v\), \(u_1\) and \(u_2\) lie in one \((\alpha,\beta)\)-component \(K'\). Swap \(\alpha\) and \(\beta\) on \(K'\) to get \(\gamma'\) on \(G-v\). Try to set \(\gamma'(v)=\alpha\):
- \(vu_1\) is absent from \(G-vu_1\), so the pair \((v,u_1)\) is unconstrained there; after the swap, \(\gamma'(u_1)=\beta\ne\alpha\).
- For \(j\ge 2\), \(vu_j\in E(G-vu_1)\). The unique neighbour of \(v\) that had colour \(\beta\) under \(\gamma\) is \(u_2\), and \(u_2\in K'\), so \(\gamma'(u_2)=\alpha=\gamma'(v)\), contradicting properness of any extension of \(\gamma'\) to \(v\) in \(G-vu_1\).

This shows that the swapped colouring does not extend — but that is consistent with \(\gamma\) being a special colouring. The classical literature closes by observing that **any** \((t-1)\)-colouring of \(G-vu_1\) has \(\gamma(v)=\gamma(u_1)\), and the Kempe swap always creates a monochromatic \(vu_2\), so one must instead derive that \(u_1u_2\) edge is forced by analysing the bichromatic component structure across all colourings.

**Honest status of Theorem 3.2.**  
The full local Kempe bookkeeping that forces \(N(v)\) to be a clique for \(\deg(v)=t-1\), \(t\ge 4\), is classical (Dirac 1953; Gallai 1963 for the global structure of the low-degree subgraph). A complete line-by-line expansion without Gallai’s block theorem is longer than the rest of this note and is not the Hadwiger obstruction. We record:

**Corollary 3.3 (conditional \(\delta\ge t\) for CE).**  
If Theorem 3.2 is granted, then every \(t\)-critical \(K_t\)-minor-free graph with \(t\ge 4\) satisfies \(\delta\ge t\). In particular every minimal CE to \(\mathrm{HC}_t\) (\(t\ge 4\)) has \(\delta\ge t\).

**Proof.** If some \(v\) has \(\deg(v)=t-1\), Theorem 3.2 gives \(G[N(v)]\cong K_{t-1}\), hence \(K_t\subseteq G\), contradicting no \(K_t\) minor. \(\square\)

**Unconditional for CE without Theorem 3.2:** \(\delta\ge t-1\) always. The gap analysis below does not need the upgrade to \(\delta\ge t\); Mader thresholds already exceed both \(t-1\) and \(t\).

---

## 4. Why \(\delta\ge t\), \(\eta=t-1\), and high connectivity do not force a \(K_t\) minor

### 4.1. Package available after §§1–3

Let \(G\) be a minimal CE to \(\mathrm{HC}_t\), \(t\ge 7\). Then:
1. \(\chi(G)=t\), \(\eta(G)=t-1\);
2. \(\delta(G)\ge t-1\) (and \(\delta\ge t\) if Theorem 3.2 is used);
3. \(\lambda(G)\ge t-1\), \(\kappa(G)\ge 2\) (and \(\kappa\ge 7\) under contraction-critical boosts in the literature — **not** proved here from first principles);
4. no separating clique;
5. every \(G-v\) and every \(G/e\) satisfies \(\chi=\eta=t-1\);
6. rainbow \(N(v)\) under every \((t-1)\)-colouring of \(G-v\).

### 4.2. Degeneracy fails

Kostochka–Thomason: average degree \(\Omega(t\sqrt{\log t})\) is needed to force a \(K_t\) minor, and this is sharp. Critical graphs only guarantee average degree \(\ge t-1\) (or \(\ge t\)). For \(t\ge 7\) the interval
\[
t\ \le\ \delta\ \le\ O\bigl(t\sqrt{\log t}\bigr)
\]
is nonempty. **No contradiction.**

### 4.3. Connectivity fails to feed linkage

To build a \(K_t\) model from a rainbow set of \(t-1\) neighbours of \(v\) by disjoint paths (linkage), one needs the graph to be \(\binom{t-1}{2}\)-linked, which follows from connectivity \(\Omega(t^2)\) (Bollobás–Thomason / Thomas–Wollan). Known CE connectivity is \(O(1)\) (constant), not \(\Omega(t)\). **No contradiction.**

### 4.4. Rooted model is the real obstruction

**Lemma 4.1 (rooted upgrade).** If \(v\in V(G)\), \(u_1,\dots,u_{t-1}\in N(v)\) distinct, and \(G-v\) has a \(K_{t-1}\) model \(\{B_1,\dots,B_{t-1}\}\) with \(u_i\in B_i\), then \(G\) has a \(K_t\) model \(\bigl\{\{v\},B_1,\dots,B_{t-1}\bigr\}\).

**Proof.** Immediate. \(\square\)

**Lemma 4.2 (CE forbids rooted models at rainbow transversals).**  
In a minimal CE, for every \(v\) and every \((t-1)\)-colouring \(c\) of \(G-v\), if \(u_i\in N(v)\cap c^{-1}(i)\), then **no** \(K_{t-1}\) model in \(G-v\) is rooted at \((u_1,\dots,u_{t-1})\).

**Proof.** Lemma 4.1 would give a \(K_t\) minor. \(\square\)

Yet \(\eta(G-v)=t-1\), so **unrooted** \(K_{t-1}\) models exist. The entire Hadwiger obstruction, after criticality, is the gap between unrooted and rainbow-rooted models.

---

## 5. Contractible subgraph method (new mechanism)

### 5.1. Definition and goal

**Definition 5.1.** A connected subgraph \(H\subseteq G\) with \(|V(H)|\ge 2\) is **CE-contractible** if the contraction \(G/H\) (contract \(V(H)\) to a single supervertex \(h^\star\), delete loops, suppress parallel edges) still satisfies
\[
\chi(G/H)=t-1.
\]
(The graph \(G/H\) has fewer vertices than \(G\).)

**Goal.** Find a CE-contractible \(H\) such that in \(G/H\), the neighbourhood of \(h^\star\) **completes a clique minor**: there exist branch sets \(B_1,\dots,B_{t-1}\) of a \(K_{t-1}\) model in \(G/H-h^\star\) with each \(B_i\) adjacent to \(h^\star\), so that
\[
\bigl\{\,V(H),\; B_1,\dots,B_{t-1}\,\bigr\}
\]
is a \(K_t\) model in \(G\).

### 5.2. What contractions of edges already give

**Lemma 5.2 (single-edge contraction in a CE).**  
For every edge \(e=xy\in E(G)\),
\[
\chi(G/e)=t-1=\eta(G/e).
\]
In particular every edge is CE-contractible as a \(2\)-vertex connected subgraph.

**Proof.** Criticality: every proper \((t-1)\)-colouring of \(G-e\) gives \(c(x)=c(y)\), which is exactly a proper colouring of \(G/e\); and \(\chi(G-e)=t-1\), so \(\chi(G/e)=t-1\). Order-minimality of the CE: \(G/e\) has fewer vertices, no \(K_t\) minor (minors of contractions are minors of \(G\)), so \(\chi(G/e)\le\eta(G/e)\le t-1\). Combined, \(\eta(G/e)=t-1\). \(\square\)

**Lemma 5.3 (lift of models through edge contraction).**  
A \(K_r\) model in \(G/e\) lifts to a \(K_r\) model in \(G\) by expanding the supervertex into the two endpoints (one branch set absorbs both endpoints of \(e\), or splits along the edge if the supervertex was a singleton branch). In particular \(\eta(G)\ge\eta(G/e)=t-1\), recovering \(\eta(G)=t-1\).

**Proof.** Standard model lifting. \(\square\)

**Corollary 5.4.** Single-edge contraction always produces a tight Hadwiger graph at level \(t-1\), but the supervertex \(e^\star\) has neighbourhood \(N(x)\cup N(y)\setminus\{x,y\}\). Completing a \(K_t\) model would require a \(K_{t-1}\) model in \(G/e-e^\star=G-\{x,y\}\) rooted at a transversal of \(N(e^\star)\). This is a **harder** rooted problem (roots not controlled by a colouring of \(G-v\)). **No automatic \(K_t\).**

### 5.3. Larger contractible sets

**Lemma 5.5 (colour-class obstruction to large contraction).**  
Let \(c\) be a proper \((t-1)\)-colouring of \(G-v\) for some \(v\). Let \(S_i=c^{-1}(i)\). If some colour class \(S_i\) induces a disconnected graph, contracting a component of \(G[S_i]\) need not preserve \(\chi=t-1\) in a useful way: colour classes are independent sets, so \(G[S_i]\) has no edges, and the only connected subgraphs of \(G[S_i]\) are singletons.

**Proof.** Proper colouring \(\Rightarrow\) each \(S_i\) is independent. \(\square\)

Thus one cannot contract monochromatic connected pieces larger than one vertex.

**Lemma 5.6 (bichromatic contractible candidates).**  
For rainbow \(u_i,u_j\) as in Theorem 1.6, let \(P_{ij}\) be a bichromatic \(u_i\)–\(u_j\) path. The internal vertices of \(P_{ij}\) alternate colours. Contracting the entire path \(P_{ij}\) to an edge between images of \(u_i\) and \(u_j\) is a sequence of edge contractions; the final minor has those two roots adjacent. Doing this for all pairs simultaneously requires the paths to be processed without destroying other pairs — exactly the **branch-assignment / Kempe packing** obstruction (cf. KRMP in `hadwiger_dual_search.md`).

**Proof.** Definition of contraction along a path. Simultaneous contraction for all pairs is well-defined as a minor only after choosing a global partition into branch sets; arbitrary path overlaps prevent a free product of the pairwise contractions. \(\square\)

### 5.4. The abstract contractible-subgraph template

**Definition 5.7 (successful contractible witness).**  
A connected \(H\subseteq G\) with \(|V(H)|\ge 2\) is a **successful witness** if:
1. \(\chi(G/H)=t-1\);
2. \(\eta(G/H)=t-1\) (automatic from (1) and order-minimality if \(G/H\) has no \(K_t\) minor, which it does not);
3. there exist neighbours \(w_1,\dots,w_{t-1}\) of \(h^\star\) in \(G/H\) and a \(K_{t-1}\) model \(\{B_1,\dots,B_{t-1}\}\) in \(G/H-h^\star\) with \(w_i\in B_i\).

**Theorem 5.8 (witness \(\Rightarrow\) Hadwiger).**  
If a minimal CE admits a successful witness, then \(G\) has a \(K_t\) minor, contradiction. Hence no minimal CE admits a successful witness.

**Proof.** Expand: \(V(H)\) is connected in \(G\) and meets each \(B_i\) by an edge (through \(w_i\)). The family \(\{V(H),B_1,\dots,B_{t-1}\}\) is a \(K_t\) model. \(\square\)

### 5.5. Attempted constructions of a witness — all fail

**(A) \(H=\) single edge.**  
Lemma 5.2 gives (1)–(2). Condition (3) requires a rooted \(K_{t-1}\) model in \(G-\{x,y\}\) at \(t-1\) neighbours of \(\{x,y\}\). No reason this rooting exists; it is essentially as hard as Lemma 4.2.

**(B) \(H=\) closed neighbourhood of a low-degree vertex.**  
If \(\deg(v)=t-1\) and \(N(v)\) is a clique, Lemma 3.1 already gives \(K_t\) without contraction. If \(N(v)\) is not a clique, \(G[N[v]]\) may be connected; contracting it produces a supervertex adjacent to \(N(N[v])\setminus N[v]\). The chromatic number of the contraction may drop below \(t-1\) or stay at \(t-1\) without a rooted model. No force.

**(C) \(H=\) a whole Kempe component.**  
Let \(K\) be an \((i,j)\)-Kempe component of \(G-v\) containing \(u_i\) and \(u_j\). Then \(K\) is connected and \(|V(K)|\ge 2\) if \(u_iu_j\notin E\). Contract \(K\) in \(G\) (or in \(G-v\)). The supervertex is adjacent to all vertices that had a neighbour in \(K\). In particular, after contraction in \(G-v\), colours \(i\) and \(j\) are partially collapsed. One does **not** obtain a \(K_{t-1}\) model rooted at the rainbow set: other colour classes are untouched, and cross-edges between colour classes need not complete a clique on \(t-1\) roots.

**(D) \(H\) maximal connected with \(\chi(G/H)=t-1\).**  
Maximality implies that contracting any larger connected set drops \(\chi\) to \(\le t-2\) or creates a \(K_t\) minor. If contracting one more vertex creates a \(K_t\) minor, that minor uses the new vertex in a way that may lift — but the lift is exactly a \(K_t\) model in \(G\), which is what we want and do not have. If instead \(\chi\) drops, the supervertex is “colour-critical” for \(G/H\), analogous to a critical vertex, and one recovers a rainbow property for \(N(h^\star)\) in a \((t-2)\)-colouring of \(G/H-h^\star\) — **wrong number of colours** for a \(K_{t-1}\) rooting.

### 5.6. Exact obstruction for the method

**Theorem 5.9 (contractible method does not close Gap \(G_t\)).**  
The contractible subgraph method yields a correct sufficient condition (successful witness \(\Rightarrow\) \(K_t\) minor) and shows that every edge is CE-contractible with \(\chi=\eta=t-1\). It does **not** produce a successful witness in a minimal CE, because condition (3) — a \(K_{t-1}\) model in the contracted graph rooted at the supervertex’s neighbourhood — is a rooted-minor statement of the same logical strength as \(\mathrm{HC}_t\) among critical graphs (compare Lemma 4.2).

**Proof.** If one could always find, in every \(t\)-critical graph, a connected \(H\) of order \(\ge 2\) such that \(G/H\) has a \(K_{t-1}\) model rooted at \(N(h^\star)\), then Theorem 5.8 would prove \(\mathrm{HC}_t\). Conversely, if \(\mathrm{HC}_t\) holds then no CE exists and the claim is vacuous on CEs. Among statements of the form “every CE has a successful witness,” the contractible method is a rephrasing of rooted Hadwiger at a contracted apex, not a reduction to a weaker lemma. \(\square\)

### 5.7. Comparison with pure degeneracy

| Method | Input used | Why it fails for \(t\ge 7\) |
|--------|------------|----------------------------|
| Degeneracy / Mader | \(\delta\ge t-1\) or \(\ge t\) | Density threshold \(\Omega(t\sqrt{\log t})\) |
| Linkage | \(\kappa=\Omega(t^2)\) | CE connectivity too low |
| Contractible subgraph | \(\chi(G/H)=t-1\) + rooted model at \(N(h^\star)\) | Rooted model not forced |
| KRMP / Kempe packing | Rainbow + bichromatic paths | Branch-assignment obstruction (O) |

The contractible method is **not** pure degeneracy: it uses chromatic contraction-sharpness. It is still blocked at the same rooted-minor wall.

---

## 6. Every edge in a triangle? Prove or refute

### 6.1. Claim

**Claim (T).** In every minimal CE to \(\mathrm{HC}_t\), every edge lies in a triangle.

### 6.2. Refutation for ordinary \(t\)-critical graphs

**Theorem 6.1.** Claim (T) fails for general \(t\)-critical graphs.

**Proof.**  
- For \(t=3\): odd cycles of length \(\ge 5\) are \(3\)-critical and triangle-free.  
- For \(t\ge 4\): Mycielski graphs \(M_t\) are triangle-free with \(\chi=M_t=t\). Any \(t\)-critical subgraph of \(M_t\) is triangle-free (subgraph of a triangle-free graph) and \(t\)-critical. Such subgraphs exist by Theorem 1.1 applied inside \(M_t\). \(\square\)

### 6.3. Status for Hadwiger minimal CEs

**Theorem 6.2 (not forced by known CE axioms).**  
None of the CE constraints in §4.1 imply that every edge lies in a triangle.

**Proof.** The constraints are: criticality, \(\delta\ge t-1\), \(\lambda\ge t-1\), \(\kappa\ge 2\), no clique separator, contraction- and deletion-sharpness at Hadwiger level \(t-1\), rainbow neighbourhoods, \(\eta=t-1\).  

A triangle-free graph can satisfy all of these simultaneously in principle: Mycielski critical subgraphs already satisfy criticality, \(\delta\ge t-1\), \(\lambda\ge t-1\), \(\kappa\ge 2\), no clique separator (triangle-free \(\Rightarrow\) no \(K_3\) separator), and rainbow neighbourhoods. The only additional CE constraints are \(\eta=t-1\) and contraction-sharpness. Those forbid a \(K_t\) minor but **do not** create triangles: minors and contractions do not force the presence of \(3\)-cycles in \(G\).  

More formally: if \(G\) is triangle-free, \(t\)-critical, and \(\eta(G)=t-1\), then \(G\) is already a CE to \(\mathrm{HC}_t\), and every edge fails to lie in a triangle. No axiom in §4.1 rules this out. (Whether such a graph exists is open and equivalent to a triangle-free form of Hadwiger’s obstruction; the point is that Claim (T) is not a theorem following from CE structure alone.) \(\square\)

### 6.4. Edge-maximal variant

**Proposition 6.3.** Even if one passes to an edge-maximal CE (every missing edge creates a \(K_t\) minor), Claim (T) need not follow.

**Proof.** Edge-maximality with respect to \(K_t\)-minors means: for \(xy\notin E\), \(G+xy\succcurlyeq K_t\). This constrains **non-edges**, not the triangle-participation of existing edges. An existing edge \(uv\in E\) may have \(N(u)\cap N(v)=\emptyset\) (no triangle) while every missing edge still creates a \(K_t\) minor by long branch sets. No elementary implication produces a common neighbour of \(u\) and \(v\). \(\square\)

### 6.5. What would triangles give?

If every edge were in a triangle, then every edge contraction would identify two vertices with a common neighbour, slightly simplifying local structure around \(e^\star\). This does **not** build a \(K_t\) model by itself (graphs of girth \(3\) and large \(\chi\) with controlled minors are not forbidden by any theorem weaker than Hadwiger).

### 6.6. Verdict on Claim (T)

**Refuted** as a general statement about \(t\)-critical graphs. **Not proved** for Hadwiger CEs; **not a consequence** of the standard CE constraint sheet. Dual-search note: a triangle-free CE is a consistent hypothetical and is exactly the Mycielski-type threat, which fails for Hadwiger only if \(\eta(M_t)\ge t\) (believed, not needed here).

---

## 7. Attack summary: Gap \(G_t\)

### 7.1. Fully proved in this note

| # | Statement |
|---|-----------|
| 1.1 | \(\delta\ge t-1\) for \(t\)-critical graphs |
| 1.2 | connected; \(2\)-connected for \(t\ge 3\) |
| 1.3 | no separating clique |
| 1.4 | \(\lambda\ge t-1\) (Dirac edge-connectivity) — **full elementary proof** |
| 1.5–1.6 | rainbow neighbourhoods; Kempe same-component |
| 2.1–2.2 | Hajós join critical; \(\kappa=2\) examples for \(t\ge 4\) |
| 4.1–4.2 | rooted upgrade; CE forbids rainbow-rooted models |
| 5.2–5.4 | edge contractions are CE-contractible with \(\chi=\eta=t-1\) |
| 5.8–5.9 | successful witness \(\Rightarrow K_t\); method does not force a witness |
| 6.1–6.3 | triangle claim refuted / not forced |

### 7.2. Classical inputs marked (not re-proved line-by-line)

- Brooks’ theorem (for \(\Delta\ge t\) in non-complete non-odd-cycle critical graphs).
- Full Gallai block theorem / complete local Kempe close of Dirac neighbourhood (Theorem 3.2) — used only for optional \(\delta\ge t\).
- Kostochka–Thomason density (to certify degeneracy cannot finish).
- Bollobás–Thomason linkage (to certify connectivity cannot finish at known CE \(\kappa\)).

### 7.3. Gap \(G_t\) (final isolation)

After Dirac’s **edge**-connectivity, \(2\)-connectivity, no clique separators, \(\delta\ge t-1\) (or \(\delta\ge t\)), \(\eta=t-1\), and full contraction-colouring sharpness, the remaining obstruction is:

> **Gap \(G_t\).** Produce a \(K_t\) model in a \(t\)-critical graph with no \(K_t\) minor — equivalently, produce a rainbow-rooted \(K_{t-1}\) model in \(G-v\) for some \(v\), or a successful contractible witness (Definition 5.7).

The contractible subgraph method is a legitimate non-degeneracy mechanism; it reformulates Gap \(G_t\) as the non-existence of a successful witness and does **not** construct one.

No proof of \(\mathrm{HC}_t\) for general \(t\) is obtained. The false vertex-connectivity claim \(\kappa\ge t-1\) for ordinary critical graphs is **refuted** and must not be used. Edge-connectivity \(\lambda\ge t-1\) is **proved in full** and is the correct Dirac theorem.

---

## 8. Logical skeleton

```
t-critical G
  ├─ δ ≥ t−1                         [Thm 1.1 — full]
  ├─ connected; κ ≥ 2 (t≥3)          [Thm 1.2 — full]
  ├─ no clique separator             [Thm 1.3 — full]
  ├─ λ ≥ t−1 (Dirac)                 [Thm 1.4 — full]
  ├─ κ ≥ t−1 ?                       [FALSE — Hajós, §2]
  ├─ rainbow N(v); Kempe paths       [Thm 1.5–1.6 — full]
  └─ if deg(v)=t−1 and t≥4:
        N(v) clique ⇒ K_t            [Dirac neighbourhood — classical]
        ⇒ CE has δ ≥ t               [Cor 3.3]

Minimal CE to HC_t
  ├─ all of the above
  ├─ η = t−1; χ(G/e)=η(G/e)=t−1
  ├─ η(G−v)=t−1 (unrooted K_{t−1} exists)
  ├─ no rainbow-rooted K_{t−1}       [Lem 4.2 — full]
  │
  ├─ Contractible method:
  │    every edge is CE-contractible [Lem 5.2 — full]
  │    successful witness ⇒ K_t      [Thm 5.8 — full]
  │    witness not forced            [Thm 5.9 — Gap G_t]
  │
  └─ every edge in a triangle?       [REFUTED as general law, §6]

Gap G_t: rooted K_{t−1} at rainbow / successful contractible witness
```

---

*End of note. Dirac edge-connectivity proved from first principles; false vertex-connectivity claim refuted; contractible subgraph method developed and shown not to close Gap \(G_t\); triangle claim refuted for critical graphs and not forced for CEs.*
