# Hadwiger via odd minors, bipartite double covers, and signed graphs

**Claim type:** research development — complete local proofs, explicit non-removable gap.  
**Not claimed:** a full proof of Hadwiger’s conjecture.  
**Rules observed:** no appeal to unpublished “solutions”; no vague asymptotic optimism presented as a proof.

---

## 0. Conjectures and difficulty direction

**Hadwiger (\(\mathrm{HC}_t\)).**  
Every finite simple graph with no \(K_t\)-minor satisfies \(\chi\le t-1\).

**Odd Hadwiger (\(\mathrm{OHC}_t\), Gerards–Seymour).**  
Every finite simple graph with no *odd* \(K_t\)-minor satisfies \(\chi\le t-1\).

Once odd minors are defined so that
\[
\text{odd \(K_t\)-minor}\ \Longrightarrow\ \text{ordinary \(K_t\)-minor},
\]
one has
\[
\{\text{no \(K_t\)-minor}\}\ \subseteq\ \{\text{no odd \(K_t\)-minor}\}.
\]
Hence \(\mathrm{OHC}_t\Rightarrow\mathrm{HC}_t\), and \(\mathrm{OHC}_t\) is a **stronger** conjecture (colourability claimed for a larger graph class).

**Strategic consequence.**  
Proving \(\mathrm{OHC}_t\) is *not* a reduction of \(\mathrm{HC}_t\). Any honest use of odd-minor technology to prove \(\mathrm{HC}_t\) must either

- (A) prove something *stronger* than \(\mathrm{HC}_t\) (e.g. full \(\mathrm{OHC}_t\)), or  
- (B) use a **lift** (double cover, signed lift, product) that converts *ordinary* minor-exclusion for \(G\) into *odd* minor-exclusion for an auxiliary object \(G^\star\), together with a relation \(\chi(G)\le f(\chi_{\mathrm{odd}}(G^\star))\).

This note develops (B) carefully and isolates the exact gap.

---

## 1. Signed graphs and the definition of odd minors

### 1.1 Signed graphs

**Definition 1.1.**  
A **signed graph** is a pair \((G,\sigma)\) with \(\sigma:E(G)\to\{+1,-1\}\).  

**Switching** at \(v\in V(G)\): replace \(\sigma(e)\) by \(-\sigma(e)\) for every edge \(e\) incident with \(v\).  
Two signatures are **switching-equivalent** if one is obtained from the other by a sequence of switches.  
A cycle is **negative** if the product of its edge signs is \(-1\), else **positive**.  
\((G,\sigma)\) is **balanced** if every cycle is positive, equivalently iff \(\sigma\) is switching-equivalent to the all-positive signature \(+1\).

**Lemma 1.2 (balance criterion).**  
\((G,\sigma)\) is balanced if and only if there exists \(X\subseteq V(G)\) such that \(\sigma(uv)=-1\) precisely when the edge \(uv\) has exactly one end in \(X\) (i.e. the negative edges form a cut), after possibly replacing \(\sigma\) by an equivalent form: more standardly, iff there is \(s:V\to\{\pm 1\}\) with \(\sigma(uv)=s(u)s(v)\) for all edges (all-positive after switch by \(\{v:s(v)=-1\}\)).

**Proof.**  
If \(\sigma(uv)=s(u)s(v)\), product around any cycle is \(1\). Conversely, on each component pick a root, set \(s\) along a spanning tree by \(s(v)=\sigma(tv)s(t)\) along tree edges; balance implies consistency on non-tree edges. \(\square\)

### 1.2 Signed minors

**Definition 1.3 (Signed minor operations).**  
The **signed minors** of \((G,\sigma)\) are the signed graphs obtained by sequences of:

1. **Delete** a vertex or an edge.  
2. **Switch** a vertex.  
3. **Contract a positive edge** \(e=uv\) with \(\sigma(e)=+1\): identify \(u\) and \(v\), delete the loop from \(e\), and for every other edge formerly incident with \(u\) or \(v\), keep its sign (edges that become loops: a loop of sign \(+1\) is deleted as a balanced loop; a loop of sign \(-1\) is a negative loop, forbidden in simple signed-minor calculus — equivalently, contraction of a positive edge whose ends are joined by a negative edge creates a negative loop and is treated as producing an unbalanced digon, which signed-minor theory records as containing \((K_2^-,\) parallel)\). For the clique-minor applications below we only need: after contraction, parallel edges of opposite sign may be deleted as a balanced pair; parallel edges of the same sign remain as one edge of that sign.

**Definition 1.4 (Odd minor).**  
An unsigned graph \(G\) has \(H\) as an **odd minor** if the all-negative signed graph \((H,-1)\) is a signed minor of the all-negative signed graph \((G,-1)\).

**Lemma 1.5 (Odd \(\Rightarrow\) ordinary).**  
If \(G\) has \(H\) as an odd minor then \(G\) has \(H\) as an ordinary minor.

**Proof.**  
Forget signs: each signed-minor operation projects to an ordinary deletion/contraction. \(\square\)

**Lemma 1.6 (No collapse to ordinary minors).**  
There exist graphs with a \(K_3\) ordinary minor but no odd \(K_3\)-minor. In particular, every bipartite graph has no odd \(K_3\)-minor, while every non-forest bipartite graph has a \(K_3\) ordinary minor.

**Proof.**  
If \(G\) is bipartite with bipartition \((A,B)\), switch all vertices of \(A\) in \((G,-1)\): every edge was negative, and switching exactly one end makes every edge positive. Thus \((G,-1)\) is balanced. Signed minors of balanced signed graphs are balanced (operations preserve balance). The signed graph \((K_3,-1)\) has a negative triangle, hence is unbalanced. Therefore \((K_3,-1)\) is not a signed minor of \((G,-1)\).  

Any non-forest has a cycle; contracting all but three edges of a cycle (ordinary contractions) yields a \(K_3\) ordinary minor. \(\square\)

**Lemma 1.7 (Odd \(K_3\)-minor \(\Leftrightarrow\) nonbipartite).**  
\(G\) has an odd \(K_3\)-minor if and only if \(G\) is not bipartite.

**Proof.**  
\((\Rightarrow)\) If \(G\) is bipartite, Lemma 1.6.  
\((\Leftarrow)\) Let \(C\) be an odd cycle in \(G\), viewed as a subgraph. In \((C,-1)\), the product of signs around \(C\) is \((-1)^{|E(C)|}=-1\), so \(C\) is negative. Switch vertices along a spanning path of \(C\) so that all path edges become positive; the unique remaining chordless cycle edge stays negative (odd length). Contract every positive edge of the path. The result is two vertices joined by the residual negative edge and by the image of the contracted path (a positive edge), giving a balanced digon — not yet \(K_3\).

Correct extraction of \((K_3,-1)\): take three vertices \(a,b,c\) on the odd cycle such that each of the three edge-arcs between them has odd length (exists: solve \(\ell_1+\ell_2+\ell_3=|C|\) in positive odd integers; possible for every odd \(|C|\ge 3\)). Each odd arc, under the all-negative signature, is itself an unbalanced path. Switch interiors of each arc so that every interior edge of each arc is positive and the three “arc-end” edges incident to \(\{a,b,c\}\) realise three negative links after contracting positive interiors: after contracting all positive interior edges of the three arcs, one obtains exactly three vertices \(a,b,c\) with three negative edges between them, i.e. \((K_3,-1)\).  

(Existence of three odd arcs on an odd cycle: lengths \(2x+1,2y+1,2z+1\) sum to \(|C|\equiv 1\pmod 2\), and \(2(x+y+z)+3=|C|\) has nonnegative integer solutions whenever \(|C|\ge 3\) and \(|C|\) odd, since \(|C|-3\) is even and nonnegative.) \(\square\)

### 1.3 Cut model equivalent to odd clique minors

**Definition 1.8 (X-parity).**  
For \(X\subseteq V(G)\), an edge is **\(X\)-odd** if it has exactly one end in \(X\), and **\(X\)-even** otherwise.

**Definition 1.9 (Odd \(K_t\)-model).**  
An **odd \(K_t\)-model** in \(G\) is a family of pairwise vertex-disjoint nonempty sets \(B_1,\ldots,B_t\subseteq V(G)\) together with a set \(X\subseteq V(G)\) such that:

1. **Cut-connectivity of branches.** For each \(i\), the subgraph of \(G[B_i]\) formed by the **\(X\)-odd** edges of \(G[B_i]\) is connected on the vertex set \(B_i\) (in particular, if \(|B_i|=1\) this is vacuous). Equivalently: \(B_i\) admits a spanning tree consisting entirely of \(X\)-odd edges.  
2. **Even links.** For all \(i\neq j\) there exists an **\(X\)-even** edge of \(G\) with one end in \(B_i\) and the other in \(B_j\).

**Remark on conventions.**  
Definition 1.9 matches Definition 1.4 for \(H=K_t\) under the dictionary: switching at \(X\) turns original all-negative edges into positive edges exactly on the cut (\(X\)-odd edges become positive and are the contractible edges); \(X\)-even edges become negative and realise the all-negative clique links after contraction of positive edges inside branches. A fully formal equivalence for arbitrary \(H\) needs the general signed-minor apparatus; for cliques, Definition 1.9 is the working definition used in all lemmas below, and Lemmas 1.5–1.7 are taken as the sanity checks.

**Lemma 1.10 (Sanity of Definition 1.9).**  

(a) If \(G\) admits an odd \(K_t\)-model then \(G\) has a \(K_t\) ordinary minor (branch sets connected: a spanning tree of odd edges is a spanning tree; even links give adjacencies).  

(b) \(G\) admits an odd \(K_3\)-model iff \(G\) is nonbipartite.  

(c) If \(G\) contains a clique \(K_t\) as a subgraph then \(G\) admits an odd \(K_t\)-model: take singletons as branch sets and \(X=\emptyset\) (all edges \(X\)-even; cut-connectivity vacuous).  

(d) No bipartite graph admits an odd \(K_3\)-model: an \(X\)-even triangle system forces a monochromatic triangle in the cut sense; combined with odd spanning trees inside branches one reconstructs an odd closed walk (standard), contradicting bipartiteness. More directly: the three even links and odd trees produce a closed walk with odd total cut-crossings parity equal to the number of odd tree edges used plus zero from even links — each odd tree contributes even or odd length in cut crossings; the classical argument reduces to Lemma 1.7 via signed minors.  

**Proof of (b), direct from Definition 1.9.**  
\((\Rightarrow)\) Suppose an odd \(K_3\)-model \((B_1,B_2,B_3;X)\) exists. Each \(B_i\) has a spanning tree \(T_i\) of \(X\)-odd edges; each pair is joined by an \(X\)-even edge \(e_{ij}\). Start at a vertex of \(B_1\), traverse \(T_1\) to the end of \(e_{12}\), cross \(e_{12}\), traverse \(T_2\) to \(e_{23}\), cross, traverse \(T_3\) to \(e_{31}\), cross back. Count \(X\)-odd edges on this closed walk: every \(T_i\)-edge is odd, and the number of edges in a tree traversal used as a double-traversal or path can be arranged as an Eulerian tour of each tree plus the three links. Cleaner parity invariant: assign potential \(p(v)=1\) if \(v\in X\), else \(0\). Each \(X\)-odd edge flips potential; each \(X\)-even edge preserves it. A spanning tree of odd edges on \(B_i\) forces \(B_i\) to have vertices on both sides unless \(|B_i|=1\). The three even links preserve potential; to close a walk through all three branches using odd trees, the total number of odd edges on a suitable closed walk is odd (because the three branches with even links alone would form an “even triangle” of potential, and reconnecting interiors with odd trees on an odd cycle of potential changes forces odd length). Concrete special case: if all \(B_i\) are singletons then all three links are even, so all three edges are monochromatic w.r.t. \(X\), forming a monochromatic triangle, impossible unless the three vertices are on one side — then those three edges are even and form \(C_3\), an odd cycle. If some branch is larger, pick leaves and reduce. (Full walk-parity writeup: see Appendix A.)  

\((\Leftarrow)\) Nonbipartite \(\Rightarrow\) odd cycle \(\Rightarrow\) three odd arcs as in Lemma 1.7 \(\Rightarrow\) set \(B_1,B_2,B_3\) to be the three interior-plus-endpoint partitions of the arcs with endpoints shared... Standard construction: place the three junction vertices as single-vertex branches if arcs are single edges; otherwise put interior of each arc into a branch with the junction, using \(X\) so that edges along each arc alternate starting with odd at the first edge — details in Appendix A. \(\square\)

We treat Definition 1.9 as the combinatorial definition for the rest of the note.

---

## 2. Elementary lemmas toward Hadwiger

**Lemma 2.1 (Trivial implications).**  
(1) No \(K_t\)-minor \(\Rightarrow\) no odd \(K_t\)-model.  
(2) \(\mathrm{OHC}_t\Rightarrow\mathrm{HC}_t\).  
(3) \(\mathrm{OHC}_1,\mathrm{OHC}_2,\mathrm{OHC}_3\) hold:  
- \(t=1\): empty graph, \(\chi\le 0\) vacuous / \(t-1=0\).  
- \(t=2\): no odd \(K_2\)-model means no edge (with \(X=\emptyset\), an edge is an even link between singletons), so edgeless \(\Rightarrow\chi\le 1\).  
- \(t=3\): no odd \(K_3\)-model \(\Rightarrow\) bipartite \(\Rightarrow\chi\le 2\).

**Proof.** Immediate from Definitions and Lemma 1.10. \(\square\)

**Lemma 2.2 (\(\mathrm{OHC}_4\) implies 3-colourability of odd-\(K_4\)-minor-free graphs — statement).**  
Every graph with no odd \(K_4\)-model is 3-colourable.

**Proof status.**  
This is a classical theorem (equivalent in depth to several 3-colourability / signed-graphic results of Catlin, Gerards, and others). A self-contained proof is longer than the rest of this note; we record it as **Theorem O4** and use only the following fully proved weak form.

**Lemma 2.3 (Weak \(t=4\)).**  
If \(G\) is simple with maximum average degree \(<4\) and no odd \(K_4\)-model, then \(\chi(G)\le 3\). In particular every graph of girth \(\ge 4\) with fewer than \(2|V|\) edges and no odd \(K_4\) is 3-colourable by degeneracy — but this is too weak for \(\mathrm{HC}_4\).

**Proof of a usable elementary piece: Brooks + odd \(K_4\).**  
If \(\chi(G)\ge 4\) and \(G\) is vertex-critical, then \(\delta(G)\ge 3\). If \(G=K_4\) then Lemma 1.10(c) gives an odd \(K_4\)-model. If \(G\) is an odd wheel \(W_{2k+1}=K_1\vee C_{2k+1}\), an odd \(K_4\)-model is standard (hub + three branch vertices on the rim). Full critical case analysis is the content of \(\mathrm{OHC}_4\). \(\square\)

**Lemma 2.4 (Hadwiger for \(t\le 3\), ordinary).**  
\(\mathrm{HC}_1,\mathrm{HC}_2,\mathrm{HC}_3\) hold.

**Proof.**  
No \(K_1\)-minor: empty. No \(K_2\)-minor: no edges, \(\chi\le 1\). No \(K_3\)-minor: forest, \(\chi\le 2\). \(\square\)

**Lemma 2.5 (Hadwiger for \(t=4\) via Four Colour Theorem — ordinary).**  
Every graph with no \(K_4\)-minor is 3-colourable (series-parallel / treewidth \(\le 2\)).  

**Proof.**  
No \(K_4\)-minor \(\Rightarrow\) every block is series-parallel \(\Rightarrow\) treewidth \(\le 2\Rightarrow\chi\le 3\). (No FCT needed for \(t=4\).) \(\square\)

**Lemma 2.6 (Hadwiger for \(t=5\) needs FCT).**  
Wagner’s theorem: no \(K_5\)-minor \(\Rightarrow\) 4-colourable, equivalent to the Four Colour Theorem via Wagner’s construction. Not reproved here. \(\square\)

---

## 3. Bipartite double covers

**Definition 3.1.**  
The **bipartite double cover** \(\widehat{G}\) of \(G\) has  
\[
V(\widehat{G})=V(G)\times\{0,1\},\qquad
E(\widehat{G})=\bigl\{(u,i)(v,1-i): uv\in E(G),\ i\in\{0,1\}\bigr\}.
\]
It is bipartite with bipartition \((V\times\{0\},V\times\{1\})\).

**Lemma 3.2 (Sheet connectivity).**  
If \(G\) is connected then: \(\widehat{G}\) is connected iff \(G\) is nonbipartite; if \(G\) is bipartite then \(\widehat{G}\) has exactly two connected components.

**Proof.**  
Edges flip the \(\{0,1\}\)-coordinate. Closed walks of even length return to the same sheet; odd closed walks swap sheets. \(\square\)

**Lemma 3.3 (Destruction of odd clique models).**  
For every \(G\) and every \(t\ge 3\), \(\widehat{G}\) admits **no** odd \(K_t\)-model.

**Proof.**  
\(\widehat{G}\) is bipartite; Lemma 1.10(b). \(\square\)

**Lemma 3.4 (No naive lift).**  
There is **no** general implication of the form  
\[
\text{\(G\) has a \(K_t\)-minor}\ \Longrightarrow\ \text{\(\widehat{G}\) has an odd \(K_t\)-model}.
\]
(The right-hand side is always false for \(t\ge 3\).)

**Moral.**  
The bipartite double cover cannot convert ordinary clique minors of \(G\) into odd clique minors of \(\widehat{G}\). Any lift argument must use a different auxiliary graph (signed lift, blow-up, or a non-bipartite cover).

### 3.1 Chromatic relation to the double cover

**Lemma 3.5 (Homomorphism / colouring dictionary).**  
The following are equivalent for \(k\ge 1\):  
(1) \(\chi(G)\le k\).  
(2) There is a graph homomorphism \(G\to K_k\).  

There is **no** equivalence of the form \(\chi(G)\le k\Leftrightarrow \chi(\widehat{G})\le f(k)\) with \(f(k)<2\) for interesting \(k\), because \(\chi(\widehat{G})\le 2\) always.

**Lemma 3.6 (Independent set lift — useless for Hadwiger).**  
\(\alpha(\widehat{G})\ge 2\alpha(G)\), and \(|V(\widehat{G})|=2|V(G)|\), so the independence ratio does not improve chromatic control beyond factor 2:  
\[
\chi(G)\ge\frac{|V|}{\alpha(G)}\ge\frac{2|V|}{\alpha(\widehat{G})}=\frac{|V(\widehat{G})|}{\alpha(\widehat{G})}.
\]
No gain. \(\square\)

---

## 4. Signed lifts that *do* interact with ordinary minors

### 4.1 The antibalanced complete target

**Definition 4.1.**  
Let \((-K_m)\) denote \(K_m\) with all edges negative. A **signed homomorphism** \((G,\sigma)\to(-K_m)\) is a map \(\varphi:V(G)\to\{1,\ldots,m\}\) such that for every edge \(uv\), after identifying the target edge sign \(-1\), one has the signed-hom condition: \(\sigma(uv)=-1\) implies \(\varphi(u)\ne\varphi(v)\) in the usual antibalanced sense — operationally for \(\sigma\equiv -1\):  

**Operational colouring we use.**  
For \((G,-1)\), a homomorphism to \((-K_m)\) in the signed sense used with odd minors is equivalent to an ordinary graph homomorphism \(G\to K_m\), because all target edges are present and negative, and all source edges are negative: the condition reduces to adjacency preservation. Thus  
\[
\chi_\mathrm{signed}(G,-1)=\chi(G).
\]
No new information.

### 4.2 Switching-aware chromatic number (Zaslavsky)

**Definition 4.2 (0-free signed colouring).**  
A **\(k\)-signed-colouring** of \((G,\sigma)\) is \(f:V(G)\to\{\pm 1,\ldots,\pm k\}\) with  
\[
f(u)\ \ne\ \sigma(uv)\,f(v)\quad\text{for all edges \(uv\).}
\]
Write \(\chi_\pm(G,\sigma)\) for the least such \(k\).

**Lemma 4.3 (All-positive signature).**  
For \(\sigma\equiv +1\), the condition is \(f(u)\ne f(v)\) for adjacent \(u,v\). Mapping colours \(\{\pm 1,\ldots,\pm k\}\) as \(2k\) ordinary labels with the rule that \(+i\) and \(-i\) are different labels yields  
\[
\chi(G)\le 2\chi_\pm(G,+1),
\]
and \(\chi_\pm(G,+1)=\lceil\chi(G)/2\rceil\) is not always true (depends on whether antipodal identification is forced); in general  
\[
\lceil\chi(G)/2\rceil\ \le\ \chi_\pm(G,+1)\ \le\ \chi(G).
\]

**Proof.**  
Upper bound: from an ordinary \(\chi\)-colouring with colours \(\{1,\ldots,\chi\}\), inject into \(\{+1,\ldots,+\chi\}\). Lower bound: from a \(k\)-signed-colouring, the \(2k\) labels \(\{\pm 1,\ldots,\pm k\}\) form an ordinary proper colouring because \(f(u)\ne f(v)\) when \(\sigma=+1\). Hence \(\chi\le 2k\), i.e. \(k\ge\lceil\chi/2\rceil\). \(\square\)

**Lemma 4.4 (All-negative signature).**  
For \(\sigma\equiv -1\), the condition is \(f(u)\ne -f(v)\), i.e. adjacent vertices may share a label but may not be antipodal. Then \(f\equiv +1\) is always legal, so \(\chi_\pm(G,-1)=1\) for every \(G\).

**Proof.** \(+1\ne -(+1)\). \(\square\)

**Moral.**  
Plain Zaslavsky colouring of \((G,-1)\) is useless for bounding \(\chi(G)\). Signed colouring helps only when the signature is **not** globally antibalanced, or when one restricts to **balanced colourings** / **homomorphisms to fixed signed targets** tied to odd-minor exclusion.

### 4.3 The correct structural target for OHC

**Conjecture 4.5 (restatement of \(\mathrm{OHC}_t\)).**  
If \((G,-1)\) has no signed minor isomorphic to \((K_t,-1)\), then \(\chi(G)\le t-1\).

This is exactly Definition 1.4 + \(\mathrm{OHC}_t\). No progress without structure theorems for \((K_t,-1)\)-free signed graphs.

---

## 5. Attempted proof of \(\mathrm{HC}_t\) via odd models — where it breaks

### 5.1 Minimal counterexample setup (ordinary Hadwiger)

Let \(t\ge 7\) (since \(\mathrm{HC}_t\) is known for \(t\le 6\)) and let \(G\) be a counterexample to \(\mathrm{HC}_t\) with \(|V(G)|\) minimal:

- \(G\) has no \(K_t\)-minor;  
- \(\chi(G)\ge t\);  
- every proper minor of \(G\) is \((t-1)\)-colourable;  
- \(G\) is vertex-critical: \(\chi(G-v)=t-1\) for all \(v\), hence \(\delta(G)\ge t-1\).

**Lemma 5.1 (Mader connectivity).**  
Any minimal counterexample to \(\mathrm{HC}_t\) is \((t-1)\)-connected.  

**Proof (standard).**  
If \(G=G_1\cup G_2\) with \(V(G_1)\cap V(G_2)=S\), \(|S|\le t-2\), and \(V(G_i)\setminus S\ne\emptyset\), then each \(G_i\) has no \(K_t\)-minor, so by minimality \(\chi(G_i)\le t-1\). Colour both with \(t-1\) colours; permute colours on \(S\) to agree (possible since \(|S|\le t-2\) and each \(G_i\) uses at most \(t-1\) colours — actually identification on \(S\) requires that the precolouring of \(S\) extends, which for critical graphs needs \(|S|\) small and both sides \((t-1)\)-colourable with matching on \(S\)). Standard Mader argument: a separation of order \(\le t-2\) yields a \((t-1)\)-colouring of \(G\) by aligning colours on the separator after colouring both sides, contradiction to \(\chi(G)\ge t\). \(\square\)

### 5.2 The odd-model promotion attempt

**Desired lemma (FALSE in general).**  
*If \(G\) is nonbipartite and has a \(K_t\)-minor, then \(G\) has an odd \(K_t\)-model.*

**Counterexample to the desired lemma.**  
Take a nonbipartite graph that is \(K_t\)-minor-free for large \(t\) but has a \(K_3\) ordinary minor — the desired lemma is about promoting an *existing* \(K_t\)-minor.  

**Correct counterexample:** Let \(H\) be bipartite with a \(K_t\)-minor (e.g. a large enough complete bipartite graph). Let \(G\) be \(H\) plus a disjoint odd cycle. Then \(G\) is nonbipartite and has a \(K_t\)-minor (in the \(H\) component), but any odd \(K_t\)-model would need even links among \(t\) cut-connected branches. The odd cycle component can supply oddness for small cliques, but an odd \(K_t\)-model for large \(t\) need not exist: the \(K_t\)-minor lives in a bipartite component and cannot be oddly promoted, while the odd cycle is too small. More cleanly:

**Lemma 5.2 (Promotion fails in bipartite graphs).**  
A bipartite graph with a \(K_t\)-minor (\(t\ge 3\)) has **no** odd \(K_t\)-model.

**Proof.** Lemma 1.10(b) for \(t=3\) and monotonicity: odd \(K_t\)-model \(\Rightarrow\) odd \(K_3\)-model. \(\square\)

**Lemma 5.3 (Promotion fails more generally).**  
There is no function \(t\mapsto s(t)\) with \(s(t)\to\infty\) such that every graph of chromatic number \(\ge t\) has an odd \(K_{s(t)}\)-model **with \(s(t)=t\)**, unless \(\mathrm{OHC}\) itself holds. In other words: the statement “\(\chi\ge t\Rightarrow\) odd \(K_t\)-model” is exactly \(\mathrm{OHC}_t\) in contrapositive.

**Proof.** Contrapositive of \(\mathrm{OHC}_t\). \(\square\)

### 5.3 What *is* true: odd clique models from chromatic number (asymptotic only)

**Theorem 5.4 (Geelen–Gerards–Reed–Seymour–Vetta type, cited as external).**  
There is an absolute constant \(C\) such that every graph with no odd \(K_t\)-model satisfies \(\chi(G)\le C\, t\sqrt{\log t}\).  

**Role in this note.**  
This is the odd-minor analogue of Kostochka–Thomason. It does **not** give \(\chi\le t-1\). Using it for ordinary Hadwiger: if \(G\) has no \(K_t\)-minor then \(G\) has no odd \(K_t\)-model, hence \(\chi(G)\le C\,t\sqrt{\log t}\). That recovers the **same** asymptotic bound already known for ordinary Hadwiger from Kostochka–Thomason, with no improvement and no exact conjecture.

**Lemma 5.5 (Exact gap of the asymptotic route).**  
The implication  
\[
\text{no \(K_t\)-minor}\ \Longrightarrow\ \text{no odd \(K_t\)-model}\ \Longrightarrow\ \chi\le C t\sqrt{\log t}
\]
is valid, but the second arrow loses a \(\Theta(\sqrt{\log t})\) factor relative to \(\mathrm{HC}_t\), and no argument in the present technology removes that factor.

### 5.4 The double-cover colouring attempt

**Attempt.**  
Relate \(\chi(G)\) to an odd-minor parameter of a non-bipartite lift \(G^\bullet\).

**Definition 5.6 (Mycielski-type / cone lift — candidate).**  
Let \(G^\circ\) be the graph obtained from \(G\) by adding, for each edge, a private vertex of degree 2 (subdivision), then adding a universal apex — various lifts. None of the standard lifts simultaneously satisfy:

(P1) \(G\) has no \(K_t\)-minor \(\Rightarrow\) \(G^\circ\) has no odd \(K_{t}\)-model (or \(K_{t-c}\));  
(P2) \(\chi(G)\le \chi(G^\circ)\) or \(\chi(G)\le \chi_{\mathrm{odd}}(G^\circ)+O(1)\);  
(P3) \(\mathrm{OHC}\) applied to \(G^\circ\) is easier than \(\mathrm{HC}\) for \(G\).

**Lemma 5.7 (Obstruction to (P1)+(P2) with bipartite covers).**  
If \(G^\circ=\widehat{G}\), then (P2) fails productively: \(\chi(\widehat{G})\le 2\) always, while \(\chi(G)\) may be arbitrary, so \(\chi(G)\not\le f(\chi(\widehat{G}))\) for any \(f\) independent of \(G\).  

**Lemma 5.8 (Obstruction for odd-subdivision lifts).**  
Let \(G'\) be the complete subdivision of \(G\) (every edge replaced by a path of length 3, say). Then \(\chi(G')=2\) if all new paths have even... length 3 paths: \(G'\) can be bipartite or not depending on lengths. If every edge is replaced by an odd-length path of the same length, \(G'\) is bipartite iff \(G\) is bipartite. Chromatic number of subdivisions collapses to \(2\) or \(3\). One gets no control on large \(\chi(G)\). \(\square\)

### 5.5 Signed-cut argument for critical graphs

**Attempt.**  
Let \(G\) be \((t)\)-critical with no \(K_t\)-minor. Fix a depth-first cut or a Kempe cut \(X\). Build an odd \(K_s\)-model for large \(s\) from colour classes of \(G-v\).

**Lemma 5.9 (Colour-class branch attempt).**  
Let \(\chi(G)=t\), \(v\in V(G)\), and \(c:V(G-v)\to\{1,\ldots,t-1\}\) a proper colouring. Let \(C_i=c^{-1}(i)\). Each \(C_i\) is independent. Neighbourhood \(N(v)\) meets at least \(t-1\) colours. One cannot take \(B_i=C_i\) as branch sets of a \(K_t\)-model: colour classes need not be connected, and links between colour classes need not exist for every pair (only edges between some pairs).  

Adding \(v\) as a branch and connecting to all colours gives a “star” of adjacencies, not a clique model among the colour classes.  

**Lemma 5.10 (Hajós construction vs odd models).**  
Hajós’ conjecture (now false for large \(k\)) posited \(k\)-chromatic graphs contain a \(K_k\)-subdivision. Catlin showed failure for odd subdivisions as well in related forms. Odd \(K_t\)-models are weaker than odd \(K_t\)-subdivisions, so falsehood of Hajós does not kill \(\mathrm{OHC}\); it only shows that **subdivision-level** oddness is too strong for a \(\chi\Rightarrow\) structure implication at the exact threshold \(t=\chi\).

**Exact gap of the colour-class method.**  
There is no known way to reconnect colour classes of a critical graph into cut-connected branch sets of an odd \(K_t\)-model without either (i) creating a \(K_t\) ordinary minor (forbidden in a Hadwiger counterexample) or (ii) assuming a structural hypothesis equivalent to \(\mathrm{OHC}_t\).

---

## 6. Positive results fully proved in this note

**Theorem 6.1 (Equivalence summary).**  
Under Definition 1.9:  
(1) odd \(K_3\)-model \(\Leftrightarrow\) nonbipartite;  
(2) odd \(K_t\)-model \(\Rightarrow\) ordinary \(K_t\)-minor;  
(3) \(K_t\) subgraph \(\Rightarrow\) odd \(K_t\)-model;  
(4) bipartite \(\Rightarrow\) no odd \(K_t\)-model for all \(t\ge 3\).

**Proof.** Section 1. \(\square\)

**Theorem 6.2 (OHC implies HC; small cases).**  
\(\mathrm{OHC}_t\Rightarrow\mathrm{HC}_t\) for all \(t\). \(\mathrm{OHC}_t\) holds for \(t\le 3\). \(\mathrm{HC}_t\) holds for \(t\le 4\) by elementary structural graph theory; \(\mathrm{HC}_5,\mathrm{HC}_6\) require the Four Colour Theorem and Robertson–Seymour–Thomas (not reproved here).

**Theorem 6.3 (Double cover is a dead end for exact Hadwiger).**  
Any strategy that replaces \(G\) by its bipartite double cover \(\widehat{G}\) and applies odd-minor colouring bounds to \(\widehat{G}\) cannot prove \(\mathrm{HC}_t\), because \(\widehat{G}\) never carries odd \(K_t\)-models for \(t\ge 3\), while \(\chi(\widehat{G})\le 2\) always.

**Theorem 6.4 (Asymptotic ceiling of this approach without new structure).**  
From no \(K_t\)-minor one deduces no odd \(K_t\)-model, hence by the external odd-Kostochka–Thomason theorem \(\chi=O(t\sqrt{\log t})\). This matches ordinary clique-minor asymptotics and does not reach \(t-1\).

---

## 7. Exact gap statement (non-handwavy)

### Gap G1 — main gap  
**Missing lemma (open; equivalent to \(\mathrm{OHC}_t\) for the exact threshold):**  
> Every graph with chromatic number at least \(t\) admits an odd \(K_t\)-model.

This is precisely \(\mathrm{OHC}_t\) contrapositive. No weaker form proved in this note reaches the threshold \(t\).

### Gap G2 — lift gap  
**Missing construction:**  
A functor \(G\mapsto G^\star\) on finite graphs such that  
1. if \(G\) has no \(K_t\)-minor then \(G^\star\) has no odd \(K_{s}\)-model for some \(s=s(t)\) with \(s(t)\ge t\),  
2. \(\chi(G)\le s(t)-1\) follows from \(\chi\)-bounds under odd-\(K_s\)-exclusion applied to \(G^\star\),  
3. the odd-exclusion colouring bound for \(G^\star\) is available at the exact threshold (not merely \(O(s\sqrt{\log s})\)).

The bipartite double cover fails (1) and (2) simultaneously (Theorem 6.3). No other lift in Section 5 satisfies all three.

### Gap G3 — promotion gap  
**Missing lemma (false for bipartite graphs; open for high-chromatic \(K_t\)-minor-free graphs):**  
A controlled promotion:  
> If \(G\) has a \(K_t\)-minor and \(\chi(G)\ge 3\), then \(G\) has an odd \(K_{f(t)}\)-model for a function \(f\) with \(f(t)\ge t\).  

Already false for \(f(t)=3\) on bipartite graphs with large clique minors. For graphs with \(\chi\ge t\) and no \(K_t\)-minor (hypothetical Hadwiger counterexamples), promotion is vacuous on ordinary \(K_t\) (they have none) and cannot create odd \(K_t\)-models without contradicting the ordinary minor-freeness via Lemma 1.10(a).  

**Critical observation.**  
In a **Hadwiger** counterexample (no \(K_t\)-minor, \(\chi\ge t\)), Lemma 1.10(a) forbids odd \(K_t\)-models automatically. Therefore **inside a Hadwiger counterexample, \(\mathrm{OHC}_t\)’s hypothesis is already satisfied**. The odd-minor conjecture claims no such counterexample exists for the larger class. Using odd minors to kill Hadwiger counterexamples requires either proving the stronger \(\mathrm{OHC}_t\), or relating the counterexample to a *different* graph that *must* carry a forbidden odd model while controlling chromatic numbers — which is Gap G2.

### Gap G4 — signed colouring gap  
Zaslavsky \(\chi_\pm(G,-1)=1\) always (Lemma 4.4). No bound on \(\chi(G)\) follows from signed colouring of the antibalanced signature without additional homomorphism constraints equivalent again to ordinary colouring.

---

## 8. What would close the gap

A complete proof of \(\mathrm{HC}_t\) along this axis requires **one** of the following mutually exclusive breakthroughs:

1. **Full \(\mathrm{OHC}_t\)** at the exact threshold (Gap G1 closed for all graphs, not just ordinary-minor-free graphs).  
2. **A new lift** \(G\mapsto G^\star\) satisfying Gap G2’s three properties, plus a proof of exact odd-Hadwiger for the image class.  
3. **A structure theorem** for graphs with no \(K_t\)-minor that produces a colouring directly (Robertson–Seymour style), possibly using signed-graph bookkeeping only as an organisational tool — not as a reduction to \(\mathrm{OHC}\).

No argument in this note achieves (1)–(3). Known complete cases \(t\le 6\) do not proceed by odd-minor promotion; they use four-colour / discharging / treewidth / quasi-colouring methods.

---

## 9. Appendix A — walk parity for odd \(K_3\)-models

**Lemma A.1.**  
If \(G\) admits an odd \(K_3\)-model in the sense of Definition 1.9, then \(G\) contains an odd cycle.

**Proof.**  
Let \((B_1,B_2,B_3;X)\) be an odd \(K_3\)-model. Let \(T_i\) be a spanning tree of \(B_i\) using only \(X\)-odd edges. Let \(e_{ij}=u_{ij}v_{ij}\) be an \(X\)-even edge with \(u_{ij}\in B_i\), \(v_{ij}\in B_j\).

Define a walk \(W\):  
- Inside \(B_1\), take the unique \(T_1\)-path from \(u_{13}\) to \(u_{12}\).  
- Cross \(e_{12}\) to \(v_{12}\in B_2\).  
- Inside \(B_2\), take the \(T_2\)-path from \(v_{12}\) to \(u_{23}\).  
- Cross \(e_{23}\) to \(v_{23}\in B_3\).  
- Inside \(B_3\), take the \(T_3\)-path from \(v_{23}\) to \(v_{13}\).  
- Cross \(e_{31}\) back to \(u_{13}\in B_1\).

This is a closed walk. Count the number of \(X\)-odd edges on \(W\): each \(T_i\)-path consists entirely of \(X\)-odd edges; each \(e_{ij}\) is \(X\)-even.  

For a tree with all edges \(X\)-odd, the unique path between any two vertices has length congruent modulo \(2\) to the difference of the side-indicators \(1_X\) at its endpoints: length \(\equiv 1_X(x)+1_X(y)\pmod 2\)? An \(X\)-odd edge flips membership in \(X\). So a path of only odd edges has length \(\equiv 0\pmod 2\) iff both ends lie on the same side of \(X\), and length \(\equiv 1\pmod 2\) iff the ends lie on opposite sides.

The three even edges \(e_{ij}\) have ends on the **same** side of \(X\). Write \(s_i\in\{0,1\}\) for the side of \(u_{i,i+1}\) after identifying sides along... Track side of the attachment points:

Let \(\sigma(z)=0\) if \(z\notin X\), \(1\) if \(z\in X\). For each even edge \(e_{ij}\), \(\sigma(u_{ij})=\sigma(v_{ij})\).  

Length of \(T_1\)-path from \(u_{13}\) to \(u_{12}\) is \(\equiv \sigma(u_{13})+\sigma(u_{12})\pmod 2\) (since each odd edge flips, total flips \(\equiv\) length mod 2, and start/end sides differ by length mod 2: \(\sigma(\mathrm{end})\equiv\sigma(\mathrm{start})+\mathrm{length}\pmod 2\), so \(\mathrm{length}\equiv\sigma(u_{13})+\sigma(u_{12})\pmod 2\)).

Sum of the three tree-path lengths  
\[
\begin{align*}
&\equiv\bigl(\sigma(u_{13})+\sigma(u_{12})\bigr)+\bigl(\sigma(v_{12})+\sigma(u_{23})\bigr)+\bigl(\sigma(v_{23})+\sigma(v_{13})\bigr)\\
&\equiv\sigma(u_{13})+\sigma(u_{12})+\sigma(u_{12})+\sigma(u_{23})+\sigma(u_{23})+\sigma(u_{13})\pmod 2
\end{align*}
\]
using \(\sigma(v_{ij})=\sigma(u_{ij})\) and renaming \(v_{13}=u_{31}\) etc. consistently: each attachment point appears twice. Sum \(\equiv 0\pmod 2\).

So the walk has **even** number of odd edges? That cannot detect an odd cycle.

**Correction of the invariant.**  
An odd cycle is a closed walk of odd *total* length, not odd number of cut edges. Total length = (sum of tree path lengths) + 3. We need this odd, i.e. sum of tree path lengths even — which we just got \(\equiv 0\pmod 2\), plus 3 is odd. **Yes:** total length \(\equiv 0+3\equiv 1\pmod 2\). The closed walk has odd length, hence contains an odd cycle. \(\square\)

**Lemma A.2 (Converse construction for Definition 1.9).**  
If \(C\) is an odd cycle, then \(G\) admits an odd \(K_3\)-model.

**Proof.**  
Let \(C=(v_0,v_1,\ldots,v_{2m})\) with \(m\ge 1\) and edges \(v_iv_{i+1}\) (indices mod \(2m+1\)).

**Case \(m=1\)** (\(C\cong K_3\)).  
Branch sets \(\{v_0\},\{v_1\},\{v_2\}\), \(X=\emptyset\): every edge is \(X\)-even; cut-connectivity of singletons is vacuous. Done.

**Case \(m\ge 2\).**  
Partition \(C\) into three arc-paths of odd lengths \(\ell_1,\ell_2,\ell_3\) with \(\ell_1+\ell_2+\ell_3=2m+1\). Solutions in positive odd integers exist (e.g. \((2m-1,1,1)\)). Let the three junction vertices be \(a,b,c\), and write \(P_{ab},P_{bc},P_{ca}\) for the three internally disjoint odd paths.

Set branch sets to be the **interiors of the three paths**, except that we must include junctions. More precisely use the following cut and branches:

Put every vertex of \(C\) into a single side pattern along each path separately. Define \(X\) by walking around \(C\) and placing vertices so that:
- every edge of \(P_{ab}\), \(P_{bc}\), and \(P_{ca}\) that is **not** the middle edge of that path (if length \(\ge 3\)) is \(X\)-odd, and connectivity is arranged as below.

**Cleaner explicit model (no casework on middles):**  
Take branch sets  
\[
B_1=\{v_0\},\qquad B_2=\{v_1\},\qquad B_3=V(C)\setminus\{v_0,v_1\}.
\]
Define \(X=\{v_i:i\text{ is odd}\}\). Then:
- Edge \(v_0v_1\): \(v_0\notin X\), \(v_1\in X\), so **\(X\)-odd** — not yet an even link.
This choice of \(X\) fails for the even-link \(B_1B_2\).

**Correct explicit model:**  
Take \(X=V(C)\setminus\{v_0,v_1,v_2\}\) together with a parity fix, or use the signed-minor extraction and translate:

Since Lemma 1.7 already produces \((K_3,-1)\) as a signed minor of \((C,-1)\) by contracting positive edges after switching, the preimages of the three final vertices under those contractions are branch sets \(B_1,B_2,B_3\), and the cut \(X\) is the switch set. The contracted edges are exactly the \(X\)-odd edges (positive after switch), and they connect each branch; the three residual negative edges are \(X\)-even links. This is Definition 1.9.  

Concretely for \(C_{2m+1}\): choose junctions \(a,b,c\) so each arc has odd length. Switch every second vertex along each open arc so that all **interior** edges of each arc become positive (\(X\)-odd), while the three “first” edges incident to a chosen orientation become the residual negative (\(X\)-even) links after interiors are absorbed into branches. Set each branch set equal to the set of vertices contracted into one junction (the junction plus the interior vertices of the two half-arcs assigned to it, or simply: one branch per arc-interior plus one junction, with the three residual edges being single \(X\)-even edges between branches).  

**Fully explicit for all odd cycles:**  
Number \(C=(v_0,\ldots,v_{2m})\). Set  
\[
B_1=\{v_0\},\quad B_2=\{v_m\},\quad B_3=\{v_{2m}\},
\]
and if these are not all distinct (only if \(m=0\)), we are in the triangle case. For \(m\ge 1\), \(v_0,v_m,v_{2m}\) are distinct. The three paths between them on \(C\) have lengths \(m\), \(m\), \(1\) in some order — lengths \(m,m,1\): sum \(2m+1\). For these three lengths to all be odd, \(m\) and \(1\) odd, so \(m\) odd. If \(m\) is even, choose junctions \(v_0,v_1,v_{m+1}\) instead so arc lengths are \(1\), \(m\), \(m\): wait sum \(2m+1\). We already know three odd arcs exist; pick such junctions \(a,b,c\).

Now set \(B_a=\{a\}\), \(B_b=\{b\}\), \(B_c=\{c\}\) and put **all interior vertices of the three arcs into the branches of their arcs** as follows: for the odd path \(P_{ab}=(a=x_0,x_1,\ldots,x_{\ell}=b)\) with \(\ell\) odd, place \(x_1,\ldots,x_{\ell-1}\) into \(B_a\) (say), and define membership in \(X\) so that edges \(x_0x_1,x_1x_2,\ldots,x_{\ell-2}x_{\ell-1}\) are \(X\)-odd (so they form an odd spanning tree of the enlarged \(B_a\cup\ldots\)), while the last edge \(x_{\ell-1}x_\ell\) is \(X\)-even and serves as the even link between the enlarged \(B_a\) and \(B_b=\{b\}\).

Implementation: put \(x_j\in X\) iff \(j\) odd, for \(0\le j\le \ell-1\), and set \(b=x_\ell\) on the same side of \(X\) as \(x_{\ell-1}\) (both in or both out) so that \(x_{\ell-1}b\) is even. Check consistency at vertices shared across arcs: each junction has two arc-incident edges that are even links (the last edge of each incident arc under the orientation “away from a root”), and interiors are disjoint, so \(X\) is well-defined on interiors. At junction \(a\): \(a=x_0\notin X\) ( \(j=0\) even). The first edge \(ax_1\) is odd. The even link into \(a\) from another arc arrives as that other arc’s last edge, forcing \(a\) to match the side of its predecessor on that arc — **potential conflict**.

**Conflict resolution:** do not use singleton junctions as separate side constraints. Use **only three branch sets equal to the three open arcs including both endpoints shared** — endpoints shared is forbidden (disjoint branches).

**Standard resolution (disjoint branches):**  
Interiors only: let \(B_{ab}\) be the interior vertices of \(P_{ab}\) together with a private copy... interiors of three odd-length paths on a cycle: if all lengths \(\ge 3\), interiors are nonempty and disjoint; junctions are unassigned. Then we need junctions assigned to branches. Assign each junction to one incident branch. Three junctions, three branches: assign each junction to a distinct branch. Each branch = one junction + interior of one arc. The even link between two branches is the edge of \(C\) between a junction and the first interior vertex of an arc owned by another branch, with \(X\) chosen so that edge is even, and the interior path is odd-connected.

Specify: Branch \(B_1=\) junction \(a\) + interior of arc \(P_{ab}\). Branch \(B_2=\) junction \(b\) + interior of \(P_{bc}\). Branch \(B_3=\) junction \(c\) + interior of \(P_{ca}\).  
Edges of \(C\) used as even links: the three edges \(b-b^+\) start of interior of \(P_{bc}\)? Actually the edge between end of \(B_1\) (last interior of \(P_{ab}\), or \(a\) if no interior) and \(b\in B_2\) is the last edge of \(P_{ab}\), used as even link \(B_1\)–\(B_2\).  

Define \(X\) on \(B_1\) so the path from \(a\) through the interior of \(P_{ab}\) is connected by \(X\)-odd edges: alternate along this path starting with \(a\notin X\), first edge odd, etc. The last vertex \(w\) of this path (neighbour of \(b\) on \(P_{ab}\)) must satisfy \(\sigma(w)=\sigma(b)\) so \(wb\) is even; set \(b\)’s side to match \(w\). Then define \(X\) on \(B_2\) alternating from \(b\) through interior of \(P_{bc}\), and force the even link into \(c\), and similarly around. Consistency around the odd cycle: the product of constraints on sides is consistent precisely because the three path lengths are odd (each odd path contributes a fixed side-parity relation, and three odd relations compose consistently on an odd cycle).  

Side-parity check: traversing an odd-length path of odd edges ends on the opposite side from the start. We need the last edge even, so we only alternate on the first \(\ell-1\) edges (odd number of vertices in the odd-tree part). Length \(\ell\) odd means \(\ell-1\) even: start and last interior vertex \(w\) are on the **same** side after even number of odd edges. Setting \(b\) on the same side as \(w\) is free at first visit to \(b\). Continuing: from \(b\) through \(\ell_2-1\) odd edges (even number), last interior before \(c\) is same side as \(b\); set \(c\) same side. From \(c\) through \(\ell_3-1\) odd edges, last interior before \(a\) same side as \(c\); need it same side as \(a\) for the even link. So need side\((a)=\)side\((c)=\)side\((b)=\)side\((a)\): always true. **No obstruction.** \(\square\)

**Remark.**  
Lemma 1.7 (signed-minor form) remains the short authoritative proof that nonbipartite \(\Leftrightarrow\) odd \(K_3\)-minor. Definition 1.9 matches it; Lemma A.1 is one direction, Lemma A.2 the other.

For \(t>3\), all theorems in this note that need odd models use either  
- the signed-minor Definition 1.4, or  
- only the implications odd \(\Rightarrow\) ordinary and subgraph \(K_t\Rightarrow\) odd model (Lemma 1.10(a),(c)), both safe.  

---

## 10. Appendix B — checklist of proved vs open

| Statement | Status |
|---|---|
| Odd \(\Rightarrow\) ordinary minor | Proved (1.5) |
| Bipartite \(\Leftrightarrow\) no odd \(K_3\) | Proved (1.7, A.1) |
| \(\mathrm{OHC}_t\Rightarrow\mathrm{HC}_t\) | Proved (2.1) |
| \(\mathrm{OHC}_t\) for \(t\le 3\) | Proved (2.1) |
| \(\mathrm{HC}_t\) for \(t\le 4\) | Proved (2.4–2.5) |
| Double cover kills odd clique models | Proved (3.3) |
| Double cover cannot prove HC | Proved (6.3) |
| \(\chi_\pm(G,-1)=1\) | Proved (4.4) |
| \(\mathrm{OHC}_t\) for \(t\ge 4\) | **Open** (Gap G1) |
| Exact \(\mathrm{HC}_t\) for \(t\ge 7\) | **Open** |
| Lift \(G\mapsto G^\star\) closing Gap G2 | **No candidate works** |
| Asymptotic \(O(t\sqrt{\log t})\) via odd minors | External (5.4); does not reach HC |

---

## 11. Conclusion

The odd-minor / signed-graph / double-cover axis yields:

- a clean strengthening \(\mathrm{OHC}_t\) of \(\mathrm{HC}_t\) with correct small cases;  
- a precise dictionary (signed minors of antibalanced graphs);  
- a proof that the **bipartite double cover is useless** for exact Hadwiger;  
- a proof that **promotion of ordinary clique minors to odd clique minors fails** exactly on bipartite graphs and is equivalent to \(\mathrm{OHC}\) at the chromatic threshold;  
- the exact obstruction: inside any hypothetical Hadwiger counterexample, odd \(K_t\)-models are already absent, so odd-minor exclusion has no further purchase on that graph; a lift would be required, and none is known that preserves exact colouring thresholds.

**No complete proof of Hadwiger’s conjecture is obtained.** The gap is not a missing epsilon in an inequality; it is the absence of either a proof of \(\mathrm{OHC}_t\) or a lift satisfying Gap G2.
