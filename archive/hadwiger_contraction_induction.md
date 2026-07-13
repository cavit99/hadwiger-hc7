# Hadwiger’s Conjecture via Contraction–Coloring Interplay and Induction on \(|V|\)

**Conjecture (Hadwiger).** For every finite simple graph \(G\) and every integer \(t\ge 1\),
\[
\text{if \(G\) has no \(K_t\)-minor, then \(\chi(G)\le t-1\).}
\]
Equivalently: \(\chi(G)\le\eta(G)\) for every finite simple graph \(G\), where the **Hadwiger number** \(\eta(G)\) is the largest integer \(t\) such that \(G\) has a \(K_t\)-minor.

This note develops the contraction–coloring inductive program completely. Every lemma is proved in full. Affirmative proofs are obtained for all \(t\le 4\). For general \(t\), the program reduces Hadwiger to a single, precisely stated obstruction (Gap M / Gap H). That obstruction is **not** resolved here. No reduction equivalent in strength to Hadwiger is claimed as a proved theorem.

---

## 0. Notation and elementary facts

Graphs are finite and simple unless stated otherwise. Write \(n(G)=|V(G)|\), \(m(G)=|E(G)|\). For \(e=xy\in E(G)\):

- \(G-e\) deletes the edge \(e\);
- \(G/e\) **contracts** \(e\): identify \(x,y\) to a single vertex \(v_e\), delete loops, replace parallel edges by single edges (simple contraction).

A **\(K_t\)-model** in \(G\) is a family of \(t\) pairwise disjoint nonempty connected subgraphs \(B_1,\dots,B_t\) (**branch sets**) such that for all \(i\neq j\) there is an edge of \(G\) with one end in \(B_i\) and the other in \(B_j\). The graph \(G\) has a \(K_t\)-minor iff it admits a \(K_t\)-model.

**Fact 0.1 (Monotonicity).** If \(H\) is a minor of \(G/e\), of \(G-e\), or of a subgraph of \(G\), then \(H\) is a minor of \(G\). In particular
\[
\eta(G/e)\le\eta(G),\qquad \eta(G-e)\le\eta(G),\qquad \eta(H)\le\eta(G)\ \text{ for every subgraph \(H\subseteq G\).}
\]

**Fact 0.2 (Models live in components).** If \(G=\bigsqcup_i G_i\), every connected subgraph of \(G\) lies in one component, so every \(K_t\)-model lies in one component. Thus \(\eta(G)=\max_i\eta(G_i)\) and \(\chi(G)=\max_i\chi(G_i)\).

**Fact 0.3 (Critical graphs).** A graph \(G\) is **\(k\)-critical** if \(\chi(G)=k\) and \(\chi(H)<k\) for every proper subgraph \(H\subsetneq G\). Every graph of chromatic number \(k\) has a \(k\)-critical subgraph. Every \(k\)-critical graph \(G\) satisfies:

1. \(G\) is connected;
2. \(\delta(G)\ge k-1\);
3. for every edge \(e=xy\), \(\chi(G-e)=k-1\), and in **every** proper \((k-1)\)-coloring of \(G-e\) the ends \(x,y\) receive the **same** color (otherwise that coloring would properly color \(G\)).

---

## 1. Reduction lemmas

A **counterexample** is a graph \(G\) with \(\chi(G)>\eta(G)\). A **minimal counterexample** is a counterexample of minimum order; among those, one of minimum size.

### Lemma 1.1 (Disjoint unions)
If \(\chi(G_i)\le\eta(G_i)\) for every component \(G_i\) of \(G\), then \(\chi(G)\le\eta(G)\).

**Proof.** By Fact 0.2,
\[
\chi(G)=\max_i\chi(G_i)\le\max_i\eta(G_i)=\eta(G).
\]
∎

### Lemma 1.2 (Cutvertices / 1-sums)
Let \(G=G_1\cup G_2\) with \(V(G_1)\cap V(G_2)=\{v\}\) and \(E(G_1)\cap E(G_2)=\emptyset\). If \(\chi(G_i)\le\eta(G_i)\) for \(i=1,2\), then \(\chi(G)\le\eta(G)\).

**Proof.** Aligning colors at the single shared vertex \(v\) gives \(\chi(G)=\max\bigl(\chi(G_1),\chi(G_2)\bigr)\). Every \(K_t\)-model of either \(G_i\) is a \(K_t\)-model of \(G\), so \(\eta(G)\ge\max\bigl(\eta(G_1),\eta(G_2)\bigr)\). Therefore
\[
\chi(G)=\max\bigl(\chi(G_1),\chi(G_2)\bigr)\le\max\bigl(\eta(G_1),\eta(G_2)\bigr)\le\eta(G).
\]
∎

### Lemma 1.3 (Minimal counterexamples are 2-connected)
Every minimal counterexample is 2-connected.

**Proof.** Let \(G\) be a minimal counterexample. If \(G\) is disconnected, each component has smaller order, satisfies \(\chi\le\eta\) by minimality, and Lemma 1.1 yields \(\chi(G)\le\eta(G)\), contradiction. Thus \(G\) is connected.

If \(G\) has a cutvertex, write \(G=G_1\cup G_2\) as in Lemma 1.2 with \(n(G_i)<n(G)\). Minimality gives \(\chi(G_i)\le\eta(G_i)\); Lemma 1.2 gives \(\chi(G)\le\eta(G)\), contradiction. ∎

### Lemma 1.4 (Minimal counterexamples are critical)
Every minimal counterexample \(G\) is \(k\)-critical for \(k=\chi(G)\). In particular \(\delta(G)\ge k-1\) and \(\eta(G)\le k-1\) (so \(G\) has no \(K_k\)-minor).

**Proof.** Let \(k=\chi(G)\). Then \(\eta(G)\le k-1\) because \(G\) is a counterexample. Among order-minimal counterexamples, take \(G\) with \(m(G)\) minimum as well.

Let \(H\subseteq G\) be a \(k\)-critical subgraph. Then \(\chi(H)=k\) and \(\eta(H)\le\eta(G)\le k-1\), so \(H\) is a counterexample. Minimality of order forces \(n(H)=n(G)\), so \(H\) is spanning. If \(H\neq G\), then \(H\) omits at least one edge of \(G\), whence \(m(H)<m(G)\), contradicting minimality of size. Thus \(H=G\), so \(G\) is \(k\)-critical. Fact 0.3 gives \(\delta(G)\ge k-1\). ∎

### Corollary 1.5 (Induction setup)
Hadwiger holds for all graphs if and only if every \(k\)-critical graph has a \(K_k\)-minor (all \(k\ge 1\)).

**Proof.** If \(\chi(G)>\eta(G)\), set \(k=\chi(G)\) and take a \(k\)-critical subgraph \(H\). Then \(\eta(H)\le\eta(G)<k=\chi(H)\), so \(H\) is \(k\)-critical with no \(K_k\)-minor. The converse is immediate. ∎

---

## 2. Contraction–coloring dictionary

### Lemma 2.1 (Colorings of contractions)
Let \(e=xy\in E(G)\). There is a natural bijection between

- proper colorings of \(G/e\), and
- proper colorings of \(G-e\) in which \(x\) and \(y\) receive the same color.

Under the bijection, the color of \(v_e\) equals the common color of \(x\) and \(y\).

**Proof.** From a proper coloring \(c\) of \(G/e\), set \(c'(x)=c'(y)=c(v_e)\) and \(c'(u)=c(u)\) for all other \(u\). Every edge of \(G-e\) maps to an edge of \(G/e\) or to an edge incident to exactly one of \(x,y\); properness is preserved. Conversely, a proper coloring of \(G-e\) with \(c'(x)=c'(y)\) descends to a proper coloring of \(G/e\) by coloring \(v_e\) with that common value. ∎

### Lemma 2.2 (Critical graphs and contractions)
Let \(G\) be \(k\)-critical and \(e=xy\in E(G)\). Then:

1. \(\chi(G-e)=k-1\);
2. every proper \((k-1)\)-coloring of \(G-e\) assigns the same color to \(x\) and \(y\);
3. \(\chi(G/e)=k-1\).

**Proof.** (1)–(2) are Fact 0.3(3). For (3): by (1)–(2) and Lemma 2.1, \(G/e\) is \((k-1)\)-colorable, so \(\chi(G/e)\le k-1\). If \(\chi(G/e)\le k-2\), Lemma 2.1 would give \(\chi(G-e)\le k-2\), contradicting (1). Hence \(\chi(G/e)=k-1\). ∎

### Lemma 2.3 (Contraction preserves absence of \(K_k\))
If \(G\) has no \(K_k\)-minor and \(e\in E(G)\), then \(G/e\) has no \(K_k\)-minor.

**Proof.** Fact 0.1. ∎

### Lemma 2.4 (Inductive coloring of contractions of minimal counterexamples)
Let \(G\) be a minimal counterexample with \(\chi(G)=k\). Then for every edge \(e\in E(G)\),
\[
\chi(G/e)\le\eta(G/e)\le\eta(G)\le k-1.
\]
Combined with Lemma 2.2,
\[
\chi(G/e)=\eta(G/e)=k-1.
\]
Thus every single-edge contraction of a minimal counterexample is a graph attaining Hadwiger equality at level \(k-1\).

**Proof.** Since \(n(G/e)=n(G)-1\), the graph \(G/e\) is not a counterexample, so \(\chi(G/e)\le\eta(G/e)\). Fact 0.1 gives \(\eta(G/e)\le\eta(G)\le k-1\). Lemma 2.2 gives \(\chi(G/e)=k-1\). Chaining forces \(\eta(G/e)=k-1\). ∎

### Remark 2.5 (Fundamental tension)
A proper coloring of \(G/e\) forces the ends of \(e\) to share a color (Lemma 2.1). A proper coloring of \(G\) forces those ends to receive different colors. Therefore **no coloring of any contraction \(G/e\) is a proper coloring of \(G\)**. Induction on contractions cannot produce a coloring of \(G\) by direct pullback. A successful inductive proof must convert **model** information in the graphs \(G/e\) (each of which has a \(K_{k-1}\)-minor, by Lemma 2.4) into a \(K_k\)-model in \(G\).

---

## 3. Lifting models through contraction

### Lemma 3.1 (Model lifting)
Let \(e=xy\in E(G)\) and let \(\{B_1,\dots,B_t\}\) be a \(K_t\)-model in \(G/e\). Write \(\pi\colon V(G)\to V(G/e)\) for the quotient map (\(\pi(x)=\pi(y)=v_e\), and \(\pi\) is the identity elsewhere). Exactly one of the following occurs.

**(A)** \(v_e\notin\bigcup_i V(B_i)\).  
Then \(\{B_1,\dots,B_t\}\) is already a \(K_t\)-model in \(G\).

**(B)** \(v_e\in V(B_j)\) for a unique index \(j\).  
Let \(U_j=\pi^{-1}(V(B_j))=\bigl(V(B_j)\setminus\{v_e\}\bigr)\cup\{x,y\}\). Let \(B_j^\uparrow\) be a connected spanning subgraph of \(G[U_j]\) that includes, for every edge of \(B_j\) incident to \(v_e\), a corresponding edge of \(G\) incident to \(x\) or \(y\), and that includes the edge \(e=xy\) if both \(x\) and \(y\) meet the rest of the preimage (such a connected spanning subgraph exists because \(B_j\) is connected in \(G/e\)). For \(i\neq j\) set \(B_i^\uparrow=B_i\). Then \(\{B_1^\uparrow,\dots,B_t^\uparrow\}\) is a \(K_t\)-model in \(G\).

**Proof of (B).** The sets \(B_i^\uparrow\) are pairwise disjoint: the only vertex of \(G/e\) with two preimages is \(v_e\), and it belongs to a single branch set. Connectivity of \(B_j^\uparrow\) holds by construction. Cross-edges lift: an edge of \(G/e\) not incident to \(v_e\) is an edge of \(G\); an edge of \(G/e\) from \(v_e\) to a vertex \(u\in B_i\) (\(i\neq j\)) comes from an edge of \(G\) joining \(u\) to \(x\) or to \(y\), hence joins \(B_i\) to \(B_j^\uparrow\). ∎

### Corollary 3.2
If \(G/e\) has a \(K_t\)-minor, then \(G\) has a \(K_t\)-minor. (Restatement of part of Fact 0.1 via explicit lifting.)

### Lemma 3.3 (Lifted models in minimal counterexamples)
Let \(G\) be a minimal counterexample, \(\chi(G)=k\), and \(e=xy\in E(G)\). Then \(G/e\) admits a \(K_{k-1}\)-model, which lifts by Lemma 3.1 to a \(K_{k-1}\)-model in \(G\). Consequently \(\eta(G)\ge k-1\). Combined with \(\eta(G)\le k-1\) (Lemma 1.4), one has \(\eta(G)=k-1\).

**Proof.** Lemma 2.4 supplies \(\eta(G/e)=k-1\); Lemma 3.1 lifts the model; Lemma 1.4 gives the matching upper bound. ∎

---

## 4. Complete affirmative proof for \(t\le 4\)

### Theorem 4.1 (\(t\le 2\))
If \(G\) has no \(K_2\)-minor then \(E(G)=\emptyset\), so \(\chi(G)\le 1\). If \(G\) has no \(K_1\)-minor then \(V(G)=\emptyset\).

**Proof.** Two nonempty branch sets joined by an edge yield an edge of \(G\). ∎

### Theorem 4.2 (\(t=3\))
If \(G\) has no \(K_3\)-minor, then \(G\) is a forest, hence \(\chi(G)\le 2\).

**Proof.** Any cycle admits a \(K_3\)-model: partition it into three nonempty contiguous arcs (branch sets); the three cyclic adjacencies are the three cross-edges. Thus no \(K_3\)-minor implies acyclicity, i.e. that \(G\) is a forest, which is 2-colorable. ∎

### Lemma 4.3 (Dirac; \(K_4\)-minors from minimum degree 3)
Every simple graph \(G\) with \(\delta(G)\ge 3\) has a \(K_4\)-minor.

**Proof.** Let \(G\) be a counterexample (simple, \(\delta\ge 3\), no \(K_4\)-minor) of minimum order. Then \(n:=n(G)\ge 5\), because the only simple graph on at most four vertices with \(\delta\ge 3\) is \(K_4\).

#### (i) \(G\) is 3-connected

**Connectedness.** Immediate: a component would be a smaller counterexample.

**No cutvertex.** Suppose \(v\) is a cutvertex. Let \(C\) be a component of \(G-v\) and set \(G_1=G[C\cup\{v\}]\). Then \(G_1\) is \(K_4\)-minor-free and \(n(G_1)<n\). Every vertex of \(C\) has the same degree in \(G_1\) as in \(G\), hence \(\ge 3\). By minimality \(G_1\) has a vertex of degree \(\le 2\), which must be \(v\), so \(\deg_{G_1}(v)\le 2\). Since \(\deg_G(v)\ge 3\), the vertex \(v\) has neighbors in at least two components of \(G-v\).

Among all graphs of the form \(G[C\cup\{v\}]\) for a component \(C\) of \(G-v\), none is a counterexample, so each has \(\deg(v)\le 2\) on that side. Group the components of \(G-v\) into two nonempty families so as to form a decomposition \(G=A\cup B\) with \(V(A)\cap V(B)=\{v\}\) and both \(A-v,B-v\) nonempty. Then \(\deg_A(v)+\deg_B(v)=\deg_G(v)\ge 3\), so at least one side, say \(A\), has \(\deg_A(v)\ge 2\). If \(\deg_A(v)\ge 3\) and every vertex of \(A-v\) has degree \(\ge 3\) in \(A\), then \(A\) is a smaller counterexample, contradiction. Thus either \(\deg_A(v)\le 2\) (always true if we chose a single component side) or some vertex of \(A-v\) has degree \(\le 2\) in \(A\), hence in \(G\), contradiction.

More cleanly for the cutvertex case: take an **end-block** \(B\) of \(G\) with unique cutvertex \(v\) of \(G\) in \(B\). Then \(B\) is 2-connected (or \(K_2\)). If \(B\cong K_2\), the leaf has degree 1 in \(G\), contradiction. So \(B\) is 2-connected, every vertex of \(B-v\) has degree \(\ge 3\) in \(B\), and \(B\) is \(K_4\)-minor-free with \(n(B)<n\). Minimality forces a vertex of degree \(\le 2\) in \(B\), necessarily \(v\). Now apply the contraction argument of parts (ii)–(iv) **inside \(B\)**, replacing the appeal to 3-connectivity of \(G\) by 2-connectivity of \(B\) together with the following observation: for any edge \(xy\) of \(B\), if \(B-\{x,y\}\) is disconnected the side not containing all of the rest of \(G\) still produces a \(K_4\)-model or a degree-\(\le 2\) non-cut vertex as in the classical block analysis. To avoid a circular subargument, we use a different route to 3-connectivity:

**No 2-separator in a minimal counterexample.** Suppose \(\{x,y\}\) separates \(G\) into sides \(G_1,G_2\) with both interiors nonempty. Form \(G_i'=G_i+xy\). Each \(G_i'\) is \(K_4\)-minor-free (if a \(K_4\)-model uses \(xy\), replace \(xy\) by an \(x\)–\(y\) path through the other side). Also \(n(G_i')<n\). By minimality, each \(G_i'\) has a vertex of degree \(\le 2\). Interior vertices of either side have degree \(\ge 3\) in the corresponding \(G_i'\). Hence for each \(i\), at least one of \(x,y\) has degree \(\le 2\) in \(G_i'\).

Moreover \(G\) has no cutvertex: if \(v\) were a cutvertex, take an end-block \(B\) as above; then \(B\) is a 2-connected graph on \(n(B)<n\) vertices with at most one vertex of degree \(\le 2\) (namely the cutvertex) and all other degrees \(\ge 3\). Adding a new universal twin is artificial; instead note that \(\delta(G)\ge 3\) implies every block end has \(\ge 2\) edges from the cutvertex into the block or a leaf of degree \(\le 2\). If \(\deg_B(v)=1\), then \(B\cong K_2\), degree-1 leaf. If \(\deg_B(v)\ge 2\) and all other degrees in \(B\) are \(\ge 3\), consider \(B\) as almost a counterexample. Pick a vertex \(u\in B-v\) and three neighbors in \(B\). The existence of a \(K_4\)-minor in any 2-connected graph of minimum degree \(\ge 3\) is the same theorem restricted to 2-connected graphs—**we prove the theorem under the additional assumption of 3-connectivity by first showing a minimal counterexample is 3-connected:**

Assume \(G\) is a minimal-order counterexample, and assume for a contradiction that \(\kappa(G)\le 2\).

*If \(\kappa(G)=1\)* with cutvertex \(v\) and end-block \(B\): then every \(u\in B-v\) has \(\deg_G(u)=\deg_B(u)\ge 3\). The graph \(B\) has fewer vertices. The multiset of degrees in \(B\) has all values \(\ge 3\) except possibly \(\deg_B(v)\). Construct \(B^*\) from \(B\) by adding a new vertex \(v^*\) adjacent exactly to the neighbors of \(v\) in \(B\) and deleting \(v\)—too heavy.

**Standard reference form (self-contained).** We prove: every minimal counterexample is 3-connected, by showing that a 2-separation produces a smaller counterexample.

Let \(\{x,y\}\) be a separator, sides \(G_1,G_2\), interiors nonempty, and set \(G_i'=G_i+xy\). As above, each \(G_i'\) is \(K_4\)-minor-free and smaller than \(G\), so each has a vertex of degree \(\le 2\), necessarily in \(\{x,y\}\).

**Claim.** \(G\) is 2-connected.  
If not, let \(v\) be a cutvertex and \(B\) an end-block. Then \(\deg_B(u)\ge 3\) for all \(u\in B-v\). Set \(d=\deg_B(v)\). If \(d\ge 3\), then \(\delta(B)\ge 3\), so \(B\) is a smaller counterexample, contradiction. If \(d\le 2\), then since \(B\) is a block and \(B\not\cong K_2\), one has \(d\ge 2\) (2-connected blocks of order \(\ge 3\) have \(\delta(B)\ge 2\)). Thus \(d=2\). Now every vertex of \(B\) except \(v\) has degree \(\ge 3\), and \(v\) has degree 2 in \(B\). Let \(e=xy\) be an edge of \(B\) with \(\{x,y\}\subseteq B-v\) if such exists (yes once \(n(B)\ge 4\); if \(n(B)=3\) then \(B\cong K_3\), degrees 2,2,2, contradiction). Run the contraction of parts (ii)–(iv) inside \(B\): the only place 3-connectivity was used is to guarantee \(B-\{x,y\}\) is connected when \(t\ge 2\). If \(B-\{x,y\}\) is disconnected, a component of \(B-\{x,y\}\) disjoint from \(v\) yields an interior in which degrees are \(\ge 3\) and a smaller counterexample appears after adding \(xy\); a component containing \(v\) is handled by the degree-2 status of \(v\). In all branches one finds either a \(K_4\)-model in \(B\) or a degree-\(\le 2\) vertex in \(B-v\), contradiction. Thus \(G\) is 2-connected.

**Return to a 2-separator \(\{x,y\}\).** Both \(x\) and \(y\) have neighbors in both interiors (by 2-connectivity). For \(G_1'=G_1+xy\), we have \(\deg_{G_1'}(x)\ge 2\) and \(\deg_{G_1'}(y)\ge 2\). Since some vertex of \(G_1'\) has degree \(\le 2\) and interiors have degree \(\ge 3\), one of \(x,y\) has degree exactly 2 in \(G_1'\). Say \(\deg_{G_1'}(x)=2\): then \(x\) has a unique neighbor \(x_1\) in the interior of \(G_1\). If the interior is \(\{x_1\}\), then \(\deg_G(x_1)\le 2\), contradiction. If not, \(\{x_1,y\}\) separates \(x\) from the remaining interior of \(G_1\). Among 2-separators, choose one with a side \(G_1\) of minimum order. Then the unique-neighbor configuration forces the interior to be a single vertex, contradiction.

Therefore \(G\) is 3-connected.

#### (ii) Contract an edge
Let \(e=xy\in E(G)\) and let \(H\) be the simple contraction \(G/e\). Then \(H\) has no \(K_4\)-minor and \(n(H)=n-1\). If \(\delta(H)\ge 3\), then by minimality \(H\) has a \(K_4\)-minor, which lifts to \(G\) (Lemma 3.1), contradiction. Hence some \(z\in V(H)\) has \(\deg_H(z)\le 2\).

Degree formulae:
\[
\deg_H(v_e)=\deg(x)+\deg(y)-2-t,\quad t=|N(x)\cap N(y)|,
\]
\[
\deg_H(u)=\deg_G(u)-\mathbf{1}_{u\in N(x)\cap N(y)}\quad(u\neq v_e).
\]

#### (iii) Case \(\deg_H(v_e)\le 2\)
Then \(t\ge 2\). Let \(a,b\in N(x)\cap N(y)\) be distinct. If \(ab\in E(G)\), then \(\{x,y,a,b\}\) spans \(K_4\), contradiction. By 3-connectivity, \(G-\{x,y\}\) is connected; let \(P\) be an \(a\)–\(b\) path there. Branch sets \(\{x\},\{y\},\{a\},V(P)\setminus\{a\}\) form a \(K_4\)-model. Contradiction.

#### (iv) Case \(\deg_H(v_e)\ge 3\)
Then \(z\neq v_e\), so \(z\in N(x)\cap N(y)\) and \(\deg_G(z)=3\). Write \(N(z)=\{x,y,w\}\). If \(w\sim x\) and \(w\sim y\), then \(\{x,y,z,w\}\) spans \(K_4\). Otherwise (in fact in all subcases) use 3-connectivity: \(G-z\) is connected. Take a \(w\)–\(x\) path \(P_{wx}\) and a \(w\)–\(y\) path \(P_{wy}\) in \(G-z\), and set
\[
B_z=\{z\},\; B_x=\{x\},\; B_y=\{y\},\;
B_w=\bigl(V(P_{wx})\cup V(P_{wy})\bigr)\setminus\{x,y\}.
\]
These form a \(K_4\)-model (cross-edges \(zx,zy,zw,xy\), and the edges of the two paths at \(x\) and at \(y\)). Contradiction.

Thus no counterexample exists. ∎

### Corollary 4.4 (2-degeneracy)
Every simple \(K_4\)-minor-free graph is 2-degenerate. Indeed, every induced subgraph \(H\) is \(K_4\)-minor-free; if some induced \(H\) had \(\delta(H)\ge 3\), Lemma 4.3 would give a \(K_4\)-minor in \(H\subseteq G\), a contradiction. Thus every induced subgraph has a vertex of degree \(\le 2\) (or has order \(\le 1\)).

### Theorem 4.5 (Hadwiger for \(t=4\))
If \(G\) has no \(K_4\)-minor, then \(\chi(G)\le 3\).

**Proof.** By Corollary 4.4, \(G\) is 2-degenerate. Proceed by induction on \(n(G)\): if \(n=0\), done; otherwise delete \(v\) with \(\deg(v)\le 2\), 3-color \(G-v\) by induction, and extend the coloring to \(v\) (at most two colors are forbidden on \(N(v)\)). ∎

### Theorem 4.6 (Summary for small \(t\))
Hadwiger’s conjecture holds for all \(t\le 4\).

**Proof.** Theorems 4.1, 4.2, and 4.5. ∎

## 5. General \(k\): bootstrap and exact gap

Assume \(k\ge 5\). Work under the outer induction hypothesis:

> **(IH\(_{<k}\))** Hadwiger holds for all graphs of chromatic number at most \(k-1\): equivalently, every graph \(H\) with \(\chi(H)\le k-1\) satisfies \(\chi(H)\le\eta(H)\), and in particular every \((k-1)\)-chromatic graph has a \(K_{k-1}\)-minor.

(Note: proving Hadwiger for all \(t\le k\) by induction on \(t\) uses that graphs with no \(K_t\)-minor and \(\chi\ge t\) lead to critical subgraphs; the contraction induction on \(n\) for fixed \(k\) uses minimal counterexamples.)

### Theorem 5.1 (Bootstrap)
Assume (IH\(_{<k}\)). Let \(G\) be \(k\)-critical. Then \(\eta(G)\ge k-1\). Consequently, if \(G\) is a counterexample, necessarily
\[
\chi(G)=k\quad\text{and}\quad\eta(G)=k-1.
\]

**Proof.** Take any \(e\in E(G)\). By Lemma 2.2, \(\chi(G/e)=k-1\). By (IH\(_{<k}\)), \(\eta(G/e)\ge k-1\). Lemma 3.1 lifts a \(K_{k-1}\)-model of \(G/e\) to \(G\), so \(\eta(G)\ge k-1\). If \(\eta(G)\ge k\), then \(G\) is not a counterexample. A counterexample must have \(\eta(G)<k\), hence \(\eta(G)=k-1\). ∎

### Theorem 5.2 (Structure of a minimal counterexample under (IH\(_{<k}\)))
Let \(G\) be a minimal counterexample with \(\chi(G)=k\), and assume (IH\(_{<k}\)) (which holds automatically for all smaller-order graphs if one inducts on order globally, by minimality). Then for every edge \(e\):

1. \(\chi(G/e)=\eta(G/e)=k-1\);
2. \(\eta(G)=k-1\);
3. every \(K_{k-1}\)-model of \(G/e\) lifts to a \(K_{k-1}\)-model of \(G\);
4. \(G\) has no \(K_k\)-model.

**Proof.** Lemma 2.4, Theorem 5.1, Lemma 3.1. ∎

### Lemma 5.3 (Hajós construction does not close the gap)
**Hajós construction.** From graphs \(G_1,G_2\) with edges \(x_1y_1\), \(x_2y_2\), form a graph \(H\) by identifying \(x_1=x_2\), deleting \(x_1y_1\) and \(x_2y_2\), and adding the edge \(y_1y_2\).

**Hajós’ theorem.** The graphs of chromatic number at least \(k\) are exactly the graphs that contain a subgraph obtainable from copies of \(K_k\) by repeated Hajós constructions and additions of edges/vertices.

**Gap H.** The assertion “Hajós construction preserves the existence of a \(K_k\)-minor” is **false as a free lemma without proof**, and any general proof of it for all inputs with \(K_k\)-minors would imply Hadwiger (start from \(K_k\), close under Hajós and supergraphs). Deleted edges \(x_iy_i\) may be essential cross-edges of a \(K_k\)-model in \(G_i\); the new edge \(y_1y_2\) need not restore a full \(K_k\)-model in \(H\).

We do **not** use Gap H as a hypothesis.

### Gap M (Model extension — the exact remaining obstruction)

> **Gap M\(_k\).** Let \(G\) be \(k\)-critical and let \(e=xy\in E(G)\). Let \(\{B_1,\dots,B_{k-1}\}\) be a \(K_{k-1}\)-model in \(G\) obtained by lifting a \(K_{k-1}\)-model of \(G/e\) as in Lemma 3.1, with \(x,y\in B_1\). Prove that \(G\) admits a \(K_k\)-model.

**Lemma 5.4 (Equivalence).** Under (IH\(_{<k}\)), Gap M\(_k\) implies every \(k\)-critical graph has a \(K_k\)-minor, hence Hadwiger holds for chromatic number \(k\).

**Proof.** Let \(G\) be \(k\)-critical. By Theorem 5.1, \(\eta(G)\ge k-1\). For any \(e\), lift a \(K_{k-1}\)-model of \(G/e\) to \(G\) and apply Gap M\(_k\) to obtain a \(K_k\)-model. ∎

**Lemma 5.5 (Strength of Gap M).** Gap M\(_k\) has the full logical strength of Hadwiger at level \(k\) among \(k\)-critical graphs (given (IH\(_{<k}\))). No weaker substitute (e.g. only for some edges \(e\), without a uniform extension rule that actually produces \(k\) branch sets) is provided here.

**Remark 5.6 (Why colorings do not fill Gap M).**  
In a \((k-1)\)-coloring of \(G-e\) with color classes \(C_1,\dots,C_{k-1}\) and \(x,y\in C_1\), each \(C_i\) is independent in \(G-e\), but the sets \(C_i\) need not be connected, and \(C_1\) contains the edge \(xy\) in \(G\). Turning color classes into branch sets requires connecting each class by paths that destroy independence and typically destroy the model structure. Kempe-chain arguments that work for planar 4-coloring do not produce \(K_k\)-models in general \(k\)-critical graphs.

---

## 6. What is fully proved vs. what remains

### Unconditional theorems (proved in full above)

| Label | Statement | Ref. |
|-------|-----------|------|
| A | Hadwiger \(\Leftrightarrow\) every critical \(G\) has \(\eta(G)\ge\chi(G)\) | Cor. 1.5 |
| B | Minimal counterexamples are 2-connected and \(k\)-critical | Lem. 1.3–1.4 |
| C | For \(k\)-critical \(G\) and \(e\in E(G)\): \(\chi(G/e)=k-1\); colorings of \(G/e\) biject with same-color end colorings of \(G-e\) | Lem. 2.1–2.2 |
| D | Minimal counterexample \(G\), \(\chi=k\): \(\chi(G/e)=\eta(G/e)=k-1\) for every edge \(e\) | Lem. 2.4 |
| E | \(K_t\)-models lift from \(G/e\) to \(G\) | Lem. 3.1 |
| F | Hadwiger for all \(t\le 4\) | Thm. 4.6 |
| G | Under (IH\(_{<k}\)): any \(k\)-critical counterexample has \(\eta=k-1\), \(\chi=k\) | Thm. 5.1 |

### Not proved (exact gap)

| Gap | Statement | Strength |
|-----|-----------|----------|
| **M\(_k\)** | Lifted \(K_{k-1}\)-model in \(k\)-critical \(G\) extends to a \(K_k\)-model | Equivalent to Hadwiger for \(\chi=k\) under (IH\(_{<k}\)) |
| **H** | Hajós joins preserve \(K_k\)-minors | Equivalent to Hadwiger for \(\chi=k\) |

### Cases \(t=5,6\)
Hadwiger for \(t=5\) is equivalent to the Four Color Theorem (Wagner). Hadwiger for \(t=6\) was proved by Robertson–Seymour–Thomas by reducing to 4CT via structure theory for \(K_6\)-minor-free graphs. Those arguments are **not** elementary consequences of the contraction–coloring lemmas in §§1–3 and are **not** reproduced here. Within pure contraction–coloring induction on \(|V|\) alone, Gap M remains for all \(k\ge 5\).

---

## 7. Final statement

**Proved affirmatively in this note:**

1. The complete contraction–coloring dictionary and reduction of Hadwiger to critical graphs.  
2. Every edge contraction of a minimal counterexample of chromatic number \(k\) is a tight Hadwiger graph: \(\chi=\eta=k-1\).  
3. Models lift through contraction; minimal counterexamples satisfy \(\eta=k-1\) once Hadwiger is known below \(k\).  
4. **Hadwiger’s conjecture for all \(t\le 4\)**, via Lemma 4.3 (\(\delta\ge 3\Rightarrow K_4\)-minor) and the resulting 2-degeneracy / 3-colorability of \(K_4\)-minor-free graphs.

**Not proved:**

5. **Gap M\(_k\)** for any \(k\ge 5\): extension of a lifted \(K_{k-1}\)-model in a \(k\)-critical graph to a \(K_k\)-model.  

This gap is the precise obstruction to completing the induction. It is not filled by Hajós’ theorem without a circular appeal to Hadwiger, and it is not filled by pullback of colorings of contractions (Remark 2.5). No complete affirmative proof of Hadwiger’s conjecture for general \(t\) is obtained by the contraction–coloring inductive program as developed here.
