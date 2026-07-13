# Independent audit: exact-seven thin-shore exchange

## Verdict

**GREEN after four explicit corrections made in place.**  Under the
written strong `HC_7` hypotheses, Theorem 1, Corollaries 2.1--2.3,
Lemma 3.1, the corrected sufficient form of Proposition 4.1,
Proposition 4.2, Corollary 4.3, Theorem 4.4, and Corollary 4.5 are valid.

The corrections were:

1. Theorem 1 was strengthened, legitimately, from a partition
   `L=X dotcup Y` to two disjoint adjacent connected subgraphs
   `X,Y subseteq L`.  The proof never needs the unused vertices of `L`.
2. The distribution sentence in Case 4 was made exact: the only failure
   occurs when one initial block is a singleton and the leftover set is
   empty.
3. The two-vertex shore, which is not covered by the cutvertex argument
   under the usual definition, was closed explicitly before asserting
   that the residue has order at least three.
4. Proposition 4.1 no longer says that its raw lobe-defect test is an
   exact characterization for `k=2`.  Contacts from the cut vertices
   `p,q` to `S` can shrink the actual defects, so the displayed test is
   sufficient, not necessary.

This audit does **not** close the remaining 2-connected thin shore.  It
does not produce a two-vertex transversal, a rural embedding, an apex
pair, or a common equality state beyond the explicit carrier hypotheses.

## 1. Hypotheses and audited dependency

The note uses contraction-criticality in the strong form

\[
 \chi(G)=7\quad\hbox{and every proper minor of }G\hbox{ is
 six-colourable}.
\]

The separation is actual: the two open shores are nonempty and
anticomplete, with literal common boundary `S` of order seven.  The
input `results/hc7_exact_seven_packet_packing.md` has an independent
GREEN audit.  In the `(nu_L,nu_R)=(1,3)` cell it gives:

* every open-shore component is `S`-full;
* `L` is connected, since two components would be two disjoint full
  packets;
* `omega(G[S])<=2`, hence `G[S]` is triangle-free; and
* any admissible one-block boundary state would splice two
  proper-minor colourings and six-colour `G`.

These are exactly the packet-theorem consequences used below.

## 2. Theorem 1: contact count and literal models

Let

\[
 C=N_S(X)\cap N_S(Y).
\]

Since each of the disjoint connected adjacent sets `X,Y` misses at most
one member of `S`, `|C|>=5`.  No step needs `X union Y=L`.

### Case 1

If `qq'` is an edge of `G[C]`, choose distinct
`r_1,r_2,r_3 in C-{q,q'}` and put

\[
 A_i=P_i\cup\{r_i\}\quad(1\le i\le3).
\]

The complete audit of the 21 required adjacencies among

\[
 A_1,A_2,A_3,X,Y,\{q\},\{q'\}
\]

is as follows.

| Bag pairs | Number | Literal witness |
|---|---:|---|
| `A_i A_j`, `i<j` | 3 | `P_i` has a neighbour at the literal anchor `r_j` |
| `A_i X` | 3 | `r_i in N_S(X)` |
| `A_i Y` | 3 | `r_i in N_S(Y)` |
| `A_i {q}` | 3 | `P_i` is full at `q` |
| `A_i {q'}` | 3 | `P_i` is full at `q'` |
| `XY` | 1 | the assumed `XY` edge |
| `X{q},X{q'}` | 2 | `q,q' in C` |
| `Y{q},Y{q'}` | 2 | `q,q' in C` |
| `{q}{q'}` | 1 | the edge `qq'` |

The count is `3+3+3+3+3+1+2+2+1=21`.  Every `A_i` is connected because
`P_i` contacts its anchor, and all seven bags are disjoint.  Thus this is
a literal `K_7` model.

### Cases 2 and the low-degree subcase of Case 3

After Case 1, `C` is independent.

* If one defect is empty or the two defects coincide, then
  `S-{d}` is independent for a suitable `d`; the partition
  `(S-{d}) | {d}` is admissible.
* With distinct defects `a,b`, `C=S-{a,b}` is independent.  If `ab` is
  an edge, `C | {a,b}` is admissible.
* If `a,b` have a common neighbour `c` and both have boundary degree
  one, then `S-{a,c}` is independent and `{a,c}` is a clique.

In each instance one full packet in either shore funds the same exact
one-block state.  Explicitly, contract `P union I` in a proper minor.
Its representative and the clique `Q` have distinct colours; restricting
to the untouched opposite closed shore and expanding only the independent
literal block `I` gives exactly `I | Q`.  Repeating from the other shore,
permuting the six colour names, and gluing is legitimate because the open
shores are anticomplete.  No internal packet is expanded.

### Literal model in the remaining common-neighbour subcase

Assume, after symmetry, that `a` has distinct neighbours `c,x in C`,
where `c` is also adjacent to `b`, and enumerate

\[
 \{r_1,r_2,r_3\}=S-\{a,b,c,x\}.
\]

Put `A_i=P_i union {r_i}`, `B=X union {x}`, `D=Y`,
`E={a}`, and `F={c}`.  The 21 adjacencies have the following complete
certificate.

| Bag pairs | Number | Literal witness |
|---|---:|---|
| `A_i A_j`, `i<j` | 3 | `P_i-r_j` by fullness |
| `A_i B` | 3 | `r_i-X` |
| `A_i D` | 3 | `r_i-Y` |
| `A_i E` | 3 | `P_i-a` |
| `A_i F` | 3 | `P_i-c` |
| `BD` | 1 | the assumed `XY` edge |
| `BE` | 1 | `xa` |
| `BF` | 1 | `X-c` |
| `DE` | 1 | `Y-a`, since `Y` misses only `b` |
| `DF` | 1 | `Y-c` |
| `EF` | 1 | `ac` |

Again the total is 21.  Connectivity of `B` follows from `x in N_S(X)`;
the other bags are visibly connected and all are disjoint.  The unused
boundary vertex `b` causes no problem.

## 3. Case 4: the exact two-block state

Now `a,b` have disjoint neighbourhoods in the independent set `C`.  The
initial sets

\[
 J_X^0=\{b\}\cup N_S(a),\qquad
 J_Y^0=\{a\}\cup N_S(b)
\]

are disjoint and independent.  A leftover vertex in
`C-(N_S(a) union N_S(b))` is adjacent to neither `a` nor `b`, so it may
be assigned to either block without destroying independence.  Both
blocks can be made nontrivial except when exactly one initial block is a
singleton and no leftover exists.  In that exception, respectively
`S-{b}` or `S-{a}` is independent, so the already audited one-block
splice applies.  If both initial blocks are singletons, all five vertices
of `C` are leftover and there is ample room for both blocks.

As a dependency-free finite check, all `32^2=1024` possible pairs of
neighbourhoods of `a,b` in the five-element set `C` were enumerated.
The common-neighbour model/state cases and this disjoint-neighbour
distribution cover every pair; there were zero uncovered patterns.

For the nontrivial blocks `J_X,J_Y`, the sets

\[
 X\cup J_X,\qquad Y\cup J_Y
\]

are disjoint and connected: every literal vertex assigned to a block
has a neighbour in its carrier.  They are adjacent through the `XY`
edge.  Contracting both therefore gives a proper minor in which the two
representatives are adjacent.  Restrict a six-colouring of this minor to
`R` and the two representatives and expand only the literal independent
sets.  This gives a proper colouring of `G[R union S]` whose boundary
partition is **exactly** `J_X | J_Y`.

Crucially, unused vertices of `L-(X union Y)` are not expanded or
coloured on this side; they are simply absent from the restriction.  In
the reverse direction, contract

\[
 P_1\cup J_X,\qquad P_2\cup J_Y
\]

using two of the three disjoint full packets in `R`.  Packet fullness
makes the representatives adjacent.  Restricting that minor colouring
to `L union S` gives the same exact two-block state and colours every
unused vertex of `L`.  A palette permutation aligns the two block
colours, and the closed-shore colourings glue.  This verifies both
proper-minor uses and explains why the strengthened theorem does not
require `X union Y=L`.

## 4. Corollaries 2.1--2.3

If `z` is a cutvertex of connected `L`, every component `C` of `L-z`
has a neighbour at `z`, and

\[
 N_G(C)\subseteq S\cup\{z\}.
\]

The opposite shore and another component give a nonempty far side, so
seven-connectivity applies to this neighbourhood and yields
`|N_S(C)|>=6`.  Taking one component for `X` and the connected remainder
for `Y` supplies two adjacent near-full connected sets.  Theorem 1
closes every cutvertex shore.

If `L={x}`, actual separation and fullness give `N_G(x)=S`, hence
`d_G(x)=7`.  Dirac's neighbourhood inequality for a strongly
7-contraction-critical graph gives

\[
 \alpha(G[N(x)])\le d_G(x)-7+2=2.
\]

But `nu_L+nu_R=4`, so the packet theorem gives
`omega(G[S])<=2`; thus `G[S]` is triangle-free.  The Ramsey fact
`R(3,3)=6` gives an independent triple in a triangle-free graph on seven
vertices, contradicting Dirac's bound.

The usual definition of 2-connected requires at least three vertices,
and a connected two-vertex graph has no cutvertex.  This formerly missing
case is now explicit: if `L=xy`, then minimum degree at least seven and
the absence of edges to the opposite shore give
`|N_S(x)|,|N_S(y)|>=6`.  The singleton sets `{x},{y}` satisfy Theorem 1.
Therefore every surviving thin shore is genuinely 2-connected and has
order at least three.  The wording about block chains has also been
restricted to chains with at least two blocks, avoiding the convention
under which a single 2-connected block is a trivial block chain.

## 5. Lemma 3.1

For an admissible partition `S=I_1 dotcup I_2 dotcup Q`, each
`T_i union I_i` is connected and the two carriers are disjoint.  The
mutual-carrier hypothesis makes their contracted representatives
adjacent.  The singleton-contact hypothesis makes every representative
adjacent to every literal `q in Q`, and `Q` is a clique.  Thus these
representatives together with `Q` form a clique of order at most five,
forcing distinct boundary-block colours in any proper-minor
six-colouring.

Restricting to `R union S` therefore funds exactly the displayed state.
Two of the three full packets in `R` fund the same state on `L union S`.
The palette alignment and gluing are the same legitimate operations as
in Theorem 1.  The lemma correctly warns that adjacency of the two block
carriers alone is insufficient when a singleton in `Q` sees neither the
carrier nor its independent block.

## 6. Proposition 4.1

Let `C_i` be a component of `L-{p,q}`.  Since `L` is 2-connected, each
`C_i` has a neighbour at both `p` and `q`; otherwise one of the cut
vertices alone disconnects it.  Now

\[
 N_G(C_i)\subseteq S\cup\{p,q\},
\]

and seven-connectivity gives `|N_S(C_i)|>=5`, so every raw lobe defect
`D_i` has order at most two.

For a nonempty group `A`, the union of its lobes has raw defect

\[
 \bigcap_{i\in A}D_i.
\]

Adding `p` to one group and `q` to the other can only shrink these
defects.  Both grouped sets are connected, cover `L`, and are adjacent,
because every lobe meets both cut vertices.  Hence two raw intersections
of order at most one are a valid sufficient certificate for Theorem 1.

The set-family argument is correct: an intersection has order two
exactly when every member of the group is the same 2-set.  For `k>=4`,
unless some 2-set occurs at least `k-1` times, the indices can be split
into two groups neither of which is monochromatic in a 2-set (or each
receives a defect of order at most one).  For `k=3`, failure of this raw
certificate has exactly the two listed forms.  For `k=2`, the raw test
guarantees closure when both individual defects have order at most one.

The old word “exactly” for `k=2` was false.  For example, a lobe may
have raw defect `{a,b}` while `p` contacts `a`, so the actual defect of
`{p} union C_i` is at most `{b}`.  The corrected proposition explicitly
allows contacts at `p,q` to close some listed exceptional raw patterns.

## 7. Proposition 4.2 and Corollary 4.3

Assume `k>=3` and two lobes `C_1,C_2` have common raw defect
`{a,b}`.  Let `H` consist of `p,q` and all other lobes.

The claim that `H+pq` is 2-connected is sound.  Every lobe meets both
`p` and `q`.  Deleting one of `p,q` leaves the other joined to every
lobe.  If an internal vertex `z` of a lobe is deleted, every component
of that lobe minus `z` must still meet `p` or `q`; otherwise `z` would
be a cutvertex of the 2-connected graph `L`.  The artificial edge `pq`
then joins all surviving pieces.

Because `C_1,C_2` miss `a,b`, every `L`-neighbour of `a` or `b` lies in
`H`.  The two nonempty portal sets

\[
 A=N_L(a)\cap V(H),\qquad B=N_L(b)\cap V(H)
\]

have distinct representatives.  Failure of a two-set SDR, with both
sets nonempty, means `A=B={z}`.  Then

\[
 \{z\}\cup(S-\{a,b\})
\]

is a six-vertex cut: after its deletion the nonempty lobes `C_1,C_2`
have no edge to the remaining boundary vertices `a,b`, `z` was the only
`a`- or `b`-portal anywhere in `L`, and the actual separation has no
open-shore cross-edge.  This contradicts seven-connectivity.

Choose distinct `r in A`, `s in B`.  The set form of Menger in the
2-connected graph `H+pq` gives an unpaired two-linkage from `{p,q}` to
`{r,s}`.  This remains true when the source and target sets overlap:
use a trivial path at a common vertex and connectivity after deleting
it; if they are disjoint, no one-vertex separator can separate the two
sets in a 2-connected graph.  Relabel `p,q` if necessary to obtain
disjoint `p-r` and `q-s` paths.  Neither path can use the artificial
edge `pq`, because it would then contain both source vertices and meet
the other path.

Adjoining the first path and `p` to `C_1`, and the second path and `q`
to `C_2`, gives disjoint connected sets.  They are adjacent through a
`C_1-q` edge.  The first lobe already contacts `S-{a,b}` and its path
terminal repairs `a`, so it misses at most `b`; symmetrically the second
set misses at most `a`.  The strengthened Theorem 1 applies.  Every
connectivity, disjointness, and literal-contact assertion in Proposition
4.2 is therefore verified.

The corollary follows exactly.  For `k>=4`, Proposition 4.1 leaves a
2-set repeated at least `k-1>=3` times, which Proposition 4.2 closes.
For `k=3`, every repeated defect pair closes, including the
small-defect-plus-equal-pair exception.  Hence any three-lobe raw residue
has three pairwise distinct 2-set defects.  Nothing is asserted about
the unresolved two-lobe case.

## 8. Theorem 4.4 and the exact two-lobe frontier

**GREEN.**  For each of three lobes `C_i`, seven-connectivity gives a
raw defect `D_i` of order at most two.  Therefore

\[
 |D_1\cup D_2\cup D_3|\le6<7,
\]

so a literal boundary vertex `t` lies outside all three defects and is
contacted by all three lobes.  After deleting `t`, each contact list

\[
 L_i=N_S(C_i)-\{t\}
\]

has order at least four in the six-element set `S-{t}`.  Hall's
condition for the three lists is immediate but valid: a union of one,
two, or three lists has order at least four, hence at least the number
of lists in the subfamily.  Thus distinct representatives
`x_i in L_i` exist.  Exhaustive enumeration of all
`29^3=24,389` ordered triples of subsets `D_i subseteq S` of order at
most two found no failure of either the common-`t` choice or the SDR.

Let `r_1,r_2,r_3` be the three remaining boundary vertices and use the
seven displayed bags

\[
 A_1=C_1\cup\{p,x_1\},\quad
 A_2=C_2\cup\{q,x_2\},\quad
 A_3=C_3\cup\{x_3\},\quad
 B_i=P_i\cup\{r_i\},\quad T=\{t\}.
\]

They are disjoint.  Each `A_i` is connected because its lobe contacts
its assigned cut vertex, when present, and its anchor `x_i`; each `B_i`
is connected by packet fullness.  All 21 adjacencies have literal
witnesses:

| Bag pairs | Number | Literal witness |
|---|---:|---|
| among `A_1,A_2,A_3` | 3 | `C_1-q`, `C_3-p`, and `C_3-q` |
| `A_i T` | 3 | `C_i-t` |
| among `B_1,B_2,B_3` | 3 | `P_i-r_j` for `i!=j` |
| `B_i A_j` | 9 | `P_i-x_j` |
| `B_i T` | 3 | `P_i-t` |

The total is `3+3+3+9+3=21`.  Hence this is a literal `K_7` model,
with no palette or contraction issue.  Theorem 4.4 supersedes the
defect-pattern residue of Propositions 4.1 and 4.2 whenever a 2-cut has
at least three lobes.  A 2-cut has at least two components by definition,
so Corollary 4.5 correctly says that every surviving 2-cut has exactly
two lobes.

## 9. Novelty/overlap within the repository

The two engines are not new in isolation:

* packet-plus-anchor lifting and exact packet-funded state transfer are
  already audited in `hc7_exact_seven_packet_packing.md`; and
* carrier contraction followed by restriction to the untouched shore is
  the repository's established bounded-adhesion gluing mechanism.

The useful new result is their exact combination in Theorem 1: **any two
disjoint adjacent connected subgraphs of the packet-thin shore which
each miss at most one literal boundary vertex close the `(1,3)` cell**.
No duplicate of this label-free strengthened formulation was found among
the current audited `results/` notes.  Its cutvertex closure eliminates
an infinite family, and Proposition 4.1 supplies a reusable coherent-
defect necessary condition at branching 2-cuts.  This is a repository
novelty assessment, not a claim of novelty relative to the literature.

## 10. Trust boundary

The proof uses all of the following essentially:

* three disjoint full packets on the rich shore for the literal models;
* an `XY` edge for both the literal models and the two-block state;
* defect at most one for each carrier, giving five common anchors; and
* strong proper-minor six-colourability for every state transfer.

No counterexample survives these full hypotheses.  Dropping any of these
conditions is not justified by the proof.  In particular, the coherent
raw 2-cut patterns left by Proposition 4.1 are not contradictions; the
2-connected labelled-society residue remains open.  Theorem 4.4 now
closes every 2-cut with at least three lobes, but the exact two-lobe
frontier still needs the proposed block-terminal Two-Paths/web or another
genuinely new exchange theorem.
