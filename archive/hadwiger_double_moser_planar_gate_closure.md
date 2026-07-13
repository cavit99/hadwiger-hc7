# Retracted attempt: contracting the opposite-outer path does not preserve colourings

## Retraction notice

**The claimed planar-gate closure below is invalid and must not be
cited.**  The error is in the first sentence after the construction of
\(J=L/Q\) in the proof of Theorem 3.1.  A proper colouring of the path
contraction \(L/Q\) does not lift to a proper colouring of \(L\): expanding
the contracted vertex monochromatically assigns one colour to adjacent
vertices of \(Q\).  Even alternating the path cannot in general preserve
properness at its external attachments.  Consequently the saturation of
\(X\cup\{q\}\) in \(L\) has not been transferred to
\(X\cup\{w\}\) in \(L/Q\), so Strong Hadwiger for four colours cannot be
applied as claimed.

The valid conclusion retained from this attempt is only the already
proved palette saturation in Lemma 2.1 (and the stronger vertexwise
saturation recorded as Lemma 4.3 of
`hadwiger_double_moser_reserved_connector_linkage.md`).  Any repaired
argument needs a genuine colour-extension lemma for a \(q\)-\(b\) path,
not merely a minor contraction.

## 1. Setting

Use the adjacent pure-Moser notation

\[
 X=\{x_1,x_2,x_3,x_4\},\qquad
 A=\{a,b\},\qquad P=\{p,q\},
\]

with adjacent degree-seven centres \(u,v\), where

\[
 N(u)=\{v\}\dot\cup X\dot\cup P,
 \qquad N(v)=\{u\}\dot\cup X\dot\cup A,
\]

and the fixed edges include

\[
 a x_1,a x_2,\qquad b x_3,b x_4,\qquad
 qx_1,qx_2,\qquad px_3,px_4,\qquad ab,pq.
\tag{1.1}
\]

Put \(H=G-\{u,v\}\).  Let \(T\) be a clean \(a\)-\(p\)
connector: its ends are \(a,p\), its internal vertices lie in the
common body, and it is chosen shortest in the induced graph on that body
together with its ends.  Put

\[
                         L=H-V(T).
\tag{1.2}
\]

The reserved-connector theorem in
`hadwiger_double_moser_reserved_connector_linkage.md` gives three
outcomes: a \(K_7\)-minor, a separator of order at most three in \(L\),
or a planar graph \(L\) in which \(x_1,x_2,x_3,x_4\) are cofacial.
This note eliminates the third outcome completely.

We use the following established theorem of Martinsson--Steiner (the
four-colour case of Holroyd's Strong Hadwiger Conjecture).

> **Strong Hadwiger theorem for four colours.**  Let \(J\) be
> four-colourable and let \(Z\subseteq V(J)\).  If every proper
> four-colouring of \(J\) uses all four colours on \(Z\), then \(J\)
> contains a \(Z\)-rooted \(K_4\)-model; that is, four pairwise disjoint,
> pairwise adjacent connected branch sets, each meeting \(Z\).

Only this exact rooted-set formulation is used below.

## 2. Palette saturation on the planar remainder

### Lemma 2.1

Assume that \(G\) is not six-colourable and that \(L\) is planar.  Then
every proper four-colouring of \(L\) uses all four colours on each of

\[
                         X\cup\{q\},\qquad X\cup\{b\}.
\tag{2.1}
\]

#### Proof

This is the palette-saturation argument from Theorem 4.1 of the reserved
connector note, included to make the dependency explicit.

The shortest connector \(T\), together with \(u,v\), induces the
chordless cycle

\[
                         u v a T p u.
\tag{2.2}
\]

If \(T\) had odd length, (2.2) would be even.  Four-colour \(L\) and
two-colour (2.2) with two fresh colours; this would six-colour \(G\).
Thus \(T\) has even length and (2.2) is odd.

Let \(c\) be a four-colouring of \(L\).  If a colour \(\alpha\) were
absent from \(X\cup\{q\}\), give \(u\) colour \(\alpha\).  Removing
\(u\) from (2.2) leaves a path, which can be coloured with two fresh
colours.  This produces a six-colouring of \(G\), a contradiction.
Hence \(X\cup\{q\}\) uses all four colours.  The same argument after
removing \(v\) proves the assertion for \(X\cup\{b\}\). \(\square\)

## 3. Contract the opposite-outer connector

### Theorem 3.1 (planar gate closure)

In the setting of Section 1, if \(L\) is planar, then \(G\) contains a
\(K_7\)-minor.

#### Proof

The graph \(L\) is connected in the planar outcome of the
reserved-connector theorem (indeed, that outcome is reached only after
excluding separators of order at most three).  Choose a \(q\)-\(b\)
path \(Q\) in \(L\), and contract all of \(Q\) to one vertex \(w\).
Call the resulting simple graph \(J=L/Q\).  Since edge contraction
preserves planarity, \(J\) is four-colourable.

Every four-colouring of \(J\) lifts to a four-colouring of \(L\) in
which all vertices of \(Q\), and in particular \(q,b\), have the colour
of \(w\).  Lemma 2.1 therefore implies that every four-colouring of
\(J\) uses all four colours on

\[
                              Z=X\cup\{w\}.
\tag{3.1}
\]

Apply Strong Hadwiger for four colours to \((J,Z)\).  We obtain four
pairwise disjoint, pairwise adjacent connected branch sets
\(B_1,\ldots,B_4\), each meeting \(Z\).  Lift the contraction of \(Q\):
if one branch set contains \(w\), replace \(w\) in that set by all of
\(Q\).  The four lifted sets are a \(K_4\)-model in \(L\), and every one
of them contains either a vertex of \(X\) or the path \(Q\).

Now use the seven branch sets

\[
                    \{u\},\quad\{v\},\quad V(T),
                    \quad B_1,B_2,B_3,B_4.
\tag{3.2}
\]

They are disjoint and connected.  The four \(B_i\)'s are pairwise
adjacent.  The singleton bags \(\{u\},\{v\}\) are adjacent, and each
sees every \(B_i\): a bag meeting \(X\) is seen through the two centre
stars; a bag containing \(Q\) contains both \(q\) and \(b\), and is
seen through \(uq\) and \(vb\).

The connector bag \(V(T)\) is adjacent to both centres through \(p\)
and \(a\), respectively.  It also sees every \(B_i\).  If \(B_i\)
meets \(X\), then (1.1) gives an edge from \(a\) to that root when it
lies in \(\{x_1,x_2\}\), and an edge from \(p\) to that root when it
lies in \(\{x_3,x_4\}\).  If \(B_i\) contains \(Q\), then it contains
\(b,q\), and the fixed edges \(ab,pq\) join it to \(V(T)\).

Thus every two bags in (3.2) are adjacent, so they form a
\(K_7\)-model. \(\square\)

The symmetric statement, with a clean \(b\)-\(q\) connector and a
\(p\)-\(a\) path in the planar remainder, follows by interchanging the
two literal halves.

## 4. Strengthened reserved-connector dichotomy

### Corollary 4.1

For every clean cross connector \(T\) of type \(a\)-\(p\) or
\(b\)-\(q\), at least one of the following holds:

1. \(G\) contains a \(K_7\)-minor; or
2. \(H-V(T)\) has a vertex separator of order at most three.

#### Proof

Apply Theorem 2.2 of the reserved-connector note.  Its rooted-minor
outcome is already a \(K_7\)-minor, and Theorem 3.1 converts its planar
cofacial outcome into a \(K_7\)-minor.  Only the small-separator outcome
remains. \(\square\)

## 5. Consequence for multi-trace synchronization

The universal exact traces at the two adjacent Moser centres supply many
clean cross connectors, each reserving a different bichromatic demand.
Corollary 4.1 shows that their common rural endpoint no longer needs to
be synchronized: **each individual rural endpoint already closes**.
Therefore, in a \(K_7\)-minor-free residue, every such trace-selected
cross connector exposes a three-adhesion in its deletion.

This changes the remaining synchronization problem from

\[
  \text{``make several web rotations agree''}
\]

to the more rigid problem

\[
  \text{``uncross the order-at-most-three adhesions exposed by the
  different exact traces.''}
\]

Together with the ambient vertices \(u,v\), equality in the portal-load
bound gives an exact seven-cut.  Only strict-surplus, mutually crossing
three-adhesions remain for the multi-trace exchange.
