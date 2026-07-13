# Strict order-four full-gate closure

## 1. Result

Let

\[
 S=A\mathbin{\dot\cup}B\mathbin{\dot\cup}C\mathbin{\dot\cup}\{s\},
 \qquad |A|=|B|=|C|=2,
\]

and suppose `G[S]` is the complete four-partite graph
`K_{2,2,2,1}` with these parts.  Let `D` be a four-vertex clique in one
component of `G-S`, and let `R` be a connected subgraph in a different
component of `G-S` which is adjacent to every vertex of `S`.  Assume:

1. `D` is adjacent to every vertex of `S`; and
2. for every nonempty proper `X subset D`,
   \[
        |N_D(X)-X|+|N_S(X)|\ge 8.                 \tag{1.1}
   \]

The two components are anticomplete because they are distinct components
of `G-S`.

### Theorem 1.1 (strict four-core completion)

Under these hypotheses, `G` contains a `K_7` minor.

Consequently no order-four strict relative-boundary obstruction survives
behind a `K_{2,2,2,1}` adhesion and an opposite full shore.  This conclusion
does not require the three pairwise packet hypotheses, failure of a
simultaneous triple packet, or an operation-critical colouring state.

## 2. Cross-part transversal lemma

Put `U=A union B union C`.

### Lemma 2.1

There is a matching from the four vertices of `D` into their portal sets in
`U` which leaves two unmatched vertices belonging to different two-vertex
parts of `U`.

#### Proof

For a singleton `x in D`, (1.1) and `D=K_4` give

\[
                 |N_S(x)|\ge 5.
\]

After deleting `s`, every vertex of `D` therefore has at least four
neighbours in the six-vertex set `U`.  For every nonempty `X subseteq D`,
the union of its neighbour sets in `U` consequently has order at least
four, and hence at least `|X|`.  Hall's theorem supplies a matching `f`
saturating `D` into `U`.

If the two unmatched vertices lie in different parts, this is the desired
matching.  Otherwise they are the two members `u,u'` of one part.  Fullness
of `D` gives a vertex `x in D` adjacent to `u`.  Replace the matching edge
`x f(x)` by `xu`.  The new unmatched vertices are `u'` and `f(x)`.
The latter was matched before the exchange, so it lies outside the omitted
part `{u,u'}`.  Thus the new unmatched pair belongs to different parts.
\(\square\)

The exchange is the useful structural point: the apparent
pairwise-but-not-triple packet circuit disappears after a single
boundary-faithful transversal rotation.

## 3. Explicit branch sets

Let `f` be the matching in Lemma 2.1 and let `u,v` be the two unmatched
vertices.  The following seven disjoint connected sets form a `K_7` model:

\[
       \{x,f(x)\}\quad(x\in D),\qquad
       R,\qquad \{s\},\qquad \{u,v\}.             \tag{3.1}
\]

The four first bags are connected by the matching portal edges and are
pairwise adjacent through the clique `D`.  Each meets `S`, so it is adjacent
to the full shore `R`.  The singleton `s` is adjacent to every vertex of
`U`, hence to all four rooted `D` bags and to `{u,v}`.  The set `{u,v}` is
connected because `u,v` lie in different parts.

It remains only to check that `{u,v}` sees every rooted `D` bag.  For a
root `f(x)`, the only vertex of `U` nonadjacent to it is its mate in the
same two-vertex part.  Since `u,v` lie in different parts, they cannot both
be that mate.  Hence at least one of `u,v` is adjacent to `f(x)`.  Finally,
fullness of `R` supplies all its adjacencies to `{s}`, `{u,v}`, and the four
rooted bags.  Thus all 21 pairs of bags in (3.1) are adjacent, proving
Theorem 1.1.

## 4. The displayed `K_4` packet circuit

Number the shore vertices `d_0,d_1,d_2,d_3`.  For the contact assignment

\[
\begin{array}{c|c}
0&d_0,d_1\\
1&d_2,d_3\\
2&d_0,d_1,d_2,d_3\\
3&d_0,d_1,d_2,d_3\\
4&d_1,d_3\\
5&d_0,d_2\\
6&d_0,d_1,d_2,d_3,
\end{array}                                                     \tag{4.1}
\]

one cross-part matching is

\[
 d_0\mapsto3,qquad d_1\mapsto4,qquad
 d_2\mapsto5,qquad d_3\mapsto1,
\]

leaving `0,2`.  Contracting the far shore to `r`, the seven bags are

\[
 \{d_0,3\},\ \{d_1,4\},\ \{d_2,5\},\ \{d_3,1\},\
 \{r\},\ \{6\},\ \{0,2\}.                    \tag{4.2}
\]

This is a spanning `K_7` model of the twelve-vertex quotient.

For completeness, (4.1) really is the proposed packet obstruction.  An
`01`-carrier needs at least one vertex from each of
`{d_0,d_1}` and `{d_2,d_3}`, while a `45`-carrier needs at least one from
each of `{d_1,d_3}` and `{d_0,d_2}`.  A `23`-carrier may be a singleton.
Thus three simultaneous carriers would use at least `2+1+2=5` vertices.
On the other hand the disjoint carriers

```text
01 | 23 : {d0,d2} | {d1}
01 | 45 : {d0,d3} | {d1,d2}
23 | 45 : {d0}    | {d1,d2}
```

give every two-demand packet.  The singleton, pair and triple portal
unions have orders at least `5,6,7`, respectively, so (1.1) holds.

The quotient has vertex-connectivity exactly seven.  The boundary `S` is
a seven-cut separating `D` from `r`.  Conversely, deleting at most six
vertices cannot separate a surviving part of `D`: for `1 <= |X| <= 3`,
(1.1) says that deleting `N_D(X)-X` and `N_S(X)` costs at least eight,
and separating all of `D` from the boundary costs all seven boundary
vertices.  If `r` survives it joins all surviving boundary vertices.  If
`r` is deleted, at least two boundary vertices survive; `K_{2,2,2,1}`
connects them unless they are the two vertices of one part, and in that
last case all four vertices of `D` survive and fullness joins both vertices
through `D`.  Hence no cut of order at most six exists.

## 5. Independent executable audit

Run

```text
python3 strict_order4_full_gate_verify.py
```

It independently checks (4.2), computes connectivity seven and the unique
minimum cut `S`, and then performs a complete Z3/branch-set replay over
every `4 x 7` contact matrix satisfying fullness and (1.1).  A proposed
matrix is blocked only by the contact edges of a verified explicit `K_7`
model.  The run terminates with

```text
displayed connectivity 7; unique minimum cut (0, 1, 2, 3, 4, 5, 6)
displayed K7 bags ((3, 7), (4, 8), (5, 9), (1, 10), (11,), (6,), (0, 2))
all strict K4 contact matrices {'status': 'unsat', 'iterations': 55}
```

The computation is redundant for Theorem 1.1; its purpose is to audit the
portal indexing, connectivity claim, and every branch-set adjacency.
