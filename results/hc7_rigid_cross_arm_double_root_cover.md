# Double-root cover forced by a rigid private-pair certificate

**Status:** proved and independently cold-audited after the two scope
repairs recorded in the adjacent audit.

This is the part of the private-pair structure that is invisible in the
three named supports alone.  In a rigid cross-arm outcome, every pair of
vertices of the avoided support that touches the common arm core forces an
additional small `K_5` model containing both private roots.

## 1. Mandatory double-root supports

### Theorem 1.1

Let `F` be a family of sets of order five or six with `tau(F)>2`.  Let
`A in F`, and let `P={p,q}` be disjoint from `A` and meet every member of
`F-{A}`.  Suppose the two separated arm families at `P` have the rigid
form

\[
 \mathcal B_p=\{X\cup\{p\}\},\qquad
 \mathcal B_q=\{X\cup\{q\}\},                       \tag{1.1}
\]

where an exact-one-root member `D` is called a separated arm when

\[
              |A\cap D|\le \max\{|A|,|D|\}-2.       \tag{1.2}
\]

Put `I=A cap X`.  For every two-set `R subset A` with `R cap I` nonempty,
there is a member `D_R in F` such that

\[
              D_R\cap R=\varnothing,qquad
              \{p,q\}\subseteq D_R.                 \tag{1.3}
\]

### Proof

Since `tau(F)>2`, the two-set `R` is not a transversal.  Choose
`D_R in F` disjoint from `R`.  It is not `A`, because `R subset A`, so the
private pair `P` meets `D_R`.

Suppose first that `P cap D_R={p}`.  The support `D_R` avoids both vertices
of `R subset A`, and therefore

\[
 |A\cap D_R|\le |A|-2\le \max\{|A|,|D_R|\}-2.
\]

Thus `D_R` is a separated `p`-arm.  By (1.1), it equals `X union {p}`.
But `R cap I` is nonempty and `I subset X`, so this arm meets `R`, contrary
to the choice of `D_R`.  The case `P cap D_R={q}` is symmetric.  Since
`P` meets `D_R`, the only remaining possibility is `P subset D_R`, which
is (1.3).  \(\square\)

### Corollary 1.2 (rooted demand fan)

For every fixed `a in I` and every `b in A-{a}`, there is a support
`D_{a,b}` containing `p,q` and avoiding `a,b`.  These supports need not be
distinct, and each contains at most four other elements.  When `F` is a
family of graph-model supports, as in Section 2, each returned set carries
an actual bounded labelled model rather than only a set-system witness.

## 2. Orientation in the literal-arm cell

Assume now that `F` consists of supports of `K_5` models on at most six
vertices in a seven-connected, `K_7`-minor-free graph `G`, and that the
rigid arms have order five.  Then `|X|=4`, both `X union {p}` and
`X union {q}` are literal `K_5`s, and hence `X` is a clique and both roots
are complete to `X`.

### Corollary 2.1

In this literal-arm cell:

1. `pq` is not an edge; and
2. every support `D_R` supplied by Theorem 1.1 has order six.  In every
   normalized spanning `K_5` model on `D_R`, exactly one of `p,q` lies in
   the unique two-vertex edge bag and the other is a singleton bag.

### Proof

If `pq` were an edge, the six vertices `X union {p,q}` would form a
literal `K_6`.  Seven-connectivity lifts a `K_6` supported on six vertices
to a `K_7` minor: after deleting those six vertices the connected remainder
is nonempty and must meet every clique vertex, or a set of at most five
neighbours would separate it.  Thus `pq` is absent.

An order-five `K_5` support is a literal clique, so it cannot contain both
nonadjacent vertices `p,q`.  Hence every `D_R` has order six.  Its five
branch bags have sizes `(2,1,1,1,1)`.  The roots cannot be two singleton
bags, since singleton bags are adjacent, and they cannot occupy the one
edge bag together, since `pq` is absent.  Therefore exactly one root lies
in the edge bag and the other is a singleton.  \(\square\)

The last conclusion is a genuine two-state orientation on every mandatory
double-root support.  It is the next labelled object to compose with the
split-row duties of `A` and the one-root replacement supports.

## 3. Two-apex exclusion as a consistency check

### Proposition 3.1

Let `G` be seven-connected, and suppose a pair `Z={z_1,z_2}` makes
`G-Z` planar.  Then every `K_5` model on at most six vertices contains both
vertices of `Z`.  Consequently no rigid cross-arm certificate of the form
above occurs in `G`.

### Proof

Put `H=G-Z`.  The graph `H` is five-connected and planar.  A small `K_5`
model avoiding `Z` would lie in `H`, impossible by planarity.  If such a
model contained exactly one vertex of `Z`, delete the branch bag containing
that vertex.  The other four bags form a `K_4` model in `H` on at most five
vertices, contrary to the audited five-connected planar support-five
exclusion theorem.  Thus every small `K_5` model contains both vertices of
`Z`.  In particular, either vertex of `Z` is a one-vertex transversal of
every family `F` of small-model supports, contradicting the standing
hypothesis `tau(F)>2`.  Hence no rigid certificate satisfying that
hypothesis occurs.  \(\square\)

## 4. Exact contribution and gap

Theorem 1.1 upgrades the rigid cross-arm outcome from three supports plus
one-root replacements to a bounded family of compulsory **double-root**
models.  It is valid for both arm orders and both avoided-support orders.

It does not align the edge bags of the `D_R`, and opposite orientations in
Corollary 2.1 do not automatically give disjoint carriers.  The next
composition theorem must use those orientations to produce a literal
`K_7`, a coherent global pair, or a strict model-preserving handoff.
