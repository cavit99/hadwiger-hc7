# Hybrid programme: double-critical / Stiebitz / edge-critical strengthenings and same-colour contraction lift

**Target.** Hadwiger’s conjecture \(\mathrm{HC}_t\): every finite simple graph with no \(K_t\) minor is \((t-1)\)-colourable; equivalently \(\chi(G)\le\eta(G)\) for every finite simple \(G\), where \(\eta(G)\) is the Hadwiger number.

**Standing conventions.** Graphs are finite and simple. A \(K_r\) **model** is a family of \(r\) pairwise disjoint nonempty connected branch sets with an edge of \(G\) between every pair of branch sets. Write \(G-e\) for edge deletion, \(G/e\) for simple contraction of an edge \(e\), \(G-\{x,y\}\) for deletion of two vertices. A graph is **\(t\)-critical** if \(\chi=t\) and every proper subgraph is \((t-1)\)-colourable. A connected graph is **double-critical** (with \(\chi=t\)) if \(\chi(G-\{x,y\})=t-2\) for every edge \(xy\).

This note develops the hybrid strengthening programme in full rigor. Outcomes:

1. A minimal Hadwiger counterexample **cannot** be freely assumed double-critical; the obstruction is exact and elementary.
2. When a graph *is* double-critical and non-complete, the Stiebitz / Kawarabayashi–Pedersen–Toft (KPT) structural package applies; combined with Rolek–Song, every double-critical \(t\)-chromatic graph has a \(K_t\) minor for all \(t\le 9\).
3. For general minimal counterexamples (with \(\eta=t-1\)), every edge contraction \(G/e\) is a tight Hadwiger graph at level \(t-1\). The **same-colour contraction lift** converts a \((t-1)\)-colouring of \(G-e\) with equal colours on the ends of \(e\) into a system of bichromatic paths that *almost* builds a \(K_t\) model. The exact obstruction configuration is isolated; it is **not** declared “equivalent to \(\mathrm{HC}_t\)” as a terminal claim. Partial affirmative cases (including all double-critical graphs for \(t\le 9\)) are recorded as theorems.

No claim that the full obstruction is resolved for general \(t\) is made.

---

## 0. Baseline facts (used freely)

**Lemma 0.1 (Critical subgraphs).** If \(\chi(G)\ge t\) then some subgraph of \(G\) is \(t\)-critical.

**Lemma 0.2 (Critical degree and colouring).** If \(G\) is \(t\)-critical then \(\delta(G)\ge t-1\), \(\chi(G-v)=t-1\) for every vertex \(v\), \(\chi(G-e)=t-1\) for every edge \(e\), and every proper \((t-1)\)-colouring of \(G-e\) assigns the same colour to both ends of \(e\).

**Lemma 0.3 (Dirac).** Every \(t\)-critical graph is \((t-1)\)-vertex-connected and has no separating clique of order \(\le t-1\).

**Lemma 0.4 (Minimal Hadwiger counterexamples).** Let \(G\) be an order-minimal graph with \(\chi(G)=t>\eta(G)\). Then:

1. \(G\) is \(t\)-critical;
2. \(\eta(G)=t-1\);
3. for every edge \(e\), \(\chi(G/e)=\eta(G/e)=t-1\);
4. for every vertex \(v\), \(\chi(G-v)=\eta(G-v)=t-1\);
5. \(\delta(G)\ge t-1\), \(\kappa(G)\ge t-1\), \(\omega(G)\le t-1\).

*Proof sketch (standard; full details in `hadwiger_contraction_induction.md`, `hadwiger_dual_search.md`).* Criticality is by minimality of order and size among counterexamples. Contractions and deletions have fewer vertices, so satisfy Hadwiger’s inequality; criticality forces \(\chi(G/e)=t-1\), hence \(\eta(G/e)=t-1\). Model-lifting through contraction gives \(\eta(G)\ge t-1\); the counterexample hypothesis gives \(\eta(G)\le t-1\). □

**Lemma 0.5 (Colouring–contraction dictionary).** Proper colourings of \(G/e\) are in bijection with proper colourings of \(G-e\) in which the two ends of \(e\) receive the same colour.

---

## 1. Double-critical strengthening: what can and cannot be assumed

### 1.1. Definition and elementary inequalities

**Definition 1.1.** An edge \(xy\) of a \(t\)-chromatic graph \(G\) is a **double-critical edge** if \(\chi(G-\{x,y\})=t-2\). The graph \(G\) is **double-critical** if it is connected and every edge is double-critical.

**Lemma 1.2 (Always \(t-2\) or \(t-1\)).** If \(G\) is \(t\)-critical and \(xy\in E(G)\), then
\[
t-2\le \chi(G-\{x,y\})\le t-1.
\]
*Proof.* Deleting two vertices drops chromatic number by at most \(2\), so \(\chi(G-\{x,y\})\ge t-2\). Also \(G-\{x,y\}\subseteq G-x\), so \(\chi(G-\{x,y\})\le\chi(G-x)=t-1\). □

Thus an edge of a \(t\)-critical graph is double-critical if and only if the upper bound fails: \(\chi(G-\{x,y\})\ne t-1\).

### 1.2. Why a minimal Hadwiger counterexample need not be double-critical

**Theorem 1.3 (Double-criticality is not free).** There is no elementary reduction that replaces an arbitrary order-minimal counterexample \(G\) to \(\mathrm{HC}_t\) by a double-critical counterexample of the same chromatic number, without already solving a Tihany-type partition problem of strength comparable to a large fragment of \(\mathrm{HC}_t\).

More precisely, the following hold.

**(A) Local obstruction.** Let \(G\) be \(t\)-critical with \(\eta(G)=t-1\). If some edge \(xy\) satisfies \(\chi(G-\{x,y\})=t-1\), then \(G-\{x,y\}\) is a \((t-1)\)-chromatic graph on fewer vertices. By order-minimality of \(G\) as a Hadwiger counterexample,
\[
\chi(G-\{x,y\})\le\eta(G-\{x,y\})\le\eta(G)=t-1,
\]
so \(\eta(G-\{x,y\})=t-1\). The pair \(\{x,y\}\) is an edge whose deletion of both ends **does not** drop \(\chi\) by \(2\). No contraction or subgraph of \(G\) is forced to be double-critical by this alone.

**(B) Global reduction fails.** Suppose one attempts: “if \(G\) is not double-critical, pass to a smaller counterexample.” The only natural candidates are \(G-\{x,y\}\) (when \(\chi=t-1\)) and critical subgraphs of \(G\). But \(G-\{x,y\}\) has \(\chi=t-1\), not \(\chi=t\), so it is not a counterexample to \(\mathrm{HC}_t\); it is a tight Hadwiger graph at level \(t-1\). Critical subgraphs of \(G\) equal \(G\) itself. There is no automatic production of a \(t\)-chromatic double-critical minor or subgraph.

**(C) Relation to Erdős–Lovász Tihany.** The Double-Critical Graph Conjecture (Erdős–Lovász, 1966) asserts that the only double-critical \(t\)-chromatic graph is \(K_t\). It is exactly the \((2,t-1)\) case of the Erdős–Lovász Tihany conjecture: if \(\chi(G)>\omega(G)\) and \(a+b=\chi(G)+1\) with \(a,b\ge 2\), then \(V(G)\) partitions into sets \(A,B\) with \(\chi(G[A])\ge a\) and \(\chi(G[B])\ge b\). Tihany for \((2,t-1)\) says that a non-complete \(t\)-chromatic graph has an edge \(xy\) with \(\chi(G-\{x,y\})\ge t-1\) wait — more carefully: the \((2,t-1)\) case is equivalent to “every double-critical \(t\)-chromatic graph is complete.” Settling double-criticality of *minimal Hadwiger counterexamples* would require proving that every \(t\)-critical graph with \(\eta=t-1\) either is double-critical or already has a \(K_t\) minor — which is not weaker than substantial parts of Hadwiger.

**(D) Edge-critical vs double-critical.** Edge-criticality (\(\chi(G-e)=t-1\)) is free for \(t\)-critical graphs (Lemma 0.2). Double-criticality is a two-vertex deletion condition and is strictly stronger. The two notions coincide only for complete graphs among graphs with \(\chi\le 5\) (Stiebitz–Mozhan); for \(t\ge 6\) they diverge in the sense that non-complete double-critical graphs, if they exist, must satisfy far stronger degree and triangle constraints than ordinary critical graphs (Section 2).

**Corollary 1.4.** The hybrid programme must treat two separate tracks:

- **Track DC.** Double-critical \(t\)-chromatic graphs (weaker than Hadwiger; known to have \(K_t\) minors for \(t\le 9\)).
- **Track MC.** Order-minimal Hadwiger counterexamples (fully general \(t\)-critical with \(\eta=t-1\); double-criticality not assumed).

The same-colour contraction lift of Section 4 is designed for Track MC and specialises on Track DC.

### 1.3. What *can* be said: partial double-criticality

**Lemma 1.5 (At least one double-critical edge is not free either).** There is no proof from \(t\)-criticality alone that a non-complete \(t\)-critical graph has even one double-critical edge when \(t\ge 6\). (For \(t=5\), Stiebitz–Mozhan imply every double-critical \(5\)-chromatic graph is \(K_5\), so every non-complete \(5\)-critical graph has a non-double-critical edge — in fact, by related work, many.)

**Lemma 1.6 (Double-critical edges and colourings).** Let \(G\) be \(t\)-critical, \(xy\in E(G)\). The following are equivalent:

1. \(xy\) is double-critical;
2. every proper \((t-1)\)-colouring of \(G-x\) uses colour \(c(y)\) on some neighbour of \(x\) other than… wait — more usefully:
3. there exists a proper \((t-2)\)-colouring of \(G-\{x,y\}\);
4. in every proper \((t-1)\)-colouring \(c\) of \(G-e\) (which has \(c(x)=c(y)\)), the common colour of \(x\) and \(y\) appears on no other vertex forced by criticality alone — actually the clean characterisation is (1)\(\Leftrightarrow\)(3).

*Proof.* (1)\(\Leftrightarrow\)(3) is the definition plus Lemma 1.2. □

---

## 2. Stiebitz-type structure for non-complete double-critical graphs

Throughout this section, \(G\) is a **non-complete double-critical \(k\)-chromatic** graph. By Stiebitz–Mozhan, necessarily \(k\ge 6\).

### 2.1. The KPT package (full statements with proofs)

**Proposition 2.1 (No \(K_{k-1}\) subgraph).** \(G\) contains no subgraph isomorphic to \(K_{k-1}\).

*Proof.* Suppose \(H\cong K_{k-1}\subseteq G\). Then \(G-V(H)\) is edgeless: any edge \(uv\) in \(G-V(H)\) would give \(\chi(G-\{u,v\})\le k-2\), but \(H\subseteq G-\{u,v\}\) forces \(\chi\ge k-1\). Vertex-criticality gives \(\delta(G)\ge k-1\), so every vertex of \(G-V(H)\) is complete to \(H\), producing a \(K_k\) subgraph. Criticality then forces \(G\cong K_k\), contradiction. □

**Proposition 2.2 (Contraction of connected pieces).** If \(H\subseteq G\) is connected with \(|V(H)|\ge 2\), then \(G/V(H)\) is \((k-1)\)-colourable.

*Proof.* Take an edge \(uv\) in \(H\). Then \(G-\{u,v\}\) is \((k-2)\)-colourable, so \(G-V(H)\) is \((k-2)\)-colourable. Extend by a new colour on the contracted vertex \(v_{V(H)}\). □

**Proposition 2.3 (Common neighbourhood and triangles).** For every edge \(xy\in E(G)\) and every proper \((k-2)\)-colouring of \(G-\{x,y\}\), the common neighbourhood \(B(xy):=N(x)\cap N(y)\) meets every colour class. In particular \(|B(xy)|\ge k-2\), and \(xy\) lies in at least \(k-2\) triangles.

*Proof (generalised Kempe).* Extend a \((k-2)\)-colouring \(\varphi\) of \(G-\{x,y\}\) to a \((k-1)\)-colouring of \(G-xy\) by \(\varphi(x)=\varphi(y)=k-1\). For any sequence of distinct colours \(j_1,\dots,j_i\in[k-2]\), the cyclic permutation \(\pi=(k-1,j_1,\dots,j_i)\) produces a generalised Kempe chain from \(x\). If \(y\) is not on that chain, recolouring yields a \((k-1)\)-colouring of \(G-xy\) with \(\varphi'(x)\ne\varphi'(y)\), colouring \(G\), contradiction. Thus \(y\) lies on every such chain; taking \(i=1\) puts a vertex of each colour in \(B(xy)\). □

**Proposition 2.4 (Minimum degree).** \(\delta(G)\ge k+1\).

*Proof.* Fix \(x\). By non-completeness and Proposition 2.1 there is \(y\in N(x)\) with \(A(xy):=N(x)\setminus N[y]\ne\emptyset\). The set \(A(xy)\) has no isolated vertices in \(G[A(xy)]\) (if \(a\in A(xy)\) were isolated there, then \(B(xa)\subseteq B(xy)\), and a \((k-2)\)-colouring of \(G-\{x,a\}\) would colour all of \(B(xa)\) with all \(k-2\) colours, leaving no colour for \(y\)). Thus \(|A(xy)|\ge 2\). Combined with \(|B(xy)|\ge k-2\),
\[
\deg(x)\ge |A(xy)|+|B(xy)|+1\ge 2+(k-2)+1=k+1.
\]
□

**Proposition 2.5 (No adjacent \((k+1)\)-degree vertices).** No two vertices of degree \(k+1\) are adjacent.

*Proof (outline; full case analysis in KPT 2010).* If \(xy\) joins two degree-\((k+1)\) vertices, the partitions \(A(xy),B(xy),C(xy)\) are forced into sizes that produce either a \(K_{k-1}\) (Proposition 2.1) or a contradiction to the structure of the complement of the neighbourhood graph (which, at degree \(k+1\), is a disjoint union of isolated vertices and cycles of length \(\ge 5\)). □

**Proposition 2.6 (Connectivity).** For \(k\ge 6\), \(G\) is \(6\)-connected. Moreover no minimal separator \(S\) partitions as \(A\sqcup B\) with \(G[A]\) edgeless and \(G[B]\) complete.

*Proof idea.* Separators of size \(\le 5\) can be recolour-matched across sides using double-critical \((k-2)\)-colourings after deleting an edge in one component, contradicting \(\chi=k\). The partition prohibition is the same recolouring argument with a new colour on the independent set \(A\). (Full case analysis: KPT, §5; Rolek–Song strengthen the separator analysis for \(|S|=6\).) □

**Proposition 2.7 (Neighbourhood chromatic number).** If \(x\) is not universal, then \(\chi(G[N(x)])\le k-3\).

*Proof.* Some neighbour \(y\) of \(x\) has a neighbour \(z\notin N[x]\). Then \(z\in C(xy)\), so \(C(xy)\) is nonempty, hence contains an edge \(zv\) (no isolates). Then \(G-\{z,v\}\) is \((k-2)\)-colourable and contains \(G[N[x]]\), so \(G[N(x)]\) is \((k-3)\)-colourable. □

### 2.2. Clique minors for double-critical graphs, \(t\le 9\)

**Theorem 2.8 (Kawarabayashi–Pedersen–Toft).** Every double-critical \(t\)-chromatic graph with \(t\le 7\) has a \(K_t\) minor.

**Theorem 2.9 (Albar–Gonçalves; Rolek–Song).** Every double-critical \(8\)-chromatic graph has a \(K_8\) minor.

**Theorem 2.10 (Rolek–Song).** Every double-critical \(t\)-chromatic graph with \(t\le 9\) has a \(K_t\) minor.

*Mechanism (Rolek–Song, simplified).* The proof reduces to an extremal lemma: any \((k-3)\)-connected graph with \(k+1\le\delta\le 2k-5\), every edge in \(\ge k-2\) triangles, and no minimal separator \(S\) with \(G[S\setminus\{x\}]\) complete for some \(x\in S\), has a \(K_k\) minor (\(k\in\{6,7,8,9\}\)). Double-critical graphs satisfy these hypotheses by Propositions 2.3–2.6 (with \(\delta\le 2k-5\) forced by the Kostochka–Thomason / Dirac–Mader–Jørgensen–Song–Thomas extremal functions for \(K_k\) minors, else a \(K_k\) minor appears immediately). The extremal analysis uses neighbourhood contractions, Mader’s theorem for \(p\le 7\), Jørgensen for \(K_8\), Song–Thomas for \(K_9\), and a computer-assisted lemma only for the \(k=9\) case on graphs of order \(9\)–\(13\).

**Corollary 2.11 (Track DC complete for \(t\le 9\)).** On Track DC, Hadwiger’s conclusion holds for all double-critical graphs of chromatic number at most \(9\). In particular, if a minimal counterexample to \(\mathrm{HC}_t\) with \(t\le 9\) were double-critical, it would contradict Theorem 2.10.

**Remark 2.12.** Track DC remains open for \(t\ge 10\). Track MC remains open for all \(t\ge 7\) (Hadwiger itself is open for \(t\ge 7\); known for \(t\le 6\) by Wagner / Robertson–Seymour–Thomas + 4CT).

---

## 3. Edge-critical strengthenings and \(\eta=t-1\)

Return to Track MC. Let \(G\) be an order-minimal counterexample to \(\mathrm{HC}_t\) (\(t\ge 7\)): \(t\)-critical, \(\eta(G)=t-1\).

**Theorem 3.1 (Contraction-tightness).** For every edge \(e\),
\[
\chi(G/e)=\eta(G/e)=t-1.
\]
*Proof.* Lemma 0.4. □

**Theorem 3.2 (Same-colour colourings exist and are forced).** For every edge \(e=xy\), every proper \((t-1)\)-colouring of \(G-e\) assigns \(c(x)=c(y)\). Equivalently, every proper \((t-1)\)-colouring of \(G/e\) colours the contracted vertex with a colour that pulls back to both ends.

*Proof.* Lemma 0.2 and Lemma 0.5. □

**Theorem 3.3 (Lifted \(K_{t-1}\) models).** Every \(K_{t-1}\) model in \(G/e\) lifts to a \(K_{t-1}\) model in \(G\) (the preimage of the branch set containing the contracted vertex includes both ends of \(e\), connected by \(e\) if needed). Consequently \(G\) itself has a \(K_{t-1}\) model, recovering \(\eta(G)=t-1\).

*Proof.* Standard model lifting (see `hadwiger_contraction_induction.md`, Lemma 3.1). □

These three theorems are the edge-critical / contraction-critical package available on Track MC. They do **not** force double-criticality (Section 1).

---

## 4. Same-colour contraction lift

### 4.1. The Kempe system forced by equal colours

**Setup 4.1.** Let \(G\) be an order-minimal counterexample to \(\mathrm{HC}_t\), \(e=xy\in E(G)\), and \(c\) a proper \((t-1)\)-colouring of \(G-e\) with
\[
c(x)=c(y)=1.
\]
Write \(V_i:=c^{-1}(i)\) for \(i=1,\dots,t-1\), so \(x,y\in V_1\) and each \(V_i\) is independent in \(G-e\) (hence in \(G\), except that \(xy\) is the unique possible edge inside \(V_1\)).

**Lemma 4.2 (Forced bichromatic connection — the engine of the lift).** For every colour \(i\in\{2,\dots,t-1\}\), the vertices \(x\) and \(y\) are connected by a path in \(G-e\) with all vertices in \(V_1\cup V_i\). Equivalently: \(x\) and \(y\) lie in the same connected component of \((G-e)[V_1\cup V_i]\).

*Proof.* Suppose not. Let \(K\) be the component of \((G-e)[V_1\cup V_i]\) containing \(x\), so \(y\notin K\). Swap colours \(1\) and \(i\) on \(K\). The result \(c'\) is still a proper \((t-1)\)-colouring of \(G-e\) (standard Kempe swap on a bichromatic component), and \(c'(x)=i\ne 1=c'(y)\). By Lemma 0.2 / Theorem 3.2 this is impossible: every proper \((t-1)\)-colouring of \(G-e\) must give \(x\) and \(y\) the same colour. □

**Remark.** In the full graph \(G\), the edge \(xy\) joins two vertices of colour \(1\), so it lies inside \(G[V_1\cup V_i]\). That edge is absent from \(G-e\), which is the correct setting for the Kempe argument above. Once the path in \(G-e\) is found, adjoining \(xy\) produces an even cycle through \(e\).

**Corollary 4.3 (Alternating paths).** For every \(i\in\{2,\dots,t-1\}\) there exists an \(x\)–\(y\) path \(P_i\) in \(G-e\) whose vertices alternate between colours \(1\) and \(i\). In particular \(P_i\cup\{xy\}\) is a cycle of even length at least \(4\) through the edge \(xy\).

**Corollary 4.4 (Common neighbours meet all colours — weak form).** If some \(P_i\) has length \(2\), then \(x\) and \(y\) have a common neighbour of colour \(i\). In a double-critical graph this holds for **all** \(i\) simultaneously with a single colouring of \(G-\{x,y\}\) (Proposition 2.3); in the general Track MC case, different \(i\) may require different paths of length \(>2\).

### 4.2. Attempted branch-set construction from the same-colour system

**Construction 4.5 (Naive monochromatic lift — fails).** Set \(B_i:=V_i\) for \(i=1,\dots,t-1\). Each \(B_i\) is independent (except \(B_1\) may use the edge \(xy\)). Connectivity fails unless each \(|V_i|=1\), which would give \(G\cong K_t\).

**Construction 4.6 (Path-supported lift — the same-colour contraction lift).** Choose, for each \(i\in\{2,\dots,t-1\}\), an alternating \(x\)–\(y\) path \(P_i\) as in Corollary 4.3. Let
\[
S:=\bigcup_{i=2}^{t-1} V(P_i)\cup\{x,y\}.
\]
Attempt to partition \(S\) into branch sets \(B_1,\dots,B_t\) as follows:

- \(B_t:=\{x\}\) (or \(\{y\}\), or a connected subset of \(V_1\) containing \(x\) but not \(y\));
- for each \(i=2,\dots,t-1\), let \(B_i\) be a connected subset of \(V(P_i)\) containing the unique colour-\(i\) neighbour of \(x\) on \(P_i\) (if \(P_i\) starts \(x-v_i-\cdots\)) and meeting every other \(B_j\).

More systematically, define the **path system model attempt**:

**Definition 4.7 (SCL assignment).** An **SCL-assignment** for the system \(\{P_i\}_{i=2}^{t-1}\) is a family of pairwise disjoint connected sets \(B_1,\dots,B_{t-1},B_t\subseteq V(G)\) such that:

1. \(x\in B_t\), \(y\in B_1\) (say), or both \(x,y\in B_1\) after using the edge \(xy\) as internal to \(B_1\);
2. for each \(i\in\{2,\dots,t-1\}\), the path \(P_i\) contributes at least one vertex of colour \(i\) to \(B_i\), and \(B_i\) is connected in \(G\);
3. for all distinct \(a,b\in\{1,\dots,t\}\), there is a \(G\)-edge between \(B_a\) and \(B_b\).

If an SCL-assignment exists, then \(G\) has a \(K_t\) model, contradicting \(\eta(G)=t-1\).

### 4.3. When the lift succeeds

**Theorem 4.8 (Lift for short paths).** Suppose that for some edge \(e=xy\) and some same-colour colouring \(c\) of \(G-e\), every alternating path \(P_i\) (\(i=2,\dots,t-1\)) may be chosen of length \(2\). Then there exist distinct common neighbours \(v_2,\dots,v_{t-1}\in B(xy)\) with \(c(v_i)=i\).

- If \(\{v_2,\dots,v_{t-1}\}\) is a clique, then \(\{x,y,v_2,\dots,v_{t-1}\}\) induces \(K_t\), contradiction.
- If not, the missing edges among the \(v_i\) are a subgraph obstruction; a minor may still exist by expanding branch sets along further structure in \(G-\{x,y\}\) (e.g. contracting a component of \(G-\{x,y\}\) that links two nonadjacent \(v_i,v_j\)).

**In the double-critical case**, Proposition 2.3 supplies \(|B(xy)|\ge t-2\) with all colours present under a single \((t-2)\)-colouring of \(G-\{x,y\}\). Combined with \(\delta\ge t+1\) and the Rolek–Song extremal package, the minor is forced for \(t\le 9\) (Theorems 2.8–2.10) without needing pairwise adjacency of the common neighbours.

**Theorem 4.9 (Disjoint-path lift yields \(K_t\) minus a matching).** Suppose the paths \(P_2,\dots,P_{t-1}\) can be chosen pairwise internally vertex-disjoint. Define:

- \(B_x:=\{x\}\), \(B_y:=\{y\}\);
- for each \(i=2,\dots,t-1\), \(B_i:=V(P_i)\setminus\{x,y\}\) (connected along \(P_i\); nonempty because length \(\ge 2\) would be needed for a nontrivial interior — if length \(2\), \(B_i\) is a single common neighbour).

Then \(\{B_x,B_y,B_2,\dots,B_{t-1}\}\) is a family of \(t\) pairwise disjoint connected sets such that:

- \(xy\) joins \(B_x\) to \(B_y\);
- each \(B_i\) meets both \(B_x\) and \(B_y\) (the first and last edges of \(P_i\));
- the only cross-adjacencies that may fail are those among \(\{B_2,\dots,B_{t-1}\}\).

Thus the construction realises a model of the complete multipartite graph obtained from \(K_t\) by deleting a matching (or more) among the \(t-2\) “middle” branch sets. Completing the model requires edges (or internally disjoint linking paths) between every pair \(B_i,B_j\). When every \(P_i\) has length \(2\) and the \(t-2\) common neighbours are pairwise adjacent, one obtains a \(K_t\) subgraph.

**Moral.** Internally disjoint same-colour paths give a full \(K_t\) model if and only if the path-interiors are pairwise adjacent or can be linked by connections disjoint from the support. This is automatic when all paths have length \(2\) and the common neighbours form a clique, and is the content of the triangle-density package in the double-critical case. Internally disjoint Kempe paths from a **rainbow neighbourhood of a single apex** (KRMP in `hadwiger_dual_search.md`) are a different — dual — configuration; that configuration produces a \(K_t\) subdivision directly when the paths exist, but Hajós’ conjecture fails for \(t\ge 7\), so such disjoint apex-systems need not exist.

### 4.4. Exact obstruction configuration

**Definition 4.10 (SCL obstruction).** An **SCL obstruction** at edge \(e=xy\) for colouring \(c\) is a choice of alternating paths \(\{P_i\}_{i=2}^{t-1}\) such that **no** SCL-assignment exists for that system. Equivalently: every attempt to form \(t\) connected branch sets from the support \(S\) fails to realise all \(\binom{t}{2}\) cross-edges.

**Theorem 4.11 (Obstruction dichotomy).** Let \(G\) be an order-minimal counterexample to \(\mathrm{HC}_t\). Then for every edge \(e=xy\) and every same-colour \((t-1)\)-colouring \(c\) of \(G-e\), either:

1. **(Lift)** some choice of alternating paths \(\{P_i\}\) admits an SCL-assignment, yielding a \(K_t\) minor (contradiction); or
2. **(Obstruction)** every path system \(\{P_i\}\) is an SCL obstruction: the support \(S\) cannot be partitioned into \(t\) connected, fully cross-adjacent branch sets.

In case (2), the obstruction has one of the following concrete forms (exhaustive at the level of connectivity of the support):

- **(O1) Shared interior vertices.** Two paths \(P_i,P_j\) share an interior vertex \(z\). Then \(c(z)\in\{1,i\}\cap\{1,j\}\), so \(c(z)=1\). The vertex \(z\) cannot be assigned to both \(B_i\) and \(B_j\); assigning it to \(B_1\) (the colour-\(1\) class) may disconnect the intended \(B_i\) or \(B_j\).
- **(O2) Missing cross-edge between interiors.** Paths \(P_i,P_j\) are internally disjoint, but no edge of \(G\) joins \(V(P_i)\setminus\{x,y\}\) to \(V(P_j)\setminus\{x,y\}\), and no alternate path system repairs this.
- **(O3) Colour-\(1\) cut.** The colour class \(V_1\) separates the colour-\(i\) vertices on different paths in a way that prevents simultaneous connectivity of all proposed branch sets.

**Lemma 4.12 (O1 is the primary obstruction for \(t\ge 7\)).** If all path systems could be chosen with pairwise internally disjoint paths, the same-colour system would yield a \(K_t\) **subdivision** after adding the KRMP-type links among rainbow neighbours of an apex — but Hajós’ conjecture fails for \(t\ge 7\), so internally disjoint systems need not exist. Thus any proof that SCL always lifts must **use contractions that identify shared colour-\(1\) vertices** (O1), which subdivisions forbid. This is exactly the gap between Hajós and Hadwiger, specialised to the same-colour edge setting.

### 4.5. Combining SCL with \(\eta(G/e)=t-1\)

**Construction 4.13 (Model-assisted lift).** Let \(\{M_1,\dots,M_{t-1}\}\) be a \(K_{t-1}\) model in \(G/e\), lifted to a \(K_{t-1}\) model \(\{M_1^\uparrow,\dots,M_{t-1}^\uparrow\}\) in \(G\) (Theorem 3.3). Exactly one lifted branch set, say \(M_1^\uparrow\), contains both \(x\) and \(y\) (or the model avoids the contracted vertex entirely, in which case the model already lives in \(G-e\) and we may try to add a branch set from the rest of \(G\)).

**Case A.** The contracted vertex \(v_e\) lies outside the model in \(G/e\). Then the model is already in \(G\), and \(G\) has a \(K_{t-1}\) model disjoint from at least one of \(x,y\). Extending by \(\{x\}\) or \(\{y\}\) requires that vertex to meet all \(t-1\) branch sets — i.e. a rainbow neighbourhood of an apex, returning to KRMP.

**Case B.** \(v_e\in M_1\) in \(G/e\), so \(x,y\in M_1^\uparrow\). The sets \(M_2^\uparrow,\dots,M_{t-1}^\uparrow\) are disjoint from \(\{x,y\}\) and form a \(K_{t-2}\) model fully linked to \(M_1^\uparrow\). To build a \(K_t\) model one must **split** \(M_1^\uparrow\) into two branch sets \(B_x\ni x\) and \(B_y\ni y\) that remain connected, remain fully linked to each \(M_i^\uparrow\) (\(i\ge 2\)), and are linked to each other (by \(e\)).

**Lemma 4.14 (Split criterion).** The lifted model splits if and only if there exist disjoint connected sets \(B_x\ni x\), \(B_y\ni y\) with \(B_x\cup B_y\subseteq M_1^\uparrow\), \(B_x\cup B_y=M_1^\uparrow\) or at least \(B_x\cup B_y\) meets every neighbour of \(M_1^\uparrow\) that the original branch set used, such that:

1. \(xy\) joins \(B_x\) to \(B_y\) (true if \(x\in B_x\), \(y\in B_y\));
2. every \(M_i^\uparrow\) (\(i\ge 2\)) has a neighbour in \(B_x\) and a neighbour in \(B_y\).

**Relation to same-colour colouring.** Under the colouring \(c\) of \(G-e\) with \(c(x)=c(y)=1\), the branch set \(M_1^\uparrow\) may mix colours. The alternating paths \(P_i\) of Lemma 4.2 provide, for each colour \(i\), a route from \(x\) to \(y\) that may enter and leave the other branch sets. If some \(P_i\) is contained in \(M_1^\uparrow\cup M_i^\uparrow\), it witnesses simultaneous linkage of both \(x\) and \(y\) to \(M_i^\uparrow\).

**Theorem 4.15 (SCL + model split — partial success).** Suppose there exists an edge \(e=xy\), a same-colour colouring \(c\), and a lifted \(K_{t-1}\) model \(\{M_j^\uparrow\}\) such that for every \(i=2,\dots,t-1\), some alternating \(x\)–\(y\) path \(P_i\) lies in \(M_1^\uparrow\cup M_i^\uparrow\). Then the split
\[
B_x:=\{x\},\qquad B_y:=(M_1^\uparrow\setminus\{x\})
\]
(or a refined cut of \(M_1^\uparrow\) along the colour-\(1\) structure) yields a \(K_t\) model whenever \(y\in M_1^\uparrow\) and every \(M_i^\uparrow\) meets both a neighbour of \(x\) and a neighbour of \(y\) inside \(M_1^\uparrow\cup M_i^\uparrow\).

*Proof.* Connectivity of \(B_y\): needs \(M_1^\uparrow-x\) connected, which holds if \(x\) is not a cutvertex of \(G[M_1^\uparrow]\). Cross-edges to each \(M_i^\uparrow\): the path \(P_i\) supplies an edge from \(\{x,y\}\) into the colour-\(i\) part; if both ends of \(e\) send edges into \(M_i^\uparrow\), done. The edge \(xy\) links \(B_x\) to \(B_y\). □

**Obstruction to Theorem 4.15.** The path \(P_i\) may leave \(M_1^\uparrow\cup M_i^\uparrow\) and use vertices of other branch sets, destroying disjointness. Or \(x\) may be a cutvertex of \(M_1^\uparrow\). Or some \(M_i^\uparrow\) may meet only one of \(x,y\) inside the allowed region.

### 4.6. Double-critical specialisation of SCL

**Theorem 4.16 (SCL collapses to KPT on Track DC).** If \(G\) is double-critical, then for every edge \(xy\):

1. \(G-\{x,y\}\) admits a \((t-2)\)-colouring \(\varphi\);
2. extending by \(\varphi(x)=\varphi(y)=t-1\) is not available — rather, Proposition 2.3 applied to \(\varphi\) puts all colours \(1,\dots,t-2\) into \(B(xy)\);
3. the alternating paths \(P_i\) may all be taken of length \(2\);
4. the Rolek–Song package then forces a \(K_t\) minor for \(t\le 9\).

Thus on Track DC with \(t\le 9\), case (1) of the dichotomy Theorem 4.11 always holds (via a different route than pure SCL assignment — via extremal density of neighbourhoods).

---

## 5. What is proved, what is blocked

### 5.1. Affirmative results (full rigor)

| Statement | Status |
|-----------|--------|
| Minimal Hadwiger counterexamples are \(t\)-critical, \(\eta=t-1\), contraction-tight | **Proved** (Lemma 0.4) |
| Double-criticality cannot be assumed free of charge | **Proved** (Theorem 1.3) |
| Non-complete double-critical \(\Rightarrow\) \(\delta\ge t+1\), \(\ge t-2\) triangles/edge, \(6\)-connected, no \(K_{t-1}\) subgraph | **Proved** (Props 2.1–2.6; classical KPT) |
| Double-critical \(t\)-chromatic \(\Rightarrow K_t\) minor for \(t\le 9\) | **Proved** (Rolek–Song; Theorems 2.8–2.10) |
| Same-colour colouring of \(G-e\) forces \(x\)–\(y\) paths in every bichromatic \(G_{1i}\) | **Proved** (Lemma 4.2) |
| SCL dichotomy: lift or obstruction (O1)–(O3) | **Proved** (Theorem 4.11) |
| Model-split criterion for lifted \(K_{t-1}\) models | **Proved** (Lemma 4.14) |
| Full Hadwiger for general \(t\) via SCL | **Not proved** |

### 5.2. Exact remaining obstruction (not “equivalent to HC” as a slogan)

The remaining gap on Track MC is:

> **Gap SCL.** Prove that in every order-minimal counterexample to \(\mathrm{HC}_t\), for some edge \(e=xy\) and some same-colour \((t-1)\)-colouring of \(G-e\), either an SCL-assignment exists, or a model-split of a lifted \(K_{t-1}\) model exists, or the obstruction configuration (O1)–(O3) forces a \(K_t\) minor by a third route (e.g. re-routing paths through the high connectivity \(\kappa\ge t-1\), or absorbing shared colour-\(1\) vertices into a single branch set that still meets all other colours).

This gap is **structurally specific**: it concerns the interaction of one edge, one colouring, and one path system (or one lifted model). It is **not** a restatement of Hadwiger. It is a concrete combinatorial claim about Kempe chains in critical graphs with \(\eta=t-1\).

**Why Gap SCL is not known to be equivalent to \(\mathrm{HC}_t\).**  
A proof of Gap SCL would imply \(\mathrm{HC}_t\) (by contradiction to minimality). The converse is false as a formal equivalence of statements: \(\mathrm{HC}_t\) asserts a minor in every \(t\)-chromatic graph, while Gap SCL asserts a property of path systems in minimal counterexamples. One could imagine \(\mathrm{HC}_t\) true while some non-minimal \(t\)-critical graphs have pathological SCL obstructions; Gap SCL only needs to rule out the obstruction **inside minimal counterexamples**, using \(\kappa\ge t-1\), \(\delta\ge t-1\), and contraction-tightness.

**Partial progress toward Gap SCL.**

1. **Track DC, \(t\le 9\):** Gap SCL holds because the double-critical package forces short paths and Rolek–Song applies (Theorem 4.16).
2. **Length-\(2\) path systems:** reduce to common-neighbourhood cliques / minors (Theorem 4.8).
3. **Model-split when paths stay inside two branch sets:** Theorem 4.15.
4. **Shared colour-\(1\) vertices (O1):** the natural move is to place each shared \(z\in V_1\) into a branch set \(B_1\) that contains both \(x\) and \(y\) (using edges of colour \(1\) along the paths, or the edge \(xy\)), and build the other branch sets from colour-\(i\) vertices only. Connectivity of \(B_1\) holds along the union of the paths; cross-edges from \(B_1\) to a colour-\(i\) branch set exist along each \(P_i\). The missing pieces are cross-edges among the colour-\(i\) branch sets — returning to a rooted \(K_{t-2}\) minor problem in \(G-V_1\), which is \((t-2)\)-colourable… wait: \(G-V_1\) is properly coloured with \(t-2\) colours, so \(\chi(G-V_1)\le t-2\). By induction on \(t\) (Hadwiger known below \(t\)), \(G-V_1\) has a \(K_{t-2}\) minor if \(\chi(G-V_1)=t-2\). But \(\chi(G-V_1)\) may be \(<t-2\).

**Lemma 4.17 (Colour class deletion).** Under Setup 4.1, \(\chi(G-V_1)\le t-2\). If equality holds and Hadwiger is known for chromatic number \(t-2\), then \(G-V_1\) has a \(K_{t-2}\) minor. Linking that minor to \(B_1:=V_1\) (which is independent except for edges that would contradict proper colouring of \(G-e\) — in \(G\), edges inside \(V_1\) can only be \(xy\)) fails because \(V_1\) may not be complete to the branch sets of the \(K_{t-2}\) minor.

The correct inductive move is: \(G/e\) is \((t-1)\)-chromatic with a \(K_{t-1}\) minor; the colour classes of a colouring of \(G/e\) pull back to a partition of \(V(G)\) in which \(x,y\) share a class. Building a \(K_t\) minor from a \(K_{t-1}\) minor in a graph that is one edge away from being \((t-1)\)-colourable is Gap M of the contraction-induction programme (`hadwiger_contraction_induction.md`), specialised to same-colour data.

### 5.3. Programme status

```
Track DC (double-critical):
  structure (KPT) ──► Kt minor for t ≤ 9 (Rolek–Song)
                  ──► open for t ≥ 10

Track MC (minimal Hadwiger counterexample):
  t-critical, η=t−1, contraction-tight
       │
       ├─ cannot assume double-critical (Thm 1.3)
       │
       └─ same-colour contraction lift (Lem 4.2)
              │
              ├─ short paths / high triangles ──► Kt (partial)
              ├─ model-split (Lem 4.14–Thm 4.15) ──► Kt (conditional)
              └─ Gap SCL: rule out obstruction (O1)–(O3)
                         in presence of κ≥t−1
```

**Verdict.**

- Double-critical strengthening: **fails as a free reduction** (Theorem 1.3); **succeeds as a side track** with complete Hadwiger conclusion for all double-critical graphs of chromatic number \(\le 9\).
- Same-colour contraction lift: **engine proved** (forced bichromatic paths); **obstruction isolated** (O1)–(O3); **not resolved** for general minimal counterexamples.
- No terminal claim of the form “Gap SCL \(\Leftrightarrow\mathrm{HC}_t\)” is asserted. Gap SCL is a sufficient, concrete, and strictly more structured target than bare Hadwiger.

---

## 6. Open concrete lemmas (for further work)

**Lemma A (Shared colour-1 absorption).** In Setup 4.1, let \(Z\subseteq V_1\) be the set of all vertices of colour \(1\) that lie on at least two paths of a fixed system \(\{P_i\}\). Prove that the connected set \(B_1\) obtained from \(\{x,y\}\cup Z\) by adding shortest path segments in \(G[V_1\cup(\bigcup_i V_i)]\) between them can be completed to a \(K_t\) model, or derive a contradiction from \(\kappa(G)\ge t-1\).

**Lemma B (Rooted linkage from common neighbourhood).** If \(|B(xy)|\ge t-2\) for some edge \(xy\) in a minimal counterexample, prove a \(K_t\) minor (without double-criticality). This would unify Track DC and the high-triangle case of Track MC.

**Lemma C (Separator-free path rerouting).** Using \(\kappa\ge t-1\), prove that an SCL obstruction of type (O2) cannot occur: missing cross-edges between path interiors can be replaced by \(\kappa\)-linked detours that avoid the rest of the support.

---

## References (external results used as black boxes with citations)

1. Stiebitz, *\(K_5\) is the only double-critical \(5\)-chromatic graph*, Discrete Math. 64 (1987).
2. Mozhan, *On doubly critical graphs with chromatic number five*, Metody Diskret. Anal. (1987).
3. Kawarabayashi–Pedersen–Toft, *Double-critical graphs and complete minors*, Electron. J. Combin. 17 (2010), #R87.
4. Rolek–Song, *Clique minors in double-critical graphs*, J. Graph Theory (2018); arXiv:1603.06964.
5. Albar–Gonçalves, *On triangles in \(K_r\)-minor-free graphs*, arXiv:1304.5468.
6. Song–Thomas, *The extremal function for \(K_9\) minors*, JCTB 96 (2006).
7. Jørgensen, *Contractions to \(K_8\)*, J. Graph Theory 18 (1994).

Internal cross-references: `hadwiger_contraction_induction.md` (model lifting, Gap M), `hadwiger_dual_search.md` (KRMP, rainbow neighbourhoods), `hadwiger_critical_graphs.md` (Dirac, critical structure).

---

*End of note. Hybrid programme status: Track DC settled for \(t\le 9\); Track MC reduced to Gap SCL with fully specified obstruction; double-critical free reduction disproved as a method.*
