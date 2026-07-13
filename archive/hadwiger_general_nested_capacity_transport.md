# Nested minimum cuts preserve rooted capacity models

## 1. A label-free transport theorem

Let \(G\) be \(k\)-connected.  Let \(S_0\) be a \(k\)-cut and let
\(D\) be a component of \(G-S_0\).  Give the vertices of \(S_0\)
distinct labels.  Suppose the outer side contains pairwise disjoint
connected bags

\[
                         A_1,\ldots,A_m                 \tag{1.1}
\]

forming a \(K_m\)-model.  Precisely, require

\[
                 A_i\subseteq V(G)-D\quad(1\le i\le m),          \tag{1.0}
\]

where the adhesion vertices in \(S_0\) are counted outside \(D\).
Suppose also that the labelled roots in
\(S_0\) are partitioned among these bags: for a partition
\(S_0=R_1\dot\cup\cdots\dot\cup R_m\), every \(A_i\) contains
\(R_i\).  The bags may contain additional vertices of that outer side.  Condition
(1.0) is essential: allowing an old bag to enter the annulus can make it
overlap a transported linkage path.

Let \(S_1\) be another \(k\)-cut and let \(F\) be a component of
\(G-S_1\) such that

\[
                         F\subseteq D.                    \tag{1.2}
\]

### Theorem 1.1 (rooted clique-model transport)

There is a bijection \(\lambda:S_0\to S_1\) and pairwise
vertex-disjoint paths \(L_s\), joining \(s\) to \(\lambda(s)\), whose
nontrivial interiors lie in

\[
                  D-(F\cup S_0\cup S_1).                 \tag{1.3}
\]

After putting

\[
 A_i'=A_i\cup\bigcup_{s\in R_i}V(L_s),                  \tag{1.4}
\]

the sets \(A_1',\ldots,A_m'\) are disjoint connected bags forming the
same \(K_m\)-model, and

\[
                         A_i'\cap S_1=\lambda(R_i).       \tag{1.5}
\]

#### Proof

Use the ordered separations

\[
 (V(G)-D,S_0\cup D),\qquad (V(G)-F,S_1\cup F).
\]

They are nested.  Moreover \(N(F)=S_1\): if a vertex of \(S_1\)
had no neighbour in \(F\), the other \(k-1\) cut vertices would
separate \(F\) from that unused vertex itself, contrary to
\(k\)-connectivity.  Thus
\(S_1=N(F)\subseteq S_0\cup D\).  The nested minimum-cut linkage lemma
gives \(k\) disjoint paths, fixes every common adhesion vertex by a
trivial path, and confines every other path to the open annulus (1.3).

By (1.0), the paths avoid the old outer bags except at their distinct
roots in \(S_0\).  Since the \(R_i\) partition \(S_0\) and the old bags
are disjoint, \(A_i\cap S_0=R_i\).  Hence the unions (1.4) are disjoint
and connected.  Enlarging
bags cannot destroy any old interbag edge, so they still form a
\(K_m\)-model.  Since \(S_1-S_0\subseteq D\), (1.0) says that no old
bag contains another inner-adhesion vertex.  The linkage paths meet the
inner adhesion only at their distinct final vertices, proving (1.5).
\(\square\)

## 2. Capacity is monotone under inward transport

For disjoint labelled sets \(T_1,\ldots,T_q\subseteq S_0\), say that
a shore has \((T_1,\ldots,T_q)\)-capacity when it contains pairwise
disjoint connected carriers, the \(j\)-th carrier meeting the portal set
of every label in \(T_j\).

### Theorem 2.1 (capacity lift)

If the inner fragment \(F\), with labels transported to \(S_1\) by
\(\lambda\), has \((T_1,\ldots,T_q)\)-capacity, then the original shore
\(D\) has the same capacity.

#### Proof

Let \(Y_j\subseteq F\) be the inner carriers.  For every nontrivial
path \(L_s\), delete its old endpoint \(s\) and retain the remaining
tail through \(\lambda(s)\); for a trivial path no tail is needed.
Join to \(Y_j\) all tails whose labels lie in \(T_j\).  A nontrivial
inner end lies in \(S_1-S_0\subseteq D\), and the carrier has a vertex
adjacent to that end; hence the union is connected.  The first vertex of
the tail after \(s\) is an old \(s\)-portal in \(D\).  For a trivial path,
\(s=\lambda(s)\) and \(Y_j\) itself already meets the old \(s\)-portal
set.  Thus the resulting set lies in \(D\), is connected, and meets every
old portal set indexed by \(T_j\).  Distinct results are disjoint because
the \(Y_j\), label sets, and linkage paths are disjoint, while the path
interiors avoid \(F\). \(\square\)

Equivalently, every rooted capacity family of an inner fragment is a
subfamily of the capacity family of the outer shore after transport.
Thus a capacity state forbidden in \(D\) remains forbidden in every
nested fragment, while every rooted clique model already built on the
outer side survives at the new adhesion.

## 3. Minimum fragments remove exact-cut recursion

Choose, among all pairs \((S,F)\) satisfying (1.2), one with \(|F|\)
minimum; the original pair \((S_0,D)\) is allowed.  If \(|F|>1\), then
for every nonempty proper \(X\subsetneq F\),

\[
                         |N_G(X)|\ge k+1.                 \tag{3.1}
\]

Indeed another component of \(G-S\) is anticomplete to \(F\), so it
survives as a far side outside \(N_G(X)\); hence \(k\)-connectivity gives
\(|N_G(X)|\ge k\).  If equality held, take a component \(K\) of
\(G[X]\).  Then \(N_G(K)\subseteq N_G(X)\), while the same far side
survives.  Connectivity forces \(|N_G(K)|\ge k\), so
\(N_G(K)=N_G(X)\).  Thus \(K\) is a smaller component behind a nested
\(k\)-cut, contrary to the choice of \(F\).

Consequently any local augmentation theorem with outcomes

\[
 \text{target minor},\qquad
 \text{new capacity},\qquad
 \text{proper nested }k\text{-cut}                  \tag{3.2}
\]

closes on the minimum fragment: the second outcome lifts back and
contradicts the original capacity obstruction, while the third is
excluded by (3.1).  Only a singleton fragment or a genuinely
strict-surplus atomic torso can survive.

## 4. Scope

The theorem is uniform in \(k,m\) and in the block sizes \(|R_i|\).
It is the scalable mechanism extracted from the \(HC_7\) two-pair web:
nested exact cuts do not erase labels, rooted model adjacencies, or
capacity failures.  What it does not supply is the local augmentation
theorem for an arbitrary strict-surplus torso.  For \(HC_7\) and two
pair blocks, that local theorem is the audited planar-web/curvature
closure; for general \(t\), proving its analogue remains the uniform
model-meeting obstruction.

The outer-side condition (1.0) is essential.  If an old bag is allowed
to enter the annulus, a clean adhesion-to-adhesion linkage can be forced
through it and (1.4) need not remain disjoint.  Thus the theorem
transports a model built on the already processed side; it does not
transport an arbitrary model crossing the cut.
