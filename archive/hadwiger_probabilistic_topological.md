# Hadwiger’s Conjecture via Probabilistic, Random-Partition, and Topological Methods

**Approach family:** Probabilistic method, random partitions, topological methods (Kneser / Borsuk–Ulam), geometric embeddings and separators.

**Target statement (Hadwiger).** For every integer \(t\ge 2\), every graph \(G\) with no \(K_t\) minor satisfies \(\chi(G)\le t-1\).

**Standing conventions.** All graphs are finite, simple, undirected. Write \(h(G)\) for the Hadwiger number (order of a largest clique minor). A graph is \(K_t\)-minor-free if \(h(G)<t\). Degeneracy of \(G\) is \(\mathrm{degen}(G)=\max_{H\subseteq G}\delta(H)\). Always \(\chi(G)\le\mathrm{degen}(G)+1\).

---

## 0. Executive status

| Sub-approach | Best rigorous conclusion in this note | Status for \(\chi\le t-1\) |
|---|---|---|
| Random colouring / direct LLL | \(\chi=O(t\sqrt{\log t})\) from degeneracy; LLL does not close the gap to \(t-1\) | **BLOCKED** |
| Probabilistic partitions + expansion | Recoverable \(O(t\sqrt{\log t})\) colourings; partition schemes need average degree \(o(t)\) or stronger expansion than known | **BLOCKED** |
| Topological (Kneser / continuous) | Homology/Borsuk–Ulam lower bounds on \(\chi\) for *special* complexes; no reduction that forces \(\chi\le t-1\) for all \(K_t\)-minor-free graphs | **BLOCKED** (no reduction) |
| Geometric separators | Recursive colouring gives \(\chi=n^{o(1)}\) historically, and with modern density \(\chi=O(t\sqrt{\log t})\); separator size too large for \((t-1)\)-colour recursion alone | **BLOCKED** for exact bound |

**Verdict.** Given only the known extremal sparsity of \(K_t\)-minor-free graphs (Kostochka–Thomason density \(\Theta(t\sqrt{\log t})\)), pure probabilistic density arguments are **insufficient** for \(\chi\le t-1\). The same density gap blocks naive random partitions and separator recursion from reaching \(t-1\). Topological methods supply tools for *lower* bounds and for special graph classes, but no known continuous invariant of minor-free graphs forces \((t-1)\)-colourability.

What *is* proved below is a package of concrete lemmas: density → degeneracy colouring; LLL obstruction lemmas; random-cluster partition lemmas; Alon–Seymour–Thomas style separator colouring recursion; and a precise “density gap” meta-lemma explaining the blockage.

---

## 1. Density, degeneracy, and the probabilistic baseline

### Lemma 1.1 (Kostochka–Thomason density; stated for use)

There exist absolute constants \(c_1,c_2>0\) such that for every integer \(t\ge 3\):
- every graph of average degree at least \(c_2\,t\sqrt{\log t}\) has a \(K_t\) minor;
- there exist \(K_t\)-minor-free graphs of average degree at least \(c_1\,t\sqrt{\log t}\).

**Consequence for colouring.** If \(G\) is \(K_t\)-minor-free then \(\mathrm{degen}(G)=O(t\sqrt{\log t})\), hence
\[
\chi(G)\le O\bigl(t\sqrt{\log t}\bigr).
\]
This is the classical probabilistic/extremal baseline (every minimal counterexample is \(\delta\ge\chi-1\), so average degree is large, hence a large clique minor).

### Lemma 1.2 (Degeneracy colouring is sharp up to constants under density alone)

Let \(\mathcal{F}_t\) be the class of \(K_t\)-minor-free graphs. Suppose a colouring argument uses only the information
\[
\max_{G\in\mathcal{F}_t}\ \mathrm{avgdeg}(G)\ \le\ D(t)
\]
and the fact that every graph is \((\mathrm{degen}+1)\)-colourable. Then the best guaranteed bound is \(\chi\le D(t)+1\). In particular, with the true order \(D(t)=\Theta(t\sqrt{\log t})\), one cannot deduce \(\chi\le t-1\) from density + degeneracy alone.

**Proof.** Degeneracy colouring uses only local minimum degree; it never exploits global structure beyond \(\delta(H)\le D(t)\) for every subgraph \(H\). Extremal examples in Lemma 1.1 show \(D(t)=\Omega(t\sqrt{\log t})\), so the method’s ceiling is \(\Omega(t\sqrt{\log t})\). ∎

### Definition 1.3 (Density gap)

The **Hadwiger density gap** is the ratio
\[
\Gamma(t)\ :=\ \frac{\sup\{\mathrm{avgdeg}(G): h(G)<t\}}{t-2}.
\]
By Lemma 1.1, \(\Gamma(t)=\Theta(\sqrt{\log t})\to\infty\).

---

## 2. Random colouring and the Lovász Local Lemma

### Setup 2.0

Fix \(G\) \(K_t\)-minor-free, \(n=|V(G)|\), and an integer \(k\ge 1\). Sample a uniform random map \(c:V(G)\to\{1,\dots,k\}\). For each edge \(e=uv\) let \(A_e\) be the event that \(c(u)=c(v)\). We want \(\mathbb{P}(\bigcap_e A_e^c)>0\).

### Lemma 2.1 (Naive union bound)

If \(k>|E(G)|\) then a random \(k\)-colouring is proper with positive probability. For \(K_t\)-minor-free \(G\), \(|E|=O(nt\sqrt{\log t})\), so this only yields \(k=\Omega(nt\sqrt{\log t})\), useless for fixed \(t\).

### Lemma 2.2 (Symmetric LLL for improper edges)

Suppose each vertex has degree at most \(\Delta\). Then each \(A_e\) depends on at most \(2\Delta-2\) other edge-events, and \(\mathbb{P}(A_e)=1/k\). Symmetric LLL gives a proper colouring whenever
\[
e\cdot\frac{1}{k}\cdot(2\Delta-1)\ \le\ 1,
\]
i.e. \(k\ge e(2\Delta-1)\). Thus \(\chi\le O(\Delta)\). For \(K_t\)-minor-free graphs one may take \(\Delta=O(t\sqrt{\log t})\) after deleting high-degree vertices carefully, or work in a \(\Delta\)-degenerate orientation; the conclusion remains \(\chi=O(t\sqrt{\log t})\), not \(t-1\).

**Proof.** Standard symmetric LLL (Erdős–Spencer). Dependency degree \(\le 2\Delta-2\) for line-graph of \(G\). ∎

### Lemma 2.3 (LLL obstruction under only degree information)

Let \(\Delta=\Delta(G)\). Any application of the (symmetric or asymmetric) LLL to the bad events \(\{A_e\}_{e\in E}\) that uses only the estimates \(\mathbb{P}(A_e)=1/k\) and dependency degree \(O(\Delta)\) requires \(k=\Omega(\Delta)\) to conclude \(\mathbb{P}(\bigcap A_e^c)>0\). If the only available bound is \(\Delta=\Omega(t\sqrt{\log t})\) on some \(K_t\)-minor-free graphs (or on core subgraphs), LLL cannot force \(k=t-1\).

**Proof.** The LLL criterion is of the form \(p(D+1)\le 1/e\) (or asymmetric products). Here \(p=1/k\) and \(D=\Theta(\Delta)\), so \(k=\Omega(\Delta)\). Extremal minor-free graphs attain \(\Delta=\Omega(t\sqrt{\log t})\). ∎

### Lemma 2.4 (List-colouring / choice-number via LLL)

The same LLL analysis for list assignments of size \(k\) yields \(\mathrm{ch}(G)=O(\Delta)\). No improvement to \(t-1\) for \(K_t\)-minor-free graphs without stronger dependence structure than the line graph provides.

### Remark 2.5 (Why “smarter” bad events do not remove the gap)

One may redefine bad events as “a monochromatic connected subgraph of order \(\ge s\)”, aiming at *cluster* colourings (cf. Haxell–McDiarmid–Reed style, or Reed–Seymour cluster method). Probabilistically, with \(k=t-1\) colours, expected monochromatic component sizes in a graph of average degree \(\Theta(t\sqrt{\log t})\) are **not** forced to be \(O(1)\); the branching-process offspring mean is \(\sim \mathrm{avgdeg}/k=\Theta(\sqrt{\log t})\to\infty\). Thus monochromatic components are typically large, and contracting them does not produce a \(K_t\) minor under control without additional structure. This is formalized next.

---

## 3. Random partitions and expansion

### Definition 3.1 (Random \(k\)-partition)

A **random \(k\)-partition** of \(V(G)\) is a uniform random colouring \(c:V\to[k]\); parts \(V_i=c^{-1}(i)\). Write \(G[V_i]\) for induced subgraphs and \(\mathcal{C}(V_i)\) for the set of connected components of \(G[V_i]\).

### Lemma 3.2 (Monochromatic branching mean)

Let \(G\) be \(d\)-regular (or average degree \(d\)) and \(c\) random with \(k\) colours. For a fixed vertex \(v\), the expected number of neighbours of \(v\) of the same colour is \(d/k\). In the exploration process of the monochromatic component of \(v\), the mean offspring is \(d/k\) (up to depletion). In particular, if \(d/k>1+\varepsilon\) then with positive probability (in infinite \(d\)-regular trees, and typically in expanders) monochromatic components have exponential tails only above a large threshold, and \(\mathbb{E}|C(v)|=\Omega_\varepsilon(1)\) can be large.

**For \(K_t\)-minor-free graphs with \(d=\Theta(t\sqrt{\log t})\) and \(k=t-1\):**
\[
\frac{d}{k}=\Theta(\sqrt{\log t})\ \xrightarrow{t\to\infty}\ \infty.
\]
Thus random \((t-1)\)-partitions do **not** produce small monochromatic components on the basis of density alone.

### Lemma 3.3 (Cluster contraction heuristic — sufficient condition)

Suppose \(G\) admits a partition of \(V\) into sets \(X_1,\dots,X_m\) such that each \(G[X_j]\) is connected and the **contracted** graph \(H\) obtained by contracting each \(X_j\) satisfies \(\chi(H)\le r\) and each \(G[X_j]\) is \(s\)-colourable. Then \(\chi(G)\le rs\).

In particular, if one finds a partition into \(O(1)\)-colourable clusters whose contraction is \((t-1)\)-colourable (e.g. if the contraction is a forest, \(r=2\)), one obtains a constant-factor colouring — but to reach \(t-1\) one needs \(rs\le t-1\).

### Lemma 3.4 (Reed–Seymour style: existence of highly connected clusters)

(Reed–Seymour, qualitative form used as a black box.) There is a function \(f\) such that every graph \(G\) with \(\chi(G)>f(\ell)\) has a \(K_\ell\) minor; more sharply for our purposes: large chromatic number forces highly linked subgraphs. Combined with density theorems, this yields \(\chi(G)=O(t\sqrt{\log t})\) for \(h(G)<t\), matching Lemma 1.1 — **not** \(t-1\).

### Lemma 3.5 (Random partition → minor: insufficient density for \(k=t-1\))

Assume only that every subgraph of \(G\) has average degree \(\le D\), with \(D=\Theta(t\sqrt{\log t})\). Let \(c\) be a random \((t-1)\)-colouring and contract monochromatic components to obtain a minor \(H\). Then:

1. \(H\) is a minor of \(G\), hence \(K_t\)-minor-free if \(G\) is.
2. There is **no** general upper bound \(\Delta(H)=O(1)\) or \(\mathrm{avgdeg}(H)=O(1)\) following from density alone; expected monochromatic degrees remain \(\Theta(\sqrt{\log t})\).
3. Therefore iterating “random colour → contract components → recolour” does not reduce to a graph of bounded degree in \(O(1)\) rounds when \(k=t-1\).

**Proof of (2).** Each original edge survives as an edge of \(H\) between components with probability depending on endpoint colours; the expected degree contribution per original neighbour is \(\Theta(1)\) when colours differ, and the number of distinct neighbouring components of a given monochromatic component \(C\) is typically on the order of the edge boundary of \(C\) divided by internal connections. Under only average-degree control, boundary can be \(\Theta(|C|\cdot D)\), and after colouring, neighbouring component count is \(\Omega(|C|\cdot D/k)\) in expander-like cores — still \(\omega(1)\) for \(D/k=\omega(1)\). ∎

### Lemma 3.6 (Expansion of minor-free graphs is not free)

\(K_t\)-minor-free graphs need **not** be global expanders (they have small separators — see §5). Locally, however, they may contain subgraphs of girth and expansion comparable to random graphs of degree \(\Theta(t\sqrt{\log t})\). Any probabilistic method that assumes spectral expansion of the *whole* \(G\) to force small random cuts or equitable colour classes is inapplicable without further structural decomposition (e.g. graph minor structure theorem), which is outside pure density probability.

### Lemma 3.7 (BLOCKED: probabilistic partitions at \(k=t-1\))

**Statement.** There is no proof of Hadwiger’s conjecture that proceeds solely by:

- sampling a random partition into \(t-1\) parts, and
- applying first-moment / LLL / alteration only to events defined from degrees, codegrees, and monochromatic component sizes,

while using as its only extremal input that \(K_t\)-minor-free graphs have average degree \(O(t\sqrt{\log t})\).

**Reason.** Lemmas 1.2, 2.3, 3.2, and 3.5: the critical branching ratio \(D/(t-1)=\Theta(\sqrt{\log t})>1\) for large \(t\) prevents monochromatic components from being tiny and prevents LLL from clearing all conflicts at \(k=t-1\).

---

## 4. Topological methods (Kneser, Borsuk–Ulam, continuous maps)

### 4.1 What topology classically gives

Lovász’s proof of the Kneser conjecture: for the Kneser graph \(KG_{n,k}\),
\[
\chi(KG_{n,k})=n-2k+2,
\]
via the Borsuk–Ulam theorem applied to a continuous test map from a sphere associated with the neighbourhood complex. More generally, for a graph \(G\), if the neighbourhood complex \(\mathcal{N}(G)\) (or Hom complex) has high connectivity / high \(\mathbb{Z}_2\)-index, then \(\chi(G)\) is large.

### Lemma 4.1 (Topological lower bound schema)

If \(\mathrm{conn}(\mathcal{N}(G))\ge m\) (connectivity), then \(\chi(G)\ge m+3\) (Lovász). Variants with \(\mathbb{Z}_2\)-index give \(\chi(G)\ge\mathrm{ind}(\mathcal{N}(G))+2\).

These are **lower** bounds on \(\chi\). Hadwiger needs an **upper** bound \(\chi\le t-1\) under a minor-free hypothesis. Topology does not automatically reverse.

### Lemma 4.2 (No free upper bound from vanishing topology)

Suppose \(\mathcal{N}(G)\) is \((m)\)-connected. This does **not** imply \(\chi(G)\le m+C\) for any universal \(C\); high connectivity only forces \(\chi\) large. Conversely, if \(\mathcal{N}(G)\) is highly disconnected, \(\chi\) may still be large (e.g. Mycielski graphs, high-girth high-chromatic graphs). In particular, \(K_t\)-minor-freeness does not translate into a known upper bound on \(\mathrm{ind}(\mathcal{N}(G))\) of the form \(\le t-3\).

### Lemma 4.3 (Homotopy obstruction for colouring maps)

A proper \(k\)-colouring of \(G\) is equivalent to a graph homomorphism \(G\to K_k\), i.e. a continuous equivariant map (in the Hom-complex formalism) \(\mathrm{Hom}(K_2,G)\to\mathrm{Hom}(K_2,K_k)\). Borsuk–Ulam type theorems obstruct such maps when the domain has high index. For \(K_t\)-minor-free \(G\), one would need to prove that an equivariant map **exists** into \(\mathrm{Hom}(K_2,K_{t-1})\). Existence is a constructive / combinatorial problem; non-existence criteria (index comparisons) only help when one already knows \(\mathrm{ind}(\mathrm{Hom}(K_2,G))\) is small, which is essentially as hard as bounding \(\chi(G)\).

### Lemma 4.4 (BOXED limitation)

**There is no known natural continuous functor \(F\) from graphs to \(\mathbb{Z}_2\)-spaces such that:**

1. \(h(G)<t\) implies \(\mathrm{ind}(F(G))\le t-3\), and
2. \(\mathrm{ind}(F(G))\le t-3\) implies \(\chi(G)\le t-1\),

with (1) substantially easier than Hadwiger. Any such \(F\) with (2) for free (as in Lovász) would require (1) to encode nearly the full strength of Hadwiger.

### Remark 4.5 (Topological methods that *do* help special cases)

- For **surface graphs**, colouring bounds use Euler genus + discharging / four colour, not Borsuk–Ulam.
- For **Kneser-type** and **stable Kneser** graphs, topology computes \(\chi\) exactly but these graphs typically have huge clique minors relative to \(\chi\) (they do not stress Hadwiger).
- **Hom complex** techniques have been used for circular chromatic number and for some homomorphism problems; none currently yield \(\chi\le h(G)\).

### Lemma 4.6 (BLOCKED: pure topological route)

A pure Borsuk–Ulam / Kneser-complex argument does not, with present reductions, prove Hadwiger. Status: **BLOCKED** for lack of a minor-monotone upper bound on a topological index that matches \(t-1\).

---

## 5. Geometric embeddings and separators

### Lemma 5.1 (Alon–Seymour–Thomas separator)

There is an absolute constant \(c\) such that every \(K_t\)-minor-free graph \(G\) on \(n\) vertices has a separator \(S\subseteq V(G)\) with
\[
|S|\le c\,t^{3/2}\sqrt{n}
\]
whose removal leaves no component larger than \(2n/3\).

(Modern improvements exist in the \(t\)-dependence; the \(\sqrt{n}\) barrier is the important geometric feature.)

### Lemma 5.2 (Separator recursion for colouring)

Suppose every \(K_t\)-minor-free graph has a separator of size at most \(s(n)\), and subgraphs remain \(K_t\)-minor-free. If one colours the two sides recursively with \(k\) colours and the separator with \(\chi(G[S])\le m\) colours, a crude product / list argument does **not** automatically give \(\chi\le t-1\). More carefully: if \(G-S=A\cup B\) (no \(A\)–\(B\) edges) and \(\chi(G[A\cup S]),\chi(G[B\cup S])\le k\), then \(\chi(G)\le k\). So separator recursion **preserves** a colouring number \(k\) if one can colour every induced subgraph with \(k\) colours — it reduces the problem to smaller instances but needs a base bound.

**Inductive scheme.** To prove \(\chi\le k\) for all \(K_t\)-minor-free graphs by separator induction, it suffices that every such \(G\) either has a vertex of degree \(<k\) or admits a separator whose sides can be coloured and glued. Degree \(<k\) fails when \(k=t-1\) because \(\delta\) may be \(\Omega(t\sqrt{\log t})\). Gluing across a separator of size \(s\) in the worst case requires matching precolourings of the separator, i.e. up to \(k^{|S|}\) extensions — algorithmically hard but existence-wise still needs \(\chi\le k\) on smaller graphs plus extendability. Extendability of precolourings of \(S\) with \(|S|=\Theta(t^{3/2}\sqrt{n})\) fails in general for \(k=t-1\).

### Lemma 5.3 (Quantitative separator colouring bound)

If one uses only \(\chi\le\Delta+1\) on separator-induced subgraphs and recursion, the best classical outcome from Lemma 5.1 style separators plus density is still on the order of the degeneracy bound, or historically weaker \(n^{o(1)}\) when density was not fed in. Separators alone (with \(s(n)=O(t^{3/2}\sqrt{n})\)) give
\[
\chi(G)\ \le\ O\bigl(t^{3/2}\sqrt{n}\bigr)
\]
by “colour the separator with new colours and recurse” in the worst case — far worse than degeneracy. Combining separators with degeneracy returns \(O(t\sqrt{\log t})\).

### Lemma 5.4 (Geometric embedding)

\(K_t\)-minor-free graphs admit (after structure-theoretic decomposition) pieces nearly embeddable on surfaces of genus \(g=g(t)\) with vortices and apices. Colouring each piece with \(O(t)\) colours is plausible in structure-theorem approaches (Robertson–Seymour–Thomas for \(t=6\) uses the Four Colour Theorem on planar pieces). **This is not a pure probabilistic method**; it is excluded from the “density-only probability” track. Within pure probability + geometry of separators: **BLOCKED** at the density gap (Lemma 1.2).

### Lemma 5.5 (BLOCKED: separator recursion to \(t-1\))

Separator size \(\Omega(\sqrt{n})\) (even for planar \(t=5\)) prevents a direct “delete separator, recolour with \(t-1\) colours by induction, extend across separator” argument without a strong precolouring extension theorem. For planar graphs the Four Colour Theorem supplies the bound; for general \(t\), no such extension theorem at \(k=t-1\) is available from probability alone.

---

## 6. Alteration method and residual graphs

### Lemma 6.1 (Alteration for almost-colourings)

Sample random \(c:V\to[k]\). Let \(X\) be the number of monochromatic edges. Then \(\mathbb{E}X=|E|/k\). Delete one vertex from each monochromatic edge: residual independent set / properly coloured set on \(n-\mathbb{E}X\) vertices in expectation. Iterating gives a colouring with
\[
O\Bigl(\frac{|E|}{n}\log n\Bigr)
\]
colours in the classical greedy-alteration sense for general graphs — for sparse graphs \(O(D\log n)\), worse than degeneracy’s \(O(D)\).

### Lemma 6.2 (Alteration does not beat degeneracy)

For hereditary classes with max average degree \(\le D\), alteration and LLL do not improve on \(\chi\le D+1\). Hence for \(K_t\)-minor-free graphs, alteration yields nothing better than \(O(t\sqrt{\log t})\).

---

## 7. Meta-lemma: when probability can prove Hadwiger

### Lemma 7.1 (Necessary density for first-moment colouring)

Suppose a proof that every graph with average degree \(\le D\) (hereditarily) is \(k\)-colourable proceeds by random mapping to \([k]\) plus first-moment deletion of conflicts, and never uses structure beyond degrees. Then one needs \(D=O(k)\). For Hadwiger with \(k=t-1\), this would require hereditary average degree \(O(t)\). But true extremal average degree is \(\Theta(t\sqrt{\log t})\). **Contradiction for large \(t\).**

### Lemma 7.2 (Conditional route — what would unblock probability)

Any of the following would reopen a probabilistic path to \(\chi\le t-1\):

1. **Stronger structure than density:** e.g. every \(K_t\)-minor-free graph is \(O(t)\)-degenerate after deleting a set of size \(o(n)\) with special properties; or a decomposition into \(O(1)\) graphs each of average degree \(O(t)\).
2. **Clustering theorem at scale \(t\):** every such \(G\) has a partition into connected pieces of radius \(O(1)\) such that the quotient has average degree \(O(t)\) (or is \((t-1)\)-colourable).
3. **Local resilience:** every subgraph \(H\subseteq G\) with \(\delta(H)\ge t-1\) contains a \(K_t\) minor (this is essentially Hadwiger for minimal counterexamples: a minimal counterexample satisfies \(\delta\ge t-1\), so one needs every graph with \(\delta\ge t-1\) to have a \(K_t\) minor — false in general without extra structure, since complete bipartite \(K_{t-2,n}\) has \(\delta=t-2\) and no \(K_t\) minor; the critical case is \(\delta\ge t-1\) with no large complete bipartite obstruction).

Note: Hadwiger is equivalent to: every minimal graph with \(\chi\ge t\) has a \(K_t\) minor. Minimal such graphs satisfy \(\delta\ge t-1\). The open core is building a \(K_t\) minor in every graph with \(\chi\ge t\) (or \(\delta\ge t-1\) plus criticality).

### Lemma 7.3 (Bipartite obstruction to naive degree conditions)

For every \(t\), the graph \(K_{t-2,n}\) is \(K_t\)-minor-free (a clique minor needs \(t\) branch sets with all cross-edges; bipartite graphs have \(h\le O(\sqrt{|E|})\) constraints — specifically \(K_{t-2,n}\) has no \(K_t\) minor), \(\chi=2\le t-1\), and \(\delta=t-2\). Thus \(\delta\ge t-2\) does not force large \(\chi\), and any probabilistic minor-building argument must use more than minimum degree \(t-2\).

---

## 8. Positive lemmas worth keeping (affirmative partial results)

### Lemma 8.1 (Probabilistic colouring under linear density)

If a hereditary class \(\mathcal{G}\) satisfies \(\mathrm{avgdeg}(H)\le c\cdot r\) for every \(H\in\mathcal{G}\) with \(h(H)<r\), with \(c\le 1\), then \(\chi\le r\) on \(\{h<r\}\). In particular, if it were true that \(K_t\)-minor-free graphs were \((t-2)\)-degenerate, Hadwiger would follow. (False for large \(t\) by Lemma 1.1.)

### Lemma 8.2 (Small \(t\))

Hadwiger holds for \(t\le 6\) by classical structural arguments (Wagner \(t=5\); Robertson–Seymour–Thomas \(t=6\) + Four Colour Theorem). Probabilistic methods are not required for these cases.

### Lemma 8.3 (Weak Hadwiger via probability — optimal density form)

Every \(K_t\)-minor-free graph is \(O(t\sqrt{\log t})\)-colourable. Proof: Lemma 1.1 ⇒ degeneracy \(O(t\sqrt{\log t})\) ⇒ greedy colouring. This is the affirmative theorem of this approach family at the natural density limit.

### Lemma 8.4 (Random greedy in sparse expanders)

If \(G\) is \(d\)-degenerate, the random greedy algorithm uses at most \(d+1\) colours almost surely in appropriate models. Again saturates at \(d+1=O(t\sqrt{\log t})\).

### Lemma 8.5 (Partition into low-chromatic induced subgraphs — conditional)

If \(G\) is \(K_t\)-minor-free and one can show that a random partition into \(s\) parts yields \(\mathbb{E}[\chi(G[V_i])]\le (t-1)/s\), then linearity might give \(\chi(G)\le t-1\). Under only density, \(\chi(G[V_i])\) is typically \(\Theta((t\sqrt{\log t})/s)\) by the same density applied to random induced subgraphs (edge probability issues aside — induced random subsets of minor-free graphs remain minor-free). Balancing forces \(s\cdot O(t\sqrt{\log t}/s)=O(t\sqrt{\log t})\), no gain.

---

## 9. Attempted proof sketch (where it fails)

**Attempt.** Let \(G\) be a minimal counterexample to Hadwiger: \(h(G)<t\), \(\chi(G)\ge t\), \(\delta(G)\ge t-1\). Sample random \(c:V\to[t-1]\). Use LLL to eliminate monochromatic edges.

**Failure.** Dependency degree is \(\ge 2\delta-2\ge 2t-4\), and \(\mathbb{P}(A_e)=1/(t-1)\). Check LLL:
\[
e\cdot\frac{1}{t-1}\cdot(2t-3)\ \approx\ 2e>1
\]
for all \(t\ge 2\). Symmetric LLL **never** fires for \(k=t-1\) when \(\Delta\ge t-1\). Asymmetric LLL with the same \(p\) and \(D\) likewise fails by the same margin. If in fact \(\delta=\Omega(t\sqrt{\log t})\) in a dense core, the failure is larger:
\[
e\cdot\frac{1}{t-1}\cdot\Omega(t\sqrt{\log t})=\Omega(\sqrt{\log t})\to\infty.
\]

**Second attempt.** Contract monochromatic components; claim the quotient is \((t-1)\)-colourable by induction or is bipartite.

**Failure.** Quotient still may have high chromatic number and only \(K_t\)-minor-freeness; monochromatic components are large (Lemma 3.2), and the quotient is not simpler in chromatic number in any quantifiable way from first moments.

**Third attempt.** Borsuk–Ulam on a complex built from \((t-1)\)-colourings.

**Failure.** The space of all (not necessarily proper) maps \(V\to[t-1]\) is discrete; continuous relaxations (fractional colourings, homomorphisms to Kneser graphs) give fractional Hadwiger-type statements at best, not integral \(\chi\le t-1\).

---

## 10. Concrete lemma list (index)

| ID | Lemma | Type |
|----|--------|------|
| 1.1 | Kostochka–Thomason density \(\Theta(t\sqrt{\log t})\) | Input extremal |
| 1.2 | Degeneracy ceiling = density ceiling | Blockage |
| 1.3 | Density gap \(\Gamma(t)=\Theta(\sqrt{\log t})\) | Definition |
| 2.1–2.4 | Random colouring + LLL ⇒ \(\chi=O(\Delta)\) only | Probabilistic |
| 2.3 | LLL obstruction at \(k=t-1\) | **BLOCKED** |
| 3.2 | Monochromatic branching mean \(D/k\) | Probabilistic |
| 3.5–3.7 | Random partitions insufficient | **BLOCKED** |
| 4.1–4.6 | Topology gives lower bounds; no upper-bound functor | **BLOCKED** |
| 5.1–5.5 | Separators: recursion without extension theorem fails | **BLOCKED** |
| 6.1–6.2 | Alteration ≤ degeneracy | Negative |
| 7.1–7.3 | Meta: need linear density or structure | Conditional |
| 8.3 | \(\chi=O(t\sqrt{\log t})\) for \(K_t\)-minor-free | **Affirmative partial** |

---

## 11. Final determination for this approach family

**Can the probabilistic method / random partitions / topology / separators, using only known minor-free sparsity, complete an affirmative proof of Hadwiger (\(\chi\le t-1\))?**

# **BLOCKED**

**Primary obstruction.** The Hadwiger density gap \(\Gamma(t)=\Theta(\sqrt{\log t})\): extremal \(K_t\)-minor-free graphs are too dense for first-moment, LLL, alteration, or random monochromatic-component analysis to succeed with \(k=t-1\) colours.

**Secondary obstruction.** Topological index methods are oriented toward lower bounds on \(\chi\) and lack a minor-monotone upper-bound invariant of strength \(t-1\).

**Tertiary obstruction.** Separator geometry enables recursion but requires precolouring-extension or degeneracy \(\le t-2\), neither of which follows from known probabilistic density.

**Best affirmative theorem in-family.**  
\[
\boxed{\text{Every }K_t\text{-minor-free graph is }O(t\sqrt{\log t})\text{-colourable.}}
\]

**What would unblock.** A structural theorem reducing \(K_t\)-minor-free graphs to pieces of average degree \(O(t)\), or a clustering theorem producing a \((t-1)\)-colourable quotient with \(O(1)\)-colourable clusters, or a proof that every \(\chi\)-critical graph with \(\chi=t\) has a \(K_t\) minor by non-probabilistic linkage (the classical structural path for small \(t\)).

---

## Appendix A. Explicit LLL calculation (minimal counterexample)

Let \(G\) be \(t\)-critical, so \(\delta\ge t-1\), \(k=t-1\), \(p=1/k=1/(t-1)\), dependency degree \(D\le 2\Delta-2\) but at least one uses \(D\ge 2\delta-2\ge 2t-4\). Symmetric LLL needs \(ep(D+1)\le 1\):
\[
e\cdot\frac{1}{t-1}\cdot(2t-3)\ =\ e\cdot\frac{2t-3}{t-1}\ =\ e\cdot\Bigl(2-\frac{1}{t-1}\Bigr)\ \ge\ e > 1.
\]
Hence LLL never applies at the critical minimum degree threshold, even before the Kostochka–Thomason cores with \(\delta=\Omega(t\sqrt{\log t})\).

## Appendix B. First-moment monochromatic component size (regular tree proxy)

On the infinite \(d\)-regular tree, monochromatic exploration with retention probability \(1/k\) is a Galton–Watson process with offspring \(\mathrm{Bin}(d-1,1/k)\). Extinction probability \(<1\) iff \((d-1)/k>1\). For \(d=\lceil c t\sqrt{\log t}\rceil\) and \(k=t-1\), mean offspring \(\sim c\sqrt{\log t}>1\) for large \(t\). Thus infinite monochromatic components occur with positive probability in the tree proxy, signalling that random \((t-1)\)-colourings of dense minor-free cores leave giant monochromatic pieces.

## Appendix C. Separator cost

With \(|S|\le C t^{3/2}n^{1/2}\), a brute-force “new colours for \(S\)” recurrence \(T(n)\le\max_{n/3\le n'\le 2n/3} T(n')+|S|\) yields \(T(n)=O(t^{3/2}n^{1/2})\), i.e. \(\chi=O(t^{3/2}\sqrt{n})\), illustrating that separators without degeneracy or extension give polynomial-in-\(n\) colour bounds, not \(t-1\).

---

*End of note. Approach family status: BLOCKED for full Hadwiger; affirmative partial bound \(O(t\sqrt{\log t})\) recorded as Lemma 8.3.*
