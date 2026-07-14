# Exact-seven multishore state synchronization

**Status:** proved and independently audited.

This theorem is a finite-boundary composition principle rather than a
boundary census.  Two adjacent labelled carriers in one component and one
additional full component reproduce the exact state returned using two
other full components.  The same state can then be synchronized over every
component of the cut.

## 1. The uniform theorem

Let `G` be a graph in which every proper minor is six-colourable.  Let `S`
be a literal seven-vertex cut such that `G-S` has at least three nonempty
connected components, each `S`-full.  Suppose one component `C` contains
disjoint adjacent connected subgraphs `X,Y`.

Let `I,J` be disjoint nonempty independent subsets of `S` satisfying

\[
 I\subseteq N_S(X),\qquad J\subseteq N_S(Y).           \tag{1.1}
\]

Put `W=S-(I union J)` and assume

\[
 |W|=3,qquad E(G[W])\ne\varnothing,qquad
 W\subseteq N_S(X)\cap N_S(Y).                        \tag{1.2}
\]

### Theorem 1.1 (multishore synchronization)

The graph `G` is six-colourable.

### Proof

Choose two components `A,Q` of `G-S` different from `C`.  Contract the two
disjoint connected sets

\[
                            A\cup I,\qquad Q\cup J.    \tag{1.3}
\]

Their images are adjacent, and fullness makes each image adjacent to every
literal vertex of `W`.  Six-colour this proper minor, restrict to the
untouched original closed `C`-side, and expand only the independent sets
`I,J`.  The exact equality partition on `S` is

\[
                            \Sigma=I\mid J\mid\Theta,  \tag{1.4}
\]

where `Theta` is the proper equality partition induced on `W`.  The edge in
`G[W]` means that `Theta` has either two or three blocks.

Fix any component `R ne C` of `G-S`.  Choose another full component `F`
different from both `C,R`; this is possible because `G-S` has at least
three components.  We now reproduce the actual state (1.4) on the closed
`R`-side by an operation using `C` and `F`.

If `Theta` has two blocks, write it as an independent pair `K` and a
singleton `{w}`.  Contract

\[
                       X\cup I,qquad Y\cup J,qquad F\cup K             \tag{1.5}
\]

and retain `w`.  These four representatives form a clique.  The first two
are adjacent by hypothesis; fullness of `F` supplies its two carrier
adjacencies and its adjacency to `w`; and (1.2) supplies the two remaining
carrier-to-`w` edges.

If `Theta` has three singleton blocks, choose an edge `uv` of `G[W]`, let
`w` be the third vertex of `W`, contract

\[
                       X\cup I,qquad Y\cup J,qquad F\cup\{w\},        \tag{1.6}
\]

and retain `u,v`.  The five representatives form a clique by adjacency of
`X,Y`, fullness of `F`, the two complete contact conditions in (1.2), and
the literal edge `uv`.

In either case the contractions are a proper minor operation: the nonempty
component `R` is untouched.  A six-colouring therefore pulls back to the
closed `R`-side with equality partition exactly `Sigma`, because the
displayed representative clique has one vertex for every block.

Repeat this construction for every component `R ne C`.  Permute the six
colour names in all component-side colourings so that corresponding blocks
of `Sigma` agree.  The components of `G-S` are pairwise anticomplete, hence
the aligned colourings glue over the literal common boundary `S` to a
six-colouring of `G`.  \(\square\)

## 2. Application to a complementary two-cut lock

Continue under the hypotheses of Theorem 1.1, and use the paired-triangle
boundary notation

\[
 S=\{c,a_1,t_1,a_2,t_2,a_3,t_3\},\qquad
 B_i=\{a_i,t_i\}.
\]

For a carrier `Z`, write `Delta(Z)=S-N_S(Z)`.  Suppose the distinguished
component `C` has a two-cut with two disjoint adjacent carriers
`X,Y` satisfying

\[
 \Delta(X)=\{a_1,a_2\}=:P,\qquad
 \Delta(Y)=\{t_1,t_2\}=:T,                             \tag{2.1}
\]

and suppose `G-S` has at least two further full components.  The paired
state gives `B_3` independent and at least one literal edge from `c` to
`B_3`.

### Corollary 2.1

If both `P` and `T` are independent, then `G` is six-colourable.
Consequently any surviving complementary lock satisfies

\[
                         E(G[P])\ne\varnothing
                 \quad\hbox{or}\quad E(G[T])\ne\varnothing.           \tag{2.2}
\]

### Proof

Apply Theorem 1.1 with

\[
 I=T,\qquad J=P,qquad W=B_3\cup\{c\}.                 \tag{2.3}
\]

Equations (2.1) say that `X` funds `T`, `Y` funds `P`, and both carriers
contact every vertex of `W`.  The named `c-B_3` adjacency supplies the
edge required in (1.2).  \(\square\)

## 3. Exact scope

The theorem does not require a selected colouring, a planar embedding, a
bounded component order, or a fixed boundary graph.  It synchronizes the
state actually returned in (1.3).  Some carrier-to-retained-block adjacency
is essential: without it a retained singleton need not be adjacent to one
of the two labelled carrier representatives.  Section 4 records the exact
weaker duty condition; it does not replace that adjacency by a raw contact
count.

## 4. Attained-duty extension

The complete-contact condition (1.2) can be weakened to the exact
adjacency duty of the state returned on `W`.  Retain the setup of Section 1
except for the last condition in (1.2), and define

\[
 \begin{aligned}
 R_X&=W\cap\bigl(N_S(X)\cup N_{G[S]}(I)\bigr),\\
 R_Y&=W\cap\bigl(N_S(Y)\cup N_{G[S]}(J)\bigr),\\
 R&=R_X\cap R_Y.
 \end{aligned}                                         \tag{4.1}
\]

Thus `w in R` says literally that both contracted representatives
`X union I` and `Y union J` are adjacent to the retained singleton `w`;
the adjacency may come from the carrier or from its assigned boundary
block.

### Theorem 4.1 (duty-aware synchronization)

The conclusion of Theorem 1.1 still holds if its complete-contact condition
on `W` is replaced by

1. `G[R]` contains an edge; and
2. every `w in W` for which `W-{w}` is independent belongs to `R`.

### Proof

Use (1.3) to obtain the actual partition `Sigma=I|J|Theta` exactly as in
Theorem 1.1.  If `Theta` has two blocks, it is

\[
                         (W-\{w\})\mid\{w\}
\]

with `W-{w}` independent.  Condition 2 says that both labelled carrier
representatives see the retained singleton `w`; the third full component
funds the independent pair.  If `Theta` has three singleton blocks, retain
the endpoints of an edge of `G[R]` and let the third full component fund the
remaining singleton.  The definitions in (4.1) supply every carrier-to-
retained-singleton adjacency.  The componentwise reproduction, exactness,
palette alignment, and gluing are then identical to Theorem 1.1.  \(\square\)

### Corollary 4.2 (one edged defect pair)

In the complementary lock of Section 2, suppose `P` is an edge and `T` is
independent.  Put

\[
                         D=N_{G[S]}(T)\cap P.           \tag{4.2}
\]

If `|D|=2`, or if `D={p}` and `cp in E(G)`, then `G` is six-colourable.
Consequently a survivor satisfies

\[
 |D|\le1,qquad D=\{p\}\Longrightarrow cp\notin E(G). \tag{4.3}
\]

The symmetric statement holds with `P,T` interchanged.

### Proof

Apply Theorem 4.1 with

\[
                         I=T,\qquad J=B_3,qquad
                         W=P\cup\{c\}.                 \tag{4.4}
\]

The `X` representative sees exactly `{c} union D` in `W`, while the `Y`
representative sees all of `W`.  Hence

\[
                              R=\{c\}\cup D.           \tag{4.5}
\]

If `D=P`, the literal edge on `P` lies in `G[R]`, and every possible
retained singleton lies in `R`.  If `D={p}` and `cp` is an edge, that edge
lies in `G[R]`.  Writing `P={p,q}`, the only vertex of `W-R` is `q`, but
`W-{q}` contains the edge `cp`; hence `q` cannot be the singleton of a
two-block proper partition of `W`.  The two duty-aware conditions again
hold.  Theorem 4.1 finishes both cases.  \(\square\)
