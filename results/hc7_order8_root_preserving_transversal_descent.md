# Transversal reductions at a split-response order-eight separation

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_root_preserving_transversal_descent_audit.md`](hc7_order8_root_preserving_transversal_descent_audit.md).
This is an unbounded host-level reduction.  It does not prove `HC_7`.

## 1. Setting

Let `G` be a seven-connected graph with a separation

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad E_G(L,R)=\varnothing,
 \qquad L,R\ne\varnothing,                         \tag{1.1}
\]

where `G[R]` is connected and

\[
 S=\{d,e\}\mathbin{\dot\cup}X\mathbin{\dot\cup}Y,
 \qquad |X|=|Y|=3.                                \tag{1.2}
\]

Assume that `d,e` are nonadjacent and that `X,Y` are independent.  Assume
also that `R` is adjacent to every literal vertex of `S`.  In particular,
each of the three support families defined below is nonempty.

Fix a proper six-colouring `c` of `G[R union S]` whose exact equality
partition on `S` is

\[
                    X\mid Y\mid\{d\}\mid\{e\}.       \tag{1.3}
\]

Suppose that `G[R union S]` has no proper six-colouring inducing

\[
                    X\mid Y\mid\{d,e\}.               \tag{1.4}
\]

A **root connector** is a nonempty connected subgraph of `G[R]` having a
neighbour at each of `d,e`.  For `B` equal to `X` or `Y`, a set
`F subseteq R` is a **boundary-block carrier for `B`** when
`G[B union F]` is connected and contains an edge.  The set `F` need not
induce a connected subgraph.

## 2. A common three-vertex transversal

### Theorem 2.1

Let `Z subseteq R`, with `|Z|<=3`, meet every root connector and every
boundary-block carrier for each of `X,Y`.  Then `R-Z` is nonempty, and for
every component `C` of `G[R-Z]`,

\[
                         7\le |N_G(C)|\le8.             \tag{2.1}
\]

Consequently one of the following holds.

1. `G` has an actual separation of order seven; or
2. `|Z|=3`, and for every component `C` of `G[R-Z]` there are unique
   vertices

   \[
        r_C\in\{d,e\},\qquad x_C\in X,\qquad y_C\in Y
                                                               \tag{2.2}
   \]

   such that

   \[
        N_G(C)=Z\mathbin{\dot\cup}
                   \bigl(S-\{r_C,x_C,y_C\}\bigr).      \tag{2.3}
   \]

In outcome 2, every component of `G-N_G(C)` is adjacent to every literal
vertex of `N_G(C)`.  The restriction of `c` to
`G[C union N_G(C)]` is a proper six-colouring.  On the inherited boundary
vertices, `X-{x_C}` is monochromatic, `Y-{y_C}` is monochromatic, these two
colours are distinct, and the surviving member of `{d,e}` has a third
colour.  The vertices of `Z` retain their actual colours under `c`; they
may enlarge one of those equality blocks or form further blocks.

#### Proof

First, `R-Z` is nonempty.  Otherwise `R=Z` has order at most three.  Give
the three independent boundary blocks `X`, `Y`, and `{d,e}` three distinct
colours.  The graph `G[R]`, having order at most three, is three-colourable
with the other three colours.  This gives a proper six-colouring of
`G[R union S]` inducing (1.4), a contradiction.

Let `C` be a component of `G[R-Z]`.  Since `Z` meets every root connector,
`C` cannot have neighbours at both `d,e`.  Since `Z` meets every
`X`-carrier, `C` cannot have a neighbour at every vertex of `X`: otherwise
`C` itself would be such a carrier.  The same holds for `Y`.  Therefore

\[
                     |N_G(C)\cap S|\le1+2+2=5.          \tag{2.4}
\]

All neighbours of `C` in `R-C` lie in `Z`, and `C` has no neighbour in
`L`.  Hence

\[
                     |N_G(C)|\le |Z|+5\le8.             \tag{2.5}
\]

The set `N_G(C)` is the boundary of an actual separation: `C` is nonempty,
whereas the nonempty set `L` lies outside `C union N_G(C)`.  Seven-
connectivity gives the lower bound in (2.1).  If equality seven occurs,
outcome 1 holds.

Assume now that `G` has no actual separation of order seven.  Then equality
eight holds in (2.5) for every `C`.  Equality forces `|Z|=3`, every vertex
of `Z` to have a neighbour in `C`, and equality in each of the three terms
of (2.4).  Thus `C` misses exactly one root, one vertex of `X`, and one
vertex of `Y`, proving (2.2)--(2.3).

Put `T=N_G(C)`.  Let `K` be a component of `G-T`.  If `K` missed a vertex
`t in T`, then

\[
                         N_G(K)\subseteq T-\{t\}.        \tag{2.6}
\]

If the left side had order at most six, this would contradict seven-
connectivity.  If it had order seven, it would be the boundary of an
actual order-seven separation: `K` is one nonempty side and `t` lies
outside `K union N_G(K)`.  Both alternatives are excluded.  Hence every
component of `G-T` is adjacent to every vertex of `T`.

Finally, restrict `c` to `C union T`.  Properness is preserved, and (1.3)
gives precisely the inherited equality relations stated after (2.3).
This proves the theorem. \(\square\)

## 3. A two-vertex transversal preserving both roots

The preceding theorem treats the three support families symmetrically,
but its order-eight outcome necessarily omits one of `d,e`.  The next
version instead transverses only the two boundary-block-carrier families.

### Theorem 3.1

Let `Z subseteq R`, with `|Z|<=2`, meet every boundary-block carrier for
`X` and every boundary-block carrier for `Y`.  Then `R-Z` is nonempty, and
for every component `C` of `G[R-Z]`,

\[
                         7\le |N_G(C)|\le8.             \tag{3.1}
\]

Consequently one of the following holds.

1. `G` has an actual separation of order seven; or
2. `|Z|=2`, and for every component `C` of `G[R-Z]` there are unique
   vertices `x_C in X`, `y_C in Y` such that

   \[
        N_G(C)=Z\mathbin{\dot\cup}
                         \bigl(S-\{x_C,y_C\}\bigr).     \tag{3.2}
   \]

In outcome 2, every component of `G-N_G(C)` is adjacent to every literal
vertex of `N_G(C)`.  The restriction of `c` to
`G[C union N_G(C)]` is a proper six-colouring in which

\[
 X-\{x_C\},\qquad Y-\{y_C\},\qquad\{d\},\qquad\{e\}   \tag{3.3}
\]

are four distinct inherited colour blocks.  The two vertices of `Z`
retain their actual colours under `c`; either may share a colour with an
inherited block or with the other vertex of `Z` when properness permits.

#### Proof

The proof that `R-Z` is nonempty is identical to the first paragraph of
Theorem 2.1, now using `|R|<=2` if `R=Z`.

Let `C` be a component of `G[R-Z]`.  Since `Z` meets both carrier families,
`C` misses at least one vertex of `X` and at least one vertex of `Y`.
There is no restriction yet on its two root contacts.  Therefore

\[
                     |N_G(C)\cap S|\le2+2+2=6,          \tag{3.4}
\]

and, as before,

\[
                     |N_G(C)|\le |Z|+6\le8.             \tag{3.5}
\]

The boundary is actual because `L` is a nonempty opposite side, and seven-
connectivity gives the lower bound in (3.1).  An order-seven boundary is
outcome 1.

Assume no actual order-seven separation exists.  Equality must then hold
throughout (3.5).  Thus `|Z|=2`, every vertex of `Z` has a neighbour in
`C`, and `C` has neighbours at both `d,e` and at exactly two vertices of
each of `X,Y`.  This proves (3.2).  The argument following (2.6) proves
that every component complementary to this order-eight boundary is full
to it.  Restricting `c` proves (3.3), because the four blocks in (1.3)
have four distinct colours. \(\square\)

## 4. Exact gain and trust boundary

Both theorems replace a support-family transversal by a literal host
separation of order at most eight.  In the absence of an order-seven
separation, each resulting component `C` is a proper subset of `R`, because
`Z` is nonempty and disjoint from `C`.

Theorem 2.1 applies to a common transversal of the root, `X`, and `Y`
support families, but its order-eight outcome loses one root.  Theorem 3.1
uses the role-sensitive parameter

\[
 \tau_{XY}(R)=\min\{|Z|:Z\text{ meets every `X`-carrier and every
 `Y`-carrier}\},                                      \tag{4.1}
\]

and preserves both roots when `tau_XY(R)<=2`.  This makes Theorem 3.1
compatible at the level of literal labels with the three colour-indexed
`d`--`e` Kempe paths on the merged-response shore.

Neither theorem proves that the required transversal exists.  In fact the
audited split-shore counterexample has `tau_XY=3`, so a static one-shore
argument cannot force Theorem 3.1.  The theorems also do not prove that the
opposite closed shore realizes the complete equality partition returned by
the restricted colouring.  Although `C` is strictly smaller than `R`, the
new separation is not asserted to be a valid recursive opposite-response
interface: the remaining response data and any inherited minor-model
labels have not been transferred.

No `K_7`-minor exclusion, contraction-critical colouring beyond the
selected response (1.3), or finite boundary classification is used.

## 5. Immediate references

- [the generalized root-connector reflection theorem](../results/hc7_order8_root_connector_reflection.md),
  which motivates the three support families;
- [the common two-vertex transversal descent](../results/hc7_order8_common_two_vertex_transversal_descent.md),
  recovered and sharpened here by retaining the order-eight alternative;
- [the minor-free split-shore transversal barrier](../barriers/hc7_order8_split_shore_transversal_barrier.md),
  which has `tau_XY=3`; and
- [three colour-indexed Kempe locks on the merged-response shore](../results/hc7_merged_root_three_kempe_locks.md).
