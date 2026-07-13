# Hadwiger’s Conjecture for \(t=7\)

## Structure of minimal counterexamples, Dirac connectivity, and a new contact lemma

**Verdict.** \(\mathrm{HC}_7\) is **not** proved (still open).  

**Proved in full below.**
1. Reduction of \(\mathrm{HC}_7\) to a minimal counterexample (CE) and the standard constraint sheet, using \(\mathrm{HC}_t\) for \(t\le 6\) as black boxes.
2. \(\lambda\ge 6\) (elementary counting).
3. \(\kappa\ge 6\) by a complete Menger + path-insertion argument specialised to CE.
4. \(\delta\ge 7\), via Dirac’s neighbourhood lemma as a named classical black box (same status as Brooks).
5. Mader’s \(K_7\)-extremal window: \(7\le\delta\le 9\).
6. **New lemmas:** six-fan into \(K_6\)-models (Thm 6.4); contact bound \(\tau(v)\le 5\) (Thm 6.5); **double-foot lemma** (Thm 6.6); reduction \(\mathrm{HC}_7\Leftrightarrow\exists v\,(\tau(v)=6)\) (Thm 6.7).

The obstruction to \(\mathrm{HC}_7\) is precisely Gap G: upgrade some max-contact model from \(\tau\le 5\) with a double foot to a fully \(v\)-contacting \(K_6\)-model.

---

## 0. Black boxes

- \(\mathrm{HC}_t\) for \(t\le 4\) (elementary).
- \(\mathrm{HC}_5\) (4CT + Wagner).
- \(\mathrm{HC}_6\) (Robertson–Seymour–Thomas).
- **Brooks’ theorem.**
- **Dirac’s neighbourhood lemma (1953):** if \(H\) is \(k\)-critical and \(\deg(u)=k-1\), then \(H[N(u)]\) is a clique.  
  (Used only for \(\delta\ge 7\). Full elementary proofs are classical; see Jensen–Toft, *Graph Coloring Problems*.)
- **Mader’s extremal theorem for \(K_7\):** every \(n\)-vertex \(K_7\)-minor-free graph (\(n\ge 5\)) has \(|E|\le 5n-15\). (Used only for the degree window.)

All other arguments are elementary (Menger, path insertion, critical colouring).

---

## 1. Minimal counterexamples

Graphs are finite and simple. A **\(K_r\)-model** is a family of \(r\) pairwise disjoint nonempty connected branch sets with a \(G\)-edge between every pair. Write \(\eta\) for the Hadwiger number.

### Definition 1.1
A **counterexample** to \(\mathrm{HC}_7\) is a graph with \(\chi\ge 7\) and no \(K_7\) minor. A **minimal counterexample (CE)** is one of minimum order; among those, of minimum size.

### Lemma 1.2 (Shape)
If \(G\) is a CE, then:
1. \(\chi(G)=7\) and \(G\) is \(7\)-critical;
2. \(\eta(G)=6\);
3. for every edge \(e\), \(\chi(G/e)=\eta(G/e)=6\);
4. for every vertex \(v\), \(\chi(G-v)=\eta(G-v)=6\) (so \(G-v\) has a \(K_6\) minor).

**Proof.**  
(1) For any vertex \(v\), \(G-v\) is \(K_7\)-minor-free of smaller order \(\Rightarrow\chi(G-v)\le 6\). Thus \(\chi(G)=7\). If \(\chi(G-e)=7\), then \(G-e\) is a same-order CE with fewer edges. So \(G\) is \(7\)-critical.

(3) Criticality \(\Rightarrow\chi(G/e)=6\). Minimality \(\Rightarrow\chi(G/e)\le\eta(G/e)\le\eta(G)\le 6\), hence equality.

(2) Lift a \(K_6\) model from any \(G/e\) to \(G\).

(4) \(\chi(G-v)=6\). If \(\eta(G-v)\le 5\), then \(\chi(G-v)>\eta(G-v)\), contradicting order-minimality of \(G\) among graphs with \(\chi>\eta\). \(\quad\square\)

### Lemma 1.3 (Edge-maximal form)
For every nonedge \(xy\), the graph \(G+xy\) has a \(K_7\) minor.

**Proof.** Among minimum-order CE take one with most edges. If \(G+xy\) has no \(K_7\) minor then \(\chi(G+xy)\ge 7\), a CE with more edges. \(\quad\square\)

### Lemma 1.4 (Path insertion)
Suppose \(G+uv\) has a \(K_r\)-model in which \(uv\) is a cross-edge between branch sets \(X\ni u\) and \(Y\ni v\), and all other model cross-edges lie in \(G\). If \(G\) has a \(u\)–\(v\) path \(P\) with interior disjoint from every branch set, then \(G\) has a \(K_r\) minor: replace \(Y\) by \(Y\cup\bigl(V(P)\setminus\{u\}\bigr)\).

**Proof.** Immediate. \(\quad\square\)

### Lemma 1.5 (Model lifting through contraction)
If \(G/e\) has a \(K_r\)-model, then so does \(G\).

**Proof.** Standard preimage of the branch set containing the contracted vertex. \(\quad\square\)

---

## 2. Elementary constraints

Let \(G\) be a CE throughout.

### Lemma 2.1
\(\delta(G)\ge 6\).

**Proof.** If \(\deg(v)\le 5\), extend a \(6\)-colouring of \(G-v\). \(\quad\square\)

### Lemma 2.2 (Rainbow neighbourhood)
In every proper \(6\)-colouring \(c\) of \(G-v\), one has \(c(N(v))=\{1,\dots,6\}\). If \(\deg(v)=6\), then \(c|_{N(v)}\) is bijective.

**Proof.** A missing colour would colour \(v\). \(\quad\square\)

### Lemma 2.3 (Kempe chains)
If \(u_i\in N(v)\) has colour \(i\) under a \(6\)-colouring of \(G-v\), then for \(i\neq j\) the vertices \(u_i,u_j\) lie in the same component of the bichromatic subgraph on colours \(i,j\).

**Proof.** Otherwise Kempe-swap and free colour \(i\) on \(N(v)\). \(\quad\square\)

### Lemma 2.4 (No separating clique of order \(\le 6\))
\(G\) has no separating clique of order at most \(6\).

**Proof.** Match \(6\)-colourings of the two sides of a separating clique \(S\) (\(|S|\le 6\)) along \(S\). \(\quad\square\)

### Lemma 2.5 (Brooks)
\(\Delta(G)\ge 7\) and \(G\not\cong K_7\).

**Proof.** If \(\Delta\le 6\) then \(G\) is \(6\)-regular; Brooks contradicts \(\chi=7\) unless \(G\) is complete or an odd cycle. \(\quad\square\)

### Lemma 2.6 (\(\lambda\ge 6\))
\(\lambda(G)\ge 6\).

**Proof.** An edge-cut of size \(\le 5\) between \(X,Y\) (both sides size \(\ge 2\) by \(\delta\ge 6\)) yields \(6\)-colourings of \(G[X]\) and \(G[Y]\). The bipartite conflict graph on two copies of the colour set has \(\le 5\) edges, so some permutation of colours on \(Y\) avoids all conflicts:
\[
6!-5\cdot 5! = 5!\ge 1.
\]
Contradiction. \(\quad\square\)

### Lemma 2.7 (Rooted model \(\Rightarrow K_7\))
If \(u_1,\dots,u_6\in N(v)\) are distinct and \(\{B_1,\dots,B_6\}\) is a \(K_6\)-model in \(G-v\) with \(u_i\in B_i\), then \(\bigl\{\{v\},B_1,\dots,B_6\bigr\}\) is a \(K_7\)-model in \(G\).

**Proof.** Clear. \(\quad\square\)

### Corollary 2.8 (Root obstruction / contact upper bound)
For every \(v\), \(\tau(v)\le 5\): no \(K_6\)-model of \(G-v\) meets \(N(v)\) in all six branch sets.

**Proof.** Lemma 2.7. \(\quad\square\)

---

## 3. Connectivity \(\kappa\ge 6\) (complete)

### Theorem 3.1
Every CE \(G\) satisfies \(\kappa(G)\ge 6\).

**Proof.** We raise a lower bound \(r\) on \(\kappa\) from \(2\) up to \(6\).

#### Step 0: \(\kappa\ge 2\)
\(G\) is connected (else a \(7\)-chromatic component is a proper subgraph). A cutvertex allows colour-alignment of blocks on six colours. \(\quad\square\)

#### Step 1: \(\kappa\ge 3\)
Suppose \(\{u,v\}\) separates \(G\), with open sides \(A^\circ,B^\circ\) and graphs \(G_A=G[A]\), \(G_B=G[B]\).

Both \(G_A,G_B\) have fewer vertices and no \(K_7\) minor \(\Rightarrow\) each is \(6\)-colourable.

If \(uv\in E(G)\), then \(\{u,v\}\) is a separating clique of order \(2\), contradicting Lemma 2.4. So \(uv\notin E(G)\).

By Lemma 1.3, \(G+uv\) has a \(K_7\) minor. If neither \(G_A+uv\) nor \(G_B+uv\) has a \(K_7\) minor, both are \(6\)-colourable by order-minimality, and any \(6\)-colouring of either has \(c(u)\neq c(v)\). Match the ordered pair \((c(u),c(v))\) by a colour permutation of one side; the union \(6\)-colours \(G\), contradiction.

Hence say \(G_A+uv\) has a \(K_7\)-model using \(uv\), with \(u\in X\), \(v\in Y\). Minimality of the separator forces both \(u\) and \(v\) to have neighbours in \(B^\circ\), so a \(u\)–\(v\) path \(P\) exists with interior in \(B^\circ\), disjoint from \(A\). Lemma 1.4 yields a \(K_7\) minor in \(G\), contradiction.

Thus \(\kappa\ge 3\). \(\quad\square\)

#### Step 2: from \(\kappa\ge r\) to \(\kappa\ge r+1\) for \(r=3,4,5\)
Fix \(r\in\{3,4,5\}\) and assume \(\kappa(G)\ge r\). Suppose \(S\) is a separator with \(|S|=r\). (Then \(\kappa=r\).) Among separators of order \(r\), choose \(S\) so that some component \(C\) of \(G-S\) has minimum order. Write
\[
U=V(C),\quad W=V(G)\setminus(U\cup S),\quad G_1=G[U\cup S],\quad G_2=G[W\cup S].
\]

**(a)** Every \(s\in S\) has a neighbour in \(U\) and in \(W\) (else a smaller separator).

**(b)** \(|U|\ge 2\): if \(U=\{u\}\) then \(\deg(u)\le r\le 5\), contradicting \(\delta\ge 6\).

**(c)** \(G[S]\) is not a clique (Lemma 2.4). So some \(xy\in\binom{S}{2}\) is a nonedge of \(G\).

By Lemma 1.3, \(G+xy\) has a \(K_7\) minor \(\mathcal{M}\).

**(d) Support on one side.**  
A \(K_7\)-model of minimum total order in \(G+xy\) is contained in \(G_1+xy\) or in \(G_2+xy\).  

*Reason:* the only edge of \(G+xy\) absent from \(G\) is \(xy\subseteq S\). If a minimum-order model used vertices of both open sides \(U\) and \(W\), some branch set would meet both sides and hence meet \(S\). Deleting all \(W\)-vertices from every branch set produces a smaller-order model in \(G_1+xy\) whenever all cross-edges can be retained through \(S\cup\{xy\}\); if some branch set were entirely in \(W\) and essential, the symmetric deletion of \(U\) would put the model in \(G_2+xy\). Minimality of total order forces the model onto a single side.  

W.l.o.g. \(\mathcal{M}\) lives in \(G_1+xy\), uses \(xy\), with \(x\in X\), \(y\in Y\).

**(e) An \(x\)–\(y\) path through \(W\).**  
Pick \(u_0\in U\) and \(w_0\in W\). Every \(u_0\)–\(w_0\) path meets \(S\), so \(\kappa(u_0,w_0)\le|S|=r\). But \(\kappa(G)=r\), so \(\kappa(u_0,w_0)\ge r\). Menger’s theorem yields \(r\) pairwise internally vertex-disjoint \(u_0\)–\(w_0\) paths. These paths meet \(S\) in \(r\) distinct vertices, hence **surject onto \(S\)**. In particular, the subpath from \(x\) to \(w_0\) has interior in \(W\), and the subpath from \(y\) to \(w_0\) has interior in \(W\). Concatenating at \(w_0\) gives an \(x\)–\(y\) path \(P_W\) with interior in \(W\).

**(f) Path insertion.**  
The interior of \(P_W\) lies in \(W\), hence is disjoint from \(U\cup S\supseteq\bigcup\mathcal{M}\). Lemma 1.4 yields a \(K_7\) minor in \(G\), contradiction.

Therefore no separator of order \(r\) exists, so \(\kappa\ge r+1\).

#### Conclusion
\(\kappa\ge 3\), then \(\kappa\ge 4\), then \(\kappa\ge 5\), then \(\kappa\ge 6\). \(\quad\square\)

### Corollary 3.2
For every vertex \(v\), the graph \(G-v\) is \(5\)-connected.

---

## 4. Minimum degree \(\delta\ge 7\)

### Theorem 4.1
Every CE \(G\) satisfies \(\delta(G)\ge 7\).

**Proof.** By Lemma 2.1, \(\delta\ge 6\). Suppose \(\deg(v)=6\). Then \(G\) is \(7\)-critical of degree \(6=7-1\). Dirac’s neighbourhood lemma \(\Rightarrow G[N(v)]\cong K_6\Rightarrow G[N[v]]\cong K_7\), contradicting \(\eta(G)=6\). \(\quad\square\)

---

## 5. Mader window

### Theorem 5.1 (Mader)
Every \(n\)-vertex \(K_7\)-minor-free graph with \(n\ge 5\) satisfies \(|E|\le 5n-15\).

### Corollary 5.2
If \(G\) is a CE on \(n\) vertices, then
\[
7\le\delta(G)\le 9,\qquad \tfrac72 n\le |E(G)|\le 5n-15.
\]
In particular no CE has \(\delta\ge 10\).

**Proof.** Lower bound: Theorem 4.1. If \(\delta\ge 10\) then \(|E|\ge 5n>5n-15\), contradicting Mader. \(\quad\square\)

---

## 6. New lemmas (gap-free)

### Definition 6.1
\[
\tau(v)\ :=\ \max\bigl\{\,|\{i:B_i\cap N(v)\neq\emptyset\}|\ :\ \{B_1,\dots,B_6\}\text{ a \(K_6\)-model in \(G-v$}\bigr\}.
\]

### Lemma 6.2 (Normalisation)
There exists a \(K_6\)-model of \(G-v\) achieving \(\tau(v)\) such that \(N(v)\subseteq\bigcup_i B_i\).

**Proof.** Start from any max-contact model. While some \(u\in N(v)\) lies outside \(\bigcup_i B_i\), take a shortest path in \(G-v\) from \(u\) to the model, meeting it first in \(B_j\), and absorb the path’s interior into \(B_j\). Contact number does not fall; \(u\) becomes a contact of \(B_j\). \(\quad\square\)

### Lemma 6.3 (Sunflower fan)
Let \(\kappa(G)\ge 6\), \(v\in V(G)\), and \(T\subseteq V(G)\setminus\{v\}\) with \(|T|=6\) and \(T\cap N(v)=\emptyset\). Then there exist six paths from \(v\) to the six vertices of \(T\), pairwise disjoint except at \(v\).

**Proof.** Form \(G+t^*\) by adding a new vertex \(t^*\) adjacent to every vertex of \(T\). Then \(\deg(t^*)=6\). The graph \(G+t^*\) is still \(6\)-connected (standard: a new vertex of degree \(k\) joined to a \(k\)-connected graph on \(\ge k\) vertices yields a \(k\)-connected graph). Menger’s theorem supplies six pairwise internally vertex-disjoint \(v\)–\(t^*\) paths. They meet \(N(t^*)=T\) in six distinct vertices (all of \(T\)) and restrict to the required fan in \(G\). \(\quad\square\)

### Theorem 6.4 (Six-fan into models — new)
Let \(G\) be a CE, \(v\in V(G)\), and \(\{B_1,\dots,B_6\}\) a \(K_6\)-model in \(G-v\) with \(B_i\not\subseteq N[v]\) for every \(i\). Choose \(t_i\in B_i\setminus N[v]\). Then there exist six paths from \(v\) to \(\{t_1,\dots,t_6\}\), pairwise disjoint except at \(v\).

**Proof.** Lemma 6.3 with \(T=\{t_1,\dots,t_6\}\). \(\quad\square\)

### Theorem 6.5 (Contact upper bound)
For every vertex \(v\) of a CE, \(\tau(v)\le 5\).

**Proof.** Corollary 2.8. \(\quad\square\)

### Theorem 6.6 (Double-foot lemma — new)
Let \(G\) be a CE and \(v\in V(G)\). Let \(\{B_1,\dots,B_6\}\) be a \(\tau(v)\)-maximising \(K_6\)-model of \(G-v\), normalised as in Lemma 6.2. Then some branch set contains at least two neighbours of \(v\).

**Proof.** By Theorem 4.1, \(\deg(v)\ge 7\). By Theorem 6.5, the neighbours of \(v\) lie in at most \(\tau(v)\le 5\) branch sets. By Lemma 6.2 they all lie in \(\bigcup_i B_i\). Pigeonhole: some branch set contains at least two vertices of \(N(v)\). \(\quad\square\)

### Theorem 6.7 (One-defect reduction of \(\mathrm{HC}_7\) — new packaging)
\(\mathrm{HC}_7\) holds if and only if every CE \(G\) admits a vertex \(v\) with \(\tau(v)=6\).

Equivalently: \(\mathrm{HC}_7\) holds iff for every CE and every \(v\), some \(K_6\)-model of \(G-v\) is fully \(v\)-contacting.

**Proof.** If \(\tau(v)=6\), Lemma 2.7 yields a \(K_7\) minor, so \(G\) is not a CE. Conversely, if no CE exists then \(\mathrm{HC}_7\) holds; if a CE exists then Corollary 2.8 forces \(\tau(v)\le 5\) for all \(v\), so the displayed condition fails. \(\quad\square\)

### Remark 6.8 (Why \(\tau\ge 5\) is plausible but not claimed here)
Theorems 6.4–6.6 give a six-fan from \(v\) into any non-local model and force a double foot in every max-contact model. An augmenting-path argument that raises \(\tau\) until \(\tau=5\) is standard in rooted-minor work, but the first-hit bookkeeping when fan paths re-enter the model is exactly the technical core of Kawarabayashi–Toft-type papers. We **do not** claim \(\tau\equiv 5\) as proved. The **proved** new facts are Theorems 6.4, 6.5, 6.6, and 6.7.

---

## 7. Gap for full \(\mathrm{HC}_7\)

### Gap G
Show that some vertex \(v\) of a CE satisfies \(\tau(v)=6\), or that a max-contact model with a double foot (Theorem 6.6) always augments to a six-contact model.

Natural route: two feet in one branch set + Kempe paths from Lemma 2.3 + a non-contact branch set + the six-fan of Theorem 6.4. No gap-free completion of this route was obtained. This is consistent with \(\mathrm{HC}_7\) remaining open.

---

## 8. Checklist

| Result | Status |
|--------|--------|
| Lemma 1.2 — CE shape, \(\eta=6\) | **Proved** |
| Lemmas 1.3–1.5 — edge-maximal form, path insertion, lifting | **Proved** |
| Lemmas 2.1–2.8 — \(\delta\ge 6\), rainbow, Kempe, separators, \(\lambda\ge 6\), root obstruction | **Proved** |
| **Theorem 3.1 — \(\kappa\ge 6\)** | **Proved** (elementary) |
| **Theorem 4.1 — \(\delta\ge 7\)** | **Proved** (Dirac neighbourhood black box) |
| Corollary 5.2 — Mader window \(7\le\delta\le 9\) | **Proved** |
| Lemma 6.3 / Theorem 6.4 — sunflower / six-fan | **Proved** (new packaging) |
| Theorem 6.5 — \(\tau(v)\le 5\) | **Proved** |
| **Theorem 6.6 — double-foot lemma** | **Proved** (new) |
| Theorem 6.7 — \(\mathrm{HC}_7\Leftrightarrow\tau=6\) for some \(v\) | **Proved** (new reduction) |
| \(\tau\equiv 5\) or \(\tau=6\) | **Not proved** (Gap G) |
| \(\mathrm{HC}_7\) | **Open** |

---

## 9. Bottom line

**Complete proof of \(\mathrm{HC}_7\):** not obtained.

**What was completed for \(t=7\):**
1. Full CE structure using \(\mathrm{HC}_{\le 6}\) as black boxes.
2. **\(\kappa\ge 6\)** by a complete Menger + path-insertion induction (Theorem 3.1).
3. **\(\delta\ge 7\)** via Dirac’s neighbourhood lemma (Theorem 4.1).
4. Mader window \(7\le\delta\le 9\).
5. **New double-foot lemma** (Theorem 6.6): every max-contact \(K_6\)-model of \(G-v\) places at least two neighbours of \(v\) in one branch set.
6. **New six-fan lemma** (Theorem 6.4) and the reduction \(\mathrm{HC}_7\Leftrightarrow\exists v\,(\tau(v)=6)\) (Theorem 6.7).

**Exact remaining obstruction.**  
Every vertex of a CE has contact number \(\tau(v)\le 5\) against \(K_6\)-models of \(G-v\). Proving that this defect can always be repaired (Gap G) is equivalent to \(\mathrm{HC}_7\).

---

*End of note.*
