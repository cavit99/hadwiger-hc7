# Elimination of the four-component degree-nine cell in \(\mathrm{HC}_7\)

## 1. Result

### Theorem 1

Let \(G\) be a proper-minor-minimal counterexample to \(\mathrm{HC}_7\),
let \(v\in V(G)\), and suppose \(d(v)=9\).  Then

\[
  G-N[v]
\]

has at most three components.

The previous two-defect shore theorem gave the upper bound four.  This note
eliminates exactly four components by combining explicit quotient
\(K_6\)-models with colorings of four carefully chosen proper minors.

---

## 2. Four two-defect shores

Put \(N=N_G(v)\), so \(|N|=9\), and suppose

\[
  G-N[v]=C_1\mathbin{\dot\cup}C_2\mathbin{\dot\cup}
             C_3\mathbin{\dot\cup}C_4.                 \tag{2.1}
\]

Seven-connectivity gives \(|N_G(C_i)|\ge7\).  Consequently each shore
misses a set \(M_i\subseteq N\) of order at most two.  Enlarge it, if
necessary, to a two-element set; ignoring the extra shore-boundary edges
can only make the desired certificates harder.  Dirac's inequality gives

\[
  \alpha(G[N])\le4.                                   \tag{2.2}
\]

Write \(A=G[N]\).  The **four-shore quotient** is obtained from
\(A\cup C_1\cup\cdots\cup C_4\) by contracting every \(C_i\) to a vertex
\(c_i\), where \(c_i\) sees exactly \(N-M_i\).  The shore vertices are
pairwise nonadjacent.

---

## 3. Anchor partitions

### Definition 2 (four-anchor partition)

An ordered partition

\[
  N=S\mathbin{\dot\cup}T_1\mathbin{\dot\cup}T_2
       \mathbin{\dot\cup}T_3                           \tag{3.1}
\]

is usable if all four blocks are nonempty and independent and the following
holds for each retained side \(i\).  The other three shores can be assigned
bijectively to \(T_1,T_2,T_3\) so that

1. the miss set of a shore is disjoint from its assigned block; and
2. the three sets \(C_j\cup T_a\) supplied by that assignment are pairwise
   adjacent.

The assignment may depend on \(i\).

### Definition 3 (five-anchor partition)

A partition

\[
  N=S\mathbin{\dot\cup}T_1\mathbin{\dot\cup}T_2
       \mathbin{\dot\cup}T_3\mathbin{\dot\cup}\{w\}   \tag{3.2}
\]

is usable if \(S,T_1,T_2,T_3\) are nonempty independent sets and, for
each retained side, the other shores can be assigned as in Definition 2
so that the three connected shore-block sets are pairwise adjacent and
each is adjacent to \(w\).

All adjacency conditions refer to actual quotient edges.  For example,
the sets \(C_j\cup T_a\) and \(C_k\cup T_b\) are automatically adjacent
if \(C_j\) sees a vertex of \(T_b\) or \(C_k\) sees a vertex of \(T_a\);
otherwise an edge of \(A\) from \(T_a\) to \(T_b\) is required.

---

## 4. Certified finite dichotomy

### Lemma 4

For every nine-vertex graph \(A\) with \(\alpha(A)\le4\), and every four
two-element miss sets \(M_1,\ldots,M_4\), at least one of the following
holds:

1. the four-shore quotient has an \(N\)-meeting \(K_6\)-model;
2. there is a usable four-anchor partition; or
3. there is a usable five-anchor partition.

Moreover, in outcome 1 the six bags may be chosen in the simple form

\[
  C_i\cup\{x_i\}\quad(1\le i\le4),\qquad
  \{y\},\quad\{z\},                                  \tag{4.1}
\]

where the six boundary representatives are distinct.

#### Certified proof

Regard the four miss sets as the four edges of a loopless multigraph;
parallel edges are allowed.  Shore and boundary permutations show that
only the isomorphism type of this multigraph matters.  A direct canonical
generation gives exactly twenty-three loopless multigraphs with four edges
(isolated vertices are then added to make the boundary order nine).

For the boundary graph use the thirty-six Boolean edge variables
\(e_{xy}\).  The 126 clauses

\[
  \bigvee_{xy\in\binom X2} e_{xy}
  \qquad(X\in\tbinom N5)                              \tag{4.2}
\]

are exactly \(\alpha(A)\le4\).

For every candidate partition in Definitions 2 and 3, its usability is an
explicit Boolean formula:

* independence says that all same-block edge variables are false;
* connectivity says that an assigned miss edge is disjoint from its block;
* every required adjacency is either a fixed shore-boundary edge or a
  disjunction of boundary edge variables.

Add the negation of every usability formula.  For a quotient model of the
form (4.1), connectedness and pairwise adjacency are likewise exact
monotone formulas; add their negations.

For every one of the twenty-three miss-multigraph types the resulting
system is unsatisfiable.  The certificates contain between ten and
twenty-seven quotient models per type, 423 models in total.  The files are

```text
degree9_four_shore_certificate_00.txt
...
degree9_four_shore_certificate_22.txt
```

The independent verifier `degree9_four_shore_verify.py`:

1. regenerates and canonically checks all twenty-three miss types;
2. reconstructs (4.2);
3. independently enumerates all four- and five-anchor partitions and their
   assignment permutations;
4. checks disjointness and boundary meeting for every quotient model;
5. reconstructs bag connectedness from all bag cuts and every pairwise bag
   adjacency; and
6. obtains `UNSAT` for every type.

The discovery program `degree9_four_shore_probe.py` is not imported by the
verifier.  The remaining formal trust boundary is Z3; no DRAT or
proof-assistant trace is exported. \(\square\)

---

## 5. Converting the dichotomy to a contradiction

### Lemma 5 (quotient outcome)

Outcome 1 of Lemma 4 gives a \(K_7\)-minor in \(G\).

#### Proof

Replace every quotient shore vertex in (4.1) by the corresponding connected
component \(C_i\).  The six bags lift to an \(N\)-meeting \(K_6\)-model in
\(G-v\).  Add the singleton bag \(\{v\}\). \(\square\)

### Lemma 6 (four-anchor color gluing)

Outcome 2 of Lemma 4 is impossible.

#### Proof

Fix the partition (3.1).  For each retained index \(i\), choose the supplied
assignment of the other shores, say \(C_{j_a}\) to \(T_a\), and contract

\[
  \{v\}\cup S,qquad C_{j_1}\cup T_1,qquad
  C_{j_2}\cup T_2,qquad C_{j_3}\cup T_3.              \tag{5.1}
\]

All four sets are connected: the first is a star, and a shore assigned to
\(T_a\) misses no vertex of that independent block.  The four contracted
vertices form a clique.  The star image is adjacent to the other three
through \(v\), and the remaining adjacencies are part of Definition 2.

This is a proper minor, so it has a six-coloring.  Delete the three
contracted exterior components and expand their independent boundary
blocks.  The result is a coloring of \(G[N\cup C_i]\) in which the four
blocks in (3.1) have four distinct colors.

Align those four colors across the four retained sides.  Since the
components in (2.1) are anticomplete, the colorings glue to a six-coloring
of \(G-v\).  Only four colors occur on \(N\), so an unused fifth color can
be assigned to \(v\), contradicting \(\chi(G)=7\). \(\square\)

### Lemma 7 (five-anchor color gluing)

Outcome 3 of Lemma 4 is impossible.

#### Proof

Use the same contractions (5.1).  Definition 3 says that their four images,
together with the uncontracted singleton \(w\), form a \(K_5\).  A
six-coloring of the proper minor therefore expands to a coloring of the
retained side with the five prescribed boundary blocks in (3.2).  Align
these colors over all four sides and glue.  The sixth color is absent from
\(N\), so give it to \(v\), again a contradiction. \(\square\)

### Proof of Theorem 1

Lemma 4 gives one of its three outcomes, while Lemmas 5--7 contradict all
three.  Thus four exterior components are impossible.  The previous
two-defect shore theorem excludes five or more, proving

\[
  \boxed{\#\operatorname{comp}(G-N[v])\le3}
\]

when \(d(v)=9\). \(\square\)

---

## 6. Remaining degree-nine gap

The remaining degree-nine cells have one, two, or three exterior
components.  The present four-side gluing proof needs three outside shores
to prescribe three independent connector blocks on every retained side;
it does not automatically descend to fewer components.
