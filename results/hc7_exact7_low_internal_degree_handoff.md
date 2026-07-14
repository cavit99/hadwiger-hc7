# Low-internal-degree exact-seven handoff

**Status:** proved and independently audited.

This note gives a label-free infinite-family closure for the
cutvertex-free thin packet in the connected-rich width-two frontier.  It
uses the actual seven-adhesion twice, Dirac's critical-neighbourhood
inequality once, and then displays a literal near-`K_7` model.  No portal
enumeration, web-completion edge, or palette-to-label identification is
used.

## 1. Setup

Let

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad |S|=7,
\tag{1.1}
\]

be an actual separation in a seven-connected graph: `L,R` are nonempty
and anticomplete, and `G[L]` is connected.  Suppose
`P,Q subseteq R` are disjoint connected
`S`-full packets and are adjacent.  Put `H=G[S]`.

Assume also the critical-neighbourhood inequality at a vertex `v in L`,

\[
             \alpha(G[N_G(v)])\le d_G(v)-5.             \tag{1.2}
\]

This is Dirac's inequality in a hypothetical strongly
seven-contraction-critical counterexample.

Write `d_L(v)=|N_G(v) cap L|`.

## 2. The literal handoff

### Lemma 2.1 (overlap-edge handoff)

Let `X,Y subseteq L` be disjoint adjacent connected subgraphs.  Put

\[
                       C=N_S(X)\cap N_S(Y).
\]

Suppose `C` contains distinct literals `x,y,t` with `xy in E(H)`, and
there are distinct anchors

\[
 a\in N_S(X)-\{x,y,t\},\qquad
 b\in N_S(Y)-\{x,y,t,a\}.
\]

Then `G` contains a labelled `K_7^vee` minor.  In particular, the anchor
condition is automatic when both supports have order at least five.

#### Proof

Use

\[
 X\cup\{a\},\qquad Y\cup\{b\},\qquad P,\qquad Q,
 \qquad\{x\},\qquad\{y\},\qquad\{t\}.
\]

The first four bags form a clique: `X-Y` and `P-Q` are literal edges, and
the anchors supply all four cross-shore adjacencies.  All four bags meet
each of `x,y,t`, and `xy` is a literal edge.  The only possible missing
pairs are therefore `xt,yt`, which share `{t}`.

If both supports have order at least five, choose `a` after deleting the
three displayed literals.  At most four literals are then forbidden when
choosing `b`, so one remains in its support. \(\square\)

### Theorem 2.2 (nonseparating subcubic vertex)

Suppose `L-{v}` is nonempty and connected and

\[
                              d_L(v)\le3.                \tag{2.1}
\]

Then `G` contains a labelled `K_7^vee` minor.

#### Proof

Put

\[
 W=N_S(v),\qquad Y=L-\{v\},\qquad C=W\cap N_S(Y).
\tag{2.2}
\]

The open shore `R` is nonempty and anticomplete to `v`.  Hence `N_G(v)`
separates `v` from `R`, and seven-connectivity gives

\[
                 |W|+d_L(v)=d_G(v)\ge7.                 \tag{2.3}
\]

Likewise `Y` is nonempty and connected, and

\[
                       N_G(Y)\subseteq S\cup\{v\}.
\]

The vertex `v` has a neighbour in `Y` because `G[L]` is connected.  The
set `N_G(Y)` separates `Y` from the nonempty opposite shore `R`, so
seven-connectivity gives

\[
                         |N_S(Y)|\ge6.                   \tag{2.4}
\]

Inclusion--exclusion in the literal seven-set `S` now yields

\[
                         |C|\ge |W|-1.                  \tag{2.5}
\]

By (2.1) and (2.3), `|W|>=4`, so `|C|>=3`.

The set `C` cannot be independent in `H`.  If it were, it would be an
independent set in the neighbourhood of `v`, and (1.2) would give

\[
 |W|-1\le |C|
       \le \alpha(G[N_G(v)])
       \le d_G(v)-5
       =d_L(v)+|W|-5
       \le |W|-2,
\]

a contradiction.  Choose a literal edge `xy` of `H[C]`, and choose

\[
                         t\in C-\{x,y\}.                 \tag{2.6}
\]

Since `|W|>=4`, choose

\[
                         a\in W-\{x,y,t\}.               \tag{2.7}
\]

By (2.4), at least two members of `N_S(Y)` remain after deleting the at
most four literals `x,y,t,a`.  Choose one of them as

\[
                  b\in N_S(Y)-\{x,y,t,a\}.              \tag{2.8}
\]

These choices satisfy Lemma 2.1 with `X={v}` and the connected set `Y`.
Explicitly, its seven branch sets are

\[
 \{v,a\},\qquad Y\cup\{b\},\qquad P,\qquad Q,
 \qquad\{x\},\qquad\{y\},\qquad\{t\}.                 \tag{2.9}
\]

The conclusion follows from Lemma 2.1.  \(\square\)

## 3. Width-two consequence

### Corollary 3.1 (the thin frontier has internal minimum degree four)

In the cutvertex-free thin-packet residue of the connected-rich
width-two frontier, either the graph has already handed off to `S1` via a
labelled `K_7^vee` model, or

\[
                         \delta(G[L])\ge4.               \tag{3.1}
\]

#### Proof

The audited frontier proves that `L` is nonsingleton.  It is the whole
thin shore and is connected: every open-shore component is `S`-full,
whereas the thin packet number is one.  Because `G[L]` is cutvertex-free,
`L-{v}` is connected for every `v in L`.  Apply Theorem 2.2 to any vertex
of internal degree at most three.  \(\square\)

## 4. Scope

The same literal packing idea also closes every two-gate with at least
three lobes.  This second statement does not use Dirac's inequality.

### Theorem 4.1 (three lobes behind a two-gate)

Retain the separation and the adjacent full packets `P,Q` from Section 1.
Suppose `G[L]` is cutvertex-free and a two-set `Z={u,v}` separates it
into at least three components.  Then `G` contains a labelled
`K_7^vee` minor.

#### Proof

Choose three components `D_1,D_2,D_3` of `L-Z`.  Each `D_i` has a
neighbour at both `u` and `v`: if, for example, it had no neighbour at
`u`, then the single vertex `v` would separate `D_i` from the other
components, contrary to cutvertex-freeness.

Moreover

\[
                    N_G(D_i)=N_S(D_i)\cup\{u,v\}.
\]

This set separates `D_i` from the nonempty opposite shore.  Therefore
seven-connectivity gives

\[
                         |N_S(D_i)|\ge5.                \tag{4.1}
\]

Put `Delta_i=S-N_S(D_i)`, so `|Delta_i|<=2`.  The three defect sets have
at most six incidences in total.  Hence there is a literal

\[
                 x\in S-(\Delta_1\cup\Delta_2\cup\Delta_3). \tag{4.2}
\]

Since none of the defect sets contains `x`, their at-most-six incidences
are distributed over the six-set `S-{x}`.  Choose `y in S-{x}` which
belongs to at most one of `Delta_1,Delta_2,Delta_3`.  Thus every `D_i`
contacts `x`, and at least two of them contact `y`.

For each `i`, the set

\[
                       N_S(D_i)-\{x,y\}
\]

has order at least three.  Three subsets of a five-set, each of order at
least three, have a system of distinct representatives: Hall's condition
is immediate for one, two, or three sets.  Choose distinct representatives

\[
        a_i\in N_S(D_i)-\{x,y\}\qquad(i=1,2,3).        \tag{4.3}
\]

Use the seven branch sets

\[
 D_1\cup\{u,a_1\},\quad
 D_2\cup\{v,a_2\},\quad
 D_3\cup\{a_3\},\quad
 P,\quad Q,\quad\{x\},\quad\{y\}.                    \tag{4.4}
\]

They are disjoint and connected.  The first three are pairwise adjacent:
`u` and `v` each have a neighbour in every `D_i`.  Their distinct boundary
anchors make each of them adjacent to both `P` and `Q`, while `P-Q` is an
assumed edge.  Thus the first five bags form a clique.

All five meet `{x}`.  The full packets and at least two of the first three
bags meet `{y}`.  Consequently the only possible missing pairs are `xy`
and the edge from `{y}` to the one lobe bag which may miss it.  These two
pairs share `{y}`, so (4.4) is a labelled `K_7^vee` model. \(\square\)

### Corollary 4.2 (exact surviving two-cuts)

After the `K_7^vee` handoff is excluded from the local `S3` branch, every
two-vertex cut of `G[L]` has exactly two lobes.  Combined with Corollary
3.1, the remaining thin packet has internal minimum degree at least four,
no cutvertex, and exactly two components behind each of its two-vertex
cuts.  No stronger chain or nesting conclusion is asserted.

## 5. Scope

The theorem is stronger than a contact-surplus statement and weaker than
the full width-two portal pullback.  It eliminates every order and every
portal distribution having a nonseparating subcubic thin vertex.  A
survivor has internal minimum degree at least four, so any remaining
crossed web is a genuinely bridge-rich or triangulated object.  Theorem
4.1 additionally removes every two-gate with three or more lobes; it does
not by itself organize the surviving two-lobe cuts into a chain.

The conclusion is a literal near-model handoff, not a `K_7` contradiction.
It must be composed with the separately audited `S1` near-model machinery.
