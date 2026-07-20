# Augmented path-span exchange with two boundary-full connected subgraphs

**Status:** written proof; separate internal audit GREEN in
[`hc7_exact7_augmented_path_span_exchange_audit.md`](hc7_exact7_augmented_path_span_exchange_audit.md).
This is an unbounded positive exchange inside the exact-seven two-subgraph
interface.  It does not prove `HC_7`.

## 1. Setting

Let `G` be seven-connected, not six-colourable, and suppose every proper
minor of `G` is six-colourable.  Let

\[
 V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}B,
 \qquad E_G(A,B)=\varnothing,
 \qquad |S|=7,                                      \tag{1.1}
\]

where both open shores are nonempty.  Write

\[
 S=D\mathbin{\dot\cup}E\mathbin{\dot\cup}\{r,z\},
 \qquad |D|=3,\quad |E|=2.                           \tag{1.2}
\]

Assume a selected proper six-colouring of `G[A union S]` induces one of
the exact boundary partitions

\[
 \Pi_A=D\mid E\mid\{r\}\mid\{z\},
 \qquad rz\notin E(G),                              \tag{1.3}
\]

or

\[
 \Pi_B=D\mid E\mid\{r,z\}.                          \tag{1.4}
\]

Let `P_1,P_2` be vertex-disjoint connected subgraphs of `G[A]`, each
adjacent to every literal vertex of `S`.  Let

\[
                         P=r p_0p_1\cdots p_k z      \tag{1.5}
\]

be an `r`--`z` path with internal vertices in `A`, disjoint from `P_2`,
and meeting `P_1` internally.

For `u in {r,z}` and `F in {D,E}`, put

\[
 Q_u(F)=F\cup
 \begin{cases}
 \{u\},&E_G(u,F)=\varnothing,\\
 \varnothing,&E_G(u,F)\ne\varnothing.
 \end{cases}                                        \tag{1.6}
\]

These are the literal required-contact sets from the audited
componentwise path-residual exchange.

## 2. A general reserved-span criterion

### Lemma 2.1

Suppose `P'` is an `r`--`z` path with internal vertices in `A`, disjoint
from `P_2`, and `K subseteq A` induces a nonempty connected subgraph
disjoint from `P' union P_2`.  Assume `K` is adjacent to the internal part
of `P'`.

1. If the selected partition is `Pi_A` and `K` has a neighbour at every
   literal vertex of one of

   \[
                  Q_r(D),\quad Q_z(D),\quad
                  Q_r(E),\quad Q_z(E),                \tag{2.1}
   \]

   then the same complete partition `Pi_A` is induced on both closed
   shores, and `G` is six-colourable.
2. If the selected partition is `Pi_B` and `K` has a neighbour at every
   vertex of `D` or at every vertex of `E`, then the same complete
   partition `Pi_B` is induced on both closed shores, and `G` is
   six-colourable.

#### Proof

Assume first that `Pi_A` is selected and, for definiteness, that `K` meets
every vertex of `Q_r(D)`.  Keep `{r}` literal and let `P'_z` be the path
obtained from `P'` by deleting `r`.  The four sets

\[
                  K\cup D,\qquad P_2\cup E,
                  V(P'_z),\qquad\{r\}                \tag{2.2}
\]

are disjoint and connected.  They are pairwise adjacent:

* `K union D` meets `P'_z` by the assumed edge from `K` to the internal
  part of `P'`;
* `P_2 union E` meets both path blocks through its boundary-full contacts
  at `r,z`;
* the two boundary-block sets meet because `P_2` has a neighbour at every
  vertex of `D`;
* `r` meets `P'_z` at the first path edge and meets `P_2 union E` through
  boundary-fullness; and
* `r` meets `K union D` either through an edge from `r` to `D` or because
  `r in Q_r(D)` and `K` has the required literal contact.

Contract a spanning tree in each nonsingleton set of (2.2).  Their four
images form a clique and contain the four independent blocks of `Pi_A`.
A six-colouring of this proper minor pulls back on the untouched closed
`B`-shore to the exact partition `Pi_A`, which aligns with the selected
colouring on the closed `A`-shore.  The other three contact sets in (2.1)
are symmetric under interchanging `D,E` and/or `r,z`.

Now suppose `Pi_B` is selected and, for definiteness, that `K` meets every
vertex of `D`.  The three disjoint connected sets

\[
                         K\cup D,qquad P_2\cup E,
                         V(P')                       \tag{2.3}
\]

are pairwise adjacent.  The first and third meet by hypothesis, the second
and third through a boundary-full contact at `r`, and the first two through
a contact from `P_2` to `D`.  Their contraction forces the exact partition
`D|E|{r,z}` on the untouched closed shore.  It glues to the selected
colouring.  The case in which `K` meets all of `E` is symmetric.
\(\square\)

## 3. Augmenting the span of a detour

An **off-path component** is a component of

\[
                  G[A-(V(P)\cup V(P_2))].             \tag{3.1}
\]

This definition deliberately uses the whole open shore, rather than only
`P_1`.  Thus an ambient connector joining several residual pieces of
`P_1-V(P)` is absorbed into one off-path component.

### Theorem 3.1

Suppose one off-path component `R_0` has neighbours at two distinct
internal path vertices `p_i,p_j`, where `i<j`, and let `W` be a
`p_i`--`p_j` path whose internal vertices lie in `R_0`.  Put

\[
 I=\{p_{i+1},\ldots,p_{j-1}\}                       \tag{3.2}
\]

and assume `I` is nonempty.  Define

\[
 K=I\ \cup
   \bigcup\{V(R):R\ne R_0\text{ is an off-path component with }
                         N_G(R)\cap I\ne\varnothing\}. \tag{3.3}
\]

If `K` meets one of the four required-contact sets in (2.1) in the
`Pi_A` case, or every vertex of `D` or `E` in the `Pi_B` case, then `G` is
six-colourable.

#### Proof

Every off-path component included in (3.3) is connected and has an edge to
`I`, so `G[K]` is connected.  Reroute `P` through `W`:

\[
 P'=P[r,p_i]\cup W\cup P[p_j,z].                    \tag{3.4}
\]

The path `P'` is disjoint from `K`: its detour interior lies in `R_0`,
whereas (3.3) excludes `R_0`, and it avoids the open segment `I`.  Both
`K` and `P'` remain disjoint from `P_2`.  Finally, `K` is adjacent to the
internal part of `P'` through the path edges at `p_i` and `p_j`.
Lemma 2.1 now applies. \(\square\)

The theorem also applies to a chord `p_ip_j` of `P`, with no excluded
off-path component in (3.3).

## 4. Exact gain and trust boundary

The augmented span may combine an arbitrary number of off-path components,
including ambient connectors through vertices outside `P_1`.
It therefore captures positive exchanges that no residual component or
single bridge detects by itself.  All contacts in the proof are with
literal members of the fixed boundary blocks, and the complete selected
partition is reproduced on the opposite closed shore.

The theorem does not prove that a suitable detour exists or that one
augmented span meets a required-contact set.  Failure of every augmented
span has not yet been converted into an order-seven separator or a strict
response-preserving descent.

## 5. Dependencies

- proper-minor six-colourability;
- the exact boundary-block contractions in the audited componentwise
  path-residual exchange; and
- the audited two-full-subgraph Kempe-compression theorem, which supplies
  the selected path/interface to which the exchange applies.
