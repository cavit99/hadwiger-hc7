# Compression of repeated labelled first-hit exposure

**Status:** written proof; separate internal audit GREEN in
[`hc7_labelled_first_hit_exposure_compression_audit.md`](hc7_labelled_first_hit_exposure_compression_audit.md).
This is a strengthening of the
five-label exposure-collision alternative.  It reduces every repeated
unused-label exposure either to two independent contact edges, an actual
order-seven separation, or a connected source component on at most four
literal vertices.  It does not preserve a selected boundary colouring and
does not prove `HC_7`.

## 1. First-hit setting

Let `H` be a finite seven-connected graph.  Let `P` be a set of at least
five source vertices, and let

\[
                         T_1,\ldots,T_5
\]

be nonempty, pairwise disjoint vertex sets disjoint from `P`.  Put
`T=\bigcup_iT_i`.  Let `F` be a further literal vertex set, disjoint from
`P\cup T`, with

\[
                              |F|\le 3.                 \tag{1.1}
\]

Use the terminal-sink network in which `H-(T\cup F)` is the nonterminal
part and each vertex of `T` has a separate directed sink copy.  Thus a
path to `T_i` meets `T` only in its last vertex.  Suppose that there is no
family of five pairwise vertex-disjoint such paths from distinct members
of `P`, one ending in each `T_i`.

The Rado--gammoid theorem and directed Menger theorem then give:

* a nonempty set `I\subseteq[5]` of selected labels;
* a directed separator `Z`, with

  \[
                              |Z|\le |I|-1;             \tag{1.2}
  \]

* its injective literal image `\overline Z`; and
* a component `C` containing a surviving source in the graph obtained
  from `H-(T\cup F)` by deleting the nonterminal members of `Z`.

For `j\notin I`, define the literal exposure set

\[
                         E_j=N_H(C)\cap T_j.            \tag{1.3}
\]

The first-hit construction gives

\[
 N_H(C)\subseteq
 \overline Z\ \cup\ (N_H(C)\cap F)\ \cup
 \bigcup_{j\notin I}E_j.                              \tag{1.4}
\]

Moreover, some selected terminal outside `\overline Z` lies outside `C`
and outside the right-hand side of (1.4).  Consequently, every separator
constructed below has a nonempty opposite side.

## 2. Exposure-compression theorem

For `j\notin I`, let `B_j` be the bipartite graph with parts `C` and
`E_j` whose edges are the edges of `H` between these two sets.

### Theorem 2.1 (matching, exact separation, or atomic source component)

In the setting above, at least one of the following holds.

1. There is a nonempty connected set `D` whose full neighbourhood
   `N_H(D)` has order seven and is the boundary of an actual separation
   with two nonempty open sides.
2. For some `j\notin I`, the graph `B_j` contains a matching of order two.
   Equivalently, there are two independent literal exposure edges

   \[
                        c_1t_1,\ c_2t_2,
   \qquad c_1\ne c_2\in C,\quad t_1\ne t_2\in E_j.     \tag{2.1}
   \]
3. The component `C` has order at most the number of indices `j\notin I`
   for which `|E_j|\ge2`, and hence

   \[
                              |C|\le4.                 \tag{2.2}
   \]

   In addition, every vertex `c\in C` can be assigned an index
   `j(c)\notin I` such that `|E_{j(c)}|\ge2` and every edge of `B_{j(c)}`
   is incident with `c`.  In particular, `c` has at least two neighbours
   in the single named terminal class `T_{j(c)}`.

Outcome 3 is called the **atomic exposure outcome**.  The word *atomic*
only refers to the returned literal component `C`; it does not bound the
order of any model branch set containing `C`.

#### Proof

Assume outcome 2 fails.  Partition the unselected labels into

\[
 \begin{aligned}
 R&=\{j\notin I:|E_j|\ge2\},\\
 S&=\{j\notin I:|E_j|=1\},
 \end{aligned}                                         \tag{2.3}
\]

and ignore the labels with empty exposure.  For every `j\in R`, the
bipartite graph `B_j` has matching number one.  By Konig's theorem it has
a one-vertex cover.  Such a cover cannot be a vertex of `E_j`: at least
two distinct vertices of `E_j` are incident with edges, because they
belong to `N_H(C)`.  Hence there is a vertex `c_j\in C` incident with
every edge of `B_j`.  In particular,

\[
                         E_j\subseteq N_H(c_j).         \tag{2.4}
\]

Put

\[
                         X=\{c_j:j\in R\}\subseteq C.  \tag{2.5}
\]

Repeated choices may coincide, so `|X|\le |R|`.

Suppose first that `C-X` is nonempty, and let `D` be any component of
`H[C-X]`.  No vertex of `D` is adjacent to an exposed terminal in a class
indexed by `R`, because all such edges are incident with the corresponding
member of `X`.  Distinct components of `C-X` have no edge between them.
Together with (1.4), this gives

\[
 N_H(D)\subseteq
 \overline Z\ \cup\ (N_H(C)\cap F)\ \cup X\ \cup
 \bigcup_{j\in S}E_j.                                 \tag{2.6}
\]

The right-hand side has order at most

\[
 \begin{aligned}
 |Z|+|F|+|X|+|S|
 &\le (|I|-1)+3+|R|+|S|\\
 &\le (|I|-1)+3+(5-|I|)=7.                            \tag{2.7}
 \end{aligned}
\]

It is disjoint from `D`.  The selected terminal outside the exposure set
described after (1.4) also lies outside this displayed set, so the opposite
open side is nonempty.  Seven-connectivity now implies
`|N_H(D)|\ge7`.  Equations (2.6)--(2.7) force equality throughout:
the displayed set is exactly `N_H(D)` and has order seven.  This is
outcome 1.

It remains to consider `C-X=\varnothing`.  Then `C=X`, so

\[
                  |C|=|X|\le |R|\le5-|I|\le4,         \tag{2.8}
\]

because `I` is nonempty.  Every `c\in C=X` equals `c_j` for at least one
`j\in R`; choose one such index as `j(c)`.  Equations (2.3)--(2.4) show
that `c` is incident with all exposure edges to the at least two vertices
of `E_{j(c)}`.  This is outcome 3.  \(\square\)

### Remarks on sharpness

1. The labels assigned to different vertices in outcome 3 need not be
   distinct.  What is forced is a surjection from the repeated exposed
   labels used to define `X` onto the vertices of `C`.
2. The two edges in outcome 2 are vertex-disjoint.  The two edges supplied
   at one vertex in outcome 3 share that vertex; this distinction matters
   in later linkage arguments.
3. No colouring information is used in the proof.  Thus outcome 1 is a
   bare order-seven separation, not yet a colour-gluing conclusion.

## 3. Specialization to a spanning labelled near-complete model

The preceding alternatives have a direct deletion-critical consequence.

### Proposition 3.1 (model-preserving critical edge pairs)

Assume, in addition, that:

1. `G=H` is not six-colourable and every proper minor of `G` is
   six-colourable;
2. `V(G)` is partitioned into the connected branch sets of a spanning
   labelled `K_7`-minus-one-edge model;
3. `C` is contained in one branch set `D`; and
4. each terminal class `T_j` considered below is contained in a different
   branch set `U_j`.

Then the following statements hold.

* In outcome 2 of Theorem 2.1, the two independent exposure edges in
  (2.1) are both model-preserving deletion-critical edges: deleting either
  one leaves the same spanning labelled model, because the other still
  realizes the `D`--`U_j` adjacency.
* In outcome 3, for every `c\in C` choose distinct

  \[
                         t_1,t_2\in E_{j(c)}.
  \]

  The incident pair `ct_1,ct_2` has the same property: deleting either
  edge leaves the other as the old `D`--`U_{j(c)}` model adjacency.

For every edge `e` obtained in either bullet,

\[
                         \chi(G-e)=\chi(G/e)=6.         \tag{3.1}
\]

Furthermore, in every six-colouring of `G-e`, the ends of `e` have one
common colour `alpha` and lie in one `alpha`--`beta` component for each of
the other five colours `beta`.

#### Proof

Every displayed edge joins `D` to a different branch set `U_j`.  The
companion edge remains after its deletion, while the branch sets and all
their internal edges are unchanged.  Hence the same spanning labelled
near-complete model survives either single deletion.

Both `G-e` and `G/e` are proper minors and therefore are six-colourable.
Neither is five-colourable.  A five-colouring of `G-e` would extend to a
six-colouring of `G` after recolouring one end of `e` with a new sixth
colour.  A five-colouring of `G/e` expands to the ends of `e`, after which
the same recolouring gives a six-colouring of `G`.  This proves (3.1).

In a six-colouring of `G-e`, the ends of `e` must have the same colour,
or the deleted edge could be restored.  If their `alpha`--`beta`
components were distinct for some other colour `beta`, interchanging the
two colours on the component containing one end would give the ends
different colours, again allowing `e` to be restored.  This proves the
Kempe-component assertion.  \(\square\)

## 4. Exact contribution and remaining gap

The theorem replaces an arbitrarily large repeated exposure by one of two
finite local edge configurations unless a literal order-seven separator
already exists:

* two independent edges between the source component and one named branch
  set; or
* a connected source component on at most four vertices, every vertex of
  which supports an incident pair of such edges into one named branch set.

This is an unbounded host-level compression, but not the desired dynamic
exchange theorem.  A selected proper-minor colouring response still has to
turn one of these persistent edge pairs into an increase of the labelled
first-hit rank, a smaller response-preserving kernel, an explicit
`K_7`-minor model, or an order-seven separation carrying a boundary
partition extendable through both closed shores.

In particular, the theorem does not identify a palette colour with a model
label and does not claim that the Kempe components obtained in Proposition
3.1 are mutually disjoint.

## 5. Dependency

The only non-elementary ingredient in the proof is the Rado--gammoid and
Menger reduction recorded in
[`hc7_labelled_first_hit_rado_reduction.md`](hc7_labelled_first_hit_rado_reduction.md).
The one-vertex-cover step is the matching form of Konig's theorem.
