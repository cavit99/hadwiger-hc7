# Exact-seven two-connected lobe funnel

## 1. Frozen setting

Assume the audited exact-seven `(1,3)` setting

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad |S|=7,
\]

where `G` is seven-connected and strongly seven-contraction-critical,
there are no `LR` edges, `R` contains three pairwise disjoint connected
`S`-full packets, `G[S]` is triangle-free, and `G[L]` is
three-connected.  Let `T={t_1,t_2,t_3}` be a three-cut of `G[L]`, and
let `J,K` be the two components of `G[L]-T`.  Assume that `J` is
two-connected.

This note gives a uniform funnel for the genuinely two-connected lobe.
It has two independent parts.

1. Seven-connectivity forces four *distinct literal first hits* of `S`
   in `J`.  A rooted `K_4` on any such four hits is already a literal
   `K_7` after adjoining the three opposite packets.  Thus every
   four-hit basis in a survivor lies in one of the six exact rooted-
   `K_4` obstruction classes of Fabila-Monroy--Wood.
2. A bipolar ordering of `J` turns every possible complementary gate
   split into two monotone literal contact capacities.  Overlap of the
   two capacity intervals gives three spanning clique carriers, so the
   audited boundary trichotomy closes.  Failure is one exact crossed
   capacity interval in every bipolar ordering.

Neither conclusion uses a virtual web edge as a literal edge.  The last
crossed interval is not by itself asserted to be a two-vertex apex set.

## 2. Four literal first hits in every lobe

For `s in S`, put

\[
                         P_s=N_J(s).
\]

Call a set of vertices of `J` independent if it can be matched to the
same number of distinct literal labels of `S` in the incidence graph
`s x` precisely when `x in P_s`.

### Lemma 2.1 (lobe portal rank)

If `|J|>=4`, the literal portal-incidence graph between `S` and `J` has
matching number at least four.

#### Proof

Suppose its matching number is at most three.  By Koenig's theorem it
has a vertex cover

\[
                         X\mathbin{\dot\cup}Y,
        \qquad X\subseteq S,\quad Y\subseteq V(J),
        \qquad |X|+|Y|\le3.                              \tag{2.1}
\]

The set `J-Y` is nonempty.  Delete

\[
                              Z=T\cup X\cup Y.           \tag{2.2}
\]

It has order at most six.  There is no edge from `J-Y` to `S-X`, since
such an edge would be uncovered in the portal-incidence graph.  There
is no edge from `J` to `K` or `R`, and all remaining exits through `T`,
`X`, or `Y` were deleted.  Hence a component of `J-Y` is separated from
the nonempty opposite open shore `R`, contradicting seven-connectivity.
`square`

### Lemma 2.2 (the order-three lobe closes)

If `|J|=3`, then `G` contains a literal `K_7` minor.

#### Proof

Two-connectivity makes `J` a literal triangle.  The same vertex-cover
argument as Lemma 2.1, with a cover of order at most two, shows that the
`S`--`J` incidence graph has a matching saturating `J`.

Likewise the incidence graph between `T` and `J` has a matching
saturating `T`.  Otherwise a vertex cover of order at most two, deleted
inside `G[L]`, would separate a nonempty part of `J` from `K`, contrary
to three-connectivity of `G[L]`.

Write the two matchings as

\[
       s_i x_i\in E(G),\qquad t_i x_i\in E(G)
                         \quad(1\le i\le3),              \tag{2.3}
\]

after independently relabelling the matched boundary and gate vertices.
The three bags `{s_i,x_i,t_i}` are disjoint, connected and pairwise
adjacent through the triangle `J`.  The other lobe `K` meets every
literal gate and satisfies `|N_S(K)|>=4`, because
`T union N_S(K)` is an actual separator.  Choose

\[
                       s_0\in N_S(K)-\{s_1,s_2,s_3\}.
\]

Then `K union {s_0}` is a fourth connected bag adjacent to the first
three through the three gate vertices.  Anchor the three `S`-full
packets in `R` at the remaining three boundary vertices.  These are
seven literal pairwise adjacent bags. `square`

The two matchings in (2.3) need not pair a prescribed boundary label
with a prescribed gate.  Only their common three internal vertices are
used.

### Lemma 2.3 (every portal occurrence extends to four hits)

Assume `|J|>=4`.  Every vertex of `J` which has a neighbour in `S`
belongs to an independent four-set of portal vertices.

#### Proof

The independent portal sets form a transversal matroid on the portal
vertices.  Lemma 2.1 gives rank at least four.  Every portal vertex is a
nonloop, and every nonloop of a matroid extends to a basis of its
rank-four truncation. `square`

## 3. Literal rooted-model lift and the exact negative classes

### Lemma 3.1 (four-hit rooted lift)

Let `x_1,...,x_4` be distinct vertices of `J`, matched to distinct
literal labels `s_1,...,s_4 in S`.  If `J` has a `K_4` model rooted at
the four `x_i`, then `G` has a literal `K_7` model.

#### Proof

Adjoin `s_i` to the rooted bag containing `x_i`.  Anchor the three
opposite `S`-full packets at the remaining three boundary vertices.
The four rooted bags are pairwise adjacent, the packet bags are pairwise
adjacent, and every packet bag sees every rooted bag through its literal
boundary anchor. `square`

### Theorem 3.2 (basis-by-basis rooted obstruction funnel)

In a `K_7`-minor-free survivor with `|J|>=4`, every independent
four-set `B` of literal portal vertices has the following exact negative
certificate:

\[
   J\text{ is a spanning subgraph of an obstruction in }
                   \mathcal A\cup\mathcal B\cup\mathcal C
                   \cup\mathcal D\cup\mathcal E\cup\mathcal F, \tag{3.1}
\]

with the four members of `B` nominated.  These are precisely the six
Fabila-Monroy--Wood rooted-`K_4` obstruction classes.  If `J` is
three-connected, (3.1) specializes to a `B`-web; equivalently, failure
of the rooted model is an ordered planar rib with the permitted clique
pieces inserted at facial triangles.

Every literal portal vertex occurs among the four nominated vertices
of at least one certificate (3.1).

#### Proof

A rooted model would close by Lemma 3.1.  In its absence, Theorem 15 of
Fabila-Monroy and Wood, *Rooted K4-Minors*, gives (3.1).  Their Theorem 8
gives the web form when `J` is three-connected.  The last assertion is
Lemma 2.3. `square`

The supergraph in (3.1) is only an obstruction certificate.  Edges of
its planar rib and edges from an inserted clique to a facial triangle
which are absent from `J` may not be used as branch-set edges in `G`.

## 4. Bipolar support sweep

Three-connectivity of `G[L]` also gives a matching from the three gate
vertices `T` to three distinct vertices of `J`, by the vertex-cover
argument in the proof of Lemma 2.2.  Choose distinct indices `p,q,r`
and distinct literal neighbours

\[
                         x\in N_J(t_p),\qquad
                         y\in N_J(t_q).                   \tag{4.1}
\]

Since `J` is two-connected, it has a bipolar ordering

\[
                         v_1=x,v_2,\ldots,v_n=y           \tag{4.2}
\]

in which every prefix and every suffix is connected.  This follows by
adding `xy` if necessary and taking an `xy`-numbering.

For `0<=h<=n`, put

\[
 P_h=\{v_1,\ldots,v_h\},\qquad
 Q_h=\{v_{h+1},\ldots,v_n\},                             \tag{4.3}
\]

and define the literal gated capacities

\[
 \lambda(h)=|N_S(P_h\cup\{t_p\})|,
 \qquad
 \rho(h)=|N_S(Q_h\cup\{t_q\})|.                        \tag{4.4}
\]

Empty `P_0` or `Q_n` is allowed: its carrier below still contains its
gate vertex.  The function `lambda` is nondecreasing and `rho` is
nonincreasing.

### Theorem 4.1 (bipolar split or crossed capacity interval)

Exactly one of the following occurs for the chosen gates and bipolar
ordering.

1. There is an index `h` with

   \[
                         \lambda(h)>=4,
                         \qquad \rho(h)>=4.              \tag{4.5}
   \]

   In this case `G` has a literal `K_7` minor or is six-colourable.
2. With

   \[
      a=\min\{h:\lambda(h)>=4\},\qquad
      b=\max\{h:\rho(h)>=4\},                           \tag{4.6}
   \]

   one has `b<a`.  Thus the two support-four intervals are crossed, and

   \[
       |N_S(P_{a-1}\cup\{t_p\})|<=3,
       \qquad
       |N_S(Q_{b+1}\cup\{t_q\})|<=3.                   \tag{4.7}
   \]

#### Proof

Suppose (4.5) holds.  The three sets

\[
 C_p=P_h\cup\{t_p\},\qquad
 C_q=Q_h\cup\{t_q\},\qquad
 C_r=K\cup\{t_r\}                                    \tag{4.8}
\]

are disjoint, connected, and span `L`.  There is a `P_hQ_h` edge when
both sides are nonempty; at an empty end the literal edge from its gate
to `x` or `y` gives the same `C_pC_q` adjacency.  The other two carrier
adjacencies are the edges from `K` to `t_p` and `t_q`.  The first two
contact at least four boundary vertices by (4.5), and the third does so
because `|N_S(K)|>=4`.

Apply the audited exact-seven boundary rooted-model trichotomy to the
three spanning clique carriers.  Its list-colouring outcome glues two
proper-minor six-colourings; its anchored-`K_4` outcome lifts with the
three opposite packets to a literal `K_7`; and its one-block outcome
glues using one full packet on each open shore.  This proves outcome 1.

If (4.5) never holds, monotonicity says that the final interval
`{a,...,n}` on which `lambda>=4` and the initial interval
`{0,...,b}` on which `rho>=4` are disjoint.  Hence `b<a`, and (4.7) is
the definition of the two transition indices. `square`

### Corollary 4.2 (universal ordered negative state)

In a hypothetical counterexample, outcome 2 of Theorem 4.1 holds for
every choice of two distinct gate duties, every choice of distinct
literal first hits in (4.1), and every bipolar ordering with those
endpoints.

Thus the genuinely two-connected residue is no longer an unspecified
failure of a connected partition.  It simultaneously has:

* four-hit portal rank and one exact rooted-`K_4` obstruction
  certificate through every literal portal occurrence; and
* a crossed pair of support-capacity transition indices in every
  gate-rooted bipolar ordering.

The unproved composition step is now precise: show that changing the
bipolar ordering or the four-hit basis either overlaps the two capacity
intervals, produces a literal rooted model in one of the six obstruction
classes, or leaves one common actual two-vertex core which meets every
`K_5` model.  The last assertion cannot be inferred merely from one
ordering or from one obstruction supergraph.

## 5. Scope

This theorem closes every two-connected lobe admitting one balanced
bipolar cut.  It also supplies the exact negative web/core catalogue
without any Moser labels or bounded-order enumeration.  It does not yet
prove that the crossed transitions for different bipolar orderings have
the same two pivots, and it does not claim that a two-vertex core in an
obstruction *supergraph* is a separator or an apex pair in the literal
graph.
