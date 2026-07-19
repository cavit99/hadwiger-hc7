# Two marked list exceptions do not bound total list-degree excess

**Status:** explicit unbounded counterexample to an intermediate claim;
separate internal audit GREEN in
[`hc7_two_mark_list_excess_barrier_audit.md`](hc7_two_mark_list_excess_barrier_audit.md).

This note refutes the following list-theoretic shortcut:

> A vertex-minimal uncolourable list instance which has a proper colouring
> using colours outside the lists at only two named vertices has bounded
> total list-degree excess.

The counterexample can be embedded in a literal exact-seven separation and
the resulting host can be seven-connected.  It deliberately has a `K_7`
minor and is not contraction-critical, so it does not refute a theorem using
the full hypothetical-`HC_7` host assumptions.

## Proposition 1 (unbounded-excess family)

For every `m>=2` there is a connected planar graph `K`, a list assignment
`A`, two vertices `p,q in V(K)`, and a proper colouring `psi_K` such that

1. `K` is not `A`-colourable but every proper induced subgraph is;
2. `A(v)={1,2,3}` for every vertex;
3. `psi_K(v) in A(v)` for `v notin {p,q}`, while
   `psi_K(p),psi_K(q) notin A(p)=A(q)`; and
4. the total list-degree excess is

   \[
       \sum_{v\in V(K)}(d_K(v)-|A(v)|)=2m-2.
   \]

### Proof

Let `K` be the odd wheel whose rim is the cycle `C_{2m+1}`.  Choose two
distinct rim vertices `p,q`.  With the uniform lists `A(v)={1,2,3}`, the
graph is not `A`-colourable because the odd rim needs three colours and its
universal hub then needs a fourth.  Deleting the hub leaves a
three-colourable odd cycle.  Deleting a rim vertex leaves the join of the
hub with a path, which is three-colourable.  Hence every proper induced
subgraph is `A`-colourable.

Colour `p` with colour four and `q` with colour five.  The remaining rim is
a disjoint union of paths and can be coloured with colours one and two;
colour the hub with colour three.  This is a proper colouring, and precisely
`p,q` use colours outside their lists.  The vertex carrying all positive
excess, namely the hub, is not one of the exceptions.

Every rim vertex has degree three, while the hub has degree `2m+1`.
Therefore the total excess is

\[
 (2m+1-3)+(2m+1)(3-3)=2m-2,
\]

which is unbounded.  \(\square\)

### Remark 2 (all six boundary colours do not repair the local shortcut)

There is also a version whose boundary-forbidden-list realization uses all
six colours on the boundary.  Choose adjacent rim vertices `p,q` and set

\[
 A(p)=\{1\},\qquad A(q)=\{2\},\qquad
 A(v)=\{1,2,3\}\quad(v\notin\{p,q\}).                 \tag{2.1}
\]

This is again vertex-minimal uncolourable.  Deleting an ordinary rim vertex
allows the hub to receive colour three and the remaining rim path to
alternate one and two with `p,q` in their forced colours.  After deleting
`p` (respectively `q`), colour the hub one (respectively two) and alternate
the other two colours on the rim path.  After deleting the hub, colour the
odd rim with `p=1,q=2` and use colour three once on the other `p-q` arc.

Colouring `p,q` with four and five, the hub with three, and the remaining
rim path with one and two gives exactly two list exceptions.  Its excess is

\[
 (2m+1-3)+(3-1)+(3-1)=2m+2.                          \tag{2.2}
\]

To realize (2.1), use a seven-boundary containing all six colours.  Let
ordinary wheel vertices see precisely boundary colours four, five and six;
let `p` additionally see two and three; and let `q` additionally see one
and three.  Delete the unique colour-four edge at `p` and the unique
colour-five edge at `q`.  Thus even the number `b=6` of boundary colours
does not bound the local excess from the two exceptions.  This modified
contact pattern is not asserted to retain the seven-connectivity of the
complete-join realization below.

## Literal exact-seven realization

Take a seven-vertex independent set `S` containing vertices `x,y,z`, give
them colours four, five and six, respectively, and give the other four
boundary vertices colour six.  Join every vertex of `K` to every vertex of
`S`.  Designate the crossing edges `xp` and `yq` and delete them when
extending the colouring above.  Then

\[
 A(v)=[6]\setminus
 \{\psi(s):s\in N(v)\cap S\}=\{1,2,3\}
\]

for every `v`, and the expanded colouring fails precisely on `xp,yq`.

Add one opposite vertex `ell` adjacent to all of `S` and to no vertex of
`K`.  This gives a literal decomposition

\[
 V(G)=\{\ell\}\mathbin{\dot\cup}S\mathbin{\dot\cup}V(K)
\]

with no edge between its open sides.  It is seven-connected.  Indeed,
deleting at most six vertices leaves a boundary vertex.  If a wheel vertex
also remains, the complete `S-K` join connects every remaining vertex; if
the whole wheel was deleted, which is possible only for `m=2` using all six
deletions, `ell` and `S` remain connected.

The host has a `K_7` minor: choose six vertex-disjoint edges between `S`
and `K` as six branch sets, and use the seventh vertex of `S` as a singleton
branch set.  These seven connected sets are pairwise adjacent.  The host is
also not asserted to be contraction-critical.

Thus neither exact-seven geometry nor seven-connectivity, together with
the two marked list exceptions, bounds the excess.  Any such bound in the
current programme must use `K_7`-minor exclusion or the full proper-minor
colouring dynamics.
