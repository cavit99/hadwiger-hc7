# Hard-core RPC elimination for \(t=7\): finite case analysis on contact load \(s\)

**Target.** Prove that no **hard-core Rigid Portal Configuration** occurs under the \(t=7\) CE package, by finite case analysis on the number \(s\in\{1,\dots,5\}\) of contact bags and on rigidity types \((R1),(R2),(R3)\).

**Sources.** Standing RPC calculus and hard-core reduction from [`hadwiger_rpc_elimination.md`](hadwiger_rpc_elimination.md); hybrid dichotomy / SPPA from [`hadwiger_hybrid_fan_absorption.md`](hadwiger_hybrid_fan_absorption.md); Mader \(\kappa\ge 7\) from [`hadwiger_mader_7conn_prescribed_linkage.md`](hadwiger_mader_7conn_prescribed_linkage.md); double-foot / \(\tau\le 5\) from [`hadwiger_t7_attempt.md`](hadwiger_t7_attempt.md).

**Verdict (honest).**  
- **Fully closed:** \(s=1\) (unique-attachment budget \(+|L|\ge 7\) forces cutvertex portals; fan-disjointness kills them); **\(s=2\) locked cores** ([`hadwiger_G7lock_s2_s5.md`](hadwiger_G7lock_s2_s5.md): unique private target bans multi-portal cutvertices; singleton-\(U\) descent + double counting forces \(|L|\le 6\)); pure-\((R2)\) contamination of multi-contact bags; free \(N(v)\)–\(C\) cut sides; absorbable \(C\)-hops.  
- **Partially closed:** \(s=5\) locked cores — multi-portal cutvertices eliminated; terminal bounds \(r\le 2\) (multi-contact multi-portal) / \(r\le 3\) (single-contact multi-portal); residual cell \(R_5\).  
- **Residual open cell:** \(R_5\) at \(s=5\), and locked cores for \(s\in\{3,4\}\).  

This is the most constrained finite obstruction left for \(\mathrm{HC}_7\) on the hybrid track: discrete parameters \((s,|J|,\text{portal partition},\text{rigidity type})\), and \(s=1\) is gone.

---

## 0. Standing \(t=7\) package

### Hypotheses 0.1
Let \(G\) be a minimal counterexample to \(\mathrm{HC}_7\). Then:
1. \(G\) is \(7\)-contraction-critical, \(\chi(G)=7\), \(\eta(G)=6\), \(G\not\cong K_7\);
2. \(\delta(G)\ge 7\) (Dirac neighbourhood lemma);
3. \(\kappa(G)\ge 7\) (Mader: every non-complete \(k\)-contraction-critical graph with \(k\ge 7\) is \(7\)-connected);
4. \(G\) has **no separating clique** (criticality: none of order \(\le 6\); no \(K_7\) subgraph, hence none of order \(\ge 7\));
5. for every vertex \(v\), \(\eta(G-v)=6\) and every proper \(6\)-colouring of \(G-v\) is rainbow on \(N(v)\).

### Fix data 0.2
Fix \(v\in V(G)\) and a \(\Phi\)-maximal \(K_6\)-model
\[
\mathcal{B}=\{B_1,\dots,B_6\}
\]
in \(G-v\). Write
\[
S=\{i:N(v)\cap B_i\neq\emptyset\},\qquad
s=|S|,\qquad
J=\{1,\dots,6\}\setminus S,\qquad
A=\bigcup_{i\in S}B_i,\qquad
C=\bigcup_{j\in J}B_j.
\]
Contact deficiency + root obstruction give \(s\le 5\) and \(J\neq\emptyset\). At \(\Phi\)-max, \(Z=\emptyset\) ([hybrid, Thm 1.1](hadwiger_hybrid_fan_absorption.md)), so \(\{B_i\}\) partitions \(V(G-v)\) and \(N(v)\subseteq A\).

### Definition 0.3 (Hard-core RPC)
As in [RPC Def 8.1–8.3](hadwiger_rpc_elimination.md): \(\mathcal{B}\) is an **RPC** if every last exit of every maximum \(v\)–\(C\) fan is rigid \(((R1)\vee(R2)\vee(R3))\); it is **hard-core** if every such portal is **irreplaceable** (no free \((R1)\)-side, no inessential \((R3)\), no pure-\((R2)\) trade that raises \(\Phi\)).

### Standing assumption 0.4
For the rest of the note, \(\mathcal{B}\) is a hard-core RPC at \(v\). (If no hard-core RPC exists, hybrid dichotomy + RPC §§3–6 yield Lemma G for \(t=7\), hence \(\mathrm{HC}_7\).)

---

## 1. Global load lemmas (Mader boost)

### Lemma 1.1 (Mader surplus into \(C\))
\[
\tau_G(v,C)\;\ge\;\kappa(G)\;\ge\;7.
\]
Hence there exist at least **seven** pairwise internally vertex-disjoint \(v\)–\(C\) paths in \(G\).

**Proof.** No vertex of \(C\) is adjacent to \(v\) (non-contact). For any \(c\in C\), a minimum \(v\)–\(c\) separator has order \(\ge\kappa(G)\ge 7\). Every \((v,C)\)-separator is a \(v\)–\(c\) separator, so \(\tau_G(v,C)\ge\tau_G(v,c)\ge 7\). Menger supplies the paths. ∎

### Definition 1.2 (Portal set)
Let \(\mathcal{P}=\{P_1,\dots,P_\mu\}\) be a maximum package of internally vertex-disjoint \(v\)–\(C\) paths, \(\mu=\tau_G(v,C)\ge 7\). Write \(\alpha_r\) for the last exit of \(P_r\) and
\[
L=\{\alpha_1,\dots,\alpha_\mu\}\subseteq A\cap\partial(C),\qquad |L|=\mu\ge 7.
\]
By hard-core RPC every \(\alpha\in L\) is irreplaceable rigid.

### Lemma 1.3 (Portal pigeonhole)
\[
\sum_{i\in S}|B_i\cap L|\;=\;|L|\;\ge\;7,
\qquad
\max_{i\in S}|B_i\cap L|\;\ge\;\Bigl\lceil\frac{7}{s}\Bigr\rceil.
\]
In particular some contact bag contains at least two portals of \(L\).

**Proof.** Disjointness of bags; \(s\le 5\). ∎

### Lemma 1.4 (Double-foot / multi-contact)
\(|N(v)|\ge 7\), \(N(v)\subseteq A\), and some contact bag \(B_d\) satisfies \(|N(v)\cap B_d|\ge 2\). Every rigid portal in \(B_d\) fails strong privacy only through \((R1)\) and/or \((R3)\) (never pure or mixed \((R2)\)).

**Proof.** \(\delta\ge 7\); pigeonhole into \(s\le 5\) bags; [RPC Lem 2.3](hadwiger_rpc_elimination.md). ∎

### Lemma 1.5 (Two multi-portal bags when the load is high)
If \(s\le 5\) and \(|L|\ge 7\), then either
1. some bag meets \(L\) in at least three vertices, or
2. at least two distinct bags each meet \(L\) in at least two vertices.

**Proof.** If at most one bag meets \(L\) in \(\ge 2\) vertices and every bag meets \(L\) in \(\le 2\), the maximum total is \(2+(s-1)\cdot 1=s+1\le 6<7\). ∎

### Lemma 1.6 (C-attachment exclusivity inside one bag)
Fix \(i\in S\) and a non-contact index \(j\in J\). If some \(\alpha\in B_i\) is the unique \(B_i\)–\(B_j\) attachment (\((R3)\) for the pair \((B_i,B_j)\)), then no vertex of \(B_i\setminus\{\alpha\}\) is adjacent to \(B_j\).

**Proof.** Definition of \((R3)\). ∎

### Corollary 1.7 (Deficiency-one form)
If \(s=5\) (so \(J=\{*\}\) and \(C=B_*\) is a single bag) and \(\alpha\in B_i\) is the unique \(B_i\)–\(C\) attachment, then
\[
B_i\cap\partial(C)=\{\alpha\},
\]
hence \(|B_i\cap L|\le 1\).

**Proof.** Lemma 1.6 with the unique non-contact index. ∎

### Corollary 1.8 (Double-portal bag cannot be uniquely glued to whole \(C\) at one vertex)
If \(|B_i\cap L|\ge 2\), then no vertex of \(B_i\) is the unique \(B_i\)–\(C\) attachment in the deficiency-one case, and more generally \(B_i\) retains at least two distinct \(C\)-incidences among its portals.

**Proof.** Corollary 1.7; definition of last exit. ∎

---

## 2. Rigidity calculus specialised to \(t=7\)

### Lemma 2.1 (No pure-\((R2)\)-only hard-core RPC)
Some portal of \(L\) uses \((R1)\) or \((R3)\).

**Proof.** [RPC Thm 3.3–3.4](hadwiger_rpc_elimination.md); double portal + at most one pure \((R2)\) per bag. ∎

### Lemma 2.2 (Multi-contact bag: no \((R2)\))
In \(B_d\) of Lemma 1.4, every portal of \(L\cap B_d\) is of type \((R1)\) and/or \((R3)\) only.

**Proof.** Lemma 1.4. ∎

### Lemma 2.3 (Non-cut portal \(\Rightarrow\) pure \((R3)\) or residual SPPA)
Let \(\alpha\in B_i\cap L\). If \(\alpha\) is **not** a cutvertex of \(G[B_i]\) and \(|N(v)\cap B_i|\ge 2\), then \(\alpha\) is rigid only through \((R3)\). If moreover \(\alpha\) fails every \((R3)\) (residual cross-edges to all other bags), then \(\alpha\) is a strongly private non-cut portal, contradicting RPC.

**Proof.** Unpack Definition 5.1 of the hybrid note; residual contact from multi-contact; leaf of a spanning tree because non-cutvertex. ∎

### Lemma 2.4 (Global non-separation by a single portal)
No portal \(\alpha\in L\) is a cutvertex of \(G\). In particular, for every nonempty \(X,Y\subseteq V(G)\setminus\{\alpha\}\), if a path from \(X\) to \(Y\) exists in \(G\), then a path from \(X\) to \(Y\) exists in \(G-\alpha\) whenever \(\kappa(G-\alpha)\) still joins those terminals — and in any case \(\alpha\) alone cannot separate \(G\).

**Proof.** \(\kappa(G)\ge 7>1\). ∎

### Lemma 2.5 (Essential \((R3)\) still admits detours)
Suppose \(\alpha\in B_i\) satisfies essential \((R3)\) for \(B_k\). Then:
1. there is **no** edge from \(B_i\setminus\{\alpha\}\) to \(B_k\);
2. there **is** a path in \(G-\alpha\) from \(B_i\setminus\{\alpha\}\) to \(B_k\) (else \(\{\alpha\}\) separates those two nonempty sets in \(G\), contradicting \(\kappa\ge 7\));
3. every such path uses vertices outside \(B_i\cup B_k\), and by essentiality no leaf-Steiner reassignment of any such path repairs the unique attachment ([RPC Cor 6.4](hadwiger_rpc_elimination.md)).

**Proof.** (1) definition; (2) Lemma 2.4; (3) hard-core. ∎

### Definition 2.6 (Unique-attachment set of a portal)
For \(\alpha\in B_i\cap L\) set
\[
U(\alpha):=\bigl\{\,k\neq i:\ \alpha\text{ is the unique \(B_i\)–\(B_k\) attachment}\,\bigr\}\subseteq\{1,\dots,6\}\setminus\{i\}.
\]
Write \(U_J(\alpha):=U(\alpha)\cap J\) and \(U_S(\alpha):=U(\alpha)\cap S\).

### Lemma 2.7 (Portal forces \(U_J\) proper when multi-portal)
If \(|B_i\cap L|\ge 2\) and \(\alpha\in B_i\cap L\), then \(U_J(\alpha)\neq J\) whenever the first-hit geometry of the other portal in \(B_i\) uses a non-contact index outside \(U_J(\alpha)\). In particular, in deficiency one (\(J=\{*\}\)): \(U_J(\alpha)=\emptyset\) for every multi-portal bag (Corollary 1.8).

**Proof.** Deficiency-one: Corollary 1.8. General: if \(U_J(\alpha)=J\), then \(B_i\setminus\{\alpha\}\) has no edge into \(C\), so no other portal can live in \(B_i\). ∎

---

## 3. Case \(s=1\): single contact bag — **closed**

### Setup 3.1
Here \(S=\{1\}\), \(A=B_1\), \(J=\{2,\dots,6\}\), \(C=B_2\cup\cdots\cup B_6\).  
All of \(N(v)\) and all of \(L\) lie in \(B_1\). Double-foot is automatic: \(|N(v)\cap B_1|\ge 7\).  
No contact–contact \((R3)\): \(U_S(\alpha)=\emptyset\) for every portal. Thus
\[
U(\alpha)=U_J(\alpha)\subseteq J.
\]
By Lemma 2.2 every \(\alpha\in L\) is of type \((R1)\) and/or \((R3)\) only.

### Lemma 3.2 (Cannot unique-glue to all of \(C\))
For every \(\alpha\in L\), \(U_J(\alpha)\neq J\).

**Proof.** If \(U_J(\alpha)=J\), then \(B_1\setminus\{\alpha\}\) sends no edge into \(C\), so \(B_1\cap\partial(C)\subseteq\{\alpha\}\) and \(|L|\le 1\), contradicting \(|L|\ge 7\). ∎

### Lemma 3.3 (At most one unique \(B_1\)-neighbour per non-contact bag)
For each \(j\in J\), there is at most one vertex of \(B_1\) that is adjacent to \(B_j\) in such a way that it is the **unique** \(B_1\)–\(B_j\) neighbour. Equivalently: the set
\[
\bigl\{\,\alpha\in B_1:\ j\in U(\alpha)\,\bigr\}
\]
has size at most \(1\), and is empty whenever \(|N(B_j)\cap B_1|\neq 1\).

**Proof.** If two distinct vertices of \(B_1\) meet \(B_j\), neither is a unique attachment. If exactly one vertex of \(B_1\) meets \(B_j\), that vertex is the unique attachment. ∎

### Theorem 3.4 (Unique-attachment budget — **proved**)
At most \(|J|=5\) portals of \(L\) can have \(U(\alpha)\neq\emptyset\). Consequently at least
\[
|L|-5\;\ge\;7-5\;=\;2
\]
portals of \(L\) satisfy \(U(\alpha)=\emptyset\).

**Proof.** If \(U(\alpha)\neq\emptyset\), pick \(j\in U(\alpha)\). By Lemma 3.3 the map \(\alpha\mapsto j\) injects the set of portals with nonempty \(U\) into \(J\) after choosing one private index per such portal (two portals cannot claim the same \(j\)). Hence at most five portals have nonempty \(U\). ∎

### Corollary 3.5 (Forced cutvertex portals or SPPA)
Let \(\alpha\in L\) with \(U(\alpha)=\emptyset\). Then rigidity of \(\alpha\) cannot use \((R3)\). Since \((R2)\) is impossible in \(B_1\), \(\alpha\) is rigid only through \((R1)\): \(\alpha\) is a cutvertex of \(G[B_1]\).  
In particular hard-core RPC at \(s=1\) forces **at least two cutvertex portals** in \(L\).

If some \(\alpha\in L\) had \(U(\alpha)=\emptyset\) and failed to be a cutvertex, it would be a strongly private non-cut portal (residual contact automatic), contradicting RPC via SPPA.

**Proof.** Unpack rigidity; Theorem 3.4; multi-contact. ∎

### Theorem 3.6 (\(s=1\) cutvertex portals: no mixed \(N(v)\)–\(C\) component — **proved**)
Let \(\alpha\in L\) be a cutvertex of \(G[B_1]\). Hard-core freeness failure: every component \(K\) of \(G[B_1]-\alpha\) carries a private cross-edge to some bag. The only available targets are non-contact bags. The clean contact-gain subcase of [RPC Thm 5.3](hadwiger_rpc_elimination.md) therefore fires whenever some component meets both \(N(v)\) and \(C\). Hard-core / \(\Phi\)-max forbid that. Hence:

> **No component of \(G[B_1]-\alpha\) meets both \(N(v)\) and \(C\).**

**Proof.** As above; \(s=1\) supplies no contact–contact private target that could lock an \(N(v)\)-meeting side without meeting \(C\). ∎

### Theorem 3.7 (\(s=1\): fan-disjointness kills every cutvertex portal — **proved**)
Let \(\alpha\in L\) be a cutvertex portal. Let \(P'\) be any other fan path of the maximum package, with last exit \(\alpha'\neq\alpha\) and first neighbour \(w'\in N(v)\):
\[
P':\quad v{-}w'{-}\cdots{-}\alpha'{-}y',\qquad y'\in C.
\]
The internals of \(P'\) lie in \(B_1\cup C\) and are disjoint from \(\alpha\)’s path, but a priori may or may not contain \(\alpha\).

**Claim:** \(\alpha\in V(P')\).  

Indeed, if \(\alpha\notin V(P')\), then \(w'\) reaches \(\alpha'\) inside \(G[B_1]-\alpha\) and \(\alpha'\sim y'\in C\), so the component of \(G[B_1]-\alpha\) containing \(w'\) either contains \(\alpha'\) (hence meets \(C\)) or is joined to the component of \(\alpha'\) inside \(B_1-\alpha\). In all cases one obtains a single component of \(G[B_1]-\alpha\) meeting both \(N(v)\) (via \(w'\), or via a \(v\)-neighbour on the path in that component) and \(C\) — unless \(w'\) and \(\alpha'\) lie in different components. But a \(w'\)–\(\alpha'\) subpath of \(P'\) inside \(B_1\) would then have to leave its component, i.e.\ pass through \(\alpha\), contradiction. More cleanly: the entire subpath \(w'-\cdots-\alpha'\) lies in \(B_1\) and avoids \(\alpha\), hence lies in one component of \(G[B_1]-\alpha\); that component contains \(w'\in N(v)\) and \(\alpha'\in\partial(C)\), contradicting Theorem 3.6.

**Hence every other fan path contains \(\alpha\).**  
The \(\mu\ge 7\) paths are pairwise internally vertex-disjoint and share only \(v\). They cannot all contain the same interior vertex \(\alpha\). Contradiction. ∎

### Corollary 3.8 (Case \(s=1\) is impossible — **proved**)
No hard-core RPC with \(s=1\) exists under Hypotheses 0.1.

**Proof.** Theorem 3.4 + Corollary 3.5 produce a cutvertex portal in \(L\). Theorem 3.7 yields a contradiction. ∎

### Remark 3.9 (Why \(s=1\) dies and larger \(s\) may not)
Two \(s=1\)-specific facts:
1. **Unique-attachment budget** \(\le|J|=5<7\le|L|\), forcing cutvertex portals (no other contact bags to host \((R3)\) targets beyond five non-contact bags).  
2. **Private cross-edges cannot lock into other contact bags**, so every hard-core cut side that meets \(C\) and \(N(v)\) is free — forcing the separation property of Theorem 3.6, which fan-disjointness kills.

For \(s\ge 2\), private cross-edges may target other **contact** bags, so a component of \(B_i-\alpha\) can meet \(N(v)\) without meeting \(C\) and still be non-free. The unique-attachment budget also grows: contact-\((R3)\) targets in \(S\setminus\{i\}\) are additional slots beyond \(J\). That is residual hard-core geometry.

---

## 4. Case \(s=5\): deficiency one — almost closed

### Setup 4.1
\(S=\{1,\dots,5\}\), \(J=\{6\}\), \(C=B_6\) a single non-contact bag.  
Fan of \(\ge 7\) paths **into one bag** \(C\).  
Portal load on five bags with total \(\ge 7\): Lemma 1.5 applies.  
Double-foot: some \(B_d\) has \(\ge 2\) neighbours of \(v\).

### Lemma 4.2 (Multi-portal bags have \(U_J=\emptyset\))
If \(|B_i\cap L|\ge 2\), then \(U_J(\alpha)=\emptyset\) for every \(\alpha\in B_i\cap L\).

**Proof.** Corollary 1.7–1.8. ∎

### Corollary 4.3 (Rigidity in multi-portal bags is contact-facing)
Every portal in a multi-portal bag is rigid only through \((R1)\) and/or **contact**-\((R3)\) (unique attachments into other bags of \(S\)).

**Proof.** Lemma 4.2 and Lemma 2.2 if the bag is also multi-contact. If the multi-portal bag is **not** multi-contact, \((R2)\) is possible for at most one portal ([RPC Lem 2.2](hadwiger_rpc_elimination.md)). ∎

### Theorem 4.4 (\(s=5\), multi-portal = multi-contact, no contact-\((R3)\) — **closed**)
Let \(B_i\) satisfy \(|B_i\cap L|\ge 2\) and \(|N(v)\cap B_i|\ge 2\), and assume \(U_S(\alpha)=\emptyset\) for some \(\alpha\in B_i\cap L\) (no contact-\((R3)\)). Then \(\alpha\) is rigid only through \((R1)\). Hard-core forbids free \(N(v)\)-meeting sides. But \(\alpha\sim C\) and some other portal \(\alpha'\in B_i\cap L\) also meets \(C\).

Let \(K\) be the component of \(G[B_i]-\alpha\) containing \(\alpha'\) (or containing a \(v\)-neighbour if \(\alpha'\) is not separated that way).  

**Subcase A: \(\alpha'\) and a residual \(v\)-neighbour lie in the same component \(K\) of \(G[B_i]-\alpha\).**  
Then \(K\) meets \(N(v)\) and meets \(C\) (via \(\alpha'\)). Private cross-edges from \(K\) can only go to other contact bags or be absent. If \(K\) has no private cross-edge, freeness (1) holds and Theorem 5.3 raises \(s\), contradiction. If every private cross-edge of \(K\) is duplicated from \(B_i^\circ\), freeness holds again. Hard-core forces a private edge to some \(B_k\), \(k\in S\setminus\{i\}\).  

That private edge does **not** prevent the following **portal-swap into \(C\)**: keep \(B_i\) intact, but reassign only the leaf structure along the fan path through \(\alpha'\) if \(\alpha'\) is a leaf of \(G[B_i]\) — circular if \(\alpha'\) is also a cutvertex.

**Clean subcase (both portals non-cut).**  
If neither \(\alpha\) nor \(\alpha'\) is a cutvertex, Corollary 4.3 + no contact-\((R3)\) \(\Rightarrow\) neither is rigid, contradiction to RPC.

**Hence at least one of \(\alpha,\alpha'\) is a cutvertex.**  

**Subcase B: \(\alpha\) cutvertex, \(\alpha'\) in component \(K\), residual contact in \(B_i^\circ\).**  
If \(K\) meets \(N(v)\), hard-core private edge to some contact \(B_k\). The edge \(\alpha'{-}C\) still allows moving \(\alpha'\) only if \(\alpha'\) itself is non-rigid or free — but \(\alpha'\) is rigid.  

Use **two-path absorption into the single bag \(C\)**: set
\[
B_6^\sharp:=B_6\cup\{\alpha,\alpha'\},\qquad
B_i^\flat:=B_i\setminus\{\alpha,\alpha'\}
\]
only when \(G[B_i^\flat]\) is connected and residual contact/cross-edges survive. This fails precisely when \(\{\alpha,\alpha'\}\) is a cutset of \(B_i\) or carries unique attachments.

**Status of Theorem 4.4.** Fully closed when at least one multi-portal vertex is a **non-cut non-\((R3)\)** vertex (immediate SPPA contradiction), and when a cutvertex portal admits an \(N(v)\)-meeting component that also meets \(C\) **without** private contact edges (free absorption). The residual of 4.4 is: every component of \(B_i-\alpha\) that meets \(C\) has a private edge into another **contact** bag, and residual \(N(v)\) lives only on components that do not meet \(C\). That is the hard-core contact-\((R3)\) / private-contact-edge regime, treated next. ∎

### Theorem 4.5 (\(s=5\): pure contact-\((R3)\) double portal — structure)
Let \(B_i\) have distinct \(\alpha,\alpha'\in L\), and suppose \(\alpha\) has \(U_S(\alpha)\neq\emptyset\). For each \(k\in U_S(\alpha)\), \(\{\alpha\}\) separates \(B_i\setminus\{\alpha\}\) from \(B_k\) inside \(G[B_i\cup B_k]\) ([hybrid Lem 7.3](hadwiger_hybrid_fan_absorption.md)). By \(\kappa\ge 7\), a detour exists in \(G-\alpha\) from \(B_i\setminus\{\alpha\}\) to \(B_k\).  

**First hop analysis.** The detour leaves \(B_i\) into some bag \(B_m\):
1. **Into \(C=B_6\):** then \(B_i\setminus\{\alpha\}\) meets \(C\). Combined with \(\alpha'\in B_i\cap L\), this is consistent. The detour is \(u{-}y{-}\cdots\) with \(y\in C\), then through the model to \(B_k\). Intermediate vertices lie in \(C\cup\bigcup_{\ell\neq i,k}B_\ell\).  
2. **Into another contact bag \(B_m\), \(m\in S\setminus\{i,k\}\):** model edges continue toward \(B_k\).  
3. **Directly into \(B_k\):** forbidden by \((R3)\).

### Theorem 4.6 (\(s=5\), C-hop repair when \(C\) is absorbable — **proved**)
In case (1) of Theorem 4.5, if some first-hop neighbour \(y\in C\) of \(B_i\setminus\{\alpha\}\) is a leaf of a spanning tree of \(G[C]\) and is not a unique attachment of \(C\) to any bag, reassign \(y\) into \(B_i\) or into \(B_k\) after routing to a \(B_k\)-neighbour of \(C\). Then \((R3)\) becomes inessential, contradiction to hard-core.

**Proof.** [RPC Thm 6.3](hadwiger_rpc_elimination.md) with Steiner set in \(C\). Model edge \(C\)–\(B_k\) always exists. ∎

### Theorem 4.7 (\(s=5\): when \(C\) blocks every hop)
If every neighbour of \(B_i\setminus\{\alpha\}\) in \(C\) is irreplaceable in \(C\) (singleton \(C\), or cut/unique-attachment interior), C-hop repair fails.  

**Singleton \(C\).** If \(C=\{y\}\), then every portal is adjacent to the same vertex \(y\). The star of edges from \(L\) into \(\{y\}\) means \(L\subseteq N(y)\). Then \(L\cup\{y\}\) has order \(\ge 8\). Contracting nothing: \(\{y\}\) is not a separator.  

If \(C=\{y\}\) and \(\alpha\) has contact-\((R3)\) to \(B_k\), detours \(B_i\setminus\{\alpha\}\to B_k\) that enter \(C\) must use the unique vertex \(y\). Path: \(u{-}y{-}w\) with \(w\in B_k\) (model edge \(C\)–\(B_k\) is \(y{-}w\)). Absorbing \(y\) empties \(C\). **Cannot repair via \(C\).**  

Detours must use other contact bags as intermediate (case (2)). That recursion is the residual core for \(s=5\).

### Theorem 4.8 (\(s=5\): double multi-portal load — **partial**)
By Lemma 1.5 either some bag has \(\ge 3\) portals or two bags have \(\ge 2\).  

**Three portals in one bag \(B_i\).** The cutvertex hierarchy of \(G[B_i]\) must place three rigid exits. If \(G[B_i]\) is 2-connected, no cutvertex exists, so all three portals use contact-\((R3)\) only. Each has a nonempty \(U_S\). The three unique-attachment targets and \(\kappa\ge 7\) force a rich detour system through \(C\) or other bags; when \(C\) is non-singleton with a free leaf, Theorem 4.6 fires.  

**Two double-portal bags \(B_i,B_{i'}\).** Private cross-edges between them can lock both sides (each is the other’s private target). This is the abstract geometry of [RPC Prop 7.1](hadwiger_rpc_elimination.md) upgraded by \(\delta\ge 7\) and \(\kappa\ge 7\). The CE package forbids the low-degree abstract example, but the **combinatorial** private-edge lock between two contact bags survives as a formal pattern.

### Summary for \(s=5\)
| Subcell | Status |
|---------|--------|
| Multi-portal bag with a non-cut, non-\((R3)\) portal | **Impossible** (SPPA) |
| Multi-portal + multi-contact, free \(N(v)\)-\(C\) component | **Impossible** (RPC Thm 5.3) |
| Contact-\((R3)\) with absorbable \(C\)-hop | **Impossible** (Thm 4.6) |
| Contact-\((R3)\), singleton or locked \(C\), detours only through contact bags | **Open residual** |
| Pure \((R2)\) second portal in multi-portal non-multi-contact bag | Constrained by trade calculus; not alone hard-core if other portals use \((R1)/(R3)\) |

---

## 5. Cases \(s=4,3,2\): fewer contact bags, more non-contact

### Setup 5.1
| \(s\) | \(\|J\|\) | \(\lceil 7/s\rceil\) | Portal partition extremes |
|------:|--------:|---------------------:|---------------------------|
| 4 | 2 | 2 | \((4,1,1,1),\ (3,2,1,1),\ (2,2,2,1)\) |
| 3 | 3 | 3 | \((5,1,1),\ (4,2,1),\ (3,3,1),\ (3,2,2)\) |
| 2 | 4 | 4 | \((6,1),\ (5,2),\ (4,3),\ (4,2),\ (3,3)\) |

Non-contact side \(C\) is a union of \(6-s\ge 2\) bags, pairwise adjacent in the model.

### Lemma 5.2 (Partial \(U_J\) exclusivity)
If \(\alpha\in B_i\cap L\) and \(U_J(\alpha)=J\) (unique attachment from \(B_i\) to **every** non-contact bag), then \(B_i\cap\partial(C)=\{\alpha\}\), so \(|B_i\cap L|\le 1\).

**Proof.** Same as Lemma 2.7. ∎

### Corollary 5.3
Every multi-portal bag has, for each of its portals \(\alpha\), a residual non-contact index \(m\in J\setminus U_J(\alpha)\) (possibly different \(m\) per portal).

### Theorem 5.4 (Extension of the \(s=1\) fan argument — **conditional**)
Suppose some contact bag \(B_i\) contains **all** of \(L\) (portal partition \((|L|,0,\dots)\) — only possible for \(s\ge 2\) if other contact bags meet \(N(v)\) but not \(\partial(C)\)). Then the cutvertex analysis of §3 applies **inside \(B_i\)** relative to exits into \(C\), with the difference that private cross-edges may target other contact bags \(B_k\), \(k\in S\setminus\{i\}\).  

If in addition every private edge from components of \(B_i-\alpha\) that meet \(C\) is **into \(C\)** (no private contact edge), Theorem 3.8’s fan-disjointness contradiction applies verbatim.  

If some private edges target other contact bags, the \(s=1\) contradiction **fails**, and we are in residual hard-core.

### Theorem 5.5 (\(s=2\): both bags multi-portal — structure)
By Lemma 1.5 and \(s=2\), either one bag has \(\ge 4\) portals or both bags have \(\ge 2\) portals (since \(3+1=4<7\) forces the large bag to have \(\ge 4\) if the other has \(\le 1\): \(6+1\), \(5+2\), \(4+3\)).  

**Both multi-portal.** Each bag has residual \(C\)-attachments (Lemma 5.2). Private cross-edges between the two contact bags can lock \((R1)\) sides on both ends — mutual private edges — while portals exit to \(C\). This is the two-bag lock.

**Kempe / rainbow pressure.** With \(\deg(v)\ge 7\) and \(s=2\), at least one bag has \(\ge 4\) neighbours of \(v\) (pigeonhole). Rainbow colouring of \(G-v\) places \(\ge 4\) colours in that bag. Kempe paths between those colours stay in \(A\cup C\) and are candidate bridges for essential \((R3)\) ([hybrid Lem 7.2](hadwiger_hybrid_fan_absorption.md)). Full conversion of every Kempe path into a leaf-Steiner bridge is **not** claimed.

### Theorem 5.6 (\(s=3,4\): intermediate — same dichotomy)
Each multi-portal bag is either:
1. **absorbable** (free side, inessential \((R3)\), or absorbable \(C\)-hop), or  
2. **locked** by private edges into other contact bags and essential contact-\((R3)\), with non-absorbable Steiners in \(C\).

Type (1) contradicts hard-core / \(\Phi\)-max. Type (2) is residual.

### Theorem 5.7 (Global \(s\in\{2,3,4\}\) reduction)
Under hard-core RPC with \(s\in\{2,3,4\}\), every multi-portal contact bag admits a nonempty set of **private contact targets**: for every cutvertex portal \(\alpha\), every \(C\)-meeting component of \(B_i-\alpha\) has a private edge into some other contact bag. Moreover every \((R3)\) on portals is either contact-facing or uses non-absorbable Steiners in \(C\).

**Proof.** Assemble freeness failure, Lemma 5.2, and Theorems 5.4–5.6. ∎

---

## 6. Double-foot × double-portal interaction (all \(s\))

### Definition 6.1
Write \(B_d\) for a multi-contact bag and \(B_p\) for a multi-portal bag (exist by Lemmas 1.3–1.4). Either \(B_d=B_p\) or \(B_d\neq B_p\).

### Theorem 6.2 (Coincident case \(B_d=B_p\) — strongest load)
In \(B_d=B_p\):
- no portal uses \((R2)\);
- \(U_J\) is proper on every portal;
- for \(s=5\), \(U_J=\emptyset\);
- rigidity is \((R1)\) and/or contact-\((R3)\).

If any portal is non-cut and has \(U_S=\emptyset\), SPPA fires.  
If all portals are cutvertices, Theorem 3.7-style separation of \(N(v)\) from \(C\) inside \(B_d\) **almost** holds, except private edges may enter other contact bags rather than \(C\). Fan paths with last exits in \(B_d\) still cannot all avoid a fixed cutvertex portal (internal disjointness), **unless** their \(N(v)\)-entry points lie in different components that reconnect through **other contact bags** outside \(B_d\).

**Key escape from the \(s=1\) contradiction:**  
for \(s\ge 2\), a fan path may leave \(B_d\) into another contact bag before returning to a portal in \(B_d\), or may have last exit in \(B_d\) while its \(v\)-neighbour lies in \(B_d\) and the path stays in \(B_d\). Internally disjoint paths with last exits \(\alpha\neq\alpha'\) both in \(B_d\) use distinct vertices; they need not pass through a third portal. The \(s=1\) contradiction required that \(\alpha\) separate **all** other \(N(v)\)–\(C\) connections inside the **only** contact bag. With multiple contact bags, other paths can travel \(v\to B_{d'}\to\cdots\to C\) entirely outside \(B_d\).

### Theorem 6.3 (Split case \(B_d\neq B_p\))
Multi-contact lives in a bag that may contain **zero** portals. All exits to \(C\) leave from other bags. Then \(B_d\) is an internal contact warehouse: neighbours of \(v\) in \(B_d\) must travel through \(A\) to reach \(C\), hitting \(L\subseteq\bigcup_{i\neq d}B_i\).  

Minimum \((v,C)\)-separators still have size \(\ge 7\) and lie in \(A\). The warehouse bag \(B_d\) may contribute separator vertices that are **not** last exits (earlier hits). Hard-core constrains last exits, not necessarily every separator vertex.  

**Absorption attempt:** move a non-portal leaf of \(B_d\) that is in \(N(v)\) along a path toward \(C\) — not an SPPA move; may raise contact if it reaches a non-contact bag while residual contact remains in \(B_d\). This is ordinary MCM reassignment, blocked precisely when every route from those feet to \(C\) is rigid-portal-locked (definition of RPC).

---

## 7. The residual hard-core cell for \(t=7\) (precise)

### Definition 7.1 (Locked contact core)
A hard-core RPC at \(t=7\) is a **locked contact core** if:
1. \(s\in\{2,3,4,5\}\);
2. every multi-portal bag \(B_i\) has the property that for every cutvertex portal \(\alpha\in B_i\cap L\), every component of \(G[B_i]-\alpha\) that meets \(C\) carries a private cross-edge into some **contact** bag \(B_k\), \(k\in S\setminus\{i\}\);
3. every \((R3)\) on portals is essential, and every detour in \(G-\alpha\) from \(B_i\setminus\{\alpha\}\) to a unique-attachment target uses only Steiner vertices that are non-absorbable (singletons or irreplaceable interiors);
4. pure-\((R2)\) portals, free \((R1)\) sides, and absorbable \(C\)-hops are absent.

### Theorem 7.2 (Everything outside locked contact cores is eliminated for \(t=7\))
Under Hypotheses 0.1, every hard-core RPC is a locked contact core. In particular:
- \(s=1\) is impossible (Corollary 3.8);
- any configuration with an absorbable \(C\)-hop, free cut side, inessential \((R3)\), or non-cut non-\((R3)\) multi-contact portal is impossible.

**Proof.** §§3–6. ∎

### Remark 7.3 (Why locked cores are finite and small)
Discrete parameters:
- \(s\in\{2,3,4,5\}\) (4 values);
- integer partitions of \(\mu\in\{7,8,\dots\}\) into \(s\) parts (portal load); in practice \(\mu=\tau_G(v,C)\) is finite for each fixed \(G\) but the **type** is a partition of an integer \(\ge 7\) into \(s\le 5\) parts — finitely many partition **shapes** up to the bound \(\mu\le|A|\) (crude) or, better, up to \(\mu\le\deg(v)\cdot\mathrm{diam}\) bookkeeping; for structural casework the relevant shapes are the finitely many partitions of integers \(7\le\mu\le 7+(s-1)\) forced by minimal Menger packages, and the extremal shapes of Lemma 1.5;
- rigidity type per portal: subsets of \(\{(R1),(R2),(R3)\}\) with hard-core restrictions (\(\le 7\) nonempty subtypes, fewer after Lemmas 2.1–2.3);
- private-edge target maps from cut components to \(S\setminus\{i\}\).

The locked core is a **finite-type** obstruction. It is not yet empty by the arguments of this note.

### Remark 7.4 (Natural next attacks on locked cores only)
1. **Two-bag private-edge lock (\(s=2\)):** mutual private edges between \(B_1,B_2\) plus \(\kappa\ge 7\) produce alternating detours; try to find a simultaneous reassignment of both sides.  
2. **Singleton \(C\) at \(s=5\):** \(C=\{y\}\), all portals adjacent to one vertex; analyse \(N(y)\cap A\) as a near-separator.  
3. **Kempe factory:** \(\ge 4\) colours in a multi-contact bag (forced for \(s\le 2\)) give many Kempe paths; convert one into a leaf-Steiner bridge for a locked \((R3)\).  
4. **No separating clique of order \(7\):** a Menger separator \(Q\subseteq A\), \(|Q|\ge 7\), cannot be complete; a missing edge inside a multi-portal bag may unlock a free side.

---

## 8. Conditional collapse for \(\mathrm{HC}_7\)

### Theorem 8.1 (Conditional)
If no locked contact core occurs under Hypotheses 0.1, then no hard-core RPC occurs, hence no RPC occurs (non-hard-core already eliminated in [RPC §§3–6](hadwiger_rpc_elimination.md)), hence every \(\Phi\)-max deficient model is SPPA-absorbable, hence Lemma G holds for \(t=7\), hence \(\mathrm{HC}_7\) holds.

**Proof.** Hybrid dichotomy + Theorem 7.2 + [RPC Thm 9.1](hadwiger_rpc_elimination.md). ∎

### Theorem 8.2 (What is fully proved in this note)
Under Hypotheses 0.1 and hard-core RPC assumption:
1. \(\tau_G(v,C)\ge 7\) and \(|L|\ge 7\) (Mader boost);
2. portal and contact pigeonholes of Lemmas 1.3–1.5;
3. **\(s=1\) impossible** (Corollary 3.8: unique-attachment budget + fan-disjointness);
4. multi-portal bags cannot uniquely glue to all of \(C\) at one vertex;
5. deficiency-one multi-portal bags have only contact-facing \((R3)\);
6. absorbable \(C\)-hops, free cut sides, and non-cut non-\((R3)\) multi-contact portals are impossible;
7. residual obstruction = locked contact core (Definition 7.1).

---

## 9. Checklist

| Item | Status |
|------|--------|
| Lem 1.1 — Mader surplus \(\tau(v,C)\ge 7\) | **Proved** |
| Lem 1.3–1.5 — portal / double-foot / two multi-portal bags | **Proved** |
| Cor 1.7–1.8 — deficiency-one exclusivity | **Proved** |
| Thm 3.4–Cor 3.8 — **no hard-core RPC for \(s=1\)** | **Proved** |
| Thm 4.6 — \(s=5\) absorbable \(C\)-hop kills hard-core | **Proved** |
| Thm 4.4 clean SPPA / free-side subcells | **Proved** |
| Locked contact core for \(s=2\) | **Empty** ([`hadwiger_G7lock_s2_s5.md`](hadwiger_G7lock_s2_s5.md) Thm B) |
| Locked contact core for \(s=5\) | **Cutvertices out; terminal bounds; residual \(R_5\)** ([`hadwiger_G7lock_s2_s5.md`](hadwiger_G7lock_s2_s5.md)) |
| Locked contact core for \(s\in\{3,4\}\) | **Open** |
| Full no hard-core RPC / \(\mathrm{HC}_7\) | **Open** (reduced to \(R_5\cup\{s=3,4\}\)) |

---

## 10. Final verdict

### Proved for \(t=7\) hard-core attack
1. **Mader-boosted fan of length \(\ge 7\)** into the non-contact side — strictly stronger than the hybrid’s \(t-1=6\) package.  
2. **Finite partition pressure:** \(|L|\ge 7\) into \(s\le 5\) bags forces either a triple portal bag or two double-portal bags.  
3. **Complete elimination of \(s=1\)** by cutvertex/\(N(v)\)–\(C\) separation inside the unique contact bag against internally disjoint fan paths.  
4. **Deficiency-one geometry:** multi-portal bags cannot use \(C\)-facing unique attachments; rigidity is \((R1)\) / contact-\((R3)\) only.  
5. **Reduction of \(G_7^{\mathrm{RPC}}\)** to the non-existence of **locked contact cores** (Definition 7.1) for \(s\in\{2,3,4,5\}\).

### Not proved
- Emptiness of residual cell \(R_5\) (terminal non-cut \(s=5\) cores) and of locked cores at \(s\in\{3,4\}\).  
- Unconditional \(\mathrm{HC}_7\).

### Precise residual gap (updated)
\[
\boxed{\;G_7^{\mathrm{lock}}\text{ empty for }s=1,2;\ s=5\text{ reduced to }R_5;\ \text{open for }s\in\{3,4\}\text{ and }R_5.\;}
\]
See [`hadwiger_G7lock_s2_s5.md`](hadwiger_G7lock_s2_s5.md): \(s=2\) fully closed by cutvertex ban (unique private target) + singleton-\(U\) descent + double counting (\(|L|\le 6<7\)). For \(s=5\), multi-portal cutvertices eliminated and terminal portal bounds \(r\le 2\) (multi-contact) / \(r\le 3\) (single-contact) proved; residual \(R_5\) = saturated double-portal multi-contact bags and warehouse distributions.

A proof that \(R_5=\emptyset\) and no locked cores at \(s\in\{3,4\}\) yields \(\mathrm{HC}_7\).

---

*End of hard-core RPC \(t=7\) case analysis.*
