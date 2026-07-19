# Same-shore edge responses do not synchronize two six-colourable closed shores

**Status:** written finite barrier with deterministic verifier; separate
internal audit in
[`hc7_exact7_crossing_disjoint_languages_barrier_audit.md`](hc7_exact7_crossing_disjoint_languages_barrier_audit.md).
This graph is not a counterexample to `HC_7`: it contains an explicit
`K_7`-minor model and has a proper seven-chromatic subgraph.

## 1. Statement

There is a finite graph `G` with an actual separation

\[
        V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}B,
        \qquad |S|=7,
\]

and two vertex-disjoint edges

\[
                         e=ab,\qquad f=cd
\]

from the same open shore `A` to `S`, with all of the following properties.

1. `G` is seven-connected and seven-chromatic.
2. The open shores are connected, anticomplete, and adjacent to every
   literal vertex of `S`.  Their maximum numbers of pairwise disjoint
   connected subgraphs adjacent to every vertex of `S` are

   \[
                            (\nu_A,\nu_B)=(2,1).
   \]

3. The boundary graph has chromatic number three.
4. Both intact closed shores `G[A\cup S]` and `G[B\cup S]` are exactly
   six-chromatic, but their six-colouring extension languages on `S` are
   disjoint.
5. The common deletion `G-{e,f}` has six-colourings of exactly the three
   endpoint signatures

   \[
      (\mathsf{equal},\mathsf{equal}),\quad
      (\mathsf{equal},\mathsf{proper}),\quad
      (\mathsf{proper},\mathsf{equal});
   \]

   the fourth signature is absent.  Every common-deletion colouring induces
   the same boundary equality partition

   \[
      \Pi=
      \bigl\{
        \{b\},\{d\},\{x_1,x_2\},\{y_1,y_3\},\{y_2\}
      \bigr\}.
   \]

6. Each of `G-e`, `G-f`, `G/e`, `G/f`, and `G/e/f` is exactly
   six-chromatic.  The partition `Pi` occurs in all three response types.
7. The full-connected-subgraph demand of `Pi` is

   \[
                    d_{G[S]}(\Pi)=3>\nu_B=1.
   \]

Thus even the correct boundary order, seven-connectivity, a `(2,1)` packing
vector, a high-demand common response, the complete three-chamber edge
response profile, and **six-colourability of both intact closed shores** do
not force a common intact-shore partition.  Any positive theorem needs
additional global information excluding this construction.  In the active
`HC_7` setting, the available inputs are `K_7`-minor exclusion and
six-colourability of every proper minor.

## 2. The response core and the separation

Let `J` have vertices

```text
a b ap bp pa qa pb qb c d.
```

On `a,ap,pa,qa`, put the diamond with missing edge `a ap`; on
`b,bp,pb,qb`, put the analogous diamond with missing edge `b bp`.  Thus the
first diamond has edges

```text
pa qa,  a pa, a qa,  ap pa, ap qa,
```

and analogously for the second.  Join each of `c,d` to both `ap,bp`, and
add

\[
                         e=ab,\qquad f=cd.             \tag{2.1}
\]

Let `W=K_{2,3}` have bipartition

\[
       X=\{x_1,x_2\},\qquad Y=\{y_1,y_2,y_3\},
\]

and make `W` complete to `J`.  Put

\[
       S=\{b,d,x_1,x_2,y_1,y_2,y_3\},
       \qquad A=V(J)-\{b,d\}.                          \tag{2.2}
\]

The second open shore has vertices

\[
                     B=Q\mathbin{\dot\cup}\{r,s,ell\},
       \qquad Q=\{q_0,q_1,q_2,q_3\}.
\]

Make `Q` a clique, make it complete to `r,s,y_1,y_2`, and add the path

\[
                         y_1-r-s-y_2.                  \tag{2.3}
\]

Make `ell` complete to `S` and adjacent to `q_0`.  The remaining
`B`--`S` adjacencies are given by the following table; repetitions of edges
already specified above are harmless.

| open vertex | boundary neighbours |
|---|---|
| `q0` | `b,d,y1,y2,y3` |
| `q1` | `d,x2,y1,y2,y3` |
| `q2` | `b,x2,y1,y2,y3` |
| `q3` | `b,x2,y1,y2,y3` |
| `r`  | `b,d,x2,y1,y3` |
| `s`  | `b,d,x2,y2` |

There are no other edges, in particular no `A`--`B` edge.  This completely
specifies a graph on 22 vertices and 124 edges.

The distinguished edges have the promised placement: `a,c` belong to `A`
and `b,d` belong to `S`.

## 3. Seven-connectivity

The graph `J` is two-connected: deleting any one vertex leaves the two
diamonds joined through at least one of `ab` and the two internally
disjoint routes through `c,d`.  Since `W` is two-connected and is complete
to `J`, the graph

\[
                         K=G[A\cup S]=J\vee W
\]

is seven-connected.  Indeed, a separator that leaves vertices on both
sides of the join must contain all five vertices of `W` and at least two
vertices separating `J`, or all ten vertices of `J`.

It remains to add `B`.  The six vertices

\[
                         H=Q\cup\{r,s\}
\]

induce `K_6`.  Directly from the boundary-neighbour table, for a nonempty
set `C\subseteq H`, the minimum of `|N_G(C)|`, grouped by
`|C|=1,...,6`, is

\[
                          9,9,9,8,7,7.                 \tag{3.1}
\]

When `ell\in C\subseteq B`, all seven vertices of `S` lie in `N_G(C)`.
Consequently every nonempty subset of `B` has at least seven neighbours
outside itself.

After deleting at most six vertices, the surviving part of `K` is connected.
Any component not meeting that part would be a nonempty subset of `B` whose
entire neighbourhood was deleted, contradicting (3.1).  Hence `G` is
seven-connected.  Deleting `S` leaves the two nonempty connected sets
`A,B`, so (2.2) is an actual order-seven separation.

## 4. The two intact extension languages are disjoint

In every proper three-colouring of a diamond, the ends of its missing edge
have the same colour.  Thus, after deleting `e,f`, the effective constraint
graph on `a,b,c,d` is `K_4-{ab,cd}`.  With both edges restored it is `K_4`.
Therefore

\[
                         \chi(J)=4.
\]

Since `W` is connected and bipartite,

\[
                 \chi(G[A\cup S])=\chi(J\vee W)=4+2=6. \tag{4.1}
\]

Every six-colouring in (4.1) uses disjoint palettes of orders four and two
on `J` and `W`; hence its restriction to `W` is the bipartition colouring,
and in particular

\[
                              c(y_1)=c(y_2).            \tag{4.2}
\]

On the other shore, `Q\cup\{r,s\}` is a literal `K_6`.  In every
six-colouring of `G[B\cup S]`, the clique `Q` uses four colours and the
adjacent vertices `r,s`, each complete to `Q`, use the other two.  Since
`y_1` is complete to `Q` and adjacent to `r`, while `y_2` is complete to
`Q` and adjacent to `s`, one necessarily has

\[
                              c(y_1)\ne c(y_2).          \tag{4.3}
\]

The explicit response colourings in Section 5 restrict to a six-colouring
of this closed shore, so its chromatic number is exactly six.  Equations
(4.2)--(4.3) prove that the intact extension languages are disjoint.
Thus `G` is not six-colourable.

## 5. Exact three-chamber response

Write `J_0=J-{e,f}`.  The diamond equalities reduce every three-colouring
of `J_0` to a three-colouring of `K_4-{ab,cd}`.  Hence its endpoint
signatures are exactly `EE,EP,PE`; simultaneous properness would require
four colours.  Also `b,d` receive different colours in every such
colouring, since `d bp` is an edge and the second diamond forces `b=bp`.

Here are normalized six-colourings for all three signatures.  In all rows,

```text
q0 q1 q2 q3 = 0 1 2 3
x1 x2 y1 y2 y3 r s = 0 0 4 5 4 5 4.
```

The core and `ell` receive the following colours.

| signature | `a b ap bp pa qa pb qb c d ell` |
|---|---|
| `EE` | `1 1 1 1 2 3 2 3 2 2 3` |
| `EP` | `1 1 1 1 2 3 2 3 3 2 3` |
| `PE` | `2 1 2 1 1 3 2 3 3 3 2` |

These colourings prove existence.  They also show that `G-e`, `G-f`, and
the indicated contractions are six-colourable: use `EP` for `G-e` and
`G/e`, `PE` for `G-f` and `G/f`, and `EE` for `G/e/f`.

For completeness, the common boundary partition is forced, not merely
selected.  The clique `Q\cup\{r,s\}` uses all six colours.  The vertices
`y_1,y_2` receive the two colours used by `s,r`, respectively.  The graph
`J_0` contains a triangle and is complete to `W`; while `W` already contains
the two colours on `y_1,y_2` and a common neighbour of both.  Thus `J_0`
and `W` each use exactly three disjoint colours.  It follows that
`x_1=x_2`.  Every vertex of `Q` and `r` is adjacent to `y_3`, forcing
`y_3=y_1`.  Finally `b,d` are distinct, as observed above.  This gives
exactly

\[
      \Pi=\{\{b\},\{d\},\{x_1,x_2\},\{y_1,y_3\},\{y_2\}\}.
\]

The literal `K_6=Q\cup\{r,s\}` survives all the named deletions and
contractions, so every named response graph is exactly six-chromatic.
Since `G-e` is six-colourable, restoring `e` and recolouring one endpoint
with a seventh colour gives `chi(G)<=7`.  Together with the disjoint
intact-shore languages, this proves `chi(G)=7`.

## 6. Packing and demand

Every vertex of `A` is adjacent to all of `W`.  Its portal sets at the two
remaining boundary vertices are

\[
       N_A(b)=\{a,pb,qb\},\qquad
       N_A(d)=\{c,ap,bp\}.                             \tag{6.1}
\]

The connected sets

\[
                       \{a,pa,ap\},\qquad \{pb,bp\}
\]

are disjoint and adjacent to every boundary vertex.  Conversely, every
connected boundary-full subset of `A` contains a path between the two
portal sets in (6.1), and every such path meets `\{ap,bp\}`.  Hence
`nu_A=2`.

The vertex `ell` is itself adjacent to all of `S`.  It is the unique
`B`-neighbour of `x_1`, so every boundary-full subset of `B` contains
`ell`.  Hence `nu_B=1`.

The boundary graph is

\[
                         G[S]=I_2\vee K_{2,3},
\]

and has chromatic number three.  The singleton blocks of `Pi` are
`b,d,y_2`; they induce the path `b-y_2-d`, whose clique number is two.
Therefore

\[
                         d_{G[S]}(\Pi)=5-2=3>1.         \tag{6.2}
\]

## 7. Exact trust boundary

The following seven disjoint connected sets form an explicit `K_7`-minor
model:

\[
 \{q_0\},\ \{q_1\},\ \{q_2\},\ \{q_3\},\
 \{y_1\},\ \{r\},\ \{s,y_2,x_2\}.                   \tag{7.1}
\]

Moreover `G-y_3` is still seven-chromatic.  The incompatibility
`y_1=y_2` versus `y_1\ne y_2` survives that deletion, while the `EP`
colouring above restricts to a six-colouring of `G-e-y_3`; restoring `e`
uses at most one new colour.  Thus `G` is not minor-minimal.

The construction therefore does **not** refute a terminal theorem in a
hypothetical minor-minimal `K_7`-minor-free counterexample.  It proves the
sharper dependency statement that making both intact closed shores
six-colourable does not repair the static three-response inference.  In the
active `HC_7` setting, global minor exclusion and additional proper-minor
colourings are the available sources of the missing host-level information.

## 8. Verification

Run from the repository root:

```text
python3 barriers/hc7_exact7_crossing_disjoint_languages_barrier_verify.py
```

Expected output:

```text
GREEN exact-seven crossing disjoint-languages barrier
order=22 size=124 kappa=7 boundary=7 chi_boundary=3 packing=(2,1)
common signatures=EE,EP,PE; PP absent; one five-block partition of demand=3
both intact closed shores are exactly 6-colourable and their languages are disjoint
full host contains explicit K7 minor; deleting y3 leaves a 7-chromatic graph
```

The verifier exhausts all vertex cuts of order at most six, all connected
boundary-full subsets of both shores, and all normalized common-deletion
six-colourings.  It also checks the two closed-shore chromatic assertions,
the explicit response colourings, the common partition and its demand, the
`K_7` branch sets, and the noncritical proper subgraph.
