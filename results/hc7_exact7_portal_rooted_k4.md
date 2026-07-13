# Exact-seven portal matching and rooted-`K_4` exchange

## Status and scope

This proved and independently audited note gives a label-free structural consequence of an actual
order-seven adhesion.  Its first theorem uses only seven-connectivity.  Its
second part specializes to the audited packet vector

\[
                         (\nu_L,\nu_R)=(1,3),
\]

where `R` contains three pairwise disjoint `S`-full packets.  It proves that
Hall deficiency cannot be the obstruction to a rooted model: every
four-connected thin shore either gives a literal `K_7`, or is planar with
**all literal boundary portals on one face**.

The planar/cofacial outcome is not claimed to close the cell by itself.

## 1. A maximum literal portal matching

Let `(G_1,G_2)` be an actual separation of a `k`-connected graph `G`, with
literal boundary

\[
                         S=V(G_1)\cap V(G_2),\qquad |S|=k,
\]

and both open shores nonempty.  If `C` is a component of `G_1-S`, form the
bipartite portal graph with parts `S,V(C)`, joining `s` to `x` exactly when
`sx` is an edge of `G`.

### Theorem 1.1 (portal matching saturates the smaller side)

The portal graph has a matching of order

\[
                              \min\{k,|C|\}.             \tag{1.1}
\]

#### Proof

Let `m` be its maximum matching order and suppose

\[
                            m<\min\{k,|C|\}.              \tag{1.2}
\]

The deficiency form of Hall's theorem gives a set `A\subseteq S` such
that

\[
                   m=k-|A|+|N_C(A)|.                    \tag{1.3}
\]

Put

\[
                         X=(S-A)\cup N_C(A).              \tag{1.4}
\]

Then `|X|=m<k`.  Also `C-N_C(A)` is nonempty.  Indeed, if
`V(C)=N_C(A)`, then (1.3) gives

\[
                         m=k-|A|+|C|\ge |C|,
\]

contrary to (1.2).

No vertex of `C-N_C(A)` has a neighbour in `A`, by the definition of
`N_C(A)`.  Its possible neighbours outside `C` lie in `S`, because `C` is
a component of an open shore.  After deleting `X`, all such neighbours in
`S-A` and all internal exits through `N_C(A)` are gone.  The nonempty
opposite open shore remains outside `X`.  Hence `X` separates the nonempty
set `C-N_C(A)` from that opposite shore, contradicting `k`-connectivity.
This proves (1.1). \(\square\)

For `k=7`, every component of order at least seven therefore has seven
distinct literal first-hit portals, one for each member of `S`; a component
of order at most six has distinct portals for all of its own vertices.

## 2. Four rooted portal bags lift literally

Assume now the exact-seven `(1,3)` packet setting.  Let
`P_1,P_2,P_3\subseteq R` be three disjoint `S`-full packets.

### Lemma 2.1 (rooted four-portal lift)

Let `T={t_1,t_2,t_3,t_4}\subseteq S`.  Choose distinct

\[
                         x_i\in N_L(t_i)\quad(1\le i\le4).
\]

If `L` has a `K_4` model with disjoint branch bags `B_i` rooted at the
`x_i`, then `G` has a literal `K_7` model.

#### Proof

Write `S-T={r_1,r_2,r_3}`.  The seven bags are

\[
 B_i\cup\{t_i\}\quad(1\le i\le4),
 \qquad P_j\cup\{r_j\}\quad(1\le j\le3).              \tag{2.1}
\]

They are pairwise disjoint and connected.  The first four are pairwise
adjacent because the `B_i` form a `K_4` model.  The last three are pairwise
adjacent because every `P_j` contacts the other packets' literal anchors.
Finally every last bag is adjacent to every first bag because `P_j` is
full at the literal vertex `t_i` contained in that first bag.  Thus (2.1)
is a literal seven-bag clique model. \(\square\)

No colour class or old near-clique row is identified with a branch bag in
this argument.

## 3. The four-connected thin shore is one coherent rural page

For `s\in S`, put

\[
                              Z_s=N_L(s).
\]

Regard the family `(Z_s:s\in S)` as a transversal matroid on the set of
literal portal vertices `\bigcup_s Z_s`: a set is independent when its
vertices can be assigned injectively to distinct labels `s` which contact
them.

### Theorem 3.1 (four-connected portal dichotomy)

In the exact-seven `(1,3)` setting, suppose the thin open shore `L` is
four-connected.  Then either

1. `G` contains a `K_7` minor; or
2. `L` is planar and one face of its unique plane embedding contains every
   literal portal vertex in `N_L(S)`.

#### Proof

A four-connected graph has at least five vertices.  Theorem 1.1 therefore
gives the portal transversal matroid rank at least four.  Truncate it to
rank four.  Every basis `B={x_1,x_2,x_3,x_4}` is represented by four
distinct labels `t_i` with `x_i\in Z_{t_i}`.

If `L` has a `K_4` model rooted at one such basis, Lemma 2.1 gives outcome
1.  Assume this never happens.  The rooted-`K_4` theorem for four-connected
graphs then says, for every basis `B`, that `L` is planar and the four
vertices of `B` lie on one face.

Fix the unique plane embedding of the three-connected planar graph `L`.
The basis-exchange graph of a matroid is connected.  Consecutive rank-four
bases share three vertices.  Two distinct faces of a three-connected plane
graph share at most two vertices, so the cofacial bases along any exchange
path all lie on one fixed face `F`.

Every portal vertex is a nonloop of the transversal matroid.  Since its
rank is at least four, every nonloop extends to a rank-four basis.  Hence
every vertex of `N_L(S)` occurs in one of the bases already put on `F`.
Thus all literal portals lie on the single face `F`, proving outcome 2.
\(\square\)

### Corollary 3.2 (the live thin-shore obstruction has connectivity at most three or is cofacial)

In a `K_7`-minor-free exact-seven `(1,3)` cell, a four-connected thin shore
is one planar society whose entire seven-label portal system is supported
on one facial cycle.  Therefore a noncofacial surviving thin shore has an
ordinary separator of order at most three.  Together with the audited
near-full exchange, every 2-cut in such a survivor has exactly two lobes.

The corollary deliberately does not infer a bounded portal transversal or
a global apex set from cofaciality.  Closing that single rural page requires
either a labelled crossing-to-rooted-`K_4` argument or an exact proper-minor
state matching the three-packet shore.

## Dependencies

1. Hall's theorem in deficiency form.
2. Fabila-Monroy--Wood: four nominated vertices in a four-connected graph
   root a `K_4` minor unless the graph is planar and the four roots are
   cofacial.
3. The audited exact-seven packet setting and the literal existence of
   three disjoint `S`-full packets in `R`.
