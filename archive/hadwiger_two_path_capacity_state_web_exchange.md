# Two carrier paths do not by themselves give a liftable web

## 1. Relative setting

Let (S) be a labelled seven-set with pair mode

\[
 S=B_0\mathbin{\dot\cup}B_1\mathbin{\dot\cup}B_2
   \mathbin{\dot\cup}\{q\},\qquad |B_i|=2.        \tag{1.1}
\]

Let (C) be a connected full (S)-boundaried graph of order at least
two.  For (\varnothing\ne Y\subsetneq C), put

\[
 \partial_S(Y)=(N_C(Y)-Y)\mathbin{\dot\cup}N_S(Y).                 \tag{1.2}
\]

The no-descent branch of the relative pair-mode theorem assumes

\[
                         |\partial_S(Y)|\ge8                       \tag{1.3}
\]

for every nonempty proper (Y).  Corollary 6.5 of
`hadwiger_bichromatic_gate_peel_or_adhesion.md` then leaves two disjoint
minimal carrier paths (L_j,L_k) whose union separates either

1. the two portal sets of the third pair block; or
2. all (q)-portals from a third carrier (L_i).

The phrase "apply Two Paths" is not valid until four terminal objects
and the lifting operation are specified.  Sections 2--3 isolate the two
problems, and Section 4 shows that the actual antipodal gate never reaches
this branch.

## 2. The smallest valid quotient statement

Let (L_1,L_2\subseteq C) be disjoint connected sets, and let
(U,V\subseteq C-(L_1\cup L_2)) be nonempty.  Contract each (L_i) to
a labelled vertex (\ell_i), producing (\bar C).

### Lemma 2.1 (quotient crosslessness)

If (L_1\cup L_2) separates (U) from (V) in (C), then (\bar C)
has no pair of vertex-disjoint paths, one joining (U) to (V) and
one joining (\ell_1) to (\ell_2).

#### Proof

The (U)-(V) member of such a linkage is disjoint from the second
path and hence avoids both of its terminal vertices (\ell_1,\ell_2).
Lifting it to (C) gives a (U)-(V) path avoiding
(L_1\cup L_2), contrary to the separation hypothesis.  \(\square\)

Thus the ordinary Two Paths/Web Theorem may be applied to the four
**individual** terminal objects

\[
                         U,quad V,quad\ell_1,quad\ell_2          \tag{2.1}
\]

after adding artificial terminals for the two set terminals (U,V),
provided (U,V) really are nonempty and disjoint from the carrier
paths.

### Lemma 2.2 (what a quotient cross would give)

Before imposing the separator conclusion, suppose the four-terminal
quotient in Lemma 2.1 has a cross.

1. If (U,V) are the two portal sets of the third pair block, the
   (U)-(V) member lifts to a third carrier disjoint from
   (L_1\cup L_2).
2. In the helper branch, let (U) be the (q)-portal side and let
   (V=V(L_i)).  Assume, as in the construction preceding (6.5), that
   the connected union of the (q)-components is already adjacent to
   the other two carrier bags.  The lifted (U)-(V) path may be
   stopped at its first vertex of (L_i).  Adjoining its prefix to that
   (q)-union produces the helper of Lemma 6.2.

#### Proof

The second member of the cross contains both contracted carrier vertices,
so the first member avoids them.  Lifting therefore makes its interior
disjoint from both carrier paths.  In case 1, shrink the lifted support
to a minimal portal-to-portal connected subgraph.  In case 2, include the
initial (q)-portal edge, stop immediately before (L_i), and use the
last edge as the required helper-to-(L_i) adjacency.  The previously
available contacts to the other two bags are unaffected.  \(\square\)

Thus the crossing half is valid once the quotient and its nonempty
terminal sets are explicit.  It is the **crossless web lift**, not the
crossing implication, that fails under the bare relative hypotheses.

There are two serious limitations.

* If all portals of one demand lie in (L_1\cup L_2), one of the
  terminal sets left outside the contraction is empty.  The four-terminal
  theorem has no such instance.
* A facial triangle in the quotient may contain (\ell_1) or
  (\ell_2).  Lifting that three-vertex quotient separator replaces
  (\ell_i) by the whole path (L_i), whose order is unbounded.  It
  therefore does **not** produce a relative boundary of order at most
  seven.

Adding artificial terminals adjacent to all vertices of (L_i) avoids
the contraction but does not repair the logic.  Two disjoint set-terminal
paths may use different vertices of (L_i): the first demand can meet an
unused part of (L_i) while the second demand uses another part.  Hence
separation by the whole union (L_1\cup L_2) does not imply crosslessness
for that artificial-terminal tuple.

This is the smallest sound Two Paths formulation.  It proves neither the
helper nor the tight-adhesion conclusion without an additional
root-replaceable or bounded carrier-interface hypothesis.

## 3. Sharp abstract counterexample

The desired implication from (1.3) and the path-separator outcome to a
helper or tight set is false.

Let

\[
 B_0=\{v,p\},\qquad B_1=\{a_1,b_1\},\qquad
 B_2=\{a_2,b_2\},
\]

and let (C) be the triangle on vertices (x_0,x_1,x_2).  Give the
three vertices the following complete boundary-contact sets:

\[
 \begin{aligned}
 N_S(x_0)&=S-\{q\},\\
 N_S(x_1)&=S-\{v\},\\
 N_S(x_2)&=S-\{p\}.
 \end{aligned}                                                       \tag{3.1}
\]

Take the boundary graph to have (qv,qp,vp\notin E(G[S])); it may have
the gate-core edges from (6.2), namely (v) adjacent to the four core
roots and the two matching edges between (B_1,B_2).  None of those
boundary edges affects the calculation below.

The singleton paths

\[
                         L_i=\{x_i\}\qquad(i=0,1,2)                 \tag{3.2}
\]

are pairwise disjoint minimal carriers for (B_0,B_1,B_2), respectively.
All (q)-portals are (x_1,x_2).  Hence (L_1\cup L_2) separates the
(q)-portal set from (L_0) in exactly the endpoint-gate sense allowed
by Lemma 6.3: all portals already lie in the separator.

There is no singleton helper for these three carriers.  A set (Z)
disjoint from all carriers is necessarily empty, while (q) has no edge
to either (B_0) or (L_0).  Thus the fourth bag required by Lemma 6.2
is absent.

Nevertheless the strict inequality (1.3) holds.  For a singleton
(Y=\{x_i\}),

\[
 |N_C(Y)-Y|+|N_S(Y)|=2+6=8.                       \tag{3.3}
\]

For a two-vertex set (Y), the remaining triangle vertex is its one
internal boundary vertex, while any two rows in (3.1) cover all seven
labels of (S).  Hence

\[
 |N_C(Y)-Y|+|N_S(Y)|=1+7=8.                       \tag{3.4}
\]

These are all nonempty proper subsets of (C).  Thus there is no tight
relative seven-set.

The example is smallest possible for the three-carrier helper-separation
branch: three pairwise disjoint nonempty carriers require at least three
shore vertices, and the triangle construction has exactly three.

It also pinpoints why no four-terminal web is available.  The natural
outside terminal set

\[
                  N_C(q)-(L_1\cup L_2)
\]

is empty.  Strict relative boundary does not force a portal outside the
two separator paths; dense contacts with the other six labels compensate
exactly.

## 4. Portal multiplicity forced by strict boundary

The actual antipodal gate has an additional fact absent from the abstract
counterexample.

### Lemma 4.1 (strict boundary forces two portals per label)

Under (1.3), every boundary label (s\in S) has at least two distinct
neighbours in (C).

#### Proof

Fullness gives at least one (s)-portal.  Suppose it were unique, say
(N_C(s)=\{z\}).  Since (|C|\ge2), put (Y=C-\{z\}).  Then

\[
              N_C(Y)-Y\subseteq\{z\},\qquad
              N_S(Y)\subseteq S-\{s\}.
\]

Therefore

\[
                         |\partial_S(Y)|\le1+6=7,
\]

contrary to (1.3).  \(\square\)

Equivalently, a full shore with a unique portal for any boundary label
already exposes a relative boundary of order at most seven.  When the
ambient relative inequality is at least seven, that boundary is tight.

## 5. The actual gate immediately descends

Return to the exact antipodal adhesion

\[
                         L=\{v\}\cup X\cup\{p,q\}
\]

and its (K_0)-shore (C_0).  By
`hadwiger_gate_exact_adhesion_multishore.md`, this adhesion has exactly
two shores.  Moreover

\[
                         N_G(v)-L=\{0,5,6\},
\]

with (0\in C_0) and (5,6) in the opposite shore.  Consequently

\[
                         N_{C_0}(v)=\{0\}.                          \tag{5.1}
\]

Assume first that \(|C_0|\ge2\).  (This is automatic in the
state-rich placement treated in Section 6 of
`hadwiger_bichromatic_gate_peel_or_adhesion.md`, but not in every
possible placement of \(p,q\).)  Put

\[
                         Y=C_0-\{0\}.
\]

Then

\[
 |N_{C_0}(Y)-Y|\le1,qquad |N_L(Y)|\le6,          \tag{5.2}
\]

so (|\partial_L(Y)|\le7).  Seven-connectivity supplies the reverse
inequality.  Hence

\[
                         |\partial_L(Y)|=7.                         \tag{5.3}
\]

In fact connectedness of (C_0) and fullness force the exact boundary

\[
                         \partial_L(Y)=\{0\}\cup(L-\{v\}).         \tag{5.4}
\]

Thus the (K_0)-shore exposes the nested exact seven-adhesion obtained
by replacing (v) with its unique shore portal (0).  The strict branch
(1.3), and therefore the two-path residue of Corollary 6.5, never occurs
in the actual antipodal gate.

### Theorem 5.1 (capacity-state web residue closes by descent or a
singleton re-rooting)

In the antipodal exact-adhesion branch, the relative pair-mode theorem
never leaves an atomic Two Paths/web residue.  If \(|C_0|\ge2\), the
nested adhesion is (5.4).  If \(C_0=\{0\}\), then

\[
                         N_G(0)=L,
\]

so \(d_G(0)=7\) and the opposite gate shore is the sole component of
\(G-N_G[0]\).  Thus the singleton alternative is exactly a re-rooting at
a degree-seven vertex with one exterior component.  No assumption that
the four boundary blocks form a clique is used.

#### Proof

When \(|C_0|\ge2\), equation (5.1) contradicts Lemma 4.1 under the
strict alternative.  Equivalently, the direct calculation
(5.2)--(5.4) supplies the tight set.

If \(C_0=\{0\}\), fullness of every component behind the exact cut gives
\(N_G(0)=L\): the singleton has a neighbour at every cut vertex and has
no neighbour in the opposite component.  The opposite component contains
\(5,6\), and deleting \(N_G[0]=L\cup\{0\}\) leaves precisely that
component.  This is the asserted sole-exterior re-rooting.  \(\square\)

## 6. Exact lesson

The abstract Corollary 6.5 residue is not a valid stand-alone web lemma.
The smallest missing condition is not another cyclic ordering: it is a
way to replace a contracted carrier path by a bounded real interface, and
nonempty terminal sets outside both paths.  The order-three triangle shows
that strict relative boundary alone supplies neither.

For the actual (HC_7) gate, the unique (v)-portal is stronger than
either missing condition and forces exact-cut descent immediately.  The
remaining task is therefore the already isolated exact-cut recursion; no
new unbounded two-path web family arises at this gate.
