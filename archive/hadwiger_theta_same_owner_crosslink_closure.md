# The two theta crossbars cannot have one owner

## 1. Statement

Retain the exact theta setting of
`hadwiger_theta_crossbar_nonowner_descent.md`.  Thus `S={0,...,6}` is a
full seven-adhesion and

\[
 E(\overline{G[S]})=\{01,02,05,12,15,24,45\}.       \tag{1.1}
\]

The two complete-quotient crossbars are

\[
  R_A=05\mid12\mid3\mid4\mid6,
  \qquad
  R_B=15\mid02\mid3\mid4\mid6.                    \tag{1.2}
\]

Each has a unique shore owner by exact-state packet transfer.

### Theorem 1.1 (same-owner crosslink closure)

If one full shore owns both crossbars in (1.2), then `G` contains a
`K_7` minor.

Consequently the crossbars have opposite owners in every `K_7`-minor-free
theta cell.

## 2. The rooted-cycle cross lemma

We use the following standard result of Fabila-Monroy and Wood, *Rooted
K4-Minors*, Lemma 7.

### Lemma 2.1 (cycle plus an opposite linkage)

Let a cycle contain distinct vertices `a,b,c,d` in this cyclic order.  If
the graph contains vertex-disjoint paths joining `a` to `c` and `b` to
`d`, then it has a `K_4` minor rooted at `a,b,c,d`.

The paths in the linkage need not avoid the cycle internally.  This is
the important strength of the lemma: intersections between two packet
systems do not create a residue.  The result is proved in the cited paper
by taking a vertex/edge-minimal counterexample and contracting a
reducible edge.

## 3. Proof of the same-owner theorem

Let `C` own both crossbars and let `D` be the opposite full shore.

From the `R_A` packet choose internally shore-contained, vertex-disjoint
paths

\[
                         P_{05},\qquad P_{12}.       \tag{3.1}
\]

Here `P_{ij}` includes the two boundary endpoints `i,j`; its internal
vertices lie in the corresponding connected carrier in `C`.  Such paths
exist by taking a shortest path inside each carrier after adding its two
portal edges.  Carrier disjointness makes the two paths internally and
mutually disjoint.

The theta boundary contains the path `0-4-1` and the edge `5-2`.
Therefore

\[
       P_{05}\cup 52\cup P_{21}\cup 14\cup40        \tag{3.2}
\]

is a cycle through the four active roots in cyclic order

\[
                              0,5,2,1.              \tag{3.3}
\]

All internal vertices of the two carrier paths lie in `C`, while the
only additional internal vertex in (3.2) is the boundary vertex `4`, so
no hidden overlap occurs.

The `R_B` packet supplies vertex-disjoint paths

\[
                         P_{15},\qquad P_{02}.       \tag{3.4}
\]

They may intersect the cycle (3.2), and may intersect the first packet
paths; only their mutual disjointness is asserted or needed.  Relative to
the order (3.3), they join the two opposite pairs

\[
                         (1,5),\qquad(0,2).          \tag{3.5}
\]

Apply Lemma 2.1 with

\[
                         (a,b,c,d)=(0,5,2,1).        \tag{3.6}
\]

It gives four pairwise disjoint, pairwise adjacent connected branch bags

\[
                         B_0,B_5,B_2,B_1            \tag{3.7}
\]

inside \(G[C\cup\{0,1,2,4,5\}]\), with each `B_i` containing its named
boundary root.

Now add the three branch bags

\[
                         D,\qquad\{3\},\qquad\{6\}. \tag{3.8}
\]

They are disjoint from (3.7).  Fullness makes `D` adjacent to each
`B_i`, through the root `i`, and adjacent to both singleton bags.
Boundary labels `3,6` are adjacent to one another and to every one of
`0,1,2,5`, so each singleton is adjacent to all four rooted bags.
Consequently (3.7)--(3.8) are seven pairwise adjacent connected branch
sets, a `K_7` model.  This proves Theorem 1.1.  QED.

## 4. Consequence with the nonowner descent theorem

### Corollary 4.1 (both theta shores descend)

In a `K_7`-minor-free theta cell the two crossbars have opposite owners.
Thus each full shore is the nonowner of one crossbar, and Theorem 5.1 of
`hadwiger_theta_crossbar_nonowner_descent.md` gives a proper fragment
behind a nested exact seven-cut inside **each** shore.

### Corollary 4.2 (theta is absent at a minimum fragment)

No theta adhesion can have a shore which is globally minimum among all
fragments behind exact seven-cuts.  Such a shore is a nonowner for one of
the two oppositely owned crossbars, and Corollary 4.1 produces a strictly
smaller fragment.

This closes the theta equality type only in an argument which first
chooses a globally minimum exact-seven fragment, applies the equality-gate
funnel to that same fragment, and obtains the theta boundary there.  It
does not assert that an arbitrary nested cut again has theta boundary;
the descent theorem's nonedge-transport warning remains in force.

## 5. Why the operation state is still essential

The branch-set construction after ownership is static, but ownership is
not.  A connected shore can contain neither, one, or both crossbar
packets under the coarse portal hypotheses.  Exact five-block packet
transfer and crossed-state gluing are what prove that every crossbar has a
unique owner.  Once those two oriented bits exist, Lemma 2.1 converts the
same-owner assignment to the rooted model, while the opposite-owner
assignment activates strict descent on both shores.
