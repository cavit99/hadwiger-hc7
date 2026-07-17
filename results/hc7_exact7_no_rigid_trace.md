# Exact seven-vertex boundaries have no rigid five-colour trace

**Status:** written proof; separate internal audit GREEN.

This note identifies a closure mechanism which cannot occur in a surviving
order-seven separation of a hypothetical minimal counterexample to
Hadwiger's Conjecture for \(t=7\).  It does not prove `HC_7`.

## 1. Setup

Let `G` be a seven-connected graph with no `K_7` minor, and let

\[
        V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
        \qquad |S|=7,
\]

where `L` and `R` are nonempty, there is no edge between them, and

\[
                 N_G(L)\subseteq S,
                 \qquad N_G(R)\subseteq S.                 \tag{1.1}
\]

The sets `L` and `R` are allowed to be disconnected.  This includes an
arbitrary actual separation of order seven after assigning every component
of `G-S` to one of its two nonempty open shores.

A connected subgraph of `G-S` is **`S`-full** when every vertex of `S` has
a neighbour in it.

## 2. Every vertex deletion is `K_5`-minor-free

### Lemma 2.1 (two full components and a deleted boundary root)

Every component of `G[L]` and every component of `G[R]` is `S`-full.
Moreover, for every `v in S`,

\[
                         K_5\not\preccurlyeq G[S-v].       \tag{2.1}
\]

Consequently

\[
                         \omega(G[S])\le 4.                \tag{2.2}
\]

#### Proof

Let `C` be a component of `G-S`.  Its neighbourhood is contained in `S`.
If it missed a vertex `s` of `S`, then

\[
                         N_G(C)\subseteq S-\{s\}
\]

would separate `C` from the nonempty opposite open shore using at most six
vertices, contrary to seven-connectivity.  Thus `C` is `S`-full.

Choose one component `P_L` in `L` and one component `P_R` in `R`.  Fix
`v in S`, and suppose that

\[
                            Q_1,\ldots,Q_5
\]

are the branch sets of a `K_5`-minor model in `G[S-v]`.  Then

\[
           P_L\cup\{v\},\qquad P_R,qquad
           Q_1,\ldots,Q_5                                  \tag{2.3}
\]

are seven pairwise disjoint connected branch sets.  The two packet-derived
sets are adjacent because `P_R` has a neighbour at `v`.  Each is adjacent
to every `Q_i` by fullness, and the five `Q_i` are pairwise adjacent by
hypothesis.  Thus (2.3) is a `K_7`-minor model, a contradiction.  This
proves (2.1).

If `G[S]` contained a five-vertex clique, deleting either of the other two
vertices would leave a `K_5` subgraph, contrary to (2.1).  This proves
(2.2).  \(\square\)

This strengthens the clique bound from the two-packet case of the audited
exact-seven packet theorem: every `K_5` model on the boundary must use all
seven literal boundary vertices.

The branch-set argument is parameter-uniform.  If a `K_t`-minor-free graph
has two disjoint connected subgraphs outside a set `T`, each adjacent to
every vertex of `T`, then

\[
                     K_{t-2}\not\preccurlyeq G[T-v]
                     \qquad(v\in T).                       \tag{2.4}
\]

Indeed, adjoining `v` to the first connected subgraph and using the second
one separately extends any `K_{t-2}` model in `T-v` to a `K_t` model,
exactly as in (2.3).

### Corollary 2.2 (the only five-chromatic boundary)

Assume the established case `HC_5`.  Then

\[
                         \chi(G[S])\le5.                  \tag{2.5}
\]

If equality holds, then

\[
                         G[S]\cong K_2\vee C_5.           \tag{2.6}
\]

#### Proof

By Lemma 2.1 and `HC_5`, every graph `G[S-v]` is four-colourable.  Giving
`v` a new colour proves (2.5).  If equality holds, `G[S]` is therefore
vertex-critical with chromatic number five.

We prove the required seven-vertex classification.  Put `H=G[S]` and
\(F=\overline H\).  Vertex-criticality gives \(\delta(H)\ge4\), and hence
\(\Delta(F)\le2\).  Thus every component of `F` is a path, a cycle, or an
isolated vertex.  A proper colouring of `H` is exactly a partition of
`V(F)` into cliques.  Write `theta(F)` for the minimum number of cliques in
such a partition.  Then

\[
                \theta(F)=5,
                \qquad \theta(F-v)\le4\quad(v\in V(F)).   \tag{2.7}
\]

For a graph `J` of maximum degree at most two, call
`|J|-theta(J)` its saving.  Isolated vertices have saving zero; `P_2` and
`P_3` have saving one; each of `P_4,P_5,C_3,C_4,C_5` has saving two; and
every longer path or cycle has saving at least three.  Savings add over
components.  Equation (2.7) says that `F` has total saving two and that
deleting any vertex leaves saving at least two.

There are only two ways to obtain total saving two: one component has
saving two, or two components have saving one.  In the second case,
deleting a suitable vertex from either nontrivial component lowers the
total saving to at most one.  The same is true for a component
`P_4,P_5,C_3`, or `C_4`: respectively delete an endpoint, a vertex next
to an endpoint, any vertex, or any vertex.  The sole surviving component
is `C_5`, since deleting any of its vertices leaves `P_4`, still of saving
two.  All other components are isolated.  As `|F|=7`,

\[
                             F\cong C_5\mathbin{\dot\cup}2K_1.
\]

Taking complements gives \(H\cong K_2\vee C_5\), which is (2.6).
\(\square\)

### Corollary 2.3 (canonical connected `(1,1)` residue)

Assume in addition that `G` is seven-chromatic and every proper minor of
`G` is six-colourable.  If `chi(G[S])=5`, write

\[
                        G[S]=G[\{p,q\}]\vee C,
                        \qquad C\cong C_5,                \tag{2.8}
\]

as in Corollary 2.2.  Then each open shore is connected and contains no
two vertex-disjoint `S`-full connected subgraphs.  Equivalently, the
full-packet vector is exactly `(1,1)`.

Moreover, `G-{p,q}` contains a `K_5` minor, but it has no `K_5`-minor
model with five branch sets respectively containing the five vertices of
`C`.

#### Proof

Let `nu_L,nu_R` be the two full-packet packing numbers.  The audited
exact-seven packet theorem gives

\[
               \omega(G[S])\le6-(\nu_L+\nu_R).            \tag{2.9}
\]

Here `omega(G[S])=4`, while each packet number is at least one.  Therefore
`nu_L+nu_R<=2`, and hence `nu_L=nu_R=1`.  Every component in either open
shore is `S`-full by Lemma 2.1.  Two components in one shore would be two
disjoint full packets, so both shores are connected.

Deleting two vertices lowers chromatic number by at most two, so

\[
                             \chi(G-\{p,q\})\ge5.
\]

The contrapositive of `HC_5` now gives a `K_5` minor in `G-{p,q}`.  If
that graph had a `K_5` model rooted at the five vertices of `C`, adjoining
the singleton branch sets `\{p\}` and `\{q\}` would give a `K_7` model:
`p,q` are adjacent to each other and to every cycle root.  This contradicts
the hypothesis on `G`.  \(\square\)

## 3. Unique five-colourability on at most six vertices

### Lemma 3.1

Let `H` be a graph on five or six vertices with chromatic number five.

1. If `|H|=5`, then `H=K_5`.
2. If `|H|=6`, then `H` is uniquely five-colourable up to permutation of
   the colours if and only if `H=K_6-e` for one edge `e`.

In either case, a uniquely five-colourable `H` contains a `K_5` subgraph.

#### Proof

The first assertion is immediate.

Suppose `|H|=6` and `chi(H)=5`.  Every proper five-colouring has exactly
one colour class of order two and four singleton classes.  The two vertices
in the nonsingleton class form a nonedge.  Conversely, every nonedge
`xy` gives a proper five-colouring: give `x,y` one colour and give the
remaining four vertices four distinct colours.  Hence the partition into
five colour classes is unique up to colour permutation exactly when `H`
has exactly one nonedge.  This is precisely `K_6-e`, and deleting either
end of its missing edge leaves a `K_5`.  \(\square\)

## 4. No rigid trace survives

### Theorem 4.1 (no rigid five-colour trace)

Under the setup of Section 1, there is no nonempty independent set
`I subseteq S` such that `G[S-I]` has chromatic number five and is uniquely
five-colourable up to permutation of colours.

#### Proof

If such an `I` existed, then `5<=|S-I|<=6`, because `I` is nonempty and
`|S|=7`.  Lemma 3.1 would give a `K_5` subgraph of `G[S-I]`, and hence of
`G[S]`.  This contradicts Lemma 2.1.  \(\square\)

### Corollary 4.2 (the rigid-boundary splice is vacuous here)

In the exact order-seven setting, the uniquely-five-colourable-trace
hypothesis of the rigid-boundary contraction splice can never be the live
closure mechanism.  If that hypothesis occurs, the two full components
already give the explicit `K_7`-minor model in (2.3).

## 5. Correct replacement target

The theorem rules out a strategically tempting but impossible target; it
does not synchronize the two closed-shore colourings.  Let
`Ext_L(S)` and `Ext_R(S)` denote the equality partitions of the literal
boundary induced by proper six-colourings of the two unmodified closed
shores.  In a hypothetical seven-chromatic graph,

\[
                         Ext_L(S)\cap Ext_R(S)=\varnothing.          \tag{5.1}
\]

If, in addition, every proper minor of `G` is six-colourable, a
proper-minor operation supported in one open shore returns a partition
which extends to the opposite unmodified closed shore but not to the
unmodified closed shore on which the operation was performed.  Thus the
two families of operation responses are polarized rather than
automatically convergent.

The appropriate conjectural replacement for a five-branch-set-supported
interface is therefore a **label-preserving opposite-response theorem**:
the five named branch sets and the literal operation witnesses must force
either

1. the same equality partition from operations in opposite open shores,
   and hence a six-colouring by gluing;
2. an explicit `K_7`-minor model; or
3. two vertices meeting every `K_5`-minor model.  By `HC_5`, deleting
   those vertices leaves a four-colourable graph, so two new colours give
   a six-colouring of `G`.  The promoted transversal theorem additionally
   yields an actual order-seven separation in the contraction-critical
   setup.

No assertion in this section proves that conjectural theorem.  Its point is
to record the correct dynamic target after Theorem 4.1 eliminates rigid
static traces.

## 6. Dependencies

- [exact-seven full-packet packing](hc7_exact_seven_packet_packing.md)
- [rigid-boundary contraction splice](hc7_near_k7_rigid_boundary_splice.md)
- [two-vertex `K_5`-model transversal yields an order-seven separation](hc7_k5_transversal_order7_separator.md)
