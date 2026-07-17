# A shortest locked path interval can migrate through a Kempe orbit

**Status:** barrier to an intermediate recolouring claim; written proof;
adjacent internal audit.  The graphs below are seven-connected and
seven-chromatic, but they contain `K_7` minors and are not claimed to be
minor-minimal.  They are not counterexamples to `HC_7`.

## 1. Claim ruled out

The contracted-path list obstruction suggests choosing a six-colouring
whose first dynamic-programming failure occurs as late as possible, and
then choosing a shortest locked odd subpath.  One might hope that, at
such an extremal colouring, every pair of noncontracted colours has a
bichromatic component mixed at both locked endpoints; otherwise a Kempe
interchange would strictly improve the lock.

This is false even for seven-connected, seven-chromatic graphs.  In the
family below a Kempe interchange transfers a one-edge lock from one end
of the path to the other.  In the colouring with the latest possible
first failure, one endpoint of the lock has no mixed component for the
two relevant colours, but every interchange which changes that fact moves
the first failure earlier.  The shortest locked interval has length one
throughout the full colouring space.

## 2. Construction

Fix an integer `m>=2`.  Let

\[
 K=K[K_0,K_1]\cong K_{m,m},\qquad
 L=K[L_0,L_1]\cong K_{m,m}
\]

be disjoint complete bipartite graphs, with all four displayed sides of
order `m`.  Add an induced path

\[
                         P=v_1v_2v_3v_4.
\]

Define `F_m` by the following additional adjacencies:

- `v_1` and `v_4` are complete to `K union L`;
- `v_2` is complete to `K_0 union L_1`; and
- `v_3` is complete to `K_1 union L_1`.

There are no other edges.  Finally put

\[
                         G_m=K_3\vee F_m.             \tag{2.1}
\]

## 3. Chromatic number and connectivity

### Proposition 3.1

For every `m>=2`,

\[
                         \chi(F_m)=4,
 \qquad                  \kappa(F_m)=4.               \tag{3.1}
\]

Consequently,

\[
                         \chi(G_m)=7,
 \qquad                  \kappa(G_m)=7.               \tag{3.2}
\]

Moreover, the seven vertices `V(K_3) union V(P)` form an actual
order-seven separator in `G_m`, with `K` and `L` on its two open sides.

### Proof

Colour both `K` and `L` with two colours and alternate two new colours on
`P`; this gives a four-colouring of `F_m`.

Suppose that `F_m` had a three-colouring.  Because each of `v_1,v_4` is
complete to `K union L`, the two bipartite graphs together must use only
two colours and `v_1,v_4` must receive the same third colour.  Since `K`
and `L` are connected and contain edges, each uses both of the first two
colours, with its bipartition sides monochromatic.  Write the colours of
`K_0,K_1` as `a,b`.  The side `L_1` has colour `a` or `b`.  In the first
case `v_3` sees both `a,b` and is forced to have the colour of its adjacent
vertex `v_4`; in the second case `v_2` sees both `a,b` and is forced to
have the colour of its adjacent vertex `v_1`.  Both cases contradict
properness.  Hence `chi(F_m)=4`.

Deleting all four vertices of `P` separates `K` from `L`, so
`kappa(F_m)<=4`.  Conversely, delete at most three vertices.  If both
`v_1,v_4` are deleted, at most one further vertex is deleted; the edge
`v_2v_3` and the surviving vertices of the two complete bipartite graphs
still join all remaining vertices.  If at least one of `v_1,v_4`
survives, it is adjacent to every surviving vertex of `K union L`.
Every surviving path vertex either is adjacent along `P` to that connected
part or has a surviving neighbour in one of its two prescribed sides;
each such pair of sides has total order at least four.  Thus the remainder
is connected, proving `kappa(F_m)>=4`.

Chromatic number is additive under joins, giving `chi(G_m)=3+4=7`.
Every vertex of the `K_3` factor is universal.  Hence a vertex cut of
`G_m` contains all three such vertices and at least four vertices of
`F_m`; conversely, the three universal vertices together with `V(P)`
disconnect `K` from `L`.  This proves (3.2) and the final assertion.
\(\square\)

## 4. The complete contracted-path colouring pattern

Contract `P` to a vertex `p`.  Then

\[
              G_m/P = K_4\vee (K\mathbin{\dot\cup}L),              \tag{4.1}
\]

where the `K_4` consists of `p` and the original `K_3`.  Fix any proper
six-colouring and call the colour of `p` zero.  The `K_4` uses four
distinct colours.  Both connected bipartite graphs use the remaining
two nonzero colours; call them `a,b`.  Each bipartition has one of the
two possible orientations, independently of the other component.

For a path vertex `v`, let

\[
 \Lambda(v)=\{0,1,\ldots,5\}\setminus
             \psi(N_{G_m}(v)-V(P))                  \tag{4.2}
\]

be its expansion list.  Always

\[
                     \Lambda(v_1)=\Lambda(v_4)=\{0\}.              \tag{4.3}
\]

If `L_1` has the colour of `K_1`, then

\[
                     \Lambda(v_2)=\{0\},\qquad
                     \Lambda(v_3)=\{0,a\};                       \tag{4.4}
\]

after possibly exchanging the names `a,b`.  If `L_1` has the colour of
`K_0`, then

\[
                     \Lambda(v_2)=\{0,b\},\qquad
                     \Lambda(v_3)=\{0\}.                          \tag{4.5}
\]

Thus (4.4) has the one-edge locked interval `v_1v_2`, while (4.5) has
the one-edge locked interval `v_3v_4`.  No proper six-colouring of the
contraction has any other pattern.

In the subgraph induced by colours `a,b`, the graphs `K` and `L` are two
distinct Kempe components.  Interchanging the colours on exactly one of
them changes (4.4) into (4.5), and conversely.  Palette permutations and
the two independent component interchanges generate every proper
six-colouring of (4.1).  Consequently:

1. every colouring in the full Kempe orbit has a shortest locked interval
   of length one;
2. orienting `P` from `v_1` to `v_4`, the first failure of the exact path
   dynamic programme is at `v_2` in (4.4) and at `v_4` in (4.5); and
3. in the orbit-extremal pattern (4.5), the endpoint `v_3` has its
   `a`- and `b`-neighbours in the two distinct components `K,L`, so no
   `a,b`-component is mixed at `v_3`.

The Kempe move which would remove that local failure returns (4.4), whose
first failure is earlier.  Hence neither the shortest locked length nor
the latest first-failure rule forces the desired endpoint coherence.

## 5. Exact scope and the surviving route

The construction deliberately exposes the correct escape: it has the
actual order-seven separator from Proposition 3.1.  It also contains a
`K_7` minor.  Indeed `K union {v_1}` contains a `K_4` minor (in one
`K_{2,2}` subgraph, use one adjacent pair as singleton branch sets, use
`v_1` as a third singleton, and use the edge on the remaining pair as the
fourth branch set), and the three
universal vertices extend it to a `K_7` model.

Thus the family does not refute a theorem whose alternatives explicitly
include an actual order-seven separation or a `K_7` model.  It proves
that the Kempe-orbit extremum cannot be the engine establishing that
theorem: a lock can migrate reversibly between different bichromatic
components without improving any well-founded shortest-lock quantity.
A positive `HC_7` argument must use the labelled near-`K_7` model and
minor-critical colourings to turn such migration directly into the
minor or separation outcome.
