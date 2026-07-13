# Atomic three-packet circuits and rooted-core completion

## 1. Status

The tempting statement

> strict minimum-fragment surplus plus all three pairwise packets forces a
> simultaneous three-packet

is false.  It already fails on a four-vertex complete shore.  This note
gives the sharp circuit and then proves that it cannot occur in any of the
seven fully-positive matching rows of the audited seven-edge funnel.  The
proof of the latter fact is an explicit two-case `K_7` construction, not a
minor-search assertion.

The same completion principle eliminates the exact order-five and
order-six circuits returned by the small-order solver.  Thus these circuits
are genuine counterexamples to a purely relative linkage theorem but are
not obstructions in the actual full-adhesion gate.

## 2. The rank-two `K_4` capacity circuit

Let the seven boundary labels be

\[
 A=\{a_0,a_1\},\qquad B=\{b_0,b_1\},\qquad
 C=\{c_0,c_1\},\qquad\{s\}.                       \tag{2.1}
\]

The three demands are the pairs `A,B,C`.  Let the open shore consist of
four pairwise adjacent vertices

\[
                         x_{00},x_{01},x_{10},x_{11},             \tag{2.2}
\]

where, for `i,j in {0,1}`,

\[
 N_S(x_{ij})\supseteq\{a_i,b_j,c_0,c_1,s\}.        \tag{2.3}
\]

### Proposition 2.1 (strict surplus does not force the triple)

The shore (2.2)--(2.3) satisfies

\[
 |N_D(Y)-Y|+|N_S(Y)|\ge8                           \tag{2.4}
\]

for every nonempty proper \(Y\subset D\).  Every two of `A,B,C` have
disjoint carriers, but the three demands do not have simultaneous
disjoint carriers.

#### Proof

For a singleton, the two terms in (2.4) have orders three and five.  Any
two rows in (2.3) together contain at least six boundary labels, and any
three contain all seven.  Since `D=K_4`, this proves (2.4) for subsets of
orders one, two, and three.

An `A`-carrier has at least two vertices: the `a_0`- and `a_1`-portal
sets are disjoint.  The same is true of a `B`-carrier.  Disjoint `A`- and
`B`-carriers therefore consume all four shore vertices, leaving no
nonempty `C`-carrier.  On the other hand, the edges

For the `A,B` packet, the two diagonal edges

\[
 \{x_{00},x_{11}\},\qquad \{x_{01},x_{10}\}
\]

are disjoint carriers (indeed each diagonal meets both portal classes of
both demands), and one may assign the first to `A` and the second to `B`.
For the `A,C` packet use the edge `x_{00}x_{10}` and the singleton
`x_{01}`; for the `B,C` packet use `x_{00}x_{01}` and the singleton
`x_{10}`.  Hence every two-demand subfamily is linkable.
\(\square\)

For complete clarity, one literal labelling of (2.3), in the numerical
order `a_0,a_1,b_0,b_1,c_0,c_1,s=0,...,6`, is

\[
 02456,\qquad03456,\qquad12456,\qquad13456,         \tag{2.5}
\]

in the order `x_00,x_01,x_10,x_11`.

The first and second packets in a capture--capture comparison can be
chosen as `A|C` and `B|C`.  Thus (2.5) also refutes the claim that capture
multiplicity and strict surplus alone close the capture--capture branch.

## 3. The boundary dichotomy already present in the audited funnel

Let `J=G[S]` and `Q=overline J`.  Assume that `Q` is one of the seven
fully-positive matching rows in Theorem 4.1 of
`hadwiger_equality_seven_edge_packet_funnel.md`, and orient its displayed
matching as the three pairs in (2.1).  The orientation is arbitrary: the
three pairs may be permuted and the ends of each pair may be interchanged.

The already audited ten-type list has the following much smaller
orientation consequence.

### Lemma 3.1 (one ordinary row and one exceptional row)

Exactly one of the following holds.

1. `s` has a boundary neighbour in `C`.
2. After interchanging `A,B` and/or the ends within them, the missing
   boundary edges are exactly
   \[
   \begin{split}
   E(Q)=\{&a_0a_1,b_0b_1,c_0c_1,sc_0,sc_1,\\
           &a_0c_0,b_0c_0\}.                     \tag{3.1}
   \end{split}
   \]

#### Certification

This is not a new refinement of the 31-type atlas.  It merely normalizes
the 336 orientations of the seven matching rows already certified there.
The circuit automorphisms are the endpoint flips in `A,B,C` and the
interchange of `A,B`.  The ordinary orientations all satisfy item 1; the
orientations failing item 1 form the single orbit (3.1).  The executable
replay is part of
`atomic_three_packet_core_completion_verify.py`: its exceptional branch
asserts the two extra missing incidences at `c_0`, and all 336 rows pass.

## 4. Hand closure of the `K_4` circuit

The vertices in (2.2) may be replaced by four pairwise disjoint,
pairwise adjacent connected pieces `X_ij`, provided each piece has all
the portal contacts in (2.3).  Let `R` be the opposite full shore behind
the same adhesion.

### Theorem 4.1 (rank-two core completion)

Under the hypotheses of Section 3, the four pieces `X_ij` and the full
shore `R` force a `K_7` minor.

#### Proof: ordinary row

Choose `c_0` adjacent to `s`, and write `c_1` for the other member of
`C`.  The seven bags are

\[
\begin{array}{lll}
 X_{00}\cup\{a_0,c_1\},&X_{01}\cup\{b_1\},
     &X_{10}\cup\{b_0\},\\
 X_{11}\cup\{a_1\},&R,&\{c_0\},\quad\{s\}.
\end{array}                                                       \tag{4.1}
\]

The first four bags are connected and pairwise adjacent through their
core pieces.  Each contains a distinct root of \(A\cup B\), and is
therefore adjacent to `R`.  Every core piece contacts `c_0` and `s`, so
the last two singleton bags see the first four.  They see one another by
the edge `c_0s`, and fullness supplies all adjacencies from `R` to the
two singletons.  Thus (4.1) is a `K_7` model.

#### Proof: exceptional row

Use the labels in (3.1).  The seven bags are

\[
 \{a_0\},\quad\{b_0\},\quad\{c_1\},\quad X_{00},
 \quad\{a_1,s\},\quad X_{10}\cup X_{01},
 \quad R\cup\{c_0\}.                              \tag{4.2}
\]

All bags are connected: `a_1s` is not a missing edge, the two core
pieces in the sixth bag are adjacent, and fullness connects `c_0` to
`R`.  The only missing boundary edges are those displayed in (3.1).
Together with the portal rows

\[
\begin{array}{c|ccccc}
X_{00}&a_0&b_0&c_0&c_1&s\\
X_{10}&a_1&b_0&c_0&c_1&s\\
X_{01}&a_0&b_1&c_0&c_1&s,
\end{array}
\]

they verify every pair in (4.2): `a_0,b_0,c_1` form a triangle; each
contacts `X_00` or one of `X_10,X_01` as indicated; `s` contacts every
core piece; and every apparent missing incidence with `c_0` is repaired
through the full shore `R`.  Hence (4.2) is again a `K_7` model.

The two cases of Lemma 3.1 exhaust every orientation, proving the theorem.
\(\square\)

This result uses no operation state.  The operation-critical comparison is
needed only after this entire rank-two core has been excluded.

## 5. Uniform rooted Hall completion

The order-five and order-six solver outputs have an even cleaner common
reason for failing in the actual gate.

### Theorem 5.1 (rooted Hall completion)

Let \(|S|=t\), let `s,r in S` be adjacent, and let `R` be a connected
full `S`-shore.  Suppose there are \(t-2\) disjoint pairwise adjacent
connected pieces

\[
                         U_1,\ldots,U_{t-2},                     \tag{5.1}
\]

disjoint from \(R\cup S\), such that

1. every `U_i` has an `s`-portal; and
2. the portal incidence family on \(S-\{s,r\}\) satisfies Hall's
   condition:
   \[
   \left|\bigcup_{i\in I}
       \bigl(N_S(U_i)\cap(S-\{s,r\})\bigr)\right|\ge |I|
   \quad\text{for every }I\subseteq\{1,\ldots,t-2\}.             \tag{5.2}
   \]

Then `G` has a `K_t` minor.

#### Proof

Hall's theorem gives distinct labels

\[
 t_i\in N_S(U_i)\cap(S-\{s,r\})
 \quad(1\le i\le t-2).                              \tag{5.3}
\]

Because both sides of this matching have order `t-2`, these labels are
exactly \(S-\{s,r\}\).  Use the `t-2` bags

\[
                         U_i\cup\{t_i\}\quad(1\le i\le t-2),   \tag{5.4}
\]

together with `R` and `\{s,r\}`.  The first `t-2` bags are connected
and pairwise adjacent.  Their distinct roots make each adjacent to the full
shore `R`; their `s`-portals make each adjacent to the connected boundary
bag `\{s,r\}`.  Fullness supplies the last adjacency.  These are `t`
clique bags. \(\square\)

This is the parameter-uniform rooted-model principle extracted from the
small packet circuits.  It depends only on a protected clique frame and a
portal Hall condition, not on the seven-edge atlas.

### Corollary 5.2 (the `HC_7` five-core form)

For `t=7`, five protected pairwise adjacent pieces, all seeing `s`,
complete to a `K_7` whenever their portal rows into the other five
boundary labels have an SDR.

## 6. The exact small-order circuits

Again write the six demand endpoints as `0,...,5` and the singleton as
`6`.

### 6.0 Order two

There is one smaller static exception to the proposed three-packet
theorem: two adjacent shore vertices, each adjacent to all seven boundary
labels.  They realize every two-demand packet but cannot contain three
disjoint nonempty carriers.

This circuit also closes before operation states.  More generally, if
`x,y` are adjacent full pieces and `J-r` contains a `K_4` model
`L_1,...,L_4`, then

\[
 \{x\},\quad\{y\},\quad L_1,\ldots,L_4,
 \quad R\cup\{r\}                                  \tag{6.1}
\]

is a `K_7` model.  The last bag is connected by fullness; the first two
pieces see it through `r`; and the four boundary bags see it through `R`.

For the seven fully-positive atlas rows, suitable choices are:

\[
\begin{array}{c|c|c}
\text{row}&r&K_4\text{ bags in }J-r\\ \hline
\texttt{F[JG?}&0&1\mid3\mid4\mid6\\
\texttt{FhoW?}&0&1\mid3\mid6\mid245\\
\texttt{FHHGg}&0&1\mid3\mid4\mid256\\
\texttt{FHOgg}&1&0\mid2\mid4\mid6\\
\texttt{FIS`G}&0&3\mid5\mid16\mid24\\
\texttt{Fpq?G}&0&1\mid2\mid5\mid34\\
\texttt{FhCKG}&0&1\mid3\mid5\mid26.
\end{array}                                                       \tag{6.2}
\]

Every multi-vertex entry induces a connected bag, and the four entries
in each row are pairwise adjacent.

### 6.1 Order five

The solver's shore is `K_5`, with portal rows

\[
 0356,\quad0246,\quad1256,\quad1346,\quad1246.     \tag{6.3}
\]

All five vertices are `6`-portals.  For every possible omitted endpoint
`r`, the following row gives distinct representatives for the five
vertices; entries are in vertex order:

\[
\begin{array}{c|c}
r&\text{representatives}\\ \hline
0&3,2,5,1,4\\
1&0,2,5,3,4\\
2&0,4,5,3,1\\
3&0,2,5,1,4\\
4&0,2,5,3,1\\
5&0,2,1,3,4
\end{array}                                                       \tag{6.4}
\]

Choose any endpoint `r` adjacent to `6`.  Such an endpoint exists in
every seven-edge boundary containing the three matching edges: only four
additional missing edges remain, so `6` cannot miss all six endpoints.
Apply Theorem 5.1 to the five singleton pieces of the `K_5`.

### 6.2 Order six

The shore is `K_6-{03,14}` and its portal rows are

\[
 0246,\quad1346,\quad026,\quad1356,\quad0256,
 \quad136.                                         \tag{6.5}
\]

It has the `K_5` model

\[
 \{0,1\},\quad\{2\},\quad\{3\},\quad\{4\},\quad\{5\}.       \tag{6.6}
\]

Every bag in (6.6) has a `6`-portal.  For the same six choices of omitted
endpoint, SDRs into the bags in the displayed order are

\[
\begin{array}{c|c}
r&\text{representatives}\\ \hline
0&4,2,1,5,3\\
1&4,0,5,2,3\\
2&4,0,1,5,3\\
3&4,0,5,2,1\\
4&0,2,1,5,3\\
5&4,0,1,2,3.
\end{array}                                                       \tag{6.7}
\]

Theorem 5.1 again gives `K_7`.

### Theorem 6.1 (the displayed small packet circuits are excluded)

None of the explicit strict-surplus, pairwise-but-not-triple circuits of
orders two, four, five, and six displayed in this note survives behind a
seven-edge fully-positive matching boundary with an opposite full shore.

Order two is (6.1)--(6.2).  The order-four case is Theorem 4.1.  The
order-five and order-six cases are Theorem 5.1 with the two SDR tables.
\(\square\)

The satisfiability run also proves that no order-three circuit exists.
It does **not** enumerate all nonisomorphic circuits at orders four through
six; its `SAT` output supplies one witness at each order.  Consequently
Theorem 6.1 must not be read as a complete small-order classification.

## 7. Verification and exact remaining gap

Three independent executable layers are provided.

* `atomic_three_packet_z3.py` encodes relative surplus and all path masks.
  It reports `UNSAT` at order three and the explicit circuits at orders
  two, four, five, and six; it proves that order three is impossible.
* `atomic_three_packet_circuit_verify.py` independently enumerates every
  connected carrier and every shore subset, replaying strict surplus,
  all pair packets, and failure of the triple for the four displayed
  circuits.
* `atomic_three_packet_core_completion_verify.py` constructs the bags in
  Sections 4--6 for all 48 orientations of each of the seven audited
  matching rows.  It checks nonempty disjoint connected bags and all 21
  adjacencies, printing

  ```text
  explicit core-completion certificates {2: 336, 4: 336, 5: 336, 6: 336}
  ```

The theorem is a genuine family closure, but not the whole
capture--capture or web--web branch.  A remaining atomic packet obstruction
must avoid both the rank-two completion of Theorem 4.1 and the rooted Hall
completion of Theorem 5.1.  It may still have order four, five, or six in a
portal pattern not represented by the displayed solver witness; no
small-order classification is claimed.  Only after these static rooted
cores are absent can boundary-faithful operation states add information
not already supplied by the portal geometry.
