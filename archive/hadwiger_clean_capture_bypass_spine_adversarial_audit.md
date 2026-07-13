# Adversarial audit: clean capture, bypass, and dependency spine

## Verdict

* hadwiger_rooted_k24_clean_capture.md: **GREEN after a categorical
  correction.** Directed source--sink Menger, the lift, contact count,
  and attachment bound are sound. A minimum directed separator may be
  a source as well as an internal vertex or a contracted sink; the main
  note now lists the source-gate outcome explicitly.
* hadwiger_clean_gate_minimal_bypass.md: **GREEN after the same
  endpoint correction.** The internal-gate and sink-bypass
  constructions lift to disjoint branch sets. In the sink lemma the
  new separator may be \(a\) or \(z\), so Theorem 5.2 now concludes
  “a closer one-vertex gate, possibly a source,” not necessarily an
  ordinary internal gate.
* hadwiger_locked_carrier_dependency_spine.md: **RED as formerly
  stated; GREEN at the corrected strength.** The bounded-spine theorem,
  contraction lift, colour-reuse repair, defect-star model, and protected
  Two Paths equivalence are sound. The former Corollary 2.3 incorrectly
  promoted separation in a chosen spanning tree to separation in the
  original carrier. That graph-gate claim and its downstream
  “one-stem topological lock” consequence have been retracted.

No audited result closes the zero-access helper. The corrected exact
gap is control of non-tree bridges across the dependency spine, followed
by a state-gluable web or adhesion.

## 1. Directed versus undirected gates

In the clean-capture auxiliary digraph, \(C_1,C_2\) are contracted to
capacity-one sinks and all arcs leaving them are deleted. A flow of
value two therefore uses \(a,z\) as distinct starts and the two carriers
as distinct ends. Lifting a sink replaces it by the whole connected
carrier and keeps the two lifted paths disjoint.

A cut of order one has three genuinely different forms:

1. an internal vertex of the undirected remainder;
2. a source \(a\) or \(z\);
3. a contracted sink.

Only the first is an ordinary internal cutvertex. The third says that
every admissible route to the other sink first enters this carrier; it
need not produce a cutvertex inside the lifted carrier. The second is
the source-gate residue treated conditionally by the source bypass
theorem. The root-capture corollary formerly compressed the first two
into “ordinary gate”; it has been patched.

The same endpoint issue occurred in Lemma 5.1 of the bypass note.
Menger's separator \(q\in U\) can equal a source. The proof still gives
a strictly smaller reachable root shore, but Theorem 5.2 may return a
source gate rather than an internal gate. Its statement and iteration
paragraph now retain this outcome.

## 2. Branch-set lift in the bypass theorems

For an internal gate, the two root-side paths end at \(p\in A\) and
\(s\), respectively. The far-side path begins at \(s\), so its only
intersection with the \(s\)-path is assigned to the same new rooted
branch. Its interior avoids the root shore and \(C_1\); the arm
\(A\subseteq T_i\) is outside the remainder \(R\). Hence

\[
 P_p\cup A\cup C_1,\qquad P_s\cup Q\cup C_2
\]

are disjoint and connected. Replacing \(T_i\) by its connected residue
\(B\) preserves the prescribed terminal and all stated helper
adjacencies. A shortest final connector is taken in \(R\), from which
every \(T_j\) was deleted, so it cannot consume a terminal branch.

The sink construction has the same lift. The path to \(C_1\) is stopped
at first entry; the other root path lies in \(U\), while \(C_2\notin U\).
The arm joins that second path to \(C_2\). Thus the two prospective
rooted sets are disjoint before the final connector. These checks use
the hypotheses exactly; no stronger ambient linkage is implicit.

## 3. Same-colour Kempe prefixes

Theorem 4.2 does not need a matching between missing helpers and second
colours. Each selected prefix starts in the same residue branch \(B\),
stops on first entry into its own reserved helper, and has interior
disjoint from every reserved branch and every fixed bypass path. The
union of all prefix interiors is therefore connected to \(B\).
Intersections among prefixes are harmless because every intersecting
vertex is assigned to that one enlarged branch. Reusing the same
\(\alpha/\gamma\)-component for several helpers creates no branch-set
conflict.

The first-entry and avoidance clauses are indispensable. Without them,
a prefix for one helper could pass through another reserved helper and
the simultaneous statement would be false.

## 4. The zero-access defect star

After all helpers outside \(\mathcal Z\) are repaired, the fixed bypass
certificate still gives six disjoint connected carriers. All clique
edges are present except possibly those from the protected residue to
members of \(\mathcal Z\). The four terminal residues retain their old
neighbours of the apex, and the two new carriers contain \(a,z\).
Adding the singleton apex therefore gives exactly the asserted

\[
                  K_7-K_{1,|\mathcal Z|}
\]

model. In particular \(|\mathcal Z|=1\) gives a prescribed
\(K_7^-\)-minor. This is a conditional near-clique model, not a
\(K_7\)-minor and not by itself a contradiction.

## 5. The false graph-gate inference

Theorem 2.1 correctly confines every **mixed tree edge** to the union of
the root-to-LCA dependency stems. It does not control non-tree edges.
The former Corollary 2.3 asserted that, when there is no mixed tree edge,
\(t\) separates \(R\) from \(F\) in the carrier.

A four-vertex counterexample with disjoint portal sets refutes this.
Let

\[
 V(T)=\{t,r,f,q\},\quad E(T)=\{tr,tf,rf,rq,fq\},
\qquad R=\{r\},\quad F=\{f\},\quad Q_1=\{q\},
\]

and choose the spanning tree \(tr,tf,rq\). No tree edge is mixed. Any
arm must contain \(r,f\). If it omits \(q\), the residue
\(\{t,q\}\) is disconnected; if it contains \(q\), the residue misses
\(Q_1\). Thus no detachable partition exists. Nevertheless the
non-tree edge \(rf\) survives in \(T-t\), so \(t\) is not a graph
separator.

The corrected corollary says only that no component of
\(\mathcal T-t\) meets both portal types. Consequently
\(|\mathcal Z|=1\) gives a one-stem **tree** lock, not a one-stem
topological lock or a one-vertex graph gate.

## 6. Contractions and the protected Two Paths equivalence

The contraction lift is valid. If a contracted vertex \(w\) belongs to
one side of a connected adjacent partition, expanding \(w\) to the edge
\(uv\) on that same side preserves connectedness, adjacency to the other
side, and the union of all portal labels. The same argument expands the
connected protected residue \(B_0\) after contracting it to \(\beta\).

Theorem 4.5 is an exact equivalence:

* a detachable partition with \(B_0\) on the residue side contains an
  \(R'\)-\(F'\) path in the arm and a disjoint
  \(\beta\)-\(Q\) path in the residue;
* conversely, two such paths can be made adjacent by a shortest
  connector, and a spanning tree containing their connecting edge
  assigns every unused carrier vertex to one of two connected sides.

The classical Two Paths Theorem applies only after fixing distinct
representatives \(r\in R'\), \(f\in F'\), and \(q\in Q\). Failure of
the set-valued linkage implies failure for every such fixed choice, so
this use is legitimate. A web obtained for one fixed choice must not be
treated as a simultaneous web for all portal choices. If endpoint roles
coincide, the correct residue is the stated one-path-avoidance or
common-portal case.

## 7. Exact remaining gap

After the corrections, the surviving chain is

\[
\text{zero-access helper}
\Longrightarrow
\text{bounded mixed-tree spine plus unrestricted non-tree bridges}.
\]

To progress, one must either use minor-critical state transitions to
reroute those bridges into a clean helper prefix, or show that the
resulting fixed-terminal Two Paths obstruction yields a colour-gluable
adhesion. Neither conclusion follows from the portal system or
seven-connectivity alone.
