# Omitted-bag absorption in the exact two-gate source-tight cell

> **Status correction (12 July 2026).** The absorption moves in Section 5
> are valid. However, a globally contact-maximal model cannot have a Hall
> circuit of order greater than one: every singleton proper subset of such
> a circuit is linkable and would augment contact. Therefore Theorem 5.6 is
> only a conditional descent/exit theorem, not a proof that this cell
> directly contains (K_{r+1}). Sections 6 onward record conditional
> geometry before applying the label-escape move; they are not a live
> terminal residue.

## 1. Setup

Use the notation and hypotheses of
`hadwiger_source_tight_two_gate_web.md`.  In particular,

\[
 |X|=r-2,\qquad Y=\{y_1,y_2\},\qquad |P|=|I|=r-1,
\]

and every component of \(U-Y\) has exact neighbourhood \(Y\cup P\).
The old deficient bags \((B_j:j\in I)\) are pairwise adjacent, and the
accessible old bag is \(B\).  For \(p\in P\), let \(K_p\) be its private
region in \(B\), and put

\[
 A_j=N_B(B_j),\qquad
 L(p)=\{j:A_j\cap K_p\ne\varnothing\},\qquad
 O(p)=\{j:A_j\subseteq K_p\}.
\]

The private regions are pairwise disjoint, so

\[
                 \sum_{p\in P}|O(p)|\le r-1.                 \tag{1.1}
\]

The point of this note is that the unused label in a far Hall
certificate can be put into a *gate branch set*, rather than merely used
to repair one far carrier.  This removes every gate-support requirement
from the low-owner case.

## 2. Uniform omitted-bag absorption

### Theorem 2.1 (a live low-owner private region closes)

Assume that \(U-Y\) has at least two components.  If some \(p\in P\)
satisfies

\[
                       |O(p)|\le1,
        \qquad          L(p)\ne\varnothing,                  \tag{2.1}
\]

then \(G\) contains a \(K_{r+1}\)-minor.  No adjacency between either
gate and \(X\) is required.

#### Proof

Choose \(b\in L(p)\) as follows.  If \(O(p)=\{j\}\), take \(b=j\);
if \(O(p)=\varnothing\), take any \(b\in L(p)\).  Thus

\[
                         O(p)\subseteq\{b\},
                  \qquad b\in L(p).                          \tag{2.2}
\]

Take distinct components \(C,D\) of \(U-Y\).  Let

\[
 \begin{aligned}
 Z_1&=\{y_1\}\cup C\cup K_p\cup B_b,\\
 Z_2&=\{y_2\}\cup D\cup(B-K_p).
 \end{aligned}                                               \tag{2.3}
\]

These sets are disjoint.  The set \(Z_1\) is connected: \(C\) meets
both \(y_1\) and \(p\), the set \(K_p\) is connected and contains
\(p\), and \(b\in L(p)\) supplies an edge from \(K_p\) to \(B_b\).
Every component of \(B-K_p\) contains a portal in \(P-p\), while \(D\)
meets \(y_2\) and every portal; hence \(Z_2\) is connected.  The sets
\(Z_1,Z_2\) are adjacent, for example through an edge from \(y_1\) to
\(D\), because \(N(D)=Y\cup P\).

Use the far Hall certificate omitting label \(b\).  For each \(x\in X\),
adjoin its suffix to its terminal retained bag
\(B_{\lambda_b(x)}\), producing pairwise disjoint, pairwise adjacent
connected far carriers \((F_x:x\in X)\).  These suffixes avoid every old
model bag except their retained terminal bag, so they are disjoint from
the omitted bag \(B_b\) and from both sets in (2.3).

The set \(Z_1\) is adjacent to every \(F_x\), since it contains \(B_b\)
and the deficient old bags are pairwise adjacent.  For every retained
label \(j\ne b\), (2.2) gives \(j\notin O(p)\), so
\(A_j\not\subseteq K_p\).  Hence \(A_j\cap(B-K_p)\ne\varnothing\), and
therefore \(Z_2\) is adjacent to every \(F_x\) as well.

Consequently

\[
                 Z_1,Z_2,(F_x:x\in X)                       \tag{2.4}
\]

are \(2+(r-2)=r\) disjoint, connected, pairwise adjacent branch sets in
\(G-v\).  They contain respectively the distinct neighbours
\(y_1,y_2,X\) of \(v\).  Adding \(\{v\}\) gives a
\(K_{r+1}\)-model. \(\square\)

### Corollary 2.2 (exact support obstruction)

If the exact two-component source-tight cell is \(K_{r+1}\)-minor-free,
then

\[
              L(p)\ne\varnothing\quad\Longrightarrow\quad
              |O(p)|\ge2.                                  \tag{2.5}
\]

In particular, at least

\[
                    \left\lceil\frac{r-1}{2}\right\rceil   \tag{2.6}
\]

portals satisfy \(L(p)=\varnothing\).  For \(HC_7\), at least three of
the five portal-private regions are completely label-free.

#### Proof

The implication is the contrapositive of Theorem 2.1.  A label can be
owned by at most one portal, so (1.1) holds.  Thus at most
\(\lfloor(r-1)/2\rfloor\) portals can own at least two labels.  Every
remaining portal has at most one owned label and must have empty
\(L(p)\) by (2.5), proving (2.6). \(\square\)

This is strictly stronger than a bound on the number of labels seen by a
low-owner region: every such region is dead to *all* deficient clique
bags.  It also shows that the remaining obstruction is not a gate-support
pattern on \(X\).  It is a concentration theorem: all deficient-label
contacts with \(B\) are confined to at most
\(\lfloor(r-1)/2\rfloor\) private regions and to the common portal core
\(B-\bigcup_pK_p\).

## 3. The named-shadow alternative

Let

\[
             F=V(G-v)-\bigl(Q\cup U\cup X\bigr).          \tag{3.1}
\]

### Lemma 3.1 (dead private lobe exposes a far shadow)

Suppose \(L(p)=\varnothing\).  If \(E\) is a component of
\(K_p-p\), then \(E\) has a neighbour in \(F\).  Consequently, under
the additional normalization that no such far shadow is present,
\(K_p=\{p\}\).

#### Proof

Inside \(B\), every neighbour of \(E\) outside \(E\) is \(p\), by the
definition of \(K_p\).  The set \(E\) contains no portal other than
\(p\), and therefore has no neighbour in \(U\).  The equality
\(L(p)=\varnothing\) excludes every edge from \(E\) to a deficient bag
\(B_j\).  If \(E\) also missed \(F\), then

\[
                         N_G(E)\subseteq X\cup\{p,v\}.     \tag{3.2}
\]

The right side has order at most \((r-2)+2=r\), and the deficient bags
survive outside \(E\cup N(E)\).  This contradicts the assumed
\((r+1)\)-connectivity of \(G\). \(\square\)

The far-shadow conclusion is useful dynamically.  In a target-free
exact cell there are at least (2.6) pairwise disjoint dead private
regions.  Every non-singleton one therefore names an actual off-model
shadow which bypasses its portal cut.  Absorbing or operating on these
shadows is the only remaining way to avoid the small cut (3.2).

## 4. Crossed-state consequence

Let \(W=Y\cup P\).  Distinct exact web components have disjoint
boundary-faithful operation-state spectra on \(W\), by Theorem 6.1 of
`hadwiger_source_tight_two_gate_web.md`.  Combined with Corollary 2.2,
the target-free residue has the following exact form:

1. at least \(\lceil(r-1)/2\rceil\) disjoint dead portal regions in
   \(B\);
2. each non-singleton dead region has a named far shadow as in Lemma 3.1;
3. every internal operation on either of two exact web components must
   induce a different equality partition on the common \((r+1)\)-set
   \(W\).

Thus a closure argument no longer has to align arbitrary gate support on
\(X\).  It suffices to prove one of the following uniform statements:

* a named far shadow can be absorbed into its dead region without
  destroying the exact Hall circuit, after which Theorem 2.1 applies; or
* operations on two exact web components force the same state on \(W\).

The second item is precisely a crossed-state contradiction, while the
first is a label-preserving model move.  No assertion here identifies an
exact star-trace colouring with an operation colouring.

## 5. Dead-shadow incidence and the bypass potential

> **Potential audit correction.**  The absorption moves in this section
> preserve the labelled model and are valid.  However, a globally
> contact-maximal model cannot at the same time have a nontrivial
> inclusion-minimal Hall circuit: every uncontacted singleton is already
> nonlinkable, since a singleton linkage would itself augment contact.
> Consequently the phrase “contact-maximal, then minimum circuit” makes
> the co-rank-one \(|I|=r-1>1\) cell vacuous.  Lemmas 5.2, 5.4 and 5.5
> must be read as the following local trichotomy: the displayed model move
> gives either more contacted bags, a smaller Hall circuit, or a strict
> same-\((c,|I|)\) enlargement of \(B\).  Thus Theorem 5.6 eliminates the
> exact cell modulo those descent outcomes; it is not, without a separate
> proof closing every exit, a direct proof that \(G\) has a
> \(K_{r+1}\)-minor.  The corrected general statement is
> `hadwiger_root_free_bag_saturation.md`.

The preceding named-shadow alternative can be sharpened after making the
standard finite choice of the model.  Among contact-maximal labelled
models, first minimize the order of a Hall circuit in the uncontacted
labels; subject to this, maximize the order of the accessible bag \(B\).
The statements below are conditional only on being in the co-rank-one
cell after this choice.  Encountering a smaller Hall circuit is therefore
an allowed strict descent, not a discarded case.

Call a path \(T\) a **far escape from \(K_p\)** when

* its first vertex lies in \(K_p-p\);
* all its internal vertices lie in \(F\); and
* its last vertex is its first vertex in \(Q-K_p\).

Thus the last vertex lies either in \(B-K_p\), or in a deficient bag
\(B_j\).  The former kind is a **\(B\)-bypass** and the latter a
**label escape**.

### Lemma 5.1 (every nontrivial dead region has a far escape)

If \(L(p)=\varnothing\) and \(K_p\ne\{p\}\), then \(K_p\) has a far
escape.

#### Proof

Let \(E\) be a component of \(K_p-p\), and let \(S\) be the component
containing \(E\) in the graph induced by \((K_p-p)\cup F\).  Suppose
there is no far escape.  Distinct components of \(B-p\) have no edge,
so the only neighbour of \(S\) in \(K_p-S\) is possibly \(p\).  There
is no neighbour in \(B-K_p\) or in a deficient bag, by the assumption
that there is no escape.  There is no neighbour in \(U\): a vertex of
\(K_p-p\) is not a portal, while an edge from \(F\) to \(U\) would put
its endpoint in the same component of the graph outside \(Q\cup X\) as
\(U\), contrary to the definition of \(F\).  Consequently

\[
                         N_G(S)\subseteq X\cup\{p,v\}.   \tag{5.1}
\]

This set has order at most \((r-2)+2=r\).  A deficient bag survives
outside \(S\cup N(S)\), so (5.1) contradicts
\((r+1)\)-connectivity. \(\square\)

### Lemma 5.2 (a \(B\)-bypass is a strict model move)

At the model/circuit choice made above, no dead private region has a
\(B\)-bypass.

#### Proof

Let \(T\) be such a bypass and enlarge the accessible bag to

\[
                         B'=B\cup V(T).                  \tag{5.2}
\]

The new bag is connected.  Its added vertices lie in \(F\), hence none
is a neighbour of \(v\); the number of contacted model bags is unchanged.
All old clique-bag adjacencies are retained, and \(|B'|>|B|\).

The uncontacted label set \(I\) cannot become fully linkable in the new
model, since such a linkage would increase the number of contacted bags.
Choose an inclusion-minimal nonlinkable subset \(J\subseteq I\).  It is
a Hall circuit.  By the primary minimality of the circuit order,
\(|J|\ge|I|\); hence \(J=I\).  Thus (5.2) is another admissible
model/circuit pair with the same first two potential coordinates and a
strictly larger accessible bag, a contradiction. \(\square\)

### Corollary 5.3 (the dead-shadow incidence graph has no merge)

No component of \(F\) meets \(K_p-p\) and \(K_q-q\) for distinct dead
portals \(p,q\).  In particular, in the bipartite incidence graph between
dead private regions and components of \(F\), every shadow vertex has
degree at most one.

#### Proof

A path through such a shadow from \(K_p-p\) to \(K_q-q\subseteq
B-K_p\) is a \(B\)-bypass for \(K_p\), contrary to Lemma 5.2.
\(\square\)

This rules out every alternating cycle in the dead-region/shadow
incidence graph.  The remaining objects are genuine private leaves, not
an uncontrolled web of mutually shared shadows.

### Lemma 5.4 (a singleton dead portal is a strict root-hub move)

At the same model/circuit choice, no dead private region is a singleton.

#### Proof

Suppose \(K_p=\{p\}\), and take one exact component \(D\) of
\(U-Y\).  Replace the accessible bag by

\[
                    B'=(B-p)\cup D\cup\{y_2\}.          \tag{5.3}
\]

Every component of \(B-p\) contains a portal in \(P-p\), by the
definition of \(K_p\).  The component \(D\) meets every portal and
\(y_2\), so (5.3) is connected.  Since \(L(p)=\varnothing\), the
vertex \(p\) is not an attachment to any deficient bag; hence \(B'\)
retains an edge to every \(B_j\).  The other old model adjacencies are
unchanged.

The new bag is contacted by \(y_2\).  If it also retains the old foot
\(a\), this still counts as one contacted bag; if \(p=a\), the new foot
\(y_2\) simply replaces it.  Thus the number of contacted bags is
unchanged.  Moreover

\[
                         |B'|=|B|+|D|>|B|.              \tag{5.4}
\]

Exactly as in Lemma 5.2, the uncontacted labels cannot all become
linkable, and a minimal new deficit cannot have smaller order at the
chosen potential.  It is therefore the same full circuit \(I\), making
(5.3) an admissible strict improvement of \(|B|\), a contradiction.
\(\square\)

The use of the exact component is important: it is a hub meeting every
portal, so no assertion that \(B-p\) itself is connected is made.

### Lemma 5.5 (a label escape is also a strict model move)

At the model/circuit choice of Section 5, no dead private region has a
label escape.

#### Proof

Let \(T\) be a label escape from \(K_p-p\) whose last vertex
\(z\) lies in a deficient bag \(B_b\).  Replace the accessible bag by

\[
                         B'=B\cup(V(T)-\{z\}).           \tag{5.5}
\]

This is connected, because the first vertex of \(T\) lies in \(B\).
It is disjoint from every other model bag; in particular the last vertex
\(z\) remains in \(B_b\).  The last edge of \(T\) makes \(B'\)
adjacent to \(B_b\), and every other old model adjacency is retained.

Every newly absorbed vertex lies in \(F\), hence is not a neighbour of
\(v\).  Thus the number of contacted bags is unchanged.  At least one
new vertex is absorbed: otherwise \(T\) would be a direct edge from
\(K_p\) to \(B_b\), contrary to \(L(p)=\varnothing\).  Therefore
\(|B'|>|B|\).

As in Lemma 5.2, the uncontacted set \(I\) cannot become linkable, and
an inclusion-minimal new deficit cannot have order smaller than \(|I|\)
at the chosen potential.  It is consequently the same circuit \(I\).
The model (5.5) now contradicts maximality of \(|B|\). \(\square\)

### Theorem 5.6 (conditional exact-portal multi-component descent)

Fix a contact count and a nontrivial Hall-circuit order, exclude a contact
augmentation and a smaller circuit, and within the remaining comparison
class maximize \(|B|\). If

\[
                  |P|=r-1
       \quad\text{and}\quad
                  U-Y\text{ has at least two components},             \tag{5.6}
\]

then the exact cell has no terminal representative in that comparison
class. Equivalently, the cell yields a target minor, more contact, a
smaller circuit, or a strict same-coordinate model enlargement.

#### Proof

If the target minor is absent, Corollary 2.2 supplies a dead portal
\(p\) (in fact at least \(\lceil(r-1)/2\rceil\) of them).  Lemma 5.4
excludes \(K_p=\{p\}\), so \(K_p\) is nontrivial.  Lemma 5.1 gives a
far escape.  Its endpoint lies either in \(B-K_p\), contradicting the
no-bypass Lemma 5.2, or in a deficient bag, contradicting Lemma 5.5.
These exhaust the first possible endpoints in \(Q-K_p\). \(\square\)

For \(HC_7\), Theorem 5.6 supplies a strict descent from the exact
five-portal, two-or-more-component source-tight cell. It does **not** close
the higher-contact or smaller-circuit exit. The later sections retain the
first-hit and state analysis as conditional geometry; they are not a
terminal residue after the absorption move.

## 6. Essential label escapes

**Scope of Sections 6--12.**  These are fixed-model auxiliary lemmas.
Under the global potential of Section 5, Theorem 5.6 says that their
target-free exact-cell hypothesis is empty.  They apply only when the
model is held fixed (so the absorption in Lemma 5.5 is not an admissible
move), or when their hypotheses arise inside a non-exact portal cell.

By Lemmas 5.1--5.2, every nontrivial dead private region has a label
escape.  Such an escape either gives the target immediately or is forced
to block the relevant far linkage.

### Theorem 6.1 (connector or essential-linkage blocker)

Let \(p\) be dead, and let \(T\) be a label escape from \(K_p\) whose
last vertex lies in \(B_b\).  If some far Hall certificate omitting
\(b\) has all its suffixes disjoint from the internal vertices of
\(T\), then \(G\) contains a \(K_{r+1}\)-minor.

Consequently, in a target-free residue, every far certificate omitting
\(b\) meets the interior of every such escape \(T\).

#### Proof

Take distinct exact web components \(C,D\) and put

\[
 \begin{aligned}
 Z_1&=\{y_1\}\cup C\cup K_p\cup V(T)\cup B_b,\\
 Z_2&=\{y_2\}\cup D\cup(B-K_p).
 \end{aligned}                                           \tag{6.1}
\]

The first set is connected along \(K_p,T,B_b\), with \(C\) joining it
to \(y_1\).  The second is connected because every component of
\(B-K_p\) contains a portal met by \(D\).  They are disjoint and are
adjacent through an edge from \(y_1\) to \(D\).

Use the assumed \(b\)-omitting certificate and form its far carriers
\((F_x:x\in X)\).  Its suffixes lie outside \(U\), avoid the old model
except at their retained terminal bags, and by hypothesis avoid the
interior of \(T\).  They are therefore disjoint from (6.1).  The set
\(Z_1\) sees every far carrier through the clique edges from \(B_b\).
Since \(L(p)=\varnothing\), every retained attachment set \(A_j\) lies
in \(B-K_p\), so \(Z_2\) sees every far carrier as well.  The two sets
in (6.1) and the \(r-2\) far carriers are the required \(r\) rooted
clique bags; add \(\{v\}\). \(\square\)

### Corollary 6.2 (exact terminal shadow residue)

Suppose a fixed target-free exact representation satisfies the three
auxiliary hypotheses that the displayed dead regions are nontrivial,
that they have far escapes, and that no such escape is a \(B\)-bypass.
Then it satisfies all of the following.

1. At least \(\lceil(r-1)/2\rceil\) portal-private regions are dead.
2. Every dead region is nontrivial and has a label escape.
3. Distinct dead regions use distinct far-shadow components.
4. A label escape ending in \(B_b\) intersects every far Hall linkage
   from \(X\) to \((B_j:j\ne b)\).

For \(HC_7\), there are at least three such dead regions.  Therefore the
remaining obstruction contains at least three pairwise private,
omitted-label-essential far blockers.  This
is the exact finite support obstruction promised by the two-gate
analysis: arbitrary gate--\(X\) nonadjacencies have disappeared, and the
only surviving information is a family of private vital-linkage
components indexed by omitted labels.

The conclusion is deliberately not promoted to a contradiction.  The
next required lemma is a gammoid exchange statement saying that three
pairwise private components cannot each be essential after three
different one-element deletions of the same co-rank-one circuit, or else
that their internal operations synchronize on the common exact gate.

## 7. Adversarial audit: abstract circuit exchange is insufficient

The first alternative in the preceding sentence is false for an abstract
transversal gammoid.  Here is the smallest relevant counterexample.

Let the interface be \(X=\{x_1,x_2,x_3,x_4\}\), and let the five target
labels have neighbourhoods

\[
 \begin{array}{c|ccccc}
 j&1&2&3&4&5\\ \hline
 N(j)&\{x_1\}&\{x_1,x_2\}&\{x_2,x_3\}&
       \{x_3,x_4\}&\{x_4\}.
 \end{array}                                               \tag{7.1}
\]

The full set of five labels is a circuit of rank four.  Indeed, after
omitting any label, the other four have a matching to \(X\); minimality
also follows by restricting such a matching.  Three of the bases are
unique:

\[
\begin{array}{c|cccc}
\text{omitted label}&\multicolumn{4}{c}{\text{forced matching}}\\ \hline
1&2x_1&3x_2&4x_3&5x_4\\
3&1x_1&2x_2&4x_3&5x_4\\
5&1x_1&2x_2&3x_3&4x_4.
\end{array}                                               \tag{7.2}
\]

Subdivide respectively the arcs \(x_1\!\to2\),
\(x_2\!\to2\), and \(x_4\!\to4\) by distinct vertices
\(w_1,w_2,w_3\).  Then \(w_1\) is contained in every linkage after
omitting label 1, \(w_2\) in every linkage after omitting label 3, and
\(w_3\) in every linkage after omitting label 5.  The three blockers are
pairwise private, yet all circuit and basis-exchange axioms hold.

Thus Corollary 6.2 cannot be finished by circuit elimination alone.  A
valid closure must use information absent from (7.1): the undirected
attachments of each blocker to its dead private region and omitted old
bag, or the minor-critical colouring state created by operating inside
that blocker.  This audit prevents the terminal source-tight problem
from being silently replaced by a false matroid lemma.

## 8. First-hit truncation: the exact two-gate support obstruction

There is nevertheless more information in the undirected model than in
the abstract circuit.  The following lemma uses the clique structure of
\(X\), which holds in the \(HC_7\) residue when the old foot
\(a\in P\) (Lemma 4.1 of `hadwiger_source_tight_two_gate_web.md`).

Fix a dead private region \(K_p\), a label escape \(T\) ending in
\(B_b\), and a far Hall certificate omitting \(b\).  For \(x\in X\),
write \(P_x\) for its suffix, including its final edge into the retained
bag.  Define the hit set

\[
              H(T,\mathcal P)=
              \{x\in X: P_x\text{ meets }V(T)-Q\}.       \tag{8.1}
\]

### Theorem 8.1 (gate-supported first-hit truncation)

Assume \(X\) is a clique.  If one of the gates, say \(y_2\), is adjacent
to every vertex of \(H(T,\mathcal P)\), then \(G\) contains a
\(K_{r+1}\)-minor.

#### Proof

Put

\[
 \begin{aligned}
 Z_1&=\{y_1\}\cup C\cup K_p\cup V(T)\cup B_b,\\
 Z_2&=\{y_2\}\cup D\cup(B-K_p),                         \tag{8.2}
 \end{aligned}
\]

using distinct exact components \(C,D\).  As in Theorem 6.1, these are
disjoint connected adjacent rooted sets.

If \(x\notin H(T,\mathcal P)\), keep the full far carrier \(F_x\).
If \(x\in H(T,\mathcal P)\), orient \(P_x\) from \(x\), let \(t_x\)
be its first vertex in \(V(T)-Q\), and replace \(F_x\) by the nonempty
prefix

\[
                         F'_x=xP_xt_x-t_x.               \tag{8.3}
\]

The prefixes in (8.3) are connected, mutually disjoint, disjoint from
(8.2), and adjacent to \(Z_1\) across their last edge.  Every such prefix
is adjacent to \(Z_2\) through the edge \(xy_2\).  A full carrier with
\(x\notin H\) is adjacent to \(Z_1\) through the clique edge from its
retained old bag to \(B_b\), and to \(Z_2\) through its retained
attachment in \(B-K_p\), since \(L(p)=\varnothing\).

Finally, all full and truncated far carriers are pairwise adjacent:
each contains its distinct root in \(X\), and \(X\) is a clique.  Thus
the two sets in (8.2), together with the \(r-2\) full or truncated far
carriers, are \(r\) disjoint pairwise adjacent rooted branch sets.  Add
\(\{v\}\). \(\square\)

### Corollary 8.2 (two-sided transversal law)

In the target-free clique-\(X\) residue, for every label escape \(T\)
to \(B_b\) and every far certificate \(\mathcal P\) omitting \(b\),

\[
        H(T,\mathcal P)\cap M(y_1)\ne\varnothing,
        \qquad
        H(T,\mathcal P)\cap M(y_2)\ne\varnothing,        \tag{8.4}
\]

where \(M(y_i)=\{x\in X:xy_i\notin E(G)\}\).

For \(HC_7\), if \(|H(T,\mathcal P)|=1\), its unique root is
nonadjacent to both gates.  The independence bound
\(\alpha(N(v))\le2\) then forces \(y_1y_2\in E(G)\).  If
\(y_1y_2\notin E(G)\), no root can miss both gates, and (8.4) forces at
least two distinct hit carriers, one witnessing each gate defect.

#### Proof

If the first intersection in (8.4) were empty, every hit root would be
adjacent to \(y_1\); orient Theorem 8.1 with \(y_1\) as the second gate.
The other equality is symmetric.  The final assertions follow directly
from \(\alpha(N(v))\le2\). \(\square\)

This is the exact finite \(X\)-support obstruction.  An essential escape
is not merely used by a far linkage: every corresponding basis linkage
must send through it either a doubly gate-missed root, or at least two
roots whose gate-support sets have empty intersection.  That condition
has no analogue in the abstract example (7.1).

## 9. Dependency and scope audit

The positive results in this note use the following inputs, and no
stronger ones.

1. Theorem 2.1 and Corollary 2.2 use exact portal equality
   \(N(C)=N(D)=Y\cup P\), two distinct components, the co-rank-one far
   certificates, and the clique adjacency of the deficient model bags.
   They do not use gate--\(X\) edges, colouring traces, or planarity.
2. Lemmas 5.2 and 5.4 additionally use the stated lexicographic choice:
   maximum contact, minimum Hall-circuit order, then maximum \(|B|\).
   Without this normalization they give improving model moves, not
   contradictions.
3. Theorem 6.1 is unconditional once a label escape and an avoiding
   omitted-label certificate are supplied.
4. Theorem 8.1 additionally assumes that \(X\) is a clique.  In the
   current \(HC_7\) application this follows from \(a\in P\) and
   \(\alpha(N(v))\le2\); it is not asserted in the general co-rank-one
   cell.
5. Exact star-trace colourings are not identified anywhere with
   minor-operation colourings.

The omitted endpoint labels of distinct essential blockers need **not**
be distinct.  Neither ownership counting nor Corollary 5.3 implies such
distinctness.  Repeated endpoint labels only say that several private
escapes are simultaneous transversals for every basis omitting the same
label; obtaining a contradiction from that repetition still requires a
linkage-capacity or crossed-operation argument.

## 10. One-cut web exchange along an essential escape

The first-hit prefixes can also be divided between the two gates.  This
extracts the ordered obstruction hidden by the phrase “essential
blocker.”

Orient a label escape \(T\) from \(K_p\) toward its last vertex in
\(B_b\), and fix a \(b\)-omitting far certificate.  For every hit root
\(x\), let \(t_x\) be the first vertex of \(T\) met while traversing
\(P_x\) from \(x\).  The vertices \(t_x\) are distinct because the
suffixes are disjoint.

### Theorem 10.1 (ordered two-gate escape split)

Assume \(X\) is a clique and no vertex of \(X\) is nonadjacent to both
gates.  Let \(\{i,j\}=\{1,2\}\).  Suppose there is an edge of \(T\)
whose deletion gives an initial segment \(T_L\) and final segment
\(T_R\) such that

\[
 \begin{aligned}
 &M(y_i)\subseteq H(T,\mathcal P),\\
 &t_x\in V(T_L) &&(x\in M(y_i)),\\
 &t_x\in V(T_R) &&(x\in H(T,\mathcal P)\cap M(y_j)).
 \end{aligned}                                           \tag{10.1}
\]

Then \(G\) contains a \(K_{r+1}\)-minor.

#### Proof

Use \(y_i\) on the initial side and \(y_j\) on the final side, putting

\[
 \begin{aligned}
 Z_L&=\{y_i\}\cup C\cup K_p\cup V(T_L),\\
 Z_R&=\{y_j\}\cup D\cup(B-K_p)\cup V(T_R)\cup B_b.
 \end{aligned}                                           \tag{10.2}
\]

Both sets are connected.  For \(Z_R\), use the edge from \(B_b\) to
\(B-K_p\), which exists because \(L(p)=\varnothing\); the exact component
\(D\) joins all components of \(B-K_p\).  The two sets are disjoint and
adjacent across the cut edge of \(T\).

For every hit root \(x\), replace its far carrier by the prefix ending
immediately before \(t_x\), as in (8.3).  It is adjacent to the side of
(10.2) containing \(t_x\).  If \(t_x\in T_L\), condition (10.1) and the
absence of a doubly missed root give \(xy_j\in E(G)\), so the prefix also
sees \(Z_R\).  If \(t_x\in T_R\), it similarly sees \(Z_L\): a root
missed by \(y_i\) was required to have its hit in \(T_L\).

For an unhit root \(x\), keep its full far carrier.  The first line of
(10.1) gives \(xy_i\in E(G)\), while the retained old bag sees
\(B_b\subseteq Z_R\).  Hence it is adjacent to both sides.  All far
carriers are pairwise adjacent through their clique roots in \(X\).
Together with (10.2) they give \(r\) rooted clique bags; add \(\{v\}\).
\(\square\)

### Corollary 10.2 (exact alternating-order residue)

Suppose \(M(y_1)\cap M(y_2)=\varnothing\).  In a target-free residue,
for every essential escape and corresponding omitted-label certificate,
both of the following orientations fail:

\[
 \begin{array}{ll}
 M(y_1)\subseteq H
   &\text{and every }M(y_1)\text{-hit precedes every }M(y_2)\text{-hit},\\
 M(y_2)\subseteq H
   &\text{and every }M(y_2)\text{-hit precedes every }M(y_1)\text{-hit}.
 \end{array}                                             \tag{10.3}
\]

Thus each certificate has one of two sharply defined defects:

1. it entirely misses a nonneighbour of each possible initial gate; or
2. its first-hit order alternates between the two exclusive gate-support
   classes, so that no single cut of \(T\) separates the classes.

In particular, if each gate has a unique nonneighbour in \(X\), the
cell closes: Corollary 8.2 makes both roots hit \(T\), and whichever of
their first hits occurs first supplies one of the two orientations in
(10.3).

This is an infinite-family closure.  It applies to arbitrary orders and
internal structures of \(B,C,D\) and of the far network.  The remaining
failure is a literal ordered web, rather than an unordered portal-count
defect.

## 11. A doubly missed carrier as the middle bridge

The absence of a doubly missed root in Theorem 10.1 is not necessary
when one such carrier can be kept intact and used between the two outer
segments of the escape.

Let \(x_0\in M(y_1)\cap M(y_2)\) and suppose its suffix \(P_{x_0}\)
meets the label escape \(T\).  Along the orientation of \(T\), let
\(s\) and \(t\) be respectively the first and last vertices of
\(T\cap P_{x_0}\).  They are internal vertices of \(T\), since suffixes
avoid the old model.  Let \(T_-\) be the initial segment ending just
before \(s\), and \(T_+\) the final segment beginning just after \(t\).

### Theorem 11.1 (pivot-carrier escape split)

Assume \(X\) is a clique.  Keep the full far carrier \(F_{x_0}\).  For
each \(x\ne x_0\) whose suffix meets \(T_-\cup T_+\), truncate it just
before its first such meeting.  If the following conditions hold after
possibly interchanging the gates,

1. every carrier truncated at \(T_-\) has its root adjacent to \(y_2\);
2. every carrier truncated at \(T_+\) has its root adjacent to \(y_1\);
3. every untruncated carrier other than \(F_{x_0}\) has its root adjacent
   to \(y_1\),

then \(G\) contains a \(K_{r+1}\)-minor.

#### Proof

Put

\[
 \begin{aligned}
 Z_-&=\{y_1\}\cup C\cup K_p\cup V(T_-),\\
 Z_+&=\{y_2\}\cup D\cup(B-K_p)\cup V(T_+)\cup B_b.
 \end{aligned}                                           \tag{11.1}
\]

These sets are connected and disjoint.  They are adjacent through an
edge from \(y_1\) to \(D\).  The full pivot carrier \(F_{x_0}\) is
disjoint from (11.1): all of its intersections with \(T\) lie between
\(s\) and \(t\), whose non-pivot vertices are simply unused.  It is
adjacent to \(Z_-\) and \(Z_+\) across the two boundary edges of \(T\).

Every other truncated carrier sees the side of (11.1) at which it was
cut and sees the opposite side by condition 1 or 2.  An untruncated
carrier sees \(Z_-\) through its root--\(y_1\) edge and sees \(Z_+\)
through the clique edge from its retained bag to \(B_b\).  All carriers,
including the pivot, are pairwise adjacent through their roots in the
clique \(X\).  Thus (11.1) and the \(r-2\) carriers are \(r\) rooted
clique bags; add \(\{v\}\). \(\square\)

### Corollary 11.2 (both one-defect gate patterns close)

In a fixed-model exact two-component \(HC_7\) representation satisfying
the auxiliary hypotheses of Section 6 and with \(a\in P\), if

\[
                         |M(y_1)|=|M(y_2)|=1,            \tag{11.2}
\]

then \(G\) contains a \(K_7\)-minor.

#### Proof

There is a dead private region by Corollary 2.2, and it has an essential
label escape by Sections 5--6.  If the two unique nonneighbours are
distinct, Corollary 10.2 applies.  If they are the same root \(x_0\),
Corollary 8.2 forces \(P_{x_0}\) to meet the escape.  Every other root is
adjacent to both gates, so all three conditions of Theorem 11.1 hold.
\(\square\)

Thus the terminal exact cell requires at least one gate to miss two or
more vertices of \(X\).  This conclusion uses the full unbounded escape
geometry; it is not a finite-order computation.

## 12. Connectivity budget at a private vital blocker

Let \(W\) be a component of \(G[F]\) which meets a dead region
\(K_p-p\).  In the auxiliary fixed-model regime, assume that \(W\)
has no \(B\)-bypass, and put

\[
 A_p(W)=N_G(W)\cap K_p,
 \qquad
 A_I(W)=N_G(W)\cap\bigcup_{j\in I}B_j.                  \tag{12.1}
\]

### Lemma 12.1 (three noninterface attachments or a small cut)

One has

\[
                         |A_p(W)|+|A_I(W)|\ge3.          \tag{12.2}
\]

More generally, without \((r+1)\)-connectivity, failure of (12.2)
exhibits the cut

\[
                         N_G(W)\subseteq
                         X\cup A_p(W)\cup A_I(W)         \tag{12.3}
\]

of order at most \(r\).

#### Proof

There is no edge from \(W\) to \(U\), since \(U\) is a union of
components of \((G-v-Q)-X\).  There is no edge to \(B-K_p\), since a
path through \(W\) from \(K_p-p\) to such an edge would be a
\(B\)-bypass, forbidden by Lemma 5.2.  A vertex of \(W\) is not a
neighbour of \(v\), by the definition of \(F\).  As \(W\) is a component
of \(G[F]\), these observations give (12.3).

The exact web components and the old model survive outside
\(W\cup N(W)\), so \(N(W)\) is a genuine cut.  Connectivity gives

\[
 r+1\le |N(W)|le |X|+|A_p(W)|+|A_I(W)|
                =(r-2)+|A_p(W)|+|A_I(W)|,
\]

which is (12.2). \(\square\)

### Corollary 12.2 (distributed portal or exact operation adhesion)

For \(HC_7\), every private vital blocker has at least three distinct
attachment vertices outside the four-set \(X\).  Consequently it has at
least one of the following distributed-contact features.

1. It has two distinct attachment vertices in its dead region.
2. It has two distinct attachment vertices in deficient bags (possibly
   in the same bag).

Moreover, if it has exactly three non-\(X\) attachment vertices and is
adjacent to all of \(X\), then
   \[
                         N(W)=X\cup A_p(W)\cup A_I(W)    \tag{12.4}
   \]
is an exact seven-vertex adhesion.

In the equality case, every deletion or contraction internal to \(W\) is a
boundary-faithful operation on one side of (12.4), so its six-colour
state is eligible for the crossed-minor state machinery.  Items 1--2
are precisely the two distributed-contact inputs missing from the static
quotient: two lobe portals or two deficient-label portals.  Lemma 12.1
does not claim that either pair is already linked in the required order.

The omitted endpoint labels of different blockers can still repeat.  If
they do, (12.2) applies separately to their disjoint private components;
no distinct-label conclusion is inferred.
