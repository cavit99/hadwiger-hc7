# Hadwiger's Conjecture: Strongest Completely Elementary Affirmative Results

**Self-contained synthesis from first principles.**  
Full LaTeX source: [`hadwiger_complete_affirmative_results.tex`](hadwiger_complete_affirmative_results.tex)

No black-box citations. No claims for general \(t\) beyond what is proved. No 4CT, no RST, no Kostochka–Thomason.

---

## Master theorem (what is fully proved)

### A. Reductions
1. \(\chi(G)=\max\{\chi(C):C\text{ component}\}\), \(\eta(G)=\max\eta(C)\). Hadwiger reduces to **connected** graphs.
2. \(\mathrm{HC}_t\) ⇔ every **\(t\)-critical** graph has a \(K_t\) minor.
3. Every graph with \(\chi\ge t\) has a \(t\)-critical subgraph.

### B. Structure of \(t\)-critical graphs / minimal counterexamples
If \(G\) is \(t\)-critical:
- connected; \(\delta\ge t-1\);
- if \(t\ge 3\), then \(2\)-connected;
- no separating clique of order \(\le t-1\);
- Brooks: \(G\cong K_t\), or odd cycle (\(t=3\)), or \(\Delta\ge t\).

Every minimal Hadwiger counterexample with \(\chi=k\) is \(k\)-critical, has \(\eta=k-1\), and every contraction \(G/e\) attains equality \(\chi=\eta=k-1\).

### C. Full Hadwiger for \(t\le 4\)
| \(t\) | Statement | Method |
|------|-----------|--------|
| \(\le 2\) | trivial | definitions |
| \(3\) | \(K_3\)-minor-free ⇔ forest ⇒ \(\chi\le 2\) | cycle = \(K_3\)-model |
| \(4\) | \(K_4\)-minor-free ⇒ \(2\)-degenerate ⇒ \(\chi\le 3\) | Dirac: \(\delta\ge 3\Rightarrow K_4\) minor |

### D. Exponential bound (all \(t\))
\[
G\not\succcurlyeq K_t \quad\Longrightarrow\quad \chi(G)\le 2^{t-2}.
\]
Two proofs:
1. **BFS layering (Wagner-type):** levels induce \(K_{t-1}\)-minor-free graphs; even/odd palettes give \(2\cdot 2^{t-3}=2^{t-2}\).
2. **Average degree (Mader):** \(d(G)\ge 2^{t-2}\) forces a **dominating** \(K_t\)-model ⇒ ordinary \(K_t\) minor ⇒ \(\mathrm{degen}\le 2^{t-2}-1\).

### E. Case \(t=5\) without 4CT
| Result | Needs 4CT? |
|--------|------------|
| \(\mathrm{HC}_5\Rightarrow 4CT\) (planar ⇒ \(K_5\)-minor-free) | no |
| Planar graphs are \(5\)-colourable (Heawood) | no |
| \(K_5\)-minor-free graphs are \(8\)-colourable | no |
| \(K_5\)-minor-free graphs are \(5\)-colourable via Wagner structure + 5CT | Wagner structure (not proved here); no 4CT |
| Full \(\mathrm{HC}_5\) (\(\chi\le 4\)) | **yes** (≡ 4CT via Wagner) |

### Deliberately not claimed
- \(\mathrm{HC}_6\) (RST + 4CT)
- \(\chi=O(t\sqrt{\log t})\) (Kostochka–Thomason)
- Mader linear density for \(t\le 7\)
- Full Dirac \(\kappa\ge t-1\) for critical graphs
- Wagner’s structural characterisation of \(K_5\)-minor-free graphs

---

## Key proof sketches

### Dirac: \(\delta\ge 3\Rightarrow K_4\) minor
1. Pass to the nonempty \(3\)-core.
2. Pass to a minor \(H\) of minimum order with \(\delta(H)\ge 3\); such \(H\) is \(3\)-connected.
3. In \(3\)-connected \(H\), take \(v\) and a cycle \(C\) in \(H-v\) maximising \(|V(C)\cap N(v)|\); get \(\ge 3\) neighbours on \(C\); partition into a \(K_4\)-model.

### BFS colouring bound
Root at \(r\), levels \(V_i\). If some \(G[V_i]\succcurlyeq K_{t-1}\), the ball \(B=V_0\cup\cdots\cup V_{i-1}\) is connected and meets every branch set ⇒ \(K_t\)-model. So each level is \(K_{t-1}\)-minor-free ⇒ \(\chi\le 2^{t-3}\) by IH. Even/odd double palette: \(2^{t-2}\) colours.

### Average degree ⇒ dominating \(K_t\)-model
Strong IH: connected \(G\) with \(d\ge 2^{t-2}\), any \(v\), model with \(v\in T_1\).
- If some edge \(vw\) has \(<2^{t-3}\) triangles, contract; average degree preserved; lift.
- Else \(G[N(v)]\) has \(\delta\ge 2^{t-3}\); get dominating \(K_{t-1}\)-model there; prepend \(\{v\}\).

### Five Colour Theorem
Euler ⇒ \(e\le 3n-6\) ⇒ \(\delta\le 5\). Delete low-degree \(v\); if \(\deg=5\) and five colours on \(N(v)\), Kempe swap on a \(2\)-coloured component blocked by a separating bichromatic path.

---

## Logical dependence

```
definitions
  → components, criticality, δ≥t−1, 2-connected, clique separators
  → HC₂, HC₃
  → Dirac K₄ ⇒ HC₄
  → BFS layering ⇒ χ≤2^{t−2}
  → avg-degree induction ⇒ degeneracy form
  → Euler ⇒ planar density ⇒ 5CT
  → planar ⇒ K₅-minor-free ⇒ (HC₅ ⇒ 4CT)
```
