# Operation-sensitive states at a complex gated quotient shore

## 1. Setup

Let `r\ge2`.  Let `G` be non-`r`-colourable and suppose every proper
minor of `G` is `r`-colourable.  Fix `v`, put `H=G-v`, and suppose a
complex bag `B` and a set `X\subseteq V(H)-B` satisfy the quotient-deficit
conclusion of Theorem 4.1 in
`hadwiger_foreign_transit_cycle_potential.md`:

* `H-(B\cup X)` has at least two components; and
* for every such component `D`,
  \[
                  N_H(D)\subseteq B\cup X,
        \qquad P_D:=N_B(D)\ne\varnothing.               \tag{1.1}
  \]

If `H` is `r`-connected, then

\[
                         |P_D|\ge r-|X|\ge2              \tag{1.2}
\]

for every shore `D`.

This note records the exact operation-sensitive information available at
such a shore.  It is stronger than portal counting but still exposes one
sharp blocker: a defect-coloured shadow in `X` can serve every Kempe
layer.  Any final allocation theorem must remove that shadow using the
promoted Hall/rainbow data.

## 2. Every shore operation creates a genuine boundary transition

Put

\[
                         W_D=X\cup P_D.                  \tag{2.1}
\]

Then `(D\cup W_D,H-D)` is a separation of `H` with adhesion `W_D`.
For a colouring `c` of a graph containing `v` and `W_D`, write

\[
 \sigma_{W_D}(c)=(\Pi_{W_D}(c),M_{W_D}(c)),             \tag{2.2}
\]

where `M_{W_D}(c)` is the block, possibly empty, receiving the colour of
`v`.

### Theorem 2.1 (genuine gated-shore novelty)

Let `e` be an edge with both ends in `D`, and let `c_e` be any
`r`-colouring of `G-e`.  Its restriction to the closed `D`-shore cannot be
replaced by a proper colouring of
`G[D\cup W_D\cup\{v\}]` with the original edge `e` present which

1. has the same colours on `W_D`; and
2. gives `v` the same colour.

Equivalently, the marked state (2.2) is accepted by the operated shore and
by the untouched opposite shore, but not by the original shore.

#### Proof

The restriction of `c_e` to `H-D`, together with the colour of `v`, is
proper because the deleted edge lies inside `D`.  If the proposed
replacement on `D\cup W_D\cup\{v\}` existed, glue it to that untouched opposite
restriction.  The colours agree literally on `W_D\cup\{v\}`.  Every edge
of `G`, including `e`, is then properly coloured, contradicting the choice
of `G`.

More generally, suppose an original-shore colouring induced only the same
marked state rather than the same literal colour names.  Equality of the
boundary partitions gives a palette permutation aligning all colours on
`W_D`; equality of the marked apex block lets the same permutation align
the colour of `v` (in the unpinned case both apex colours are absent from
the boundary and the permutation extends accordingly).  The preceding
gluing argument applies after that permutation.  This proves the stated
marked-state form. \(\square\)

Thus every internal shore edge creates actual transition novelty at the
small adhesion `X\cup P_D`; it is not merely a colouring of a quotient.

### Theorem 2.2 (different shores have disjoint full-gate states)

Let `D,E` be distinct components of `H-(B\cup X)`, let
`e\in E(H[D])` and `f\in E(H[E])`, and let `c_e,c_f` colour `G-e,G-f`.
On the common enlarged adhesion

\[
                              W=B\cup X,                 \tag{2.3}
\]

one has

\[
                         \sigma_W(c_e)\ne\sigma_W(c_f). \tag{2.4}
\]

#### Proof

Group `D` on one open shore and all other components on the other, while
placing `W` in both closed shores.  The edges `e,f` are supported on
opposite shores.  Equality in (2.4) would let the two untouched
restrictions cross-splice, after a palette permutation fixing the marked
apex block, to give an `r`-colouring of `G`.  This is Theorem 1.1 of
`hadwiger_fixed_model_transition_gate.md`. \(\square\)

The enlargement from `W_D` to `W` is intentional.  Marked states from two
different shores live on different sets `W_D,W_E`; they may be compared
only after retaining the whole complex gate bag.  Contracting `B` would
lose precisely the expansion information needed to colour `G`.

## 3. Simultaneous operations give exact gate capacity

Take distinct shores `D,E` and vertex-disjoint internal edges
`e=xy\subseteq D`, `f\subseteq E`.  Contract both and colour the proper
minor.  Expand the two contraction vertices, obtaining a colouring `c` of
`G-\{e,f\}`.  Write

\[
                         c(x)=c(y)=\beta.                \tag{3.1}
\]

By the double-operation repair exclusion, at least one shore is locked;
rename so that it is `D`.

### Theorem 3.1 (complex-gate Kempe capacity)

For every colour `\gamma\ne\beta`, one of the following holds.

1. The ends `x,y` are joined by a `\{\beta,\gamma\}`-path in
   `G-\{e,f\}` avoiding `e`.
2. They lie in distinct `\{\beta,\gamma\}`-components, and each component
   meets
   \[
                         K_D=X\cup P_D\cup\{v\}.         \tag{3.2}
   \]

In the second outcome, if `n_\theta` denotes the number of vertices of
`K_D` coloured `\theta`, then

\[
                         n_\beta+n_\gamma\ge2.           \tag{3.3}
\]

#### Proof

If the two endpoint components are distinct and one avoids the gate
`K_D`, that component lies wholly in the open shore `D`: by (1.1), a path
can leave `D` only through `X\cup P_D`, and `v` is the only vertex omitted
when passing from `G` to `H`.  Switching `\beta,\gamma` on that component
fixes `W_D\cup\{v\}`, separates the colours of `x,y`, and repairs `e`
while `f` stays deleted.  This is the forbidden one-shore repair.  Hence
both components meet (3.2).

The components are disjoint.  Every gate vertex they contain has colour
`\beta` or `\gamma`, so their two distinct gate hits prove (3.3).
\(\square\)

### Corollary 3.2 (the single-shadow obstruction is exact)

In a separated layer:

* if `n_\beta=0`, then `n_\gamma\ge2`;
* if `n_\beta=1`, then `n_\gamma\ge1`; and
* only when `n_\beta\ge2` can the layer be blocked without any
  `\gamma`-coloured gate vertex.

Summing over all `\gamma\ne\beta`, if `n_\beta\le1` and every layer is
separated, the gate contains at least

\[
                  2(r-1)\quad\hbox{or}\quad r           \tag{3.4}

\]

vertices counted with colour multiplicity, respectively.  More precisely,
the bounds are `2(r-1)` when `n_\beta=0` and `1+(r-1)=r` when
`n_\beta=1`.

This is the exact capacity statement.  Portal multiplicity (1.2) alone
does not say where these coloured shadows lie: all nondefect colours may
be carried by `X`, while one or two `\beta`-vertices may lie in `P_D` (or
vice versa).  The Hall-circuit rainbow core and collision theorem are
therefore the correct extra inputs for assigning capacity to model labels.

## 4. When the capacity theorem already gives a model move

Suppose the locked edge `e` is an essential edge of a connected piece
which is intended to remain one branch bag.  In outcome 1 of Theorem 3.1,
take a shortest endpoint path.  Then exactly one of the following occurs.

1. Its interior avoids `v` and every foreign branch bag.  Replacing `e`
   by the path is a label-preserving rerouting.
2. It first hits a named foreign bag, giving the lobe transfer tested by
   Lemma 3.1 of `hadwiger_foreign_transit_cycle_potential.md`.
3. It uses `v`, giving an apex-pinned obstruction.

If case 2 is root-safe and its source lobe owns no label other than the
target, the lexicographic potential performs the transfer.  Directed
cycles of all such transfers are impossible.  Therefore the only residue
left by Theorems 2.1--3.1 is exactly

\[
 \boxed{\text{a multi-owner/contact-protected lobe together with a
 defect-coloured gate shadow.}}                          \tag{4.1}
\]

This is a strictly smaller operation-sensitive target than arbitrary
foreign-bag transit termination.

### Theorem 4.1 (opposite singleton defects merge and close)

In the co-rank-one Hall setup of
`hadwiger_corank_one_portal_basis_descent.md`, take the two clean portal
endpoints `p,q` and a connected adjacent split

\[
                         B=Y_p\mathbin{\dot\cup}Y_q.     \tag{4.2}
\]

Use the deficient-label sets

\[
 D_p=\{j:Y_p\not\sim B_j\},\qquad
 D_q=\{j:Y_q\not\sim B_j\}.                             \tag{4.3}
\]

If

\[
                         D_p=\{a\},\qquad D_q=\{b\},
                         \qquad a\ne b,                  \tag{4.4}
\]

then `G` contains a `K_{r+1}` minor.

#### Proof

Choose the far Hall certificate which omits label `b`.  It has disjoint
`X`-suffixes to all `B_j`, `j\ne b`.  Concatenate these suffixes with the
fixed clean root-to-`X` paths.  This gives `r-2` pairwise adjacent rooted
far branch sets `F_j`, one for every `j\ne b`; each `F_j` contains `B_j`.

There is no suffix ending in `B_b`, so enlarge

\[
                         F_a\longmapsto F_a\cup B_b.     \tag{4.5}
\]

This set is connected because `B_a` and `B_b` are adjacent old clique
bags.  It remains adjacent to every other `F_j`, and disjointness is
preserved.

Absorb the two clean portal paths into `Y_p,Y_q`.  The resulting two sets
are connected, adjacent, rooted, and disjoint from all far sets.  The
`p`-side misses `B_a` but sees `B_b`, so it is adjacent to the enlarged
set (4.5).  The `q`-side misses `B_b` but sees `B_a`, so it too is
adjacent to (4.5).  By (4.4), both sides see every other far bag.

We have therefore constructed

\[
             Y_p^+,\quad Y_q^+,\quad
             F_a\cup B_b,\quad (F_j:j\notin\{a,b\})      \tag{4.6}
\]

as `r` disjoint pairwise adjacent connected sets in `H`, each containing
a distinct neighbour of `v`.  Together with `\{v\}` they form a
`K_{r+1}`-model. \(\square\)

### Corollary 4.2 (the split lock is at least three-sided)

In a target-minor-free co-rank-one cell, if both defect sets of a connected
two-portal split are nonempty, then

\[
                         |D_p\cup D_q|\ge3.              \tag{4.7}
\]

Indeed they are disjoint because every deficient bag is adjacent to the
unsplit connected bag `B`; union size two would therefore give (4.4).

This improves the former bound `|D_p\cup D_q|\ge2`.  It is a genuine
branch-set closure, not a state count.  In `HC_7`, where there are five
deficient labels, every surviving two-ended split consumes at least three
labels before any dynamic state argument is needed.

### Theorem 4.3 (portal-piece / clique-group assembly)

The preceding merge is the two-piece instance of a uniform rooted-model
assembly principle.

Let `I` index pairwise adjacent old branch bags `(B_j:j\in I)`.  Suppose
we have

* `\ell` disjoint, pairwise adjacent, connected rooted pieces
  `Y_1,\ldots,Y_\ell`;
* `h` disjoint, pairwise adjacent, connected rooted far carriers
  `F_1,\ldots,F_h`, disjoint from the `Y_i`;
* distinct representative labels `a_1,\ldots,a_h\in I`, with
  `B_{a_s}\subseteq F_s`; and
* a partition
  \[
                         I=J_1\dot\cup\cdots\dot\cup J_h,
             \qquad a_s\in J_s,                         \tag{4.8}
  \]
  such that for every `i\in[\ell]` and `s\in[h]`,
  \[
                         Y_i\sim B_j
                 \quad\hbox{for some }j\in J_s.         \tag{4.9}
  \]

Assume all displayed root carriers are mutually disjoint and
`h+\ell=r`.  Then `G` contains a `K_{r+1}` minor.

#### Proof

For each `s`, enlarge

\[
                   F_s^+=F_s\cup\bigcup_{j\in J_s-\{a_s\}}B_j. \tag{4.10}
\]

The old bags inside one group are pairwise adjacent, so `F_s^+` is
connected.  Distinct groups are disjoint and adjacent because every pair
of old bags was adjacent.  Condition (4.9) makes every `Y_i` adjacent to
every `F_s^+`, while the `Y_i` are pairwise adjacent by hypothesis.
Thus the `\ell+h=r` displayed sets are disjoint pairwise adjacent rooted
branch sets.  Adding `\{v\}` gives the target minor. \(\square\)

This separates the uniform problem into two finite-rank objects:

1. a root-shore gammoid basis selecting the `Y_i` and the far
   representatives; and
2. a partition of the clique-bag labels into groups whose support vectors
   cover all portal pieces.

For `\ell=2` in a co-rank-one circuit, `h=r-2` and `|I|=r-1`, so a
partition has exactly one nonsingleton group.  All singleton groups must
be adjacent to both pieces.  The one doubleton group can repair exactly
one defect on each opposite side.  This recovers Theorem 4.1 and gives the
exact two-piece allocation obstruction:

\[
 \boxed{\text{at least three defective labels, or two defects on the same
 side.}}                                                 \tag{4.11}
\]

For three portal pieces, only two units of grouping surplus are needed.
The missing input is correspondingly precise: exchange one `X` endpoint
of the root-shore gammoid basis for a third portal while retaining a
compatible far linkage on the remaining `X` endpoints.  This is a
finite-rank basis-exchange statement, rather than an unrestricted rooted
clique theorem.

### Theorem 4.4 (third portal, exact two-gate adhesion, or source-tight lock)

Retain the co-rank-one Hall setup, assume `G` is `(r+1)`-connected, and
let `M_U` be the root-shore gammoid on `X\cup P`.  Thus

\[
                         |X|=r-2,                         \tag{4.12}
\]

and Theorem 3.1 of `hadwiger_corank_one_portal_basis_descent.md` gives
distinct `p,q\in P` such that

\[
                         X\cup\{p,q\}                    \tag{4.13}
\]

is independent.  Then at least one of the following holds.

1. **Third-portal exchange.**  There are `z\in P-\{p,q\}` and `x\in X`
   such that
   \[
                    (X-\{x\})\cup\{p,q,z\}              \tag{4.14}
   \]
   is independent.  Hence a single shore-clean linkage has three portal
   endpoints and all but one Hall-interface endpoint.
2. **Exact two-gate adhesion.**  There are a two-vertex set `Y` disjoint
   from `X` and a nonempty root-side component `C` such that
   \[
                    N_G(C)=X\mathbin{\dot\cup}Y
                              \mathbin{\dot\cup}\{v\}.    \tag{4.15}
   \]
   In particular, the right side of (4.15) is an exact `(r+1)`-vertex
   separator between an unused neighbourhood root and the deficient
   clique bags.
3. **Source-tight lock.**  One has
   \[
                    |R-X|=2,qquad |R|=r,qquad X\subseteq R, \tag{4.16}
   \]
   and the two roots `R-X` separate every root in `X` from `P` inside the
   root shore.  In particular this can occur only in the exact
   minimum-degree cell `d_G(v)=r+1`.

#### Proof

Assume outcome 1 fails.  Fix `z\in P-\{p,q\}`.  If
`X\cup\{p,q,z\}` were independent, deleting any `x\in X` would give
(4.14).  Hence it is dependent.  Since (4.13) is independent, adding `z`
creates a unique circuit `C_z`.

If `C_z` contained a member `x\in X`, the elementary circuit exchange
property would make `(X-x)\cup\{p,q,z\}` independent, again giving
outcome 1.  Therefore

\[
                         C_z\subseteq\{p,q,z\}.           \tag{4.17}
\]

It follows that every `z\in P-\{p,q\}` lies in the closure of
`\{p,q\}`.  Consequently

\[
                         r_{M_U}(P)\le2.                  \tag{4.18}
\]

In the strict-gammoid presentation, (4.17) says that at most two
vertex-disjoint shore-clean paths can join the unused-root source set `R`
to `P`.  Directed vertex Menger therefore supplies a vertex set `Y` of
order at most two separating `R-Y` from `P-Y` inside the root shore.

If `(R-X)-Y` is empty, then `R-X\subseteq Y`.  The source lower bound
`|R|\ge r` and `|X|=r-2` give `|R-X|\ge2`; hence equality holds,
`Y=R-X`, `|R|=r`, and `X\subseteq R`.  The separator statement says
exactly that these two roots separate the remaining root sources `X`
from `P`.  This is outcome 3, and `|R|=d_G(v)-1=r` gives the asserted
degree equality.

We may therefore choose `s\in(R-X)-Y`.  Let `C` be its component in
`U-Y`.

By the Hall promotion theorem, every neighbour of `U` outside `U` lies in
`X\cup P` (apart from the apex `v` in `G`).  The choice of `Y` excludes a
neighbour of `C` in `P-Y`, since such an edge would give an `R-Y` to
`P-Y` path avoiding `Y`.  Hence

\[
                         N_G(C)\subseteq X\cup Y\cup\{v\}. \tag{4.19}
\]

Every deficient branch bag survives outside this set, so `N_G(C)` is a
genuine separator.  Its order is at most

\[
                         (r-2)+2+1=r+1.                  \tag{4.20}
\]

The `(r+1)`-connectivity of `G` forces equality throughout: `|Y|=2`,
`Y\cap X=\varnothing`, and no vertex on the right side of (4.18) can be
absent from `N_G(C)`.  This is exactly (4.15). \(\square\)

### Corollary 4.5 (compatible far side after the exchange)

In outcome 1, fix a far Hall certificate omitting a label `i`.  Its
`r-2` suffixes biject `X` with the labels in `I-\{i\}`.  Delete the suffix
starting at the exchanged vertex `x`.  The remaining `r-3` suffixes are
compatible with the root linkage (4.14).

Thus the third-portal outcome supplies exactly the `\ell=3,h=r-3` root
and far linkage counts required by Theorem 4.3.  The only remaining task
there is geometric/support allocation: split the accessible bag into
three pairwise adjacent portal pieces and group the deficient labels into
`r-3` covering classes.

Theorem 4.4 is the promised structural trichotomy.  Failure of a third
portal exchange no longer leaves an amorphous rank obstruction: it gives
an exact two-shore adhesion of the ambient connectivity order, ready for
crossed minor-transition state analysis, except in the sharply isolated
minimum-degree source-tight cell.

### Corollary 4.6 (normal form of the source-tight lock)

In outcome 3 of Theorem 4.4, write `Y=R-X`.  Every component `C` of
`U-Y` has a neighbour in `P` and has no neighbour in `X`.  Consequently

\[
                         N_U(X)\subseteq Y.              \tag{4.21}
\]

#### Proof

No vertex of `U-Y` belongs to `N_G(v)`: all neighbourhood roots outside
the old model are `R=X\dot\cup Y`, while the unique old-model foot lies
in `B`.  Suppose a component `C` of `U-Y` had no neighbour in `P`.
Hall promotion gives

\[
                         N_G(C)\subseteq X\cup Y,         \tag{4.22}
\]

because `v` has no neighbour in `C`.  The right side has order `r`, and
the deficient bags survive outside it.  This contradicts
`(r+1)`-connectivity.  Hence every component meets `P`.

But `Y` separates the source set `X=R-Y` from `P` in the root shore.  A
component of `U-Y` with both an `X`-neighbour and a `P`-neighbour would
give an `X`--`P` path avoiding `Y`.  Therefore no such component meets
`X`, proving (4.21). \(\square\)

Thus the degree-`r+1` exception is a literal two-gate web: all access from
the `r-2` interface roots into the portal shore goes first through the two
remaining neighbourhood roots, and every part beyond those roots reaches
the accessible bag.  This is substantially more rigid than an arbitrary
rank-two gammoid obstruction.

## 5. Audit on the two-path counterarchitecture

Use the graph in Proposition 5.1 of
`hadwiger_foreign_transit_cycle_potential.md`.  It has the explicit proper
five-colouring

\[
\begin{array}{c|ccccccccccc}
 &v&a_L&a_0&a_R&b_L&b_0&b_R&s_1&s_2&s_3&s_4\\ \hline
c&0&1&2&1&2&1&3&0&3&2&4.
\end{array}                                             \tag{5.1}
\]

Viewed as a six-colouring, (5.1) remains a proper colouring after every
edge deletion or contraction-free shore operation.  In particular, for
any two opposite deleted edges, both shores admit the same honest marked
boundary state: simply restrict (5.1).  No deleted edge is forced to be a
monochromatic defect, and Theorem 2.1's novelty conclusion fails.

This pinpoints the exact axiom excluding the static construction:

\[
 \boxed{\text{proper-minor minimal non-`r`-colourability, through genuine
 one-step boundary-state novelty.}}                     \tag{5.2}
\]

The example already has spanning, contact maximality, inclusion-minimal
bags, a foreign-transit cycle, and no target minor.  It fails neither
portal geometry nor tree normalization; it fails precisely the dynamic
transition axiom used in Sections 2--3.

## 6. Exact remaining gap

Theorems 2.1--3.1 prove that the quotient shore carries both kinds of
capacity now known to be necessary:

1. at least `r-|X|` distinct geometric portals in `B`; and
2. a new, shore-specific marked state whose locked Kempe layers consume
   the actual gate `X\cup P_D\cup\{v\}`.

What is not yet proved is the final alignment: a defect-coloured shadow
can be unrelated to the portal vertices which make a lobe transferable.
The next lemma must use the promoted Hall rainbow/collision data to show
that this shadow either belongs to the multiply owned bag in the required
label position, or can be switched to create the same full-gate state on
an opposite shore.  Without that alignment, (3.3) is sharp.
