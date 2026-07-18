# Low-order separators inside a boundary-full component

**Status:** written proof; independent audit pending.  This is a structural
reduction for one component behind an order-seven separation.  It does not
by itself preserve the named branch sets or a boundary colouring, and it
does not prove `HC_7`.

## 1. Setup and terminology

Let `G` be a seven-connected graph and let `T` be a set of seven vertices.
Let `D` be a component of `G-T`, and assume that there is a vertex outside
`D union T`.  Seven-connectivity then gives

\[
                         N_G(D)=T.                       \tag{1.1}
\]

Fix a vertex `b in T` and a two-element set `I subseteq T-{b}`.  For
`X subseteq D`, write

\[
 N_T(X)=N_G(X)\cap T,
 \qquad
 \delta(X)=T-N_T(X).                                   \tag{1.2}
\]

A **repair support** is a connected subgraph of `G[D]` adjacent to `b`
and to at least one vertex of `I`.  A **residual boundary-full subgraph**
is a connected subgraph of `G[D]`, disjoint from the repair support, that
is adjacent to every vertex of `T`.

The purpose of the theorem is to identify exactly when a cutvertex or a
two-vertex separator of `D` supplies these two disjoint subgraphs.  Its
alternative is another actual order-seven separation of `G`.

## 2. Cutvertices

### Theorem 2.1 (cutvertex reduction)

Suppose that `x` is a cutvertex of `D`.  Then at least one of the following
holds.

1. There is a component `A` of `D-x` and a vertex `t in T` such that

   \[
                       N_G(A)=\{x\}\cup(T-\{t\});       \tag{2.1}
   \]

   in particular, this is an actual separation boundary of order seven.
2. `D` contains a repair support and a disjoint residual boundary-full
   subgraph.

### Proof

Let `A` be any component of `D-x`.  Since `D` is connected, `A` has a
neighbour at `x`, and no vertex of `A` has a neighbour in another component
of `D-x`.  Hence

\[
                         N_G(A)=\{x\}\cup N_T(A).       \tag{2.2}
\]

The set on the right separates the nonempty set `A` from a different
component of `D-x` and from the vertex outside `D union T`.  Therefore
seven-connectivity gives

\[
                         |N_T(A)|\ge 6.                 \tag{2.3}
\]

If equality holds for some `A`, then (2.1) holds for the unique member
`t` of `T-N_T(A)`.  We may consequently assume that every component of
`D-x` is adjacent to all seven vertices of `T`.

Choose two distinct components `A_1,A_2` of `D-x`.  Since `A_1` is
connected and has neighbours at both `b` and every vertex of `I`, it
contains a path whose vertex set is a repair support.  The connected graph
`G[A_2]` is a disjoint residual boundary-full subgraph.  This proves the
second outcome.  \(\square\)

## 3. Two-vertex separators: the exact choice criterion

Suppose now that `D` is two-connected and `Z={x,y}` is a two-vertex
separator of `D`.  Call the components

\[
                         A_1,\ldots,A_m                 \tag{3.1}
\]

of `D-Z` the `Z`-lobes.  Two-connectivity implies that every `A_h` has a
neighbour at both `x` and `y`.  Hence

\[
 N_G(A_h)=Z\cup N_T(A_h),
 \qquad
 |\delta(A_h)|\le 2.                                  \tag{3.2}
\]

The inequality follows from seven-connectivity exactly as in (2.3).

If some lobe has defect two, (3.2) is an actual order-seven separation.
We therefore concentrate on the remaining case

\[
                    |\delta(A_h)|\le 1
                    \quad(1\le h\le m).                \tag{3.3}
\]

Put

\[
 R_x=N_T(\{x\}),\qquad R_y=N_T(\{y\}).                 \tag{3.4}
\]

Fix a lobe `A_c` and a symbol `w in {empty,x,y}`.  This pair is
**admissible for a repair support** when

- `w=empty` and `b in N_T(A_c)`, or
- `w=x` and `b in R_x`, or
- `w=y` and `b in R_y`.

Here `empty` means that neither separator vertex is consumed by the repair
support.  Define

\[
 Z_w=
 \begin{cases}
 Z,&w=empty,\\
 Z-\{w\},&w\in\{x,y\}.
 \end{cases}                                           \tag{3.5}
\]

### Theorem 3.1 (exact two-cut criterion)

Under (3.3), an admissible choice `(c,w)` yields a repair support inside
`A_c union {w}` and a disjoint residual boundary-full subgraph on

\[
                  Z_w\cup\bigcup_{h\ne c}A_h           \tag{3.6}
\]

if and only if

\[
       \bigcap_{h\ne c}\delta(A_h)
              \ \subseteq\ N_T(Z_w).                   \tag{3.7}
\]

### Proof

Every lobe has a neighbour at at least one vertex of `I`, because its
defect has order at most one whereas `|I|=2`.

If `w=empty`, admissibility supplies a neighbour of `b` in `A_c`; a path
inside the connected lobe from such a neighbour to a neighbour of `I`
is a repair support.  If `w=x`, join `x` inside `A_c union {x}` to a
neighbour of `I`; adjacency `bx` supplies the required `b` contact.  The
case `w=y` is symmetric.

Every remaining lobe is adjacent to every vertex of `Z_w`.  Thus (3.6)
induces a connected subgraph and is disjoint from the chosen repair
support.  A boundary vertex `t` is missed by this residual subgraph exactly
when it is missed by every remaining lobe and also by every retained
separator vertex.  Equivalently,

\[
 t\in
 \left(\bigcap_{h\ne c}\delta(A_h)\right)-N_T(Z_w).
\]

The residual subgraph is therefore boundary-full exactly when (3.7)
holds.  \(\square\)

## 4. Explicit exceptional patterns

The exact criterion has a short exhaustive form.  The classifications
below assume (3.3) and use `N_T(D)=T`; that fullness rules out a boundary
vertex missed by all lobes and both separator vertices.

### Proposition 4.1 (two lobes)

Suppose `m=2`.  The criterion in Theorem 3.1 succeeds unless one of the
following patterns occurs.

1. Exactly one lobe is adjacent to `b`, the other lobe has defect `{b}`,
   and neither `x` nor `y` is adjacent to `b`.
2. Neither lobe is adjacent to `b` (so both have defect `{b}`), and exactly
   one of `x,y` is adjacent to `b`.
3. Both lobes are adjacent to `b`; their defects are distinct singletons
   `{s}` and `{t}`, with `s,t != b`; and neither `s` nor `t` belongs to
   `R_x union R_y`.

In pattern 2, if `z` is the unique member of `{x,y}` adjacent to `b`, then

\[
                         N_G(D-z)=\{z\}\cup(T-\{b\}),  \tag{4.1}
\]

so an actual order-seven separation is already present.

### Proof

If exactly one lobe, say `A_1`, is adjacent to `b`, then `A_2` has defect
`{b}`.  Choosing `A_1` and retaining both of `x,y` succeeds precisely when
at least one retained separator vertex is adjacent to `b`.  This gives
pattern 1.

If neither lobe is adjacent to `b`, both have defect `{b}`.  Fullness of
`D` implies that at least one of `x,y` is adjacent to `b`.  A repair support
must consume such a separator vertex.  The residual subgraph is full
precisely when the other separator vertex is also adjacent to `b`.  This
gives pattern 2.  In its exceptional case, `D-z` is connected because `D`
is two-connected.  Its neighbourhood is contained in the seven-set on the
right of (4.1); seven-connectivity forces equality.

It remains to suppose that both lobes are adjacent to `b`.  Either lobe can
then be used without consuming `x` or `y`.  The choice of `A_1` fails
exactly when the defect of `A_2` is a singleton missed by both separator
vertices, and the symmetric statement holds for the choice of `A_2`.
Thus both choices fail exactly as in pattern 3.  The two singleton defects
must be distinct: if they were both `{s}` and the separator vertices also
missed `s`, then all of `D` would miss `s`, contrary to `N_T(D)=T`.
\(\square\)

### Proposition 4.2 (at least three lobes)

Suppose `m>=3`.  The criterion in Theorem 3.1 succeeds unless one of the
following patterns occurs.

1. Neither `x` nor `y` is adjacent to `b`, exactly one lobe is adjacent to
   `b`, and every other lobe has defect `{b}`.
2. Every lobe has defect `{b}`, and exactly one of `x,y` is adjacent to
   `b`.

Pattern 2 again gives the exact order-seven boundary (4.1), where `z` is
the unique separator vertex adjacent to `b`.

### Proof

If exactly one lobe is adjacent to `b`, it is the only lobe that can be
used without consuming a separator vertex.  Retaining all of `Z` repairs
the common defect `{b}` of the other lobes exactly when one of `x,y` is
adjacent to `b`.  This is pattern 1.

If no lobe is adjacent to `b`, every lobe has defect `{b}`.  Fullness of
`D` says that at least one separator vertex is adjacent to `b`.  A repair
support must consume one such vertex, and the other repairs the common
defect precisely when both separator vertices are adjacent to `b`.  This
is pattern 2, with (4.1) proved as in Proposition 4.1.

  Finally suppose that at least two lobes are adjacent to `b`.  Choose one
  of them as `A_c` and retain both separator vertices.  Such a choice can
  fail only when every other lobe has the same singleton defect `{t}` and
both separator vertices miss `t`.  Boundary-fullness forces the initially
chosen lobe `A_c` itself to be adjacent to `t`, because every other lobe
misses `t`.  Choose a different `b`-adjacent lobe as the repair lobe.  The
residual subgraph now retains `A_c`, which meets `t`, as well as at least
one lobe whose defect was `{t}`.  Hence the intersection of the remaining
defects is empty, and criterion (3.7) holds.  \(\square\)

## 5. The unique-portal observation

The exact-separation argument used above is useful independently.

### Lemma 5.1

Let `D` be two-connected and boundary-full, and let `t in T` have a unique
neighbour `z` in `D`.  Then

\[
                         N_G(D-z)=\{z\}\cup(T-\{t\}),  \tag{5.1}
\]

an actual order-seven separation boundary.

### Proof

The graph `D-z` is connected.  Its neighbourhood is contained in the
right side of (5.1), which has order seven.  The connected set `D-z` and
the vertex outside `D union T` lie on opposite sides, so seven-connectivity
forces equality.  \(\square\)

## 6. Scope and remaining gap

This theorem is a low-order structural reduction, not a completion theorem.
In the degree-eight five-subgraph setup, the connected subgraphs with traces
`I`, `J`, and the empty trace show that the boundary-full component has at
least three vertices.  Thus, after Theorem 2.1 removes the cutvertex case,
the use of two-connectivity above is genuine rather than a convention for a
one- or two-vertex graph.

However, a repair support selected by Theorems 2.1 or 3.1 need not contain
or preserve either of the already named connected subgraphs used by the
contact-allocation theorem.  Those named subgraphs can cross the displayed
cutvertex or two-vertex separator.  The reduction also supplies no common
boundary partition for the exact order-seven alternative.  Consequently,
an additional label-preserving exchange or colour-gluing theorem is still
required before these conclusions can close the active branch.
