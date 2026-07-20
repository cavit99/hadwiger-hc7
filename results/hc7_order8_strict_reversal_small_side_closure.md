# Small-side closure and exact Hall-response reduction in the endpoint-reversal case

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_strict_reversal_small_side_closure_audit.md`](hc7_order8_strict_reversal_small_side_closure_audit.md).
This is a
conditional theorem inside the connected order-eight opposite-response
interface.  It does not prove `HC_7`.

## 1. Setting

Assume the complete setting of the audited
[symmetric allocation theorem](hc7_order8_strict_reversal_d_side_allocation.md).
Thus

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad E_G(L,R)=\varnothing,
 \qquad L=E\mathbin{\dot\cup}D,
\]

where `E,D` are adjacent connected induced subgraphs, `R` contains adjacent
disjoint connected subgraphs `P_0,P_1` each adjacent to every vertex of `S`,
and

\[
 S=\{d,e,x_d,y_d,x_e,y_e,x_0,y_0\}.
\]

Write

\[
 X=\{x_d,x_e,x_0\},\qquad Y=\{y_d,y_e,y_0\}.
\tag{1.1}
\]

The closed `L`-shore has a proper six-colouring inducing

\[
                     X\mid Y\mid\{d,e\},
\tag{1.2}
\]

but, in the live opposite-response orientation, it has no proper
six-colouring inducing

\[
                     X\mid Y\mid\{d\}\mid\{e\}.
\tag{1.3}
\]

The three-vertex endpoint-reversal part is

\[
 E=a b c,\qquad N_E(x_d)=N_E(y_d)=\{a\},
\tag{1.4}
\]

and

\[
 N_E(x_e)=N_E(y_e)=N_E(x_0)=N_E(y_0)=\{c\}.
\tag{1.5}
\]

Every vertex of `E` is adjacent to `d` and has a neighbour in `D`, while
`D` is anticomplete to `d` and adjacent to every other boundary vertex.
The minimum-degree calculation in the cited theorem gives

\[
                 |N_D(a)|\ge3,\qquad |N_D(b)|\ge4.
\tag{1.6}
\]

## 2. Complete elimination of `|D|<=4`

### Lemma 2.1 (three-colourable `D` gives the forbidden response)

If `G[D]` is three-colourable, then the closed `L`-shore has a proper
six-colouring inducing (1.3).

#### Proof

Give `X,Y,d,e` four distinct colours

\[
                         \xi,\eta,\delta,\epsilon
\]

and denote the remaining two colours by `gamma_1,gamma_2`.  Properly colour
`G[D]` using only

\[
                         \delta,\gamma_1,\gamma_2.
\tag{2.1}
\]

This creates no conflict with the boundary: the only boundary vertex of
colour `delta` is `d`, and `D` is anticomplete to `d`.  Now colour

\[
                         a,c\text{ with }\epsilon,
                 \qquad b\text{ with }\xi.              \tag{2.2}
\]

The path `a-b-c` is properly coloured.  The vertices `a,c` are nonadjacent,
`E` is anticomplete to `e`, and no vertex of `D` uses `epsilon`; hence the
two uses of `epsilon` are proper.  Equations (1.4)--(1.5) show that `b` has
no neighbour in `X`, and no vertex of `D` uses `xi`.  Thus (2.1)--(2.2),
together with the four prescribed boundary colours, gives the asserted
colouring. \(\square\)

Consequently every survivor has `chi(G[D])>=4`, and the known case `HC_4`
gives a `K_4` minor in `G[D]`.  Only the order-four equality case is needed
below.

### Theorem 2.2 (small-side closure)

Under the hypotheses above,

\[
                              |D|\ge5.
\tag{2.3}
\]

More precisely, if `|D|<=4`, then either `G` contains an explicit
`K_7`-minor model or the closed `L`-shore realizes (1.3).

### Proof

If `G[D]` is not `K_4`, then it is three-colourable and Lemma 2.1 gives the
forbidden response (1.3).  It remains that `G[D]` is `K_4`; in particular
`|D|=4`.  We first obtain a
matching from its four vertices to four distinct boundary neighbours.  If
Hall's condition failed, some nonempty set `U subseteq D` would satisfy

\[
                         |N_G(U)\cap S|\le |U|-1.
\tag{2.4}
\]

Since `D` is a clique, `|D-U|=4-|U|`; since `|E|=3`; and since there are no
`L`--`R` edges, one would have

\[
 N_G(U)\subseteq (D-U)\cup E\cup(N_G(U)\cap S),
 \qquad |N_G(U)|\le6.                                  \tag{2.5}
\]

The nonempty set `R` lies outside `U union N_G(U)`, so (2.5) is a genuine
separation contradicting seven-connectivity.  Hall's theorem therefore
gives distinct vertices

\[
                 s_v\in S\cap N_G(v)\qquad(v\in D).
\tag{2.6}
\]

Choose

\[
                    s_0\in (S-\{e\})-\{s_v:v\in D\}.
\tag{2.7}
\]

This is possible because `|S-{e}|=7` and only four boundary vertices occur
in (2.6).  The normalization makes `E` adjacent to every vertex of
`S-{e}`, so `E union {s_0}` is connected.  Also (1.6) and `|D|=4` imply
that `b` is adjacent to every vertex of `D`.

The following seven vertex sets are now pairwise disjoint and connected:

\[
 P_0,\quad P_1,\quad
 \{v,s_v\}\ (v\in D),\quad E\cup\{s_0\}.              \tag{2.8}
\]

The first two sets are adjacent and meet each later set through its displayed
boundary vertex.  The four two-vertex sets are pairwise adjacent through the
`K_4` on `D`.  Finally `E union {s_0}` is adjacent to each of them through
the edge `bv`.  Thus (2.8) is an explicit `K_7`-minor model.  Both cases are
impossible in the surviving opposite-response branch, proving (2.3).
\(\square\)

## 3. The Hall separator retains an exact response

Use the five portal sets

\[
 Q_a=N_D(a),\quad Q_e=N_D(e),\quad Q_b=N_D(b),
 \quad Q_{x_d}=N_D(x_d),\quad Q_{y_d}=N_D(y_d).
\tag{3.1}
\]

### Lemma 3.1 (operation-specific response at every Hall separator)

Suppose the sets in (3.1) have no system of distinct representatives.  Let
`I` be a Hall-deficient subfamily, put

\[
                 Z=\bigcup_{Q\in I}Q,\qquad |Z|\le |I|-1,
\tag{3.2}
\]

and let `C` be a component of `G[D-Z]`.  Then `Z` is nonempty,

\[
                         \varnothing\ne C\subsetneq D,
\tag{3.3}
\]

and, with `B=N_G(C)`,

\[
                              7\le |B|\le9.              \tag{3.4}
\]

Let `pi_C` be the equality partition induced on `B` by the fixed colouring
(1.2).  For every edge `uv` with `u in C` and `v in B`, every proper
six-colouring of `G-uv` has

\[
                              c(u)=c(v),                 \tag{3.5}
\]

and its restriction to `G-C` induces on `B` a partition different from
`pi_C`.

### Proof

Every portal set in (3.1) is nonempty, so a deficient subfamily has at least
two members and its union `Z` is nonempty.  The small-side alternative
`D=Z` in the audited symmetric-allocation theorem would give `|D|<=4`,
which Theorem 2.2 has eliminated.  Hence `D-Z` is nonempty and every one of
its components satisfies (3.3).  The cited Hall calculation gives
`|N_G(C)|<=9`; seven-connectivity gives the lower bound.

The fixed colouring (1.2) is defined on `C union B`, because `B` is
contained in `D union E union S`.  If a six-colouring of `G-uv` gave its
ends different colours, restoring `uv` would six-colour `G`, proving (3.5).
If its restriction to `G-C` induced `pi_C`, a permutation of its colour
names would align it on `B` with the fixed colouring of `G[C union B]`.
The two colourings would glue to a proper six-colouring of `G`, a
contradiction.  This proves the response assertion. \(\square\)

### Corollary 3.2 (orders seven and eight are absorbed)

In the setting of Lemma 3.1:

1. if `|B|=7`, then `(C,B,V(G)-(C union B);uv,c)` is a generic exact-seven
   response interface whose selected connected shore is a proper subset of
   `D`;
2. if `|B|=8`, the audited small-boundary lobe theorem gives either an
   actual order-seven separation or a strict boundary-full order-eight
   descent with selected shore `C`; the incompatible response of Lemma 3.1
   remains available at every selected boundary edge.

### Proof

For the first assertion, `C` is connected, `B=N_G(C)`, and the opposite
open shore is nonempty because it contains `R`.  Lemma 3.1 supplies the
edge-deletion colouring and the rejected intact-shore partition required by
the generic-interface definition.  Strictness is (3.3).

For the second assertion, `L` is a component of `G-S`, `C` is a nonempty
connected proper subset of `L`, and

\[
 |N_{G[L]}(C)|+|N_G(C)\cap S|=|N_G(C)|=8.
\]

The small-boundary lobe theorem applies.  Its proof does not alter the
edge-deletion response established in Lemma 3.1. \(\square\)

## 4. Exact order-nine normal form

### Proposition 4.1

If `|B|=9` in Lemma 3.1, then every inequality in the Hall bound is tight:

\[
 |Z|=|I|-1,\qquad N_D(C)=Z,                             \tag{4.1}
\]

and `C` is adjacent to every vertex of

\[
                         E\cup(S-\{d\})
\]

except the `|I|` distinct vertices whose portal sets occur in `I`.
Moreover, `I` has one of the following three forms:

1. all five portal sets in (3.1), with `|Z|=4`;
2. `\{Q_a,Q_e,Q_{x_d},Q_{y_d}\}`, with `|Z|=3`;
3. a two- or three-member subfamily of
   `\{Q_e,Q_{x_d},Q_{y_d}\}`, with `|Z|=|I|-1`.

### Proof

The Hall proof bounds

\[
 |B|\le |Z|+10-|I|\le9.                                \tag{4.2}
\]

Equality `|B|=9` forces equality throughout.  This proves (4.1), and it
forces every one of the `10-|I|` permitted outside vertices to lie in
`B`, giving the asserted exact outside contact pattern.

If `Q_b` belongs to `I`, then `|Z|>=|Q_b|>=4`; hence
`|I|-1>=4`, and `I` is the full five-member family.  If `Q_a in I` but
`Q_b notin I`, then `|Z|>=|Q_a|>=3`, so `|I|>=4`; the only possible family
is the four-set family in item 2.  If neither `Q_a` nor `Q_b` belongs to
`I`, the deficient family is a two- or three-member subfamily of the three
remaining portal sets.  These are exactly the listed cases. \(\square\)

### Proposition 4.2 (order-nine boundary alternative)

Retain `|B|=9`.  At least one of the following holds.

1. `G` has an actual separation of order seven or eight.
2. Every component of `G-B` is adjacent to every literal vertex of `B`, and
   the induced graph `G[B]` is four-colourable or isomorphic to
   `K_2 vee C_7`.

In an order-seven outcome, deletion of any edge entering the selected
component gives a generic exact-seven response interface.  An order-eight
outcome likewise carries an operation-specific edge-deletion response,
although it is not asserted to be a strict descent from `C`.

### Proof

The set `C` is a component of `G-B` and is adjacent to every member of `B`.
Let `H` be any other component of `G-B`; one exists because the old open
shore `R` survives outside `C union B`.  If `H` misses a vertex of `B`, then

\[
                         |N_G(H)|\le8.
\]

Its full neighbourhood is an actual separator, with `C` on the opposite
side, so seven-connectivity makes its order seven or eight.  Deleting an
edge entering `H` gives the stated response: its endpoints have one colour
in every six-colouring of the deleted-edge minor, and the induced boundary
partition cannot extend through the intact `H`-shore without six-colouring
`G`.

Suppose no such component exists.  Then every component of `G-B` is
boundary-full.  In particular `C` and `H` are two nonempty connected
anticomplete subgraphs, each adjacent to every vertex of the nine-set `B`.
The audited two-full-shore boundary-absorption theorem now says that `G[B]`
is four-colourable or isomorphic to its unique five-chromatic exception
`K_2 vee C_7`. \(\square\)

### Proposition 4.3 (localization of the cyclic exception)

Suppose the second outcome of Proposition 4.2 holds and

\[
                            G[B]\cong K_2\vee C_7.
\tag{4.3}
\]

Then the Hall family `I` has form 1 or 2 of Proposition 4.1.  Moreover the
two universal vertices of `G[B]` are

\[
                              c\quad\text{and}\quad z
\tag{4.4}
\]

for some `z in Z`.

### Proof

The degree sequence of `K_2 vee C_7` consists of two vertices of degree
eight and seven vertices of degree four.  No vertex of
`W={x_e,y_e,x_0,y_0}` can be universal: each has another member of `W` in
the same independent bipartition class `X` or `Y`.

In form 3 of Proposition 4.1, all of `a,b,c,W` belong to `B`.  The vertex
`c` is adjacent to `b` and to all four vertices of `W`, so it has degree at
least five in `G[B]`; but it is nonadjacent to `a`.  Its degree is therefore
neither four nor eight, contradicting (4.3).

In form 2, the set `B` consists of `Z`, `b,c`, and `W`.  Again `c` is
adjacent to `b` and all four members of `W`, so (4.3) forces `c` to be
universal.  The vertex `b` is nonadjacent to every member of `W`, and no
member of `W` is universal, so the second universal vertex lies in `Z`.

In form 1, the set `B` consists of `Z`, `c`, and `W`.  The vertex `c` is
adjacent to all four members of `W`.  If it had degree four, it would be
adjacent to neither universal vertex, since neither universal can lie in
`W`; this is impossible for a cycle vertex of `K_2 vee C_7`.  Hence `c` is
universal, and the second universal vertex again lies in `Z`. \(\square\)

## 5. Exact gain and remaining gap

Lemma 2.1 shows more generally that the `D`-side of any survivor is at least
four-chromatic.  Theorem 2.2 removes the complete bounded Hall residue
`|D|<=4`.  Lemma 3.1
and Corollary 3.2 absorb every Hall separator of order seven and reduce every
order-eight Hall separator to the already promoted strict lobe machinery.
At order nine, Proposition 4.1 leaves only three exact Hall-deficiency
patterns, while Proposition 4.2 either returns a smaller-order separation or
places the residue over a four-colourable boundary (apart from the unique
`K_2 vee C_7` boundary).  Proposition 4.3 localizes that sole exception to
an explicit pair `c,z`, with `z` in the internal Hall separator.

This does not eliminate the distinct-representative cases `|D|=5,6`, nor
does it turn the order-nine response into a common boundary partition or a
label-preserving recursive order-eight interface.  Those are the exact
remaining obligations.

## 6. Dependencies

- the audited [symmetric allocation theorem](hc7_order8_strict_reversal_d_side_allocation.md);
- the audited [generic exact-seven response restart](../results/hc7_generic_exact7_response_restart.md);
- the audited [small-boundary lobe descent](../results/hc7_order8_small_boundary_lobe_descent.md);
- the audited [two-full-shore boundary absorption](../results/hc7_two_full_shore_boundary_absorption.md); and
- seven-connectivity and proper-minor six-colourability.
