# Colourful rooted-`K_4` exchange at a two-gate SPQR transition

## 1. Status and purpose

This note gives a structural replacement for the false assertion that one
four-terminal web remains cofacial after every SPQR flip.  It uses all of
the information which is invariant under the flip:

* colourful rooted-`K_4` exclusion for the relevant four portal classes;
* the exact Fabila--Monroy--Wood reduction across a `(2,2)` separation;
* the full portal sets, rather than one independently selected root; and
* the Hall certificate of a portal incidence which cannot be put into a
  transversal.

The result is a genuine infinite-order dichotomy.  A direct `R--R`
transition is either pole-face coherent, or it exposes an exact order-seven
cut, an order-at-most-eight two-gate adhesion, or a bounded capacity core.
It does not, by itself, prove that the order-eight state is colour-gluable;
that is the remaining operation-state interface.

Throughout this note, `S` is a seven-vertex boundary and `D` is a connected
side with no neighbours outside `D union S`.  For `s in S`, put

\[
                         P_s=N_D(s).
\]

## 2. The colourful completion terminal

Use the `C_6 dotunion K_1` notation

\[
 S=\{c_0,\ldots,c_5,z\},
 \qquad \overline{G[S]}=c_0c_1\cdots c_5c_0\ \dot\cup\ K_1.
\]

For `j=0,1,2`, put

\[
 M_j=\{c_j,c_{j+3}\},\qquad X_j=S-(M_j\cup\{z\}).
\]

Thus `M_j` is an antipodal pair on the missing cycle and `|X_j|=4`.
A **colourful rooted `K_4` at `X_j` in `D`** consists of four disjoint,
connected, pairwise adjacent sets, one meeting each portal class `P_x`,
`x in X_j`.

### Lemma 2.1 (colourful completion)

Assume that a connected set `R`, disjoint from `D union S`, is adjacent to
every vertex of `S`.  If `D` contains a colourful rooted `K_4` at some
`X_j`, then `G` contains a `K_7` minor.

### Proof

Let the four colourful bags be `U_x`, `x in X_j`.  Add `c_x` to `U_x`.
The enlarged bags are connected, disjoint and pairwise adjacent.  Add the
three bags

\[
                         R,\qquad \{z\},\qquad M_j.
\]

The last bag is connected because the two vertices of `M_j` are antipodal,
and hence adjacent in `G[S]`.  Every other cycle vertex is adjacent to at
least one end of `M_j`: its two nonneighbours are consecutive neighbours
on the missing cycle and therefore cannot be the antipodal pair `M_j`.
Fullness of `R` and universality of `z` supply all remaining adjacencies.
These are seven clique bags.  QED.

Consequently, every `K_7`-minor-free realization is colourful-rooted-
`K_4`-free for all three antipodal omissions.  Notice that the desired
four-piece Hall core is not merely analogous to the forbidden antipodal
two-linkage: it is exactly a rooted strengthening of it.

## 3. Exact localization across an `R--R` edge

Let

\[
 D=D_L\cup D_R,\qquad V(D_L\cap D_R)=\{p,q\},
\]

be a separation of order two with both open sides nonempty.  Put

\[
 T_L=D_L+pq,\qquad T_R=D_R+pq.
\]

In a direct `R--R` SPQR transition, `T_L,T_R` are three-connected planar
torsos; the edge `pq` may be virtual.

### Lemma 3.1 (rooted-`K_4` localization)

Let `a,b` be distinct portal vertices in `D_L-{p,q}` and let `c,d` be
distinct portal vertices in `D_R-{p,q}`.  If `D` has no `K_4` minor rooted
at `a,b,c,d`, then

\[
 T_L\text{ has no }K_4\text{ rooted at }a,b,p,q,
\]

and symmetrically `T_R` has no `K_4` rooted at `p,q,c,d`.  Hence, when the
torsos are three-connected and planar, `a,b,p,q` lie on one face of
`T_L`, and `p,q,c,d` lie on one face of `T_R`.

### Proof

Fabila--Monroy and Wood, Lemma 12, says exactly that in a two-connected
graph with a `(2,2)` separation of order two, a rooted `K_4` at the four
roots exists if and only if one of the two edge-completed sides contains
the corresponding rooted `K_4` at its two local roots and the two poles.
The first assertion is its contrapositive.  Their planar rooted-`K_4`
theorem then gives the facial conclusion in each three-connected planar
torso.  The virtual edge causes no lifting problem: its expansion through
the other side is precisely the content of Lemma 12.  QED.

This is the valid substitute for reflecting a web face.  It makes no claim
that a face chosen in one embedding survives a flip; instead it localizes
the rooted obstruction separately in the two fixed torsos.

## 4. Portal incidence failure is an adhesion certificate

The following lemma is label-free.  It is the capacity-state part of the
exchange.

### Lemma 4.0 (defect-two side is already an exact descent)

Let `C` be a component of `D-{p,q}`.  If

\[
                         |S-N_S(C)|=2,
\]

then

\[
                         N_S(C)\cup\{p,q\}          \tag{4.0}
\]

is an exact seven-cut in a seven-connected graph.

### Proof

The set (4.0) is the entire external neighbourhood of `C`, has order
seven, and separates `C` from the opposite full shore.  Seven-connectivity
forces every displayed vertex to be an actual neighbour, so it is an
exact cut.  QED.

Consequently a cut-irreducible rank-two/rank-two transition has defect at
most one on each open side.  The defect-two rows in the exact two-piece
atlas do not require any further SPQR analysis.

### Lemma 4.1 (forced incidence or gate adhesion)

Let `C` be one open side of a two-separation with gate

\[
                              Z=\{p,q\}.
\]

Assume

\[
 N_G(C)\subseteq Z\cup(S-\Delta),                 \tag{4.1}
\]

where `Delta subseteq S` is the boundary defect of `C`.  Let `A` be a set
of boundary labels in `S-Delta` whose portal sets in `C` satisfy Hall's
condition.  Fix an incidence `x in P_i cap C`, `i in A`.

If no matching of `A` into `C` uses the incidence `i x`, then one of the
following holds.

1. `C` is a bounded capacity core of order at most `|A|-1`.
2. A nonempty proper connected subset of `C` lies behind a separator of
   order at most
   \[
                              9-|\Delta|.           \tag{4.2}
   \]

More precisely, there is `J subseteq A-{i}` with

\[
 x\in U:=\bigcup_{j\in J}(P_j\cap C),
 \qquad |U|=|J|,                                   \tag{4.3}
\]

and every component `K` of `C-U` satisfies

\[
 N_G(K)\subseteq
 U\cup Z\cup\bigl(S-(J\cup\Delta)\bigr).          \tag{4.4}
\]

In a seven-connected graph, if `|Delta|=2`, outcome 2 is a nested exact
seven-cut.  If `|Delta|=1`, it is an order-seven or order-eight gate; in
the absence of a nested exact seven-cut it is exactly order eight.

### Proof

Force `i` to be matched to `x` and delete that label and vertex from the
bipartite portal graph.  Since the remaining labels cannot be matched,
Hall's theorem gives `J subseteq A-{i}` with

\[
 \left|\left(\bigcup_{j\in J}(P_j\cap C)\right)-\{x\}\right|
       \le |J|-1.
\]

The original Hall condition gives `|U|>=|J|`.  Therefore equality holds,
`x in U`, and (4.3) follows.

If `C=U`, then `|C|=|J|<=|A|-1`, which is outcome 1.  Otherwise take a
component `K` of `C-U`.  It has no boundary neighbour in `J`; it has no
boundary neighbour in `Delta` by (4.1); and every shore neighbour outside
`K` lies in `U union Z`.  This proves (4.4).  Its right side has order

\[
 |J|+2+(7-|J|-|\Delta|)=9-|\Delta|.
\]

In the full-shore application an opposite component lies beyond this set,
so it is a genuine separator.  Seven-connectivity gives the last claims.
QED.

### Lemma 4.2 (Hall failure is one order sharper)

In the same setting, if a label set `J subseteq S-Delta` itself violates
Hall, then either `C` is a capacity core of order at most `|J|-1`, or a
proper part of `C` lies behind a separator of order at most

\[
                              8-|\Delta|.           \tag{4.5}
\]

Thus, apart from the bounded-capacity outcome, defect two makes Hall
failure impossible in a seven-connected graph, while defect one turns it
into a nested exact seven-cut.

### Proof

Put `U=union_{j in J}(P_j cap C)`, with `|U|<=|J|-1`, and repeat the proof
of Lemma 4.1.  The right side of (4.4) now has order at most

\[
 (|J|-1)+2+(7-|J|-|\Delta|)=8-|\Delta|.
\]
QED.

### Lemma 4.3 (tight portal block)

Still in the same setting, suppose a nonempty label set `J` has

\[
 U=\bigcup_{j\in J}(P_j\cap C),\qquad |U|=|J|.
\]

Then either `C=U`, or a proper part of `C` lies behind a separator of
order at most `9-|Delta|`.

### Proof

Take a component of `C-U` and use (4.4).  The count is exactly the one in
Lemma 4.1.  QED.

### Corollary 4.4 (exact pair-incidence lock at defect one)

Let `Delta={alpha}` and take `A={i,k}` in Lemma 4.1.  Suppose the two
portal classes have a matching, but an occurrence `x in P_i cap C` cannot
be used in one.  Then either `C={x}`, or

\[
                         P_k\cap C=\{x\},           \tag{4.6}
\]

and every component of `C-x` lies behind

\[
 B=\{x,p,q\}\cup\bigl(S-\{k,\alpha\}\bigr),
 qquad |B|=8.                                     \tag{4.7}
\]

In a seven-connected graph with no nested exact seven-cut, (4.7) is an
exact order-eight separator.  The vertex `x` is a literal common portal
of the two labels `i,k`, and it is the unique `k`-portal in this open
side.

### Proof

The nonempty Hall witness `J subseteq A-{i}` in Lemma 4.1 can only be
`J={k}`.  Equation (4.3) gives (4.6), and (4.4) is exactly (4.7).  If
`C-U` is empty then `C={x}`.  Otherwise seven-connectivity gives boundary
order seven or eight; excluding the former makes all eight displayed
vertices necessary.  QED.

If `c_i c_k` is one of the missing-cycle edges, the common portal in
Corollary 4.4 is the centre of the faithful star `c_i-x-c_k`.  Contracting
that star invokes the coupled two-edge Kempe lock from
`hadwiger_two_edge_star_kempe_lock.md`.  Thus the nonedge-labelled part of
the order-eight state already carries a proper-minor exchange witness;
what remains is to convert its coupled Kempe intersections/cross-edges
into either the missing portal matching or a common boundary colouring
state.

The distinction between (4.2) and (4.5) is essential.  An SDR may exist
while one particular portal occurrence is not allowed in any SDR.  At
defect one this is genuinely an order-eight, rather than order-seven,
capacity state.

## 5. Synchronizing full portal sets inside one torso

We isolate the planar argument used after Lemmas 3.1 and 4.1.

### Lemma 5.1 (pole-face synchronization)

Let `T` be a three-connected plane graph with distinct poles `p,q`.  Let
`A_0,A_1,C_0,C_1` be nonempty portal sets in `V(T)-{p,q}`.  Assume:

1. for every distinct `a in A_0`, `b in A_1`, the graph `T` has no
   rooted `K_4` at `a,b,p,q`;
2. the graph on `A_0 union A_1` whose edges are the distinct pairs
   `ab`, `a in A_0,b in A_1`, is connected;
3. every vertex of `C_0 union C_1` belongs to a four-element transversal
   `a,b,c,d` of `A_0,A_1,C_0,C_1`; and
4. `T` has no rooted `K_4` at any such four-element transversal; and
5. the transversal in item 3 can be chosen so that its private incidence
   edge `ab` has an adjacent private incidence edge `ab'` or `a'b` whose
   new endpoint avoids `{c,d}`.

If the incidence graph in item 2 has at least three vertices, then one
face of `T` contains

\[
                     \{p,q\}\cup A_0\cup A_1\cup C_0\cup C_1.
                                                               \tag{5.1}
\]

### Proof

By the planar rooted-`K_4` theorem, every distinct pair `a in A_0`,
`b in A_1` lies with `p,q` on a face.  Two such pairs sharing an endpoint
give faces sharing `p,q` and that endpoint.  Distinct faces in a
three-connected plane graph meet in at most one edge, so the two faces are
equal.  Connectivity of the incidence graph propagates this equality to
one face `F` containing `p,q,A_0,A_1`.

Take `c in C_0 union C_1` and a transversal `a,b,c,d` supplied by item 3.
Item 4 and the planar rooted theorem put these four vertices on a face
`H`.  If `H=F`, then `c in F`.  Suppose `H ne F`.  Their intersection
contains `a,b`, so it is exactly the edge `ab`; in particular `c,d` do
not lie on `F`.

By item 5 choose an adjacent incidence edge, say `ab'`, with
`b' notin {c,d}`.  The four vertices `a,b',c,d` are distinct, so item 4
puts them on a face
`H'`.  Again `H' ne F`.  But `H,H'` share the three distinct vertices
`a,c,d`, hence `H=H'`.  This common face and `F` then share both adjacent
edges `ab,ab'`, a path on three vertices, impossible for two distinct
faces of a three-connected plane graph.  Therefore `H=F`, and `c in F`.
As `c` was arbitrary, (5.1) follows.  QED.

The hypotheses are phrased in terms of the full portal sets.  Lemma 4.1
is exactly what converts failure of item 3 for a particular occurrence
into an adhesion certificate, rather than silently replacing that
occurrence by an unrelated SDR representative.
Item 5 is separately necessary when portal classes overlap: connectedness
of the private incidence graph alone does not prevent its only adjacent
edge from reusing `c` or `d`.

### Proposition 5.2 (exact overlap-lock normal form)

Let `a,b,c,d` be a four-element transversal in Lemma 5.1 and suppose
`ab` has no adjacent private incidence edge whose new endpoint avoids
`{c,d}`.  Then

\[
                         A_0\cup A_1\subseteq\{a,b,c,d\}. \tag{5.2}
\]

Consequently exactly one of the following holds.

1. `A_0 union A_1={a,b}`.  This is a tight two-label block, so Lemma 4.3
   gives an order-`9-|Delta|` adhesion unless the open side is the
   two-vertex capacity core.
2. At least one of `c,d` is simultaneously a portal for a private label
   and for its displayed further label.  Thus the overlap is represented
   by an actual double-labelled shore vertex, not merely by two portal
   sets meeting somewhere in a quotient.

### Proof

If `y in A_1-{a}`, then `ay` is an incidence edge adjacent to `ab`.
By the lock, `y in {c,d}` unless `y=b`.  Hence
`A_1 subseteq {a,b,c,d}`.  Interchanging the two private classes gives
the same inclusion for `A_0`, proving (5.2).  If neither `c` nor `d`
belongs to a private class, the union is exactly `{a,b}`; otherwise the
second outcome holds.  QED.

### Corollary 5.3 (the non-tight overlap has a faithful star operation)

In outcome 2 of Proposition 5.2, let `w` be a double-labelled portal and
let `r,s in S` be the two corresponding boundary labels.  If `rs` is a
boundary nonedge, then contracting the connected star

\[
                              r-w-s                \tag{5.3}
\]

and six-colouring the proper minor produces exactly the coupled two-edge
Kempe lock of Theorem 1.1 in `hadwiger_two_edge_star_kempe_lock.md`, with
centre `w` and leaves `r,s`.

### Proof

The two star edges are literal portal incidences and the leaves are
nonadjacent.  Expand the contracted image with one colour and apply the
cited theorem.  No boundary labels are identified in the original graph,
and the operation is a proper minor operation.  QED.

This is the exact point at which minor-criticality enters the overlap
branch.  The static rooted-web argument reduces it to either the tight
two-label adhesion or one faithful two-edge-star state.  The coupled Kempe
lock alone does not assert disjoint rooted bags; a further proof must use
its common-colour intersection/cross-edge alternative to create the
missing transversal incidence or a common boundary state.

## 6. The direct `R--R` exchange theorem

### Theorem 6.1 (colourful core, rural transition, or adhesion)

Consider a direct `R--R` SPQR transition in a seven-connected two-full-
shore `C_6 dotunion K_1` cell.  Suppose the portal labels relevant on each
torso can be grouped as two pole-local classes `A_0,A_1` and two further
classes `C_0,C_1`, so that the `(2,2)` rooted reductions of Lemma 3.1 and
the four-class transversals of Lemma 5.1 are the three antipodal colourful
root states.  Assume, as in the exact negative two-piece lock, that each
open side has nonempty boundary defect (hence defect one or two).

Then at least one of the following occurs.

1. There is a colourful rooted `K_4`, and hence a `K_7` minor by Lemma
   2.1.
2. A proper part lies behind a nested exact seven-cut.
3. A proper part lies behind an order-eight two-gate adhesion, with a
   tight Hall set (4.3).  This can occur only on a defect-one side.
4. One open torso is a bounded capacity core of order at most three.
5. A four-class **overlap lock** occurs: some transversal `a,b,c,d` has
   no adjacent private incidence edge avoiding `{c,d}`.
6. Both `R` torsos are pole-face coherent.  Gluing their two disk
   embeddings along the virtual edge gives a common rural embedding of
   all portal classes which satisfy the displayed grouping.

### Proof

If a relevant four-class portal family violates Hall, apply Lemma 4.2.
If an occurrence needed in Lemma 5.1 is not allowed in a transversal,
apply Lemma 4.1.  If the two pole-local portal classes have only two
distinct portal vertices, apply Lemma 4.3 to that tight two-label block.
These are outcomes 2--4 (with outcome 3 only at defect one).  Otherwise
Hall gives a distinct pole-local pair; the graph of all such pairs is
connected, and it has at least three vertices.  If item 5 of Lemma 5.1
fails, retain outcome 5.  Otherwise all hypotheses of Lemma 5.1 hold on
each torso.
Lemma 3.1 and the planar rooted-`K_4` theorem supply its rooted exclusions,
so Lemma 5.1 gives a pole face containing the full relevant portal sets.
In a three-connected plane graph every facial boundary is an induced
cycle.  Since `pq` is an edge and both poles lie on the displayed face,
that face is incident with `pq`.  The two plane torsos can therefore be
glued along the two copies of `pq`, with one copy reflected if necessary.
Deleting the virtual edge leaves a plane embedding of the two-sum in which
the two pole faces merge.  This is outcome 6.  QED.

In the complete six-state high-owner application, if outcome 6 contains
all six portal classes, Theorem 1.1 of
`hadwiger_circular_obstruction_frame_theorem.md` says that the common-face
society realizes at most one opposite frame pair.  A high-owner shore
requires two, so the rural outcome is impossible.  Therefore the exact
remaining state after this theorem is not another arbitrary SPQR flip:
it is one of outcomes 2--5, or a failure to place the six labels into the
two four-class groupings required in Theorem 6.1.

## 7. The exact defect-one polarity

The six `C_6` labels allow the grouping issue in the preceding paragraph
to be solved without a portal enumeration.

Let the three antipodal pairs be `M_0,M_1,M_2` as in Section 2.  For
`alpha,beta in W union {z}`, where `W={c_0,...,c_5}`, define a graph
`H(alpha|beta)` as follows.  Its vertex set is

\[
 W-\bigl(\{\alpha\}\cap W\bigr).
\]

Two labels `i,k` are adjacent when, for some `j`,

\[
 \{i,k\}\subseteq X_j,
 \qquad \beta\notin X_j-\{i,k\}.                   \tag{7.1}
\]

Thus `i,k` may be rooted on the `alpha`-defect side and the other two
labels of `X_j` may be rooted on the `beta`-defect side.

### Lemma 7.1 (compatibility graph)

The graph `H(alpha|beta)` is disconnected if and only if

\[
                         \alpha=\beta\in W.         \tag{7.2}
\]

In that case the antipodal mate `alpha*` is isolated and the other four
vertices induce a clique.

### Proof

View `W` as the disjoint union of the three antipodal pairs.  If `i,k`
belong to different pairs, the unique set `X_j` containing them and
omitting the third pair has remaining roots `i*,k*`.  Hence

\[
 ik\in E(H(\alpha|\beta))
 \quad\Longleftrightarrow\quad
 \beta\notin\{i^*,k^*\}.                           \tag{7.3}
\]

If `i,k` are antipodal mates, they lie together in either of the two
sets `X_j` which omit another pair; choose one whose remaining pair does
not contain `beta`.  Thus every available antipodal-mate edge is present.

If `alpha=beta in W`, the vertex `alpha` is absent and (7.3) forbids
every edge from `alpha*` to another antipodal part.  Its mate edge is also
absent, so `alpha*` is isolated.  The remaining four vertices lie in two
complete antipodal parts, and (7.3) gives every cross-edge between them.

Conversely, if `beta=z`, all eligible edges are present.  Suppose
`beta in W` and `alpha ne beta`.  If `alpha ne beta*`, the mate edge
`beta beta*` is present.  Every other available antipodal pair is joined
by its mate edge, and (7.3) supplies cross-edges between the three pair
blocks.  If `alpha=z` all three mate edges remain; if `alpha in W`, only
its mate `alpha*` loses that edge, but because
`alpha notin {beta,beta*}`, equation (7.3) joins `alpha*` to either of
the other two pair blocks.

It remains to take `alpha=beta*`.  The four vertices in the other two
antipodal pairs induce a clique: their mate edges and every cross-edge
between the two pairs are present.  Moreover `beta` is adjacent to all
four, since for `u` outside the `beta`-pair the remaining roots in the
antipodal omission containing `beta,u` are `beta*=alpha,u*`, neither of
which is `beta`.  Hence the graph is connected in this case as well.
QED.

### Theorem 7.2 (different defects synchronize; equal defects polarize)

Let a direct `R--R` transition have open components `C_L,C_R` with
singleton boundary defects `alpha,beta`, respectively.  Assume:

1. all three antipodal colourful rooted `K_4` states are absent;
2. neither side exposes a nested exact seven-cut, an order-eight gate of
   Lemma 4.1, or a bounded capacity core; and
3. the augmented sides are three-connected planar `R` torsos.

Then:

* if `alpha ne beta`, or if either defect is `z`, all six cycle portal
  classes lie on the one facial cycle obtained by gluing the two pole
  faces;
* if `alpha=beta=c_a in W`, every portal of `c_a` in `D` lies in
  `{p,q}`, and on each torso the other four nonmate classes lie on one
  pole face.  The sole class not forced onto that face is the antipodal
  mate `c_{a+3}`.

### Proof

Fix an edge `ik` of `H(alpha|beta)` and a portal occurrence
`x in P_i cap C_L`.  By Lemmas 4.1 and 4.2 and the excluded outcomes,
`x` can be extended to distinct representatives `x,y` of the two labels
`i,k` in `C_L`.  Condition (7.1) similarly gives distinct representatives
of the other two labels of the corresponding `X_j` in `C_R`.

If the augmented left torso had a rooted `K_4` at `x,y,p,q`, Lemma 3.1
would lift it to a colourful rooted `K_4` at `X_j`.  Therefore it has no
such rooted model, and the planar rooted theorem puts `x,y,p,q` on one
face.

For completeness, this synchronizes the **full** two portal classes, not
only the selected representatives.  Fix distinct base representatives
`a in P_i cap C_L`, `b in P_k cap C_L`.  For any
`r in P_i cap C_L` with `r ne b`, apply the preceding argument to `r,b`;
the resulting face and the base face share `p,q,b`, and hence are equal.
If `r=b`, it is already on the base face.  Symmetrically every occurrence
of `P_k cap C_L` lies on that face.  For two incident edges of
`H(alpha|beta)`, use any occurrence of their common label.  Their two
full-set faces share that occurrence and `p,q`, so they are equal.
Connectivity propagates one pole face through every label in a component
of `H(alpha|beta)`.

Apply the same argument on the right, with `H(beta|alpha)`.  Lemma 7.1
now proves the first conclusion.  The pole faces are incident with `pq`,
as in Theorem 6.1, and so glue to one face of the two-sum.

In the exceptional case `alpha=beta=c_a`, neither open component has a
`c_a`-portal.  Fullness of `D` therefore gives

\[
                              P_{c_a}\subseteq\{p,q\}.
\]

Lemma 7.1 gives exactly the asserted isolated mate and the common face for
the other four classes on both sides.  QED.

### Lemma 7.3 (the gate root repairs the isolated mate)

In the exceptional equal-defect outcome of Theorem 7.2, assume again that
there is no exact seven-cut, order-eight gate, or bounded capacity core.
Then the mate class `P_{c_{a+3}}` also lies on the pole face of each
torso.  Consequently all six cycle portal classes lie on the common face
of the two-sum.

### Proof

Rotate indices to write the common defect as `c_a`, and choose a pole

\[
                         g\in P_{c_a}\cap\{p,q\};
\]

such a pole exists by fullness.  Choose either of the other antipodal
pairs, say `M_b={u,v}`.  The four labels

\[
                         \{c_a,c_{a+3},u,v\}        \tag{7.4}
\]

are exactly one of the sets `X_j` from Section 2.

Let `x` be an occurrence of the mate class in `C_L`.  Apply Lemmas 4.1
and 4.2 to the three open-side label classes
`c_{a+3},u,v`, forcing the displayed occurrence `x`.  Since all adhesion
and capacity outcomes are excluded, there are distinct representatives

\[
                         x\in P_{c_{a+3}},\ y\in P_u,\ t\in P_v
\]

inside `C_L`.  The vertices `g,x,y,t` are therefore a colourful
transversal of (7.4) in the augmented left torso.  A rooted `K_4` at
these vertices would already be a colourful rooted `K_4` in `D`, so it
is absent.  The planar rooted theorem puts `g,x,y,t` on a face `H`.

The pole face `F` from Theorem 7.2 contains `p,q` and the full portal
sets of the four nonmate classes; in particular it contains `g,y,t`.
The two faces `F,H` share three distinct vertices, and a three-connected
plane graph has no two distinct faces with such an intersection.  Hence
`F=H` and `x in F`.  This works for every mate occurrence in `C_L`, and
the argument in `C_R` is identical.  Any mate occurrence at a pole is
already on both pole faces.  Gluing the faces proves the conclusion.
QED.

### Corollary 7.4 (structural replacement for the failed flip)

In a high-owner `C_6 dotunion K_1` shore, the first outcome of Theorem 7.2
contradicts the common-face circular obstruction theorem.  Hence every
direct `R--R` transition has one of the following exact forms:

1. a `K_7` minor;
2. a nested exact seven-cut;
3. an order-eight tight-Hall gate;
4. a bounded capacity core.

This uses all three antipodal rooted states simultaneously and never
reflects a previously selected face.  In particular, the apparent
equal-defect two-gate polarity is not a fifth static residue: the pole
itself repairs the isolated mate unless the repair is blocked by the exact
order-eight capacity state.

## 8. Exact audit boundary

The following conclusions are proved here.

* A colourful four-piece Hall core is an explicit `K_7` terminal.
* Fabila--Monroy--Wood Lemma 12 localizes every `(2,2)` failure to the
  two augmented torsos without assuming face invariance under reflection.
* A forbidden portal incidence has the exact capacity certificate
  (4.3)--(4.4): defect two gives an exact seven-cut; defect one gives an
  order-at-most-eight gate.
* Once the four-class transversal conditions hold, full portal sets, not
  selected representatives, synchronize on one pole face.

What is not claimed is that the existing `C_6` hypotheses automatically
choose the same two four-class groupings on both sides in every
rank-two/rank-two transition.  Proving that final assignment statement,
or showing that its failure is itself the tight Hall state (4.3), is the
remaining finite-capacity exchange.  This is strictly narrower than the
retracted one-web SPQR assertion and retains the operation-sensitive
order-eight alternative rather than hiding it.
