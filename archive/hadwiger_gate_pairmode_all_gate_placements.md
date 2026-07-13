# Pair-mode normalization when both adhesion vertices use gate colours

## 1. Setting

Use the exact antipodal gate notation of
`hadwiger_bichromatic_gate_peel_or_adhesion.md`.  Thus

\[
 L=\{v\}\mathbin{\dot\cup}X\mathbin{\dot\cup}\{p,q\},
 \qquad X=\{1,2,3,4\},
\]

is an exact seven-cut with precisely two shores, the four vertices of
(X) have four distinct core colours, and the two omitted gate colours are
(\alpha,\beta).  Assume in this note only that both (p) and (q) have gate
colours.  They may lie in the same or in different
(\alpha,\beta)-components.

For a missing edge (ij\in\{13,14,23,24\}), let (ij\in F_0) when its
ends have a bichromatic path whose interior lies in the (K_0)-shore.

## 2. Uniform normalization theorem

### Theorem 2.1 (all-gate pair-mode normalization)

There is an independent two-vertex block (B_0\subseteq\{v,p,q\}) and
the remaining singleton (r\in\{v,p,q\}-B_0) such that at least one of
the following holds.

1. The (K_0)-shore accepts one of the modes
   \[
       B_0\mid13\mid24\mid\{r\},
       \qquad
       B_0\mid14\mid23\mid\{r\}.                 \tag{2.1}
   \]
2. The shore contains two vertex-disjoint core-colour carriers for one
   of the two displayed core matchings.
3. The set (F_0) and its complement are the two adjacent-edge stars of
   the missing (C_4).  Their shore-local paths assemble an
   (X)-rooted (K_4)-model with the two centre bags in opposite shores.

If (c(p)=c(q)), one may take

\[
                         B_0=\{p,q\},\qquad r=v.  \tag{2.2}
\]

If (c(p)\ne c(q)), after possibly interchanging (p,q), one may take

\[
                         B_0=\{v,p\},\qquad r=q.  \tag{2.3}
\]

#### Proof

If (c(p)=c(q)), properness gives (pq\notin E(G)).  Switch (K_0), if
necessary, and give (v) the gate colour opposite to the resulting colour
of (0), choosing the orientation in which (v) has the other gate colour
from (p,q).  The resulting (K_0)-shore state has the pair block (pq) and
singleton (v), as in (2.2).

If (c(p)\ne c(q)), choose the (K_0)-orientation in which
(c(v)=c(p)).  Since (vp\notin E(G)), this gives the pair block in
(2.3), with (q) as the other gate-colour singleton.  Neither construction
requires independent switches at (p) and (q); it remains valid when they
belong to one extra bichromatic component.

The four core colours are untouched.  Four-saturation of (X) supplies a
global bichromatic path for each edge of the missing (C_4).  Such a path
has no internal cut vertex: (p,q,v) use gate colours and the other two
members of (X) have the other two core colours.  Since the exact gate cut
has only two shores, every path interior lies wholly in one shore.

Now use the same exhaustive (C_4) split as in Theorem 6.1 of the cited
note.  If (\overline{F_0}) contains an opposite-edge matching, switch one
endpoint component for each of its two disjoint colour pairs on the
(K_0)-side.  These switches commute, do not alter (B_0\mid\{r\}), and
give the corresponding mode (2.1).  If (F_0) contains an opposite-edge
matching, the two paths have disjoint colour sets, so their interiors are
disjoint carriers.  If neither set contains a matching, each contains one
edge from each opposite pair and therefore is an adjacent-edge star.  The
two star centres are joined by one of (12,34), their singleton leaves by
the other, and the four arms supply all centre-to-leaf adjacencies.  This
is outcome 3. \(\square\)

## 3. Consequence for the former same-component residue

The same-extra-component placement is therefore not a separate
normalization gap.

* If (p,q) have the same gate colour, their fixed equality supplies the
  first pair and (v) is the singleton.
* If they have opposite gate colours, (v) can be matched to either one by
  the (K_0)-switch.  If (pq\in E(G)), the remaining singleton already
  has a literal edge to the first pair block; this removes that one
  helper demand.

What remains different from the distinct-component case is only the
helper geometry.  One cannot claim that the singleton and (B_0) are
anticomplete unless their vertices lie in distinct bichromatic components.
The full independent three-bit state cube is likewise unavailable in a
single component.  These facts affect transfer after normalization, not
the existence of the palette-tight (2+2+2+1) mode itself.

## 4. Exactly one gate-coloured adhesion vertex

The next placement also has a uniform normalization, with one sharply
typed star residue.

### Theorem 4.1 (one-gate normalization or a shore-local rooted triangle)

Suppose (p) has a gate colour and (q) has the same core colour as the
unique root (x_i\in X).  Then at least one of the following holds.

1. The (K_0)-shore accepts a mode
   \[
              \{v,p\}\mid\{q,x_i\}\mid\{x_j,x_k\}
                    \mid\{x_\ell\},               \tag{4.1}
   \]
   where (x_jx_k) is a missing edge of (G[X]).
2. The other three roots (X-\{x_i\}) have a rooted (K_3)-model whose
   centre bag has its interior in (C_0) and whose other two bags are the
   singleton ends of one of the literal edges (12,34).

#### Proof

Choose the (K_0)-orientation in which (c(v)=c(p)).  Properness gives the
two independent equality blocks (\{v,p\}) and (\{q,x_i\}).

Among the remaining three roots, exactly two of the three pairs are
missing edges, and they share a centre root; the two leaves form the
other literal matching edge in (G[X]).  For example, if (x_i=1), the
candidate missing edges are (23,24) and the leaf edge is (34).  The other
three cases follow by symmetry of this description, not by an assumed
automorphism of the labelled Moser spindle.

Each candidate missing edge has a global bichromatic path by
four-saturation.  Its path interior lies in one shore: neither (p) nor
(v) has a core colour, (q) has the excluded colour of (x_i), and the only
cut vertices in the two relevant colours are its ends.

If either candidate pair has no path on the (C_0)-side, its two ends are
in distinct components of the corresponding two-colour graph on that
side.  Switch the component containing one end.  This merges precisely
that root pair, leaves the two existing equality blocks unchanged, and
gives (4.1).

Otherwise both candidate paths have interiors in (C_0).  Join their
interiors to their common root to make the centre bag, and retain their
two other roots as singleton bags.  The two path arms give the two
centre-to-leaf adjacencies, and the literal matching edge joins the
leaves.  These are the three bags in outcome 2. \(\square\)

Thus the exactly-one placement is also pair-mode normalized unless one
shore already contains a completely explicit three-root triangle frame.
The remaining problem in that frame is helper transfer, rather than an
unclassified boundary equality state.
