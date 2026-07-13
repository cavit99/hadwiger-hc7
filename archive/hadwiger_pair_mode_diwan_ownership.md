# Exact ownership of pair modes from planar-cycle extension

## 1. Setting

Let \(G\) be \(r\)-minor-critical and \(k\)-connected.  Let \(S\) be a
\(k\)-cut with

\[
 G-S=D_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}D_q,
 \qquad N(D_i)=S,
\tag{1.1}
\]

where \(q\ge2\).  Suppose \(G[S]\) has an optimal colouring partition

\[
 \Pi=B_1\mid\cdots\mid B_q\mid\{s\},
 \qquad |B_i|=2,
\tag{1.2}
\]

so \(k=|S|=2q+1\).  Optimality makes the block-adjacency quotient of
\(\Pi\) complete.

A shore **owns** \(\Pi\) if it contains disjoint connected carriers for
some two distinct pair blocks.  The general shore-capacity theorem says
that at most one shore owns \(\Pi\): two owners would transfer the exact
state to every target shore and the resulting colourings would glue.

The missing direction is supplied by planar precolouring, provided the
palette has four colours of slack beyond the \(q\) pair blocks.

## 2. Bare four-webs

### Lemma 2.1

Fix two pair blocks

\[
 B_a=\{a_1,a_2\},\qquad B_b=\{b_1,b_2\}.
\]

If a shore \(D\) does not have two-block capacity for these blocks, then
the graph induced by \(D\cup B_a\cup B_b\) is a subgraph of a plane graph
in which

\[
 a_1b_1a_2b_2a_1
\tag{2.1}
\]

is an induced facial four-cycle.  The four cycle edges in (2.1) may be
added and later discarded.

#### Proof

Add four artificial terminals to \(G[D]\), one for each displayed
boundary root, and join each terminal to the complete portal set of its
root.  Two vertex-disjoint paths joining the two \(a\)-terminals and
the two \(b\)-terminals would give the forbidden two carriers.
Complete this auxiliary graph, on the same vertex set, edge-maximally
without creating the two paths.  The rooted Two Paths Theorem gives a
four-web whose frame has the alternating order displayed in (2.1).

No nonempty clique inserted behind a facial triangle can contain an
original shore vertex.  Its neighbours in the auxiliary graph outside
that clique lie among the at most three triangle vertices.  Replace each
artificial terminal among those vertices by its actual boundary root,
and add the \(k-4\) omitted boundary roots.  These at most
\(3+(k-4)=k-1\) actual vertices separate the clique interior from any
other shore in (1.1), contradicting \(k\)-connectivity.  Since frame
terminals are rib vertices, every inserted-clique vertex is an original
shore vertex; hence the web has no nonempty insertion.

Delete every completion edge except the four frame edges, and relabel
each artificial terminal by its boundary root.  The resulting plane
graph is exactly

\[
 H^+=G[D\cup B_a\cup B_b]+E(K_{B_a,B_b}).
\]

The frame remains facial after edge deletion.  It is induced because
each \(B_i\) is independent and its four edges are precisely all edges
between the two pair blocks. \(\square\)

## 3. The at-least-one theorem

We use Diwan's induced-cycle extension theorem: if an induced cycle of
length at most \(2h-5\) is properly precoloured with at most \(h-1\)
colours, then the precolouring extends to an \(h\)-colouring of every
plane supergraph containing that cycle as an induced cycle.  Only the
case of a two-coloured \(C_4\) and \(h\ge5\) is needed.

### Theorem 3.1 (Diwan ownership)

If

\[
                         r\ge q+4,                \tag{3.1}
\]

then at least one shore owns \(\Pi\).

#### Proof

Suppose no shore owns \(\Pi\).  Fix \(B_1,B_2\).  By Lemma 2.1, for
every \(i\) the graph

\[
H_i^+=G[D_i\cup B_1\cup B_2]+E(K_{B_1,B_2})
\]

is plane and has the indicated induced facial frame \(C_4\).

Give the two vertices of \(B_1\) colour \(1\), and the two vertices of
\(B_2\) colour \(2\).  Reserve \(q-1\) further distinct colours, one for
each of \(B_3,\ldots,B_q,\{s\}\), and do not use those reserved colours
in any \(H_i^+\).  The remaining palette has

\[
                         h=r-(q-1)\ge5             \tag{3.2}
\]

colours and includes colours \(1,2\).  Since
\(4\le2h-5\) and the frame uses only two colours, Diwan's theorem
extends its fixed precolouring to an \(h\)-colouring of every \(H_i^+\).

Now give every omitted pair block and the singleton its reserved colour.
All edges from an omitted root into a shore are proper because the shore
uses none of the reserved colours.  All boundary edges are proper because
\(\Pi\) is a proper partition and its blocks have distinct colours.  The
side colourings agree on \(S\), and distinct shores are anticomplete.
They therefore combine to an \(r\)-colouring of \(G\), a contradiction.
\(\square\)

### Corollary 3.2 (exact ownership)

Under (3.1), every pair mode (1.2) has exactly one owner.

#### Proof

Theorem 3.1 gives at least one owner.  The at-most-one capacity theorem
gives at most one. \(\square\)

This is the general coverage mechanism which the three-shore Moser proof
obtains from its special facial-(C_4) three-pattern identity.  It works
for arbitrarily many shores and arbitrary boundary labels; the price is
the four-colour slack in (3.1).

### Theorem 3.3 (arbitrary singleton residue)

More generally, replace the one singleton in (1.2) by (cge0)
singleton blocks, retain (q) pair blocks and (q) full shores, and
assume that the whole boundary partition is optimal.  If

\[
                         r\ge q+c+3,               \tag{3.3}
\]

then the mode has exactly one owner.

#### Proof

The at-most-one proof is unchanged, since singleton blocks need no shore
carrier.  If there were no owner, fix two pair blocks.  Reserve distinct
colours for the other (q-2) pairs and for all (c) singleton blocks.
This reserves (q+c-2) colours and leaves

\[
                         h=r-(q+c-2)\ge5
\]

colours for every bare facial (C_4).  Diwan's theorem and the gluing
argument of Theorem 3.1 apply verbatim. \(\square\)

## 4. Combination with atomic nonowner structure

Combine exact ownership with the label-free results of
`hadwiger_capacity_ownership_descent_general.md`.

* A nonowner shore with no proper exact \(k\)-fragment and more than
  \(q\) vertices is internally \(q\)-connected.
* For pair blocks and \(q\ge6\), such an atomic nonowner is impossible:
  four-connectivity plus Jung's theorem makes it planar, while planar
  connectivity is at most five.
* For \(q\in\{4,5\}\), a large atomic nonowner has a single facial
  transversal of all \(2q\) portal classes, in antipodal matching order.

Consequently, whenever (3.1) holds, the matching modes form an exact
ownership system.  If a separate simultaneous-face argument also proves
that every large atomic shore is nonowner for at most one mode of each
tag, then the ownership-count descent theorem applies.  In that case, if
the number of admissible pair modes satisfies

\[
             (q-1)|\mathcal P|>q|T|,              \tag{4.1}
\]

where \(T\) is the tag set, then some shore is small or exposes a proper
exact \(k\)-fragment.  The additional simultaneous-face premise is
essential for \(q=4,5\): a facial transversal chosen separately for
each mode does not by itself bound the number of nonowner incidences.

For \(q\ge6\), no numerical mode count or face synchronization is
needed.  Every mode has \(q-1\ge5\) nonowner shores, and each nonowner
already satisfies the small-or-exact dichotomy.

Thus, for \(q\ge6\), (3.1) implies the following structural dichotomy for
every pair mode:

\[
 \boxed{\text{every nonowner shore has at most \(q\) vertices, or it
 exposes a nested exact \(k\)-fragment.}}
\tag{4.2}

This is an infinite-family contact-or-adhesion theorem.  It does not yet
resolve arbitrary optimal boundary partitions, the bounded shore in
(4.2), or the atomic planar \(q=4,5\) residues.

## 5. Scope and generalization

The proof uses only:

1. a pair-mode with complete block quotient;
2. as many full shores as pair blocks, so two owners can distribute the
   remaining blocks one per shore;
3. connectivity equal to the boundary order, which removes inserted web
   parts; and
4. the induced-cycle extension theorem.

It does not use the Moser graph, a prescribed cyclic labelling, or a
finite quotient atlas.  More generally, the same argument works whenever
all blocks except two selected pairs can be assigned distinct reserved
colours and the unreserved palette has at least five colours.
