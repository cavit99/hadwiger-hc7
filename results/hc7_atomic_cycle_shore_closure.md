# Atomic cyclic-shore closure

**Status:** proved and independently audited.

This note closes an unbounded family in the fully crossed atomic residue.
It uses only relative seven-connectivity, the audited deleted-root
normalization, and the audited near-full two-carrier state exchange.  No
choice of an equality-state orientation and no finite boundary enumeration
is involved.

## 1. Setup

Use the atomic exact-seven separation

\[
 V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad S=W\mathbin{\dot\cup}\{u\},\qquad |W|=6,
\]

where:

1. `G` is seven-connected, `K_7`-minor-free, is not six-colourable, and
   every proper minor is six-colourable;
2. there is no `A-R` edge;
3. `A` is connected and `S`-full;
4. `zu` is the unique `A-u` edge; and
5. `R` contains two disjoint adjacent connected `S`-full packets; and
6. `G[S]` is either connected and bipartite or is
   `K_{1,3} dotunion K_3`, the two audited atomic frontier forms.

The independently audited root-deletion normalization gives

\[
                         N_S(A-z)=W.                    \tag{1.1}
\]

The independently audited near-full two-carrier exchange says that this
setup is impossible whenever there are disjoint nonempty connected adjacent
sets `X,Y subseteq A`, with `z in X`, such that

\[
                  |N_S(X)|\ge6,\qquad |N_S(Y)|\ge6.     \tag{1.2}
\]

## 2. Uniform cycle theorem

### Theorem 2.1 (every atomic cycle of order at least four closes)

In the setup of Section 1, suppose `G[A]` is a cycle of order `n>=4`.
Then the atomic separation cannot occur in a hypothetical counterexample.

### Proof

Every vertex of the cycle has exactly two neighbours in `A`.  Apply
relative seven-connectivity to the singleton set `{v}`.  It gives

\[
                        2+|N_S(v)|\ge7.                 \tag{2.1}
\]

Thus every `v in A` has at least five literal boundary neighbours.  If
`v ne z`, the uniqueness of the edge `zu` says that `v` has no neighbour
at `u`; hence

\[
                         |N_W(v)|\ge5.                  \tag{2.2}
\]

The vertex `z` sees `u`, so (2.1) also gives

\[
                         |N_W(z)|\ge4.                  \tag{2.3}
\]

Let `x,y` be the two cycle neighbours of `z`.  Consider the two cyclic
edge cuts

\[
\begin{aligned}
 X_x&=\{z,x\},&Y_x&=A-\{z,x\},\\
 X_y&=\{z,y\},&Y_y&=A-\{z,y\}.
\end{aligned}                                           \tag{2.4}
\]

Because `n>=4`, all four sets in (2.4) are nonempty.  Each induces a
connected path, and each displayed pair is adjacent through a literal
cycle edge.

The set `X_x` contacts `u` through `z` and at least five vertices of `W`
through `x`, by (2.2).  Therefore

\[
                         |N_S(X_x)|\ge6.                \tag{2.5}
\]

The same argument gives `|N_S(X_y)|>=6`.

We claim that at least one of `Y_x,Y_y` is `W`-full.  Suppose not.  Since
every vertex of either set lies outside `z`, (2.2) says that each such
vertex misses at most one member of `W`.  Consequently there are literals
`d_x,d_y in W` such that every vertex of `Y_x` misses `d_x` and every
vertex of `Y_y` misses `d_y`.

The overlap

\[
                   Y_x\cap Y_y=A-\{z,x,y\}             \tag{2.6}
\]

is nonempty when `n>=4`; for `n=4` it consists of the unique cycle vertex
opposite `z`.  A vertex in (2.6) misses both `d_x` and `d_y`, while (2.2)
says that it misses at most one member of `W`.  Hence `d_x=d_y=:d`.

Now `Y_x` contains `y` and every vertex of (2.6), while `Y_y` contains
`x` and every vertex of (2.6).  Thus every vertex of `A-z` misses `d`.
This contradicts the deleted-root fullness (1.1).  The claim follows.

Choose `q in {x,y}` so that `Y_q` is `W`-full.  It cannot see `u`, since
it avoids `z`, and hence

\[
                         |N_S(Y_q)|=6.                  \tag{2.7}
\]

Equations (2.5)--(2.7) show that the disjoint connected adjacent pair
`X_q,Y_q`, with `z in X_q`, satisfies (1.2).  The audited near-full
two-carrier state exchange then six-colours `G` or gives a literal
`K_7`, contradicting the setup.  \(\square\)

## 3. Exact triangle boundary of the argument

For `n=3`, the two remainders in (2.4) are the disjoint singletons
`{y}` and `{x}`.  They may miss two different members of `W`, so the
overlap step (2.6) is unavailable.  The theorem therefore does not claim
the atomic triangle.  This is a genuine boundary of this proof mechanism,
not a hidden appeal to finite enumeration.

## 4. Consequence for the crossed-hull programme

Every surviving two-connected atomic shore is not itself a cycle of order
at least four.  Thus the fully crossed residue cannot be an arbitrarily
long bare cyclic shore: it must contain a chord, an off-cycle bridge, or
other noncyclic structure (apart from the unclaimed triangle cell).

This theorem does **not** by itself close a cycle torso in a larger Tutte
decomposition.  Attachments outside such a torso increase the actual
internal neighbourhoods in the relative-cut inequality, so the singleton
support estimate (2.2) need not survive.  Any torso-level use requires a
separate attachment-allocation argument.
