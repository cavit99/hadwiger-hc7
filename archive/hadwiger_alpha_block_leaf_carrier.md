# Leaf carriers in the rigid alpha/delta Gallai web

## 1. Setting

Let (r\ge3).  Let (G) be non-(r)-colourable and suppose every proper
minor of (G) is (r)-colourable.  Fix (v\in V(G)), put (H=G-v), and
assume

\[
 V(H)=V(B)\mathbin{\dot\cup}\{b_1,\ldots,b_{r-1}\},
\]

where the (b_i)'s form a clique and

\[
             (B,\{b_1\},\ldots,\{b_{r-1}\})
\]

is a spanning (K_r)-model.  Contract (B), colour the resulting proper
minor, and write

\[
 c(B)=\alpha,\qquad c(b_i)=p_i,\qquad c(v)=p_j=\delta.
\]

Put (P_i=N_B(b_i)) and (F=N_B(v)).  Assume (B) is its whole minimal
equality-list core.  We work in the rigid residue of the dynamic Gallai
theorem:

1. the blocks whose palettes contain (\alpha) are pairwise
   vertex-disjoint and cover (V(B)); and
2. every other block is a (K_2)-block with palette (\{\delta\}).

Contracting every alpha-block to a node and retaining the intervening
delta bridges gives a tree, denoted by (\mathcal T_\alpha).

The exact expansion-list formula is

\[
 L(x)=\{\alpha\}\cup
 \{p_i:x\notin P_i\text{ and }(i\ne j\text{ or }x\notin F)\}. \tag{1.1}
\]

## 2. A leaf alpha-block with an exterior connector closes

### Theorem 2.1 (leaf alpha-block carrier)

Let (K) be a leaf of (\mathcal T_\alpha).  Suppose the component on the
other side of its unique delta bridge contains both

* a foot (f\in F), and
* a selected portal (p\in P_j).

Then (G) contains a (K_{r+1})-minor.

#### Proof

Let (q\in V(K)) be the end in (K) of the unique delta bridge (qy).
Write (C_K) for the palette of (K), and put (s=|C_K|).  Since the
incident block palettes at (q) are disjoint,

\[
                    \alpha\in C_K,\qquad \delta\notin C_K. \tag{2.1}
\]

The block (K) is either a clique of order (s+1), or an odd cycle with
(s=2).  In either case it has a (K_{s+1})-model whose branch sets lie
in (K).  Explicitly, for an odd cycle
\(q u_1\ldots u_{2a}q\), use

\[
             \{q\},\qquad
             \{u_1,\ldots,u_a\},\qquad
             \{u_{a+1},\ldots,u_{2a}\}.                 \tag{2.1a}
\]

The two path bags are adjacent at \(u_au_{a+1}\), and each is adjacent
to \(\{q\}\) at one end of the cycle.

The graph outside (K), beginning with (y), is connected because (K)
is a leaf alpha-block.  Choose a connected subgraph (Z_0\subseteq B-V(K))
containing (y,f,p), and put

\[
                         Z=Z_0\cup\{v,b_j\}.             \tag{2.2}
\]

It is connected through the edges (vf) and (b_jp).  It is adjacent to
(q) through (yq).  Every other vertex (x\in V(K)-\{q\}) has list
(C_K), so (2.1) and (1.1) imply

\[
                         x\in F\cup P_j.                 \tag{2.3}
\]

Hence (Z) is adjacent to every vertex of (K), and therefore to every
branch set of the (K_{s+1})-model in (K).

Let

\[
                    J_K=\{i:p_i\in C_K\}.
\]

The colour (\alpha) is not a singleton-bag colour, so

\[
                          |J_K|=s-1,qquad j\notin J_K.  \tag{2.4}
\]

If (i\notin J_K\cup\{j\}), then (p_i) is absent from the list of every
vertex of (K), including (q), whose only additional block palette is
(\{\delta\}).  Formula (1.1) gives

\[
                          V(K)\subseteq P_i.             \tag{2.5}
\]

Keep the singleton bags (\{b_i\}) for
(i\notin J_K\cup\{j\}), and discard the singleton bags indexed by
(J_K\cup\{j\}).  The kept singleton bags are pairwise adjacent.  By
(2.5) each is adjacent to every branch set inside (K); each is adjacent
to (Z) through the clique edge (b_ib_j).  We therefore have

\[
 (s+1)+1+\bigl((r-1)-(s-1)-1\bigr)=r+1
\]

pairwise disjoint connected pairwise adjacent branch sets.  They form a
(K_{r+1})-model. \(\square\)

The proof uses the internal clique capacity of a large alpha-block rather
than trying to split it into portal-complete pieces.  Its (s+1) clique
bags replace exactly the (s-1) singleton labels in its palette, while the
exterior (v)-to-(b_j) carrier supplies the two remaining units.

## 3. Exact owner-path consequence

### Corollary 3.1 (opposite leaf owners)

If (G) has no (K_{r+1})-minor and the rigid alpha/delta web has at least
two alpha-blocks, then (\mathcal T_\alpha) is a path.  One end
alpha-block contains every foot of (B), and the other contains every
vertex of (P_j).

#### Proof

For a leaf alpha-block (K), Theorem 2.1 says that its exterior cannot
contain both a foot and a (P_j)-portal.  Hence

\[
                         F\subseteq V(K)
              \quad\hbox{or}\quad
                         P_j\subseteq V(K).              \tag{3.1}
\]

Distinct alpha-blocks are vertex-disjoint.  Since (F) and (P_j) are
both nonempty, at most one leaf can satisfy the first inclusion and at
most one can satisfy the second.  Thus the alpha-block tree has at most
two leaves and is a path.

If the same end contained both (F) and (P_j), the exterior of the
opposite end would contain both sets, contradicting Theorem 2.1 there.
Therefore the two ownership types occur at opposite ends. \(\square\)

This is the large-block analogue of the end-locked
(\alpha,\delta,\alpha,\ldots,\alpha) corridor.  All branching is gone,
and the only remaining full-core spanning-singleton equality residue is an
alpha-block path with the apex feet and the selected portal class trapped
at opposite ends.

## 4. Opposite-owner exchange

### Theorem 4.1 (the opposite-owner path closes)

Under the hypotheses of Corollary 3.1, \(G\) contains a
\(K_{r+1}\)-minor.  Consequently the rigid alpha/delta web has no
counterexample.

#### Proof

Write the alpha-block path from its foot-owning end to its
\(P_j\)-owning end as

\[
                         K_0,K_1,\ldots,K_m.             \tag{4.1}
\]

Every internal alpha-block is a \(K_2\).  Indeed, it has two incident
delta bridges, and the disjointness of incident block palettes permits at
most one such bridge at a given vertex.  Any further vertex \(x\) of that
block would have \(\delta\notin L(x)\), so (1.1) would put \(x\) in
\(F\cup P_j\), contrary to the opposite-end ownership.  Thus the only
possibly non-\(K_2\) alpha-blocks are \(K_0,K_m\).

Let

\[
 C_a=\{\alpha\}\cup\{p_i:i\in Q_a\}
 \qquad(a\in\{0,m\})                                    \tag{4.2}
\]

be an endpoint palette.  We first prove that

\[
               vb_i\in E(G)\quad\hbox{for every }
               i\in Q_0\cup Q_m.                        \tag{4.3}
\]

Suppose instead that \(b_i\) is noncontact.  Recolour the quotient
\(G/B\) so that \(v\) receives \(p_i\), and let \(L_i\) be the resulting
expansion lists.  The vertices outside \(F\) keep exactly their old
lists.  Every foot lies in \(K_0\), and every nonattachment vertex of
\(K_0\) is a foot but not a \(P_j\)-portal.

If \(i\notin Q_0\), then at each such nonattachment vertex the new list
gains \(\delta\) and loses nothing.  All other lists are unchanged.
Thus every list has order at least the \(B\)-degree and one is strictly
larger; the degree-list lemma colours \(B\), and hence \(G\), a
contradiction.  Therefore \(i\in Q_0\).

Put

\[
                   C'_0=(C_0-\{p_i\})\cup\{\delta\}.     \tag{4.4}
\]

At every nonattachment vertex of \(K_0\), the new list is \(C'_0\).
At the attachment vertex \(q\), which is not a foot, the list remains
\(C_0\cup\{\delta\}\).  All lists are still degree-tight.  If \(B\)
were not \(L_i\)-colourable, the degree-list characterization would give
a block-palette decomposition.  The nonattachment vertices force the
palette of \(K_0\) to be \(C'_0\).  Hence the palette of the unique bridge
leaving \(q\) is forced to be

\[
                              \{p_i\}.                   \tag{4.5}
\]

If \(m\ge2\), the far end \(y\) of that bridge lies in the internal
alpha-\(K_2\) block \(K_1\), and its unchanged list is
\(\{\alpha,\delta\}\); it does not contain \(p_i\), contradicting
(4.5).  If \(m=1\), then \(y\) is the attachment vertex of \(K_m\).
If \(p_i\notin C_m\), (4.5) again contradicts its list.  If
\(p_i\in C_m\), removing the forced bridge palette from
\(L_i(y)=C_m\cup\{\delta\}\) forces the palette

\[
                         (C_m-\{p_i\})\cup\{\delta\}
\]

on \(K_m\), whereas every nonattachment vertex of \(K_m\) still has list
\(C_m\).  This is impossible.  Thus \(B\) is \(L_i\)-colourable in every
case, contradicting the assumed non-\(r\)-colourability of \(G\).
This proves (4.3).

If both endpoint alpha-blocks were \(K_2\), every alpha-block in the web
would be a \(K_2\), a case already eliminated by the matching-alpha
Gallai theorem.  Choose a genuine endpoint block \(K\), put
\(s=|C_K|\), and select \(i\in Q_K\).  By (4.3), \(vb_i\) is an edge.
Let \(q y\) be the unique delta bridge leaving \(K\).  The graph
\(B-V(K)\) is connected and contains the opposite owner: a \(P_j\)-portal
if \(K=K_0\), and a foot if \(K=K_m\).  Therefore

\[
 Z=(B-V(K))\cup\{v,b_i,b_j\}                            \tag{4.6}
\]

is connected.  At the foot end it is joined to \(B-V(K)\) through
\(b_jP_j\), and \(v-b_i-b_j\) connects \(v\); at the portal end it is
joined through \(vF\), and \(v-b_i-b_j\) connects \(b_j\).

The set \(Z\) is adjacent to the attachment vertex \(q\) through \(qy\).
Every other vertex of \(K\) is a foot when \(K=K_0\), or a
\(P_j\)-portal when \(K=K_m\); hence \(Z\) is adjacent to every vertex of
\(K\).  Take a \(K_{s+1}\)-model inside \(K\), keep the singleton bags
\(\{b_\ell\}\) for

\[
                         \ell\notin Q_K\cup\{j\},
\]

and use \(Z\) as one further branch set.  Every kept singleton is adjacent
to every vertex of \(K\): its colour is absent from
\(C_K\cup\{\delta\}=L(q)\) and from \(C_K\) at all other vertices.
It is adjacent to \(Z\) through \(b_j\).  The number of branch sets is

\[
 (s+1)+1+\bigl((r-1)-(s-1)-1\bigr)=r+1.
\]

They form a \(K_{r+1}\)-model, the final contradiction. \(\square\)

The proof is the promised uniform exchange.  A palette contact supplies a
zero-cost carrier; if that contact is absent, changing the quotient colour
forces a palette swap which cannot cross the rigid alpha/delta block path.
No enumeration of block orders or path length is involved.

## 5. Audit boundary

The leaf assumption is essential to Theorem 2.1 as written.  It ensures
that the exterior vertices \(y,f,p\) can be joined without using a vertex
of \(K\), so the carrier \(Z\) remains disjoint from every branch set
inside \(K\).  Theorem 4.1 nevertheless closes the only leaf arrangement
left by Corollary 3.1, using quotient-colour switching rather than an
internal-block connector.

The remaining extensions are:

1. derive the rigid alpha/delta web from an arbitrary full equality Gallai
   core while preserving the labelled model; and
2. exchange a proper minimal core with its portal-bearing hanging society.

Neither extension is supplied merely by the static block-palette theorem.
