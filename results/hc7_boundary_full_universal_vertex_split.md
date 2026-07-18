# A universal boundary-contact vertex in a three-connected component

**Status:** written proof; separate internal audit pending.  This is a
conditional structural lemma.  It does not preserve a previously chosen
minor model or a boundary colouring, and it does not prove `HC_7`.

## 1. Nonseparating-path input

We use Tutte's nonseparating-path theorem in the following standard form.

> **Tutte's theorem.**  If `D` is three-connected and `x,y,w` are distinct
> vertices of `D`, then `D-w` contains an `x-y` path `P` such that
> `D-V(P)` is connected.

The exact formulation above is Theorem 1.2.1 of Yingjie Qian,
*Non-Separating Paths in Graphs*, PhD dissertation, Georgia Institute of
Technology, 2022, where it is attributed to W. T. Tutte, *How to Draw a
Graph*, Proceedings of the London Mathematical Society (3) **13** (1963),
743--767, DOI
[`10.1112/plms/s3-13.1.743`](https://doi.org/10.1112/plms/s3-13.1.743).
Qian's statement is also deduced there from Tutte's equivalent two-path
form: two internally disjoint `x-y` paths can be chosen so that deleting
the vertices of either path leaves a connected graph.

## 2. Setup

Let `G` be a seven-connected graph, let `T` be a set of seven vertices,
and let `D` be a component of `G-T`.  Assume that

\[
                 V(G)-(V(D)\cup T)\ne\varnothing .       \tag{2.1}
\]

Thus `T` is an actual boundary between `D` and a nonempty opposite side.
Since `N_G(D)\subseteq T`, seven-connectivity gives

\[
                         N_G(D)=T.                       \tag{2.2}
\]

Fix `b in T` and a two-element set

\[
                         I\subseteq T-\{b\}.             \tag{2.3}
\]

A **repair support** is a connected subgraph of `G[D]` adjacent to `b`
and to at least one vertex of `I`.  A **residual boundary-full subgraph**
is a connected subgraph of `G[D]`, disjoint from the repair support, that
is adjacent to every vertex of `T`.

## 3. Universal-contact split

### Theorem 3.1

Suppose `D` is three-connected and contains a vertex `w` adjacent to every
vertex of `T`.  Then at least one of the following holds.

1. For some `t in {b} union I`,

   \[
              N_G(D-w)=\{w\}\cup(T-\{t\}),              \tag{3.1}
   \]

   so the right side of (3.1) is an actual separation boundary of order
   seven.
2. There is a path `P` in `D-w` whose vertex set is a repair support and
   `D-V(P)` is a connected residual boundary-full subgraph.  The path is
   allowed to consist of one vertex.

### Proof

Put

\[
 X=N_D(b)-\{w\},\qquad
 Y=\left(\bigcup_{i\in I}N_D(i)\right)-\{w\}.           \tag{3.2}
\]

Suppose first that `X` is empty.  Then `w` is the unique neighbour of `b`
in `D`.  Three-connectivity makes `D-w` connected and nonempty.  Moreover,

\[
                 N_G(D-w)\subseteq \{w\}\cup(T-\{b\}).  \tag{3.3}
\]

The connected set `D-w` and the nonempty opposite side in (2.1) lie on
opposite sides of this neighbourhood.  Seven-connectivity gives
`|N_G(D-w)|>=7`; the set on the right of (3.3) has order seven.  Equality
therefore holds, proving outcome 1 with `t=b`.

If `Y` is empty, then both members of `I` have `w` as their only neighbour
in `D`, and

\[
                 N_G(D-w)\subseteq \{w\}\cup(T-I).     \tag{3.4}
\]

The right side has order six, while `D-w` and the nonempty opposite side
in (2.1) make this a genuine separation.  This contradicts
seven-connectivity.  We may henceforth assume that `X` and `Y` are both
nonempty.

If there are distinct vertices `x in X` and `y in Y`, apply Tutte's theorem
to `x,y,w`.  It gives an `x-y` path `P` in `D-w` for which `D-V(P)` is
connected.  The path is adjacent to `b` through `bx`; by the definition of
`Y`, its other end `y` is adjacent to some member of `I`.  Thus `V(P)` is
a repair support.  The residual graph contains `w`, because the path
avoids `w`.  Since `w` is adjacent to every vertex of `T`, the connected
graph `D-V(P)` is boundary-full.  This is outcome 2.

It remains that no such distinct choice exists.  Nonempty sets `X,Y` with
no pair of distinct representatives must satisfy

\[
                              X=Y=\{z\}                 \tag{3.5}
\]

for one vertex `z`.  Take the one-vertex path `P=z`.  It is adjacent to
`b` and, because `z in Y`, to at least one member of `I`.  Three-connectivity
makes `D-z` connected; it contains `w`, and hence is adjacent to all of
`T`.  Outcome 2 follows again. \(\square\)

## 4. Scope

The theorem handles every endpoint degeneracy: an absent off-`w` contact
gives the unique-portal separation, two distinct contacts give Tutte's
path, and a single common contact gives the one-vertex repair support.
The conclusion is stronger than merely finding two disjoint connected
subgraphs: the residual is the whole connected graph left after deleting
the repair path.

The lemma does not say that this path contains, avoids, or preserves any
previously named branch set inside `D`.  In applications requiring labelled
minor-model data, that is a separate obligation.
