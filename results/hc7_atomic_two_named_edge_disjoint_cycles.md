# Two disjoint named edges lie on disjoint literal cycles

**Status:** proved and independently audited.

This is a global linkage theorem for the active twin-seam exchange.  It
eliminates a crossless/web obstruction for the two named edges, but it does
not by itself transport an exact colouring state or split a labelled model
row.

## 1. Statement

### Theorem 1.1 (two named-edge disjoint cycles)

Let `G` be a finite simple seven-connected graph, and let

\[
                  e=zu,\qquad f=dt
\]

be vertex-disjoint edges.  Then `G-{e,f}` contains vertex-disjoint paths

\[
                  P_e:z\longrightarrow u,
        \qquad    P_f:d\longrightarrow t.              \tag{1.1}
\]

Consequently

\[
                         P_e+e,\qquad P_f+f             \tag{1.2}
\]

are vertex-disjoint literal cycles of `G`, the first containing `e` and the
second containing `f`.

### Theorem 1.2 (rooted four-pole core)

Under the same hypotheses, `G-{e,f}` contains a literal `K_4` minor rooted
at `z,u,d,t`: there are pairwise disjoint connected subgraphs

\[
                         B_z,B_u,B_d,B_t              \tag{1.3}
\]

of `G-{e,f}`, containing their indicated roots, such that every two of the
four subgraphs are adjacent.

This is a single simultaneous label-preserving certificate, stronger than
one prescribed two-linkage.  In particular all four branch labels are
preserved; no palette colour is being interpreted as a root label.  No
comparison with the collection of all three possible linkages is needed.

### HC7 specialization

In the atomic twin seam the four vertices `z,u,d,t` are distinct:

* `z in E`;
* `u in B_0 subseteq S`;
* `d in D`; and
* `t in Z={p,q}`.

Thus Theorem 1.1 applies to the compulsory edge `e=zu` and every named
lobe--gate edge `f=dt`.  In particular, at the unrestricted literal level,
the response-matched gate-edge-bypass branch has one **simultaneous
vertex-disjoint pair** avoiding both named edges.  The paths supplied here
need not lie in the prescribed lock layers or shores.

## 2. Edge deletion loses at most one unit of vertex connectivity

### Lemma 2.1

If `J` is `k`-connected, `k>=2`, and `xy in E(J)`, then `J-xy` is
`(k-1)`-connected.

### Proof

Suppose to the contrary that a set `X`, with `|X|<=k-2`, disconnects
`J-xy`.  Since `J-X` is connected, neither `x` nor `y` belongs to `X`, the
vertices `x,y` lie in different components of `(J-xy)-X`, and adding the
single edge `xy` joins all those components.  Hence there are exactly two
components, say `A` containing `x` and `B` containing `y`.

Neither component is a singleton.  Indeed, if `A={x}`, then

\[
                         N_J(x)\subseteq X\cup\{y\},
\]

so `d_J(x)<=|X|+1<=k-1`, contrary to the minimum-degree consequence of
`k`-connectivity.  The same argument applies to `B`.

Now `X union {x}` has order at most `k-1`, and its deletion from `J`
leaves the two nonempty anticomplete sets `A-{x}` and `B`.  This contradicts
`k`-connectivity.  Therefore no such `X` exists.  \(\square\)

Applying Lemma 2.1 twice gives

\[
                         \kappa(G-\{e,f\})\ge5.          \tag{2.1}
\]

The second application is legitimate whether or not the two edges are
adjacent; in Theorem 1.1 they are disjoint for the later degree count and
the four prescribed linkage terminals.

## 3. The double-edge deletion is nonplanar

Put

\[
                              H=G-\{e,f\},
          \qquad             n=|V(G)|.
\]

Seven-connectivity gives `delta(G)>=7`.  Because `e,f` are
vertex-disjoint, their four ends lose one incident edge each, and no other
vertex loses an edge.  Hence

\[
 \sum_{v\in V(H)}d_H(v)
       \ge 4\cdot6+(n-4)\cdot7
       =7n-4.                                           \tag{3.1}
\]

A finite simple planar graph of order `n>=3` has degree sum at most
`6n-12`.  Since `7n-4>6n-12`, formula (3.1) proves that `H` is nonplanar.

## 4. Jung's linkage theorem completes the proof

Jung's four-terminal theorem says that a four-connected nonplanar graph is
two-linked.  In the exact prescribed-terminal form used here: for any four
distinct vertices `x_1,x_2,y_1,y_2`, there are vertex-disjoint paths joining
`x_i` to `y_i`, `i=1,2`.  A primary-source formulation is Corollary 1 of
Carsten Thomassen, *2-Linked Graphs*, European Journal of Combinatorics 1
(1980), 371--378, doi:10.1016/S0195-6698(80)80039-4, which attributes the
corollary to Jung.  The original
source is H. A. Jung, *Eine Verallgemeinerung des n-fachen Zusammenhangs
fuer Graphen*, Mathematische Annalen 187 (1970), 95--103,
doi:10.1007/BF01350174.

By (2.1), `H` is five-connected and hence four-connected; by Section 3 it
is nonplanar.  Apply Jung's theorem in `H` to the ordered terminal pairs

\[
                             (z,u),\qquad(d,t).
\]

It gives the paths in (1.1).  They avoid `e,f` because those edges are
absent from `H`, and adding the corresponding named edge to each path gives
the two disjoint cycles in (1.2).  This proves Theorem 1.1.  \(\square\)

For Theorem 1.2 use the rooted `K_4` theorem of R. Fabila-Monroy and
D. R. Wood, *Rooted K4-Minors*, Electronic Journal of Combinatorics 20(2)
(2013), #P64, doi:10.37236/3476.  One of its stated special cases is that a
four-connected nonplanar graph contains a `K_4` minor rooted at any four
prescribed vertices.  The graph `H` is four-connected and nonplanar by
Sections 2--3, so applying that theorem to `z,u,d,t` produces (1.3).
\(\square\)

## 5. Coupling to the response-matched bypass branch

Let `phi` be a six-colouring of `G-e`, let `alpha` be the common colour of
`z,u`, and let `c_f` be a six-colouring of `G-f`.  Align its palette so that
`c_f(z)=alpha`, and put

\[
               \beta=c_f(u),\qquad \gamma=c_f(d)=c_f(t).
\]

Then `beta ne alpha`.  Assume that `f` is eligible in the
`alpha-beta` compulsory lock of `phi` and that deleting `f` leaves a
literal `z-u` bypass in that lock.  The following response facts coexist:

1. For every one of the five colours `epsilon ne gamma`, the
   `gamma-epsilon` graph of `c_f` contains a `d-t` path.  Distinct such
   paths meet away from `d,t` only at `gamma`-coloured vertices.
2. At most one of these five paths can use `e`; hence at least four avoid
   both `e` and `f`.
3. Let `U` be the spanning subgraph of `G-f` with
   \[
      E(U)=\{xy\in E(G-f):\gamma\in\{c_f(x),c_f(y)\}\}.
   \]
   Equivalently, `U` is the full union of the five
   `gamma-epsilon` layers.  Vertex Menger gives either two internally
   disjoint `d-t` paths in `U`, or one internal `gamma`-coloured vertex
   `w` meeting every `d-t` path in every layer.
4. In the second outcome, seven-connectivity gives five internally
   disjoint `d-t` paths in `G-f` avoiding `w`, each containing an edge with
   neither end coloured `gamma`; four can additionally be chosen to avoid
   `e`.

For item 1, a Kempe swap of the component containing `d` would restore
`f` and six-colour `G` unless it also contains `t`.  Item 2 follows because
one edge has only one unordered endpoint-colour pair.  Item 3 is Menger;
the common vertex has colour in
`intersection_{epsilon ne gamma}{gamma,epsilon}={gamma}`.  For item 4,
the fan argument used in the audited separating response bundle gives six
internally disjoint `d-t` paths in `G-f`; at most one uses `w` and at most
one further path uses `e`.  A `w`-avoiding path cannot lie in `U`, and an
edge is outside `U` precisely when neither end has colour `gamma`.

Theorems 1.1--1.2 are stronger at the uncoloured literal level: regardless
of how these five layers overlap the selected `z-u` lock bypass, there is
some simultaneous disjoint pair `P_e,P_f`, and indeed a four-pole rooted
`K_4` model, in the common edge-deleted host.

## 6. Exact scope

These theorems close the **unrestricted common-host crossless geometric**
branch.  A two-paths web cannot be the terminal obstruction for the named
edge pair in the whole common edge-deleted graph: that graph is already
nonplanar and two-linked.  This does not close a web obstruction inside a
prescribed colour layer, shore, or duty-carrying subgraph.

They do **not** prove that `P_e` is an `alpha-beta` Kempe path, that `P_f`
lies in one `gamma-epsilon` layer, or that either path carries a literal
boundary/model-row duty.  The Jung linkage may use mixed colours and may
cross both twin shores.  Therefore (1.2) is not yet:

* a common exact boundary state;
* a labelled carrier split;
* a literal `K_7` model;
* a fixed-pair terminal; or
* a strict noncycling `S1/S4` handoff.

The rooted `K_4` bags in (1.3) also need not meet the old seven-boundary or
the rows of a regenerated `K_6` model in prescribed places.  The remaining
bypass obligation is consequently narrower and genuinely stateful: decode
the rooted four-pole core jointly with the two proper-minor response states.
Further work must prove confluence of those states, extend the rooted core
to a duty-faithful row/carrier split, or produce a ranked handoff.  The
present theorem must not be cited as that missing decoder.

## 7. What the rooted core already allocates across the twins

The rooted model does give one label-faithful separator fact which is useful
for the next step.

### Lemma 7.1 (clique-model separator allocation)

Let `V(J)=X dotunion Omega dotunion Y`, with no `X-Y` edge, and let
`M_1,...,M_r` be a clique-minor model in `J`.  The model bags which avoid
`Omega` cannot occur in both open shores.  Equivalently, all
boundary-avoiding bags lie in at most one of `X,Y`.

### Proof

A connected bag avoiding `Omega` lies wholly in `X` or wholly in `Y`.
If two such bags lay on opposite shores, there could be no edge between
them, contradicting pairwise adjacency of the clique-model bags.
\(\square\)

Apply this to the rooted core `(B_z,B_u,B_d,B_t)`.

* Across `Omega_D`, the bag `B_t` meets the boundary.  If `B_d` avoids
  it, then both `B_z` and `B_u` must meet it, because `d in D` while
  `z,u in B_D`.  Thus either `B_d,B_t` meet `Omega_D`, or
  `B_z,B_u,B_t` do.
* Across `Omega_E`, the bags `B_u,B_t` meet the boundary through their
  literal roots.  Since `z in E` and `d in B_E`, at least one of
  `B_z,B_d` also meets `Omega_E`.  Hence at least three rooted bags meet
  that twin boundary.

These are literal bag--boundary incidences, not palette assignments.  The
precise next allocation lemma is now narrower: promote the guaranteed
three-bag contact on `Omega_E` (or the complementary two/three pattern on
`Omega_D`) to one of

1. a fourth boundary-contacting rooted bag together with the two unused
   packet duties needed for a near-`K_7`/`K_7` extension;
2. an exact-state confluence across that same literal twin; or
3. an actual smaller state-carrying receiver with a declared noncycling
   rank.

Lemma 7.1 alone supplies none of these three promotions.  It is the exact
rooted-core allocation input, not the missing allocation theorem.
