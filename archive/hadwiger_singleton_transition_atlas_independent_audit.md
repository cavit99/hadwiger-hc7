# Independent audit: full-singleton transition atlas

## Verdict

**GREEN.**  The state counts, the saturation inequalities and their
equality cases, the degree-two Kempe paths, the degree-free rooted-
\(K_4\) invocation, and all six partitions in Lemma 6.1 are correct.
The note is conditional exactly where it says it is: it does not prove
that an endpoint-saturated degree-two rung exists, nor that one of the six
rooted-core partitions succeeds.

There is one important warning for the next step.  A completion using
\(\{d\},\{b\},\{w\}\) and the four rooted bags cannot work as stated.
The rooted model lies in

\[
 J_0=G-\{d,b,a,c,1,2\},
\]

and the only neighbours of \(d\) in \(J_0\) are \(h,r\).  Therefore at
most two disjoint rooted bags can contain a \(d\)-neighbour.  Lemma 6.1's
partition of \(Z=\{d,a,c,1,2\}\) into two bags is the correct completion
interface.

## 1. The 17+8 states

The complement edges are

\[
 hc,ra,hb,rb,1a,1c,2a,2c.
\]

Direct enumeration gives seventeen two-edge matchings and eight
three-edge matchings.  The order-three list is exactly

\[
\begin{split}
&hc+rb+1a,\ hc+rb+2a,\ ra+hb+1c,\ ra+hb+2c,\\
&hb+1a+2c,\ hb+1c+2a,\ rb+1a+2c,\ rb+1c+2a.
\end{split}
\]

The orbit sizes in (2.2) sum to \(17\) and \(8\), respectively.  The
only defect is typographical: the occurrence of `au` in the proof of
Lemma 2.1 should read \(\tau\).

After a proper operation in \(O\), the retained vertex \(d\) has a colour
absent from \(B\), so \(B\) uses at most five colours.  Since \(B\)
contains a \(K_4\) and has independence number two, the nonsingleton
classes are exactly a matching of order two or three.  Thus no other state
size is omitted.

## 2. Rung saturation

For an endpoint-saturated rung \(xy\), the contracted image is adjacent
to all of \(B\); hence its colour \(\alpha\) is absent from \(B\).  A
matching of order \(m\) has \(7-m\) boundary blocks.  The row
\(N_B(x)=B-\{1\}\) loses one visible colour exactly when \(1\) is a
singleton block.  Consequently

\[
 |c(N_B(x))|=(7-m)-s_1(M),
\]

and similarly at \(y\).  Substitution into contraction-state saturation

\[
 d_O(u)+|c(N_B(u))|\ge6
\]

gives precisely (3.2)--(3.3).  Here \(d_O(x)\) includes the rung
neighbour \(y\), as required by the source theorem.

When equality holds, the source theorem says that the
\(d_O(u)-1\) internal neighbours other than the contracted partner have
distinct colours, disjoint from the boundary-row palette, and together
with that palette realize all five non-\(\alpha\) colours.  This is the
equality statement used in Section 4; no stronger rainbow assertion is
being imported.

## 3. Degree-two Kempe paths

If \(d_O(x)=d_O(y)=2\) and the unlocked state has order three, (3.3)
forces both \(1,2\) to be paired.  Exactly the last four order-three states
have this property, proving (4.2).

Those states use four colours on \(B\).  Besides \(\alpha\), choose the
other boundary-absent colour \(\delta\) for \(d\); this recolouring is
safe because \(d\) is anticomplete to \(O\).  Each endpoint row sees all
four boundary colours.  Equality in saturation therefore forces the sole
other internal neighbours \(x',y'\) to have colour \(\delta\).

After expanding the contraction in \(G-xy\), the edge-deletion Kempe fan
puts \(x,y\) in one \(\alpha/\delta\)-component.  Neither colour occurs
on \(B\), and the only \(\delta\)-vertex outside \(B\cup O\) which might
matter is \(d\), anticomplete to \(O\).  A shortest connecting path is
therefore contained in \(O-xy\), and degree two forces its first and last
edges to be \(xx'\) and \(y'y\).

For an order-two state leaving \(1\) singleton, the row at \(x\) sees the
other four boundary colours.  Equality forces \(c(x')=c(1)\), and the
\(\alpha/c(1)\)-fan begins with \(xx'\).  The note correctly does not
claim that this latter path avoids all boundary vertices.  The statement
at \(y\) is symmetric.

## 4. True bridges

If \(xy\) is a bridge and \(A,C\) are the two sides, then

\[
 N_G(A)=\{y\}\cup N_B(A),\qquad
 N_G(C)=\{x\}\cup N_B(C),
\]

because \(d\) is anticomplete to \(O\).  A one-label defect bounds either
set by seven, while seven-connectivity gives the reverse inequality.
The exact identities (5.2) follow.  This argument applies only to a true
bridge, exactly as stated.

## 5. Independent audit of the degree-free rooted core

For the edge \(db\), the common set

\[
 W=\{a,c,1,2\}=\{a,1\}\dot\cup\{c,2\}
\]

is a disjoint union of two independent sets.  Contract the two stars and
let their distinct colours be \(\alpha,\beta\).  After deleting the two
centres and expanding only the independent leaves, \(W\) uses those two
colours.  Apart from \(b\) and \(W\), the degree-seven vertex \(d\) has
only \(h,r\) as neighbours, so its residual list has size at least two.
The residual list at \(b\) must therefore be empty, or the two lists have
distinct representatives and colour \(G\).

It follows that all four other colours occur on

\[
 E=N(b)-(\{d\}\cup W)=N_O(b).
\]

Let \(J\) be induced in the contracted minor by those four colour
classes and put \(X=E\cap V(J)\).  If a proper four-colouring of \(J\)
omitted one colour on \(X\), combine it with the unchanged
\(\alpha,\beta\) classes.  The residual list at \(d\) is still of size at
least two, while the omitted colour enters the residual list at \(b\),
again colouring \(G\).  Hence every four-colouring uses all four colours
on \(X\).  The proved four-colour Strong Hadwiger theorem supplies an
\(X\)-rooted \(K_4\)-model.

The contracted star images have colours \(\alpha,\beta\), so the rooted
model avoids them and lifts literally to
\(G-\{d,b,a,c,1,2\}\).  This proof uses no assumption on \(d(b)\); the
degree-free invocation in Section 6 is valid.

## 6. The six completion partitions

The graph induced by

\[
 Z=\{d,a,c,1,2\}
\]

is the join of \(\{d\}\) with the two disjoint edges \(ac\) and \(12\).
In a connected bipartition, the side not containing \(d\) must be a
nonempty connected subset of \(2K_2\).  These are exactly

\[
 \{a\},\{c\},\{1\},\{2\},\{a,c\},\{1,2\}.
\]

The complementary side is connected through \(d\), and the two sides are
adjacent through \(d\).  Vertex \(b\) is adjacent to every vertex of
\(Z\), while every rooted bag contains a \(b\)-neighbour.  Therefore, if
both sides of any one displayed partition see all four rooted bags, the
seven bags in (6.4) are connected, disjoint and pairwise adjacent.
Lemma 6.1 and its claim of six exhaustive tests are correct.

