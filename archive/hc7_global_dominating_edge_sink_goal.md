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

### 3.1 Common-host refinement of every sink arc

Let the tail itself be an edge `e=xy`, let `C` be a terminal cycle for
`e`, and let `f=uv` be any edge of `C`.  The edges `e,f` are
vertex-disjoint.  Put

\[
                         H_f=G-\{e,f\},                \tag{3.3}
\]

where (3.3) means edge deletion.  Seven-connectivity makes every `H_f`
connected.  The audited common edge-deletion fork gives at least one of the
following usable substrates:

1. the four endpoints of `e,f` induce a literal `K_4` in `G`; or
2. `chi(H_f)=6` and `H_f` contains a spanning `K_6` model.

In the second case, every six-colouring of `G-f=H_f+e` restricts to the
edge signature `(e proper,f equal)`, every six-colouring of
`G-e=H_f+f` restricts to `(e equal,f proper)`, and no six-colouring of
`H_f` makes both edges proper.  Identifying the equal pair gives the two
named contraction responses.

Independently of which fork branch is used, strong minor-criticality also
colours the simultaneous contraction
`G/e/f`.  Expanding it gives an `(equal,equal)` colouring in `H_f`.  The
audited whole-component switching theorem implies that, in this one shared
colouring, one of `e,f` has at least three bichromatic locks, or at least
four when the two equality colours differ.  Separately, each of the two
one-edge responses gives four common-host locks for its equal pair.  These
lock paths are literal; different palettes may still share vertices of the
common equality colour.

Thus a sink terminal cycle carries a whole **cycle of common state/lock
certificates**.  Every edge has the endpoint-`K_4` or common-six-row fork,
and every edge has the simultaneous state and lock allocation; the two fork
outcomes may coexist.  This is a graph-global strengthening of
terminal-cycle closure, but still not a row allocation or a monotone
transition.

### 3.2 Whole-cycle synchronization on an even terminal cycle

The preceding certificates choose one cycle edge at a time.  When `C` is
even, the audited whole-cycle contraction theorem removes that choice.
Contract `C` to one vertex and expand a six-colouring of `G/C` to
`G-E(C)`.  If `C_0,C_1` are the two cyclic parity classes, then for every
alternate colour a bichromatic component meets both classes; after also
deleting the sink edge `e`, at least four of those components survive in
one common colouring.  Shortest paths in them have their interiors outside
`C`.

Source: [terminal-cycle contraction and synchronized parity
locks](../results/hc7_terminal_cycle_contraction_parity_locks.md), with its
[audit](../results/hc7_terminal_cycle_contraction_parity_locks_audit.md).

This is the first certificate attached to the whole terminal cycle rather
than to independently coloured arcs.  It still does not give disjoint
paths: different palettes may share vertices of the common cycle colour.
It also gives no conclusion for an odd cycle, where a two-colour
alternation around `C` is impossible for parity reasons.

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

The first constructive subproblem is now one whole terminal cycle, not two
locally chosen frames.  Fix a sink edge `e` and a shortest terminal cycle
`C`.  For every `f in E(C)`, use the literal endpoint-`K_4` branch or the
spanning common model in `H_f`.  The required composition theorem must
either:

1. decode one endpoint `K_4` together with the dominating frame into a
   literal `K_7` or fixed pair;
2. split or reselect one common `K_6` model label-faithfully under the
   opposite edge signatures; or
3. use the cyclic family of failed splits to produce a six-residual
   successor with a verified strict near-Hajós height increase.

Two consecutive models, an unranked row rotation, or another portal normal
form is not an admissible output.

For even `C`, the first attack must use the synchronized parity-lock family
of Section 3.2 and prove a disjoint/labelled composition or identify its
common obstruction.  For odd `C`, the first attack is a three-colour or
interval-contraction lift.  Repeating the pairwise lock theorem around the
cycle is no longer an adequate next step in either branch.

There are two sharp guardrails.  An all-double-critical sink does not make
`G` double-critical: the published complete-minor theorem requires every
edge of `G` to be double-critical.  A sink containing a six-residual edge
regenerates an unrooted `K_6` in its deletion, but an arc supplies only an
existence witness in the old deleted graph; it does not exclude small
near-Hajós carriers after deleting the new edge.  Thus neither branch is
closed by existing literature.

Source for Section 3.1: [common edge-deletion chromatic fork and `K_6`
regeneration](../results/hc7_common_edge_deletion_k6_fork.md), with its
[independent audit](../results/hc7_common_edge_deletion_k6_fork_audit.md),
and [common-host double-contraction lock allocation](../results/hc7_common_host_double_contraction_lock_allocation.md),
with its [audit](../results/hc7_common_host_double_contraction_lock_allocation_audit.md),
and [terminal-cycle contraction and synchronized parity locks](../results/hc7_terminal_cycle_contraction_parity_locks.md),
with its [audit](../results/hc7_terminal_cycle_contraction_parity_locks_audit.md).

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
