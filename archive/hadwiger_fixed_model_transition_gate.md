# Fixed-model consequences of the all-trace transition gate

## 1. Scope and audit

Let \(r\ge2\).  Throughout, \(G\) is not \(r\)-colourable and every
proper minor of \(G\) is \(r\)-colourable.  Fix \(v\in V(G)\), put

\[
                         H=G-v,\qquad N=N_G(v),
\]

and fix a \(K_r\)-model

\[
                         {\cal B}=(B_1,\ldots,B_r)             \tag{1.1}
\]

in \(H\).  Write \(M=\bigcup_i B_i\).

The transition-splicing proof in
hadwiger_all_trace_transition_gate.md has been checked against the
following failure modes.

1. The deleted edge is put on the side coloured by an honest colouring
   of \(H\), never on the side coloured from \(G-e\).
2. Equality of boundary partitions, not equality of arbitrary colour
   names, is sufficient: the boundary bijection extends to a permutation
   of the whole palette.
3. The colour of \(v\) is absent from all of \(N\) in a colouring of
   \(G-e\), because \(e\subseteq H\) and no \(vN\)-edge was deleted.
4. In the unpinned case the image of \(d(v)\) ranges through every
   colour absent from the trace boundary, giving the full free palette,
   not merely one colour.
5. A minimum-pin Kempe switch is performed in \(G-e\), so it preserves
   properness; a colour missing on the adhesion ensures that the switch
   creates no new pin there.

The earlier \(C_7\) illustration was incorrectly called
proper-minor-minimal.  It is only edge-critical.  This affects that
illustration, not any theorem: the proofs use only the explicitly
provided colourings of the relevant edge-deleted graphs.

This note pushes the gate theorem against the fixed model (1.1).

## 1A. Crossed transitions: the exact two-shore exchange

For a colouring \(d\) of \(G-e\), define its **marked state** at \(X\)
to be

\[
 \sigma_X(d)=\bigl(\Pi_X(d),P_X(d)\bigr),\qquad
 P_X(d)=\{x\in X:d(x)=d(v)\}.                              \tag{1.2}
\]

The second coordinate is either empty or one whole block of the first
coordinate.

### Theorem 1.1 (opposite shores have disjoint marked states)

Let \((A,B)\) be a separation of \(H\), with \(X=A\cap B\), and let

\[
 e_A\in E(H[A])\setminus E(H[B]),\qquad
 e_B\in E(H[B])\setminus E(H[A]).                           \tag{1.3}
\]

If \(d_A,d_B\) are proper \(r\)-colourings of \(G-e_A,G-e_B\),
respectively, then

\[
                         \sigma_X(d_A)\ne\sigma_X(d_B).       \tag{1.4}
\]

In particular, opposite unpinned transitions cannot induce the same
boundary equality partition.

#### Proof

Suppose the marked states agree.  Their equality partitions agree, so
there is a palette permutation \(\pi\) such that

\[
                         \pi d_A(x)=d_B(x)\quad(x\in X).      \tag{1.5}
\]

If the common marked block is nonempty, (1.5) necessarily maps
\(d_A(v)\) to \(d_B(v)\).  If it is empty, both apex colours are unused
on \(X\), and the boundary bijection can be extended so that it also
maps \(d_A(v)\) to \(d_B(v)\).  Thus in both cases arrange

\[
                         \pi d_A(v)=d_B(v)=:\alpha.           \tag{1.6}
\]

Use \(d_B\) on \(A\), use \(\pi d_A\) on \(B-A\), and give \(v\)
colour \(\alpha\).  The restrictions agree on \(X\).  The colouring
\(d_B\) is proper on \(A\), because its sole missing edge is \(e_B\),
which is not an edge of \(H[A]\).  Symmetrically, \(\pi d_A\) is proper
on every edge having a vertex in \(B-A\), including \(e_B\).  Finally,
\(d_B(v)\) is absent from \(N\) on the \(A\)-side and
\(\pi d_A(v)=\alpha\) is absent from \(N\) on the \(B\)-side.  Hence
the crossed colouring is a proper \(r\)-colouring of \(G\), a
contradiction.  \(\square\)

This is a genuine colour-gluable-separator conclusion.  It uses no
private-root count and no rooted-model assumption: the two minor
transitions repair one another's deleted edges.

### Corollary 1.2 (component state capacity)

Fix \(X\subseteq V(H)\).  For a component \(C\) of \(H-X\), let
\(\Sigma_C(X)\) be the set of marked states induced by colourings of
\(G-e\), over all edges \(e\) having at least one endpoint in \(C\) and
both endpoints in \(C\cup X\).  If \(C,D\) are distinct components of
\(H-X\), then

\[
                         \Sigma_C(X)\cap\Sigma_D(X)
                         =\varnothing.                        \tag{1.7}
\]

#### Proof

An edge contributing to \(\Sigma_C\) and one contributing to
\(\Sigma_D\) lie on opposite open shores of the separation which groups
\(C\) on one side and every other component on the other.  A common
marked state would contradict Theorem 1.1.  \(\square\)

Thus a transit adhesion has a finite, injective operation-state
capacity.  The state records only an equality partition and one marked
block; no geometric information has been hidden in its definition.

### Corollary 1.3 (per-partition shore bound)

Fix an equality partition \(\Pi\) of \(X\) with \(b\) blocks.  At most
\(b+1\) components \(C\) of \(H-X\) can have \(\Sigma_C(X)\) contain a
state whose first coordinate is \(\Pi\).

Consequently, if every component under consideration contains an
internal edge and some transition state, their total number is at most

\[
 \sum_{\Pi\in{\rm Part}(X)}\bigl(|\Pi|+1\bigr)
 ={\rm Bell}(|X|+1),                                        \tag{1.8}
\]

where partitions not realizable by proper boundary colourings may be
omitted.

#### Proof

For fixed \(\Pi\), a marked state has only \(b+1\) possible second
coordinates: one of its \(b\) blocks or the empty set.  Corollary 1.2
makes the state sets of distinct components disjoint, proving the first
claim.  Summing over first coordinates proves (1.8).  \(\square\)

The equality with the Bell number has a direct interpretation: a marked
partition of \(X\) is exactly a partition of \(X\cup\{v^\ast\}\), where
\(v^\ast\) is either a singleton (the unpinned state) or joins the
marked block.

This is a literal capacity theorem for minor-transition states.  In
particular, if an all-trace argument synchronizes one boundary partition
across many shores, no more than one shore may be unpinned and no two
may pin the same boundary block.

## 1B. Simultaneous contraction forces a locked Kempe shore

The crossed theorem can be used without first synchronizing two
independently chosen transition colourings.

### Theorem 1.4 (double-operation repair exclusion)

In the separation of Theorem 1.1, assume the two edges \(e_A,e_B\) are
vertex-disjoint.  Contract both, colour the proper minor
\(G/e_A/e_B\), and expand the two contraction vertices.  This gives a
proper colouring \(f\) of

\[
                              G-\{e_A,e_B\}                   \tag{1.9}
\]

in which the ends of each deleted edge have one colour.

Call an **\(A\)-repair** any proper colouring of \(G-e_B\) which agrees
with \(f\) on \(X\cup\{v\}\), and define a \(B\)-repair symmetrically.
Then an \(A\)-repair and a \(B\)-repair cannot both exist.

#### Proof

An \(A\)-repair is a colouring of \(G-e_B\), and a \(B\)-repair is a
colouring of \(G-e_A\).  Their restrictions have exactly the same
colours on \(X\cup\{v\}\), hence the same marked state at \(X\).
Theorem 1.1 gives a contradiction.  \(\square\)

Thus one of the two monochromatic edge defects is not repairable from
its own shore while the common gate state is held fixed.

### Corollary 1.5 (Kempe-lock dichotomy)

For at least one side \(C\in\{A,B\}\), write \(e_C=xy\) and
\(f(x)=f(y)=\beta\).  For every colour \(\gamma\ne\beta\), at least one
of the following holds in the \(\{\beta,\gamma\}\)-subgraph of (1.9):

1. \(x\) and \(y\) lie in the same component, giving a bichromatic
   \(x\)-to-\(y\) detour which avoids \(e_C\); or
2. they lie in distinct components and **both** of those components
   meet \(X\cup\{v\}\).

#### Proof

Choose a side with no repair, as supplied by Theorem 1.4.  If \(x,y\)
are in different bichromatic components and, say, the component of
\(x\) avoids \(X\cup\{v\}\), then the separation implies that this
component is contained in the open \(C\)-shore.  Switching
\(\beta,\gamma\) on it fixes \(X\cup\{v\}\), makes \(x,y\) different,
and restores \(e_C\).  The other deleted edge remains deleted.  This is
a \(C\)-repair, a contradiction.  The same argument applies to the
component of \(y\).  \(\square\)

If \(e_C\) is an essential edge of a transit branch bag, outcome 1 is
a potential replacement detour in \(G-\{e_A,e_B\}\); it may still pass
through \(v\).  Outcome 2 is an adhesion/apex carrier for each endpoint.
Hence simultaneous minor-criticality gives the following exact,
label-free residue:

\[
\boxed{\text{model-edge detour (possibly apex-transiting), or two
gate-reaching Kempe carriers, for every colour.}}            \tag{1.10}
\]

No assertion is made that the detours for different colours are
disjoint.  That is the remaining packing step needed to split an
already double-foot bag.

### Corollary 1.6 (fixed-model cleaning form)

Suppose the locked edge \(e_C=xy\) of Corollary 1.5 belongs to a branch
bag \(B_i\) of (1.1).  For every \(\gamma\ne\beta\), at least one of
the following concrete certificates exists.

1. There is a \(\{\beta,\gamma\}\)-detour in \(H-\{e_A,e_B\}\)
   whose interior avoids every branch bag other than \(B_i\).  In a
   chosen connected support for \(B_i\), replacing the use of \(e_C\)
   by this detour is a label-preserving model-clean rerouting.
2. Such a detour exists in \(H-\{e_A,e_B\}\), but every one meets a
   branch bag other than \(B_i\).  The first such hit is a named
   transit-bag obstruction.
3. The two ends are connected in the bichromatic subgraph of (1.9) but
   disconnected after deleting \(v\).  Thus every bichromatic detour
   uses \(v\), an explicit **apex-transit obstruction**.
4. The two endpoint components are distinct and both meet
   \(X\cup\{v\}\), giving the two gate-reaching carriers of
   Corollary 1.5.

#### Proof

In outcome 1 of Corollary 1.5, first ask whether the ends remain
connected after deleting \(v\).  If not, item 3 holds.  If so, either
some detour avoids all foreign bags, giving item 1, or every such
detour meets a foreign bag, giving item 2.  In item 1 the support

\[
          (H[B_i]-e_C)\cup P
\]

is connected: if \(e_C\) was a bridge of the old support, \(P\)
reconnects its two sides, and otherwise the old support without
\(e_C\) was already connected.  Enlarge the branch-set vertex set by
the internal vertices of \(P\).  They avoid all old bags, so
disjointness and every old interbag adjacency are preserved.  Outcome
2 of Corollary 1.5 is item 4.  \(\square\)

Thus the simultaneous transition produces an actual clean rerouting,
a named foreign transit bag, an apex-transit obstruction, or a
two-carrier gate for every colour.  It never ends at an unlabelled
assertion that “some Kempe path exists.”

If \(\beta\ne\alpha:=f(v)\), only one colour layer can be
apex-transiting: \(v\) belongs to the
\(\{\beta,\gamma\}\)-subgraph only for \(\gamma=\alpha\).
Consequently, for every \(\gamma\notin\{\beta,\alpha\}\):

* every detour in Corollary 1.5 already lies in \(H\); and
* in the two-component outcome, both carriers meet the actual adhesion
  \(X\), not merely \(X\cup\{v\}\).

Thus at least \(r-2\) colour layers are genuine
model-rerouting/transit/gate layers inside the apex-deleted graph.  The
hypothesis \(\beta\ne\alpha\) is automatic when the locked edge has an
endpoint in \(N\), since its edge to \(v\) remains in (1.9).  If neither
endpoint lies in \(N\), the exceptional equality \(\beta=\alpha\) must
be retained; then the apex may occur in every colour layer.

## 2. Model-clean absorption of a fan endpoint

Say that (1.1) is **contact-maximal** if the number

\[
 s=\bigl|\{i:B_i\cap N\ne\varnothing\}\bigr|                 \tag{2.1}
\]

is maximum among all \(K_r\)-models in \(H\).

### Lemma 2.1 (first-hit absorption)

Let \(n\in N-M\), and suppose \(P\) is an \(n\)-to-\(M\) path in \(H\).
Truncate \(P\) at its first vertex in \(M\), say in \(B_j\).  Adding the
model-free prefix to \(B_j\) preserves a \(K_r\)-model.  It either

1. increases the number of contact bags; or
2. gives \(B_j\) two distinct vertices of \(N\).

#### Proof

Before its terminal vertex the truncated path avoids every old bag.
Its union with \(B_j\) is connected, is disjoint from the other bags,
and retains every old interbag edge.  It contains the new vertex
\(n\).  If \(B_j\) was noncontact, outcome 1 holds.  Otherwise its old
neighbourhood vertex is distinct from \(n\notin M\), giving outcome 2.
\(\square\)

Thus in a contact-maximal model, every path from a new neighbourhood
vertex into the model is automatically a model-clean double-foot
certificate.

### Theorem 2.2 (pinned fan selects a clean double foot)

Assume (1.1) is contact-maximal.  Let \(e\in E(H)\), let
\(X\subseteq B_i\) for some branch bag, and choose, among all proper
\(r\)-colourings \(d\) of \(G-e\), one minimizing

\[
                         |\{x\in X:d(x)=d(v)\}|.              \tag{2.2}
\]

Suppose this pinned set is nonempty.  If

\[
                         r-|d(X)|>s,                          \tag{2.3}
\]

then some branch bag contains two distinct vertices of \(N\), reached
after a label-preserving model-clean absorption.

#### Proof

If the current model already has a double-foot bag, there is nothing to
prove.  Assume it has none.

By the minimum-pinning theorem, for every colour
\(\gamma\notin d(X)\) and every pinned \(p\in X\), the
\(\{d(v),\gamma\}\)-component of \(G-e\) contains both \(p\) and \(v\).
Delete the last edge at \(v\).  This gives in \(H-e\), and hence in
\(H\), a path from \(p\in B_i\) to a vertex \(n_\gamma\in N\) of colour
\(\gamma\).

The \(r-|d(X)|\) vertices \(n_\gamma\) are distinct.  If the model has
no double-foot bag, each of its \(s\) contact bags contains exactly one
vertex of \(N\), and every noncontact bag contains none.  Thus

\[
                              |N\cap M|=s.                    \tag{2.5}
\]

Under (2.3), some \(n_\gamma\) lies outside \(M\).  Reverse its fan path
and truncate it at the first old model vertex.  Lemma 2.1 gives a clean
contact augmentation or a double foot.  Contact maximality excludes the
first outcome, proving the theorem.  \(\square\)

No disjointness among the different Kempe paths is asserted or needed.
Only one endpoint outside the old model is absorbed.

The conclusion concerns the resulting model, not necessarily the
original one.  It therefore does **not** imply the false persistent
inequality \(|X|\ge r-s\) merely from the assumption that the original
model has no double foot.  Indeed, in a connected graph any
\(N-M\)-to-\(M\) path already gives a double foot in a contact-maximal
model.  The extra information here is only that the double foot can be
chosen on a specified missing-colour layer of the pinned transition.

## 3. An unpinned off-haven transition glues

Let \(c\) be an \(r\)-colouring of \(H\).  Call a colour **private on
\(N\)** when it occurs at exactly one vertex of \(N\).

### Lemma 3.1 (off-haven edge transition is colour-gluable)

Let \((A,B)\) be a separation of \(H\), with \(X=A\cap B\), and let

\[
                         e\in E(H[A])\setminus E(H[B]).       \tag{3.1}
\]

Suppose:

1. \(d\) is an unpinned \(r\)-colouring of \(G-e\);
2. \(\Pi_X(d)=\Pi_X(c)\); and
3. some colour \(\gamma\notin c(X)\), private on \(N\) in \(c\), has
   its unique root in \(B-X\).

Then the two side colourings align to an \(r\)-colouring of \(G\), a
contradiction.

#### Proof

The transition-splicing theorem says that every colour outside \(c(X)\)
occurs on \(N\cap(A-X)\).  Applied to the private colour \(\gamma\),
this puts its unique root in \(A-X\), contrary to hypothesis 3.

Equivalently, the proof is constructive: align \(d|_X\) to \(c|_X\),
map \(d(v)\) to \(\gamma\), use \(c\) on \(A\), use the aligned \(d\)
on \(B-X\), and give \(v\) colour \(\gamma\).  The edge \(e\) is proper
on the \(c\)-side, while the unique \(\gamma\)-root lies on the
\(d\)-side where \(d(v)\)'s colour is absent from \(N\).  \(\square\)

### Corollary 3.2 (model-haven form)

Assume \(c\) has \(h>0\) private roots and \(|c(X)|<h\).  Suppose the
component \(K\) of \(H-X\) containing every model bag disjoint from
\(X\) also contains all private roots whose colours are absent from
\(c(X)\).  If \(e\) lies on a different component side of \(X\), no
unpinned colouring of \(G-e\) can induce \(\Pi_X(c)\).

#### Proof

At least one private-root colour is absent from \(c(X)\), and its root
lies in \(K\).  Orient the separation so that \(e\) lies in \(A-X\)
and \(K\subseteq B-X\), and apply Lemma 3.1.  \(\square\)

The hypothesis is exactly the agreement of the private-colour haven
with the model haven at \(X\).  Thus an unpinned operation off the common
haven is not merely a linkage obstruction: its side restrictions
literally colour-glue.

## 4. The fixed-model transit-gate theorem

The preceding two mechanisms combine cleanly.

### Theorem 4.1 (small transit gate trichotomy)

Assume:

1. \({\cal B}\) is a contact-maximal \(K_r\)-model with \(s\) contact
   bags;
2. \(X\subseteq B_i\) for one branch bag;
3. \(D\) is a component of \(H-X\) containing none of the bags
   \(B_j\) for \(j\ne i\), while a component \(K\ne D\) contains all
   those \(r-1\) bags;
4. \(c\) is an \(r\)-colouring of \(H\) for which all private roots
   with colours outside \(c(X)\) lie in \(K\); and
5.
   \[
                  |c(X)|<\min\{h,r-s\},                     \tag{4.1}
   \]
   where \(h\) is the number of private colours of \(c\) on \(N\).

Let

\[
 e\in E(H[D\cup X])\setminus E(H[V(H)-D])                   \tag{4.2}
\]

be an edge on the \(D\)-side.  Choose a colouring \(d\) of \(G-e\)
globally minimizing its pinned set on \(X\).  Then at least one of the
following holds:

1. \(\Pi_X(d)\ne\Pi_X(c)\); or
2. a label-preserving modification of \({\cal B}\) is a contact-maximal
   \(K_r\)-model with a double-foot branch bag.

#### Proof

Suppose \(\Pi_X(d)=\Pi_X(c)\).  If \(d\) is unpinned, Corollary 3.2
contradicts the common-haven placement of the private roots.

If \(d\) is pinned, then

\[
 r-|d(X)|=r-|c(X)|>s
\]

by (4.1).  Theorem 2.2 gives a clean model move and, by contact
maximality, a double foot.  This is outcome 2.  \(\square\)

### Equality-cell specialization

For a star-contraction trace with an independent block \(S\subseteq N\)
and

\[
                         |N-S|=r-1,                          \tag{4.4}
\]

the \(r-1\) vertices of \(N-S\) are private.  The private-colour haven
puts all roots whose colours are absent from \(c(X)\) into one component
whenever \(|X|<r-1\).  If that component is the model-haven component
\(K\), Theorem 4.1 applies whenever

\[
                         |c(X)|<r-s.                          \tag{4.5}
\]

Hence a contact-deficient model with deficiency \(r-s\) cannot preserve
the exact trace state at such an off-haven transit edge without
producing a double-foot model.  The alternatives are explicit and
uniform:

\[
\boxed{
\begin{array}{c}
\text{boundary partition changes under the one-step minor;}\\
\text{or a clean contact augmentation exists;}\\
\text{or a branch bag obtains a certified double foot.}
\end{array}}
\tag{4.6}
\]

## 5. Exact remaining limitation

The crossed-transition Theorem 1.1 is stronger than the static
model-haven/Rado statement: opposite shores cannot reuse one marked
minor-transition state.  Theorem 4.1 adds a model-clean trichotomy, but
does not yet split a double-foot bag while preserving its \(r-1\)
labelled adjacencies.

Nor does it eliminate a **large chromatic gate** with
\(|c(X)|\ge r-s\), or a gate at which every canonical edge transition
changes the exact boundary partition.  Those two residues are genuine:

* pinning supplies paths but not arbitrary mutual disjointness; and
* a changed equality partition need not itself be colour-gluable with
  the opposite side.

The next uniform principle must therefore show that repeated
partition-changing transitions around one transit bag either cycle back
to a common boundary state (where Theorem 4.1 applies) or realize the
same rooted clique partition on both shores.
