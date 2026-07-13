# Terminal-free low-cut descent

**Status:** proved and independently audited.  This is a
label-preserving gate exchange, not a contact-count surrogate for an
attained boundary duty.

## 1. Setting

Retain all hypotheses and notation from Section 1 of
`../results/hc7_exact7_terminal_free_state_or_rural.md`, including the
supported pair decoration `W={w} union L`, the partition of `U` by the
three core traces, and the anticompleteness of `L` to `A union B`.  In
particular, use the exact terminal-free shore

\[
                         J^\circ=G[D_t\cup U].                 \tag{1.1}
\]

Let `K_0,A,B` be the original supported core.  Assume explicitly that
`K_0` is three-connected, has trace `{x,y}`, and that `A,B` are connected,
adjacent, and carry the other two traces, so the three traces partition
`U`.  Put

\[
 X_0=A\cup B,\qquad Y_0=L.                              \tag{1.2}
\]

The inherited literal contacts satisfy

\[
 \begin{aligned}
 |N_{K_0}(X_0)-\{x,y\}|&\ge3,\\
 |N_{K_0}(Y_0)-\{x,y\}|&\ge3.                         \tag{1.3}
 \end{aligned}
\]

Consider spanning triples

\[
                 V(J^\circ)=K\mathbin{\dot\cup}X
                                  \mathbin{\dot\cup}Y           \tag{1.4}
\]

such that the three induced parts are connected, `X,Y` are anticomplete,
`K_0 subseteq K`, `X_0 subseteq X`, and `Y_0 subseteq Y`.  Component
absorption supplies at least one such triple whenever `X_0,Y_0` lie in
distinct components of `J^circ-V(K_0)`.  Every triple in (1.4) has carrier
trace `{x,y}` and retains both bounds (1.3).

Choose a triple (1.4) minimizing `|K|`.

## 2. A leaf side away from a three-connected core

### Lemma 2.1 (trace-free low-cut side)

If `K` is not three-connected, there is a nonempty connected set
`C subseteq K-K_0` such that

\[
             K-C\text{ is connected},\qquad |N_K(C)|\le2.       \tag{2.1}
\]

#### Proof

If `K` has a cutvertex `z`, root its block--cutvertex tree at the unique
block-subtree containing the three-connected graph `K_0`, and take an
end component away from that root.  Its vertices excluding `z` form a
connected set `C`; deleting `C` leaves a connected graph, and
`N_K(C)={z}`.  The graph `K_0` lies wholly on the retained side because a
cutvertex cannot separate two vertices of a three-connected graph.

Now suppose `K` is two-connected but not three-connected.  Choose a
two-cut `{r,s}`.  The graph `K_0-{r,s}` is connected, so it lies in one
component `H` of `K-{r,s}`.  Choose any other component `C`.  In a
two-connected graph every component of `K-{r,s}` has a neighbour at both
`r` and `s`; hence the union of `H`, `{r,s}`, and all components other
than `C` is connected.  Thus `K-C` is connected and
`N_K(C)={r,s}`.  Again `C` contains no vertex of `K_0`.  This proves
(2.1). \(\square\)

## 3. Gate descent

### Theorem 3.1 (low cut gives descent or state-faithful promotion)

For the carrier-minimal triple (1.4), either `K` is three-connected or
there is a trace-preserving supported core in which
`W'={w} union Y` contacts the retained pair block and one named target
block.  The target is the named side containing the selected `C-X` edge;
it is not asserted to be a preselected one of `A,B`.  If that target trace
is admissible, the operation attains the corresponding supported state in
addition to the retained pair state.  If it is inadmissible, the same
operation exposes the corresponding literal boundary-incompatibility
certificate.

#### Proof

Assume `K` is not three-connected and take `C` from Lemma 2.1.  It is a
nonempty subset of the open shore `D_t`.  Since (1.4) spans `J^circ`,
the exact terminal-shore exposure gives

\[
 N_G(C)\subseteq N_K(C)\cup N_X(C)\cup N_Y(C)\cup\{w,t\}.       \tag{3.1}
\]

If `C` sees neither `X` nor `Y`, then (2.1)--(3.1) give
`|N_G(C)|<=4`.  The set `N_G(C)` separates nonempty `C` from `v`,
contrary to seven-connectivity.

Suppose `C` sees exactly one pole, say `X`.  Replace

\[
                   (K,X,Y)\longmapsto(K-C,X\cup C,Y).            \tag{3.2}
\]

Both new parts in (3.2) are connected by (2.1) and the literal `C-X`
edge.  They are anticomplete to `Y` because `C` has no `Y`-neighbour.
The fixed sets `K_0,X_0,Y_0` remain in their named parts, so the traces
and both inherited portal bounds (1.3) remain.  Thus (3.2) is another
eligible spanning triple with smaller carrier, contradicting minimality.
The case in which `C` sees only `Y` is symmetric.

It remains that `C` sees both `X` and `Y`.  Apply the endpoint-faithful
target partition from the terminal-free theorem to write

\[
                         X=A'\mathbin{\dot\cup}B'                \tag{3.3}
\]

as two connected adjacent sets containing `A,B`, respectively.  Fix one
literal `C-X` edge, let `M' in {A',B'}` be the part containing its
`X`-end, and let `N'` be the other part.  Define

\[
                         K'=K-C,\qquad M''=M'\cup C.             \tag{3.4}
\]

The sets `K',M'',N'` are disjoint and connected.  They are pairwise
adjacent: `M''-N'` retains the literal edge between the two parts of
(3.3), while the old `K_0-A` and `K_0-B` edges give the two adjacencies
from `K'` to the enlarged named targets.  No adhesion vertex lies in `C`,
so all three traces are unchanged.

The set `W'={w} union Y` is connected, avoids the side terminal, and has
trace `{w}`.  It contacts `M''` through the literal `Y-C` edge.  It also
contacts `K'`: the original set `N_{K_0}(L)-{x,y}` from (1.3) remains in
`K_0 subseteq K'`, while `L subseteq Y`.  Hence `W'` has literal contact
with the retained pair block and the named target.  This is the claimed
state-faithful promotion; admissibility depends only on the unchanged
target trace, and its failure is the stated boundary certificate.
\(\square\)

## 4. Consequence

After minimizing the carrier, the low-cut outcome of the spanning-rural
quadrichotomy is impossible unless the desired state promotion (or its
literal boundary-incompatibility certificate) has already occurred.
Combining Theorem 3.1 with the audited terminal-free state-or-rural theorem
leaves only the terminal-free rural-page outcome:

\[
 \boxed{\text{state-faithful promotion/boundary certificate, or a planar
 two-pole quotient spanning }J^\circ.}
\]

The promotion is one literal attained rank-two state on this shore.  It
does not itself assert that the opposite shore supports the same named
target; that remains a bilateral state-matching obligation.

The remaining rural task is induced-pole expansion, or conversion of a
pole-rotation obstruction to `K_7`, a common bilateral state, or the
terminal-free planar-colouring endgame.  Reinsertion of `t` is unnecessary
by `hc7_exact7_terminal_free_bilateral_endgame.md`.
