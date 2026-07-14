# Packet-donor rotation lock

**Status:** proved and independently audited.

This note transports actual paired-state information into the first
near-`K_7` rotation produced by the complementary-lock handoff.  It does
not assume that a full packet survives a split.  Instead, the two literal
boundary anchors in a packet bag identify exactly which lobe rows a gate
can monopolize.  In the no-`K_7^-` branch, every packet-donor rotation is
either aligned through the selected old twin or creates a new
three-terminal Kempe lock.

## 1. The decorated spanning model

Use the exact complementary-lock setup

\[
 S=\{c,a_1,t_1,a_2,t_2,a_3,t_3\},\qquad
 B_i=\{a_i,t_i\}.
\tag{1.1}
\]

Let `r,s` be the two vertices of `B_3`, chosen so that `cr` is a literal
edge.  Work in the two-hole branch `cs notin E(G)`.  The audited handoff
has the spanning labelled `K_7^vee` model

\[
 \{s\},\{c\},\{r\},X,Y,F_1,F_2,
 \qquad F_1=L\cup B_1,\quad F_2=Q\cup B_2,             \tag{1.2}
\]

where `{s}` misses exactly `{c},{r}`.  The four bags `X,Y,F_1,F_2` form a
clique model and meet all three singleton bags.  More precisely,

\[
 X=D\cup\{x\},\qquad Y=E\cup\{y\},                    \tag{1.3}
\]

and the complementary-lobe incidences give

\[
 N_{F_1}(X)=\{t_1\},\qquad N_{F_1}(Y)=\{a_1\}.         \tag{1.4}
\]

Here `N_{F_1}(X)` denotes the set of vertices in `F_1` having a neighbour
in `X`.  Indeed, different components of `G-S` have no edge, `X` misses
`a_1`, `Y` misses `t_1`, and both poles miss `B_1`; the displayed lobe
contacts supply the two remaining edges.  Symmetrically,

\[
 N_{F_2}(X)=\{t_2\},\qquad N_{F_2}(Y)=\{a_2\}.         \tag{1.5}
\]

Let `phi` be the legally attained rich-side colouring with colour classes

\[
 B_1:\alpha,\qquad B_2:\beta,\qquad B_3:\gamma,
 \qquad \{c\}:\delta.                                 \tag{1.6}
\]

## 2. A rotation through the first packet bag

Consider a legal single-gate rotation with donor `F_1`.  Thus

\[
 F_1=Z\mathbin{\dot\cup}W                               \tag{2.1}
\]

where `Z,W` are nonempty connected and adjacent, `Z` meets the old centre
`s` and both old missing rows `c,r`, and `W` meets `s`.  Put

\[
 \mathcal E=\{H\in\{c,r,X,Y,F_2\}:E(W,H)=\varnothing\}.
\tag{2.2}
\]

The rotated model has centre `W` and missing-row set `mathcal E`.  Assume
throughout this section that `G` has no `K_7^-` minor.  Then

\[
 |\mathcal E|=2,qquad
 \mathcal E\cap\{c,r\}\ne\varnothing.                 \tag{2.3}
\]

The first equality holds because zero missing rows give `K_7` and one
missing row gives `K_7^-`.  For the second, if the two old and two new
missing-row sets were disjoint, the seven bags

\[
                  \{s\}\cup W,\quad Z,\quad
                  \{c\},\{r\},X,Y,F_2                 \tag{2.4}
\]

would form a `K_7^-` model: the first bag meets every fixed row using
`s` outside the old missing pair and `W` outside the new pair, while `Z`
meets all four rows in their union and can miss only the fifth row.

### Theorem 2.1 (exact anchor classification)

Every such target-free rotation satisfies:

1. `X in mathcal E` if and only if `t_1 in Z`, and
   `Y in mathcal E` if and only if `a_1 in Z`.
2. The gate `Z` cannot contain both `a_1,t_1`.
3. The gate `Z` must contain at least one anchor.  Hence, by item 2, it
   contains exactly one of `a_1,t_1`.
4. Writing `H` for the
   corresponding lobe row (`H=X` for `t_1` and `H=Y` for `a_1`),

   \[
                         \mathcal E=\{H,h\}
                         \quad\text{for some }h\in\{c,r\}.             \tag{2.5}
   \]

### Proof

Item 1 is immediate from the singleton portal identities (1.4): a row is
newly missing exactly when its entire donor portal set lies in the moved
gate.  If both anchors lay in `Z`, then `mathcal E` would contain `X,Y`;
as it has order two, it would equal `{X,Y}`, contrary to (2.3).  This
proves item 2.

If neither anchor lies in `Z`, the partition (2.1) puts all of `B_1` in
`W`, so `Z subseteq L`.  The paired state supplies an edge from `c` to
`B_1`, hence `W` meets `c`.  It also meets `F_2`, because the full packet
`Q subseteq F_2` has a neighbour at each literal vertex of `B_1`.  Item 1
gives edges from `W` to `X,Y`.  Thus among the five fixed rows `W` can
miss only `r`, contrary to `|mathcal E|=2`.  Together with item 2, this
proves item 3.

If exactly one anchor moves, item 1 puts its corresponding row `H` in
`mathcal E` and excludes the other lobe row.  The second member belongs
to `{c,r}` by (2.3), proving (2.5). \(\square\)

Thus every target-free packet-donor move transfers exactly one literal
anchor.  There is no zero-anchor rotation hidden behind an uncontrolled
loss of packet fullness.

### Theorem 2.2 (every packet rotation has an exact median)

Use Theorem 2.1.  Let `b` be the unique anchor in `Z`, let `H` be its
corresponding lobe row, and let `K` be the other lobe row.  Write

\[
                         \mathcal E=\{H,h\},\qquad
                         \{c,r\}=\{h,\bar h\}.           \tag{2.6}
\]

Then the seven literal bags

\[
                  \{s\}\cup W,\quad Z,\quad \{h\},\quad K,
                  \quad\{\bar h\},\quad H,\quad F_2     \tag{2.7}
\]

form exactly a `K_3 join C_4` model.  The `K_3` side is

\[
                         \{\bar h\},\quad H,\quad F_2,   \tag{2.8}
\]

and the cyclic order on the other four bags is

\[
                    (\{s\}\cup W)-Z-\{h\}-K-(\{s\}\cup W).
\tag{2.9}
\]

Its two absent diagonals are

\[
                    (\{s\}\cup W)\not\sim\{h\},\qquad
                    Z\not\sim K.                         \tag{2.10}
\]

### Proof

The first bag is connected because `W` meets the old centre `s`.  It is
adjacent to `Z` through the gate cut, while `Z` meets `h` because every
legal gate repairs both old missing rows `c,r`.  The lobe row `K` meets
`h`, and it meets the first bag through the unique anchor retained in
`W`.  These are the four edges in (2.9).

The first diagonal in (2.10) is absent because `W` misses `h` and `s` is
anticomplete to both `c,r`.  The second is absent because the sole
`F_1-K` portal is the retained anchor in `W`, not the moved anchor in
`Z`.

It remains to check the common triangle.  The bag `{s} union W` meets
`bar h` through `W`, meets `H` through the old `s-H` edge, and meets
`F_2` through the old `s-F_2` edge.  The gate `Z` meets `bar h` as the
other old missing row, meets `H` through its moved anchor, and meets
`F_2` because that anchor has a neighbour in the `S`-full packet
`Q subseteq F_2`.  Finally `{h}` and `K` meet all three common rows by
the old foreign-clique and complementary-lobe adjacencies.  The three
common rows are pairwise adjacent in the original near model.  Hence
every common-to-cycle edge and every common-row edge is literal, proving
the claimed `K_3 join C_4`. \(\square\)

Thus a packet rotation is not merely another missing-star model.  It has
a canonical median whose two independent repair demands are explicitly
the moved-anchor diagonal and the missing-twin diagonal.

## 3. A one-anchor change forces a Kempe lock

### Theorem 3.1 (the `c`-changing move is bichromatically locked)

Suppose `t_1 in Z`, `a_1 in W`, and

\[
                         \mathcal E=\{X,c\}.            \tag{3.1}
\]

Then `c,t_1,a_1` lie in one `alpha-delta` Kempe component of `phi`.

Symmetrically, if `a_1 in Z`, `t_1 in W`, and
`mathcal E={Y,c}`, the same three vertices lie in one
`alpha-delta` Kempe component.

### Proof

Consider the first orientation.  Since `W` is anticomplete to `c` and
contains `a_1`, the edge `ca_1` is absent.  The paired-state edge from `c`
to `B_1` is therefore `ct_1`.  Hence `c,t_1` already lie in one
`alpha-delta` Kempe component.

Suppose this component misses `a_1`, and swap `alpha,delta` on it.  The
new rich-side colouring has exact boundary partition

\[
             \Sigma=\{\{c,a_1\},\{t_1\},B_2,B_3\}.     \tag{3.2}
\]

The following four disjoint connected sets form a literal `K_4` indexed
by the four blocks of `Sigma`:

\[
       Y\cup\{c,a_1\},\qquad \{t_1\},\qquad
       Q\cup B_2,\qquad X\cup B_3.                     \tag{3.3}
\]

For completeness, `X-Y` gives the first--fourth adjacency; fullness of
`Q` gives every adjacency incident with the third set not already supplied
by a boundary vertex; and the three adjacencies incident with `{t_1}` are
witnessed respectively by `ct_1`, a `Q-t_1` edge, and a `D-t_1` edge.
The remaining first--third and third--fourth pairs are also supplied by
fullness of `Q`.

Contract the three nonsingleton representatives in (3.3).  This is a
proper minor operation supported in the rich shore, with the nonempty thin
shore untouched.  Its six-colouring restricts to the original closed thin
shore with exact boundary state `Sigma`, because the four representatives
form a clique.  The Kempe-swapped colouring supplies the same exact state
on the rich closed shore.  Aligning palettes and gluing gives a
six-colouring of `G`, a contradiction.  Thus the component also contains
`a_1`.

The second orientation is obtained by interchanging `a_1,t_1` and
`X,Y`. \(\square\)

The previously audited complementary-lock Kempe lemma already puts
`a_1,t_1` in one `alpha-gamma` component.  Hence a rotation which changes
the persistent missing twin from `r` to `c` is simultaneously locked in
the two colour pairs `alpha-gamma` and `alpha-delta`; it is not a free
model-local pivot.

## 4. Symmetric second-packet statement

Replacing

\[
 (F_1,B_1,a_1,t_1,\alpha,F_2)
 \quad\text{by}\quad
 (F_2,B_2,a_2,t_2,\beta,F_1)                           \tag{4.1}
\]

gives the identical conclusions.  In particular every target-free rotation
through `F_2` transfers exactly one of `a_2,t_2`, while a rotation which
changes to `c` forces `c,a_2,t_2` into one
`beta-delta` Kempe component.

## 5. Exact remaining obstruction

The theorem does not claim that `W` still contains an `S`-full packet.
That assertion is false from the model data alone: the seven packet
contacts can be divided between `Z` and `W`.  What the theorem forces is
an exact one-anchor move.  Twin drift through `c` pays for a named
three-terminal Kempe component.  Closing the rotation component now
requires composing that Kempe lock with the gate connector, or showing
that all such locked one-anchor moves have one coherent two-apex
realization.
