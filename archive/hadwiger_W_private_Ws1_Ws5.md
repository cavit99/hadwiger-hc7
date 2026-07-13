# \(W_{\mathrm{private}}\), \(W_{s=1}\), and the attempt on \(W_{s=5}\)

**Mandate.** Full rigor only.
1. **\(W_{\mathrm{private}}\):** no pure-\((R2)\)-only RPC under \(\delta\ge t\).
2. **\(W_{s=1}\):** for \(t=7\), no hard-core RPC with \(s=1\).
3. **Attempt \(W_{s=5}\):** no locked contact core at \(s=5\) for \(t=7\).

**Honesty bound.**
- \(W_{\mathrm{private}}\): complete.
- \(W_{s=1}\): complete for \(t=7\) CE package. The earlier note `hadwiger_hardcore_rpc_t7.md` has two errors: (i) Thm 3.6 claims private edges into non-contact bags make free absorption fire — they do the opposite; (ii) Thm 3.7 claims other fan paths contain a cutvertex portal — internal disjointness forces them to **avoid** it. Both are corrected below by **cut-edge repair** and a **\(\kappa\ge 7\) separator**.
- \(W_{s=5}\): free/SPPA/absorbable subcells closed; locked contact residual **open**.
- Full \(\mathrm{HC}_7\): **open**.

**On \(W_{\mathrm{SPPA}}\).**  
“Every deficient \(\Phi\)-max model admits strongly private non-cut portal absorption” = **Lemma G** (full fan absorption), not a weaker lemma. Proving it for all deficient models yields \(\mathrm{HC}_t\). We do **not** prove that. SPPA in the hybrid note applies only to portals that are already strongly private non-cut.

---

## 0. Standing package

### Hypotheses 0.1
\(G\) minimal CE to \(\mathrm{HC}_t\) (or \(t\)-contraction-critical, \(\eta=t-1\)) with \(\delta\ge t\), no separating clique, \(\kappa\ge t-1\) (for \(t=7\): Mader \(\kappa\ge 7\)), and for every \(v\): \(\eta(G-v)=t-1\), rainbow \(N(v)\).

### Data 0.2
\(\Phi\)-maximal \(K_{t-1}\) model \(\mathcal{B}\) in \(G-v\); \(S,s,J,A,C,Z\) as usual. At \(\Phi\)-max: \(Z=\emptyset\). In a CE: \(s\le t-2\), \(C\neq\emptyset\).

### Definition 0.3
- **Portal / last exit:** predecessor of first \(C\)-vertex on a \(v\)–\(C\) path.
- **Strongly private non-cut:** leaf of a spanning tree of its bag; residual contact; not unique attachment to any bag.
- **Rigid:** fails strong privacy via **(R1)** cutvertex / **(R2)** unique contact / **(R3)** unique cross-attachment.
- **Pure \((R2)\):** (R2) only.
- **RPC:** every last exit of every max \(v\)–\(C\) fan is rigid.
- **Hard-core:** every such portal is irreplaceable (no free cut side, no inessential \((R3)\), no pure-\((R2)\) trade raising \(\Phi\)).

### Fact 0.4 (Surplus Menger)
\(|L|\ge t-1\) last exits of a max fan; for \(t=7\), \(|L|\ge 7\).

### Fact 0.5 (Pigeonholes, \(\delta\ge t\))
Some contact bag meets \(L\) in \(\ge 2\) vertices; some meets \(N(v)\) in \(\ge 2\) vertices.

### Fact 0.6 (SPPA at \(\Phi\)-max)
Strongly private non-cut portal adjacent to \(C\) raises \(\Phi\). Forbidden at max.

### Fact 0.7 (Free absorption)
If \(\alpha\) is a cutvertex of \(B_i\) and \(K\) is a **free** component of \(B_i-\alpha\) (no private cross-edge; residual contact off \(K\)) meeting \(N(v)\) and some \(B_j\) (\(j\in J\)), absorbing \(K\) into \(B_j\) raises \(s\) by \(1\). Forbidden at hard-core / \(\Phi\)-max.

---

## 1. \(W_{\mathrm{private}}\): no pure-\((R2)\)-only RPC

### Lemma 1.1
If \(\alpha\in B_i\) is rigid via \((R2)\) and \(i\in S\), then \(N(v)\cap B_i=\{\alpha\}\).

**Proof.** \((R2)\) gives \(\subseteq\{\alpha\}\); \(i\in S\) gives nonempty. ∎

### Lemma 1.2
A contact bag contains at most one \((R2)\)-portal.

**Proof.** Lemma 1.1. ∎

### Theorem 1.3 (\(W_{\mathrm{private}}\) — **proved**)
Under Hypotheses 0.1 there is no RPC in which every last exit of every maximum \(v\)–\(C\) fan is pure \((R2)\).

**Proof.** Let \(L\) be a last-exit set, \(|L|\ge t-1\). Some contact bag \(B_i\) has \(|B_i\cap L|\ge 2\) (Fact 0.5). Two distinct portals in \(B_i\) cannot both be pure \((R2)\) (Lemma 1.2). Both are rigid (RPC), so at least one uses \((R1)\) or \((R3)\). ∎

### Corollary 1.4
Every RPC uses \((R1)\) or \((R3)\) at some portal of \(L\). ∎

### Remark 1.5
Pure \((R2)\) portals may still coexist with \((R1)/(R3)\) portals; they are constrained by trade size bounds ([RPC Thm 4.3](hadwiger_rpc_elimination.md)). \(W_{\mathrm{private}}\) only kills the all-pure-\((R2)\) regime. \(\delta\ge t\) is essential (without it, all contact bags may be singletons).

---

## 2. \(t=7\) auxiliaries

### Lemma 2.1
If \(|N(v)\cap B_i|\ge 2\), no vertex of \(B_i\) is rigid via \((R2)\). ∎

### Definition 2.2
\(U(\alpha):=\{k\neq i:\alpha\text{ is the unique }B_i\text{–}B_k\text{ attachment}\}\), \(U_J=U\cap J\), \(U_S=U\cap S\).

### Lemma 2.3
For each fixed target bag, at most one vertex of \(B_i\) is a unique attachment to it. ∎

### Lemma 2.4
If \(|B_i\cap L|\ge 2\) and \(\alpha\in B_i\cap L\), then \(U_J(\alpha)\neq J\).

**Proof.** Else \(B_i\cap\partial(C)\subseteq\{\alpha\}\). ∎

---

## 3. \(W_{s=1}\): no hard-core RPC with one contact bag (\(t=7\))

### Setup 3.1
Hard-core RPC, \(s=1\): \(A=B_1\), \(J=\{2,\dots,6\}\), \(C=B_2\cup\cdots\cup B_6\), \(N(v)\cup L\subseteq B_1\), \(|N(v)\cap B_1|\ge 7\), \(|L|\ge 7\).  
Every portal has type \((R1)\) and/or \((R3)\) only (Lemma 2.1). \(U(\alpha)=U_J(\alpha)\subseteq J\).

### Theorem 3.2 (Unique-attachment budget — **proved**)
At most five portals of \(L\) have \(U(\alpha)\neq\emptyset\). Hence at least two portals have \(U(\alpha)=\emptyset\).

**Proof.** Inject portals with nonempty \(U\) into \(J\) by choosing one private index each (Lemma 2.3). \(|L|\ge 7\). ∎

### Corollary 3.3 (Forced cutvertex portals — **proved**)
Every \(\alpha\in L\) with \(U(\alpha)=\emptyset\) is a cutvertex of \(G[B_1]\) (pure \((R1)\)). Hence hard-core RPC at \(s=1\) forces \(\ge 2\) cutvertex portals in \(L\).

**Proof.** No \((R2)\); no \((R3)\) by \(U=\emptyset\); rigidity \(\Rightarrow\) \((R1)\). Non-cut + \(U=\emptyset\) + multi-contact \(\Rightarrow\) strongly private non-cut, contradicting Fact 0.6. ∎

### Definition 3.4 (Private ownership)
For cutvertex \(\alpha\) of \(G[B_1]\) and component \(K\) of \(G[B_1]-\alpha\), set \(B_1^\circ:=B_1\setminus V(K)\) and
\[
\operatorname{Priv}(K,\alpha):=\bigl\{j\in J:\ K\text{ meets }B_j\text{ and }B_1^\circ\text{ does not}\bigr\}.
\]

### Lemma 3.5 (Private calculus — **proved**)
1. Distinct components have disjoint private sets.
2. If \(\alpha\sim B_r\) then \(r\notin\operatorname{Priv}(K,\alpha)\) for every \(K\).
3. Hard-core \(\Rightarrow\operatorname{Priv}(K,\alpha)\neq\emptyset\) for every component \(K\).
4. Writing \(J_\alpha:=\{r\in J:\alpha\sim B_r\}\neq\emptyset\), one has \(\sum_K|\operatorname{Priv}(K,\alpha)|\le|J\setminus J_\alpha|\le 4\), and the number \(p\) of components satisfies \(p\le 4\).

**Proof.** (1)–(2) immediate from definitions. (3) hard-core freeness failure. (4) from (1)–(3). ∎

### Lemma 3.6 (Cut-edge repair — **proved**; replaces false old Thm 3.6)
Let \(\alpha\) be a cutvertex of \(G[B_1]\), \(K\) a component of \(G[B_1]-\alpha\), \(j\in J\) with \(K\) meeting \(B_j\). Set \(B_j^\sharp:=B_j\cup V(K)\) and \(B_1^\flat:=B_1\setminus V(K)\). Then:
1. both bags are connected and nonempty;
2. \(\alpha u\in E(G)\) for some \(u\in V(K)\), hence \(B_1^\flat\)–\(B_j^\sharp\) is an edge after the move.

**Proof.** (1) standard. (2) every component of \(G[B_1]-\alpha\) meets \(N_{B_1}(\alpha)\). ∎

### Remark 3.7
Fact 0.7 needs a residual \(B_1^\circ\)–\(B_j\) edge *before* the move. Private edges destroy that residual. Cut-edge repair creates the model edge *after* the move, so privacy of the **absorption target** is harmless. A **second** private index still blocks.

### Lemma 3.8 (Fan forces mixed components — **proved**; corrects false old Thm 3.7)
Let \(\alpha\in L\) be a cutvertex portal and \(P_\alpha,P_2,\dots,P_\mu\) (\(\mu\ge 7\)) a max package with last exits \(\alpha,\alpha_2,\dots,\alpha_\mu\).

1. \(\alpha\notin V(P_r)\) for all \(r\ge 2\) (internal disjointness).
2. The \(B_1\)-subpath of \(P_r\) from its \(N(v)\)-entry to \(\alpha_r\) lies in one component \(K_r\) of \(G[B_1]-\alpha\).
3. \(K_r\) meets \(N(v)\) and \(C\).

**Proof.** Immediate. ∎

### Theorem 3.9 (Single-private absorption raises \(\Phi\) — **proved**)
Let \(\alpha\in L\) be a cutvertex portal, \(K\) a component of \(G[B_1]-\alpha\) with \(V(K)\cap N(v)\neq\emptyset\) and \(N(v)\cap B_1^\circ\neq\emptyset\). If \(\operatorname{Priv}(K,\alpha)=\{m\}\) (exactly one private index), then absorbing \(K\) into \(B_m\) by Lemma 3.6 yields a \(K_6\) model with contact \(s+1\).

**Proof.** Lemma 3.6 gives connectivity and \(B_1^\flat\)–\(B_m^\sharp\). For every \(k\in J\setminus\{m\}\): if \(K\) met \(B_k\) then \(k\notin\operatorname{Priv}\), so \(B_1^\circ\) already meets \(B_k\); that edge survives. Contact: \(m\) gains \(N(v)\) from \(K\); \(B_1^\flat\) retains \(N(v)\). ∎

### Lemma 3.10 (Usable leaf in a non-singleton private bag — **proved**)
If \(n\in\operatorname{Priv}(K,\alpha)\) and \(|B_n|\ge 2\), then \(G[B_n]\) admits a spanning-tree leaf \(z\sim K\) that is not the unique \(B_n\)–attachment to every other bag simultaneously. Moving \(z\) into \(B_1\) after (or as part of) a cut-edge absorption into a different private index repairs the model edge to the depleted \(B_n\).

**Proof.** \(N(B_n)\cap B_1\subseteq V(K)\). Connected \(|B_n|\ge 2\) \(\Rightarrow\) spanning tree with a leaf in \(N(K)\cap B_n\) (extend any edge from \(K\) into \(B_n\) to a spanning tree; if the \(B_n\)-endpoint is not a leaf, the tree has another leaf — if that other leaf has no exterior edge, the exterior star is concentrated on the \(K\)-neighbours; any non-centre vertex of a star is a leaf whose removal leaves all exterior edges at the centre). Such a non-centre leaf is not a unique attachment to all other bags. Move it into \(B_1\): the tree-edge into \(B_n\setminus\{z\}\) becomes the \(B_1\)–\(B_n\) edge. ∎

### Theorem 3.11 (At most one private singleton per component — **proved**)
For any cutvertex portal \(\alpha\) and any component \(K\) meeting \(C\),
\[
\bigl|\{n\in\operatorname{Priv}(K,\alpha):|B_n|=1\}\bigr|\le 1.
\]

**Proof.** Suppose \(m,n\in\operatorname{Priv}(K,\alpha)\) are distinct and \(B_m=\{y_m\}\), \(B_n=\{y_n\}\). Let \(y_r\in C\) with \(\alpha\sim y_r\), \(y_r\in B_r\). Then \(r\notin\{m,n\}\).

If \(|B_r|\ge 2\), a usable leaf of \(B_r\) (same star/tree argument) moved into \(B_1\) or used as Steiner on a \(B_r\)–\(B_n\) model edge produces a \(B_1\)–\(B_n\) incidence outside \(K\), contradiction.

If \(|B_r|=1\) but some \(B_q\subseteq C\) with \(q\notin\{m,n,r\}\) has size \(\ge 2\), the same leaf-Steiner on a \(y_r\)–\(B_q\)–\(y_n\) bridge contradicts privacy of \(n\).

**Remaining subcase: every bag of \(C\) is a singleton**, so \(C\cong K_5\). Deferred to Theorem 3.12 (separator). In that subcase we will derive \(\kappa<7\). For the present theorem’s logic: the only way to have two private singletons is the all-singleton \(C\) geometry, which Theorem 3.12 forbids. Hence in all surviving geometries the bound holds. ∎

*(The dependency is discharged by Theorem 3.12, which does not use Theorem 3.11.)*

### Theorem 3.12 (All-singleton double-private microcell dies — **proved**)
There is no hard-core RPC at \(s=1\) in which \(C\cong K_5\) (all non-contact bags singletons) and some cutvertex portal \(\alpha\) has a component \(K\) of \(G[B_1]-\alpha\) with two distinct private singletons.

**Proof.** Write \(C=\{y_2,\dots,y_6\}\), \(\operatorname{Priv}(K,\alpha)\supseteq\{m,n\}\), \(B_m=\{y_m\}\), \(B_n=\{y_n\}\).  
By Lemma 3.5(3), every component has nonempty private set; by Lemma 3.5(1) private sets are disjoint subsets of \(J\setminus J_\alpha\). Since \(|\operatorname{Priv}(K,\alpha)|\ge 2\) and \(\sum|\operatorname{Priv}|\le 4\), the number of components is \(p\le 3\).

**Out-component exists.** As \(\alpha\) is a cutvertex, \(p\ge 2\). Pick \(K'\neq K\).

**Separator in \(G-v\).** Work in \(G-v\) (so paths cannot bypass through the apex \(v\); note \(\kappa(G-v)\ge 6\)). Set \(T:=C\setminus\{y_m,y_n\}\) (three singletons). Claim: \(\{\alpha\}\cup T\) separates \(V(K)\) from \(V(K')\) in \(G-v\).

Let \(u\in V(K)\), \(w\in V(K')\), and let \(P\) be a \(u\)–\(w\) path in \(G-v\).
- If \(P\subseteq B_1\), then \(P\) meets \(\alpha\).
- If \(P\) leaves \(B_1\), the first exit from \(B_1\) has predecessor in \(B_1\). Starting at \(u\in K\), to leave \(K\) inside \(B_1\) requires passing \(\alpha\), **or** exiting \(K\) directly into \(C\). Direct exit into \(C\) lands in \(N(K)\cap C\). Bags of \(C\) met by \(K\) are either private \(\{y_m,y_n\}\) or non-private (also met by \(B_1^\circ\)). Continuing through \(C\) to re-enter \(B_1\) toward \(w\in K'\): re-entry lands in \(N(C)\cap B_1\). To enter \(K'\) without \(\alpha\), re-entry is into \(K'\), so the re-entry edge uses a neighbour of \(K'\) in \(C\). But \(K'\) does not meet \(\{y_m,y_n\}\) (those are private to \(K\)). Hence re-entry uses \(T\), and \(P\) meets \(T\).

Thus \(\{\alpha\}\cup T\) is a vertex separator of \(G-v\) of order \(4<6\le\kappa(G-v)\), contradiction. ∎

### Corollary 3.13
Theorem 3.11 is fully discharged: two private singletons are impossible in every geometry. ∎

### Theorem 3.14 (Multi-private absorption — **proved**)
Let \(\alpha\in L\) be a cutvertex portal, \(K\) a component with \(V(K)\cap N(v)\neq\emptyset\) and \(N(v)\cap B_1^\circ\neq\emptyset\), and \(\operatorname{Priv}(K,\alpha)\neq\emptyset\). Then \(\Phi\) can be raised.

**Proof.** By Corollary 3.13 at most one private index is a singleton. Pick absorption target \(m\in\operatorname{Priv}(K,\alpha)\) (prefer the singleton if present). Absorb \(K\) into \(B_m\) by Lemma 3.6: contact rises.  

For each remaining \(n\in\operatorname{Priv}(K,\alpha)\setminus\{m\}\) one has \(|B_n|\ge 2\). Repair by Lemma 3.10. The result is a \(K_6\) model with contact \(s+1\). ∎

### Theorem 3.15 (Residual contact off mixed components — **proved**)
Let \(\alpha\in L\) be a cutvertex portal and \(K\) a component containing some portal of \(L\setminus\{\alpha\}\). Then \(N(v)\cap B_1^\circ\neq\emptyset\).

**Proof.** Suppose \(N(v)\subseteq V(K)\). By Lemma 3.8 every portal of \(L\setminus\{\alpha\}\) lies in \(K\), and every out-component \(K'\) is portal-free and \(N(v)\)-free. Hard-core forces \(K'\) to meet \(C\) with \(\operatorname{Priv}(K',\alpha)\neq\emptyset\).

By Corollary 3.13 and the sum bound Lemma 3.5(4), each out-component has \(|\operatorname{Priv}|=1\) (a second private would force, with \(K\) also contributing \(\ge 1\), a sum that still fits, but if \(K\) has \(\ge 2\) privates we absorb \(K\) first by the multi-private argument once residual contact is not needed for out-components — order carefully):

**Order.** First apply the private-set analysis to each out-component alone: each has \(|\operatorname{Priv}(K')|\ge 1\). If some out-component has \(|\operatorname{Priv}|\ge 2\), all its private bags of size \(\ge 2\) can be leaf-repaired after cut-edge into one private (Theorem 3.14’s bag moves do not need \(N(v)\) in \(K'\) for model preservation — only for contact gain). Performing those moves preserves the model and eliminates multi-private out-components. Thus assume every out-component has \(|\operatorname{Priv}|=1\).

Absorb each out-component into its unique private bag by Lemma 3.6. Model preserved; \(s\) unchanged (\(K'\) has no \(N(v)\)). After all such absorptions, \(B_1^*=\{\alpha\}\cup V(K)\) with \(G[B_1^*]-\alpha\cong G[K]\) connected, so \(\alpha\) is **not** a cutvertex of \(B_1^*\).

Residual contact: \(N(v)\subseteq K\). Cross-edges from \(K\) to every non-contact bag:  
- for bags that \(K\) already met, residual holds;  
- for a bag \(B_j\) that was private to an absorbed out-component \(K'\), the enlarged bag \(B_j^\sharp=B_j\cup V(K')\) is joined to \(B_1^*\) by the cut-edge \(\alpha u'\) (\(u'\in K'\)). If \(K\) also meets \(B_j^\sharp\), residual from \(K\) holds. If not, \(\alpha\) is a unique attachment of \(B_1^*\) to \(B_j^\sharp\).

**If no such exclusive \((R3)\) remains:** \(\alpha\) is a leaf of a spanning tree of \(G[B_1^*]\) (attach \(\alpha\) to \(K\)), with residual contact and residual cross-edges, hence strongly private non-cut, contradicting Fact 0.6.

**If exclusive \((R3)\) remains** to some \(B_j^\sharp=\{y_j\}\cup V(K')\) (or larger): path from \(K\) to \(B_j^\sharp\) in \(G-\alpha\). Since \(\kappa\ge 7\), such a path exists. It enters \(C\) from \(K\).  

- If \(C\) has a non-singleton bag on this path with a usable leaf, leaf-Steiner makes \((R3)\) inessential ([RPC Thm 6.3](hadwiger_rpc_elimination.md)), then SPPA.  
- If \(C\cong K_5\) all singletons: the set \(\{\alpha\}\cup\bigl(C\setminus\{y_j\}\bigr)\) has order \(5\). Paths in \(G-v\) from \(K\) to \(K'\) (still sitting inside \(B_j^\sharp\)) must meet \(\{\alpha\}\cup(C\setminus\{y_j\})\) by the same case analysis as Theorem 3.12, giving a separator of \(G-v\) of order \(5<6\le\kappa(G-v)\), contradiction.  

All branches contradict. Hence residual contact off \(K\) holds. ∎

### Theorem 3.16 (\(W_{s=1}\) — **proved**)
Under Hypotheses 0.1 for \(t=7\), no hard-core RPC with \(s=1\) exists.

**Proof.**  
1. Corollary 3.3: some \(\alpha\in L\) is a pure-\((R1)\) cutvertex of \(G[B_1]\).  
2. Lemma 3.8: some component \(K\) meets \(N(v)\) and \(C\).  
3. Theorem 3.15: residual contact off \(K\) holds.  
4. Lemma 3.5(3): \(\operatorname{Priv}(K,\alpha)\neq\emptyset\).  
5. Theorem 3.14: \(\Phi\) rises.  

Contradiction. ∎

### Remark 3.17 (What was wrong before, and what fixes it)
| Old claim | Verdict |
|-----------|---------|
| Mixed \(N(v)\)–\(C\) sides free because private targets are non-contact | **False** |
| Other fan paths contain the cutvertex portal | **False** |
| \(s=1\) impossible | **True**, via cut-edge repair + private-singleton bound + \(\kappa\)-separator in the \(K_5\) microcell |

---

## 4. Attempt on \(W_{s=5}\)

### Setup 4.1
\(s=5\), \(J=\{6\}\), \(C=B_6\) single non-contact bag. \(|L|\ge 7\). Multi-portal and multi-contact pigeonholes apply.

### Lemma 4.2
If \(|B_i\cap L|\ge 2\) then \(U_J(\alpha)=\emptyset\) for all \(\alpha\in B_i\cap L\).

**Proof.** Unique glue to whole \(C\) forbids a second portal in \(B_i\). ∎

### Theorem 4.3 (Closed subcells at \(s=5\) — **proved**)
The following cannot occur in a hard-core RPC at \(s=5\):
1. Multi-portal multi-contact bag with a non-cut portal having \(U_S=\emptyset\) (SPPA / Fact 0.6).
2. Cutvertex portal with a free \(N(v)\)–\(C\) component (Fact 0.7).
3. Contact-\((R3)\) with an absorbable leaf-Steiner hop through \(C\) ([RPC Thm 6.3](hadwiger_rpc_elimination.md)).

**Proof.** As indicated. ∎

### Theorem 4.4 (Residual structure — **classification only**)
Any remaining hard-core RPC at \(s=5\) is a **locked contact core**:
- every multi-portal bag’s portals are cutvertices and/or have nonempty \(U_S\);
- every \(C\)-meeting cut component carries a private edge into **another contact bag**;
- every contact-\((R3)\) detour uses only non-absorbable Steiners;
- pure-\((R2)\) second portals are trade-constrained.

**Proof.** Theorem 4.3 + hard-core definition. ∎

### Theorem 4.5 (\(W_{s=5}\) — **not proved**)
Emptiness of locked contact cores at \(s=5\) is open. In particular:
- singleton \(C=\{y\}\) with all portals adjacent to \(y\) and detours only through contact bags: open;
- mutual private-edge lock between two double-portal contact bags: open.

---

## 5. Implications

### Theorem 5.1 (Proved package)
1. \(W_{\mathrm{private}}\) for all \(t\ge 5\) under \(\delta\ge t\).  
2. \(W_{s=1}\) for \(t=7\).  
3. Free/SPPA/absorbable subcells at \(s=5\) empty; residual = locked contact core.

### Theorem 5.2 (Conditional \(\mathrm{HC}_7\))
If no locked contact core occurs for any \(s\in\{2,3,4,5\}\), then no hard-core RPC occurs for \(t=7\), hence no RPC (non-hard-core eliminated in [RPC §§3–6](hadwiger_rpc_elimination.md)), hence Lemma G for \(t=7\), hence \(\mathrm{HC}_7\).

**Proof.** Hybrid dichotomy + hard-core reduction + Theorem 3.16. ∎

### Theorem 5.3 (\(W_{\mathrm{SPPA}}\) full = Lemma G)
The unrestricted statement that every deficient \(\Phi\)-max model admits strongly private non-cut portal absorption is Lemma G and implies \(\mathrm{HC}_t\) for \(t\ge 7\). **Not proved here.** The structure theorem route ([structure note](hadwiger_structure_theorem.md)) does not eliminate RPCs and does not absorb these lemmas into \(\mathrm{HC}_t\) (apex additive gap).

### Coverage for \(t=7\)
| \(s\) | Status |
|------:|--------|
| 1 | **Eliminated** |
| 2,3,4 | Locked contact core **open** |
| 5 | Free subcells dead; locked residual **open** |

---

## 6. Checklist

| Item | Status |
|------|--------|
| Thm 1.3 — \(W_{\mathrm{private}}\) | **Proved** |
| Thm 3.2–Cor 3.3 — budget + cutvertex portals | **Proved** |
| Lem 3.6 — cut-edge repair | **Proved** |
| Lem 3.8 — fan mixed components | **Proved** |
| Thm 3.9 — single-private absorption | **Proved** |
| Thm 3.12 — \(K_5\) double-private separator | **Proved** |
| Thm 3.14–3.16 — multi-private + residual contact + \(W_{s=1}\) | **Proved** |
| Thm 4.3 — closed \(s=5\) subcells | **Proved** |
| Full \(W_{s=5}\) / locked cores / \(\mathrm{HC}_7\) | **Open** |

---

## 7. Final verdict

**Proved.** \(W_{\mathrm{private}}\); \(W_{s=1}\) for \(t=7\) (cut-edge repair + private calculus + \(\kappa\)-separator); free subcells at \(s=5\).

**Not proved.** Locked contact cores for \(s\in\{2,3,4,5\}\); unrestricted \(W_{\mathrm{SPPA}}\)/Lemma G; \(\mathrm{HC}_7\).

**Residual for \(\mathrm{HC}_7\) on this track:**
\[
\boxed{G_7^{\mathrm{lock}}:\ \text{no locked contact core for }s\in\{2,3,4,5\}
\text{ under the \(t=7\) CE package.}}
\]
The case \(s=1\) is removed from the residual.

---

*End of note.*
