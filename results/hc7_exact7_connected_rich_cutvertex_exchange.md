# Connected-rich carrier exchange

**Status:** proved and independently audited.  The finite boundary
certificates require inclusion-maximal independent witnesses.

## 1. Label-free near-full carrier lemma

Let `Pi` be a proper equality partition of the literal seven-set `S`.
Choose a maximum clique `C` among its singleton blocks, and suppose

\[
                              d_H(\Pi)=3.
\]

Thus exactly three blocks remain outside `C`.

### Lemma 1.1 (two full carriers plus one near-full carrier)

Suppose `Pi` contains a non-singleton maximal independent set `I` of
`H=G[S]` as an exact block.  If one shore contains two disjoint `S`-full packets
`P_1,P_2` and a connected subgraph `T` disjoint from both with

\[
                              |D(T)|\le1,
\]

then that shore reflects `Pi`.

#### Proof

The full packets can fund any two of the three blocks outside `C`.  It is
enough to assign the third block `B` to `T` so that `T union B` is
connected and its representative is adjacent to every literal of `C`.

There is nothing to prove if `T` is full.  Otherwise write `D(T)={a}`.
If `a in C`, maximality of `I` gives an edge from `a` to some vertex of
`I`; assign `B=I`.  Since `a notin I`, the carrier contacts every vertex
of `I`, and the boundary edge repairs its sole missing adjacency to `C`.

If `a notin C`, then `a` belongs to one of the three remaining blocks.
Assign to `T` either of the other two.  This block avoids `a`, so its union
with `T` is connected, and `T` contacts every vertex of `C`.

In both cases the other blocks go to `P_1,P_2`.  Packet fullness makes all
three representative sets pairwise adjacent.  The audited labelled-carrier
reflection lemma then contracts the representatives to a clique indexed
by the blocks of `Pi` and reflects the exact state. `square`

This is a genuinely label-free palette-to-carrier statement.  Its geometric
content is also sharp: one must still find a connected near-full carrier
disjoint from the two full packets.

### Lemma 1.2 (exact defect-two capacity obstruction)

Keep the hypotheses on `Pi,I,C,P_1,P_2`, but let the third connected
carrier `T` have

\[
                              |D(T)|\le2.
\]

The state reflects whenever one of the three blocks `B` outside `C`
satisfies

\[
 B\cap D(T)=\varnothing
 \quad\hbox{and}\quad
 N_H(c)\cap B\ne\varnothing
 \quad\hbox{for every }c\in C\cap D(T).                 \tag{1.1}
\]

If `|D(T)|=2` and no such block exists, then, writing
`D(T)={a,b}` after a swap, all of the following hold:

1. `C intersect D(T)={a}`;
2. `b in I`; and
3. neither of the other two blocks outside `C` contains a neighbour of
   `a`.

Conversely, these three conditions make (1.1) fail.

#### Proof

Condition (1.1) is precisely what is needed to assign `B` to `T` in the
audited labelled-carrier reflection lemma.  Avoiding `D(T)` makes
`T union B` connected.  Every retained singleton outside `D(T)` is
contacted directly by `T`, while the second condition supplies each
missing representative-to-singleton adjacency.  The two full packets fund
the other blocks and make all representatives pairwise adjacent.

Now suppose `D(T)={a,b}` and (1.1) fails.  If neither defect lies in `C`,
then the one or two blocks containing the defects leave another block
disjoint from `D(T)`, and the second condition is vacuous.  If both defects
lie in `C`, then `I` is disjoint from `D(T)` and maximality of `I` gives
each of `a,b` a neighbour in `I`, so `B=I` works.  Hence exactly one
defect, say `a`, lies in `C`.

Maximality gives `N_H(a) intersect I` nonempty.  Therefore `I` would
satisfy (1.1) unless the other defect `b` lies in `I`.  Once `b in I`,
the only candidate blocks are the other two outside `C`; failure is
equivalent to both avoiding `N_H(a)`.  This proves necessity and the same
reasoning proves sufficiency. `square`

Thus a failed defect-two reflection produces a canonical oriented pair:
one missed literal is a retained colour representative and the other is
locked inside the forced equality block.  This is substantially narrower
than an arbitrary portal defect and is the exact state information a
two-paths/web exchange must exploit.

## 2. Equal-defect extension of the audited adaptive theorem

The audited three-carrier theorem states that, for each of the ten hard
boundary orbits and each ordered pair of distinct defect vertices `a,b`,
one can choose an independent block `I(H,a,b)` before the state is returned
so that one full carrier and two adjacent near-full carriers reflect every
possible returned state.

### Theorem 2.1 (equal defects are also allowed)

The same statement holds without the restriction `a!=b`.

#### Proof

The first nine graph6 certificates in the audited theorem work unchanged
for all 49 ordered pairs in `S times S`.  In the standard Moser labeling

\[
 E(H)=\{01,02,03,04,12,16,26,34,35,45,56\},
\]

use `I={0,5}` when both defects lie in `{3,4}`, and use `I={1,5}`
otherwise.  The verifier

`results/hc7_exact7_equal_defect_extension.py`

enumerates every exact proper partition containing the selected block,
every maximum singleton clique, all six assignments of the three remaining
blocks, and all 49 ordered defect pairs.  It uses the corrected connectivity
condition that a carrier cannot fund any independent block containing its
missed literal.  It terminates with

`CERTIFIED equal-defect adaptive three-carrier extension`.

Hence the audited proof applies verbatim for equal defects as well.
`square`

### Theorem 2.2 (two full packets absorb every defect-two carrier)

For every one of the ten hard boundary orbits and every set
`D subseteq S` with `|D|<=2`, there is a normalized non-singleton maximal
independent block
`I=I(H,D)` such that every exact state returned from contracting `I`
with the opposite full packet reflects through two full packets and any
third connected carrier `T` with `D(T) subseteq D`.

#### Proof

Lemma 1.2 gives the exact state-by-state carrier criterion and the only
possible obstruction.  The deterministic verifier

`results/hc7_exact7_single_defect2_probe.py`

chooses `I` after `H,D` are known but before the equality state is known,
and explicitly checks that `I` is inclusion-maximal in `H`.
It then checks every exact state containing `I`, every maximum singleton
clique and every possible assignment of the partial carrier's block.  It
covers the empty defect, all seven singleton defects and all 21 two-vertex
defects in each of the ten hard orbits, and terminates with

`CERTIFIED single defect-two carrier exchange`.

The selected block has demand three in every state, so the other two
blocks are funded by the full packets and Lemma 1.2 reflects the returned
state. `square`

Theorem 2.2 is the capacity half of the desired web exchange: once a
third carrier has five literal contacts, the palette-to-label problem is
finished.  Any remaining obstruction must prevent such a carrier by
forcing at least three packet attachments around every complementary
bridge.

## 3. Connected-rich cutvertex consequence

Work in the exact packet cell

\[
 |S|=7,\qquad (\nu_L,\nu_R)=(1,2),
\]

with a hard boundary orbit, and suppose `G[R]` is connected.

### Corollary 3.1 (a rich cutvertex has exactly two lobes)

If `w` is a cutvertex of `G[R]`, then `R-w` has exactly two components.

#### Proof

Let `P_1,P_2` be disjoint `S`-full packets in `R`.  At most one contains
`w`, so one packet `Q` avoids `w` and lies in a component `D_0` of `R-w`.
Suppose there are at least three components.  Choose two other components
`D_1,D_2` and put

\[
                           X=D_1,\qquad Y=D_2\cup\{w\}.
\]

The three carriers `Q,X,Y` are pairwise disjoint and connected, and an
edge from `D_1` to `w` is an `XY` edge.  For `i=1,2`,

\[
                         N_G(D_i)\subseteq S\cup\{w\}.
\]

The opposite open shore is nonempty, so this neighbourhood is a genuine
separator.  Seven-connectivity gives `|N_S(D_i)|>=6`; hence both `X` and
`Y` are near-full.  Their missed literals may coincide, which is precisely
why Theorem 2.1 rather than only the distinct-defect theorem is needed.

Choose the independent contraction block supplied by Theorem 2.1 and
contract it together with the thin full packet.  Fullness makes it an exact
boundary block.  Strong contraction-criticality returns an arbitrary
six-colouring of that proper minor, and Theorem 2.1 reflects its actual
boundary state through `Q,X,Y`.  Palette alignment then six-colours `G`,
a contradiction.  Thus `R-w` has at most two components; because `w` is a
cutvertex it has exactly two. `square`

### Corollary 3.2 (three-attachment bridge condition)

Fix any two disjoint `S`-full packets `P_1,P_2` in a connected rich shore.
For every component

\[
                         K\text{ of }R-(P_1\cup P_2),
\]

the attachment set

\[
                A_K=N_R(K)\cap(P_1\cup P_2)
\]

has order at least three.

#### Proof

If `|A_K|<=2`, then

\[
                          N_G(K)\subseteq S\cup A_K.
\]

The nonempty opposite open shore lies beyond this neighbourhood, so it is
a genuine separator.  Seven-connectivity gives

\[
                  |N_S(K)|+|A_K|\ge7,
\]

and hence `|N_S(K)|>=5`.  Thus the connected subgraph `K`, disjoint from
both full packets, has boundary defect at most two.  Select the thin-shore
contraction block supplied by Theorem 2.2; its returned demand-three state
reflects through `P_1,P_2,K`, six-colouring `G`, a contradiction. `square`

This is independent of the order or internal structure of `K`.  It turns
the residual connected-rich problem into a stable-bridge problem: every
bridge of an extremal packet pair has at least three literal attachment
vertices on the packet union.

### Lemma 3.3 (cross-bridge triangle closure)

Let `Q` be the thin `S`-full packet and `P_1,P_2` the selected rich full
packets.  Let `K` be a connected subgraph disjoint from all three which has
a neighbour in each of `P_1,P_2`.  If `K` contacts every vertex of a
boundary triangle `T` and also contacts some `r_0 in S-T`, then `G`
contains a literal `K_7` minor.

#### Proof

Choose distinct

\[
                     r_1,r_2\in S-(T\cup\{r_0\}).
\]

The seven branch sets are

\[
 Q\cup\{r_0\},\quad P_1\cup\{r_1\},\quad
 P_2\cup\{r_2\},\quad K,\quad \{t\}\ (t\in T).
\]

They are connected and disjoint.  Fullness supplies all adjacencies among
the three anchored packet bags and from those bags to the triangle.
The contact at `r_0` joins `K` to the thin packet bag, the two rich
attachments join `K` to `P_1,P_2`, and the contacts at `T` join `K` to
the three triangle singletons.  Hence the seven bags are pairwise adjacent.
`square`

Consequently, in a residual hard boundary with two disjoint triangles,
every complementary bridge that attaches to both rich packets has one of
two sharply restricted boundary supports: it contains no full boundary
triangle, or its entire support is exactly that triangle.  In particular a
four-contact cross-bridge can contain neither boundary triangle.

## 4. Constructive residue

Combining this with the audited two-component-rich theorem gives:

* if the rich shore has two components, both are cutvertex-free;
* if the rich shore is connected, every cutvertex has exactly two lobes;
* any additional connected near-full carrier disjoint from a selected pair
  of full packets closes immediately by Lemma 1.1; and
* every component outside a selected packet pair has at least three packet
  attachments, by Corollary 3.2; and
* a bridge attached to both packets cannot contact a triangle plus any
  further boundary literal, by Lemma 3.3.

The surviving connected-rich geometry is therefore a chain-like
two-lobe articulation structure in which the two full packets block every
near-full peel.  The next constructive target is to show that this chain
either supplies the third carrier after a packet re-choice or induces an
exact two-shore adhesion state that glues.
