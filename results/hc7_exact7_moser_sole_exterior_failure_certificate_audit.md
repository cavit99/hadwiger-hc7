# Independent audit: sole-exterior reserved-connector failure certificate

Audited file:
`results/hc7_exact7_moser_sole_exterior_failure_certificate.md`.

**Verdict:** **GREEN**, with the empty-remainder clarification in Section 3.

The separator count, equality-case adhesion, fullness of every component on
both sides, and the pure-Moser portal multiplicities are all correct.  The
result is a geometric failure certificate only; it does not itself provide
a common equality state on an equality-seven adhesion.

## 1. Exact separator and surplus inequality

Let `R` be a component of `C-B`, where `B=X union Y`.  Since `R` is a
component after deleting `B`, it has no edge to another component of
`C-B`.  Since `C` is the sole component of `G-N[v]`, it has no edge to an
exterior vertex outside `C`, and no vertex of `C` is adjacent to `v`.
Consequently

\[
        N_G(R)=A_R\mathbin{\dot\cup}T_R,
        \qquad A_R=N_G(R)\cap S,quad T_R=N_G(R)\cap B.
\]

The two sets are disjoint because `S` and `C` are disjoint.  The vertex `v`
survives outside `R union A_R union T_R`, so this external neighbourhood is
a genuine cut separating nonempty `R` from `v`.  Seven-connectivity gives

\[
                         |A_R|+|T_R|\ge7.
\]

No connectedness of `B` and no adjacency between `X,Y` is needed for this
count.

## 2. Equality gives a literal full seven-adhesion

If equality holds, put

\[
                         K=A_R\cup T_R.
\]

Take the separation

\[
                         (R\cup K,\;G-R).
\]

Its literal adhesion is `K`, its first open shore is `R`, and its other open
shore is nonempty because it contains `v`.  Every member of `K` has a
neighbour in `R` by the definitions of `A_R,T_R`, so `R` is full to all
seven adhesion vertices.

Now let `Q` be any component of `G-K` different from `R`, including any
component on the opposite open shore.  Its external neighbourhood is a
subset of the seven-set `K`.  If it missed one member of `K`, then
`|N_G(Q)|<=6`; this set would separate nonempty `Q` from the still nonempty
component `R`, contradicting seven-connectivity.  Therefore

\[
                           N_G(Q)=K.
\]

Thus every component on either open shore is literally `K`-full.  This
also covers the component containing `v`; fullness is forced globally and
is not being inferred merely from the definition of `A_R,T_R`.

It follows correctly that, if no actual equality-seven adhesion occurs,
every nonempty component `R` of `C-B` satisfies the strict integer bound

\[
                         |A_R|+|T_R|\ge8.
\]

## 3. Empty and connected-remainder cases

Under the standard convention, “`C-B` is connected” means it is nonempty.
For a nonempty connected remainder which is not `S`-full, choose a literal
`s` having no neighbour in it.  Since

\[
                         C=B\mathbin{\dot\cup}(C-B),
\]

all exterior neighbours of `s` lie in `B`, proving

\[
                         N_C(s)\subseteq B.
\]

If `C-B` is empty, Lemma 1 is vacuous and Lemma 2 is not literally invoked
under that convention.  Nevertheless the intended portal-exhaustion
conclusion is stronger: `C=B`, so `N_C(s) subseteq B` for **every**
`s in S`.  The proof-spine dichotomy should mention this empty case
explicitly or declare the empty graph connected for that sentence.  No
mathematical countercase is created.

If `C-B` is nonempty and disconnected, Lemma 1 applies separately to every
component.  No assertion that one component is full to `S` is being made.

## 4. Pure-Moser portal multiplicity

The literal Moser degrees inside `S` are

\[
                         d_S(0)=4,
             \qquad d_S(s)=3\quad(s\ne0).
\]

Every `s in S` is adjacent to the apex `v`, and all its remaining possible
neighbours outside `S union {v}` lie in the sole exterior component `C`.
Hence

\[
                         |N_C(s)|=d_G(s)-d_S(s)-1.
\]

Seven-connectivity implies `delta(G)>=7`, so

\[
                         |N_C(0)|\ge2,
             \qquad |N_C(s)|\ge3\quad(s\ne0).
\]

Thus when a portal class is completely consumed by `B`, it contains at
least two exterior neighbours for label `0` and at least three for every
other label.  This is a genuine multiplicity statement; it does not say
that those neighbours are distributed between `X` and `Y` or can be
rerouted independently.

## 5. Exact scope

The certificate rigorously leaves the following alternatives after a
candidate reserved connector is removed:

* an empty remainder, giving total portal consumption;
* a nonempty connected deficient remainder, giving complete consumption of
  at least one portal class; or
* multiple remainder components, each producing either an actual full
  order-seven adhesion at equality or at least eight total boundary/carrier
  attachments.

The equality case supplies geometry, not automatically compatible
proper-minor states.  Likewise the surplus bound counts attachment vertices
but does not allocate them to labelled carrier blocks.  The source file
states these limitations correctly.
