# The bichromatic \(K_6^-\) gate: peel, exact adhesion, or three-path capacity

## 1. Setup

Let \(H\) contain six pairwise disjoint connected sets

\[
                 A,B,R_1,R_2,R_3,R_4.             \tag{1.1}
\]

The sets \(R_1,\ldots,R_4\) are pairwise adjacent, each of them is
adjacent to both \(A\) and \(B\), and \(A,B\) are anticomplete.  Thus
(1.1) is a \(K_6^-\)-model whose deficient pair is \(AB\).  Suppose in
addition that there are distinct roots

\[
             x_i\in R_i\cap N_H(A)\cap N_H(B)
             \qquad(i\in[4]).                     \tag{1.2}
\]

In the antipodal Moser gate of
`hadwiger_palette_deletion_rooted_core.md`, the two gate sets are
\(K_0,K_{56}\), the roots are \(1,2,3,4\), and (1.2) follows from the
literal boundary edges: \(0\) sees all four roots, while \(6\) sees
\(1,2\) and \(5\) sees \(3,4\).

The point of this note is that the four rooted bags cannot be treated as
an amorphous separator.  The four length-two paths

\[
                         A-x_i-B                  \tag{1.3}
\]

reserve four units of gate capacity.  Six-connectivity supplies two more
units, or an exact adhesion, without any Moser labels.

## 2. The fixed-root capacity dichotomy

### Lemma 2.1 (a clean gate connector repairs the near-clique)

If \(H\) contains an \(A\)-to-\(B\) path whose internal vertices avoid
\(R_1\cup\cdots\cup R_4\), then the six sets in (1.1) can be changed
into a \(K_6\)-model.

#### Proof

Choose such a path shortest, and absorb all of its internal vertices into
\(A\).  The enlarged \(A\) is connected and is adjacent to \(B\) at the
last edge of the path.  It remains disjoint from every \(R_i\), and all
the old model adjacencies remain.  Hence the six resulting sets form a
\(K_6\)-model. \(\square\)

### Theorem 2.2 (three-path capacity or an exact rooted adhesion)

Assume that \(H\) is six-connected and satisfies (1.1)--(1.2).  Put

\[
                         X=\{x_1,x_2,x_3,x_4\}.
\]

Then exactly one of the following alternatives can be selected.

1. There are three internally vertex-disjoint \(A\)-to-\(B\) paths in
   \(H-X\).
2. There are vertices \(p,q\notin A\cup B\cup X\) such that
   \(X\cup\{p,q\}\) separates \(A\) from \(B\) in \(H\).

In outcome 2 the displayed set is an exact six-cut of \(H\).  If
\(H=G-v\), where \(G\) is seven-connected, then

\[
                     \{v\}\cup X\cup\{p,q\}       \tag{2.1}
\]

is an exact seven-cut of \(G\).

#### Proof

The graph \(H-X\) is two-connected: deleting at most one further vertex
from it deletes at most five vertices from the six-connected graph
\(H\).  In particular no set of order at most one separates \(A\) from
\(B\) in \(H-X\).

Apply the vertex form of Menger's theorem in \(H-X\) to the two connected
sets \(A,B\).  If their local connectivity is at least three, Menger gives
outcome 1.  Otherwise a minimum \(A\)-\(B\) separator in \(H-X\) has
order exactly two; call it \(\{p,q\}\).  Then
\(X\cup\{p,q\}\) separates \(A\) from \(B\) in \(H\).  Its order is
six, so it is an exact six-cut.

Finally, when \(H=G-v\), the set in (2.1) separates the same two
nonempty sides in \(G\) and has order seven.  Seven-connectivity makes it
an exact seven-cut. \(\square\)

### Corollary 2.3 (the two additional capacity paths)

Even in outcome 2, \(H-X\) contains two internally vertex-disjoint
\(A\)-to-\(B\) paths.  Together with the four literal paths (1.3), these
give six internally disjoint gate routes, four of which retain their
prescribed roots.  If no \(K_6\)-model exists, each of the two additional
routes meets \(R_1\cup\cdots\cup R_4\) by Lemma 2.1.

This is the precise capacity input for a two-shore web exchange.  It is
stronger than an unrooted application of Menger: the first four units are
fixed pointwise before the other two are found.

## 3. Exact peel certificates

The capacity paths become useful as soon as they enter and leave a rooted
bag through detachable pieces.  The following certificates record exactly
what must be preserved; neither statement hides a branch-set adjacency.

### Lemma 3.1 (one-root gate peel)

In the setup (1.1), suppose for some \(i\) that

\[
                         R_i=P\mathbin{\dot\cup}Q
\]

where \(P,Q\) are nonempty connected and adjacent.  If

* \(P\) is adjacent to both \(A\) and \(B\); and
* \(Q\) is adjacent to \(B\) and to every \(R_j\), \(j\ne i\),

then \(H\) contains a \(K_6\)-minor.  The same holds with \(A,B\)
interchanged.

#### Proof

Use the six bags

\[
             A\cup P,\quad B,\quad Q,\quad
             R_j\ (j\ne i).
\]

The first bag is connected and meets \(B\) through the \(P\)-\(B\)
edge.  It meets \(Q\) through the \(P\)-\(Q\) edge and meets every
other rooted bag through the old contacts of \(A\).  The hypotheses on
\(Q\) give all its remaining contacts.  All other pairs were adjacent
in (1.1). \(\square\)

When \(x_i\in P\), the first bullet is automatic from (1.2).  Thus a
surviving rooted bag has no root-side peel whose residue retains the
opposite gate and the other three rooted-bag contacts.

### Lemma 3.2 (matched two-root gate peel)

Assume in addition that \(x_1x_2\in E(H)\).  For \(i=1,2\), let

\[
                  R_i=P_i\mathbin{\dot\cup}Q_i
\]

be a partition into nonempty connected adjacent sets with
\(x_i\in P_i\).  Suppose

1. \(Q_1Q_2\ne\varnothing\);
2. \(Q_i\) is adjacent to both \(R_3,R_4\), for \(i=1,2\);
3. \(A\) is adjacent to \(Q_2\), and \(B\) is adjacent to \(Q_1\).

Then \(H\) contains a \(K_6\)-minor.

More generally, in item 3 the contact \(A Q_2\) may be replaced by
\(P_1Q_2\), and \(B Q_1\) may be replaced by \(P_2Q_1\).

#### Proof

Use

\[
 A\cup P_1,\quad B\cup P_2,\quad Q_1,\quad Q_2,
 R_3,\quad R_4.                                   \tag{3.1}
\]

The first two bags are connected by (1.2).  They are adjacent through
the edge \(x_1x_2\).  Each is adjacent to its own residue through the
corresponding \(P_iQ_i\) edge.  Item 3 (or its stated replacements)
gives the two crossed contacts to the opposite residues.  Item 1 joins
the residues, item 2 joins each residue to \(R_3,R_4\), and the old gate
contacts join each of the first two bags to \(R_3,R_4\).  Finally
\(R_3R_4\ne\varnothing\).  Hence all pairs in (3.1) are adjacent.
\(\square\)

For the Moser rooted core, both \(x_1x_2\) and \(x_3x_4\) are literal
boundary edges.  Lemma 3.2 is therefore available in two independent
orientations.  Its failure is a genuine *crossed portal lock*, not merely
failure to connect the deficient bags.

## 4. Minimal rooted bags have only two charged lobes

The next reduction is label-free apart from the matching already present
on the four roots.

### Lemma 4.1 (two-lobe skeleton)

Assume (1.1)--(1.2), and suppose that

\[
                         x_1x_2,\ x_3x_4\in E(H).  \tag{4.1}
\]

Choose the rooted \(K_4\)-model \((R_1,\ldots,R_4)\), with the gate
sets \(A,B\) fixed, so that
\(\sum_i|R_i|\) is minimum.  Let \(\bar i\) denote the mate of \(i\)
in the matching (4.1).  Then every component \(C\) of
\(R_i-x_i\) is the unique \(R_i\)-side carrier of the adjacency to at
least one of the two bags

\[
                 \{R_j:j\notin\{i,\bar i\}\}.     \tag{4.2}
\]

Consequently \(R_i-x_i\) has at most two components.  If it has two,
the two components are charged bijectively to the two bags in (4.2).

#### Proof

For a component \(C\) of \(R_i-x_i\), the set \(R_i-C\) is nonempty
and connected: it consists of \(x_i\) together with the other components,
each of which has a neighbour at \(x_i\).

The smaller set retains both gate contacts through \(x_i\), and retains
the contact to \(R_{\bar i}\) through the literal edge
\(x_ix_{\bar i}\).  If it also retained a contact to each of the two
bags in (4.2), replacing \(R_i\) by \(R_i-C\) would give a smaller
rooted \(K_4\)-model with the same gate sets, a contradiction.  Hence
all \(R_i\)-to-\(R_j\) edges for at least one \(j\) in (4.2) have
their \(R_i\)-endpoint in \(C\); this is the asserted unique charge.

One fixed \(R_j\) cannot charge two different components: its nonempty
set of \(R_i\)-neighbours cannot be contained in two disjoint components.
There are only the two possible labels in (4.2), proving both remaining
claims. \(\square\)

Thus the arbitrary rooted \(K_4\) has collapsed to four rooted hubs with
at most two charged lobes apiece.  The two extra gate paths from
Corollary 2.3 must run through this bounded-valence lobe skeleton unless
they already repair the model.  A three-path outcome in Theorem 2.2 gives
one further unit of capacity through the same skeleton.  This is exactly
the finite *state* on which a web exchange should operate; the interiors
of the lobes may remain unbounded.

There is a complementary normalization which retains actual portal
multiplicity instead of the two-lobe skeleton.

### Lemma 4.2 (spanning gate normalization)

If there is no clean connector as in Lemma 2.1, the model (1.1) can be
enlarged, without changing its roots or creating an \(A\)-\(B\) edge, so
that its six bags partition \(V(H)\).

#### Proof

Let \(U\) be a component of the vertices unused by the current model.
If \(U\) has a neighbour in each of \(A,B\), a path through the connected
set \(U\) is a clean connector and Lemma 2.1 gives a \(K_6\)-minor.
Thus this does not occur.

Every such component has a neighbour in at least one model bag because
\(H\) is connected.  If it meets \(A\), absorb it into \(A\); otherwise,
if it meets \(B\), absorb it into \(B\); otherwise absorb it into any
rooted bag it meets.  The enlarged bag is connected.  Distinct unused
components are anticomplete, and no component assigned to one gate meets
the other gate, so the two enlarged gate bags remain anticomplete.  All
old model edges and roots remain.  Doing this for every unused component
gives the asserted spanning model. \(\square\)

### Lemma 4.3 (five units of external portal load)

Use a spanning model from Lemma 4.2 and assume that \(H\) is
six-connected.  If \(C\) is a component of \(R_i-x_i\), then

\[
 \sum_{Z\in\{A,B,R_j:j\ne i\}} |N_H(C)\cap Z|\ge5. \tag{4.3}
\]

Consequently, if \(C\) meets vertices in only \(s\) of the five bags in
the sum, one of those bags contains at least \(\lceil5/s\rceil\)
distinct neighbours of \(C\).  In particular, support on at most two
bag labels forces a triple portal, and support on at most three forces a
double portal.

#### Proof

There are no edges from \(C\) to another component of \(R_i-x_i\), and
the model is spanning.  Therefore

\[
 N_H(C)\subseteq \{x_i\}\cup A\cup B
                    \cup\bigcup_{j\ne i}R_j.       \tag{4.4}
\]

The complement of \(C\) contains at least the six distinct nonempty
objects \(x_i,A,B,R_j\ (j\ne i)\).  If some vertex outside
\(C\cup N(C)\) exists, then \(N(C)\) is a vertex cut and
six-connectivity gives \(|N(C)|\ge6\).  If none exists, then
\(N(C)=V(H)-C\), which again has order at least six by the preceding
observation.  Removing the possible neighbour \(x_i\) from this count
gives (4.3).  The remaining assertions are the pigeonhole principle.
\(\square\)

Lemmas 4.1 and 4.3 are the two sides of the desired exchange theorem.  A
minimal core has only two charged lobes at a root; a spanning core forces
each of its lobes to export five actual portal incidences.  They are not
asserted to be the same normalization: synchronizing minimum skeletal
form with spanning portal load is part of the remaining exchange.  Any
quotient which records only which *bags* are met discards precisely the
double and triple contacts that must perform the compensating peel.

## 5. Specialization to the antipodal Moser gate

Let \(G,v,H,A,B,J,X,K_0,K_{56}\) be as in Theorem 3.1 of
`hadwiger_palette_deletion_rooted_core.md`, and set

\[
                         A=K_0,\qquad B=K_{56}.
\]

The four rooted bags supplied there satisfy all hypotheses above.  Since
\(G\) is seven-connected, \(H=G-v\) is six-connected.  Hence:

* a clean gate connector gives a \(K_6\)-model in \(H\), and adding
  \(\{v\}\) gives a \(K_7\)-model;
* otherwise Theorem 2.2 gives either the exact seven-cut (2.1), or three
  root-avoiding gate paths forced through the two-lobe skeleton;
* either peel certificate in Section 3 again gives a \(K_7\)-model after
  adding \(\{v\}\).

Finally, the Kempe switch on \(K_0\) which exchanges the exact traces

\[
                         05\mid6
                    \quad\longleftrightarrow\quad
                         5\mid06                   \tag{5.1}
\]

does not change any of the sets
\(K_0,K_{56},J,R_1,\ldots,R_4\).  In the exact-adhesion outcome it also
fixes every vertex of \(X\cup\{p,q\}\), because that separator is
disjoint from \(K_0\), the only bichromatic component on which colours
are switched.  (The vertices \(p,q\) need not lie in \(J\); they may
belong to another component of the two omitted colour classes.)  Thus
(5.1) descends through the same actual adhesion; the two trace
orientations cannot be assigned to unrelated quotient geometries.

The switch gives an exact state/core dichotomy on that adhesion.

### Lemma 5.1 (two-state export or a pure four-colour adhesion)

Assume the exact-adhesion outcome of Theorem 2.2.  Let
\(\alpha=c(0)=c(5)\) and \(\beta=c(6)\), and let \(C_0\) be the
component of

\[
 G-\bigl(\{v\}\cup X\cup\{p,q\}\bigr)
\]

which contains \(K_0\).  The side
\(G[C_0\cup\{v\}\cup X\cup\{p,q\}]\) admits two proper six-colour
boundary states \(\psi_\alpha,\psi_\beta\) which agree on
\(X\cup\{p,q\}\) and satisfy

\[
                        \psi_\alpha(v)=\alpha,
          \qquad       \psi_\beta(v)=\beta.       \tag{5.2}
\]

Their equality partitions are distinct if and only if at least one of
\(p,q\) has colour \(\alpha\) or \(\beta\) under \(c\).  Equivalently,
either

1. the \(K_0\)-shore accepts two distinct exact cut partitions; or
2. \(p,q\in V(J)\), and the two switch orientations induce the same
   equality partition.

#### Proof

In the original colouring, vertex \(0\in K_0\) has colour \(\alpha\).
The only neighbour of \(v\) in \(C_0\) is \(0\): the other six
neighbours of the degree-seven vertex \(v\) are
\(X\cup\{5,6\}\), with \(X\) on the cut and \(5,6\) in the
\(K_{56}\)-side.  Hence the restriction of \(c\) to the displayed
side extends after giving \(v\) colour \(\beta\).  Switch
\(\alpha,\beta\) on \(K_0\).  Now \(0\) has colour \(\beta\), every
cut vertex keeps its old colour, and giving \(v\) colour \(\alpha\)
gives the second extension.  The vertices \(p,q\) are not neighbours of
\(v\), since they lie outside
\(K_0\cup K_{56}\cup X\supseteq N(v)\).  Thus both extensions are
proper.

Put

\[
 Y_\gamma=\{z\in\{p,q\}:c(z)=\gamma\}
 \qquad(\gamma\in\{\alpha,\beta\}).
\]

In \(\psi_\alpha\), the equality block containing \(v\) is
\(\{v\}\cup Y_\alpha\); in \(\psi_\beta\), it is
\(\{v\}\cup Y_\beta\).  The sets \(Y_\alpha,Y_\beta\) are disjoint,
so the two equality partitions coincide exactly when both are empty.
The omitted two colour classes are precisely \(\alpha,\beta\), hence
both sets are empty exactly when \(p,q\in J\). \(\square\)

Thus the exact-cut branch no longer has an undifferentiated state gap.
Either minor-critical gluing has two genuinely different states to work
with on the \(K_0\)-side, or the adhesion vertices are entirely in the
rooted four-colour core, where the four-terminal web theorem applies
without omitted-colour decorations.

The state-rich branch actually carries the entire componentwise Kempe
orbit.

### Corollary 5.2 (the gate-state cube)

Let \(\mathcal C\) be the set of components of the bichromatic graph on
colours \(\alpha,\beta\), other than \(K_0,K_{56}\), which meet
\(\{p,q\}\).  Independently switch the two colours on any subfamily of
\(\mathcal C\), independently switch \(K_0\), and give \(v\) the gate
colour opposite to the resulting colour of \(0\).  Every resulting
boundary colouring extends over the \(K_0\)-shore.

In particular:

* if exactly one of \(p,q\) lies in an extra gate-colour component, the
  shore accepts both possibilities that it agrees or disagrees with
  \(v\);
* if \(p,q\) lie in two distinct extra components, then \(pq\notin E(G)\)
  and the shore accepts all four equality partitions of
  \(\{v,p,q\}\) realizable with two colours; and
* if \(\mathcal C=\varnothing\), the cut is the pure-core outcome of
  Lemma 5.1.

#### Proof

Kempe switches on distinct bichromatic components commute and preserve
properness.  No component in \(\mathcal C\) contains a vertex of
\(\{0,5,6\}\), since those vertices lie in \(K_0\) or \(K_{56}\).
Thus these switches preserve the exact trace at \(N(v)\).  The switch on
\(K_0\) is also independent.  After all switches, the only neighbour of
\(v\) on the \(K_0\)-shore is still \(0\), so the opposite gate colour
is safe at \(v\).  Restricting the resulting global colouring of \(H\)
to the shore proves the first assertion.

If \(p,q\) belong to distinct bichromatic components, they cannot be
adjacent, since an \(\alpha\)-\(\beta\) edge would join those components
(and equal-coloured ends cannot be adjacent).  Their colours and the
choice at \(v\) may therefore be toggled independently.  Modulo a global
interchange of \(\alpha,\beta\), the eight binary assignments give the
four equality partitions of three vertices.  The other assertions are
the corresponding one- and zero-component specializations. \(\square\)

This is genuine finite-boundary criticality extracted from the gate, not
an abstract extension-set hypothesis: every state is supplied by an
actual Kempe component in the original counterexample.  The opposite
shore must reject the entire displayed orbit, or a common state glues.

## 6. Pair-mode normalization and the exact singleton-helper gap

Retain the state-rich exact-cut branch and suppose that \(p,q\) lie in
distinct extra \(\alpha\)-\(\beta\) components.  Choose from the
gate-state cube the state in which

\[
                         c(v)=c(p)\ne c(q).        \tag{6.1}
\]

The four roots still have their four distinct core colours.  For a missing
edge \(ij\in\{13,14,23,24\}\), say that \(ij\in F_0\) when the
two roots have a bichromatic path whose interior lies in the
\(K_0\)-shore \(C_0\).

### Theorem 6.1 (matching state, disjoint carriers, or a two-shore star)

At least one of the following holds.

1. The \(K_0\)-shore accepts one of the pair modes
   \[
   \begin{aligned}
    &\{v,p\}\mid\{1,3\}\mid\{2,4\}\mid\{q\},\\
    &\{v,p\}\mid\{1,4\}\mid\{2,3\}\mid\{q\}.
   \end{aligned}                                  \tag{6.2}
   \]
2. The shore contains two vertex-disjoint core-colour carriers for one
   of the matchings \(13\mid24\) or \(14\mid23\).
3. The support graph \(F_0\) consists of two adjacent edges of the
   missing \(C_4\).  The two edges in the complementary star have
   bichromatic paths on the far side of the cut, and the two stars
   assemble an \(X\)-rooted \(K_4\)-model with one centre bag in
   \(C_0\) and the other centre bag in the far side.

#### Proof

Four-saturation of \(X\) implies that the ends of every missing root edge
lie in one global bichromatic component: otherwise a Kempe switch merges
their boundary colours and uses at most three core colours on \(X\).
Every global bichromatic path for one of the four missing root edges has
its interior in a single component of the exact cut.  Indeed, its only cut
vertices in the two relevant core colours are its two ends: \(p,q\) have
gate colours, \(v\) is absent from \(H\), and the other two roots have
different core colours.  Thus every edge outside \(F_0\) has a path whose
interior is in a far component.

If the complement of \(F_0\) contains one of the two perfect matchings of
the \(C_4\), the two corresponding pairs lie in different bichromatic
components of the \(K_0\)-side.  Switch one end component for each pair.
The switches use disjoint pairs of colours and commute.  They merge both
pairs without changing (6.1), giving the corresponding state in (6.2).

If \(F_0\) contains a perfect matching, choose its two paths.  Their
colour pairs are disjoint, so their interiors are vertex-disjoint and are
the two carriers in outcome 2.

It remains that neither \(F_0\) nor its complement contains a perfect
matching.  From each of the two opposite-edge pairs of the \(C_4\),
\(F_0\) then contains exactly one edge.  These two selected edges are
adjacent, so they form a star; the other two edges form the star centred
at the opposite root.  Take the two \(C_0\)-paths and join their interiors
to their common root, making one rooted bag.  Do the same with far-side
paths for the complementary star.  Keep the other two roots as singleton
bags.  The two centre bags are adjacent through one of the root edges
\(12,34\), the singleton bags through the other, and the four star arms
give every centre-to-singleton adjacency.  These four bags form the
claimed rooted \(K_4\)-model. \(\square\)

Outcome 1 is exactly the palette-tight \(2+2+2+1\) mode needed by the
uniform pair-mode packet-or-tight-adhesion theorem.  It is not yet a
colour-transfer contradiction, because the singleton has one unavoidable
missing block adjacency:

\[
 E\bigl(\{q\},\{v,p\}\bigr)=\varnothing.          \tag{6.3}
\]

Both edges vanish: \(v\) has degree seven and neither \(p\) nor \(q\)
is in \(N(v)\), while distinct bichromatic components containing
\(p,q\) are anticomplete.  Thus no proof may silently contract the four
blocks of (6.2) to a clique.

The relative pair-mode theorem is genuinely applicable to \(C_0\).
Seven-connectivity makes every component behind the exact cut full to all
seven cut vertices and gives the relative boundary inequality of order
seven for every proper subset.  Moreover \(|C_0|\ge2\): a gate-coloured
vertex \(p\) in a component different from \(K_0\) has no bichromatic
edge to \(K_0\), while fullness supplies a \(p\)-neighbour in \(C_0\)
outside \(K_0\).  Hence the theorem gives either a nested tight
seven-adhesion or two-block capacity for each mode in (6.2).

The exact additional object required is the following.

### Lemma 6.2 (singleton-helper transfer certificate)

Let \(B_0=\{v,p\}\), and let \(B_1,B_2\) be either of the two root
matchings in (6.2).  Suppose that the \(K_0\)-shore contains pairwise
disjoint connected carriers \(L_0,L_1,L_2\) for
\(B_0,B_1,B_2\), respectively.  Suppose also that it contains a vertex
set \(Z\), disjoint from the three carriers, such that

* \(\{q\}\cup Z\) is connected; and
* for every \(i\in\{0,1,2\}\), the set \(\{q\}\cup Z\) is adjacent
  to \(B_i\cup L_i\).

Then the mode in (6.2) transfers to the far side.  Since it already
extends the \(K_0\)-shore, \(G\) is six-colourable.

#### Proof

The four sets

\[
        B_0\cup L_0,\quad B_1\cup L_1,\quad
        B_2\cup L_2,\quad \{q\}\cup Z             \tag{6.4}
\]

are disjoint and connected.  The first three are pairwise adjacent:
\(v\) sees every root in \(X\), and the edges \(12,34\) join the two
root-matching blocks.  The hypotheses on \(Z\) give all three contacts
from the last set.  Thus (6.4) is a \(K_4\)-model, one bag for each
block of (6.2).

Contract these four bags, delete the unused part of the \(K_0\)-shore,
and retain every far component.  This is a proper minor of \(G\), so it
has a six-colouring.  The four clique images receive four distinct
colours; expanding only the cut vertices gives exactly the mode (6.2)
on the far side.  Align it with the shore colouring supplied by outcome
1 of Theorem 6.1 and glue. \(\square\)

### Lemma 6.3 (helper or a two-path portal separator)

Suppose three pairwise disjoint carriers
\(L_0,L_1,L_2\) for \(B_0,B_1,B_2\) exist in the \(K_0\)-shore
\(C_0\).  They may be chosen so that each \(L_i\) is a path (a
one-vertex path is allowed).  For such a minimal choice, either the helper
in Lemma 6.2 exists, or for some permutation
\(\{i,j,k\}=\{0,1,2\}\),

\[
 q\text{ has no edge to }B_i,\qquad
 L_j\cup L_k\text{ separates }N_{C_0}(q)
                     \text{ from }L_i\text{ in }C_0.               \tag{6.5}
\]

Here separation permits all \(q\)-neighbours to lie in
\(L_j\cup L_k\); equivalently every path starting with an edge from
\(q\) and ending in \(L_i\) meets one of the other two carrier paths.

#### Proof

First shrink each carrier inclusion-minimally while preserving its two
portal classes.  A one-vertex carrier is already a path.  In a minimal
carrier of order at least two, every
non-cutvertex is the unique representative of one of the two classes.
Thus there are at most two non-cutvertices.  The block injection argument
of Lemma 2.0 in `hadwiger_connected_t_carrier_contraction.md` makes every
block an edge.  The carrier is a tree with at most two leaves, hence a
path.

Put \(L=L_0\cup L_1\cup L_2\), and let \(\mathcal W\) be the
components of \(C_0-L\) which contain a neighbour of \(q\).  Let

\[
                         Z=\bigcup_{W\in\mathcal W}V(W).
\]

Every member of \(\mathcal W\) has an edge to \(q\), so
\(\{q\}\cup Z\) is connected.  If, for every \(i\), either \(q\)
sees \(B_i\cup L_i\) directly or some member of \(\mathcal W\) is
adjacent to \(B_i\cup L_i\), Lemma 6.2 applies.

Otherwise choose \(i\) for which both possibilities fail.  Then
\(q\) misses \(B_i\), has no neighbour in \(L_i\), and no component
of \(\mathcal W\) is adjacent to \(L_i\).  A path in \(C_0\) from a
\(q\)-neighbour to \(L_i\) which avoided \(L_j\cup L_k\) would start
either in \(L_i\), contrary to the second assertion, or in a member of
\(\mathcal W\) adjacent to \(L_i\), contrary to the third.  This proves
(6.5). \(\square\)

Lemma 6.3 is the promised structural endpoint.  Failure of exact state
transfer does not create another finite contact pattern: it creates two
actual carrier paths which block every \(q\)-to-third-carrier route.  A
Two Paths/web theorem can now be applied to these path societies.  Its
crossing outcome supplies the helper; its crossless outcome must be
combined with relative seven-connectivity to expose the tight adhesion.

The relative theorem initially gives only two carriers.  The missing third
carrier has an equally exact path-separator alternative.

### Lemma 6.4 (third carrier or two-path separation)

Let \(L_j,L_k\) be disjoint carriers for two blocks of the mode, shrunk
to minimal paths, and let \(B_i=\{a_i,b_i\}\) be the remaining block.
Then either there is a \(B_i\)-carrier disjoint from
\(L_j\cup L_k\), or \(L_j\cup L_k\) separates the two portal sets

\[
                  N_{C_0}(a_i)\quad\text{and}\quad N_{C_0}(b_i)
                                                                  \tag{6.6}
\]

inside \(C_0\).

#### Proof

Delete \(L_j\cup L_k\).  If one remaining component meets both sets
in (6.6), a minimal connected subgraph of that component meeting them is
the required carrier.  Otherwise no path between the two portal sets can
avoid \(L_j\cup L_k\), which is exactly the second outcome. \(\square\)

### Corollary 6.5 (pair-mode output is a two-path web or descent)

Apply the relative pair-mode theorem to a mode in (6.2).  Then one of the
following holds:

1. a nested tight seven-adhesion is exposed;
2. Lemma 6.2 transfers the state and six-colours \(G\); or
3. two disjoint minimal carrier paths separate either the two portal sets
   of the third pair block, as in (6.6), or the \(q\)-portal set from the
   third carrier, as in (6.5).

#### Proof

Outside outcome 1, the relative theorem gives two-block capacity.  Shrink
the two carriers to paths.  Lemma 6.4 either gives outcome 3 immediately
or supplies a disjoint third carrier.  In the latter case Lemma 6.3 gives
the helper in outcome 2 or the other separator in outcome 3. \(\square\)

This is the desired reusable web-exchange input.  All unbounded interiors
have disappeared from the statement: the residual is two actual paths
separating two prescribed portal systems under the relative
seven-connectivity inequality.  It is precisely the form to which the
generalized Two Paths theorem can attach a crossing-or-planar-web
dichotomy.

Consequently the desired use of the relative pair-mode theorem is now
precise.  Applied to \(C_0\), that theorem gives either its proved tight
seven-adhesion or two-block capacity.  Only the latter branch remains: it
must be upgraded, using the reserved gate carrier, to the four-set helper
certificate (6.4), or made to expose another tight adhesion.  The missing
object is one connected helper for the singleton \(q\), not an unspecified
rooted clique minor.

## 7. Exact remaining exchange

The gate has therefore been reduced without enlarging a finite Moser
atlas:

\[
\begin{array}{c}
\text{clean connector or detachable lobe}\ 
        \Longrightarrow K_7,\\[2mm]
\text{two units of root-avoiding capacity}\
        \Longrightarrow
        \begin{cases}
        \text{exact two-shore seven-adhesion},\\
        \text{or a three-path packet through four two-lobe hubs.}
        \end{cases}
\end{array}
\]

What remains is a capacity--state exchange on that bounded lobe skeleton:
three root-avoiding paths and the two shore-local trace orientations must
either satisfy Lemma 3.1/3.2, or uncross to the exact adhesion.  This is
strictly narrower than a general nonseparating rooted \(K_4\) theorem and
is stated without the Moser edge labels.

## 8. Adversarial boundary: three paths alone do not close the gate

The state and relative-connectivity hypotheses cannot be dropped.  The
following nine-vertex quotient has all the static objects above but no
\(K_6\)-minor.  Use vertices

\[
 A=0,\quad B=1,\quad X=\{2,3,4,5\},\quad
 L=\{7,8,9\},
\]

where \(7,8,9\) are lobes behind \(3,4,5\), respectively, and use the
edge set

\[
\begin{split}
\{&02,03,04,05,07,08,09,
12,13,14,15,17,18,19,\\
&23,24,25,37,38,45,48,59,79\}.
\end{split}                                      \tag{7.1}
\]

The four sets \(\{2\},\{3,7\},\{4,8\},\{5,9\}\) form a rooted
\(K_4\)-model, the roots have matching edges \(23,45\), and each root
is a common neighbour of \(A,B\).  After deleting the roots, the three
paths

\[
                         A-7-B,\quad A-8-B,\quad A-9-B
\]

are internally disjoint.  Nevertheless an exhaustive connected-branch-set
search finds no \(K_6\)-model.  The quotient is even four-connected.
The replay is `bichromatic_gate_lobe_probe.py`; it enumerates all
one-lobe contact quotients of this type, finds a ten-vertex survivor, and
certifies (7.1) after deleting its dispensable lobe.

The quotient is not six-connected, so it is not an ambient counterexample
to Theorem 2.2.  It proves the narrower and important point that
contracting portal lobes and retaining only three-path capacity loses
indispensable information.  The next lemma must use actual relative
boundary size, the two exact Kempe states, or both.  A bare claim that the
three paths force a matched peel is false.
