# Binary two-gates force a labelled near model

**Status:** proved and independently audited.  No boundary-label census is
used.

This note closes the binary two-cut geometry left by the connected-rich
width-two frontier.  The proof is a literal carrier construction.  Its
only finite-boundary input is the already proved structural alternative:
the paired boundary is connected with a spanning non-path tree, or is
`K_{1,3} dotcup K_3`.

## 1. A repairable-incidence lemma

Let `T` be a tree on a seven-set `S`, and let `D_X,D_Y subseteq S` be
disjoint sets of order at most two.  Put

\[
                         C=S-(D_X\cup D_Y).              \tag{1.1}
\]

Call an edge `uf` **repairable** if `u in C`, `f in D_Z` for one of
`Z in {X,Y}`, and

\[
                  N_T(f)-\{u\}\not\subseteq D_Z.        \tag{1.2}
\]

Thus there is a second neighbour `a` of `f`, different from `u`, which
is not missed by carrier `Z`.

### Lemma 1.1 (common edge or repairable incidence)

If `T` is not a path, then either `T[C]` has an edge or `T` has a
repairable edge.

#### Proof

Suppose `C` is independent and there is no repairable edge.  Contract each
component of `T-C` to one node, retaining the vertices of `C`.  The
resulting incidence graph `B` is a bipartite tree whose parts are `C` and
the components of `T-C`.

If an edge from `u in C` enters a component `K` at `f in D_Z`, the
failure of (1.2) says that every neighbour of `f` in `K` belongs to the
same set `D_Z`.  In particular `f` has no second neighbour in `C`.
Hence the `d_B(K)` attachment edges at a component node `K` use
`d_B(K)` distinct vertices of `K`, and

\[
                              |K|\ge d_B(K).             \tag{1.3}
\]

Let `k` be the number of component nodes of `B`.  Summing (1.3) gives

\[
 |D_X\cup D_Y|
   =\sum_K|K|
   \ge\sum_Kd_B(K)
   =|E(B)|
   =|C|+k-1.                                            \tag{1.4}
\]

Now `|C|>=3`, `|D_X union D_Y|<=4`, and `k>=1`.  Equation (1.4) forces

\[
                  |C|=3,\qquad |D_X\cup D_Y|=4,
                  \qquad k\le2.                         \tag{1.5}
\]

If `k=2`, equality holds throughout (1.4).  The two component-node degrees
sum to four.  Neither can have degree three: a three-vertex connected
component with three attachment vertices is a path, whose middle
attachment vertex has two neighbours in the component; the no-repair
condition would put that vertex and both neighbours in one defect set of
order at most two.  Thus both component nodes have degree two, both
components have order two, and `B` is the alternating path through its
three vertices of `C`.  Expanding the two component nodes shows that `T`
itself is a path.

If `k=1`, the single component `K=T-C` has four vertices and three
attachments.  A tree on four vertices is a path or a claw.  In a path,
at most its two leaves can be attachment vertices: an internal attachment
vertex has two component neighbours, again requiring three vertices in
one defect set.  In a claw, three attachments would have to be the three
leaves, and the no-repair condition would put each leaf together with the
common centre in its own defect set.  Three leaves cannot all share a
centre using two disjoint defect sets of order at most two.  Both cases
are impossible.

The only remaining outcome of (1.5) made `T` a path, contrary to the
hypothesis.  Hence an edge of `T[C]` or a repairable incidence exists.
\(\square\)

### Lemma 1.2 (the disconnected frontier)

Let `H=K_{1,3} dotcup K_3` on `S`.  With `D_X,D_Y,C` as above, either
`H[C]` has an edge or there is a repairable edge in the sense of (1.2),
with `H` in place of `T`.

#### Proof

Assume `C` is independent.  It contains at most one triangle vertex.
Since `|C|>=3`, it contains at least two vertices of the claw.  Those two
must be leaves, because the claw centre is adjacent to every leaf.  The
centre `f` therefore lies in one defect set, while two common leaves are
neighbours of `f`.  Taking one as `u` and the other as the repairing
neighbour `a` gives (1.2).  \(\square\)

## 2. Two nearly full adjacent carriers

Let `H` be a graph on a literal seven-set `S`.  Let `X,Y,P,Q` be pairwise
disjoint connected sets outside `S` such that:

1. `X` and `Y` are adjacent;
2. `P` and `Q` are adjacent and `S`-full;
3. `|N_S(X)|,|N_S(Y)|>=5`; and
4. `N_S(X) union N_S(Y)=S`.

Put

\[
 D_X=S-N_S(X),\qquad D_Y=S-N_S(Y),qquad
 C=N_S(X)\cap N_S(Y).                                  \tag{2.1}
\]

Thus `D_X,D_Y` are disjoint and have order at most two.

### Theorem 2.1 (two-defect anchored near model)

Suppose either

1. `H` contains a spanning tree which is not a path; or
2. `H=K_{1,3} dotcup K_3`.

Then the displayed sets together with `S` contain a literal labelled
`K_7^vee` model.

#### Proof

First suppose `H[C]` contains an edge `rs`.  Choose any
`t in C-{r,s}`.  Since each support has order at least five, the two sets

\[
 N_S(X)-\{r,s,t\},\qquad N_S(Y)-\{r,s,t\}
\]

each have order at least two and hence have distinct representatives
`a,b`.  Use the seven bags

\[
 X\cup\{a\},\quad Y\cup\{b\},\quad P,\quad Q,
 \quad\{r\},\quad\{s\},\quad\{t\}.                    \tag{2.2}
\]

The first four form a clique: `X-Y` and `P-Q` are literal, and the
boundary anchors join each of `X,Y` to both full packets.  All four meet
each of `r,s,t`.  Among the last three bags, `rs` is literal, so the only
two possibly missing pairs are `rt,st`, both incident with `{t}`.  Thus
(2.2) is a `K_7^vee` model.

It remains to suppose that `C` is independent.  Apply Lemma 1.1 to a
spanning non-path tree of `H`, or Lemma 1.2 in the disconnected case.
There are `u in C`, `f in D_Z`, and

\[
                    a\in N_H(f)-\bigl(\{u\}\cup D_Z\bigr). \tag{2.3}
\]

Assume `Z=X`; the other case is symmetric.  Choose

\[
                    w\in C-\{u,a\}.                     \tag{2.4}
\]

This is possible because `|C|>=3`; when `a notin C`, only `u` is excluded
from `C`.  Finally choose

\[
                 b\in N_S(Y)-\{u,f,w,a\}.               \tag{2.5}
\]

There are three literals outside the four-set in (2.5), while `Y` misses
at most two, so such a `b` exists.

Use

\[
 X\cup\{a\},\quad Y\cup\{b\},\quad P,\quad Q,
 \quad\{u\},\quad\{f\},\quad\{w\}.                    \tag{2.6}

Again the first four bags form a clique.  Both `X` and `Y` contact `u,w`.
The carrier `Y` also contacts `f`, because the two defect sets are
disjoint; the carrier bag `X union {a}` sees `f` through the literal edge
`af`.  Hence all four carrier bags meet all three singleton bags.  The
edge `uf` is literal, while `uw` is absent because `C` is independent.
The edge `fw` may or may not be present.  Therefore the only possible
missing singleton pairs are `uw,fw`, and they share `{w}`.  The bags in
(2.6) form a labelled `K_7^vee` model.  \(\square\)

No quotient edge is being lifted implicitly in this proof: every carrier
adjacency is either an assumed literal edge, a boundary anchor, a literal
support contact, or one of the displayed boundary edges.

## 3. Binary gates in the connected-rich frontier

Use the connected-rich width-two frontier setup.  Thus `L` is the
cutvertex-free thin packet, `P,Q` are the adjacent `S`-full packets in the
rich shore, and the paired boundary `H=G[S]` is a connected tree, a
six-cycle with one pendant vertex, or `K_{1,3} dotcup K_3`.

### Theorem 3.1 (every binary two-cut leaves the local spine)

If `Z={p,q}` is a two-vertex cut of `G[L]`, then `G` contains a labelled
`K_7^vee` minor.

#### Proof

The audited low-internal-degree handoff first disposes of the case in
which `L-Z` has at least three components: that case already yields a
labelled `K_7^vee` minor.  We may therefore assume that `L-Z` has exactly
two components; call them `D,E`.  Since `G[L]` has no cutvertex, each of
`D,E` has a neighbour at both `p` and `q`.  Put

\[
                         X=D\cup\{p\},\qquad
                         Y=E\cup\{q\}.                  \tag{3.1}
\]

These sets are disjoint, connected and adjacent.  For each lobe,

\[
                         N_G(D)=N_S(D)\cup\{p,q\}.
\]

This separates `D` from the nonempty rich shore, so seven-connectivity
gives `|N_S(D)|>=5`, and symmetrically `|N_S(E)|>=5`.  Hence
`|N_S(X)|,|N_S(Y)|>=5`.  Moreover `X union Y=L` is `S`-full, so their
supports cover `S`.

If `H` is connected, the three literal neighbours of `c`, one in each
paired block, form a three-edge star.  Extend that forest to a spanning
tree of `H`; the spanning tree is not a path.  If `H` is disconnected, the
frontier theorem gives exactly `K_{1,3} dotcup K_3`.  All hypotheses of
Theorem 2.1 now hold, which supplies the labelled `K_7^vee` model.
\(\square\)

### Corollary 3.2

After the labelled near-model handoff is excluded from the local `S3`
branch, the thin packet `G[L]` is three-connected.  Together with the
audited low-internal-degree theorem, it also satisfies

\[
                              \delta(G[L])\ge4.
\]

The remaining local width-two obstruction is therefore not an arbitrary
SPQR chain: it lies in one three-connected block.  Any further rural/web
outcome must spend the actual Dirac neighbourhood inequalities or a
proper-minor state transition inside that block.
