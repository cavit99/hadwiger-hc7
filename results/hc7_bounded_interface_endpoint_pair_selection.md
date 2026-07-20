# Endpoint-pair selection for bounded-interface Kempe paths

**Status:** written proof;
[separately audited **GREEN**](hc7_bounded_interface_endpoint_pair_selection_audit.md).
This is a nonterminal consequence of the audited exact-block Kempe
reduction.  It does not place two failed lifts in one colouring, make their
paths disjoint, or prove the pole-free bridge composition theorem.

## 1. Setup

Let `G` be seven-connected and seven-chromatic, with no `K_7` minor, and
suppose every proper minor of `G` is six-colourable.  Use the bounded
anti-neighbourhood setup from the audited exact-block reduction: `u` is a
vertex with

\[
                 7\le d_G(u)\le9,
\]

`C` is a component of `G-N[u]`,

\[
 S=N_G(C)\subseteq N(u),\qquad
 A=G[C\cup S],\qquad B=G-C,
\]

and `7 <= |S| <= d_G(u)`.  Retain the aligned vertex `z in S` for which

\[
                         \chi(G-\{u,z\})=6.             \tag{1.1}
\]

Theorem 5.1 of
[`hc7_bounded_interface_exact_block_kempe_reduction.md`](hc7_bounded_interface_exact_block_kempe_reduction.md)
says that, for every `x in S`, an exact-singleton transition based on a
six-colouring of `G-ux` returns a bichromatic path.  Choose one such path
`P_x`, and write its boundary ends as `p_x,q_x`.  Its internal vertices
avoid `S union {u,x}` and lie wholly in one open shore.

Put

\[
                            e_x=\{p_x,q_x\}.             \tag{1.2}
\]

The choices for different `x` may arise from different colourings and
different Kempe sequences.

## 2. The endpoint-pair alternative

### Lemma 2.1 (avoidance and boundary nonadjacency)

For every `x in S`,

\[
                        e_x\subseteq S-\{x\},
        \qquad e_x\notin E(G[S]).                       \tag{2.1}
\]

### Proof

The Kempe sequence used for `x` never uses the fixed colour of `u` and
`x`.  Its obstructing bichromatic path therefore avoids `x`, including at
its ends.  This proves the first assertion.

The two ends lie in distinct components of the corresponding two-colour
subgraph of `G[S]`.  If they were adjacent in `G[S]`, that edge would put
them in the same component.  Hence they are nonadjacent.  \(\square\)

### Theorem 2.2 (disjoint pair or independent triple)

For any one choice of `P_x` for every `x in S`, at least one of the
following holds.

1. There are distinct `x,y in S` such that

   \[
                              e_x\cap e_y=\varnothing.  \tag{2.2}
   \]

2. There is an independent three-set `Q` of `G[S]` such that

   \[
                 e_x\in\binom Q2\quad(x\in S),
       \qquad e_q=Q-\{q\}\quad(q\in Q).                 \tag{2.3}
   \]

### Proof

Suppose outcome 1 fails.  The family of two-sets `(e_x:x in S)` is then
pairwise intersecting.  It contains at least two distinct members: if its
only member were `{a,b}`, the set `e_a` would contain `a`, contrary to
Lemma 2.1.

A pairwise-intersecting family of two-sets with at least two distinct
members is contained either in a star or in the three edges of a triangle.
The star alternative is impossible.  If its centre were `q`, then `e_q`
would contain `q`, again contrary to Lemma 2.1.  Thus all pairs lie in
`binom(Q,2)` for some three-set `Q`.

For `q in Q`, the only pair in `binom(Q,2)` avoiding `q` is `Q-{q}`;
hence the second equality in (2.3) holds, and all three pairs occur.
Lemma 2.1 says that each is a nonedge of `G[S]`, so `Q` is independent.
\(\square\)

When `d_G(u)=7`, the contraction-critical neighbourhood bound gives
`alpha(G[S])<=2`; hence outcome 2 is impossible.  This recovers disjoint
**terminal pairs**, but not disjoint paths.  The paths for two boundary
vertices were selected from separate colourings of separate edge-deleted
graphs.  The stronger audited degree-seven matching-bundle theorem obtains
simultaneous path disjointness from one fixed colouring; Theorem 2.2 does
not.

## 3. Two safe minor constructions

The following checks record exactly when two literal returned paths are
already terminal.  Neither condition follows from Theorem 2.2.

### Proposition 3.1 (augmented-boundary `K_6` lift)

Suppose `e_x,e_y` are disjoint and `P_x,P_y` are internally
vertex-disjoint.  If

\[
                         G[S]+e_x+e_y
\]

contains a `K_6` minor, then `G` contains a `K_7` minor.

### Proof

Replace each added edge by its corresponding path.  If an added edge is
used inside one branch set, add the path interior to that branch set.  If
it supplies an adjacency between two branch sets, divide the path at one
of its edges and add the two resulting segments to the branch sets at its
ends.  The two replacements are compatible because their ends and their
interiors are disjoint.

This gives a `K_6` model in `G[S] union P_x union P_y`.  Every branch set
retains a vertex of `S`.  The singleton `{u}` is disjoint from the model
and adjacent to every branch set, so it completes a `K_7` model.  \(\square\)

### Proposition 3.2 (two exterior paths with a reserved shore)

Let

\[
 R=\{p_1,q_1,p_2,q_2,b\}\subseteq S
\]

have five distinct vertices, and suppose `G[R]` contains every edge of
`K_5` except the two independent nonedges `p_1q_1,p_2q_2`.  Suppose there
are internally vertex-disjoint paths `P_1,P_2`, with all internal vertices
in `B-(S union {u})`, joining `p_i` to `q_i`.  If there is a vertex
`a in S-R`, then `G` contains a `K_7` minor.

### Proof

For each `i`, put the internal vertices of `P_i` in the bag containing
`p_i`, and use `{q_i}` as the other endpoint bag.  Together with the
singleton bag `{b}`, these are five disjoint connected branch sets.  The
last edge of each path supplies the corresponding missing adjacency, and
all other adjacencies are literal edges of `G[R]`.  They therefore form a
`K_5` model.

The component `C` is connected and adjacent to every vertex of `S`.
The set `{u,a}` is connected, is adjacent to all five model bags through
`u`, and is adjacent to `C` through an `a-C` edge.  The set `C` is
adjacent to every model bag through its boundary vertex.  Path interiors
lie in the opposite open shore, so these seven branch sets are disjoint.
They form a `K_7` model.  \(\square\)

## 4. The exact strict restart

### Proposition 4.1 (restart preserving the aligned vertex)

Let `D` be another component of `G-N[u]`.  If

\[
                   |V(D)|<|V(C)|,
        \qquad z\in N_G(D),                                \tag{4.1}
\]

then `D`, with boundary `S_D=N_G(D)`, is a strict same-form restart using
the same vertices `u,z` and the same rank `|D|<|C|`.

### Proof

The host graph and the pole `u` are unchanged.  Since `D` is a component
of `G-N[u]`,

\[
             S_D\subseteq N(u),\qquad
             7\le |S_D|\le d_G(u)\le9.
\]

The pair `(G[D union S_D],G-D)` is an actual separation with connected
`S_D`-full side `D` and the `S_D`-full singleton `{u}` on the other side.
The original aligned vertex remains on the literal boundary by (4.1), and
(1.1) is a property of the unchanged host.  Thus all bounded-interface
entry hypotheses, including the named `uz` response, hold with `D,S_D`
in place of `C,S`.  The component-order rank decreases strictly.  \(\square\)

If `z` is not in `N_G(D)`, proper-minor minimality still supplies colourings of
`G-ux` for vertices `x in N_G(D)`, but this does not literally preserve
the aligned pair from (1.1).  A fresh restart then requires a separately
proved vertex `z_D in N_G(D)` with `chi(G-{u,z_D})=6`; path occurrence in
`D` alone supplies no such vertex.

## 5. Residual-neighbourhood accounting and trust boundary

Let `Z` be a nonempty connected subgraph of `C`, and let `D` be a component
of `C-Z`.  Put

\[
 d(D)=|S-N_S(D)|,
 \qquad a(D)=|N_Z(D)|.
\]

There are no edges from `C` to the rest of `G` outside `S`, and distinct
components of `C-Z` are anticomplete.  Hence

\[
 N_G(D)=N_S(D)\mathbin{\dot\cup}N_Z(D),
 \qquad |N_G(D)|=|S|-d(D)+a(D).                         \tag{5.1}
\]

Seven-connectivity gives only

\[
                         a(D)\ge 7-|S|+d(D),             \tag{5.2}
\]

which is a lower bound.  It does not imply `|N_G(D)|<=9`.

Even when (5.1) happens to have order at most nine, this is not a
same-form restart at `u`: connectedness of `C` gives `a(D)>=1`, while
every vertex of `Z subseteq C` is a nonneighbour of `u`.  Thus `u` is not
complete to the new boundary, and neither the exact-block trace nor the
aligned response transfers automatically.

Theorem 2.2 therefore isolates a genuine bounded endpoint alternative,
not a terminal bridge-composition theorem.  Further progress must either
put two failures in one operation-specific colouring, prove a literal
disjoint linkage satisfying Section 3, or preserve the aligned response
through a restart of the exact form in Proposition 4.1.

## 6. Dependencies

- [boundary-aligned low-degree pair](hc7_low_degree_boundary_edge_alignment.md)
- [exact-block Kempe reduction](hc7_bounded_interface_exact_block_kempe_reduction.md),
  especially Theorem 5.1
- [degree-seven simultaneous matching bridge bundle](hc7_degree7_matching_bridge_bundle.md),
  used only to delimit the stronger degree-seven conclusion
