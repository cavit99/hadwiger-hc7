# Adversarial audit of the double-root `P4` capacity/state note

## 1. Executive verdict

The new separator and state machinery is mathematically sound.  In
particular, I found no counterexample to Theorems 2.0, 2.1, 3.1, or 3.2
after reconstructing the separators and the two splicings from first
principles.

There are two mandatory presentation repairs.

1. Theorem 2.0 uses **terminal-meeting** without defining it.  The proof is
   valid if this means that every branch bag meets
   `T={a,b,u_1,...,u_m}` (not that every terminal must be used).  If the
   stronger convention that the union of the bags must contain all of `T`
   is intended, the proof needs the short absorption argument in Section 2
   below.
2. Corollary 3.5 does not prove that a `K_4`-free graph on seven vertices
   has chromatic number at most four.  Its displayed dichotomy omits that
   step.  The conclusion is true; Section 7 supplies a self-contained
   repair.

The equality-gate corollaries also inherit substantial external or
computer-assisted dependencies.  They are valid conditional on the exact
installed theorems cited below, but should not be described as consequences
of Theorems 3.1--3.2 alone.

The verdicts are:

| Result | Verdict |
|---|---|
| Theorem 2.0 | **GREEN after terminology repair** |
| Theorem 2.1 | **GREEN** |
| Theorem 3.1 | **GREEN** |
| Theorem 3.2 | **GREEN** |
| Corollary 3.3 | **GREEN, computer-assisted/structural dependencies explicit** |
| Corollary 3.4 | **GREEN, computer-assisted/structural dependencies explicit** |
| Corollary 3.5 | **RED as proved; GREEN after the repair in Section 7** |
| Section 4 residue dichotomy | **GREEN; the portal-exchange target remains unproved** |

No result in the note proves `HC_7`.

## 2. Theorem 2.0: uniform double-root gate

### Separator construction

Put `W=union_i B_i`.  If no reserved connector exists, `a,b` lie in
different components `A,D` of `H-W`.  Direct root adjacency gives

\[
                       I_A\cup I_D=[m].
\]

If `I_A=[m]`, then `A,B_1,...,B_m` are a `K_{m+1}`-model and every bag
meets `T={a,b,u_1,...,u_m}`.  Thus the proof is complete under the weak,
degree-seven-relevant definition of terminal-meeting.

Under the stronger definition requiring the model union to contain every
terminal, absorb `D` into a bag it contacts.  Such a contact exists because
`H` is connected.  If `D` contacts `B_j`, replace `B_j` by `B_j union D`.
The old clique adjacencies survive, the new bag contains `b`, and `A`
contains `a`.  Hence `I_A=[m]` is forbidden under this convention as well.
The same argument applies to `I_D`.

Two proper sets covering `[m]` have nonempty opposite differences.  For
`y in I_D-I_A`, deleting

\[
                       W_A=\bigcup_{i\ne y}B_i
\]

separates the connected set `A` from the connected set `D union B_y`.
An inclusion-minimal subseparator `Z_A` has order at least `k`.  For every
`z in Z_A`, minimality supplies an `A`--`(D union B_y)` path in
`H-(Z_A-{z})`; its two segments at `z` prove that `z` has a neighbour in
both distinguished components of `H-Z_A`.  Thus both sides are full to
`Z_A`.  The symmetric construction is identical.

Define the portal surplus explicitly by

\[
 \operatorname{sur}(Z_A)=|Z_A|-|\{i\ne y:Z_A\cap B_i\ne\varnothing\}|.
\]

Then

\[
 \operatorname{sur}(Z_A)\ge k-(m-1)=k-m+1.
\]

This removes the second minor ambiguity in the statement: empty named
bags do not contribute negative surplus.

### Verdict

**GREEN after defining terminal-meeting and portal surplus.**

## 3. Theorem 2.1: the degree-seven oriented adhesions

Every use of the counterexample hypotheses is legitimate:

* Mader's theorem gives seven-connectivity of `G`, hence six-connectivity
  of `H=G-v`.
* Dirac's inequality gives `alpha(G[N(v)])<=2`; hence, for every unique
  root `u_i`, at least one of `au_i,bu_i` is an edge.
* A reserved connector would give an `N(v)`-meeting `K_6` in `H` and then
  a `K_7` with the singleton `{v}`.

For `y in I_D-I_A`, `A` is anticomplete to both `D` and `B_y`, while
`D union B_y` is connected.  The four-bag separator and its fullness
therefore follow exactly as in Theorem 2.0.  If its order is six, put
`S=Z_A union {v}`.  There are already two components of `G-S`.  Every
component `C` of `G-S` has `N_G(C) subseteq S`; seven-connectivity forces
`N_G(C)=S`.  Thus the assertion that **all**, not only the two
distinguished, components are full is correct.

The strict row also has the advertised capacity: a separator of order at
least seven in four named bags has surplus at least three.

### Verdict

**GREEN.**

## 4. Theorem 3.1: crossed state splicing

Let `S=Z union {v}`.  The components of `G-S` are exactly the components
`C_i` of `H-Z`, and are pairwise anticomplete.

### Item 1

Suppose `d_i` colours `G-e_i`, `d_j` colours `G-e_j`, and they induce
the same marked state on `Z`.  A palette permutation makes them agree
pointwise on `Z` and on `v`:

* if the marked block is nonempty, the colour of `v` is forced by that
  block;
* if it is empty, the bijection on the colours used by `Z` extends to a
  bijection sending `d_i(v)` to `d_j(v)`.

Now use `d_j` on `C_i`, and use `d_i` on every other component, retaining
their common restriction on `S`.  The edge `e_i` is present and properly
coloured in `d_j`; `e_j` is present and properly coloured in `d_i`.
There are no edges between open components, and every edge to `S` is
coloured by one of the two original colourings.  This is a six-colouring
of `G`, a contradiction.

This direct formulation is preferable to the source proof's phrase about
a transition being "faithful on its own open side", because the actual
construction deliberately uses the *opposite* transition on the side of
each restored edge.

### Item 2

Align an unpinned transition `d` with the exact trace colouring `c` on
`Z`.  Because `d(v)` is absent from `d(Z)`, the unused-colour part of the
palette permutation can send `d(v)` to any prescribed colour `gamma`
absent from `c(Z)`.  If `gamma` were absent from `N(v) intersect C_i`,
use `c` on `C_i`, the aligned transition on every other open component,
and colour `v` with `gamma`.  The operated edge is restored on the `c`
side.  Edges from `v` to `C_i`, to `Z`, and to the other components are
all proper.  This would colour `G`, proving the orientation assertion.

Items 3 and 4 then follow from the exact trace: colour 0 occurs on
`N(v)` exactly at `a,b`, every nonzero colour occurs there at its unique
root, and `Z` lies in the union of the five nonzero colour classes.

### Verdict

**GREEN.**

## 5. Theorem 3.2: simultaneous operation and Kempe lock

The two portal edges are vertex-disjoint because their boundary endpoints
are distinct and their interior endpoints lie in different components.
Contracting both therefore gives a proper minor.  Expanding a six-colouring
gives a colouring `f` of `G-{e_i,e_j}` in which the ends of each deleted
edge agree.

An `i`-repair is a colouring of `G-e_j`; hence it is a transition for the
edge `e_j` on the `C_j` side.  A `j`-repair is symmetrically a transition
for `e_i` on `C_i`.  Since both repairs leave `S` pointwise fixed, their
simultaneous existence would contradict Theorem 3.1(1).  Thus one edge,
say `e_i=z_ir_i`, has no repair.

For a colour `gamma` different from the common endpoint colour `beta`,
either the two ends lie in one `beta/gamma` component, which gives the
stated detour, or they lie in different components.  The component of
`z_i` already meets `S`.  If the component of `r_i` avoided `S`, it would
be wholly contained in `C_i`; switching it would fix `S`, separate the
endpoint colours, and repair `e_i`.  Hence it too meets `S`.

The conclusion is correct, but its strength should not be overstated:
one of the two gate contacts in alternative 2 is automatic because
`z_i in Z`.  The new content is that the *interior endpoint's* component
also reaches the gate for every colour for which there is no detour.  No
disjointness or named-bag preservation follows.

### Verdict

**GREEN.**

## 6. Corollaries 3.3 and 3.4

### Corollary 3.3

The elementary part is correct.  The three distinct vertices
`a,b,u_y` lie outside `Z`, so at most four vertices of `Z` are neighbours
of `v`; hence `d_{overline{G[S]}}(v)>=2`.

The missing-edge bound uses the following exact dependency chain:

1. Theorem 13.1 of `hadwiger_contact_order7_threeedge_closure.md` excludes
   at most five missing boundary edges.
2. Theorem 14.1 of that note reduces the six-edge layer to
   `C_6 disjoint-union K_1`.  This theorem uses the finite six-edge atlas,
   generalized Two Paths/web closures, exact-block nonsplitness, and the
   `K_{3,3} join K_1` two-piece closure.
3. With exactly two shores, the computer-assisted theorem audited in
   `hadwiger_c6_closure_dependency_audit_2026-07-12.md` excludes that
   final type.  Its Dirac/criticality hypothesis is available here.
4. With three shores, `G[S]` contains a `K_4`: use the complement-isolated
   vertex and one alternating triple of the `C_6`.  Three full shores plus
   those four singleton boundary bags give a `K_7` model.
5. Four or more shores are excluded by the audited full-shore block-gluing
   and multicomponent theorems.

There is a small scope point hidden in item 2: several unbounded web
closures are stated for exactly two shores.  This causes no lost
three-shore case.  I independently added a third universal, mutually
nonadjacent helper to each of the twelve two-helper-negative six-edge
quotient types listed in `hadwiger_six_edge_web_closures.md` and ran the
complete seven-bag partition checker from
`exact7_multicomponent_quotient_atlas.py`.  All twelve are `K_7`-positive.
Thus a six-edge survivor which needs a two-shore web closure necessarily
has exactly two shores; a third shore already closes its quotient.

The order-seven contact theorem is applicable here even though this cut
was obtained from the double-root gate rather than the original contact
model: its closure proofs use only minor-criticality, seven-connectivity,
`K_7`-minor-freeness, two full distinguished shores, and
`eta(G[S])<=5`.  The first four properties hold by construction; the last
follows because a `K_6`-model in `G[S]` plus any full shore would give a
`K_7`.

**Verdict: GREEN with computer-assisted/structural dependencies stated.**

### Corollary 3.4

Theorem 4.1 of `hadwiger_full_split_cyclic_hull.md` applies exactly to a
seven-cut with two full components in a seven-connected,
six-minor-critical, `K_7`-minor-free graph.  It supplies a cyclic hull and
a crossing.  Lemma 1.1 of that note extends the crossing to a connected
covering split, and `K_7`-minor-freeness makes its quotient a bad split.

The one-step state assertion should cite Lemma 1.2 of
`hadwiger_degree9_lobe_equality_transition.md`: for any label-preserving
operation in one shore, the operated-shore state is accepted by every
unchanged shore and rejected by the original operated shore.  This remains
valid for an operation internal to either member of the connected split,
because it is still an operation internal to the original shore.

This corollary depends on the cyclic-hull matrix certificate, the
generalized Two Paths theorem, exact-block nonsplitness, and the exceptional
`K_{3,3} join K_1` closure.

**Verdict: GREEN with the transition citation repaired and dependencies
stated.**

## 7. Corollary 3.5: three-shore classification

The proof as written establishes

\[
                    \chi(G[S])\ge3,\qquad \omega(G[S])\le3,
\]

and correctly handles the cases `chi=3` and `chi=4`.  It does not exclude
`chi>=5`.  The following elementary lemma repairs the gap.

### Lemma 7.1

Every `K_4`-free graph on at most seven vertices is four-colourable.

#### Proof

Otherwise it contains a subgraph `F` minimal subject to not being
four-colourable.  Then `F` is 5-critical, so `delta(F)>=4`, and
`n=|F|<=7`.  In the complement `Q=overline F` we have

\[
                         \Delta(Q)\le n-5\le2.
\]

As `F` is `K_4`-free, `alpha(Q)<=3`.  Every component of `Q` is a path or
cycle.  Such a graph has a clique cover of order at most `alpha(Q)`, except
that an odd cycle of length at least five costs one additional clique.
There cannot be two such cycles on at most seven vertices.  Consequently
`Q` has a clique cover of order at most four.  That clique cover is a
four-colouring of `F`, a contradiction.  QED.

Thus a surviving three-shore boundary has chromatic number three or four.
In the three-colour row, Theorem 1.2 of
`hadwiger_full_shore_block_gluing.md` forbids a singleton class; the class
sizes are therefore `3,2,2`.

In the four-colour row, the support-efficient theorem rules out a
`K_4`-model supported on at most five boundary vertices.  The exact atlas
check gives precisely two seven-vertex graphs with `alpha<=2` and no such
model: the Moser spindle and its one-edge extension.  I independently
replayed this check with NetworkX's 1,044 seven-vertex atlas graphs and the
exact four-/five-vertex branch-set test in
`exact7_multicomponent_quotient_atlas.py`: among 107 graphs with
`alpha<=2`, exactly two survive, with 11 and 12 edges.  The five-block
partition

\[
                    25\mid46\mid0\mid1\mid3
\]

and clique-residual block gluing eliminate the extension.  Hence the pure
Moser spindle is the only four-colour row.

### Verdict

**RED as currently proved; GREEN after inserting Lemma 7.1 (and retaining
the atlas certificate as an explicit computer-assisted dependency).**

## 8. Section 4 and the exact remaining gap

For each orientation, either an order-six four-bag separator exists or all
such separators have order at least seven.  If an order-six separator
exists, an inclusion-minimal subset is still a separator and
six-connectivity forces it to retain order six.  Otherwise every separator
has order at least seven and surplus at least three.  Thus the dichotomy is
exhaustive.

The `P4` portal-exchange statement is explicitly a target, not a theorem.
Nothing in Theorems 3.1--3.2 converts the gate-reaching Kempe components
into a split that preserves all five model labels.  In particular,
Theorem 3.2 supplies neither simultaneous disjoint carriers nor a common
owner with the cyclic crossing of Corollary 3.4.

**Verdict: the residue description is GREEN; the stated portal-exchange
target remains the exact unproved step.**
