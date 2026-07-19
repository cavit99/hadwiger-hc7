# A labelled portal linkage splits a donor branch set among all of its owners

**Status:** written proof; separate internal audit GREEN in
[`hc7_multi_owner_portal_linkage_transfer_audit.md`](hc7_multi_owner_portal_linkage_transfer_audit.md).
This theorem
extends the label-preserving two-contact transfer from zero or one owner to
an arbitrary owner set whenever the owner portals can be linked disjointly
to distinct attachment vertices of the retained donor.  Failure has an
exact Rado--Menger certificate inside the transferred piece.  It does not
turn that internal certificate into a colour-compatible host separation and
does not prove `HC_7`.

## 1. Setting

Use the spanning labelled `K_7`-minus-one-edge model and fixed response data
of
[`hc7_first_hit_rank_preserving_branch_set_transfer.md`](../results/hc7_first_hit_rank_preserving_branch_set_transfer.md):

\[
                 X,\ Y,\ D,\ U,\ F_1,\ F_2,\ F_3.     \tag{1.1}
\]

The only possible missing adjacency is `X-Y`.  The connected branch set
`D` contains the fixed connected response subgraph `Z`.  There are edges

\[
                         c_1u_1,\ c_2u_2,              \tag{1.2}
\]

where `c_1,c_2 in Z`, and

\[
 U=W\mathbin{\dot\cup}U',\qquad
 u_1\in U',\quad u_2\in W,                             \tag{1.3}
\]

with `W,U'` nonempty and connected and the prescribed root of `U` in `U'`.

Write the owner set as

\[
 \Omega(W)=\{R_1,\ldots,R_k\}
 \subseteq\{X,Y,F_1,F_2,F_3\}.                         \tag{1.4}
\]

Assume `k>=1`; the owner-free transfer is already covered by the cited
theorem.

For every owner and for the retained donor define the literal portal sets
inside `W` by

\[
 A_i=N_G(R_i)\cap W,\qquad
 B=N_G(U')\cap W.                                      \tag{1.5}
\]

Every `A_i` is nonempty: the old model has an `R_i-U` edge, while the
definition of an owner makes `R_i` anticomplete to `U'`.  The set `B` is
nonempty because `G[U]` is connected and both sides of (1.3) are nonempty.

Retain the relaxed first-hit rank `lambda` of the cited theorem.  Its paths
have distinct designated ports on `Z`, may overlap inside `Z`, and are
pairwise vertex-disjoint outside `Z`.

## 2. Portal-linkage transfer

### Theorem 2.1

Suppose `G[W]` contains pairwise vertex-disjoint paths

\[
                         P_1,\ldots,P_k               \tag{2.1}
\]

such that `P_i` has one end in `A_i` and its other end in `B`.  Trivial
one-vertex paths are allowed when `A_i cap B` is nonempty.  Then either

1. the displayed sets give an explicit `K_7`-minor model in `G`; or
2. there is another spanning labelled `K_7`-minus-one-edge model with the
   same possible missing pair, prescribed roots, selected boundary
   partition and response subgraph `Z`, in which `U` is replaced by the
   proper connected subset `U'`.

In outcome 2 the relaxed first-hit rank does not decrease.

#### Proof

Let `K_i=V(P_i)`.  The sets `K_i` are nonempty, connected and pairwise
disjoint.  Every component of

\[
                         G[W-\bigcup_iK_i]             \tag{2.2}
\]

has an edge to at least one `K_i`, because `G[W]` is connected.  Assign
each such component to one adjacent `K_i`, arbitrarily when there is a
choice, and let `L_i` be `K_i` together with all components assigned to it.
Then

\[
 W=L_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}L_k, \tag{2.3}
\]

every `L_i` is connected, and every `L_i` has an edge both to `R_i` and to
`U'`.

Replace the old owner and donor branch sets by

\[
                         R_i'=R_i\cup L_i\quad(1\le i\le k),
              \qquad    U'=U-W.                       \tag{2.4}
\]

Every `R_i'` is connected through its `A_i` portal, and `U'` is connected
by hypothesis.  The sets remain pairwise disjoint and, by (2.3), still
partition the whole host together with the unchanged branch sets.

For every owner, the `B` end of `P_i` gives an edge from `R_i'` to `U'`.
For every branch set `R` which is not an owner, the definition of
`Omega(W)` gives an old edge from `R` to `U'`.  The edge `c_1u_1` preserves
the `D-U'` adjacency.  Enlarging an owner cannot destroy any of its other
old adjacencies, and every pair of unchanged branch sets retains its old
adjacency.  Hence the only pair which can still be nonadjacent is `X,Y`.
If that pair has become adjacent, the seven sets form a `K_7`-minor model;
otherwise they are the compatible spanning labelled model in outcome 2.
All prescribed owner roots remain in their old sets, and the prescribed
root of `U` remains in `U'`.

It remains to check the rank.  Every old first-hit path with terminal label
different from `U` avoided all of old `U`, and hence avoids every `L_i`.
It remains valid when an owner is enlarged.  An old `U`-path ending in
`U'` also remains valid.  If it ended in `W`, retain its designated port
`p`, take any `p-c_1` path inside connected `Z`, and append `c_1u_1`.
This replacement may overlap other paths inside `Z`, while outside `Z` it
contains only the new terminal `u_1`.  Thus it preserves disjointness,
literal first-hit ownership and every designated port.  A maximum old
family therefore gives a new family of the same order, proving rank
nondecrease. \(\square\)

### Corollary 2.2 (extremal obstruction)

Fix the host, labels, roots, boundary partition, `Z`, and permitted ports.
Among all compatible models, first maximize `lambda` and then minimize
`|U|`.  If the host has no `K_7` minor, the labelled portal linkage (2.1)
does not exist for the full owner set of any admissible split (1.3).

#### Proof

The first outcome of Theorem 2.1 is excluded.  Its second outcome has rank
at least the chosen maximum and hence equal to it, but replaces `U` by its
proper subset `U'`, contradicting the secondary minimum. \(\square\)

## 3. Exact local failure certificate

For `I subseteq [k]`, let `r_B(A_I)` be the maximum number of pairwise
vertex-disjoint paths in `G[W]` from distinct vertices of `B` to distinct
vertices of

\[
                         A_I=\bigcup_{i\in I}A_i.       \tag{3.1}
\]

Zero-edge paths are allowed when a vertex belongs to both endpoint sets.

### Theorem 3.1 (Rado--Menger owner certificate)

The labelled portal linkage (2.1) exists if and only if

\[
                         r_B(A_I)\ge |I|               \tag{3.2}
\]

for every `I subseteq[k]`.  Consequently, in the extremal situation of
Corollary 2.2 there is an inclusion-minimal deficient owner set `I`, with
`|I|>=2`, and a vertex set `K` in `G[W]` such that

\[
                 |K|=r_B(A_I)=|I|-1\le4,              \tag{3.3}
\]

and `K` meets every path in `G[W]` from `B` to `A_I`.  Every proper
subfamily of `I` has its full labelled portal linkage.

#### Proof

The subsets of `V(W)` which can be linked by pairwise vertex-disjoint paths
to distinct vertices of `B` are the independent sets of a strict gammoid.
Apply Rado's independent-transversal theorem to the (not necessarily
disjoint) subsets `A_1,...,A_k` of its ground set.  Its rank on `A_I` is
exactly `r_B(A_I)`, so the independent transversal is precisely (2.1), and
Rado's criterion is (3.2).

If the linkage is absent, choose `I` inclusion-minimal subject to violating
(3.2).  A singleton cannot be deficient: `G[W]` is connected and each
`A_i,B` is nonempty.  Thus `|I|>=2`.  For every `i in I`, minimality gives

\[
 r_B(A_{I-\{i\}})\ge |I|-1.
\]

Monotonicity and deficiency now force `r_B(A_I)=|I|-1`.  The same
minimality verifies all Rado inequalities for every proper subfamily, so
each has its full labelled portal linkage.  Finally, vertex Menger, with
the usual vertex-splitting convention and with endpoints permitted in the
separator, gives a set `K` of order `r_B(A_I)` meeting every `B-A_I` path.
Since `k<=5`, this proves (3.3). \(\square\)

### Corollary 3.2 (the two-owner bottleneck)

If `k=2` and the model is extremal as in Corollary 2.2, there is a
literal vertex `s in W` which meets every path in `G[W]` from `B` to
`A_1 union A_2`.

#### Proof

Connectedness of `G[W]` and nonemptiness of `A_i,B` give
`r_B(A_i)>=1` for each singleton owner set.  Thus the deficient set in
Theorem 3.1 must be `{1,2}`.  Its rank is at least one and at most one, so
the Menger set has order exactly one. \(\square\)

## 4. The two-owner host fork

The internal one-vertex obstruction in Corollary 3.2 has a useful
host-level consequence once the ambient graph is seven-connected.

### Theorem 4.1 (concentrated portals, exact boundary, or repeated contact)

Assume `G` is seven-connected and `k=2`, and let `s` be the vertex supplied
by Corollary 3.2.  Then at least one of the following holds.

1. Both owner portal sets are concentrated at `s`:
   \[
                            A_1=A_2=\{s\}.             \tag{4.1}
   \]
   In particular, an edge from `s` to `R_1` and an edge from `s` to `R_2`
   form an incident pair of owner-contact edges with different branch-set
   labels.
2. There is a nonempty connected set `C subseteq W-s` such that
   \[
              E_G(C,U')=\varnothing,\qquad N_{G[W]}(C)=\{s\}.             \tag{4.2}
   \]
   Moreover, either:

   a. `N_G(C)` has order seven and consists of `s` and one literal vertex
      from each of the six other branch sets in (1.1); or
   b. one of those six branch sets contains two distinct neighbours of
      `C`.  Two edges from `C` to those distinct neighbours are
      model-preserving as a pair: deleting either one leaves the other edge
      realizing the same branch-set adjacency.

#### Proof

The vertex `s` meets every path in `G[W]` from `B` to `A_1 union A_2`.
If `A_1 union A_2 subseteq {s}`, nonemptiness of both owner portal sets
gives (4.1).

Otherwise choose a component `C` of `G[W-s]` which contains a vertex of
`(A_1 union A_2)-{s}`.  It contains no vertex of `B`: if it contained
`b in B`, a path inside connected `C` from `b` to the chosen owner portal
would be a `B`--`(A_1 union A_2)` path avoiding `s`.  By the definition of
`B`, this proves `E_G(C,U')` is empty.  Because `G[W]` is connected and
`C` is a component after deleting `s`, its full neighbourhood inside `W`
is exactly `{s}`.  This proves (4.2).

The seven branch sets in (1.1) span the host.  Consequently every neighbour
of `C` other than `s` lies in one of the six branch sets different from
`U`.  The set `N_G(C)` separates the nonempty set `C` from the nonempty
set `U'`, so seven-connectivity gives

\[
                              |N_G(C)|\ge7.             \tag{4.3}
\]

If each of the six outside branch sets contributes at most one vertex to
`N_G(C)`, then `|N_G(C)|<=7`.  Equality holds in (4.3), and each outside
branch set contributes exactly one vertex.  This is outcome 2a.

Otherwise some outside branch set `R` contains distinct vertices `x,y` of
`N_G(C)`.  Choose edges `c_xx` and `c_yy` with `c_x,c_y in C`.  Deleting
either edge preserves the connected branch sets and leaves the other edge
between `U` and `R`; hence the displayed pair is model-preserving in the
stated sense.  This is outcome 2b. \(\square\)

### Corollary 4.2 (critical-host interpretation)

If, in addition, `G` is not six-colourable and every edge-deleted proper
subgraph of `G` is six-colourable, the edge pairs in outcomes 1 and 2b are
deletion-critical.
Only the pair in outcome 2b is automatically model-preserving edge by
edge.  In outcome 2a, any edge from `s` into `C` lies across an actual
order-seven separation and may be used with the proper-minor colouring
response at that literal boundary.

This corollary does not say that the boundary partition returned after
deleting such an edge extends through the intact `C`-side.  Nor does it
place the repeated pair from outcome 2b in a preselected open shore.

### Theorem 4.3 (a general owner circuit has a bounded host outcome)

Assume `G` is seven-connected.  Let `I` and `K` be an inclusion-minimal
deficient owner family and its transversal from Theorem 3.1.  Then at least
one of the following holds.

1. Every portal belonging to the owners in `I` lies in `K`:
   \[
                              A_I\subseteq K,           \tag{4.4}
   \]
   where `|K|=|I|-1<=4`.  In this case one vertex of `K` is a portal for
   two different owners, and hence supports an incident pair of
   differently labelled owner-contact edges.
2. There is a nonempty connected set `C subseteq W-K`, anticomplete to
   `U'`, whose full host neighbourhood is an actual separator of order
   between seven and `|I|+5<=10`.  Its vertices in `U` lie in `K`, and it
   has at most one neighbour in each of the six other branch sets.
3. There are two distinct edges from `C` to distinct vertices of one
   outside branch set, for some nonempty connected `C subseteq W-K`
   anticomplete to `U'`.  Deleting either edge leaves the other realizing
   the same branch-set adjacency.

#### Proof

If (4.4) holds, choose one vertex from each nonempty `A_i`.  There are
`|I|` chosen occurrences in a set of order `|I|-1`, so two owners have the
same chosen portal.  Edges from that vertex to the two distinct owner
branch sets give the asserted incident pair.

Suppose now that (4.4) fails.  Choose a component `C` of `G[W-K]` containing a
vertex of `A_I-K`.  The set `C` contains no vertex of `B`: otherwise a
path inside `C` would join `B` to `A_I` without meeting `K`.  Hence `C` is
anticomplete to `U'`.  Since `C` is a component of `G[W-K]`,

\[
                             N_{G[W]}(C)\subseteq K.    \tag{4.5}
\]

As in Theorem 4.1, `N_G(C)` separates the nonempty set `C` from the
nonempty retained donor `U'`, so it has order at least seven.  Every
neighbour outside `K` lies in one of the six branch sets different from
`U`.

If each such outside branch set contributes at most one vertex, then

\[
                 7\le |N_G(C)|\le |K|+6=|I|+5\le10.   \tag{4.6}
\]

Together with (4.5), this is outcome 2.  Otherwise one outside branch set
contains distinct vertices `x,y` of `N_G(C)`.  Choosing one edge from `C`
to each of `x,y` gives outcome 3 by the same companion-edge argument as in
Theorem 4.1. \(\square\)

## 5. Trust boundary

The set `K` is an internal separator of `G[W]`, not automatically a
separator of the host.  Its source-side component may have arbitrarily many
neighbours in other model branch sets, and the theorem gives no compatible
boundary colouring.  Seven-connectivity only lower-bounds the full host
neighbourhood after such exposure is included.

For two owners, Theorem 4.1 converts the internal obstruction into a
concentrated incident edge pair, a label-transversal exact seven-boundary,
or a repeated model-preserving contact.  It does not close any of those
three dynamic outcomes.  For three or more owners, Theorem 4.3 converts the
same internal obstruction into a portal set concentrated on at most four
vertices, an actual separation of order at most ten, or another repeated
model-preserving contact.  The bounded separation need not have order seven
or carry a common boundary partition.

The next host theorem must use the proper-minor colouring response and
`K_7`-minor exclusion either to align one of the returned edge pairs with
the five named labels, or to show that the operation-specific partition at
the exact seven-boundary reflects by the Hall criterion for mixed connected
supports.
