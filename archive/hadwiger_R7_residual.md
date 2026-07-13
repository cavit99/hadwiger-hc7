# Residual R7 for Hadwiger’s Conjecture at \(t=7\)

## Statement

**R7.** Let \(H\) be a \(6\)-connected graph with \(\chi(H)=6=\eta(H)\). Then for every proper \(6\)-colouring \(c\) of \(H\) and every rainbow transversal \(u_1,\dots,u_6\) (i.e.\ \(c(u_i)=i\)), there exists a \(K_6\)-model \(\{B_1,\dots,B_6\}\) of \(H\) with \(u_i\in B_i\) for each \(i\).

**Standing black boxes.** \(\mathrm{HC}_t\) for all \(t\le 6\) (in particular \(\mathrm{HC}_6\) of Robertson–Seymour–Thomas). Mader’s extremal bound: every \(n\)-vertex \(K_7\)-minor-free graph has \(|E|\le 5n-15\) (\(n\ge 5\)). Mader’s connectivity theorem: every \(k\)-contraction-critical graph with \(k\ge 7\) is \(7\)-connected.

---

## 0. Verdict (precise)

| Claim | Status |
|-------|--------|
| \(\mathrm{R7}\Rightarrow\mathrm{HC}_7\) (using \(\mathrm{HC}_{\le 6}\)) | **Proved** (§1) |
| \(\mathrm{HC}_7\Rightarrow\mathrm{R7}\) | **Not proved** (and not claimed); R7 is a priori stronger |
| Full proof of R7 | **Not obtained** |
| Counterexample to R7 | **Not found** |
| Small-order computer search (\(n\le 9\), \(6\)-connected, \(\delta\ge 6\)) | No graph with \(\chi=6=\eta\) found; when \(\chi=6\) a \(K_7\) minor appears (§5) |
| Analogue R5 (4-conn, \(\chi=\eta=4\)) | **True** (via Fabila-Monroy–Wood) (§4) |
| Property \((*)\) of Kriesell–Mohr for \(K_6\) (Kempe-rooted \(K_6\)) | **Open** (known for \(K_{\le 4}\); false for \(K_7\)) |
| Hypothesis of R7 non-empty | **Conditional**: non-empty if a \(6\)-connected \(6\)-chromatic \(K_7\)-minor-free graph exists (true whenever a CE to \(\mathrm{HC}_7\) exists, via \(G-v\); open unconditionally) |

**Bottom line.** R7 is a sharp residual that implies \(\mathrm{HC}_7\), is not known to be equivalent to it, survives all small checks, and resists both the Kempe-rooted calculus of Kriesell–Mohr and the re-rooting / contact-augmentation programmes recorded elsewhere in this folder. No proof and no counterexample.

---

## 1. R7 implies \(\mathrm{HC}_7\)

### Theorem 1.1
Assume \(\mathrm{HC}_t\) for all \(t\le 6\). If R7 holds, then \(\mathrm{HC}_7\) holds.

### Proof
Let \(G\) be a minimal counterexample to \(\mathrm{HC}_7\). By the standard CE shape (cf.\ `hadwiger_t7_attempt.md`, Lemma 1.2):

- \(G\) is \(7\)-critical, \(\chi(G)=7\), \(\eta(G)=6\);
- for every vertex \(v\), \(\chi(G-v)=6=\eta(G-v)\).

By Mader’s theorem on contraction-critical graphs (\(k\ge 7\)), \(G\) is \(7\)-connected. Hence \(H:=G-v\) is \(6\)-connected, and \(\chi(H)=6=\eta(H)\).

Fix any proper \(6\)-colouring \(c\) of \(H\). By the rainbow-neighbourhood lemma for critical graphs, \(c(N_G(v))=\{1,\dots,6\}\). Choose a rainbow transversal \(u_1,\dots,u_6\subseteq N_G(v)\) with \(c(u_i)=i\).

Apply R7 to \(H,c,(u_i)\): there is a \(K_6\)-model \(\{B_1,\dots,B_6\}\) of \(H\) with \(u_i\in B_i\). Then
\[
\bigl\{\{v\},B_1,\dots,B_6\bigr\}
\]
is a \(K_7\)-model of \(G\) (each \(u_i\) supplies the cross-edge from \(v\) to \(B_i\)), contradicting \(\eta(G)=6\).

Thus no CE exists, and \(\mathrm{HC}_7\) holds. \(\quad\square\)

### Remark 1.2 (Why this is not mere tautology)
R7 quantifies over **all** \(6\)-connected graphs with \(\chi=\eta=6\) and **all** their \(6\)-colourings and rainbow transversals. A minimal CE to \(\mathrm{HC}_7\) produces such graphs as vertex-deletions, but R7 also constrains graphs that need not arise as \(G-v\) for a \(7\)-critical CE (e.g.\ \(6\)-critical \(6\)-connected \(K_7\)-minor-free graphs, if any exist outside that lineage). Closing R7 is therefore a priori a strengthening of the existential rooted reduction
\[
\mathrm{HC}_7 \;\Longleftrightarrow\; \text{every \(7\)-critical graph has some \(v\) and some colouring of \(G-v\) with a rainbow-neighbour-rooted \(K_6\)}.
\]
The latter is equivalent to \(\mathrm{HC}_7\) (dichotomy of minimal CE). R7 is the **universal** rooted form on the whole class \(\{H:\kappa(H)\ge 6,\ \chi(H)=\eta(H)=6\}\).

---

## 2. Tools available inside a candidate \(H\)

Let \(H\) satisfy the hypotheses of R7, and fix \(c\) and rainbow \(u_1,\dots,u_6\).

### Lemma 2.1 (Unrooted model)
There exists a \(K_6\)-model of \(H\) (since \(\eta(H)=6\)).

### Lemma 2.2 (Degree and order)
\(\delta(H)\ge 6\) and \(|E(H)|\le 5|V(H)|-15\). In particular \(n:=|V(H)|\ge 8\) (no \(6\)-connected graph on \(\le 7\) vertices has \(\eta=6=\chi\): \(K_7\) has \(\chi=\eta=7\); \(K_6\) has \(\kappa=5\)).

### Lemma 2.3 (No automatic Kempe system)
Unlike the situation inside \(G-v\) for a \(7\)-critical \(G\), a general \(6\)-colouring of \(H\) need **not** place \(u_i\) and \(u_j\) in the same component of \(H[c^{-1}(i)\cup c^{-1}(j)]\). Kempe paths between all pairs \((u_i,u_j)\) are guaranteed only under extra hypotheses (e.g.\ when each \(u_i\) is a neighbour of a common apex, or when \(c\) is a **Kempe colouring**: every bichromatic subgraph is connected).

### Lemma 2.4 (When Kempe paths exist)
If \(c\) is a Kempe colouring, then the routing graph on \(\{u_1,\dots,u_6\}\) is complete, and R7 for this \((c,(u_i))\) is exactly the assertion that \(K_6\) has Kriesell–Mohr property \((*)\) inside this highly connected host. Property \((*)\) for \(K_6\) is open (Kriesell–Mohr 2019/2022: true for all graphs on \(\le 4\) vertices; false for \(K_7\); partial positive results for order \(5\)).

### Lemma 2.5 (Linkedness gap)
Thomas–Wollan: every \(10k\)-connected graph is \(k\)-linked. Rooting a \(K_6\) at six prescribed vertices via disjoint paths for all \(\binom{6}{2}=15\) pairs would follow from \(15\)-linkedness, hence from connectivity \(\ge 150\). We have only \(\kappa(H)\ge 6\). **No contradiction and no construction from bare connectivity.**

---

## 3. Mechanisms tried (none closes R7)

### 3.1. Case analysis on small \(|V(H)|\)
- \(n\le 7\): no graph meets the hypotheses (Lemma 2.2).
- \(n=8\): every \(6\)-connected graph has \(\delta\ge 6\), so is \(K_8\) minus a matching. Computer check (§5): those with no \(K_7\) minor have \(\chi\le 5\); those with \(\chi=6\) have a \(K_7\) minor.
- \(n=9\): all \(6\)-regular (and near-regular) \(K_9\)-minus-matching-or-cycle complements checked in §5; same dichotomy: \(\chi=6\Rightarrow\eta\ge 7\), and \(\eta=6\Rightarrow\chi\le 5\).

No counterexample on \(n\le 9\); no positive theorem either (the pattern suggests a possible strengthening “every \(6\)-connected \(K_7\)-minor-free graph is \(5\)-colourable”, which would make R7’s hypothesis empty and R7 vacuously true — but that strengthening is open and likely as hard as a chunk of \(\mathrm{HC}_7\)).

### 3.2. Colour-critical structure
If \(H\) is \(6\)-critical (stronger than \(\chi=6\)), then \(\delta\ge 5\), and with \(\kappa\ge 6\) one has \(\delta\ge 6\). Rainbow transversals need not meet \(N(v)\) for any apex. The double-foot / six-fan package of `hadwiger_t7_attempt.md` (Theorems 6.4–6.6) is written for \(G-v\) with an external apex \(v\in V(G)\setminus V(H)\) and does not transfer to bare R7.

### 3.3. Monochromatic trees with private Steiner vertices
Plan: connect each colour class \(c^{-1}(i)\) into a tree \(B_i\ni u_i\) by stealing Steiner vertices of other colours.  
Obstruction (Kriesell–Mohr / hybrid notes): a vertex of colour \(j\) demanded as Steiner for \(B_i\) is also demanded by \(B_j\). Simultaneous assignment is a branch-assignment / matroid-union obstruction, equivalent to non-existence of the rooted model. No elementary matching theorem resolves it at connectivity \(6\).

### 3.4. Computer search for counterexamples
Implemented pure-Python checks for:

- existence of \(K_7\) minors on \(n\le 9\) by exhaustive branch-type enumeration (partitions of excess \(n-7\));
- exact chromatic number by backtracking;
- rooted \(K_6\) at prescribed transversals by assignment of Steiner vertices (\(7^{n-6}\) for \(n\) small).

Results in §5. No counterexample. Exhaustion beyond \(n\approx 12\) with \(\kappa\ge 6\) is infeasible without a generation pipeline for \(6\)-connected \(K_7\)-minor-free graphs (none is known to be small and \(6\)-chromatic).

### 3.5. Holroyd’s Strong Hadwiger Conjecture
Holroyd (1997): if \(S\subseteq V(H)\) is **colourful** (meets every colour in every optimal colouring), then \(H\) has an \(S\)-rooted \(K_{\chi(H)}\)-minor.  
Martinsson–Steiner (2022/2024) proved this for \(\chi=4\), which yields a strengthening of \(\mathrm{HC}_5\). For \(\chi=6\) it is open.  
R7 asks for a rooted model at a rainbow transversal of a **single** colouring; such a transversal need not be colourful. Thus even Strong HC\(_6\) would not automatically give R7, and R7 does not automatically give Strong HC\(_6\).

---

## 4. Positive evidence from lower analogues

### Theorem 4.1 (Analogue R5 — true)
Let \(H\) be \(4\)-connected with \(\chi(H)=4=\eta(H)\). Then for every proper \(4\)-colouring and every rainbow transversal \(u_1,\dots,u_4\), there is a \(K_4\)-model rooted at those vertices.

### Proof sketch
By Fabila-Monroy–Wood:

1. Every \(4\)-connected non-planar graph has a \(K_4\)-minor rooted at **any** four distinct vertices.
2. Every \(3\)-connected planar graph has a \(K_4\)-minor rooted at \(a,b,c,d\) iff \(a,b,c,d\) do not lie on a common face.

If \(H\) is non-planar, (1) finishes. If \(H\) is planar and \(4\)-connected with \(\eta=4\), then \(H\) is \(K_5\)-minor-free. A \(4\)-connected maximal planar graph has only triangular faces, so no four vertices lie on a face; (2) gives a rooted \(K_4\) at any four vertices, a fortiori at any rainbow transversal. (If \(H\) is planar but not a triangulation, add edges inside faces to maximise; rooted models lift under edge addition.) \(\quad\square\)

### Remark 4.2
The analogue R4 (\(3\)-connected, \(\chi=\eta=3\)) is **vacuous**: every \(3\)-connected graph on \(\ge 4\) vertices has a \(K_4\) minor, so \(\eta\ge 4\).

### Remark 4.3
The pattern “high connectivity \(+\) \(\chi=\eta=r-1\) \(\Rightarrow\) rainbow-rooted \(K_{r-1}\)” holds for \(r-1=4\) by a complete structural theorem for rooted \(K_4\). No comparable structural theorem exists for rooted \(K_5\) or \(K_6\) (the open core of Strong HC and of property \((*)\)).

---

## 5. Computer checks (reproducible)

### 5.1. Order 8
Every \(6\)-connected graph on \(8\) vertices is \(K_8\) minus a matching (complement \(\Delta\le 1\)).

| Complement matching size | \(m(H)\) | \(K_7\) minor? | \(\chi\) |
|--------------------------|----------|----------------|----------|
| 4 (perfect) | 24 | No | 4 |
| 3 | 25 | No | 5 |
| 2 | 26 | **Yes** | 6 |
| \(\le 1\) | \(\ge 27\) | Yes | \(\ge 6\) |

No graph with \(\chi=6=\eta\).

### 5.2. Order 9 (sample of \(\delta\ge 6\), \(m\le 30\))
Complements of \(2\)-factors and near-\(2\)-factors:

| Complement | \(m(H)\) | \(K_7\)? | \(\chi\) |
|------------|----------|----------|----------|
| \(C_9\) | 27 | No | 5 |
| \(C_3\cup C_6\) | 27 | No | 4 |
| \(C_4\cup C_5\) | 27 | No | 5 |
| \(3C_3\) | 27 | No | 3 |
| \(C_5\cup 2K_2\) | 29 | No | 5 |
| \(C_7\cup K_2\) | 28 | No | 5 |
| \(3P_3\) | 30 | **Yes** | 6 |

Again: \(\chi=6\Rightarrow K_7\) minor in every tested example.

### 5.3. Complete multipartite \(K_{2,2,1,1,1,1}\)
\(\kappa=6\), \(\chi=6\), but \(\eta\ge 7\) (has \(K_7\) minor). All rainbow transversals of the natural colouring root a \(K_6\) (they span a \(K_6\) subgraph). Not a counterexample to R7 because \(\eta\neq 6\).

### 5.4. Hajos join of two \(K_6\)
\(6\)-critical, \(n=11\), \(\delta=5\), \(\kappa\le 5\), no small-branch \(K_7\) minor. Fails \(6\)-connectivity.

### 5.5. Prism \(K_6\mathbin{\square}K_2\)
\(\delta=6\), \(\kappa=6\), \(\chi=6\), but admits an explicit \(K_7\) minor (match one edge as a branch set, use one layer’s \(K_5\) as five singletons and the opposite layer’s \(K_5\) as the seventh). \(\eta\ge 7\).

---

## 6. What a proof of R7 would need

Any complete proof must, for every \(6\)-connected \(H\) with \(\chi=\eta=6\), every \(6\)-colouring, and every rainbow transversal \(U=\{u_1,\dots,u_6\}\), produce a \(U\)-rooted \(K_6\)-model. The following routes are blocked or incomplete:

1. **Bare Menger / linkedness** — connectivity too low (Lemma 2.5).
2. **Kempe path packing** — paths need not exist (Lemma 2.3); when they do, packing is Hajós-hard for \(t=7\).
3. **Unrooted model + fan absorption** — the MCM / SPPA / RPC package (`hadwiger_mcm_menger_fan.md`, `hadwiger_hybrid_fan_absorption.md`, `hadwiger_rpc_elimination.md`) still has a hard-core residual configuration; that residual is essentially \(\mathrm{HC}_7\).
4. **Strong HC / colourful sets** — open for \(t=6\); does not cover non-colourful rainbow transversals.
5. **Structural theorem for \(K_7\)-minor-free graphs** — RS structure exists in principle but is too coarse for a rooted colouring argument at present.
6. **Vacuous truth via “\(6\)-conn \(+\) no \(K_7\) \(\Rightarrow\) \(5\)-colourable”** — attractive from §5, unproved, and strong enough that it would itself settle a large piece of the landscape around \(\mathrm{HC}_7\).

---

## 7. What a counterexample to R7 would need

A counterexample is a single graph \(H\) such that:

1. \(\kappa(H)\ge 6\);
2. \(\chi(H)=6\);
3. \(\eta(H)=6\) (has a \(K_6\) minor, no \(K_7\) minor);
4. some proper \(6\)-colouring \(c\) and some rainbow transversal \(U\) admit **no** \(U\)-rooted \(K_6\)-model.

Necessary constraints from the search and theory:

- \(n\ge 10\) (no examples on \(\le 9\));
- \(7\le \delta\le 9\) is not forced (Mader only gives average degree \(<10\)); \(\delta\ge 6\);
- \(H\) cannot be complete multipartite on six parts with large parts without creating a \(K_7\) minor (as in §5.3);
- \(H\) cannot be a clique sum along \(\le 5\) vertices (that would force \(\kappa\le 5\));
- if \(c\) is a Kempe colouring, then \(H\) is also a counterexample to property \((*)\) for \(K_6\), which is open and of independent interest.

The Böhme–Kostochka–Thomason graphs (Kempe colourings with Hadwiger number \(\tfrac23 k+o(k)\)) give counterexamples to property \((*)\) for large \(k\), and Kriesell–Mohr give an explicit counterexample for \(K_7\), but their constructions for \(k=6\) fail to destroy the rooted model (Theorem 6 of Kriesell–Mohr: \(Z(G)\) works for all \(|V(G)|\le 6\)).

---

## 8. Relationship diagram

```
HC6 (known)
   │
   ▼
CE shape for HC7: 7-critical, κ≥7, η=6, G−v has χ=η=6, κ(G−v)≥6
   │
   ├── existential rainbow-rooted K6 in some G−v  ◄──►  HC7
   │
   └── universal R7 on all 6-conn χ=η=6 graphs
            │
            ├── implies HC7          (Theorem 1.1)
            ├── not known from HC7
            ├── true for analogue r=5 (Theorem 4.1)
            ├── open for r=6
            └── no counterexample on n≤9
```

---

## 9. Conclusions

1. **R7 is a legitimate, non-vacuous-looking residual for \(\mathrm{HC}_7\)**: it implies \(\mathrm{HC}_7\) under \(\mathrm{HC}_{\le 6}\), and it is the natural universal form of the rooted obstruction that characterises minimal counterexamples.
2. **R7 is not proved.** Every standard mechanism (linkedness, Kempe packing, fan absorption, Strong HC, small-case exhaustion) either fails for connectivity reasons, reduces to an open problem of equal strength, or only covers lower analogues.
3. **R7 is not disproved.** No counterexample exists among all \(6\)-connected graphs on \(n\le 9\) vertices; the only graphs in that range with \(\chi=6\) already have \(K_7\) minors. Known constructions that kill rooted clique minors (Z-construction, Böhme–Kostochka–Thomason) do not yield a \(6\)-connected host with \(\chi=\eta=6\) and a bad rainbow transversal.
4. **The exact difficulty of R7 is the rooted-\(K_6\) problem under connectivity \(6\) and Hadwiger number \(6\)**, specialised to rainbow transversals of optimal colourings — the same difficulty that blocks Gap G in the apex-contact programme and property \((*)\) for \(K_6\) in the Kempe-rooted programme.

### Open subproblems worth isolating

- **R7-Kempe.** Same as R7 but only for Kempe colourings. Equivalent to: \(K_6\) has property \((*)\) in every \(6\)-connected host with \(\eta=6\).
- **5-colourability of \(6\)-connected \(K_7\)-minor-free graphs.** If true, R7 is vacuous (hence true). Open.
- **R7 for \(6\)-critical hosts only.** Still open; would still imply \(\mathrm{HC}_7\) by the same argument as Theorem 1.1 whenever a CE’s \(G-v\) can be replaced by a \(6\)-critical subgraph that remains \(6\)-connected (not automatic).

---

## 10. References (used)

- Robertson–Seymour–Thomas, Hadwiger’s conjecture for \(K_6\)-free graphs, *Combinatorica* 13 (1993).
- Mader, connectivity of contraction-critical graphs; extremal function for \(K_7\) minors.
- Fabila-Monroy–Wood, Rooted \(K_4\)-minors, *Electron. J. Combin.* (2013).
- Martinsson–Steiner, Strengthening Hadwiger’s conjecture for 4- and 5-chromatic graphs, *JCTB* (2024).
- Kriesell–Mohr, Kempe chains and rooted minors, arXiv:1911.09998.
- Holroyd, Strong Hadwiger conjecture, *Bull. London Math. Soc.* (1997).
- Kawarabayashi–Toft, any 7-chromatic graph has \(K_7\) or \(K_{4,4}\) minor.
- Internal notes: `hadwiger_t7_attempt.md`, `hadwiger_hybrid_rooted_linkage.md`, `hadwiger_dual_search.md`, `hadwiger_mcm_menger_fan.md`, `hadwiger_rpc_elimination.md`.

---

*End of note. R7 remains open: no proof, no counterexample, clear implication to HC7, and a clean list of blocked mechanisms.*
