# Constant-owner corridors in a lex-minimal `K_7^vee` source

## Status

This note closes the block--cutvertex part of the arbitrary-model rooting
problem.  A constant monopoly interval is not an arbitrary sequence of
blocks: it is an induced path of bridge blocks, with no source-bag branch
off the path.  In a minor-minimal non-six-colourable host, every internal
edge of that path carries at least three externally started and externally
ended Kempe detours in one contraction colouring.  Every finite interval
of the path is either behind an exact seven-boundary or has actual ambient
boundary of order at least eight.

These statements remove arbitrary source-bag SPQR geometry.  They do not
finish the rooting step.  The colours of the three detours are palette
colours, not labels of the six other branch bags.  The family in Section 5
shows that a constant owner set and repeated proper edge-operation states
can coexist along an arbitrarily long corridor.  Thus the remaining
theorem must use seven-connectivity together with target-freeness to align
an external Kempe packet with literal model labels (or make all such
packets one coherent two-apex society).

## 1. Exact nested-lobe convention

Use the ordered labelled model and notation of
`../results/hc7_near_k7_literal_rooting_bridge.md`.  In particular, for a required
label `j`, let

\[
 P_j=\{u\in U_1: u\hbox{ is the }U_1\hbox{-end of a }U_1V_j
                    \hbox{ edge}\}.
\tag{1.1}
\]

Every `P_j` is nonempty.  If `c` is a cutvertex of `G[U_1]`, an **open
descendant lobe at `c`** is a component `X` of `G[U_1]-c`, after a root
of the block--cutvertex tree has been fixed.  It is detachable: `X` and
`U_1-X` are connected.  Its monopoly set is exactly

\[
                         \Omega(X)=\{j:P_j\subseteq X\}. \tag{1.2}
\]

Let

\[
             X_0\supsetneq X_1\supsetneq\cdots\supsetneq X_m
\tag{1.3}
\]

be consecutive open descendant lobes on one root--leaf chain.  Thus
`X_i-X_{i+1}` is the part traversed between two consecutive cutvertex
nodes of the chain, including all side branches met there.  Call (1.3) a
**constant-owner interval** when

\[
                   \Omega(X_0)=\cdots=\Omega(X_m)=M.    \tag{1.4}
\]

The source theorem gives `|M|>=2`.

## 2. Constancy forces a literal bridge path

### Theorem 2.1 (constant-block collapse)

In a constant-owner interval (1.3), every block between two consecutive
cutvertices is the single bridge edge joining them.  No intermediate
cutvertex has a component of `G[U_1]` off the displayed chain.

Consequently the vertices traversed by the interval induce a path in
`G[U_1]`.  Every strictly internal vertex of this path has precisely its
two path neighbours in `U_1` and has no neighbour in any owner bag
`V_j`, `j in M`.

#### Proof

Let `B` be a block between consecutive cutvertices `c,d`, with `c` on
the root side.  The vertices of `B-{c}` lie in the larger descendant lobe
and all vertices of `B-{c,d}` lie outside the smaller one.

First suppose `u in B-{c,d}` is not a cutvertex of `G[U_1]`.  Then
`{u}` is detachable: deleting a noncut vertex from the nonseparable block
leaves the block connected, and all other blocks remain attached through
their old cutvertices.  The ordered-source theorem gives
`|Omega({u})|>=2`.  For every `j in Omega({u})`, (1.1) gives
`P_j={u}`.  Hence `j` belongs to the monopoly set of the larger lobe and
not to that of the smaller lobe, contradicting (1.4).

If a third vertex `u in B-{c,d}` is a cutvertex, it has a component `K`
off the block-chain.  This component is detachable, so
`|Omega(K)|>=2`.  It lies in the larger lobe and is disjoint from the
smaller lobe.  Therefore every label in `Omega(K)` again belongs to the
larger monopoly set and not the smaller one, the same contradiction.
Thus `B` has only `c,d`.  In a simple graph it is the bridge `cd`.

The identical side-component argument at an intermediate chain
cutvertex excludes every off-chain component.  A chord between
nonconsecutive chain vertices would put the intervening edges in a
nonseparable block, already excluded.  The traversed subgraph is
therefore an induced bridge path.

Finally, if an internal path vertex `u` had a neighbour in `V_j` for
some `j in M`, then `u in P_j`.  But the two consecutive constant lobes
on the two sides of `u` put `P_j` wholly in the deeper lobe while `u`
lies outside it, a contradiction.  Hence no owner bag meets an internal
path vertex.  The degree statement inside `U_1` was proved above.  QED.

### Corollary 2.2 (all source events are bounded)

Along a root--leaf chain there are at most five monopoly changes.  Between
those changes the source bag is a bridge path.  Thus all nontrivial block
geometry and all source-bag branching occur at a bounded number of event
nodes; only subdivisions of the bridge paths can be unbounded.

This is stronger than a bounded-leaf portal-tree statement: arbitrary
SPQR length inside a constant interval is impossible.

## 3. Actual adhesions and the exact-seven exit

### Theorem 3.1 (interval gate dichotomy)

Let `I` be a nonempty consecutive set of strictly internal vertices of a
constant-owner path.  Then `G[I]` is connected and

\[
                              |N_G(I)|\ge7.              \tag{3.1}
\]

If equality holds, `N_G(I)` is an actual exact seven-boundary separating
`I` from every owner bag `V_j`, `j in M`.  Deletions and contractions
supported inside `I`, and operations supported in an opposite open shore,
are faithful relative to this boundary; equal marked boundary states
would cross-splice to a six-colouring.

#### Proof

Theorem 2.1 makes `I` connected and anticomplete to every owner bag.
Choose `j in M` and a vertex of the nonempty bag `V_j`.  It lies outside
`I union N_G(I)`.  Hence `N_G(I)` genuinely separates `I` from a
nonempty opposite side.  Seven-connectivity gives (3.1).  At equality it
is an exact seven-cut.  The faithful-operation and crossed-splicing
statement is the standard opposite-shore theorem applied to this actual
separation.  QED.

Thus a constant corridor either descends through an exact seven-adhesion,
or every one of its internal intervals has ambient gate order at least
eight.  Label ownership by itself gives no upper bound on that gate.

## 4. The operation packet on every corridor edge

Assume now that `G` is minor-minimal non-six-colourable.  Hence, for every
edge `xy`, a six-colouring of `G/xy` expands to a colouring of `G-xy` in
which `x,y` have one colour.

### Theorem 4.1 (three external palette layers)

Let `xy` be an internal edge of a constant-owner path, with path
neighbours `x^-` and `y^+` on its two outer sides.  In any six-colouring
`c` of `G-xy`, put

\[
                            c(x)=c(y)=\alpha.             \tag{4.1}
\]

There are at least three distinct colours `beta != alpha` such that the
`{alpha,beta}`-component containing `x,y` contains an `x-y` path whose
first edge at `x` and last edge at `y` leave `U_1`.

For an edge at an end of the constant interval, the same count is at
least four when only one outer source neighbour is present.

#### Proof

For every `beta != alpha`, the vertices `x,y` lie in the same
`{alpha,beta}`-component.  Otherwise switching the component of one end
makes their colours different and restores `xy`, producing a
six-colouring of `G`.

By Theorem 2.1, after `xy` is deleted the only neighbour of `x` in
`U_1` is `x^-`, and the only neighbour of `y` in `U_1` is `y^+`.
Exclude from the five colours different from `alpha` the at most two
colours `c(x^-)` and `c(y^+)`.  For every remaining colour `beta`, an
`alpha-beta` path cannot take its first edge through `x^-` or its last
edge through `y^+`.  It therefore starts and ends outside `U_1`.
At least `5-2=3` colours remain.  With only one outer source neighbour,
at most one colour is excluded.  QED.

The theorem deliberately says nothing about the middle of these paths.
It may re-enter the two sides of `U_1`, and paths belonging to different
colours may share `alpha`-coloured vertices.  Seven-connectivity also
gives six internally disjoint alternatives to the bridge edge, but their
interiors likewise need not avoid `U_1`.  Each alternative contains a
subpath whose interior avoids `U_1` and whose ends lie on opposite bridge
sides (allowing `x` or `y` as an end), but the truncated subpaths need not
have distinct ends.  This is not a six-linkage of outside rooted paths.

### Corollary 4.2 (the exact active-face input still missing)

The only obstruction after Theorems 2.1--4.1 is **label alignment**.
If four of the external layers can be replaced by four disjoint fixed
extensions with the required literal pool/reserve contacts, the
fixed-extension active-face theorem gives a labelled `K_7` or one common
rural face.  Off-face failure localizes in a shared lobe, and the
shared-lobe theorem gives a split, a nested exact seven-cut, an exact
order-eight two-gate, or one active torso.

The operation colours in Theorem 4.1 are not, however, automatically the
six branch-bag labels.  A connected branch bag need not be monochromatic
in a colouring of `G-xy`.  This prevents an unconditional invocation of
the active-face theorem and is the remaining boundary-faithful lift.

## 5. A sharp arbitrary-length state counterarchitecture

The next construction shows why repeating edge states do not by
themselves pump the corridor.

Fix `m>=2`.  Let

\[
 C=\{a,b_1,b_2,b_3,b_4,b_5\}
\]

be a clique and let `T=x_0x_1...x_{2m-1}` be a path.  Add a clique
`S={s_1,...,s_5}`.  Join every `s_i` to every vertex of `C` except
`b_i`.  Add a vertex `v`, join it to every vertex of `C` except `b_1`,
and add exactly the model edges

\[
 vs_3,vs_4,vs_5,\quad vx_0,vx_{2m-1},\quad
 x_0s_1,x_0s_2,\quad x_{2m-1}s_3,x_{2m-1}s_4,x_{2m-1}s_5. \tag{5.1}
\]

For each required pair `(k,i)` below add a shadow vertex `y_{k,i}`,
join it to `x_k`, and join it to every vertex of `C` except `b_i`:

\[
\begin{array}{c|c}
k& i\\ \hline
0&3,4,5\\
1\le k\le2m-2&2,3,4,5\\
2m-1&2\\
\end{array}                                               \tag{5.2}
\]

There are no other edges.

### Proposition 5.1 (constant owners plus repeated operations)

The graph just constructed has the following properties.

1. It is not six-colourable.
2. For every path edge `e`, both `G-e` and `G/e` are six-colourable.
   All vertices outside `T` receive the same colours in these transition
   states; the colour on the contracted edge merely alternates between
   two values with the parity of `e`.
3. The bags
   
   \[
       A=\{v\},\ B=\{s_1\},\ C'=\{s_2\},\
       U_1=T,\ U_2=\{s_3\},\ U_3=\{s_4\},\ U_4=\{s_5\}
   \]
   form an exact labelled `K_7^vee` model with deficient pairs `AB,AC'`.
4. With the other six bags held fixed, `T` is inclusion-minimal.  Every
   detachable prefix owns exactly `{s_1,s_2}`, every detachable suffix
   owns exactly `{s_3,s_4,s_5}`, and the `v`-portal occurs at both ends.
   Thus the whole arbitrary-length middle is a constant multi-owner
   corridor satisfying the zero-or-two lex ownership rule.

#### Proof

In any six-colouring the clique `C` uses all colours.  Rename them so
that `a` has colour `alpha` and `b_i` has colour `p_i`.  Each `s_i` and
each `y_{k,i}` is forced to `p_i`, while `v` is forced to `p_1`.
The external neighbours of `x_0` force its list to `{alpha}`; those of
`x_{2m-1}` do the same; and every internal path vertex has precisely
`{alpha,p_1}` available.  Alternation on a path with `2m` vertices cannot
give `alpha` to both ends.  This proves item 1.

Delete `x_kx_{k+1}`.  Starting with `alpha` at each outside end, alternate
`alpha,p_1` independently on the two path components.  The two ends of
the deleted edge receive the same colour: `alpha` when `k` is even and
`p_1` when `k` is odd.  All outside colours remain the forced colours
above.  This colours `G-e`; identifying the equally coloured ends colours
`G/e`.  Item 2 follows.

The model assertions follow immediately from (5.1) and the clique on
`S`.  Its only missing displayed pairs are `vs_1,vs_2`.  Finally the
portal sets in `T` are

\[
 P_{s_1}=P_{s_2}=\{x_0\},\quad
 P_{s_3}=P_{s_4}=P_{s_5}=\{x_{2m-1}\},\quad
 P_v=\{x_0,x_{2m-1}\}.
\]

Any connected subpath retaining all six required labels contains both
ends and hence equals `T`.  The detachable proper connected subsets of a
path are its prefixes and suffixes, giving item 4.  QED.

This family is intentionally not seven-connected, target-free, or
minor-minimal; its forcing part in fact supplies other clique-minor
routes.  It therefore does not refute the desired `HC_7` theorem.  It
does prove that the following data are insufficient even at arbitrary
length:

\[
 \boxed{\text{constant multi-owner sets + fixed outside edge states
          + equality of every corridor-edge operation state}.}
\]

The missing hypothesis cannot be another finite state count.  It must
turn seven-connected external routing into literal labelled extensions,
or prove that every such routing has one coherent two-apex embedding.

## 6. The spanning sole-complex subcell

There is one useful unconditional elimination.  Suppose the selected
lex-minimal model is already spanning and `U_1` is its only nonsingleton
bag.  Delete the singleton deficient centre `A`.  The remaining graph is
six-connected and consists of the complex bag `U_1` and the five
singleton clique bags

\[
                         B,C,U_2,U_3,U_4.
\]

If there is no `K_7` minor, the spanning-singleton core theorem says that
`U_1` is two-connected and each of the five singleton portal classes has
at least two vertices.  Corollary 2.4 of the literal-rooting note says
that a nonsingleton two-connected lex source is a triangle and every one
of all six portal classes is concentrated at one triangle vertex.  This
contradicts the five portal multiplicities.  Hence in this spanning
sole-complex subcell `U_1` is a singleton (or `K_7` already exists).

The word **spanning** is essential.  For a nonspanning lex model, absorb
all unused components into `U_1` and the spanning-singleton theorem makes
the enlarged remainder two-connected, but the new bypass vertices may
supply the second portals.  It does not make the original lex source
two-connected and does not contradict its constant corridor.  What it
does prove is that every such nonspanning corridor lies in a
two-connected ear closure; its missing pump is precisely the faithful
alignment of those ears with the original six labels.

## 7. Exact residual theorem

After this note, the arbitrary-model rooting gap has the following
uniform form.

* The source block tree has a bounded event kernel joined by induced
  bridge paths.
* Every internal interval either descends through an exact seven-boundary
  or has gate order at least eight.
* Every internal edge has a three-colour external Kempe packet.
* If four literal private extensions can be selected from those packets,
  active-face occurrence closure gives `K_7` or a coherent rural
  two-apex structure.
* Repeated palette states alone do not select those literal extensions.

Thus the needed pumping statement is now sharply label-sensitive:

> **Corridor label-alignment theorem.**  In a seven-connected,
> minor-minimal non-six-colourable, `K_7`-minor-free host, a gate-rich
> constant-owner bridge corridor either supplies four disjoint extensions
> carrying the prescribed model-label rows, or all of its external Kempe
> packets and their active torso occurrences have one compatible rural
> expansion after deleting the same two vertices.

This is strictly narrower than arbitrary `K_7^vee` rooting and cannot be
replaced by a finite equality-state pigeonhole.

## 8. Nonspanning ears collapse to exact seven or one torso

The nonspanning qualification in Section 6 does not leave an arbitrary
ear chain in the sole-complex cell.  The six literal shell vertices make
every internal two-gate an order-seven/eight boundary.

### Theorem 8.1 (literal-row ear collapse)

Let `G` be seven-connected and `K_7`-minor-free.  Suppose

\[
                         L=\{v,b_1,b_2,b_3,b_4,b_5\}    \tag{8.1}
\]

are the six singleton bags of a `K_7^vee` model, with the `b_i` forming
a clique.  Assume this is the exact shell: `v` is adjacent to precisely
three of the `b_i` and nonadjacent to the other two.  Put

\[
                         B^*=G-L.                        \tag{8.2}
\]

Assume `B^*` is the sole complex spanning bag; equivalently it is
connected and is adjacent to every member of `L`.  Then `B^*` is
two-connected.  Moreover at least one of the following holds.

1. A nonempty proper shore inside `B^*` has an actual exact
   seven-boundary in `G`.
2. `B^*` is three-connected.

More precisely, if `Z` is a two-cut of `B^*` and `D` is a component of
`B^*-Z`, put `Z_D=N_{B^*}(D)`.  Then

\[
 N_G(D)=Z_D\mathbin{\dot\cup}N_L(D),\qquad
 |Z_D|\le2,\qquad |N_G(D)|\ge7.                         \tag{8.3}
\]

Thus either `|N_G(D)|=7`, or

\[
                  Z_D=Z,\qquad N_L(D)=L,                \tag{8.4}
\]

and `D` is a full exact-order-eight two-gate lobe.  For one fixed
two-cut, two components satisfying (8.4) already give a `K_7` model.

#### Proof

Delete the deficient singleton `v`.  The graph `G-v` is six-connected
and consists of `B^*` and the five-singleton clique.  The
spanning-singleton cutvertex theorem makes `B^*` two-connected (otherwise
it directly supplies `K_7`).

Also `|B^*|>=4`: seven-connectivity gives `d_G(v)>=7`, while the exact
shell supplies only three neighbours of `v` among the `b_i`.  Hence `v`
has at least four distinct neighbours in `B^*`.

Let `Z,D,Z_D` be as in the statement.  There is another component of
`B^*-Z`, so `N_G(D)` is an actual separator.  Every neighbour of `D`
outside `B^*` lies in the six-vertex set `L`; hence (8.3), and
seven-connectivity gives its lower bound.  The right side of (8.3) has
order at most eight.  If its order is not seven, equality at eight forces
both gate vertices and all six literal rows, which is (8.4).

Suppose two components `D_1,D_2` at `Z` satisfy (8.4).  The seven sets

\[
             D_1\cup\{v\},\quad D_2,\quad
             \{b_1\},\ldots,\{b_5\}                   \tag{8.5}
\]

are connected and pairwise adjacent.  Indeed `D_2` sees `v`, each `D_i`
sees every `b_j`, and the `b_j` form a clique.  They are a `K_7` model,
contrary to the hypothesis.  Therefore every two-cut has a component
with boundary exactly seven.  If outcome 1 is absent, no two-cut exists;
together with two-connectivity this is outcome 2.  QED.

### Corollary 8.2 (the ear-chain pumping theorem)

In the sole-complex nonspanning cell, enlarge the old lex source `U_1` to
`B^*=G-L`.  Every old constant-owner bridge corridor lies in this
two-connected ear closure.  Apply Theorem 8.1 recursively to its Tutte
decomposition.  Then either

1. the corridor enters a nested exact-seven shore, where faithful
   proper-minor state descent applies; or
2. all of its nonspanning bypass ears are contained in one
   three-connected torso of `B^*`.

There is no third possibility consisting of an unbounded chain of
full two-gate ears: at the first two-cut exposing two such components,
(8.5) is the target minor.  In outcome 2, if the torso is planar or
four-connected, the remaining occurrences are governed by active-face
closure: a rooted literal extension conflict gives `K_7`, while
compatible rural occurrences give the coherent two-apex alternative.
For a merely three-connected nonplanar torso, the rooted-occurrence
exchange remains an additional local input.  In either case arbitrary
ear length and arbitrary block-cut length have disappeared; the unproved
selection is confined to one torso and is the same literal four-extension
alignment isolated in Corollary 4.2.

### Theorem 8.3 (three-cuts expose exact seven/eight lobes)

Retain the hypotheses and notation of Theorem 8.1, and suppose that
`B^*` is three-connected.  Then at least one of the following holds.

1. A nonempty proper shore inside `B^*` has an actual boundary of order
   seven or eight in `G`.
2. `B^*` is four-connected.

More precisely, for every three-cut `Z` of `B^*` there is a component
`D` of `B^*-Z` with

\[
                         7\le |N_G(D)|\le8.             \tag{8.6}
\]

#### Proof

For a component `D` of `B^*-Z`, put
`Z_D=N_{B^*}(D)`.  As in (8.3), the displayed six-label shell accounts
for every neighbour outside `B^*`, so

\[
 N_G(D)=Z_D\mathbin{\dot\cup}N_L(D),\qquad
 |Z_D|\le3,\qquad |N_L(D)|\le6.                      \tag{8.7}
\]

This is a genuine separator because another component of `B^*-Z`
remains.  Seven-connectivity therefore gives `|N_G(D)|>=7`.  If a
component fails (8.6), equality in both upper bounds of (8.7) is forced:

\[
                         Z_D=Z,\qquad N_L(D)=L,          \tag{8.8}
\]

and its boundary has order nine.

There cannot be two components `D_1,D_2` satisfying (8.8).  If there
were, the seven branch sets

\[
             D_1\cup\{v\},\quad D_2,\quad
             \{b_1\},\ldots,\{b_5\}                  \tag{8.9}
\]

would be pairwise adjacent: both components see every literal shell
vertex, `D_1 union {v}` is connected, and the five `b_i` form a clique.
Thus (8.9) is a `K_7` model.  Every three-cut has at least two components,
so at least one of them satisfies (8.6).  If outcome 1 is absent, no
three-cut exists.  When `|B^*|>=5`, three-connectivity then strengthens
to four-connectivity.

It remains to exclude `B^* congruent K_4`.  Every `d in B^*` has its
three neighbours in `B^*`, and minimum degree seven forces at least four
neighbours in the six-vertex shell `L`.  If some `d` is not full to `L`,
then `N_G(d)` has order seven or eight and separates `d` from a missed
shell label, giving outcome 1.  Otherwise all four vertices of `B^*` are
full to `L`.  The vertex `v` has only three neighbours among the `b_i`
and minimum degree at least seven, so it is adjacent to all four vertices
of `B^*`.  The seven bags

\[
 \{b_1\},\ldots,\{b_5\},\quad \{d_1\},\quad
 \{v,d_2,d_3,d_4\}
\]

then form a `K_7` model.  Thus the four-vertex exception is impossible,
and outcome 2 follows.  QED.

### Corollary 8.4 (the nonplanar torso is no longer untyped)

In outcome 2 of Corollary 8.2, refine the single three-connected torso at
its three-cuts.  Either a literal exact-seven/eight lobe appears, or the
remaining active torso is four-connected.  In the latter case the
active-root theorem applies without a planarity assumption: a feasible
active quadruple has a rooted `K_4` (and hence the labelled `K_7`), or the
torso is planar and all active occurrences lie on one coherent face.

Thus the arbitrary-model rooting route has no residual consisting merely
of an unspecified three-connected nonplanar torso.  Its only unclosed
local objects are exact order-seven/eight lobes, loss of active-role
feasibility, or the already explicit coherent rural/two-apex branch.
