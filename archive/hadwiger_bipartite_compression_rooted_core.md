# Bipartite compression forces parity-rooted clique cores

## Status

This note proves a label-free contraction-critical lemma.  It is not a
proof of \(HC_7\), but it replaces a family of Kempe-path statements by
actual rooted clique models and applies to every induced tree bag, of
arbitrary order.

The only non-elementary input is the proved four-colour case of Holroyd's
Strong Hadwiger Conjecture:

> If a four-colourable graph \(J\) has a set \(X\) on which every proper
> four-colouring uses all four colours, then \(J\) has an \(X\)-rooted
> \(K_4\)-minor.

Here an \(X\)-rooted \(K_4\)-model means four pairwise adjacent disjoint
connected bags, each meeting \(X\).

## 1. Compression theorem

### Theorem 1.1 (parity-rooted core)

Let \(k\ge5\).  Let \(G\) have no proper \(k\)-colouring, and let
\(T\) be a nontrivial connected induced bipartite subgraph of \(G\), with
bipartition

\[
                         V(T)=U\mathbin{\dot\cup}W.
\]

Suppose the minor \(Q=G/T\), obtained by contracting all of \(T\) to a
vertex \(z\), has a proper \(k\)-colouring \(c\).  Put
\(c(z)=\alpha\).  For any four-element set
\(\Gamma\subseteq[k]-\{\alpha\}\), let

\[
 J=Q[c^{-1}(\Gamma)]
\]

and

\[
 X_U=(N_G(U)-V(T))\cap V(J),\qquad
 X_W=(N_G(W)-V(T))\cap V(J).                       \tag{1.1}
\]

Then both \(X_U\) and \(X_W\) are four-colour-saturating in \(J\).
Consequently \(J\) contains an \(X_U\)-rooted \(K_4\)-model and an
\(X_W\)-rooted \(K_4\)-model.  Each model lies in \(G-V(T)\), and adding
the connected bag \(T\) produces a \(K_5\)-model whose other four bags
all meet the selected parity portal set.

#### Proof

Contraction changes no edge with both ends outside \(T\), and
\(z\notin V(J)\).  Thus \(J\) is literally the subgraph of \(G-V(T)\)
induced by the four named colour classes.

Every vertex of \(N_G(T)-V(T)\) is adjacent to \(z\) in \(Q\).  Therefore
the original \(\alpha\)-class is disjoint from the entire external
neighbourhood of \(T\).

Suppose a proper four-colouring \(\varphi:V(J)\to\Gamma\) omitted a
colour \(\gamma\in\Gamma\) on \(X_U\).  On \(G-V(T)\), use \(\varphi\)
on \(J\) and retain \(c\) on every old colour class outside \(\Gamma\).
This is proper because the two palettes are disjoint.

Now colour every vertex of \(U\) with \(\gamma\), and every vertex of
\(W\) with \(\alpha\).  The sets \(U,W\) are independent because \(T\)
is induced bipartite, and every internal edge of \(T\) has colour pair
\(\gamma,\alpha\).  No external neighbour of \(U\) has colour
\(\gamma\): a neighbour in \(J\) belongs to \(X_U\), where \(\gamma\)
was omitted, and a neighbour outside \(J\) retains a colour outside
\(\Gamma\).  No external neighbour of \(W\) has colour \(\alpha\), by
the preceding paragraph.  Hence this is a proper \(k\)-colouring of
\(G\), a contradiction.

Thus \(X_U\) is four-colour-saturating.  Interchanging \(U,W\) proves
the same for \(X_W\).  Strong \(HC_4\) supplies both rooted models.
They avoid \(T\), and every one of their bags contains a vertex adjacent
to \(T\).  Adding \(T\) as a fifth bag therefore gives the asserted
\(K_5\)-models. \(\square\)

## 2. Consequences at an actual edge

### Corollary 2.1 (two specified-singleton cores)

Let \(G\) be minor-minimal subject to having no proper \(k\)-colouring,
where \(k\ge5\), and let \(xy\in E(G)\).  Fix a \(k\)-colouring of
\(G/xy\), let \(\alpha\) be the contraction colour, and choose any four
other colour classes with induced graph \(J\).  Then

\[
 X_x=(N_G(x)-\{y\})\cap V(J),\qquad
 X_y=(N_G(y)-\{x\})\cap V(J)
\]

are four-colour-saturating in \(J\).  Hence \(J\) has an
\(X_x\)-rooted \(K_4\)-model and an \(X_y\)-rooted \(K_4\)-model.
Adjoining \(\{x\}\) to the first and \(\{y\}\) to the second gives two
\(K_5\)-models with a prescribed singleton bag, each avoiding the other
endpoint.

This applies to the named edge of an alternating tree-society cut.  The
operation-critical output is an actual rooted clique core at each end,
not merely five pairwise Kempe detours.

### Corollary 2.2 (induced-star center and leaves)

If \(T\) is an induced star with center \(h\) and leaf set \(L\), then
both

\[
 (N(h)-V(T))\cap V(J),qquad
 (N(L)-V(T))\cap V(J)
\]

are four-colour-saturating.  The center version may be expanded with
\(h\) receiving a missing colour and only the independent leaves retaining
\(\alpha\); the reverse version swaps the two star bipartition classes.

## 3. Exact completion dichotomy for \(HC_7\)

Specialize to \(k=6\).  Let \(\mathcal R\) be either parity-rooted
\(K_4\)-model from Theorem 1.1, and let \(X\) be its saturating portal
set.  Suppose there are two disjoint connected reserved sets \(A_1,A_2\),
disjoint from \(J\cup T\), such that

\[
 T\sim A_1,qquad T\sim A_2,qquad A_1\sim A_2.
\]

Put

\[
                         Y=X\cap N(A_1)\cap N(A_2).  \tag{3.1}
\]

If \(Y\) is four-colour-saturating in \(J\), Strong \(HC_4\) gives a
\(Y\)-rooted \(K_4\)-model.  Together with \(T,A_1,A_2\), its four bags
form an explicit \(K_7\)-model.  Therefore a \(K_7\)-minor-free host has
the opposite, exact state:

> For every available completion pair \(A_1,A_2\), some proper
> four-colouring of \(J\) has a colour represented on \(X\) but absent
> from the fully compatible portals \(Y\).

This is a named operation-forced dark portal colour.  A two-shore exchange
need only transport this state to the opposite bag; no arbitrary linkage
or universal rooted-\(K_5\) theorem is required.

The same conclusion holds for the star-center model with \(\{h\}\) in
place of the whole bag \(T\); in that form the reserved sets may use the
unused leaves of the star.

### Corollary 3.1 (operated-edge common-portal state)

Use Corollary 2.1 at an edge \(xy\), and let \(A\) be a connected set
disjoint from \(J\cup\{x,y\}\) and adjacent to both \(x\) and \(y\).
Put

\[
 Z=X_x\cap X_y\cap N(A).                            \tag{3.2}
\]

Exactly one of the following conclusions is available.

1. \(Z\) is four-colour-saturating, in which case a \(Z\)-rooted
   \(K_4\)-model together with \(\{x\},\{y\},A\) is a \(K_7\)-model.
2. There is a proper four-colouring of \(J\) and a colour \(\gamma\)
   which occurs on both \(X_x\) and \(X_y\), but on no portal that is
   simultaneously adjacent to \(x,y\), and \(A\).

Indeed, if \(Z\) is not saturating, choose a colouring omitting
\(\gamma\) on \(Z\).  The separate saturation of \(X_x,X_y\) forces
\(\gamma\) to occur on each of them.  Thus the negative state consists
either of two side-private \(\gamma\)-portals or of a common
\(x,y\)-portal which is dark to \(A\).  This is precisely a two-shore
capacity state.  Applied to an alternating tree edge, it records the
failure of the desired split in one common operation colouring.

## 4. Audit boundaries

1. **The center and leaves do not share a colour.**  In the star proof the
   center receives \(\gamma\); only the independent leaves receive
   \(\alpha\).
2. **Induced bipartiteness is essential.**  Extra edges inside \(U\) or
   \(W\) would invalidate the two-colour expansion.
3. **The old \(\alpha\)-class stays fixed.**  The recolouring uses only
   \(\Gamma\), so \(\alpha\) remains absent from every external neighbour
   of \(T\).
4. **The minor lifts literally.**  Since \(z\notin J\), every rooted bag
   consists of unchanged vertices and edges of \(G-V(T)\).
5. **No unproved rooted theorem is used.**  Only the established
   four-colour Strong Hadwiger theorem is invoked.
6. **The theorem does not itself prove \(K_7\).**  Two compatible reserved
   bags are still needed.  Failure of that compatibility is recorded as a
   dark portal state, not declared a contradiction.
