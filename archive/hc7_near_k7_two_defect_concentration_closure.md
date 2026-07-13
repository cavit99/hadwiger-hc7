# The concentrated two-defect cell closes by a rooted `K_4`

## Status

This note completes the portal-concentration branch left by
`hc7_near_k7_two_defect_cut_closure.md`.

In a seven-connected graph, the concentrated `d=2` singleton/bipartite
shell gives either a literal `K_7` model or one fixed pair whose deletion
is planar.  The proof uses the rooted-`K_4` theorem in a four-connected
remainder.  No rurality assumption on the complex bag is needed.

Together with the disconnected-bag closure, this discharges every `d=2`
outcome of the audited palette-to-label theorem.

## 1. Exact concentrated atom

Use the notation of `hc7_near_k7_two_defect_cut_closure.md`:

\[
 S=\{b_s,b_t,q_1,q_2,q_3\},\quad
 X=\{x_s,x_t\},\quad O=\{q_1,q_2,q_3\}.                 \tag{1.1}
\]

The rows are

\[
\begin{array}{c|c|c|c}
 &v&\text{missed singleton}&\text{seen singleton rows}\cr\hline
x_s&\checkmark&b_s&b_t,q_1,q_2,q_3\cr
x_t&\checkmark&b_t&b_s,q_1,q_2,q_3,
\end{array}                                               \tag{1.2}
\]

while `v` misses `b_s,b_t` and sees all of `O`.  Assume `B-X` is
connected and that some portal class is contained in `X`.

The elementary gate count in Theorem 1.1 of
`hc7_near_k7_two_defect_concentration_rural.md` gives the following exact
facts in every seven-connected target-free host.

* There is a unique `q in O` with `P_q=X`.
* Writing `O-{q}={h_1,h_2}` and `R=B-X`,

  \[
                  N_G(R)=X\cup\{v\}\cup(S-\{q\}).       \tag{1.3}
  \]

* The five vertices

  \[
                         Z=(b_s,b_t,x_s,v,x_t)            \tag{1.4}
  \]

  induce a cycle in the displayed cyclic order.
* Each of `q,h_1,h_2` is complete to `V(Z)`, the three vertices form a
  triangle, and `q` is anticomplete to `R`.

For completeness, uniqueness in the first item follows because `N(R)` is
contained in the two witnesses, the apex, and the nonconcentrated
singleton rows.  Two concentrated ordinary rows would give a cut of order
at most six.  A deficient row cannot be concentrated: it would give
`b_s` or `b_t` degree five.

## 2. Rooted quadruples close or become cofacial

### Theorem 2.1 (concentrated-cell closure)

Let `G` be seven-connected and satisfy the exact atom in Section 1.  Then
at least one of the following holds:

1. `G` contains a `K_7` minor;
2. the fixed pair `{h_1,h_2}` is an apex pair:

   \[
                         G-\{h_1,h_2\}\text{ is planar}.  \tag{2.1}
   \]

#### Proof

Delete the triangle vertices `q,h_1,h_2` and put

\[
                         W=G-\{q,h_1,h_2\}.              \tag{2.2}
\]

The graph `W` is four-connected: a separator of order at most three,
together with the three deleted vertices, would disconnect `G` with at
most six vertices.

Choose any four distinct vertices `z_1,z_2,z_3,z_4` of the literal cycle
`Z`.  The rooted-`K_4` theorem for four-connected graphs gives one of two
outcomes.

If `W` has a `K_4` model with branch bags `D_i` rooted at `z_i`, then

\[
           D_1,D_2,D_3,D_4,\quad \{q\},\quad
           \{h_1\},\quad\{h_2\}                          \tag{2.3}
\]

are seven pairwise adjacent connected bags.  Indeed each of
`q,h_1,h_2` is adjacent to every root `z_i`, hence to every rooted bag;
the three singleton bags form a triangle; and the first four bags form a
clique model.  Thus (2.3) is a literal `K_7` model.

Assume the first outcome never occurs.  The rooted theorem then says that
`W` is planar and every four-subset of `V(Z)` lies on one face in its
plane embedding.  Since `W` is four-connected, its embedding is unique up
to reflection.  Fix three cycle vertices `z_1,z_2,z_3`.  The face
containing `z_1,z_2,z_3,z_4` and the face containing
`z_1,z_2,z_3,z_5` are the same: two distinct faces of a three-connected
plane graph share at most two vertices.  Hence all five vertices of `Z`
lie on one face `F` of `W`.

After `h_1,h_2` are deleted, the complete neighbourhood of `q` is exactly
`V(Z)`: equation (1.3) makes `q` anticomplete to `R`, and the other two
triangle neighbours have been deleted.  Place `q` inside `F` and join it
to the five boundary vertices.  This extends the plane drawing of `W` to
a plane drawing of `G-{h_1,h_2}`.  Thus (2.1) holds.  \(\square\)

The two apex vertices are selected once by the unique concentrated label;
they are not chosen independently by local pieces.  This is therefore a
coherent P5-compatible output.

## 3. Consequence for P4

### Corollary 3.1 (the entire `d=2` shell is discharged)

Let `G` be seven-connected and `K_7`-minor-free in the audited spanning
singleton/bipartite shell, and suppose the apex has exactly two
nonneighbours in the singleton clique.  Then

\[
                         G-\{h_1,h_2\}\text{ is planar}    \tag{3.1}
\]

for one fixed pair of contact singleton vertices.

#### Proof

The audited palette-to-label theorem gives a same-parity witness pair
`X`.  If `B-X` is disconnected,
`hc7_near_k7_two_defect_cut_closure.md` gives `K_7`, contrary to the
hypothesis.  Therefore `B-X` is connected, and the only other outcome of
that theorem is concentration of one portal class on `X`.  Theorem 2.1
gives `K_7` or (3.1); the former is again excluded.  \(\square\)

In a 7-contraction-critical graph, (3.1) is impossible: four-colour the
planar remainder and give `h_1,h_2` two fresh colours.  Thus the `d=2`
singleton/bipartite cell cannot occur in a minimal `HC_7` counterexample.
