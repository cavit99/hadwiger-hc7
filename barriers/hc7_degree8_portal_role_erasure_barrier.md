# Terminal-free portal cuts can erase the independent-block role

**Status:** explicit barrier/counterexample to an intermediate local
inference; deterministic verifier and separate internal audit **GREEN** in
[`hc7_degree8_portal_role_erasure_barrier_audit.md`](hc7_degree8_portal_role_erasure_barrier_audit.md).
This is not a counterexample to `HC_7` and does not refute a theorem using
the full seven-connected, minor-minimal host assumptions.

The adjacent verifier is
[`hc7_degree8_portal_role_erasure_barrier_verify.py`](hc7_degree8_portal_role_erasure_barrier_verify.py).

## 1. The invalid local inference

The two applications of the five-terminal portal reduction, one with the
independent triple `I` and one with the independent triple `T`, need not
produce two different connected sets.  In particular, the following local
inference is false:

> the aligned path, the four incidence splits, universal
> connector--carrier intersection, at most one two-defect post-path
> component, and one positive-excess completion cut for each of `I,T`
> force two disjoint adjacent connected sets with one common boundary
> defect of order at most two.

The obstruction is the terminal-free branch of the completed separation.
That branch can forget which independent triple generated it.

### Lemma 1.1 (terminal-free role erasure)

For \(B\in\{I,T\}\), let \(U_B\subseteq Q\) be the five nominated
representatives in a five-terminal completion \(H_B^+\).  Suppose that a
nonempty connected set \(C\subsetneq Q\) and a set \(K\subseteq Q\) satisfy

\[
 C\cap K=\varnothing,\qquad
 N_{G[Q]}(C)\subseteq K,\qquad |K|\le5,
 \qquad Q-(C\cup K)\ne\varnothing,                    \tag{1.1}
\]

and

\[
                         C\cap(U_I\cup U_T)=\varnothing. \tag{1.2}
\]

Then `C` is a terminal-free component of both \(H_I^+-K\) and
\(H_T^+-K\).

#### Proof

Every original edge from `C` to `Q-C` ends in `K` by (1.1).  Every virtual
completion edge has both ends in the corresponding nominated set `U_B`,
which is disjoint from `C` by (1.2).  Thus neither completion adds an edge
from `C` to \(Q-(C\cup K)\).  Connectedness makes `C` a component after
deleting `K`, and the last condition in (1.1) supplies another open side.
No nominated terminal lies in `C`. \(\square\)

If additionally \(|N_G(C)|\) is at least nine, all positive-excess
arithmetic is the same in the two applications.  In a contraction-critical
host, the equal-endpoint response for every entering edge and the mismatch
with a fixed intact-shore colouring also depend only on the literal sets
`C,N_G(C)`, not on the name `I` or `T`.  The only role-dependent data then
left are nominees and virtual edges lying entirely outside `C`.

## 2. A minimum-order decorated shore

Put

\[
 I=\{i_1,i_2,i_3\},\qquad T=\{t_1,t_2,t_3\},\qquad
 S=I\mathbin{\dot\cup}T\mathbin{\dot\cup}\{p,q\}.
\]

On `S`, take the disjoint union of

\[
 K_3[p,i_2,t_2],\qquad K_3[q,i_3,t_3],\qquad K_2[i_1,t_1]. \tag{2.1}
\]

Thus `I,T` are independent, `pq` is absent, the boundary has independence
number three, and deletion of any two boundary vertices leaves no
`K_4` minor.

Let

\[
 Q=\{a,b,c,d,r_2,r_3,s_3\}.                            \tag{2.2}
\]

Its internal edges are

\[
 ca,\ cb,\ cr_2,\ cr_3,\ cs_3,\ da,\ db.              \tag{2.3}
\]

The boundary contacts are

\[
\begin{array}{c|c}
v&N_G(v)\cap S\\ \hline
a&\{p,i_1\}\\
b&\{q,t_1\}\\
c&\{i_2,i_3,t_2,t_3\}\\
d&\{i_1,t_1\}\\
r_2&\{i_2,t_2\}\\
r_3&\{i_3\}\\
s_3&\{t_3\}.
\end{array}                                             \tag{2.4}
\]

The set `Q` is connected and adjacent to every vertex of `S`.  Its order
is seven, the smallest order not covered by the portal reduction's
small-shore alternative.

For a bilateral local decoration, add `u` adjacent exactly to `S`, and an
opposite open shore `F={x,y}` with edge `xy`, where `x` is adjacent to
`S-{q}` and `y` to `S-{p}`.  There are no edges between `Q` and `F`.
Then `G-N[u]` has exactly the two boundary-full components `Q,F`.

## 3. Aligned paths, incidence splits, and entanglement

The closed `Q`-shore has a proper colouring inducing

\[
                         I\mid T\mid\{p,q\},           \tag{3.1}
\]

in which

\[
                         P_Q=pacbq                     \tag{3.2}
\]

is bichromatic.  Explicitly, give `I,T,{p,q}` colours `0,1,2`, give
`a,b,r_2` colour `3`, give `c,d` colour `2`, and give `r_3,s_3` colours
`1,0`, respectively.  The closed `F`-shore has a proper colouring inducing

\[
                         I\mid T\mid\{p\}\mid\{q\},   \tag{3.3}
\]

in which

\[
                         P_F=pxyq.                     \tag{3.4}
\]

Here give `I,T,p,q,x,y` colours `0,1,2,3,3,2`, respectively.  In each
shore the full two-colour component containing `q` also contains `p`, so
these are opposite failed lifts of the same singleton boundary operation.
Their union is a simple odd cycle of length seven.

Deleting \(P_Q^\circ=\{a,c,b\}\) leaves the four singleton components

\[
                         \{d\},\{r_2\},\{r_3\},\{s_3\}. \tag{3.5}
\]

Their boundary contact sets are, respectively,

\[
 \{i_1,t_1\},\quad\{i_2,t_2\},\quad\{i_3\},\quad\{t_3\}. \tag{3.6}
\]

Hence the `I` and `T` incidence graphs both split, and no component misses
exactly two vertices of `S`.  The path \(P_F\) fills its open shore, so its
two incidence splits hold vacuously.

The universal connector--carrier conclusion also holds literally in both
shores.  In `Q`, every root connector contains `a,b`, because these are the
unique `Q`-neighbours of `p,q`.  Every `I`-carrier and every `T`-carrier
contains at least one of `a,b`.  For example, an `I`-carrier avoiding `a`
must use `d` to meet `i_1`, and `d` can connect to the other two `I`
contacts only through `b`; the other cases are symmetric.  In `F`, every
root connector contains both `x,y`, so it meets every nonempty carrier.

## 4. The same positive lobe in both completions

Put

\[
 K=\{a,b,r_2,r_3,s_3\},\qquad C=\{c\}.                \tag{4.1}
\]

For the `I`-completion nominate

\[
 (p,q,i_1,i_2,i_3)\longmapsto(a,b,d,r_2,r_3),          \tag{4.2}
\]

and for the `T`-completion nominate

\[
 (p,q,t_1,t_2,t_3)\longmapsto(a,b,d,r_2,s_3).          \tag{4.3}
\]

Each is a system of five distinct representatives.  In either completed
graph, deleting `K` leaves `C` as a terminal-free singleton component and
leaves the nonempty component `{d}` on the other side.  Moreover

\[
 N_{G[Q]}(C)=K,\qquad
 N_G(C)\cap S=\{i_2,i_3,t_2,t_3\},\qquad |N_G(C)|=9.   \tag{4.4}
\]

Thus the two positive-excess witnesses can be literally identical, with
internal boundary five and boundary defect four.

### Proposition 4.1 (no common-near-full pair)

There do not exist disjoint connected sets \(A_0,A_1\subseteq Q\) such
that

\[
                 |(N_G(A_0)\cap S)\cap(N_G(A_1)\cap S)|\ge6. \tag{4.5}
\]

#### Proof

The vertex `p` has the unique `Q`-neighbour `a`, and `q` has the unique
`Q`-neighbour `b`.  Neither can belong to the common contact set of two
disjoint sets.  A common set of order at least six would therefore be all
of `I union T`.

Both connected sets would have to meet the two portal pairs

\[
             N_Q(i_1)=\{a,d\},\qquad N_Q(t_1)=\{b,d\}. \tag{4.6}
\]

If neither set contains `d`, both must contain `a,b`, contradicting
disjointness.  If one contains `d`, the other must contain both `a,b`.
The first set then cannot contain `a` or `b`; since these are the only
`Q`-neighbours of `d`, it is the singleton `{d}` and does not meet the
remaining four boundary vertices.  This is again a contradiction.
\(\square\)

## 5. Exact scope and next target

The construction retains the compact degree-eight boundary, two full
shores, one named bilateral bichromatic operation, all four incidence
splits, universal connector--carrier intersection, the sparse-two-defect
condition, both five-terminal completion cuts, and the exact positive-excess
arithmetic.  It shows that independent portal applications supply no
coupling in their terminal-free branch.

It deliberately fails the full hypothetical-counterexample assumptions.
For example, `r_3` has neighbourhood `{c,i_3}`, so the graph is not
seven-connected.  The verifier also checks an explicit proper five-colouring of
the whole graph.  Consequently an intact colouring separates the ends of
every edge entering `C`, and the contraction-critical equal-endpoint
responses fail.  The graph is not asserted to be `K_7`-minor-free.  It
therefore does not refute the live paired-lobe theorem, which must use
precisely those missing global inputs.

The smallest honest next theorem is the **common terminal-free lobe
closure**: in the full live host, if one positive-excess connected set
behind at most five internal vertices is terminal-free for valid `I` and
`T` completions, then force a primary terminal outcome, a generic
exact-seven response, a strict response-preserving order-eight reduction,
or two adjacent connected sets with one common boundary defect of order at
most two.  Until this branch is closed, uncrossing two independently named
lobes assumes a distinction that need not exist.
