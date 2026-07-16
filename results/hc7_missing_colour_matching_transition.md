# Missing-colour transitions on a matching deletion

**Status:** proved and independently cold-audited.

This note records the exact Kempe bookkeeping available in the
five-connected common-deletion residue.  It does not assume that a
matching edge toggles merely because it crosses a swapped component: both
of its endpoint colours must belong to the swapped colour pair.

## 1. Exact toggle formula

Let `F` be a matching in a graph `G`, put `K=G-F`, and let `c` be a proper
colouring of `K`.  Write

\[
   \operatorname{Eq}_F(c)
      =\{uv\in F:c(u)=c(v)\}.
\]

Fix two colours `a,b`, let `C` be a component of the subgraph of `K`
induced by the vertices coloured `a` or `b`, and let `c^C` be obtained by
interchanging `a` and `b` on `C`.  Define

\[
 \partial_F^{a,b}(C,c)=
 \left\{uv\in F:
  |\{u,v\}\cap V(C)|=1\text{ and }
  c(u),c(v)\in\{a,b\}
 \right\}.
\]

### Lemma 1.1 (matching-signature toggle)

The colouring `c^C` is a proper colouring of `K`, and

\[
 \operatorname{Eq}_F(c^C)
   =\operatorname{Eq}_F(c)\mathbin{\triangle}
      \partial_F^{a,b}(C,c).                       \tag{1.1}
\]

#### Proof

A Kempe interchange on a two-colour component preserves properness in
`K`.  Consider an edge `uv in F`.  If neither or both endpoints lie in
`C`, the equality of their colours is unchanged.  Suppose exactly one
endpoint, say `u`, lies in `C`.  Its colour changes from `a` to `b` or
from `b` to `a`.  If `c(v)` is outside `{a,b}`, the row is unequal before
and after the interchange.  If `c(v)` is in `{a,b}`, equality changes to
inequality or inequality changes to equality.  These are exactly the
rows in `partial_F^{a,b}(C,c)`, proving (1.1).  \(\square\)

The condition on both endpoint colours is essential.  A matching edge
with one endpoint in `C` and its other endpoint carrying a third colour
does not toggle.

## 2. The missing-colour alternative from an arbitrary exact state

Assume now that `chi(G)=7`, let

\[
                      F=\{e_1,e_2,e_3\},
       \qquad e_r=x_r y_r,
\]

be a matching, and put `K=G-F`.  Let `D` be a nonempty subset of `F`,
fix `e_i in D`, and suppose that `c` is a six-colouring of `K` with exact
matching signature

\[
                  \operatorname{Eq}_F(c)=D.          \tag{2.1}
\]

Let `alpha=c(x_i)=c(y_i)`.  Suppose also that `Q_i` is a literal
`K_4`, disjoint from the endpoints of `F`, and that every vertex of
`Q_i` has an edge in `K` to at least one of `x_i,y_i`.  Thus
`Q_i` together with the connected bag `{x_i,y_i}` is the named
support-six `K_5` model before `e_i` is deleted.

The four vertices of `Q_i` have four distinct colours, none equal to
`alpha`.  Let `gamma` be the unique colour in the six-colour palette
which occurs neither on `Q_i` nor on `{x_i,y_i}`.  Let `C_i` be the
`alpha,gamma` component of `K` containing `x_i`, and put

\[
 U_i=\partial_F^{\alpha,\gamma}(C_i,c),\qquad
 D_i'=D\mathbin\triangle U_i.                         \tag{2.2}
\]

### Theorem 2.1 (exact-state missing-colour transition)

Exactly one of the following alternatives holds.

1. `y_i in C_i`.  Then `C_i` contains an `x_i-y_i` path in `K-Q_i`.
2. `y_i notin C_i`.  Then `e_i in U_i`, so `e_i notin D_i'`.
   The set `D_i'` is nonempty.  Interchanging `alpha,gamma` on `C_i`
   produces a proper six-colouring of `K` whose exact matching signature
   is `D_i'`:

   \[
             \operatorname{Eq}_F(c^{C_i})=D_i'.      \tag{2.3}
   \]

   Since `D_i'` is a nonempty matching and all rows outside `D_i'` remain
   proper, this colouring descends to a six-colouring of the proper minor
   `G/D_i'`.  Thus (2.3) is a legal contraction state, not only a formal
   boundary signature.

   Moreover, `C_i` avoids `Q_i`, contains `x_i`, and for every row in
   `U_i-{e_i}` contains exactly one endpoint while its other endpoint lies
   outside `C_i`, with both endpoint colours in `{alpha,gamma}`.

   The transition is an involution: `C_i` is the same
   `alpha,gamma` component after the interchange, and interchanging it
   again returns the exact state `D`.

#### Proof

No vertex of `Q_i` has colour `alpha` or `gamma`, so every
`alpha,gamma` component of `K` avoids `Q_i`.  If `y_i in C_i`, a path in
the connected component `C_i` proves item 1.

Suppose `y_i notin C_i`.  The row `e_i` belongs to
`partial_F^{alpha,gamma}(C_i,c)`: exactly one of its endpoints lies in
`C_i`, and both originally have colour `alpha`.  Hence the interchange
makes `e_i` proper.  Lemma 1.1 gives (2.3) for every row at once, and in
particular `e_i notin D_i'`.

If `D_i'` were empty, every edge of `F` would be proper under
`c^{C_i}`.  Restoring the three deleted matching edges would then give
a six-colouring of `G`, contrary to `chi(G)=7`.  Thus `D_i'` is nonempty.
Contracting the equal rows in `D_i'` and
restoring every other (proper) row carries the same colouring to
`G/D_i'`.  The final carrier statement is just the definition of `U_i`, and
the avoidance of `Q_i` was established above.  \(\square\)

### Corollary 2.2 (singleton carrier)

If `D={e_i}` and alternative 2 occurs, then

\[
                   T_i=D_i'=U_i-\{e_i\}
\]

is a nonempty subset of `F-{e_i}`.  Thus `C_i` is one connected labelled
star carrier from the `i`-row to one literal endpoint of every row in the
new exact state `T_i`.

### Corollary 2.3 (strict first descent from the all-equal state)

If `D=F`, then for every `i` either `K-Q_i` contains the missing-colour
`x_i-y_i` path from alternative 1, or one Kempe interchange produces a
legal exact state

\[
                 \varnothing\ne D_i'\subseteq F-\{e_i\}.
\]

In particular the equality-set size drops strictly from three to one or
two.  This is a genuine first descent, not a global rank: subsequent
moves among the lower states can still cycle.

## 3. Relation with the usual edge-critical Kempe path

In the singleton case, write the colouring as `c_i`.  It extends from
`K` to `G-e_i`, because the other two matching rows are proper.  In any
six-colouring of `G-e_i`, the two ends
of `e_i` lie in one `alpha,beta` Kempe component for every
`beta != alpha`: otherwise swapping the component containing `x_i`
would make `e_i` proper and six-colour `G`.  In particular they are
joined by an `alpha,gamma` path in `G-e_i-Q_i`.

When alternative 2 of Corollary 2.2 occurs, that path must leave `C_i`
through at least one of the other matching rows.  Its first such row is
in `T_i`.  Thus the transition in (2.3) is carried by a literal
two-colour component and is not merely an abstract second colouring.

## 4. HC7 source of the hypotheses

In a strongly seven-contraction-critical graph, contract any nonempty
subset `D` of `F` and six-colour the proper minor.  Expanding the
contracted vertices after deleting all of `F` gives (2.1): the rows in
`D` are equal and, because `F` is a matching, the uncontracted rows
survive as edges and are proper.  Therefore Theorem 2.1 applies at every
nonempty vertex of the punctured signature cube and Corollary 2.2 applies
at each singleton.

## 5. Trust boundary

The theorem gives a genuine labelled state transition, but it does not
by itself give a decreasing rank.

* In the singleton case, `T_i` may be a singleton or may contain both
  other rows.
* Different `C_i` may overlap, and their transitions may form a cycle.
* A matching row crossing `C_i` does not toggle unless both of its
  endpoint colours are `alpha,gamma`.
* The theorem gives no three-way disjointness and no literal `K_7` by
  itself.

The next composition step must use the actual two-colour carriers or the
weighted separator rank; abstract existence of the target signature was
already known from the punctured-cube theorem.
