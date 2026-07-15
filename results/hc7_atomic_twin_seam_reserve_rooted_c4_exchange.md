# Reserve-rooted `C_4` exchange in the atomic twin seam

**Status:** proved conditional lemma.  It closes the carrier-allocation step once one
ordinary reserve-rooted `C_4` model has been obtained.  It does not prove
that the model exists.

## 1. Frozen setting

Use the atomic twin-seam notation.  Thus

\[
 Z=\{p,q\},\qquad I=T_D\cap T_E,\qquad
 A_0=T_D-T_E=\{a_1,a_2\},\qquad
 B_0=T_E-T_D,
\]

\[
 J=I\mathbin{\dot\cup}B_0,\qquad |J|=5,
 \qquad \Omega_E=Z\mathbin{\dot\cup}J,
\]

and

\[
 N_G(D)=Z\mathbin{\dot\cup}I\mathbin{\dot\cup}A_0,
 \qquad
 N_G(E)=Z\mathbin{\dot\cup}J.
 \tag{1.1}
\]

The old rich shore contains two disjoint connected `S`-full packets
`R_1,R_2`.  Put

\[
 C_i=R_i\cup\{a_i\}\qquad(i=1,2).
 \tag{1.2}
\]

Each `C_i` is connected, the two are disjoint, and each is `J`-full.
We are in the normalized residual in which

\[
                 \nu_{B_E}^{\Omega_E}=1.                \tag{1.3}
\]

Work in the literal graph

\[
 W=G[D\cup A_0\cup V(R_1)\cup V(R_2)\cup\{p,q\}].
 \tag{1.4}
\]

A **reserve-rooted `C_4` model** in `W` is a four-tuple of disjoint
connected branch sets

\[
                         (P,A,Q,B)                       \tag{1.5}
\]

such that

\[
 p\in P,\quad C_1\subseteq A,\quad q\in Q,\quad C_2\subseteq B,
 \tag{1.6}
\]

and the four cyclic adjacencies

\[
                         PA,AQ,QB,BP                     \tag{1.7}
\]

are present.  No adjacency between opposite bags is required.

## 2. Stem normalization

### Lemma 2.1 (spoke form)

Every reserve-rooted `C_4` model can be chosen so that

\[
 P=p\ldots c_p,\qquad Q=q\ldots c_q                 \tag{2.1}
\]

are paths, and each of `c_p,c_q` has a neighbour in each of `A,B`.

### Proof

Start with any model.  Choose one `P-A` edge and one `P-B` edge, and
let their endpoints in `P` be `x_A,x_B`.  In `G[P]`, take a minimal tree
joining `p,x_A,x_B`.  Let `c_p` be the median of these three vertices in
that tree.  Keep the path from `p` to `c_p` as the new `P` bag.  Absorb
the arm from `c_p` towards `x_A`, excluding `c_p`, into `A`, and absorb
the other arm, excluding `c_p`, into `B`.  Discard unused vertices of the
old `P` bag.

The two absorbed arms are disjoint.  Each enlarged carrier is connected,
the four bags remain disjoint, and `c_p` is adjacent to both carriers,
either by the first edge of an absorbed arm or by the originally selected
model edge when an arm is empty.  The old `A-Q` and `Q-B` adjacencies
remain intact.  Apply the same operation to `Q`.  This proves (2.1).
\(\square\)

Among all spoke-form reserve-rooted models, choose one minimizing

\[
                         |E(P)|+|E(Q)|.                 \tag{2.2}
\]

Write

\[
 P^-=P-c_p,\qquad Q^-=Q-c_q,
 \qquad M=P\cup A\cup Q\cup B.                         \tag{2.3}
\]

An `M`-path means a path whose two ends lie in `M` and whose internal
vertices avoid all four branch sets.

### Lemma 2.2 (stem shortening)

There is no `M`-path from a vertex of `P^-` to `A\cup B`, and none from a
vertex of `Q^-` to `A\cup B`.

### Proof

Suppose that an `M`-path `L` joins `x\in P^-` to `A`; the other cases are
symmetric.  Replace the four bags by

\[
 \begin{aligned}
 P'&=P[p,x],\\
 A'&=A\cup(L-x),\\
 Q'&=Q,\\
 B'&=B\cup P(x,c_p].
 \end{aligned}                                          \tag{2.4}
\]

They are disjoint and connected.  The first edge of `L` supplies the
`P'-A'` adjacency; the first edge of the removed suffix supplies the
`P'-B'` adjacency; and the old `A-Q` and `Q-B` adjacencies survive.  The
reserve roots remain in `A',B'`.  Moreover, `x` is the new end of the
`p`-stem and is adjacent to both carriers.  Thus (2.4) is another
spoke-form model with a strictly shorter `p`-stem, contrary to (2.2).
\(\square\)

## 3. Sharp model or strict exact-seven descent

### Theorem 3.1 (reserve-rooted `C_4` exchange)

If `W` contains a reserve-rooted `C_4` model, then the twin seam has one
of the following outcomes.

1. The opposite side `B_E=D\cup A_0\cup R` contains two disjoint
   `\Omega_E`-full packets.
2. There is a literal actual seven-separation whose packet-one shore
   `X^*` satisfies

   \[
                            |X^*|<|A_{\rm old}|,          \tag{3.1}
   \]

   while its opposite shore contains two disjoint full packets.
   Consequently the exact-seven packet theorem either closes the cell
   terminally or returns a strict oriented `(1,2)` member of
   `\mathcal F_{12}(G)`.

Under the globally minimal packet-one-shore choice in the active spine,
outcome 2 is already contradictory.  Corollary 3.2 below records that the
same separator also supports a named proper-minor handoff if one is needed.

### Proof

Use the jointly stem-minimal spoke-form model fixed above.

If

\[
                            c_p=p,\qquad c_q=q,           \tag{3.2}
\]

then `A` and `B` themselves are disjoint `\Omega_E`-full packets.  Indeed,
`C_1\subseteq A` and `C_2\subseteq B` supply every duty in `J`, while
(3.2) and spoke form say that each carrier is adjacent to both literal
gates.  This is outcome 1, and it contradicts (1.3).

Assume that at least one stem is nontrivial.  Put

\[
 C=\{c_p,c_q\},\qquad X_0=P^-\cup Q^- .                 \tag{3.3}
\]

The two hubs are distinct and avoid `J`, so

\[
                            S'=J\mathbin{\dot\cup}C       \tag{3.4}
\]

has order seven.

There is no path in `W-C` from `X_0` to `A\cup B`.  Otherwise, on a
shortest such path choose its last vertex in `X_0` and its first later
vertex in `A\cup B`.  Since

\[
                         M-C=X_0\mathbin{\dot\cup}A
                                  \mathbin{\dot\cup}B,
\]

the intervening subpath is an `M`-path forbidden by Lemma 2.2.

Let `X` be the union of the components of `W-C` which meet `X_0`.  The
whole reserve roots `C_1,C_2` lie in `A,B`, respectively, and hence avoid
`X`.  Moreover,

\[
                             X\subseteq D\cup\{p,q\}.    \tag{3.5}
\]

To see this, note that `A_0\subseteq C_1\cup C_2\subseteq A\cup B`,
there is no old `A-R` edge, and the only vertices of the old boundary
present in `W` are `a_1,a_2`.  A component reached from a gate stem
without meeting a carrier therefore cannot enter either reserve packet.

Now add the opposite lobe:

\[
                              X^*=X\cup E.               \tag{3.6}
\]

Every nonempty stem prefix contains its literal gate.  The lobe `E` is
connected and adjacent to both `p,q`, so it joins all components used in
`X`; hence `X^*` is connected.  Equations (1.1), the definition of `X`,
and the absence of `D-E` and old `A-R` edges give

\[
                              N_G(X^*)\subseteq S'.       \tag{3.7}
\]

The complement of `X^*\cup S'` is nonempty because it contains the two
carrier bags.  Seven-connectivity and (3.4)--(3.7) therefore force

\[
                              N_G(X^*)=S'.                \tag{3.8}
\]

Thus `X^*` is an open shore of an actual order-seven separation.

The opposite open shore contains `A` and `B` as two disjoint `S'`-full
packets.  Each is connected; `C_i` supplies all five vertices of `J`;
and spoke form makes both hubs adjacent to both carriers.  By (3.8),
`X^*` itself is `S'`-full.  Applying the exact-seven packet theorem gives
vector `(1,2)` or `(1,3)`, oriented with `X^*` as its packet-one shore.
The audited adaptive packet-reflection theorem closes `(1,3)` by a literal
`K_7` model or a six-colouring.  The remaining vector is `(1,2)`.

Finally, the construction and (3.5) give

\[
                     X^*\subseteq D\cup E\cup Z=A_{\rm old}.
\]

Since at least one stem is nontrivial, at least one of `c_p,c_q` is a
vertex of `D`; both hubs lie in `S'` and outside `X^*`.  Hence (3.1)
holds (in fact `X^*\subseteq A_{\rm old}-\{c_p,c_q\}`).  This proves
outcome 2. \(\square\)

### Corollary 3.2 (named high-demand handoff)

In the `(1,2)` branch of Theorem 3.1, choose an edge `xs` with
`x\in X^*` and `s\in S'`, and contract it toward the literal boundary
label `s`.  A six-colouring of the proper minor pulls back to the
untouched packet-two closed shore and induces an exact partition `Pi` on
`S'` satisfying

\[
                       d_{G[S']}(\Pi)\ge3.              \tag{3.9}
\]

### Proof

Such an edge exists because `X^*` is `S'`-full.  Strong
contraction-criticality six-colours `G/xs`.  On expansion, keep the colour
of the contracted image at the literal boundary vertex `s`; the opposite
open shore was untouched, so this gives a proper colouring of that closed
side and a literal exact partition `Pi` of `S'`.

If `Pi` had packet demand at most two, the two disjoint `S'`-full packets
on the opposite shore would reproduce `Pi` on the `X^*` closed side by
the audited exact packet-reflection lemma.  After permuting colour names,
the two closed-side colourings would glue, unless the same construction
already returned a literal `K_7`.  Both are terminal outcomes.  Hence in
the unresolved branch the returned demand is at least three. \(\square\)

## 4. Exact remaining obligation

Contract each connected set `C_i` in `W` to a literal root `r_i`.  Apply
Robertson--Seymour--Thomas (2.1) to the cyclic order

\[
                              p,r_1,q,r_2.               \tag{4.1}
\]

It says that an ordinary rooted `C_4` model exists exactly when both
subpartitions

\[
                  \{p,r_1\},\{q,r_2\},
 \qquad           \{r_1,q\},\{p,r_2\}                 \tag{4.2}
\]

are feasible by disjoint connected fragments.  Lifting the model through
the two contractions gives precisely the reserve-rooted model used in
Theorem 3.1.

Therefore the allocation gap is no longer a five-duty or singleton-gate
problem.  Its exact unresolved implication is:

> Use the named proper-minor response bundle to force both feasibility
> tests in (4.2), or decode the Two-Paths/web certificate returned by a
> failed test into a terminal model or a globally ranked exact-seven
> descent.

No claim is made that seven-connectivity alone forces either feasibility
test.  A failed test may be a genuine web obstruction.

## 5. Scope

This lemma eliminates every stable nonzero gate stem once an ordinary
reserve-rooted `C_4` exists.  It also shows that the earlier requirement
of two carriers meeting all five common labels inside `D` was stronger
than necessary: the old packets already carry the five non-gate duties.

It does **not** prove the twin-seam double-lock exchange theorem, because
the two linkages in (4.2) have not yet been derived from the common-host
edge states.  Completion edges in a web are not literal host edges and
may not be used as model adjacencies.
