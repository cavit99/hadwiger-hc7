# Near-full path pieces must miss the boundary triangle

**Status:** written proof; separate internal audit GREEN in
[`hc7_distance_one_reversal_triangle_collision_audit.md`](hc7_distance_one_reversal_triangle_collision_audit.md).

This note closes every two-piece outcome of the
[shore-spanning distance-one normal form](hc7_distance_one_spanning_path_normal_form.md)
whose possible omitted contacts avoid the distinguished boundary triangle.
It confines both the strict-reversal and shared-portal residues to literal
triangle contacts.  The proof is an explicit `K_7`-minor model and is
independent of the length of the obstruction path.

## 1. Near-full two-piece completion

### Theorem 1.1

Suppose

\[
 V(G)=E\mathbin{\dot\cup}B\mathbin{\dot\cup}C,
 \qquad
 B=(S-\{e\})\mathbin{\dot\cup}W,
 \qquad |B|=9,
\]

where

\[
 S=\{d,e,x_d,y_d,x_e,y_e,x_0,y_0\},
 \qquad d x_d y_d d
\]

is a triangle.  Let `C=Q_0 dotcup Q_1`, where the two parts are connected
and adjacent, one is full to `B`, and the other is full to `S-{e}`.

Let `E_0,E_1` be disjoint nonempty connected subgraphs of `G[E]` with an
edge between them.  For `i=0,1`, suppose

\[
 D_i=B-N_G(E_i),
 \qquad |D_i|\le1,
 \qquad D_i\cap\{d,x_d,y_d\}=\varnothing.            \tag{1.1}
\]

Then `G` contains a `K_7` minor.

#### Proof

Put

\[
                       A=\{x_e,y_e,x_0,y_0\}.
\]

Choose distinct `r_0,r_1 in A` with `r_i notin D_i`.  Such a choice always
exists: each of the two choices forbids at most one member of the four-set
`A`.  Let `q_0,q_1` be the two remaining members of `A`, in either order.

Consider

\[
 E_0\cup\{r_0\},\qquad
 E_1\cup\{r_1\},\qquad
 Q_0\cup\{q_0\},\qquad
 Q_1\cup\{q_1\}.                                  \tag{1.2}
\]

These sets are pairwise disjoint.  The first two are connected by (1.1)
and the choice of their anchors; the last two are connected because all
four vertices of `A` lie in `S-{e}`, to which both `Q`-parts are full.  The
first two sets are adjacent by hypothesis, and the last two are adjacent
by the connected partition of `C`.

Every `E`-side set in (1.2) is adjacent to every `Q`-side set: each `Q_j`
has a neighbour at both `r_0` and `r_1`, which belong to the two `E`-side
branch sets.  Thus the four sets in (1.2) are pairwise adjacent.

By (1.1), both `E`-side sets are adjacent to all three vertices
`d,x_d,y_d`.  Both `Q`-parts are also adjacent to all three because the
triangle lies in `S-{e}`.  Finally its three vertices are pairwise
adjacent.  Hence the four sets in (1.2), together with

\[
                         \{d\},\quad\{x_d\},\quad\{y_d\},
\]

are seven pairwise disjoint, pairwise adjacent connected branch sets.
They form an explicit `K_7`-minor model. \(\square\)

## 2. Consequences for the path normal form

Retain the notation

\[
                    F_* = \max_{s\in B} f(s),
       \qquad      L_* = \min_{s\in B} \ell(s)
\]

of the shore-spanning path normal form, and put

\[
                         T=\{d,x_d,y_d\}.
\]

Assume throughout this section that the order-seven or order-eight
full-neighbourhood response of Lemma 2.1 in that normal form has not
occurred.  Hence every nonempty proper prefix and suffix of the path meets
at least eight of the nine vertices of `B`.

### Corollary 2.1 (strict reversal)

If `F_*>L_*`, choose `a,b` with `f(a)=F_*` and `ell(b)=L_*` as in the
normal form.  In a `K_7`-minor-free graph,

\[
                         \{a,b\}\cap T\ne\varnothing.            \tag{2.1}
\]

#### Proof

For every `L_*<=i<F_*`, the two path parts are adjacent and have exact
missing sets `{a}` and `{b}`.  If both omissions avoided `T`, Theorem 1.1
would give a `K_7` minor. \(\square\)

### Corollary 2.2 (shared portal)

Suppose `F_*=L_*=k`, and choose `a,b` with `f(a)=k=ell(b)`.  In a
`K_7`-minor-free graph:

1. if `k>1`, then `a in T`;
2. if `k<r`, then `b in T`.

Thus every internal shared-portal outcome (`1<k<r`) has selected first- and
last-contact witnesses in the boundary triangle.  Only an endpoint portal,
and in particular the atomic case `r=1`, can avoid one or both conclusions.

#### Proof

If `k>1`, cut the path immediately before `p_k`.  The prefix misses `a`
and, by the prefix-contact theorem, no other boundary vertex.  The suffix
is full to `B`, since `ell(s)>=L_*=k` for every `s in B`.  Theorem 1.1
therefore gives a `K_7` minor unless `a in T`.

If `k<r`, cut immediately after `p_k`.  Now the prefix is full to `B`,
since `f(s)<=F_*=k` for every boundary vertex, while the suffix misses
exactly `b`.  Theorem 1.1 gives a `K_7` minor unless `b in T`. \(\square\)

## 3. Exact remaining issue

The shore-spanning distance-one residue is now confined to triangle-owned
contact defects:

- a strict reversal in which at least one omitted vertex lies in `T`;
- an internal shared portal whose selected extremal witnesses both lie in
  `T`; or
- a shared portal at an end of the path, including the atomic one-vertex
  shore.

The theorem does not turn a missing triangle contact into a compatible
order-seven or order-eight response.  That remaining step must either use
the second obstruction path through the opposite shore or split one of the
four anchored branch sets without losing its prescribed label.
