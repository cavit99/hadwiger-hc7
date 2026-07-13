# Elimination of the three-component degree-eight cell in \(\mathrm{HC}_7\)

## 1. Result

### Theorem 1

Let \(G\) be a proper-minor-minimal counterexample to \(\mathrm{HC}_7\),
let \(v\in V(G)\), and suppose \(d(v)=8\).  Then

\[
   G-N[v]
\]

has at most two components.

The previous shore-packing argument in
`hadwiger_degree8_degree9_exterior_bounds.md` gave the upper bound three.
The new content is the elimination of exactly three exterior components.
The proof combines a finite eight-vertex boundary lemma with color gluing
across proper minors.

---

## 2. Setup

Put \(N=N_G(v)\), so \(|N|=8\), and suppose for a contradiction that

\[
  G-N[v]=C_1\mathbin{\dot\cup}C_2\mathbin{\dot\cup}C_3.
\]

The graph \(G\) is seven-connected.  Therefore every \(C_i\) has at
least seven neighbors in \(N\), and hence misses at most one boundary
vertex.  Choose \(m_i\in N\) so that

\[
  N\setminus\{m_i\}\subseteq N_G(C_i).                 \tag{2.1}
\]

If \(C_i\) misses no vertex, \(m_i\) is an arbitrary dummy miss and the
edge from \(C_i\) to \(m_i\) is simply ignored.  Dirac's neighborhood
inequality gives

\[
  \alpha(G[N])\le 3.                                  \tag{2.2}
\]

Let \(A=G[N]\).  Contracting each \(C_i\) to a shore vertex \(c_i\), and
discarding the ignored dummy edges, produces the **three-shore quotient**
\(Q(A;m_1,m_2,m_3)\).  Thus the \(c_i\) are pairwise nonadjacent and
\(c_i\) is adjacent to every vertex of \(N-\{m_i\}\).

---

## 3. The finite boundary dichotomy

### Definition 2 (three-anchor partition)

An ordered partition

\[
  N=S\mathbin{\dot\cup}T\mathbin{\dot\cup}P
\]

is a three-anchor partition if all three blocks are nonempty independent
sets and, for every retained index \(i\), the other two indices \(j,k\)
can be assigned bijectively to \(T,P\) so that the shore assigned to a
block does not miss a vertex of that block.  In symbols, either

\[
  m_j\notin T,\quad m_k\notin P,
\]

or

\[
  m_j\notin P,\quad m_k\notin T.                       \tag{3.1}
\]

Because of (2.2), the block sizes of such a partition are \(3,3,2\).

### Definition 3 (four-anchor partition)

An ordered partition

\[
  N=S\mathbin{\dot\cup}T\mathbin{\dot\cup}P
      \mathbin{\dot\cup}\{w\}
\]

is a four-anchor partition if \(S,T,P\) are nonempty independent sets
and the following holds for every retained index \(i\).  The other shores
can be assigned, say \(C_j\) to \(T\) and \(C_k\) to \(P\), so that

1. \(m_j\notin T\) and \(m_k\notin P\);
2. \(C_j\cup T\) is adjacent to \(C_k\cup P\) in the quotient; and
3. \(w\) is adjacent to both \(C_j\cup T\) and \(C_k\cup P\).

The assignment may depend on \(i\).

### Lemma 4 (certified boundary dichotomy)

Let \(A\) be any graph on eight vertices with \(\alpha(A)\le3\), and let
\(m_1,m_2,m_3\) be any three, not necessarily distinct, boundary
vertices.  At least one of the following holds:

1. \(Q(A;m_1,m_2,m_3)\) contains an \(N\)-meeting \(K_6\)-model;
2. there is a three-anchor partition; or
3. there is a four-anchor partition.

#### Certified proof

Only the equality pattern of the three misses matters.  Up to permuting
the boundary and shores, the patterns are

\[
  000,\qquad001,\qquad012.                             \tag{3.2}
\]

For every pair \(xy\subseteq N\), introduce a Boolean variable \(e_{xy}\).
The seventy clauses

\[
  \bigvee_{xy\in\binom X2}e_{xy}
  \qquad(X\in\tbinom N4)                              \tag{3.3}
\]

are exactly the assertion \(\alpha(A)\le3\).

For every usable three- or four-anchor partition, add the negation of the
condition that its indicated blocks are independent and that its required
quotient adjacencies hold.  Finally, for an explicit proposed six-bag
quotient model, its validity is expressed exactly as follows:

* every bag meets \(N\) and the bags are disjoint;
* for every bipartition of a bag, some quotient edge crosses the cut; and
* for every pair of bags, some quotient edge joins them.

The fixed shore-boundary edges are constants and boundary edges are the
variables \(e_{xy}\).  Thus the validity of a proposed model is a monotone
Boolean formula.  Add its negation.

For the three miss patterns in (3.2), respectively, the supplied
certificates use

\[
  141,\qquad183,\qquad98                               \tag{3.4}
\]

explicit quotient-model formulas.  In each case, (3.3), the absence of
all usable anchor partitions, and the absence of the listed quotient
models are jointly unsatisfiable.  This proves the dichotomy.

The independent verifier is

`degree8_three_shore_verify.py`.

It reads

`degree8_three_shore_certificate_0.txt`,
`degree8_three_shore_certificate_1.txt`, and
`degree8_three_shore_certificate_2.txt`,

checks bag disjointness and boundary meeting, reconstructs connectivity
from every bag cut, independently reconstructs all three- and four-anchor
conditions, and obtains `UNSAT` in all three cases.  A complete run reports

```text
degree8_three_shore_certificate_0.txt verified UNSAT with 141 model templates
degree8_three_shore_certificate_1.txt verified UNSAT with 183 model templates
degree8_three_shore_certificate_2.txt verified UNSAT with 98 model templates
```

The discovery program `degree8_three_shore_probe.py` is not trusted by the
verification step.  The remaining formal trust boundary is the Z3 kernel;
no DRAT or proof-assistant trace is presently exported. \(\square\)

---

## 4. Why every outcome closes the graph-theoretic cell

### Lemma 5 (quotient-model outcome)

If outcome 1 of Lemma 4 holds, then \(G\) contains a \(K_7\)-minor.

#### Proof

Replace every quotient shore vertex \(c_i\) occurring in a branch set by
the connected graph \(C_i\).  Connectivity and all bag adjacencies lift
from the quotient, and every bag still meets \(N\).  The six lifted bags
form an \(N\)-meeting \(K_6\)-model in \(G-v\).  The singleton \(\{v\}\)
is adjacent to all six bags and completes a \(K_7\)-model. \(\square\)

### Lemma 6 (three-anchor gluing)

Outcome 2 of Lemma 4 is impossible in a proper-minor-minimal
counterexample.

#### Proof

Fix a three-anchor partition \(S|T|P\).  For each \(i\), let \(j,k\) be
the other two indices and assign them to \(T,P\) as in (3.1).  In \(G\),
contract the three disjoint connected sets

\[
  \{v\}\cup S,\qquad C_j\cup T,\qquad C_k\cup P.       \tag{4.1}
\]

The first is a star.  The other two are connected because their shores
miss no vertex of their assigned independent block.  The three contracted
vertices are pairwise adjacent.  The first sees the other two through the
edges from \(v\) to \(T\cup P\).  Also \(|T|,|P|\ge2\), while each shore
misses at most one boundary vertex, so an edge joins the latter two sets.

The contracted graph is a proper minor and is six-colorable.  Delete the
two contracted exterior components and expand the boundary blocks, giving
a proper six-coloring of

\[
  G[N\cup C_i]
\]

in which \(S,T,P\) receive three distinct colors.  This expansion is
valid: each block is independent, and all original edges from \(C_i\) to
a block are represented by edges to the corresponding contracted vertex.

Perform this construction for \(i=1,2,3\).  Permute colors on the three
sides so that the colors on \(S,T,P\) agree.  The components \(C_i\) are
pairwise anticomplete, so the three colorings glue to a six-coloring of
\(G-v\) in which only three colors occur on \(N\).  Give \(v\) any fourth
color.  This is a six-coloring of \(G\), a contradiction. \(\square\)

### Lemma 7 (four-anchor gluing)

Outcome 3 of Lemma 4 is impossible in a proper-minor-minimal
counterexample.

#### Proof

Fix \(S|T|P|\{w\}\).  For a retained side \(i\), choose the assignment
of the other two shores supplied by Definition 3 and contract

\[
  \{v\}\cup S,\qquad C_j\cup T,\qquad C_k\cup P.       \tag{4.2}
\]

Together with the uncontracted singleton \(w\), the three contracted
vertices form a \(K_4\): the first is adjacent to all three through \(v\),
and the remaining adjacencies are precisely those required in Definition
3.  A six-coloring of this proper minor therefore gives, after deleting
the two contracted exterior components and expanding the independent
blocks, a coloring of \(G[N\cup C_i]\) in which

\[
  S,\quad T,\quad P,\quad\{w\}
\]

receive four distinct colors.  Align these four colors over all three
sides and glue.  A fifth color is absent from \(N\) and can be assigned to
\(v\), again contradicting \(\chi(G)=7\). \(\square\)

### Proof of Theorem 1

Lemma 4 gives one of its three outcomes.  Lemmas 5--7 contradict every
outcome.  Therefore exactly three exterior components cannot occur.  The
previous four-component shore certificate already excluded four or more,
so \(G-N[v]\) has at most two components. \(\square\)

---

## 5. Exact advance and remaining degree-eight gap

The degree-eight component bound is now

\[
  \boxed{\#\operatorname{comp}(G-N[v])\le2}.           \tag{5.1}
\]

The remaining degree-eight cells have one or two exterior components.
They are not settled by this theorem: with only one outside component per
retained side, the three-/four-anchor color-gluing mechanism loses one of
its two independent boundary connectors.  Resolving those cells requires
splitting a component, a rooted model, or stronger one-step minor-transition
information.
