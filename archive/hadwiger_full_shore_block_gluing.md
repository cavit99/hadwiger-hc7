# Full-shore block gluing

## 1. The label-free theorem

Let \(G\) be \(r\)-minor-critical: \(G\) is not \(r\)-colourable, while
every proper minor of \(G\) is \(r\)-colourable.  Let \(S\) be a
separator, and let

\[
 G-S=D_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}D_m
\]

be its components.  Say that a component is **full** if
\(N_G(D_i)=S\).

### Theorem 1.1 (full-shore block gluing)

If all \(m\) components are full, then

\[
 \chi(G[S])\ge m.                                  \tag{1.1}
\]

#### Proof

Suppose instead that \(J=G[S]\) has chromatic number
\(p\le m-1\), and fix an optimal colouring with nonempty colour classes

\[
 S=A_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}A_p.
                                                        \tag{1.2}
\]

The graph \(J\) is a proper minor of \(G\), so it is
\(r\)-colourable; in particular \(p\le r\).

Fix \(i\in[m]\).  Choose \(p\) distinct components among
\(\{D_j:j\ne i\}\), say \(D_{j_1},\ldots,D_{j_p}\).  For each
\(\ell\in[p]\), the set

\[
 Q_\ell=D_{j_\ell}\cup A_\ell
                                                        \tag{1.3}
\]

is connected: \(D_{j_\ell}\) is connected and, by fullness, every
vertex of \(A_\ell\) has a neighbour in it.  The sets \(Q_\ell\) are
pairwise adjacent.  Indeed, if \(\ell\ne h\), the full component
\(D_{j_\ell}\) has a neighbour at every vertex of the nonempty set
\(A_h\).

Contract each \(Q_\ell\) to a vertex \(q_\ell\), and delete every
component of \(G-S\) other than \(D_i\) and the components already
absorbed into the \(Q_\ell\).  The absorbed components disappear in
the contractions, so the resulting graph \(M_i\) consists of
\(D_i\), the clique \(q_1,\ldots,q_p\), and their inherited edges.
It is a proper minor of \(G\).  Hence \(M_i\) has an \(r\)-colouring.

The vertices \(q_1,\ldots,q_p\) receive distinct colours.  Expand only
the boundary part of each contraction: give every vertex of
\(A_\ell\) the colour of \(q_\ell\), retain the colours on \(D_i\),
and discard the contracted opposite components.  This is a proper
colouring of \(G[S\cup D_i]\):

* each \(A_\ell\) is independent;
* different \(A_\ell\)'s receive different colours; and
* every edge from \(A_\ell\) to \(D_i\) is represented by an edge from
  \(q_\ell\) to the same vertex of \(D_i\) in \(M_i\).

Thus the single equality partition

\[
 \Pi=\{A_1,\ldots,A_p\}                            \tag{1.4}
\]

extends over \(G[S\cup D_i]\).  The argument works for every
\(i\in[m]\).  Permute the colour names in these \(m\) side colourings
so that they agree on the blocks of \(\Pi\), and glue them across
\(S\).  Distinct components of \(G-S\) are anticomplete, so this gives
an \(r\)-colouring of \(G\), a contradiction.  Therefore
\(\chi(J)\ge m\). \(\square\)

### Theorem 1.2 (singleton residual block)

Under the hypotheses of Theorem 1.1, suppose \(m\ge2\) and that \(J\)
has a proper \(m\)-colouring

\[
 S=A_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}A_m
                                                        \tag{1.5}
\]

in which one colour class is a singleton.  Then \(G\) is
\(r\)-colourable, a contradiction.  Consequently either

\[
 \chi(J)\ge m+1,
\]

or every proper \(m\)-colouring of \(J\) has all its colour classes of
order at least two.  In particular, if \(|S|<2m\), then
\(\chi(J)\ge m+1\).

#### Proof

Write \(A_m=\{s\}\).  For a fixed \(i\), use the \(m-1\) components
other than \(D_i\) and contract

\[
 Q_\ell=D_{j_\ell}\cup A_\ell
 \qquad(1\le\ell\le m-1)
\]

exactly as in Theorem 1.1, but leave the boundary vertex \(s\)
uncontracted.  Delete all unabsorbed components other than \(D_i\).
The resulting proper minor consists of \(D_i\), the clique
\(q_1,\ldots,q_{m-1}\), and \(s\).  Moreover \(s\) is adjacent to
every \(q_\ell\), since each absorbed component is full to \(S\).  In
an \(r\)-colouring of this minor, the \(m\) vertices

\[
 q_1,\ldots,q_{m-1},s
\]

therefore receive distinct colours.  Expanding each boundary class
\(A_\ell\) with the colour of \(q_\ell\) gives a proper colouring of
\(G[S\cup D_i]\) whose labelled equality partition is exactly (1.5).
Doing this for every \(i\), permuting colour names on the common \(m\)
blocks, and gluing gives an \(r\)-colouring of \(G\), the required
contradiction.  The final assertion is the pigeonhole principle.
\(\square\)

### Theorem 1.3 (clique residual blocks)

More generally, suppose \(m\ge2\), and let

\[
 S=A_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}A_p,
 \qquad m-1\le p\le r,                              \tag{1.6}
\]

be a proper colouring of \(J\).  If, after reindexing, every class
\(A_m,\ldots,A_p\) is a singleton and those \(p-m+1\) singleton
vertices induce a clique in \(J\), then \(G\) is \(r\)-colourable, a
contradiction.

#### Proof

For each \(D_i\), contract \(A_1,\ldots,A_{m-1}\) using the other
\(m-1\) full components, and leave the singleton clique
\(A_m\cup\cdots\cup A_p\) uncontracted.  The contracted vertices form
a clique, see every uncontracted singleton by fullness, and the latter
are pairwise adjacent by hypothesis.  They therefore form a \(K_p\) in
the proper minor.  Its \(r\)-colouring assigns the \(p\) boundary blocks
distinct colours.  Expanding the contracted boundary classes produces
the same labelled equality partition (1.6) on every side, and colour
permutation followed by gluing gives an \(r\)-colouring of \(G\).
\(\square\)

## 2. Exact-cut consequences for \(HC_7\)

Let \(G\) be a hypothetical seven-contraction-critical
\(K_7\)-minor-free graph and let \(S\) be a seven-cut.  Seven-connectivity
makes every component of \(G-S\) full.  Theorem 1.1 gives:

\[
\begin{array}{c|c}
m&\text{necessary boundary condition}\\
\hline
2&\chi(G[S])\ge2,\\
3&\chi(G[S])\ge3,\\
4&\chi(G[S])\ge4.
\end{array}                                        \tag{2.1}
\]

The singleton residual theorem in fact raises the four-component lower
bound to \(\chi(G[S])\ge5\), because \(|S|=7<2m=8\).  Independently,
the four-component row is already impossible by the following sharper
minor argument.  By
hadwiger_exact7_multicomponent_closure.md, a \(K_7\)-minor-free
four-component cut has triangle-free boundary.  Every triangle-free
graph on at most seven vertices is three-colourable, by induction on its
order:

* if a vertex has degree at most two, remove it, colour inductively,
  and put it back;
* otherwise the minimum degree is at least three.  If the graph were
  non-bipartite, a shortest odd cycle would be an induced \(C_5\) or
  \(C_7\).  A spanning \(C_7\) with minimum degree three has a chord,
  and a shortest odd cycle is then an induced \(C_5\).  The two
  vertices outside that \(C_5\) have at most two cycle neighbours each,
  since a neighbour set on an induced \(C_5\) is independent.  Minimum
  degree three forces the two outside vertices to be adjacent and forces
  each to have exactly two cycle neighbours.  Each pair is nonconsecutive,
  and the two pairs are disjoint (a common neighbour together with the
  outside edge would be a triangle).  One cycle vertex therefore has no
  outside neighbour and, since the cycle is induced, has degree two, a
  contradiction.

Hence the boundary has chromatic number at most three, contrary to
Theorem 1.1 with \(m=4\).

Combining this with the five-component closure yields:

### Corollary 2.1

Every seven-cut in a hypothetical \(HC_7\) counterexample has at most
three components.  If it has three components, then

\[
 3\le\chi(G[S])\quad\text{and}\quad\omega(G[S])\le3.
                                                        \tag{2.2}
\]

If \(\chi(G[S])=3\), every proper three-colouring of \(G[S]\) has
colour-class sizes \(3,2,2\).  In particular, a three-shore boundary
admitting a proper three-colouring with a singleton class is impossible.
If \(\chi(G[S])=4\), no proper four-colouring can have two singleton
colour classes whose two vertices are adjacent.  In an optimal
four-colouring any two singleton colour classes are automatically
adjacent (otherwise they can be merged).  Hence every optimal
four-colouring of a surviving boundary has the unique size pattern
\(2,2,2,1\).

The clique bound is the explicit three-shore packing from
hadwiger_exact7_multicomponent_closure.md: a boundary \(K_4\) plus
the three full shores gives a \(K_7\)-model.  The final assertion follows
from Theorem 1.2, since three nonempty classes of order at least two on
seven vertices must have sizes \(3,2,2\).  The four-colour assertion is
Theorem 1.3 with \(m=3,p=4\), followed by the preceding merge
observation.

## 3. Why this is a scalable mechanism

Theorem 1.1 does not mention seven-connectivity, a cyclic boundary, or
a finite portal atlas.  It converts the number of full shores directly
into boundary chromatic pressure by using opposite shores as connected
realizations of the colour blocks.  In an all-\(t\) least-counterexample
programme it can be combined with:

* a connectivity theorem, to make every component behind a minimum cut
  full;
* an upper bound on the chromatic number of the adhesion graph; or
* a rooted clique packing forced by a high-chromatic adhesion.

The exact remaining \(HC_7\) multi-shore cell is therefore a
three-component seven-cut with a \(3\)- or higher-chromatic,
\(K_4\)-free boundary.  The two-component cell remains the atomic
covering-split/portal-lock problem.

## 4. Support-efficient boundary minors

The same full-shore geometry has a complementary minor-packing form.

### Theorem 4.1

Let \(p,q\ge1\), let \(S\) have order \(k\), and suppose \(G-S\) has
at least \(q\) full components.  If \(G[S]\) has a \(K_p\)-model whose union uses at
most \(s\) vertices of \(S\), where

\[
 k-s\ge q-1,
                                                        \tag{4.1}
\]

then \(G\) has a \(K_{p+q}\)-minor.

#### Proof

Choose \(q\) full components \(C_0,C_1,\ldots,C_{q-1}\), and choose
distinct unused boundary vertices

\[
 x_1,\ldots,x_{q-1}\in
 S-\bigcup\{\text{the }K_p\text{-model bags}\}.
\]

Keep the \(p\) boundary-model bags and add the \(q\) bags

\[
 C_0,\qquad C_i\cup\{x_i\}\quad(1\le i<q).
\]

Every new bag is connected.  It is adjacent to every boundary-model
bag by fullness.  Two anchored component bags are adjacent because
each full component sees the other bag's anchor, and \(C_0\) sees every
anchor.  Thus all \(p+q\) bags are pairwise adjacent. \(\square\)

For a three-component seven-cut, Theorem 4.1 with \(p=4,q=3\) says
that every boundary \(K_4\)-model supported on at most five vertices
already gives \(K_7\).  Therefore a surviving \(4\)-chromatic boundary
must lie in the small-support obstruction class: every one of its
\(K_4\)-models uses at least six of the seven boundary vertices.  This
explains, without relying on the quotient atlas as a proof, why the
odd-wheel and Moser-type cores recur in the three-shore residue.

### Corollary 4.2 (the four-chromatic three-shore boundary)

If a surviving three-component seven-cut has
\(\chi(G[S])=4\), then \(G[S]\) is isomorphic to the pure Moser spindle.

#### Proof

Section 2 shows that every optimal four-colouring has class sizes
\(2,2,2,1\).  We claim that \(\alpha(G[S])\le2\).  Otherwise take an
independent triple \(I\).  The graph on the other four vertices has no
\(K_4\), by Corollary 2.1.  It is therefore three-colourable.  It
cannot be two-colourable, since then \(I\) together with its two colour
classes would three-colour \(G[S]\).  Hence it has a three-colouring
with class sizes \(2,1,1\).  Together with \(I\), this is an optimal
four-colouring of sizes \(3,2,1,1\), contrary to Section 2.

By Theorem 4.1, \(G[S]\) has no \(K_4\)-model supported on at most five
vertices.  The audited seven-vertex classification in
hadwiger_external_expert_audit.md now applies: among graphs of order
seven with independence number at most two, exactly the Moser spindle
and its unique relevant one-edge extension have no such small-support
\(K_4\)-model.

The one-edge extension is nevertheless excluded by the block theorem.
In the standard labelling its added edge is \(13\), and

\[
 \{2,5\}\mid\{4,6\}\mid\{0\}\mid\{1\}\mid\{3\}
                                                        \tag{4.2}
\]

is a proper five-colouring: \(25\) and \(46\) are nonedges, while
\(0,1,3\) induce a triangle.  Theorem 1.3 with \(m=3,p=5\) glues this
partition across the three full shores, a contradiction.  Only the pure
Moser spindle remains. \(\square\)

Thus the four-chromatic three-shore branch is not a new boundary atlas:
it is the pure Moser core already isolated in the degree-seven
neighbourhood laboratory.  The other three-shore branch has
\(\chi(G[S])=3\) and every optimal colour partition has sizes
\(3,2,2\).

## 5. Uniform minimum-cut sharpening

The label-free continuation in
`hadwiger_uniform_full_cut_inequalities.md` strengthens Theorems
1.1--1.3 as follows.  If `S` is a minimum cut of order `c`, with `m`
components behind it, and `p=chi(G[S])`, then

\[
                              m\le p\le c-m,
                              \qquad c\ge2m.                  \tag{5.1}
\]

Indeed singleton classes in an optimal boundary colouring form a
clique.  Theorem 1.3 therefore forces at least `m` nonsingleton classes,
and counting boundary vertices gives `c>=p+m`.

The same note proves the exact extension-family form: on every fixed
side, any `ell<=m-1` prescribed pairwise-disjoint independent boundary
sets occur as `ell` distinct exact colour classes in some side
colouring.  Thus all difficulty after (5.1) is synchronization of the
completion states of the `m`-th nonsingleton block; saturation of fewer
blocks is automatic.
