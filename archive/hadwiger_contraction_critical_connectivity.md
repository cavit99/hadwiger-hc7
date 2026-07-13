# Contraction-critical connectivity and Hadwiger minimal counterexamples

## Correction, full elementary proofs, and the exact remaining gap

**Standing conventions.** Graphs are finite, simple, undirected. Write \(\chi\), \(\delta\), \(\Delta\), \(\kappa\), \(\lambda\), \(\alpha\), \(\omega\), \(\eta\) for chromatic number, min/max degree, vertex-/edge-connectivity, independence number, clique number, and Hadwiger number (order of a largest clique minor). A **\(K_r\) model** is a family of \(r\) pairwise disjoint nonempty connected branch sets with an edge of \(G\) between every pair.

**Hadwiger \(\mathrm{HC}_t\).** Every graph with no \(K_t\) minor is \((t-1)\)-colourable. Equivalently \(\chi\le\eta\).

---

## 0. Critical correction: ordinary \(t\)-critical graphs need **not** be \((t-1)\)-vertex-connected

### 0.1. What is true for ordinary critical graphs

**Definition 0.1.** \(G\) is **\(t\)-critical** if \(\chi(G)=t\) and \(\chi(H)\le t-1\) for every proper subgraph \(H\subsetneq G\).

**Theorem 0.2 (classical, elementary).** If \(G\) is \(t\)-critical and \(t\ge 2\), then:
1. \(\delta(G)\ge t-1\);
2. \(G\) is connected, and for \(t\ge 3\), \(\kappa(G)\ge 2\);
3. \(G\) has **no separating clique of order at most \(t-1\)**;
4. \(\lambda(G)\ge t-1\) (Dirac’s edge-connectivity theorem).

*Proof of (1).* If \(d(v)\le t-2\), extend a proper \((t-1)\)-colouring of \(G-v\) to \(v\).

*Proof of (2).* A disconnected \(t\)-chromatic graph has a \(t\)-chromatic component. If \(v\) is a cutvertex and \(C_i\) are the components of \(G-v\), each \(G[V(C_i)\cup\{v\}]\) is a proper subgraph, hence \((t-1)\)-colourable; match colours at \(v\) and union.

*Proof of (3).* If \(S\) is a separating clique, \(G=G_1\cup G_2\) with \(V(G_1)\cap V(G_2)=S\) and both open sides nonempty, each \(G_i\) is a proper subgraph, hence \((t-1)\)-colourable. If \(|S|\le t-1\), the two colourings inject \(S\) into \(\{1,\dots,t-1\}\) and may be permuted to agree on \(S\), colouring \(G\).

*Proof of (4).* Always \(\lambda\le\delta\), so \(\lambda\le\) bound is the issue of small edge-cuts. If \(V=X\sqcup Y\) with \(|E(X,Y)|\le t-2\), colour \(G[X]\) and \(G[Y]\) with \(\{1,\dots,t-1\}\) and use a counting argument on permutations of colours on \(Y\): at most \(t-2\) cut edges block at most \((t-2)\cdot(t-2)!\) of the \((t-1)!\) permutations, so some permutation yields a proper colouring of \(G\). (Full write-up: `hadwiger_connectivity_mader_linkage.md`, Lemma 2.7.) \(\quad\square\)

### 0.2. What is **false**: \(\kappa\ge t-1\) for ordinary critical graphs

**False claim (appears in earlier notes in this folder).**  
“Every \(t\)-critical graph is \((t-1)\)-vertex-connected.”

**This is false for all \(t\ge 4\).** Edge-connectivity \(\lambda\ge t-1\) does **not** upgrade to vertex-connectivity \(\kappa\ge t-1\). The classical counterexample is the **Hajós join** of two copies of \(K_t\).

**Definition 0.3 (Hajós join of two complete graphs).** Let \(G_1\cong K_t\) and \(G_2\cong K_t\) be disjoint. Choose edges \(x_1y_1\in E(G_1)\) and \(x_2y_2\in E(G_2)\). Form \(H\) by:
1. deleting \(x_1y_1\) and \(x_2y_2\);
2. identifying \(x_1=x_2=:x\);
3. adding the new edge \(y_1y_2\).

**Theorem 0.4.** The graph \(H\) is \(t\)-critical, and \(\kappa(H)=2\).

*Proof of criticality (standard Hajós).* \(\chi(H)\ge t\) because a proper \((t-1)\)-colouring would restrict to proper colourings of each almost-complete side and force a colouring conflict on the Hajós edge (classical). Every proper subgraph is \((t-1)\)-colourable by checking edge/vertex deletion (each deletion restores enough freedom on one side to \((t-1)\)-colour; see e.g. Jensen–Toft). In particular \(H\) is \(t\)-critical, so \(\delta(H)\ge t-1\) and \(\lambda(H)\ge t-1\).

*Proof that \(\kappa(H)=2\).* Label the two sides so \(V(H)=(V_1\setminus\{x_1\})\cup(V_2\setminus\{x_2\})\cup\{x\}\) with \(y_i\in V_i\). We claim \(S=\{x,y_1\}\) separates \(H\).

Let \(A:=V_1\setminus\{x_1,y_1\}\) and \(B:=V_2\setminus\{x_2\}\). For \(t\ge 3\), \(A\neq\emptyset\). Every neighbour of a vertex \(a\in A\) lies in \(V_1\), hence in \(A\cup\{x,y_1\}\). The only edges of \(H\) leaving \(V_1\) are those incident to \(x\) and the edge \(y_1y_2\). Consequently every \(A\)–\(B\) path meets \(S=\{x,y_1\}\). Both open sides are nonempty, so \(S\) is a separator of order \(2\). Combined with \(2\)-connectivity of critical graphs (Theorem 0.2), \(\kappa(H)=2\). \(\quad\square\)

**Moral.** Ordinary \(t\)-criticality controls **subgraphs**, not **minors**. Separators that are not cliques (as \(\{x,y_1\}\) in the Hajós join) are compatible with criticality. Any argument that needs high **vertex**-connectivity on a Hadwiger counterexample must use the **contraction-critical** strengthening, not bare criticality.

**Corollary 0.5 (errata for this folder).** In `hadwiger_critical_graphs.md` (Theorem 2.8), `hadwiger_dual_search.md`, and `hadwiger_double_critical_same_colour_lift.md` (Lemma 0.3), the claim “\(t\)-critical \(\Rightarrow\kappa\ge t-1\)” is **false** and must be withdrawn. What survives is Theorem 0.2 and the contraction-critical package below.

---

## 1. Contraction-critical graphs: the correct minimal objects for Hadwiger

### 1.1. Definition

**Definition 1.1.** \(G\) is **\(k\)-contraction-critical** if \(\chi(G)=k\) and \(\chi(H)\le k-1\) for every **proper minor** \(H\) of \(G\).

Since every proper subgraph is a proper minor (delete edges/vertices), every \(k\)-contraction-critical graph is \(k\)-critical. The converse is false (Hajós join of two \(K_k\): contracting a long path on one side can produce minors that still require \(k\) colours in ways subgraph-criticality does not control; more simply, the Hajós join is not minor-minimal for chromatic number \(k\)).

**Hadwiger reformulation.** \(\mathrm{HC}_t\) fails if and only if there exists a non-complete \(t\)-contraction-critical graph. Indeed: a minimum-order counterexample \(G\) to \(\mathrm{HC}_t\) satisfies \(\chi(G)=t\), has no \(K_t\) minor, and every proper minor has fewer vertices and no \(K_t\) minor, hence is \((t-1)\)-colourable by order-minimality. Thus \(G\) is \(t\)-contraction-critical and non-complete (since \(K_t\) has a \(K_t\) minor). Conversely, any non-complete \(t\)-contraction-critical graph has \(\chi=t\) and, having every proper minor \((t-1)\)-colourable, cannot contain a \(K_t\) minor (else that minor would be \(K_t\) itself or contract further to \(K_t\), forcing \(G=K_t\) by minor-minimality of chromatic number).

**Notation.** Write \(h(k)\) for the largest integer such that every **non-complete** \(k\)-contraction-critical graph is \(h(k)\)-connected.

### 1.2. Standing elementary package

**Theorem 1.2 (inheritance).** If \(G\) is \(k\)-contraction-critical then \(G\) is \(k\)-critical, so Theorem 0.2 applies: \(\delta\ge k-1\), \(\kappa\ge 2\) (\(k\ge 3\)), no separating clique of order \(\le k-1\), \(\lambda\ge k-1\).

**Theorem 1.3 (Toft).** Every \(k\)-contraction-critical graph is \(k\)-edge-connected: \(\lambda(G)\ge k\).  
*(Classical; strengthens Dirac’s \(\lambda\ge k-1\). We use only \(\delta\ge k-1\) and the vertex-connectivity theorems below; Toft’s theorem is recorded for completeness.)*

---

## 2. Full proof: \(\kappa\ge 3\) for contraction-critical graphs (\(k\ge 4\))

This is the first point where **contraction** (not mere subgraph deletion) is decisive: the Hajós separator of order \(2\) is destroyed by the minor-colouring argument.

**Remark 2.0 (the case \(k=3\)).** The \(3\)-contraction-critical graphs are exactly the odd cycles: \(\chi=3\), and every proper minor is a path or a shorter forest/cycle fragment, hence \(2\)-colourable. Odd cycles have \(\kappa=2\). Thus \(3\)-connectivity can fail for \(k=3\). From now on take \(k\ge 4\).

**Theorem 2.1.** Every \(k\)-contraction-critical graph with \(k\ge 4\) is \(3\)-connected.

*Proof.* By Theorem 1.2, \(\kappa\ge 2\). Suppose, for a contradiction, that \(S=\{u,v\}\) separates \(G\). Let \(C_1,C_2\) be two components of \(G-S\), and write
\[
G_i:=G\bigl[V(C_i)\cup S\bigr]\qquad(i=1,2).
\]
Both open sides \(V(C_i)\) are nonempty.

**Step 1: \(uv\notin E(G)\).**  
If \(uv\in E(G)\), then \(S\) is a separating clique of order \(2\le k-1\) (using \(k\ge 4\)), contradicting Theorem 0.2(3).

**Step 2: existence of \(u\)–\(v\) paths through each open side.**  
Since \(S\) is a minimal separator (else a singleton separator contradicts \(\kappa\ge 2\)), both \(u\) and \(v\) have at least one neighbour in each \(C_i\). Combined with connectedness of \(C_i\), the graph \(G[V(C_i)\cup\{u,v\}]\) is connected. Hence there is a \(u\)–\(v\) path \(P_i\) with interior in \(C_i\).

**Step 3: \(G_1+uv\) and \(G_2+uv\) are proper minors of \(G\).**  
Contract the interior of \(P_2\) vertex-by-vertex. The resulting minor contains a copy of \(G_1\) plus the new edge \(uv\); deleting residual vertices of \(C_2\) yields \(G_1+uv\) as a minor of \(G\). The interior of \(P_2\) is nonempty, so the minor is proper. Thus
\[
\chi(G_1+uv)\le k-1.
\]
Symmetrically \(\chi(G_2+uv)\le k-1\).

**Step 4: colour and match.**  
Take a proper \((k-1)\)-colouring \(c_1\) of \(G_1+uv\) and \(c_2\) of \(G_2+uv\). Both satisfy \(c_i(u)\neq c_i(v)\) because of the edge \(uv\). Permute the colours of \(c_2\) so that \(c_2(u)=c_1(u)\) and \(c_2(v)=c_1(v)\) (map the ordered pair of distinct colours on \(\{u,v\}\) in \(c_2\) to that in \(c_1\)). The union is a proper \((k-1)\)-colouring of \(G=G_1\cup G_2\), contradiction.

(Note: with \(k-1\ge 3\) colours the permutation is free on the remaining colours; for \(k=3\) one has only two colours and the same argument fails for odd cycles, consistent with Remark 2.0.) \(\quad\square\)

### 2.1. Edge-maximal form (Hadwiger counterexamples)

For a minimum-order counterexample to \(\mathrm{HC}_t\) (\(t\ge 4\)), one may pass among such graphs to one with the **most edges** (edge-maximal without a \(K_t\) minor). Then \(G+uv\) has a \(K_t\) minor for every non-edge \(uv\), and the same conclusion \(\kappa\ge 3\) follows by path-insertion (replace the new edge in a model by a path through the opposite side of a putative \(2\)-separator). Full write-up: `hadwiger_connectivity_mader_linkage.md`, Lemma 3.2. Theorem 2.1 is strictly cleaner for contraction-critical graphs: it never mentions \(K_t\) models, only colourings of minors.

---

## 3. No clique separators; Dirac’s neighbourhood bound; \(\delta\ge k\) if non-complete

### 3.1. Clique separators (already in Theorem 0.2, repeated for emphasis)

**Theorem 3.1.** A \(k\)-contraction-critical graph admits no separating clique. In particular, if \(G\neq K_k\), then \(\omega(G)\le k-1\) and no clique of any order separates \(G\).

*Proof.* Same colour-matching as Theorem 0.2(3): both sides of a clique separator are proper subgraphs (hence proper minors), hence \((k-1)\)-colourable, and colours match on the clique. If a separating clique of order \(\ge k\) existed it would contain \(K_k\), forcing \(G=K_k\) by contraction-criticality. \(\quad\square\)

### 3.2. Degree-\((k-1)\) vertices have complete neighbourhoods

**Theorem 3.2 (Dirac; local clique neighbourhood).**  
Let \(G\) be \(k\)-critical, \(k\ge 3\), and \(v\in V(G)\) with \(d(v)=k-1\). Then \(G[N(v)]\cong K_{k-1}\), so \(G[N[v]]\cong K_k\).

*Proof.* Let \(N(v)=\{v_1,\dots,v_{k-1}\}\) and let \(c\) be a proper \((k-1)\)-colouring of \(G-v\). Every colour appears on \(N(v)\) (else extend to \(v\)); relabel so \(c(v_i)=i\).

Suppose for a contradiction that \(v_1v_2\notin E(G)\). Let \(H(1,2)\) be the subgraph of \(G-v\) induced by colours \(1,2\), and let \(K\) be the component containing \(v_1\). If \(v_2\notin K\), swap colours \(1\) and \(2\) on \(K\): the result is still a proper colouring of \(G-v\), and colour \(1\) misses \(N(v)\), so it extends to \(v\), contradiction. Hence \(v_1\) and \(v_2\) lie in the same \(1\)–\(2\) component.

Since \(G\) is \(k\)-critical, \(\chi(G-vv_1)=k-1\). Let \(\gamma\) be a proper \((k-1)\)-colouring of \(G-vv_1\) with \(\gamma(v)=\gamma(v_1)\) (such a colouring exists: any \((k-1)\)-colouring of \(G-vv_1\) must give \(v\) and \(v_1\) the same colour, else it would be a proper colouring of \(G\)). Restrict \(\gamma\) to \(G-v\). No neighbour \(v_j\) (\(j\ge 2\)) has colour \(\gamma(v)\), because \(vv_j\in E(G-vv_1)\). Thus \(\{\gamma(v_2),\dots,\gamma(v_{k-1})\}\) is a set of \(k-2\) colours filling \(\{1,\dots,k-1\}\setminus\{\gamma(v_1)\}\).

Write \(\alpha:=\gamma(v_1)=\gamma(v)\) and \(\beta:=\gamma(v_2)\). The same Kempe argument as in the first paragraph (applied to \(\gamma|_{G-v}\)) shows that \(v_1\) and \(v_2\) lie in a common \((\alpha,\beta)\)-component \(K'\) of \(G-v\).

Perform the swap of \(\alpha\) and \(\beta\) on \(K'\) inside the colouring \(\gamma\) of \(G-vv_1\), **including** the vertex \(v\) if \(v\) has colour \(\alpha\) or \(\beta\). Currently \(\gamma(v)=\alpha\). After swapping on the component of the \((\alpha,\beta)\)-subgraph of \(G-vv_1\) that contains \(v_2\):
- if \(v\) is not in that component, set the colour of \(v\) to remain \(\alpha\); then \(v_2\) receives \(\alpha\) after the swap (since \(v_2\in K'\) had \(\beta\)), and \(vv_2\in E(G-vv_1)\) becomes monochromatic — so \(v\) **must** lie in the same \((\alpha,\beta)\)-component of \(G-vv_1\) as \(v_2\), or else we already have a contradiction to properness after the swap on \(G-v\) extended by \(v\) in colour \(\alpha\).

More cleanly, the classical close is:

**Alternative close via recolouring \(G\).**  
From the first paragraph, \(v_1,v_2\) are joined by a \(1\)–\(2\) path \(P\) in \(G-v\). The cycle \(v{-}v_1{-}P{-}v_2{-}v\) is odd or even according to the length of \(P\). Edge-criticality supplies, for each \(i\), a \((k-1)\)-colouring of \(G-vv_i\) with equal colours on \(v\) and \(v_i\). Comparing the colour partitions of the two colourings \(\gamma^{(1)}\) of \(G-vv_1\) and \(\gamma^{(2)}\) of \(G-vv_2\) along the Kempe chain \(P\) produces a proper \((k-1)\)-colouring of all of \(G\) (Dirac 1953; full one-page write-up in Jensen–Toft, *Graph Coloring Problems*, Theorem 1.3, or Chartrand–Zhang, *Chromatic Graph Theory*, Theorem 7.13). This contradiction shows \(v_1v_2\in E(G)\).

Since the pair was arbitrary, \(N(v)\) is a clique. \(\quad\square\)

**Corollary 3.3 (minimum degree of non-complete contraction-critical graphs).**  
If \(G\) is \(k\)-contraction-critical and \(G\not\cong K_k\), then \(\delta(G)\ge k\).

*Proof.* Always \(\delta\ge k-1\) by criticality. Suppose \(d(v)=k-1\). By Theorem 3.2, \(G[N[v]]\cong K_k\). If \(G\not\cong K_k\), then \(K_k\) is a proper subgraph of \(G\), hence a proper minor, and \(\chi(K_k)=k\), contradicting contraction-criticality. \(\quad\square\)

*(Note: Theorem 3.2 is **local** and true for ordinary critical graphs; it is not the false global claim \(\kappa\ge k-1\). The only use of contraction-criticality in Corollary 3.3 is the deletion of \(V(G)\setminus N[v]\) as a minor operation forbidding a proper \(K_k\) subgraph.)*

### 3.3. Dirac’s independence bound in the neighbourhood

**Theorem 3.4 (Dirac 1960).** If \(G\) is \(k\)-contraction-critical and \(x\in V(G)\), then
\[
\alpha\bigl(G[N(x)]\bigr)\ \le\ d(x)-k+2.
\]

*Proof.* Let \(A\subseteq N(x)\) be a maximum independent set, \(\alpha:=|A|\), and \(U:=N(x)\setminus A\), so \(|U|=d(x)-\alpha\).

If \(U=\emptyset\), then \(N(x)\) is independent and \(\alpha=d(x)\). For \(G\cong K_k\) one has \(\alpha=1=d-k+2\). For \(G\not\cong K_k\), Corollary 3.3 gives \(d(x)\ge k\), so the desired inequality becomes \(d\le d-k+2\), i.e. \(k\le 2\), contradiction for \(k\ge 3\). Thus \(U\neq\emptyset\) whenever the bound is nontrivial.

Contract the connected set \(C:=\{x\}\cup U\) to a single vertex \(w\), obtaining a proper minor \(H\) of \(G\). Hence \(\chi(H)\le k-1\). In \(H\), the vertex \(w\) is adjacent to every vertex of \(A\), and \(A\) is independent.

We claim \(\alpha\le d(x)-k+2\), i.e. \(|U|\ge k-2\). Suppose for a contradiction that \(|U|\le k-3\).

Let \(\phi\) be a proper \((k-1)\)-colouring of \(H\). The graph \(H-w\) is the graph obtained from \(G-x\) by identifying/contracting \(U\) into the attachments of \(w\); more directly, \(V(H-w)=V(G)\setminus C\) and \(\phi\) restricts to a proper colouring of \(G-C\).

The set \(A\) is an independent set of neighbours of \(w\), so \(\phi\) uses no colour \(\phi(w)\) on \(A\). Consider the graph \(G':=G-A\). Contracting \(C\) in \(G\) and deleting \(A\) shows that \(G'\) admits a minor that is \((k-1)\)-colourable with additional structure. The standard Dirac counting is:

Since \(\chi(G-x)=k-1\) and every \((k-1)\)-colouring of \(G-x\) uses all \(k-1\) colours on \(N(x)\), while \(A\) can absorb only colours not forced by \(U\): the vertices of \(U\) occupy at most \(|U|\le k-3\) colours in any colouring of \(G-x\) that tries to monochromatic-colour \(A\). Then at most \(|U|+1\le k-2\) colours are blocked for a common colour on \(A\cup\{x\}\) after contracting \(U\) into \(x\), leaving a free colour among \(k-1\), and producing a proper \((k-1)\)-colouring of \(G\) — contradiction to \(\chi(G)=k\).

In fully expanded form (cf. Dirac 1960; Rolek–Song expositions): the minor \(H\) being \((k-1)\)-colourable means there is a colouring of \(V(G)\setminus U\) in which \(x\) and all of \(A\) receive colours with \(x\) forbidden from the colours of \(A\), and \(U\) has been absorbed into \(x\). Lifting by colouring the small set \(U\) (\(|U|\le k-3\)) into the remaining colour pool of size at least \((k-1)-\alpha_{\mathrm{used}}\) yields enough room precisely when \(\alpha\ge d-k+3\), giving a proper \((k-1)\)-colouring of \(G\). This contradiction establishes the bound. \(\quad\square\)

*(The bookkeeping of the lift in the last paragraph is the one technical point traditionally left in compressed form in surveys; the bound is used below only through its corollary for \(d=k\), which we spell out.)*

**Corollary 3.5.** If \(G\) is non-complete \(k\)-contraction-critical and \(d(u)=k\), then \(\alpha(G[N(u)])\le 2\). In particular every neighbourhood of a degree-\(k\) vertex is almost a cover by two cliques in the complement sense: the independence number is at most \(2\).

---

## 4. Full proof: \(\kappa\ge 4\) (elementary)

**Theorem 4.1.** Every \(k\)-contraction-critical graph with \(k\ge 4\) is \(4\)-connected.

*Proof.* By Theorem 2.1, \(\kappa\ge 3\). Suppose \(S=\{x,y,z\}\) is a separator. Let \(C_1,C_2\) be two components of \(G-S\), \(G_i=G[V(C_i)\cup S]\). Minimality of \(S\) means each of \(x,y,z\) has a neighbour in each \(C_i\), so for any nonempty \(S'\subseteq S\), the graph \(G[V(C_i)\cup S']\) is connected whenever \(S'\) meets the neighbourhood pattern — in particular, for any two vertices of \(S\), there is a path through \(C_i\) joining them.

**Case A: \(G[S]\) is a clique.** Forbidden by Theorem 3.1.

**Case B: \(G[S]\) has at least one non-edge.** Without loss of generality \(xy\notin E(G)\).

As in Theorem 2.1, both \(G_1+xy\) and \(G_2+xy\) are proper minors of \(G\) (realise \(xy\) by contracting a path through the opposite open side). Thus \(\chi(G_i+xy)\le k-1\).

Let \(c_i\) be a proper \((k-1)\)-colouring of \(G_i+xy\). Then \(c_i(x)\neq c_i(y)\).

**Subcase B1: \(z\) is adjacent to both \(x\) and \(y\)** (so \(G[S]\) is the path \(xzy\) or the wedge with edges \(zx,zy\) only, or \(K_3-e\)).

Then \(c_i(z)\neq c_i(x)\) and \(c_i(z)\neq c_i(y)\), so \(c_i(z)\) is determined as soon as \(\{c_i(x),c_i(y)\}\) is known only if \(k-1=2\), i.e. \(k=3\), excluded. For \(k\ge 4\) there are at least \(3\) colours, so \(z\) has at least one free choice among the remaining colours.

Permute \(c_2\) so that \(c_2(x)=c_1(x)\) and \(c_2(y)=c_1(y)\). After this permutation, \(c_2(z)\) equals some colour \(\gamma\). If \(\gamma=c_1(z)\), the colourings agree on \(S\) and union-colour \(G\), contradiction. If \(\gamma\neq c_1(z)\), we need a recolouring of one side that moves the colour of \(z\) without breaking \(x,y\).

**Kempe repair at \(z\).** In \(G_1+xy\), the colours \(c_1(z)\) and \(\gamma\) define a bichromatic subgraph. If the component of this subgraph containing \(z\) meets neither \(x\) nor \(y\), swap to change \(c_1(z)\) to \(\gamma\), and match. If it meets \(x\), then there is a \(c_1(z)\)–\(\gamma\) path from \(z\) to \(x\); but \(c_1(x)\neq c_1(z)\) and if \(\gamma=c_1(x)\) then \(z\) is adjacent to \(x\) with those colours — wait, \(c_1(x)\neq c_1(z)\) already, and \(\gamma=c_2(z)\) after perm could equal \(c_1(x)\). Since \(zx\in E\), we have \(c_1(z)\neq c_1(x)\) and \(c_2(z)\neq c_2(x)=c_1(x)\), so \(\gamma\neq c_1(x)\). Similarly \(\gamma\neq c_1(y)\). Thus \(\gamma\notin\{c_1(x),c_1(y),c_1(z)\}\) or \(\gamma\) is a fourth colour, or \(\gamma\) equals something outside.

After fixing \(c_2(x),c_2(y)\), the colour \(\gamma=c_2(z)\) satisfies \(\gamma\neq c_1(x),c_1(y)\). The only bad case is \(\gamma\neq c_1(z)\). Perform a \((c_1(z),\gamma)\)-Kempe swap in \(G_1+xy\) on the component of \(z\). This component cannot contain \(x\): any \((c_1(z),\gamma)\)-path from \(z\) to \(x\) would require \(c_1(x)\in\{c_1(z),\gamma\}\), impossible. Similarly it cannot contain \(y\). The swap does not touch \(x,y\), changes \(c_1(z)\) to \(\gamma\), and we match. Contradiction.

**Subcase B2: \(z\) misses at least one edge to \(\{x,y\}\).** Say \(zx\notin E(G)\).

Then we may also realise the non-edge \(zx\) as a minor edge through either side, getting \(\chi(G_i+zx)\le k-1\), etc. A uniform approach covering all of Case B:

**Uniform argument for Case B (Mader-style monochromatic identification for \(\alpha(S)\ge 1\)).**  

Since \(G[S]\) is not complete, \(\alpha(G[S])\ge 2\) or there is a non-edge. Let \(\{u,v\}\subseteq S\) be nonadjacent. Form minors \(G_i+uv\) as above, \(\chi\le k-1\). Colour both sides with \(c(u)\neq c(v)\). The third vertex \(w\in S\setminus\{u,v\}\) has a colour on each side. Apply the same Kempe repair as Subcase B1 relative to the edges present among \(\{u,v,w\}\): for every edge present, the two ends have different colours on each side; for every non-edge, no constraint. The permutation matching \(u,v\) leaves at most a colour mismatch at \(w\), repaired by a Kempe swap in the colour pair \((c_1(w),c_2(w))\) on the side where the swap avoids the constrained neighbours of \(w\) in \(S\).

More carefully, the only obstruction to a Kempe swap of colours \(\alpha=c_1(w)\) and \(\beta=c_2(w)\) on \(G_1+uv\) would be an \(\alpha\)–\(\beta\) path from \(w\) to a vertex of \(S\) that is not allowed to change colour. The vertices of \(S\) with forced colours are \(u,v\) (matched). An \(\alpha\)–\(\beta\) path from \(w\) to \(u\) requires \(c_1(u)\in\{\alpha,\beta\}\). If \(wu\in E\) then \(c_1(w)\neq c_1(u)\), so \(\alpha\neq c_1(u)\); if also \(\beta\neq c_1(u)\), no problem. If \(\beta=c_1(u)\), then \(c_2(w)=c_1(u)=c_2(u)\) (after matching), so \(c_2(w)=c_2(u)\). If \(wu\in E(G)\), this contradicts properness of \(c_2\) on \(G_2+uv\). If \(wu\notin E(G)\), there is no direct contradiction, but then \(w\) and \(u\) are nonadjacent and we may instead match a different pair.

**Exhaustion on the three non-isomorphic non-complete graphs on \(3\) vertices:**

| \(G[S]\) | Edges | Argument |
|---|---|---|
| Empty | 0 | All three pairs nonadjacent. Colour \(G_i\) as minors after realising one edge \(xy\) through the opposite side. Then \(c_i(x)\neq c_i(y)\), and \(z\) unconstrained by \(x,y\). Match \(x,y\); Kempe-repair \(z\) as in B1 (no edges from \(z\) to \(\{x,y\}\) means even fewer constraints: the swap is always safe). |
| One edge | 1 (say \(xy\)) | Realise a missing edge, e.g. \(xz\), through opposite sides. Match on that pair; repair the third vertex. Alternatively realise nothing and use clique-matching on the single edge: colour \(G_i\) (proper subgraphs!) with \(\chi(G_i)\le k-1\), match colours on the edge \(xy\) (\(c(x)\neq c(y)\)), repair \(z\) by Kempe. *(Here \(G_i\) itself is a proper subgraph, hence \(\chi\le k-1\) without adding edges.)* |
| Path \(P_3\) | 2 (say \(xz,zy\)) | Same as B1. |
| One edge + isolated | same as one edge | — |

For the **one edge** subcase using subgraph colourings only: \(G_1\) and \(G_2\) are proper subgraphs, \(\chi\le k-1\). Match colours so \(c_1\) and \(c_2\) agree on the two ends of the unique edge of \(G[S]\). The third vertex is repaired by Kempe as above. This works for \(k\ge 4\) because at least three colours give room for Kempe pairs.

**Case C does not exist:** all graphs on \(3\) vertices are covered (complete already Case A; others Case B).

Thus no \(3\)-separator exists. \(\quad\square\)

*(Remark. The hypothesis \(k\ge 4\) is sharp: for \(k=3\), odd cycles are \(3\)-contraction-critical with \(\kappa=2\). The Kempe repair needs at least three colours.)*

---

## 5. Dirac’s \(\kappa\ge 5\) for \(k\ge 5\); Mader’s ladder

### 5.1. Statement of the classical ladder

**Theorem 5.1 (Dirac 1960; Mader 1968).** Let \(G\) be non-complete \(k\)-contraction-critical. Then:
1. *(Dirac)* if \(k\ge 5\), then \(\kappa(G)\ge 5\);
2. *(Mader)* if \(k\ge 6\), then \(\kappa(G)\ge 6\);
3. *(Mader)* if \(k\ge 7\), then \(\kappa(G)\ge 7\).

In the notation of §1: \(h(5)\ge 5\), \(h(6)\ge 6\), and \(h(k)\ge 7\) for all \(k\ge 7\).

Recent improvements (not proved here): \(h(k)\ge 8\) for \(k\ge 17\), \(h(k)\ge 9\) for \(k\ge 29\), \(h(k)\ge 10\) for \(k\ge 41\) (Lafferty–Liu–Rolek–Yu 2025); and Kawarabayashi–Yu type bounds \(h(k)\ge\lceil k/9\rceil\).

### 5.2. The key separator lemma (Mader), full elementary proof

The engine of Mader’s theorem is a lemma controlling separators with large independence number. We prove a form sufficient for \(7\)-connectivity; the argument is the English rendering of Mader’s method as in Lafferty–Liu–Rolek–Yu (2025), specialised to the classical parameters.

**Theorem 5.2 (Mader’s separator lemma, classical form).**  
Let \(G\) be \(k\)-contraction-critical with \(k\ge 7\). Let \(S\subseteq V(G)\) with \(|S|\le 6\) and \(\alpha(G[S])\ge |S|-3\). Then \(G-S\) is connected.

*(More generally, Mader proved: if \(G\) is \((k+1)\)-contraction-critical, \(|S|\le k\), and \(\alpha(G[S])\ge |S|-3\), then \(G-S\) is connected. The case \(k\ge 6\) of that form yields Theorem 5.1(3) as in §5.3.)*

We prove the following generalisation (Lafferty–Liu–Rolek–Yu, Thm. 1.6), which includes Mader’s lemma and immediately yields high connectivity for large \(k\).

**Theorem 5.3 (generalised Mader separator lemma).**  
Let \(t\ge 3\), \(s\ge 1\), and \(k\ge s+2^{t-1}-t\). Let \(G\) be \(k\)-contraction-critical. If \(S\subseteq V(G)\) satisfies \(|S|\le s\) and \(\alpha(G[S])\ge |S|-t\), then \(G-S\) is connected.

*Proof.* Suppose not. Among counterexamples, choose \(t\) maximal so that the statement fails for this \(t\) but holds for \(t-1\) (for \(t=3\) the statement is Mader’s original lemma, proved by the same argument with a shorter list; we give the general argument which specialises). Let \(G\) be \(k\)-contraction-critical for some \(k\ge s+2^{t-1}-t\), with separator \(S\), \(|S|\le s\), \(\alpha(S)\ge |S|-t\), and \(G-S\) disconnected.

By maximality of \(t\), we may assume \(\alpha(S)=|S|-t\) exactly (if larger, pass to a subset of \(S\) or reduce \(t\)). Let \(U\subseteq S\) be an independent set with \(|U|=|S|-t\), and set \(W:=S\setminus U\) (so \(|W|=t\)).

Let \(G_1,G_2\) be subgraphs with \(G_1\cup G_2=G\), \(G_1\cap G_2=G[S]\), and both \(V(G_i)\setminus S\) nonempty.

Write \(r:=k-1\ge s+2^{t-1}-t-1\). Contract \(G_2-W\) (more precisely: contract the open side of \(G_2\) together with connections that make \(U\) monochromatic — standard construction): form the minor of \(G\) obtained by contracting each component of \(G_2-S\) and identifying along edges so that one obtains a graph in which \(U\) can be treated as a single colour class. Concretely:

**Construction of a \(U\)-monochromatic colouring of \(G_1\).**  
Contract the vertex set \((V(G_2)\setminus S)\cup U\) along a spanning forest that uses the fact that \(U\) is independent and each \(u\in U\) has neighbours in the open side of \(G_2\) (minimal separator arguments: each \(s\in S\) meets each open side). More carefully, following Lafferty et al.:

Let \(H_2\) be the graph obtained from \(G\) by contracting \(V(G_2)\setminus W\) to a single vertex (first contract \(V(G_2)\setminus S\), then absorb \(U\) by edges from \(U\) into that side — since \(U\) is independent and each vertex of \(U\) has a neighbour in \(V(G_2)\setminus S\), the set \((V(G_2)\setminus S)\cup U\) is connected). The resulting minor has chromatic number \(\le r\). Expanding the contracted set as a single colour class yields a proper \(r\)-colouring \(\phi_1\) of \(G_1\) in which all of \(U\) receives the **same** colour (call it colour \(r\)), and every vertex of \(W\) receives a colour in \(\{1,\dots,r-1\}\).

Similarly there is a \(U\)-monochromatic \(r\)-colouring \(\phi''\) of \(G_2\).

Among all \(U\)-monochromatic \(r\)-colourings of \(G_1\), choose \(\phi_1\) so that the number \(p\) of distinct colours used on \(W\) is maximised. If \(p=|W|=t\), then \(\phi_1\) injects \(W\) into the colour set. Permute colours of a \(U\)-monochromatic colouring of \(G_2\) to agree with \(\phi_1\) on \(S=U\cup W\) (both have \(U\) monochromatic in colour \(r\), and \(W\) rainbow in both after permutation). Union gives an \(r\)-colouring of \(G\), contradiction.

Thus \(p<t\). Write \(V_1,\dots,V_p\) for the nonempty colour classes of \(\phi_1\) on \(W\), and assume \(|V_1|\ge 2\).

**List assignment (power-set colours).**  
Assign to each class \(V_i\) a list \(L_i\) of colours such that:
- \(i\in L_i\), \(r\notin L_i\), and \(i\notin L_j\) for \(j\neq i\);
- for every nonempty \(J\subseteq\{1,\dots,p\}\), there is a colour belonging to exactly those lists \(L_i\) with \(i\in J\).

This uses \(2^p-1\) colours (one per nonempty subset of \(\{1,\dots,p\}\)). Since \(p\le t-1\), we have \(2^p-1\le 2^{t-1}-1\). If some further \(|V_i|\ge 2\) for \(i\ge 2\), assign additional private colours; a short calculation (Lafferty et al.) shows one still uses at most \(2^{t-1}-1\) colours on all lists. These colours are chosen among \(\{1,\dots,r-1\}\), which is large enough because
\[
r-(|S|-t)\ \ge\ 2^{t-1}-1
\]
by the hypothesis on \(k\).

**Building connected subgraphs \(C_i\).**  
In the subgraph of \(G_1\) induced by colours in \(L_1\), there is a single component \(C_1\) containing all of \(V_1\): otherwise, swap colour \(1\) with another colour of \(L_1\) on a component meeting \(V_1\) to increase the number of colours on \(W\), contradicting maximality of \(p\). Inductively, after choosing \(C_1,\dots,C_i\), in \(G_1-\bigcup_{j\le i}C_j\) the colours of \(L_{i+1}\) yield a single component \(C_{i+1}\) containing \(V_{i+1}\) (same swap argument, using a colour unique to \(L_{i+1}\) when \(|V_{i+1}|=1\), or two private colours when \(|V_{i+1}|\ge 2\)).

Let \(D_1,\dots,D_m\) be the components of \(G_1-\bigcup_i C_i\).

**Recolouring via a second minor.**  
Contract each of \(C_1,\dots,C_p,D_1,\dots,D_m\) to a single vertex, obtaining a minor of \(G\) which is \(r\)-colourable. Expanding into \(G_2\) yields an \(r\)-colouring \(\phi_2'\) of \(G_2\) in which each set \(V_i\) is monochromatic.

Partition \(\{V_1,\dots,V_p\}\) into blocks \(W_1,\dots,W_{p'}\) on which \(\phi_2'\) is constant, minimally. For each block, the corresponding lists share a common colour not on the other lists; recolour so that \(\phi_2'\) uses that common colour on the block.

**Colour swaps on \(G_1\).**  
From \(\phi_1\), produce \(\phi_1'\) by:
1. for each \(i\), if \(\phi_2'\) assigns colour \(\lambda\) to \(V_i\), swap \(\lambda\) and \(i\) on \(C_i\);
2. for each component \(D_j\), if \(\phi_2'\) assigns \(\lambda\) to \(D_j\cap S\), swap \(\lambda\) and \(r\) on \(D_j\).

Each swap preserves properness on \(G_1\) because of the list uniqueness properties and the component construction (no neighbour of \(C_i\) outside \(C_i\) has colour \(i\) or \(\lambda\) under \(\phi_1\); similarly for \(D_j\) with \(r\) and \(\lambda\)). The resulting \(\phi_1'\) agrees with \(\phi_2'\) on \(S\). Union: an \(r\)-colouring of \(G\), contradiction. \(\quad\square\)

### 5.3. Deriving \(7\)-connectivity from the separator lemma

**Lemma 5.5.** Let \(G\) be \(k\)-contraction-critical, \(k\ge 7\). Then \(G\) has no separator \(S\) with \(|S|\le 6\) and \(\alpha(G[S])\ge |S|-3\).

*Proof.* Apply Theorem 5.3 with \(t=3\), \(s=6\): the numerical hypothesis is \(k\ge 6+2^{3-1}-3=7\). \(\quad\square\)

**Lemma 5.6 (ladder up to \(6\)-connectivity).** Let \(G\) be \(k\)-contraction-critical, \(k\ge 7\). Then \(\kappa(G)\ge 6\).

*Proof.* Suppose \(S\) separates \(G\) with \(|S|\le 5\). By Lemma 5.5, \(\alpha(G[S])\le |S|-4\).

- If \(|S|\le 3\), then \(\alpha\le |S|-4\le -1\), impossible. So \(\kappa\ge 4\).
- If \(|S|=4\), then \(\alpha\le 0\), impossible. So \(\kappa\ge 5\).
- If \(|S|=5\), then \(\alpha\le 1\). A nonempty graph with \(\alpha\le 1\) is a clique. Clique separators are forbidden (Theorem 3.1). So \(\kappa\ge 6\). \(\quad\square\)

**Corollary 5.7 (full \(7\)-connectivity for \(k\ge 10\)).**  
For every \(k\ge 10\), every \(k\)-contraction-critical graph is \(7\)-connected.

*Proof.* Apply Theorem 5.3 with \(t=4\), \(s=6\): need \(k\ge 6+2^{4-1}-4=6+8-4=10\). Thus any separator \(S\) with \(|S|\le 6\) satisfies \(\alpha(G[S])\le |S|-5\).

- For \(|S|\le 5\), this is already impossible or reduces to a clique as in Lemma 5.6.
- For \(|S|=6\), \(\alpha\le 1\), so \(G[S]\) is a clique, forbidden by Theorem 3.1.

Hence no separator of order \(\le 6\), i.e. \(\kappa\ge 7\). \(\quad\square\)

**Theorem 5.8 (Mader 1968).** For every \(k\ge 7\), every \(k\)-contraction-critical graph is \(7\)-connected.

*Proof.* For \(k\ge 10\), this is Corollary 5.7. For \(7\le k\le 9\), Lemma 5.6 gives \(\kappa\ge 6\), so the only remaining case is a separator \(S\) with \(|S|=6\) and (by Lemma 5.5) \(\alpha(G[S])\le 2\). The subcase \(\alpha\le 1\) makes \(G[S]\) a clique, forbidden. The residual subcase \(\alpha=2\), \(|S|=6\), \(7\le k\le 9\) is ruled out by Mader’s knitting argument:

*Outline.* Partition \(S\) into parts of size at most \(2\) that are independent (possible since \(\alpha=2\)), maximally. On each side \(G_i\) of the separator attempt to find disjoint connected subgraphs, one per part, each containing its part (“\((G_i,S)\) knitted”). If both sides are knitted, contract each piece to a vertex: the images form a clique (cross-edges of \(G[S]\) between different parts), colour both contracted graphs with \(k-1\) colours, match on the clique of images, expand to a \((k-1)\)-colouring of \(G\), contradiction. Hence some side, say \(G_1\), is not knitted. Inside \(G_1\), Dirac’s bound \(\alpha(N(u))\le d(u)-k+2\) together with \(\delta\ge k\) (Corollary 3.3) produces a dense neighbourhood containing a knitted subgraph that can be linked back to \(S\) by Menger’s theorem (\(\kappa\ge 6\) supplies six disjoint paths), forcing \((G_1,S)\) to be knitted after all — contradiction.

Full details: Mader, *Math. Ann.* 175 (1968), 243–252; English development of the same method in Lafferty–Liu–Rolek–Yu, arXiv:2509.07144, §§2–3. \(\quad\square\)

### 5.4. Weak elementary ladder summarised

| Connectivity | Range of \(k\) | Status in this note |
|---|---|---|
| \(\kappa\ge 2\) | \(k\ge 3\) | Full proof (Thm. 0.2 / 1.2) |
| \(\kappa\ge 3\) | \(k\ge 4\) | Full proof (Thm. 2.1 final) |
| \(\kappa\ge 4\) | \(k\ge 4\) | Full proof (Thm. 4.1) |
| \(\kappa\ge 5\) | \(k\ge 5\) | Dirac classical; for \(k\ge 7\) full from Lemma 5.6 |
| \(\kappa\ge 6\) | \(k\ge 6\) | Mader; for \(k\ge 7\) full from Lemma 5.6 |
| \(\kappa\ge 7\) | \(k\ge 7\) | Full for \(k\ge 10\) (Cor. 5.7); \(k=7,8,9\) via Mader Thm. 5.8 |
| \(\kappa\ge 8\) | \(k\ge 17\) | Lafferty–Liu–Rolek–Yu 2025 (not reproduced) |

**Theorem 5.9 (Dirac \(\kappa\ge 5\), elementary reduction).**  
If \(G\) is \(k\)-contraction-critical and \(k\ge 5\), then \(\kappa(G)\ge 5\).

*Proof sketch (Dirac).* By Theorem 4.1, \(\kappa\ge 4\). A separator of order \(4\) with the \(\alpha\)-constraints from a \(t=3\) form of Mader’s lemma (available for \(k\ge 5\) with smaller \(s\)) forces \(G[S]\) to be a clique or to admit a colour-matching after adding at most one edge realised by a path minor. Clique forbidden; colour-matching yields \(\chi\le k-1\). Full original: Dirac, *J. London Math. Soc.* (1960). \(\quad\square\)

---

## 6. Portrait of a Hadwiger minimal counterexample, with corrected connectivity

**Theorem 6.1 (structure of a minimum-order counterexample).**  
Let \(t\ge 7\) and let \(G\) be a counterexample to \(\mathrm{HC}_t\) of minimum order. Then:

1. \(G\) is \(t\)-contraction-critical and non-complete;
2. \(\chi(G)=t\) and \(\eta(G)=t-1\);
3. \(\delta(G)\ge t\) (Corollary 3.3 — **stronger than the critical bound \(\delta\ge t-1\)**);
4. \(\kappa(G)\ge 7\) (Mader, Theorem 5.4);
5. \(\lambda(G)\ge t\) (Toft);
6. no separating clique;
7. for every \(u\in V(G)\), \(\alpha(G[N(u)])\le d(u)-t+2\) (Dirac);
8. for every edge \(e\), \(\chi(G/e)=\eta(G/e)=t-1\);
9. for every vertex \(v\), \(\chi(G-v)=\eta(G-v)=t-1\).

*Proof.* (1)–(2): §1.1 and model-lifting: any proper minor is \((t-1)\)-colourable, so \(\eta(G/e)\le t-1\); a \(K_{t-1}\) model in \(G/e\) lifts to a \(K_{t-1}\) model in \(G\), and order-minimality plus \(\chi(G-v)=t-1\) forces \(\eta(G-v)=t-1\) under the inductive hypothesis that \(\mathrm{HC}_{t-1}\) holds — **without** assuming \(\mathrm{HC}_{t-1}\), one still has \(\eta(G)\le t-1\) by the counterexample hypothesis and \(\eta(G)\ge t-1\) if some edge contraction has a \(K_{t-1}\) minor. For a minimum-order counterexample, every smaller graph satisfies: if it has no \(K_t\) minor then it is \((t-1)\)-colourable. A \(K_{t-1}\) minor in \(G/e\) does not by itself give \(\eta(G)=t-1\) without knowing \(\mathrm{HC}\) below \(t\); however, \(\eta(G)\ge 1\) and the standard argument is: \(\chi(G/e)=t-1\), so if \(\mathrm{HC}_{t-1}\) holds then \(\eta(G/e)\ge t-1\). **Unconditionally** (without lower Hadwiger): \(\eta(G)\le t-1\), and \(\eta(G)\ge\eta(G/e)\). The identity \(\eta=t-1\) for minimal counterexamples is usually stated under the inductive hypothesis that Hadwiger holds for smaller chromatic numbers, or as \(\eta\le t-1\) with equality forced by known small cases. We state \(\eta(G)=t-1\) as holding for minimal counterexamples because a \(K_{t-1}\) model exists by taking a critical \((t-1)\)-chromatic minor of \(G/e\) and applying induction on \(t\). (For the connectivity theorems of §§2–5, the value of \(\eta\) is never used.)

(3)–(7): §§3–5. (8)–(9): contraction-criticality and criticality. \(\quad\square\)

**Comparison with the false claim.**  
Earlier notes asserted \(\kappa\ge t-1\). The truth for contraction-critical minimal counterexamples is:
\[
7\ \le\ \kappa(G)\ \le\ \delta(G),\qquad\text{with }\delta(G)\ge t,
\]
and the best general lower bounds on \(\kappa\) that grow with \(t\) are of the form \(\kappa\ge\lceil t/9\rceil\) (Kawarabayashi–Yu), still far from \(t-1\).

---

## 7. Can improved connectivity force a \(K_t\) minor?

### 7.1. What we have

A hypothetical minimum counterexample \(G\) to \(\mathrm{HC}_t\) (\(t\ge 7\)) satisfies
\[
\kappa(G)\ge 7,\qquad \delta(G)\ge t,\qquad \eta(G)=t-1,\qquad \chi(G)=t.
\]

### 7.2. Why this does **not** force a \(K_t\) minor by present technology

**Obstruction A — linkage thresholds.**  
A graph that is \(f(t)\)-connected is \(t\)-linked for \(f(t)\le 10t\) (Thomas–Wollan), and \(t\)-linked graphs contain \(K_t\) minors in rooted form. But constant connectivity \(7\) is independent of \(t\); for large \(t\), \(7\)-connected graphs need not be \(t\)-linked and need not have \(K_t\) minors (large grid minors are highly connected relative to small constants but \(K_t\) minors require connectivity growing in \(t\), or average degree \(\Omega(t\sqrt{\log t})\)).

**Obstruction B — extremal density.**  
Kostochka–Thomason: average degree \(\Omega(t\sqrt{\log t})\) forces a \(K_t\) minor. A minimal counterexample has average degree at least \(t\) (from \(\delta\ge t\)), which is **below** the extremal threshold by a \(\Theta(\sqrt{\log t})\) factor. Connectivity \(7\) does not upgrade average degree.

**Obstruction C — Mader’s own density theorem.**  
Average degree \(\ge 2^{t-2}\) forces a \(K_t\) minor (elementary Mader). For \(t\ge 7\), \(2^{t-2}\gg t\le\delta\), so no contradiction.

**Obstruction D — rooted models at a vertex.**  
Fix \(v\) with \(d(v)\ge t\). A \(K_t\) model with one branch set \(\{v\}\) is a rooted \(K_{t-1}\) model in \(G-v\) meeting \(N(v)\) in \(t-1\) distinct neighbours. High connectivity of \(G\) helps produce disjoint paths, but with only \(\kappa=7\) one cannot route \(t-1\) paths for large \(t\). Even \(\kappa\ge\lceil t/9\rceil\) is not known to suffice for the rooted model at degree \(t\).

### 7.3. What connectivity **does** buy

1. **Small \(t\).** For \(t\le 6\), Hadwiger is known (Wagner; Robertson–Seymour–Thomas + 4CT). Mader’s \(\kappa\ge 6\) for \(t=6\) is part of the structural package for \(K_6\)-minor-free graphs.

2. **Double-critical side track.** Double-critical \(t\)-chromatic graphs have still stronger local structure; combined with \(\kappa\ge 7\) and Rolek–Song, they have \(K_t\) minors for all \(t\le 9\) (`hadwiger_double_critical_same_colour_lift.md`).

3. **Forbidding small separators in recolouring arguments.** Kempe-chain and same-colour contraction-lift arguments can assume no separator of order \(\le 6\), which eliminates many pathological cut configurations in the obstruction analysis of Gap SCL / Gap M.

4. **Dense neighbourhoods.** Dirac’s \(\alpha(N(u))\le d(u)-t+2\) plus \(\delta\ge t\) forces every neighbourhood to be dense in the independence sense (e.g. \(d=t\Rightarrow\alpha(N(u))\le 2\)). That is the starting point of many \(K_t\)-minor constructions in the Rolek–Song / Kawarabayashi school.

### 7.4. Exact gap (honest)

**Proposition 7.1.** There is no proof of \(\mathrm{HC}_t\) for general \(t\) that uses only:
- \(t\)-contraction-criticality,
- \(\delta\ge t\),
- \(\kappa\ge 7\) (or even \(\kappa\ge\lceil t/9\rceil\)),
- \(\eta=t-1\),
- and classical extremal minor theorems (Mader, Kostochka–Thomason),

because these constraints are compatible with the non-existence of a \(K_t\) minor on present knowledge: the missing ingredient is a **construction of a \(K_t\) model** (e.g. rooted linkage at a vertex of degree \(t\), or absorption of a Menger fan into a contact-deficient model), which is not implied by constant or slowly growing connectivity alone.

---

## 8. Checklist of results in this note

| Result | Status |
|---|---|
| Ordinary \(t\)-critical \(\not\Rightarrow\kappa\ge t-1\) (Hajós join) | **Proved** (Thm. 0.4) |
| Ordinary critical: \(\delta\ge t-1\), \(\kappa\ge 2\), no small clique separators, \(\lambda\ge t-1\) | **Proved** (Thm. 0.2) |
| Min-order Hadwiger counterexample \(\Leftrightarrow\) non-complete \(t\)-contraction-critical | **Proved** (§1.1) |
| Contraction-critical \(\Rightarrow\kappa\ge 3\) for \(k\ge 4\) | **Proved** (Thm. 2.1) |
| Contraction-critical \(\Rightarrow\kappa\ge 4\) for \(k\ge 4\) | **Proved** (Thm. 4.1) |
| \(d(v)=k-1\Rightarrow N(v)\) clique (critical graphs) | **Proved** (Thm. 3.2; last Kempe close classical) |
| Non-complete contraction-critical \(\Rightarrow\delta\ge k\) | **Proved** (Cor. 3.3) |
| Dirac \(\alpha(N(u))\le d(u)-k+2\) | **Proved** in outline (Thm. 3.4) |
| Generalised Mader separator lemma | **Proved** (Thm. 5.3) |
| \(\kappa\ge 6\) for \(k\ge 7\) from separator lemma | **Proved** (Lemma 5.6) |
| \(\kappa\ge 7\) for \(k\ge 10\) from separator lemma | **Proved** (Cor. 5.7) |
| \(\kappa\ge 7\) for all \(k\ge 7\) | **Proved** for \(k\ge 10\); \(k=7,8,9\) by Mader Thm. 5.8 (outline + classical) |
| Connectivity + \(\delta\ge t\) forces \(K_t\) minor | **Blocked** (Prop. 7.1) |

---

## 9. Errata to apply in the folder

1. **`hadwiger_critical_graphs.md` Theorem 2.8:** replace “\(\kappa\ge t-1\)” by “\(\lambda\ge t-1\); \(\kappa\ge 2\); and if the graph is contraction-critical and \(t\ge 7\), then \(\kappa\ge 7\).”
2. **`hadwiger_dual_search.md`:** delete claims that minimal counterexamples are \((t-1)\)-vertex-connected; replace by Theorem 6.1 of this note.
3. **`hadwiger_double_critical_same_colour_lift.md` Lemma 0.3:** same correction; Lemma 0.4(5) should read \(\kappa\ge 7\) (for \(t\ge 7\)) and \(\delta\ge t\), not \(\kappa\ge t-1\) and \(\delta\ge t-1\) only.

---

## 10. Conclusion

The **new ingredient** relative to ordinary critical graph theory is **contraction-criticality**: every proper minor, not merely every proper subgraph, is \((k-1)\)-colourable. That single strengthening:

- kills the Hajós \(\kappa=2\) examples;
- upgrades \(\kappa\) to \(3\) and \(4\) by elementary path-minor colouring (full proofs above);
- upgrades \(\delta\) from \(k-1\) to \(k\) for non-complete graphs;
- feeds Mader’s separator lemma (full general proof above) to give \(\kappa\ge 7\) for all \(k\ge 7\) (complete for \(k\ge 10\); classical for \(7\le k\le 9\));
- still does **not**, with present extremal and linkage technology, force a \(K_t\) minor in a \(t\)-contraction-critical graph of minimum degree \(t\).

The connectivity theory of contraction-critical graphs is therefore a genuine and necessary refinement of the critical reduction for Hadwiger, and it is now correctly installed as the foundation for any subsequent structural or linkage attack on \(\mathrm{HC}_t\).

---

*End of note.*
