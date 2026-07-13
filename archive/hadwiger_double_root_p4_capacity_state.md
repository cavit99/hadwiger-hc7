# The double-root trace gives two oriented `P4` gates

## 1. Scope and audit verdict

Let `G` be a proper-minor-minimal non-six-colourable graph with no
`K_7` minor.  Let `v` have degree seven, put

\[
                       H=G-v,\qquad N=N_G(v),
\]

and fix a nonedge `ab` of `G[N]`.  Contracting the star on
`{v,a,b}` and expanding a six-colouring gives an exact trace `c` on
`H`: vertices `a,b` have colour 0 and the other five vertices

\[
                       U=\{u_1,\ldots,u_5\}
\]

have the five distinct colours `1,...,5`.

The reserved-connector theorem and its degree-seven application in
`hadwiger_reserved_connector_adhesion_principle.md` are sound.  The
only repair made during this audit is a wording correction in the proof
of its private-bag split lemma.  In particular:

* Kriesell--Mohr supplies a rooted `K_5`-model
  `B_1,...,B_5` in the union of the five nonzero colour classes;
* if `a,b` have a connector avoiding the five bags, it is the sixth
  neighbourhood-meeting bag and gives a `K_7` minor with `{v}`;
* otherwise the repeated roots lie in distinct components of the
  complement of the model.

This note sharpens the latter alternative.  It produces two *oriented*
separators contained in only four named bags, and records the exact
minor-transition state forced when one has order six.  No Moser labels
or finite enumeration are used.

## 2. Two oriented four-bag separators

The underlying statement is uniform.  It is useful to record it before
specialising the parameters.

### Theorem 2.0 (uniform double-root `P4` gate)

Let `H` be `k`-connected, let `B_1,...,B_m` be a rooted
`K_m`-model with roots `u_i`, and let `a,b` lie outside its union.
Assume that at least one of `au_i,bu_i` is an edge for every `i`.
Here a **terminal-meeting extension** means the old `m` bags together
with one connected branch set outside their union which contains at
least one of `a,b` and is adjacent to every old bag.  If these data do
not contain such a `K_{m+1}`-model, then:

1. `a,b` lie in distinct components `A,D` outside the model;
2. their model-bag contact sets cover `[m]`, are both proper, and have
   nonempty opposite differences;
3. for any
   `x in I_A-I_D` and `y in I_D-I_A`, there are two oriented
   inclusion-minimal separators, one separating `A` from
   `D union B_y` inside `union_{i ne y}B_i`, and the other separating
   `D` from `A union B_x` inside `union_{i ne x}B_i`;
4. both separators have order at least `k` and are distributed among
   only `m-1` named bags.  If the portal surplus is defined by

   \[
      \sum_i \max\{|Z\cap B_i|-1,0\},
   \]

   their total portal surplus is therefore at
   least

   \[
                             k-m+1.                         \tag{2.0}
   \]

Both distinguished components are full to the selected separator.

#### Proof

If `a,b` have a path outside the model, that path and the `m` old bags
are the desired `K_{m+1}`-model.  Thus their outside components are
distinct.  Root adjacency makes the two contact sets cover `[m]`.  A
contact set equal to `[m]` likewise gives the forbidden model by using
that component and the `m` old bags.  Hence both sets are proper; two
proper sets whose union is `[m]` have nonempty opposite differences.

For `y in I_D-I_A`, the set `A` is anticomplete to both `D` and
`B_y`, while `D union B_y` is connected.  Deleting all old bags except
`B_y` therefore separates these two connected sets.  Take an
inclusion-minimal subseparator.  Connectivity gives order at least `k`,
and minimality gives a neighbour in each distinguished component from
every separator vertex, exactly as in the standard full-adhesion proof.
The separator lies in `m-1` named bags, yielding (2.0).  Interchange the
two sides and use `x` for the second orientation.  QED.

For `m=5,k=6`, (2.0) is the surplus-two threshold.  This is the first
uniform rooted principle produced by the repeated-pair analysis: the
obstruction is not an arbitrary failure of rooted linkage, but two
oppositely oriented atomic `P4` gates.

Put

\[
             W=\bigcup_{i=1}^5B_i,
\]

and let `A,D` be the components of `H-W` containing `a,b`,
respectively.  Define

\[
 I_A=\{i:E(A,B_i)\ne\varnothing\},\qquad
 I_D=\{i:E(D,B_i)\ne\varnothing\}.
\]

### Theorem 2.1 (double-root `P4` adhesion dichotomy)

If `G` has no `K_7` minor, then there are distinct indices

\[
                  x\in I_A-I_D,\qquad y\in I_D-I_A.       \tag{2.1}
\]

For these indices define

\[
 W_A=\bigcup_{k\ne y}B_k,\qquad
 W_D=\bigcup_{k\ne x}B_k.                                \tag{2.2}
\]

Then:

1. `W_A` separates `A` from the connected set `D union B_y`;
2. `W_D` separates `D` from the connected set `A union B_x`;
3. there are inclusion-minimal separators

   \[
       Z_A\subseteq W_A,\qquad Z_D\subseteq W_D,
       \qquad |Z_A|,|Z_D|\ge6;                            \tag{2.3}
   \]

4. each selected separator is full on both distinguished sides: if
   `R_A,T_A` are the components of `H-Z_A` containing `A` and
   `D union B_y`, then

   \[
                N_H(R_A)=Z_A=N_H(T_A),                    \tag{2.4}
   \]

   and the symmetric assertion holds for `Z_D`;
5. the separator in (2.3) is distributed among four named model bags.
   Hence its total portal surplus over one vertex per bag is at least
   two, and is at least three if its order is strictly greater than six.

If either separator has order six, adjoining `v` gives a full
seven-adhesion in `G`.  Every component of `G-(Z_A union {v})` (or of
the symmetric cut) is full to that seven-set.

#### Proof

Dirac's inequality gives `alpha(G[N])<=2`.  Since `ab` is a
nonedge, for every `i` at least one of `au_i,bu_i` is an edge.
Consequently

\[
                         I_A\cup I_D=[5].                  \tag{2.5}
\]

If `I_A=[5]`, the six bags `A,B_1,...,B_5` form an
`N`-meeting `K_6`-model; the same holds with `D` in place of
`A`.  Thus both contact sets are proper.  Equation (2.5) then implies
that neither contains the other, proving (2.1).

The component `A` is anticomplete to `D`, and `y notin I_A`, so it
is anticomplete to `B_y`.  The set `D union B_y` is connected:
`y in I_D`, and in fact the root edge `bu_y` already supplies the
contact.  Every neighbour of `A` outside `A` belongs to `W`; after
deleting `W_A`, the only model bag left is `B_y`, which is
anticomplete to `A`.  Thus `W_A` separates the displayed sets.
The symmetric argument proves the assertion for `W_D`.

Choose an inclusion-minimal subset `Z_A` of `W_A` retaining the
separation.  The graph `H` is six-connected, so `|Z_A|>=6`.
For every `z in Z_A`, minimality gives a path between the two
distinguished sets in `H-(Z_A-{z})`; the path passes through `z`
and shows that `z` has a neighbour in both distinguished components of
`H-Z_A`.  Conversely every neighbour outside either component lies in
`Z_A`.  This proves (2.4).  The same proof gives `Z_D`.

Each separator lies in four disjoint named bags, proving the surplus
counts.  If `|Z_A|=6`, put `S=Z_A union {v}`.  The components
`R_A,T_A` contain `a,b`, respectively, and hence see `v`; (2.4)
shows they are full to `S`.  Any other component `C` of `H-Z_A`
has `N_G(C) subseteq S`.  Seven-connectivity of `G` forces
`N_G(C)=S`.  This proves the last assertion.  QED.

The missing support edges

\[
                         B_xD,\quad DA,\quad AB_y
\]

form the atomic missing-`P_4`.  Theorem 2.1 is stronger than merely
recognising that quotient: it attaches a genuine four-bag separator to
each orientation of the path.

## 3. Exact operation states at an equality gate

Assume `|Z_A|=6`, abbreviate `Z=Z_A`, and let
`C_1,...,C_m` be the components of `H-Z`.  For a six-colouring `d`
of `G-e`, where `e` has an endpoint in `C_i` and both endpoints in
`C_i union Z`, define the marked state

\[
 \sigma_Z(d)=(\Pi_Z(d),P_Z(d)),\qquad
 P_Z(d)=\{z\in Z:d(z)=d(v)\}.                             \tag{3.1}
\]

The second coordinate is empty or is one block of the first.

### Theorem 3.1 (capacity--state lock at the double-root gate)

In the equality gate above the following statements hold.

1. **Component state disjointness.**  If `i ne j`, no marked state
   occurs as an edge-transition state on both `C_i` and `C_j`.
2. **Exact-trace orientation.**  Put `Pi=Pi_Z(c)`.  If `d` is
   unpinned (`P_Z(d)=emptyset`) and `Pi_Z(d)=Pi` for an edge on
   the `C_i` side, then every colour absent from `c(Z)` occurs on
   `N intersect C_i`.
3. **Private-colour gate.**  Since every `B_k` avoids colour 0,
   colour 0 is absent from `c(Z)`.  Its two neighbourhood occurrences
   `a,b` lie on the two distinguished sides, so this layer has exactly
   the double capacity allowed by item 2.  If a nonzero colour `k` is
   absent from `c(Z)`, its private root `u_k` belongs to only one
   component.  On every other component, an edge transition must either
   change `Pi` or be pinned on `Z`.
4. **Saturated equality row.**  If all five nonzero colours occur on
   `Z`, then `Pi` has block sizes `2,1,1,1,1`.  Giving `v` colour 0
   gives a proper boundary partition of `Z union {v}` with sizes
   `2,1,1,1,1,1`.  Opposite shores still cannot reuse one marked
   transition state, even though the repeated colour 0 meets the
   numerical double-capacity test exactly.

#### Proof

For item 1, suppose edges `e_i,e_j` on distinct component sides have
colourings with the same marked state.  A palette permutation aligns
the two colourings on `Z` and also aligns the two colours of `v`: when
the marked block is nonempty this is forced, and when it is empty the
boundary bijection can be extended to do it.  Use the colouring from
  `G-e_j` on the `C_i` side and the colouring from `G-e_i` on the
  opposite side.  Each restored edge lies on the side coloured by the
  other transition.  The restrictions agree on the full gate
  `Z union {v}`; moreover each transition restriction is faithful on
  every edge from `v` to the neighbourhood vertices on its own open
  side.  The result is a six-colouring of `G`, a contradiction.

For item 2, align `d` with `c` on `Z`.  Because `d(v)` is absent
from `d(Z)`, its image can be chosen as any colour absent from
`c(Z)`.  If such a colour did not occur on `N intersect C_i`, use
`c` on `C_i union Z`, the aligned transition colouring on the other
side, and that free colour on `v`.  The edge `e` is restored on the
`c` side, giving a six-colouring of `G`.  This contradiction proves
the orientation assertion.

The model bags lie in the union of colour classes `1,...,5`, so their
subset `Z` has no colour-0 vertex.  The remaining assertions are now
immediate from item 2, the exact trace on `N`, and `|Z|=6`.  QED.

### Theorem 3.2 (a simultaneous operation exposes a locked shore)

Choose two distinct components `C_i,C_j` and distinct vertices
`z_i,z_j in Z`.  Fullness supplies vertex-disjoint portal edges

\[
             e_i=z_ir_i,\quad r_i\in C_i,\qquad
             e_j=z_jr_j,\quad r_j\in C_j.                 \tag{3.2}
\]

Contract both edges, colour the proper minor, and expand the two
contraction vertices.  This gives a six-colouring `f` of
`G-{e_i,e_j}` in which both deleted pairs are monochromatic.  For at
least one of the two sides, say `e_i=pq` with colour `beta`, and for
every colour `gamma ne beta`, either

1. `p,q` are joined by a `beta/gamma` detour in
   `G-{e_i,e_j}`; or
2. their two distinct `beta/gamma` components both meet
   `Z union {v}`.

#### Proof

For an edge `e_i=pq`, call an **`i`-repair** a colouring of
`G-e_j` obtained from `f` by switches wholly in the open `C_i` side,
which restores `e_i` and leaves every colour on `Z union {v}` fixed.
Define a `j`-repair symmetrically.  An `i`-repair and a `j`-repair
would be opposite edge-transition colourings with exactly the same full
gate state, contradicting Theorem 3.1(1).  Therefore one of the two
edges, say `e_i`, admits no repair at all.

Fix any `gamma ne beta`.  If `p,q` are in one
`beta/gamma` component, a bichromatic detour gives outcome 1.  Otherwise,
suppose one endpoint component avoids `Z union {v}`.  Because components
of `H-Z` are anticomplete, that bichromatic component is wholly in the
open `C_i` side.  Switching it fixes every colour on `Z union {v}`,
makes `p,q` different, and hence is an `i`-repair of `e_i`.  This
contradicts the choice of `e_i`.  Thus both endpoint components meet the
full gate, proving outcome 2 simultaneously for every `gamma`.  QED.

The theorem gives actual Kempe geometry, not merely incompatible abstract
extension families.  It does **not** assert that the detours for different
colours are disjoint, or that a gate-reaching carrier preserves all five
old model labels.

### Corollary 3.3 (an equality gate lies beyond the six-edge boundary)

Let `S=Z union {v}`.  Under the installed, independently audited
order-seven full-shore closure theorems,

\[
 |E(\overline{G[S]})|\ge7,
 \qquad d_{\overline{G[S]}}(v)\ge2.                       \tag{3.3}
\]

#### Proof

Every component of `G-S` is full to `S`, and there are at least two.
The two distinguished components contain `a` and `b,u_y`, respectively.
Thus at least three vertices of `N` lie outside `Z`, so at most four of
the six vertices of `Z` are adjacent to `v`.  This proves the second
inequality in (3.3).

The order-seven contact theorem eliminates every boundary complement
with at most five edges.  At six edges its quotient analysis leaves only
`C_6 disjoint-union K_1`.  If there are exactly two full shores, that
last type is eliminated by the audited two-full-shore `C_6` theorem.  If
there are three shores, the explicit elementary packing uses four
alternating boundary singleton bags and three shore-derived bags to give
a `K_7` minor.  Four or more components behind a seven-cut are already
excluded by full-shore block gluing.  Hence no complement with at most
six edges survives.  QED.

The corollary is a genuine interaction between the uniform rooted-model
principle and the earlier cyclic full-shore machinery: the atomic `P_4`
does not determine the boundary graph, but it now forces the boundary
strictly beyond the completely closed six-edge layer.

### Corollary 3.4 (the equality gate is a crossed covering split)

If `G-S` has exactly two components, then the boundary has a cyclic hull
which is crossed in at least one shore.  Every such crossing extends to a
connected covering split of that shore; since `G` is `K_7`-minor-free,
its seven-label partition quotient is a bad split.  The split carries the
one-step minor-transition condition, while Theorem 3.2 independently
marks at least one of the two shores as Kempe-locked for every colour.

#### Proof

This is the routing half of the audited order-seven full-shore theorem,
applied to the exact adhesion supplied by Theorem 2.1.  Its hypotheses
hold here: `G` is seven-connected, proper-minor-minimal
non-six-colourable, `K_7`-minor-free, and the two components are full.
The theorem gives a cyclic hull crossed in one shore.  The connected
full-split extension turns the crossing into a covering bipartition; a
positive partition quotient would lift to a `K_7` model, so the quotient
must be bad.  Minor-criticality supplies the quoted transition condition.
The Kempe lock is Theorem 3.2.  QED.

No assertion is made that the shore owning the first cyclic crossing is
the same shore selected by the simultaneous-operation lock.  Proving a
common owner, or exchanging the two structures across the adhesion, is
exactly the two-shore capacity--state web problem.

### Corollary 3.5 (the only three-shore equality boundaries)

If `G-S` has three components, then `omega(G[S])<=3` and exactly one
of the following holds:

1. `chi(G[S])=3`, and every optimal boundary colouring has class sizes
   `3,2,2`; or
2. `chi(G[S])=4`, and `G[S]` is the pure Moser spindle.

#### Proof

This is the three-shore specialization of full-shore block gluing and
the support-efficient boundary-minor theorem.  Three full shores forbid a
boundary `K_4`.  We first note that every `K_4`-free graph on at most
seven vertices is four-colourable.  Otherwise take a 5-critical subgraph
`F` of order `n<=7`.  Then `delta(F)>=4`, so every component of
`overline F` is a path or cycle (`Delta(overline F)<=n-5<=2`).  Moreover
`alpha(overline F)<=3`, since `F` has no `K_4`.  A disjoint union of
paths and cycles has a clique cover of order at most its independence
number, except that one odd cycle may require one additional clique; on
at most seven vertices there cannot be two odd cycles of length at least
five.  Thus `overline F` has a clique cover of order at most four, which
is a four-colouring of `F`, a contradiction.

Consequently only the three- and four-colour rows occur.
Singleton-residual gluing fixes the `3,2,2` pattern in the three-colour
row.  In the four-colour row the seven-vertex
small-support classification leaves the Moser spindle and its one-edge
extension, and block gluing eliminates the extension.  QED.

## 4. Exact remaining dynamic gap

For every prescribed repeated nonedge and every resulting rooted
`K_5` certificate, a surviving degree-seven cell has two orientations.
In each orientation exactly one of the following occurs:

1. an order-six separator gives a full seven-adhesion, with the
   partition-changing/pinned gate and simultaneous-operation lock of
   Section 3; in the two-shore row it also gives a crossed cyclic-hull
   bad split; or
2. every such four-bag separator has order at least seven, hence has
   total portal surplus at least three inside four named bags.

This is the smallest honest residue of the present method.  To close it
one needs one new label-preserving statement:

> **`P4` portal-exchange target.**  In either the strict-surplus row or
> the locked equality row, one of the multiply hit bags can be split so
> that the detached portal side and the rooted remainder retain the old
> clique labels required by the private-bag split lemma; otherwise two
> opposite operation states realize one common colour-gluable boundary
> partition.

Static connectivity cannot prove this target: it supplies many portals
but not their placement inside a bag.  The exact new information now
available is (i) two opposed four-bag gates rather than one arbitrary
separator, (ii) disjoint marked transition states, and (iii) a locked
Kempe carrier for every colour after a simultaneous operation.  The
unproved step is precisely the conversion of those carriers into a
label-preserving split.
