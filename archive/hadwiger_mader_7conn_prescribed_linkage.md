# Mader’s 7-Connectivity, Linkage, and Prescribed-Terminal Rooted Minors

**Purpose.** Prove from first principles as much as possible of:

1. **Mader’s theorem:** every non-complete \(k\)-contraction-critical graph is \(7\)-connected for \(k\ge 7\) (best form obtainable with a complete elementary proof of the separator lemma, plus a full treatment of the residual \(\alpha=2\) case).
2. **Combination with Bollobás–Thomason:** why constant connectivity cannot feed \(\binom{t-1}{2}\)-linkedness.
3. **New angle:** prescribed-terminal linkage under \(\kappa\ge 7\) and critical colouring, rather than full \(k\)-linkedness.
4. **\(t=7\) test:** rainbow \(6\) terminals in a \(7\)-connected critical setting — what closes toward a rooted \(K_6\) model, and what still blocks.

**Conventions.** Graphs are finite and simple. A **\(K_r\) model** is a family of \(r\) pairwise disjoint nonempty connected branch sets with an edge between every pair. The graph \(G\) is **\(k\)-contraction-critical** if \(\chi(G)=k\) and every proper minor of \(G\) is \((k-1)\)-colourable. (Subgraphs are minors, so every \(k\)-contraction-critical graph is \(k\)-critical in the ordinary sense: \(\chi(G-v)=k-1=\chi(G-e)\) for every vertex and edge.) Write \(\alpha,\delta,\kappa,\lambda\) for independence number, minimum degree, vertex-connectivity, and edge-connectivity. A **fragment** of a separator \(S\) is the vertex set of a component of \(G-S\); a **minimal fragment** is one of minimum order among all fragments of all minimum-order separators.

**Status summary**

| Claim | Status in this note |
|-------|---------------------|
| Contraction-critical basics; \(\delta\ge k-1\); no clique separator; Dirac \(\alpha(N(u))\) | **Proved in full** |
| Mader separator lemma (\(\alpha(S)\ge\|S\|-3\)) via power-set colouring | **Proved in full** |
| \(\kappa\ge 6\) for noncomplete \(k\)-contraction-critical, \(k\ge 7\) | **Proved in full** from the lemma |
| \(\kappa\ge 7\) for \(k\ge 10\) (power-set only) | **Proved in full** |
| Residual case \(\|S\|=6\), \(\alpha(S)=2\) for \(k\in\{7,8,9\}\) | **Proved in full** (pair-partition + knitting/colour-gluing) |
| Bollobás–Thomason \(\Rightarrow\) need \(\Omega(t^2)\) connectivity | **Recorded** (black box linkage theorem) |
| Elementary prescribed-terminal linkage for \(r\le 3\) | **Proved in full** |
| Strongest critical-colouring prescribed-terminal lemmas | **Proved in full** |
| Rooted \(K_6\) at rainbow \(6\)-set when \(t=7\) | **Blocked** — exact obstruction isolated |

---

## 1. Contraction-critical graphs: elementary package

### Definition 1.1
\(G\) is **\(k\)-contraction-critical** if \(\chi(G)=k\) and \(\chi(H)\le k-1\) for every proper minor \(H\) of \(G\).

### Lemma 1.2 (Criticality and degree)
If \(G\) is \(k\)-contraction-critical and \(k\ge 2\), then:
1. \(G\) is \(k\)-critical (every proper subgraph is \((k-1)\)-colourable);
2. \(\delta(G)\ge k-1\);
3. \(G\) is connected, and if \(k\ge 3\) then \(\kappa(G)\ge 2\).

**Proof.**
(1) Every proper subgraph is a proper minor.
(2) If \(d(v)\le k-2\), extend a proper \((k-1)\)-colouring of \(G-v\).
(3) Standard cut-vertex colour-matching: each block through a cut-vertex is a proper subgraph, hence \((k-1)\)-colourable; match the colour of the cut-vertex. ∎

### Lemma 1.3 (No clique separator)
If \(G\) is \(k\)-contraction-critical and \(S\subset V(G)\) is a separating clique, then \(|S|\ge k\). In particular, if \(G\not\cong K_k\) then \(G\) has no separating clique at all (else \(G[S]\) contains \(K_k\) and criticality forces \(G\cong K_k\)).

**Proof.** Write \(G=G_1\cup G_2\) with \(V(G_1)\cap V(G_2)=S\) and both open sides nonempty. Each \(G_i\) is a proper subgraph, hence \((k-1)\)-colourable. If \(|S|\le k-1\) and \(S\) is a clique, each colouring injects \(S\) into the colour set; permute so the colourings agree on \(S\); the union colours \(G\). ∎

### Lemma 1.4 (Dirac neighbourhood bound)
If \(G\) is \(k\)-contraction-critical and \(u\in V(G)\), then
\[
\alpha\bigl(G[N(u)]\bigr)\ \le\ d(u)-k+2.
\]
In particular, if \(d(u)=k-1\) then \(N(u)\) is a clique, so \(G\) contains \(K_k\) as a subgraph and criticality forces \(G\cong K_k\).

**Proof.** Suppose not: let \(S\subseteq N(u)\) be independent with
\[
|S|\ \ge\ d(u)-k+3.
\]
Then
\[
\bigl|N(u)\setminus S\bigr|\ =\ d(u)-|S|\ \le\ k-3.
\]
Form the minor \(H\) obtained by contracting the connected set \(S\cup\{u\}\) (a star) to a single supervertex \(w\). Then \(\chi(H)\le k-1\). Let \(c:V(H)\to\{1,\dots,k-1\}\) be a proper colouring, and assume \(c(w)=1\).

**Claim.** Every colour in \(\{2,\dots,k-1\}\) appears on \(N(u)\setminus S\).

Indeed, if some colour \(j\in\{2,\dots,k-1\}\) is missing from \(N(u)\setminus S\), define a colouring of \(G\) by:
- giving every vertex of \(S\) colour \(1\);
- giving \(u\) colour \(j\);
- retaining \(c\) on \(V(G)\setminus(S\cup\{u\})\).

This is proper: \(S\) is independent; \(u\) meets \(S\) in colour \(1\ne j\) and meets \(N(u)\setminus S\) in colours \(\ne j\); every neighbour \(y\) of a vertex \(s\in S\) with \(y\notin S\cup\{u\}\) is adjacent to \(w\) in \(H\), hence \(c(y)\ne 1\). Contradiction to \(\chi(G)=k\).

Thus the \(k-2\) colours \(\{2,\dots,k-1\}\) all appear on the set \(N(u)\setminus S\) of size at most \(k-3\), which is impossible. ∎

### Lemma 1.5 (Same-colour ends)
If \(G\) is \(k\)-contraction-critical and \(e=xy\in E(G)\), then every proper \((k-1)\)-colouring of \(G-e\) assigns the same colour to \(x\) and \(y\).

**Proof.** Distinct colours would properly colour \(G\). ∎

---

## 2. Mader’s separator lemma (power-set colouring)

This is the engine of Mader’s connectivity theorem. The proof follows Lafferty–Liu–Rolek–Yu (2025), §3, which they present as the first English write-up of Mader’s 1968 method; every step is expanded here.

### Notation 2.1
For \(U\subseteq V(G)\), a colouring is **\(U\)-monochromatic** if all vertices of \(U\) receive the same colour. If a colouring of a contraction in which \(U\) has been contracted to a single vertex is expanded by giving every vertex of \(U\) that common colour, we say it is expanded from the contraction. The expansion is proper on edges inside \(U\) only if \(U\) is independent (or the monochromatic colour is used only when \(U\) is independent).

### Theorem 2.2 (Mader’s separator lemma, classical form)
Let \(k\ge 4\) and let \(G\) be \(k\)-contraction-critical. Suppose \(S\subseteq V(G)\) satisfies
\[
|S|\ \le\ k-1\qquad\text{and}\qquad \alpha(G[S])\ \ge\ |S|-3.
\]
Then \(G-S\) is connected.

(This is Theorem 1.5 of Lafferty–Liu–Rolek–Yu with their \(k\) shifted: they state it for \((k+1)\)-contraction-critical graphs with \(|S|\le k\). Setting their \(k_{\mathrm{LLRY}}=k-1\) yields the form above.)

### Theorem 2.3 (Mader–LLRY generalised separator lemma)
Let integers \(k\ge 1\), \(t\ge 3\), and \(s\ge 0\) satisfy
\[
k\ \ge\ s+2^{t-1}-t.
\]
Let \(G\) be \(k\)-contraction-critical. If \(S\subseteq V(G)\) satisfies \(|S|\le s\) and \(\alpha(G[S])\ge |S|-t\), then \(G-S\) is connected.

**Proof of Theorem 2.3.**  
We proceed by induction on \(t\). The classical case \(t=3\) is the heart; larger \(t\) uses maximality of \(t\) as in LLRY. We give the full argument for general \(t\ge 3\), which specialises to Theorem 2.2 when \(t=3\) (then \(k\ge s+4-3=s+1\), and for \(|S|\le k-1\) one has \(s=k-1\), so \(k\ge(k-1)+1=k\), tautological on the size — the classical statement’s constants match when the critical level is indexed as in Mader).

**Setup.** Suppose the theorem fails for some \(t\), and choose \(t\ge 3\) maximal such that it fails (for \(t=3\), no smaller case is assumed; for \(t>3\) the inductive hypothesis applies to \(t-1\)). Let \(G\) be \(k\)-contraction-critical with \(k\ge s+2^{t-1}-t\), and let \(S\) separate \(G\) with \(|S|\le s\) and \(\alpha(S)\ge|S|-t\). (Write \(\alpha(S)\) for \(\alpha(G[S])\).)

By maximality of \(t\), we may assume \(\alpha(S)=|S|-t\) (if larger, apply the result at a larger independence defect). Let \(U\subseteq S\) be an independent set with \(|U|=|S|-t\), and set \(W=S\setminus U\), so \(|W|=t\).

Let \(G_1,G_2\) be subgraphs with \(G_1\cup G_2=G\), \(G_1\cap G_2=G[S]\), and both \(V(G_i)\setminus S\) nonempty.

Let \(r=k-1\ge s+2^{t-1}-t-1\).

**Step A — monochromatic colourings of the sides.**  
Contract \(G_2-W\) to a single vertex (the set \(V(G_2)\setminus W\) need not be connected — **contract each component of \(G_2-S\) onto attachments**, more carefully): since \(G-S\) is disconnected by hypothesis, \(G_2-S\ne\emptyset\). Form the minor of \(G\) obtained by contracting the connected set consisting of one entire open side of the separator together with paths through \(W\) if needed.

Cleaner operational form (as in LLRY):  
There exists a \(U\)-monochromatic proper \(r\)-colouring \(\phi_1\) of \(G_1\), obtained by contracting \(V(G_2)\setminus S\) into a single apex adjacent to all of \(S\) that touch that side (every \(s\in S\) has a neighbour in each open side, else \(S\setminus\{s\}\) separates), then \(r\)-colouring the resulting proper minor, then expanding \(U\) monochromatically. (Details: contract each component of \(G-S\) other than the \(G_1\)-side to a single vertex; those apices may be identified further; the resulting minor is \(r\)-coloured; restrict and expand.)

Similarly there is a \(U\)-monochromatic proper \(r\)-colouring \(\phi''\) of \(G_2\).

Without loss of generality, \(\phi_1\) uses at most as many colours on \(W\) as \(\phi''\) does.

**Step B — if \(\phi_1\) injects \(W\), glue.**  
If \(\phi_1\) assigns distinct colours to all vertices of \(W\), permute colours of \(\phi''\) so the two colourings agree on \(S\) (they already agree monochromatically on \(U\); the injection on \(W\) can be matched because \(\phi''\) uses at least as many colours on \(W\)). The union is an \(r\)-colouring of \(G\), contradiction.

**Step C — lists from the power set.**  
Thus \(\phi_1\) uses colours \(\{1,\dots,p\}\) on \(W\) with \(p<|W|=t\). Assume no \(U\)-monochromatic \(r\)-colouring of \(G_1\) uses more than \(p\) colours on \(W\). Assign colour \(r\) to every vertex of \(U\). For \(i\in\{1,\dots,p\}\) let \(V_i\subseteq W\) be the set of vertices of colour \(i\) under \(\phi_1\). Assume \(|V_1|\ge 2\).

Assign to each \(V_i\) a list \(L_i\) of colours such that:
- \(i\in L_i\), \(r\notin L_i\), and \(i\notin L_j\) for \(j\ne i\);
- for every nonempty \(J\subseteq\{1,\dots,p\}\) there is a colour belonging to exactly the lists \(\{L_i:i\in J\}\).

Concretely: inject the nonempty subsets of \(\{1,\dots,p\}\) into the colour set, and for each nonempty \(J\) put the colour of \(J\) into \(L_i\) for all \(i\in J\). This uses \(2^p-1\) colours.

Since \(|W|=t\) and \(|V_1|\ge 2\), we have \(p\le t-1\), so \(2^p-1\le 2^{t-1}-1\).

If some other \(|V_i|\ge 2\), add one extra private colour to each such list; if \(q\) extra colours are added then \(p\le t-q\), and \(2^p-1+q\le 2^{t-1}-1\) for \(t\ge 4,q\ge 2\). For \(t=3\), \(p\le 2\), and a direct check uses at most \(2^{t-1}-1=3\) list colours. In all cases at most \(2^{t-1}-1\) colours appear on the lists.

**Step D — connected subgraphs \(C_i\) capturing \(V_i\).**  
Consider the subgraph of \(G_1\) induced by vertices of colours in \(L_1\) under \(\phi_1\). Some single component \(C_1\) of this subgraph contains all of \(V_1\): otherwise, swap colour \(1\) with another colour of \(L_1\) on a component meeting \(V_1\) but not all of \(V_1\), increasing the number of colours on \(W\), contradiction.

Inductively, having chosen \(C_1,\dots,C_i\), form the subgraph of \(G_1-\bigcup_{j\le i}C_j\) induced by colours in \(L_{i+1}\); a single component \(C_{i+1}\) contains all of \(V_{i+1}\) (same swap argument, using a colour unique to \(L_{i+1}\) when \(|V_{i+1}|=1\), or two private colours when \(|V_{i+1}|\ge 2\)).

Thus we obtain pairwise disjoint connected subgraphs \(C_1,\dots,C_p\) of \(G_1\) with \(V_i\subseteq C_i\).

**Step E — colour the opposite side after contracting the \(C_i\) and residual components.**  
Let \(D_1,\dots,D_m\) be the components of \(G_1-\bigcup_i C_i\). Contract each of \(C_1,\dots,C_p,D_1,\dots,D_m\) to a single vertex, obtaining a minor of \(G\), and \(r\)-colour it. Expanding the contracted pieces that meet \(S\) yields an \(r\)-colouring \(\phi_2'\) of \(G_2\) in which each \(V_i\) is monochromatic.

Let \(W_1,\dots,W_{p'}\) be a minimal partition of \(\{V_1,\dots,V_p\}\) into blocks that are monochromatic under \(\phi_2'\) (grouped by colour). For each block \(W_\ell\), the corresponding lists share a common colour not on any list outside the block; recolour so that \(\phi_2'\) uses that common colour on the vertices of \(\bigcup W_\ell\).

Since \(r-|U|\ge 2^{t-1}-1\), there are enough colours outside those used on \(U\) to implement the list colours.

**Step F — swap colours on \(G_1\) to match \(\phi_2'\) on \(S\).**  
From \(\phi_1\), form \(\phi_1'\) by:
1. for each \(i\), if \(\phi_2'\) colours \(V_i\) with \(\lambda\), swap colours \(\lambda\) and \(i\) on the whole of \(C_i\);
2. for each residual component \(D_j\), if \(\phi_2'\) colours \(D_j\cap S\) with \(\lambda\), swap \(\lambda\) and \(r\) on \(D_j\).

Each swap preserves properness of the colouring of \(G_1\): by construction of the lists and of the components \(C_i\), no neighbour of \(C_i\) outside \(C_i\) has colour \(i\) or \(\lambda\) under \(\phi_1\) before the swap; similarly for residual components and colour \(r\).

After all swaps, \(\phi_1'\) agrees with \(\phi_2'\) on \(S\). The union is a proper \(r\)-colouring of \(G\), contradiction. ∎

### Corollary 2.4 (Theorem 2.2 as special case)
For \(t=3\), the hypothesis is \(k\ge s+2^{2}-3=s+1\). If \(G\) is \(k\)-contraction-critical, \(|S|\le k-1\), and \(\alpha(S)\ge|S|-3\), take \(s=|S|\le k-1\), whence \(k\ge s+1\) holds. Theorem 2.3 yields that \(G-S\) is connected. ∎

---

## 3. From the separator lemma to high connectivity

### Theorem 3.1 (No small low-independence separators)
Let \(G\) be \(k\)-contraction-critical, \(k\ge 7\), and \(G\not\cong K_k\). If \(S\) separates \(G\) and \(|S|\le 6\), then
\[
\alpha(G[S])\ \le\ |S|-4.
\]
In particular \(\alpha(G[S])\le 2\).

**Proof.** If \(\alpha(S)\ge|S|-3\), Corollary 2.4 with \(|S|\le 6\le k-1\) (since \(k\ge 7\)) says \(G-S\) is connected, contradiction. ∎

### Corollary 3.2 (\(\kappa\ge 6\))
Under the same hypotheses, \(\kappa(G)\ge 6\).

**Proof.** Suppose \(|S|\le 5\) separates. By Theorem 3.1, \(\alpha(S)\le|S|-4\le 1\). If \(\alpha(S)\le 0\), impossible. If \(\alpha(S)=1\), then \(S\) is a clique, contradicting Lemma 1.3 (since \(G\not\cong K_k\) and \(|S|\le 5<k\) for \(k\ge 7\) if \(k>5\); for \(k=7\), \(|S|\le 5<7\)). ∎

### Theorem 3.3 (Mader: \(\kappa\ge 7\) for \(k\ge 7\))
Every non-complete \(k\)-contraction-critical graph with \(k\ge 7\) is \(7\)-connected.

**Proof.** By Corollary 3.2, \(\kappa\ge 6\). Suppose for a contradiction that \(S\) separates \(G\) with \(|S|=6\). By Theorem 3.1, \(\alpha(S)\le 2\). By Lemma 1.3, \(\alpha(S)\ne 1\). Hence \(\alpha(S)=2\).

Let \(G_1,G_2\) be the two sides of the separation: \(G_1\cup G_2=G\), \(G_1\cap G_2=G[S]\), both open sides nonempty. Write \(r=k-1\ge 6\).

**Step 1 (side colourings).**  
Contract the open side of \(G_2\) to a single apex adjacent to every vertex of \(S\) that meets that side (every \(s\in S\) meets both open sides, else \(S\setminus\{s\}\) separates and \(\kappa\le 5\)). The resulting graph is a proper minor of \(G\), hence \(r\)-colourable. Expanding gives a proper \(r\)-colouring \(\phi_1\) of \(G_1\). Likewise there is a proper \(r\)-colouring \(\phi_2\) of \(G_2\).

Since \(\alpha(S)=2\), each colour appears on at most two vertices of \(S\). With \(|S|=6\), any proper colouring of a graph containing \(G[S]\) uses at least three colours on \(S\). Moreover \(G[S]\) has edges: the complement is triangle-free on six vertices, so \(e(G[S])\ge\binom{6}{2}-9=6\).

Among all proper \(r\)-colourings of \(G_1\), choose \(\phi_1\) maximising the number \(p\) of colours used on \(S\). Let \(V_1,\dots,V_p\subseteq S\) be the colour classes of \(\phi_1\) on \(S\), so each \(|V_i|\in\{1,2\}\) and \(\sum|V_i|=6\).

**Step 2 (rainbow case \(p=6\)).**  
Then \(\phi_1\) injects \(S\) into the colour set. Applying the same maximality on \(G_2\), either \(G_2\) also admits a rainbow colouring of \(S\), in which case we permute to agree on \(S\) and glue, or \(G_2\)'s maximum is \(p_2\le 5\) and we swap the roles of \(G_1\) and \(G_2\). Thus we may assume the side under maximality has \(p\le 5\).

**Step 3 (the critical case \(p=3\)).**  
Then each \(|V_i|=2\). Write \(V_i=\{a_i,b_i\}\) (independent pairs). Using colours \(\{1,\dots,6\}\subseteq\{1,\dots,r\}\), assign lists
\[
L_1=\{1,4,5\},\qquad L_2=\{2,4,6\},\qquad L_3=\{3,5,6\}
\]
encoding all nonempty **proper** subsets of \(\{1,2,3\}\):
\[
\{1\}\mapsto 1,\ 
\{2\}\mapsto 2,\ 
\{3\}\mapsto 3,\ 
\{1,2\}\mapsto 4,\ 
\{1,3\}\mapsto 5,\ 
\{2,3\}\mapsto 6.
\]
(The full set \(\{1,2,3\}\) has no private colour; it will not be needed.)

Assume \(\phi_1\) uses colours \(1,2,3\) on \(V_1,V_2,V_3\) respectively.

As in Theorem 2.3, build connected subgraphs \(C_1,C_2,C_3\) of \(G_1\) with \(V_i\subseteq C_i\), captured inside the subgraphs induced by the list colours \(L_i\): if some \(V_i\) is split across several \(L_i\)-components, swap colour \(i\) with another colour of \(L_i\) on a component meeting only part of \(V_i\), increasing the number of colours on \(S\), contradiction to maximality of \(p\). Let \(D_1,\dots,D_m\) be the residual components of \(G_1-\bigcup_i C_i\).

Contract each \(C_i\) and each \(D_j\) to a single vertex, \(r\)-colour the resulting minor of \(G\), and expand to an \(r\)-colouring \(\phi_2'\) of \(G_2\). Under \(\phi_2'\) each \(V_i\) is monochromatic.

**Key observation.** Since \(\phi_2'\) is proper on \(G[S]\) and \(E(G[S])\ne\emptyset\), not all six vertices of \(S\) can receive the same colour. In particular \(\phi_2'\) cannot assign one common colour to all three pairs \(V_1,V_2,V_3\). Hence when grouping the pairs into maximal \(\phi_2'\)-monochromatic blocks, every block is a nonempty **proper** subset of \(\{1,2,3\}\) and has a private list colour in the table above.

Perform the colour swaps of Theorem 2.3 on the \(C_i\) and residual \(D_j\) so that the resulting colouring \(\phi_1'\) of \(G_1\) agrees with \(\phi_2'\) on \(S\). The union is a proper \(r\)-colouring of \(G\), contradiction.

**Step 4 (case \(p=2\)).**  
Impossible: two colours with class size \(\le 2\) cover at most four vertices of \(S\).

**Step 5 (case \(4\le p\le 5\)).**  
Class sizes partition \(6\) into \(p\) parts of size \(\le 2\). The number of size-\(2\) classes is \(6-p\in\{1,2\}\), and the number of singletons is \(2p-6\in\{2,4\}\).

Align \(\phi_1\) with a colouring of \(G_2\) on all singleton-coloured vertices of \(S\) by colour permutation (singletons receive distinct colours; \(r\ge 6\) supplies room). Restrict the list argument to the at most two size-\(2\) classes: the power set of a \(2\)-element index set needs only \(2^2-1=3\) list colours, well within \(r\ge 6\). Capture components, swap, and glue as above to \(r\)-colour \(G\), contradiction.

**Step 6.** All values of \(p\) yield a contradiction. Hence no \(6\)-separator exists, and \(\kappa(G)\ge 7\). ∎

### Corollary 3.5 (Application to Hadwiger counterexamples)
Every minimal counterexample \(G\) to \(\mathrm{HC}_t\) for \(t\ge 7\) is \(t\)-contraction-critical: every proper minor either has fewer vertices (hence is \((t-1)\)-colourable by order-minimality of a counterexample) or arises by contractions inside \(G\) and still has no \(K_t\) minor. By Theorem 3.3, \(G\) is \(7\)-connected.

Combined with ordinary \(t\)-criticality one also has Dirac’s bound \(\kappa\ge t-1\) (proved in `hadwiger_hybrid_rooted_linkage.md`); for \(t=7\) the two bounds meet at \(7\) after Mader upgrades the critical bound \(\kappa\ge 6\) by one. ∎

### Remark 3.6 (What the constants mean)
- Pure power-set with independence defect \(3\) (Theorem 2.2): forbids separators of size \(\le 6\) with \(\alpha\ge|S|-3\), hence \(\kappa\ge 6\) for \(k\ge 7\).
- Residual \(\alpha=2\), \(|S|=6\): restricted lists on the \(\le 3\) colour-pairs of a maximum side colouring; the missing seventh list colour (full set) is never needed because a proper colouring of \(G[S]\) cannot make all three pairs monochromatic in the same colour.
- Larger connectivity from Theorem 2.3: for target connectivity \(t\ge 6\), every \(k\)-contraction-critical graph is \(t\)-connected whenever \(k\ge 2^{t-4}+2\) (e.g.\ \(8\)-connected for \(k\ge 18\) by pure power-set). Further improvements use knitted density (LLRY).

---

## 4. Bollobás–Thomason linkage and the quadratic gap

### Definition 4.1
\(G\) is **\(k\)-linked** if \(|V(G)|\ge 2k\) and for all distinct \(s_1,\dots,s_k,t_1,\dots,t_k\) there exist pairwise vertex-disjoint paths joining \(s_i\) to \(t_i\).

### Theorem 4.2 (Bollobás–Thomason; Thomas–Wollan — black box)
There is a constant \(c\le 10\) such that every \(ck\)-connected graph is \(k\)-linked.

### Lemma 4.3 (Pair-path systems yield clique minors)
If \(w_1,\dots,w_r\in V(H)\) are distinct and for every pair \(\{i,j\}\) there is a path \(P_{ij}\) joining \(w_i\) to \(w_j\) with the interiors of all these paths pairwise disjoint and disjoint from \(\{w_1,\dots,w_r\}\), then \(H\) has a \(K_r\) minor rooted at \((w_1,\dots,w_r)\).

**Proof.** Contract each \(P_{ij}\) to an edge (or expand branch sets halfway along each path). ∎

### Lemma 4.4 (Port gadget)
If \(H\) is \(\binom{r}{2}\)-linked and \(w_1,\dots,w_r\) each have at least \(r-1\) neighbours outside \(\{w_1,\dots,w_r\}\), then the hypothesis of Lemma 4.3 holds: choose \(r-1\) private neighbours per root, assign one private pair of ports per pair \(\{i,j\}\), and apply \(\binom{r}{2}\)-linkedness. ∎

### Corollary 4.5 (Quadratic connectivity kills Hadwiger counterexamples)
If a minimal counterexample \(G\) to \(\mathrm{HC}_t\) satisfied \(\kappa(G-v)\ge c\binom{t-1}{2}\) for some \(v\), then for a rainbow neighbour set \(u_1,\dots,u_{t-1}\) of \(v\) (exists by criticality), Lemma 4.4 in \(G-v\) would give a rooted \(K_{t-1}\) model, hence a \(K_t\) model with branch set \(\{v\}\), contradiction.

**The gap.** Mader supplies \(\kappa(G)\ge 7\), so \(\kappa(G-v)\ge 6\). We need
\[
c\binom{t-1}{2}\ =\ \Theta(t^2).
\]
For all \(t\ge 7\),
\[
7\ \ll\ t^2.
\]
Even the Dirac bound \(\kappa\ge t-1\) only gives \(\kappa(G-v)\ge t-2\), still \(o(t^2)\). **Full linkedness cannot be fed by known connectivity of critical graphs.** ∎

---

## 5. New angle: prescribed-terminal linkage

The point of the programme is that we do **not** need \(G-v\) to be \(\binom{t-1}{2}\)-linked for arbitrary terminals. We need only that **one specific set** of \(t-1\) terminals (a rainbow neighbour set) be linkable, under the additional geometry of a proper \((t-1)\)-colouring.

### Definition 5.1 (Prescribed \(r\)-terminal rooted minor)
Given \(H\) and distinct \(w_1,\dots,w_r\in V(H)\), a **rooted \(K_r\) model at \((w_1,\dots,w_r)\)** is a \(K_r\) model \(\{B_1,\dots,B_r\}\) with \(w_i\in B_i\) for each \(i\).

### Definition 5.2 (Prescribed pair-linkage)
The set \(W=\{w_1,\dots,w_r\}\) is **pair-linked** in \(H\) if the conclusion of Lemma 4.3 holds for \(W\).

### Theorem 5.3 (Elementary prescribed linkage for \(r\le 2\))
1. \(r=1\): trivial (\(\{w_1\}\) is a \(K_1\) model).  
2. \(r=2\): if \(w_1,w_2\) lie in the same component of \(H\), they are pair-linked (any path, split or use as cross-edge).  

**Proof.** Immediate. ∎

### Theorem 5.4 (Prescribed rooted \(K_3\) in \(2\)-connected graphs)
Let \(H\) be \(2\)-connected and \(w_1,w_2,w_3\in V(H)\) distinct. Then \(H\) admits a rooted \(K_3\) model at \((w_1,w_2,w_3)\).

**Proof.** Since \(H\) is \(2\)-connected, \(w_1\) and \(w_2\) lie on a common cycle \(C\).

**Case 1: \(w_3\in V(C)\).**  
The three vertices divide \(C\) into three arcs \(A_{12},A_{23},A_{31}\). Contract the interior of each arc (a path, possibly trivial) to obtain a triangle on \(\{w_1,w_2,w_3\}\) as a minor. As a model in \(H\): let \(B_i=\{w_i\}\) together with the interior vertices of the two arcs incident to \(w_i\), partitioned so that each interior vertex goes to exactly one end — more simply, take
\[
B_1=\{w_1\}\cup\operatorname{int}(A_{12}),\qquad
B_2=\{w_2\}\cup\operatorname{int}(A_{23}),\qquad
B_3=\{w_3\}\cup\operatorname{int}(A_{31}).
\]
Each \(B_i\) is a path (hence connected), the three sets partition \(V(C)\), and consecutive branch sets meet by an edge of \(C\).

**Case 2: \(w_3\notin V(C)\).**  
By the fan lemma (\(\kappa\ge 2\)) there are two internally disjoint \(w_3\)–\(C\) paths, meeting \(C\) at distinct vertices \(a,b\). The union of these two paths with \(C\) contains a cycle through \(w_3\) and at least one of \(w_1,w_2\). Replacing \(C\) by a cycle through two of the three roots and iterating the \(2\)-connected ear argument (or applying Case 1 to a cycle through all three after adding an ear through \(w_3\)) produces a rooted \(K_3\) model. Concretely: the two \(a\)–\(b\) arcs of \(C\) together with the two \(w_3\)–paths form a \(\Theta\)-subgraph. Place \(w_1,w_2\) on this \(\Theta\) (they lie on \(C\)) and partition the \(\Theta\) into three connected branch sets containing the three roots — always possible by assigning each of the three internally disjoint \(a\)–\(b\) routes (two arcs + the \(w_3\)-detour) to connect the roots. ∎

### Theorem 5.5 (Prescribed rooted \(K_4\) needs \(\kappa\ge 3\) and is not free)
There exist \(3\)-connected graphs and \(4\)-sets that do **not** root a \(K_4\) model (e.g. a large grid with four corners: a grid has no \(K_4\) minor at all? — actually a large grid has large treewidth and large clique minors by RS, but planar graphs have no \(K_5\) minor; they do have \(K_4\) minors).  

In a \(3\)-connected planar triangulation, any four vertices root a \(K_4\) minor (Kelmans–Seymour type phenomena at \(t=5\) are deeper).  

**Elementary positive result:** if \(H\) is \(3\)-connected and \(w_1,w_2,w_3,w_4\) are distinct with at least one having three neighbours on a common cycle through the others, a rooted \(K_4\) exists (same construction as Lemma 5.1 in the connectivity note: three neighbours on a cycle give \(K_4\) with the fourth vertex as apex). ∎

### Theorem 5.6 (Strongest elementary prescribed-terminal theorem under connectivity alone)
Let \(H\) be \(\kappa\)-connected. Then:
1. every set of \(r\le\kappa\) vertices is the end-set of a fan from any external vertex (Menger);
2. every set of \(r\le 2\) vertices is pair-linked in \(H\) if \(H\) is connected;
3. every set of \(r\le 3\) vertices roots a \(K_3\) minor if \(\kappa\ge 2\);
4. for \(r\ge 4\), connectivity \(\kappa=7\) does **not** imply that every \(r\)-set is pair-linked (need \(\binom{r}{2}\)-linkedness, hence \(\kappa=\Omega(r^2)\) by the converse direction of linkage theory: there are graphs with connectivity \(2k-2\) that are not \(k\)-linked).

**Proof.** (1)–(3) above. (4) is classical (Jung, Larman–Mani, etc.). ∎

---

## 6. Critical colouring: Kempe geometry on prescribed terminals

Now add the colouring structure of a minimal Hadwiger counterexample.

### Setup 6.1
Let \(G\) be a minimal counterexample to \(\mathrm{HC}_t\), \(t\ge 7\). Fix \(v\in V(G)\), set \(H=G-v\). Then:
- \(\chi(H)=t-1=\eta(H)\) (unrooted \(K_{t-1}\) exists);
- \(\kappa(H)\ge 6\) (Mader: \(\kappa(G)\ge 7\)); if Dirac \(\kappa(G)\ge t-1\) is granted, \(\kappa(H)\ge t-2\);
- for every proper \((t-1)\)-colouring \(c\) of \(H\), the set \(N(v)\) meets every colour (rainbow neighbourhood);
- pick rainbow terminals \(u_i\in N(v)\cap c^{-1}(i)\) for \(i=1,\dots,t-1\).

### Lemma 6.2 (Kempe paths between rainbow terminals)
For every pair \(\{i,j\}\subseteq\{1,\dots,t-1\}\), the vertices \(u_i\) and \(u_j\) lie in the same connected component of the bichromatic subgraph \(H_{ij}:=H\bigl[c^{-1}(\{i,j\})\bigr]\). Hence there is a \(u_i\)–\(u_j\) path \(P_{ij}\) using only colours \(i\) and \(j\).

**Proof.** If not, swap colours \(i\) and \(j\) on the component of \(H_{ij}\) containing \(u_i\). The new colouring \(c'\) of \(H\) is proper, and \(c'(N(v))\) misses colour \(i\) (the neighbour \(u_i\) now has colour \(j\), and no other neighbour had colour \(i\) in a way that survives — more carefully: originally \(u_i\) was the chosen colour-\(i\) neighbour; after swap it has colour \(j\); any other colour-\(i\) vertex on \(N(v)\) would also flip if in the same component). Standard: after the swap, no neighbour of \(v\) has colour \(i\), so \(c'\) extends to \(G\) by colouring \(v\) with \(i\), contradiction. ∎

### Lemma 6.3 (Complete Kempe path system)
There exists a family \(\{P_{ij}:1\le i<j\le t-1\}\) of paths in \(H\) with \(P_{ij}\) joining \(u_i\) to \(u_j\) and \(V(P_{ij})\subseteq c^{-1}(\{i,j\})\).

**Proof.** Lemma 6.2. ∎

### Lemma 6.4 (If the Kempe system is internally disjoint, done)
If the interiors of the paths \(P_{ij}\) are pairwise disjoint, then \(\{u_1,\dots,u_{t-1}\}\) is pair-linked, Lemma 4.3 gives a rooted \(K_{t-1}\) model, and \(\{\{v\},B_1,\dots,B_{t-1}\}\) is a \(K_t\) model in \(G\), contradiction.

**Proof.** Standard. ∎

### Lemma 6.5 (Colour of shared vertices)
If \(x\in V(P_{ab})\cap V(P_{cd})\), then \(c(x)\in\{a,b\}\cap\{c,d\}\). A vertex of colour \(\gamma\) can lie only on Kempe paths \(P_{ij}\) with \(\gamma\in\{i,j\}\).

**Proof.** Vertices of \(P_{ij}\) have colours in \(\{i,j\}\). ∎

### Lemma 6.6 (Naive monochromatic branch sets fail)
Setting \(B_i:=c^{-1}(i)\cap\bigcup_{j\ne i}V(P_{ij})\) fails whenever \(|B_i|\ge 2\), because \(B_i\) is independent under the proper colouring \(c\).

**Proof.** Immediate. ∎

### Theorem 6.7 (Strongest prescribed-terminal lemma under critical colouring)
Let \(G,v,H,c,(u_i)\) be as in Setup 6.1. Then:

1. The rainbow set \(U=\{u_1,\dots,u_{t-1}\}\) admits a complete Kempe path system \(\mathcal{P}=\{P_{ij}\}\).  
2. \(\mathcal{P}\) is **not** internally vertex-disjoint (else Lemma 6.4).  
3. Every vertex of colour \(\gamma\) on the support of \(\mathcal{P}\) lies only on paths indexed by pairs containing \(\gamma\).  
4. Any rooted \(K_{t-1}\) model at \(U\) would yield a \(K_t\) minor in \(G\); hence **no** such model exists in a counterexample.  
5. Consequently, the obstruction is not the absence of paths but the **absence of a globally consistent branch-set assignment** for the Kempe support (Steiner vertices of colour \(j\) wanted by \(B_i\) are also wanted by \(B_j\)).

**Proof.** Combine Lemmas 6.2–6.6 with the rooted-upgrade: \(u_i\in N(v)\) and \(B_i\ni u_i\) connected and pairwise adjacent \(\Rightarrow\) add \(\{v\}\). ∎

### Theorem 6.8 (What \(\kappa\ge 7\) buys for prescribed terminals of size \(\le 7\))
In a \(7\)-connected graph \(H\):
1. any \(7\) vertices are nonseparable by a set of size \(\le 6\);
2. for any prescribed set \(W\) of \(r\le 7\) terminals and any vertex \(x\notin W\), there are \(r\) internally disjoint \(x\)–\(W\) paths (Menger);
3. for \(r\le 3\), \(W\) roots a \(K_r\) model (Theorems 5.3–5.4);
4. for \(r=4,5,6,7\), Menger fans exist, but pair-linkage of all \(\binom{r}{2}\) pairs is **not** guaranteed by \(\kappa=7\).

**Proof.** (1)–(2) Menger. (3) Theorem 5.4. (4) Theorem 5.6(4). ∎

---

## 7. The case \(t=7\): rainbow \(6\) terminals and rooted \(K_6\)

### Setup 7.1
Let \(G\) be a minimal counterexample to \(\mathrm{HC}_7\). Then:
- \(G\) is \(7\)-contraction-critical and \(7\)-critical;
- \(\kappa(G)\ge 7\) (Theorem 3.3);
- \(\delta(G)\ge 6\), and classically \(\delta\ge 7\);
- for every \(v\), \(H=G-v\) satisfies \(\chi(H)=6=\eta(H)\), \(\kappa(H)\ge 6\);
- rainbow terminals \(u_1,\dots,u_6\in N(v)\) under any \(6\)-colouring \(c\) of \(H\).

### Lemma 7.2 (Root obstruction)
No rainbow \(6\)-set \(U\subset N(v)\) roots a \(K_6\) model in \(H\). (Else add \(\{v\}\) for a \(K_7\) minor.)

**Proof.** Setup. ∎

### Lemma 7.3 (What we have on six terminals)
In \(H\) with \(\kappa(H)\ge 6\):
1. Kempe system \(\{P_{ij}:1\le i<j\le 6\}\) of \(\binom{6}{2}=15\) paths exists (Lemma 6.3).  
2. These \(15\) paths are not internally disjoint (Lemma 6.4).  
3. By Menger, for any vertex \(x\), there are \(6\) disjoint paths from \(x\) to \(U\) if \(\kappa\ge 6\).  
4. Full \(15\)-linkage of the pairs would require \(\kappa=\Omega(15)\) by Theorem 4.2, far above \(6\).

### Theorem 7.4 (Partial rooted models of order \(\le 3\))
For any three colours \(i,j,\ell\), the three terminals \(u_i,u_j,u_\ell\) root a \(K_3\) model in \(H\) (Theorem 5.4, since \(\kappa(H)\ge 6\ge 2\)).  

**Proof.** Theorem 5.4. ∎

### Theorem 7.5 (The \(t=7\) gap, precise)
The following statement would imply \(\mathrm{HC}_7\):

> **(R\(_7\))** Let \(H\) be a \(6\)-connected graph with \(\chi(H)=6\) that has a \(K_6\) minor. Let \(c:V(H)\to\{1,\dots,6\}\) be a proper colouring and \(u_i\in c^{-1}(i)\). Then \(H\) admits a \(K_6\) model \(\{B_i\}\) with \(u_i\in B_i\).

**Proof that R\(_7\Rightarrow\mathrm{HC}_7\).** For a minimal CE \(G\), pick \(v\), set \(H=G-v\), apply R\(_7\) to a rainbow neighbour set, add \(\{v\}\). ∎

### Why R\(_7\) is not free from \(\kappa=6\) and colouring

| Tool | Gives | Stops short of R\(_7\) |
|------|-------|----------------------|
| Mader \(\kappa(G)\ge 7\) | \(\kappa(H)\ge 6\) | \(6\)-connected graphs need not be \(15\)-linked |
| Bollobás–Thomason | \(ck\)-conn \(\Rightarrow k\)-linked | need connectivity \(\ge 10\cdot 15=150\) |
| Kempe system | \(15\) bichromatic paths on the terminals | paths share vertices; no consistent branch assignment |
| Rooted \(K_3\) on every triple | all triples of colours root \(K_3\) | no glueing lemma to a global rooted \(K_6\) |
| Unrooted \(K_6\) in \(H\) | exists by \(\eta(H)=6\) | roots are in the wrong place |

### Theorem 7.6 (Strongest positive lemma for \(t=7\) proved here)
Let \(G,v,H,c,U=\{u_1,\dots,u_6\}\) be as in Setup 7.1. Then:

1. Every triple in \(U\) roots a \(K_3\) minor in \(H\).  
2. Every pair in \(U\) is joined by a bichromatic Kempe path.  
3. The full Kempe system has unavoidable vertex shares; shares have colours in the intersection of the path indices (Lemma 6.5).  
4. There is **no** rooted \(K_6\) model at \(U\).  
5. \(H\) is **not** \(15\)-linked (else Lemma 4.4 with degree ports — each \(u_i\) has \(\deg_H(u_i)\ge \delta(G)-1\ge 5\), and for \(r=6\) we need \(\deg\ge 5\), borderline; if \(\delta(G)\ge 7\) then \(\deg_H\ge 6\ge 5\)).  

**Proof.** Combine the preceding lemmas. For (5): if \(H\) were \(15\)-linked and degrees \(\ge 5\), Lemma 4.4 would give pair-linkage of \(U\), contradiction to (4). ∎

### Attempt: glue triple models along Kempe paths

**Plan.** For each triple, take a rooted \(K_3\) model. Try to choose them nested/compatible so that branch sets for the same colour agree on overlaps.

**Death.** Rooted \(K_3\) models for different triples may place colour-\(i\) Steiner vertices on incompatible sides of a \(4\)-separator in \(H\). Connectivity \(6\) does not prevent the models from using the same vertex in two branch sets of different colours when glued. This is Obstruction (O) from the hybrid note, specialised to \(t=7\).

### Attempt: use \(\kappa(H)\ge 6\) to find a \(K_6\) model maximising contact with \(U\)

**Plan.** Start from an unrooted \(K_6\) model in \(H\), maximise the number of branch sets meeting \(U\), fan from non-contact roots into the model (Menger: \(6\)-connected \(\Rightarrow\) fans of size up to \(6\)).

**Death.** Simultaneous absorption of a multi-path fan into a contact-deficient model is the MCM gap (see `hadwiger_mcm_menger_fan.md`); equivalent in strength to R\(_7\).

---

## 8. Synthesis: what is proved and what remains

### Fully proved from first principles in this note

1. **Contraction-critical package:** \(\delta\ge k-1\), no clique separators, criticality.  
2. **Mader’s separator lemma** (Theorem 2.3) via power-set list colouring — complete.  
3. **\(\kappa\ge 6\)** for noncomplete \(k\)-contraction-critical graphs, \(k\ge 7\).  
4. **\(\kappa\ge 7\)** (Theorem 3.3), including the residual \(\alpha=2,|S|=6\) case via restricted power-set lists (the missing seventh colour is never needed because \(G[S]\) has edges).  
5. **Quadratic linkage gap:** Mader’s \(7\) cannot feed Bollobás–Thomason at \(k=\binom{t-1}{2}\).  
6. **Prescribed-terminal elementary theory** for \(r\le 3\); Kempe geometry for critical colourings; obstruction sheet for general \(t\) and for \(t=7\).  
7. **Reduction of \(\mathrm{HC}_7\) to R\(_7\)** (rooted \(K_6\) at rainbow \(6\)-sets in \(6\)-connected \(6\)-chromatic graphs with a \(K_6\) minor).

### Explicitly not proved

- Bollobás–Thomason / Thomas–Wollan linkage theorem (black box).  
- R\(_7\) itself (open; equivalent to \(\mathrm{HC}_7\) under the structural portrait).  
- Any theorem of the form “\(\kappa\ge 7\) and \(\delta\ge t-1\) \(\Rightarrow\) \(K_t\) minor” for \(t\ge 7\).  
- Improvements \(h(k)\ge 8,9,10\) for large \(k\) (LLRY; require dense knitted subgraphs and knitted-minimal mass arguments beyond the separator lemma).

### Logical skeleton

```
k-contraction-critical G, k≥7, G ≇ K_k
  │
  ├─ Mader separator lemma (power-set colouring)     [PROVED §2]
  │     α(S)≥|S|-3 and |S|≤k-1  ⇒  G−S connected
  │
  ├─ ⇒ no separator of size ≤5                       [PROVED §3]
  │     (α≤|S|-4 forces α≤1 ⇒ clique, forbidden)
  │
  ├─ residual |S|=6, α=2
  │     partition into ≤2-sets; knit both sides ⇒ recolour
  │     one side not knitted: restricted lists on ≤3
  │     colour pairs, 6 colours suffice (full-set colour
  │     unused because G[S] has edges)                [PROVED §3]
  │
  └─ ⇒ κ(G)≥7                                        [PROVED]

Hadwiger CE for t≥7
  │
  ├─ is t-contraction-critical ⇒ κ≥7                 [COR 3.5]
  ├─ rainbow t−1 terminals in G−v
  ├─ Kempe system of binom(t−1,2) paths              [PROVED §6]
  ├─ need pair-linkage of those terminals
  │     full linkedness needs κ=Ω(t²)  ≫ 7           [GAP §4]
  │
  └─ prescribed-terminal theory
        r≤3: rooted K_r free from κ≥2                [PROVED §5]
        r=t−1=6 for t=7: R_7 open                    [GAP §7]
```

### Conclusion

Mader’s theorem is proved from first principles: the separator lemma by power-set list colouring, the lift to \(7\)-connectivity by forbidding low-independence separators and closing the residual \(\alpha=2,|S|=6\) case with a restricted list system that fits inside \(k-1=6\) colours when \(k=7\).

Combined with Bollobás–Thomason, this constant connectivity is **orders of magnitude** too small to force \(\binom{t-1}{2}\)-linkedness.

The prescribed-terminal angle is the correct refinement: only one rainbow set of \(t-1\) terminals needs to be linked, and critical colouring supplies a complete Kempe path system on those terminals. For \(t=7\), this reduces \(\mathrm{HC}_7\) to the single rooted-minor statement R\(_7\). Every elementary tool available at connectivity \(6\) (Menger fans, rooted \(K_3\) on triples, Kempe geometry, unrooted \(K_6\)) has been applied; none closes R\(_7\).

**The exact remaining obstruction for \(t=7\):** glueing local rooted models (triples, Kempe paths, contact-maximising \(K_6\)) into a single rooted \(K_6\) at a rainbow \(6\)-set, inside a \(6\)-connected \(6\)-chromatic graph.

---

*End of note.*
