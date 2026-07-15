# Rich-edge quotient of the five compulsory locks

**Status:** proved and independently audited.

This note identifies the exact consequence of the audited twin-state
handoff for the surviving compulsory locks.  It obtains five pairwise
edge-disjoint two-route systems in one fixed `G-zu` colouring whenever all
five locks genuinely use the rich shore.  It also
locates the first unsupported decoder: edge-disjoint coloured routes may
share an arbitrary set of vertices of the repeated colour, and the
independently attained final-duty routes have no common-state relation to
them.

## 1. Setup

Use the frozen atomic separation

\[
 V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad S=W\mathbin{\dot\cup}\{u\},
\]

and the compulsory edge `e=zu`.  Fix one proper six-colouring `phi` of
`G-e`, and put

\[
                         \phi(z)=\phi(u)=\alpha.        \tag{1.1}
\]

For each of the other five colours `delta`, let `K_delta` be the
`alpha-delta` component of `G-e` containing `z` and `u`.  These components
exist by the compulsory-edge Kempe locks.

Assume the rich lock-bridge branch has already been handed to the audited
state-labelled `(1,1)` S4 cell.  Equivalently, no `K_delta` has a
`z-u`-separating bridge which is rich-internal or boundary--rich.

## 2. The rich-edge quotient

Let `C_delta` be the set of connected components of

\[
                         K_\delta-R
                =K_\delta[V(K_\delta)\cap(A\cup S)].   \tag{2.1}
\]

Contract every member of `C_delta` to one vertex, leave every rich vertex
uncontracted, delete loops, and retain parallel edges.  Call the resulting
multigraph `Q_delta`.  Let `s_delta,t_delta` be the contracted vertices
containing `z,u`, respectively.

Every nonloop edge of `Q_delta` represents one literal edge of `K_delta`
which is either rich-internal or boundary--rich.  Indeed, an edge with
both ends outside `R` lies within one component of (2.1), while the old
separation has no `A-R` edge.

### Theorem 2.1 (same thin component or two rich-edge routes)

For every alternate colour `delta`, exactly one of the following
structural alternatives applies:

1. `s_delta=t_delta`; equivalently, `K_delta-R` contains a literal
   `z-u` path; or
2. `Q_delta` contains two edge-disjoint `s_delta-t_delta` paths.

In item 2, the lifted paths use pairwise disjoint sets of literal
rich-internal/boundary--rich edges.  Paths belonging to different colours
`delta != epsilon` also use disjoint sets of such literal edges.

#### Proof

The graph `Q_delta` is connected because `K_delta` is connected and only
connected vertex sets were contracted.  If `s_delta=t_delta`, item 1
holds.  Assume they are distinct.

Suppose the minimum size of an `s_delta-t_delta` edge cut in `Q_delta`
were one.  Its unique edge `bar f` is an `s_delta-t_delta`-separating
bridge of the multigraph.  Because parallel edges were retained,
`bar f` has one well-defined literal preimage edge `f` in `K_delta`.
Deleting `f` disconnects `z` from `u`: otherwise a surviving literal
`z-u` path would contract to a walk, and hence a path, from `s_delta` to
`t_delta` avoiding `bar f`.

The edge `f` is rich-internal or boundary--rich by the observation before
the theorem.  It is therefore precisely a rich `z-u`-separating lock
bridge, excluded by the state-labelled S4 handoff theorem.  The minimum
edge cut has order at least two.  The edge form of Menger's theorem,
valid for multigraphs, supplies two edge-disjoint source--target paths.
Their literal lifts use disjoint retained edges, proving item 2.

Finally fix distinct alternate colours `delta,epsilon`.  Every retained
literal edge in the `delta` system has endpoints of colours `alpha` and
`delta`, because `phi` is proper.  An edge in the `epsilon` system has
endpoint colours `alpha` and `epsilon`.  One literal edge cannot satisfy
both descriptions when `delta != epsilon`.  Thus the five systems are
pairwise edge-disjoint on all retained rich-internal/boundary--rich edges.
\(\square\)

### Corollary 2.2 (the exact five-system certificate)

If no compulsory lock has a `z-u` path wholly in \(A\cup S\), the one
fixed colouring `phi` supplies ten rich-edge source--target routes: two
for each alternate colour, pairwise edge-disjoint within a colour and
with the edge sets for distinct colours disjoint as well.

This is stronger than five independently chosen Kempe paths, but it is
an edge-capacity statement only.

## 3. Exact unsupported decoders

Theorem 2.1 first leaves the thin-component alternative.  No audited
theorem currently turns one bichromatic `z-u` path in \(A\cup S\) into
adjacent near-full carriers, a rooted model, or an attained lower-demand
state.  The path must meet `W` because `zu` is a bridge of `G-W`, but it
may run through several literal boundary vertices and need not split `A`.

### Lemma 3.1 (thin locks force distinct coloured neighbours of `u`)

If alternate colour `delta` satisfies item 1 of Theorem 2.1, then there is
a literal vertex

\[
                w_\delta\in N_{G[S]}(u)\cap W,
                \qquad \phi(w_\delta)=\delta.          \tag{3.1}
\]

Vertices obtained from distinct alternate colours are distinct.
Consequently:

1. in the exceptional frontier
   `G[S]=K_{1,3} dotunion K_3`, at most three compulsory locks can be
   thin; and
2. if all five locks are thin in the connected-bipartite frontier, its
   bipartition is
   \[
                   S=\{u,p\}\mathbin{\dot\cup}J,
                   \qquad |J|=5,                       \tag{3.2}
   \]
   the vertex `u` is adjacent to every member of `J`, and the five
   vertices of `J` receive the five colours different from `alpha`.
   The remaining vertex `p` repeats one of the six colours, so the exact
   boundary state under `phi` has six blocks, exactly one of order two.

#### Proof

Take a literal `z-u` path in `K_delta-R`.  Its last edge is not `zu`,
because the lock lies in `G-zu`.  Its predecessor `w_delta` at `u` cannot
lie in `A`, since `zu` is the unique `A-u` edge, and it does not lie in
`R` by construction.  Hence it lies in `S-{u}=W`.  The path is
`alpha-delta` bichromatic and `u` has colour `alpha`, so properness forces
`phi(w_delta)=delta`.  Different colours give different literal vertices.

The exceptional frontier has maximum boundary degree three, proving item
1.  In the connected-bipartite frontier orient the bipartition as
`S=I dotunion J` with `u in I`; the frozen atomic setup has `|I|>=2`.
Five thin colours give five distinct neighbours of `u`, all in `J`.
Since `|S|=7`, it follows that `|J|=5` and `I={u,p}`.  The five neighbours
carry the five alternate colours.  Together with `u` they already use all
six colours, so `p` repeats exactly one of them.  Properness makes the
repeated pair independent, proving the final state assertion.  \(\square\)

Thus an unconditional continuation first needs a **thin-lock decoder**
for this forced rainbow-neighbour structure, or an argument that all five
alternate colours fall in item 2.

Condition now on that all-rich-routes branch.  Even there, Theorem 2.1
does not give two internally vertex-disjoint paths.  Distinct colour
systems can meet only at vertices coloured `alpha`, but all five systems
may concentrate at the same such vertex.

The following quotient architecture is the sharp local warning.  Use
source and target vertices `s,t`, one common rich vertex `h` of colour
`alpha`, and, for each alternate colour `delta_i`, four rich vertices
`a_i,b_i,c_i,d_i` of colour `delta_i`.  Put in the two routes

\[
  s-a_i-h-c_i-t,
  \qquad
  s-b_i-h-d_i-t.                                      \tag{3.3}
\]

For each `i` the routes are edge-disjoint and no one of their edges
separates `s` from `t`.  Edge sets for different `i` are disjoint.  Yet
`h` is a common internal vertex of every source--target route in this
displayed network, so it contains no two internally vertex-disjoint
`s-t` paths.  The pattern respects the only cross-colour intersection
allowed by `phi`: the shared vertex has colour `alpha`.

This is a quotient obstruction, not a counterexample to HC7.  Ordinary
seven-connectivity does not exclude it inside a two-colour subgraph;
edges of the other colours can keep the host highly connected.

Consequently the first new theorem required **within the all-rich-routes
branch** is
an **alpha-articulation dispersion lemma**:

> In the frozen atomic counterexample, either the repeated-colour
> articulation set of the five rich-edge quotient systems can be split so
> as to give the required vertex-disjoint labelled carriers/rooted bags,
> or it exposes an actual order-seven state-carrying adhesion, a literal
> `K_7`, or the normalized fixed-pair/near-model handoff.

Edge-Menger alone cannot prove this statement.

There is a second, logically later compatibility issue.  The audited
final-duty dichotomy gives either its own two edge-disjoint rich routes or
one localized separating edge with a compressed state.  That certificate
comes from a separately attained colouring, not from `phi`.  Hence its
edges, repeated-colour vertices, and equality blocks have no proved
relation to the five systems above.  Before it can repair (3.3), one must
either:

1. decode the five fixed-state systems without using the final-duty
   certificate; or
2. prove a named common-minor/common-state transition placing one
   final-duty route or localized edge in the same quotient state.

Asserting such compatibility is exactly the previously rejected
intersection of unrelated proper-minor state families.  Thus the complete
decoder order is precise:

1. close or exclude the thin-lock alternative;
2. disperse repeated-colour articulations in the all-rich-routes branch;
3. only then synchronize one surviving route with the independently
   attained final-duty alternative.
