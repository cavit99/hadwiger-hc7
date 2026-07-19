# Two-part shore normal form and common-transversal descent

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_common_two_vertex_transversal_descent_audit.md`](hc7_order8_common_two_vertex_transversal_descent_audit.md).
This is an unbounded reduction for the connected order-eight
opposite-response interface.  It does not prove `HC_7`.

## 1. Setting

Let `G` be a seven-connected graph such that every proper minor of `G` is
six-colourable.  Suppose

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad E_G(L,R)=\varnothing,
 \qquad |S|=8,
 \qquad L,R\ne\varnothing,                         \tag{1.1}
\]

where `G[R]` is connected.  Write

\[
 S=\{d,e\}\mathbin{\dot\cup}X\mathbin{\dot\cup}Y,
 \qquad |X|=|Y|=3.                                 \tag{1.2}
\]

Assume that `d,e` are nonadjacent, that `X,Y` are independent, that there
is an edge between `X` and `Y`, and that each of `d,e` has a neighbour in
each of `X,Y`.

The two closed shores have opposite responses to the exact boundary
partitions

\[
 \Pi_{\rm split}=X\mid Y\mid\{d\}\mid\{e\},
 \qquad
 \Pi_{\rm merged}=X\mid Y\mid\{d,e\}.              \tag{1.3}
\]

More precisely, `G[L\cup S]` realizes `Pi_merged` but not `Pi_split`,
whereas `G[R\cup S]` realizes `Pi_split` but not `Pi_merged`.

Assume also that `G[R]` contains two vertex-disjoint nonempty connected
subgraphs, each adjacent to every literal vertex of `S`.

A **root connector** is a nonempty connected subgraph of `G[R]` having a
neighbour at each of `d,e`.  For `B` equal to `X` or `Y`, a set
`F\subseteq R` is a **boundary-block carrier for `B`** if `G[B\cup F]` is
connected and contains an edge.  The set `F` need not induce a connected
subgraph.

## 2. Two-part normal form and common-transversal descent

### Theorem 2.1

There is a partition

\[
                         R=P_0\mathbin{\dot\cup}P_1              \tag{2.1}
\]

such that each `G[P_i]` is connected and adjacent to every literal vertex
of `S`, and there is a `P_0`--`P_1` edge.

For either `i\in\{0,1\}`, every root connector contained in `P_i`
intersects every boundary-block carrier for `X` contained in `P_i`, and
also intersects every boundary-block carrier for `Y` contained in `P_i`.

Suppose, in addition, that a set `Z\subseteq R` of order at most two meets

1. the vertex set of every root connector;
2. every boundary-block carrier for `X`; and
3. every boundary-block carrier for `Y`.

Then `|Z|=2`.  For every component `C` of `G[R-Z]` there are unique
vertices

\[
                r_C\in\{d,e\},\qquad x_C\in X,
                \qquad y_C\in Y                         \tag{2.2}
\]

such that

\[
                  N_G(C)=Z\mathbin{\dot\cup}
                   \bigl(S-\{r_C,x_C,y_C\}\bigr).       \tag{2.3}
\]

Consequently `N_G(C)` is the boundary of an actual separation of order
seven.  Every component of `G-N_G(C)` is adjacent to every literal vertex
of `N_G(C)`.

Moreover, the selected colouring in (1.3), restricted to
`G[C\cup N_G(C)]`, supplies a proper six-colouring of that closed shore.
On the five inherited vertices of `S\cap N_G(C)`, it retains the literal
blocks

\[
 X-\{x_C\},\qquad Y-\{y_C\},\qquad
 \{d,e\}-\{r_C\};                                    \tag{2.4}
\]

the two vertices of `Z` retain their actual selected colours.

### Proof

Apply Lemma 1.1 of the audited connected-rich width-two frontier to the
two disjoint boundary-full connected subgraphs in `R`.  It gives the
partition (2.1), connectedness and boundary fullness of both induced
parts, and a cross-edge.

Fix `i`, let `D\subseteq P_i` be a root connector, and suppose for a
contradiction that `F_X\subseteq P_i-V(D)` is a boundary-block carrier for
`X`.  The set `P_{1-i}` is a boundary-block carrier for `Y`, since it is
connected and adjacent to every vertex of `Y`.  Thus

\[
                         V(D),\qquad F_X,\qquad P_{1-i}
\]

are pairwise disjoint.  The audited root-connector reflection theorem then
forces `G[L\cup S]` to realize `Pi_split`, contrary to the opposite-response
hypothesis.  Interchanging `X,Y` proves the same assertion for every
`Y`-carrier.  This establishes the symmetric cross-intersection statement.

First, `R\ne Z`.  Indeed, let `Q_0,Q_1` be the two disjoint connected
subgraphs of `G[R]` that are adjacent to every vertex of `S`.  If
`R=Z`, then `|R|\le2` forces

\[
                  V(R)=\{q_0,q_1\},\qquad
                  V(Q_i)=\{q_i\}\quad(i=0,1).          \tag{2.5}
\]

Connectedness of `G[R]` gives the edge `q_0q_1`, and each `q_i` is
adjacent to every vertex of `S`.  The merged-root partition `Pi_merged` uses
three colours on `S`.  Give `q_0,q_1` two distinct colours among the other
three.  This properly colours `G[R\cup S]` and induces `Pi_merged`, contrary to
the hypothesis.  Thus `G[R-Z]` has a component.

Let `C` be any such component.  It cannot have neighbours at both `d,e`,
because then the connected graph `G[C]` would itself be a root connector
disjoint from `Z`.  Hence `C` misses at least one of the two root vertices.

Likewise, `C` cannot have a neighbour at every vertex of `X`.  If it did,
then `G[X\cup C]` would be connected and would contain an edge, so `C`
would be a boundary-block carrier for `X` disjoint from `Z`.  The same
argument applies to `Y`.  Therefore

\[
                       |N_G(C)\cap S|\le 1+2+2=5.     \tag{2.6}
\]

Since `C` is a component of `G[R-Z]`, all its neighbours in `R-C` lie in
`Z`; it has no neighbour in `L` by (1.1).  Thus

\[
                       |N_G(C)|\le |Z|+5\le7.         \tag{2.7}
\]

The set `N_G(C)` is a genuine separator: `C` is nonempty, while the
nonempty open shore `L` lies outside `C\cup N_G(C)`.  Seven-connectivity
and (2.6) force equality throughout.  Hence `|Z|=2`, every vertex of `Z`
has a neighbour in `C`, and `C` has exactly five neighbours in `S`.  It
misses exactly one vertex from each of the three groups in (1.2), proving
the uniqueness in (2.2) and the identity (2.3).

Put `T=N_G(C)`.  If a component `K` of `G-T` missed some vertex `t\in T`,
then

\[
                           N_G(K)\subseteq T-\{t\},
\]

which has order six.  There is another component of `G-T` because `T` is
an actual separator.  Thus `N_G(K)` would be a separator of order at most
six, contrary to seven-connectivity.  Every component of `G-T` is
therefore adjacent to every vertex of `T`.

Finally, restrict the selected proper six-colouring of `G[R\cup S]` to
`C\cup T`.  Restriction preserves properness and the equality relations
on the five retained vertices of `S`, giving (2.4); the colours on `Z`
are the actual colours already assigned by the selected colouring.  This
proves the last assertion. \(\square\)

## 3. Exact gain and trust boundary

The theorem first replaces the two initially named boundary-full connected
subgraphs by an adjacent two-part cover of the whole connected shore.  In
each part, the root-connector family cross-intersects both labelled
boundary-block-carrier families.  A common transversal of order at most
two for the three global families then gives an exact order-seven
separation.  The descent preserves a literal one-sided colouring response
and makes every new complementary component full to the new boundary.

It does not prove that such a transversal exists.  It also does not show
that the opposite closed shore induces the same equality partition on the
new seven-set; therefore the returned separation is not yet a colouring-
compatible gluing certificate.  No inference from abstract colours to the
labels `d,e,X,Y` is made.

## 4. Immediate proof dependencies

The two-part cover is exactly
[Lemma 1.1 of the connected-rich width-two frontier](../results/hc7_exact7_connected_rich_width2_frontier.md).
The cross-intersection conclusion uses the
[root-connector reflection theorem](../results/hc7_order8_root_connector_reflection.md),
including its generalized boundary-block-carrier definition.  The
common-transversal descent is elementary from seven-connectivity and the
selected opposite boundary response.

The theorem does not invoke `K_7`-minor exclusion or a finite boundary
census.
