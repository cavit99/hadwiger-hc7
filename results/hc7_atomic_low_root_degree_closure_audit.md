# Independent audit: atomic low-root-degree closure

## Verdict

**GREEN** at frozen source SHA-256
`cbc7c26adca059eb2b723e5988720a6fcd7eed40063f98b532a72666a779cb7c`.

The two-defect list lemma is correct, including the requirement that both
seed classes be nonempty.  In the atomic application, relative
seven-connectivity makes the root miss at most two boundary literals;
root-deletion makes the other carrier full to all six noncompulsory
literals.  The resulting lists are exactly those of the lemma, and its
singleton clique reservoir meets every hypothesis of the audited adaptive
clique-reservoir return theorem.  Hence every connected-bipartite atom
with `d_{G[A]}(z)<=2` six-colours.

No adjacency between the two rich packets is required.  The disconnected
`K_{1,3} dotunion K_3` frontier is correctly excluded.

## 1. Audit of the two-defect reservoir lemma

Fix the bipartition side `B_u` containing `u`, and put

\[
                         D_{\rm bad}=D\cap B_u.
\]

Under the global orientation assigning label zero to `B_u`, the
prescription at `u` is satisfied and precisely the vertices of
`D-D_bad` receive their prescribed label one.  The three reservoir choices
in the source are exhaustive.

* If `|D_bad|=0`, take `U=emptyset`; the global orientation satisfies all
  prescriptions.
* If `|D_bad|=1`, remove that unique incompatible prescribed vertex.  All
  surviving prescribed vertices agree with the same global orientation,
  even if deletion disconnects `H`.
* If `|D_bad|=2`, remove `u`.  Both surviving prescribed vertices lie on
  the same original bipartition side and demand label one, so the opposite
  global orientation satisfies them.  Components containing no prescribed
  vertex may be oriented arbitrarily.

Thus `H-U` always has a proper list-colouring.  It can also be chosen to
use both labels.  If `H-U` contains an edge, properness supplies both.
If it is independent, connectedness of `H` implies `U` is nonempty and
hence a singleton.  At least three vertices survive, and at most two of
them retain singleton lists.  A flexible isolated vertex can be assigned
the missing label.  Therefore the two seed classes are genuinely nonempty,
not merely formal empty parts.  Finally, an empty set or singleton is a
clique, as required.

## 2. Root support and exact carrier lists

The atomic hypotheses include `|A|>=2`, so the audited root-deletion
normalization applies and gives

\[
                         A-z\text{ connected},
                 \qquad N_S(A-z)=W.
\]

The stated `S`-fullness of `A` also follows directly from the remaining
hypotheses: if `A` missed any `w in W`, the six-set `S-{w}` would separate
the nonempty `A` from the nonempty `R`.

Since there is no `A-R` edge,

\[
 d_{G[A]}(z)+|N_S(z)|=d_G(z)\ge7.
\]

Consequently `d_{G[A]}(z)<=2` gives `|N_S(z)|>=5`.  The root contacts `u`
through the compulsory edge, so its defect

\[
                         D=S-N_S(z)
\]

lies in `W` and has order at most two.

Set `C_0={z}` and `C_1=A-z`.  These sets are nonempty, disjoint and
connected.  They are adjacent because `A` is connected.  Their literal
boundary-contact lists are exactly

\[
 \Lambda(u)=\{0\},\qquad
 \Lambda(d)=\{1\}\ (d\in D),\qquad
 \Lambda(s)=\{0,1\}\ (s\notin D\cup\{u\}).
\]

Indeed, `zu` is the unique `A-u` edge, `A-z` contacts every member of
`W`, and membership outside `D` is precisely contact with `z`.

## 3. Adaptive return and gluing

Apply the reservoir lemma to the connected bipartite graph `H=G[S]`.
Let `I_0,I_1` be its two nonempty colour classes.  Properness makes each
an independent set.  The list condition says every literal of `I_i`
contacts the named connected carrier `C_i`.  The carriers are disjoint
and adjacent, and `U` is a clique of order at most one.  Thus all
hypotheses of the audited adaptive clique-reservoir theorem hold at
`(k,q)=(7,2)`.

That theorem contracts the two connected carrier-seed sets in a proper
minor.  Its actual returned boundary partition may absorb the reservoir
vertex into either seed block, but its recomputed packet demand is at most
two.  Two disjoint connected `S`-full rich packets therefore reproduce
that exact state on the opposite closed shore.  A palette permutation
aligns corresponding blocks, and the absence of `A-R` edges makes the
gluing proper.  Hence `G` is six-colourable.

The conclusion is confined to a connected bipartite boundary.  For
`K_{1,3} dotunion K_3`, deleting a possible reservoir vertex leaves
multiple independently orientable components, so this proof does not
silently cover that frontier.
