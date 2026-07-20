# The two--three centre-component configuration closes

**Status:** written proof; separate internal audit **GREEN** in
[`hc7_order8_two_three_centre_component_closure_audit.md`](hc7_order8_two_three_centre_component_closure_audit.md).
This is an unbounded host-level closure inside the two-component
order-eight interface.  It does not prove `HC_7`.

## 1. Statement

### Theorem 1.1

Let `G` be a seven-connected, 7-contraction-critical graph.  Let `S` be
an eight-vertex set such that `G-S` has distinct connected components
`C,D`, each adjacent to every vertex of `S`.  Choose `p in S` and edges

\[
                         pv\in E(G),\quad v\in C,
             \qquad      pw\in E(G),\quad w\in D.       \tag{1.1}
\]

Suppose `C-v` has exactly two components and `D-w` has exactly three.
Then at least one of the following holds.

1. A nonempty connected set `R` has

   \[
                              |N_G(R)|=7,              \tag{1.2}
   \]

   and its full neighbourhood is the boundary of an actual separation
   with two nonempty open sides.
2. `G` contains an explicit `K_7`-minor model.

The orders and internal structures of the five components are arbitrary.

## 2. Preliminary reductions

Write the components as

\[
                 C-v=A_1\mathbin{\dot\cup}A_2,
       \qquad    D-w=B_1\mathbin{\dot\cup}B_2
                         \mathbin{\dot\cup}B_3.        \tag{2.1}
\]

Every component in (2.1) is adjacent to its deleted centre.  If one of
them, say `K`, misses at least two vertices of `S`, then

\[
             N_G(K)\subseteq S\cup\{v\}
       \quad\hbox{or}\quad
             N_G(K)\subseteq S\cup\{w\},              \tag{2.2}
\]

and hence `|N_G(K)|<=7`.  The other open component witnesses that this is
the boundary of a genuine separation.  Seven-connectivity forces equality,
which is outcome 1.  We may therefore assume throughout the rest of the
proof that every component in (2.1) is adjacent to all but at most one
vertex of `S`.

We use twice the following elementary facts.

- If a connected graph contains disjoint nonempty connected subgraphs
  `P_0,Q_0`, its vertex set can be partitioned into adjacent connected sets
  `P,Q` with `P_0 subseteq P` and `Q_0 subseteq Q`: contract `P_0,Q_0`,
  take a spanning tree, and delete an edge on the path between their
  images.
- For `m` connected subgraphs, each missing at most one vertex of a set of
  order at least `m+1`, one can choose distinct adjacent representatives
  with no **reciprocal defect pair**.  Explicitly, representatives `x_i`
  can be chosen so that no `i ne j` satisfy both

  \[
       K_i\not\sim x_j\quad\hbox{and}\quad K_j\not\sim x_i.       \tag{2.3}
  \]

  This is the representative lemma in
  [`hc7_order8_center_component_clique_decoder.md`](hc7_order8_center_component_clique_decoder.md).

## 3. A repeated centre-neighbour closes

Suppose first that one component, say `A_1`, contains two distinct
neighbours `a,b` of `v`.  Let `M` be the union of the boundary vertices
actually missed by the other four components in (2.1), and put

\[
                         Y=S-(M\cup\{p\}).             \tag{3.1}
\]

Since `|M|<=4`, the set `Y` has order at least three, and every one of the
other four components is adjacent to every vertex of `Y`.

Apply set-Menger in `G[A_1\cup Y]` between `{a,b}` and `Y`.  If there are
not two vertex-disjoint paths, a separator `Z` of order at most one leaves
one of `a,b` outside `Z`.  The component `R` containing that surviving
source and separated from `Y` lies in `A_1` and satisfies

\[
                N_G(R)\subseteq \{v\}\cup M\cup\{p\}\cup Z,
                \qquad |N_G(R)|\le7.                  \tag{3.2}
\]

The open component `D` lies outside `R\cup N_G(R)`, so seven-connectivity
makes (3.2) an actual order-seven separation.  This is outcome 1.

Otherwise the two paths use both sources and have distinct ends `x,y in
Y`.  Truncate them at their first vertices of `Y`, delete `x,y` from the
paths, and use the connected-bipartition fact above to obtain an adjacent
connected partition

\[
                              A_1=P\mathbin{\dot\cup}Q              \tag{3.3}
\]

such that `P\cup{x}` and `Q\cup{y}` are connected, `a in P`, and
`b in Q`.

The set `S-{p,x,y}` has order five.  Apply the representative lemma to
the other four components and obtain distinct vertices `z_K` there, with
`K` adjacent to `z_K` and with no reciprocal defect pair.  The following
seven sets are pairwise disjoint and connected:

\[
 \{v,p,w\},\quad P\cup\{x\},\quad Q\cup\{y\},
 \quad K\cup\{z_K\}
 \quad(K\in\{A_2,B_1,B_2,B_3\}).                    \tag{3.4}
\]

The first set is connected through `vp,pw`; it meets `P,Q` through
`va,vb` and every other component through `v` or `w`.  The two split sets
are adjacent by (3.3).  Each of the other four components meets both `x`
and `y`, and (2.3) supplies all adjacencies among their augmented bags.
Thus (3.4) is a `K_7`-minor model.

The same argument applies if the repeated centre-neighbour lies in any
other component.  Hence we may assume from now on that every component in
(2.1) contains exactly one neighbour of its centre.

## 4. The boundary allocation in the unique-neighbour case

The two neighbours of `v` in `C` are independent, and the three neighbours
of `w` in `D` are independent.  Dirac's neighbourhood-independence
inequality for a 7-contraction-critical graph gives

\[
 \begin{aligned}
  2&\le d_G(v)-5=|N_G(v)\cap S|-3,\\
  3&\le d_G(w)-5=|N_G(w)\cap S|-2.
 \end{aligned}                                      \tag{4.1}
\]

Consequently each centre has at least five neighbours in `S`.  Put

\[
 U=S-\{p\},\qquad
 V=(N_G(v)\cap S)-\{p\},\qquad
 W=(N_G(w)\cap S)-\{p\},\qquad
 P=N_G(p)\cap U.                                    \tag{4.2}
\]

Thus `|U|=7` and `|V|,|W|>=4`.  For each of the five components, let its
**defect** be its possible unique missed vertex of `S`, using a symbol
`perp` when it misses none.

If some

\[
                          q\in V\cup W\cup P          \tag{4.3}
\]

is missed by none of the five components, apply the paired-centre
component decoder with connected central set `G[{v,p,w}]`, the five
components, and the singleton clique `{q}`.  It gives a `K_7`-minor model.

Assume no such `q` exists and put

\[
                             K=V\cup W\cup P.          \tag{4.4}
\]

Every member of `K` is then one of the five defects.  Hence

\[
                              4\le |K|\le5.            \tag{4.5}
\]

We next choose one distinct representative `x_H in U` for each component
`H` in (2.1), satisfying all of the following:

1. `x_{A_i} in W`;
2. if `B_j` misses `p`, then `x_{B_j} in V\cup P`;
3. every component meets its representative; and
4. no two components form a reciprocal defect pair.

These conditions are exactly what is needed for the two root bags
`{v,p}` and `{w}`.  We prove the representatives exist by the two cases in
(4.5).

### Case 1: `|K|=5`

The five defects are precisely the five distinct vertices of `K`; in
particular, every `B_j` meets `p`.  Choose two distinct representatives for
`A_1,A_2` in `W`, avoiding both of their defects.  This is possible because
`|W|>=4`, and it also prevents a reciprocal pair between them.

Three vertices of `K` remain unused.  Choose a representative for `B_1`
among them, avoiding its own defect and, if its defect is one of the two
chosen `A`-representatives, the one additional value which would complete
that reciprocal pair.  At most two of the three values are forbidden.
Assign the two vertices of `U-K` to `B_2,B_3`.  All defects lie in `K`, so
these last two assignments create neither an own defect nor a reciprocal
pair.

### Case 2: `|K|=4`

Now `V=W=K`.  First suppose no `B_j` misses `p`.  Choose the two
`A`-representatives distinctly in `K`, avoiding both `A`-defects.  Assign
the three `B`-representatives bijectively to the three vertices of `U-K`.
Because the five defects cover all four vertices of `K`, at most one defect
lies outside `K`; if it exists, the four defects in `K` are pairwise
distinct.  Thus at most one incidence in this three-by-three assignment is
forbidden, either by an own defect or by the unique possible reciprocal
pair with an `A`-component.  Choose the bijection avoiding that incidence.

Finally suppose some `B_0` misses `p`.  It is the unique such `B`-component:
otherwise the remaining three defect slots could not cover the four
vertices of `K`.  The other four defects are exactly the four distinct
vertices of `K`.  Choose the two `A`-representatives distinctly in `K`
while avoiding both `A`-defects, give `B_0` either remaining vertex of
`K`, and give the other two `B`-components distinct vertices of `U-K`.
No reciprocal pair can involve `B_0`, whose defect is `p`, or an
outside-`K` representative, while the `A`-representatives avoid both
`A`-defects.

This completes the allocation in every case.

## 5. The final seven branch sets

For each component `H` in (2.1), put

\[
                              M_H=H\cup\{x_H\}.       \tag{5.1}
\]

The seven branch sets are

\[
                 \{v,p\},\qquad \{w\},\qquad
                 M_{A_1},M_{A_2},M_{B_1},M_{B_2},M_{B_3}.          \tag{5.2}
\]

The two root bags are adjacent through `pw`.  The bag `{v,p}` meets each
`A_i` through `v`; it meets `M_{B_j}` through `p` when `B_j` meets `p`,
and otherwise through the representative in `V\cup P`.  The bag `{w}`
meets each `B_j` through `w` and each `M_{A_i}` through its representative
in `W`.  Finally, two component-derived bags fail to be adjacent only if
each component misses the other's representative, exactly the reciprocal
defect pair excluded above.  Thus all pairs in (5.2) are adjacent, and
(5.2) is an explicit `K_7`-minor model.  This proves Theorem 1.1.

## 6. Exact contribution and trust boundary

The theorem eliminates the entire `(2,3)` centre-component configuration
without bounding the five component orders.  It combines literal
seven-connectivity, Dirac's contraction-critical inequality, set-Menger,
and a label-preserving boundary allocation.  A deterministic exhaustive
check of 138,240 canonical defect tables independently corroborated the
finite allocation in Section 4; the written proof does not depend on that
computation.

The theorem is conditional on reaching exactly two and three components
after deleting the selected centres.  It does not prove that every
two-component order-eight response interface reaches this count pair,
synchronize the two closed-shore colourings, or close the remaining count
pairs `(1,1)`, `(1,2)`, `(1,3)`, and `(2,2)`.

## 7. Dependencies

- Dirac's neighbourhood-independence inequality for contraction-critical
  graphs;
- vertex Menger's theorem;
- the connected-bipartition lemma; and
- the audited representative and paired-centre component decoders.
