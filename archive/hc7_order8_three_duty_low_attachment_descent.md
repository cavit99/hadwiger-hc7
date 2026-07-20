# Low-attachment components in a three-duty obstruction strictly descend

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_three_duty_low_attachment_descent_audit.md`](hc7_order8_three_duty_low_attachment_descent_audit.md).
This is an unbounded reduction in the connected two-component order-eight
interface.  It does not prove `HC_7`.

## 1. Setting

Let `G` be a seven-connected graph satisfying

\[
 \chi(G)=7,\qquad K_7\not\preccurlyeq G,
 \qquad \chi(M)\le 6\text{ for every proper minor }M\text{ of }G.
 \tag{1.1}
\]

Let

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad E_G(L,R)=\varnothing,
 \qquad |S|=8,
 \qquad L,R\ne\varnothing,                         \tag{1.2}
\]

where `R` is connected.  Let

\[
 S=D\mathbin{\dot\cup}X\mathbin{\dot\cup}Y,
 \qquad D=\{d,e\},                                  \tag{1.3}
\]

where `X,Y` are nonempty.  A connected subgraph of `R` **supports** one
of the three sets in (1.3) when it has a neighbour at every literal vertex
of that set.

Suppose that `R` contains two disjoint connected subgraphs `Q_0,Q_1`, each
adjacent to every literal vertex of `S`.  A **three-duty packing** is a
triple of pairwise vertex-disjoint nonempty connected subgraphs of `R`, one
supporting each of `D,X,Y`.

## 2. The low-attachment descent

### Theorem 2.1

Assume that `R` has no three-duty packing.  Let `C` be any component of

\[
                     R-(V(Q_0)\cup V(Q_1)),           \tag{2.1}
\]

and put

\[
                     A=N_{G[R]}(C).                   \tag{2.2}
\]

Then all of the following hold.

1. `C` fails to support each of `D,X,Y`.  In particular,

   \[
                          |N_G(C)\cap S|\le5.          \tag{2.3}
   \]

2. If `|A|<=2`, then `N_G(C)` is the boundary of an actual separation of
   order seven.  Every edge from `C` to `N_G(C)` supplies a strict generic
   exact-seven selected-response descent with connected shore `C`.
3. If `|A|=3`, then one of the following holds:

   - `C` supplies the same strict generic exact-seven descent;
   - `G` has an actual order-seven separation returned on another
     complementary component; or
   - `C` is the selected component in a strict boundary-full order-eight
     descent of the small-boundary lobe theorem.

Consequently, in a normalized interface in which no actual order-seven
separation and no strict order-eight descent is available, every component
in (2.1) has at least four distinct attachment vertices in
`Q_0\cup Q_1`.

#### Proof

Suppose first that `C` supports `D`.  Then

\[
                           C,\qquad Q_0,\qquad Q_1     \tag{2.4}
\]

are pairwise disjoint connected subgraphs supporting `D,X,Y`, respectively.
This is a three-duty packing.  If `C` supports `X`, use `Q_0,C,Q_1` for
`D,X,Y`; and if it supports `Y`, use `Q_0,Q_1,C`.  The assumed absence of a
packing therefore shows that `C` fails all three duties.

Choose one missed vertex from each of the three pairwise disjoint sets
`D,X,Y`.  These are three distinct vertices of `S`, proving (2.3).

Because `C` is a component after deleting `Q_0\cup Q_1`, all its neighbours
in `R-C` lie in `Q_0\cup Q_1`, and hence are exactly the vertices in `A`.
There are no `L`--`R` edges.  Therefore

\[
             N_G(C)=A\mathbin{\dot\cup}(N_G(C)\cap S),
             \qquad |N_G(C)|\le |A|+5.                \tag{2.5}
\]

The set on the left is the boundary of an actual separation: `C` is
nonempty and `L` is a nonempty subset of the opposite open side.  Thus
seven-connectivity gives

\[
                             |N_G(C)|\ge7.             \tag{2.6}
\]

If `|A|<=2`, (2.5)--(2.6) force equality.  Choose any edge `cv` from `C`
to `N_G(C)`.  The graph `G-cv` has a proper six-colouring `phi`, and
`phi(c)=phi(v)`, since otherwise restoring `cv` would six-colour `G`.
The restriction of `phi` to the closed shore opposite `C` induces one exact
equality partition `Pi` on `N_G(C)`.  The same partition cannot extend
through `G[C union N_G(C)]`, for then the two closed-shore colourings would
align and six-colour `G`.  Hence `(C,N_G(C);cv,Pi)` is a generic exact-seven
selected-response interface.  It is strict because both nonempty subgraphs
`Q_0,Q_1` lie outside `C`.  This proves item 2.

Suppose `|A|=3`.  Equations (2.5)--(2.6) give

\[
                              7\le |N_G(C)|\le8.       \tag{2.7}
\]

If the lower value occurs, the preceding edge-deletion argument gives the
same strict exact-seven descent.  If the upper value occurs, apply the
audited small-boundary lobe descent to
the component `R` of `G-S` and its nonempty connected proper subset `C`.
It returns an actual order-seven separation or a boundary-full
order-eight interface in which `C` is a component and
`|C|<|R|`.  In the former outcome the order-seven component need not be
`C`; this is why item 3 lists it separately.  This proves item 3, and the
final assertion is immediate. \(\square\)

## 3. Exact gain and trust boundary

The theorem eliminates every tree-like bridge component with at most three
attachments to the two named boundary-full subgraphs.  It applies to
components of arbitrary order and uses the three duties only through their
literal, disjoint boundary labels.  It is therefore stronger than a finite
quotient check.

It does not construct a three-duty packing when every outside component has
at least four attachments.  It also says nothing when
`R=Q_0\cup Q_1`; and it does not turn an arbitrary order-seven separation
into a common old boundary partition.  The returned interface is useful
through the existing generic selected-response restart only when the
relevant shore comparison is strict; no preservation of `d,e,X,Y` is
proved.

## 4. Dependencies

- the audited small-boundary lobe descent at an order-eight interface;
- the generic exact-seven selected-response restart argument;
- seven-connectivity; and
- the literal two-subgraph fullness hypotheses in Section 1.
