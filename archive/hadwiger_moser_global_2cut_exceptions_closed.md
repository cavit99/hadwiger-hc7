# Closing the two exceptional global two-cut pairs

## Theorem

Let \(G\) be a proper-minor-minimal counterexample to \(\mathrm{HC}_7\),
let \(d(v)=7\), and suppose

\[
G-N[v]=X\mathbin{\dot\cup}Y,
\qquad G[N(v)]\cong M,
\]

where

\[
E(M)=\{01,02,03,04,12,16,26,34,35,45,56\}.
\]

Then neither exterior component has a two-vertex cut.

The support-independent quotient theorem in
`hadwiger_moser_global_2cut_closure.md` reduces a two-cut to the two
unordered defect pairs

\[
\{13,24\}\qquad\text{and}\qquad\{14,23\}.             \tag{1}
\]

Both pairs are impossible by the colour-gluing argument below.

## Complementary-defect gluing lemma

Split \(X\) into disjoint, connected, adjacent shores \(A,B\).  Suppose
their exact boundary defects are two disjoint nonedges \(r,e\) of
\(M\), respectively, and suppose

\[
N-(r\cup e)=\{0,5,6\},
\qquad 56\in E(M),\quad 05,06\notin E(M).              \tag{2}
\]

Assume \(Y\) is connected and meets every vertex of \(N\).  Then \(G\)
is six-colourable.

### Proof

Write \(L_X=G[N\cup X]\) and \(L_Y=G[N\cup Y]\).  We first obtain one
of three exact boundary states on \(L_X\).

Contract the two disjoint connected sets

\[
\{v\}\cup r,
\qquad
Y\cup e.                                                \tag{3}
\]

The first is a star and the second is connected because \(Y\) meets both
ends of \(e\).  Their images are adjacent.  This is a proper minor, so it
has a six-colouring.  Delete \(v\) and \(Y\), and expand the two boundary
pairs.  The result is a six-colouring of \(L_X\) in which each of
\(r,e\) is monochromatic.

The two pair-blocks have distinct colours and are each adjacent to all of
\(\{0,5,6\}\): the first through \(v\), the second through the
full-attachment component \(Y\).  Also \(5\) and \(6\) have different
colours by (2).  Consequently the equality state induced on \(N\) is
exactly one of

\[
R_0=\{r,e\},\qquad
R_5=\{r,e,05\},\qquad
R_6=\{r,e,06\}.                                        \tag{4}
\]

There are no other possibilities: vertex \(0\) is different from both
pair-blocks and may equal \(5\), equal \(6\), or equal neither, while
\(5\ne6\).

We next show that **all three** states in (4) extend to \(L_Y\).  Since
\(A\) misses exactly \(r\), the set \(A\cup e\) is connected.  Since
\(B\) misses exactly \(e\), the set \(B\cup r\) is connected.  These
two sets are disjoint and adjacent because \(A,B\) are adjacent shores.

For \(q\in\{0,5,6\}\), put

\[
I_0=\{0\},\qquad I_5=\{0,5\},\qquad I_6=\{0,6\}.
\]

The sets \(I_q\) are independent by (2).  For each \(q\), contract

\[
A\cup e,
\qquad B\cup r,
\qquad \{v\}\cup I_q.                                 \tag{5}
\]

These are disjoint connected sets.  Their images are pairwise adjacent:
the first two through an \(AB\)-edge, and the star image to both through
edges from \(v\) to the boundary vertices in \(r\cup e\).

For \(q=0\), the three images together with the singletons \(5,6\)
form a \(K_5\).  Indeed, both shores meet \(5,6\), the star image sees
them through \(v\), and \(56\in E(M)\).  Thus every six-colouring of
this proper minor, after deleting \(A,B,v\) and expanding the boundary
blocks, induces the exact state \(R_0\) on \(L_Y\).

For \(q=5\), the three images together with singleton \(6\) form a
\(K_4\), so the exact state is \(R_5\).  For \(q=6\), the three images
together with singleton \(5\) form a \(K_4\), so the exact state is
\(R_6\).  Hence every state in (4) extends to \(L_Y\).

Choose the state in (4) produced on \(L_X\), choose the corresponding
colouring of \(L_Y\), and permute colours so that the two boundary
colourings agree.  The components \(X,Y\) are anticomplete, so these
colourings glue to a six-colouring of \(G-v\).  At most five colours
occur on \(N\) (in fact four for \(R_5,R_6\)), so a colour absent from
\(N\) can be assigned to \(v\).  This is a six-colouring of \(G\), a
contradiction. \(\square\)

## Application to the two quotient exceptions

For defect pair \(\{13,24\}\), orient the shores so that

\[
r=13,\qquad e=24.
\]

For defect pair \(\{14,23\}\), orient them so that

\[
r=14,\qquad e=23.
\]

In both cases the two sets are disjoint nonedges of \(M\), their
complement is \(\{0,5,6\}\), and (2) holds.  The complementary-defect
gluing lemma eliminates both cases.  Combined with the global quotient
theorem, this eliminates every two-cut in either exterior component.

Together with `hadwiger_moser_global_cutvertex_closure.md`, every
surviving exterior component therefore has no vertex cut of order one or
two; if it has at least four vertices, it is 3-connected.

## Consequence for the old 33-pair residual

The 33 fixed-trace defect pairs in
`hadwiger_moser_4plus1_closures.md` are all eliminated a fortiori.  The
closure here is support-independent and also applies to the balanced
support families; no bichromatic-path traversal assumption is used.
