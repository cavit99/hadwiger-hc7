# The singleton rooted core has a dark multiply-hit bag

## 1. Setting

Retain the full-singleton boundary and the rooted \(K_4\)-model

\[
                         K_1,K_2,K_3,K_4                 \tag{1.1}
\]

from Section 6 of `hadwiger_singleton_transition_atlas.md`.  Thus the
bags lie in

\[
                         J_0=G-\{d,b,a,c,1,2\},          \tag{1.2}
\]

are pairwise adjacent, and each contains a neighbour of \(b\) in the
owner shore.  Put

\[
                         A=\{a,c\},\qquad C=\{1,2\}.     \tag{1.3}
\]

The graph \(J_0\) is connected, since deleting six vertices from a
seven-connected graph leaves a connected graph.

### Lemma 1.1 (spanning extension)

The rooted model (1.1) may be chosen so that its four bags partition
\(V(J_0)\).

#### Proof

Start with the rooted model supplied by Strong HC4.  Every component of
the complement of its bag union has an edge to at least one bag, because
\(J_0\) is connected.  Assign the whole component to any such bag.  The
enlarged bag remains connected, all old model adjacencies and roots remain,
and distinct assigned components are disjoint.  Repeating for all
components gives the spanning model. \(\square\)

## 2. A Hall-type allocation or a dark bag

### Theorem 2.1 (two-group allocation)

If every bag in (1.1) which contains neither \(h\) nor \(r\) has a
neighbour in each of \(A\) and \(C\), then \(G\) contains a
\(K_7\)-minor.

Consequently, in a \(K_7\)-minor-free graph some bag \(K_0\) contains
neither \(h\) nor \(r\) and is anticomplete to one of \(A,C\).

#### Proof

Use the completion partition

\[
                         A\mid(\{d\}\cup C).              \tag{2.1}
\]

Both parts are connected: \(ac\) and \(d1,d2\) are edges.  A bag
containing \(h\) sees \(A\) through \(ha\) and sees
\(\{d\}\cup C\) through \(hd,h1,h2\).  A bag containing \(r\) uses
\(rc\) and \(rd,r1,r2\).  Every remaining bag sees both sides by the
hypothesis.  Lemma 6.1 of the transition atlas, using the four bags,
\(\{b\}\), and the two parts in (2.1), is therefore a \(K_7\)-model.

At most two disjoint bags contain \(h\) or \(r\), so at least two bags
avoid both.  The contrapositive gives the last assertion. \(\square\)

This is the exact Hall obstruction for the two nonsingleton completion
parts.  It does not enumerate the six partitions.

## 3. Seven-connectivity forces a doubled model portal

### Theorem 3.1 (dark bag is multiply hit)

Let \(K_0\) be the dark bag from Theorem 2.1.  Then some other model bag
\(K_j\) has at least two distinct vertices adjacent to \(K_0\):

\[
                         |N_{K_j}(K_0)|\ge2.               \tag{3.1}
\]

More precisely, if \(K_0\) is anticomplete to \(A\), then

\[
 N_G(K_0)\subseteq \{b,1,2\}\cup
                  \bigcup_{i\ne0}K_i,                     \tag{3.2}
\]

and the symmetric containment with \(\{b,a,c\}\) holds when \(K_0\)
is anticomplete to \(C\).

#### Proof

Because the model is spanning in \(J_0\), every neighbour of \(K_0\)
inside \(J_0\) belongs to one of the other three bags.  The only neighbour
of \(d\) in \(J_0\) which can lie in \(K_0\) is \(h\) or \(r\); neither
does.  Thus \(d\) has no edge to \(K_0\).  Every bag has a \(b\)-portal,
while darkness to \(A\) excludes \(a,c\).  This proves (3.2); the other
case is symmetric.

The set \(N_G(K_0)\) separates the nonempty bag \(K_0\) from, for
example, either excluded boundary vertex.  Seven-connectivity gives
\(|N_G(K_0)|\ge7\).  The three singleton classes in (3.2) contribute at
most three vertices.  If every one of the other three bags contributed at
most one neighbour, the right side would have order at most six.  Hence
one other bag contributes at least two distinct neighbours, proving
(3.1). \(\square\)

### Corollary 3.2 (exact peel seed)

Every \(K_7\)-free full-singleton lock has a pair of adjacent rooted bags
\((K_0,K_j)\) with the following port-labelled profile:

1. \(K_0\) contains a \(b\)-root but neither \(h\) nor \(r\);
2. \(K_0\) misses one whole completion pair \(A\) or \(C\); and
3. \(K_j\) has two distinct portals into \(K_0\).

Thus failure of the rooted-core completion is not a diffuse four-bag
obstruction.  It produces exactly the multiply-hit adjacent bag needed by
a labelled splitter theorem.

There is a version which guarantees that the multiply-hit donor sees the
missing group, at the price of consolidating all bags with the same
defect.

### Theorem 3.3 (dark-cluster/light-donor theorem)

Fix \(T\in\{A,C\}\), let \(\mathcal D_T\) be the nonempty family of
model bags anticomplete to \(T\), and put

\[
                         U_T=\bigcup_{K_i\in\mathcal D_T}K_i.  \tag{3.3}
\]

Then \(U_T\) is connected, and some \(T\)-light bag
\(K_j\notin\mathcal D_T\) contains at least two distinct neighbours of
\(U_T\).

#### Proof

The bags in \(\mathcal D_T\) are pairwise adjacent, so their union is
connected.  No such bag contains \(h\) or \(r\), since either vertex sees
both groups.  If \(T=A\), then

\[
 N_G(U_T)\subseteq \{b,1,2\}\cup
       \bigcup_{K_j\notin\mathcal D_T}K_j,          \tag{3.4}
\]

and for \(T=C\) use \(\{b,a,c\}\).  The excluded group leaves a vertex
outside the open neighbourhood, so seven-connectivity gives
\(|N_G(U_T)|\ge7\).  The three singleton vertices contribute at most
three.  There are at most three light bags.  If each contributed at most
one neighbour, the total would be at most six.  Hence some light bag
contributes at least two. \(\square\)

Thus the doubled interface can always be chosen with the missing group on
the donor side.  Its two edges may hit different dark bags; this is the
only distinction between Theorem 3.3 and the single-bag seed of
Theorem 3.1.

## 4. The sufficient one-bag peel

The precise surgery target can now be stated without ambiguity.  Suppose,
say, \(K_0\) is anticomplete to \(A\), and let \(K_j\) be multiply hit.
If \(K_j=X\dot\cup Y\) is a connected bipartition such that

* \(X\) has a neighbour in \(A\) and an edge to \(K_0\);
* \(Y\) retains the prescribed \(b\)-root, an edge to \(K_0\), and an
  edge to each of the other two rooted bags; and
* every other bag avoiding \(h,r\), including \(K_0\cup X\), meets both
  \(A\) and \(C\),

then replace

\[
                         K_0\longmapsto K_0\cup X,
                         \qquad K_j\longmapsto Y.          \tag{4.1}
\]

The four sets remain a rooted \(K_4\)-model and Theorem 2.1 gives a
\(K_7\)-minor.  The two distinct portals in Theorem 3.1 provide a robust
transfer.  For a component-lobe transfer below, even one old
\(K_0\)-edge is enough: the lobe's attachment back to the protected core
becomes a new \(K_0Y\)-edge after transfer.

The unresolved step is now sharp: prove this labelled peel, or show that
its failure exposes at most six actual portal vertices.  Merely knowing
that \(K_j\) is connected is insufficient, because all of its
\(A\)-contacts and its three model adjacencies may lie behind one internal
bottleneck.

## 5. Off-core lobes can be peeled rigorously

The following removes all inessential bridge geometry from the multiply
hit bag.  Continue with \(K_0\) dark to \(A\), and suppose \(K_j\) has an
\(A\)-portal.  Select in \(K_j\):

* one prescribed \(b\)-root;
* one portal to each of the two model bags other than \(K_0,K_j\);
* one retained portal to \(K_0\); and
* the vertices \(h,r\), if either belongs to \(K_j\); and
* one portal for each of \(A,C\) seen by \(K_j\), unless a selected
  \(h\)- or \(r\)-vertex already supplies that contact.

There are at most six selected vertices.  Indeed, without \(h,r\) there
are four model/root terminals and at most two group terminals; with one
of \(h,r\), that vertex itself sees both groups; and with both there are
six model/root terminals already.  Let \(W\subseteq K_j\) be a
vertex-minimal connected subgraph containing them.

### Lemma 5.1 (mixed off-core lobe peel)

If a component \(L\) of \(K_j-W\) contains an \(A\)-portal and has an
edge to \(K_0\), then the replacement

\[
                         K_0'=K_0\cup L,
                         \qquad K_j'=K_j-L             \tag{5.1}
\]

is a spanning rooted \(K_4\)-model in which \(K_0'\) now sees \(A\).

#### Proof

The set \(K_0'\) is connected through the assumed edge.  The set
\(K_j'\) is connected: it contains the connected core \(W\), and every
other component of \(K_j-W\) has a neighbour in \(W\).  (A component
with none would be a component of \(K_j\).)

All protected model adjacencies of \(K_j'\) remain.  Its chosen
\(b\)-root and its portals to the other two bags lie in \(W\); so do
\(h,r\) when relevant.  Its adjacency to \(K_0'\) remains through the
selected \(K_0\)-portal in \(W\).  The enlarged \(K_0'\) retains all old
adjacencies of \(K_0\), retains its own \(b\)-root, and gains an
\(A\)-contact from \(L\).  The four bags remain connected, disjoint,
pairwise adjacent, rooted, and spanning. \(\square\)

### Corollary 5.2 (protected-core lock)

After repeatedly applying Lemma 5.1, every surviving \(A\)-portal--
\(K_0\)-portal connection in \(K_j\) is carried by the protected Steiner
core \(W\), or the two portal types occur in different components of
\(K_j-W\).  Thus arbitrary off-core bridge webs do not survive: the
unresolved obstruction is an order constraint inside a connected core
spanning at most six prescribed terminal vertices.

The number of terminal **classes** is at most six, but \(|W|\) need not be
at most six.  Treating \(W\) itself as a six-vertex separator would be an
invalid contraction of paths.  A complete proof still needs either a
label-preserving splitter inside this Steiner core or an edge-critical
detour which changes its terminal order.

## 6. Potential maximality makes every mixed lobe an owner

Among all spanning rooted models (1.1), maximize

\[
 \Phi(\mathcal K)=
 \sum_{i=1}^4\bigl(
   \mathbf 1[K_i\sim A]+\mathbf 1[K_i\sim C]
 \bigr).                                             \tag{6.1}
\]

The roots are still the four prescribed \(b\)-neighbours; only the
allocation of the remaining vertices of \(J_0\) changes.

### Lemma 6.1 (no mixed off-core lobe at maximum potential)

Let \(K_0\) miss a group \(T\in\{A,C\}\), let \(K_j\) see \(T\), and
choose the protected core \(W\subseteq K_j\) as in Section 5.  If a
component \(L\) of \(K_j-W\) sees \(T\), then it has no edge to
\(K_0\).

#### Proof

The protected core contains a retained portal for every group seen by
\(K_j\).  If \(L\) also saw \(K_0\), Lemma 5.1 would transfer
\(L\) to \(K_0\).  The recipient
would gain the previously missing \(T\)-incidence, while the donor
retained all of its group incidences through \(W\).  This strictly
increases (6.1), contrary to its maximality. \(\square\)

### Corollary 6.2 (all mixed routing is core-locked)

The core \(W\) already contains one \(T\)-portal.  Hence no component of
\(K_j-W\) containing any further \(T\)-portal can also see \(K_0\).

Thus a potential-maximal obstruction has one of two exact forms:

1. the donor has a unique essential \(T\)-portal, lying in \(W\); or
2. every off-core \(T\)-portal lies in a lobe with no \(K_0\)-edge, so
   all \(T\)-to-\(K_0\) routes return through the protected Steiner core.

This is an operation-level lock, not an arbitrary bridge web.  It does
**not**, however, specify a structurally critical edge.  The unique
\(T\)-portal and the retained \(K_0\)-portal may coincide, a shortest
route between them may be the old boundary edge \(hr\), and an edge of a
chosen Steiner tree need not be a bridge of the induced donor bag.

The strongest valid edge transition is conditional.  If a genuine donor
bridge \(xy\) separates an off-core \(T\)-piece from all protected donor
terminals, and an \(x\)-\(y\) detour in \(G-xy\) has interior entirely in
\(K_0\), then transferring that piece and the detour to \(K_0\) strictly
raises \(\Phi\).  Hence no such **bag-aligned** detour exists at maximum
potential.  Generic Kempe detours need not be bag-aligned: their failures
charge whole branch bags, not boundedly many vertices.

The remaining separator claim therefore cannot be obtained merely by
counting the six protected terminal classes; the Steiner paths between
them may be arbitrarily long.  What has been proved is the necessary
precursor to a valid cut argument--all inessential mixed lobes have been
removed.  The exact missing input is a bag-aligned detour-or-explicit
six-vertex-separator theorem (with a separate treatment when the two
essential portals coincide).

## 7. Independent-audit correction

Theorems 3.3, 5.1 and 6.1 above survive independent audit.  The final
phrase “localized at one actual edge” requires a qualification.  The
unique group portal and retained \(K_0\)-portal may be the same vertex,
so their minimal route can have length zero.  Even for distinct portals,
a first shortest-path edge need not be a bridge of the donor (a triangular
core is the smallest example), and a route consisting only of \(hr\) has
no subsequent boundary--shore edge.  Thus an edge is not yet guaranteed
which both preserves the fixed boundary atlas and separates the owner
terminal order.

Every edge which does exist is chromatically critical in the
minor-minimal host, but its five Kempe detours need not be aligned with the
four fixed rooted bags.  The strongest valid positive transition is the
bag-aligned bridge lemma in
`hadwiger_rooted_core_dark_bag_split_audit.md`: a genuine donor bridge
whose protected side retains all donor incidences, together with a detour
whose interior lies in \(K_0\), raises \(\Phi\).  Failure of arbitrary
detours currently charges whole branch bags, not at most six actual
vertices.  Hence the detour-or-six-cut conclusion remains unproved.
