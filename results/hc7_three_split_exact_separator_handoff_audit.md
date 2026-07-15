# Audit of the three-split exact separator handoff

**Verdict:** **GREEN.**  The weighted separator equality expands to an
actual seven-boundary, hit and unhit split bundles behave exactly as
claimed, every lifted component is full, and no named model can straddle
the two open shores.

## 1. Expansion order and component correspondence

The three split edges form a matching because the model supports are
pairwise vertex-disjoint.  Replacing every hit quotient image `z_i in T`
by its two endpoints increases the separator order once per hit image, so

\[
                         |T^+|=|T|+\rho(T).
\]

Thus the displayed equality in Theorem 3.1 gives `|T^+|=7` literally.

For an unhit quotient image, its fibre under the contraction map is the
connected edge `x_i y_i`; every other fibre is a singleton.  Every edge of
`H-T` has a literal preimage edge joining the corresponding fibres, so the
full preimage of each connected quotient component is connected.  In the
other direction, any edge of `G-T^+` joining the preimages of two quotient
components would contract to an edge between those components.  Hence no
such edge exists.  The component correspondence in Lemma 2.1 is therefore
a bijection, including when a quotient component consists only of one or
more bundle images.

Since `T` is a separator, `H-T` has at least two nonempty components; their
preimages give at least two nonempty components of `G-T^+`.  Thus the
order-seven set is an actual boundary rather than only a deletion set of
the right cardinality.

## 2. Fullness

For a component `C` of `G-T^+`, all its neighbours lie in `T^+`.  Another
lifted component is nonempty, so `N_G(C)` genuinely separates two nonempty
vertex sets.  Seven-connectivity yields `|N_G(C)|>=7`.  As `N_G(C)` is a
subset of the seven-set `T^+`, equality holds and every literal boundary
vertex has a neighbour in `C`.  This proves the asserted `S`-fullness
without any minimum-degree substitute.

## 3. Named-model placement

For each model, `L_i=Q_i union {z_i}` is a clique in the quotient.  Its
vertices outside `T` lie in at most one component of `H-T`, because any
two such vertices retain their clique edge.  The exact component
correspondence then gives the following two cases.

* If `z_i in T`, both `x_i,y_i` lie in the lifted boundary, all
  `Q_i cap T` vertices also lie there, and all remaining singleton rows
  lie in one expanded component.
* If `z_i notin T`, its entire connected fibre `x_i y_i` and every
  singleton row outside the boundary lie in the one expanded component
  containing the fibre.  Thus the unhit split bag cannot divide between
  shores.

Consequently every complete support `Q_i union {x_i,y_i}` is contained in
the boundary plus at most one component.  After any nontrivial bipartition
of the component set, it belongs wholly to the corresponding closed shore;
a support entirely in the boundary may be assigned to either.  The three
models need not choose the same shore, and the theorem does not claim that
they do.

## 4. Collision counts and RST cells

If `|T|<=6`, the equality `|T|+rho(T)=7` and
`0<=rho(T)<=3` force `rho(T)>=1` and give exactly

\[
                         (4,3),(5,2),(6,1).
\]

The number of split edges in the adhesion is exactly `rho(T)`; all other
split bags remain intact in components.

For an active RST cell, the off-boundary condition gives

\[
 N_H(Y_j-X_j)\subseteq W\cup X_j.
\]

The two stated nonemptiness conditions leave vertices on both sides after
deleting `W union X_j`, so this set is a genuine separator.  Literal
expansion of order at most six contradicts seven-connectivity by the same
component correspondence, while expanded order seven invokes the audited
decoder.  The statement about `W` correctly includes the separate
hypothesis that `W` itself is a separator.

## 5. Scope

The result is only an exact-weight decoder.  It neither finds a separator
with expanded order seven nor handles expanded order at least eight.  It
also does not orient the resulting exact-seven separation or preserve a
colouring state.  These limitations are stated correctly in the source.
