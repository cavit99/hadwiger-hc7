# Exact-state depth for minimum-separator chains

## 1. Purpose

The web and portal calculations repeatedly produce a new separator of the
same order inside the current shore.  It is not enough to say that this
process "cannot continue forever": a minor-critical graph is finite, but
its order is not bounded a priori.  The theorem below supplies the missing
uniform invariant.  It does not use planarity, a prescribed boundary graph,
or named portal labels.

Throughout, an ordered separation is a pair \((O,I)\) with

\[
 O\cup I=V(G),\qquad E(O-I,I-O)=\varnothing,
\]

and adhesion \(S=O\cap I\).  A sequence \((O_i,I_i)\) is nested inward if

\[
 O_i\subseteq O_{i+1},\qquad I_{i+1}\subseteq I_i.       \tag{1.1}
\]

It is strict if each consecutive nesting has a nonempty open annular
vertex set, or has a nontrivial linkage strand which is contracted in the
pumping operation.  Equivalently for the applications here, passing from
the outer inward side to the next inward side loses at least one vertex
after the two adhesions are identified by the linkage.

For an ordered \(k\)-tuple \(S\), let

\[
 \mathcal E_r(L,S)
\]

denote the equality partitions of \(S\) into at most \(r\) colour classes
which extend to a proper \(r\)-colouring of \(L\).  Put

\[
 N(r,k)=\sum_{q=1}^{\min\{r,k\}}{k\brace q}.       \tag{1.2}
\]

Thus at most \(2^{N(r,k)}\) different extension families exist on an
ordered \(k\)-set.

## 2. Connectivity supplies the clean linkage

### Lemma 2.1 (nested minimum-cut linkage)

Let \(G\) be \(k\)-connected and let \((O,I)\), \((O',I')\) be nested
separations with adhesions \(S,S'\), both of order \(k\), where

\[
 O\subseteq O',\qquad I'\subseteq I.
\]

Then there are \(k\) pairwise vertex-disjoint \(S\)-\(S'\) paths.  Every
vertex of \(S\cap S'\) may be prescribed as a trivial path, and every
nontrivial path can be chosen with interior in

\[
 (I\cap O')-(S\cup S').                            \tag{2.1}
\]

Consequently the paths induce a bijection from \(S\) to \(S'\).

#### Proof

Put \(R=S\cap S'\).  Since \(G\) is \(k\)-connected, \(G-R\) is
\((k-|R|)\)-connected (with the usual complete-small-graph convention).
The set version of Menger's theorem therefore gives \(k-|R|\) disjoint
paths from \(S-R\) to \(S'-R\), with distinct ends.  Add the \(|R|\)
trivial paths.

On each nontrivial path retain a minimal subpath having one end in \(S\)
and the other in \(S'\).  Its interior avoids both adhesions.  Nesting gives

\[
 S-R\subseteq O'-I',\qquad S'-R\subseteq I-O.
\]

If a retained subpath left \(I\), the separation \((O,I)\) would force it
to meet \(S\) again.  If it entered \(I'-O'\) before its final end, the
separation \((O',I')\) would force it to meet \(S'\) earlier.  Both
possibilities contradict minimality of the retained subpath.  Hence its
interior lies in (2.1).  Truncation preserves disjointness and distinct
ends. \(\square\)

### Lemma 2.2 (coherent linkage through a chain)

For a nested sequence of order-\(k\) separations in a \(k\)-connected
graph, choose the linkage of Lemma 2.1 between each consecutive pair.
Label \(S_0\) arbitrarily and propagate the labels through the induced
bijections.  Concatenating consecutive paths gives a clean
label-preserving linkage between every \(S_i\) and \(S_j\), \(i<j\).

#### Proof

The open annuli between consecutive nested separations are disjoint.
Consecutive linkage systems meet only in their common adhesion, and the
propagated bijections use every adhesion vertex exactly once.  Concatenation
therefore produces \(k\) disjoint paths.  Lemma 2.1 confines their internal
vertices to the union of the consecutive open annuli, which is the open
annulus between \(S_i\) and \(S_j\). \(\square\)

## 3. The state-depth theorem

### Theorem 3.1 (minimum-separator state depth)

Let \(G\) be both

1. \(k\)-connected, and
2. \(r\)-minor-critical: \(G\) is not \(r\)-colourable, while every proper
   minor of \(G\) is \(r\)-colourable.

Then every strict nested chain of order-\(k\) separations has fewer than

\[
 2^{N(r,k)}                                             \tag{3.1}
\]

annuli.

#### Proof

Use Lemma 2.2 to order all adhesions coherently.  For every \(i\), record
the inward extension family

\[
 \mathcal F_i=\mathcal E_r(G[I_i],S_i),             \tag{3.2}
\]

transported to the common label set.  There are at most
\(2^{N(r,k)}\) possibilities.

If the chain had at least that many annuli, it would have more boundary
states than possible extension families.  Hence \(\mathcal F_i=\mathcal
F_j\) for some \(i<j\).  Lemma 2.2 supplies a clean label-preserving
linkage between these adhesions.  Apply the exact linked-annulus pumping
theorem: retain the outer context \(G[O_i]\), the inner side \(G[I_j]\),
and the linkage paths; delete all other annular material and all extraneous
edges incident with linkage interiors; then contract every linkage path.

The resulting rooted inner graph at \(S_i\) has extension family exactly
\(\mathcal F_j=\mathcal F_i\).  Thus the resulting graph is
\(r\)-colourable exactly when \(G\) is.  Strictness makes it a proper
minor, contradicting minor-criticality. \(\square\)

### Audit note: root edges and permutations

No isomorphism between \(G[S_i]\) and \(G[S_j]\) is assumed.  Contracting
a linkage may transport inner root edges to the outer roots.  Those
restrictions are already encoded in \(\mathcal F_j\), and equality with
\(\mathcal F_i\) is exactly what the proof uses.  Likewise, no canonical
portal names are assumed: the consecutive Menger linkages propagate their
own labels.  This is why no extra factor of \(k!\) is required in (3.1).

If two consecutive adhesions overlap, their common vertices are fixed by
the trivial paths in Lemma 2.1.  If the two adhesions are equal but the
separations are strict, all linkage paths may be trivial; pumping still
deletes the nonempty annular material and hence still produces a proper
minor.

## 4. Consequences for the current Hadwiger programme

### Corollary 4.1 (HC7 exact seven-cut descent)

In a hypothetical proper-minor-minimal counterexample to \(HC_7\), every
strict nested chain of seven-separations has fewer than

\[
 2^{N(6,7)}=2^{876}                                  \tag{4.1}
\]

annuli.

Thus the exact order-seven separators produced by a portal-rank leaf cannot
form an unbounded ladder.  A surviving descent must terminate in a torso,
branch through crossing separators, or repeat a boundary state and violate
minor-criticality.

### Corollary 4.2 (boundary-specific sharpening)

If the transported boundary families all lie in one fixed universe of
only \(m\) labelled equality partitions, the same proof replaces (3.1) by
\(2^m\).  It is not enough that the adhesions merely have the same
*unlabelled* boundary type: an arbitrary linkage bijection can move the
edges among the root labels and thereby enlarge the state universe.

For the \(K_2\vee C_5\) boundary used by the critical planar-web
programme, the two clique roots are fixed and planarity makes every
pentagon linkage dihedral.  Those transports preserve the labelled
ten-state universe, so the depth is below \(1024\).

## 5. Scope

Theorem 3.1 is a uniform structural invariant, not a proof of Hadwiger's
Conjecture.  It eliminates infinite *depth* in every fixed-order linked
separator recursion.  It does not bound the size of a single torso or the
number of mutually crossing minimum separators.  The next dichotomy is
therefore exact: a portal obstruction either reaches a bounded-depth core,
or crossing minimum separators must be uncrossed into a rooted model or a
colour-gluable decomposition.
