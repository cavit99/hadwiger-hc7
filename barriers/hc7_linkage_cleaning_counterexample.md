# A sharp obstruction to cleaning a model-transiting linkage

## 1. The proposed implication

The nonpolarized outcome of the palette-haven dichotomy gives (h)
vertex-disjoint paths from (h) private roots to a transversal in (h)
prescribed bags of a (K_r)-model.  The paths are allowed to pass through
other bags before reaching their prescribed endpoints.

It is tempting to infer, using the one spare bag when (h=r-1), either
an (h)-rooted (K_h)-model or an (h)-rooted (K_r)-model.  That
inference is false if one retains only the model and the linkage.  The
counterexample below even rules out the weaker rooted (K_h) conclusion.

## 2. The end-locked comb

Fix (h\ge 3) and put (r=h+1).  Let (L_h) have vertex set

\[
 U=\{u_1,\ldots,u_h\},\qquad
 X=\{x_1,\ldots,x_h\},\qquad
 Q=\{b_1,\ldots,b_{h-1}\},\qquad \{z\}.
\]

Its edges are exactly the following:

1. (u_ix_i) for (1\le i\le h);
2. (x_ix_{i+1}) for (1\le i<h);
3. (x_ib_i) for (1\le i<h);
4. all edges (b_ib_j) for (1\le i<j<h);
5. (zb_i) for (1\le i<h), and (zx_1).

Thus (X) is a path, (Q) is a clique, every (u_i) is a leaf at
(x_i), and (z) sees all of (Q) and the first vertex of (X).

### Proposition 2.1 (one spare bag does not clean the linkage)

The graph (L_h) has a (K_{h+1})-model

\[
 B_i=\{b_i\}\quad(1\le i<h),\qquad
 B_h=X,\qquad B_{h+1}=\{z\}.                 \tag{2.1}
\]

Moreover the (h) paths

\[
 P_i=u_ix_ib_i\quad(1\le i<h),\qquad
 P_h=u_hx_h                                      \tag{2.2}
\]

are pairwise vertex-disjoint and end in the (h) distinct prescribed
bags (B_1,\ldots,B_h).  Nevertheless (L_h) has no (K_h)-model
whose (h) branch sets contain (u_1,\ldots,u_h), respectively.
Consequently it also has no (K_{h+1})-model in which the (h) roots
lie in distinct branch sets.

#### Proof

The sets in (2.1) are connected and disjoint.  The singleton bags
(B_1,\ldots,B_{h-1}) are pairwise adjacent because (Q) is a
clique.  The edge (b_ix_i) joins (B_i) to (B_h), the edge
(zb_i) joins (B_{h+1}) to (B_i), and (zx_1) joins
(B_{h+1}) to (B_h).  Hence they form a (K_{h+1})-model.  The
paths in (2.2) plainly have disjoint vertex sets and the stated
end-bag labels.

Suppose, for a contradiction, that

\[
                         R_1,\ldots,R_h          \tag{2.3}
\]

are the branch sets of a (K_h)-model with (u_i\in R_i).  Since
(u_i) has the unique neighbour (x_i), connectedness implies either
(R_i=\{u_i\}) or (x_i\in R_i).  The first alternative would leave
(R_i) adjacent to at most one other branch set, whereas a branch set
of a (K_h)-model must be adjacent to (h-1\ge2) other branch sets.
Thus

\[
                              x_i\in R_i
                    \quad\text{for every }i.     \tag{2.4}
\]

In particular (x_{h-1}\in R_{h-1}), so it is unavailable to
(R_h).  But the only neighbours of (x_h) are (u_h) and
(x_{h-1}).  It follows from connectedness and disjointness that

\[
                              R_h=\{u_h,x_h\}.    \tag{2.5}
\]

The only edge leaving this set is (x_hx_{h-1}), so (R_h) is
adjacent to at most the single branch set (R_{h-1}), contradicting
(h\ge3).  This proves that no rooted (K_h)-model exists.

If an (h)-rooted (K_{h+1})-model existed, deleting its one
root-free branch set would leave an (h)-rooted (K_h)-model.  Hence
that stronger model is impossible as well.  \(\square\)

### Sharpness of the parameter

The obstruction begins at (h=3), equivalently (r=4).  For (h=2),
the two roots lie in one connected component and the path between them
itself gives a rooted (K_2)-model.  Thus no statement of this form can
be rescued merely by saying that (h=r-1) and retaining one spare bag.

### Corollary 2.2 (even a full (r)-path Rado transversal does not clean)

Add one new leaf (u_{h+1}) adjacent only to (z), and append the path

\[
                         P_{h+1}=u_{h+1}z
\]

to (2.2).  With (r=h+1), these are (r) pairwise vertex-disjoint
paths from (r) roots to a transversal containing one endpoint in
**every** bag of the (K_r)-model (2.1).  Nevertheless there is no
(K_r)-model rooted at all (r) roots.

Indeed, deleting from such a hypothetical rooted model the branch set
containing (u_{h+1}) would leave a (K_{r-1}=K_h)-model rooted at
(u_1,\ldots,u_h), contrary to Proposition 2.1.  Thus even the full
Rado linkage supplied by the full-palette form of the haven theorem is
not, by itself, a cleaning theorem.

## 3. A second sharp obstruction if the desired conclusion retains all bags

There is a useful variant in which every target bag is a singleton and
only the rooted (K_r) conclusion fails.  Fix (r\ge5), put
(h=r-1), let (Q=\{b_1,\ldots,b_h\}) be a clique, let
(X=x_1\cdots x_h) be a path, and add only the edges

\[
                         u_ix_i,qquad x_ib_i
                         \quad(1\le i\le h).      \tag{3.1}
\]

Then the singleton bags ({b_i}), together with the spare path bag
(X), form a (K_r)-model, and the disjoint paths (u_ix_ib_i)
reach the (h) singleton bags.  There is no (K_r)-model with all
(u_i) in distinct branch sets.

Indeed, in any such model each rooted branch set contains its (x_i).
The unique root-free branch set lies in (Q); choose (b_k) in it.
The rooted branch set containing (u_k,x_k) cannot reach any vertex of
(Q), because its only (Q)-neighbour is the already occupied (b_k),
and the adjacent path vertices belong to the other rooted branch sets.
It is therefore ({u_k,x_k}).  This set can see only the root-free
bag and the at most two rooted bags indexed by (k-1,k+1), hence at
most three other branch sets.  A bag in a (K_r)-model must see
(r-1\ge4), a contradiction.

For (r=4) this last threshold is sharp: with (h=3), the four bags

\[
 \{u_1,x_1,b_1\},\quad \{u_2,x_2\},\quad
 \{u_3,x_3,b_3\},\quad \{b_2\}
\]

do form a rooted (K_4)-model.

## 4. Exact consequence for the palette-haven programme

The counterexample does **not** refute a theorem that continues to use
the full equality of the colour and model havens.  It refutes the
strictly weaker proposed post-processing step

\[
 \text{``model + one disjoint transversal linkage''}
 \Longrightarrow
 \text{``rooted clique model''}.                \tag{4.1}
\]

Indeed, delete the endpoint (x_h) in (L_h).  The root (u_h) is
then isolated from the model core, and properness gives
(c(u_h)\ne c(x_h)).  If all (u_i) were private-colour roots, their
colours would be pairwise distinct; among the other (h-1\ge2) roots,
at most one can have colour (c(x_h)).  Hence (u_h) and at least one
root in the core both have colours absent from (c(\{x_h\})), although
they lie in different components of (L_h-x_h).  The private-colour
haven condition itself therefore fails at this one-vertex deletion,
while the model haven points toward the clique core.  Thus the
construction exposes exactly the information lost on passing from
haven equality to one linkage.

Two valid cleaning statements remain:

* If the paths have interiors disjoint from every old bag and end in
  distinct bags, adjoining each path to its end bag gives a rooted
  (K_r)-model while preserving every old interbag adjacency.
* More generally, if truncation at the first old-bag hit gives distinct
  hit bags, adjoining the disjoint model-free prefixes to those hit bags
  gives a rooted (K_r)-model (with the root-to-label assignment given
  by the first-hit permutation).

A collision/double-hit bag is not itself a split certificate: the
end-locked comb has an (h)-fold first hit in the path bag and still
has no rooted (K_h).  Any successful upgrade of the uniform theorem
must therefore reuse the haven equality (or an equivalent separator
exclusion) to reroute the collision; one spare bag alone supplies no
such cleaning mechanism.
