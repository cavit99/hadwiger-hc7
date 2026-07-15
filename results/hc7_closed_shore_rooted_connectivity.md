# Closed-shore rooted connectivity

**Status:** proved and independently audited.

## Lemma

Let `G` be seven-connected and let

\[
        V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
        \qquad |S|=7,
\]

where `A` and `R` are nonempty and there is no `A-R` edge.  For every
nonempty set `Q subseteq S`, put

\[
                         J_Q=G[A\cup Q].
\]

Then the rooted pair `(J_Q,Q)` is internally `|Q|`-connected: there
is no separation `(X,Y)` of `J_Q` such that

\[
 Q\subseteq X,\qquad Y-X\ne\varnothing,
 \qquad |X\cap Y|<|Q|.
\]

In particular, if `|Q|=4`, then `(G[A union Q],Q)` is internally
four-connected.

## Proof

Suppose that `(X,Y)` is such a separation and define

\[
                         Z=(X\cap Y)\cup(S-Q).
\]

Because `Q subseteq X`, every vertex of `Y-X` lies in `A`.  The separation
of `J_Q` implies that no vertex of `Y-X` has a neighbour in `X-Y` inside
`J_Q`.  A vertex of `Y-X` has no neighbour in `R` by hypothesis, and all
of its possible neighbours in `S-Q` belong to `Z`.  Hence in `G-Z` there
is no edge from `Y-X` to a vertex outside `Y-X`.

The set `Y-X` is nonempty.  The set `R` is also nonempty and is disjoint
from `Z`, so `G-Z` has at least two components.  Since the orders are
integral,

\[
 |X\cap Y|\le |Q|-1,
 \qquad
 |Z|\le (|Q|-1)+(7-|Q|)=6.
\]

This contradicts seven-connectivity and proves the claim.  \(\square\)

## Application to the active four-root decoder

Let

\[
 Q=\{a_0,a_1,b_0,b_1\}
\]

be the four distinct literal roots produced by the audited two-list/Menger
dichotomy.  Then `(G[A union Q],Q)` is internally four-connected.  Thus
the Robertson--Seymour--Thomas rooted four-terminal trichotomy and
Jorgensen's rooted `K_4^-` consequence apply to the literal closed thin
shore without any additional local-connectivity assumption.

This does **not** prove the active decoder.  A rooted `K_4^-` supplies only
four rooted bags and does not supply the fifth boundary-rooted bag needed
with the two rich packets.  In the rural alternative, the three omitted
literal boundary vertices and the global seven-cut inequalities still
have to be decoded.

### Corollary (rural branch normalizes to a rooted `K_4`)

Assume `|A|>=2`, and let `P_0,P_1` be the two vertex-disjoint boundary
paths with respective ends `a_0,b_0` and `a_1,b_1`.  If

\[
 G[A\cup Q]
\]

has a disk embedding with boundary order

\[
                       a_0,a_1,b_0,b_1,
\]

then `G[A union S]` has a `Q`-rooted `K_4` model.  Moreover the interior
of one of `P_0,P_1` can be kept disjoint from all four bags of that model.

#### Proof

The pair `(G[A union Q],Q)` is internally four-connected and has at least
six vertices.  Jorgensen's rooted consequence therefore gives a
`Q`-rooted `K_4^-` model in this literal graph.

The nonrequired pair of this diamond cannot be consecutive in the displayed
facial order.  Indeed, if (for example) `a_0a_1` were the nonrequired pair,
the required bag adjacencies `a_0b_0` and `a_1b_1` would contain two
vertex-disjoint paths joining alternating vertices of the disk boundary,
which is impossible.  The same argument handles every consecutive pair.
Nor can all six bag adjacencies be present.  Such a rooted `K_4` model
would contain, using the two relevant model edges and paths inside their
four pairwise disjoint bags, vertex-disjoint paths from `a_0` to `b_0`
and from `a_1` to `b_1`.  Their ends alternate on the boundary of the
disk, contradicting the Jordan curve theorem.  Hence the unique missing
adjacency is one of

\[
                         a_0b_0,\qquad a_1b_1.
\]

Suppose it is `a_i b_i`.  The path `P_i` has no internal vertex in `Q`,
and its internal vertices lie in `S-Q`, whereas all four diamond bags lie
in `A union Q`.  Add all vertices of `P_i-b_i` to the bag rooted at
`a_i`.  This bag stays connected and the final edge of `P_i` supplies the
missing adjacency to the `b_i` bag.  The four bags now form a literal
rooted `K_4` model.

The paths `P_0,P_1` are vertex-disjoint, so the interior of `P_{1-i}` is
disjoint from all four expanded bags.  \(\square\)

The remaining constructive problem is now an augmentation problem, not
the existence of a rooted four-bag model: split or reroute this literal
`K_4` using the unused boundary path and the remaining portal sets to
obtain either the adaptive two-carrier return or a fifth rooted clique bag.

## Literature check

The rooted consequence used above is stated as Lemma 10 in Norin and
Totschnig, *Every graph with no `K_7^vee`-minor is 6-colorable*,
arXiv:2507.03244.  The generalized web/crossing machinery of Humeau and
Pous, arXiv:2505.16431v2, organizes the rural/crossing alternative but does
not create the missing fifth rooted bag or preserve a colouring state.
