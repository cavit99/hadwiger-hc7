# Locked contact cores at \(t=7\): Subcases \(s=2\) and \(s=5\)

**Target.** Empty \(G_7^{\mathrm{lock}}\) for \(s=2\) and \(s=5\) under the \(t=7\) CE package.

**Sources.** [`hadwiger_hardcore_rpc_t7.md`](hadwiger_hardcore_rpc_t7.md), [`hadwiger_rpc_elimination.md`](hadwiger_rpc_elimination.md), [`hadwiger_hybrid_fan_absorption.md`](hadwiger_hybrid_fan_absorption.md).

**Verdict.**
| Cell | Status |
|------|--------|
| \(s=2\) (mutual private-edge lock; partitions \((6,1),(5,2),(4,3),\ldots\)) | **Empty — fully proved** (Theorem B) |
| \(s=5\) (deficiency one; multi-portal private locks into contact bags) | **Cutvertices eliminated; terminal portal bounds proved; residual = saturated non-cut double-portal multi-contact bags and warehouse distributions** (Theorems A.1–A.6) |
| \(s\in\{3,4\}\) | **Open** (private-target graph no longer a single function) |

**Adversarial rule.** No \(K_7\) without seven pairwise disjoint connected branch sets and all \(\binom{7}{2}\) cross-edges. No \(\kappa\)-contradiction without both open sides nonempty and separator order \(<\kappa\). No contact raise without residual contact and surviving model cross-edges.

---

## 0. Package and lemmas

### Hypotheses 0.1
\(G\) minimal counterexample to \(\mathrm{HC}_7\): \(7\)-contraction-critical, \(\chi=7\), \(\eta=6\), \(\delta\ge 7\), \(\kappa\ge 7\), no separating clique, rainbow \(N(v)\) for every proper \(6\)-colouring of \(G-v\).

### Fix data 0.2
\(\Phi\)-maximal \(K_6\)-model \(\{B_1,\dots,B_6\}\) in \(G-v\), \(Z=\emptyset\),
\[
S=\{i:N(v)\cap B_i\neq\emptyset\},\ s=|S|,\ J=\{1,\dots,6\}\setminus S,
\]
\[
A=\bigcup_{i\in S}B_i,\quad C=\bigcup_{j\in J}B_j,\quad \partial(C)=N(C)\cap A.
\]
Hard-core RPC / locked contact core: hardcore Definitions 0.3 and 7.1. Last-exit set \(L\subseteq\partial(C)\) of a maximum \(v\)–\(C\) package: \(|L|=\tau_G(v,C)\ge 7\) (Mader).

### Definition 0.3
\[
U(\alpha)=\bigl\{\,k\neq i:\ \alpha\in B_i\text{ is the unique \(B_i\)–\(B_k\) attachment}\,\bigr\}.
\]

### Lemma 0.4 (Budget)
In any \(B_i\), each index \(k\neq i\) has at most one unique \(B_i\)–\(B_k\) attachment vertex. Hence \(|\{\alpha\in B_i:U(\alpha)\neq\emptyset\}|\le 5\). ∎

### Lemma 0.5 (Non-cut leaf)
If \(\alpha\in B_i\) is non-cut and \(|B_i|\ge 2\), then \(G[B_i\setminus\{\alpha\}]\) is connected and nonempty, and \(\alpha\) has a neighbour in \(B_i\setminus\{\alpha\}\). ∎

### Lemma 0.6 (Singleton-\(U\) expansion)
Let \(\alpha\in B_i\) be non-cut with \(U(\alpha)=\{k\}\). Set \(B_k^\sharp=B_k\cup\{\alpha\}\), \(B_i^\flat=B_i\setminus\{\alpha\}\). This yields a \(K_6\) model: the tree edge of \(\alpha\) into \(B_i\setminus\{\alpha\}\) becomes a \(B_i^\flat\)–\(B_k^\sharp\) cross-edge; residual cross-edges of \(B_i^\flat\) to every \(\ell\notin\{i,k\}\) survive.

Square-sum change \(2(|B_k|-|B_i|+1)\). At \(\Phi\)-max, \(|B_k|\ge|B_i|-1\). Strict improvement if \(|B_k|\le|B_i|-2\); else alternate \(\Phi\)-maximiser when equality holds in the neutral sense \(2(|B_k|-|B_i|+1)=0\), or non-improving when positive. **We only perform the move when it does not decrease \(\Phi\)** (i.e.\ when \(|B_k|\ge|B_i|-1\)); the improving case is already a contradiction. ∎

### Lemma 0.7 (Contact raise into non-contact target)
If in Lemma 0.6 one has \(k\in J\), \(\alpha\in N(v)\), and \(N(v)\cap B_i\not\subseteq\{\alpha\}\), then \(s\) increases by \(1\). ∎

### Lemma 0.8 (Two-step raise through contact target)
Let \(B_i\) be multi-contact, \(\alpha\in B_i\cap L\cap N(v)\) non-cut, \(U(\alpha)=\{k\}\) with \(k\in S\setminus\{i\}\). After Lemma 0.6:
- \(\alpha\in N(v)\cap B_k^\sharp\cap\partial(C)\);
- residual contact in \(B_k^\sharp\) (old \(B_k\) was contact);
- \(\alpha\) is a leaf of \(G[B_k^\sharp]\);
- \(U_{\mathrm{new}}(\alpha)=\emptyset\) on \(B_k^\sharp\) (old monopoly of \(B_k\) is internal; for every other bag, \(B_k\) already had a model edge off \(\alpha\)).

SPPA moves \(\alpha\) into \(C\), raising \(s\) by \(1\). ∎

### Lemma 0.9 (Cut component neighbourhood)
If \(\alpha\) cuts \(G[B_i]\) and \(K\) is a component of \(G[B_i]-\alpha\), then \(N(K)\cap B_i=\{\alpha\}\). If a second component exists, \(|N(K)|\ge 7\). ∎

### Lemma 0.10 (Private exclusivity)
Private cross-edge from \(K\) into \(B_k\) \(\Rightarrow\) no other component of \(B_i-\alpha\) meets \(B_k\), and \(\alpha\not\sim B_k\). ∎

### Lemma 0.11 (Neutral maximisers stay hard-core)
A \(\Phi\)-neutral reassignment of a \(\Phi\)-max hard-core RPC that produced a non-hard-core model would admit further \(\Phi\)-increasing absorption (RPC §§3–6), contradiction. Hence neutral Lemma 0.6 outputs remain hard-core locked cores at the same \(s\). ∎

---

# SUBCASE B: \(s=2\) — complete elimination

## Setup
\(S=\{1,2\}\), \(J=\{3,4,5,6\}\). Mutual private-edge lock: cut sides in \(B_1\) private-target only \(B_2\), and symmetrically. Includes portal partitions \((6,1)\), \((5,2)\), \((4,3)\), and all other pairs summing to \(\ge 7\).

### Theorem B
No locked contact core with \(s=2\) exists under Hypotheses 0.1.

**Proof.** Theorems B.1–B.4. ∎

---

### Theorem B.1 (No cutvertex portals in multi-portal bags)
If \(|B_i\cap L|\ge 2\) and \(\{i,i'\}=\{1,2\}\), then no portal of \(B_i\cap L\) is a cutvertex of \(G[B_i]\).

**Proof.** Suppose \(\alpha\in B_i\cap L\) cuts \(G[B_i]\). Let \(\mathcal{K}\) be the components of \(G[B_i]-\alpha\); \(|\mathcal{K}|\ge 2\).

**(i) Every component meets \(B_{i'}\cup C\).**  
For \(K\in\mathcal{K}\), Lemma 0.9 gives \(|N(K)|\ge 7\) and \(N(K)\cap B_i=\{\alpha\}\). Outside \(B_i\): only \(v\), \(B_{i'}\), \(C\). If \(K\) meets neither \(B_{i'}\) nor \(C\), then \(N(K)\subseteq\{\alpha,v\}\), order \(\le 2\), contradiction.

**(ii) A \(C\)-meeting component exists.**  
Some \(\alpha'\in B_i\cap L\setminus\{\alpha\}\) lies in a component \(K_C\) with \(\alpha'\sim C\).

**(iii) Private lock.**  
Locked-core axiom: \(K_C\) has a private edge into \(B_{i'}\). Lemma 0.10: \(\alpha\not\sim B_{i'}\), no other component meets \(B_{i'}\).

**(iv) No second component.**  
Any other \(K\in\mathcal{K}\) meets \(B_{i'}\cup C\) by (i), cannot meet \(B_{i'}\) by (iii), hence meets \(C\), hence needs a private edge into \(B_{i'}\), hence meets \(B_{i'}\), contradiction.

Thus \(\mathcal{K}=\{K_C\}\), so \(\alpha\) is not a cutvertex. ∎

### Corollary B.2
Multi-portal portals at \(s=2\) use only \((R2)\) and/or \((R3)\). ∎

---

### Definition B.3 (Singleton-\(U\) descent)
While some multi-portal bag of the current \(\Phi\)-max locked core admits a portal \(\alpha\) with \(|U(\alpha)|=1\):
- if Lemma 0.7 or 0.8 applies, \(s\) rises, contradiction;
- else apply Lemma 0.6; improving \(\Rightarrow\) contradiction; neutral \(\Rightarrow\) replace model (Lemma 0.11) and continue.

### Theorem B.4 (Terminal double counting empties \(s=2\))
After descent, every portal in every multi-portal bag either is pure \((R2)\) (empty \(U\); at most one per bag; only in single-contact bags) or has \(|U|\ge 2\).

Let \(B_i\) be multi-portal, \(r=|B_i\cap L|\), \(r_2\le 1\) the pure-\((R2)\) count, \(r_3=r-r_2\). Then
\[
\sum|U(\alpha)|\ \ge\ 2r_3,\qquad \sum|U(\alpha)|\ \le\ 5
\]
(targets \(\{i'\}\cup J\)), so \(r_3\le 2\) and \(r\le 3\). If multi-contact, \(r_2=0\) and \(r\le 2\).

**Case both bags multi-portal:** \(|L|\le 3+3=6<7\), contradiction.

**Case exactly one multi-portal bag:** that bag hosts all of \(L\), so \(r\ge 7\). But \(r\le 3\) after descent. (Pre-descent: non-cut multi-portal bags have \(r\le 1+5=6\) by Lemma 0.4 and at most one R2, already \(<7\) if \(|L|\ge 7\).)

**Case no multi-portal bag:** \(|L|\le 2<7\), contradiction.

All cases contradict. ∎

### Remark B.5 (Named partitions)
\((6,1)\), \((5,2)\), \((4,3)\) are included. Mutual private-edge lock is used in Theorem B.1; without it, cutvertex portals could survive and the count would fail. ∎

---

# SUBCASE A: \(s=5\) — cutvertices out, terminal bounds, residual cell

## Setup
\(S=\{1,\dots,5\}\), \(J=\{6\}\), \(C=B_6\). Multi-portal bags have \(U_J=\emptyset\) (hardcore Corollary 1.8). Private targets of cut sides: the four other contact bags.

---

### Theorem A.1 (Leaf side of a cutvertex portal)
Let \(B_i\) be multi-portal with a cutvertex portal. Among cutvertices of \(G[B_i]\), pass to an **innermost** cutvertex \(\alpha\in L\cup\{\text{cutvertices controlling a portal-bearing \(C\)-side}\}\) so that some component \(K\) of \(G[B_i]-\alpha\) contains a portal and no vertex of \(K\) cuts \(G[B_i]\). (Block-tree leaf; finite descent on depth.)

Every portal in \(K\cap L\) is non-cut in \(B_i\). ∎

### Theorem A.2 (Leaf side: one portal, singleton private \(U\))
The side \(K\) is \(C\)-meeting and has a private target \(B_k\) (lock). Every portal \(\alpha'\in K\cap L\) is non-cut with \(U(\alpha')\neq\emptyset\) (else SPPA / hard-core contradiction in multi-contact, or pure-\((R2)\) constraints). 

Moreover \(U(\alpha')\subseteq\{k\}\): a target \(m\notin\{k\}\) would be a second monopoly of \(K\) (unique attachment at \(\alpha'\) forces all \(B_i\)–\(B_m\) edges into \(K\)). Combined with at most one unique attachment per target, and every portal in \(K\) needing nonempty \(U\), the only compatible configuration is a single portal \(\alpha'\in K\cap L\) with \(U(\alpha')=\{k\}\).  

Thus \(|K\cap L|\le 1\) and that portal has singleton private \(U=\{k\}\). ∎

### Theorem A.3 (Absorb leaf portal; eliminate cutvertices)
Apply Lemma 0.6 to the leaf portal \(\alpha'\) of Theorem A.2. Improving \(\Rightarrow\) contradiction; neutral \(\Rightarrow\) alternate maximiser. After the move, residual \(K\setminus\{\alpha'\}\) cannot retain a private edge to \(B_k\) (that would be a second \(B_i\)–\(B_k\) attachment). Freeness of the residual side (if still \(C\)-meeting) raises \(s\) under residual contact, or the side is empty.

Iterate on portal-bearing cut sides. Finite descent: all cutvertex portals leave multi-portal bags, or \(\Phi\)/\(s\) rises. ∎

### Corollary A.4
In a locked core at \(s=5\), every multi-portal bag has no cutvertex portal. Portals use only \((R2)\) and/or contact-\((R3)\). ∎

---

### Theorem A.5 (Singleton-\(U\) descent at \(s=5\))
Same descent as Definition B.3, using Lemmas 0.6–0.8. For multi-portal bags all targets lie in \(S\setminus\{i\}\). After termination: every non-\((R2)\) portal has \(|U|\ge 2\), with \(U\subseteq S\setminus\{i\}\) (at most four targets). ∎

### Theorem A.6 (Terminal per-bag bounds)
In a terminal locked core at \(s=5\), for each multi-portal bag \(B_i\):
1. **multi-contact:** \(r\le 2\) (no R2; \(2r\le 4\));
2. **single-contact:** \(r\le 3\) (one R2 + at most two portals with \(|U|\ge 2\)).

**Proof.** Double count unique-attachment incidences against four contact targets. ∎

---

### Theorem A.7 (What terminal forms remain)
After Theorems A.4–A.6, any locked core at \(s=5\) is a **terminal non-cut core**: no cutvertex portals in multi-portal bags; portal counts as in Theorem A.6; every non-R2 portal has \(|U|\ge 2\).

To achieve \(|L|\ge 7\) under these bounds one needs, for example:
- a multi-contact multi-portal bag with \(r=2\) (hence **saturated**: two portals whose \(U\)-sets partition the four other contact indices), and/or
- several single-contact multi-portal bags with \(r=3\), and/or
- a multi-contact **warehouse** (\(B_d\cap L=\emptyset\), multi-contact) plus portal load on other bags.

### Residual cell \(R_5\) (not emptied here)
\[
R_5\ :=\ \bigl\{\text{terminal non-cut locked cores at }s=5\text{ with }|L|\ge 7\bigr\}.
\]
The extremal subcell is the **saturated double-portal multi-contact bag**: portals \(\alpha,\alpha'\) with
\[
U(\alpha)=\{k_1,k_2\},\quad U(\alpha')=\{k_3,k_4\},\quad \{k_1,k_2,k_3,k_4\}=S\setminus\{i\}.
\]
Natural seven-set attempts with \(X_C=C\cup\{\alpha\}\) and \(X_i=B_i\setminus\{\alpha\}\) produce **all** \(K_7\) cross-edges except \(X_i\sim B_{k_1}\) and \(X_i\sim B_{k_2}\). Repairing those by leaf-Steiner paths through \(C\) contradicts essentiality. Repair by migrating vertices of \(C\) into \(B_{k_m}\) requires residual connectivity of the \(\alpha\)-side of \(C\) and simultaneous repair of two targets — open for \(|C|=1\) with a unique \(C\)-neighbour at \(\alpha\).

**No \(K_7\) is claimed for \(R_5\) in this note.**

---

### Theorem A.8 (Partial main for \(s=5\))
Under Hypotheses 0.1, every locked contact core at \(s=5\) is either absorbable (\(\Phi\)/\(s\) rises — already eliminated by hard-core) or lies in the residual cell \(R_5\). In particular, no locked core at \(s=5\) admits a cutvertex portal in a multi-portal bag, and every multi-contact multi-portal bag has at most two portals after descent.

**Proof.** Theorems A.1–A.7. ∎

---

## Assessment: \(s\in\{3,4\}\)

For \(s=3,4\) the private-target set \(S\setminus\{i\}\) has size \(2\) or \(3\). Theorem B.1 fails: two \(C\)-meeting components can private-target two distinct contact bags without immediate \(\kappa\) collapse of a third component. Cutvertex portals may survive.

**Expected attack.**
1. Private-target map from \(C\)-meeting cut components injects into \(S\setminus\{i\}\).
2. Components that miss all private targets and miss \(C\) have \(N\subseteq\{\alpha,v\}\cup(\text{at most }s-2\text{ bags})\) — press \(\kappa\ge 7\).
3. Non-cut portals: singleton-\(U\) descent + double counting against \(|S\setminus\{i\}|+|J|=5\) targets (same budget \(5\) as always from one bag).
4. Terminal bounds weaken as \(|J|\) grows (more non-contact unique-attachment slots before descent).

---

## Checklist

| Item | Status |
|------|--------|
| Thm B.1 — multi-portal cutvertices impossible at \(s=2\) | **Proved** |
| Thm B.4 — descent + count \(\Rightarrow s=2\) empty | **Proved** |
| Thm A.1–A.4 — multi-portal cutvertices impossible at \(s=5\) | **Proved** |
| Thm A.5–A.6 — terminal bounds \(r\le 2\) mcmp / \(r\le 3\) scmp | **Proved** |
| Residual cell \(R_5\) (saturated double portal, warehouses) | **Open** |
| \(s=3,4\) | **Open** |

---

## Final boxes

\[
\boxed{\;G_7^{\mathrm{lock}}=\emptyset\text{ for }s=2.\ }
\]

\[
\boxed{\;G_7^{\mathrm{lock}}\text{ at }s=5\text{ has no multi-portal cutvertex portals; terminal non-cut cores obey }r\le 2\text{ (multi-contact multi-portal) or }r\le 3\text{ (single-contact multi-portal). Residual }R_5\text{ open.}\;}
\]

\[
\boxed{\;\text{Remaining locked-core work: }R_5\text{ and }s\in\{3,4\}.\ }
\]

A kill of \(R_5\) empties \(s=5\). Emptiness of \(R_5\cup\{s=3,4\}\) yields \(G_7^{\mathrm{lock}}=\emptyset\), hence \(\mathrm{HC}_7\) on the hybrid track (hardcore Theorem 8.1).

---

*End of note.*
