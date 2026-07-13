# Contact augmentation: a rooted model, a portal-rich bag, or a Hall--Menger deficit

## 1. Setup

Let \(G\) be a finite graph, let \(N\subseteq V(G)\), and let

\[
 \mathcal B=(B_1,\ldots,B_m)
\]

be pairwise disjoint connected branch sets of a \(K_m\)-model. Thus every
two \(B_i,B_j\) are adjacent. Assume

\[
 |N|\ge m.                                         \tag{1.1}
\]

A bag is **contacted** if it meets \(N\). The model is \(N\)-meeting if
every bag is contacted.

## 2. A portal-rich bag splits

### Lemma 2.1 (two-root bag split)

If a connected bag \(B\) contains distinct roots \(u,v\in N\), then it has
a partition

\[
 B=X\mathbin{\dot\cup}Y
\]

into nonempty connected adjacent sets with \(u\in X\) and \(v\in Y\).

#### Proof

Choose a \(u\)-\(v\) path, extend it to a spanning tree of \(B\), and delete
an edge of the path. The two tree components give \(X,Y\), and the deleted
tree edge gives their adjacency. \(\square\)

This is a genuine extra carrier. It is not automatically a larger clique
model, because the adjacencies from \(B\) to the other \(m-1\) bags may be
concentrated on one side. That concentration is precisely the
portal-placement obstruction addressed by the splitter and web lemmas.

## 3. The relative Hall--Menger theorem

Assume now that every contacted bag contains exactly one vertex of \(N\).
Let \(C\subseteq[m]\) index the contacted bags, put \(c=|C|\), and let

\[
 I_0=[m]-C,\qquad R=N-\bigcup_{i=1}^m B_i.
\]

Then (1.1) gives

\[
 |R|=|N|-c\ge m-c=|I_0|.                          \tag{3.1}
\]

Delete all model bags from \(G\), and denote the resulting graph by \(H\).
Replace every edge of \(H\) by its two orientations. For every
\(i\in I_0\), add an artificial **sink** terminal \(\tau_i\), with an arc
from every external portal of \(B_i\) to \(\tau_i\), and with no arc out of
\(\tau_i\). Denote this auxiliary digraph by \(A\), and put
\(T=\{\tau_i:i\in I_0\}\).

### Theorem 3.1 (augmentation or relative deficiency)

Exactly one of the following alternatives is certified.

1. There are \(|I_0|\) pairwise vertex-disjoint \(R\)-\(T\) paths in \(A\),
   with distinct initial and terminal vertices. They augment
   \(\mathcal B\) to an \(N\)-meeting \(K_m\)-model in \(G\).
2. There are a nonempty set \(I\subseteq I_0\) and a vertex set
   \(X\subseteq V(H)\) such that

   \[
    |X|<|I|,                                       \tag{3.2}
   \]

   and, in \(H-X\), no path runs from a vertex of \(R-X\) to a vertex
   having a neighbour in \(B_i\), for any \(i\in I\). Thus \(X\)
   separates the unused roots from the external portal sets of the bags
   indexed by \(I\), relative to paths avoiding all model bags.

#### Proof

Apply the directed vertex form of Menger's theorem to the sets \(R,T\) in
\(A\).
If it gives \(|T|=|I_0|\) disjoint paths, their terminal ends are distinct
and hence exhaust \(T\). No artificial terminal can occur internally on
one of the directed paths because every terminal is a sink. If a path
contains more than one vertex of \(R\), truncate
it before its last such vertex. The resulting initial roots remain
distinct.

Delete each artificial terminal from its path and add a final edge into
the corresponding \(B_i\). The resulting paths in \(G\) are mutually
disjoint, start at distinct roots of \(R\), and avoid every original model
bag until their last edge. Adjoin the path assigned to \(i\) to \(B_i\).
The bags remain disjoint and connected, their old pairwise adjacencies
remain, and each now contains a distinct vertex of \(N\). This proves
alternative 1.

Otherwise Menger gives an \(R\)-\(T\) separator \(Z\) with
\(|Z|<|T|\). Put

\[
 I=\{i\in I_0:\tau_i\notin Z\},\qquad X=Z-T.
\]

Since \(|Z|<|I_0|\), the set \(I\) is nonempty and

\[
 |X|=|Z|-|Z\cap T|<|I_0|-|Z\cap T|=|I|.
\]

Suppose that, for some \(i\in I\), an \(R-X\) path in \(H-X\) ended at
an external portal \(p\) of \(B_i\). Adding the artificial edge
\(p\tau_i\) gives a directed \(R\)-\(T\) path in \(A\) which avoids \(X\).
It cannot contain an artificial terminal internally because every terminal
is a sink, and therefore avoids \(Z\cap T\). Since \(\tau_i\notin Z\),
this path avoids all of \(Z\), a
contradiction. Thus \(X\) has the asserted relative separation property.
\(\square\)

The two outcomes are mutually exclusive. If the full linkage exists, its
paths assigned to any \(I\) are disjoint model-avoiding paths to the
corresponding portal sets, so every relative separator for those paths has
order at least \(|I|\).

## 4. Contact-augmentation trichotomy

### Corollary 4.1

For every \(K_m\)-model and root set \(N\) satisfying \(|N|\ge m\), at
least one of the following holds:

1. the model is already \(N\)-meeting;
2. a contacted bag contains two roots and admits the split in Lemma 2.1;
3. all contacted bags contain one root, and Theorem 3.1 either augments the
   model to an \(N\)-meeting model or supplies a relative Hall deficit
   \((I,X)\) with \(|X|<|I|\).

This statement is uniform in \(m\), contains no planarity assumption, and
is strictly weaker than Hadwiger's Conjecture. It identifies two concrete
objects—not an amorphous failure of rerouting—which a complete proof must
eliminate:

* a portal-rich clique bag whose external adjacencies resist the two-root
  split; or
* a subfamily of more branch bags than the size of the outside separator
  shielding all their portals from unused roots.

## 5. Application to a hypothetical Hadwiger counterexample

Let \(G\) be a minimal counterexample at parameter \(t\), choose \(v\), put
\(N=N_G(v)\), and let \(B_1,\ldots,B_{t-1}\) be the guaranteed unrooted
\(K_{t-1}\)-model in \(G-v\). Since \(\delta(G)\ge t\),

\[
 |N|\ge t>t-1.
\]

Apply Corollary 4.1 with ambient graph **\(G-v\)** and \(m=t-1\).  This
qualification is necessary: if augmentation were run in \(G\), an
augmenting path could use \(v\), so \(v\) could not then be used as a
separate branch set.  The first or augmentation outcome gives an
\(N\)-meeting \(K_{t-1}\)-model in \(G-v\), and adding the singleton bag \(\{v\}\)
gives a \(K_t\)-minor. Therefore every counterexample-derived model has
one of the following two audited obstructions:

1. a multiply rooted branch bag with concentrated interbag portals; or
2. a relative deficit \((I,X)\), where fewer than \(|I|\) outside vertices
   separate all unused roots from the external portals of \(|I|\) bags.

The first obstruction is exactly the domain of label-preserving bag
surgery. The second is the precise separator input for color gluing or
knittedness. A uniform contact-or-separator proof no longer needs to
quantify over arbitrary failed reroutings: it needs to show that a
minor-critical graph converts either object into a proper-minor coloring,
a smaller exact adhesion, or a \(K_t\)-model.

## 6. Scope warning

The separator \(X\) is **relative to paths avoiding the existing model
bags**. It need not be a vertex cut of the whole graph, because a path may
run through another branch bag. Promoting a relative deficit to a global
or knitted adhesion is the remaining hard step. Omitting this qualifier
would make the theorem false and would hide the same portal-concentration
gap encountered in the sharp \(t=7\) cells.
