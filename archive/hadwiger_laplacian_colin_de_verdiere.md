# Hadwiger’s Conjecture via Laplacian partitions, electrical networks, matroids, and the Colin de Verdière invariant

**Assigned approach family.** Matroid / algebraic connectivity / Laplacian partition methods; electrical-network interpretations of minors; the Colin de Verdière graph invariant \(\mu(G)\).

**Conjecture (Hadwiger).** For every integer \(t\ge 1\), every finite simple graph with no \(K_t\) minor is \((t-1)\)-colourable.
Write \(\mathrm{HC}_t\) for the fixed-\(t\) statement, \(\eta(G)\) for the Hadwiger number (largest \(s\) such that \(G\) has a \(K_s\) minor), and \(\chi(G)\) for the chromatic number. Equivalently \(\chi(G)\le\eta(G)\) for all \(G\).

**Standing conventions.** Graphs are finite and undirected; simple unless multigraphs are explicitly allowed (Laplacian and electrical network arguments are unaffected by suppressing loops and by treating multi-edges as parallel unit resistors / multi-contributions to the adjacency matrix). A **\(K_t\) model** in \(G\) is a family of pairwise disjoint nonempty connected vertex-sets \(B_1,\dots,B_t\) (branch sets) such that for all \(i\neq j\) there is at least one \(G\)-edge between \(B_i\) and \(B_j\). Write \(L_G=D_G-A_G\) for the combinatorial Laplacian (\(D_G\) diagonal degree matrix, \(A_G\) adjacency). Eigenvalues of \(L_G\) are ordered \(0=\lambda_1(G)\le\lambda_2(G)\le\cdots\le\lambda_n(G)\); the **algebraic connectivity** is \(\alpha(G):=\lambda_2(G)\).

**Status of this route (executive summary).**
1. Laplacian / Fiedler partitions yield **inductive cut structure** and spectral analogues of Cheeger cuts, but the natural “spectral colouring” they produce is controlled by \(\lambda_2\) and \(\Delta\), **not** by \(\eta(G)\). They **do not** produce a homomorphism \(G\to K_{t-1}\) from the mere absence of a \(K_t\) minor.
2. Electrical-network quantities (effective resistance, energy of flows) give clean characterisations of connectivity and of **contraction-closed** edge sets, and they detect when pairs of vertices “behave like edges after contraction.” This is a useful language for **minor models**, but the known quantitative bounds recover only connectivity / sparse-cut information of the same strength as Cheeger-type inequalities—again short of \(\chi\le t-1\).
3. Graphic-matroid partition methods reorganise the cut space and can isolate **series–parallel** / **low-rank** structure, which proves \(\mathrm{HC}_t\) for \(t\le 4\) by classical structure (outerplanar / series–parallel). For \(t\ge 5\), treewidth is **unbounded** on \(K_t\)-minor-free graphs (planar grids), so \(\chi\le\mathrm{tw}+1\) yields no \(t\)-only bound; the matroid rank of the cut space likewise fails to force \((t-1)\)-colourability.
4. The Colin de Verdière invariant satisfies the **proved** inequalities \(\mu(H)\le\mu(G)\) whenever \(H\) is a minor of \(G\), and \(\mu(K_t)=t-1\). Hence always
   \[
   \eta(G)\le\mu(G)+1.
   \]
   Colin de Verdière’s conjecture \(\chi(G)\le\mu(G)+1\) is therefore **weaker than Hadwiger** (Hadwiger \(\Rightarrow\) CdV). Using \(\mu\) to prove Hadwiger requires a **separate** upper bound \(\mu(G)\le\eta(G)-1\) on \(K_t\)-minor-free graphs—i.e. \(\mu=\eta-1\)—which is **false** in general. The exact residual gap is isolated below as three named axioms; even assuming all three standard deep black boxes about \(\mu\), **Hadwiger does not close**.

---

## 0. Critical reduction (shared with other routes)

### Definition 0.1
\(G\) is **\(k\)-critical** if \(\chi(G)=k\) and \(\chi(H)<k\) for every proper subgraph \(H\).

### Lemma 0.2 (Minimal counterexamples are critical)
Let \(t\ge 2\). If \(\mathrm{HC}_t\) fails, take a counterexample \(G\) of minimum order, and among such, of fewest edges. Then \(\chi(G)=t\), \(G\) is \(t\)-critical, \(\delta(G)\ge t-1\), \(\kappa(G)\ge 2\), and every smaller-order \(K_t\)-minor-free graph is \((t-1)\)-colourable. No clique of order \(\le t-2\) is a separator of \(G\).

**Proof sketch (standard).** For \(v\in V(G)\), \(G-v\) is \(K_t\)-minor-free of smaller order, so \(\chi(G-v)\le t-1\), hence \(\chi(G)=t\). Edge-minimality forces \(\chi(G-e)=t-1\) for every edge. Criticality, \(\delta\ge t-1\), no cut-vertex, and the clique-separator lemma are the usual critical-graph arguments: a colouring of the blocks of a clique cut of size \(\le t-2\) can be aligned on the clique inside a palette of \(t-1\) colours. ∎

### Remark 0.3
Thus \(\mathrm{HC}_t\) \(\Leftrightarrow\) every \(t\)-critical graph has a \(K_t\) minor.

---

## 1. Laplacian, Rayleigh quotients, and algebraic connectivity

### Definition 1.1 (Laplacian quadratic form)
For \(x\in\mathbb{R}^{V(G)}\),
\[
x^\top L_G x = \sum_{uv\in E(G)}(x_u-x_v)^2.
\]
By the variational characterisation,
\[
\lambda_2(G)=\min\bigl\{\,x^\top L_G x : x\perp\mathbf{1},\ \|x\|_2=1\,\bigr\}.
\]

### Lemma 1.2 (Fiedler’s basic facts)
Let \(G\) be connected on \(n\ge 2\) vertices.
1. \(\lambda_2(G)>0\).
2. If \(H\) is obtained from \(G\) by adding edges (on the same vertex set), then \(\lambda_2(H)\ge\lambda_2(G)\).
3. If \(G'\) is a spanning subgraph of \(G\), then \(\lambda_2(G')\le\lambda_2(G)\).

**Proof.** (1) Kernel of \(L_G\) is the constants iff \(G\) is connected. (2)–(3) follow from the quadratic form: more edges enlarge the form, fewer edges shrink it, and the constraint \(x\perp\mathbf{1}\) is unchanged. ∎

### Lemma 1.3 (Edge-contraction does not increase algebraic connectivity in a controlled way — partial)
Let \(e=uv\in E(G)\) and let \(G/e\) be the multigraph obtained by contracting \(e\) (loops deleted for the simple Laplacian if desired; the form identity below is for the multigraph Laplacian). Identify \(V(G/e)\) with \(\bigl(V(G)\setminus\{u,v\}\bigr)\cup\{w\}\). For \(y\in\mathbb{R}^{V(G/e)}\) define the lift \(\tilde y\in\mathbb{R}^{V(G)}\) by \(\tilde y_u=\tilde y_v=y_w\) and \(\tilde y_x=y_x\) for \(x\notin\{u,v\}\). Then
\[
\tilde y^\top L_G\tilde y = y^\top L_{G/e} y.
\]
Consequently, if \(y\perp\mathbf{1}\) on \(G/e\) and \(\|y\|_2=1\), the lift \(\tilde y\) is orthogonal to \(\mathbf{1}\) on \(G\) only after projection: writing \(\tilde y^\perp:=\tilde y-\bigl(\frac{\mathbf{1}^\top\tilde y}{n}\bigr)\mathbf{1}\),
\[
\lambda_2(G)\le \frac{(\tilde y^\perp)^\top L_G\tilde y^\perp}{\|\tilde y^\perp\|_2^2}.
\]
In particular \(\lambda_2\) is **not** minor-monotone in either direction in a form that yields \(\lambda_2(G)\le f(\eta(G))\) sharp enough for colouring.

**Proof.** Every edge of \(G\) not incident to \(\{u,v\}\) contributes identically on both sides. Edges from \(\{u,v\}\) to a third vertex become edges from \(w\), and the terms \((y_w-y_x)^2\) match. The edge \(uv\) contributes \(0\) on the lift. The projection formula is the definition of the Rayleigh quotient on the orthogonal complement of constants. ∎

### Remark 1.4 (Why spectral monotonicity fails for Hadwiger)
Minor operations mix **deletion** (which can only decrease \(\lambda_2\)) and **contraction** (which can increase \(\lambda_2\): e.g. a long path has tiny \(\lambda_2\), while contracting it toward \(K_2\) increases \(\lambda_2\)). Hence \(\lambda_2\) is not a minor-monotone parameter. One cannot read “no \(K_t\) minor” as an upper bound on \(\lambda_2\), nor as a lower bound sufficient to force a large clique minor from spectral expansion alone without additional structural input.

### Lemma 1.5 (Spectral lower bound forces large complete minors only through edge-density)
If \(\lambda_2(G)\ge c>0\) and \(\Delta(G)\le\Delta\), then \(G\) has average degree controlled only through Cheeger (next section); the best complete-minor conclusions available from \(\lambda_2\) alone are of the same quality as those from **expansion + degeneracy**, which historically give \(\eta(G)=\Omega\bigl(\frac{n}{\mathrm{polylog}\,n}\bigr)\) for strong expanders, not a classification of \(K_t\)-minor-free graphs.

**Proof.** Standard: expanders of bounded degree have large Hadwiger number by results in the expansion/minor literature; the point for this route is that the **hypothesis** “no \(K_t\) minor” is compatible with \(\lambda_2\to 0\) (e.g. long grids, planar graphs with large diameter) **and** with \(\lambda_2\) bounded away from zero on some bounded-degree \(K_t\)-minor-free families only when \(t\) grows. There is no theorem of the form “\(\eta(G)<t\Rightarrow\lambda_2(G)\le f(t)\)” that is both true for a useful \(f\) and strong enough to colour. ∎

---

## 2. Fiedler partitions and the attempt to build a homomorphism to \(K_{t-1}\)

### Definition 2.1 (Fiedler vector and nodal partition)
Let \(G\) be connected, \(x\) a unit eigenvector for \(\lambda_2(G)\) (a **Fiedler vector**). Write
\[
V_+:=\{v:x_v>0\},\qquad V_-:=\{v:x_v<0\},\qquad V_0:=\{v:x_v=0\}.
\]
The **Fiedler cut** is the bipartition of \(V\setminus V_0\) into \(V_+,V_-\) (with \(V_0\) assigned by any fixed rule, e.g. to the side of smaller boundary).

### Lemma 2.2 (Fiedler’s nodal domain theorem — discrete form)
If \(G\) is connected and \(x\) is a Fiedler vector, then both \(G[V_+\cup V_0]\) and \(G[V_-\cup V_0]\) are connected (after deleting isolated parts of \(V_0\) as appropriate). More precisely: the subgraph induced by \(\{v:x_v\ge 0\}\) has at most one connected component that meets \(\{v:x_v>0\}\), and likewise for the nonpositive side.

**Proof (standard energy argument).** Suppose \(\{v:x_v>0\}\) meets two distinct components \(C_1,C_2\) of \(G[\{x\ge 0\}]\). Define \(y\) by \(y_v=x_v\) on \(C_1\), \(y_v=0\) elsewhere on \(\{x\ge 0\}\), and \(y_v=x_v\) on \(\{x<0\}\) (or the usual sign-flip construction of Fiedler / van der Holst). Then \(y\not\parallel x\), one checks \(y^\top L_G y\le x^\top L_G x\) while \(y\perp\mathbf{1}\) after centering, contradicting minimality of the Rayleigh quotient unless the cut edges force a contradiction. The classical references implement this by comparing \(\sum(x_u-x_v)^2\) across the cut; the inequality is strict unless there are no cross edges of mixed sign in the forbidden configuration. ∎

### Lemma 2.3 (Cut size vs \(\lambda_2\))
Let \(S\subset V(G)\), \(S\notin\{\emptyset,V\}\), and write \(\partial S\) for the set of edges with one end in \(S\). Then
\[
\frac{|\partial S|}{|S|\,|V\setminus S|}\cdot n \ge \lambda_2(G),
\]
and more tightly, for the characteristic vector \(1_S\) after centering,
\[
\lambda_2(G)\le \frac{n\,|\partial S|}{|S|\,|V\setminus S|}.
\]

**Proof.** Let \(z=1_S-\frac{|S|}{n}\mathbf{1}\). Then \(z\perp\mathbf{1}\) and
\[
z^\top L_G z = \sum_{uv\in E}(z_u-z_v)^2 = |\partial S|,
\]
while \(\|z\|_2^2 = |S|\,|V\setminus S|/n\). Rayleigh gives the claim. ∎

### Definition 2.4 (Cheeger constant)
\[
h(G):=\min_{\emptyset\neq S\subset V,\ |S|\le n/2}\frac{|\partial S|}{|S|}.
\]

### Lemma 2.5 (Cheeger inequalities)
\[
\frac{\lambda_2(G)}{2}\le h(G)\le\sqrt{2\Delta(G)\,\lambda_2(G)}.
\]

**Proof.** Standard. Lower bound: for any \(S\) with \(|S|\le n/2\), Lemma 2.3 gives \(\lambda_2\le n|\partial S|/(|S||V\setminus S|)\le 2|\partial S|/|S|\), so \(\lambda_2/2\le h\). Upper bound: take a Fiedler vector, sweep a threshold cut \(S_t=\{v:x_v\ge t\}\), and optimise; the usual co-area / Cauchy–Schwarz argument produces a cut with \(\frac{|\partial S|}{|S|}\le\sqrt{2\Delta\lambda_2}\). ∎

### Proposition 2.6 (What Fiedler partitions give for colouring — positive but weak)
Suppose one recursively bipartitions \(G\) by Fiedler cuts, producing a binary tree of depth \(d\) whose leaves induce subgraphs of maximum degree \(\le t-2\) or of chromatic number \(\le t-1\). Then \(\chi(G)\le 2^d\cdot(t-1)\) in the crudest product bound—**not** \(\chi\le t-1\).

**Proof.** Each cut decomposes colouring into colouring the two sides plus identifying colours across a bipartite cut interface. Without a bound on the cut’s **interaction pattern** (the bipartite graph of cross edges), one cannot merge palettes; the safe bound multiplies. ∎

### Attempted strategy 2.7 (Algebraic partition \(\Rightarrow\) homomorphism to \(K_{t-1}\))
**Hope.** If \(G\) has no \(K_t\) minor, then some eigenmap
\[
\Phi:V(G)\to\mathbb{R}^{t-2},\qquad v\mapsto\bigl(x^{(2)}_v,\dots,x^{(t-1)}_v\bigr)
\]
(using the first \(t-2\) nontrivial Laplacian eigenvectors), after a suitable quantisation / clustering of \(\Phi(V)\), yields a proper colouring with \(t-1\) colours, or a homomorphism to a \((t-1)\)-colourable template.

**Lemma 2.8 (Spectral embedding does not force \(K_{t-1}\) colouring)**
There is no function \(c\) of the multiset \(\{\lambda_2,\dots,\lambda_{t-1}\}\) alone such that every graph with no \(K_t\) minor admits a proper colouring from a \(c\)-quantisation of \(\Phi\). In particular, the map \(\Phi\) may send adjacent vertices arbitrarily close (small \(|\Phi(u)-\Phi(v)|\)) while nonadjacent vertices are far, so threshold colouring of \(\Phi\) need not be proper, and the number of clusters needed can exceed \(t-1\).

**Proof.** Take a \(K_t\)-minor-free graph that is not \((t-1)\)-colourable—**if** a Hadwiger counterexample exists, its spectral embedding cannot yield a \((t-1)\)-colouring. Unconditionally (without assuming a counterexample): already for \(t=5\), \(K_{3,3}\) is \(K_5\)-minor-free (Wagner), \(\chi=2\), while planar triangulations with large diameter have \(\lambda_2=O(1/n)\) and spectral embeddings that fold geometrically; the number of \(\varepsilon\)-clusters of \(\Phi(V)\) for \(\varepsilon\) small enough to separate edges grows with \(n\), not bounded by \(4\). The obstruction is structural: \(\Phi\) is a **Lipschitz** map for the resistance / edge metric only in a weak average sense (\(\sum_{uv\in E}\|\Phi(u)-\Phi(v)\|^2=\sum_{i=2}^{t-1}\lambda_i\)), not a discrete homomorphism. ∎

### Lemma 2.9 (Exact obstruction for the “homomorphism from Laplacian partition” program)
Let \(\mathcal{P}_{t}\) be the class of \(K_t\)-minor-free graphs. Suppose there existed a rule that, to each \(G\in\mathcal{P}_t\), assigns a partition \(V=V_1\cup\cdots\cup V_{t-1}\) from Laplacian data (eigenvectors / nodal domains of \(L_G\) or of a Schrödinger operator \(L_G+W\)) such that each \(G[V_i]\) is empty of edges. Then \(\mathrm{HC}_t\) would hold. Conversely, any proof of \(\mathrm{HC}_t\) yields some (not necessarily spectral) such partition. **Gap:** no proof is known that nodal domains of the first \(O(1)\) eigenfunctions of \(L_G\) (or \(L_G+W\)) are independent sets when \(G\in\mathcal{P}_t\), and for \(t\ge 5\) this is false for the plain Laplacian: a single Fiedler vector has **two** positive/negative nodal regions, not \(t-1\) independent sets; higher eigenfunctions can have many nodal domains (Courant’s theorem gives an upper bound of \(k\) nodal domains for the \(k\)-th eigenfunction on manifolds; the discrete analogue is weaker and in any case bounds domains from above, not the chromatic number from above by \(t-1\)).

**Proof.** The forward direction is the definition of colouring. Courant-type bounds limit the **number of nodal domains of one eigenfunction**, which does not colour \(G\): colouring needs a partition into independent sets, whereas a nodal domain is only a sign region and may contain many edges (edges within \(\{x>0\}\) are allowed so long as endpoints have positive values). The quadratic form penalises value differences, not the existence of edges inside a sign class. ∎

### Corollary 2.10 (Laplacian partition gap, precise)
The program “no \(K_t\) minor \(\Rightarrow\) Laplacian eigenmap \(\Rightarrow\) homomorphism to \(K_{t-1}\)” fails at the step
\[
\text{eigenmap \(\Phi:V\to\mathbb{R}^{r}\)} \;\Longrightarrow\; \text{proper colouring with \(t-1\) colours},
\]
for every fixed \(r=r(t)\). The missing ingredient is a **minor-closed discrete monotonicity** of a spectral colouring number, which the Laplacian does not provide (Remark 1.4).

---

## 3. Electrical networks and minors

### Definition 3.1 (Resistive network)
Assign each edge of \(G\) resistance \(1\) (unit resistors). For \(a,b\in V(G)\), the **effective resistance** \(R_{\mathrm{eff}}(a,b)\) is the voltage difference \(v_a-v_b\) when a unit current is injected at \(a\) and extracted at \(b\), where \(v\) solves the Laplacian equation
\[
L_G v = \mathbf{e}_a-\mathbf{e}_b
\]
on the orthogonal complement of \(\mathbf{1}\) (solution unique up to constants; fix \(v_b=0\)). Equivalently,
\[
R_{\mathrm{eff}}(a,b)=(\mathbf{e}_a-\mathbf{e}_b)^\top L_G^{+}(\mathbf{e}_a-\mathbf{e}_b),
\]
with \(L_G^{+}\) the Moore–Penrose pseudoinverse.

### Lemma 3.2 (Rayleigh monotonicity)
If \(G'\) is obtained from \(G\) by adding an edge or decreasing a resistance, then \(R_{\mathrm{eff}}^{G'}(a,b)\le R_{\mathrm{eff}}^{G}(a,b)\) for all \(a,b\). Deleting an edge or increasing a resistance weakly increases all effective resistances.

**Proof.** Thomson’s principle: \(R_{\mathrm{eff}}(a,b)\) is the minimum energy \(\sum_e i_e^2 r_e\) over unit \(a\)–\(b\) flows. Enlarging the feasible set or decreasing \(r_e\) decreases the minimum. ∎

### Lemma 3.3 (Foster’s theorem)
\[
\sum_{uv\in E(G)} R_{\mathrm{eff}}(u,v) = n-c(G),
\]
where \(c(G)\) is the number of connected components.

**Proof.** \(\operatorname{tr}(L_G L_G^{+})=n-c(G)\), and the diagonal of the projection onto \(\mathbf{1}^\perp\) paired with the edge incidence gives Foster’s identity. ∎

### Lemma 3.4 (Resistance metric and cuts)
For any \(a,b\),
\[
R_{\mathrm{eff}}(a,b)=\min\bigl\{\,\|f\|_2^2 : f\text{ is a unit \(a\)–\(b\) flow on edges}\,\bigr\}
\]
(Thomson). Consequently, if \(\kappa_G(a,b)\ge k\) (local edge-connectivity), then \(R_{\mathrm{eff}}(a,b)\le 1/k\) by sending \(1/k\) along \(k\) edge-disjoint paths of length \(\ge 1\) in the crudest bound—more carefully, \(R_{\mathrm{eff}}(a,b)\le \mathrm{dist}(a,b)/\kappa_G(a,b)\) is false in general, but
\[
R_{\mathrm{eff}}(a,b)\le \min\bigl\{|E(P)|:P\text{ an \(a\)–\(b\) path}\bigr\}
\]
and by parallel law \(R_{\mathrm{eff}}(a,b)\le 1/\kappa_G(a,b)\) when there are \(\kappa_G(a,b)\) edge-disjoint paths **of length 1** (i.e. \(\kappa\) parallel edges); for general paths the energy depends on lengths.

**Proof.** Immediate from Thomson and the parallel/series laws. ∎

### Definition 3.5 (Electrical contraction interpretation of an edge)
Contracting \(uv\) is electrically the operation of setting \(R_{uv}=0\) (gluing equipotential vertices). A **branch set** \(B_i\) of a minor model is an equipotential cluster after a set of contractions (zero-resistance edges spanning \(B_i\)).

### Lemma 3.6 (Minor models as resistance collapses)
\(G\) has a \(K_t\) minor if and only if there exist pairwise disjoint nonempty \(B_1,\dots,B_t\subseteq V(G)\) such that:
1. for each \(i\), \(R_{\mathrm{eff}}^{G[B_i]}(x,y)<\infty\) for all \(x,y\in B_i\) (i.e. \(G[B_i]\) is connected—equivalently, after contracting a spanning tree of each \(B_i\) to a supervertex \(b_i\), one has \(R_{\mathrm{eff}}=0\) inside each supervertex);
2. for all \(i\neq j\), there is a positive-conductance edge between \(B_i\) and \(B_j\) in \(G\).

This is exactly the classical model definition rewritten in electrical language; **no new information**.

**Proof.** Connectivity of \(G[B_i]\) \(\Leftrightarrow\) finite effective resistance between any pair in \(B_i\) on the induced network. ∎

### Proposition 3.7 (Energy tests do not yield chromatic bounds)
Suppose one tries to certify \(\chi(G)\ge t\) electrically, e.g. by finding \(t\) vertices \(v_1,\dots,v_t\) with pairwise small \(R_{\mathrm{eff}}(v_i,v_j)\) and “independent” current supports. Small pairwise resistances mean the vertices are well-connected, which is compatible with **bipartite** graphs (two hubs joined by many paths). Thus low resistance does **not** force large cliques or large chromatic number.

**Proof.** In \(K_{n,n}\), \(R_{\mathrm{eff}}\) between any two vertices on opposite sides is \(O(1/n)\), \(\chi=2\), and \(\eta(K_{n,n})=\Theta(n)\) (large Hadwiger number, small chromatic number). Electrical connectivity tracks \(\eta\) more than \(\chi\), and even for \(\eta\) the constant-factor detection of clique minors from resistance matrices is not known to improve on combinatorial minor algorithms. ∎

### Lemma 3.8 (Effective-resistance diameter and planarity-type classes)
If \(G\) is planar, resistances and circle packings interact (e.g. via discrete uniformization), recovering \(\chi\le 4\) only by invoking the Four Colour Theorem or an equivalent—not by a pure resistance computation.

**Proof.** Observation: all purely electrical identities (Foster, Rayleigh, Thomson) hold for nonplanar graphs equally, so they cannot by themselves detect planarity or bound \(\chi\) by \(4\). ∎

### Corollary 3.9 (Electrical-network gap, precise)
Electrical networks **faithfully encode** connectivity and contraction, hence encode the existence of \(K_t\) models (Lemma 3.6). They **do not** encode colouring. The gap for Hadwiger is identical to the combinatorial gap: one must still prove that high chromatic number produces a \(K_t\) model. Resistance supplies no new homomorphic image \(G\to K_{t-1}\).

---

## 4. Matroid methods (graphic matroid, cut space, algebraic connectivity of the matroid)

### Definition 4.1 (Graphic matroid)
Let \(M(G)\) be the cycle matroid of \(G\): ground set \(E(G)\), independent sets = forests. Rank \(r(M(G))=n-c(G)\). The dual \(M^*(G)\) is the bond matroid (cocircuits = bonds = minimal cuts).

### Definition 4.2 (Algebraic connectivity of a weighted graph as a matroidal Rayleigh measure)
Given positive edge weights \(w_e\), the weighted Laplacian \(L_w\) has
\[
\lambda_2(L_w)=\min_{x\perp\mathbf{1},\ \|x\|_2=1}\sum_{e=uv}w_e(x_u-x_v)^2.
\]
This is the first nonzero eigenvalue of a measure on the cut space.

### Lemma 4.3 (Cut-space dimension)
The cycle space over \(\mathbb{R}\) has dimension \(m-n+c\), the cut space dimension \(n-c\). A partition of \(V\) into \(k\) labelled blocks that are each connected contributes a cut of rank at most \(k-1\) in the cut space after contracting blocks.

**Proof.** Standard linear algebra of the incidence matrix. ∎

### Lemma 4.4 (Series–parallel / rank-2 case proves \(\mathrm{HC}_3\) and \(\mathrm{HC}_4\) structure fragments)
1. If \(M(G)\) is a direct sum of matroids of rank \(\le 1\), then \(G\) is a forest, \(\chi\le 2\), \(\eta\le 2\).
2. Graphs of treewidth \(\le 2\) are series–parallel, \(K_4\)-minor-free, and \(3\)-colourable. This is \(\mathrm{HC}_4\) restricted to treewidth \(\le 2\).

**Proof.** (1) immediate. (2) series–parallel graphs are \(2\)-degenerate after \(K_1,K_2\) base, or induct on parallel/series reductions: each reduction preserves \(3\)-colourability. ∎

### Proposition 4.5 (Matroid partition does not bound \(\chi\) by \(\eta\))
There is no theorem of the form “if \(G\) has no \(K_t\) minor, then \(M(G)\) is a direct sum / parallel connection of matroids each of rank \(\le f(t)\) with \(f(t)\)-colourable bases” that is both true and strong enough to give \(\chi\le t-1\) for all \(t\).

### Lemma 4.6 (Treewidth vs Hadwiger — one side only)
If \(G\succcurlyeq K_t\), then \(\mathrm{tw}(G)\ge t-1\). Equivalently \(\eta(G)\le\mathrm{tw}(G)+1\).

**Proof.** A \(K_t\) model yields a bramble of order \(t\) (the branch sets, completed by standard bramble arguments), hence bramble number \(\ge t\), and \(\mathrm{tw}\ge t-1\) by the treewidth–bramble duality theorem. Alternatively: every chordal supergraph of \(G\) still has a \(K_t\) minor, hence contains a clique of size \(\ge t\) only after triangulation pressure—more elementarily, \(K_t\) itself has treewidth \(t-1\), and treewidth is minor-monotone. ∎

### Lemma 4.7 (Excluded **clique** minor does **not** bound treewidth)
For every \(t\ge 5\) and every \(W\), there exists a \(K_t\)-minor-free graph with \(\mathrm{tw}(G)>W\).

**Proof.** The \(n\times n\) grid is planar, hence \(K_5\)-minor-free (Wagner), and has treewidth \(n\). For \(t>5\), the same grids remain \(K_t\)-minor-free. ∎

### Remark 4.7b (Contrast: excluded **planar** minor)
Robertson–Seymour: for each fixed **planar** graph \(H\), the \(H\)-minor-free graphs have treewidth bounded by some \(w(H)\). Since \(K_t\) is nonplanar for \(t\ge 5\), this theorem does **not** apply to \(\mathrm{HC}_t\). (Large grids exclude no fixed \(K_t\) as \(t\to\infty\), but for each fixed \(t\ge 5\) they already show unbounded treewidth inside the \(K_t\)-minor-free class.)

### Lemma 4.8 (Treewidth colours, useless for global HC)
If \(\mathrm{tw}(G)\le w\), then \(\chi(G)\le w+1\).

**Proof.** A tree decomposition of width \(w\) yields a chordal completion with max clique \(\le w+1\); chordal graphs are perfect, so \(\chi\le w+1\). Alternatively: eliminate simplicial vertices of degree \(\le w\) and greedy-colour. ∎

### Corollary 4.9 (Matroid / width gap for Hadwiger)
Pure matroid rank of \(M(G)\) only recovers \(n-c(G)\), useless for colouring. Treewidth satisfies \(\eta\le\mathrm{tw}+1\) but \(\mathrm{tw}\) is **unbounded** on \(K_t\)-minor-free graphs for each \(t\ge 5\) (Lemma 4.7), so the bound \(\chi\le\mathrm{tw}+1\) does not give a function of \(t\) alone. The relevant deep substitute is the Graph Minors Structure Theorem (bounded-genus pieces + apices + vortices + clique-sums), which is a different approach family; within matroid language alone one only recovers series–parallel type cases (\(t\le 4\)).

### Remark 4.10 (Algebraic matroid connectivity)
One can define the **principal partition** of a matroid and deletion–contraction recurrences for Tutte–Whitney ranks. These organise edge sets into highly connected parts. For graphic matroids, high connectivity of \(M(G)\) is essentially high edge-connectivity of \(G\), which by Mader-type theorems produces large complete minors—again the **connectivity route**, not a new algebraic colouring.

---

## 5. The Colin de Verdière invariant \(\mu(G)\)

### Definition 5.1 (Colin de Verdière matrix set)
Let \(G\) be a simple graph on \(n\) vertices. Consider real symmetric \(n\times n\) matrices \(M=(M_{ij})\) such that:
1. \(M_{ij}<0\) whenever \(ij\in E(G)\);
2. \(M_{ij}=0\) whenever \(i\neq j\) and \(ij\notin E(G)\);
3. \(M\) has exactly one negative eigenvalue (of multiplicity one);
4. **Strong Arnold Property (SAP):** if \(X\) is real symmetric with \(X_{ij}=0\) whenever \(i=j\) or \(ij\in E(G)\), and \(MX=0\), then \(X=0\).

The **Colin de Verdière number** \(\mu(G)\) is the maximum corank \(\dim\ker M\) over all such matrices \(M\).

(Equivalent formulations use the Laplacian side: matrices of the form \(M=L_G+W\) with diagonal \(W\), negative off-diagonals on edges, etc., with the same SAP and inertia condition.)

### Lemma 5.2 (Elementary values)
1. \(\mu(G)=0\) iff \(G\) has no edges.
2. \(\mu(G)\le 1\) iff \(G\) is a disjoint union of paths.
3. \(\mu(K_n)=n-1\).

**Proof.** (1)–(2) are classical easy cases of the definition (optimize diagonal potentials on paths). (3) The matrix \(M=I-J\) (or a suitable affine transform of \(-A(K_n)\)) has corank \(n-1\) after adjusting the inertia/SAP normalisations; the complete graph realises the maximum possible corank \(n-1\). ∎

### Axiom CdV-Mon (Minor monotonicity — standard theorem, treated as named axiom if taken as black box)
If \(H\) is a minor of \(G\), then \(\mu(H)\le\mu(G)\).

**Status.** Theorem of Colin de Verdière / van der Holst–Lovász–Schrijver; proof uses Schur complements for contraction and restriction for deletion, preserving SAP by a dimension count. We treat the full verification as a black box and use only the statement.

### Corollary 5.3 (Hadwiger number vs \(\mu\))
For every graph \(G\),
\[
\eta(G)\le\mu(G)+1.
\]

**Proof.** If \(G\succcurlyeq K_t\), then \(\mu(G)\ge\mu(K_t)=t-1\) by Axiom CdV-Mon and Lemma 5.2(3). Thus \(t\le\mu(G)+1\). Maximise over \(t\). ∎

### Axiom CdV-Planar
\(\mu(G)\le 3\) if and only if \(G\) is planar. (More carefully: \(\mu\le 3\) for planar \(G\); the converse “\(\mu\le 3\Rightarrow\) planar” is also true.)

### Axiom CdV-Linkless
\(\mu(G)\le 4\) if and only if \(G\) is linklessly embeddable in \(\mathbb{R}^3\) (equivalently, no Petersen-family minor, Robertson–Seymour–Thomas).

### Axiom CdV-Colour (Colin de Verdière’s conjecture)
\[
\chi(G)\le\mu(G)+1\qquad\text{for every graph \(G\).}
\]

### Lemma 5.4 (Hadwiger \(\Rightarrow\) CdV-Colour)
If Hadwiger’s conjecture holds for all graphs, then Axiom CdV-Colour holds.

**Proof.** \(\chi(G)\le\eta(G)\le\mu(G)+1\) by Hadwiger and Corollary 5.3. ∎

### Lemma 5.5 (CdV-Colour does **not** imply Hadwiger)
Axiom CdV-Colour is strictly weaker than Hadwiger unless one also has \(\mu(G)\le\eta(G)-1\). But \(\mu(G)\ge\eta(G)-1\) always (Corollary 5.3), so \(\mu(G)\le\eta(G)-1\) means
\[
\mu(G)=\eta(G)-1.
\]
This equality is **false** for many graphs.

**Proof.** Planar graphs: \(\eta(G)\le 4\) (Wagner: no \(K_5\) minor), while \(\mu(G)\le 3\), so \(\mu=\eta-1\) holds at the top end for maximal examples with \(\eta=4\) and \(\mu=3\). For a counterexample to equality: any graph with \(\mu(G)>\eta(G)-1\) works. Known constructions (e.g. certain graphs with \(\mu=4\) that are \(K_5\)-minor-free—linklessly embeddable graphs may avoid \(K_6\) and even \(K_5\) in some cases while \(\mu=4\)) give \(\mu=4>\eta-1\) whenever \(\eta\le 4\). Explicit elementary example: take \(G=K_{3,3}\). Then \(G\) is nonplanar, so \(\mu(G)\ge 4\). Also \(G\succcurlyeq K_4\) (contract a matching edge of a perfect matching in a \(K_{3,3}\) drawing, or exhibit four branch sets), and \(G\not\succcurlyeq K_5\) (bipartite graphs have no \(K_5\) minor? **False**—bipartite graphs can have large clique minors by contraction). In fact \(\eta(K_{3,3})=4\), and \(\mu(K_{3,3})=4\), so \(\mu=\eta>\eta-1\). Thus \(\mu=\eta-1\) fails: \(4\neq 3\). ∎

### Corollary 5.6 (Quantitative separation)
Always \(\eta-1\le\mu\), and CdV-Colour says \(\chi\le\mu+1\). Hadwiger says \(\chi\le\eta\). The chain is
\[
\chi\ \le_{\text{? Hadwiger}}\ \eta\ \le_{\text{Cor.\ 5.3}}\ \mu+1\ \ge_{\text{? CdV}}\ \chi.
\]
CdV-Colour bounds \(\chi\) by something **at least** \(\eta\), possibly strictly larger. Whenever \(\mu+1>\eta\), even a proof of CdV-Colour leaves a gap of \(\mu+1-\eta\) colours above Hadwiger’s prediction.

### Proposition 5.7 (The \(\mu\)-route cannot close \(\mathrm{HC}_t\) by minor monotonicity alone)
Assume Axiom CdV-Mon and Lemma 5.2. The only upper bound on \(\mu\) forced by “\(G\) has no \(K_t\) minor” is **none beyond the trivial** \(\mu(G)\le n-1\): absence of a \(K_t\) minor forbids \(\mu\ge t-1\) **only if** every graph with \(\mu\ge t-1\) had a \(K_t\) minor, i.e. only if \(\mu\ge t-1\Rightarrow\eta\ge t\), which is the reverse of Corollary 5.3 and is equivalent to \(\mu\le\eta-1\), false by Lemma 5.5.

**Proof.** Logically: CdV-Mon + \(\mu(K_t)=t-1\) gives \(\eta\le\mu+1\), not \(\mu\le\eta-1\). ∎

### Proposition 5.8 (Even full CdV package fails to prove Hadwiger)
Assume **all** of: CdV-Mon, CdV-Planar, CdV-Linkless, CdV-Colour, and the known characterisation \(\mu\le 2\) \(\Leftrightarrow\) outerplanar. Then:
1. One recovers \(\chi\le 4\) for planar graphs (CdV-Planar + CdV-Colour), i.e. 4CT as a corollary of CdV-Colour—not an independent proof unless CdV-Colour is proved without 4CT.
2. One recovers \(\chi\le 5\) for linklessly embeddable graphs (\(\mu\le 4\)).
3. One does **not** recover \(\mathrm{HC}_t\) for general \(t\), because a \(K_t\)-minor-free graph may have \(\mu\) as large as the maximum \(\mu\) in that minor-closed class, which can exceed \(t-2\).

**Proof.** (1)–(2) immediate from the axioms. (3) From Proposition 5.7 and Lemma 5.5: the class \(\{G:\eta(G)<t\}\) is not contained in \(\{G:\mu(G)\le t-2\}\). ∎

### Lemma 5.9 (What \(\mu\le t-2\) would give)
If a graph \(G\) satisfies \(\mu(G)\le t-2\), then by CdV-Colour (conjectural) \(\chi(G)\le t-1\). Also, by Corollaries, \(G\) has no \(K_t\) minor. Thus the class \(\mu\le t-2\) is a **subclass** of the \(K_t\)-minor-free graphs on which Hadwiger is exactly CdV-Colour.

**Proof.** Immediate. ∎

### Remark 5.10 (Nullspace representation and homomorphism hopes)
A maximising CdV matrix \(M\) of corank \(\mu=\mu(G)\) yields a map
\[
\psi:V(G)\to\ker M\cong\mathbb{R}^{\mu},\qquad v\mapsto\text{\(v\)-coordinate projection of a basis of \(\ker M\)},
\]
more carefully: the kernel gives a multilinear representation where adjacent vertices satisfy linear inequalities from the off-diagonal signs (van der Holst–Lovász–Schrijver **nullspace representation**). This representation characterises planarity for \(\mu\le 3\) and is deep structure—but the image lies in \(\mathbb{R}^{\mu}\), and producing a colouring still requires a discrete partition of \(V\) into independent sets. The representation proves **structural** theorems (planarity, linkless embeddability) when combined with topological arguments; it does not by itself give \(\chi\le\eta\).

---

## 6. Hybrid strategy: spectral partition + critical connectivity + \(\mu\)

### Strategy 6.1
On a minimal counterexample \(G\) to \(\mathrm{HC}_t\) (\(t\)-critical, \(\delta\ge t-1\), no \(K_t\) minor):
1. Use \(\delta\ge t-1\) and Lemma 2.3 to bound \(\lambda_2\) from above if a sparse Fiedler cut exists, or deduce expansion if \(\lambda_2\) is large.
2. If \(G\) expands, invoke that expanders have large complete minors (Kostochka–Thomason density theory / combinatorial), contradiction to \(\eta<t\).
3. If \(G\) has a sparse cut \((S,V\setminus S)\), colour \(G[S]\) and \(G[V\setminus S]\) by induction and try to merge colours.

### Lemma 6.2 (Expansion branch — works in density form, not critically)
If \(d(G)\ge c\, t\sqrt{\log t}\) for a suitable absolute \(c\), then \(G\succcurlyeq K_t\) (Kostochka–Thomason). Consequently any \(K_t\)-minor-free graph has a vertex of degree \(O(t\sqrt{\log t})\), hence \(\chi=O(t\sqrt{\log t})\).

**Proof.** Named external extremal theorem; elementary proofs give weaker \(2^{O(t)}\) bounds. This is the degeneracy route’s best classical bound—not \(t-1\). ∎

### Lemma 6.3 (Sparse cut branch — colour merging fails)
Let \(G\) be \(t\)-critical, \(S\subset V\), \(0<|S|<n\), and \(B\) the bipartite graph of edges between \(S\) and \(V\setminus S\). Given proper \((t-1)\)-colourings of \(G[S]\) and \(G[V\setminus S]\) (available if both sides are smaller and \(K_t\)-minor-free—true for induced subgraphs of a minor-closed class), one can merge them into a colouring of \(G\) if and only if there is a permutation of colours on one side such that every edge of \(B\) joins differently coloured ends. This is equivalent to list-colouring / homomorphism constraints along \(B\), and fails in general when \(B\) contains a matching of size \(t-1\) joining two rainbow sets (exactly the critical situation of Lemma 0.2’s rainbow neighbourhoods).

**Proof.** If some cut edge is monochromatic under every colour identification, merging fails. In a \(t\)-critical graph, every vertex has a rainbow neighbourhood in any \((t-1)\)-colouring of \(G-v\); global cut-merging cannot evade this local obstruction without additional structure on \(B\). ∎

### Lemma 6.4 (Fiedler cut is not a clique cut)
A Fiedler cut \((V_+,V_-)\) need not have a complete bipartite join, nor a clique separator. Lemma 0.2’s alignment lemma therefore does not apply.

**Proof.** Already on a path, the Fiedler vector is a sine mode; the cut is a single edge, whose ends do not form a \((t-2)\)-clique separator of a large critical graph. ∎

### Corollary 6.5 (Hybrid gap)
The hybrid spectral-critical program reduces Hadwiger to: **either** a sparse Fiedler cut with mergeable colour boundaries, **or** enough expansion to force a \(K_t\) minor. The first subproblem is open and essentially equivalent to controlling separators in critical \(K_t\)-minor-free graphs; the second yields only \(O(t\sqrt{\log t})\) colouring from degree bounds.

---

## 7. Positive cases proved cleanly inside this approach family

### Theorem 7.1 (\(\mathrm{HC}_t\) for \(t\le 3\), spectral-free)
If \(G\) has no \(K_3\) minor, \(G\) is a forest, \(\chi\le 2\). If \(G\) has no \(K_2\) minor, \(G\) has no edges, \(\chi\le 1\).

**Proof.** Elementary. ∎

### Theorem 7.2 (\(\mathrm{HC}_4\) via \(\mu\le 2\) or via series–parallel)
Outerplanar graphs have \(\mu\le 2\) and are \(3\)-colourable. \(K_4\)-minor-free graphs are series–parallel (treewidth \(\le 2\)) and \(3\)-colourable (Lemma 4.4).

**Proof.** Structure of \(K_4\)-minor-free graphs: every block is series–parallel. Induct on series and parallel reductions. ∎

### Theorem 7.3 (\(\mathrm{HC}_5\) is the Four Colour Theorem)
\(K_5\)-minor-free graphs are exactly the graphs of treewidth \(\le 3\)? **No**—Wagner’s theorem: \(K_5\)-minor-free graphs are the graphs constructed from planar graphs and \(V_8\) by clique-sums. Colouring them with \(4\) colours requires 4CT for the planar pieces plus checking \(V_8\) and clique-sum alignment (clique-sums over \(K_r\) with \(r\le 3\) align \(4\)-colourings).

**Within the \(\mu\) language:** planar pieces have \(\mu\le 3\); CdV-Colour would give \(\chi\le 4\), but proving CdV-Colour for \(\mu\le 3\) is essentially 4CT again.

**Proof outline.** Wagner’s structural description + 4CT + clique-sum colouring lemma (same as Lemma 0.2 for cliques of size \(\le 3\) inside a \(4\)-palette). ∎

### Theorem 7.4 (Hadwiger numbers from \(\mu\) upper bounds — one direction only)
If \(\mu(G)\le k\), then \(\eta(G)\le k+1\). Under CdV-Colour, \(\chi(G)\le k+1\). Special cases \(k\le 3\) give colouring bounds for outerplanar / planar graphs **conditional** on CdV-Colour for those classes.

**Proof.** Corollary 5.3 and Axiom CdV-Colour. ∎

---

## 8. Concrete lemmas list (index) and proof status

| Label | Statement | Status |
|------|-----------|--------|
| 0.2 | Minimal HC counterexamples are \(t\)-critical, \(\delta\ge t-1\) | Proved |
| 1.2 | Basic \(\lambda_2\) facts | Proved |
| 1.3 | Contraction vs Laplacian form | Proved |
| 2.2 | Fiedler nodal connectivity | Standard; sketch proved |
| 2.3–2.5 | Cut Rayleigh + Cheeger | Proved |
| 2.8–2.9 | Spectral embedding does not colour | Proved (obstruction) |
| 3.2–3.4 | Rayleigh, Foster, Thomson | Proved |
| 3.6–3.9 | Electrical = combinatorial models; no \(\chi\) bound | Proved |
| 4.4 | Series–parallel \(\Rightarrow\mathrm{HC}_4\) fragment | Proved |
| 4.7 | \(\mathrm{tw}\) unbounded on \(K_t\)-minor-free, \(t\ge 5\) | Proved (grids) |
| 4.8 | \(\chi\le\mathrm{tw}+1\) | Proved |
| 5.2 | \(\mu(K_n)=n-1\), small cases | Standard |
| CdV-Mon | Minor monotonicity of \(\mu\) | **Named axiom** |
| 5.3 | \(\eta\le\mu+1\) | Proved from axiom |
| CdV-Colour | \(\chi\le\mu+1\) | **Open conjecture** |
| 5.5–5.8 | CdV does not imply HC | Proved |
| 6.2 | Kostochka–Thomason density | **Named external** |
| 6.3–6.5 | Cut merging obstruction | Proved |
| 7.1–7.3 | HC for \(t\le 5\) in this language | \(t\le 4\) elementary; \(t=5\) needs 4CT/Wagner |

---

## 9. Exact gap analysis (final)

### Gap G1 — Laplacian / Fiedler program
**Proved:** variational characterisation of cuts; nodal domain connectivity; Cheeger; critical-graph degree bounds.  
**Missing lemma (false in stated strength):**  
> If \(G\) has no \(K_t\) minor, then the first \(t-2\) Laplacian eigenvectors determine a partition of \(V(G)\) into \(t-1\) independent sets.  
**Why missing:** eigenmaps are continuous/averaged edge-Lipschitz, not combinatorial homomorphisms; nodal domains are not independent sets; \(\lambda_2\) is not minor-monotone.  
**Residual:** full Hadwiger for all \(t\ge 5\) (and for \(t=5\), reduction to 4CT is structural, not spectral).

### Gap G2 — Electrical networks
**Proved:** effective resistance encodes connectivity and contractions; minor models = resistance collapses of branch sets.  
**Missing lemma:** any implication from resistance matrices to \(\chi\le t-1\).  
**Why missing:** resistance tracks connectivity/\(\eta\) correlation only loosely and is orthogonal to odd-cycle / colouring phenomena (bipartite graphs can be electrically highly connected).  
**Residual:** same as combinatorial Hadwiger.

### Gap G3 — Matroid / width
**Proved:** graphic matroid basics; series–parallel case (\(\mathrm{HC}_4\) fragment); \(\chi\le\mathrm{tw}+1\); \(\eta\le\mathrm{tw}+1\); treewidth **unbounded** on each \(K_t\)-minor-free class for \(t\ge 5\) (grids).  
**Missing lemma:** any matroidal width parameter that is simultaneously (a) bounded by a function of \(\eta(G)\) alone and (b) strong enough that \(\chi\le\eta\). Treewidth satisfies (b) only as \(\chi\le\mathrm{tw}+1\), not (a). Branchwidth / rank-width have the same obstruction on grids.  
**Residual:** exit pure matroid language and use Graph Minors structure (or another family); matroids alone stop at \(t\le 4\).

### Gap G4 — Colin de Verdière route (sharp logical isolation)

Assume as axioms / black boxes:
- **CdV-Mon** (proved in literature; black-boxed here),
- \(\mu(K_t)=t-1\) (elementary),
- **CdV-Colour** \(\chi\le\mu+1\) (open),
- characterisations CdV-Planar, CdV-Linkless (deep but standard).

**Proved from these:** \(\eta\le\mu+1\); Hadwiger \(\Rightarrow\) CdV-Colour; colouring bounds for planar / linkless classes **conditional** on CdV-Colour.

**Missing for Hadwiger:** the reverse inequality \(\mu\le\eta-1\) (i.e. \(\mu=\eta-1\)), which is **false** (Lemma 5.5: e.g. \(\mu(K_{3,3})=4=\eta(K_{3,3})>\eta-1\)).

**Logical conclusion:**
\[
\boxed{\text{CdV package}+\text{all black boxes}\ \not\Rightarrow\ \text{Hadwiger.}}
\]
The \(\mu\)-route proves a **weaker** colouring conjecture and characterises important minor-closed classes; it cannot substitute for \(\chi\le\eta\) because \(\mu+1\) overshoots \(\eta\) on nonempty open sets of graphs.

### Gap G5 — Hybrid spectral-critical
**Proved:** dichotomy outline (expand vs sparse Fiedler cut); expansion branch \(\Rightarrow O(t\sqrt{\log t})\) colours; sparse cut branch blocked by colour-merging / rainbow neighbourhoods in critical graphs.  
**Missing:** a theorem that every \(t\)-critical \(K_t\)-minor-free graph has a separator on which \((t-1)\)-colourings align (false for \(t\ge 7\) if HC fails; open in general).  
**Residual:** the classical critical-separator problem for Hadwiger.

---

## 10. Verdict

| Route | Best unconditional colouring bound for \(K_t\)-minor-free \(G\) | Closes HC? |
|-------|---------------------------------------------------------------|------------|
| Laplacian eigen-partition | No bound better than general spectral graph theory; with degree bounds via Cheeger+degeneracy, same as average-degree bounds | **No** |
| Electrical networks | None for \(\chi\); reformulates \(\eta\) | **No** |
| Graphic matroid / treewidth | No \(t\)-only bound (\(t\ge 5\): unbounded tw on grids); \(t\le 4\) OK | **No** for \(t\ge 5\) |
| Colin de Verdière \(\mu\) | Conditional \(\chi\le\mu+1\); unconditional \(\eta\le\mu+1\) | **No** (wrong direction / weak inequality) |
| Hybrid Fiedler + critical | \(O(t\sqrt{\log t})\) via extremal minor density | **No** |

**Independent conclusion of this approach family.** Algebraic connectivity, electrical networks, and matroid cut-space methods are powerful **encoding languages** for connectivity and minors. They reorganise Hadwiger into spectral cut-merging and width-colouring problems but do not supply the missing inequality \(\chi\le\eta\). The Colin de Verdière invariant is the most structured algebraic minor-monotone parameter in the family; because it sits **above** \(\eta-1\) rather than equal to it, even a full proof of \(\chi\le\mu+1\) would leave Hadwiger open. The exact obstruction is the possible strict inequality \(\mu(G)>\eta(G)-1\).

---

## Appendix A. Minimal self-contained proof that \(\eta\le\mu+1\) needs only monotonicity

**Theorem A.1.** Assume only: (i) \(H\preccurlyeq G\Rightarrow\mu(H)\le\mu(G)\); (ii) \(\mu(K_t)=t-1\). Then \(\eta(G)\le\mu(G)+1\).

**Proof.** Let \(t=\eta(G)\). Then \(K_t\preccurlyeq G\), so \(t-1=\mu(K_t)\le\mu(G)\). ∎

**Theorem A.2.** The inequality \(\chi\le\mu+1\) does not follow from (i),(ii) alone.

**Proof.** (i),(ii) are also satisfied by the parameter \(\eta(G)-1\) in place of \(\mu\), and \(\chi\le\eta\) is Hadwiger—open. More formally: (i),(ii) hold for \(\mu\), but any proof of \(\chi\le\mu+1\) from (i),(ii) only would yield a proof of Hadwiger from the same for \(\eta-1\), which (i),(ii) instantiate—so no such formal deduction exists without using the **definition** of \(\mu\) beyond monotonicity and clique values. ∎

## Appendix B. Why a “Laplacian homomorphism” would need SAP-type nondegeneracy

The Strong Arnold Property in the definition of \(\mu\) is a transversality condition ensuring that \(\mu\) is minor-monotone. Ordinary Laplacian eigenvalues lack SAP control under contraction. Any attempt to replace \(\mu\) by “multiplicity of \(\lambda=0\) for \(L_G+W\)” without SAP loses minor monotonicity and cannot run the Corollary 5.3 argument. This is the precise sense in which \(\mu\) is the “correct” algebraic invariant for minors—and still the wrong strength for Hadwiger (Gap G4).

---

*End of writeup. No external search for claimed proofs of Hadwiger was used; black boxes are named (Kostochka–Thomason density, CdV monotonicity/planarity/linkless characterisations, CdV colouring conjecture, treewidth–bramble duality for Lemma 4.6).*
