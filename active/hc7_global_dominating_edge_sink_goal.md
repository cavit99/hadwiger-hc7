# Dominating-edge sink programme

**Status:** the transition system and terminal-cycle rotation are proved.
The closure and sink-classification theorems in Section 4 are open.  This is
the current global proof mechanism, not a proof of `HC_7`.

## 1. Why this replaces local state accumulation

Let `G` be a hypothetical minor-minimal counterexample to `HC_7`.  For every
two-set `P`,

\[
                         \chi(G-P)\geq 5.                \tag{1.1}
\]

By Girão--Illingworth--Mohar--Norin--Steiner--Tamitegama--Tan--Wood--Yip,
`G-P` therefore contains a dominating `K_5` model.  Such a model can be
written

\[
                  (T_1,T_2,T_3,\{v\},\{w\}),            \tag{1.2}
\]

where `T_3` is a path and `G[T_3 union {v,w}]` is an induced cycle.
This gives a graph-global transition language whose states are literal
two-sets and, after one step, literal edges.  It does not remember an
adhesion, portal order, Moser labelling, or selected near model.

The published input is Theorem 1.1 and Corollary 1.2 of *The Dominating
4-Colour Theorem*, [arXiv:2605.10112](https://arxiv.org/abs/2605.10112).

## 2. The literal transition digraph

Define a directed graph `D_G` as follows.

* Its vertices are the two-subsets of `V(G)`.
* Put an arc `P -> {v,w}` when `G-P` has a normalized dominating `K_5`
  model of the form (1.2) whose last singleton bags are `v,w`.

Every head is an edge of `G`, and it is disjoint from the tail.  Equation
(1.1) and the published theorem imply that every state of a hypothetical
counterexample has positive out-degree.  Consequently `D_G` has a sink
strongly connected component, and every state in such a component is a
literal edge.

This is more than the earlier tautological response graph: its state set is
fixed by `G`, closure follows from a published theorem, and every transition
has the same literal five-row certificate.  Finiteness alone still does not
classify a sink.

## 3. Cycle closure inside one transition

Let (1.2) certify an arc from `P`, and put

\[
                         C=G[T_3\cup\{v,w\}].           \tag{3.1}
\]

For every edge `ab` of `C`,

\[
               (T_1,T_2,C-\{a,b\},\{a\},\{b\})        \tag{3.2}
\]

is again a dominating `K_5` model in `G-P`.  The remaining part of the
cycle is connected; each of `a,b` has its other cycle-neighbour there;
and `T_1,T_2` dominate every vertex of `C`.  Thus **every edge of `C` is an
out-neighbour of `P` in `D_G`**.

In particular, if `Sigma` is a sink component and `P in Sigma`, every
terminal cycle of every normalized witness for `P` has all its edges in
`Sigma`.  This is the first proved class-level closure in the programme.
It is reversible and therefore is not a strict scalar descent.  Moreover
`|Sigma|>=4`: each edge state has a vertex-disjoint cycle of at least three
further edge states inside `Sigma`.

## 4. The chromatic stratum and the next theorem

For an edge `e=xy`, vertex-criticality gives

\[
                 \chi(G-\{x,y\})\in\{5,6\}.            \tag{4.1}
\]

Call `e` **double-critical** in the first case and **six-residual** in the
second.  The set of six-residual edges is nonempty: if every edge were
double-critical, the theorem of Kawarabayashi--Pedersen--Toft for
double-critical seven-chromatic graphs would give a `K_7` minor.

The immediate theorem to prove is the following two-part sink closure.

> **Dominating-edge sink theorem.**  Let `G` be seven-connected, strongly
> seven-contraction-critical and `K_7`-minor-free.
>
> 1. If `e` is six-residual, some normalized dominating frame in `G-V(e)`
>    has a terminal-cycle edge `f` which is again six-residual; otherwise
>    the all-double-critical terminal cycle yields a literal `K_7` or one
>    fixed pair `P` with `G-P` `K_5`-minor-free.
> 2. Every sink component of the resulting six-residual transition system
>    yields a literal `K_7` or such a fixed pair.

Part 1 would make the chromatic stratum closed.  Part 2 is the class-level
composition theorem.  Together they contradict the existence of `G`.
Neither part is currently proved.

The first constructive subproblem is deliberately global and unlabelled:
take a shortest directed cycle in a sink and its sequence of dominating
frames.  In the first nontrivial composition case, a two-cycle `e <-> f`,
link the three early bags of the `e`-avoiding frame to the three early bags
of the `f`-avoiding frame in three label-distinct carriers.  This would give
the seven branch sets

\[
                  e\text{'s endpoints},\quad
                  f\text{'s endpoints},\quad
                  \text{three linked carriers},         \tag{4.2}
\]

or turn failure of that linkage into one pair meeting every near-Hajós
carrier.  For a longer directed cycle, the required theorem must either
shortcut it or compose all frames cyclically; two merely consecutive frames
do not have the four required terminal poles.  A further portal normal form
is not an admissible output.

There are two sharp guardrails.  An all-double-critical sink does not make
`G` double-critical: the published complete-minor theorem requires every
edge of `G` to be double-critical.  A sink containing a six-residual edge
regenerates an unrooted `K_6` in its deletion, but an arc supplies only an
existence witness in the old deleted graph; it does not exclude small
near-Hajós carriers after deleting the new edge.  Thus neither branch is
closed by existing literature.

## 5. Relation to the pair-height programme

The near-Hajós height `rho_G(P)` in
[`hc7_global_near_hajos_pair_height.md`](hc7_global_near_hajos_pair_height.md)
has the exact terminal value and geometrizes all four support-six types.
It remains a selection coordinate, because strict increase requires
excluding every smaller witness for a new pair.

The transition digraph supplies the missing composition layer: a pair
chooses a robust frame, its terminal cycle supplies successor edges, and a
sink packages all neutral rotations before any terminal classification is
attempted.  The intended global signature is therefore

\[
     (\text{condensation height in }D_G,\;
       \text{near-Hajós pair height},\;
       \text{minimum sink-cycle/frame complexity}).     \tag{5.1}
\]

Only the first coordinate is presently well-founded on non-sink moves.
The second and third coordinates become useful only after the sink theorem
is proved.  They must not be advertised as a completed invariant.
