# Full-adhesion owner exchange: the exact model-clean theorem

## Status

This note records a uniform label-preserving augmentation theorem and the
sharp obstruction to a stronger static statement.

The numerical assertion

> a full cut of order `k`, covered by a `K_{k-1}`-model with a repeated
> owner, forces a `K_k`-minor

is false.  It remains false for a seven-connected graph, an exact
seven-cut, six protected model bags, six protected boundary vertices, and
even when every model bag meets the cut.  The obstruction is that an open
shore may already contain vertices of several branch bags.  "Sacrificing
one owner" then silently overlaps the proposed shore bag with the retained
bags.

What is true is a model-clean exchange.  A full shore augments a clique
model whenever all labels have protected cores outside the shore; trace
pieces may be donated to repair labels which do not themselves meet the
boundary.  With two full shores, one transverse two-terminal trace may be
split into the two new shore bags while one owner is sacrificed.  Thus a
failed exchange has a precise structural meaning: the whole surplus trace
is forced through the two distinguished shores, or some retained label has
no shore-free protected core.

## 1. Definitions

All graphs are finite and simple.  Let `Z` be a vertex cut of `G`, and let
`A,B` be distinct components of `G-Z` which are full to `Z`:

\[
                    N_G(A)=Z=N_G(B).                 \tag{1.1}
\]

A family

\[
                         K_1,\ldots,K_s              \tag{1.2}
\]

is a **protected `s`-frame** if its members are pairwise disjoint,
nonempty and connected, and every two members are adjacent.  Thus it is a
labelled `K_s`-model.  It is **`D`-clean** for a set `D` if every member is
disjoint from `D`.

Let `D` be a full component of `G-Z`, and let
`K_1,...,K_r` be a `D`-clean protected frame.  A **clean donor system** is
a vertex set `X`, disjoint from `D` and from all the `K_i`, such that

1. every component of `G[X]` is connected to `Z` inside itself, that is,
   it contains a vertex of `Z`;
2. for every `i`, either `K_i cap Z` is nonempty or
   `E_G(K_i,X)` is nonempty.

No adjacency between different donor components is required.  The full
shore will glue them.

For two shores, a **transverse connector** is a connected set

\[
             T\subseteq V(G)-(A\cup B)               \tag{1.3}
\]

which contains two distinct vertices of `Z`.

## 2. One-shore donor augmentation

### Theorem 2.1 (clean donor exchange)

Let `D` be a component full to `Z`.  If `K_1,...,K_r` is a `D`-clean
protected `r`-frame and `X` is a clean donor system, then `G` has a
`K_{r+1}`-minor.

#### Proof

Put

\[
                           L=D\cup X.                 \tag{2.1}
\]

The set `L` is connected.  Indeed, every component `R` of `G[X]`
contains a vertex `z_R in Z`, and fullness gives an edge from `z_R` to
`D`.  It is disjoint from every `K_i` by definition.

The branch sets `K_1,...,K_r` are pairwise adjacent.  If `K_i` meets
`Z`, fullness gives an edge from `D` to `K_i`.  Otherwise the donor
condition gives an edge from `X` to `K_i`.  Hence `L` is adjacent to
every `K_i`.  The `r+1` sets

\[
                         L,K_1,\ldots,K_r             \tag{2.2}
\]

are therefore a `K_{r+1}`-model.  QED.

### Corollary 2.2 (shore-free model augmentation)

If a `K_r`-model is disjoint from a full component `D` and every one of
its bags meets `Z`, then it augments with `D` to a `K_{r+1}`-model.

This is Theorem 2.1 with `X` empty.  Consequently, in a
`K_{r+1}`-minor-free graph every `K_r`-model whose bags all meet `Z` must
invade every full component of `G-Z`.

### Corollary 2.3 (trace-donor repair of missing owners)

Suppose a labelled `K_r`-model has been trimmed to protected cores
`K_1,...,K_r` outside a full shore `D`.  Let `X` be any collection of
pairwise core-disjoint trace pieces such that

* each trace piece is connected and contains a boundary vertex;
* their union is disjoint from the protected cores; and
* every core which misses `Z` is adjacent to at least one trace piece.

Then `G` has a `K_{r+1}`-minor.

This is the form used in an owner exchange: a trace piece may be peeled
from an old owner only after the remainder of every old bag is verified to
be a protected core.  Numerical trace rank without this verification is
not enough.

## 3. Two-shore sacrifice by a transverse trace

### Lemma 3.1 (prescribed connected bipartition)

If `T` is connected and `x,y` are distinct vertices of `T`, then
`V(T)` has a partition `X dotcup Y` such that

\[
 x\in X,\qquad y\in Y,\qquad G[X],G[Y]\text{ are connected},
 \qquad E_G(X,Y)\ne\varnothing.                       \tag{3.1}
\]

#### Proof

Take a spanning tree of `G[T]` and delete any edge of its `x-y` path.
The two resulting tree components have all the required properties.  QED.

### Theorem 3.2 (transverse owner sacrifice)

Let `A,B` satisfy (1.1).  Suppose

1. `K_1,...,K_{r-1}` is a protected `(r-1)`-frame contained in
   `G-(A union B)`;
2. every `K_i` meets `Z`; and
3. there is a transverse connector `T`, disjoint from the protected
   frame, containing distinct `x,y in Z`.

Then `G` has a `K_{r+1}`-minor.

#### Proof

Apply Lemma 3.1 to partition `T=X dotcup Y`, with `x in X` and
`y in Y`.  Define

\[
                         L_A=A\cup X,\qquad
                         L_B=B\cup Y.                 \tag{3.2}
\]

Both sets are connected: `A` is adjacent to `x`, and `B` to `y`.
They are disjoint from one another and from every protected core.  The
edge between `X` and `Y` makes them adjacent.

For every `i`, choose `z_i in K_i cap Z`.  Fullness gives edges from
both `A` and `B` to `z_i`; hence both `L_A` and `L_B` are adjacent to
every `K_i`.  Together with the protected `(r-1)`-frame, the sets

\[
                   L_A,L_B,K_1,\ldots,K_{r-1}         \tag{3.3}
\]

form a `K_{r+1}`-model.  QED.

### Corollary 3.3 (label-preserving repeated-owner exchange)

Let `M_0,...,M_{r-1}` be a labelled `K_r`-model.  If for some owner `h`

* every other label `i ne h` has a connected protected core
  `K_i subseteq M_i-(A union B)`;
* the cores are pairwise adjacent and meet `Z`; and
* `M_h` contains a transverse connector, disjoint from the cores, through
  two of its boundary vertices,

then sacrificing owner `h` gives a `K_{r+1}`-minor.

This is the correct version of the repeated-owner argument.  It explicitly
protects all retained labels and explicitly requires the repeated trace to
avoid the two shore interiors.

## 4. Trace rank becomes a two-shore localization theorem

For a connected bag `M`, put `Z_M=M cap Z`.  The exact trace-rank lemma
gives rank `|Z_M|-1`: terminal edges in `G[Z_M]` and connected carriers
in components of `M-Z`, with a carrier incident with `d` boundary
vertices contributing rank `d-1`.

### Theorem 4.1 (transverse trace or two-shore lock)

Assume the protected-core hypotheses of Corollary 3.3 for an owner `h`,
and let `p=|M_h cap Z|>=2`.  Then at least one of the following conclusions
is forced (and in a `K_{r+1}`-minor-free graph the second is forced):

1. `G` contains a `K_{r+1}`-minor; or
2. every connected subgraph of `M_h-(A union B)` meets at most one
   vertex of `Z_M`; equivalently, all `p-1` units needed to connect the
   boundary trace of `M_h` are carried through `A` or `B`.

In outcome 2, in particular,

* `G[Z_M]` is edgeless; and
* every component of `M_h-(A union B union Z)` has neighbours in at
  most one vertex of `Z_M`.

#### Proof

If a connected subgraph `T subseteq M_h-(A union B)` meets two distinct
vertices of `Z_M`, it is a transverse connector and Corollary 3.3 gives
outcome 1.  Otherwise outcome 2 is the literal negation.

An edge of `G[Z_M]` is itself a transverse connector.  Likewise, if a
component of `M_h-(A union B union Z)` has neighbours at two terminals,
join those neighbours through a tree in the component; together with the
two incident edges this is a transverse connector.  The final trace-rank
description follows because a connected trace on `p` terminals has rank
`p-1`, while no carrier outside the two shore interiors can have positive
rank in outcome 2.  QED.

Theorem 4.1 closes an infinite family: every full adhesion with a
label-protected repeated owner and even one transverse trace unit already
contains the larger clique minor.  Its residue is not an unstructured
"bad owner".  It is an exact two-shore trace lock.

### HC7 specialization

At a promoted maximal-society one-gate, let the root label and four of the
five protected labels have shore-free, pairwise adjacent cores meeting
the adhesion, and let the fifth protected bag be a repeated owner.  The
nonzero trace guaranteed by the seven-cut count closes the cell unless
that whole trace is routed through the two distinguished shore interiors.
Thus the count `six protected boundary vertices in five bags` becomes a
minor whenever the repeated trace is transverse; in a `K_7`-minor-free
cell it is forced into the two-shore lock of Theorem 4.1.

This specialization deliberately does not assert that arbitrary protected
bags possess shore-free cores.  That is the exact label-preservation issue
which the static count cannot settle.

## 5. Sharp seven-connected counterexample to every static strengthening

Let `I` be the icosahedral graph with edge set

\[
\begin{split}
&01,05,07,08,0\,11,12,15,16,18,23,26,28,29,34,36,39,3\,10,\\
&45,46,4\,10,4\,11,56,5\,11,78,79,7\,10,7\,11,89,9\,10,10\,11.
\end{split}                                           \tag{5.1}
\]

Put `G=I vee K_2`, and call the two universal adjacent vertices `u,v`.
The icosahedron is five-connected and planar, has a `K_4`-minor, and no
`K_5`-minor.  Therefore

\[
                  kappa(G)=7,\qquad eta(G)=6.          \tag{5.2}
\]

Indeed, adjoining a universal clique of order two raises both connectivity
and Hadwiger number by two.  For the upper bound on the latter, at most two
branch sets of any clique model can meet `{u,v}`; deleting them leaves the
remaining clique model in `I`.

Let

\[
              Z=N_I(0)\cup\{u,v\}
               =\{1,5,7,8,11,u,v\}.                  \tag{5.3}
\]

Then `G-Z` has exactly the two components

\[
              A=\{0\},\qquad B=\{2,3,4,6,9,10\},     \tag{5.4}
\]

and both are full to `Z`.  The following are six branch bags of a
`K_6`-model:

\[
        \{1\},\quad \{5\},\quad \{0,7\},\quad
        \{8,9,10,11\},\quad \{u\},\quad \{v\}.       \tag{5.5}
\]

Every bag meets `Z`, and the fourth bag meets it twice.  Nevertheless
`G` has no `K_7`-minor by (5.2).  The repeated trace is the path
`8-9-10-11`, whose interior lies in the shore `B`; the bag `{0,7}` also
invades `A`.  This is exactly the two-shore/core-invasion obstruction in
Theorem 4.1.

There is also a model with the precise numerical shape of the maximal-
society promoted gate:

\[
 \{0,1,2\},\quad \{3\},\quad \{4,5\},\quad
 \{7,8,9,11\},\quad \{u\},\quad \{v\}.               \tag{5.6}
\]

Its root bag crosses both shores and meets `Z` only at `q=1`; the other
five bags contain the remaining six boundary vertices, one protected bag
misses `Z`, and another repeats.  Thus seven-connectivity, a gate vertex,
six protected boundary vertices, full shores, and a fixed `K_6`-model do
not force `K_7`.

The graph `G` is six-colourable, not seven-contraction-critical.  Hence
the example does not refute a dynamic critical-state theorem.  It proves
that any such theorem must actually use the deletion/contraction state
locks or maximal-society exchange; capacity, connectivity and model-owner
counts alone cannot prove it.

## 6. Exact remaining dynamic target

At the HC7 one-gate, a valid completion must now establish at least one of
the following facts from contraction-criticality:

1. the protected model can be rerouted to shore-free cores, after which
   Theorem 4.1 consumes the repeated trace;
2. a trace piece can be peeled as a clean donor system and Theorem 2.1
   repairs every missing label; or
3. if all trace lies in the two shores as in (5.5), opposite tight
   deletion/society-contraction states coincide on a smaller adhesion and
   colour-glue.

The icosahedral join shows that none of these three outcomes follows from
the static full-adhesion hypotheses.  This is the sharp boundary between
the proved owner-exchange theorem and the remaining state problem.
