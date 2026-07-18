# Connected far-side subgraphs, cyclic sectors, and corner separators

**Status:** written proof; separate internal audit.

This note combines the five cyclic connected sets at a degree-eight vertex
with three connected subgraphs rooted at the other three boundary vertices.
It proves two complete minor-model constructions and an exact corner-cut
calculation.  The additional disjointness hypotheses in Section 1 are not
yet known in the active `HC_7` configuration.  In particular, the result
does not prove that a far-side subgraph can be removed while leaving a
disjoint connected subgraph with all seven prescribed contacts.

## 1. Setup

Let `G` be seven-connected and let

\[
 V(G)=L\mathbin{\dot\cup}T\mathbin{\dot\cup}R,
 \qquad E_G(L,R)=\varnothing,
 \qquad |T|=7.                                           \tag{1.1}
\]

Write

\[
 T=U\mathbin{\dot\cup}B,
 \qquad U=\{u_0,u_1,u_2,u_3\},
 \qquad B=\{b_0,b_1,b_2\}.                              \tag{1.2}
\]

Suppose that

\[
 \{v\},D,P_0,P_1,P_2,C_0,C_1,C_2,C_3,C_4              \tag{1.3}
\]

are pairwise vertex-disjoint, where \(v\in L\) and every other displayed
set is nonempty and connected.  Assume the following literal properties.

1. Each `P_j` contains `b_j`, is contained in \(R\cup\{b_j\}\), and the
   three sets `P_0,P_1,P_2` are pairwise adjacent.
2. The vertex `v` is adjacent to every `P_j`.
3. For \(0\le i\le3\),

   \[
        C_i\subseteq L\cup\{u_i\},\qquad
        C_i\cap T=\{u_i\},\qquad C_i\cap L\ne\varnothing,           \tag{1.4}
   \]

   and `C_i` contains a specified neighbour of `v` in `L`.  The set
   `C_4` lies in `L` and also contains a specified neighbour of `v`.
4. The sets `C_0,...,C_4` are cyclically adjacent:

   \[
                         E_G(C_i,C_{i+1})\ne\varnothing
                         \quad(i\bmod 5).                \tag{1.5}
   \]
5. The connected set `D` is adjacent to each of

   \[
                         P_0,P_1,P_2,C_0,C_1,C_2,C_3.    \tag{1.6}
   \]

   It may be anticomplete to `C_4`.

Let `M` be the bipartite nonadjacency graph with parts
`{P_0,P_1,P_2}` and `{C_0,...,C_4}`.  Thus `P_jC_i` is an edge of `M`
exactly when `P_j` and `C_i` are anticomplete in `G`.

## 2. Two complete minor-model constructions

### Lemma 2.1 (matching defects)

If `M` is a matching of order at most two, then `G` contains a `K_7`
minor.

### Proof

Use the explicit allocation table in
[the cyclic connected-set contact theorem](../results/hc7_degree8_contact_allocation.md),
Theorem 4.2.  In that table replace each singleton branch set `\{b_j\}`
by the connected set `P_j`.  Replace a two-vertex branch set
`\{b_j,c_i\}` by \(P_j\cup C_i\).

Every replacement is connected: `P_j` and `C_i` are connected, and the
table uses their union only when the corresponding adjacency is present.
The replacements are pairwise disjoint by (1.3).  Every adjacency checked
in the table uses only a `P_j`--`C_i` adjacency, a cyclic adjacency in
(1.5), or an edge from `v` to one of the participating connected sets.
All of those are literal edges under the present hypotheses.  No edge
inside `B` was used by that table.

The six resulting branch sets each contain one of the eight labels

\[
                     P_0,P_1,P_2,C_0,C_1,C_2,C_3,C_4.    \tag{2.1}
\]

If `D` misses `C_4`, the table puts `C_4` in a branch set containing a
second label.  By (1.6), `D` is adjacent to every one of the six branch
sets.  Appending `D` gives seven pairwise disjoint, connected, pairwise
adjacent branch sets.  Hence they form a `K_7`-minor model. \(\square\)

### Lemma 2.2 (all defects at the unrooted sector)

If

\[
              M\subseteq\{P_0C_4,P_1C_4,P_2C_4\},       \tag{2.2}
\]

then `G` contains a `K_7` minor.

### Proof

Use the following seven branch sets:

\[
 D,\quad P_0,\quad P_1,\quad P_2,\quad
 C_4\cup C_0,\quad C_1,\quad C_2\cup C_3.              \tag{2.3}
\]

They are pairwise disjoint.  The two unions in (2.3) are connected by
the cyclic adjacencies `C_4C_0` and `C_2C_3`.  The three `P_j` are
pairwise adjacent, and (2.2) makes each of them adjacent to every one of
`C_0,C_1,C_2,C_3`.  The three sector branch sets are pairwise adjacent
through `C_0C_1`, `C_1C_2`, and `C_3C_4`.  Finally, (1.6) makes `D`
adjacent to every other displayed branch set.  Thus (2.3) is an explicit
`K_7`-minor model. \(\square\)

The second lemma is useful when the connected set `D` has exactly the
seven contacts in (1.6).  It shows that an arbitrary star of missing
adjacencies at the sole unrooted sector is terminal; it is not an
additional exceptional incidence pattern.

## 3. A rooted missing pair gives two corner separators

### Lemma 3.1 (rooted corner compression)

Suppose that `P_j` is anticomplete to `C_i` for some \(0\le i\le3\), and that

\[
                             P_j\cap R\ne\varnothing.    \tag{3.1}
\]

Put `r=u_i`, `X=C_i`, and

\[
 S=N_G(X),\quad
 S_L=S\cap L,\quad
 S_T=S\cap(T-\{r\}),\quad
 S_R=S\cap R.                                           \tag{3.2}
\]

Then

\[
 K_L=\{r\}\cup S_L\cup S_T,
 \qquad
 K_R=(T-\{r\})\cup S_R                                 \tag{3.3}
\]

are vertex separators, and

\[
 |K_L|=1+|S_L|+|S_T|,qquad
 |K_R|=6+|S_R|,qquad
 |K_L|+|K_R|=7+|S|.                                    \tag{3.4}
\]

Consequently exactly one of the following conclusions is available.

1. If `|S_R|=1`, then `K_R` is the boundary of an actual nontrivial
   order-seven separation.
2. If \(|S_R|\ge2\), every component `A` of \(X-\{r\}\) satisfies

   \[
        r\in N_G(A),\qquad
        7\le |N_G(A)|<|S|,                              \tag{3.5}
   \]

   and `P_j` lies on the opposite side of the corresponding
   full-neighbourhood separation.

Thus the second outcome is a strict separator-order descent retaining the
named root `r` and the named missed connected set `P_j`.

### Proof

The set `S=N_G(X)` is a separator: `X` is nonempty, while `P_j` is
disjoint and anticomplete to `X`.  Seven-connectivity gives \(|S|\ge7\).

Delete `K_R`.  The set `X` survives.  A path from `X` into `R` must use
an edge from `r` to `R`, because \(X-\{r\}\subseteq L\) and there are no
`L`--`R` edges.  Every `R`-neighbour of \(r\in X\) belongs to `S_R` and was
deleted.  On the other hand, \(P_j\cap R\) survives, since anticompleteness
of `P_j` and `X` makes it disjoint from `S_R`.  Hence `K_R` is a genuine
separator.  Seven-connectivity gives

\[
                              6+|S_R|=|K_R|\ge7.         \tag{3.6}
\]

In particular `S_R` is nonempty, and `|S_R|=1` gives the first outcome.

Now let `A` be a component of \(X-\{r\}\).  It is nonempty by (1.4).  Since
`X` is connected, `A` has a neighbour at `r`.  Every neighbour of `A`
outside `X` lies in \(S_L\cup S_T\), and no vertex of one component of
\(X-\{r\}\) is adjacent to another such component.  Therefore

\[
             r\in N_G(A)
             \subseteq \{r\}\cup S_L\cup S_T=K_L.      \tag{3.7}
\]

The set `P_j` survives outside \(A\cup N_G(A)\) because it is
anticomplete to `X`.  Thus `N_G(A)` is the boundary of a genuine
nontrivial full-neighbourhood separation.  Seven-connectivity and (3.7)
give

\[
  7\le |N_G(A)|
     \le 1+|S_L|+|S_T|
      = |S|+1-|S_R|.                                   \tag{3.8}
\]

When \(|S_R|\ge2\), the last quantity is strictly less than `|S|`, proving
(3.5).  Formula (3.4) follows directly from the disjoint decomposition
\(S=S_L\mathbin{\dot\cup}S_T\mathbin{\dot\cup}S_R\). \(\square\)

## 4. The combined dichotomy

### Theorem 4.1

Under the setup of Section 1, at least one of the following holds.

1. `G` contains a `K_7` minor.
2. There are indices `j in {0,1,2}` and `i in {0,1,2,3}` such that
   `P_j` is anticomplete to the rooted sector `C_i`.

If, in addition, every `P_j` which occurs in outcome 2 meets `R`, then
outcome 2 has the exact-separator or strict-descent alternatives of
Lemma 3.1.

### Proof

If `M` is a matching of order at most two, apply Lemma 2.1.  If all edges
of `M` are incident with `C_4`, apply Lemma 2.2.  In every other case `M`
has an edge `P_jC_i` with \(i\le3\), which is outcome 2.  The final assertion
is Lemma 3.1. \(\square\)

This statement is intentionally conditional.  The two finite minor-model
constructions do not force the connected set in a rooted missing pair to
meet `R`; at the incidence level, all rooted defects may be concentrated
at a singleton `P_j=\{b_j\}`.

## 5. The boundary-free far-side subgraph

The five-subgraph configuration contains a useful way to remove that
singleton issue for one selected defect.  The observation does not solve
the disjoint-residual problem.

### Lemma 5.1 (targeted thickening)

Let \(B=\{a,s,t\}\).  In \(G[R\cup T]-a\), suppose that
\(Q_s,Q_t,Q_0\) are pairwise disjoint, connected, and pairwise adjacent,
that

\[
 Q_s\cap T=\{s\},\qquad Q_t\cap T=\{t\},
 \qquad Q_0\cap T=\varnothing,                          \tag{5.1}
\]

and that `a` is adjacent to each of these three subgraphs.  For any chosen
\(b\in B\), there are three pairwise disjoint, connected, pairwise adjacent
sets \(P_a,P_s,P_t\), with \(P_x\cap T=\{x\}\) for each \(x\in B\), such that the
chosen set `P_b` contains `Q_0` and hence meets `R`.

### Proof

If `b=a`, put

\[
 P_a=\{a\}\cup Q_0,qquad P_s=Q_s,qquad P_t=Q_t.       \tag{5.2}
\]

If `b=s`, put

\[
 P_a=\{a\},\qquad P_s=Q_s\cup Q_0,qquad P_t=Q_t,       \tag{5.3}
\]

and use the symmetric definition when `b=t`.  Every displayed union is
connected by the assumed row adjacencies or the edge from `a`.  The three
sets are disjoint, pairwise adjacent, and have the asserted exact traces.
Since `Q_0` is nonempty and has empty boundary trace, it lies in `R`.
Thus the selected `P_b` meets `R`. \(\square\)

For a selected missing pair `bC_i`, apply Lemma 5.1 with that `b`.  If the
thickened `P_b` remains anticomplete to `C_i`, it is an `R`-side witness
for Lemma 3.1.  If it becomes adjacent to `C_i`, then `Q_0` supplies a
literal connected repair of that incidence.

The latter alternative is precisely where the present argument stops:
`Q_0` may lie inside the connected set `D` reserved as the seventh branch
set.  Absorbing it into `P_b` can therefore destroy the disjointness in
(1.3).  The missing host theorem must prove one of the following:

1. the three rooted `B`-subgraphs can be chosen disjoint from a connected
   subgraph retaining the seven contacts in (1.6);
2. the repair can be peeled from that connected subgraph while preserving
   those contacts; or
3. failure of such a peel gives an order-seven separation with compatible
   six-colourings of its two closed sides.

## 6. Trust boundary

- The strict descent in Lemma 3.1 preserves one boundary root and one
  missed connected subgraph.  It does not automatically preserve the
  other six branch-set labels, the cyclic sector system, or a boundary
  equality partition extending through both closed sides.
- The sets `P_j` in Theorem 4.1 are required to be disjoint from `D`.
  The five named far-side subgraphs do not currently imply this after one
  of them is used to repair a missing incidence.
- Lemma 5.1 removes the singleton obstruction for one chosen rooted
  missing pair, but a single boundary-free subgraph cannot be assigned to
  several `P_j` simultaneously.
- The theorem uses seven-connectivity only in the corner calculation.
  It does not infer contraction-critical colouring compatibility from
  connectivity or from the incidence graph.

## 7. Dependency

- [degree-eight cyclic connected-set contact allocation](../results/hc7_degree8_contact_allocation.md)
