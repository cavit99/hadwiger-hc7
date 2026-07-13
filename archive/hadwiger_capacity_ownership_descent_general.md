# Capacity ownership and exact-cut descent at a full-shore adhesion

## 1. Purpose

This note extracts the label-free mechanism behind the three-shore
Moser argument.  It separates four logically different ingredients:

1. full shores act as connected realizations of colour blocks;
2. two-block capacity cannot occur in two shores;
3. a small internal separator in a nonowner shore forces an exact
   adhesion; and
4. when nonownership has a common facial order, a counting inequality
   forces some shore to be non-atomic.

Only the step which proves exact ownership and the numerical matching
count is boundary-specific.

## 2. General capacity packing

Let \(G\) be \(r\)-minor-critical, let \(S\) be a separator, and let
\(m\ge2\), with

\[
 G-S=D_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}D_m,
 \qquad N(D_i)=S.                                  \tag{2.1}
\]

Fix a proper optimal colouring partition

\[
 \Pi=A_1\mid\cdots\mid A_m\mid\{s\}              \tag{2.2}
\]

of \(G[S]\), where \(m+1\le r\).  A shore has **two-block
capacity** for \(\Pi\) if it contains disjoint connected carriers for
some two distinct blocks among \(A_1,\ldots,A_m\).  Since the shore is
connected, the carriers can be enlarged along a shortest connector so
that they are adjacent.

### Theorem 2.1 (at-most-one capacity)

At most one shore in (2.1) has two-block capacity for \(\Pi\).

#### Proof

Suppose two shores are capable.  Fix a target side \(D_i\), and choose
a capable shore \(R\ne D_i\).  Use its two adjacent carriers to realize
two blocks of (2.2).  Assign the remaining \(m-2\) blocks bijectively
to the remaining \(m-2\) shores other than \(D_i,R\), joining each
block to its full shore.  Leave \(s\) as a singleton.

The resulting \(m+1\) connected sets form a clique.  Fullness supplies
all adjacencies involving a one-block shore.  The two sets inside \(R\)
are adjacent by construction.  Optimality of (2.2) makes \(s\)
adjacent to every \(A_j\), since otherwise it could be merged into that
colour block; fullness also makes \(s\) adjacent to every shore set.

Contract these \(m\) nonsingleton sets and retain \(D_i\).  An
\(r\)-colouring of the proper minor expands to a colouring of
\(G[S\cup D_i]\) with exact boundary partition \(\Pi\).  The argument
works for every \(i\), because one of the two capable shores is always
available outside the target.  Align the block colours and glue the
side colourings.  This \(r\)-colours \(G\), a contradiction. \(\square\)

The theorem is independent of block sizes and of the graph induced by
the boundary.  It explains the at-most-one half of Moser ownership.
The at-least-one half is a separate covering theorem and does not hold
formally for arbitrary \(m\).

## 3. Hall transversals from connectivity

Now suppose \(|S|=k\) and \(G\) is \(k\)-connected.  For a full shore
\(D\), write \(P_x=N_D(x)\).

### Lemma 3.1 (relative portal Hall lemma)

Let \(R\subseteq S\) have order \(h\).  Either \(|D|\le h-1\), or the
portal classes \((P_x:x\in R)\) have an SDR.

#### Proof

If a subfamily indexed by \(I\subseteq R\) violates Hall, put
\(U=\bigcup_{x\in I}P_x\), so \(|U|<|I|\).  If \(D-U\ne\varnothing\),
a component \(C\) of \(D-U\) satisfies

\[
 N_G(C)\subseteq U\cup(S-I),
\]

whose order is at most \((|I|-1)+(k-|I|)=k-1\).  Another full shore is
a far side, contradicting \(k\)-connectivity.  Hence \(D=U\), and
\(|D|<|I|\le h\). \(\square\)

## 4. Internal separators: capacity or exact descent

Assume a boundary partition has the form

\[
 \Pi=B_1\mid\cdots\mid B_q\mid\{s\}.             \tag{4.1}
\]

Let \(D\) be a full shore which is a nonowner for \(\Pi\), meaning it
has no two-block capacity among the \(B_j\).  Let \(K\subseteq V(D)\)
have order \(a\), and suppose \(D-K\) has at least two components.

### Theorem 4.1 (separator capacity threshold)

1. If \(q\ge a+2\), then \(D\) has two-block capacity, a
   contradiction.
2. If \(q=a+1\), there is one block \(B_*\) such that every
   component \(C\) of \(D-K\) misses exactly one vertex from each of the
   other \(a\) blocks and misses no root of \(B_*\cup\{s\}\).
   Moreover

   \[
    N_G(C)=N_S(C)\cup K,
    \qquad |N_G(C)|=k.                             \tag{4.2}
   \]

Thus the palette-tight case \(q=a+1\) exposes a proper exact
\(k\)-fragment.

#### Proof

For a component \(C\) of \(D-K\),

\[
 N_G(C)\subseteq N_S(C)\cup K.
\]

The other shores give a far side, so \(k\)-connectivity yields

\[
 |S-N_S(C)|\le a.                                 \tag{4.3}
\]

Let \({\cal F}(C)\) be the blocks fully contacted by \(C\).
Every missed boundary vertex can spoil at most one colour block, hence

\[
 |{\cal F}(C)|\ge q-a.                            \tag{4.4}
\]

Take two components.  If \(q-a\ge2\), their two sets in (4.4) admit
distinct representatives.  Use the two components as carriers for the
selected blocks, and divide a shortest path between them at one edge to
make the carriers adjacent.  This is two-block capacity, proving item 1.

Now let \(q=a+1\).  Nonownership says that no two component sets
\({\cal F}(C)\) admit distinct representatives.  Since they are
nonempty, they must all be the same singleton \(\{B_*\}\).  To spoil
the other \(a\) colour blocks, a component must miss at least one vertex
from each.  By (4.3) it misses exactly those \(a\) roots, one per block,
and no other root.  Hence \(|N_S(C)|=k-a\).  The inclusions above and
\(k\)-connectivity now force

\[
 k\le |N_G(C)|\le(k-a)+a=k,
\]

which proves (4.2). \(\square\)

Thus Theorem 4.1 does not require pair blocks; it applies to arbitrary
colour blocks.  For three pair blocks, a cutvertex has
\(a=1\) and is automatically an
owner.  A two-cut has \(a=2=q-1\), exactly the descent cell found in the
Moser shore.  For four or more pair blocks, every one- or two-cut in a
nonowner shore is eliminated outright.  This is a genuinely scalable
consequence of the local laboratory.

### Corollary 4.2 (internal connectivity amplification)

If a nonowner shore for (4.1) contains no proper exact \(k\)-fragment
and \(|D|>q\), then \(D\) is \(q\)-connected.

#### Proof

A vertex cut of order \(a\le q-2\) contradicts item 1 of Theorem 4.1.
A cut of order \(q-1\) invokes item 2 and gives a forbidden proper exact
fragment.  Hence no cut of order below \(q\) exists. \(\square\)

This amplification is internal to the shore.  It can exceed the known
global connectivity of a contraction-critical graph when an optimal
boundary state has many active blocks.

### Theorem 4.3 (pair-block atomic nonowner theorem)

Suppose every \(B_i\) is a pair.  Let \(D\) be a nonowner, assume
\(|D|>q\), and assume that \(D\) contains no proper exact
\(k\)-fragment.  Then:

1. if \(q\ge4\), the graph \(D\) is planar and is not maximal planar;
   and
2. necessarily \(q\le5\).

Equivalently, for \(q\ge6\), every nonowner shore is either small,
\(|D|\le q\), or contains a proper exact \(k\)-fragment.

#### Proof

Corollary 4.2 makes \(D\) \(q\)-connected.  Suppose first that
\(q\ge4\) and that \(D\) is nonplanar.  Select any two pair blocks
\(\{x_1,x_2\}\) and \(\{y_1,y_2\}\).  Since \(|D|>q\ge4\),
Lemma 3.1 gives distinct representatives

\[
 p_{x_1},p_{x_2},p_{y_1},p_{y_2}
 \quad\text{with}\quad p_z\in P_z.
\]

Jung's theorem says that a four-connected graph is two-linked whenever
it is nonplanar or maximal planar.  Hence, in either of those two cases,
\(D\) contains disjoint paths joining
\(p_{x_1}\) to \(p_{x_2}\) and \(p_{y_1}\) to \(p_{y_2}\).
After adjoining their boundary roots, these are disjoint carriers for
the two selected blocks.  Extending them along a shortest connector in
the connected graph \(D\) makes the carriers adjacent.  This is
two-block capacity, contrary to nonownership.  Thus \(D\) is planar and
not maximal planar.

A planar graph has vertex-connectivity at most five.  Since \(D\) is
\(q\)-connected, this forces \(q\le5\). \(\square\)

The cutoff is sharp for linkage alone.  Jung's connectivity bound is
sharp: there are five-connected plane graphs with four terminals in
alternating outer-face order for which the two prescribed disjoint
paths do not exist.  Thus the first surviving cell, \(q=5\), is not an
accidental finite exception.  It is precisely the planar-web
obstruction.  Any argument eliminating it must use information beyond
internal connectivity and four portal representatives--for example
the other shores, exact minor transitions, or the placement of the
remaining portal classes.

### Theorem 4.4 (arbitrary-block knitted threshold)

Write \(b_i=|B_i|\), and retain the hypotheses that \(D\) is a
nonowner, \(|D|>q\), and \(D\) contains no proper exact
\(k\)-fragment.  Then

\[
 q<8(b_i+b_j) \qquad\text{for every }i\ne j.       \tag{4.5}
\]

Consequently,

\[
 q^2<16(k-1).                                      \tag{4.6}
\]

In particular, an atomic nonowner with arbitrary blocks is impossible
whenever \(q\ge4\sqrt{k-1}\).

#### Proof

We use the knitted-graph theorem that every \(8\ell\)-connected graph
is \(\ell\)-knitted.  Suppose, for a contradiction, that
\(q\ge8(b_i+b_j)\), and put \(\ell=b_i+b_j\).  Corollary 4.2 makes
\(D\) \(q\)-connected, hence \(8\ell\)-connected.  Lemma 3.1 supplies
distinct portal representatives in \(D\) for all roots of
\(B_i\cup B_j\), because \(|D|>q\ge\ell\).  Apply knittedness to
these \(\ell\) representatives, partitioned according to the two
blocks.  It gives two disjoint connected subgraphs, one containing all
representatives of \(B_i\), the other all representatives of
\(B_j\).  Adjoin the boundary roots and extend the carriers along a
shortest connector.  This gives two-block capacity, a contradiction,
and proves (4.5).

Let \(b_1\le b_2\le\cdots\le b_q\).  Since the blocks together have
\(k-1\) roots,

\[
 b_1+b_2\le {2(k-1)\over q}.
\]

Apply (4.5) to \(B_1,B_2\) and multiply by \(q\) to obtain (4.6).
\(\square\)

Theorem 4.4 is weaker than Theorem 4.3 for pair blocks, but it is fully
label-free and applies to arbitrary colour blocks.  It is a genuine
all-parameter reduction: outside the range \(q=O(\sqrt{k})\), a
nonowner cannot remain both large and atomic.

### Theorem 4.5 (common-face residue for pair blocks)

Under the hypotheses of Theorem 4.3, suppose in addition that
\(q\in\{4,5\}\) and \(|D|>2q-1\).  There is an SDR

\[
 X=\{p_x:x\in B_1\cup\cdots\cup B_q\},
 \qquad p_x\in P_x,                                \tag{4.7}
\]

and a single facial cycle \(F\) in the unique plane embedding of \(D\)
such that \(X\subseteq V(F)\).  On \(F\), the two representatives of
each block occupy antipodal positions in the cyclic order induced on
\(X\).

#### Proof

Lemma 3.1, applied to all \(2q\) paired roots, gives (4.7).  By
Theorem 4.3, \(D\) is planar; it is at least four-connected, so its
plane embedding is unique up to reflection.

For distinct blocks \(B_i,B_j\), nonownership forbids the two paths
joining the two representatives of \(B_i\) and the two representatives
of \(B_j\).  To spell out the standard specialization of the rooted
Two Paths Theorem, extend \(D\) edge-maximally without creating those
two paths.  The resulting graph is a web for the four terminals.
Four-connectivity excludes every clique inserted behind a facial
triangle, so the web rib is a plane graph with the terminals on its
outer face in alternating order.  Restricting that embedding back to
\(D\), and using uniqueness of the embedding, puts the four
representatives on a common face \(F_{ij}\) in alternating order.

Fix \(i\) and take \(j\ne h\).  If \(F_{ij}\ne F_{ih}\), the two
facial cycles share the two representatives of \(B_i\).  Distinct faces
of a three-connected plane graph meet in at most one edge.  Hence those
two representatives would be adjacent on each facial cycle.  This is
impossible because they alternate there with the representatives of
\(B_j\), respectively \(B_h\).  Thus \(F_{ij}=F_{ih}\).  Since the
complete graph on the block indices is connected, all \(F_{ij}\) are
one face \(F\).

Every two block chords alternate in the cyclic order of \(X\) on
\(F\).  The unique perfect matching of \(2q\) cyclic points whose edges
are pairwise alternating is the antipodal matching. \(\square\)

The theorem does not claim that every vertex in every portal class lies
on \(F\); Hall gives a common facial transversal, not prescribed
representatives.  This distinction is exactly where portal placement
and mode-preserving minor transitions must enter.  Nevertheless, it
reduces every large atomic pair-block nonowner to a single web geometry:
the only unbounded residues are a four- or five-connected planar shore
with an antipodal portal transversal on one nontriangular face.  Shores
of order at most \(2q-1\) form a bounded base, and all other shores have
already descended through an exact cut.

## 5. Abstract ownership counting

Let \({\cal P}\) be a finite family of boundary modes, and let
\(\tau:{\cal P}\to T\) be a tag map (in the matching application,
\(T=S\) and \(\tau\) records the unmatched singleton).  Suppose every
mode has exactly \(h\) owners among the \(m\) shores.

Call a shore **circularly atomic** if it is a nonowner for at most one
mode of each tag.  Thus it has at most \(|T|\) nonowner incidences.

### Theorem 5.1 (ownership-count descent)

If

\[
 (m-h)|{\cal P}|>m|T|,                            \tag{5.1}
\]

then not all \(m\) shores are circularly atomic.

#### Proof

Exact ownership gives \((m-h)|{\cal P}|\) nonowner incidences.  If all
shores were circularly atomic, there would be at most \(m|T|\). \(\square\)

The value of (5.1) is that circular atomicity has a geometric criterion
which does not mention the boundary labels.

### Lemma 5.2 (one antipodal mode per tag)

Suppose \(q\ge2\) and the modes tagged by \(s\) are perfect matchings on
\(S-\{s\}\).  Assume that whenever a shore \(D\) is a nonowner for
such a mode:

1. the complete portal classes of its matched roots lie on one facial
   cycle of a three-connected plane embedding of \(D\); and
2. those portal classes have an SDR.

Then \(D\) is a nonowner for at most one mode tagged by \(s\).

#### Proof

Two such modes use the same portal classes.  Their faces coincide,
because distinct faces meet in at most one edge while the SDR supplies
all the distinct common representatives.  Fix one SDR and its cyclic
order.  Nonownership forces the chords of either matching to be pairwise
alternating: any nonalternating two chords have disjoint facial arcs,
which are the forbidden two carriers.  On \(2q\) cyclic points the
unique pairwise-alternating perfect matching pairs each point with the
point \(q\) positions opposite.  Hence the two modes are equal.
\(\square\)

Lemma 5.2 makes every shore satisfying its hypotheses circularly atomic.
It is independent of the graph of allowed matching edges.

## 6. Why three pair blocks synchronize

For completeness, the geometric input used in the Moser case also has
a label-free statement.  Let \(|S|=7\), let (4.1) have \(q=3\), let
\(G\) be seven-connected with \(\delta(G)\ge7\), and suppose \(D\) is
three-connected of order at least six.  If \(D\) is a nonowner, the
three pairwise demands are crossless.  Same-vertex Two Paths completions
are bare: an inserted facial-triangle part together with the three
omitted boundary roots would have a separator of order at most six.

The three demand faces have pairwise intersections containing the two
portal classes of the shared block.  With the six-class SDR from Lemma
3.1, either all three faces coincide, or all are distinct and their
intersections are three disjoint edges.  In the latter case the six
portal classes have union \(X\) of order six.  If \(D-X\ne\varnothing\),
a component has exact neighbourhood \(X\cup\{s\}\).  If \(D=X\), the
three faces form the triangular prism; each prism vertex has three shore
neighbours, at most two represented boundary neighbours, and possibly
the omitted singleton, contradicting minimum degree seven.

Thus a large three-connected nonowner shore either satisfies Lemma 5.2
or exposes a smaller exact seven-fragment.  This is the precise
simultaneous-face theorem behind the owner count.

## 7. Moser specialization and indispensable facts

For the pure Moser boundary:

* \(m=3\), \(h=1\), \(|T|=7\), and
  \(|{\cal P}|=16\);
* hence (5.1) is \(2\cdot16>3\cdot7\);
* Theorem 2.1 gives at most one owner;
* the facial-\(C_4\) three-pattern theorem gives at least one owner;
* triangle-freeness of the missing-edge graph makes every optimal
  colour mode three pairs plus a singleton; and
* seven-connectivity, \(\delta\ge7\), and the same-vertex Two Paths
  Theorem turn nonownership into the simultaneous face or exact descent.

These are exactly the indispensable Moser facts.  The numerical labels,
the drawings of the spindle, and the sixteen-case list are not used
after the two numbers \((|T|,|{\cal P}|)=(7,16)\) have been established.

The \(C_6\) laboratory uses the same architecture but a different
coverage theorem and a different mode family: complementary frame
linkages give exact ownership, while opposite-frame circular orders give
the atomic nonowner bound.  What is common to both is

\[
 \text{full-shore block capacity}
 \Longrightarrow
 \text{exact ownership}
 \Longrightarrow
 \text{facial nonowner bound}
 \Longrightarrow
 \text{small separator or exact descent}.
\]

## 8. What does not yet generalize

For arbitrary \(m\), Theorem 2.1 supplies only the at-most-one half of
ownership.  Three crossless facial \(C_4\) disks have a common
four-colour equality pattern because each omits at most one of four
patterns; four disks need not.  Also, the three pair-demand faces have
the special triangular-prism intersection pattern.  With four or more
pair blocks a new polyhedral face-synchronization theorem is required.

Accordingly, a uniform Hadwiger proof still needs one of:

1. an at-least-one capacity theorem for arbitrary \(m\);
2. a replacement mode space with a Helly number exceeding \(m\); or
3. a contact-or-exact-adhesion theorem which bypasses ownership.

The general results above isolate these missing assertions without
hiding them inside Moser labels.

## 9. Exact minor transitions do not by themselves supply ownership

It is useful to state precisely why contraction-criticality has not yet
proved the missing at-least-one assertion.  For a shore \(D_i\), let
\({\cal E}_i\) be the set of boundary colour partitions which extend to
\(G[S\cup D_i]\).  Since distinct shores are anticomplete, a colouring
of all of \(G\) is equivalent to a state in

\[
 \bigcap_i {\cal E}_i.                              \tag{9.1}
\]

Thus this intersection is empty.  If \(\mu\) is an internal deletion or
contraction in \(D_i\), minor-criticality says that the modified family
\({\cal E}_i^\mu\) satisfies

\[
 {\cal E}_i^\mu\cap\bigcap_{j\ne i}{\cal E}_j
 \ne\varnothing.                                   \tag{9.2}
\]

The witness state in (9.2), however, may depend on both \(i\) and
\(\mu\).  Nothing in (9.2) relates it to the fixed mode \(\Pi\) whose
capacity is being studied.

This is a genuine logical obstruction, already visible in the smallest
abstract signature.  Take two shores and three states
\(\{\alpha,\beta,\pi\}\), with

\[
 {\cal E}_1=\{\alpha\},\qquad {\cal E}_2=\{\beta\}.
\]

For every allowed operation on shore 1 put
\({\cal E}_1^\mu=\{\alpha,\beta\}\), and for every allowed operation on
shore 2 put
\({\cal E}_2^\mu=\{\alpha,\beta\}\).  The original intersection is
empty and every one-step modified intersection is nonempty, exactly as
in (9.1)--(9.2), but the selected state \(\pi\) never appears.  This is
not asserted to be a contraction-critical graph; it proves that the
transition axiom alone has no mode-preserving content.  Realizability
results for boundary colouring families give an additional warning
that arbitrary static extension data can encode very little rooted
minor geometry.

Consequently, the missing input can now be stated sharply:

> **Mode-preserving exchange lemma.**  In a full, atomic shore, either
> a one-step transition can be converted, by portal rerouting and Kempe
> exchange, to the selected optimal mode \(\Pi\), or the shore has the
> planar-web geometry exposed in Theorem 4.3.

Such a lemma would combine the two presently separate sources of
information.  Theorems 4.3 and 4.4 show that its genuinely difficult
range is bounded: for pair modes with \(q\ge4\), only the planar
\(q=4,5\) cells remain (the cases \(q\le3\) require their separate
small-\(q\) analysis); for arbitrary blocks an atomic nonowner must satisfy
\(q^2<16(k-1)\).  This is substantially narrower than an unrestricted
at-least-one capacity theorem, but it is not yet proved.
