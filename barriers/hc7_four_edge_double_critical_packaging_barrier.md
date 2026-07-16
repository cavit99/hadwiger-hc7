# Packaging barriers for four edge-local double-critical pairs

**Status:** Both constructions and their stated properties are proved
below.  They are scoped falsifiers, not counterexamples to `HC_7`.  In
particular, neither construction is asserted to be seven-connected,
seven-contraction-critical, or `K_7`-minor-free with the full exact-two-row
decoration.

The active note
`active/hc7_four_edge_double_critical_carriers.md` obtains three disjoint
connected carriers, each meeting a literal four-clique.  This note shows why
ordinary connectivity and uncoordinated contact abundance do not supply the
missing pairwise adjacency or a nonmonotone four-linkage.

## 1. A three-connected wheel without three adjacent full carriers

Let `W` have rim

\[
                          0,1,2,3,4,5,0
\]

and hub `h` adjacent to all six rim vertices.  Put

\[
                          A=\{0,1,2\},\qquad B=\{3,4,5\}.
\]

### Proposition 1.1

The graph `W` is three-connected and contains three pairwise
vertex-disjoint `A-B` paths.  Nevertheless, it has no three pairwise
vertex-disjoint, pairwise adjacent connected subgraphs each meeting both
`A` and `B`.

#### Proof

Deleting at most two vertices leaves `W` connected.  If the hub remains,
it joins every remaining rim vertex.  If the hub is deleted, at most one
rim vertex is also deleted, and the remaining rim is a path.  Thus `W` is
three-connected.

The edge paths `23` and `50`, together with the path `1h4`, are three
pairwise vertex-disjoint `A-B` paths.

Suppose for a contradiction that `T_1,T_2,T_3` are disjoint, pairwise
adjacent connected subgraphs and each meets `A` and `B`.  A connected
subgraph of the rim that meets both `A` and `B` must contain one of the only
two rim edges crossing the displayed bipartition, namely `23` or `50`.
Therefore at most two of the `T_i` can avoid the hub.  If all three avoided
the hub, their disjointness would be impossible.  Since disjoint subgraphs
cannot both contain the hub, exactly one, say `T_3`, contains `h`.

The other two subgraphs must use different crossing edges.  Relabel them so
that `T_1` contains `2,3` and `T_2` contains `5,0`.  Since `T_3` must still
meet both `A` and `B`, and the vertices `0,2,3,5` are already occupied,
`T_3` must contain the only remaining choices `1` and `4`.  Consequently
`T_1` and `T_2` cannot contain either `1` or `4`.  Their only possible
vertices are therefore `2,3` and `5,0`, respectively.  There is no edge
between these two pairs, contradicting the assumed adjacency of `T_1` and
`T_2`.  \(\square\)

### Scope

This disproves the implication

\[
\begin{split}
 &\text{three-connectivity and two terminal sets of order three}\\
 &\qquad\Longrightarrow
   \text{three disjoint pairwise-adjacent terminal carriers}.
\end{split}
\]

It does not show that the extra ordered-colour paths arising from a single
global colouring are useless.  A successful `HC_7` argument must couple
those paths to the labelled carrier packing rather than invoke
three-connectivity alone.

## 2. A four-connected four-gate linkage obstruction

Let `L` and `R` be disjoint four-cliques, let

\[
                            S=\{s_1,s_2,s_3,s_4\}
\]

be an independent set, and add a further vertex `v`.  Add every edge from
`L` to `S`, every edge from `S` to `R`, and every edge from `v` to `S`.  Add
no other edges beyond those inside `L` and `R`.  Call the resulting graph
`J`.

### Proposition 2.1

The graph `J` is four-connected.  Every family of four pairwise
vertex-disjoint `L-R` paths uses each vertex of `S` exactly once and avoids
`v`.

Consequently, even if all five vertices of `S union {v}` are declared to
be common-contact gates, four-connectivity and contact abundance do not
force either

1. an `L-R` linkage path containing two gates; or
2. a separator of order at most three.

#### Proof

The set `S` separates `L`, `R`, and `v`, so `kappa(J)<=4`.  Conversely,
delete any set `Z` of at most three vertices.  Some vertex `s` of `S-Z`
remains.  At least one vertex of `L union R union {v}` also remains, and
every surviving vertex in that set is adjacent to `s`.  Every other
surviving vertex of `S` is adjacent to every surviving vertex of
`L union R union {v}`.  Hence `J-Z` is connected.  Thus `kappa(J)=4`.

Every `L-R` path meets `S`, because `S` separates `L` from `R`.  Four
pairwise disjoint such paths therefore consume at least four distinct
vertices of `S`; since `|S|=4`, each path contains exactly one vertex of
`S`, and all four vertices of `S` are used.

If one of these paths contained `v`, then, because its ends lie in `L` and
`R` and `N_J(v)=S`, the predecessor and successor of `v` on the simple path
would be two distinct vertices of `S`.  That path would consume at least two
vertices of `S`, leaving at most two for the other three disjoint `L-R`
paths, a contradiction.  Thus every four-linkage avoids `v`.  The two
claimed consequences follow, and four-connectivity itself excludes a
separator of order at most three.  \(\square\)

### Scope

The graph `J` carries no asserted colouring that realizes the KPT ordered
paths, and it is not an exact-two-row `HC_7` instance.  It rules out only a
purely linkage-theoretic inference from many common-contact vertices.  The
still-live mechanism must synchronize the edge-local colour paths with a
particular four-linkage or exploit contraction-critical state transitions.

## 3. Research consequence

The edge-local double-critical package yields strong labelled contacts, but
the target is a **joint** packing statement.  Neither of the following may
be used without additional hypotheses:

* three disjoint full carriers can be made pairwise adjacent merely from
  three-connectivity; or
* an extra common-contact vertex forces a nonmonotone four-linkage or a
  separator of order at most three.

Any next lemma should name the synchronization mechanism: a common
five-colouring, compatible ordered paths, a linkage exchange, or a legal
proper-minor transition.
