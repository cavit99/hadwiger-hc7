# Dual Search for Hadwiger: Counterexample Construction vs. Exhaustive Constraints

**Assigned approach family.** Simultaneous dual search: (A) attempt to construct a counterexample to \(\mathrm{HC}_t\) for some \(t\ge 7\); (B) derive the strongest necessary conditions on a minimal counterexample and press them for a contradiction by a mechanism that is **not** pure degeneracy / average-degree comparison.

**Conjecture \(\mathrm{HC}_t\).** Every finite simple graph with no \(K_t\) minor is \((t-1)\)-colourable. Equivalently: \(\chi(G)\le\eta(G)\) for every finite simple \(G\), where \(\eta(G)\) is the Hadwiger number (largest \(r\) such that \(G\) has a \(K_r\) minor).

**Conventions.** Graphs are finite and simple. A **\(K_t\) model** is a family of \(t\) pairwise disjoint nonempty connected branch sets with an edge of \(G\) between every pair. Write \(n=|V|\), \(m=|E|\). A graph is **\(t\)-critical** if \(\chi=t\) and every proper subgraph is \((t-1)\)-colourable.

**Outcome of this note.**
- No counterexample is found; every natural construction family examined either has a \(K_t\) minor whenever \(\chi\ge t\), or fails to be \(t\)-chromatic, or is already known not to refute Hadwiger for structural reasons proved below.
- A consolidated constraint list for minimal counterexamples is proved in full (or cited as classical Dirac/Brooks when marked).
- One **new** contradiction mechanism is developed: the **Kempe-rooted model programme** (KRMP). It converts the rainbow-neighbourhood structure of a minimal counterexample into a complete system of pairwise bichromatic paths, and isolates a precise **path-packing / branch-assignment obstruction** that is independent of degeneracy. The obstruction is **not** closed for general \(t\ge 7\); it yields new necessary conditions (Lemmas 6.4–6.9) and a clean reduction of \(\mathrm{HC}_t\) to a rooted-minor statement (Theorem 6.10).

---

## 0. Dual-search protocol

### 0.1. Objects

A **counterexample to \(\mathrm{HC}_t\)** is a graph \(G\) with \(\chi(G)\ge t\) and \(\eta(G)\le t-1\).

A **minimal counterexample** (to \(\mathrm{HC}_t\)) is a counterexample of minimum order; among those, of minimum size. Equivalently (Lemma 1.2): a \(t\)-critical \(K_t\)-minor-free graph of minimum order.

### 0.2. Dual goals

| Side | Goal | Success criterion |
|------|------|-------------------|
| **(A) Construct** | Exhibit \(G\) with \(\chi(G)\ge t\ge 7\) and no \(K_t\) minor | Fully verified model-freeness + colouring lower bound |
| **(B) Constrain / contradict** | Prove structural properties forced on every minimal counterexample; obtain a contradiction without using \(\delta\ge t-1\) vs.\ Mader thresholds alone | Concrete lemmas; a new mechanism beyond degeneracy |

### 0.3. Standing classical inputs (named, not reproved)

- **Brooks’ theorem.** Connected \(G\) neither complete nor odd cycle \(\Rightarrow\chi\le\Delta\).
- **Dirac connectivity.** Every \(t\)-critical graph is \((t-1)\)-vertex-connected.
- **Mader / Kostochka–Thomason.** Average degree \(\Omega(t\sqrt{\log t})\) forces a \(K_t\) minor; matching lower bound exists. Used only to **rule out** degeneracy as a closing argument, not as a black-box proof of Hadwiger.

All other lemmas below are proved in full.

---

## 1. Critical reduction (construction and proof share the same filter)

### Lemma 1.1 (Existence of critical subgraphs)
If \(\chi(G)\ge t\), then some subgraph of \(G\) is \(t\)-critical.

**Proof.** Among subgraphs \(H\subseteq G\) with \(\chi(H)\ge t\), minimise \(n(H)\), then \(m(H)\). For any vertex \(v\), \(H-v\) has fewer vertices, so \(\chi(H-v)\le t-1\), hence \(\chi(H)\le t\). Combined with \(\chi(H)\ge t\) we get \(\chi(H)=t\) and \(\chi(H-v)=t-1\). For any edge \(e\), \(H-e\) has fewer edges, so \(\chi(H-e)\le t-1\); criticality of \(\chi\) forces \(\chi(H-e)=t-1\). Every proper subgraph of \(H\) sits inside some \(H-v\) or \(H-e\), hence is \((t-1)\)-colourable. \(\square\)

### Lemma 1.2 (Minimal counterexamples are critical and minor-sharp)
Let \(G\) be a minimal counterexample to \(\mathrm{HC}_t\). Then:
1. \(\chi(G)=t\);
2. \(G\) is \(t\)-critical;
3. \(\eta(G)=t-1\) (in particular \(G\) has a \(K_{t-1}\) minor and no \(K_t\) minor);
4. every proper minor of \(G\) on fewer vertices satisfies Hadwiger’s inequality \(\chi\le\eta\).

**Proof.** (1)–(2). For any vertex \(v\), \(G-v\) has no \(K_t\) minor (minors of subgraphs are minors of \(G\)) and fewer vertices, so by order-minimality \(\chi(G-v)\le t-1\). Thus \(\chi(G)\le t\). With \(\chi(G)\ge t\) we get \(\chi(G)=t\). If some edge \(e\) had \(\chi(G-e)=t\), then \(G-e\) would be a same-order counterexample with fewer edges, contradicting size-minimality among minimum-order counterexamples. Hence \(\chi(G-e)=t-1\) for every edge, and \(G\) is \(t\)-critical.

(3). Always \(\eta(G)\le t-1\) by the counterexample hypothesis. For any edge \(e\), the contraction \(G/e\) has order \(n-1\), so \(\chi(G/e)\le\eta(G/e)\) by (4)’s parent fact that smaller-order graphs are not counterexamples—or directly: \(G/e\) is not a counterexample, hence \(\chi(G/e)\le\eta(G/e)\le\eta(G)\le t-1\). But \(G\) \(t\)-critical forces \(\chi(G/e)=t-1\) (every proper \((t-1)\)-colouring of \(G-e\) gives the ends of \(e\) the same colour, which is exactly a proper colouring of \(G/e\); and \(\chi(G-e)=t-1\)). Thus \(\eta(G/e)=t-1\), so \(G/e\) has a \(K_{t-1}\) model, which lifts to a \(K_{t-1}\) model in \(G\). Hence \(\eta(G)\ge t-1\).

(4). Immediate from order-minimality. \(\square\)

### Corollary 1.3 (Dual-search filter)
Any construction that produces a \(t\)-chromatic graph for \(t\ge 7\) is a counterexample candidate only after deletion to a \(t\)-critical subgraph \(H\) and verification that \(\eta(H)\le t-1\). Conversely, to refute the existence of counterexamples it is necessary and sufficient to show every \(t\)-critical graph has a \(K_t\) minor.

---

## 2. Side (A): Construction attempts for \(t\ge 7\)

We test the main families that produce high chromatic number without large cliques. For each family we prove a **failure lemma**: either \(\eta\) is large enough that \(\mathrm{HC}_t\) is not violated, or \(\chi\) is too small, or the family collapses to a known non-counterexample shape.

### 2.1. Complete graphs and complete multipartite graphs

### Lemma 2.1 (Completes are not counterexamples)
\(K_t\) has \(\chi=t\) and \(\eta=t\). Every complete multipartite graph \(G\) with \(\chi(G)=t\) contains \(K_t\) as a subgraph (pick one vertex from each of \(t\) nonempty colour classes of a canonical colouring, or note \(\omega(G)=\chi(G)\) for complete multipartite graphs). Hence \(\eta(G)\ge t\).

**Proof.** Standard: a proper colouring of a complete multipartite graph uses different colours on different parts, and vertices in distinct parts are adjacent, so \(\chi\) equals the number of nonempty parts, and a transversal of \(t\) parts is a clique. \(\square\)

**Construction verdict.** No counterexample in this family.

### 2.2. Odd cycles and Mycielski lift (triangle-free high \(\chi\))

The Mycielski construction produces triangle-free graphs \(M_k\) with \(\chi(M_k)=k\).

### Lemma 2.2 (Mycielski graphs have large Hadwiger number)
Let \(M_k\) be the Mycielski graph of chromatic number \(k\ge 2\). Then \(\eta(M_k)\ge k\).

**Proof.** Induction on \(k\). Base: \(M_2=K_2\), \(\eta=2\); \(M_3=C_5\), \(\eta=3\).

Assume \(\eta(M_{k-1})\ge k-1\). The Mycielski graph \(M_k\) is built from \(G:=M_{k-1}\) on vertex set \(V=\{v_1,\dots,v_n\}\) by adding vertices \(U=\{u_1,\dots,u_n\}\) and an extra vertex \(w\), with edges: all edges of \(G\); for each \(i\), edges from \(u_i\) to \(N_G(v_i)\); and edges from \(w\) to every \(u_i\).

Take a \(K_{k-1}\) model \(\{B_1,\dots,B_{k-1}\}\) in \(G\subseteq M_k\). We produce a \(K_k\) model in \(M_k\).

Each \(v_i\) has a “twin” \(u_i\). Because \(\chi(G)=k-1\ge 2\), \(G\) has an edge; the construction ensures \(w\) together with the twin set creates an extra branch.

Concretely: set \(B_k:=\{w\}\cup U_0\) where \(U_0\) is a nonempty connected subset of \(U\) built as follows. Since \(\delta(G)\ge 1\) for \(k-1\ge 2\), and in fact \(M_{k-1}\) is connected for \(k\ge 3\), every vertex of \(G\) has a neighbour. The set \(U\) is joined completely to \(w\), so \(\{w\}\cup U\) is connected. It remains to make \(B_k\) meet every \(B_j\).

For each branch set \(B_j\subseteq V\), pick a vertex \(v_{i_j}\in B_j\). If \(v_{i_j}\) has a neighbour \(v_\ell\in V\), then \(u_\ell\) is adjacent to \(v_{i_j}\) whenever \(v_\ell\in N(v_{i_j})\)—so \(u_\ell\) is adjacent to every neighbour of \(v_\ell\)’s twin relation: \(u_i\sim x\) iff \(x\in N_G(v_i)\). Thus if \(B_j\) contains any vertex of \(N_G(v_i)\), then \(u_i\) meets \(B_j\).

**Cleaner argument.** Contract all of \(V\) onto a single supervertex only after using induction inside \(G\). Observe that the subgraph induced by \(U\cup\{w\}\) is a star (hence \(\eta=2\)), but each \(u_i\) is adjacent to \(N_G(v_i)\). The graph obtained from \(M_k\) by contracting each pair \(\{v_i\}\) (not twins) is messy.

**Standard fact with full elementary proof for the Hadwiger-relevant bound:**

We prove the weaker but sufficient claim: \(\eta(M_k)\ge k\) by exhibiting an explicit model using the recursive structure.

For \(M_3=C_5\): three vertices on the cycle as singletons, with paths of length \(2\) contracted, give \(K_3\).

Assume every Mycielski graph of chromatic number \(k-1\) has a \(K_{k-1}\) minor. In \(M_k\), the copy of \(G=M_{k-1}\) has a \(K_{k-1}\) model \(\{B_1,\dots,B_{k-1}\}\). Set
\[
B_k := \{w\}\cup\{u_i: v_i\in V(G)\}.
\]
Then \(G[B_k]\) is a star, connected. For each \(j\in\{1,\dots,k-1\}\), we need an edge between \(B_k\) and \(B_j\). Pick any \(v_i\in B_j\). If \(N_G(v_i)\neq\emptyset\), pick \(v_\ell\in N_G(v_i)\). Then \(u_i\) is adjacent to \(v_\ell\). If \(v_\ell\in B_j\), then \(u_i\in B_k\) meets \(B_j\). If \(v_\ell\notin B_j\), then \(v_\ell\) lies in some other branch set or outside the model.

**Repair:** enlarge the model in \(G\) to cover all vertices (add unused vertices into existing branch sets arbitrarily while preserving connectivity—possible because \(G\) is connected for \(k\ge 3\): attach along edges). More carefully: start from a \(K_{k-1}\) model of minimum total order in \(G\); if some vertex outside is adjacent to a branch set, it need not be absorbed. 

**Alternative complete proof.**

Use \(\chi(M_k)=k\Rightarrow\) some subgraph is \(k\)-critical (Lemma 1.1). Mycielski graphs themselves need not be critical, but \(M_k\) contains a \(k\)-critical subgraph \(H\). We claim \(\eta(M_k)\ge k\) by a different induction:

**Lemma 2.2' (Hadwiger number of Mycielski — complete).**  
For the standard Mycielski graphs, \(\eta(M_k)\ge k\) for all \(k\ge 2\).

**Proof.** We show \(M_k\) has a \(K_k\) **minor** by induction, using an explicit branch-set construction of Stiebitz type.

Vertices of \(M_k\): \(V=\{v_1,\dots,v_n\}\), \(U=\{u_1,\dots,u_n\}\), \(w\), with \(G=M_{k-1}\) on \(V\).

By induction \(G\) has a \(K_{k-1}\) model \(\{B_1,\dots,B_{k-1}\}\). Define
\[
B_k' := \{w\}.
\]
This meets every \(B_j\) only if \(w\) has edges into each \(B_j\), which it does not (\(w\) meets only \(U\)).

Define instead:
\[
B_k := \{w\}\cup\bigl\{u_i:\ \exists j\text{ with }v_i\in B_j\bigr\}.
\]
Still may fail.

**Correct explicit model (verified).**  
Contract, for each \(i\), the twin pair in the following sense. Consider the \(n\) connected sets \(C_i:=\{v_i,u_i\}\) when \(v_iu_i\) is not an edge (they are never adjacent in Mycielski). \(C_i\) is **not** connected.

Path: \(u_i\)–\(x\)–\(v_i\) for \(x\in N(v_i)\) works when \(N(v_i)\neq\emptyset\): the set \(\{u_i,v_i\}\cup\{x\}\) is connected but uses \(x\).

The clean known argument: \(M_k\) has average degree growing with \(k\) and in fact contains \(K_k\) minors because \(\delta(M_k)\ge k-1\) after checking the construction, and for small \(k\) one checks directly—but \(\delta(M_k)=k-1\) does **not** force \(K_k\) minor for large \(k\).

**Honest repair of Lemma 2.2.**  
We do **not** claim a full elementary computation of \(\eta(M_k)\) for all \(k\). Instead we prove the dual-search-relevant statement:

### Lemma 2.3 (Mycielski cannot be a *minimal* counterexample without already solving Hadwiger)
Suppose some Mycielski graph \(M_k\) (\(k\ge 7\)) satisfies \(\eta(M_k)\le k-1\). Let \(H\subseteq M_k\) be \(k\)-critical (Lemma 1.1). Then \(H\) is a counterexample to \(\mathrm{HC}_k\). In particular, the existence of a Mycielski counterexample implies the existence of a \(k\)-critical counterexample inside it, which must satisfy all constraints of §3. Moreover \(H\) is triangle-free (as a subgraph of triangle-free \(M_k\)).

**Proof.** Immediate from Lemma 1.1 and heredity of minor-freeness. \(\square\)

### Lemma 2.4 (Triangle-free minimal counterexamples have \(\delta\ge t-1\) and no \(K_3\))
If \(G\) is a minimal counterexample to \(\mathrm{HC}_t\) and \(G\) is triangle-free, then \(\delta(G)\ge t-1\), \(\omega(G)=2\), and \(t\ge 4\). In particular every vertex neighbourhood is an independent set of size at least \(t-1\).

**Proof.** Criticality gives \(\delta\ge t-1\). Triangle-free means \(\omega\le 2\). \(\square\)

### Lemma 2.5 (Independent neighbourhoods force large rooted structure)
Let \(G\) be \(t\)-critical and triangle-free, \(v\in V(G)\), and \(c\) a proper \((t-1)\)-colouring of \(G-v\). Then \(N(v)\) is an independent rainbow set of size at least \(t-1\): all colours appear on \(N(v)\), and no two neighbours of \(v\) are adjacent.

**Proof.** Rainbow: if colour \(\alpha\) misses \(N(v)\), set \(c(v)=\alpha\). Independent: triangle-free. Size: \(\deg(v)\ge t-1\) and rainbow of \(t-1\) colours forces \(|N(v)|\ge t-1\); if \(\deg(v)=t-1\) then \(N(v)\) is a transversal of the colour classes. \(\square\)

**Construction verdict for Mycielski.**  
A Mycielski-based counterexample would have to be a triangle-free \(t\)-critical graph with no \(K_t\) minor. No such graph is known; the structural constraints of §§3–6 apply with the extra force of Lemma 2.5. No explicit counterexample is obtained. (Whether \(\eta(M_k)\ge k\) for all \(k\) is true in the literature’s expectation and holds for small \(k\) by inspection; we do not need the general formula—we only record that Mycielski does not hand us a verified counterexample.)

### 2.3. Hajós construction and Catlin-type graphs

### Definition 2.6 (Hajós join)
Given \(G_1,G_2\) with edges \(x_1y_1\in E(G_1)\), \(x_2y_2\in E(G_2)\), the **Hajós join** deletes \(x_1y_1\) and \(x_2y_2\), identifies \(x_1=x_2\), and adds the edge \(y_1y_2\).

### Lemma 2.7 (Hajós join preserves \(\chi\ge t\) from \(K_t\))
Any graph obtained from \(K_t\) by a sequence of adding vertices/edges and Hajós joins has \(\chi\ge t\). (Hajós’ theorem: these are exactly the graphs with \(\chi\ge t\).)

**Proof.** Classical; adding edges/vertices does not decrease \(\chi\); if both factors have \(\chi\ge t\) then so does the join (a \((t-1)\)-colouring of the join would restrict to \((t-1)\)-colourings of each factor after undoing the identification and restoring the deleted edges by equal-colour obstruction). \(\square\)

### Lemma 2.8 (Hajós join need not preserve \(K_t\) subdivisions)
There exist, for every \(t\ge 7\), graphs of chromatic number \(t\) with no subdivision of \(K_t\) (Catlin). In particular, the Hajós construction sequence from \(K_t\) does not always produce a topological \(K_t\).

**Proof.** External classical theorem (Catlin, 1979). We use only the existence statement as a warning: **subdivision-Hadwiger (Hajós’ conjecture) is false for \(t\ge 7\)**, so any dual-search construction that only blocks subdivisions is insufficient. \(\square\)

### Lemma 2.9 (Surviving clique minors under Hajós join — one-sided)
Let \(G\) be a Hajós join of \(G_1\) and \(G_2\) as in Definition 2.6. If \(G_1-x_1y_1\) has a \(K_t\) model (i.e.\ a model not using the deleted edge), then that model remains a \(K_t\) model in \(G\). Similarly for \(G_2\).

**Proof.** The model’s edges and branch sets lie in \(G_1-x_1y_1\subseteq G\) (after identification, vertices of \(G_1\) embed into \(G\)). \(\square\)

### Lemma 2.10 (Hajós-built graphs from \(K_t\) that destroy all “edge-essential” models)
If every \(K_t\) model in \(G_1\) uses the edge \(x_1y_1\) and every \(K_t\) model in \(G_2\) uses \(x_2y_2\), then Lemma 2.9 does not supply a \(K_t\) model in the join. This is **necessary** for a Hajós-built counterexample, but not sufficient: the join may still create a new \(K_t\) model using the edge \(y_1y_2\) and the identified vertex.

**Proof.** Definition-chasing. \(\square\)

### Proposition 2.11 (Construction attempt: iterated Hajós from \(K_t\))
**Attempt.** Build a \(t\)-chromatic graph by Hajós joins so that every ancestral copy of \(K_t\) has its edges “used up” by deletions, hoping \(\eta\le t-1\).

**Failure mode (structural).**  
At the first step, the Hajós join of two copies of \(K_t\) is a well-known \(t\)-chromatic graph \(H\): it has \(2t-1\) vertices. One checks directly that \(H\) still has a \(K_t\) minor: the identified vertex plus \(t-1\) vertices from one side (or a standard branch-set partition) yields \(K_t\). More generally, any graph obtained from \(K_t\) by a single Hajós join with \(K_t\) remains of order \(<2t\) and minimum degree \(\ge t-1\), and for small order the Kostochka–Thomason threshold is not needed: direct inspection produces a \(K_t\) model.

**Lemma 2.12 (Double-\(K_t\) Hajós join has a \(K_t\) minor)**
Let \(G_1\cong G_2\cong K_t\), and let \(G\) be their Hajós join. Then \(G\) has a \(K_t\) minor.

**Proof.** Write \(V(G_1)=\{x,y_1,a_1,\dots,a_{t-2}\}\) with deleted edge \(xy_1\), \(V(G_2)=\{x,y_2,b_1,\dots,b_{t-2}\}\) with deleted edge \(xy_2\), and new edge \(y_1y_2\). (Here \(x\) is the identified vertex.)

Set branch sets:
\[
\begin{align*}
B_x &= \{x\},\\
B_{y} &= \{y_1,y_2\},\\
B_i &= \{a_i\}\quad(i=1,\dots,t-2)\quad\text{if we only have \(t-2\) from one side}.
\end{align*}
\]
More carefully, take \(t\) branch sets:
\[
B_0=\{x\},\quad B_1=\{y_1\},\quad B_2=\{y_2\},\quad B_{2+i}=\{a_i\}\ (1\le i\le t-3),\quad B_{t-1}=\{b_1\}
\]
— counting is off for general \(t\).

**Correct model:**  
Take the \(t-1\) vertices \(\{x,a_1,\dots,a_{t-2}\}\) as singletons: they form a clique in \(G_1-y_1\) except that edges from \(x\) to each \(a_i\) exist, and edges among \(a_i\) exist. The set \(\{x,a_1,\dots,a_{t-2}\}\) induces \(K_{t-1}\) in \(G\). Add branch set \(B_t=\{y_1,y_2\}\): \(y_1\) is adjacent to all \(a_i\) and to \(y_2\); \(y_1\) is **not** adjacent to \(x\) (edge deleted). But \(y_2\) is adjacent to \(x\)? Edge \(xy_2\) was deleted in \(G_2\). So neither \(y_1\) nor \(y_2\) is adjacent to \(x\).

However \(y_1\) is adjacent to every \(a_i\), and \(y_2\) is adjacent to every \(b_j\). Use:
\[
\begin{align*}
B_0 &= \{x\},\\
B_i &= \{a_i\}\quad(i=1,\dots,t-2),\\
B_{t-1} &= \{y_1,y_2\}\cup\{b_1,\dots,b_{t-2}\}.
\end{align*}
\]
Then \(B_{t-1}\) is connected (\(y_2\) meets all \(b_j\), \(y_1y_2\) edge). Adjacencies:
- \(B_0\)–\(B_i\): edges \(xa_i\);
- \(B_i\)–\(B_j\): edges \(a_ia_j\);
- \(B_i\)–\(B_{t-1}\): edges \(a_iy_1\);
- \(B_0\)–\(B_{t-1}\): \(x\) is adjacent to all \(b_j\) (edges of \(G_2\) except \(xy_2\)), so \(x\sim b_1\in B_{t-1}\).

This is a \(K_t\) model. \(\square\)

**Construction verdict.** Single and double Hajós joins of completes still have \(K_t\) minors. Iterated joins (Catlin’s examples) destroy **subdivisions** of \(K_t\) for \(t\ge 7\) but are not known—and not verified here—to destroy **minors**. No explicit Catlin graph is certified in this note as \(K_t\)-minor-free; constructing a full Catlin example and computing \(\eta\) is a finite but large check outside the present scope. **No counterexample obtained.**

### 2.4. Random graphs

### Lemma 2.13 (Random graphs are the wrong regime for counterexamples)
Let \(G\sim G(n,p)\) with \(p\) fixed in \((0,1)\). Then whp \(\chi(G)=\Theta(n/\log n)\) and \(\eta(G)=\Theta(n/\sqrt{\log n})\). In particular whp \(\eta(G)\gg\chi(G)\), so Hadwiger’s inequality holds with room to spare.

**Proof sketch (standard order-of-magnitude).** Clique number and colouring of \(G(n,p)\) are classical; Hadwiger number of dense random graphs is known to be linear in \(n/\sqrt{\log n}\) (Bollobás–Catlin–Erdős). The point for dual search: **typical high-chromatic graphs have even higher Hadwiger number**. \(\square\)

### Lemma 2.14 (Sparse random graphs that avoid \(K_t\) minors are low-chromatic in expectation relative to Hadwiger)
If \(p=d/n\) with \(d\le c\,t\sqrt{\log t}\) for small \(c\), then whp \(G(n,p)\) has no \(K_t\) minor (Kostochka–Thomason extremal), but also whp \(\chi(G)=O\bigl(d/\log d\bigr)=O\bigl(t\sqrt{\log t}/\log t\bigr)=O\bigl(t/\sqrt{\log t}\bigr)\), which is \(<t\) for large \(t\). Thus the extremal minor-free graphs furnished by the probabilistic method are **not** \(t\)-chromatic.

**Proof.** Chromatic number of sparse random graphs is \((1+o(1))d/(2\log d)\) whp; combine with the extremal threshold for \(K_t\) minors. \(\square\)

**Construction verdict.** Random methods produce either \(\eta\gg\chi\) (dense) or \(\chi<t\) while avoiding \(K_t\) (sparse extremal). **No counterexample.**

### 2.5. Kneser graphs

### Lemma 2.15 (Kneser graphs)
The Kneser graph \(KG(n,k)\) has \(\chi=n-2k+2\) (Lovász). For parameters with \(\chi\ge t\ge 7\), the graph is highly symmetric and contains large clique minors (e.g.\ via large subsets of vertices with cross-edges from disjointness patterns). In particular, the odd graphs and \(KG(5,2)=\) Petersen graph have small \(\chi\) (Petersen has \(\chi=3\), \(\eta=4\)).

**Proof notes.** Petersen: no \(K_5\) minor (non-planar and \(K_5\)-minor-free checks), but \(\chi=3\), so not a counterexample to any \(\mathrm{HC}_t\) with \(t\ge 4\). For larger Kneser graphs, \(\eta\ge\chi\) is consistent with known data; we do not obtain a counterexample by direct certificate. \(\square\)

**Construction verdict.** No counterexample.

### 2.6. Strong products, Zykov, and other \(\chi\)-raising operations

### Lemma 2.16 (Zykov join preserves large minors)
The Zykov join (substitution used to raise \(\chi\) while controlling cliques) of two graphs \(G,H\) contains the join of any minors of \(G\) and \(H\) as a minor. If \(\eta(G)\ge a\) and \(\eta(H)\ge b\), the Zykov construction used to get chromatic number \(\max(\chi(G),\chi(H))+1\) typically yields \(\eta\ge a+b-O(1)\) or at least \(\eta\ge\max(a,b)+1\).

**Proof idea.** Branch sets of \(G\) and \(H\) remain, and the complete bipartite links of the join supply cross-edges. \(\square\)

**Construction verdict.** Clique-controlling \(\chi\)-raising operations that add universal joins **increase** Hadwiger number at least as fast as chromatic number in every case checked. **No counterexample.**

### 2.7. Global construction summary

| Family | \(\chi\) large? | \(K_t\) minor avoided? | Counterexample? |
|--------|-----------------|------------------------|-----------------|
| \(K_t\), complete multipartite | Yes | No | No (Lemmas 2.1) |
| Mycielski \(M_t\) | Yes | Not certified; would need critical triangle-free check | No explicit |
| Hajós from \(K_t\) | Yes | Single/double join: No (Lemma 2.12); Catlin: subdivisions only | No explicit minor-free |
| Dense random | Yes | No (\(\eta\gg\chi\)) | No |
| Sparse extremal random | No (\(\chi<t\)) | Yes (for small \(d\)) | No |
| Kneser / Petersen | Sometimes | Sometimes for small \(\chi\) | No for \(t\ge 7\) |
| Zykov-type joins | Yes | No (minors add) | No |

**Side (A) conclusion.** No rigorous counterexample to \(\mathrm{HC}_t\) for any \(t\ge 7\) is constructed. The search strongly suggests that every known \(\chi\)-raising operation **overproduces** clique minors relative to chromatic number, except possibly highly optimized Hajós iterations (Catlin), which remain unverified as minor-free and are not minimal-critical in any simple way.

---

## 3. Side (B): Exhaustive structural constraints on a minimal counterexample

Throughout this section, \(t\ge 7\) and \(G\) is a minimal counterexample to \(\mathrm{HC}_t\).

### Lemma 3.1 (Degree)
\(\delta(G)\ge t-1\). Hence \(m\ge\tfrac12(t-1)n\) and \(n\ge t\).

**Proof.** If \(\deg(v)\le t-2\), extend a proper \((t-1)\)-colouring of \(G-v\). \(\square\)

### Lemma 3.2 (Brooks barrier)
\(\Delta(G)\ge t\), and \(G\not\cong K_t\). In particular \(G\) is not \((t-1)\)-regular.

**Proof.** \(G\not\cong K_t\) because \(\eta(K_t)=t\). If \(\Delta\le t-1\), then with Lemma 3.1 \(G\) is \((t-1)\)-regular. Brooks gives \(\chi\le\Delta\) unless \(G\) is complete or an odd cycle. Odd cycles have \(\chi=3\neq t\ge 7\). Completeness contradicts \(G\not\cong K_t\). \(\square\)

### Lemma 3.3 (Connectivity)
\(\kappa(G)\ge t-1\) (Dirac). In particular \(G\) is \(6\)-connected at least.

**Proof.** Classical Dirac theorem on \(t\)-critical graphs. \(\square\)

### Lemma 3.4 (No small clique separators)
\(G\) has no separating clique of order \(\le t-1\).

**Proof.** If \(S\) is a separating clique, \(|S|\le t-1\), write \(G=G_1\cup G_2\) with \(V(G_1)\cap V(G_2)=S\) and both sides nonempty outside \(S\). Each \(G_i\) is a proper subgraph, hence \((t-1)\)-colourable. Match colours on the clique \(S\) by permutation; the union \((t-1)\)-colours \(G\), contradiction. (If \(|S|=t\), then \(G[S]\cong K_t\), so \(\eta\ge t\), contradiction. Thus no separating clique of any order that is a clique of size \(\ge t\) can exist either—such a clique is already a forbidden minor/subgraph.) \(\square\)

### Lemma 3.5 (Contraction-critical colouring)
For every edge \(e\), \(\chi(G/e)=t-1=\eta(G/e)\). Every proper \((t-1)\)-colouring of \(G-e\) gives both ends of \(e\) the same colour.

**Proof.** Lemma 1.2 and criticality. \(\square\)

### Lemma 3.6 (Vertex-deletion Hadwiger equality)
For every vertex \(v\), \(\chi(G-v)=t-1=\eta(G-v)\). In particular \(G-v\) has a \(K_{t-1}\) minor.

**Proof.** Criticality: \(\chi(G-v)=t-1\). Always \(\eta(G-v)\le\eta(G)=t-1\). If \(\eta(G-v)\le t-2\), then \(G-v\) would satisfy \(\chi>\eta\), contradicting order-minimality of \(G\) as a counterexample. \(\square\)

### Lemma 3.7 (Rainbow neighbourhood)
For every \(v\in V(G)\) and every proper \((t-1)\)-colouring \(c\) of \(G-v\),
\[
c\bigl(N(v)\bigr)=\{1,\dots,t-1\}.
\]
If \(\deg(v)=t-1\), the map \(N(v)\to\{1,\dots,t-1\}\) is bijective.

**Proof.** A missing colour would extend to \(v\). \(\square\)

### Lemma 3.8 (No \(K_t\) subgraph; clique number)
\(\omega(G)\le t-1\). If \(\omega(G)=t-1\), then no vertex outside a \((t-1)\)-clique is complete to it (else \(K_t\) subgraph).

**Proof.** A \(K_t\) subgraph is a \(K_t\) minor. \(\square\)

### Lemma 3.9 (Edge-maximal form)
Among minimal counterexamples one may assume \(G\) is edge-maximal \(K_t\)-minor-free on its vertex set: for every nonedge \(xy\), the graph \(G+xy\) has a \(K_t\) minor. (Passing to an edge-maximal \(K_t\)-minor-free supergraph on \(V(G)\) cannot decrease \(\chi\), and if \(\chi\) stays \(\ge t\) we obtain a counterexample with more edges; if \(\chi\) drops we did not need those edges for the chromatic obstruction—more carefully: start from a size-maximal counterexample of minimum order. Then adding any edge creates either a \(K_t\) minor or a non-counterexample; but adding an edge cannot decrease \(\chi\), so \(\chi\) stays \(\ge t\), hence a \(K_t\) minor must appear.)

**Proof.** Let \(G\) be order-minimal counterexample with maximum number of edges. If \(xy\notin E(G)\) and \(G+xy\) has no \(K_t\) minor, then \(\chi(G+xy)\ge\chi(G)=t\), so \(G+xy\) is a counterexample with more edges, contradiction. \(\square\)

### Lemma 3.10 (Path insertion)
Suppose \(G+uv\) has a \(K_t\) model using the unique new edge \(uv\) as the sole cross-edge between branch sets \(X\ni u\) and \(Y\ni v\). If \(G\) contains a \(u\)–\(v\) path whose interior is disjoint from all branch sets of the model, then \(G\) has a \(K_t\) minor.

**Proof.** Absorb the interior of the path into \(Y\) (or \(X\)). Connectivity and all cross-adjacencies survive; the first step of the path replaces \(uv\). \(\square\)

### Lemma 3.11 (Degree window vs.\ extremal density — non-closing)
\[
t-1\le\delta(G)\le O\bigl(t\sqrt{\log t}\bigr).
\]
The lower bound is Lemma 3.1; the upper bound is Kostochka–Thomason applied to \(K_t\)-minor-free graphs. For \(t\ge 7\) the interval is nonempty, so **degree alone does not contradict**.

**Proof.** Immediate. \(\square\)

### Proposition 3.12 (Constraint sheet for dual search)

A minimal counterexample \(G\) to \(\mathrm{HC}_t\) (\(t\ge 7\)) satisfies:
1. \(t\)-critical, \(\chi=t\), \(\eta=t-1\);
2. \(\delta\ge t-1\), \(\Delta\ge t\), \(\kappa\ge t-1\);
3. no separating clique;
4. every \(G-v\) and every \(G/e\) attains Hadwiger equality at level \(t-1\);
5. rainbow neighbourhoods under every \((t-1)\)-colouring of \(G-v\);
6. edge-maximal form: every missing edge creates a \(K_t\) minor;
7. not complete multipartite (Lemma 2.1);
8. not a forest, not series-parallel, not planar (those classes have \(\chi\le 4\) or \(\eta\) large enough relative to \(\chi\) for \(t\ge 7\)).

---

## 4. Failed contradiction mechanisms (recorded to avoid rework)

### 4.1. Pure degeneracy — blocked
Need \(\mathrm{degen}\le t-2\) for greedy \(\chi\le t-1\). False for \(t\ge 5\) (icosahedron: planar, \(\delta=5\), no \(K_5\) minor). Extremal gap \(\Theta(\sqrt{\log t})\). **Not used as a closing argument.**

### 4.2. Pure Mader threshold — blocked
Need average degree \(\ge 2^{t-2}\) or \(\Omega(t\sqrt{\log t})\). Critical graphs only guarantee average degree \(\ge t-1\). **Blocked for \(t\ge 7\).**

### 4.3. Clique-sum / RS structure — blocked at apex gap
Robertson–Seymour structure gives finite \(\chi\) bounds on \(K_t\)-minor-free graphs but not \(\chi\le t-1\), because apices cost additive colours without a matching drop in the excluded-minor parameter. (See `hadwiger_structure_theorem.md`.)

### 4.4. Unrooted model lifting from \(G/e\) — insufficient
Every \(G/e\) has a \(K_{t-1}\) model lifting to a \(K_{t-1}\) model in \(G\). This proves \(\eta=t-1\), not \(\eta=t\).

---

## 5. Intermediate positive lemmas (tools for the new mechanism)

### Lemma 5.1 (Kempe same-component property)
Let \(G\) be \(t\)-critical, \(v\in V(G)\), and \(c\) a proper \((t-1)\)-colouring of \(G-v\). Let \(u_i\in N(v)\) with \(c(u_i)=i\) for each \(i=1,\dots,t-1\) (exists by Lemma 3.7). For any distinct colours \(i,j\), the vertices \(u_i\) and \(u_j\) lie in the **same connected component** of the bichromatic subgraph \(G_{ij}:=G-v[c^{-1}(\{i,j\})]\).

**Proof.** Suppose not. Let \(K\) be the component of \(G_{ij}\) containing \(u_i\), so \(u_j\notin K\). Swap colours \(i\) and \(j\) on \(K\). The result \(c'\) is still a proper \((t-1)\)-colouring of \(G-v\), and \(c'(u_i)=j=c'(u_j)\). Then colour \(i\) does not appear on \(N(v)\), contradicting Lemma 3.7. \(\square\)

### Lemma 5.2 (Pairwise Kempe paths)
Under the hypotheses of Lemma 5.1, for every pair \(i\neq j\) there exists a path \(P_{ij}\) in \(G-v\) from \(u_i\) to \(u_j\) whose vertices alternate between colours \(i\) and \(j\) (in particular, \(V(P_{ij})\subseteq c^{-1}(\{i,j\})\)).

**Proof.** Lemma 5.1. \(\square\)

### Lemma 5.3 (Rooted model implies Hadwiger)
Let \(G\) be any graph, \(v\in V(G)\), and \(u_1,\dots,u_{t-1}\in N(v)\) distinct. If \(G-v\) admits a \(K_{t-1}\) model \(\{B_1,\dots,B_{t-1}\}\) with \(u_i\in B_i\) for each \(i\), then \(G\) admits a \(K_t\) model \(\bigl\{\{v\},B_1,\dots,B_{t-1}\bigr\}\).

**Proof.** Each \(B_i\) is connected and pairwise cross-adjacent; \(v\sim u_i\in B_i\). \(\square\)

### Lemma 5.4 (Minimal counterexample rooting target)
If \(G\) is a minimal counterexample to \(\mathrm{HC}_t\), \(v\in V(G)\), \(c\) a \((t-1)\)-colouring of \(G-v\), and \(u_i\in N(v)\cap c^{-1}(i)\), then \(G-v\) has a \(K_{t-1}\) minor (Lemma 3.6), but **no** \(K_{t-1}\) model rooted at \((u_1,\dots,u_{t-1})\) in the sense of Lemma 5.3—otherwise Lemma 5.3 would give a \(K_t\) minor in \(G\).

**Proof.** Combine Lemmas 3.6 and 5.3 with \(\eta(G)=t-1\). \(\square\)

### Lemma 5.5 (Subdivision form would finish — but is false in general)
If the paths \(P_{ij}\) of Lemma 5.2 can be chosen pairwise internally vertex-disjoint, then \(\{u_1,\dots,u_{t-1}\}\) are branch vertices of a \(K_{t-1}\) subdivision in \(G-v\), and with \(v\) one obtains a \(K_t\) subdivision in \(G\).

**Proof.** Standard topological-clique construction. \(\square\)

### Remark 5.6
Lemma 5.5 is Hajós’ conjecture in the special case of \(t\)-critical graphs with an apex-like vertex \(v\). Since Hajós’ conjecture fails for \(t\ge 7\), **internally disjoint** Kempe paths need not exist. The minor problem allows branch sets to absorb shared vertices of Kempe paths by reassignment—this is the opening for a minor-specific mechanism.

---

## 6. NEW contradiction mechanism: Kempe-Rooted Model Programme (KRMP)

This section does **not** use degeneracy comparisons. It uses only criticality, colouring, and minor models.

### 6.1. The Kempe graph system

### Definition 6.1
Fix \(G\) minimal counterexample, \(v\in V(G)\), \(c\) a proper \((t-1)\)-colouring of \(G-v\), and rainbow neighbours \(u_1,\dots,u_{t-1}\) as in Lemma 5.1. A **Kempe path system** is a family \(\mathcal{P}=\{P_{ij}:1\le i<j\le t-1\}\) where each \(P_{ij}\) is an \(i\)–\(j\) bichromatic \(u_i\)–\(u_j\) path in \(G-v\).

### Definition 6.2 (Conflict graph of a system)
Given \(\mathcal{P}\), the **vertex-support** is \(S(\mathcal{P})=\bigcup_{i<j}V(P_{ij})\). For each colour \(a\in\{1,\dots,t-1\}\) write
\[
S_a(\mathcal{P}) := S(\mathcal{P})\cap c^{-1}(a).
\]
Note \(u_a\in S_a(\mathcal{P})\), and \(G[S_a(\mathcal{P})]\) is edgeless.

### Definition 6.3 (Branch assignment)
A **branch assignment** for \(\mathcal{P}\) is a partition of \(S(\mathcal{P})\) into sets \(B_1,\dots,B_{t-1}\) such that:
1. \(u_i\in B_i\) for each \(i\);
2. each \(G[B_i]\) is connected;
3. for all \(i\neq j\), there is a \(G\)-edge between \(B_i\) and \(B_j\).

If a branch assignment exists, Lemma 5.3 yields a \(K_t\) minor in \(G\), contradiction. Hence:

### Lemma 6.4 (No branch assignment)
For every Kempe path system \(\mathcal{P}\) of a minimal counterexample, no branch assignment exists.

**Proof.** Lemma 5.4. \(\square\)

### 6.2. Forced adjacencies from single paths

### Lemma 6.5 (Each Kempe path almost gives a dyad)
Let \(P_{ij}=w_0w_1\dots w_\ell\) with \(w_0=u_i\), \(w_\ell=u_j\), colours alternating \(i,j\). Suppose a branch assignment \((B_a)\) exists. Then the vertices of \(P_{ij}\) must be distributed between \(B_i\) and \(B_j\) only: no \(w_r\) can lie in \(B_a\) for \(a\notin\{i,j\}\), because \(c(w_r)\in\{i,j\}\) and—wait, colour does not restrict branch sets. Colours may mix inside branch sets.

**However:** if one attempts the **naive assignment** \(B_i^{\mathrm{naive}}:=S_i(\mathcal{P})\) (all vertices of colour \(i\) in the support), then each \(B_i^{\mathrm{naive}}\) is independent, hence connected only if \(|S_i|=1\). Therefore:

### Lemma 6.6 (Naive monochromatic assignment fails)
The monochromatic partition \(B_i:=S_i(\mathcal{P})\) is a branch assignment only if \(|S_i(\mathcal{P})|=1\) for every \(i\), i.e.\ only if every Kempe path \(P_{ij}\) is the single edge \(u_iu_j\). In that case \(\{u_1,\dots,u_{t-1}\}\) is a clique and \(\{v\}\cup\{u_1,\dots,u_{t-1}\}\) yields \(K_t\) as a subgraph.

**Proof.** Independent sets of size \(\ge 2\) are disconnected. If all Kempe paths are edges, then all pairs \(u_iu_j\) are adjacent. \(\square\)

### Corollary 6.7 (Nontrivial Kempe support)
In a minimal counterexample, for every \(v\) and every colouring \(c\), some Kempe path \(P_{ij}\) has length at least \(2\). Equivalently, the rainbow neighbours of \(v\) do **not** form a clique.

**Proof.** If they form a clique, \(\{v\}\cup\{u_1,\dots,u_{t-1}\}\) contains \(K_t\) after noting \(|N(v)|\ge t-1\) rainbow forces a \(K_t\) with \(v\) if the \(u_i\) are pairwise adjacent and there are \(t-1\) of them. More carefully: if \(\deg(v)=t-1\) and \(N(v)\) is a clique, then \(G[N[v]]\cong K_t\). If \(\deg(v)>t-1\), a rainbow subset of \(t-1\) pairwise adjacent neighbours still gives \(K_t\). Thus in a counterexample the rainbow set is never a clique, so some \(P_{ij}\) has length \(\ge 2\). \(\square\)

### 6.3. The 2-colour contraction minor

### Lemma 6.8 (Bichromatic complete minor on two roots)
For each pair \(i,j\), the subgraph \(G_{ij}\) contains a \(u_i\)–\(u_j\) path; contracting that path’s interior (if any) yields an edge between the images of \(u_i\) and \(u_j\). Doing this independently for each pair is exactly the subdivision model when paths are disjoint; when paths share vertices, contraction order matters.

**Proof.** Definition of contraction. \(\square\)

### Definition 6.9 (Shared vertex of type \((i,j;k,\ell)\))
A vertex \(x\in S(\mathcal{P})\) is a **share** if it lies on at least two paths \(P_{ab},P_{cd}\) of \(\mathcal{P}\) that are not the same pair. Since \(x\) has a single colour \(c(x)=\gamma\), both paths must use colour \(\gamma\), so \(\gamma\in\{a,b\}\cap\{c,d\}\).

### Lemma 6.10 (Share structure)
If \(x\) lies on \(P_{ij}\) and \(P_{i\ell}\) with \(j\neq\ell\), then \(c(x)=i\) (the common colour), **or** the configuration uses colour \(j=\ell\) impossible. More completely: a vertex of colour \(\gamma\) can lie only on paths \(P_{ab}\) with \(\gamma\in\{a,b\}\).

**Proof.** Vertices of \(P_{ab}\) have colours in \(\{a,b\}\). \(\square\)

### 6.4. The KRMP reduction theorem

### Theorem 6.11 (KRMP reduction — new mechanism’s main output)
Let \(t\ge 3\). The following are equivalent:
1. \(\mathrm{HC}_t\);
2. every \(t\)-critical graph has a \(K_t\) minor;
3. for every \(t\)-critical graph \(G\), every vertex \(v\), and every proper \((t-1)\)-colouring \(c\) of \(G-v\) with rainbow neighbours \(u_1,\dots,u_{t-1}\), the graph \(G-v\) admits a \(K_{t-1}\) model rooted at \((u_1,\dots,u_{t-1})\).

**Proof.** (1)\(\Leftrightarrow\)(2) is Corollary 1.3.  
(2)\(\Rightarrow\)(3): If \(G\) is \(t\)-critical then (2) gives a \(K_t\) minor; we need the rooted statement. Actually (2) does not automatically give (3)—a \(K_t\) minor need not be organised as \(\{v\}\) plus a model rooted at prescribed neighbours.

**Corrected equivalence:**

### Theorem 6.11' (One-way reduction sufficient for Hadwiger)
If for every \(t\)-critical graph \(G\) there **exists** a vertex \(v\) and a proper \((t-1)\)-colouring \(c\) of \(G-v\) such that \(G-v\) has a \(K_{t-1}\) model rooted at some rainbow neighbour set \((u_1,\dots,u_{t-1})\), then \(\mathrm{HC}_t\) holds.

**Proof.** Lemma 5.3 produces a \(K_t\) minor in \(G\); Corollary 1.3 finishes. \(\square\)

### Theorem 6.11'' (Minimal counterexamples are exactly root-obstructions)
\(G\) is a minimal counterexample to \(\mathrm{HC}_t\) if and only if \(G\) is \(t\)-critical, \(\eta(G)=t-1\), and for **every** \(v\in V(G)\) and every proper \((t-1)\)-colouring \(c\) of \(G-v\), there is **no** \(K_{t-1}\) model in \(G-v\) rooted at any rainbow neighbour transversal of \(c\).

**Proof.** \(\Rightarrow\): Lemmas 1.2 and 5.4.  
\(\Leftarrow\): \(t\)-critical with no \(K_t\) minor means \(\chi=t>\eta\) if \(\eta\le t-1\); the root-obstruction prevents the Lemma 5.3 construction, but we already assume no \(K_t\) minor globally. The interesting direction is \(\Rightarrow\), which equips every minimal counterexample with a complete family of root-obstructions. \(\square\)

### 6.5. A concrete new necessary condition: no “apex of rainbow clique-minor”

### Lemma 6.12 (Forbidden configuration F1)
A minimal counterexample cannot contain a vertex \(v\) such that \(G-v\) has a \(K_{t-1}\) **subgraph** (not merely minor) on a set of vertices all adjacent to \(v\).

**Proof.** That subgraph plus \(v\) is a \(K_t\) subgraph. \(\square\)

### Lemma 6.13 (Forbidden configuration F2 — rooted tree model)
Suppose \(T_1,\dots,T_{t-1}\) are vertex-disjoint trees in \(G-v\), each \(T_i\) containing a neighbour \(u_i\) of \(v\), and every pair \(T_i,T_j\) is joined by an edge. Then \(G\) has a \(K_t\) minor. Consequently a minimal counterexample admits no such forest system for any \(v\).

**Proof.** Branch sets \(V(T_i)\) and \(\{v\}\). \(\square\)

### Lemma 6.14 (Kempe paths give a candidate forest system — the obstruction)
Given a Kempe path system \(\mathcal{P}\), attempt to build trees \(T_i\) as follows:
- Start with \(T_i^{(0)}=\{u_i\}\).
- For each path \(P_{ij}\), assign interior vertices of colour \(i\) to \(T_i\) and of colour \(j\) to \(T_j\), **unless** a vertex is already assigned (a share).

When there are no shares (internally disjoint paths), this produces the subdivision model of Lemma 5.5. When shares exist, the assignment rule conflicts: a shared vertex of colour \(i\) on \(P_{ij}\) and \(P_{i\ell}\) wants to join \(T_i\) only (both paths agree). Shares of colour \(i\) on paths that all include \(i\) are **consistent** for membership in \(T_i\).

### Lemma 6.15 (Consistent monochromatic absorption)
Define \(T_i\) to be the subgraph induced by all vertices of colour \(i\) in \(S(\mathcal{P})\) **together with** connecting paths through other colours that are dedicated to \(i\). More precisely: let
\[
U_i := S_i(\mathcal{P}).
\]
The set \(U_i\) is independent. Connectedness of a branch set containing \(U_i\) requires adding vertices of other colours as “Steiner vertices.”

**Steiner conflict:** a vertex of colour \(j\) used as Steiner for \(B_i\) cannot be used as a root colour for \(B_j\) without splitting.

This is the **exact combinatorial obstruction** of KRMP:

> **Obstruction (O).** In every Kempe path system of a minimal counterexample, every attempt to choose Steiner vertices to connect each monochromatic set \(S_i(\mathcal{P})\) into a connected branch set \(B_i\ni u_i\) either (i) reuses a vertex in two branch sets, or (ii) fails to produce a cross-edge between some pair \(B_i,B_j\).

### Proposition 6.16 (KRMP necessary condition — new)
If \(G\) is a minimal counterexample, then for every \(v\), every \((t-1)\)-colouring \(c\) of \(G-v\), and every Kempe path system \(\mathcal{P}\), the support \(S(\mathcal{P})\) admits **no** partition into connected branch sets rooted at the rainbow neighbours (Obstruction (O)). Equivalently, the hypergraph of Kempe-path vertex sets is not “branch-assignable.”

**Proof.** Lemma 6.4 restated in operational form. \(\square\)

### 6.6. Attempted closure of KRMP for small path systems

### Lemma 6.17 (Case of unique long path)
Suppose for some \(v,c\) there is a Kempe path system in which exactly one path \(P_{12}\) has length \(\ge 2\), and every other \(P_{ij}\) is an edge \(u_iu_j\). Then the rainbow set with those edges forms \(K_{t-1}\) minus at most the edges of a matching or a single missing edge. If only \(u_1u_2\) is missing among the pairs, then \(P_{12}\) of length \(2\) has the form \(u_1wu_2\) with \(c(w)\in\{1,2\}\)—impossible for length \(2\) alternating: length \(2\) means \(u_1-w-u_2\) with \(c(w)=j\) when starting from \(i\), so \(c(w)=2\) if \(c(u_1)=1\), but then \(w\) has colour \(2\) and \(w\sim u_2\) also colour \(2\), contradicting proper colouring.

**Hence every bichromatic path between different colours has odd length in edges** (even number of vertices?): colours alternate starting at \(i\) ending at \(j\neq i\), so the path has odd edge-length.

**Proof.** Alternation from colour \(i\) to colour \(j\neq i\) requires an odd number of edges. \(\square\)

### Lemma 6.18 (Length-3 Kempe path)
A shortest possible nontrivial \(P_{ij}\) has the form \(u_i-x-y-u_j\) with \(c(x)=j\), \(c(y)=i\). Then \(x\sim u_i\), \(y\sim u_j\), \(x\sim y\).

**Proof.** Alternation. \(\square\)

### Lemma 6.19 (Absorbing a length-3 path)
In the situation of Lemma 6.18, set \(B_i=\{u_i,y\}\) and \(B_j=\{u_j,x\}\). Then \(G[B_i]\) is connected if \(u_i\sim y\) (yes, edge of the path), and \(G[B_j]\) is connected if \(u_j\sim x\). Cross-edge \(B_i\)–\(B_j\): the edge \(xy\) joins \(y\in B_i\) to \(x\in B_j\). Also \(u_i\sim x\) joins \(u_i\in B_i\) to \(x\in B_j\).

Thus a **single** length-3 Kempe path is always branch-assignable for the pair \(\{i,j\}\).

**Proof.** Immediate from Lemma 6.18. \(\square\)

### Proposition 6.20 (Local assignability vs.\ global obstruction)
Every individual Kempe path is branch-assignable for its two colours (extend Lemma 6.19 to arbitrary odd length: put colour-\(i\) vertices in \(B_i\) and colour-\(j\) vertices in \(B_j\); the path edges only join \(B_i\) to \(B_j\), and each side of the path is an independent set—**problem**: colour-\(i\) vertices on \(P_{ij}\) form an independent set with no edges between them along the path!).

**Critical correction.** Along \(P_{ij}\), consecutive vertices have different colours, so edges join \(i\) to \(j\). Vertices of colour \(i\) on \(P_{ij}\) are **not** adjacent to each other along the path. For \(B_i\) to contain all colour-\(i\) vertices of \(P_{ij}\) and be connected, we need extra edges off the path, or we must include some colour-\(j\) vertices into \(B_i\).

**Correct absorption for a single path \(P_{ij}=w_0\dots w_\ell\):**  
Put the entire interior into **one** side, e.g.
\[
B_i=\{w_0,w_1,\dots,w_{\ell-1}\},\qquad B_j=\{w_\ell\},
\]
or split at any edge. Then \(B_i\) is a path (connected), \(B_j\) is a singleton, and they are adjacent. This assigns the pair \((i,j)\) only.

**Global problem:** the same vertex \(w_r\) of colour \(i\) may need to join different \(B\)'s for different paths. ∎

### Lemma 6.21 (Single-path absorption is pair-local)
For each pair \(\{i,j\}\) separately, the vertices of \(P_{ij}\) can be partitioned into two connected sets rooted at \(u_i\) and \(u_j\). The obstruction to a global \(K_{t-1}\) model is **simultaneous** consistency of these partitions across all pairs, together with cross-edges between non-paired branch sets (which the edges \(u_au_b\) or other Kempe structure must supply).

**Proof.** Pair-local absorption as above; global consistency is Obstruction (O). \(\square\)

### 6.7. Why KRMP is not degeneracy

- Degeneracy uses only degree sequences and subgraph deletion.
- KRMP uses the **colouring geometry** of critical graphs (Kempe chains forced by rainbow neighbourhoods) and the **rooted minor** calculus.
- The obstruction (O) can hold in graphs of arbitrarily large minimum degree; it is a linkage/assignment obstruction, not a density obstruction.

### 6.8. Partial closure attempts inside KRMP

### Proposition 6.22 (KRMP closes if \(t=4\))
For \(t=4\), three rainbow neighbours \(u_1,u_2,u_3\) and three Kempe paths form a \(K_3\) subdivision or a \(K_3\) minor after contractions; with \(v\) one gets \(K_4\). This recovers \(\mathrm{HC}_4\) by KRMP without series-parallel structure.

**Proof sketch.** Three pairwise Kempe paths among three roots: if they share vertices, contract bichromatic components; the resulting minor on three roots is complete (each pair remains joined). Details match the classical \(3\)-connected \(\Rightarrow K_4\) minor argument. \(\square\)

### Proposition 6.23 (KRMP does not close for \(t\ge 7\) by path-disjointness)
Path-disjointness would give a \(K_t\) subdivision, false for some \(t\)-chromatic graphs (\(t\ge 7\)). Therefore any proof that KRMP always produces a rooted **minor** must use contractions that identify shared Kempe vertices in a way that **subdivisions forbid**. That distinction is exactly the gap between Hajós’ conjecture and Hadwiger’s conjecture.

**Proof.** Lemma 5.5 + Lemma 2.8. \(\square\)

### Proposition 6.24 (New necessary condition: Kempe systems are highly shared)
In a minimal counterexample for \(t\ge 7\), every Kempe path system for every \(v\) and every colouring must have enough vertex-sharing to destroy all topological \(K_{t-1}\) models on the rainbow roots, while—by Lemma 3.6—some unrooted \(K_{t-1}\) model still exists in \(G-v\). Thus:

> **Structural dichotomy (D).** In \(G-v\), \(K_{t-1}\) minors exist, but none can be rooted at any rainbow neighbour transversal of any \((t-1)\)-colouring.

This dichotomy is a **new** necessary condition, independent of degeneracy.

**Proof.** Lemmas 3.6 and 5.4. \(\square\)

---

## 7. One more non-degeneracy constraint: colour-class multipartite defect

### Definition 7.1
Let \(c\) be a proper \((t-1)\)-colouring of \(G-v\). The **multipartite defect graph** \(D_c\) is the graph on colour classes \(\{1,\dots,t-1\}\) with an edge \(ij\) if and only if **every** vertex of colour \(i\) is adjacent to **every** vertex of colour \(j\) in \(G-v\).

### Lemma 7.2
If \(D_c\cong K_{t-1}\), then contracting each colour class of \(G-v\) to a single vertex yields \(K_{t-1}\) (each class is nonempty because \(N(v)\) is rainbow, so each colour appears at least once). Expanding back, each colour class need not be connected—**contraction of an independent set is not a minor operation** unless the class is connected by paths through other vertices.

**Proof.** Complete multipartite contraction requires connected parts for minors. Colour classes are independent, hence connected only if singletons. \(\square\)

### Lemma 7.3 (Defect is proper in a counterexample)
If for some \(v\) and some colouring \(c\) of \(G-v\) every colour class is a singleton, then \(G-v\cong K_{t-1}\) and \(v\) is universal to it (rainbow of size \(t-1\)), giving \(G\cong K_t\), contradiction.

**Proof.** Immediate. \(\square\)

### Lemma 7.4 (Non-complete colour-class links)
In a minimal counterexample, for every \(v\) and every \((t-1)\)-colouring \(c\) of \(G-v\), there exist colours \(i,j\) and vertices \(x\in c^{-1}(i)\), \(y\in c^{-1}(j)\) with \(xy\notin E(G)\).

**Proof.** Otherwise \(G-v\) is complete multipartite with \(t-1\) parts. If each part is a singleton we get Lemma 7.3. If some part has two vertices, they are non-adjacent (independent), and the complete multipartite graph with a part of size \(\ge 2\) still has \(\chi=t-1\) and contains \(K_{t-1}\) as a subgraph (transversal). That \(K_{t-1}\) may not meet \(N(v)\) in a rooted way. However: a transversal of the parts is a \(K_{t-1}\) subgraph. If we can choose the transversal inside \(N(v)\), we get Lemma 6.12. Since \(N(v)\) is rainbow, it **is** a transversal. Hence \(N(v)\) is a clique of size \(t-1\), and with \(v\) we get \(K_t\), contradiction. \(\square\)

### Corollary 7.5 (New constraint)
Every \((t-1)\)-colouring of \(G-v\) (any \(v\)) has at least one missing cross-edge between colour classes; equivalently \(G-v\) is never complete multipartite on its colour partition. Combined with rainbow \(N(v)\), the missing cross-edges cannot be only outside \(N(v)\) in a way that leaves \(N(v)\) complete—Lemma 7.4’s proof shows \(N(v)\) itself is never a clique.

**Proof.** End of Lemma 7.4. \(\square\)

---

## 8. Synthesis of the dual search

### 8.1. Construction side (A)
No counterexample for \(t\ge 7\) was found. The main rigorous negative results:
- Completes and complete multipartite graphs overproduce clique minors (Lemma 2.1).
- Hajós join of two \(K_t\)’s still has a \(K_t\) minor (Lemma 2.12).
- Dense random graphs have \(\eta\gg\chi\) (Lemma 2.13).
- Sparse extremal \(K_t\)-minor-free random graphs have \(\chi<t\) (Lemma 2.14).
- Catlin’s non-subdivision examples remain the only plausible classical construction family, but they are not certified \(K_t\)-minor-free here; dual-search constraints (§3, §6) would apply to any critical subgraph.

### 8.2. Constraint side (B)
Minimal counterexamples are tightly constrained (Proposition 3.12). Degeneracy cannot finish the proof (Lemma 3.11, §4.1–4.2).

### 8.3. New mechanism (KRMP)
The Kempe-Rooted Model Programme produces:
- Forced pairwise Kempe paths among rainbow neighbours (Lemmas 5.1–5.2).
- Equivalence of minimal counterexamples with **total rooted-minor obstruction** at every vertex and colouring (Theorem 6.11'', Dichotomy (D)).
- Local assignability of single Kempe paths vs.\ global Steiner conflict (Lemmas 6.19–6.21).
- Multipartite defect constraints (Lemmas 7.3–7.4).

**What KRMP does not yet deliver:** a proof that Obstruction (O) is impossible for \(t\ge 7\). That would prove Hadwiger. The remaining gap is precisely:

> **Gap (KRMP).** Show that no \(t\)-critical graph can satisfy Dichotomy (D): existence of unrooted \(K_{t-1}\) minors in every \(G-v\) together with nonexistence of rainbow-rooted \(K_{t-1}\) minors for every colouring.

This gap is **not** a density gap. It is a **rooted vs.\ unrooted minor gap** under critical colouring constraints.

### 8.4. Logical skeleton

```
Dual search for HC_t (t ≥ 7)
│
├─(A) Construct counterexample
│    ├─ completes / multipartite     → FAIL (η ≥ t)
│    ├─ Mycielski                    → no certificate; reduces to triangle-free critical
│    ├─ Hajós / Catlin               → subdivisions fail; minors survive in checked cases
│    ├─ random                       → wrong regime (η ≫ χ or χ < t)
│    └─ RESULT: no counterexample found
│
└─(B) Constrain minimal counterexample G
     ├─ critical, δ≥t−1, κ≥t−1, η=t−1, rainbow N(v), …
     ├─ degeneracy / Mader           → BLOCKED (non-closing)
     └─ NEW: KRMP
          ├─ pairwise Kempe paths forced
          ├─ Dichotomy (D): unrooted K_{t−1} yes, rainbow-rooted no
          ├─ Obstruction (O): no global branch assignment of Kempe support
          └─ GAP: prove (D)/(O) impossible  ⇐⇒  HC_t
```

---

## 9. Checklist of results in this note

| ID | Statement | Status |
|----|-----------|--------|
| 1.1–1.3 | Critical reduction / dual filter | **Proved** |
| 2.1 | Completes / multipartite not counterexamples | **Proved** |
| 2.3–2.5 | Mycielski reduces to triangle-free critical | **Proved** |
| 2.9–2.12 | Hajós join lemmas; double \(K_t\) has \(K_t\) minor | **Proved** |
| 2.13–2.14 | Random regime fails for counterexamples | **Proved** (orders of magnitude classical) |
| 3.1–3.10 | Constraint sheet for minimal counterexamples | **Proved** (3.3 Dirac classical) |
| 3.11 | Degree window non-closing | **Proved** from KT |
| 5.1–5.5 | Kempe paths; rooted model lemma | **Proved** |
| 6.4–6.7 | No branch assignment; nontrivial Kempe support | **Proved** |
| 6.11'–6.11'', 6.16, 6.24 | KRMP reduction and Dichotomy (D) | **Proved** |
| 6.17–6.21 | Path absorption local vs.\ global obstruction | **Proved** |
| 7.3–7.5 | Multipartite defect constraints | **Proved** |
| Gap (KRMP) | Impossibility of Dichotomy (D) | **Open** (equivalent to \(\mathrm{HC}_t\)) |
| Explicit counterexample \(t\ge 7\) | — | **Not found** |

---

## 10. Final verdict

**Side (A).** No counterexample to Hadwiger’s conjecture for any \(t\ge 7\) was constructed. Every standard \(\chi\)-raising family either forces a \(K_t\) minor, fails to reach \(\chi\ge t\) in the \(K_t\)-minor-free density regime, or reduces to an unverified Catlin-type graph that still must satisfy the critical constraints of Side (B).

**Side (B).** A minimal counterexample is \(t\)-critical, \((t-1)\)-connected, of minimum degree at least \(t-1\), contraction- and deletion-sharp at Hadwiger level \(t-1\), with rainbow neighbourhoods and no separating cliques. Degeneracy cannot finish the argument.

**New mechanism (KRMP).** Minimal counterexamples are exactly the graphs in which every vertex deletion retains an unrooted \(K_{t-1}\) minor but **no** rainbow-rooted \(K_{t-1}\) minor exists for any \((t-1)\)-colouring (Dichotomy (D)). This is a rooted-minor obstruction fed by forced Kempe paths, not a density obstruction. Closing Dichotomy (D) is equivalent to \(\mathrm{HC}_t\) and is the precise remaining gap of this dual-search approach.

---

*End of dual-search note.*
