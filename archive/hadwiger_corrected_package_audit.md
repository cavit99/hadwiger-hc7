# Adversarial audit of the corrected Hadwiger package

This audit concerns only the corrected statements in
`hadwiger_uniform_saturation_reduction.md`,
`hadwiger_mixed_fan_repair.md`,
`hadwiger_R7_counterexample.md`, and
`hadwiger_HC7_postaudit_nearK7.md`.  It does not validate any of the old
claims that the (s=1,2), or (R_5) cells have been eliminated.

## I. Statements verified

### 1. The uniform least-counterexample reduction

Theorem 2.1 of `hadwiger_uniform_saturation_reduction.md` is correct, with
the named theorems stated there as inputs.

Let (t) be the least failing parameter and choose, among the
(K_t)-minor-free graphs of chromatic number at least (t), a graph (G)
minimal in the proper-minor order.  Then every proper minor is
((t-1))-colourable.  Deleting one vertex and then adding a fresh colour
shows (\chi(G)\le t), so

\[
  \chi(G)=t.
\]

The graph is connected and non-complete.  Since (\mathrm{HC}_{t-1}) holds,
(\chi(G)=t) forces a (K_{t-1})-minor, while the choice of (G) forbids a
(K_t)-minor.  Hence

\[
  \eta(G)=t-1.
\]

The local degree bound used in the note is also correct.  If (Q) is
(r)-contraction-critical and (u\in V(Q)), then

\[
  \alpha(Q[N(u)])\le d(u)-r+2.                 \tag{1}
\]

Indeed, for an independent (A\subseteq N(u)) larger than the right hand
side, contract the star on (A\cup\{u\}), colour the proper minor with
(r-1) colours, and expand it.  The at most (r-3) vertices of
(N(u)-A) cannot contain all the (r-2) colours different from the
contracted star's colour.  A missing colour can be put on (u), while all
vertices of (A) receive the contracted colour, contradicting
(\chi(Q)=r).  Ordinary criticality gives (\delta(G)\ge t-1); equality in
degree at a vertex, together with (1), makes its neighbourhood a clique and
produces a (K_t) subgraph.  Thus

\[
  \delta(G)\ge t.
\]

Mader's theorem applies with exactly the needed hypothesis: a non-complete
(k)-contraction-critical graph is 7-connected for (k\ge7).  The 2025
strengthening of Lafferty--Liu--Rolek--Yu additionally gives

\[
\kappa(G)\ge8\ (t\ge17),\qquad
\kappa(G)\ge9\ (t\ge29),\qquad
\kappa(G)\ge10\ (t\ge41).
\]

For a minimum-degree vertex (v), set (H=G-v) and (N=N_G(v)).  Then

\[
 \chi(H)=\eta(H)=t-1,
 \qquad \kappa(H)\ge \kappa(G)-1.
\]

The chromatic equality follows because deletion lowers chromatic number by
at most one and (H) is a proper minor.  The lower Hadwiger-number bound is
(\mathrm{HC}_{t-1}), and the upper bound follows from (H\subseteq G).
If (X) of order at most (\kappa(G)-2) separated (H), then
(X\cup\{v\}) would separate (G).

Most importantly, the claim that the **entire** neighbourhood (N) is
inclusion-minimal colour-saturating is correct.  Saturation follows because
a colour absent from (N) in a ((t-1))-colouring of (H) could be put on
(v).  For (w\in N), colour (G/vw) with (t-1) colours and let (q)
be the contracted vertex.  Restore (w) in (H) with the colour of (q).
Every (x\in N-\{w\}) was adjacent to (q) through the edge (vx), so
(w) is the unique vertex of (N) with that colour.  Thus (N-\{w\}),
and hence every proper subset of (N), is not saturating.  There is no
hidden identification or non-minor operation in this argument.

Finally, a (K_{t-1})-model in (H) all of whose bags meet (N), together
with ({v}), would be a (K_t)-model.  This proves the asserted rooted
obstruction.

### 2. The bounds (D_7=9,D_8=11,D_9=13)

The values quoted for

\[
 D_r=\max_n\left\lfloor\frac{2\operatorname{ex}_{\rm m}(n,K_r)}n\right\rfloor
\]

are correct.  The Mader--Jorgensen--Song--Thomas upper bounds make the
average degree of a (K_7,K_8,K_9)-minor-free graph strictly less than
(10,12,14), respectively.  The lower integer values do not require any
delicate equality classification: repeatedly glue copies of (K_{r-1})
along (K_{r-2}).  The resulting graph has treewidth (r-2), hence no
(K_r)-minor, and has

\[
 e=(r-2)n-\binom{r-1}{2}.
\]

For sufficiently large (n), its average degree has floor
(9,11,13) for (r=7,8,9).  Thomason's sharp complete-minor density
theorem likewise gives

\[
 D_r=(0.63817\ldots+o(1))r\sqrt{\log r};
\]

the factor (0.63817\ldots) is twice the edge-density constant
(0.31908\ldots).

### 3. The fan-refined potential

Lemma 3.1, Lemma 4.1, and Theorem 4.2 of
`hadwiger_mixed_fan_repair.md` are correct after making one harmless endpoint
convention explicit.

Here an internally disjoint family of (v)-to-(C) paths may have a common
endpoint in (C); its members have disjoint interiors.  Every path is
truncated at its first vertex of (C).  With this convention the maximum
cardinality (\mu) and minimum total length (\ell) are well-defined.  If
(\alpha) is a non-direct strongly private portal and is moved from its
contact bag to the noncontact bag containing the next path vertex, then

\[
 s'=s,\quad Z'=Z,\quad C'=C\cup\{\alpha\}.
\]

Truncating that one fan path at (\alpha) preserves its cardinality and
decreases its total length by one.  Hence either (\mu'>\mu), or
(\mu'=\mu) and (\ell'<\ell), contradicting maximality of

\[
 \Psi=(s,-|Z|,\mu,-\ell,-\textstyle\sum_i|B_i|^2).
\]

If the portal is direct, the transfer increases (s).  If it produces six
contacted bags, the contradiction is directly the assumed nonexistence of a
fully contacted model; otherwise it is a lexicographic improvement.  This is
a minor wording repair to the proof, not a missing case.  The same convention
applies in the proof that a (\Psi)-maximal model is spanning if absorbing an
unused vertex would create the fully contacted model.

The cardinality assertion in Corollary 4.3 is valid.  Fix any (y\in C).
Seven-connectivity gives seven internally disjoint (v)-(y) paths.
Truncate them at their first entries into (C).  Because no vertex of (C)
is adjacent to (v), every truncated path has an internal predecessor
portal.  Those predecessors are distinct: a common predecessor would be an
internal vertex of two of the original paths.  Thus (\mu=|L|\ge7).

The elementary consequences listed in Section 5.1 also check out: portal
pigeonholes, the double-foot conclusion, the (R2) budget, and the
unique-attachment budget all concern this one selected fan only.  Lemma 5.1
is valid.  Moving a component (K) of (B_1-\alpha) to its sole possible
private target preserves all model adjacencies; the edge from (\alpha) to
(K) supplies the new (B_1)-target adjacency in the one-private-target
case.  Therefore such a movable component must monopolise at least two
noncontact targets.

### 4. The degree-seven exterior-component reduction

Let (v) have degree seven in a hypothetical minor-minimal
(\mathrm{HC}_7) counterexample, put (S=N(v)), and let
({\cal C}) be the components of (G-N[v]).  Lemmas 3.1--3.3 and
Proposition 3.4 of `hadwiger_HC7_postaudit_nearK7.md` are correct.

Equation (1) gives (\alpha(G[S])\le2).  Every exterior component (C)
has (N(C)=S): its neighbourhood is contained in (S), and a proper subset
would be a separator of order at most six separating (C) from (v).
Contracting distinct components therefore creates independent helper
vertices, each complete to (S).

If there are at least three components, Ramsey's (R(3,3)=6) theorem gives
a triangle (t_1t_2t_3) in (S).  For three further distinct vertices
(a_1,a_2,a_3in S), the bags

\[
 \{t_1\},\{t_2\},\{t_3\},
 C_1\cup\{a_1\},C_2\cup\{a_2\},C_3\cup\{a_3\}
\]

form an (S)-meeting (K_6)-model.  Thus there are at most two exterior
components.  If there are two and (G[S]) has a (K_4) subgraph, four
singleton bags plus two helper bags give the same contradiction.  More
generally, a (K_4)-model in (G[S]) using at most five vertices leaves at
least two **distinct** unused vertices of the seven-element set (S), so
Lemma 3.3 is sound.

The external seven-vertex lemma used in Proposition 3.4 has exactly the
needed hypotheses:

> every seven-vertex graph (J) with (\alpha(J)\le2) and no (K_4)
> subgraph contains a spanning Moser spindle.

As an independent finite check, among the 1044 unlabeled graphs of order
seven, exactly nine satisfy these two hypotheses and every one contains the
displayed spanning Moser spindle.  Given that spindle, the case analysis in
Proposition 3.4 is correct.  Adding (ap) or (aq) produces a (K_4);
adding a (Y)-edge such as (bq) gives the five-vertex model
({a},\{d\},\{e\},\{b,q\}); and any two (X)-edges give a (K_4)-model
on at most five vertices.  Hence the only unclosed local graphs are the
spindle and a one-(X)-edge extension, up to isomorphism.

There is a further unconditional consequence of a degree-seven colouring.
In every proper six-colouring of (H=G-v), one colour occurs twice on
(S), say at (a,b), and the other five colours occur uniquely on a set
(U).  Every two vertices of (U) are Kempe-connected, by the usual swap
argument.  Let

\[
 F=\overline{H[U]}.
\]

Since (\alpha(H[U])\le2), (F) is triangle-free, and Mantel's theorem
gives (|E(F)|\le6).  Kriesell--Mohr, Theorem 7, states exactly that every
five-vertex graph with at most six edges has property ((*)).  Restrict
the six-colouring to the union of the five unique colour classes; all the
relevant Kempe chains remain in this five-coloured subgraph.  Property
((*)) gives a rooted (F)-certificate.  For every nonedge of (F), the
corresponding two roots are adjacent in (H[U]), so that root edge supplies
the missing bag adjacency.  Consequently (H) contains a (K_5)-model
rooted at (U), using only the five unique colour classes.

The exact remaining step in this formulation is to find, disjoint from those
five bags, a connected sixth bag meeting ({a,b}) and adjacent to every
one of the five rooted bags.

### 5. The near-(K_7) normalization

The Norin--Totschnig input has the exact contrapositive used in the note:
every non-6-colourable graph contains (K_7^\vee) as a minor, where the two
deleted edges have a common end.

Lemmas 4.1 and 4.2 and the spanning normalization in Section 4 of
`hadwiger_HC7_postaudit_nearK7.md` are correct.  In a 7-connected graph,
an actual seven-vertex (K_7^\vee) or (K_7^-) subgraph has an outside
component meeting all seven vertices: if it missed one, its at most six
attachments would separate it.  Absorbing that component into a deficient
vertex repairs the missing edge or edges.

For a (K_7^\vee)-model with deficient bag (A) and non-required pairs
(AB,AC), an outside component meeting all three of (A,B,C) can be
absorbed into (A), producing a (K_7)-model.  Otherwise it has at least
seven attachment vertices in at most six bags, so one bag is multiply hit.

Making the model spanning is legitimate: assign each outside component to
one bag it meets.  In the (K_7)-minor-free setting no such assignment can
create a formerly missing adjacency, because the component witnessing that
adjacency would already allow the corresponding stronger model.  Thus:

* if a (K_7^-)-minor exists, its two nonadjacent spanning bags are genuinely
  anticomplete and the deficient bag has at least seven neighbours in the
  other five bags;
* if no (K_7^-)-minor exists, both deficient pairs in a spanning
  (K_7^\vee)-model are genuinely anticomplete and the deficient bag has at
  least seven neighbours in the four fully adjacent bags.

The stated portal-concentration conclusion follows by pigeonhole.

### 6. The universal-root counterexample and planar join theorem

The construction in `hadwiger_R7_counterexample.md` is valid.  For the
icosahedron (I) with one edge (tu_0) deleted, the resulting graph (F)
is planar and 4-connected, and the displayed colouring is proper and rainbow
on the facial cycle (t,u_1,u_0,u_4).  The odd wheel in (F) proves
(\chi(F)=\eta(F)=4).  For (H=K_2\vee F), join additivity of chromatic
number and the elementary fact that a universal vertex raises the Hadwiger
number by exactly one give

\[
 \kappa(H)=6,\qquad \chi(H)=\eta(H)=6.
\]

A rooted (K_6)-model at the two join vertices and the four facial roots
would leave four disjoint, pairwise adjacent connected bags in (F) rooted
at alternating vertices of one face.  The two opposite bag adjacencies give
two disjoint crossing paths, impossible in a disc.  Hence the asserted
universal rainbow-rooted statement is false.

Theorem 5.1 is also correct.  The Fabila-Monroy--Wood theorem applies because
(P) is 3-connected: four prescribed roots have a rooted (K_4)-model iff
they are not all incident with one face.  If a rainbow quadruple lies on one
face but (S) has a vertex outside it, replacing the root of the same colour
gives a non-cofacial quadruple; two faces of a 3-connected plane graph cannot
share three vertices.  If all of (S) lies on that face, add a face-centre
adjacent to its boundary and apply the Four Colour Theorem.  The boundary,
and therefore (S), avoids the centre's colour, contradicting saturation.
Corollaries 5.2 and 5.3 follow exactly as written.

The complement/pseudoforest criteria in the uniform and (R_7) notes are
also correct.  Saturation of a rainbow (k)-set forces every root pair into
one bichromatic component.  Kriesell--Mohr supplies the adjacencies indexed
by the complement graph when that complement is a pseudoforest; the actual
root edges supply all remaining adjacencies.

## II. False, unsupported, or overstated statements

### 1. None of the package proves Hadwiger's conjecture

The uniform theorem is a reduction.  It leaves a neighbourhood
(N=N(v)) of order between (t) and (D_t), with contraction-colouring
witnesses, and asks for a (K_{t-1})-model all of whose bags meet (N).
No audited lemma produces that model.  In particular, the valid
(\Psi)-fan theorem only produces one all-rigid fan for one extremal model.

### 2. The old (s=1,s=2,R_5) eliminations remain unsupported

The (\Psi)-repair does not imply that every maximum fan is rigid, does not
preserve old (Phi)-neutral trades, and does not prove the locked-core axiom
needed for the singleton-(U) descents.  Consequently the old claimed
elimination of (s=2), the final (s=1) contradiction, and the (R_5)
closure do not follow.  The explicit graph in
`hadwiger_R5_local_obstruction_audit.md` shows that the local (R_5) axioms
are consistent; it is not a counterexample because it is neither
7-connected nor of minimum degree seven.

There is also a nomenclature issue: failure of condition 1 in the new
definition includes a singleton source bag, whereas a singleton vertex is
not a cutvertex in the standard sense.  Statements using "(R1) means
cutvertex" must either exclude singleton bags or say "non-removable" rather
than "cutvertex".

### 3. The fan cardinality needs the common-end convention

If "fan" is instead given its other common definition in which the endpoints
in (C) must be distinct, 7-connectivity alone does not imply seven such
paths when (|C|<7).  Corollary 4.3 is correct only with the internally
disjoint/common-(C)-endpoint convention proved above, or with an additional
(|C|\ge7) hypothesis.  The note should state this convention explicitly.

### 4. The size-six saturating cell is not counterexample-derived

Proposition 6.1 of `hadwiger_R7_counterexample.md` is true but superseded.
The contraction witness proves that no proper subset of (N(v)) is
saturating, so the inclusion-minimal set is (N(v)) itself and has order
7, 8, or 9 in the (\mathrm{HC}_7) reduction.  Lemma 6.3 and Corollary 7.2
therefore describe a valid abstract size-six cell, but that cell is vacuous
for a minor-minimal counterexample.

### 5. Norin--Totschnig Claim 4.4 does not eliminate the Moser residual here

In the proof of their stronger excluded-(K_7^\vee) theorem,
Norin--Totschnig contract (vu'_3,vu'_4), obtain five uniquely coloured
roots (u_1,\ldots,u_5), and use a rooted (C_5)-model in

\[
 G-\{v,u'_3,u'_4\}
\]

to construct a (K_7^\vee)-minor.  This is a contradiction in their setting,
where (K_7^\vee) is excluded.  It is **not** a contradiction in a
hypothetical (\mathrm{HC}_7) counterexample, which is known to contain such
a minor.

One cannot simply absorb an exterior component into the deficient singleton
bag to turn that model into (K_7).  The five rooted (C_5) bags are allowed
to use vertices from every component of (G-N[v]); neither the theorem nor
the construction leaves an entire exterior component outside the seven
bags.  An untouched component, or a disjoint reassignment preserving the
five rooted bags, is an unproved extra requirement.  Therefore the proposed
deductions

\[
 d(v)=7\Longrightarrow \omega(G[N(v)])\ge4,
 \qquad
 m=1,
 \qquad
 \omega(G[N(v)])=4
\]

do not follow from Claim 4.4.  The valid residual remains Proposition 3.4
together with the rooted-(K_5)-plus-sixth-bag gap in Part I.4.

### 6. Citation boundary

The Moser-spindle classification, Mader connectivity, the exact excluded
minor edge bounds, the rooted-(K_4) characterization, Kriesell--Mohr's
property-((*)) theorems, Norin--Totschnig's near-clique theorem, the Four
Colour Theorem, and (\mathrm{HC}_6) are external named inputs.  Their
hypotheses match every audited use above, but the present files do not contain
self-contained proofs of those theorems.  They must remain explicitly cited
inputs rather than being described as elementary consequences of the local
arguments.

