# Sole-exterior reserved-connector failure certificate

**Status:** proved and independently audited.

## Setting

Let `G` be seven-connected, let `v` have the pure-Moser neighbourhood
`S=N(v)`, and suppose `C=G-N[v]` is the sole nonempty exterior component.
Let `X,Y` be disjoint connected subgraphs of `C` (in the intended
application they are adjacent complementary four-corner carriers), and put

\[
                             B=X\cup Y.
\]

For a component `R` of `C-B`, define its literal boundary support and its
carrier attachment set by

\[
 A_R=N_G(R)\cap S,
 \qquad
 T_R=N_G(R)\cap B.
\]

## Lemma 1 (exact adhesion or surplus attachment)

For every component `R` of `C-B`,

\[
                          |A_R|+|T_R|\ge7.              \tag{1.1}
\]

If equality holds, `A_R\cup T_R` is the literal boundary of an actual
order-seven separation of `G`, with both open shores nonempty.  Every
component on either open shore is full to that literal seven-set.

Consequently, if no actual exact-seven adhesion is available, then every
component of `C-B` satisfies the strict surplus inequality

\[
                          |A_R|+|T_R|\ge8.              \tag{1.2}
\]

### Proof

Because `R` is a component of `C-B`, and `C` is the sole component outside
`N[v]`, every neighbour of `R` outside `R` lies in

\[
                         A_R\cup T_R.
\]

The vertex `v` lies outside `R\cup A_R\cup T_R`, so this neighbour set is a
genuine separator between the nonempty graph `R` and `v`.  Seven-connectivity
gives (1.1).

If equality holds, take the separation whose first open shore is `R` and
whose boundary is `A_R\cup T_R`; its other open shore contains `v` and is
nonempty.  Every boundary vertex has a neighbour in `R` by the definitions
of `A_R,T_R`, so `R` is full to the boundary.  More generally, in a
seven-connected graph every component behind an order-seven separator has
all seven separator vertices as neighbours: otherwise its neighbourhood
would be a cut of order at most six.  Thus every component of the opposite
open shore is full as well.  This is an actual exact-seven adhesion, not a
virtual torso boundary.  The strict alternative (1.2) follows. `square`

## Lemma 2 (connected remainder means portal exhaustion)

If `C-B` is nonempty and connected but is not `S`-full, then for some literal label
`s in S`,

\[
                              N_C(s)\subseteq B.         \tag{2.1}
\]

In the pure-Moser setting, seven-connectivity gives

\[
 |N_C(0)|\ge2,
 \qquad
 |N_C(s)|\ge3\quad(s\in S-\{0\}).                       \tag{2.2}
\]

Thus (2.1) is genuine multiple-portal consumption, not the unavoidable use
of one endpoint portal by a carrier.

### Proof

If the connected graph `C-B` is not full, some `s` has no neighbour in it;
all of its exterior neighbours therefore lie in `B`, proving (2.1).

The Moser degrees inside `S` are `d_S(0)=4` and `d_S(s)=3` for every other
label.  The vertex `v` contributes one further neighbour and has no edge to
`C`.  Since seven-connectivity implies minimum degree at least seven,

\[
 |N_C(s)|=d_G(s)-d_S(s)-1,
\]

which gives (2.2). `square`

If `C-B` is empty, Lemma 1 is vacuous and the usual nonempty convention
means that the hypothesis of Lemma 2 is not invoked.  In that case portal
exhaustion is stronger and immediate: `N_C(s) subseteq B` for every
`s in S`, with the same multiplicity bounds (2.2).

## Proof-spine use

After a four-corner call in the sole-exterior cell, failure of a reserved
full connector now has only two sharp forms:

1. a connected remainder and complete consumption of a literal portal class
   of order at least two or three; or
2. several deficient remainder components, each with an exact order-seven
   adhesion or with at least one surplus attachment beyond the connectivity
   bound.

The equality case in (2) is already the desired **literal adhesion geometry**,
but it is not by itself a common equality state or a six-colouring.  In
particular an induced `(1,1)` packet vector remains possible, and the static
E5 state-selection barrier warns that abstract state languages need not
intersect.  A remaining proof must spend the one-step proper-minor transition
to make that adhesion gluable.  In the strict branch it must turn portal
exhaustion or the surplus in (1.2) into a carrier rerouting, a `K_7` model,
or such an exact state transition.
