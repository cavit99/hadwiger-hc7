# A one-block contact-adhesion theorem

## 1. Scope

Let \(t\) be the least failing parameter for Hadwiger's Conjecture and let
\(G\) be a proper-minor-minimal counterexample. Put \(r=t-1\). Thus \(G\)
has no \(K_t\)-minor, \(G\) is not \(r\)-colourable, and every proper minor
of \(G\) is \(r\)-colourable.

This note proves a contact-augmentation-or-colour-gluing statement for one
specific, but automatic, adhesion geometry. Its engine is a one-step minor
transition: contract a connected shore together with an independent block
of the adhesion. This forces that exact boundary equality block on the
opposite side.

The result does not prove the full uniform model-meeting assertion. It does
exclude a concrete infinite class of deficient-contact separators.

## 2. One-block transition across a separation

### Theorem 2.1 (one-block adhesion gluing)

Let \((A,B)\) be a separation of \(G\), with

\[
S=A\cap B,\qquad A-B\ne\varnothing,\qquad B-A\ne\varnothing.
\]

Suppose that \(P\subseteq S\) has order at least two and satisfies:

1. \(P\) is independent;
2. \(S-P\) is a clique;
3. every vertex of \(P\) is adjacent to every vertex of \(S-P\); and
4. there are connected sets \(D_A\subseteq A-S\) and
   \(D_B\subseteq B-S\) such that every vertex of \(P\) has a neighbour
   in each of \(D_A,D_B\).

If

\[
q:=|S-P|+1\le r,
\]

then \(G\) is \(r\)-colourable, a contradiction.

#### Proof

The set \(X_A=D_A\cup P\) is connected: \(D_A\) is connected and every
vertex of \(P\) has a neighbour in \(D_A\). Contract \(X_A\) to one
vertex \(z_A\), and delete all remaining vertices of \(A-S\). The result
is a proper minor \(J_B\) of \(G\), and therefore has an \(r\)-colouring.

Retain that colouring on \(B-S\). Expand the boundary by giving every
vertex of \(P\) the colour of \(z_A\), and retain the colours on \(S-P\).
This is a proper colouring of \(G[B]\):

* there is no edge inside \(P\);
* every edge from \(P\) to \(B-S\) became an edge from \(z_A\) in the
  contracted minor; and
* every vertex of \(S-P\) is adjacent to \(z_A\), because it is adjacent
  to every vertex of \(P\).

Moreover, the boundary equality partition is exactly

\[
\Pi=\{P\}\mathbin{\dot\cup}
       \bigl\{\{x\}:x\in S-P\bigr\}.                 \tag{2.1}
\]

Indeed, the image of \(P\), together with the \(|S-P|\) singleton
vertices, induces a \(K_q\) in \(J_B\). Hence its \(q\) blocks receive
pairwise distinct colours.

Symmetrically, contract \(X_B=D_B\cup P\), delete the rest of \(B-S\),
and expand. This gives an \(r\)-colouring of \(G[A]\) inducing the same
exact partition (2.1) on \(S\).

Permute the \(r\) colours on one side so that corresponding blocks of
\(\Pi\) agree. Since there is no edge from \(A-S\) to \(B-S\), the two
colourings glue to an \(r\)-colouring of \(G\), a contradiction. Every
contraction used above is of one connected set, and no vertex outside
\(P\) is identified with a boundary vertex. \(\square\)

### Corollary 2.2 (the numerical inequality is automatic)

Under the other hypotheses of Theorem 2.1, the inequality \(q\le r\) is
automatic in the counterexample setting.

#### Proof

Choose \(p\in P\). By assumptions 2 and 3,

\[
\{p\}\cup(S-P)
\]

is a clique of order \(q\) in \(G\). Since \(G\) has no \(K_t\)-minor,
it has no \(K_t\) subgraph. Thus \(q\le t-1=r\). \(\square\)

### Corollary 2.3 (deficiency-one adhesion)

There is no separation satisfying condition 4 for which

\[
G[S]\cong K_{|S|}-xy
\]

for one missing edge \(xy\). Take \(P=\{x,y\}\) in Theorem 2.1.

This conclusion has no upper bound on \(|S|\) as a hypothesis. Minor
exclusion itself gives \(|S|-1\le t-1\), hence \(|S|\le t\).

## 3. Application to a contact-maximal clique model

Fix \(v\in V(G)\) and a \(K_{t-1}\)-model

\[
\mathcal B=(B_1,\ldots,B_{t-1})
\]

in \(G-v\) maximizing the number of bags meeting \(N(v)\). Let \(A\) be
the union of the contact bags and \(C\) the union of the noncontact bags.
There is at least one noncontact bag, or adjoining the bag \(\{v\}\)
would give a \(K_t\)-model. The set \(C\) is connected, because its
branch bags are connected and pairwise adjacent.

### Lemma 3.1 (the contact region separates)

Every \(v\)-\(C\) path meets \(A\).

#### Proof

Suppose a \(v\)-\(C\) path avoids \(A\), and truncate it at its first
vertex in a noncontact bag \(B_j\subseteq C\). Its successor after \(v\)
lies in \(N(v)\), while all vertices strictly between \(v\) and the
terminal avoid every model bag. Adjoin to \(B_j\) the successor of \(v\)
and all subsequent path vertices except the terminal, but do not adjoin
\(v\). The enlarged bag is connected, remains inside \(G-v\), preserves
all old model adjacencies, and meets \(N(v)\). This increases the number
of contact bags, contrary to maximality. \(\square\)

Choose an inclusion-minimal set \(S\subseteq A\) separating \(v\) from
\(C\). Let \(D_v\) be the component of \(G-S\) containing \(v\), and
let \(D_C\) be the component containing \(C\).

### Lemma 3.2 (two full distinguished shores)

Every vertex of \(S\) has a neighbour in both \(D_v\) and \(D_C\).

#### Proof

For \(s\in S\), minimality of \(S\) gives a \(v\)-\(C\) path avoiding
\(S-\{s\}\). Since \(S\) separates, this path uses \(s\). The segment
before \(s\) lies in \(D_v\), and the segment after \(s\) lies in the
component containing the connected set \(C\), namely \(D_C\).
\(\square\)

### Theorem 3.3 (contact-adhesion exclusion)

For the separator \(S\) above,

\[
\overline{G[S]}\ne K_p\mathbin{\dot\cup}(|S|-p)K_1
\qquad\text{for every }p\ge2.                         \tag{3.1}
\]

Equivalently, the nonedges of \(G[S]\) cannot be exactly all pairs inside
one independent block \(P\), with every other separator vertex complete
to all of \(S\).

#### Proof

If (3.1) failed, let \(P\) be the vertex set of the \(K_p\)-component in
the complement. Then \(P\) is independent in \(G[S]\), \(S-P\) is a
clique, and all \(P\)-to-\(S-P\) edges are present. Use the separation

\[
A'=D_v\cup S,\qquad B'=V(G)\setminus D_v.
\]

Here \(A'\cap B'=S\), and no edge joins the two open sides because \(D_v\)
is a component of \(G-S\). Lemma 3.2 lets us take \(D_A=D_v\) and
\(D_B=D_C\subseteq B'-S\) in Theorem 2.1. Corollary 2.2 supplies the
colour bound, giving a contradiction. \(\square\)

Thus every deficient-contact separator has genuinely multi-class or
non-clique missing-edge geometry. In particular it cannot be a clique
minus one edge.

## 4. Correct Menger inequality

Let

\[
\lambda=\tau_G(v,C)
\]

be the minimum order of a \(v\)-\(C\) separator. Menger's theorem gives
\(\lambda\) internally disjoint \(v\)-\(C\) paths. Their first vertices in
\(A\) are distinct, so

\[
|A|\ge\lambda\ge\kappa(G).                            \tag{4.1}
\]

If the contact model has \(s\) contact bags, one bag contains first-hit
vertices of at least

\[
\left\lceil\frac{\kappa(G)}s\right\rceil              \tag{4.2}
\]

of these paths. For the least-counterexample package one may insert any
audited connectivity lower bound, currently at least

\[
\kappa(G)\ge
\max\left\{7,\left\lceil\frac t8\right\rceil\right\},
\]

with the stronger installed thresholds \(8,9,10\) for
\(t\ge17,29,41\).

Importantly, (4.1) does **not** assert that a minimum separator is contained
in \(A\). That assertion is false in general: all \(v\)-\(C\) paths may
pass through \(A\) and then through a smaller bottleneck outside \(A\).
Theorem 3.3 instead uses an inclusion-minimal separator contained in \(A\),
whose existence follows from Lemma 3.1 and whose size need not equal
\(\lambda\).

## 5. Exact remaining gap

Theorem 3.3 settles the first non-clique adhesion cell using an actual
minor transition, not static colour-extension signatures. To continue,
one needs one of the following genuinely stronger mechanisms:

1. two vertex-disjoint connected shore witnesses for two nontrivial
   independent blocks of a boundary partition;
2. a label-preserving contact augmentation; or
3. a proof that the complement of some contact separator must have the
   forbidden one-component form (3.1).

Generic connectedness supplies one shore witness and is exactly why the
one-block theorem is automatic. It does not supply two disjoint witnesses,
which is the next gammoid/knittedness threshold.

### Example 5.1 (why connectedness does not give two blocks)

Let an open shore \(D\) be the cycle

\[
a_1b_1a_2b_2a_1,
\]

and let four adhesion vertices \(p_1,q_1,p_2,q_2\) attach respectively
only to \(a_1,b_1,a_2,b_2\) inside \(D\), with no other terminal--\(D\)
edges. Put \(P=\{p_1,p_2\}\) and \(Q=\{q_1,q_2\}\). The shore \(D\) is
connected and every adhesion vertex has a neighbour in it. Nevertheless
there are no disjoint connected subgraphs of \(D\cup P\cup Q\), one
containing \(P\) and the other containing \(Q\). Such subgraphs would
contain vertex-disjoint \(a_1\)-\(a_2\) and \(b_1\)-\(b_2\) paths in the
cycle, which do not exist for alternating terminals.

Thus the next extension really needs relative linkage, knittedness, or a
minor-critical transition that defeats this alternating obstruction; it
cannot follow from the two full-shore property alone.
