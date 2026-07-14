# Independent audit: atomic cyclic-shore closure

## Verdict

**GREEN** at frozen source SHA-256
`835209fa1641c03c6ac68f9eb7708127d04732f89ba2476469ce211fa04f3d12`.

For every cyclic thin shore of order at least four, the two root-neighbour
splits are literal disjoint connected adjacent carrier pairs.  Relative
seven-connectivity makes both root sides near-full.  If neither opposite
side is `W`-full, their nonempty overlap forces one common missed boundary
literal, contradicting the audited root-deletion normalization.  The
resulting near-full pair satisfies every hypothesis of the independently
audited two-carrier state exchange and therefore closes the atom.

The source correctly excludes the triangle and does not claim a theorem
for a cycle torso carrying additional attachments.

## 1. Singleton support estimates

The separation is

\[
 V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad S=W\mathbin{\dot\cup}\{u\},
\]

with nonempty `R`, no `A-R` edge, and `G[A]=C_n`.  For every `v in A`,
all neighbours of `v` lie in `A union S`.  Since the cycle gives exactly
two internal neighbours and seven-connectivity gives minimum degree at
least seven,

\[
                         2+|N_S(v)|\ge7.
\]

Equivalently, the displayed neighbourhood separates `v` from the
nonempty rich shore, so this is also a direct relative-cut application.

If `v ne z`, uniqueness of `zu` excludes `u` from `N_S(v)`.  Therefore
`v` contacts at least five members of `W` and misses at most one.  The
root `z` contacts `u` and at least four members of `W`.  These estimates
use literal edges only.

## 2. Legality of the two cyclic splits

Let `x,y` be the cycle neighbours of `z`.  For either

\[
 X_q=\{z,q\},\qquad Y_q=A-\{z,q\},
 \qquad q\in\{x,y\},
\]

both sets are nonempty when `n>=4`.  Each induces a path and is therefore
connected.  A cycle edge joins the two sets.  This includes `n=4`: the
remainder is the edge joining the vertex opposite `z` to the other
neighbour of `z`.

The carrier `X_q` contacts `u` through `z` and at least five distinct
members of `W` through `q`, so

\[
                         |N_S(X_q)|\ge6.
\]

No spanning-tree contraction is performed in this source; contraction
legality and exact state return enter only through the already audited
near-full two-carrier theorem.

## 3. The overlap argument

Suppose `Y_x` is not `W`-full.  Some literal `d_x in W` is absent from
its union of contacts, hence every vertex of `Y_x` misses `d_x`.
Similarly a failure for `Y_y` gives `d_y` missed by every vertex of
`Y_y`.

For `n>=4`,

\[
 Y_x\cap Y_y=A-\{z,x,y\}
\]

is nonempty.  Any vertex in this overlap lies outside `z` and misses at
most one member of `W`.  Since it misses both `d_x` and `d_y`, the two
literals coincide.  Moreover

\[
                         Y_x\cup Y_y=A-z.
\]

Thus every vertex of `A-z` would miss the same literal of `W`, contrary
to the audited identity `N_S(A-z)=W`.  At least one `Y_q` is consequently
`W`-full.  It avoids `z`, hence has no `u` contact and has exact boundary
support six.

## 4. Terminal invocation and scope

The selected `X_q,Y_q` are disjoint, nonempty, connected and adjacent,
with `z in X_q` and both boundary supports at least six.  The boundary is
explicitly one of the two audited atomic frontier forms.  The source may
therefore invoke the near-full two-carrier state exchange, whose connected
bipartite branch legally returns a demand-at-most-two equality state and
whose exceptional branch gives a literal `K_7`.  Either conclusion
contradicts the atomic counterexample setup.

The adjacency assumed between the two full packets is stronger than is
needed for the packet-reflection part, but it is harmless.

For `n=3`, the two remainders are disjoint singleton vertices and there is
no overlap on which to identify their missed labels.  The source correctly
leaves this cell open.  The proof also relies on actual cycle degree two;
it does not extend verbatim to a cyclic torso with off-torso attachments.
