# Portalized exact boundary-state transfer

## 1. Purpose

The earlier two-side transfer theorem used the full neighborhood \(N(v)\)
as its boundary.  A cutvertex inside an exterior component introduces an
additional portal \(z\), and independently coloring the pieces without
aligning the color of \(z\) is invalid.  This note gives the exact transfer
theorem for a genuine separation with adhesion

\[
  X=N(v)\mathbin{\dot\cup}P,
\]

where \(P\) is an arbitrary set of portals.  It also proves the precise
one-step minor-transition condition forced by minor-criticality.

---

## 2. Piece decompositions and states

Let \(G\) be a proper-minor-minimal counterexample to \(\mathrm{HC}_t\),
fix \(v\in V(G)\), put \(H=G-v\), and let \(N=N_G(v)\).

An **\(X\)-piece decomposition** of \(H\) is a family of induced subgraphs

\[
  H_i=H[W_i]\qquad(1\le i\le r)
\]

such that

1. \(N\subseteq X\subseteq W_i\) for every \(i\);
2. \(W_i\cap W_j=X\) for \(i\ne j\);
3. \(\bigcup_iW_i=V(H)\); and
4. there is no edge between \(W_i-X\) and \(W_j-X\) for \(i\ne j\).

Thus the piece interiors are separated by the genuine adhesion \(X\).
The vertices of \(X-N\) are the portals.

An **exact \(X\)-state** is a partition

\[
  \Pi=\{P_1,\ldots,P_q\}
\]

of \(X\) into nonempty independent sets.  Put

\[
  \beta_N(\Pi)=|\{a:P_a\cap N\ne\varnothing\}|.        \tag{2.1}
\]

This is the number of colors used on the actual neighborhood of \(v\).
Portal-only blocks consume colors on \(X\), but do not obstruct coloring
\(v\).

---

## 3. Complementary clique realizations

### Definition 3.1

The complement of piece \(i\) **clique-realizes** \(\Pi\) if there are
pairwise disjoint connected vertex sets

\[
  Y_{i,1},\ldots,Y_{i,q}
  \subseteq V(G)\setminus(W_i-X)                       \tag{3.1}
\]

such that

1. \(Y_{i,a}\cap X=P_a\) for every \(a\);
2. \(Y_{i,a}\) and \(Y_{i,b}\) are adjacent for \(a\ne b\); and
3. contracting all \(Y_{i,a}\) and deleting every unused vertex outside
   \(W_i-X\) gives a proper minor of \(G\).

The sets may use \(v\), portals, and vertices from several other pieces.
They need not cover the complement.  Condition 1 is exact: a branch set
may not contain a vertex of the wrong adhesion block.

### Theorem 3.2 (portalized exact transfer)

If the complement of piece \(i\) clique-realizes \(\Pi\), then \(\Pi\)
extends to a proper \((t-1)\)-coloring of \(H_i\).

#### Proof

Contract the sets in (3.1) to vertices \(y_1,\ldots,y_q\), and delete the
unused complement vertices.  By Definition 3.1 this is a proper minor
\(M_i\) of \(G\), so \(M_i\) is \((t-1)\)-colorable.  The vertices
\(y_1,\ldots,y_q\) form a clique and hence receive pairwise distinct
colors.

Keep the colors on \(W_i-X\), and give every \(x\in P_a\) the color of
\(y_a\).  This is proper:

* each \(P_a\) is independent;
* edges between different blocks have differently colored ends; and
* every original edge from \(W_i-X\) to \(P_a\) became an edge to
  \(y_a\) in \(M_i\).

The equality classes on \(X\) are exactly the blocks of \(\Pi\), since
the \(y_a\) have distinct colors. \(\square\)

### Theorem 3.3 (multi-piece gluing)

Suppose \(q\le t-1\), every piece complement clique-realizes the same
state \(\Pi\), and

\[
  \beta_N(\Pi)\le t-2.                                 \tag{3.2}
\]

Then \(G\) is \((t-1)\)-colorable, a contradiction.

#### Proof

Theorem 3.2 gives a coloring of each \(H_i\) inducing exactly \(\Pi\) on
\(X\).  In each coloring the blocks have distinct colors.  Permute the
palettes so corresponding blocks agree.  The colorings glue because piece
interiors are pairwise anticomplete.

Exactly \(\beta_N(\Pi)\) colors occur on \(N\).  By (3.2), some color of
the \((t-1)\)-palette is absent from \(N\); assign it to \(v\).  A color
used only on portals is harmless because portals outside \(N\) are not
neighbors of \(v\). \(\square\)

For two pieces this specializes to the earlier separation theorem: the
\(A\)-side realization transfers the state to the \(B\)-side, and vice
versa.  The new theorem permits several pieces and makes the portal colors
part of the aligned adhesion state.

---

## 4. Exact one-step minor transitions

For a piece \(H_i\), let \(\mathcal E_i\) be the exact \(X\)-states which
extend to a \((t-1)\)-coloring of \(H_i\).

Call a one-step minor operation \(\mu\) **\(X\)-label-preserving in piece
\(i\)** if it is one of:

* deletion of a vertex of \(W_i-X\);
* deletion or contraction of an edge with both ends in \(W_i-X\); or
* deletion or contraction of an edge with one end in \(W_i-X\) and one
  end in \(X\), retaining the \(X\)-endpoint as the boundary label after
  contraction.

No two vertices of \(X\) are identified.  Let \(\mathcal E_i^\mu\) be the
extension family of the operated piece, after forgetting any extra
boundary edges created by a contraction.

### Theorem 4.1 (portal minor-transition theorem)

For every \(X\)-label-preserving operation \(\mu\) in piece \(i\), there
is an exact state \(\Pi_\mu\) such that

\[
\begin{aligned}
&q(\Pi_\mu)\le t-1,qquad
  \beta_N(\Pi_\mu)\le t-2,\tag{4.1}\\
&\Pi_\mu\in\mathcal E_i^\mu,\tag{4.2}\\
&\Pi_\mu\in\bigcap_{j\ne i}\mathcal E_j,\tag{4.3}\\
&\Pi_\mu\notin\mathcal E_i.\tag{4.4}
\end{aligned}
\]

Equivalently,

\[
  (\mathcal E_i^\mu\setminus\mathcal E_i)
  \cap\bigcap_{j\ne i}\mathcal E_j                 \tag{4.5}
\]

contains a state satisfying (4.1).

#### Proof

Apply \(\mu\) to the full graph \(G\).  The result \(G^\mu\) is a proper
minor, hence has a \((t-1)\)-coloring \(c\).  Let \(\Pi_\mu\) be the
partition of \(X\) into its nonempty color classes.  These classes are
independent in the original \(G[X]\), even if contraction temporarily
added boundary edges.  At most \(t-1\) classes occur.

The vertex \(v\) remains adjacent to every vertex of \(N\), so its color
is absent from \(N\).  Hence at most \(t-2\) color classes of
\(\Pi_\mu\) meet \(N\), proving (4.1).

Restricting \(c\) to the operated piece proves (4.2).  Every other piece
is unchanged; after any extra contraction edges are forgotten, its
restriction proves (4.3).

Suppose contrary to (4.4) that \(\Pi_\mu\in\mathcal E_i\).  Color the
original piece \(H_i\) with this state, permuting its palette so each
block color agrees with \(c\) on the other pieces.  Glue along \(X\).
The color \(c(v)\) is still absent from \(N\), so assign it to \(v\).
This gives a \((t-1)\)-coloring of \(G\), a contradiction. \(\square\)

Theorem 4.1 is the exact portal analogue of the earlier two-side
minor-transition lemma.  It is strictly stronger information than static
boundary defects or a single exact-trace coloring.

---

## 5. The first portal survivor is eliminated

Consider the first graph emitted by `degree8_cutvertex_portal_probe.py`.
The boundary \(N=\{0,\ldots,7\}\) has

\[
  E(N)=E(K_4[0,1,2,3])\cup\{36,47,56\},               \tag{5.1}
\]

the portal \(z\) sees \(2,3\), the two branch shores \(R_1,R_2\) see
\(z\) and every vertex of \(N-\{0,1\}\), and the other exterior shore
\(D\) sees every vertex of \(N-\{0\}\) but not \(z\).  The shores are
otherwise anticomplete.  Let \(v\) see all of \(N\) and no portal or
shore.

The star-only anchor encoding did not close this graph.  Arbitrary
complementary realizations do.  Use

\[
\Pi=
 \{0,4,5,z\}\mid\{1\}\mid\{2,6,7\}\mid\{3\}.        \tag{5.2}
\]

All four blocks are independent and \(\beta_N(\Pi)=4\).

For the piece containing \(R_1\), complementary branch sets are

\[
\begin{aligned}
Y_1&=\{0,4,5,z,v,R_2\},&Y_2&=\{1\},\\
Y_3&=\{2,6,7,D\},&Y_4&=\{3\}.
\end{aligned}                                         \tag{5.3}
\]

For the \(R_2\)-piece interchange \(R_1,R_2\).  For the \(D\)-piece use

\[
\begin{aligned}
Y_1&=\{0,4,5,z,v,R_1\},&Y_2&=\{1\},\\
Y_3&=\{2,6,7,R_2\},&Y_4&=\{3\}.
\end{aligned}                                         \tag{5.4}
\]

The sets in each row are connected, pairwise disjoint, have the exact
traces (5.2), and are pairwise adjacent.  Theorem 3.3 therefore eliminates
this configuration.  The essential move, absent from the earlier encoding,
is that \(Y_1\) uses both \(v\) and an outside branch shore to connect the
portal block.

`degree8_portal_exact_state_probe.py` reconstructs these witnesses.

---

## 6. A sharp falsification of the coarse static hope

The following finite quotient satisfies all of the same coarse attachment
bounds.  Let

\[
  E(N)=E(K_3[0,1,7])
       \cup E(C_5[2,4,5,3,6]),                         \tag{6.1}
\]

let \(z\) have the single boundary neighbor \(2\), let both branch shores
miss exactly \(\{0,1\}\) and meet \(z\), and let \(D\) miss exactly
\(\{0\}\) and miss \(z\).  Thus \(\alpha(N)=1+2=3\).

An exhaustive check proves both:

1. the portal quotient has no \(N\)-meeting \(K_6\)-model; and
2. there is no partition of \(X=N\cup\{z\}\) into at most six independent
   blocks, at most five of which meet \(N\), whose complement is
   clique-realized for all three pieces.

For item 1 the check exhausts all 462 partitions of an arbitrary used
subset of \(N\) into six nonempty traces and all \(7^4\) placements or
omissions of \(z,R_1,R_2,D\).  For item 2 it checks all 19,052 eligible
partitions of \(X\); 2,355 are independent, and every one fails on at
least one piece complement.

Run `degree8_portal_static_falsification_verify.py` to reproduce the
enumeration.

This graph is not claimed to be seven-connected, contraction-critical, or
a counterexample to Hadwiger.  It falsifies precisely the hoped-for static
local statement

\[
\begin{gathered}
\alpha(N)\le3,quad
|N-N(R_i)|\le2,quad |N-N(D)|\le1,\quad zR_i\ne\varnothing\\
\Longrightarrow
\text{an }N\text{-meeting }K_6\text{ or a common complementary state}.
\end{gathered}                                         \tag{6.2}
\]

---

## 7. Exact remaining requirement

Static attachment and coloring-extension data are therefore insufficient.
An actual minor-minimal counterexample must additionally satisfy the
transition condition forced by Theorem 4.1:

\[
  (\mathcal E_i^\mu\setminus\mathcal E_i)
  \cap\bigcap_{j\ne i}\mathcal E_j\ne\varnothing      \tag{7.1}
\]

for every label-preserving internal deletion or contraction, with a state
having \(\beta_N\le t-2\).

The next finite-boundary target is consequently precise: prove that no
portal-boundaried pieces with the degree-eight cutvertex attachment bounds
can satisfy (7.1) for every one-step internal minor operation while avoiding
both an \(N\)-meeting \(K_6\)-model and a common state covered by Theorem
3.3.  This requirement uses genuine minor-critical geometry and is not
present in the finite quotient (6.1).

The first bounded cell of this target is now eliminated in
`hadwiger_degree8_portal_transition_smallpieces.md`: for the explicit
boundary (6.1) with exact defects, no transition-satisfying three-piece
architecture exists when every piece has at most two interior vertices.
