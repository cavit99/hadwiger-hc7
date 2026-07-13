# Hall-circuit anti-diamond and the exact collision residue

## 1. Verdict

The three-state boundary diamond is not removed by forbidding separating
cliques.  Its graph realization has no clique separator.  Its actual defect
is quantitative: its connectivity is exactly the size of its rainbow core.

Connectivity by itself is still not a rooted-model principle.  Section 3
gives an explicit \((r+1)\)-connected, clique-separator-free graph with a
rainbow boundary core, two incompatible portal shores, and an unrooted
\(K_r\) subgraph.  The construction is deliberately not minor-critical;
the two extra contacts which raise connectivity are deletable without
repairing the colouring obstruction.

Actual Hall-circuit geometry supplies the missing restriction.  In a
\(k\)-connected graph, a Hall circuit of size \(h\) for an \(r\)-bag model
has at least \(k-h\) portal vertices in only \(r-h\) accessible bag labels.
Every rainbow-core boundary state has the same numerical surplus over the
\(r-h\) colours missing on the core.  Consequently there are at least
\(k-r\) **portal-label collisions** and at least \(k-r\)
**colour collisions**.  In particular, when \(k\ge r+1\), the one-shadow
transition diamond is impossible and every repair state contains a
collision.

This is a proved synchronization constraint, not yet the final
rooted-model theorem.  The exact remaining uniform problem is to align one
of the colour collisions with one of the multiply hit branch bags.  That
alignment is the first formulation which simultaneously uses all three
indispensable ingredients: minor operations, ambient connectivity, and the
labels of a pre-existing clique model.

## 2. Exact audit of the boundary-state diamond

Use the notation of `hadwiger_boundary_state_diamond_counterexample.md`.
Thus

\[
 q=r-h+2\ge3,
\]

the graph before suspension is the Hajós join \(F_q\) of two copies of
\(K_{q+1}\), and

\[
                 G_{r,h}=K_{h-2}\vee F_q.
\]

### Proposition 2.1

For every \(2\le h<r\),

\[
                         \kappa(G_{r,h})=h.
\]

Moreover, \(G_{r,h}\) has no separating clique.

#### Proof

Write the two open cliques of \(F_q\) as \(Z_a,Z_b\), each of order
\(q-1\), and retain the common vertex \(p\) and the edge \(ab\).  The
graph \(F_q\) is 2-connected: after deletion of any one vertex, either
\(p\) still joins the two open cliques, or the path through \(a b\) does.
On the other hand, deleting the nonadjacent pair \(\{p,a\}\) separates
\(Z_a\) from the rest.  Hence \(\kappa(F_q)=2\).

If a vertex of the universal clique \(K_{h-2}\) survives a deletion, it
joins every remaining vertex.  Therefore every disconnecting set contains
all of \(K_{h-2}\), and what remains of the set must disconnect \(F_q\).
It follows that

\[
 \kappa(K_{h-2}\vee F_q)=(h-2)+\kappa(F_q)=h.
\]

The same observation reduces a possible clique separator to
\(K_{h-2}\) together with a clique separator of \(F_q\).  But \(F_q\)
has no clique separator.  Indeed every clique lies in one of

\[
 Z_a\cup\{p\},\quad Z_a\cup\{a\},\quad
 Z_b\cup\{p\},\quad Z_b\cup\{b\},
\]

or is contained in the edge \(ab\).  Deleting any such clique leaves the
opposite side and one of \(p\) or the path through \(ab\) as a connector.
Thus no clique deletion disconnects \(F_q\), proving the claim. \(\square\)

So “no separating clique” does not touch the diamond.  A connectivity
hypothesis only excludes this particular realization when it exceeds the
rainbow-core order \(h\).

## 3. A high-connectivity static lift

The next construction shows that high connectivity, a rainbow core, full
portal attachment, and an unrooted clique still do not synchronize two
shore states without operation-criticality.

Fix

\[
                         2\le h<r,
 \qquad s=r-h+1\ge2.
\]

Let \(C\) be a clique of order \(h-2\), let \(L,R\) be disjoint cliques
of order \(s\), and let \(P\) be an independent set of order \(s\).
Add two further vertices \(a,b\).  Join \(C\) to every other vertex.  Add

* every edge from \(L\) to \(\{a\}\cup P\);
* every edge from \(R\) to \(\{b\}\cup P\);
* the edge \(ab\); and
* after selecting \(\ell_0\in L\) and \(r_0\in R\), the two cross
  contacts \(b\ell_0\) and \(ar_0\).

There are no further edges.  Denote the resulting graph by
\(D_{r,h}\).  Its boundary is

\[
 W=C\cup\{a,b\}\cup P,
\]

and its two open shores are \(L\) and \(R\).

### Proposition 3.1

The graph \(D_{r,h}\) has all of the following properties.

1. \(D_{r,h}\) is not \(r\)-colourable.
2. The left shore forces every vertex of \(P\) to have the colour of
   \(a\), while the right shore forces every vertex of \(P\) to have the
   colour of \(b\).
3. The core \(C\cup\{a,b\}\) is rainbow in every shore colouring.
4. \(D_{r,h}\) contains a \(K_r\) subgraph.
5. \(\kappa(D_{r,h})=r+1\) and \(\omega(D_{r,h})=r\).  In particular it
   has no separating clique.
6. It is not minor-critical: deletion of either cross contact leaves a
   non-\(r\)-colourable graph.

#### Proof

The set \(C\cup L\) is a clique of order

\[
 (h-2)+s=r-1.
\]

Every vertex of \(\{a\}\cup P\) sees this whole clique, so the left shore
forces all of them to the one remaining colour.  The vertex \(b\) can use
the colour of any member of \(L-\{\ell_0\}\), which is nonempty because
\(s\ge2\).  This proves that the left state exists and has the asserted
form.  The right side is symmetric.  The two states cannot agree because
\(ab\) is an edge, proving items 1--3.  Also
\(C\cup L\cup\{a\}\) is a \(K_r\), proving item 4.

It remains to compute connectivity.  Delete the universal clique \(C\)
and call the remaining graph \(D^0\).  We claim

\[
                           \kappa(D^0)=s+2.                 \tag{3.1}
\]

Let \(T\) have order at most \(s+1\).  If a vertex of \(P\) survives,
it joins every surviving vertex of \(L\cup R\).  If both open cliques
have surviving vertices, this is a connected spine to which \(a,b\)
attach.  If, say, all of \(L\) is deleted, only one further deletion is
available, so at least one of \(b,r_0\) survives and joins \(a\) to the
spine.  The symmetric statement holds for \(b\).

If all of \(P\) is deleted, then \(|P|=s\) uses all but at most one of
the allowed deletions.  The graph \(D^0-P\) is 2-connected: it contains
the chain

\[
                         L-a-b-R,
\]

and after deleting \(a\) the edge \(b\ell_0\) keeps \(L\) attached,
while after deleting \(b\) the edge \(ar_0\) keeps \(R\) attached.
Deletion of a vertex in \(L\cup R\) leaves the displayed chain because
each clique has order at least two.  Thus \(D^0-T\) is connected in all
cases.  This gives the lower bound in (3.1).  The neighbourhood

\[
                         N_{D^0}(a)=L\cup\{b,r_0\}
\]

has order \(s+2\), and its deletion isolates \(a\), proving equality.

As in Proposition 2.1, every cut of \(D_{r,h}=K_{h-2}\vee D^0\) contains
\(C\).  Hence

\[
 \kappa(D_{r,h})=(h-2)+(s+2)=h+s=r+1.
\]

The largest cliques are \(C\cup L\cup\{a\}\) and its symmetric copy,
of order \(r\).  Therefore no clique can be a separator in an
\((r+1)\)-connected graph.  Finally, the two cross contacts play no role
in the two equality-forcing arguments.  Deleting either one leaves the
left and right forced states incompatible, proving item 6. \(\square\)

For \((r,h)=(3,2)\), this is an eight-vertex, 4-connected,
clique-separator-free, non-3-colourable graph with a triangle and the two
incompatible two-shore states.  A direct exhaustive check for
\((r,h)=(3,2),(4,2),(4,3),(5,3),(5,4)\) gives respectively
\(\kappa=r+1\), \(\omega=r\), and no \(r\)-colouring, agreeing with the
uniform proof.  The dependency-free audit is
`verify_hall_anti_diamond_lift.py`.

This construction is the sharp warning: connectivity can be bought by
contacts irrelevant to the colouring obstruction.  Proper-minor
criticality is what forbids that purchase.

## 4. The Hall-circuit anti-diamond theorem

We now impose the actual geometry produced by a minimum model-relative
Hall deficit.

Let \(\mathcal B=(B_1,\ldots,B_r)\) be a labelled \(K_r\)-model in
\(G-v\).  Let \(I\) be a minimal nonlinkable family of bag labels, put

\[
                         h=|I|,
\]

and let \(X\) be its exact linkage separator, so \(|X|=h-1\).  Let
\(U\) be the root-side region and

\[
 P_j=N_{G-v}(U)\cap B_j,
 \qquad P=\bigcup_{j=1}^rP_j.
\]

The Hall-circuit promotion theorem gives

\[
 P_i=\varnothing\quad(i\in I),
 \qquad S=\{v\}\cup X\cup P
\]

as a genuine separator.  Write

\[
                         R_0=\{v\}\cup X,
 \qquad |R_0|=h.                                         \tag{4.1}
\]

### Theorem 4.1 (Hall-circuit label and colour collision)

Suppose \(G\) is \(k\)-connected.  Then:

1. The portal set satisfies
   \[
                         |P|\ge k-h.                      \tag{4.2}
   \]
2. Since the portals occur in at most \(r-h\) accessible bag labels,
   \[
     \sum_{j\notin I}\max\{0,|P_j|-1\}\ge k-r.           \tag{4.3}
   \]
3. Let \(c\) be any \(r\)-colour boundary state of a proper minor in
   which the labeled vertices of \(R_0\) survive and are rainbow.  Put
   \[
    \operatorname{col}_c(P\mid R_0)
      =|P|-\bigl|c(P)-c(R_0)\bigr|.                       \tag{4.4}
   \]
   Then
   \[
             \operatorname{col}_c(P\mid R_0)\ge k-r.     \tag{4.5}
   \]

Here (4.3) counts portal vertices in excess of one per accessible branch
bag.  Equation (4.4) counts every core-coloured portal and every occurrence
beyond the first of a colour missing on the core.

#### Proof

The genuine separator has order

\[
                         |S|=1+(h-1)+|P|=h+|P|.
\]

Connectivity gives \(|S|\ge k\), which is (4.2).

The sets \(P_i\), \(i\in I\), are empty, so at most \(r-h\) portal
classes are nonempty.  Consequently

\[
\begin{aligned}
 \sum_{j\notin I}\max\{0,|P_j|-1\}
 &=|P|-|\{j\notin I:P_j\ne\varnothing\}|\\
 &\ge(k-h)-(r-h)=k-r,
\end{aligned}
\]

which proves (4.3).

The rainbow set \(R_0\) uses \(h\) colours.  At most \(r-h\) colours
outside \(c(R_0)\) can occur on \(P\).  Thus

\[
 |c(P)-c(R_0)|\le r-h.
\]

Together with (4.2), this gives (4.5). \(\square\)

### Corollary 4.2 (anti-diamond)

If \(k\ge r+1\) and \(P\ne\varnothing\), then all of the following hold.

1. \(|P|\ge2\).  In particular, the one-shadow transition diamond cannot
   be the boundary state of a promoted Hall circuit.
2. Some accessible branch bag contains at least two distinct portal
   vertices.
3. Every rainbow-core repair state has a colour collision: either a portal
   has a colour used on \(R_0\), or two portal vertices have the same colour.

More generally there are at least \(k-r\) units of both label surplus and
colour surplus in the senses of (4.3) and (4.5).

#### Proof

If \(P\ne\varnothing\), some bag label lies outside \(I\), so
\(h\le r-1\).  Equation (4.2) gives

\[
                         |P|\ge k-h\ge2.
\]

Items 2 and 3 follow from (4.3) and (4.5), since \(k-r\ge1\). \(\square\)

For a hypothetical \(HC_7\) counterexample, \(r=6\) and \(k=7\).
Every promoted Hall circuit therefore has at least one multiply hit
accessible bag, and every six-colour state with the circuit core rainbow
has at least one colour collision.  The single-shadow rotation

\[
 \text{left anchor}\longrightarrow\text{fresh colour}
 \longrightarrow\text{right anchor}
\]

is not available.

The collision is not merely an equality in a boundary partition.  The
fixed clique model turns it into a small named carrier.

### Theorem 4.3 (uniform collision carrier)

Retain the hypotheses of Theorem 4.1, assume \(k\ge r+1\), and fix the
far-side \(X\)-rooted clique model supplied by the Hall circuit.  Thus for
each \(x\in X\) there is a branch set \(A_x\) containing \(x\), and every
\(A_x\) contains one of the original circuit bags.  Let \(c\) be an
\(r\)-colour state in which \(R_0=\{v\}\cup X\) is rainbow.  Then at least
one of the following occurs.

1. There are distinct \(p,q\in P\) with \(c(p)=c(q)\), and a connected
   carrier containing \(p,q\) lies in the union of at most two accessible
   branch bags.
2. There are \(p\in P\) and \(x\in X\) with \(c(p)=c(x)\), and a connected
   carrier containing \(p,x\) lies in \(B_j\cup A_x\), where
   \(p\in P_j\).
3. There is \(p\in P\) with \(c(p)=c(v)\), and a \(p\)-to-\(v\) carrier
   lies in \(U\cup\{p,v\}\) and otherwise avoids every old branch bag.

#### Proof

Corollary 4.2 gives a colour collision.  If two portal vertices \(p,q\)
have the same colour, write \(p\in B_j\), \(q\in B_\ell\).  If
\(j=\ell\), connectedness of \(B_j\) gives the carrier.  If
\(j\ne\ell\), the two branch bags are connected and adjacent because
they belong to a clique model, so \(B_j\cup B_\ell\) is a connected
carrier.  This is outcome 1.

Otherwise some portal \(p\) has the colour of a core vertex.  If that
vertex is \(x\in X\), the accessible bag \(B_j\) containing \(p\) is
adjacent to the original circuit bag contained in \(A_x\).  Both sets are
connected, so their union contains the carrier in outcome 2.

It remains that \(c(p)=c(v)\).  By the definition of
\(P=N_{G-v}(U)\cap Q\), the vertex \(p\) has a neighbour in a component
of \(U\) containing an unused root \(z\in N_G(v)\).  A path through that
component from \(p\) to \(z\), followed by \(zv\), gives outcome 3.  Its
interior is outside the old model by the construction of \(U\). \(\square\)

The theorem is deliberately stated in terms of a connected carrier, not
an internally boundary-clean path.  A carrier may encounter another portal
vertex before reaching its named endpoint.  Cleaning or exploiting that
first encounter is precisely the next exchange step; silently deleting it
would reintroduce the old portal-placement gap.

### Corollary 4.4 (co-rank-one alignment)

If \(|I|=r-1\) and \(k\ge r+1\), then all portals lie in the unique
accessible branch bag \(B\), \(|P|\ge2\), and every rainbow-core state has
one of the following two already aligned collisions:

1. two same-coloured portal vertices in \(B\); or
2. a core-coloured portal in \(B\), with the corresponding carrier from
   Theorem 4.3.

#### Proof

There is only one bag label outside \(I\), so all of \(P\) lies in that
bag.  Equation (4.2) gives

\[
                       |P|\ge k-(r-1)\ge2.
\]

Only one colour is missing on the rainbow core.  If no portal uses a core
colour, every portal uses this single missing colour, giving outcome 1.
Otherwise outcome 2 holds. \(\square\)

Thus label-versus-colour collision alignment is completely resolved for
Hall circuits of co-rank one.  Even in this cell, converting the aligned
carrier into a clean branch-bag split remains a geometric step; the
corollary does not silently assume it.

## 5. Exact residual principle: collision alignment

Theorem 4.1 identifies the smallest live rooted-model statement.  It is
important not to overclaim it.

The portal-label partition

\[
                         P=\dot\bigcup_{j\notin I}P_j
\]

has surplus, and every operated rainbow-core colour partition of \(P\)
has surplus.  These two collisions need not coincide combinatorially.  A
double portal in one bag can receive two different missing-core colours,
while a singleton portal in another bag carries the repeated or core
colour.  Pure pigeonhole counting cannot force alignment.

Theorem 4.3 shows that a colour collision already has a model-labelled
location involving at most two accessible bags.  The genuinely new uniform
target is therefore:

> **Collision-alignment principle.**  In a least-parameter, join-prime,
> proper-minor-minimal non-\(r\)-colourable graph, at a promoted Hall
> circuit, some faithful one- or two-shore operation produces either
>
> 1. a collision carrier can be cleaned and used for a label-preserving
>    split or rotation;
> 2. a first extra portal encountered by every such cleaning attempt yields
>    a smaller Hall circuit or a strictly larger contact routing; or
> 3. compatible original boundary states which colour-glue across the
>    promoted adhesion.

The first two outcomes are now an exact carrier-cleaning problem.  The
third contradicts the assumed counterexample.

This principle is strictly narrower than Strong Hadwiger.  Its hypotheses
include an exact Hall circuit, a genuine ambient separator, a fixed labeled
clique model, all proper-minor transition colourings, and the simultaneous
label and colour surplus of Theorem 4.1.  The original diamond fails its
connectivity conclusion; the high-connectivity lift in Section 3 fails
proper-minor criticality.  The remaining obstruction must satisfy both at
once.

What is proved here is the anti-diamond/collision theorem.  What remains is
the operation-sensitive alignment step.  This is a concrete uniform
rooted-model problem rather than another enumeration of Moser labels.
