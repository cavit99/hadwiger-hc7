# Canonical two-block states from opposite full-shore contractions

## 1. A uniform operation-state lemma

Let `G` be proper-minor-minimal subject to not being `r`-colourable.
Let `(A,B)` be a separation with boundary `S`, and suppose there are
connected full shores

\[
 D_A\subseteq A-S,\qquad D_B\subseteq B-S
\]

each adjacent to every vertex of `S`.  Let `P,Q` be disjoint nonempty
independent sets of `G[S]`, and put

\[
                             R=S-(P\cup Q).
\]

Assume `G[R]` is complete and `|R|+2<=r`.  Write

\[
 \Pi_{P,Q}=\{P,Q\}\cup\{\{x\}:x\in R\}.             \tag{1.1}
\]

### Theorem 1.1 (opposite-shore two-block forcing)

Simultaneously contract the two disjoint connected sets

\[
                         D_A\cup P,\qquad D_B\cup Q.    \tag{1.2}
\]

Every `r`-colouring of the resulting proper minor induces exactly the
partition `Pi_{P,Q}` when the contracted boundary vertices are expanded
back onto `S`.

#### Proof

The two contracted images are adjacent: fullness of `D_A` supplies an
edge to every vertex of `Q`.  Every vertex of `R` is adjacent to each
image, again by fullness, and the vertices of `R` form a clique.  Hence
the two images together with `R` induce a clique of order `|R|+2` in the
minor.  They receive pairwise distinct colours.  Expanding the first
image on `P` and the second on `Q` gives exactly (1.1).  The operation is
proper because both shores are nonempty and at least one contraction is
nontrivial.  \(\square\)

No planarity, bounded shore order, or finite boundary enumeration enters
the theorem.  It converts two full shores into one canonical operated
boundary state.

## 2. Exact two-state orientation

Let `E_A,E_B` be the boundary partitions extendable over the two closed
shores.  The full-shore exact-block theorem gives

\[
 E_A\cap E_B=\varnothing,
 \qquad
 E_A\cap\Omega(P)\ne\varnothing\ne E_B\cap\Omega(P). \tag{2.1}
\]

### Corollary 2.1 (a two-state block is an oriented lock)

If

\[
                         \Omega(P)=\{\Pi_{P,Q},\Pi'\}, \tag{2.2}
\]

then exactly one shore extends `Pi_{P,Q}`, the other extends `Pi'`, and
neither state extends both shores.  Thus the canonical double contraction
in Theorem 1.1 carries one well-defined shore-orientation bit.

#### Proof

Both disjoint side families in (2.1) must meet the two-element set
`Omega(P)`.  They therefore take its two different members, one each.
\(\square\)

If `Omega(Q)` is also a two-element set containing `Pi_{P,Q}`, the same
canonical operated state orients both exact-block constraints at once,
and the orientations necessarily agree: `Pi_{P,Q}` extends the same
shore in both constraints, while the two other states both extend the
opposite shore.  This is forced already by abstract Property B because
the two hyperedges share the same state.  It should not be confused with
two constraints having different canonical operated states; their
relative orientations may remain free, as in Section 3.

## 3. The seven-edge theta gate has two canonical bits

For the final seven-edge equality type `FwJG?`, normalize the missing-edge
graph by

\[
 E(Q)=\{01,02,05,12,15,24,45\}.                    \tag{3.1}
\]

The sets `012` and `015` are triangles of `Q`, hence independent blocks
of the boundary graph.  Direct inspection of the two remainders gives

\[
\begin{aligned}
 \Omega(012)&=\{
  012\mid3\mid4\mid5\mid6,
  012\mid3\mid45\mid6\},\\
 \Omega(015)&=\{
  015\mid2\mid3\mid4\mid6,
  015\mid24\mid3\mid6\}.
                                                               \tag{3.2}
\end{aligned}
\]

Indeed, after deleting `012` the only missing edge among the four
remaining labels is `45`; after deleting `015` it is `24`.

Apply Theorem 1.1 to

\[
                     (P,Q)=(012,45),\qquad(015,24).      \tag{3.3}
\]

The remaining two singleton labels form an edge in the boundary graph,
so the theorem applies.  It canonically produces the two merged states

\[
                  012\mid3\mid45\mid6,
                  \qquad
                  015\mid24\mid3\mid6.                 \tag{3.4}
\]

Each state extends exactly one full shore and is rejected by the other.
Thus the rank-two theta packet core carries **two explicit operation-state
orientation bits**, rather than an arbitrary Property-B colouring.

The diagnostic verifier
`equality_gate_exact_block_state_spectra.py` independently enumerates all
proper boundary partitions and NAE Property-B constraints.  Among the ten
seven-edge packet residues, these are the only two state pairs forced
opposite in every Property-B colouring.

## 4. Independent spectrum audit and the membership warning

The script `equality_gate_theta_two_bit_verify.py` imports none of the
packet-atlas or state-spectra code.  It generates the set partitions of
the seven labels directly and checks every two-colouring of the resulting
exact-block hypergraph.  It certifies:

1. there are 19 proper boundary states and 16 nonempty independent
   boundary blocks;
2. there are 12,987 Property-B colourings modulo global shore
   interchange;
3. the two pairs in (3.2) are the only forced-opposite pairs, and no pair
   is forced equal; and
4. all four assignments of the two canonical bits occur among the
   abstract Property-B colourings.

Only item 3's two displayed pairs have been promoted to actual shore
membership, and that promotion is Corollary 2.1: both shores must extend
a state in each two-element exact-block edge.  An arbitrary red or blue
entry in a computational Property-B colouring need not extend the
corresponding graph shore.  The four witnesses in item 4 prove that the
static exact-block axioms impose no relation between the bits; they do
not construct graph sides realizing those witnesses.

## 5. The two bits force actual centre paths in both shores

Write

\[
\begin{aligned}
 A_0&=012\mid3\mid4\mid5\mid6,&
 A_1&=012\mid3\mid45\mid6,\\
 B_0&=015\mid2\mid3\mid4\mid6,&
 B_1&=015\mid24\mid3\mid6.                    \tag{5.1}
\end{aligned}
\]

For a shore `C`, an **external `xy` path** means an `x`--`y` path in
`G[C union S]` whose internal vertices all lie in `C`.

### Theorem 5.1 (uniform merge-pair carrier lemma)

Let `Pi_0,Pi_1` be two proper boundary partitions which have identical
blocks except that `Pi_0` has singleton blocks `{x},{y}` while `Pi_1` has
the merged block `{x,y}`.  Suppose `Pi_0` extends one closed shore and is
rejected by the other, while `Pi_1` extends the other and is rejected by
the first.  Then:

1. in every colouring inducing `Pi_0`, vertices `x,y` lie in the same
   bichromatic component for their two boundary colours; and
2. if `Pi_1` uses at most `r-1` boundary colours, then in every colouring
   inducing `Pi_1`, vertices `x,y` lie in the same bichromatic component
   for their common colour and each colour absent from the boundary.

If `Pi_1` uses at most `r-1` boundary colours, each shore therefore
contains an external `xy` path.

#### Proof

Let a colouring of the first shore induce `Pi_0`, and let the distinct
colours of `x,y` be `alpha,beta`.  No other boundary vertex has either
colour.  If their `alpha/beta` components were distinct, interchange the
two colours on the component containing `x`.  The boundary state would
become exactly `Pi_1`, contradicting the fact that the two states extend
opposite shores.  Hence the two vertices lie in one component.  A shortest
path between them has no internal boundary vertex and is the required
external path.

Now let a colouring of the other shore induce `Pi_1`.  The bound on its
number of blocks supplies a boundary-absent colour `gamma`.  Let `alpha`
be the common colour of `x,y`.  If the two vertices lay in different
`alpha/gamma` components, switching the component of `x` would split their
common block and induce exactly `Pi_0`, again a contradiction.  The same
shortest-path argument applies. \(\square\)

### Corollary 5.2 (the theta centre paths)

Apply Theorem 5.1 to `A_0,A_1` and then to `B_0,B_1`.  Both shores contain
an external `45` path and an external `24` path.  In a colouring inducing
`A_1` or `B_1`, which uses four boundary colours, either of the two absent
colours supplies the corresponding bichromatic path.

This conclusion is simultaneous only at the level of existence.  The
`45` and `24` paths may come from different colourings of the same shore
and need not be disjoint.

### Lemma 5.3 (crossed bits force theta bridges)

Put

\[
                         U=\{0,1,4\},\qquad V=\{2,5\}.          \tag{5.2}
\]

If one shore extends exactly one of `A_1,B_1`, then it contains an
external path from `U` to `V`.  If it extends exactly one of `A_0,B_0`,
then it contains an external path from `{0,1}` to `{2,5}`.  Every such
path realizes one of the missing boundary edges joining its two displayed
terminal sets.

Consequently, in the crossed orientation `x!=y` of (7.1), each shore has
both kinds of theta bridge (possibly obtained from different colourings
and with no asserted disjointness).

#### Proof

Take a colouring inducing `A_1`, and denote the colours of blocks `012`
and `45` by `alpha,beta`.  The subgraph of the boundary induced by those
two colours has exactly two components:

\[
              0-4-1\quad\hbox{on }U,
              \qquad 2-5\quad\hbox{on }V.          \tag{5.3}
\]

Indeed, these are precisely the boundary edges between `012` and `45`.
If the two sets lay in distinct `alpha/beta` components of the whole
closed shore, switch the component containing `U`.  Its boundary blocks
become `015` and `24`, so the new state is exactly `B_1`.  Therefore a
shore which rejects `B_1` has an `alpha/beta` component meeting both
`U,V`.  A shortest connection has interior in the open shore, because
there is no boundary edge between the two components in (5.3).  The same
argument starting from `B_1` gives `A_1` after the switch.

For `A_0`, use the colours of block `012` and singleton `5`.  Their
boundary bichromatic graph has components `{0}`, `{1}`, and the edge
`2-5`.  If the component containing `2-5` avoided `{0,1}`, switching it
would induce exactly `B_0`.  Rejection of `B_0` therefore supplies an
external path from `{2,5}` to `{0,1}`.  The reverse argument starts from
`B_0`.  Finally, all six pairs between `U` and `V`, and all four pairs
between `{0,1}` and `{2,5}`, are edges of the missing graph (3.1), proving
the last assertion. \(\square\)

## 6. Two complete-quotient crossbars

Among the eight theta packet edges, two have complete block-adjacency
quotient:

\[
 R_A=05\mid12\mid3\mid4\mid6,
 \qquad
 R_B=15\mid02\mid3\mid4\mid6.                  \tag{6.1}
\]

For `R_A`, the only non-obvious quotient adjacencies are supplied by the
boundary edges `25`, `04`, and `14`; labels `3,6` are complete to the
boundary.  For `R_B`, use `25`, `04`, and `14` again.  Thus the one-way
packet-transfer theorem applies to both states.

### Lemma 6.1 (each crossbar has a unique owner)

Exactly one full shore contains disjoint carriers for `05` and `12`, and
`R_A` extends exactly the opposite shore.  Exactly one full shore contains
disjoint carriers for `15` and `02`, and `R_B` extends exactly the
opposite shore.

#### Proof

The cyclic-packet theorem supplies at least one owner for each crossbar.
An `R_A` packet in one shore transfers the exact state `R_A` to the other
shore because its block quotient is complete.  If both shores owned it,
`R_A` would extend both closed shores and their colourings would glue.
Thus the owner is unique, the nonowner extends `R_A`, and disjointness of
the two extension families says that the owner rejects it.  The proof for
`R_B` is the same. \(\square\)

The membership assertion here is proved by packet transfer.  It is not
inferred from a colour assigned by the abstract spectrum audit.

### Lemma 6.2 (crossbar plus a free theta bridge)

Let `C` own the `05|12` crossbar, and enlarge its two disjoint carriers to
disjoint adjacent rails `L_05,L_12`.  If their complement contains a
carrier for any one of

\[
                         02,\quad15,\quad24,\quad45,             \tag{6.2}
\]

then `G` contains a `K_7` minor.  For the `15|02` crossbar the analogous
closing list is

\[
                         05,\quad12,\quad24,\quad45.             \tag{6.3}
\]

Thus an internally disjoint bridge across the missing bipartite cut
`{0,1,4}|{2,5}` closes unless it merely duplicates one of the two owned
crossbar demands.

#### Proof

Let `D` be the opposite full shore and let `Z_e` be the disjoint carrier
for the displayed bridge `e`.  In the table, `xL_e` abbreviates
`{x} union L_e`, and similarly for `xyZ_e`.  Each row lists four singleton
or full-shore bags followed by the remaining three bags.

\[
\begin{array}{c|c|c|c}
\text{crossbar}&e&\text{fixed bags}&\text{three remaining bags}\\ \hline
05|12&02&0,3,6,D&5L_{05},\ 2Z_{02},\ 14L_{12}\\
05|12&15&1,3,6,D&2L_{12},\ 5Z_{15},\ 04L_{05}\\
05|12&24&2,3,6,D&5L_{05},\ 1L_{12},\ 04Z_{24}\\
05|12&45&3,4,6,D&0L_{05},\ 1L_{12},\ 25Z_{45}\\ \hline
15|02&05&0,3,6,D&2L_{02},\ 5Z_{05},\ 14L_{15}\\
15|02&12&1,3,6,D&5L_{15},\ 2Z_{12},\ 04L_{02}\\
15|02&24&2,3,6,D&5L_{15},\ 0L_{02},\ 14Z_{24}\\
15|02&45&3,4,6,D&1L_{15},\ 0L_{02},\ 25Z_{45}
\end{array}                                                       \tag{6.4}
\]

Every displayed bag is connected using its named portal edge and, when
two boundary labels occur, the boundary edge joining them.  The two rail
bags are adjacent by construction.  Their unused portal contacts and the
two contacts of `Z_e` supply precisely the boundary adjacencies missing
from the three nonsingleton bags.  All remaining pairs are adjacent in
the boundary graph, or through fullness of `D`.  Hence every row of (6.4)
is a `K_7` model.  The script `equality_gate_theta_two_bit_verify.py`
independently replays all eight rows as connected pairwise adjacent bags.
\(\square\)

### Corollary 6.3 (two certified capture-or-web frames)

Assume that `G` has no `K_7` minor.  In the unique owner of `05|12`, apply
the uniform three-demand theorem to

\[
                         05,\quad12,\quad45.        \tag{6.5}
\]

Its triple-linkage outcome is excluded by the `45` row of Lemma 6.2.
Hence the actual adjacent crossbar rails either capture an entire residual
`4`- or `5`-portal class, or define an alternating rail web for the `45`
demand.
Likewise the unique owner of `15|02` carries a capture-or-web certificate
for

\[
                         15,\quad02,\quad24.        \tag{6.6}
\]

Corollary 5.2 shows that the omitted centre demand has a carrier somewhere
in each owner shore.  Therefore (6.5)--(6.6) describe forced intersection
or portal capture by the rails, not absence of the centre connectivity.

### Corollary 6.4 (crossed bridges are rail-locked)

Assume the canonical bits are crossed, and fix either crossbar together
with its unique owner and adjacent rails.  Lemma 5.3 supplies in that same
shore an external `U`--`V` bridge.  In a `K_7`-minor-free graph, every
such chosen bridge satisfies at least one of:

1. its endpoint pair is one of the two owned crossbar demands; or
2. its interior meets the union of the two rails.

For `05|12`, this follows because the other four `U`--`V` pairs are the
first list in Lemma 6.2; for `15|02`, they are the second list.  The
additional `{0,1}`--`{2,5}` bridge from Lemma 5.3 has the same conclusion,
with only two possible nonparallel pairs in either system.

Thus the crossed-bit geometry cannot survive as two independent path
witnesses: both colour-forced bridges are rail-parallel or rail-blocked.
This is a genuine intersection constraint, but it does not bound the
blocking portion of a rail.

### Warning 6.5 (component absorption defeats the naive median cut)

A clean path from a `4`-portal to a useful rail arm, internally disjoint
from both retained rails, gives one of the verified `K_7` quotients of
Lemma 6.2.  This does **not** extend to an arbitrary component of the
shore after deleting the two rail medians.  Such a component may absorb
whole terminal arms; retaining those arms in the quotient creates
fictitious branch capacity.

The exact component-contraction verifier
`theta_rail_component_absorption_verify.py` enumerates the zero-length
arms, the arm components absorbed with the `4`-portal component, its
median contacts, and its extra `2`/`5` portal contacts.  It finds many
`K_7`-negative quotients even when a useful arm or extra target portal is
absorbed.  Therefore neither condition alone implies `K_7`, and the two
rail medians do not automatically bound a nested seven-cut.

There is a further **centre-only capture** residue: all `4`-portals in the
owner shore may be the two medians themselves.  Then no component of the
median-deleted shore contains a `4`-portal at all.  The remainder may be
one component full to `S-{4}`, and its natural boundary has order eight,
not seven.  This atomic two-gate configuration is not excluded by
Sections 5--6 and must be handled by the faithful operation states of
Section 7 or an additional label-preserving exchange.

### Theorem 6.6 (the theta crossbar nonowner strictly descends)

Return to the seven-connected, proper-minor-minimal non-six-colourable,
`K_7`-minor-free theta gate.  The nonowner of either crossbar contains a
nonempty proper connected set behind a nested exact seven-cut.

#### Proof

It is enough to use the `05|12` crossbar.  Put

\[
             P=\{0,5\},\qquad Q=\{1,2\},\qquad R=\{3,4,6\}.    \tag{6.7}
\]

The blocks `P,Q` are independent in the boundary graph, `R` is a
triangle, and

\[
                       P\mid Q\mid3\mid4\mid6                  \tag{6.8}
\]

has complete block quotient.  The only nonautomatic adjacencies are
`25` between `P,Q`, `04` from `P` to `4`, and `14` from `Q` to `4`.

Let `C` be the unique packet owner from Lemma 6.1 and `D` its nonowner.
Thus `C` contains disjoint `P`- and `Q`-carriers, while `D` contains no
such pair.  Apply the audited label-free singleton-triangle two-pair web
theorem to `D`.  If a nonempty proper connected `X subset D` has

\[
 |(N_D(X)-X)\mathbin{\dot\cup}N_S(X)|=7,                         \tag{6.9}
\]

then this set is the desired nested exact cut.  Suppose no such `X`
exists.  Seven-connectivity makes every proper relative boundary have
order at least eight.  The set-terminal Two Paths theorem then gives a
bare disk web for `D`; unique portals and cutvertices violate the strict
relative bound.

The only possible two-cut form has two lobes with complementary defects
in `P` or in `Q`.  Both forms already contain `K_7`.  If `L_0,L_5` miss
respectively `0,5`, and `E` is the opposite full shore, use

\[
 \{1\}\mid\{3\}\mid\{4\}\mid\{6\}\mid
 L_0\mid(\{2\}\cup L_5)\mid(\{5\}\cup E).          \tag{6.10}
\]

For complementary defects `L_1,L_2` in `Q`, use

\[
 \{0\}\mid\{3\}\mid\{4\}\mid\{6\}\mid
 L_1\mid(\{5\}\cup L_2)\mid(\{2\}\cup E).          \tag{6.11}
\]

Every displayed set is connected and all twenty-one bag adjacencies are
literal theta-boundary or full-shore contacts.  Hence an atomic
nonsingleton nonowner is a three-connected bare web.

Disk curvature now gives at least six outer vertices of `D`, each
adjacent to all three roots in `R`, at least one root in `P`, and at least
one root in `Q`.  Choose two and split a spanning tree of `D` into adjacent
connected sets `W_0,W_1`, one containing each chosen vertex.  If `X_P,X_Q`
are the owner carriers, then

\[
 \{3\}\mid\{4\}\mid\{6\}\mid
 (P\cup X_P)\mid(Q\cup X_Q)\mid W_0\mid W_1            \tag{6.12}
\]

is a `K_7` model.  The first three bags form `R`; the two packet bags are
adjacent through `25` and see `R` through the block-quotient edges; and
each `W_i` sees all first five bags through its tagged vertex.  This
contradiction eliminates every nonsingleton atomic nonowner.

Finally, `D` cannot be a singleton.  Such a vertex has degree seven and
neighbourhood exactly `S`, while `\{0,1,2\}` is independent in `G[S]`.
Dirac's neighbourhood bound for a 7-contraction-critical graph gives
`alpha(N(d))<=d(d)-7+2=2`, a contradiction.  Thus (6.9) must occur.
The `15|02` crossbar follows symmetrically. \(\square\)

The verifier `equality_gate_theta_singleton_triangle_descent_verify.py`
checks the complete five-block quotient, both crossed-lobe models
(6.10)--(6.11), and all sixteen possible pairs of curvature tags in
(6.12).  The theorem eliminates the centre-only and absorbed-arm locks
at every atomic theta gate.  It is a strict descent theorem, not yet a
proof that an arbitrarily long sequence of changing exact seven-cuts
terminates in a contradiction.

## 7. Exact two-bit operation-state normal form

After naming the shores `C,D`, there are bits `x,y` such that

\[
 A_x,B_y\in\mathcal E_C,
 \qquad
 A_{1-x},B_{1-y}\in\mathcal E_D.                 \tag{7.1}
\]

Contracting `D union 012` forces `A_x` on the intact `C` shore, while
contracting `C union 012` forces `A_{1-x}` on `D`; the analogous
statements hold for `015` and `y`.  The two simultaneous opposite-shore
contractions `(012,45)` and `(015,24)` canonically induce `A_1` and `B_1`,
respectively, but preserve neither whole shore.  They therefore label the
bits without by themselves relating them.

Modulo interchange of `C,D`, (7.1) has two static forms:

1. **aligned:** `x=y`, so one shore accepts both merged canonical states;
2. **crossed:** `x!=y`, so the merged states are accepted on opposite
   shores.

The independent audit proves that both forms, and both labelled versions
of each, satisfy every abstract exact-block constraint.  Sections 5--6
add the strongest presently justified geometry: both shores have both
centre paths; crossed bits additionally force the two theta bridges of
Lemma 5.3 in each shore; the two crossbars have unique owners; and those
owners carry the two explicit capture-or-web frames (6.4)--(6.5).
Warning 6.5 records why this does not yet promote to a median-cut theorem:
an arbitrary component can absorb required rail arms, and all `4`-portals
may be concentrated on the two medians.

The remaining dynamic gap is consequently exact:

* if the crossbars have one owner, exchange the two rail systems in that
  shore so that one centre carrier becomes disjoint, or extract a bounded
  rail adhesion whose operated state is accepted across the opposite
  shore;
* if the crossbars have opposite owners, align the two opposed web/capture
  certificates with the canonical bits in (7.1), or extract a nested exact
  seven-cut.

No current lemma proves either exchange.  In particular, the canonical
double contractions are not boundary-faithful to either whole shore, so
their states cannot be inserted into an extension family merely because
they occur in the operated quotient.  This is the precise obstruction
left by the theta core, rather than an unproved assertion that state parity
already closes it.
