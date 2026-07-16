# Global near-Hajós pair height

**Status:** proved elementary normalization and strategic audit; independent
audit pending.  The strict pair-exchange statement in Section 5 is open.
This note does not prove `HC_7`.

## 1. Definition and published input

Write `hat K_5` for the six-vertex graph obtained by splitting one vertex of
`K_5` into two adjacent degree-three vertices.  For a graph `G` and a
two-set `P`, define

\[
 \rho_G(P)=\min\{|V(J)|:J\subseteq G-P\text{ is a subdivision of }
                     K_5\text{ or }\widehat K_5\},
 \tag{1.1}
\]

with value infinity if there is no such subdivision, and put

\[
                         R_5(G)=\max_{|P|=2}\rho_G(P). \tag{1.2}
\]

Girão, Illingworth, Mohar, Norin, Steiner, Tamitegama, Tan, Wood and
Yip prove that every graph of chromatic number at least five contains a
subdivision of `K_5` or `hat K_5`; see *The Dominating 4-Colour Theorem*,
[arXiv:2605.10112](https://arxiv.org/abs/2605.10112), Corollary 1.2.

## 2. Exact terminal and first finite rung

### Proposition 2.1 (exact terminal)

If `G` is seven-connected and `P` is a two-set, then the following are
equivalent:

1. `rho_G(P)=infinity`;
2. `G-P` is planar;
3. `G-P` is `K_5`-minor-free.

In particular, any infinite-value pair gives a six-colouring of `G`.

### Proof

The graph `G-P` is five-connected.  If `rho_G(P)=infinity`, then in
particular `G-P` has no subdivision of `K_5`; the Kelmans--Seymour theorem
therefore makes it planar.  Conversely, both `K_5` and `hat K_5` are
nonplanar (`hat K_5` contracts to `K_5`), so a planar graph contains no
subdivision of either graph.  This proves 1 iff 2.  The equivalence of 2 and
3 follows from Wagner's four-connected form because `G-P` is
five-connected.  Finally colour `G-P` with four colours and give the two
vertices of `P` two fresh colours.  \(\square\)

### Proposition 2.2 (counterexample normalization)

Let `G` be a hypothetical minor-minimal counterexample to `HC_7`.  Then

1. `rho_G(P)` is finite for every two-set `P`; and
2. `R_5(G)>=6`.

### Proof

For every two-set `P`,

\[
                         \chi(G-P)\geq5.                \tag{2.1}
\]

The published near-Hajós corollary therefore makes `rho_G(P)` finite.
The audited literal-`K_5` transversal theorem supplies a two-set `P_0`
meeting every literal `K_5` in the `K_7`-minor-free graph `G`.  A witness
on five vertices could only be a literal `K_5`; `hat K_5` already has six
vertices.  Hence `rho_G(P_0)>=6`, proving the second assertion.  \(\square\)

The published corollary is not by itself a converse: a four-colourable graph
may contain either subdivision.  Exactness of Proposition 2.1 uses the
five-connectivity left after deleting `P`.

## 3. Exact agreement with minor support through order six

Let

\[
 \mu_G(P)=\min\{|V(\mathcal M)|:\mathcal M\text{ is a }K_5
                 \text{-model in }G-P\},               \tag{3.1}
\]

again with value infinity when appropriate.

### Theorem 3.1 (truncated-height identity)

For every graph `G` and every two-set `P`, with infinity truncated to seven,

\[
        \min\{\rho_G(P),7\}=\min\{\mu_G(P),7\}.         \tag{3.2}
\]

More explicitly:

* `rho_G(P)=5` iff `mu_G(P)=5`;
* `rho_G(P)=6` iff `mu_G(P)=6`; and
* `rho_G(P)>=7` iff `mu_G(P)>=7`.

When the common value is six, a six-vertex support can be normalized exactly
as follows.  With four singleton bags forming `Q=K_4` and edge-bag `xy`, put

\[
 D_x=\{q\in Q:xq\notin E(G)\},\qquad
 D_y=\{q\in Q:yq\notin E(G)\}.                          \tag{3.3}
\]

Up to interchanging `x,y`, the deficiency triple is one of

\[
 (1,1,2),\qquad(1,2,1),\qquad(1,3,0),\qquad(2,2,0).    \tag{3.4}
\]

The first three supports contain a `K_5` with one edge subdivided once.
In the fourth case `G[Q\cup\{x,y\}]` is literally `hat K_5`.

### Proof

Every allowed subdivision contains a `K_5` minor on the same support, so
`mu_G(P)<=rho_G(P)`.  On five vertices, either parameter is five exactly
when `G-P` contains a literal `K_5`.

Suppose `mu_G(P)=6`.  A minimum model has bag orders
`(2,1,1,1,1)`.  Its two-vertex bag is an edge `xy`, and its singleton bags
form a clique `Q`.  Since there is no support-five model, neither `x` nor
`y` is complete to `Q`; hence `D_x,D_y` are nonempty.  Model adjacency says
that every `q in Q` is adjacent to at least one of `x,y`, so
`D_x cap D_y` is empty.  The four possibilities in (3.4) follow.

In each of the first three types, orient so that `D_x={q}`.  The five branch
vertices `x` and `Q`, with the missing edge `xq` replaced by the path
`x-y-q`, form a six-vertex subdivision of `K_5`.  In type `(2,2,0)`, the
sets `D_x,D_y` partition `Q` into two pairs.  Thus the graph induced by the
six support vertices is exactly a `K_4`, the edge `xy`, and two complementary
two-edge attachments from `x,y` to the `K_4`: this is literal `hat K_5`.
Consequently `rho_G(P)<=6`; it cannot be five, so it equals six.

Conversely, a six-vertex allowed subdivision is itself a `K_5` minor on six
vertices.  If it had a support-five minor elsewhere then there would be a
literal `K_5`, which would give `rho_G(P)=5`; hence `rho_G(P)=6` implies
`mu_G(P)=6`.  These equivalences at five and six, together with
`mu_G(P)<=rho_G(P)`, give (3.2).  \(\square\)

Extra host chords cause no exception.  In a six-vertex `hat K_5` witness,
an extra split-vertex--`Q` edge either creates a literal `K_5` or moves the
support into one of the first three types, where the displayed one-edge
`TK_5` exists.  A direct enumeration of the three possible contact states
(`x` only, `y` only, or both) at each of the four clique vertices produces
only the four triples in (3.4).

This is the real advantage over the earlier `TK_5` height: `rho` gives
literal path/split geometry for the symmetric `(2,2,0)` rung as well.
Numerically, however, it is exactly the old minor-support height through the
only currently normalized rung.

## 4. Audit of the `L`-compatible dominating-model input

The same paper proves the following stronger induction statement.  If `L`
is an ordered clique of order at most two, then every non-four-colourable
graph has an `L`-compatible dominating `K_5` model.  For
`L=(v_1,v_2)`, compatibility only says

\[
 \operatorname{ind}(v_1)\leq1,\qquad
 \operatorname{ind}(v_2)\leq2,
\]

and, if `v_2` is in the second bag, `v_1` is in the first.

This is useful regeneration data, but it does **not** supply the missing
label-preserving pair exchange.

1. Either labelled vertex may be outside all five bags, so compatibility
   does not root the model at `L`.
2. Even when a label lies in an early bag, domination is supplied by the
   whole bag, not by that literal labelled vertex.
3. `L` must be a clique.  The globally selected deletion pair need not be
   adjacent and is absent from `G-P` in any event.
4. The corollary's extraction of a `K_4` subdivision and a minimal tree in
   the first bag may discard the labelled vertices.  It does not return a
   labelled near-Hajós subdivision.
5. Existence of one compatible model gives an upper bound on a witness
   size.  Strict pair exchange requires a lower bound for the new pair,
   namely exclusion of **every** smaller witness.

The contraction lemma in the paper does preserve this weak compatibility
when uncontracting a connected subgraph containing `v_1`, or a connected
subgraph of `N(v_1)` containing `v_2`.  This may be useful inside a future
decoder after a split edge has already been chosen.  It does not identify
the four singleton rows, force the labels to be used, or preserve a deleted
pair.  No stronger conclusion is justified by the published theorem.

### 4.1 Audited terminal-edge rotation

There is nevertheless one exact transition inside a normalized dominating
model.  As observed in the paper, it may be written

\[
                    (T_1,T_2,T_3,\{v\},\{w\}),          \tag{4.1}
\]

where `T_3` is a path and

\[
                         C=G[T_3\cup\{v,w\}]             \tag{4.2}
\]

is an induced cycle containing the edge `vw`.  For **every** edge `ab` of
`C`,

\[
             (T_1,T_2,C-\{a,b\},\{a\},\{b\})           \tag{4.3}
\]

is again a dominating `K_5` model.  Indeed, deleting the endpoints of an
edge from a cycle leaves a connected path.  Each of `a,b` has its other
cycle-neighbour in that path, while `ab` supplies the last singleton
adjacency.  Finally `T_1,T_2` dominate every vertex of `C` because they
dominated all three later parts in (4.1).

Thus one may define, for fixed `G-P`, a graph-global terminal-edge transition
system whose states are edges occurring as the last two singleton bags of
some normalized dominating model; every cycle `C` in (4.2) supplies a
reversible family of rotations among all its edges.

This does not yet orient the proof.  The pair `P`, the support union, and
`rho_G(P)` are unchanged.  More sharply, every certificate in (4.3) uses
**every** edge of `C`: its edges are distributed among the middle path, the
two middle-to-singleton contacts, and the last singleton edge.  Hence
rotating the terminal edge does not produce a model in `G-f` for a prescribed
edge `f` of `C`, nor a model avoiding an endpoint of `f`.  To make the
transition system useful one still needs an overlap/exchange theorem between
distinct normalized cycles which either survives a prescribed proper-minor
operation or changes the literal deletion pair with a verified height gain.

## 5. Monotonicity falsification and exact remaining exchange

The number `rho_G(P)` is unchanged by every model rerouting, adhesion move,
or colouring transition that keeps the graph and literal pair `P` fixed.
A strict increase can only come from a new pair `P'`, and proving it means
excluding every near-Hajós witness below the old threshold in `G-P'`.
Constructing or rerouting one witness can never establish that exclusion.

There is no minor-operation monotonicity to exploit.  Write `rho_0(H)` for
the analogue of (1.1) with no deleted pair.  Let `J` be `K_5` with one edge
subdivided once.  Then `rho_0(J)=6`.  Contracting either segment of
the subdivided edge gives a literal `K_5`, lowering the value to five.  By
contrast, deleting any edge of `J` leaves at most ten edges, no literal
`K_5`, and no six-vertex subdivision of `K_5` or `hat K_5` (each such
six-vertex graph has eleven edges), raising the value to infinity.  Thus
deletion and contraction move the proposed height in opposite directions.
This example is not an `HC_7` host; it rules out invariant-only monotonicity,
not a transition theorem using all counterexample hypotheses.

Finally, selecting `P` to maximize `rho_G(P)` makes a conclusion

\[
 K_7,\quad \rho_G(P')=\infty,\quad\text{or}\quad
 \rho_G(P')>\rho_G(P)                                  \tag{5.1}
\]

an `HC_7`-closing theorem at once.  The third outcome is impossible at the
maximizer and the first two are terminal.  Hence (5.1) is not yet a
well-founded engine; it is the missing exchange theorem itself.

The exact first-rung target exposed by this normalization is:

> **Near-Hajós two-transversal pullback.**  Starting from a globally
> maximizing pair `P` with `rho_G(P)=6` and its literal one-edge-`TK_5` or
> `hat K_5` support, couple a proper-minor colouring response to the named
> split vertices and four clique rows so as to produce a literal `K_7`, an
> infinite-value pair, or a new pair `P'` meeting every six-vertex near-Hajós
> support.

The last alternative is equivalently `mu_G(P')>=7` by Theorem 3.1.  The
published dominating-model theorem supplies neither the named coupling nor
the universal hitting conclusion.  Those remain the precise gap.
