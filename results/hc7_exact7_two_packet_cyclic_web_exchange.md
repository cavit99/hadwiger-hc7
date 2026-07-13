# Two-packet exchange across an alternating cyclic web

**Status:** proved and independently audited.  The theorem closes an
unbounded family of attained demand-three states.  It does not close the
coherent matching-cylinder outcome and it does not identify the two packets
when they lie in different rich components.

## 1. The paired-triangle attained state

Work in an actual exact-seven `(1,2)` separation

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad |S|=7,
\]

of a seven-connected, strongly seven-contraction-critical,
`K_7`-minor-free graph.  Let `H=G[S]`, and let `P,Q` be disjoint connected
`S`-full packets in `R`.

Suppose a legal proper-minor operation in the thin shore returns the exact
boundary partition

\[
 \Pi=\{B_0,B_1,B_2,\{c\}\},
 \qquad B_r=\{s_r,s_{r+3}\}\quad(0\le r<3),              \tag{1.1}
\]

where subscripts on the six vertices `s_0,...,s_5` are ordinary integers,
not modulo three.  Assume:

1. every `B_r` is independent;
2. `c` has a neighbour in every `B_r`.

Taking `C={c}` in the attained-duty definition, condition 2 says exactly

\[
                     D_{\Pi,C}(B_r)=B_r.                 \tag{1.2}
\]

Write `B_r~B_t` when there is a literal edge in `H` between those two
blocks.  This is state data, not a colour-to-label inference.  The theorem
below requires one explicitly named relation `B_r~B_t`; the other two
representative adjacencies are supplied geometrically by the packet cycles.
No raw carrier-defect assertion is being used.

## 2. Two alternating packet cycles

Suppose `P` contains a cycle `Z_P` and `Q` contains a cycle `Z_Q` with
six pairwise distinct selected portals

\[
 p_i\in N_P(s_i),\qquad q_i\in N_Q(s_i)\qquad(0\le i<6), \tag{2.1}
\]

which occur in the cyclic orders

\[
 p_0,p_1,p_2,p_3,p_4,p_5
 \quad\hbox{and}\quad
 q_0,q_1,q_2,q_3,q_4,q_5.                               \tag{2.2}
\]

Arcs in what follows include arbitrary subdivisions between consecutive
displayed portals.  The cycles themselves are assumed `S`-full; for the
seventh boundary literal `c`, its portal may coincide with any displayed
cycle vertex or lie on a subdivided arc.

A `Z_P-Z_Q` path is **clean** when its only vertices on the two cycles are
its ends.  A clean path from `p_i` to `q_j` is **homologous** when `i=j`, and
**transverse** otherwise.  Homology here refers to the literal boundary
label `s_i`, not merely to one of the three attained duties.

### Theorem 2.1 (label-compatible transverse web exchange)

Let a transverse clean path have ends `p_i,q_j`.  Rotate all indices so that
its ends are `p_0,q_k`, where `1<=k<=5`.  Suppose the corresponding literal
block adjacency

\[
 M_1=01,\quad M_2=M_3=M_4=12,\quad M_5=02              \tag{2.3}
\]

holds, where `M_k=rt` means `B_r~B_t`.  Then the exact state `Pi` reflects
across the rich shore, and consequently `G` is six-colourable.

#### Proof

Use the rotated indexing in the statement and write `J` for the clean
`p_0-q_k` path.  The following table gives three pairwise
vertex-disjoint connected carriers.  A string such as
`q_0 q_5 q_4 q_3` denotes the corresponding cycle arc, including every
subdivision vertex; concatenation with `J` is at the displayed common end.

| `k` | carrier for `B_0` | carrier for `B_1` | carrier for `B_2` | required block edge |
|---|---|---|---|---|
| 1 | `q_0 q_5 q_4 q_3` | `p_1 p_2 p_3 p_4` | `q_2 q_1 J p_0 p_5` | `B_0~B_1` |
| 2 | `p_0 J q_2 q_3` | `q_1 q_0 q_5 q_4` | `p_2 p_3 p_4 p_5` | `B_1~B_2` |
| 3 | `J` | `p_1 p_2 p_3 p_4` | `q_2 q_1 q_0 q_5` | `B_1~B_2` |
| 4 | `p_0 J q_4 q_3` | `p_1 p_2 p_3 p_4` | `q_2 q_1 q_0 q_5` | `B_1~B_2` |
| 5 | `q_0 q_1 q_2 q_3` | `p_1 p_0 J q_5 q_4` | `p_2 p_3 p_4 p_5` | `B_0~B_2` |

For `k=1`, for example, the third row entry means the path from `q_2` to
`q_1`, then `J` from `q_1` to `p_0`, then the `p_0-p_5` cycle arc.
Cleanliness of `J` and inspection of the two complementary cycle arcs prove
literal vertex-disjointness in every row.

If a cycle edge displayed between two different carriers has been
subdivided, split that portal-free open arc at any one of its edges: add the
initial subpath to the carrier at one end and the terminal subpath to the
carrier at the other.  The two carriers remain disjoint and connected and
become adjacent across the chosen literal edge.  The two geometric
adjacencies used in a row lie in distinct portal-free gaps, so both splits
can be made simultaneously.  Thus subdivision does not turn a quotient
adjacency into a fictitious branch-set adjacency.

Call the three carriers `X_0,X_1,X_2`.  Each `X_r` contains a selected
portal to each of `s_r,s_{r+3}`, so `X_r union B_r` is connected.  The three
sets

\[
                         R_r=X_r\cup B_r                 \tag{2.4}
\]

are pairwise disjoint.  In each table row, two of the three pairs are
adjacent through a displayed cycle edge: inspection gives respectively the
geometric adjacency patterns

\[
 \{02,12\},\ \{01,02\},\ \{01,02\},\
 \{01,02\},\ \{01,12\}.                                \tag{2.5}
\]

The required literal boundary edge in the last column supplies exactly the
missing pair.  Hence the three `R_r` are pairwise adjacent.  By condition 2,
every `R_r` is adjacent to the literal singleton `{c}`.
Therefore

\[
                         R_0,R_1,R_2,\{c\}               \tag{2.6}
\]

are four connected, disjoint, pairwise adjacent branch sets, indexed
exactly by the four blocks of `Pi`.

Contract `R_0,R_1,R_2`.  This is a proper minor: all three carriers lie in
the rich open shore, while the thin open shore is nonempty and untouched.
Strong contraction-criticality supplies a six-colouring.  In its
restriction to the untouched thin closed shore, each `B_r` expands with the
colour of its representative; the clique (2.6) makes the four block colours
pairwise distinct.  Thus its equality partition on the literal set `S` is
exactly `Pi`.

By hypothesis, the thin-shore proper operation which returned `Pi` supplied
a colouring of the opposite rich closed shore with the same exact boundary
partition.  Permute the six colour names to agree block by block and glue
the two colourings across `S`.  The open shores are anticomplete, so this is
a proper six-colouring of `G`, a contradiction.  `square`

The proof uses both full packets geometrically, although the carriers are
allowed to mix their cycle arcs through `J`.  It uses contraction-criticality
only at the exact legitimate point: colouring the proper minor obtained from
the literal carriers in (2.4).

## 3. A whole cross-packet bridge component closes

### Corollary 3.1 (three portal attachments force exchange)

Let `K` be a connected subgraph of the rich shore, disjoint from the two
cycles, whose cycle attachments all belong to

\[
             \{p_0,...,p_5,q_0,...,q_5\}.               \tag{3.1}
\]

Assume the three block pairs `B_0,B_1,B_2` are pairwise adjacent in `H`.
If `K` has an attachment on each cycle and at least three distinct
attachments in total, then `G` is six-colourable.

#### Proof

If every `P`-side attachment `p_i` were homologous to every `Q`-side
attachment `q_j`, then every such pair would satisfy `i=j`.  Hence each side
would have exactly one attachment and there would be only two in total.
Thus some pair `p_i,q_j` is transverse.  A shortest path through the
connected set `K` between neighbours of these two attachments, with its two
attachment edges added, is a clean transverse path.  Apply Theorem 2.1.
`square`

### Corollary 3.2 (connected-rich portal-pure dichotomy)

Assume `R` is connected, the two displayed cycles themselves are the
selected `S`-full packets, and every attachment of a component of
`R-(Z_P union Z_Q)` to a cycle is one of the selected portals (2.1).
Assume also that every edge directly joining the two cycles has selected
portals as both ends, and that the three block pairs are pairwise adjacent
in `H`.
Then either `G` is six-colourable, or all of the following hold:

1. every component of `R-(Z_P union Z_Q)` attaches to only one cycle;
2. every literal edge between the two cycles is homologous, namely of the
   form `p_iq_i`; and
3. at least one such homologous edge exists.

Thus the entire surviving cross-packet interface is a submatching of the
six literal label classes; all nontrivial bridge components are one-sided.

#### Proof

First we prove the needed three-attachment statement directly in this
state-specific setting.  Let `K` be a component of
`R-(Z_P union Z_Q)`, and let `A_K` be its attachment set on the two cycles.
If `|A_K|<=2`, then

\[
                         N_G(K)\subseteq S\cup A_K.
\]

The nonempty thin open shore lies beyond this set, so seven-connectivity
gives `|N_S(K)|>=5`.  At most two of the six literals
`s_0,...,s_5` are missed.  Since `B_0,B_1,B_2` are three disjoint pairs,
some `B_r` is wholly contacted by `K`.  Fund `B_r` with `K` and the other
two blocks with the full cycles.  Fullness supplies every adjacency
involving two different carrier types, the assumed block edges supply any
remaining representative adjacency, and condition 2 supplies adjacency to
`c`.  Contracting the three representatives therefore reflects `Pi` by the
same proper-minor argument as Theorem 2.1, a contradiction.  Hence
`|A_K|>=3`.

If `K` met both cycles, Corollary 3.1 would now six-colour `G`.  This proves
item 1 without invoking the hard-boundary finite normalization.

An edge `p_iq_j` with `i!=j` is itself a clean transverse path, so Theorem
2.1 proves item 2.  By item 1, distinct complementary components cannot
carry a path from one cycle to the other.  Since `R` is connected, there
must therefore be a literal edge between the cycles, proving item 3.
`square`

This is a genuine infinite-family closure.  The cycles and the one-sided
components may have arbitrary order.  The only surviving interface is the
coherent matching-cylinder; no assertion is made that this cylinder already
gives a smaller global separator.

## 4. The two-component rich shore is different

If `G[R]` has two components and the two packet cycles lie in different
components, there is no `Z_P-Z_Q` path in the open shore.  Theorem 2.1 must
not be invoked by routing through the literal boundary `S`: doing so would
consume the very vertices whose equality partition is being reflected.

Under the pairwise block-adjacency specialization of Corollaries 3.1--3.2,
there is nevertheless one exact componentwise closure.  If either rich
component contains two vertex-disjoint connected carriers funding two of
`B_0,B_1,B_2`, use the other `S`-full component for the third block.  The
literal edges between every pair of blocks and from `c` into every block
make the resulting three representatives and `{c}` a clique, so the
contraction-and-gluing proof of Theorem 2.1 applies verbatim.  Hence a
surviving two-component instance is pairwise unlinkable for all three duty
pairs inside each component.

In fact the paired-triangle state gives the required cutvertex closure
directly, without invoking the finite hard-boundary normalization.  Suppose
a rich component `K` has cutvertex `w`.  Choose a component `D` of `K-w` and
put

\[
                              X=D,\qquad Y=K-D.
\]

Both are nonempty and connected and have an edge between them.  The set
`N_G(D)` is contained in `S union {w}`, so seven-connectivity gives
`|N_S(X)|>=6`.  Applying the same argument to any other component of `K-w`,
which lies in `Y`, gives `|N_S(Y)|>=6`.  Each carrier therefore misses at
most one literal and hence forbids at most one of the three disjoint blocks
`B_0,B_1,B_2`.  Two distinct allowed blocks can be assigned to `X,Y`; the
other rich component, which is `S`-full, funds the remaining block.  The
`X-Y` edge, fullness of the third carrier, pairwise block adjacencies, and
condition 2 make the three representatives and `{c}` a clique.  Exact
reflection follows as in Theorem 2.1.  Thus both rich components of a
survivor are cutvertex-free.

Neither cutvertex-freeness nor a rural wheel excludes simultaneous
three-pair unlinkability: the six-terminal wheel is the basic web example.
Closing that componentwise coherent-web outcome requires a state transition
or an internal adhesion theorem beyond the present exchange.

## 5. Sharpness and exact residue

A single homologous edge `p_iq_i` does not suffice for the three-carrier
construction.  More strongly, two six-cycles joined by any subset of the
six homologous matching edges can remain simultaneously unlinkable for the
three paired duties.  This is the cylindrical analogue of the one-cycle
`A B D A B D` barrier; it explains why the word *transverse* in Theorem 2.1
cannot be deleted.

The live continuation is now narrower and label-exact:

* in the connected-rich portal-pure family, convert the coherent homologous
  matching-cylinder into a common proper-minor state or an actual adhesion;
* in the two-component family, compose the two simultaneous rural web
  certificates by a proper-minor transition.

No reduction of the general `(1,2)` cell to the paired-triangle state or to
these cyclic packet cores is claimed.
