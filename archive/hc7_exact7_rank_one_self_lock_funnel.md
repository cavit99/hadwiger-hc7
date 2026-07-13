# Rank-one self-locks funnel into literal owner adhesions

**Status:** proved in the exact-order-six cell, conditional on the audited
bilateral Kempe-lock lemma.  This is not a closure of the cell.  It shows
exactly where seven-connectivity first improves the static self-retracing
Kempe obstruction: every non-direct self-lock selects a connected region
with at least five contacts in its literal owner block.  Existing labelled
peels then close all duty-correct pendant-lobe, two-connected singleton,
and three-connected pair instances described below.

## 1. Setting

Use the exact-order-six cell and notation of
`../results/hc7_exact7_bilateral_decoration_kempe_lock.md`.  Thus the two open shores
`D_1,D_2` are anticomplete, their common adhesion is

\[
                       T=U\mathbin{\dot\cup}\{w\},
\]

and each side has the same labelled three-block frame

\[
                       C_1^s,C_2^s,C_3^s\qquad(s=1,2).
\]

Assume that all three decorations are admissible and that the full support
sets have rank-one mismatch

\[
                       \Sigma _1=\{p\},\qquad
                       \Sigma _2=\{q\},\qquad p\ne q.       \tag{1.1}
\]

Write `o_s` for the owner on side `s`, so `o_1=p,o_2=q`, and put
`K_s=C_{o_s}^s`.  Let `t_s` be the side terminal.  A **residual
`w`-component** on side `s` is a component `L` of

\[
 D_s-\bigl(C_1^s\cup C_2^s\cup C_3^s\bigr)                 \tag{1.2}
\]

having a neighbour at `w`.  Only open-shore vertices are meant in (1.2);
the literal roots in the traces of the core blocks are not vertices of
`D_s`.

## 2. The owner-lock funnel

### Theorem 2.1 (componentwise owner lock)

Under (1.1), the following statements hold.

1. The vertex `w` is anticomplete to `U\cup\{a,b,v\}`.  Consequently

   \[
          |N_{D_1}(w)|+|N_{D_2}(w)|=d_G(w)\ge7.             \tag{2.1}
   \]

2. Every edge from `w` to a fixed core block on side `s` ends in the owner
   block `K_s`.

3. Every residual `w`-component `L` on side `s` satisfies

   \[
        N_G(L)\subseteq K_s\cup\{w,t_s\},\qquad
        |N_G(L)\cap K_s|\ge5.                              \tag{2.2}
   \]

4. The owned first-hit Kempe path on side `s` either is the literal edge
   `wK_s`, or, after deleting its first and last vertices, lies in one
   residual `w`-component satisfying (2.2).

#### Proof

All three frame traces partition `U`.  Their simultaneous admissibility
therefore says exactly that `w` has no neighbour in `U`.  The audited
literal portal restriction gives `wa,wb\notin E(G)`, and `wv` is absent
because `w\notin N(v)`.  Exact exhaustion leaves only the two open shores,
which proves (2.1) using `\delta(G)\ge7`.

If `w` had an edge to `C_h^s` with `h\ne o_s`, the one-vertex set `{w}`
would be a connected witness, disjoint from the core and the side terminal,
supporting the admissible decoration `h`.  This contradicts the definition
of the **full** set `\Sigma_s`.  This proves statement 2.

Let `L` be a residual `w`-component.  If it had an edge to `C_h^s` with
`h\ne o_s`, then `{w}\cup L` would be a connected witness of exact trace
`{w}` supporting `h`, again contradicting (1.1).  Distinct components in
(1.2) are anticomplete.  The exact terminal separation excludes `v`, the
opposite terminal, and the opposite shore.  Hence every neighbour of `L`
lies in `K_s\cup\{w,t_s\}`, proving the containment in (2.2).

The set `N_G(L)` separates the nonempty set `L` from `v`.  Seven-
connectivity gives `|N_G(L)|\ge7`; at most `w,t_s` lie outside `K_s`.
This proves the five-contact inequality.

Finally take the shortest first-hit path supplied by the audited
bilateral Kempe-lock lemma.  Its internal vertices avoid all fixed core
blocks and the side terminal.  If it has no internal vertex it is a direct
`wK_s` edge.  Otherwise all vertices between `w` and its first core hit
belong to one component of (1.2), and its first edge makes that component
a residual `w`-component.  Statement 3 applies.  \(\square\)

The importance of (2.2) is label-faithful: the five contacts are all in
the actual owner block, not merely in vertices having the owner's colour.

## 3. Exact duty-correct exits

Fix a side `s`.  Let `M_s=C_{o_{3-s}}^s` be the block carrying the
opposite side's owner label, and let `R_s` be the third block.  A promotion
to `M_s` gives the same literal decorated trace on both shores and hence
six-colours `G` by the audited bilateral decorated-overlap theorem.

Let `Z` be either `{w}` in the direct case or `{w}\cup L` for a residual
component.  Put

\[
                         P=N_G(Z-\{w\})\cap K_s              \tag{3.1}
\]

in the residual case, and `P=N_G(w)\cap K_s` in the direct case.  In the
residual case `|P|\ge5` by Theorem 2.1.

### Proposition 3.1 (duty-correct protected-lobe exit)

Choose an endpoint `r_R\in K_s` of a `K_s-R_s` edge and an
inclusion-minimal tree `Q_R\subseteq K_s` containing the whole trace of
`K_s` and `r_R`.  If a component `C` of `K_s-V(Q_R)` contains both

* a member of `P`, and
* the `K_s` endpoint of an edge to `M_s`,

then `G` is six-colourable.

#### Proof

Apply the audited pendant-lobe decoration promotion with

\[
                 K=K_s,\quad L=R_s,\quad M=M_s,\quad W=Z.
\]

It replaces `K_s` by `K_s-C` and replaces `M_s` by
`M_s\cup C\cup Z`.  The three new blocks are connected, disjoint, and
pairwise adjacent; their traces are the old traces with `w` adjoined
legally to the trace of `M_s`.  The opposite shore already supports that
same decoration by (1.1).  Bilateral transfer aligns the states and
six-colours `G`.  \(\square\)

Thus, in a surviving self-lock, for **every** protected choice `Q_R`, no
`P`-hit pendant lobe contains a portal to the opposite owner.  This is an
exact gate statement.  It does not forbid portals to the irrelevant third
block and does not replace the attained duty by raw defect.

Two internally well-connected versions follow from the audited carrier
peels.

### Proposition 3.2 (singleton-owner exit)

Suppose `K_s` has singleton trace, is two-connected, and `|P|\ge2`.  If a
nontrace vertex of `K_s` has an edge to `M_s`, then `G` is six-colourable.

#### Proof

The two-connected singleton-carrier peel partitions `K_s=X\dot\cup Y`
with the trace in `Y`, both parts meeting `P`, and `X` adjacent to `M_s`.
Replace `M_s` by `M_s\cup X` and `K_s` by `Y`, then merge the connected
set `Z` into the enlarged `M_s` block.  This realizes the opposite-owner
decoration on side `s`; the opposite side already supports it.  Apply
bilateral transfer.  \(\square\)

### Proposition 3.3 (pair-owner exit or rail capture)

Suppose `K_s` has pair trace `{x,y}`, is three-connected, and `|P|\ge2`.
Either `G` is six-colourable, or both of the following hold:

1. no member of `P-\{x,y\}` has an edge to `M_s`; and
2. for every nontrace `M_s`-portal `z\in K_s` and every nonseparating
   `x-y` path avoiding `z`, that path contains all of `P`.

#### Proof

If clause 1 fails, the audited three-connected pair-carrier peel toward
`M_s` applies.  If clause 2 fails, its generalized nonseparating-path form
applies.  In either case the resulting labelled peel has both parts meeting
`P`; merging `Z` into the enlarged `M_s` block realizes the common
opposite-owner decoration exactly as in Proposition 3.2.  \(\square\)

For a residual self-lock, equality in the five-contact bound gives one
further literal output.  If `|P|=5`, then seven-connectivity and (2.2)
force

\[
                        N_G(L)=P\cup\{w,t_s\},                 \tag{3.2}
\]

so (3.2) is an actual separation of order seven.  This is **not** claimed
to be colour-gluable without an attained common boundary state.  If
`|P|\ge6`, the live object is instead a six-plus-contact owner gate.

## 4. Why witness minimality does not complete the descent

The static certificate in
`../barriers/hc7_exact7_two_shore_kempe_pairing_barrier.md` already has
lexicographically minimum cores and witnesses for its fixed frame.  Each
missing pair needs its displayed length-two realization, and the supported
`w`-witness on each side has minimum possible length.  Nevertheless the
first-hit Kempe path on each side simply follows that witness back into its
already owned block.  It produces no shorter witness, opposite-owner
portal, or new branch set.

That graph is not seven-connected.  The precise place where the actual
`HC_7` hypotheses improve it is Theorem 2.1(3): its one-vertex residual
region has only one owner contact, whereas every genuine non-direct
self-lock region has at least five.  Propositions 3.1--3.3 spend those
contacts whenever they are distributed in a duty-correct movable way.
What remains is exact rather than rhetorical:

* a direct owner hit trapped in the protected central core; or
* a residual region behind an exact-seven owner adhesion or at least six
  owner contacts, with every opposite-owner portal separated from its
  attachment set as in Proposition 3.1; and, in a three-connected pair
  block, the universal rail-capture condition of Proposition 3.3.

No lexicographic potential alone eliminates these configurations.  A
further proof must use a proper-minor state transition across the displayed
literal gate, or compose the two gated owner systems bilaterally.  This
note does not assert that either operation is automatic.
