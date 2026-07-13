# Uniform colour-saturating-set reduction at the least failing parameter

This note audits and generalises the corrected (t=7) reduction in
`hadwiger_R7_counterexample.md`.  It is a reduction, not a proof of
Hadwiger's conjecture.

## 1. Definitions and named inputs

Write \(\eta(F)\) for the largest \(r\) such that \(F\) has a
\(K_r\)-minor.  A graph \(F\) is **\(r\)-contraction-critical** if
\(\chi(F)=r\) and every proper minor of \(F\) is \((r-1)\)-colourable.

Let
\[
 \operatorname{ex}_{\rm m}(n,K_r)
 :=\max\{|E(F)|:|V(F)|=n,\ K_r\not\preccurlyeq F\}
\]
and define the integer
\[
 D_r:=\max_{n\ge1}
 \left\lfloor {2\operatorname{ex}_{\rm m}(n,K_r)\over n}\right\rfloor .
 \tag{1}
\]
The Kostochka--Thomason theorem makes \(D_r\) finite.  It is the best
minimum-degree upper bound obtained merely by applying the exact extremal
edge count and the inequality \(\delta(F)\le 2|E(F)|/|V(F)|\).

We use four standard named results.

1. Hadwiger's conjecture holds for \(r\le6\) (the cases \(5,6\) use the
   Four Colour Theorem and the Robertson--Seymour--Thomas theorem).
2. **Mader connectivity theorem.** Every non-complete
   \(r\)-contraction-critical graph is \(7\)-connected when \(r\ge7\).
3. The exact extremal edge theorems of Mader, Jørgensen, and Song--Thomas
   give
   \[
     D_7=9,\qquad D_8=11,\qquad D_9=13.                 \tag{2}
   \]
   More generally, Thomason's sharp form of the Kostochka--Thomason
   theorem gives, with natural logarithms,
   \[
     D_r=(0.63817\ldots+o(1))r\sqrt{\log r}.           \tag{3}
   \]
   Here the constant is twice Thomason's edge-density constant
   \(0.31908\ldots\).
4. **Kriesell--Mohr pseudoforest theorem.** Let \(c\) be a proper colouring
   of a graph \(Q\), let \(T\) contain exactly one vertex of each colour,
   and let \(M\) be a graph on \(T\).  Suppose that for every
   \(xy\in E(M)\), the vertices \(x,y\) belong to one component of the
   subgraph induced by their two colours.  If every component of \(M\)
   contains at most one cycle, then \(Q\) has pairwise disjoint connected
   bags \((B_x:x\in T)\), with \(x\in B_x\), such that \(B_x\) and \(B_y\)
   are adjacent for every \(xy\in E(M)\).

For (2), the edge bounds are \(5n-15,6n-20,7n-27\), respectively (with
the characterised equality exceptions for \(K_8,K_9\)).  They make the
average degree strictly less than \(10,12,14\).  The standard clique-sum
extremal examples approach those three values, so the integers in (2) are
indeed the values of (1), not just upper bounds.

## 2. The reduction theorem

Call \(X\subseteq V(Q)\) **\(k\)-colour-saturating** if every proper
colouring \(c:V(Q)\to[k]\) uses all \(k\) colours on \(X\).

### Theorem 2.1 (uniform corrected reduction)

Suppose Hadwiger's conjecture fails, and let \(t\) be the least parameter
at which it fails.  Put \(k=t-1\).  There are a graph \(G\), a
minimum-degree vertex \(v\in V(G)\),
\[
 H:=G-v,\qquad N:=N_G(v),
\]
with all the following properties.

1. \(t\ge7\), and \(G\) is a connected, non-complete,
   \(t\)-contraction-critical graph with
   \[
     \chi(G)=t,\qquad \eta(G)=t-1,
     \qquad \delta(G)\ge t,qquad \kappa(G)\ge7.       \tag{4}
   \]
   In particular, \(G\) is \(K_t\)-minor-free.
2. The selected apex satisfies
   \[
      t\le d_G(v)=\delta(G)\le D_t.                   \tag{5}
   \]
   Thus \(d(v)\le9\) if \(t=7\), \(d(v)\le11\) if
   \(t=8\), \(d(v)\le13\) if \(t=9\), and the upper
   bound in (3) holds asymptotically.
3. The apex-deleted graph satisfies
   \[
      \chi(H)=\eta(H)=t-1=k,
      \qquad \kappa(H)\ge6.                           \tag{6}
   \]
   No assertion that \(H\) is \(k\)-contraction-critical is made or
   needed.
4. The full neighbourhood \(N\) is \(k\)-colour-saturating in \(H\), and
   \[
      t\le |N|=d(v)\le D_t.                          \tag{7}
   \]
   More strongly, \(N\) has no proper colour-saturating subset.  For
   every \(w\in N\), a colouring of the contracted minor \(G/vw\)
   expands to a proper \(k\)-colouring \(c_w\) of \(H\) and a colour
   \(i_w\) for which \(w\) is the unique vertex of \(N\) coloured
   \(i_w\).
5. No \(K_k\)-model in \(H\) has every branch set meeting \(N\).  In
   particular, this is an obstruction rooted at the entire apex
   neighbourhood, not at a freely replaceable abstract terminal set.

### Proof

Because the conjecture is true through parameter \(6\), the least failing
parameter satisfies \(t\ge7\).  Choose a graph witnessing failure at
parameter \(t\), and inside it choose a minor \(G\) minimal under the
proper-minor relation subject to \(\chi(G)\ge t\).  Minor-closedness of
being \(K_t\)-minor-free shows that \(G\) is still \(K_t\)-minor-free.
Every proper minor of \(G\) is \((t-1)\)-colourable.  For any vertex
\(x\), colouring \(G-x\) with \(t-1\) colours and giving \(x\) one new
colour shows \(\chi(G)\le t\).  Hence \(\chi(G)=t\), and \(G\) is
\(t\)-contraction-critical.

The graph \(G\) is connected: otherwise a component of chromatic number
\(t\) would be a proper subgraph and hence a proper minor of \(G\).  It is
not complete, since the only complete \(t\)-chromatic graph is \(K_t\),
which is forbidden.  Since \(t\) is the least failing parameter,
\(\mathrm{HC}_{t-1}\) holds.  Thus \(\chi(G)=t>t-2\) forces a
\(K_{t-1}\)-minor, while \(G\) has no \(K_t\)-minor.  Consequently
\(\eta(G)=t-1\).

We next prove the degree assertion rather than importing it from ordinary
critical-graph folklore.  If \(Q\) is \(r\)-contraction-critical and
\(u\in V(Q)\), then
\[
   \alpha(Q[N(u)])\le d(u)-r+2.                       \tag{9}
\]
Indeed, otherwise take an independent set \(A\subseteq N(u)\) of order at
least \(d(u)-r+3\), and put \(B=N(u)\setminus A\).  Then
\(|B|\le r-3\).  Contract the connected star \(Q[A\cup\{u\}]\) to one
vertex \(w\), and properly colour the resulting proper minor with
\(r-1\) colours, naming the colour of \(w\) as colour \(1\).  Every
neighbour outside the star of a vertex of \(A\) has colour different from
\(1\).  If some colour \(j\ne1\) is absent from \(B\), expand the colouring
by giving all vertices of \(A\) colour \(1\), giving \(u\) colour \(j\),
and retaining all other colours.  This is a proper \((r-1)\)-colouring of
\(Q\), a contradiction.  Hence all \(r-2\) colours different from \(1\)
occur on \(B\), impossible because \(|B|\le r-3\).  This proves (9).

Ordinary criticality gives \(\delta(G)\ge t-1\).  If a vertex had degree
\(t-1\), (9) would make its neighbourhood a clique, and its closed
neighbourhood would be a \(K_t\) subgraph.  Therefore
\(\delta(G)\ge t\).  Mader's connectivity theorem gives
\(\kappa(G)\ge7\), proving (4).

Choose \(v\) with \(d(v)=\delta(G)\).  If \(n=|V(G)|\), then
\[
 d(v)\le {2|E(G)|\over n}
       \le {2\operatorname{ex}_{\rm m}(n,K_t)\over n},
\]
so integrality and (1) give (5), including the quoted special and
asymptotic bounds.

Set \(H=G-v\).  It is a proper minor of \(G\), so
\(\chi(H)\le t-1\).  Conversely, adding one vertex can increase chromatic
number by at most one, so \(t=\chi(G)\le\chi(H)+1\).  Thus
\(\chi(H)=t-1\).  Applying \(\mathrm{HC}_{t-1}\) to \(H\) gives a
\(K_{t-1}\)-minor, whereas a \(K_t\)-minor in \(H\) would also be one in
\(G\).  Therefore \(\eta(H)=t-1\).  Finally, if fewer than six vertices
separated \(H\), adjoining \(v\) to that separator would give a separator
of \(G\) of order at most six.  Hence \(\kappa(H)\ge6\), proving (6).

Every proper \(k\)-colouring of \(H\) uses all \(k\) colours on
\(N=N_G(v)\): a colour missing from \(N\) could be assigned to \(v\),
contrary to \(\chi(G)=k+1\).

Contraction-criticality gives substantially more than the existence of
some inclusion-minimal saturating subset.  Fix \(w\in N\), contract the
edge \(vw\) to a vertex \(q\), and take a proper \(k\)-colouring of the
proper minor \(G/vw\).  Expand it to \(H=G-v\) by giving \(w\) the colour
of \(q\) and retaining all other colours.  This is proper: every edge of
\(H\) incident with \(w\) becomes an edge incident with \(q\) after the
contraction.  Moreover, for every \(x\in N-\{w\}\), the edge \(vx\) makes
\(qx\) an edge of \(G/vw\).  Thus \(x\) avoids the colour of \(q\), and
\(w\) is the unique vertex of \(N\) with that colour.  Consequently
\(N-\{w\}\) is not saturating.  Every proper subset \(X\subsetneq N\) is
contained in \(N-\{w\}\) for some \(w\notin X\), and the same witness
colouring shows that \(X\) is not saturating.  Hence \(N\) itself is the
unique inclusion-minimal saturating subset of \(N\).  The bounds in (7)
are exactly (5), including the already proved lower bound \(d(v)\ge t\).

If a \(K_k\)-model \((B_1,\ldots,B_k)\) in \(H\) had every bag meeting
\(N\), then the singleton bag \(\{v\}\) would be adjacent to every
\(B_i\).  These \(k+1=t\) bags would form a \(K_t\)-model in \(G\), a
contradiction.  This proves assertion 5 and completes the proof.
\(\square\)

### Lemma 2.2 (the abstract size-\(k\) Kriesell--Mohr cell)

Let \(Q\) be a graph that admits a proper \(k\)-colouring, and let
\(S\subseteq V(Q)\) be a \(k\)-colour-saturating set of order exactly
\(k\).  If
\(\overline{Q[S]}\) is a pseudoforest (every component contains at most
one cycle), then \(Q\) has a \(K_k\)-model rooted at \(S\).  In
particular, this conclusion holds if
\[
   \Delta\bigl(\overline{Q[S]}\bigr)\le2.             \tag{8}
\]

**Proof.** Fix any proper \(k\)-colouring \(c\) of \(Q\).  Saturation and
\(|S|=k\) make \(c|_S\) a bijection.  For two roots \(x,y\in S\) of
colours \(i,j\), respectively, they must lie in one component of
\(Q[c^{-1}(\{i,j\})]\).  Otherwise swap colours \(i,j\) on the component
containing \(x\).  The unique colour-\(j\) root \(y\) lies in a different
component, and \(x\) was the unique colour-\(i\) root.  After the swap,
colour \(i\) is absent from \(S\), contrary to saturation.

Put \(M:=\overline{Q[S]}\).  The Kriesell--Mohr theorem gives disjoint
connected rooted bags \((B_x:x\in S)\) that are adjacent for every
\(xy\in E(M)\).  If \(xy\notin E(M)\), then \(xy\in E(Q[S])\), and this
root edge itself joins \(B_x\) to \(B_y\).  Thus the bags form a rooted
\(K_k\)-model.  Finally, a graph of maximum degree at most two is a
disjoint union of paths and cycles, hence is a pseudoforest. \(\square\)

### Corollary 2.3 (why the requested cell is vacuous in this reduction)

In Theorem 2.1, the only inclusion-minimal saturating subset of \(N\) is
\(N\) itself, and
\[
   |N|=d(v)\ge t=k+1.
\]
Consequently the abstract cell \(|S|=t-1\), including its
\(\Delta(\overline{H[S]})\le2\) subcell closed by Lemma 2.2, never arises
from the contraction-critical counterexample reduction.

## 3. Exact residual and adversarial cautions

The genuine counterexample-derived residual is a single neighbourhood
cell, always under all the apex-extension hypotheses in Theorem 2.1:
\[
 t\le |N|=d(v)\le D_t,                               \tag{10}
\]
where \(N\) is colour-saturating, every proper subset of \(N\) fails to
be saturating, each \(w\in N\) has the explicit contraction-colouring
witness furnished by \(G/vw\), and no \(K_{t-1}\)-model in \(H\) has all
its branch sets meeting \(N\).  Eliminating this cell for every least
failing \(t\) would prove the conjecture.  Nothing above eliminates it.

Lemma 2.2 closes the requested abstract \(|S|=t-1\),
\(\Delta(\overline{H[S]})\le2\) cell (indeed, the whole pseudoforest
cell), but Corollary 2.3 shows that this cell is not produced by the
minor-critical reduction.

It is essential to retain the full data
\[
 (G,v,H,N),\qquad G=H+v\text{ with }N=N_G(v),
\]
together with the facts that \(G\) is \(K_t\)-minor-free and
\(t\)-contraction-critical.  Abstract minimal saturation, even combined
with \(\chi(H)=\eta(H)=t-1\) and \(\kappa(H)\ge6\), does **not** by itself
characterise a counterexample.  A blanket assertion that every abstract
pair \((H,S)\) with those latter properties has an \(S\)-meeting
\(K_{t-1}\)-model is a strictly stronger target and is not proved here.

Two further pitfalls are ruled out explicitly:

- Mader supplies \(\kappa(G)\ge7\) and hence \(\kappa(H)\ge6\); ordinary
  \(t\)-criticality does not supply \(\kappa(G)\ge t-1\).
- The degree boost \(\delta(G)\ge t\) uses contraction-criticality through
  the star-contraction proof of (9); it is false as a general local-clique
  assertion for ordinary critical graphs.

## 4. Disconnected graphs and small parameters

For \(t\ge2\), both chromatic number and Hadwiger number are the maxima of
the corresponding quantities over components (a clique model, being
connected, lies in one component).  Hence any disconnected counterexample
has a counterexample component, and the proper-minor-minimal graph used
above is connected.  Isolated components cause no difficulty.

For completeness: at \(t=1\), the only graph with no \(K_1\)-minor is the
null graph, with chromatic number \(0\); at \(t=2\), the graphs with no
\(K_2\)-minor are edgeless; at \(t=3\), the graphs with no
\(K_3\)-minor are forests.  The cases \(t=4,5,6\) are the standard proved
cases quoted above.  Thus no small-parameter or disconnected exception is
being hidden in the phrase "least failing parameter \(t\ge7\)."
