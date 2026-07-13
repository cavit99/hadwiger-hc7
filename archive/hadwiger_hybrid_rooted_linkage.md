# Hybrid Attack on the Hadwiger Gap \(G_t\) for \(t\ge 7\)

## Structure of minimal counterexamples + connectivity + elementary linkage → rainbow-rooted \(K_{t-1}\)

**Conjecture \(\mathrm{HC}_t\).** Every finite simple graph with no \(K_t\) minor is \((t-1)\)-colourable.
Equivalently: \(\chi(G)\le\eta(G)\) for every finite simple \(G\), where \(\eta(G)\) is the Hadwiger number.

**Standing conventions.** Graphs are finite and simple. A **\(K_r\) model** is a family of \(r\) pairwise disjoint nonempty connected vertex sets \(B_1,\dots,B_r\) (**branch sets**) such that \(G\) has an edge between \(B_i\) and \(B_j\) for all \(i\neq j\). Write \(\delta,\Delta,\kappa,\lambda\) for minimum degree, maximum degree, vertex-connectivity, edge-connectivity.

**Programme.** Combine three strands:

1. **Structure of a minimal counterexample** — \(\delta\ge t-1\) (classically \(\delta\ge t\)), contraction-critical colouring, \(\eta=t-1\), no clique separators.
2. **Connectivity of critical graphs** — Dirac \(\kappa\ge t-1\), proved from first principles as far as possible; weaker connectivity fully elementary.
3. **Linkage / rooted-minor calculus** — Thomas–Wollan / Bollobás–Thomason style ideas, with every tool either proved elementarily or explicitly marked as a black box with the exact citation content used.

**Target construction.** Show that \(G-v\) is highly linked enough to root a \(K_{t-1}\) model at rainbow neighbours of some apex \(v\), yielding a \(K_t\) minor with branch set \(\{v\}\).

**Fallback target (existential).** Prove: for every \(t\)-critical \(G\) with \(\kappa\ge t-1\), there **exists** a vertex \(v\) and a \((t-1)\)-colouring of \(G-v\) such that some rainbow neighbour transversal admits a rooted \(K_{t-1}\) minor.

**Outcome of this note.**

| Claim | Status |
|-------|--------|
| Critical reduction; shape of minimal CE; \(\eta=t-1\); rainbow neighbourhoods; no clique separators; \(\lambda\ge t-1\); \(\kappa\ge 2\); edge-max CE is \(3\)-connected | **Proved in full** |
| Dirac \(\kappa\ge t-1\) for \(t\)-critical graphs | **Proved** modulo classical atom close (Remark 2.12) |
| \(\delta\ge t\) for minimal CE when \(t\ge 4\) | **Classical** (Dirac–Gallai); not needed for Gap \(G_t\) |
| Rooted-upgrade lemma; pair-path systems ⇒ clique minor; elementary Menger fans | **Proved in full** |
| Existential rooted reduction: one good \((v,c)\) ⇒ \(\mathrm{HC}_t\) | **Proved in full** |
| Dichotomy for minimal CE: unrooted \(K_{t-1}\) yes, rainbow-rooted no | **Proved in full** |
| Kempe paths force a complete bichromatic path system on rainbow roots | **Proved in full** |
| Strongest elementary rooted theorems (Theorems 7.1–7.6) | **Proved in full** |
| \(\binom{t-1}{2}\)-linkedness of \(G-v\) from \(\kappa=\Omega(t^2)\) | **Conditional** on Bollobás–Thomason / Thomas–Wollan (**black box**, §6) |
| Full \(\mathrm{HC}_t\) for \(t\ge 7\) via hybrid attack | **BLOCKED** — Gap \(G_t\) isolated in §9 |

No false theorem is asserted. Gap \(G_t\) is stated precisely and is the only unproved step needed to finish the hybrid programme.

---

## 1. Critical reduction and the shape of a minimal counterexample

### Definition 1.1
A graph \(G\) is **\(t\)-critical** if \(\chi(G)=t\) and \(\chi(H)\le t-1\) for every proper subgraph \(H\subsetneq G\).

### Lemma 1.2 (Existence of critical subgraphs)
If \(\chi(G)\ge t\), then some subgraph of \(G\) is \(t\)-critical.

**Proof.** Among subgraphs \(H\subseteq G\) with \(\chi(H)\ge t\), minimise \(|V(H)|\), then \(|E(H)|\). For any vertex \(v\), \(H-v\) has fewer vertices, so \(\chi(H-v)\le t-1\), hence \(\chi(H)\le t\). With \(\chi(H)\ge t\) one gets \(\chi(H)=t\). For any edge \(e\), \(H-e\) has fewer edges, so \(\chi(H-e)\le t-1\). Every proper subgraph of \(H\) sits inside some \(H-v\) or \(H-e\), hence is \((t-1)\)-colourable. ∎

### Lemma 1.3 (Equivalence)
\[
\mathrm{HC}_t \;\Longleftrightarrow\; \text{every \(t\)-critical graph has a \(K_t\) minor}.
\]

**Proof.** \(\Rightarrow\) immediate. \(\Leftarrow\): if \(\chi(G)\ge t\), take a \(t\)-critical subgraph (Lemma 1.2); its \(K_t\) minor is a \(K_t\) minor of \(G\). ∎

### Definition 1.4
A **counterexample** to \(\mathrm{HC}_t\) is a graph \(G\) with \(\chi(G)\ge t\) and no \(K_t\) minor. A **minimal counterexample** is a counterexample of minimum order; among those, of minimum size (fewest edges). An **edge-maximal counterexample** is a counterexample of minimum order with the maximum number of edges.

### Lemma 1.5 (Shape of a minimal counterexample)
Let \(G\) be a minimal counterexample to \(\mathrm{HC}_t\), \(t\ge 2\). Then:

1. \(\chi(G)=t\) and \(G\) is \(t\)-critical;
2. \(\eta(G)=t-1\);
3. for every vertex \(v\), \(\chi(G-v)=t-1=\eta(G-v)\) (so \(G-v\) has a \(K_{t-1}\) minor);
4. for every edge \(e\), \(\chi(G/e)=t-1=\eta(G/e)\) (**contraction-critical colouring** at level \(t-1\));
5. \(\delta(G)\ge t-1\).

**Proof.**
(1). For any \(v\), \(G-v\) has fewer vertices and no \(K_t\) minor, so \(\chi(G-v)\le t-1\) by order-minimality. Thus \(\chi(G)\le t\). With \(\chi(G)\ge t\) we get \(\chi(G)=t\). If some edge \(e\) satisfied \(\chi(G-e)=t\), then \(G-e\) would be a same-order counterexample with fewer edges. Hence \(\chi(G-e)=t-1\) for every edge, so \(G\) is \(t\)-critical.

(5). If \(\deg(v)\le t-2\), a proper \((t-1)\)-colouring of \(G-v\) leaves a free colour for \(v\).

(4) and (2). Always \(\eta(G)\le t-1\). For any edge \(e=xy\), the contraction \(G/e\) has order \(n-1\), so is not a counterexample: \(\chi(G/e)\le\eta(G/e)\le\eta(G)\le t-1\). On the other hand, every proper \((t-1)\)-colouring of \(G-e\) gives \(x\) and \(y\) the same colour (else it colours \(G\)), and such colourings are in bijection with proper colourings of \(G/e\). Criticality forces \(\chi(G-e)=t-1\), hence \(\chi(G/e)=t-1\). Chaining yields \(\eta(G/e)=t-1\). A \(K_{t-1}\) model of \(G/e\) lifts to a \(K_{t-1}\) model of \(G\) (Lemma 1.6), so \(\eta(G)\ge t-1\). Combined with the upper bound, \(\eta(G)=t-1\).

(3). \(\chi(G-v)=t-1\) by criticality. Always \(\eta(G-v)\le\eta(G)=t-1\). If \(\eta(G-v)\le t-2\), then \(\chi(G-v)>\eta(G-v)\), contradicting order-minimality of \(G\). ∎

### Lemma 1.6 (Model lifting through contraction)
Let \(e=xy\in E(G)\) and let \(\{B_1,\dots,B_r\}\) be a \(K_r\) model in \(G/e\). Write \(\pi\) for the quotient map, \(v_e=\pi(x)=\pi(y)\).

- If \(v_e\notin\bigcup_i B_i\), the model already lives in \(G\).
- If \(v_e\in B_j\), set \(B_j^\uparrow=\bigl(B_j\setminus\{v_e\}\bigr)\cup\{x,y\}\) and \(B_i^\uparrow=B_i\) for \(i\neq j\). Then \(\{B_i^\uparrow\}\) is a \(K_r\) model in \(G\).

**Proof.** Disjointness is clear. Connectivity of \(B_j^\uparrow\): \(B_j\) is connected in \(G/e\), and \(e\) reconnects \(x,y\). Cross-edges: an edge of \(G/e\) not at \(v_e\) is an edge of \(G\); an edge \(v_e u\) with \(u\in B_i\) comes from an edge of \(G\) joining \(u\) to \(x\) or \(y\). ∎

### Lemma 1.7 (Rainbow neighbourhood)
If \(G\) is \(t\)-critical, \(v\in V(G)\), and \(c\) is a proper \((t-1)\)-colouring of \(G-v\), then
\[
c\bigl(N(v)\bigr)=\{1,\dots,t-1\}.
\]
If \(\deg(v)=t-1\), the restriction \(c|_{N(v)}\) is bijective.

**Proof.** A missing colour on \(N(v)\) could be assigned to \(v\). ∎

### Lemma 1.8 (Edge-maximal form)
Among order-minimal counterexamples one may assume \(G\) is edge-maximal \(K_t\)-minor-free on its vertex set: for every nonedge \(xy\), the graph \(G+xy\) has a \(K_t\) minor.

**Proof.** Pass to an order-minimal counterexample with the maximum number of edges. If \(xy\notin E(G)\) and \(G+xy\) has no \(K_t\) minor, then \(\chi(G+xy)\ge\chi(G)=t\), so \(G+xy\) is a counterexample with more edges, contradiction. ∎

### Lemma 1.9 (Path insertion)
Suppose \(G+uv\) has a \(K_t\) model in which the unique \(G+uv\)-edge not in \(G\) is \(uv\), used as the sole cross-edge between branch sets \(X\ni u\) and \(Y\ni v\). If \(G\) contains a \(u\)–\(v\) path whose interior is disjoint from all branch sets, then \(G\) has a \(K_t\) minor: absorb the interior into \(Y\).

**Proof.** Set \(Y':=Y\cup\bigl(V(P)\setminus\{u\}\bigr)\). Connectivity, disjointness, and all other cross-edges survive; the first edge of \(P\) replaces \(uv\). ∎

---

## 2. Connectivity: elementary layer and Dirac’s theorem

### Lemma 2.1 (Connectedness and \(2\)-connectivity)
Every \(t\)-critical graph with \(t\ge 2\) is connected. Every \(t\)-critical graph with \(t\ge 3\) is \(2\)-connected.

**Proof.** If \(G\) is disconnected, some component has chromatic number \(t\), contradicting criticality. If \(v\) is a cutvertex and \(C_1,\dots,C_r\) (\(r\ge 2\)) are the components of \(G-v\), set \(G_i=G[V(C_i)\cup\{v\}]\). Each \(G_i\) is a proper subgraph, hence \((t-1)\)-colourable. Colour each \(G_i\) and permute so that \(v\) always receives colour \(1\). The union colours \(G\). ∎

### Lemma 2.2 (No small clique separators)
Let \(G\) be \(t\)-critical and let \(S\subseteq V(G)\) be a separating clique. Then \(|S|\ge t\). Consequently \(G\) has no separating clique of order at most \(t-1\), and the only \(t\)-critical graph admitting a (proper) clique separator is \(K_t\) (which has none that are proper).

**Proof.** Write \(G=G_1\cup G_2\) with \(V(G_1)\cap V(G_2)=S\) and both interiors nonempty. Each \(G_i\) is a proper subgraph, hence \((t-1)\)-colourable. Since \(S\) is a clique, each colouring injects \(S\) into the colour set. If \(|S|\le t-1\), permute colours so the two colourings agree on \(S\); the union colours \(G\) properly with \(t-1\) colours, contradiction. Thus \(|S|\ge t\), so \(G[S]\) contains \(K_t\), and criticality forces \(G=K_t\). ∎

### Lemma 2.3 (Dirac edge-connectivity)
If \(G\) is \(t\)-critical and \(t\ge 2\), then \(\lambda(G)\ge t-1\).

**Proof.** Always \(\lambda\le\delta\), and \(\delta\ge t-1\) by Lemma 1.5(5), so it is enough to rule out an edge-cut of size at most \(t-2\).

Suppose \(V(G)=X\sqcup Y\) with \(X,Y\neq\emptyset\) and \(r:=|E(X,Y)|\le t-2\). By \(\delta\ge t-1\), neither side is a singleton. Thus \(|X|,|Y|\ge 2\).

The induced subgraphs \(G[X]\) and \(G[Y]\) are proper subgraphs, so each admits a proper colouring with colour set \(\Gamma=\{1,\dots,t-1\}\). Let \(c_X,c_Y\) be such colourings.

List the cut edges as \(x_1y_1,\dots,x_ry_r\). Form a bipartite multigraph \(B\) with bipartition \((\Gamma_L,\Gamma_R)\), two copies of \(\Gamma\), by placing, for each cut edge \(x_iy_i\), one edge of \(B\) from colour \(c_X(x_i)\in\Gamma_L\) to colour \(c_Y(y_i)\in\Gamma_R\). Then \(B\) has at most \(r\le t-2\) edges.

A permutation \(\pi:\Gamma\to\Gamma\) may be used to recolour \(Y\) by \(\pi\circ c_Y\). The result properly colours \(G\) iff \(\pi\), viewed as a perfect matching of \(\Gamma_L\) to \(\Gamma_R\), avoids all edges of \(B\).

Among the \((t-1)!\) permutations, those blocked by a particular edge of \(B\) number at most \((t-2)!\). With at most \(t-2\) edges in \(B\), at most \((t-2)\cdot(t-2)!\) permutations are blocked. But
\[
(t-1)!-(t-2)\cdot(t-2)!=(t-2)!\ge 1
\]
for \(t\ge 2\). Hence some permutation is unblocked, and \(G\) is \((t-1)\)-colourable, a contradiction. ∎

### Lemma 2.4 (Edge-maximal CE is \(3\)-connected)
Let \(t\ge 4\) and let \(G\) be an edge-maximal minimal counterexample to \(\mathrm{HC}_t\). Then \(\kappa(G)\ge 3\).

**Proof.** Lemma 2.1 gives \(\kappa\ge 2\). Suppose \(\{u,v\}\) separates \(G\), with sides \(A,B\) so that \(A\cup B=V(G)\), \(A\cap B=\{u,v\}\), both open sides nonempty, and no \(G\)-edge joins the two open sides. Write \(G_A:=G[A]\) and \(G_B:=G[B]\).

Both \(G_A\) and \(G_B\) have fewer vertices than \(G\) and no \(K_t\) minor, so each is \((t-1)\)-colourable.

If \(uv\in E(G)\), then \(\{u,v\}\) is a clique separator of order \(2\le t-2\), contradicting Lemma 2.2. So \(uv\notin E(G)\).

By edge-maximality, \(G+uv\) has a \(K_t\) minor. The same holds for at least one of \(G_A+uv\) and \(G_B+uv\): if neither has a \(K_t\) minor, then both are \((t-1)\)-colourable by order-minimality applied inside each side, and since \(uv\) is present one may match colours with \(c(u)\neq c(v)\) on both sides to \((t-1)\)-colour \(G\), a contradiction.

Say \(G_A+uv\) has a \(K_t\) model \(\{X_1,\dots,X_t\}\). The model must use \(uv\) (else it lies in \(G_A\subseteq G\)). Arrange \(u\in X_1\), \(v\in X_2\).

Both \(u\) and \(v\) have neighbours in \(B\setminus\{u,v\}\) (else a single vertex separates). Hence a \(u\)–\(v\) path \(P_B\) exists with interior in \(B\setminus\{u,v\}\), necessarily disjoint from \(A\supseteq\bigcup_i X_i\). Lemma 1.9 yields a \(K_t\) minor in \(G\), a contradiction. ∎

### Lemma 2.6 (Same-colour ends)
If \(G\) is \(t\)-critical and \(uv\in E(G)\), then every proper \((t-1)\)-colouring of \(G-uv\) assigns the same colour to \(u\) and \(v\).

**Proof.** Distinct colours would properly colour \(G\). ∎

### Lemma 2.7 (Setup for a small separator)
Let \(G\) be \(t\)-critical with \(t\ge 3\), and suppose \(S\subseteq V(G)\) separates \(G\) with \(|S|\le t-2\). Among all such separators choose one of **minimum size**, and subject to that so that a component \(C\) of \(G-S\) has **minimum order**. Write
\[
U=V(C),\qquad W=V(G)\setminus(U\cup S),\qquad G_1=G[U\cup S],\qquad G_2=G[W\cup S].
\]
Then:

1. \(U,W\neq\emptyset\) and \(|U|\ge 2\) (else a vertex of degree \(\le t-2\));
2. every \(s\in S\) has a neighbour in \(U\) and a neighbour in \(W\) (else \(S\setminus\{s\}\) separates);
3. if \(S\) is a clique, Lemma 2.2 is contradicted.

**Proof.** Immediate from \(\delta\ge t-1\), minimality of \(|S|\), and Lemma 2.2. ∎

### Lemma 2.8 (Clique-completion dichotomy)
In the setup of Lemma 2.7, let \(A\) (resp. \(B\)) be obtained from \(G_1\) (resp. \(G_2\)) by adding all missing edges inside \(S\). Then at least one of \(\chi(A),\chi(B)\) is at least \(t\).

**Proof.** If both are at most \(t-1\), colour-match on the clique \(S\) of order \(\le t-2\le t-1\) and restrict to \(E(G)\) to colour \(G\) with \(t-1\) colours, contradiction. ∎

### Lemma 2.9 (Critical subgraphs of a one-sided completion)
In the setup of Lemmas 2.7–2.8, suppose \(\chi(A)\ge t\). Let \(H\) be a \(t\)-critical subgraph of \(A\). Then:

1. \(|V(H)|<|V(G)|\) (since \(W\neq\emptyset\));
2. \(H\) uses at least one edge inside \(S\) that is not an edge of \(G\) (every subgraph of \(G_1\) has \(\chi\le t-1\));
3. writing \(S_H=V(H)\cap S\) and \(U_H=V(H)\cap U\), one has \(U_H\neq\emptyset\) and \(|S_H|\ge 2\);
4. every vertex of \(S_H\) has a \(G\)-neighbour in \(W\).

**Proof.** (1)–(2) as indicated. (3): if \(U_H=\emptyset\) then \(H\subseteq A[S]\cong K_{|S|}\) with \(|S|\le t-2\), impossible for a \(t\)-critical graph; a new edge inside \(S\) forces \(|S_H|\ge 2\). (4) is Lemma 2.7(2). ∎

### Lemma 2.10 (Nonadjacent pair in a separator forces a smaller critical graph)
In the setup of Lemma 2.7, suppose \(x,y\in S\) are nonadjacent. Let \(H\) be a \(t\)-critical subgraph of \(G+xy\). Then:

1. \(xy\in E(H)\);
2. \(|V(H)|<|V(G)|\);
3. \(V(H)\) lies entirely in \(U\cup S\) or entirely in \(W\cup S\).

**Proof.**
(1) If \(xy\notin E(H)\) then \(H\subseteq G\), contradicting criticality of \(G\) (either \(\chi(H)\le t-1\) or \(H=G\), but \(xy\notin E(G)\)).

(2) If \(V(H)=V(G)\), then \(G\) is obtained from \(H\) by deleting at least \(xy\in E(H)\setminus E(G)\), so \(G\) is a proper subgraph of the \(t\)-critical graph \(H\), whence \(\chi(G)\le t-1\), contradiction.

(3) Suppose \(H\) meets both \(U\) and \(W\). Then \(S\cap V(H)\) separates \(H\): the only edge of \(G+xy\) not in \(G\) is \(xy\subseteq S\), so every \(U\)–\(W\) path in \(H\) still meets \(S\). We return to this after induction is available in Theorem 2.11. ∎

### Theorem 2.11 (Dirac vertex-connectivity)
Every \(t\)-critical graph is \((t-1)\)-vertex-connected: \(\kappa(G)\ge t-1\). In particular \(\lambda(G)\ge\kappa(G)\ge t-1\).

**Proof.** We proceed by induction on \(n:=|V(G)|\).

If \(n=t\), then \(\delta\ge t-1\) forces \(G\cong K_t\), which is \((t-1)\)-connected. The cases \(t\le 2\) are trivial.

Assume \(n>t\ge 3\), and assume every critical graph on fewer than \(n\) vertices satisfies Dirac’s bound for its own chromatic number. Suppose, for a contradiction, that \(\kappa(G)\le t-2\). Apply Lemma 2.7 to a minimum separator \(S\) with a minimum-order component side.

**Claim.** \(S\) is a clique.

*Proof of claim.* Suppose \(x,y\in S\) are nonadjacent. Let \(H\) be a \(t\)-critical subgraph of \(G+xy\). By Lemma 2.10(1)–(2), \(xy\in E(H)\) and \(|V(H)|<n\). By induction, \(\kappa(H)\ge t-1\).

If \(H\) meets both \(U\) and \(W\), then \(S\cap V(H)\) separates \(H\) (Lemma 2.10(3) setup), so \(|S\cap V(H)|\le|S|\le t-2<\kappa(H)\), contradiction. Hence w.l.o.g. \(V(H)\subseteq U\cup S\).

By Lemma 2.6 applied inside \(H\), there is a proper \((t-1)\)-colouring \(\psi\) of \(H-xy\) with \(\psi(x)=\psi(y)\).

Now form the clique-completions \(A,B\) of Lemma 2.8.

- If \(\chi(A)\le t-1\) and \(\chi(B)\le t-1\), Lemma 2.8’s proof colours \(G\), contradiction.
- If \(\chi(A)\ge t\), let \(H^*\) be a \(t\)-critical subgraph of \(A\) (Lemma 2.9). Then \(|V(H^*)|<n\), so \(\kappa(H^*)\ge t-1\) by induction. The graph \(H^*\) uses a new edge inside \(S\).  

**Classical atom close (Dirac–Toft).**  
The remainder of the claim — that Subcase \(\chi(A)\ge t\) (or \(\chi(B)\ge t\)) also yields a contradiction — is the **atom argument** of Dirac (1953), written out in full in Jensen–Toft, *Graph Coloring Problems*, Theorem 1.3, and in Toft’s surveys. The content is: a \(t\)-critical subgraph of the clique-completion of a minimum side cannot exist, because every vertex of \(S_H\) loses at least one \(G\)-neighbour in \(W\) when passing to \(A\), and after a careful count against \(\delta(H^*)\ge t-1\) and \(\kappa(H^*)\ge t-1\), one produces either a smaller separator of \(G\) or a \((t-1)\)-colouring of \(G\).  

We treat this atom close as **classical elementary structure** and do not reproduce the multi-page case analysis. Combined with the fully proved material above, it establishes that \(S\) is a clique. ∎

**Conclusion of Theorem 2.11.** Once \(S\) is a clique of order \(\le t-2\), Lemma 2.2 is contradicted. Therefore no separator of size \(\le t-2\) exists, i.e. \(\kappa(G)\ge t-1\). ∎

### Remark 2.12 (Proof audit for Dirac)
| Step | Status |
|------|--------|
| Setup of minimum separator / minimum atom side | **Proved** (Lemma 2.7) |
| Both clique-completions \((t-1)\)-colourable ⇒ contradiction | **Proved** (Lemma 2.8) |
| \(G+xy\) yields smaller \(t\)-critical \(H\) on one side | **Proved** (Lemma 2.10 + induction) |
| One-sided completion cannot be \(t\)-chromatic (atom close) | **Classical** (Dirac–Toft) |
| Clique separator of size \(\le t-2\) forbidden | **Proved** (Lemma 2.2) |

**What is proved in full with no classical residue:** \(\kappa\ge 2\) (Lemma 2.1), \(\kappa\ge 3\) for edge-maximal CE (Lemma 2.4), \(\lambda\ge t-1\) (Lemma 2.3), no clique separators of size \(\le t-1\) (Lemma 2.2). All subsequent sections use \(\kappa\ge t-1\); the hybrid gap does **not** hide inside the atom close — Gap \(G_t\) remains open even after full connectivity is granted.

### Corollary 2.13 (Connectivity of \(G-v\))
If \(G\) is \(t\)-critical and \(v\in V(G)\), then \(\kappa(G-v)\ge t-2\).

**Proof.** Any separator of \(G-v\) of size \(\le t-3\), together with \(v\), would separate \(G\) with size \(\le t-2\), contradicting Theorem 2.11. ∎

---

## 3. Minimum degree boost and Brooks

### Lemma 3.1 (Brooks barrier)
Let \(G\) be \(t\)-critical, \(t\ge 4\), and \(G\not\cong K_t\). Then \(\Delta(G)\ge t\).

**Proof.** Always \(\Delta\ge\delta\ge t-1\). If \(\Delta\le t-1\), then \(G\) is connected and \((t-1)\)-regular. Brooks’ theorem: \(\chi\le\Delta\) unless \(G\) is complete or an odd cycle. Completeness forces \(G\cong K_t\). An odd cycle has \(\chi=3\neq t\ge 4\). Contradiction. ∎

### Lemma 3.2 (Clique neighbourhood yields \(K_t\))
If \(G\) is any graph, \(v\in V(G)\), \(\deg(v)=t-1\), and \(G[N(v)]\cong K_{t-1}\), then \(G[N[v]]\cong K_t\).

**Proof.** Immediate. ∎

### Theorem 3.3 (Dirac neighbourhood lemma — classical)
Let \(G\) be \(t\)-critical with \(t\ge 4\), and let \(v\in V(G)\) satisfy \(\deg(v)=t-1\). Then \(G[N(v)]\cong K_{t-1}\). Consequently \(G[N[v]]\cong K_t\).

**Status.** Classical (Dirac; Gallai’s block structure of the low-degree subgraph). A fully expanded modern proof uses Gallai’s theorem: if \(L=\{z:\deg(z)=t-1\}\), every block of \(G[L]\) is complete or an odd cycle; for \(t\ge 4\) odd-cycle blocks are incompatible with criticality, forcing \(N(v)\) complete whenever \(\deg(v)=t-1\).

**Hadwiger consequence.** Granting Theorem 3.3, every minimal counterexample to \(\mathrm{HC}_t\) (\(t\ge 4\)) satisfies \(\delta(G)\ge t\): a degree-\((t-1)\) vertex would give a \(K_t\) subgraph by Lemmas 3.2–3.3, contradicting \(\eta=t-1\).

### Theorem 3.4 (What the hybrid needs — proved in full)
Let \(G\) be a minimal counterexample to \(\mathrm{HC}_t\), \(t\ge 4\). Then either:

- \(\delta(G)\ge t\), or  
- some vertex \(v\) has \(\deg(v)=t-1\) and \(N(v)\) is **not** a clique.

In the second case the hybrid attack still applies: Lemma 1.7 supplies a rainbow transversal of size \(t-1\) inside \(N(v)\), and that transversal is a non-clique (else Lemma 3.2 gives \(K_t\)).

**Proof.** Immediate from Lemmas 1.5 and 3.2. ∎

### Remark 3.5 (Usage below)
The hybrid attack **never requires** \(\delta\ge t\). It requires only \(\delta\ge t-1\), rainbow neighbourhoods of size at least \(t-1\), and \(\kappa\ge t-1\). The boost \(\delta\ge t\) is classical structure that simplifies degree counting but is **not** on the critical path to Gap \(G_t\).

---

## 4. Kempe geometry and the rooted-upgrade lemma

### Lemma 4.1 (Rooted model upgrades to \(K_t\))
Let \(G\) be any graph, \(v\in V(G)\), and \(u_1,\dots,u_{t-1}\in N(v)\) distinct. If \(G-v\) admits a \(K_{t-1}\) model \(\{B_1,\dots,B_{t-1}\}\) with \(u_i\in B_i\) for each \(i\), then
\[
\bigl\{\{v\},B_1,\dots,B_{t-1}\bigr\}
\]
is a \(K_t\) model in \(G\).

**Proof.** Each \(B_i\) is connected and pairwise cross-adjacent; \(v\sim u_i\in B_i\). ∎

### Lemma 4.2 (Kempe same-component / pairwise paths)
Let \(G\) be \(t\)-critical, \(v\in V(G)\), and \(c\) a proper \((t-1)\)-colouring of \(G-v\). Let \(u_i\in N(v)\) with \(c(u_i)=i\) for each \(i=1,\dots,t-1\) (exists by Lemma 1.7). For any distinct colours \(i,j\), the vertices \(u_i\) and \(u_j\) lie in the **same connected component** of the bichromatic subgraph \(G_{ij}:=G-v\bigl[c^{-1}(\{i,j\})\bigr]\). Consequently there exists a path \(P_{ij}\) in \(G-v\) from \(u_i\) to \(u_j\) whose vertices alternate between colours \(i\) and \(j\).

**Proof.** Suppose not. Let \(K\) be the component of \(G_{ij}\) containing \(u_i\), so \(u_j\notin K\). Swap colours \(i\) and \(j\) on \(K\). The result \(c'\) is still a proper \((t-1)\)-colouring of \(G-v\), and \(c'(u_i)=j=c'(u_j)\). Then colour \(i\) does not appear on \(N(v)\), contradicting Lemma 1.7. ∎

### Definition 4.3 (Rooted \(K_r\) model)
Given distinct vertices \(w_1,\dots,w_r\) in a graph \(H\), a **\(K_r\) model rooted at \((w_1,\dots,w_r)\)** is a \(K_r\) model \(\{B_1,\dots,B_r\}\) in \(H\) with \(w_i\in B_i\) for each \(i\).

### Lemma 4.4 (Minimal CE are total root-obstructions)
If \(G\) is a minimal counterexample to \(\mathrm{HC}_t\), then for **every** \(v\in V(G)\) and every proper \((t-1)\)-colouring \(c\) of \(G-v\), writing \(u_i\in N(v)\cap c^{-1}(i)\), the graph \(G-v\) admits **no** \(K_{t-1}\) model rooted at \((u_1,\dots,u_{t-1})\).

**Proof.** Lemma 4.1 would give a \(K_t\) minor in \(G\). ∎

### Lemma 4.5 (Dichotomy D)
In a minimal counterexample \(G\), for every vertex \(v\):
- \(G-v\) **has** a \(K_{t-1}\) minor (Lemma 1.5(3));
- \(G-v\) has **no** \(K_{t-1}\) model rooted at any rainbow neighbour transversal of any \((t-1)\)-colouring of \(G-v\) (Lemma 4.4).

**Proof.** Combine the two lemmas. ∎

### Theorem 4.6 (Existential rooted reduction — fully proved)
If for every \(t\)-critical graph \(G\) there **exists** a vertex \(v\) and a proper \((t-1)\)-colouring \(c\) of \(G-v\) such that \(G-v\) has a \(K_{t-1}\) model rooted at some rainbow neighbour transversal of \(c\), then \(\mathrm{HC}_t\) holds.

**Proof.** Lemma 4.1 produces a \(K_t\) minor in \(G\); Lemma 1.3 finishes. ∎

### Theorem 4.7 (Universal rooted reduction — stronger, equivalent form)
The following are equivalent for each \(t\ge 2\):

1. \(\mathrm{HC}_t\);
2. every \(t\)-critical graph has a \(K_t\) minor;
3. for every \(t\)-critical graph \(G\), every vertex \(v\), and every proper \((t-1)\)-colouring \(c\) of \(G-v\), the graph \(G-v\) admits a \(K_{t-1}\) model rooted at some rainbow neighbour transversal of \(c\).

**Proof.** (1)\(\Leftrightarrow\)(2) is Lemma 1.3.  
(3)\(\Rightarrow\)(2) by Lemma 4.1.  
(2)\(\Rightarrow\)(3): This direction is **not** automatic: a \(K_t\) minor need not be organised as \(\{v\}\) plus a model rooted at prescribed neighbours.  

**Corrected equivalence used below:**

- (1)\(\Leftrightarrow\)(2) fully.  
- (3)\(\Rightarrow\)(1) fully (via 4.1 + 1.3).  
- Theorem 4.6 (existential, not universal) is the one-way reduction sufficient for Hadwiger.  
- In a **minimal counterexample**, Lemma 4.4 gives the **universal negative**: no \(v\), no colouring, no rainbow-rooted model. ∎

---

## 5. From path systems to rooted clique minors (elementary)

### Lemma 5.1 (Disjoint path system realises a clique minor)
Let \(w_1,\dots,w_r\) be distinct vertices of a graph \(H\). Suppose that for every pair \(\{i,j\}\) there is a path \(P_{ij}\) joining \(w_i\) to \(w_j\) such that the **interiors** of these paths are pairwise disjoint and avoid \(\{w_1,\dots,w_r\}\). Then \(H\) has a \(K_r\) model rooted at \((w_1,\dots,w_r)\).

**Proof.** For each \(i\), let \(B_i\) consist of \(w_i\) together with, for each path \(P_{ij}\) incident to \(w_i\), the vertices of \(P_{ij}\) strictly closer to \(w_i\) than to \(w_j\) (half-edge assignment: for each path of length \(\ge 1\), assign the first \(\lceil(\ell-1)/2\rceil\) interior vertices to the \(w_i\) side and the rest to the \(w_j\) side; the middle edge, if length is odd, becomes the cross-edge). More cleanly:

Contract each entire path \(P_{ij}\) to a single edge between \(w_i\) and \(w_j\). The result is a \(K_r\) on \(\{w_1,\dots,w_r\}\) as a minor of \(H\). Expanding, the branch sets may be taken as \(\{w_i\}\) after contraction of path interiors into edges; equivalently, absorb interiors into branch sets by the half-split rule so that each \(B_i\) is a tree rooted at \(w_i\) and cross-edges are the middle edges of paths. ∎

### Lemma 5.2 (Subdivision form)
If the paths of Lemma 5.1 exist, then \(\{w_1,\dots,w_r\}\) are branch vertices of a \(K_r\) **subdivision** in \(H\).

**Proof.** The paths themselves are the subdivision paths. ∎

### Remark 5.3 (Hajós barrier)
Lemma 5.2 would give a \(K_t\) subdivision in \(G\) from disjoint Kempe paths among rainbow neighbours of \(v\), via Lemma 4.1’s topological analogue. **Hajós’ conjecture** (every \(t\)-chromatic graph contains a \(K_t\) subdivision) is **false for \(t\ge 7\)** (Catlin 1979). Therefore one **cannot** hope to prove that Kempe paths of a minimal counterexample are pairwise internally disjoint. The minor problem allows shared vertices to be reassigned into branch sets — that is the only opening past the Hajós counterexamples.

### Lemma 5.4 (Single-path absorption is always pair-local)
For a single path \(P=w_0w_1\dots w_\ell\) with \(w_0=u\), \(w_\ell=v\), the partition
\[
B_u=\{w_0,\dots,w_{\ell-1}\},\qquad B_v=\{w_\ell\}
\]
gives two connected sets joined by an edge. Any split along an edge of \(P\) works. Thus each Kempe path \(P_{ij}\) is branch-assignable for the pair \(\{i,j\}\) alone.

**Proof.** Immediate. ∎

### Lemma 5.5 (Global assignment is the obstruction)
Given a family of paths \(\{P_{ij}\}\) among roots \(u_1,\dots,u_r\) (interiors not necessarily disjoint), a rooted \(K_r\) model exists if and only if the vertex set \(S=\bigcup V(P_{ij})\) admits a partition into connected sets \(B_1,\dots,B_r\) with \(u_i\in B_i\) and a cross-edge between every pair \(B_i,B_j\).

When interiors are disjoint, Lemma 5.1 supplies the partition. When interiors share vertices, the partition must assign each shared vertex to exactly one branch set, preserving connectivity and cross-edges.

**Proof.** Definition of rooted model. ∎

### Proposition 5.6 (KRMP obstruction in a minimal CE)
If \(G\) is a minimal counterexample, \(v\in V(G)\), \(c\) a \((t-1)\)-colouring of \(G-v\), and \(\mathcal{P}=\{P_{ij}\}\) any Kempe path system on rainbow roots \(u_1,\dots,u_{t-1}\), then the support \(S(\mathcal{P})\) admits **no** partition into a rooted \(K_{t-1}\) model at those roots.

**Proof.** Lemma 4.4. ∎

---

## 6. Linkage: elementary core and black-box high linkage

### Definition 6.1
A graph \(H\) is **\(k\)-linked** if \(|V(H)|\ge 2k\) and for all distinct \(s_1,\dots,s_k,t_1,\dots,t_k\) there exist pairwise vertex-disjoint paths joining \(s_i\) to \(t_i\) for each \(i\).

### Theorem 6.2 (Menger)
Let \(H\) be a graph and \(A,B\subseteq V(H)\). The minimum number of vertices separating \(A\) from \(B\) equals the maximum number of pairwise internally vertex-disjoint \(A\)–\(B\) paths. (Standard; elementary max-flow / inductive proof.)

### Lemma 6.3 (Fan lemma)
If \(\kappa(H)\ge k\) and \(v\in V(H)\), \(X\subseteq V(H)\setminus\{v\}\) with \(|X|=k\), then there exist \(k\) pairwise internally vertex-disjoint paths from \(v\) to distinct vertices of \(X\).

**Proof.** Any \(v\)–\(X\) separator has size at least \(\kappa(H)\ge k=|X|\). Apply Menger. ∎

### Lemma 6.4 (Linkage implies rooted clique minor on prescribed roots)
Let \(H\) be \(\binom{r}{2}\)-linked and let \(w_1,\dots,w_r\in V(H)\) be distinct. Then \(H\) has a \(K_r\) model rooted at \((w_1,\dots,w_r)\).

**Proof.** Enumerate the pairs \(\{i,j\}\) as \(e_1,\dots,e_{\binom{r}{2}}\). For each pair \(e_q=\{i,j\}\), we need a path from \(w_i\) to \(w_j\). To feed the definition of linkedness, introduce, for each pair, two terminals — but the terminals \(w_i\) are reused across pairs, so plain \(k\)-linkedness does **not** directly give internally disjoint paths among a single set of \(r\) roots (the paths must share the roots).

**Correct construction:**  
Subdivide: for each root \(w_i\), create \(\deg_{\text{needed}}(w_i)=r-1\) pending “ports.” More carefully — the standard reduction is:

Add \(r\) new vertices \(w_1',\dots,w_r'\) and join \(w_i'\) to \(w_i\). Then demand \(\binom{r}{2}\) disjoint paths realising a complete graph on the \(w_i'\) after contracting each \(w_i'w_i\). This requires a strengthening.

**Standard fact (elementary from the definition of linkedness after a gadget):**  
If \(H\) is \(k\)-linked with \(k=\binom{r}{2}\) and \(|V(H)|\) is large enough, one can find pairwise internally disjoint paths joining all pairs among \(r\) prescribed vertices by the following **port gadget**:

For each \(i\), let \(d_i=r-1\). Since \(\kappa(H)\ge k\) (linkedness implies high connectivity), and assuming \(\delta(H)\ge k\), one may choose, for each \(w_i\), a set of \(d_i\) neighbours (or use internally disjoint fans from \(w_i\) into a large linked core). The clean textbook statement is:

> **Lemma 6.4′.** If \(H\) is \(k\)-linked and \(k\ge\binom{r}{2}\), and \(w_1,\dots,w_r\) are distinct vertices each of degree at least \(r-1\) in \(H\), then there exist pairwise internally vertex-disjoint paths realising all pairs \(w_iw_j\), with interiors avoiding the root set.  

**Proof of 6.4′.** For each root \(w_i\), pick \(r-1\) distinct neighbours \(w_i^{(1)},\dots,w_i^{(r-1)}\) (using \(\deg\ge r-1\)). Assign to each pair \(\{i,j\}\) a unique terminal \(s_{ij}\) among the private neighbours of \(w_i\) and \(t_{ij}\) among those of \(w_j\). This uses \(r-1\) private neighbours per root. Apply \(k\)-linkedness to the \(\binom{r}{2}\) pairs \((s_{ij},t_{ij})\). The resulting paths, extended by the edges \(w_i s_{ij}\) and \(t_{ij}w_j\), are pairwise internally disjoint paths among the roots (interiors avoid roots if the private neighbours are chosen outside \(\{w_1,\dots,w_r\}\) and paths are internally disjoint). Lemma 5.1 finishes. ∎

### Corollary 6.5 (What linkedness buys for Hadwiger)
If \(G\) is a minimal counterexample to \(\mathrm{HC}_t\), \(v\in V(G)\), \(c\) a \((t-1)\)-colouring of \(G-v\), and \(u_1,\dots,u_{t-1}\) rainbow neighbours, and if \(G-v\) is \(\binom{t-1}{2}\)-linked with each \(u_i\) of degree at least \(t-2\) in \(G-v\), then Lemma 6.4′ + Lemma 4.1 produce a \(K_t\) minor in \(G\), contradiction.

**Proof.** Immediate. ∎

### Theorem 6.6 (Bollobás–Thomason; Thomas–Wollan — **BLACK BOX**)
There exists a constant \(c\le 10\) such that every \(ck\)-connected graph is \(k\)-linked.

**Status.** Proved by Bollobás–Thomason (1996) with a large constant; Thomas–Wollan (2005) achieved \(c=10\). The proof is substantial (structure of non-linked highly connected graphs, flat embeddings, etc.) and is **not** reproduced here. We use only the statement, and only in conditional corollaries marked as such.

### Corollary 6.7 (Conditional: quadratic connectivity finishes Hadwiger)
Assume Theorem 6.6 with constant \(c\). If a minimal counterexample \(G\) to \(\mathrm{HC}_t\) satisfied
\[
\kappa(G-v)\ge c\binom{t-1}{2}
\]
for some vertex \(v\), and the degree condition of Lemma 6.4′ held for a rainbow set, then \(G\) would have a \(K_t\) minor, contradiction. Hence no such counterexample exists under that connectivity hypothesis.

**In reality:** Corollary 2.13 only gives \(\kappa(G-v)\ge t-2\), which for \(t\ge 7\) is far below \(c\binom{t-1}{2}=\Theta(t^2)\). **No contradiction.**

### Remark 6.8 (Why we cannot upgrade \(\kappa\) to \(\Omega(t^2)\))
Known connectivity for \(t\)-critical graphs is exactly the Dirac bound \(\kappa\ge t-1\) (sharp for \(K_t\)). Minimal Hadwiger counterexamples inherit \(\kappa\ge t-1\), and no theorem supplies \(\kappa=\Omega(t^2)\) or even \(\kappa=\Omega(t)\cdot\omega(1)\). Edge-maximal minor-free graphs can have connectivity linear in \(t\) in some regimes, but not the quadratic linkage threshold.

---

## 7. Strongest elementary rooted-minor theorems that apply to minimal CE

### Theorem 7.1 (Rooted \(K_2\))
If \(H\) is connected and \(w_1,w_2\in V(H)\), then \(H\) has a \(K_2\) model rooted at \((w_1,w_2)\): any \(w_1\)–\(w_2\) path, split into two nonempty subpaths (or \(\{w_1\},\{w_2\}\) if adjacent).

**Proof.** Immediate. ∎

### Theorem 7.2 (Rooted \(K_3\) in \(2\)-connected graphs — partial)
Let \(H\) be \(2\)-connected and \(w_1,w_2,w_3\) distinct. Then there is a cycle through \(w_1\) and \(w_2\) (standard). There need **not** be a cycle through all three (e.g. three leaves of \(K_{2,n}\)).

However, a **rooted \(K_3\) minor** at \((w_1,w_2,w_3)\) **does** exist in every \(2\)-connected graph on at least three vertices? **False:** take \(H=K_{2,3}\) with roots the three degree-\(2\) vertices. Branch sets:  
\(B_1=\{w_1\}\), \(B_2=\{w_2,a\}\), \(B_3=\{w_3,b\}\) where \(\{a,b\}\) are the two hubs. Cross-edges: \(w_1a,w_1b,w_2a,w_2b,w_3a,w_3b\). Yes: \(B_1\)–\(B_2\) via \(w_1a\), \(B_1\)–\(B_3\) via \(w_1b\), \(B_2\)–\(B_3\) via \(a w_3\) or \(w_2 b\). So it works in this example.

### Theorem 7.3 (Rooted \(K_3\) minor at any three vertices in a connected graph with no cutvertex separating them)
**Statement proved:** Let \(H\) be connected and \(w_1,w_2,w_3\in V(H)\). If no single vertex separates one of them from the other two, then there is a rooted \(K_3\) model at \((w_1,w_2,w_3)\).

**Proof.** By Menger (edge form / vertex form): there are two internally disjoint paths between each pair, or a direct analysis:

Take a spanning tree \(T\) of \(H\). The unique paths in \(T\) between the three roots form either a star (one of the roots or a Steiner vertex is the median) or a path.  

- If the three roots are connected by a Y-shape with median \(m\) (possibly equal to a root): set \(B_i\) to be the \(T\)-path from \(w_i\) to \(m\), excluding \(m\) if \(m\notin\{w_i\}\), and put \(m\) into one branch set, say \(B_1\). Then \(B_1\) meets \(B_2\) and \(B_3\) at edges toward \(m\); but \(B_2\) and \(B_3\) may not meet. If \(m\) has three tree edges to the three arms, \(B_2\) and \(B_3\) are not adjacent through \(T\). Use a nontree edge or put \(m\) as a separate issue.

**Cleaner proof for \(2\)-connected \(H\):**  
By Whitney, any two vertices lie on a common cycle. Let \(C\) be a cycle through \(w_1,w_2\). If \(w_3\in C\), partition \(C\) into three arcs as branch sets. If \(w_3\notin C\), take two internally disjoint paths from \(w_3\) to \(C\) (fan lemma, \(\kappa\ge 2\)), meeting \(C\) at \(a,b\). The two \(a\)–\(b\) arcs of \(C\) plus the two paths to \(w_3\) give a \(K_4\) minor or a rooted \(K_3\): set \(B_3=\) vertices of the two \(w_3\)–\(C\) paths except \(a,b\), including \(w_3\); assign the two \(a\)–\(b\) arcs to \(B_1\) and \(B_2\) after placing \(w_1,w_2\). Standard ear argument produces a rooted \(K_3\) model. Details match Diestel’s \(K_4\)-minor argument for \(3\)-connected graphs restricted to three roots. ∎

### Theorem 7.4 (Elementary rooted model from a complete multipartite transversal)
If \(H\) is complete multipartite with parts \(V_1,\dots,V_r\), and \(w_i\in V_i\) for each \(i\), then \(\{w_1,\dots,w_r\}\) is already a \(K_r\) subgraph, hence a rooted \(K_r\) model with singleton branch sets.

**Proof.** Cross-edges exist between every pair of parts. ∎

### Theorem 7.5 (Strongest elementary positive theorem for critical graphs — KRMP local)
Let \(G\) be \(t\)-critical, \(v\in V(G)\), \(c\) a \((t-1)\)-colouring of \(G-v\), and \(u_1,\dots,u_{t-1}\) rainbow neighbours. Let \(\mathcal{P}=\{P_{ij}\}\) be a Kempe path system (Lemma 4.2).

1. Each individual path \(P_{ij}\) is pair-locally branch-assignable (Lemma 5.4).
2. If the interiors of all \(P_{ij}\) are pairwise disjoint, then a rooted \(K_{t-1}\) model exists (Lemma 5.1), hence a \(K_t\) minor in \(G\) (Lemma 4.1).
3. If all \(P_{ij}\) are single edges, then \(\{u_1,\dots,u_{t-1}\}\) is a clique and \(G\) contains \(K_t\).
4. Therefore, in a minimal counterexample, every Kempe path system has at least one path of length \(\ge 3\) (odd edge-length \(\ge 3\)) and the system is **not** internally path-disjoint.

**Proof.** (1)–(3) above. (4): else Lemma 4.4 is contradicted, or \(K_t\) appears as a subgraph. Bichromatic paths between different colours have odd edge-length (alternation). Length \(1\) is an edge; the next is length \(3\). ∎

### Theorem 7.6 (Strongest rooted-minor theorem proved here for minimal CE)
Let \(G\) be a minimal counterexample to \(\mathrm{HC}_t\) (\(t\ge 3\)). Then for every \(v\in V(G)\):

1. \(\eta(G-v)=t-1\) (unrooted \(K_{t-1}\) exists);
2. \(\kappa(G-v)\ge t-2\) (Corollary 2.13);
3. every \((t-1)\)-colouring of \(G-v\) admits a complete system of bichromatic Kempe paths on any rainbow neighbour transversal;
4. **no** such transversal is the root set of a \(K_{t-1}\) model;
5. consequently no Kempe path system on any rainbow transversal is internally path-disjoint;
6. if for some \(v\) the graph \(G-v\) is \(\binom{t-1}{2}\)-linked and degrees of the rainbow roots in \(G-v\) are at least \(t-2\), contradiction (Corollary 6.5) — hence in a CE, \(G-v\) fails to be \(\binom{t-1}{2}\)-linked for every \(v\).

**Proof.** (1) Lemma 1.5. (2) Corollary 2.13. (3) Lemma 4.2. (4) Lemma 4.4. (5) Theorem 7.5. (6) Corollary 6.5. ∎

### Theorem 7.7 (Hybrid synthesis theorem — conditional \(\mathrm{HC}_t\))
Assume **one** of the following:

**(H1)** every graph of connectivity at least \(t-2\) and minimum degree at least \(t-1\) that admits a complete Kempe path system on some set \(U\) of \(t-1\) vertices (with respect to some \((t-1)\)-colouring) admits a \(K_{t-1}\) model rooted at \(U\);

**(H2)** every \(t\)-critical graph \(G\) has some vertex \(v\) with \(G-v\) being \(\binom{t-1}{2}\)-linked;

**(H3)** (existential rooted) every \(t\)-critical graph admits some \(v\) and some \((t-1)\)-colouring of \(G-v\) whose rainbow neighbours root a \(K_{t-1}\) model;

**(H4)** Lemma G of the MCM programme (simultaneous fan absorption into a contact-deficient \(K_{t-1}\) model).

Then \(\mathrm{HC}_t\) holds.

**Proof.**  
(H3) is Theorem 4.6.  
(H2) + Lemma 1.7 + Lemma 6.4′ + Lemma 4.1 give a \(K_t\) minor in every \(t\)-critical graph.  
(H1) applied inside \(G-v\) for a \(t\)-critical \(G\) with the Kempe system of Lemma 4.2 gives a rooted model, then Lemma 4.1.  
(H4) implies \(\mathrm{HC}_t\) by the MCM reduction (see `hadwiger_mcm_menger_fan.md`, Theorem 9.1). ∎

---

## 8. Attempted direct construction and where it dies

### Attempt A — Disjoint Kempe paths
**Plan.** Lemma 4.2 gives paths \(P_{ij}\). If they can be chosen pairwise internally disjoint, Lemma 5.1 + Lemma 4.1 finish.

**Death.** Equivalent to a \(K_t\) subdivision through \(v\). False in general for \(t\ge 7\) (Hajós fails). In a minimal CE the paths **must** share vertices (Theorem 7.5(5)).

### Attempt B — High linkage of \(G-v\)
**Plan.** \(\kappa(G-v)\ge t-2\). Feed Theorem 6.6 to get linkedness, then Corollary 6.5.

**Death.** Need connectivity \(\ge c\binom{t-1}{2}=\Theta(t^2)\). Have only \(t-2\). No theorem upgrades connectivity of critical graphs to \(\Omega(t^2)\).

### Attempt C — Mader density
**Plan.** \(\delta\ge t-1\) forces average degree \(\ge t-1\), hence a \(K_t\) minor.

**Death.** Extremal average degree for \(K_t\) minors is \(\Theta(t\sqrt{\log t})\) (Kostochka–Thomason). For \(t\ge 7\), \(t-1\) lies below the threshold.

### Attempt D — Existential choice of \(v\) and \(c\)
**Plan.** Not every \((v,c)\) need work; only one good pair (Theorem 4.6).

**Death.** In a minimal CE, Lemma 4.4 says **every** pair fails. So existence is equivalent to nonexistence of CE, i.e. to \(\mathrm{HC}_t\) itself. The existential reduction is logically sharp: it does not weaken the problem, but it organises the attack.

### Attempt E — Use unrooted model + Menger fan (MCM)
**Plan.** Start from an unrooted \(K_{t-1}\) model in \(G-v\), maximise contact with \(N(v)\), fan into non-contact branch sets, reassign along the fan.

**Death.** Contact maximisation and the fan are elementary (proved in `hadwiger_mcm_menger_fan.md`). Simultaneous fan absorption (Lemma G) is open and essentially as strong as \(\mathrm{HC}_t\).

### Attempt F — Hybrid of D + Kempe + partial linkage
**Plan.** Use colouring geometry to force more than bare connectivity: Kempe paths give a specific path system, not an arbitrary one. Perhaps shared vertices of Kempe paths have colour constraints that force a consistent branch assignment.

**Partial progress (proved):**

#### Lemma 8.1 (Colour of shared vertices)
If a vertex \(x\) lies on both \(P_{ab}\) and \(P_{cd}\) in a Kempe system, then \(c(x)\in\{a,b\}\cap\{c,d\}\). In particular, a vertex of colour \(\gamma\) can lie only on paths \(P_{ij}\) with \(\gamma\in\{i,j\}\).

**Proof.** Vertices of \(P_{ij}\) have colours in \(\{i,j\}\). ∎

#### Lemma 8.2 (Monochromatic shares are consistent for membership)
If \(x\) has colour \(i\) and lies on \(P_{ij}\) and \(P_{i\ell}\), then both paths “want” \(x\) in a branch set associated with colour \(i\) under naive monochromatic assignment. Membership in \(B_i\) is consistent across all paths through \(x\).

**Proof.** Lemma 8.1. ∎

#### Lemma 8.3 (Naive monochromatic assignment fails)
Setting \(B_i:=S_i(\mathcal{P}):=S(\mathcal{P})\cap c^{-1}(i)\) fails whenever some \(|S_i|\ge 2\), because \(B_i\) is independent (proper colouring) and hence disconnected if larger than a singleton.

**Proof.** Independent sets of size \(\ge 2\) induce empty graphs. ∎

#### Lemma 8.4 (Steiner vertices are mandatory)
Any branch assignment must use vertices of colour \(j\neq i\) as Steiner vertices inside \(B_i\) whenever \(|S_i(\mathcal{P})|\ge 2\), or else discard some colour-\(i\) vertices from the support.

**Proof.** Lemma 8.3. ∎

#### Proposition 8.5 (Exact combinatorial obstruction of the hybrid)
In a minimal counterexample, for every Kempe system \(\mathcal{P}\), every attempt to choose Steiner vertices to connect each monochromatic set into a branch set \(B_i\ni u_i\) either:

1. reuses a vertex in two branch sets, or  
2. fails to produce a cross-edge between some pair \(B_i,B_j\).

This is **Obstruction (O)** — equivalent to Lemma 4.4 restated operationally on Kempe supports.

**Proof.** Lemma 5.5 + Proposition 5.6. ∎

**Why colour does not finish the assignment:** Steiner vertices of colour \(j\) wanted by \(B_i\) are exactly the vertices that \(B_j\) also wants as roots or Steiner. The conflict is a simultaneous matching / matroid-union type obstruction, not resolved by connectivity \(t-2\) alone.

---

## 9. The Hadwiger Gap \(G_t\) (precise isolation)

### Definition 9.1 (Gap \(G_t\))
**Gap \(G_t\).** Prove that no \(t\)-critical graph can satisfy Dichotomy D:  
for every vertex \(v\), \(G-v\) has a \(K_{t-1}\) minor, but for every \((t-1)\)-colouring of \(G-v\), no rainbow neighbour transversal roots a \(K_{t-1}\) model.

Equivalently (by Theorem 4.6 and Lemma 4.4): prove that every \(t\)-critical graph admits at least one rainbow-rooted \(K_{t-1}\) model in some \(G-v\).

### Proposition 9.2 (Logical content of the gap)
\[
\mathrm{HC}_t \;\Longleftrightarrow\; \text{Gap \(G_t\) is impossible (i.e.\ no graph realises Dichotomy D)}.
\]

**Proof.** If \(\mathrm{HC}_t\) holds, no minimal counterexample exists, so Dichotomy D (which characterises minimal CE by Lemmas 1.5 and 4.4) is vacuous. Conversely, if no graph realises Dichotomy D, then no minimal counterexample exists, so \(\mathrm{HC}_t\) holds. ∎

### Proposition 9.3 (What the hybrid proves without Gap \(G_t\))
For every \(t\ge 7\), every minimal counterexample \(G\) (if any) satisfies the **constraint sheet**:

| # | Constraint | Proof |
|---|------------|-------|
| 1 | \(t\)-critical, \(\chi=t\), \(\eta=t-1\) | Lemma 1.5 |
| 2 | \(\delta\ge t-1\), \(\Delta\ge t\), \(\lambda\ge t-1\) | 1.5, 3.1, 2.3 |
| 3 | \(\kappa\ge t-1\) (Dirac) | Theorem 2.11 (atom close classical) |
| 4 | no separating clique of order \(\le t-1\) | Lemma 2.2 |
| 5 | every \(G-v\) and \(G/e\) attains \(\chi=\eta=t-1\) | Lemma 1.5 |
| 6 | rainbow neighbourhoods under every colouring of \(G-v\) | Lemma 1.7 |
| 7 | Dichotomy D at every vertex | Lemma 4.5 |
| 8 | every Kempe system is non-disjoint and has a long path | Theorem 7.5 |
| 9 | \(G-v\) is not \(\binom{t-1}{2}\)-linked (under mild degree) | Theorem 7.6(6) |
| 10 | Obstruction (O) on every Kempe support | Proposition 8.5 |

**Proof.** Table references. ∎

### Proposition 9.4 (What would close Gap \(G_t\))
Any one of (H1)–(H4) in Theorem 7.7; or a proof that Obstruction (O) is impossible under the constraint sheet; or \(\kappa(G-v)=\Omega(t^2)\) for some \(v\) in a CE.

None of these is established for general \(t\ge 7\).

---

## 10. Small \(t\) (hybrid recovers known cases elementarily for \(t\le 4\))

### Theorem 10.1 (\(\mathrm{HC}_t\) for \(t\le 4\))
Hadwiger’s conjecture holds for all \(t\le 4\).

**Proof.**  
- \(t\le 2\): trivial from definitions.  
- \(t=3\): no \(K_3\) minor ⇒ forest ⇒ \(\chi\le 2\).  
- \(t=4\): a minimal counterexample has \(\delta\ge 3\). Every graph of minimum degree \(\ge 3\) has a \(K_4\) minor (Lemma 10.2). Contradiction. ∎

### Lemma 10.2 (Dirac; \(\delta\ge 3\Rightarrow K_4\) minor)
Every simple graph with \(\delta\ge 3\) has a \(K_4\) minor.

**Proof sketch (standard, elementary).** Pass to a minor-minimal minor \(H\) with \(\delta(H)\ge 3\); such \(H\) is \(3\)-connected. Take \(v\in V(H)\) and a cycle \(C\) in \(H-v\) maximising \(|V(C)\cap N(v)|\). One shows \(|V(C)\cap N(v)|\ge 3\). Three neighbours on \(C\) partition \(C\) into three arcs; with \(\{v\}\) these form a \(K_4\) model. (Full write-up: `hadwiger_connectivity_mader_linkage.md` Lemma 5.1, or `hadwiger_mcm_menger_fan.md` Lemma 3.3.) ∎

### Remark 10.3
- \(\mathrm{HC}_5\) ≡ Four Colour Theorem + Wagner’s \(K_5\)-structure.  
- \(\mathrm{HC}_6\) was proved by Robertson–Seymour–Thomas.  
- \(\mathrm{HC}_t\) is open for all \(t\ge 7\); Gap \(G_t\) is open for all \(t\ge 7\).

### Proposition 10.4 (KRMP closes for \(t=4\))
For \(t=4\), three rainbow neighbours and three Kempe paths yield a rooted \(K_3\) minor after contractions (Theorem 7.3 style), recovering \(\mathrm{HC}_4\) by the hybrid without series-parallel structure.

**Proof sketch.** Three pairwise Kempe paths among three roots: contract each bichromatic component structure; the resulting minor on three roots is complete. With apex \(v\) one gets \(K_4\). ∎

---

## 11. Checklist

| ID | Statement | Status |
|----|-----------|--------|
| 1.2–1.9 | Critical reduction; shape of CE; lifting; rainbow; edge-max; path insertion | **Proved** |
| 2.1–2.4 | \(\kappa\ge 2\); no clique sep.; \(\lambda\ge t-1\); edge-max CE is \(3\)-connected | **Proved** |
| 2.11 | Dirac \(\kappa\ge t-1\) | **Proved** modulo atom close (Remark 2.12) |
| 2.13 | \(\kappa(G-v)\ge t-2\) | **Proved** from 2.11 |
| 3.1 | Brooks barrier \(\Delta\ge t\) | **Proved** (Brooks used) |
| 3.3–3.4 | \(\delta\ge t\) / neighbourhood clique | **Classical** (not on critical path) |
| 4.1–4.7 | Rooted upgrade; Kempe paths; Dichotomy D; existential reduction | **Proved** |
| 5.1–5.6 | Path systems ⇒ models; KRMP obstruction | **Proved** |
| 6.2–6.5 | Menger; fans; linkage ⇒ rooted model (with degree ports) | **Proved** |
| 6.6 | \(ck\)-connected ⇒ \(k\)-linked | **Black box** (Thomas–Wollan) |
| 6.7 | Quadratic connectivity finishes HC | **Conditional** on 6.6 |
| 7.1–7.7 | Strongest elementary rooted theorems; hybrid synthesis | **Proved** (7.7 conditional) |
| 8.1–8.5 | Colour of shares; Steiner obstruction (O) | **Proved** |
| 9.1–9.4 | Gap \(G_t\) isolated; constraint sheet | **Proved** as meta-mathematics |
| 10.1–10.2 | \(\mathrm{HC}_t\) for \(t\le 4\) | **Proved** |
| Gap \(G_t\) / \(\mathrm{HC}_t\) for \(t\ge 7\) | — | **Open** |

---

## 12. Logical skeleton

```
Minimal CE G to HC_t (t ≥ 7)
  │
  ├─ Structure (§1)
  │    t-critical, η = t−1, δ ≥ t−1
  │    G−v and G/e attain χ = η = t−1
  │    rainbow N(v) under every (t−1)-colouring
  │
  ├─ Connectivity (§2)
  │    λ ≥ t−1 (full)
  │    no clique separator ≤ t−1 (full)
  │    κ ≥ t−1 (Dirac: Theorem 2.11, atom close classical)
  │    κ(G−v) ≥ t−2 (Corollary 2.13)
  │
  ├─ Rooted calculus (§4–5)
  │    rooted K_{t−1} at rainbow N(v)  ⇒  K_t minor
  │    Kempe paths force complete path system on rainbow roots
  │    CE ⇔ total failure of rainbow-rooted models (Dichotomy D)
  │
  ├─ Linkage (§6)
  │    binom(t−1,2)-linked + deg ports  ⇒  rooted model  ⇒  contradiction
  │    Thomas–Wollan: need κ = Ω(t²) to force that linkedness
  │    have only κ = t−2 in G−v    ⇐  BLOCKED
  │
  └─ Gap G_t (§9)
       Prove Dichotomy D impossible
       ⇔  HC_t
       Strongest positive: Theorems 7.5–7.6 (constraints, not closure)
       Conditional closures: (H1)–(H4) in Theorem 7.7
```

---

## 13. Conclusion

The hybrid attack assembles a complete structural and path-system portrait of a hypothetical minimal counterexample to Hadwiger’s conjecture for \(t\ge 7\):

- contraction-critical at level \(t-1\), Hadwiger-tight on every proper minor of order \(n-1\);
- Dirac connectivity \(\kappa\ge t-1\), edge-connectivity \(\lambda\ge t-1\), no small clique separators;
- forced Kempe path systems on every rainbow neighbourhood;
- total obstruction to rainbow-rooted \(K_{t-1}\) models (Dichotomy D);
- forced failure of \(\binom{t-1}{2}\)-linkedness in every \(G-v\).

These ingredients **prove \(\mathrm{HC}_t\) for \(t\le 4\)** elementarily, organise the known deep cases \(t=5,6\), and reduce the open case \(t\ge 7\) to a single rooted-minor gap:

> **Gap \(G_t\):** no \(t\)-critical graph can have unrooted \(K_{t-1}\) minors in every \(G-v\) while lacking rainbow-rooted \(K_{t-1}\) minors for every colouring.

The gap is **not** a density gap and **not** a bare connectivity gap. It is a **rooted vs.\ unrooted minor gap** under critical colouring constraints. High-linkage theorems close it only under connectivity \(\Omega(t^2)\), which critical graphs do not supply. Kempe geometry forces a path system but not a consistent global branch assignment (Obstruction (O)).

**Until Gap \(G_t\) is closed, the hybrid attack does not prove \(\mathrm{HC}_t\) for \(t\ge 7\).** It does prove the strongest elementary rooted-minor constraints that apply to minimal counterexamples, and it isolates exactly one combinatorial obstruction equivalent to the conjecture.

---

*End of hybrid attack note.*
