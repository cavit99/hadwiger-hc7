# Load-minimal total-contraction states give a literal Kempe packet

## Status

This note proves the strongest conclusion obtainable from minimizing the
boundary-colour load at one literal carrier vertex.  It gives actual
bichromatic paths in the opposite closed shore between every two colour
portal classes seen by that vertex.  It does **not** align those colour
classes with different branch-set labels.  The final construction shows
that all of the paths may be trapped in one nonsingleton foreign bag while
the protected two-row linkage in the planar carrier remains absent.

Thus load minimization supplies a useful dynamic packet, but the packet
closes the locked gate only after an additional label-distribution or
opposite-state hypothesis.

## 1. Literal portal notation

Let `K` be a connected vertex set with at least two vertices, put

\[
                         S=N_G(K),
\]

and contract a spanning tree of `G[K]` to a vertex `z`.  Write
`M=G/K` and `O=G-K`.  In every proper six-colouring `c` of `M`, the
vertex `z` is adjacent to every member of `S`, so no vertex of `S` has
colour `c(z)`.

For `x in K` and a colour `i`, put

\[
 P_i(x,c)=\{s\in N_G(x)\cap S:c(s)=i\},\qquad
 \lambda_x(c)=|\{i:P_i(x,c)\ne\varnothing\}|.             \tag{1.1}
\]

The nonempty `P_i(x,c)` are labelled sets of actual boundary vertices;
they are not colour classes treated as connected branch sets.

## 2. The load-minimal packet

### Theorem 2.1 (pairwise literal Kempe packet)

Fix `x in K`, and among all proper six-colourings of `M` choose `c`
minimizing `lambda_x(c)`.  For every two distinct colours `i,j` seen at
`x`, some connected component of

\[
                         O[c^{-1}(\{i,j\})]               \tag{2.1}
\]

meets both `P_i(x,c)` and `P_j(x,c)`.  Equivalently, there is an
`i-j` bichromatic path in the unchanged opposite shore `O` whose ends
are literal boundary neighbours of `x`, one in each of the two named
portal sets.

#### Proof

Suppose no component in (2.1) meets both portal sets.  Let `U` be the
union of all `i-j` components which meet `P_i(x,c)`, and interchange
colours `i,j` on `U`.  This is an ordinary Kempe switch and preserves a
proper colouring of `O`.

The contracted vertex `z` has neither colour `i` nor colour `j`: its
colour is absent from all of `S`, whereas `i,j` are both represented in
`N_G(x) cap S`.  Consequently the same switch, leaving `z` fixed, is a
proper colouring of all of `M`.  Every member of `P_i(x,c)` now has
colour `j`.  By the supposition, `U` contains no member of
`P_j(x,c)`, so the old `j`-portals keep colour `j`.  No boundary
neighbour of `x` has colour `i` after the switch, while every other
colour previously seen at `x` is unchanged.  The new colouring has
load `lambda_x(c)-1`, contradicting the choice of `c`.  QED.

### Corollary 2.2 (conditional active-face output)

Under the fully rural hypotheses of the active-face list-splice theorem,
fix a facial vertex `x` and minimize its load over all total-contraction
colourings.  If this minimum is `r>=4`, the opposite shore contains a
complete system of pairwise bichromatic connections among the `r`
literal portal sets `P_i(x,c)`.  If the minimizing state has
`L(x)={c(z)}`, then `r=5`.

The active-face list-splice theorem says that **each** contraction
colouring has some heavy vertex.  It does not by itself say that one
fixed facial vertex remains heavy after its own load is minimized:
heaviness may migrate around the face as the colouring changes.  Thus
the hypothesis `r>=4` in this corollary is substantive, not automatic.

This conclusion is simultaneous only for the one chosen vertex.  A
Kempe switch which decreases the load at `x` may increase the load at a
different facial vertex, so lexicographically minimizing an arbitrarily
ordered vector does not automatically give Theorem 2.1 at every
coordinate.

### Proposition 2.3 (lexicographic vectors do not give all packets)

The preceding warning is sharp, even for a two-vertex carrier.  Let
`K=x_1x_2`, let `S={a,b,d}`, and add exactly the carrier--boundary
edges

\[
       x_1a,x_1d,\qquad x_2a,x_2b,
\]

together with the boundary edge `bd`.  After contracting `K` to `z`,
the vertex `z` is adjacent to all of `a,b,d`.

Order the load vector as `(lambda_{x_1},lambda_{x_2})`.  Its
lexicographic minimum is `(1,2)`: attaining first coordinate one forces
`a,d` to have the same colour, while the edge `bd` forces `b` to have
a different colour.  In such a minimum colouring, put
`c(a)=c(d)=i` and `c(b)=j`.  The `i-j` subgraph of `O=G-K` has
components `{a}` and `{b,d}`.  Hence no component meets both
`P_i(x_2,c)={a}` and `P_j(x_2,c)={b}`.

Switching the singleton component `{a}` changes the vector to `(2,1)`:
it improves the second coordinate only by worsening the first.  Thus a
lexicographically minimum facial load vector yields Theorem 2.1 at its
first coordinate, but need not yield it at later heavy coordinates.
Any simultaneous use must supply a potential which the relevant switch
does not increase elsewhere, or select and minimize one literal vertex
at a time.

## 3. The nonsingleton-bag falsification gate

The packet is not by itself the protected linkage required by the locked
two-row theorem.  Here is a literal target-free local witness.

Let `K=C_8^2` be the square-antiprism in its plane embedding, with the
four even vertices on one facial square in the alternating order

\[
                         A_L,A_R,P_H,P_Q.                  \tag{3.1}
\]

Let `x=A_L`.  Add a disjoint `K_4` on vertices
`s_1,s_2,s_3,s_4`, join every `s_i` to `x`, and add no other edge
between this `K_4` and the carrier.  Regard

\[
                         B=\{s_1,s_2,s_3,s_4\}             \tag{3.2}
\]

as one connected foreign branch bag.  Contracting `K` to `z` gives a
proper five-colouring in which `B` receives four distinct colours and
`z` a fifth colour (and hence also a six-colouring).  In every proper
colouring the clique `B` uses four different colours, so the load at
`x` is exactly four and is already minimum.

For every pair of those four colours, the required bichromatic path is
the corresponding literal edge of `B`.  Thus Theorem 2.1 is realized in
its strongest pairwise form, but every path is contained in the same
foreign bag.  Meanwhile the two paths

\[
                  A_L-P_H,\qquad A_R-P_Q                  \tag{3.3}
\]

cannot be vertex-disjoint inside `K`, since their four terminals
alternate on one face.

The graph is `K_7`-minor-free.  It is a one-sum at `x` of the
square-antiprism and the `K_5` induced by `B union {x}`.  A clique minor
of order at least three in a one-sum is contained in one summand after
pruning the possible cutvertex bag; the two summands have Hadwiger number
at most four and five, respectively.

This example deliberately fails seven-connectivity and full
contraction-criticality.  Its role is exact: even load-minimality,
literal pairwise bichromatic paths, planarity of the carrier, and
`K_7`-minor exclusion do not distinguish four palette roles when all
four occur in one nonsingleton model bag.

## 4. Exact remaining positive statement

To use Theorem 2.1 at the locked gate, one must prove at least one of the
following from the global hypotheses:

1. four relevant portal sets admit disjoint fixed extensions into four
   literal model rows, so the active-root face theorem applies;
2. some bichromatic component necessarily exits every single foreign
   owner and gives the protected `L-H/R-Q` linkage after a
   label-preserving transfer; or
3. the equality partition producing the packet is also produced by an
   operation in the opposite open shore, so the crossed state-splice
   colours `G`.

The theorem converts load minimality into actual opposite-shore paths.
It does not supply any of these three label/state properties, and the
single-bag witness shows why one of them is indispensable.
