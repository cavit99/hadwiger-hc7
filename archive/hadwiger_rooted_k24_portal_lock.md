# The contact-maximal split lock as a rooted \(K_{2,q}\) obstruction

## 1. Exact reformulation

Let \(B_0,B_1,\ldots,B_q\) be pairwise disjoint branch sets such that
\(B_1,\ldots,B_q\) are pairwise adjacent and \(B_0\) is adjacent to each
of them.  Let \(a,z\in B_0\) be distinct roots.  Contract every \(B_i\),
\(1\le i\le q\), to a vertex \(x_i\), and retain all vertices of
\(B_0\).  Denote the resulting graph by \(H\).  Thus
\(X=\{x_1,\ldots,x_q\}\) induces a clique in \(H\).

Call a \(K_{2,q}\)-model in \(H\) **doubly rooted** if its two branch
sets on the side of order two contain \(a\) and \(z\), respectively,
and its \(q\) branch sets on the other side contain
\(x_1,\ldots,x_q\), respectively.

### Lemma 1.1

If \(H\) has a doubly rooted \(K_{2,q}\)-model, then that model lifts to
the original graph with the \(q\) large-side carriers pairwise adjacent.
If its two small-side carriers are also adjacent, the lifted carriers
form a \(K_{q+2}\)-model, two of whose bags contain \(a,z\), respectively.

#### Proof

Lift the model through the contractions.  The two small-side branch sets
are adjacent to every large-side branch set by the \(K_{2,q}\) model.
The large-side branch sets are pairwise adjacent because they contain
the original clique bags \(B_i\).  Hence the only possible missing edge
among the \(q+2\) lifted carriers is the edge between the two small-side
carriers.  If it is present, they are the required clique model.
\(\square\)

The last qualification is important.  The exact target is therefore
the graph \(K_{2,q}+e\), where \(e\) joins the two vertices on the side
of order two.  Equivalently, one asks for a doubly rooted
\(K_{2,q}\)-model whose two small-side carriers are adjacent.  A
connected bipartition of \(B_0\) meeting every portal class gives such
a model, but the rooted-minor formulation also permits useful
reroutings through the terminal carriers.

For \(HC_7\), \(q=4\).  After dropping one uncontacted bag from the
contact-maximal \(K_6\)-model, the exact obstruction to this particular
one-bag augmentation is consequently a six-terminal rooted
\(K_{2,4}+e\) obstruction with the four vertices on the large side
already forming a clique.  Other multi-bag reroutings may still produce
the required \(K_6\)-model, so this must not be called an exact
characterization of all contact improvements.  It is the label-free
content of the former ``\(2\)-by-\(4\)'' portal lock.

## 2. Separation of the two difficulties

There are two logically distinct questions.

1. **Four-terminal packing.**  Does \(H\) contain a \(K_{2,4}\)-model
   rooted at \(x_1,x_2,x_3,x_4\) on the large side?
2. **Root capture.**  Can the two free carriers be chosen adjacent and
   made to contain \(a,z\) separately?

The established four-terminal rooted-\(K_{2,4}\) theory addresses the
first question.  It does not by itself answer the second.  In
particular, replacing the four branch bags by arbitrary terminal
vertices and invoking a four-terminal theorem would lose precisely the
root-placement information needed for contact augmentation.

### Lemma 2.1 (linkage upgrade)

Suppose an \(X\)-rooted \(K_{2,4}\)-model has free carriers \(C_1,C_2\).
If \(H-X\) contains two vertex-disjoint paths from \(\{a,z\}\) to
\(C_1,C_2\), with distinct ends and with interiors disjoint from the
model, then the model can be enlarged so that its free carriers contain
\(a,z\) separately.  If, in addition, the enlarged carriers are
adjacent, it is a rooted \(K_{2,4}+e\)-model and closes the portal lock.

#### Proof

Choose the pairing supplied by the two paths and absorb each path into
the carrier at its terminal end.  Disjointness preserves all branch
sets and all prescribed adjacencies. \(\square\)

Thus a failed lock has one of two structural causes:

* the four terminals admit no rooted \(K_{2,4}\); or
* every such model is separated from the root pair, or has its two free
  carriers nonadjacent after every root-capturing rerouting.

The second cause is a two-linkage obstruction.  This is the point at
which the Two Paths/web alternative and the contraction-critical state
exchange can enter without conflating terminal packing with root
capture.

## 3. The available planar theorem and its proper scope

Demasi--Mohar's four-terminal theorem characterizes planar graphs with
no rooted \(K_{2,4}\) whose four prescribed terminals lie on the large
side.  Its low-connectivity reductions propagate the obstruction
through one- and two-separations; in the three-connected case the
residual consists of finitely described planar structures.  This is an
exact match for the **first** question above once a web/planar outcome
has already been obtained.

It is not legitimate to apply that planar theorem directly to the
original contact model: neither planarity of \(H\) nor capture of the
two roots is automatic.  The usable dichotomy must have the form

\[
 \text{rooted }(K_{2,4}+e)
 \quad\text{or}\quad
 \text{a root-separating web/2-apex structure}.
\]

The first outcome gives the improved \(N(v)\)-meeting \(K_6\)-model.
In the second outcome, the proof must retain the contraction-critical
boundary state.  If the web can be embedded after deleting two fixed
vertices, the Four Color Theorem plus two fresh colours gives the
required six-colouring; if a web pocket is separated through at most
six vertices, seven-connectivity excludes it.  This is the precise
closure mechanism suggested by the \(C_6\) laboratory.

## 4. Uniform target

For arbitrary \(m=t-1\), the contact-maximal Hall promotion produces a
multiply rooted bag and asks for the corresponding rooted
\(K_{2,m-2}+e\).  A scalable theorem would therefore be:

> **Rooted biclique contact-or-separator target.**  In a
> contraction-critical host, a clique of \(q\) terminal branch bags and
> a connected two-root carrier either contain a label-preserving rooted
> \(K_{2,q}+e\), or failure exposes a genuine adhesion on which the two
> minor colourings admit the same equality partition.

This statement no longer mentions the Moser spindle, \(C_6\), or a
particular portal order.  For \(q=4\), planar rooted-\(K_{2,4}\) and Two
Paths structure are plausible tools for proving it.  For general \(q\),
the Hall-deficit circuit and knitted-adhesion machinery must replace
finite rooted-minor classification.

## 5. Status

The reformulation and linkage upgrade are proved here.  The rooted
biclique contact-or-separator target is not proved.  Its value is that it
identifies the reusable theorem which the local portal cases were
approximating, while keeping separate the two places where a false
application of rooted-minor theory could occur: terminal-bag
normalization and capture of the repeated roots.

The exact probe `portal_split_helly_probe.py` also rules out two possible
shortcuts.  There are four-connected nonplanar carriers with four portal
classes of multiplicity at least two and no strict rooted split.  More
strongly, on the complement of a seven-cycle there is a choice of two
roots and four portal classes for which:

* no connected root-separating bipartition splits all four classes;
* the four classes have no two-vertex transversal; and
* after adjoining a terminal \(K_4\), there is no \(K_6\)-model rooted at
  the two roots and four terminals.

Thus neither internal four-connectivity nor a two-portal-core dichotomy
proves the target.  The counterarchitecture does not satisfy the full
ambient contraction-critical hypotheses; it confirms that the missing
ingredient must be the one-step colouring exchange or an equivalent
ambient rerouting theorem.
