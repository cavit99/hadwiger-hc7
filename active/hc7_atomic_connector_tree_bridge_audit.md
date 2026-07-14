# Audit: the atomic connector tree and its bridges

**Status:** independent structural audit.  Lemmas 1--5 below are proved.
They do not close the separating-edge atom.  Section 7 isolates the weakest
remaining connector statement and the exact trust obligations on any proof.

## 1. Frozen local setup and a necessary wording correction

Use the atomic exact-seven separation

\[
 V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad S=W\mathbin{\dot\cup}\{u\},\quad |S|=7,
\]

where `G` is seven-connected and `K_7`-minor-free, there is no `A-R`
edge, `A` is connected and `S`-full, `R` contains two disjoint adjacent
connected `S`-full packets, and `zu` is the unique `A-u` edge.  Let `Q`
be the fixed path whose ends are the two named boundary blocks `B,C` and
whose nonempty internal path `Q^circ` lies in `A`, as supplied by the
audited bichromatic-edge localization theorem.

The path-or-`Y` assertion needs the following explicit convention.  Keep
`Q^circ` **as a subgraph**, and, if `z` is not on it, adjoin a shortest
`z`--`V(Q^circ)` path `J`.  Stop `J` at its first vertex of `Q^circ` and
put

\[
                         T=Q^circ\cup J.                 \tag{1.1}
\]

### Lemma 1.1 (literal path-or-`Y` core)

The graph `T` is a tree of maximum degree at most three with at most one
vertex of degree three.  It is a path when `J` ends at an end of
`Q^circ` (including the trivial case `z in V(Q^circ)`), and otherwise is
a subdivided `Y`.

#### Proof

By shortestness, `J` meets `Q^circ` only in its last vertex.  The union of
two paths having exactly one common end is a tree.  Only the common end can
have degree three, and it has degree three exactly when it is internal to
`Q^circ`.  \(\square\)

It is not enough to ask for an inclusion-minimal connected subgraph that
contains the **vertex set** of `Q^circ` and `z`.  Such a Steiner tree may
discard the edges of `Q^circ`; a new centre adjacent to `z` and three
vertices of `Q^circ` gives an inclusion-minimal degree-four star.  The
active goal should therefore use (1.1), not the ambiguous vertex-terminal
formulation.

## 2. Relative seven-connectivity

### Lemma 2.1 (relative cut inequality)

For every nonempty connected `D subseteq A`,

\[
                 |N_A(D)|+|N_S(D)|\ge7.                \tag{2.1}
\]

In particular, if `D` is a component of `A-X`, then

\[
                 |N_X(D)|+|N_S(D)|\ge7.                \tag{2.2}
\]

#### Proof

There is no `A-R` edge, so
`N_G(D)=N_A(D) dotunion N_S(D)`.  Deleting this set isolates the nonempty
set `D`, while the nonempty rich shore remains on the other side.  It is
therefore a vertex cut, and seven-connectivity gives (2.1).  Formula (2.2)
follows because a component of `A-X` has every `A`-neighbour in `X`.
\(\square\)

For a nontrivial `T`-bridge, let `D` be its component in `A-V(T)` and let

\[
  \operatorname{att}(D)=N_A(D)\cap V(T),\qquad
  \operatorname{supp}(D)=N_S(D).
\]

Then (2.1) gives the exact bridge budget

\[
 |\operatorname{att}(D)|+|\operatorname{supp}(D)|\ge7. \tag{2.3}
\]

Since `zu` is the unique `A-u` edge and `z in T`, no such component sees
`u`.  Hence its support has order at most six and every nontrivial bridge
has a `T`-attachment.  More particularly, one-attachment bridges are
full to all six vertices of `W`, and two-attachment bridges meet at least
five vertices of `W`.  These are contact statements, not attained-duty
carrier statements.

The same proof gives a useful lobe rule: a component behind an `r`-vertex
cut of `A` meets at least `7-r` old boundary literals.  It is the uniform
source of the familiar support-six cutvertex, support-five two-cut, and
support-four three-cut cells.

## 3. What `K_7`-minor-freeness adds

### Lemma 3.1 (no boundary-rooted `K_5` on the thin side)

There do not exist five pairwise disjoint, connected, pairwise adjacent
subgraphs `D_1,...,D_5` of `G[A union S]` such that every `D_i` contains a
literal member of `S`.

#### Proof

Let `P_1,P_2 subseteq R` be the two disjoint adjacent `S`-full packets.
They are disjoint from all five displayed sets, are adjacent to each other,
and each is adjacent to every `D_i` through a literal boundary vertex in
that set.  Thus

\[
                         P_1,P_2,D_1,\ldots,D_5
\]

are the seven bags of a literal `K_7` model, a contradiction.  \(\square\)

This is the precise rooted-minor resource available in the fully crossed
case.  Ordinary `K_5`-minor-freeness of `G[A union S]` does not follow.

## 4. A clean tree edge gives two near-full carriers

Use the standard bridge convention: a chord of `T` is a trivial bridge
with its two ends as attachments, and a component of `A-V(T)` together
with its incident edges is a nontrivial bridge.  For `h=vw in E(T)`, let
`T_v,T_w` be the components of `T-h`.  Call `h` **clean** when no
`T`-bridge other than `h` has attachments on both sides.

### Lemma 4.1 (clean-edge carrier split)

If `h` is clean, `A` has a vertex partition

\[
                         A=X\mathbin{\dot\cup}Y          \tag{4.1}
\]

such that `G[X],G[Y]` are nonempty and connected, `XY` contains the
literal edge `h`, and

\[
                 |N_S(X)|\ge6,\qquad |N_S(Y)|\ge6.     \tag{4.2}
\]

The two boundary defects are empty or disjoint singleton sets.

#### Proof

Put `T_v` in `X` and `T_w` in `Y`.  Every component of `A-V(T)` has a
nonempty attachment set by (2.3); cleanliness puts all of its attachments
on one side, so assign the component to that side.  A crossing chord would
be a crossing trivial bridge, so the only `X-Y` edge is `h`.  Each side is
connected because its tree part is connected and every assigned component
attaches to it.

Now `N_G(X) subseteq S union {w}` and
`N_G(Y) subseteq S union {v}`.  Each set separates a nonempty carrier side
from the nonempty rich shore.  Seven-connectivity proves (4.2).  Finally
`X union Y=A` is `S`-full, so the two singleton defects cannot be the same
literal.  \(\square\)

### Corollary 4.2 (exact frontier consequence)

Let `F` be the bipartite frontier used by the audited two-carrier theorem:
either `F=G[S]` is connected and bipartite, or

\[
 G[S]=K_{1,3}\mathbin{\dot\cup}K_3,
 \qquad F=K_{1,3}\mathbin{\dot\cup}K_2
\]

after retaining one triangle vertex.  The carriers in Lemma 4.1 fund the
audited exact clique-OCT state, and hence six-colour `G`, unless their two
defects are distinct vertices `p,q in V(F)` which lie in the same
bipartition side of the same connected component of `F`.

#### Proof

Give each `s in V(F)` the list of carriers which contact it.  Fullness of
their union makes every list nonempty, and (4.2) leaves at most one vertex
forced to each carrier.  Zero or one forced vertex can always be extended
to a proper two-colouring of each component of `F`.  With two forced
vertices, components can be oriented independently.  In one component,
the two vertices are forced to different carrier labels, which is proper
exactly when they lie in opposite bipartition sides.  The retained-clique
duty is automatic in the two audited frontier forms.  Apply the exact
two-carrier list theorem.  \(\square\)

Thus a clean edge closes unless it exposes exactly the already known
same-parity crossed-defect certificate.  Merely finding a clean edge is
not, by itself, the whole connector theorem.

## 5. The fully crossed bridge hull

### Lemma 5.1 (edge-linkage consequence)

If every edge of `T` is crossed by a `T`-bridge, then every two vertices
of `T` are joined by two edge-disjoint paths in `A`.

#### Proof

A bridge crossing a tree edge, together with the subpath of `T` between
two of its attachments, puts that tree edge on a cycle.  Hence no edge of
`T` is a bridge of `A`.  If one edge separated two vertices of `T`, that
edge would lie on their unique `T`-path and would be an edge of `T`, a
contradiction.  The edge form of Menger's theorem now gives two
edge-disjoint paths.  \(\square\)

This does not give internally vertex-disjoint paths.  If a cutvertex `v`
separates two `T` terminals, each relevant component of `A-v` has at least
six boundary contacts by (2.2), returning to the crossed-defect cutvertex
cell.  If no cutvertex separates the selected terminals, ordinary vertex
Menger gives the corresponding two internally disjoint paths.  Neither
conclusion assigns the paths to the two frontier duties.

For an edge `f=xy` internal to the rich shore, the audited double-
contraction split adds only the following literal signal.  In every
colouring of `G/zu/f`, either `z` sees all five alternate colours or both
`x,y` do.  An off-tree neighbour of `z` lies in a bridge attached at `z`;
if that bridge has another attachment beyond the first edge of the
`z`--`Q^circ` arm, it crosses that edge, while a sole-attachment bridge is
`W`-full by (2.3).  The five colours may nevertheless be concentrated in
one bridge and are not five boundary labels.  Saturation alone therefore
does not finish Lemma 5.1 label-faithfully.

## 6. Audit of standard tools

None of the following is currently a valid black-box completion.

1. **Gyori--Lovasz.**  Its theorem partitions a `k`-connected ambient graph
   into connected parts containing one prescribed root each (and prescribed
   sizes).  The open shore `A` is only relatively seven-connected in the
   sense of (2.1), and each carrier must hit several prescribed portal
   *sets*.  Applying the theorem to all of `G` also lets the parts leave
   `A`, destroying the adhesion and literal lists.
2. **Perfect fan augmentation and Pym linkage augmentation.**  These
   preserve selected endpoint sets while augmenting or splicing already
   available linkages.  They neither choose a consistent portal from every
   duty class nor preserve a bichromatic/equality-state label under a
   splice.  They become useful only after the two labelled carrier
   linkages have already been encoded.
3. **Tutte paths and stable bridges.**  A Tutte-path theorem needs a planar
   or otherwise specially structured ambient graph.  Stable-bridge
   rerouting needs an appropriate multi-segment path system in a
   three-connected ambient graph.  `G[A]` need not even be two-connected;
   seven-connectivity of `G` does not repair this.  The repository's
   unrestricted tree version was correctly retracted.
4. **Generalized Two Paths/web theorems.**  Humeau--Pous can be applied
   after fixing literal terminal occurrences.  It gives an uncoloured
   crossing or a web completion and its recursive parallel composition can
   organize the fully crossed hull.  It does not choose the portal
   occurrences, preserve `Pi/BC`, or turn completion edges into host edges.
   Hence it is an induction framework, not the missing pullback theorem.
5. **Recent tripod/rooted-subdivision theorems.**  The
   Hayashi--Kawarabayashi four-terminal theorem produces, under explicit
   relative separation and terminal-degree hypotheses, a diamond, a
   `K_{2,3}^+` subdivision, or a `K_5^-` subdivision containing some of the
   prescribed feet.  This may decode a nonrural four-terminal hull, but it
   guarantees neither the two prescribed duty groups nor all literal
   boundary roots.  Its output is therefore another possible crossing
   decoder, not a state-preserving carrier theorem.

The algorithmic fact that two disjoint connected subgraphs containing two
prescribed terminal sets is already a genuine multi-terminal problem is a
further warning: the one-root connected-partition theorem cannot silently
replace it.

## 7. Weakest useful next theorem and proposed mechanism

The separating-edge atom would be closed by the following statement; it is
strictly narrower than the full support-four theorem because the localized
state, the fixed connector path, the compulsory edge, and the path-or-`Y`
core are hypotheses.

> **Crossed-hull state exchange lemma.**  In the setup of Sections 1--5,
> with the legally localized compressed state and the double-contraction
> fork, either:
>
> 1. a clean edge has a non-crossed-defect list orientation, or a legal
>    bridge reassignment repairs the crossed-defect orientation, yielding
>    the two exact-duty carriers;
> 2. `G[A union S]` contains an `S`-rooted `K_5` model;
> 3. a bridge-hull separation gives a strictly smaller actual seven-
>    adhesion together with an explicit old-to-new boundary map and a
>    legally attained paired state; or
> 4. the hull gives the already specified normalized labelled `S1/S4`
>    handoff with a strictly decreasing receiving rank.

Item 2 is terminal by Lemma 3.1.  Item 1 is terminal by Corollary 4.2 and
the audited carrier theorem.  Items 3--4 exactly match the strict receiving
obligations in the active goal; an unlabelled web or `K_7^vee` does not
count.

A candidate proof mechanism is a **minimal bridge-hull induction**.

1. Work along the `z`--connector arm and choose an inclusion-minimal chain
   of bridge attachment hulls covering its non-clean edges.
2. At an end of the chain, perform only literal first-hit reroutings.  A
   newly clean edge invokes Corollary 4.2.  A same-parity defect is kept as
   a named state bit rather than discarded.
3. If the chain cannot shorten, fix the four literal terminal occurrences
   selected by its two end bridges and apply the generalized Two Paths
   theorem.  A crossing is decoded as two labelled carriers.  In a
   crossless web, recurse through the first parallel-composition node.
4. At every composition node, either a side has at most six total literal
   gate/boundary neighbours (contradicting (2.1)), exactly seven neighbours
   (candidate strict adhesion), or portals occur on both web sides.  In the
   last case, five disjoint boundary-rooted bags are the target prohibited
   by Lemma 3.1.
5. Use the common double-contraction colouring at the node where a bridge
   rerouting would otherwise reverse the orientation bit.  The missing
   alternate colour must produce the common state; saturation must be
   converted through the *same* literal bridge hull, not identified with a
   row label.

Steps 1--3 are supported by the proved lemmas and Humeau--Pous.  The new
mathematics is the label-faithful decoder in steps 4--5.  Before promotion
it must prove, rather than assume, that the five rooted bags are disjoint,
that every completion edge used by the web is replaced by a literal host
path, and that the proper-minor operation on the seven-boundary really
attains the named state.

## 8. Relation to the proposed three-gate pullback

The proposed state-preserving three-gate pullback is genuinely weaker than
`HC_7`: it assumes an actual `(1,2)` adhesion, one attained paired state,
one dutyless support-four lobe, and one exact three-gate geometry.  It is
not presently a compositional theorem for three independent reasons.

1. The verified pullback-matching barrier shows that all nine candidate
   old-label--gate pairs may be literal edges.  Nonreflection or a terminal
   exclusion must first *derive* the compatibility matching; fullness and
   old-state attainment do not.
2. A strict lobe `X subsetneq P` decreases the containing packet `P`, but
   need not decrease the previously oriented thin shore.  A recursive proof
   needs one declared global rank and must show that the receiving
   normalization decreases it.
3. Even an independent-pair matching proves neither the three inter-block
   adjacencies nor exact legal attainment of the whole new partition.
   Packet vector can also fall to `(1,1)`, for which no closed receiving
   theorem exists.

Accordingly that lemma becomes useful only after its conclusion includes
the same strict outcomes and receiving rank demanded above.  In that
strengthened form it would close a genuine infinite support-four family;
in its naive paired-pullback form it does not compose.
