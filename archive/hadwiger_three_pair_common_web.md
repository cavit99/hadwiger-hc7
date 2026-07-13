# Three failed pair-packets force one common hexagram web

## 1. Setting

Let \(G\) be seven-connected, let \(S\) be a seven-cut, and let \(D\)
be a component of \(G-S\). Assume that another component of \(G-S\)
is nonempty. Since \(S\) is a minimum cut, \(D\) is full to \(S\).

Partition

\[
 S=A\mathbin{\dot\cup}B\mathbin{\dot\cup}C
   \mathbin{\dot\cup}\{r\},                         \tag{1.1}
\]

where

\[
 A=\{a_1,a_2\},\qquad
 B=\{b_1,b_2\},\qquad
 C=\{c_1,c_2\}.                                    \tag{1.2}
\]

For \(s\in S\), put \(P_s=N_D(s)\). Say that two pair blocks, for
example \(A,B\), have a packet in \(D\) if there are vertex-disjoint
paths

\[
 P_{a_1}\longrightarrow P_{a_2},\qquad
 P_{b_1}\longrightarrow P_{b_2}.                   \tag{1.3}
\]

No assumption on the edges of \(G[S]\) is needed for the geometric
theorem below.

## 2. Portal transversals

### Lemma 2.1

If \(|D|\ge7\), the seven portal sets \((P_s:s\in S)\) have a system
of distinct representatives.

#### Proof

Suppose Hall fails. Choose nonempty \(I\subseteq S\) and put

\[
 X=\bigcup_{s\in I}P_s,\qquad |X|<|I|.
\]

If \(D-X\ne\varnothing\), a component \(K\) of \(D-X\) has

\[
 N_G(K)\subseteq X\cup(S-I),
\]

whose order is at most six. This contradicts seven-connectivity.
Therefore \(D=X\), whence
\[
 |D|=|X|<|I|\le7,
\]
contrary to \(|D|\ge7\). \(\square\)

## 3. Three bare four-webs

### Lemma 3.0 (low-connectivity shores have bounded defect)

Let \(Z\subseteq V(D)\) have order \(z\le2\), and let \(K\) be a
component of \(D-Z\) with \(D-(K\cup Z)\ne\varnothing\). Then

\[
                         |N_S(K)|\ge7-z.           \tag{3.0}
\]

If equality holds, \(N_S(K)\cup N_D(K)\) is an exact seven-cut. Thus
a cutvertex piece has boundary defect at most one, and a two-separator
piece has boundary defect at most two; the tight cases are nested exact
adhesions.

#### Proof

Every neighbour of \(K\) outside \(K\) lies in \(S\cup Z\), and the
opposite component of \(G-S\) lies beyond that set. Therefore
\[
 N_G(K)=N_S(K)\mathbin{\dot\cup}N_D(K)
 \subseteq N_S(K)\mathbin{\dot\cup}Z
\]
is a vertex cut. Seven-connectivity gives
\[
 7\le |N_S(K)|+|N_D(K)|
 \le |N_S(K)|+z,
\]
which is (3.0). At equality all inequalities are equalities, so the
displayed external neighbourhood has order seven and is an exact cut.
\(\square\)

Consequently the non-three-connected branch is not an arbitrary
infinite web residue. It lies in the defect-at-most-one/two split
machinery, with every tight row exported as a nested exact cut.

### Lemma 3.1

Suppose \(D\) has no packet for a chosen two blocks, say \(A,B\).
Then \(D\) has a plane embedding in which all four full portal sets

\[
                    P_{a_1},P_{a_2},P_{b_1},P_{b_2}
\tag{3.1}
\]

lie on the boundary of one face.

#### Proof

Adjoin four independent artificial terminals to \(D\), one for each
label in \(A\cup B\), with the terminal for \(s\) adjacent to the full
portal set \(P_s\). Give the terminals the alternating frame

\[
                         (a_1,b_1,a_2,b_2).
\]

A cross of this frame is exactly the packet (1.3). By the generalized
Two Paths Theorem, the crossless society has a same-vertex edge
completion to a web with this frame.

Suppose a nonempty set \(X\subseteq D\) lies in a clique inserted behind
a facial triangle \(T\) of the web rib. Replace each artificial
terminal in \(T\) by its boundary label and retain each shore vertex
of \(T\); call the resulting set \(\widehat T\). Then
\(|\widehat T|\le3\), and it accounts for every original neighbour of
\(X\) in \(D\) and in the four represented boundary classes.

The three omitted boundary labels are \(c_1,c_2,r\). Hence

\[
                 N_G(X)\subseteq
                 \widehat T\cup\{c_1,c_2,r\},
\]

of order at most six. This separates \(X\) from the nonempty opposite
component of \(G-S\), contradicting seven-connectivity. Thus no actual
shore vertex lies in an inserted clique. Deleting the four artificial
terminals from the bare rib leaves the required plane embedding of
\(D\). \(\square\)

## 4. The common-face theorem

### Theorem 4.1 (three-packet synchronization)

Assume:

1. \(D\) is three-connected;
2. \(|D|\ge7\); and
3. none of the three block pairs \(AB,AC,BC\) has a packet in \(D\).

Then at least one of the following conclusions holds.

1. \(D\) has a plane embedding with one face containing all six portal
   sets
   \[
   P_{a_1},P_{a_2},P_{b_1},P_{b_2},P_{c_1},P_{c_2}.
   \tag{4.1}
   \]
2. There is an exact seven-cut
   \[
                         X\cup\{r\},               \tag{4.2}
   \]
   where \(X\subseteq D\) consists of six vertices and separates a
   nonempty proper part of \(D\) from the other component of \(G-S\).

If the lower bound \(|D|\ge7\) is omitted, the additional residual is
the six-vertex core \(D=X\).

#### Proof

By Lemma 3.1 and uniqueness of the plane embedding of a
three-connected planar graph, there are faces

\[
\begin{aligned}
F_{AB}&\supseteq P_{a_1}\cup P_{a_2}\cup
                  P_{b_1}\cup P_{b_2},\\
F_{AC}&\supseteq P_{a_1}\cup P_{a_2}\cup
                  P_{c_1}\cup P_{c_2},\\
F_{BC}&\supseteq P_{b_1}\cup P_{b_2}\cup
                  P_{c_1}\cup P_{c_2}.
\end{aligned}                                      \tag{4.3}
\]

If two of these faces coincide, say \(F_{AB}=F_{AC}\), that face
contains all six portal sets. If \(F_{BC}\) were distinct, its
intersection with the common face would contain the four portal sets
belonging to \(B\cup C\). Lemma 2.1 supplies four distinct
representatives in that intersection. But two distinct faces of a
three-connected plane graph meet in at most one vertex or one edge, a
contradiction. Hence all three faces coincide, giving outcome 1.

Suppose the three faces are distinct. Then

\[
\begin{aligned}
P_{a_1}\cup P_{a_2}&\subseteq F_{AB}\cap F_{AC},\\
P_{b_1}\cup P_{b_2}&\subseteq F_{AB}\cap F_{BC},\\
P_{c_1}\cup P_{c_2}&\subseteq F_{AC}\cap F_{BC}.
\end{aligned}                                      \tag{4.4}
\]

Each intersection in (4.4) has order at most two. Lemma 2.1 supplies
six distinct representatives, so the three unions in (4.4) are
pairwise disjoint two-vertex sets. Let their union be \(X\); then
\(|X|=6\), and every portal in \(D\) for a label in
\(A\cup B\cup C\) belongs to \(X\).

If \(D-X\ne\varnothing\), let \(K\) be a component of \(D-X\).
No vertex of \(K\) has a neighbour in \(A\cup B\cup C\), and every
shore neighbour outside \(K\) lies in \(X\). Therefore

\[
                         N_G(K)\subseteq X\cup\{r\}.
\]

The opposite component of \(G-S\) lies beyond this set.
Seven-connectivity forces equality, so \(X\cup\{r\}\) is the exact
seven-cut (4.2). If \(D-X=\varnothing\), then \(D=X\) is the stated
six-vertex core. \(\square\)

## 5. The hexagram order

### Corollary 5.1

In outcome 1 of Theorem 4.1, choose distinct representatives

\[
 \alpha_i\in P_{a_i},\quad
 \beta_i\in P_{b_i},\quad
 \gamma_i\in P_{c_i}\qquad(i=1,2)
\]

on the common facial boundary. Up to reversing the face, interchanging
the names within pairs, and permuting \(A,B,C\), their circular order is

\[
        \alpha_1,\beta_1,\gamma_1,
        \alpha_2,\beta_2,\gamma_2.                 \tag{5.1}
\]

#### Proof

The failure of the \(AB\)-packet says that the four occurrences
\(\alpha_1,\alpha_2,\beta_1,\beta_2\) alternate on the face: otherwise
two disjoint facial arcs give the two paths. The same holds for \(AC\)
and \(BC\).

The two \(\alpha\)-occurrences divide the circle into two arcs.
Alternation puts one \(\beta\) and one \(\gamma\) on each arc.
The \(BC\)-alternation forces their orders on the two arcs to agree.
This is exactly (5.1), up to the listed symmetries. \(\square\)

Thus three unrelated-looking Two Paths failures are one simultaneous
six-terminal hexagram web, unless they expose an actual nested
seven-adhesion (or the finite six-vertex core). No symbolic portal
representatives are compared: Lemma 2.1 supplies one common SDR and the
faces contain the full portal sets.

## 6. Application to the fixed-trace transition

In Corollary 2.2C of
hadwiger_exact_trace_interface_dichotomy.md, the accepting exterior
shore \(C\) has three pair blocks \(I,J,K\) and no packet for any two.
If \(C\) is three-connected and has order at least seven, Theorem 4.1
gives either:

* one common hexagram web for the six boundary roots; or
* a nested exact seven-cut.

The nested-cut overlap theorem in
hadwiger_nested_moser_overlap_closure.md routes the pure-Moser
three-shore application to a two-shore adhesion. The common-face
hexagram is therefore the sole unbounded three-connected geometry left
by the normalized non-rainbow transition. Low-connectivity shores and
the six-vertex core remain separate finite-boundary residues.
