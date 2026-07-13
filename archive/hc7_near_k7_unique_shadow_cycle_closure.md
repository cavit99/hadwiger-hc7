# The unique shadow closes by a rooted triangle cycle

## Status

This note eliminates the `d=1` unique-shadow residue in the audited
singleton/bipartite shell.  The earlier crossed-theta reduction is not
needed.

The proof is literal: after deleting the four ordinary singleton labels,
three-connectivity puts the apex, its shadowed singleton, and one
list-saturated bag vertex on a common cycle.  Splitting that cycle into a
rooted triangle and restoring the four singleton labels gives `K_7`.

## Theorem 1 (unique-shadow cycle closure)

Let `G` be seven-connected and suppose

\[
 V(G)=\{v\}\mathbin{\dot\cup}V(B)
       \mathbin{\dot\cup}S,qquad |S|=5,                  \tag{1.1}
\]

where `S` is a clique and `B` is a nontrivial connected induced bipartite
bag adjacent to every vertex of `S`.  Contract `B` and use the canonical
six-colouring of the quotient.  Suppose the apex colour shadows a unique
singleton `b in S`; equivalently

\[
                  vb\notin E(G),qquad v\sim S-\{b\}.     \tag{1.2}
\]

Then `G` contains a `K_7` minor.

### Proof

Put

\[
                            C=S-\{b\}.                     \tag{1.3}
\]

Thus `C` induces `K_4`, and both `v` and `b` are complete to `C`.

Let `alpha` be the contraction colour and define the expansion lists on
`B` from the fixed quotient colouring.  The graph `B` is not list-
colourable, since such a colouring would expand the quotient state to a
six-colouring of `G`.  If every vertex in one bipartition class of `B`
had a list colour other than `alpha`, give the other bipartition class
colour `alpha` and choose one secondary list colour independently on the
first class.  This would list-colour `B`.  Hence each bipartition class
contains a vertex whose list is exactly `{alpha}`.

Choose one such vertex `x`.  Each of the four nonshadow colours occurs
outside `B` at exactly one member of `C`.  The singleton list at `x`
therefore forces

\[
                             x\sim C.                      \tag{1.4}
\]

Now put `K=G-C`.  Deleting four vertices from a seven-connected graph
leaves a three-connected graph.  The three distinct vertices

\[
                              v,b,x\in V(K)                 \tag{1.5}
\]

lie on a common cycle: every three specified vertices of a
three-connected graph lie on one cycle.  Split that cycle at the three
roots into three nonempty, disjoint, connected arcs, assigning the three
cycle edges between consecutive arcs as their mutual adjacencies.  This
gives a `K_3` minor in `K` with one branch bag containing each of
`v,b,x`.

By (1.2), the clique property of `S`, and (1.4), each of those three bags
is adjacent to every vertex of `C`.  Consequently the three rooted cycle
bags together with the four singleton bags `{c}`, `c in C`, are seven
pairwise adjacent connected branch sets.  They form a `K_7` model.
\(\square\)

## Audit boundary

The word **unique** in (1.2) is essential for this proof: it makes `v`
complete to the same four-clique as `b` and the saturated witness `x`.
The saturated witness is obtained from non-six-colourability of the
original graph; mere full palette exposure in a proper minor would not
be enough if the other model bags were nonsingleton.
