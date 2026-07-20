# A symmetric two--three allocation in the three-vertex reversal case

**Status:** written proof; separate internal audit **GREEN** in
[`hc7_order8_strict_reversal_d_side_allocation_audit.md`](hc7_order8_strict_reversal_d_side_allocation_audit.md).
This is an unbounded conditional reduction inside the connected order-eight interface.
It does not prove `HC_7`.  The strict connected-subgraph reduction below is
host-measured, but it is not asserted to reproduce the full order-eight
interface on the smaller subgraph.

## 1. Setting

Assume the setting of the audited
[ordered two--three allocation theorem](../results/hc7_order8_ordered_two_three_allocation.md),
including

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad E_G(L,R)=\varnothing,
\]

the boundary

\[
 S=\{d,e,x_d,y_d,x_e,y_e,x_0,y_0\},
\]

the two boundary triangles

\[
 d x_d y_d d,\qquad e x_e y_e e,
\]

and adjacent disjoint connected subgraphs `P_0,P_1` in `R`, each adjacent
to every vertex of `S`.  Let

\[
                         L=E\mathbin{\dot\cup}D
\]

be the induced connected normalization in which `E,D` are adjacent,
`E` is adjacent to every boundary vertex except `e`, and `D` is adjacent
to every boundary vertex except `d`.

Suppose the unresolved three-vertex alternative has its exact endpoint
reversal form:

\[
 V(E)=\{a,b,c\},\qquad G[E]\text{ is the induced path }a b c,
 \qquad N_E(x_d)=N_E(y_d)=\{a\},
\]

and

\[
 N_E(w)=\{c\}
 \quad\text{for every }w\in\{x_e,y_e,x_0,y_0\}.       \tag{1.1}
\]

Every member of `E` is adjacent to `d` and has a neighbour in `D`.
For a vertex `v` outside `D`, write

\[
                             Q_v=N_G(v)\cap D.          \tag{1.2}
\]

The relevant five portal sets are

\[
                    Q_a,\quad Q_e,\quad Q_b,
                    \quad Q_{x_d},\quad Q_{y_d}.        \tag{1.3}
\]

## 2. The minimum-degree information

### Lemma 2.1

\[
                             |Q_a|\ge3,
                    \qquad  |Q_b|\ge4.                 \tag{2.1}
\]

All five sets in (1.3) are nonempty.

### Proof

Every vertex of a hypothetical minor-minimal counterexample has degree at
least seven.  Outside `D`, the neighbours of `a` are exactly

\[
                         b,d,x_d,y_d,
\]

so `a` has at least three neighbours in `D`.  Outside `D`, the neighbours
of `b` are exactly

\[
                             a,c,d,
\]

so `b` has at least four neighbours in `D`.  The sets `Q_a,Q_b` are
therefore nonempty.  The normalization makes `D` adjacent to each of
`e,x_d,y_d`, proving nonemptiness of the other three sets. \(\square\)

## 3. The positive allocation

We use the same five-terminal theorem as the preceding ordered allocation.
For five distinct terminals

\[
                        r_1,r_2,r_3,p_1,p_2
\]

in a graph `F`, its **Xie completion** adds the edge `p_1p_2` and every
edge `r_i p_j`.  If the completion is six-connected, the original graph
contains disjoint connected subgraphs containing respectively the three
`r_i` and the two `p_j`.

### Theorem 3.1 (the symmetric allocation closes)

Suppose the five sets in (1.3) have distinct representatives

\[
 p_a\in Q_a,\quad p_e\in Q_e,\quad p_b\in Q_b,
 \quad p_x\in Q_{x_d},\quad p_y\in Q_{y_d}.            \tag{3.1}
\]

Form the Xie completion of `G[D]` with terminal pair `(p_a,p_e)` and
terminal triple `(p_b,p_x,p_y)`.  If this completion is six-connected,
then `G` contains an explicit `K_7`-minor model.

### Proof

The five-terminal theorem gives vertex-disjoint connected subgraphs
`T,B` of `G[D]` such that

\[
             \{p_a,p_e\}\subseteq V(T),
 \qquad      \{p_b,p_x,p_y\}\subseteq V(B).            \tag{3.2}
\]

Define

\[
                 U=V(T)\cup\{a,e\},
 \qquad          V=V(B)\cup\{b,c,x_e\}.                \tag{3.3}
\]

Both sets induce connected subgraphs.  For `U`, use the contacts
`a p_a` and `e p_e`.  For `V`, use `b p_b`, the edge `bc`, and the edge
`c x_e` from (1.1).  The two subgraphs are adjacent through the edge
`ab`.

Now take the seven branch sets

\[
       P_0,\quad P_1,\quad \{d\},\quad \{x_d\},
       \quad \{y_d\},\quad U,\quad V.                  \tag{3.4}
\]

They are pairwise disjoint and connected.  The first two are adjacent and
are adjacent to every later branch set through the displayed boundary
vertices `d,x_d,y_d,e,x_e`.  The three singleton sets form the triangle
`d x_d y_d d`.  The set `U` is adjacent to all three through `a`.  The
set `V` is adjacent to `d` through `b`, and to `x_d,y_d` through
`p_x,p_y`.  Finally `U,V` are adjacent through `ab`.  Hence (3.4) is a
`K_7`-minor model. \(\square\)

The point of (3.3) is that the four apparent obligations on the second
connected subgraph are illusory.  The boundary vertex `e` is absorbed with
the `a`-connector, while `x_e` is absorbed with the `b,c`-connector.  What
remains inside `D` is exactly a two--three allocation.

## 4. Failure of distinct representatives

### Lemma 4.1 (a separator of order at most nine)

If the five portal sets in (1.3) have no system of distinct
representatives, then at least one of the following holds.

1. `|D|\le4`.
2. There is a nonempty connected proper set `C\subset D` such that

   \[
                              |N_G(C)|\le9.             \tag{4.1}
   \]

   In particular, seven-connectivity forces
   `7\le |N_G(C)|\le9`.

### Proof

Hall's theorem gives a subfamily `I` of (1.3) whose union

\[
                              Z=\bigcup_{Q\in I}Q
\]

satisfies `|Z|\le |I|-1`.  If `D=Z`, then
`|D|\le |I|-1\le4`, giving outcome 1.

Otherwise let `C` be a component of `G[D-Z]`.  Then
`N_D(C)\subseteq Z`.  Every neighbour of `C` outside `D` lies in

\[
                         E\cup(S-\{d\}),                \tag{4.2}
\]

a set of order ten.  Moreover `C` misses the distinct member of (4.2)
whose portal set belongs to `I`.  Consequently

\[
 |N_G(C)|
   \le |Z|+10-|I|
   \le9.                                                \tag{4.3}
\]

The set `N_G(C)` is an actual separator: `C` is nonempty and `R` survives
outside `C\cup N_G(C)`.  Seven-connectivity gives its lower bound seven.
\(\square\)

Thus Hall failure is not another unstructured portal case.  It either has
bounded `D`-order or returns an actual separator with excess at most two.
The lemma does not align colourings on an order-seven boundary.

## 5. Failure of six-connectivity

### Lemma 5.1 (strict connected-subgraph reduction)

Retain distinct representatives (3.1).  If `|D|\ge7` and the selected
Xie completion is not six-connected, there are a nonempty connected proper
set `C\subset D` and a set `K\subseteq D` of order at most five such that

\[
                             N_D(C)\subseteq K.          \tag{5.1}
\]

The full neighbourhood

\[
 B_C=N_G(C)
     =N_D(C)\mathbin{\dot\cup}N_E(C)
        \mathbin{\dot\cup}(N_G(C)\cap(S-\{d\}))        \tag{5.2}
\]

is the boundary of an actual separation of `G`.  In particular

\[
                              |C|<|D|.                  \tag{5.3}
\]

### Proof

The completed graph has a separation with separator `K` of order at most
five and two nonempty open sides.  The completion changes no vertex set and
only adds virtual edges, so every component `C` of either open side in the
original graph `G[D]` satisfies (5.1).  It is nonempty and proper because
the opposite open side is nonempty.  The partition `L=E\dot\cup D`, the
absence of `L`--`R` edges, and the fact that `D` misses `d` give (5.2).
The set `R` survives outside `C\cup B_C`, so `B_C` is an actual separation
boundary.  Strictness (5.3) is immediate. \(\square\)

The reduction (5.3) is measured in the literal host graph, not in a
virtual completion.  It is not yet a recursive induction: the theorem does
not claim that `C` is adjacent to all seven required boundary labels or
that the original portal partition is reproduced on `B_C`.

### Proposition 5.2 (the operation-specific response is retained)

Let `pi` be the equality partition induced on `B_C` by the fixed merged-root
six-colouring of `G[L\cup S]`.  For every edge `uv` with
`u\in C` and `v\in B_C`, every six-colouring of the proper minor `G-uv`
satisfies

\[
                               c(u)=c(v),                \tag{5.4}
\]

and its restriction to `G-C` induces on `B_C` an equality partition
different from `pi`.

### Proof

If a six-colouring of `G-uv` assigned different colours to `u,v`, restoring
the edge would six-colour `G`; this proves (5.4).  If the restriction to
`G-C` induced `pi` on `B_C`, permute its colour names to agree on `B_C`
with the fixed colouring of `G[C\cup B_C]`.  The two colourings would glue
to a six-colouring of `G`, a contradiction. \(\square\)

## 6. Exact gain and trust boundary

The unique three-vertex endpoint-reversal case now has the following
unbounded dichotomy.

- A six-connected symmetric Xie completion gives the explicit branch sets
  (3.4).
- Hall failure gives `|D|\le4` or an actual separator of order at most nine.
- Failure of six-connectivity for `|D|\ge7` gives a strict literal
  connected-subgraph reduction inside `D`, together with the incompatible
  proper-minor boundary responses of Proposition 5.2.

The remaining cases are therefore the bounded orders `|D|\le6`, the
order-seven to order-nine separator-colouring problem from Lemma 4.1, and
the label-preserving recursion problem after Lemma 5.1.  In particular,
this note does **not** prove that the strict set `C` is another complete
order-eight instance, and it does not prove that an order-seven separator
carries one common boundary partition on both closed shores.
