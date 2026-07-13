# The full six-vertex \(K_3\dot\cup K_4\) cell

This note proves the helper lemma for the full case \(|C|=6\), not
only for the tight equality subcase \(e(C)=9\).  The proof always
produces a balanced partition \(C=P\dot\cup Q\) with
\(|P|=|Q|=3\).  Sections 1--4 first give the smaller equality-cell
certificate because it exposes the unique extremal configuration.
Section 5 then gives the finite certificate under the original degree
lower bounds and supersedes that restricted statement.  The central lemma is
a **finite exhaustive (computer-assisted) classification**, not a new
conceptual hand theorem.  To make the use of computation auditable,
all orbit representatives, orbit sizes, state counts, and the local
test applied to every state are recorded below.  Thus every entry can
also be checked directly from the tables; no SMT output or unrecorded
graph-search assertion is being used.  The short standard-library-only
checker `k34_c6_certificate.py` independently reproduces both tables
and asserts the unique exceptional state.

## 1. The tight equality statement

Let \(C\) be a connected graph on six vertices with nine edges.  Let

\[
 A=\{a_1,a_2,a_3\},\qquad B=\{b_1,b_2,b_3,b_4\}.
\]

Assume that

\[
 |N_C(a_i)|=4,\qquad |N_C(b_j)|=3                         \tag{1.1}
\]

for all \(i,j\), and, for every \(x\in C\),

\[
 d_C(x)+d_A(x)+d_B(x)=7.                                 \tag{1.2}
\]

Then there are distinct \(a_i,a_j\) and a partition
\(V(C)=P\dot\cup Q\), with \(|P|=|Q|=3\), such that

* \(C[P]\cup\{a_i\}\) and \(C[Q]\cup\{a_j\}\) are connected; and
* both \(P\) and \(Q\) meet \(N_C(b)\) for every \(b\in B\).

This is stronger than the requested conclusion, where \(P,Q\) were
not required to cover \(C\).

## 2. Balanced partitions and missing pairs

Put

\[
 M_i=V(C)-N_C(a_i).
\]

Thus each \(M_i\) is a two-set.  Regard
\(M=\{M_1,M_2,M_3\}\) as a three-edge multigraph on \(V(C)\), and
write \(m(x)=d_M(x)\), with multiplicity.  Since
\(d_A(x)=3-m(x)\), (1.2) gives

\[
 d_B(x)=4-d_C(x)+m(x).                                  \tag{2.1}
\]

In particular,

\[
 d_C(x)-4\leq m(x)\leq d_C(x).                          \tag{2.2}
\]

For an unordered partition \(\pi=\{S,\bar S\}\) into two triples,
let

\[
 R(S)=\{i:C[S]\cup\{a_i\}\text{ is connected}\}.
\]

Call \(\pi\) **A-compatible** if \(R(S)\) and \(R(\bar S)\) have
distinct representatives.  Equivalently,

\[
 R(S),R(\bar S)\neq\varnothing,
 \qquad |R(S)\cup R(\bar S)|\geq2.                     \tag{2.3}
\]

There are ten unordered partitions into two triples.  A
three-neighbourhood \(N_C(b)\) forbids exactly one of them, namely

\[
 \{N_C(b),V(C)-N_C(b)\}.                                \tag{2.4}
\]

Indeed, both sides of a balanced partition meet \(N_C(b)\) unless
one side is its three-element complement.  Hence the four vertices of
\(B\) forbid at most four partitions.  It follows at once that the
desired partition exists whenever at least five partitions are
A-compatible.

We next isolate the only case in which there can be fewer than five.

## 3. The finite balanced-partition lemma

### Lemma 3.1

Let \(C\) be a connected six-vertex nine-edge graph, and let
\(M_1,M_2,M_3\) be two-sets satisfying (2.2).  At least five of the
ten balanced partitions are A-compatible, except, up to relabelling,
in the following single case:

\[
\begin{split}
 E(C)={}&\{01,02,04,05,12,15,23,25,34\},\tag{3.1}\\
 \{M_1,M_2,M_3\}={}&\{15,34,34\}.                       \tag{3.2}
\end{split}
\]

In this exceptional case exactly the following four partitions are
A-compatible:

\[
 014|235,\qquad015|234,\qquad034|125,\qquad045|123.      \tag{3.3}
\]

### Proof by finite classification, with check certificate

Here is a direct rule for checking a row of the classification.  If
\(S\) is a triple, then:

1. if \(C[S]\) has at least two edges, it is connected and
   \(R(S)=\{1,2,3\}\);
2. if \(C[S]\) consists of the edge \(uv\) and the isolated vertex
   \(w\), then

   \[
   i\in R(S)\quad\Longleftrightarrow\quad
   w\notin M_i\text{ and }M_i\neq\{u,v\};              \tag{3.4}
   \]

3. if \(C[S]\) is independent, then

   \[
   i\in R(S)\quad\Longleftrightarrow\quad M_i\subseteq\bar S.
                                                                    \tag{3.5}
   \]

Thus (2.3)--(3.5) check any one of the ten partitions without a graph
search.

For completeness, Table 1 is an exhaustive classification of the
connected six-vertex nine-edge graphs.  Edges such as `01` mean
\(\{0,1\}\); `deg` is the sorted degree sequence; \(c\) is the
number of partitions for which both induced triples are connected.
Such a partition is A-compatible for every choice of \(M\).

| no. | edge set | deg | \(|\mathrm{Aut}(C)|\) | labelled orbit | \(c\) |
|---:|:---|:---:|---:|---:|---:|
| 1 | 01 02 03 12 13 15 23 24 25 | 123345 | 2 | 360 | 3 |
| 2 | 01 02 03 04 12 13 15 23 25 | 123444 | 2 | 360 | 3 |
| 3 | 01 03 04 12 14 23 24 34 45 | 133335 | 8 | 90 | 4 |
| 4 | 02 12 13 14 23 25 34 35 45 | 133344 | 2 | 360 | 3 |
| 5 | 01 02 03 12 13 15 23 25 45 | 133344 | 4 | 180 | 2 |
| 6 | 04 05 14 15 24 25 34 35 45 | 222255 | 48 | 15 | 6 |
| 7 | 01 02 03 04 05 12 23 25 34 | 222345 | 2 | 360 | 4 |
| 8 | 01 02 04 05 12 13 14 34 45 | 222444 | 6 | 120 | 3 |
| 9 | 01 02 05 12 13 14 15 34 45 | 223335 | 2 | 360 | 3 |
| 10 | 01 02 03 04 05 12 13 23 45 | 223335 | 12 | 60 | 1 |
| 11 | 01 03 04 05 12 15 23 34 35 | 223344 | 1 | 720 | 5 |
| 12 | 02 03 04 05 12 13 23 34 45 | 223344 | 2 | 360 | 3 |
| 13 | 02 03 05 12 13 23 24 34 45 | 223344 | 4 | 180 | 5 |
| 14 | 01 02 04 05 12 15 23 25 34 | 223344 | 4 | 180 | 4 |
| 15 | 02 04 05 14 15 24 25 34 35 | 223344 | 8 | 90 | 6 |
| 16 | 01 04 05 12 23 25 34 35 45 | 233334 | 2 | 360 | 5 |
| 17 | 01 03 04 05 12 15 23 25 34 | 233334 | 2 | 360 | 4 |
| 18 | 01 03 05 12 23 24 25 34 45 | 233334 | 2 | 360 | 6 |
| 19 | 01 02 03 14 15 23 25 34 45 | 333333 | 12 | 60 | 7 |
| 20 | 01 03 05 12 14 23 25 34 45 | 333333 | 72 | 10 | 9 |

The table is also an exhaustiveness certificate.  There are
\(\binom{15}{9}=5005\) labelled nine-edge graphs on a fixed six-set.
A disconnected one must be an isolated vertex together with
\(K_5-e\), so exactly \(6\binom52=60\) are disconnected.  The
labelled-orbit column sums to

\[
 4945=5005-60.
\]

The triples `(deg,c,|Aut|)` distinguish all rows (including the two
rows with the same degree sequence and the same value of \(c\)).
Thus the listed orbits are pairwise disjoint and exhaust all connected
graphs.  The automorphism orders and values of \(c\) are obtained by
direct inspection of the displayed nine-edge sets.

Rows with \(c\geq5\) already prove the lemma.  For the other twelve
rows, Table 2 records the complete check using (2.2)--(3.5).  There
are only

\[
 \binom{15+3-1}{3}=680                              \tag{3.6}
\]

multisets of three pairs on a six-set.  The entry `q:n` means that
exactly \(n\) of the multisets satisfying (2.2) have exactly \(q\)
A-compatible partitions.  The entries in each row sum to the number
of admissible multisets, so the table is a compact check certificate,
not merely a list of minima.

| graph no. | distribution `number compatible : number of multisets` |
|---:|:---|
| 1 | 7:8, 8:30, 9:156, 10:147 |
| 2 | 7:2, 8:46, 9:152, 10:265 |
| 3 | 7:4, 8:6, 9:238, 10:107 |
| 4 | 7:6, 8:25, 9:226, 10:238 |
| 5 | 6:2, 8:24, 9:110, 10:359 |
| 7 | 7:12, 8:70, 9:171, 10:162 |
| 8 | 7:9, 8:90, 9:163, 10:316 |
| 9 | 8:24, 9:187, 10:219 |
| 10 | 9:99, 10:331 |
| 12 | 6:2, 8:34, 9:144, 10:431 |
| 14 | 4:1, 6:2, 7:4, 8:33, 9:140, 10:431 |
| 17 | 6:3, 7:2, 8:38, 9:183, 10:419 |

To reproduce any entry, list the fifteen pairs in lexicographic order,
choose three with repetition, discard a choice when its endpoint
multiplicities violate (2.2), and apply the three local rules
(3.4)--(3.5), together with the connected case preceding them, to the
ten triples containing vertex \(0\).  No
connectivity or minor oracle is involved.  In particular, Table 2
shows directly that the only admissible multiset with fewer than five
compatible partitions occurs in row 14.  Applying (3.4)--(3.5) to
that row gives precisely

\[
 M=\{15,34,34\}
\]

and the four partitions in (3.3).  This proves Lemma 3.1. \(\square\)

For a machine-level audit of the arithmetic only, running

```text
python3 k34_c6_certificate.py
```

checks the displayed automorphism orders, orbit sum, values of \(c\),
all Table 2 distributions, and the assertion that the sole state with
fewer than five compatible partitions is
`(graph 14, {15,34,34})`.  The checker uses only `itertools` and
`collections` from the Python standard library.

## 4. Elimination of the exceptional row

We now finish the original lemma.  If Lemma 3.1 gives at least five
A-compatible partitions, at most four are forbidden by (2.4), so an
unforbidden one gives the required \(P,Q\) and two distinct roots.

It remains to treat (3.1)--(3.2).  From (2.1), the column degrees of
the four \(B\)-neighbourhoods are

\[
 (d_B(0),\ldots,d_B(5))=(0,2,0,4,4,2).               \tag{4.1}
\]

Every one of the four three-sets therefore contains \(3,4\), contains
neither \(0,2\), and has its third member in \(\{1,5\}\).  The two
remaining column sums in (4.1) force exactly two copies of each:

\[
 \{N_C(b):b\in B\}=\{134,134,345,345\}.               \tag{4.2}
\]

Consequently the only partitions forbidden by \(B\) are

\[
 134|025\quad\text{and}\quad345|012.                  \tag{4.3}
\]

Neither appears in (3.3).  For example, take

\[
 P=\{0,1,4\},\qquad Q=\{2,3,5\}.                     \tag{4.4}
\]

The graphs \(C[P]\) and \(C[Q]\) are already connected: their edge
sets are respectively \(\{01,04\}\) and \(\{23,25\}\).  Thus any
two distinct vertices of \(A\) may be used as roots.  By (4.2), both
\(P\) and \(Q\) meet every \(B\)-neighbourhood.  This proves the
claimed two-helper lemma. \(\square\)

## 5. The full \(\lvert C\rvert=6\) lower-bound lemma

We now remove every equality assumption used above.

### Theorem 5.1 (full six-vertex helper lemma; computer-assisted)

Let \(C\) be any connected graph on six vertices.  Suppose

\[
 |N_C(a)|\geq4\quad(a\in A),\qquad
 |N_C(b)|\geq3\quad(b\in B),                           \tag{5.1}
\]

where \(|A|=3\), \(|B|=4\), and suppose

\[
 d_C(x)+d_A(x)+d_B(x)\geq7\qquad(x\in C).             \tag{5.2}
\]

Then there is a balanced partition \(V(C)=P\dot\cup Q\) and distinct
\(a_i,a_j\in A\) such that

\[
 C[P]\cup\{a_i\}\text{ and }C[Q]\cup\{a_j\}
 \text{ are connected},                               \tag{5.3}
\]

and both \(P,Q\) meet \(N_C(b)\) for every \(b\in B\).

### Reduction to a finite \((C,A)\)-certificate

For each of the ten unordered balanced partitions
\(\pi=\{S,\bar S\}\), define its two root sets exactly as in Section
2.  Call \(\pi\) A-compatible when those sets have distinct
representatives.

If \(|N_C(b)|\geq3\), then \(b\) can fail to meet one side of
\(\pi\) only in the following exact situation:

\[
 N_C(b)=S\quad\text{or}\quad N_C(b)=\bar S.            \tag{5.4}
\]

Thus one vertex of \(B\) forbids at most one unordered partition.  If
there are at least five A-compatible partitions, four vertices of
\(B\) cannot forbid them all and the theorem follows.

Suppose instead that there are \(q\leq4\) A-compatible partitions and
that all of them are forbidden.  Different partitions require
different vertices of \(B\), because an exact three-set in (5.4)
determines one unordered partition.  Orient the \(q\) partitions so
that \(T_r\) is the exact neighbourhood of its blocking vertex.  The
other \(4-q\) vertices of \(B\) may be made complete to \(C\).  This
only increases every degree, so (5.2) has the following necessary
relaxation:

\[
 d_C(x)+d_A(x)+(4-q)+|\{r:x\in T_r\}|\geq7
 \qquad(x\in C).                                      \tag{5.5}
\]

For a fixed pair \((C,A)\), define its **best minimum slack** to be

\[
 \sigma(C,A)=
 \max_{(T_1,\ldots,T_q)}\ 
 \min_{x\in C}
 \bigl(d_C(x)+d_A(x)+(4-q)+|\{r:x\in T_r\}|-7\bigr), \tag{5.6}
\]

where the maximum is over the \(2^q\) orientations.  Hence a
no-helper state satisfying (5.2) must have \(q\leq4\) and
\(\sigma(C,A)\geq0\).

### Exhaustive certificate

There are 112 isomorphism classes of connected graphs on six
vertices.  For each \(C\), an A-neighbourhood has size 4, 5, or 6, so
there are

\[
 \binom64+\binom65+\binom66=22
\]

choices and

\[
 \binom{22+3-1}{3}=2024                               \tag{5.7}
\]

multisets of three choices.  Treating the A-neighbourhoods as a
multiset is valid because permuting the three roots changes neither
A-compatibility nor (5.2).

The standard-library checker `k34_c6_full_search.py` constructs the
112 graph orbits directly from all \(2^{15}\) labelled edge sets.  It
then checks all

\[
 112\cdot2024=226{,}688
\]

pairs \((C,A)\).  A first necessary filter observes that even four
B-vertices complete to \(C\) cannot repair a vertex with
\(d_C(x)+d_A(x)+4<7\); 186,354 states survive this filter.  Exactly 63
survivors have \(q\leq4\).  For each of those, all at most \(2^4\)
orientations in (5.6) are evaluated.  Their complete distribution is:

| \(e(C)\) | \(q\) | best minimum slack \(\sigma\) | number of states |
|---:|---:|---:|---:|
| 5 | 4 | -3 | 2 |
| 5 | 4 | -2 | 2 |
| 6 | 2 | -1 | 4 |
| 6 | 4 | -3 | 4 |
| 6 | 4 | -2 | 19 |
| 7 | 2 | -1 | 2 |
| 7 | 4 | -2 | 22 |
| 8 | 4 | -2 | 7 |
| 9 | 4 | -2 | 1 |

The counts sum to 63, and every slack is negative.  Thus no state
passes the necessary condition (5.5).  This proves Theorem 5.1 by
finite exhaustive verification. \(\square\)

This is explicitly a computer-assisted finite proof.  Its state space
and predicate are fully specified above.  Running

```text
python3 k34_c6_full_search.py
```

reconstructs all 112 unlabelled connected graphs rather than importing
an atlas, checks the stated counts, asserts the table, and finally
asserts that the list of degree-feasible no-helper states is empty.
It uses only `itertools` and `collections`.

## 6. Minor consequence

In the exceptional \(K_3\dot\cup K_4\) neighbourhood cell with
\(|C|=6\), Theorem 5.1 supplies two sets

\[
 J_1=P\cup\{a_i\},\qquad J_2=Q\cup\{a_j\}.
\]

They are disjoint connected bags, are mutually adjacent through the
edge \(a_i a_j\), and are adjacent to each of the four singleton bags
on \(B\).  They therefore form, with those four singleton bags, an
\(N(v)\)-meeting \(K_6\)-model; adjoining \(\{v\}\) gives a
\(K_7\)-minor.  Consequently the exceptional cell has

\[
 |C|\geq7.                                             \tag{6.1}
\]

The implication \(|C|=6\Rightarrow K_7\preccurlyeq G\), and hence
(6.1), is computer-assisted through Theorem 5.1.
