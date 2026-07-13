# The bridge--torso exchange at a double-root `P4` gate

## 1. The correct static object

Let `H` contain a rooted `K_m`-model

\[
                    (B_1,\ldots,B_m),\qquad u_i\in B_i,
\]

and two disjoint connected sets `A,D` outside its union.  Fix
`x` such that `A` is adjacent to `u_x` and `D` is anticomplete to
`B_x`.  Put

\[
 I_A=\{i:E(A,B_i)\ne\varnothing\},\qquad
 M=[m]-I_A.
\]

Assume that `M` is nonempty and choose `y in M` for which `D` is
adjacent to `B_y`.  (At the double-root gate one may take
`x in I_A-I_D` and `y in I_D-I_A`.)

For a bipartition into two **nonempty connected** sets

\[
                       B_x=X\mathbin{\dot\cup}Y,
                       \qquad u_x\in Y,                 \tag{1.1}
\]

with `X,Y` adjacent, call `X` an **A-arm** if

\[
 E(A,X)\ne\varnothing,qquad
 E(X,B_j)\ne\varnothing\quad(j\in M).                  \tag{1.2}
\]

Its monopoly set is

\[
 \Lambda(X)=\{j\ne x:E(Y,B_j)=\varnothing\}.           \tag{1.3}
\]

Thus `j in Lambda(X)` precisely when every old `B_x`--`B_j`
contact has its `B_x` endpoint in the detachable arm.

The next theorem is the useful exchange principle.  It is label-free;
the Moser spindle and the number seven play no role.

## 2. Arm, rotation, or a multi-label warehouse

### Theorem 2.1 (rooted arm exchange)

In the setup above, let `X` be an A-arm and put `Y=B_x-X`.

1. If `Lambda(X)=emptyset`, then the following `m+1` sets form a
   clique model:

   \[
      A\cup X,\quad D\cup B_y,\quad Y,
      \quad B_j\quad(j\notin\{x,y\}).                   \tag{2.1}
   \]

2. If `Lambda(X)={j}`, then replacing

   \[
       B_x\longmapsto Y,qquad
       B_j\longmapsto B_j\cup X                         \tag{2.2}
   \]

   and leaving the other bags fixed gives another rooted `K_m`-model
   on exactly the same union.  It retains the root `u_x` in the now
   smaller `x`-bag.  Moreover, either `j in M` and the new model has
   strictly larger `A`-contact set, or `j notin M` and its
   `A`-contact set is unchanged.

Choose among all rooted `K_m`-models on the same union which have `D`
anticomplete to the `x`-bag first one maximizing `|I_A|`, and subject
to that one minimizing `|B_x|`; recompute `I_A`, `M`, A-arms, and
monopoly sets in each candidate model.  The domain is invariant under the
rotation in item 2: the union, roots, and `D`-defect at `x` are
unchanged.  Unless `A,B_1,...,B_m` itself is already a clique model,
every A-arm in the selected model satisfies

\[
                         |\Lambda(X)|\ge2.               \tag{2.3}
\]

#### Proof

Suppose first that `Lambda(X)` is empty.  The first two sets in (2.1)
are connected by (1.2) and the choice of `y`.  They are adjacent via
an `X`--`B_y` edge.  The first set sees `Y` through the `X`--`Y`
edge.  It sees every remaining `B_j` through `A` when `j in I_A`
and through `X` when `j in M`.  The set `D union B_y` sees `Y` and
every remaining old bag through the old clique-model edges incident
with `B_y`.  Finally, `Y` sees every remaining old bag because its
monopoly set is empty.  All other pairs are old model pairs.  This
proves item 1.

Now suppose `Lambda(X)={j}`.  The set `B_j union X` is connected,
since the old `B_x`--`B_j` contact has an endpoint in `X`.  It is
adjacent to `Y` through the `X`--`Y` edge and to every other old bag
through `B_j`.  By the definition of the monopoly set, `Y` is
adjacent to every old bag other than `B_j`; all other model
adjacencies are unchanged.  The new bags in (2.2) are therefore a
rooted `K_m`-model, with `u_x in Y` and `u_j in B_j`.

The edge `A u_x` keeps `x` in the new `A`-contact set.  No old
`A`-contact is lost.  If `j in M`, the edge between `A` and `X`, now
inside the new `j`-bag, adds `j`; if `j notin M`, the contact set is
unchanged.  Thus a singleton monopoly contradicts the stated
lexicographic choice: it either improves the first coordinate or keeps
that coordinate and strictly shrinks `B_x`.

It remains to justify the empty-monopoly case at the selected model,
where the originally chosen label `y` need not remain outside the
new `A`-contact set.  Unless the displayed `A`-extension is already a
clique model, `M` is nonempty.  Choose any `h in M`.  Since `X` is an
A-arm, `X` is adjacent to `B_h`; since its monopoly is empty, `Y` is
also adjacent to `B_h` and to every other old bag.  The replacement

\[
             B_x\longmapsto Y,\qquad B_h\longmapsto B_h\cup X
\]

is therefore a rooted `K_m`-model in the same optimization domain and
strictly adds `h` to the `A`-contact set, a contradiction.  This proves
(2.3) without requiring the initially selected `y` to remain
admissible throughout the optimization.  QED.

At `m=5`, if `A,D` contain the repeated apex neighbours `a,b` and the
old roots `u_i` are the other five apex neighbours, every set in (2.1)
meets `N(v)`.  Thus (2.1) is an `N(v)`-meeting `K_6`-model and gives a
`K_7` minor after adjoining `{v}`.  The theorem isolates the only legitimate
static obstruction among the arms under discussion: an A-arm must be a warehouse for at least
two old model labels.  Mere portal multiplicity is not that obstruction.

### Corollary 2.2 (only root-defect labels can lock an arm)

Let

\[
       \Delta_x=\{j\ne x:u_xu_j\notin E(H)\}.            \tag{2.4}
\]

Then every A-arm satisfies

\[
                         \Lambda(X)\subseteq\Delta_x.    \tag{2.5}
\]

In a lexicographically optimal surviving model, **if an A-arm exists**, it
follows that `|Delta_x|>=2`; every A-arm warehouses at least two of these
root-defect labels.  Without the existence qualification the first
conclusion is false (for example, the `x`-bag may be a singleton).

#### Proof

If `u_xu_j` is an edge, then `u_x in Y` itself is a `Y`--`B_j`
contact.  Hence `j` cannot belong to `Lambda(X)`.  Combine this with
Theorem 2.1.  QED.

This is particularly restrictive for the five unique roots of the
degree-seven trace.  Their missing-root graph is triangle-free and has
at most six edges.  In the pure `C_5` row, `|Delta_x|=2`; every
**A-arm** must therefore contain **all** `B_x`-endpoints of both
deficient old-bag adjacencies.

## 3. The block bridge--torso

Root the block--cutvertex tree of `H[B_x]` at the cutvertex node `u_x`
when `u_x` is a cutvertex, and otherwise at the unique block node
containing `u_x`.  If `q` is a cutvertex and `K` is a component of
`B_x-q` not containing `u_x`, call `K` a rooted block lobe.  Then
`K` and `B_x-K` are connected and adjacent.  Call the lobe
**demand-complete** if it is adjacent to `A` and to every `B_j`,
`j in M`.

### Theorem 3.1 (bounded warehouse branches)

Use a lexicographically optimal model surviving the obvious
`A,B_1,...,B_m` extension, as in Theorem 2.1.
Every demand-complete rooted block lobe `K` satisfies

\[
 |\Lambda(K)|\ge2,qquad \Lambda(K)\subseteq\Delta_x.    \tag{3.1}
\]

The inclusion-minimal demand-complete lobes are pairwise disjoint, and
their monopoly sets are pairwise disjoint.  Consequently their number
is at most

\[
                         \left\lfloor{|\Delta_x|\over2}\right\rfloor.
                                                               \tag{3.2}
\]

Every demand-complete lobe contains one of these minimal lobes.  Thus:

* if `|Delta_x|<=1`, no demand-complete non-root block lobe exists;
* if `|Delta_x|` is two or three, all co-located arm demands funnel
  through one nested warehouse branch;
* even at `|Delta_x|=4`, there are at most two incomparable warehouse
  branches.

#### Proof

A demand-complete lobe is an A-arm, so (3.1) is Theorem 2.1 and
Corollary 2.2.  Rooted lobes form a laminar family, as is immediate
from their descendant-subtree description in the rooted
block--cutvertex tree.  Demand-completeness is upward-closed among
nested lobes: a larger lobe retains every edge witnessed by a contained
lobe.  Two inclusion-minimal demand-complete lobes therefore cannot be
properly nested and hence are disjoint.

If disjoint lobes `K,L` had a common monopoly label `j`, the nonempty
set of all `B_x`-endpoints of `B_x`--`B_j` edges would be contained
in both `K` and `L`, which is impossible.  Their monopoly sets are
therefore disjoint.  Each has order at least two and all lie in
`Delta_x`, proving (3.2).  Finite descent in the rooted block tree
shows that every demand-complete lobe contains an inclusion-minimal
one.  QED.

Theorem 3.1 is the promised **block-level** bridge--torso reduction.
In the `m=5` application, outside at most two charged warehouse branches,
the obstruction cannot live in a hanging block and is concentrated in
the root block torso.  For general `m`, the proved bound is (3.2), not
the constant two.
An analogous statement for 2-separations would reduce that torso to an
SPQR/web core, but that extension is not proved here.  In the pure
five-cycle cell the proved block statement leaves only one possible
warehouse branch, not an unbounded collection of hanging-block cases.

## 4. Seven-connectivity charges every warehouse geometrically

The next count specializes to `m=5`.  Assume explicitly that the seven
pairwise disjoint pieces `A,D,B_1,...,B_5` form a spanning partition of
`H=G-v`; no assertion is made here that an arbitrary initial model can
always be enlarged while preserving the displayed defects.  Assume also
that `G` is seven-connected, the
only vertex of `N_G(v)` in `B_x` is `u_x`, and `D` is anticomplete to
`B_x`.

### Lemma 4.1 (six external units at a non-root lobe)

For every rooted block lobe `K` of `B_x`, with attachment cutvertex
`q`,

\[
 \sum_{Z\in\{A,B_j:j\ne x\}} |N_G(K)\cap Z|\ge6.        \tag{4.1}
\]

In particular, at least one of the five displayed external pieces
contains two distinct neighbours of `K`.

#### Proof

The lobe does not contain `u_x`; since `u_x` is the only neighbour of
`v` in `B_x`, the vertex `v` is anticomplete to `K`.  The lobe
`K` is also anticomplete to `D` by the assumed `B_x`--`D` defect.  Since the seven
pieces span `H`,

\[
 N_G(K)\subseteq\{q\}\cup A\cup\bigcup_{j\ne x}B_j.
\]

The set `N_G(K)` separates the nonempty set `K` from `v` in the
seven-connected graph `G`, so it has order at least seven.  Removing
the single possible neighbour `q` inside `B_x` gives (4.1).  There are
only five external pieces, so one is multiply hit.  QED.

Combining Theorems 3.1 and 4.1 gives a concrete strict-surplus residue:
each surviving demand-complete rooted block lobe lies above one of at most
`floor(|Delta_x|/2)` warehouse branches, warehouses at least two root
defects, and exports at least six actual portal vertices with a repeated
external owner.  This is substantially narrower than an unspecified
"multiply hit bag".  What is still missing is a dynamic exchange which
uses the repeated external owner to open that warehouse, or else turns
its one-step minor transition into a colour-gluable adhesion.

## 5. Why a static portal-surplus splitter is false

Even seven-connectivity, the exact sharp `P4` contact pattern, and two
portals in the private bag do not force the arm of Lemma 2.4.  Here is
an explicit counterexample to that overbroad statement.

Let `C_2,C_3,C_4,C_5` be disjoint two-vertex sets whose union `C`
induces `K_8`.  Let `B_1={u,p,q}` induce the path `p-u-q`, and put
`B_i=C_i` for `i=2,3,4,5`.  Join `q` to all of `C`, and join each of
`u,p` to `C_3 union C_4 union C_5`.  Let `A,D` be disjoint triangles,
anticomplete to one another.  Join every vertex of `A` to `p` and to
`C_3 union C_4 union C_5`, and add one edge from a distinguished
`a in A` to `u`.  Join every vertex of `D` to all of `C`.
Choose roots `u_i in C_i` for `i=2,3,4,5` and a distinguished
`b in D`.  Finally add a vertex `v` adjacent precisely to

\[
                         a,b,u,u_2,u_3,u_4,u_5,
\]

and call the graph before adding `v` by `H` and the augmented graph by
`G`.

Then:

* the five displayed bags are a rooted `K_5`-model (root `B_1` at
  `u`);
* `A` contacts exactly bags `1,3,4,5`, while `D` contacts exactly
  bags `2,3,4,5`;
* the root in `B_2` is adjacent to the distinguished `b in D`, so
  the double-root root-cover condition is present;
* `H` is seven-connected.  Indeed, if at most six vertices are
  deleted and some vertex of `C_3 union C_4 union C_5` remains, that
  vertex joins every remaining displayed part.  If all six of those
  vertices are deleted, no other vertex was deleted and
  `A-p-u-q-C_2-D` remains connected.  Conversely deleting
  `(C_3 union C_4 union C_5) union {u}` separates `A union {p}`, so
  the connectivity is exactly seven;
* `G` is also seven-connected: after fewer than seven deletions, either
  `v` was deleted and the remaining subgraph of `H` is connected, or
  `v` retains a neighbour in the connected remaining subgraph of `H`.
  Its degree is seven, so the connectivity is exactly seven;
* nevertheless Lemma 2.4's arm does not exist for `x=1,y=2`.
  Such an arm must contain `p` to meet `A` and `q` to meet `B_2`.
  The unique `p`--`q` path in `B_1` contains the root `u`, which is
  required to lie in the other half.

Thus static connectivity and portal counts cannot finish the `P4`
gate by themselves.  This example contains the clique `C=K_8`, so it
is not `K_7`-minor-free and does not refute a splitter that genuinely
uses minor-freeness or contraction-criticality.  Theorem 2.1 identifies
the extra invariant that a valid proof
must use: the arm's **monopoly set**, together with lexicographic model
rotation or minor-critical boundary-state exchange.

## 6. Exact remaining obstruction

For the degree-seven double-root gate, optimize the rooted `K_5` model
as in Theorem 2.1.  A failure of the private-bag split has only two
structural locations:

1. **cross-torso:** no non-root block lobe co-locates an `A` portal
   with all missing-label portals; or
2. **warehouse:** all such co-locations run through at most
   `floor(|Delta_x|/2)` nested branches, each of which monopolizes at
   least two root-defect labels and has the six-unit external load of
   Lemma 4.1.

For a `C_5` missing-root graph this is one warehouse branch or the
cross-torso case.  Resolving those two infinite configurations requires
one of two genuinely dynamic inputs: a two-path/web exchange in the root
torso, or a minor-transition argument showing that a double-monopoly
warehouse cannot remain critical under contraction of one of its
internal edges.  No further enumeration of Moser labels is needed to
state this residue.
