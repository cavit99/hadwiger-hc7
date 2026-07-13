# The full-shore reserve obstruction is statically sharp

## 1. A uniform false-twin suspension theorem

Let `I_2={a,b}` be two nonadjacent vertices.  For a graph `H`, write
`I_2 join H` for the graph obtained by making each of `a,b` adjacent to
every vertex of `H`, while retaining `ab` as a nonedge.

### Theorem 1.1

Let `q>=1`.  Suppose

\[
        \eta(H)=q,
        \qquad
        \eta(H-x)\le q-1\quad\text{for every }x\in V(H).        \tag{1.1}
\]

Then

\[
                         \eta(I_2\vee H)=q+1.                   \tag{1.2}
\]

In particular, `I_2 join H` has no `K_{q+2}` minor, even though its two
singleton false-twin vertices are pairwise anticomplete connected shores
which are each full to the boundary `V(H)`.

#### Proof

The lower bound in (1.2) follows by adjoining `a` to a `K_q` model in
`H`.

Suppose there were a `K_{q+2}` model.  If at most one branch bag met
`{a,b}`, deleting that bag would leave at least `q+1` pairwise adjacent
branch bags entirely in `H`, contrary to `eta(H)=q`.

Thus `a,b` lie in two distinct branch bags.  Delete those two bags.  The
remaining `q` bags form a `K_q` model in `H`.  This model uses every
vertex of `H`: if some `x` were unused, it would be a `K_q` model in
`H-x`, contradicting (1.1).

It follows that the two deleted branch bags contain no vertex of `H`.
They are therefore exactly `{a}` and `{b}`.  But these singleton bags
are nonadjacent, again a contradiction.  Hence no `K_{q+2}` model
exists, proving (1.2).  QED.

This proof is model-literal and does not use treewidth, density, or a
colouring theorem.

## 2. An eight-boundary `K_7`-free example

Let `H` be obtained from `K_5` by subdividing three distinct edges once.
Then `|H|=8` and `H` is vertex-minimal for a `K_5` minor.

Indeed, suppressing the three degree-two subdivision vertices gives a
`K_5` model.  If a subdivision vertex is deleted, the remaining graph
is a subdivision of a subgraph of `K_5-e`, and hence has no `K_5`
minor.  If an original `K_5` vertex is deleted, the remaining cyclic
core is a subdivision of a subgraph of `K_4`, with only pendant remnants
of the incident subdivided edges, and again has no `K_5` minor.

Applying Theorem 1.1 with `q=5` gives

\[
                       \eta(I_2\vee H)=6.                       \tag{2.1}
\]

Thus an eight-vertex boundary can have

* a spanning `K_5` model;
* no `K_5` model after any one boundary vertex is reserved;
* two anticomplete singleton full shores; and
* no `K_7` minor.

The companion verifier `exact8_subdivided_k5_full_shore_probe.py` checks
all 120 choices of the three subdivided edges, comprising four degree-
sequence orbits.  Every boundary deletion is `K_5`-minor-free and every
two-shore suspension is `K_7`-minor-free.  The hand proof above explains
the complete output.

## 3. Consequence for the exact-eight gate

The one-reserve bilateral lift in `hadwiger_full_shore_reserve_lift.md`
is best possible as a static rooted-model principle.  Its contrapositive

\[
                      \eta(X-x)\le4\quad(x\in X)                \tag{3.1}
\]

cannot be strengthened to `eta(X)<=4`, nor can two full shores plus a
spanning `K_5` model be asserted to give `K_7`.

The example is not seven-connected: its subdividing vertices have
degree four after the two full apices are added.  Therefore it isolates
seven-connectivity (together with the proper-minor transition geometry)
as genuinely new positive input.  Any valid exact-eight closure must use
that input to destroy the vertex-minimal spanning-model architecture;
contact incidence and reserve counting are exhausted.
