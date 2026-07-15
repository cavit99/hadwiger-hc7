# Audit: twin-seam bypass parity barrier

**Verdict:** GREEN for the elementary two-colour obstruction, GREEN for
the literal mechanism-falsifying shell, and GREEN for the common
edge-deletion inequality \(\chi(G-e-f)\geq 5\).  The application of the
Dominating 4-Colour Theorem gives an unlabelled dominating \(K_5\)-model
in that common host.  The stronger path/cycle normalization of that model
is outside this audit and must remain covered by its separate proof or
audit.

**Audited sources:**

- `barriers/hc7_atomic_twin_seam_bypass_parity_barrier.md`
- `active/hc7_atomic_twin_seam_bypass_parity_probe.py`

**Source SHA-256 values:**

```text
c850aaed8496b8548314b9ee3b16738619f1c59620c7e1c62f793974dab6978c
10dbc137a593526ce7598f0b8c8b548cb304746ad4bb3483dd271d2b621ddd7a
```

The first value is for the Markdown source and the second for the probe.

## 1. Kempe-component invariant

Write

\[
 L_0=(G-e)[\phi^{-1}(\{\alpha,\beta\})]
 \quad\hbox{and}\quad
 L=L_0-f=(G-e-f)[\phi^{-1}(\{\alpha,\beta\})].
\]

This formulation removes the only notational ambiguity in Section 1 of
the source: the phrase “deleting \(f\)” refers to deleting the **edge**
\(f\) from \(L_0\), whereas the displayed definition of \(L\) has already
performed that deletion.

If \(z,u\) lie in one component of \(L\), every legal
\(\alpha\beta\)-Kempe exchange in \(G-e-f\) swaps all vertices of one
component of \(L\).  Such a swap changes no vertex's membership in the
two-colour set and changes no edge of its induced graph.  Hence the
components of \(L\) remain fixed throughout any sequence of these
exchanges.  The sequence has the same net effect as swapping a union of
the original components.

Initially \(\phi(z)=\phi(u)=\alpha\).  Since \(z,u\) occupy one component,
they are swapped together or not at all and therefore remain equal.  A
proper colouring after restoring \(e=zu\) would require them to be
different.  Thus the asserted simultaneous operation—restore \(e\) while
also making the ends of \(f\) equal so the colouring descends to
\(G/f\)—is impossible within this two-colour exchange system.  A global
palette permutation preserves equality and cannot change the conclusion.

This proves exactly the claimed mechanism barrier.  It does not rule out
Kempe exchanges involving a third colour, changing the starting response,
or using other minor-critical structure; the source does not claim that
it does.

## 2. Executable shell

The verifier ran successfully with

```text
PYTHONPATH=active/runtime/deps python3 \
  active/hc7_atomic_twin_seam_bypass_parity_probe.py
```

and returned

```text
GREEN bypass_parity_shell
orders 15 43
connectivity 4
```

The code literally checks:

1. `PHI` is proper on the graph with the edge `zu` deleted and has
   `PHI[z]=PHI[u]`;
2. `PSI` is proper on the graph with the edge `td` deleted, has
   `PSI[d]=PSI[t]`, and separates `z,u`;
3. the displayed two-colour lock contains both the through-`td` path and
   the `td`-avoiding bypass, and remains connected across all four named
   ends after edge deletion;
4. the two lobe supports, gate restrictions, unique `u`-portal, connected
   bipartite old boundary, and two adjacent full packets are literal; and
5. the exact partitions induced by the two responses differ on both twin
   boundaries.

The final `K_7`-minor check is also independently witnessed by the seven
branch sets

\[
\{i_2,z\},\quad
\{d_1,i_3\},\quad
\{a_1,a_2,d,t\},\quad
\{r_1\},\quad
\{i_1\},\quad
\{b,e_1,q\},\quad
\{r_2\}.
\]

They are pairwise disjoint and connected, and every pair has a literal
edge between it.  Thus the solver's terminal output is not being used as
an unverifiable existence assertion.

The shell has vertex-connectivity four and contains that literal
\(K_7\)-model.  It is a counterexample only to the proposed local
two-colour decoder, not to the terminal-disjunctive theorem and not to
\(HC_7\).

## 3. Common edge-deletion chromatic bound

Here and throughout this paragraph

\[
                         H=G-e-f
\]

means deletion of the two **edges**, not deletion of four endpoint
vertices.  Assume that \(G\) is not six-colourable and that the edges
\(e\) and \(f\) are vertex-disjoint.  If \(H\) had a proper colouring
with at most four colours, choose one endpoint of \(e\) and give it a new
fifth colour, and choose one endpoint of \(f\) and give it a new sixth
colour.  The chosen vertices are distinct.  Every old edge remains proper,
all edges incident with either recoloured vertex are proper because its
colour is fresh, and an edge between the two recoloured vertices, if
present, has colours five and six.  In particular the restored edges
\(e,f\) are proper.  This would six-colour \(G\), a contradiction.
Therefore

\[
                            \chi(G-e-f)\geq5.
\]

By the published Dominating 4-Colour Theorem—every graph with no
dominating \(K_5\)-model is four-colourable—the contrapositive supplies a
dominating \(K_5\)-model in this exact common edge-deletion host.  Both
named responses restrict to colourings of this same graph; they need not
be the same colouring.

This implication is unlabelled.  It does not prove that the five bags
meet prescribed boundary duties, avoid the two packet reserves, yield a
fixed pair, or return a smaller ranked exact-seven separation.  Those are
precisely the remaining allocation obligations.

## 4. Required wording discipline

The source is mathematically sound provided the following readings are
kept explicit in any promoted statement.

1. `G-{e,f}` means deletion of the two named edges.  Prefer the notation
   `G-e-f` or define the edge set of the host explicitly.
2. The lower bound \(\chi(G-e-f)\ge5\) uses both the non-six-colourability
   of \(G\) and the fact that \(e,f\) are vertex-disjoint.
3. “Both responses live in the common host” means their restrictions are
   two proper colourings of the same edge-deleted graph, not that a common
   exact boundary state has already been obtained.
4. The dominating-five conclusion is an unlabelled substrate.  No
   palette-to-duty or bag-to-boundary lift follows from the cited theorem.

With these qualifications, there is no overstatement in the barrier's
negative conclusion or in the common-host chromatic observation.
