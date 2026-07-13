# The minimum `C6+K1` atom has a genuine interface square

## 1. Full rows are already positive

Let `S={c_0,...,c_5,z}` and suppose

\[
                    \overline{G[S]}=C_6\dot\cup K_1,
\]

where the missing cycle is `c_0c_1...c_5c_0`.  Thus
`{c_0,c_2,c_4,z}` is a four-clique in `G[S]`.

### Lemma 1.1 (three full pieces)

Let `A,B,C` be pairwise disjoint connected subgraphs outside `S`, each
full to `S`.  No assumption is made about edges among the three pieces.
Then `G[S union A union B union C]` contains a `K_7` minor.

### Proof

Use the four singleton bags

\[
             \{c_0\},\ \{c_2\},\ \{c_4\},\ \{z\}
\]

and the three bags

\[
             A\cup\{c_1\},\quad B\cup\{c_3\},\quad
             C\cup\{c_5\}.
\]

Each of the last three bags is connected.  Any two are adjacent because
the first piece is adjacent to the boundary representative contained in
the second bag.  Each is adjacent to all four singleton bags by fullness.
The singleton bags form a clique.  These are seven branch bags.  QED.

### Corollary 1.2 (a full/full split is positive)

Suppose `G-S` has an opposite full shore `H`, and another shore has a
connected adjacent split `D=X dotcup Y`.  If both `X,Y` are full to `S`,
then `G` contains a `K_7` minor.

Apply Lemma 1.1 to `X,Y,H`.  Notice that no contraction of the internal
`X-Y` edge is needed.

## 2. A minimum-fragment interface is not a single edge

Assume now that `D` is a minimum fragment behind a seven-cut and that
`D=X dotcup Y` is a connected covering split.  Put

\[
 P_X=N_S(X),\quad T_X=N_Y(X),
\]

and define `P_Y,T_Y` symmetrically.  Atomic surplus gives

\[
                  |P_X|+|T_X|\ge8,
       \qquad     |P_Y|+|T_Y|\ge8.                \tag{2.1}
\]

### Lemma 2.1 (no unique interface edge)

If `E(X,Y)` consists of one edge, then `G` contains a `K_7` minor.

### Proof

A unique interface edge gives `|T_X|=|T_Y|=1`.  Equation (2.1) and
`|S|=7` force `P_X=P_Y=S`.  Corollary 1.2 applies.  QED.

Thus every edge deletion at the interface of a target-free minimum atom
leaves another interface edge and preserves the same connected covering
geometry.

### Lemma 2.2 (square or singleton hub)

If the bipartite interface graph `E(X,Y)` has a matching of order two,
then `X,Y` admit connected bipartitions

\[
 X=X_1\dot\cup X_2,\qquad Y=Y_1\dot\cup Y_2
\]

whose adjacency skeleton contains the cycle

\[
                    X_1X_2Y_2Y_1X_1.              \tag{2.2}
\]

If it has no such matching, all interface edges share one endpoint `h`.
Since every nonsingleton `C6+K1` full shore is two-connected, the side
containing `h` is the singleton `{h}`.

### Proof

For a matching `x_1y_1,x_2y_2`, split a spanning tree of `X` on the path
between `x_1,x_2`, and do the same in `Y`; this gives (2.2).

If the matching number is one, the size-one case of Konig's theorem says
that all interface edges have one common endpoint, say `h in X`.  If
`X-{h}` were nonempty, removing `h` would separate it from `Y`, making
`h` a cutvertex of the full shore `D`.  The audited two-piece lock says
that a nonsingleton full `C6+K1` shore is two-connected.  Hence
`X={h}`.  QED.

### Lemma 2.3 (exact singleton-hub load)

In the singleton outcome, write `X={h}`.  Then `Y` is full to `S`, the
boundary row of `h` has order at most four, and

\[
                         |N_Y(h)|\ge4.              \tag{2.3}
\]

### Proof

All interface edges have their `X`-end at `h`, so `T_Y={h}`.  Atomic
surplus for `Y` gives `|P_Y|+1>=8`; hence `P_Y=S`.  Apply the exact
two-piece atlas to the negative split `{h}|Y`.  With the second defect
empty, the first defect contains one of the two boundary triangles or
the complement of an antipodal pair.  Thus `h` contacts at most four
boundary vertices.  Atomic surplus for `{h}` now gives

\[
                  |N_S(h)|+|N_Y(h)|\ge8,
\]

which proves (2.3).  QED.

### Corollary 2.4 (the hub sits over a two-connected body)

The minimum fragment `D` is three-connected, and in the singleton-hub
outcome `Y=D-h` is two-connected.

### Proof

The audited defect-two SPQR descent theorem turns every two-cut of a
full `C6+K1` shore into an exact seven-cut with a proper component inside
that shore.  Minimum-fragment choice excludes this, so the already
two-connected `D` is three-connected.  Deleting one vertex from a
three-connected graph leaves a two-connected graph.  QED.

## 3. Dynamic residue

The four-piece outcome supplies two independent interface edges, so it
supports individual deletion states and a simultaneous contraction
state.  It does **not** by itself satisfy the exact two-edge-interface
hypothesis of the double-interface contraction theorem: additional
`X-Y` edges may remain and can carry incompatibility not recorded by the
two selected coordinates.  A closure therefore needs a multi-interface
factorization theorem, or a further operation which makes the selected
matching faithful without destroying the covering rows.
The singleton outcome is no longer a vague common-alpha hub.  Its other
side is full to `S`, while the singleton's boundary row is contained in
one of the clique rows forced by the exact two-piece atlas; atomic surplus
forces at least four distinct internal neighbours.

The remaining theorem must close these two precise alternatives by a
state-preserving rooted split or crossed colour gluing.  Lemmas 1.1--2.2
do not by themselves supply that last operation exchange.
