# Every independent trace does not force a rooted clique model

## 1. The static assertion is false

Let \(I\) be the icosahedral graph in its two-cap presentation, with
vertices

\[
 T,S,a_0,\ldots,a_4,b_0,\ldots,b_4 .
\]

Subscripts are modulo five.  The edges are

\[
 Ta_i,\quad Sb_i,\quad a_i a_{i+1},\quad b_i b_{i+1},
 \quad a_i b_i,\quad a_i b_{i-1}.
\tag{1.1}
\]

Add the edge \(TS\), call the resulting graph \(H\), and distinguish

\[
                         N=\{T,S,a_0,a_1,b_0\}.       \tag{1.2}
\]

The graph has the \(K_5\)-model

\[
 \{T\},\quad \{S\},\quad \{a_0,b_0\},\quad
 \{a_1,b_1\},\quad \{a_3,a_4,b_2\}.                 \tag{1.3}
\]

Nevertheless it has no \(N\)-rooted \(K_5\)-model.  The exhaustive
certificate

[verify_icosahedron_haven_cleaning_counterexample.py](verify_icosahedron_haven_cleaning_counterexample.py)

checks all \(6^7\) assignments of the seven vertices outside \(N\) to
the five prescribed rooted bags or to the unused class.  This is a
complete enumeration: a rooted branch set already contains its one
prescribed root, and every other vertex is assigned to exactly one bag
or is unused.

The new point is that the example realizes **every independent trace**.

### Theorem 1.1 (boundary universality)

Let \({\cal P}_5(H,N)\) be the equality partitions of \(N\) induced by
proper five-colourings of \(H\).  Then

\[
 {\cal P}_5(H,N)
 =
 \{\hbox{all proper equality partitions of }H[N]\}.          \tag{1.4}
\]

In particular, for every nonempty independent set \(J\subseteq N\),
some proper five-colouring of \(H\) has a colour whose trace on \(N\)
is exactly \(J\).

#### Proof

In the order

\[
             T,S,a_0,a_1,a_2,a_3,a_4,b_0,b_1,b_2,b_3,b_4,
\tag{1.5}
\]

the following six rows are proper five-colourings of \(H\):

\[
\begin{array}{c|c}
\text{partition on }(T,S,a_0,a_1,b_0)&\text{colour word on (1.5)}
\\ \hline
01120&011212303042\\
01123&011212330302\\
01210&012121303024\\
01213&012121330304\\
01230&012312102034\\
01234&012312140303
\end{array}                                                   \tag{1.6}
\]

Direct comparison with (1.1) verifies properness.

The only nonedges in \(H[N]\) are

\[
                    Sa_0,\qquad Sa_1,\qquad Tb_0.             \tag{1.7}
\]

As \(a_0a_1\) is an edge, a proper equality partition of \(H[N]\)
is one of exactly the six partitions in the first column of (1.6):
the rainbow partition; one of the three permitted pairs; or one of
the two permitted disjoint pairs.  Thus (1.6) proves (1.4).

The nonempty independent sets of \(H[N]\) are the five singletons and
the three pairs in (1.7).  The rainbow row realizes every singleton as
one of its colour traces, and a single-pair row realizes each pair
exactly.  \(\square\)

Combining Theorem 1.1 with (1.3) and the rooted-model certificate gives
the promised counterexample:

\[
\begin{array}{c}
K_5\text{-model}+\text{ every nonempty independent }N\text{-trace}
\\[2mm]
\centernot\Longrightarrow
N\text{-rooted }K_5\text{-model}.
\end{array}                                                   \tag{1.8}
\]

Thus the all-trace property is still only a collection of one-colour
projections of the full boundary extension relation.

## 2. The minimal one-step axiom present in a critical apex

The counterexample points to a particularly small additional axiom.  It
does not ask for a rooted model, a linkage, or a separator theorem.

For an \(N\)-boundaried graph \(L\), write
\({\cal P}_r(L,N)\) for the equality partitions of \(N\) induced by
proper \(r\)-colourings of \(L\).

### Lemma 2.1 (internal-edge transition novelty)

Suppose \(G\) is not \(r\)-colourable and every proper minor of \(G\)
is \(r\)-colourable.  Fix \(v\in V(G)\), put \(H=G-v\), and
\(N=N_G(v)\).  For every edge \(e=xy\in E(H)\), there is a partition
\(\pi_e\) such that

\[
 \pi_e\in {\cal P}_r(H-e,N)\setminus{\cal P}_r(H,N),\qquad
 |\pi_e|\le r-1.                                             \tag{2.1}
\]

It is induced by a colouring of \(H-e\) in which \(x,y\) have the same
colour.

#### Proof

Colour the proper minor \(G-e\) with \(r\) colours, and call the
colouring \(d\).  Restoring \(e\) would colour \(G\) unless
\(d(x)=d(y)\).  Also \(d(v)\) is absent from \(N\), because every
edge from \(v\) to \(N\) remains.  Hence the equality partition
\(\pi_e=\Pi_N(d|_{H-e})\) has at most \(r-1\) blocks.

If \(\pi_e\) belonged to \({\cal P}_r(H,N)\), take a colouring of
\(H\) inducing that partition and permute its palette to agree with
\(d\) on \(N\).  The colour \(d(v)\) is absent from this boundary, so
assigning it to \(v\) would give an \(r\)-colouring of \(G\), a
contradiction.  This proves (2.1).  \(\square\)

This is the minimal boundary-state content of one internal edge
deletion: the operation must create at least one genuinely new
\((r-1)\)-block boundary state.  It is strictly stronger than saying
that every independent set occurs as one colour block.

### Proposition 2.2 (the icosahedral obstruction fails novelty maximally)

For every edge \(e\in E(H)\) having both ends outside \(N\),

\[
                         {\cal P}_5(H-e,N)
                         ={\cal P}_5(H,N).             \tag{2.2}
\]

In particular (2.1) fails for \(e=a_2a_3\).

#### Proof

Deleting such an edge does not change \(H[N]\).  Therefore every
partition in \({\cal P}_5(H-e,N)\) is a proper equality partition of
\(H[N]\).  Boundary universality (1.4) says that every such partition
already lies in \({\cal P}_5(H,N)\).  The reverse inclusion is
automatic because deleting an edge preserves every colouring.
\(\square\)

Thus one-step transition novelty excludes the static counterexample
without assuming the desired rooted model.  It is also genuinely
forced, edge by edge, in the proper-minor-minimal apex setting.

## 3. Relation to global saturation

The example also fails global saturation: some five-colourings of
\(H\) use fewer than five colours on \(N\).  In a non-\(r\)-colourable
apex \(G=H+vN\), every \(r\)-colouring of \(H\) must use all \(r\)
colours on \(N\).  Hence global saturation already excludes this
particular graph.

That observation does not make the all-trace assertion useful by
itself.  Global saturation plus arbitrary independent traces is a
static rooted-Hadwiger type hypothesis.  Lemma 2.1 records the extra
operation-sensitive datum actually available in a minor-minimal
counterexample.  Across a separation, its sharp usable form is the
two-shore transition theorem in
hadwiger_all_trace_transition_gate.md: two opposite unpinned
transitions in the same exact trace state force every free boundary
colour to have capacity on both shores, while a private free trace
colour makes that impossible.
