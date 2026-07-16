# Independent audit: six-terminal crossing decoder

## Audit identity

- theorem file:
  `results/hc7_disjoint_k6minus_six_terminal_crossing_decoder.md`
- audited theorem SHA-256:
  `cb86d1378d5f5168b7f05f78a979add8881e69c5faed0b050e3bded4c0293e1b`
- verifier file:
  `results/hc7_disjoint_k6minus_six_terminal_crossing_decoder.py`
- audited verifier SHA-256:
  `02a37655bb2c3e4ef2a5b125deecaac41431530e7cfe5a921616406e45095b81`

## Verdict

**GREEN.**  Theorem 2.1, its twelve explicit positive certificates, the
three exact negative quotient types, their three fourteen-vertex subdivided
realisations, Corollary 2.2, and Proposition 3.1 are correct under the stated
normalized configuration.  The finite negative conclusions are properly
restricted to the bare finite graphs.  Corollary 2.2 is exactly an
application of Humeau--Pous Theorem 1.5 to the six distinct displayed
terminals.  Proposition 3.1 uses only the endpoint-preserving `2`-stable
rerouting supplied by Tutte's theorem and seven-connectivity; it does not
claim that stability alone supplies crossed paths.

This is an independent internal audit, not external peer review.  No source
content was changed during the audit.

The theorem was subsequently moved from `active/` to `results/`, and only
its status, adjacent-audit link, and verifier invocation were updated.  The
hash above binds this audit to that exact promoted revision; its mathematical
content is the revision audited below.

## 1. Fifteen crossing types

For the cyclic order

\[
                (a_3,y,x,q,r,p),
\]

the crossing associated with indices `i<j<k<l` joins positions `i,k` and
`j,l`.  Direct enumeration gives exactly the following fifteen types:

\[
\begin{array}{lll}
(a_3x,yq),&(a_3x,yr),&(a_3x,yp),\\
(a_3q,yr),&(a_3q,yp),&(a_3r,yp),\\
(a_3q,xr),&(a_3q,xp),&(a_3r,xp),\\
(a_3r,qp),&(yq,xr),&(yq,xp),\\
(yr,xp),&(yr,qp),&(xr,qp).
\end{array}
\]

The first row is exactly the declared negative set (2.1), and the other
twelve rows occur exactly once in the certificate table.  Thus there is no
missing or duplicated combinatorial type.

## 2. Positive branch-set certificates

I independently reconstructed the quotient edge set from Section 1 and
checked every row of the table.  In each row:

1. there are exactly seven nonempty, pairwise disjoint vertex sets;
2. every set induces a connected subgraph after the two crossing edges are
   added; and
3. all twenty-one pairs of sets have an edge between them.

The supplied checker verifies these three properties directly for all
twelve rows.  It then independently searches for a `K_7` model and returns
positive on all twelve graphs.  Its output was:

```text
crossing_types 15
explicit_k7_certificates 12
exact_negative_types [((3, 4), (5, 9)), ((3, 4), (5, 10)), ((3, 4), (5, 11))]
subdivided_negative_types 3
GREEN: six-terminal crossing decoder verified
```

The contraction and lifting step is sound.  The two crossing paths have
disjoint interiors and those interiors avoid the six linkage paths.  One
may first contract each linkage path to its labelled edge and then contract
each crossing path to its labelled edge.  When a crossing edge is used by a
displayed model, its internal vertices can be assigned to one incident
branch set; the two assignments remain disjoint.  Extra host edges are
irrelevant because the proof takes a subgraph before contracting.

## 3. Exact negative search

On twelve vertices, seven nonempty branch sets force at least two singleton
branch sets: otherwise at least fourteen vertices would be required.  The
checker iterates over every possible exact singleton clique of size two
through seven.  Once the singleton bags are fixed, it enumerates every
connected candidate of order at least two that is adjacent to every
singleton, and recursively selects the required number of pairwise
disjoint, pairwise adjacent candidates.  Unused vertices are permitted, as
they must be for a minor model.  The size cutoff

\[
 |B|\le |R|-2(m-1)
\]

only reserves the minimum two vertices for each of the other `m-1`
non-singleton bags, so it cannot discard a valid model.

The search returns negative precisely for

\[
               (a_3x,yq),\qquad(a_3x,yr),\qquad(a_3x,yp).
\]

As a separate implementation check, I ran the independently promoted exact
twelve-vertex detector from
`results/hc7_disjoint_k6minus_support6_linkage_classifier.py` on all fifteen
quotients.  It again returned twelve positives and exactly the same three
negatives.  Thus the negative claim is not inferred from failure of the
explicit certificate table.

For each negative type, the checker also replaces both crossing edges by
internally disjoint two-edge paths with new internal vertices.  Each new
vertex has degree two.  The recursive detector uses the exact identity

\[
 K_7\preccurlyeq H
 \quad\Longleftrightarrow\quad
 K_7\preccurlyeq H-v
 \quad\text{or}\quad
 K_7\preccurlyeq H/vw\text{ for some }w\in N_H(v)
\]

whenever `deg(v)<6`.  Indeed, `v` cannot be a singleton `K_7` branch set;
if it occurs in a nonsingleton connected branch set, some incident edge
`vw` lies in that branch set and may be contracted.  Conversely, deletion
and contraction cannot create a false positive for the original graph.
After eliminating the two new vertices, every branch reaches the audited
twelve-vertex search.  The recurrence terminates and returns negative for
all three subdivided graphs.  I inspected the deletion, contraction and
relabeling routines: they delete loops, preserve every other adjacency and
cache only normalized simple graphs.

The middle type deserves one harmless clarification: `yr` is already the
contracted edge of the linkage path `P_5`.  A second clean `y`--`r` path
contracts to a parallel edge, which is ignored in the simple quotient.  The
checker's set representation correctly implements that quotient.

## 4. Six-terminal web corollary

Put

\[
 T=(a_3,y,x,q,r,p).
\]

The six entries are pairwise distinct because the two normalized supports
are disjoint.  Humeau--Pous define a crossing of `T` as two vertex-disjoint
`T`-paths whose four endpoint positions alternate.  The interiors of such
paths avoid `T` by the definition of a `T`-path.  In the graph `J` of
(2.2), every vertex of `A union B` and of the six-path skeleton other than
the six entries of `T` has been deleted.  Consequently every crossing of
`T` in `J` is a clean crossing in the exact sense of Theorem 2.1.

The fifteen alternating endpoint types are the fifteen types listed in
Section 1 of this audit.  The decoder closes twelve by an explicit `K_7`
model.  The other three are precisely

\[
 (a_3x,yq),\qquad (a_3x,yr),\qquad (a_3x,yp),
\]

which is outcome 2 of Corollary 2.2.  If `T` is crossless, Theorem 1.5 of
Humeau--Pous says that `J` embeds in a web with frame `T`; equivalently in
the paper's Definition from Section 4, there is a set of edges `F` on the
same vertex set such that `J+F` is such a web.  This is exactly the
same-vertex web completion in outcome 3.

The source correctly warns that the completion edges in `F` need not be
host edges.  It draws no separator, linkage, or minor conclusion from those
virtual edges.  The citation in the audited revision names Theorem 1.5;
Theorem 1.3 in the paper is instead the elementary description of
three-ribs and would not support this corollary.

## 5. Stable-linkage proposition

### 5.1 Scope of the cited theorem

Wollan's paper states Tutte's theorem as Theorem 1.1: if `S` is a subgraph
of a three-connected graph and its prescribed segments are
`P_1,...,P_t`, they can be rerouted with the same endpoints so that every
bridge is `2`-stable.  The explanatory paragraph immediately following the
theorem explicitly reformulates this for a collection of internally
disjoint paths: all endpoints are preserved and every bridge attaches to
at least two distinct rerouted paths.

Here take the twelve distinct linkage ends as branch vertices of `S` and
the six paths as its six segments.  Since the host is seven-connected, the
three-connectivity hypothesis holds.  Because all twelve ends are distinct,
the endpoint-preserving internally disjoint paths remain vertex-disjoint.
This proves exactly the first sentence of Proposition 3.1.  The number six
is not needed by Tutte's theorem; it describes this application.

### 5.2 Attachment cardinality and separation

For a nontrivial bridge component `C`, every neighbour of `C` lies in
`N_Sigma(C)`.  If that set had order at most six, its deletion would
separate the nonempty component `C` from at least one of the twelve skeleton
ends.  This contradicts seven-connectivity, so
`|N_Sigma(C)|>=7`.

If equality holds, put

\[
 L=V(C)\cup N_\Sigma(C),\qquad R=V(G)\setminus V(C).
\]

Then `L union R=V(G)`, `L intersection R=N_Sigma(C)`, and no edge joins
`L-R=C` to `R-L`.  The first open side is nonempty, while the second
contains at least one of the twelve skeleton ends because the boundary has
only seven vertices.  Hence this is an actual order-seven separation, as
claimed.

### 5.3 Endpoint-sensitive augmenting path

Suppose `C` attaches at

\[
 u\in P_5-y,\qquad v\in P_i-b_i,quad i\in\{0,1,2\}.
\]

Connectivity of `C` supplies a shortest `u`--`v` path whose internal
vertices all lie in `C`.  It is disjoint internally from both six-vertex
supports and all six rerouted linkage paths.  Its endpoints meet precisely
the hypotheses of the clean augmenting-path theorem in the bridge note,
which gives a `K_7` minor.  This proves item 3.

The exclusions are exact: the cited augmenting theorem does not cover an
attachment at `y` or at `b_i`.  Nor does the argument turn an attachment
set of order at least eight into a bounded separator.  The source states
both limitations correctly.

## 6. Trust boundary

Promoted by this audit:

- the twelve explicit `K_7`-minor constructions;
- the exact three-type finite quotient residue;
- the three corresponding fourteen-vertex subdivided negative examples;
- the exact crossing-or-web trichotomy in Corollary 2.2;
- endpoint-preserving `2`-stable rerouting of the six paths;
- the order-at-least-seven attachment bound;
- the exact order-seven separation when equality holds; and
- the endpoint-sensitive prohibition in Proposition 3.1(3).

Not proved here or in the audited source:

- that any of the three residual crossing types yields a better labelled
  `K_5` model;
- that the residual paths have a bounded common transversal;
- that an attachment set of order at least eight yields a useful bounded
  separation; or
- `HC_7`.
