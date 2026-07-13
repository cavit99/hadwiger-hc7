# Independent audit: exact-seven forced-path completion

## Verdict

**GREEN.**  The containment direction, raw-versus-residual list equality,
support calculations, critical-core reduction, and anchored-`K_4` lift are
all correct.  The crucial hypothesis is written explicitly: every raw list
is a nonempty **proper** subset of the three-colour palette, so it has order
one or two.  Consequently every two-element list surviving conflict-free
exhaustive propagation is the same exact pair in the raw carrier state.

No support lower bound is silently transferred to the propagated residual.
Instead, the proof counts raw occurrences on the vertices of a selected core
and bounds every possible additional raw occurrence by the number of the
original seven vertices outside that core.  This is the valid argument.

As an independent finite guardrail, I also examined the completed
no-anchored-`K_4` catalogues

```text
active/hc7_exact7_raw_list_no_k4_catalogue_0_20.json
active/hc7_exact7_raw_list_no_k4_catalogue_20_107.json
```

covering all 107 triangle-free atlas graphs.  They contain 150 uncolourable,
support-at-least-four raw states with no anchored `K_4`.  None has a full
list, and all 150 reach a singleton-propagation conflict; zero terminate in a
nonconflicting residual.  This agrees with the theorem, although the proof
does not depend on this catalogue.

This audit also covers the stronger authoritative draft
`hc7_exact7_forced_path_completion.md`.  Its Lemma 2.1 and Proposition 4.1
are **GREEN**.  The exact qualification is that those results provide a
forcing certificate and five local switch types; they do not yet provide a
canonical choice of certificate or a transport theorem between two switch
states.  The final paragraph after Proposition 4.1 should be read with the
precise localization stated in Section 8 below.

## 1. Exact propagation invariant

At a vertex `x` with singleton list `{q}`, every list-colouring must assign
`q` to `x`.  Deleting `x` and deleting `q` from each surviving neighbour's
list therefore preserves colourability in both directions.  If a neighbour
becomes empty, the current instance and hence the original instance is
uncolourable.  Otherwise the operation is an exact equivalence.

The graph and list system are finite, so every sequence terminates.  Fix any
exhaustive sequence that does not encounter an empty list.  Because the raw
instance is uncolourable and every step is equivalent, the final residual
`(H,L)` is uncolourable.  It has no empty or singleton list by construction.
Propagation only deletes colours, while every raw list has order at most
two.  Thus, for every residual vertex `v`,

\[
       2\le |L(v)|\le |\Lambda(v)|\le2,
       \qquad L(v)=\Lambda(v).
\]

Every residual list is therefore an exact pair, equal to the raw literal
carrier-contact pair.  This equality holds only for vertices surviving the
propagation; the proof never attributes a residual list to an already
deleted forced vertex.

The theorem's order statement is also safe.  If a selected exhaustive
sequence reaches a conflict, outcome 1 holds.  If it does not, the proof
below gives outcome 2.  It need not claim that all propagation orders have
the same syntactic outcome.

## 2. Critical-core containment direction

The promoted triangle-free critical-core theorem applies to `(H,L)` because
`H` is a triangle-free graph on at most seven vertices and every residual
list is a nonempty subset of the same three-colour palette.  Core extraction

* deletes residual vertices,
* deletes residual edges, and
* enlarges selected residual lists.

Hence, at a displayed core vertex,

\[
             L(v)\subseteq L_{\rm core}(v).
\]

If the displayed core list is a pair, the residual list is also a pair, so
the two are equal.  Section 1 then gives

\[
 L_{\rm core}(v)=L(v)=\Lambda(v).
\]

Thus every carrier incidence used at a displayed pair-list vertex is a
literal incidence in the original auxiliary graph `Q`.  If the displayed
core list is `123`, its residual and raw list is one of `12,13,23`; no full
raw contact is inferred.

Similarly, every displayed core edge is an edge retained from `H`, hence a
literal original edge of `F`.  Restoring propagation-deleted vertices,
core-deleted vertices, deleted edges, and unused incidences cannot destroy a
minor model using only retained vertices and edges.

## 3. Raw support accounting through deleted vertices

The support hypothesis belongs to the original seven raw lists.  The proof
does not claim that it survives propagation.  For a core on `m` vertices,
all vertices deleted either during propagation or during core extraction
together form exactly a subset of the `7-m` original vertices outside the
core.  Therefore an omitted colour can acquire at most `7-m` additional raw
occurrences beyond those forced on the core.

This gives the stated exclusions.

* `T1` has five vertices whose exact raw lists are one common pair.  Its
  omitted colour can occur only at the other two original vertices, so its
  raw support is at most two, not four.
* `T3` has all seven vertices with the same exact raw pair.  Its omitted
  colour has support zero.
* `T7,T8,T9` each uses all seven original vertices.  There are no propagated
  or core-deleted vertices left to contribute support.  Replacing each
  displayed full list by its actual raw pair gives respectively three,
  three, and nine possible refinements; the promoted pair-bicycle audit
  verifies that every refinement leaves some colour with support at most
  three.

The surviving core types are complete.

* `T2` has six vertices with exact raw pair lists and has the explicit
  anchored certificate.  Its one outside original vertex is not used.
* `T4,T5,T6` use all seven vertices with exact raw pair lists and have their
  explicit certificates.
* `T10` uses all seven vertices.  Its displayed full-list vertex has one of
  the three raw pair refinements, while the certificate deliberately avoids
  that vertex and works for all three refinements.

No classification template is omitted, and no invalid assumption about
propagated colour support enters this case split.

## 4. Literal anchored-`K_4` lift

For `T2,T4,T5,T6` and every `T10` refinement, the promoted pair-bicycle
theorem supplies four disjoint connected pairwise adjacent auxiliary bags.
They use exactly four distinct boundary roots, one per bag, and every root
used at a carrier incidence is a displayed pair-list vertex.  By Section 2,
that displayed pair is its exact raw list.  Every boundary edge used by the
certificate is a retained original edge.

Consequently the same four bags occur in the original auxiliary graph `Q`.
Extra vertices, edges, or raw incidences are harmless.  This proves outcome
2 for every conflict-free residual core.

The proof does not try to lift an incidence that exists only after list
enlargement.  The only displayed full-list vertex that survives the support
case split is vertex `6` of `T10`, and the explicit four bags do not use it.

## 5. Literal `HC_7` consequence

Replace each auxiliary carrier vertex `c_q` in the anchored model by the
actual connected carrier `C_q`.  Distinct auxiliary bags use disjoint
carrier vertices, so the lifted bags remain disjoint.  Auxiliary
carrier--carrier edges become literal edges between the pairwise adjacent
carriers, and auxiliary root--carrier incidences become literal edges from
the boundary root to that carrier.  Connectivity and all six adjacencies
among the four lifted bags are preserved.

Let `s_1,s_2,s_3` be the remaining three boundary vertices and
`P_1,P_2,P_3` the disjoint connected `S`-full packets in the opposite shore.
The three further bags are `P_i\cup\{s_i\}`.  The final 21 adjacencies are

| Pairs | Count | Literal witness |
|---|---:|---|
| among the four anchored bags | 6 | the lifted anchored `K_4` |
| packet bags to anchored bags | 12 | packet fullness at the four anchored roots |
| among packet bags | 3 | packet fullness at the other packets' anchors |

Thus outcome 2 gives a literal `K_7` minor.  In a hypothetical exact-seven
counterexample, a support-at-least-four raw state without a full list must
therefore reach a singleton-propagation conflict.  Combining this with the
promoted full-list completion correctly covers every canonical crossed-chain
state.

## 6. Trust boundary

The theorem turns every **nonconflicting** singleton-propagation residue into
a literal minor.  It does not turn a propagation conflict itself into a
minor or a six-colouring.  Nor does it say that residual supports remain at
least four, that propagation is monotone along the block-chain sweep, or
that two different raw states have compatible forced-colour chains.  The
remaining work is exactly the transport or destruction of those literal
conflict certificates.

## 7. Audit of the stronger forcing-digraph certificate

The forcing digraph in Section 2 of
`hc7_exact7_forced_path_completion.md` is the exact implication closure of
singleton propagation for raw lists of order at most two.

For a boundary edge `uv` and common colour `q`, if `v` has raw pair
`{q,r}`, forcing `u=q` deletes `q` at `v` and forces `v=r`.  This is exactly
the arc

\[
                         (u,q)\longrightarrow(v,r).
\]

If `v` has raw singleton `{q}`, the same forced assignment empties `v`'s
list, exactly as represented by `(u,q)\to\bot`.  The symmetric arcs cover
the reverse orientation of the boundary edge.  Every raw singleton has its
own source, so every initial forced assignment is represented.

### Forward direction

A path from a singleton source to `bot` is a chain of valid forced
assignments ending by emptying a raw singleton.  If sources reach both
`(v,a)` and `(v,b)` for a raw pair `Lambda(v)={a,b}`, implication closure
forces both incompatible assignments at `v`; operationally the two chains
delete both colours from that list, possibly with the conflict detected at
an earlier equivalent point depending on processing order.  Either directed
configuration therefore forces a propagation conflict.

Shared vertices, repeated portions, or coincident sources do not invalidate
the argument: reachability is the forward closure of the unit implications,
not a demand for vertex-disjoint paths.

### Converse direction

Consider the first empty list in an exhaustive propagation sequence.  A raw
singleton becomes empty after a neighbour is forced to its sole colour.
Tracing that neighbour's forced assignment backward gives a path from an
initial singleton source, followed by the corresponding arc to `bot`.

A raw pair becomes empty only after its two colours have both been removed.
If the pair is `{a,b}`, the assignment which removes `a` gives the implication
to `(v,b)`, and the assignment which removes `b` gives the implication to
`(v,a)`.  Trace both causing assignments backward.  Every noninitial forced
assignment at a raw pair has a temporally earlier predecessor across the
edge which removed its alternative; finiteness therefore ends each trace at
a raw singleton source.  This produces the two paths in Lemma 2.1.

Thus Lemma 2.1 is an if-and-only-if certificate.  The word “canonical” can
refer safely to the certificate *type*.  The actual paths need not be unique,
and the lemma does not select a canonical representative among them.

## 8. Audit of the five cut-switch types

At a canonical crossed cut, remove the cutvertex `z` from both alternative
carrier allocations and let `M(s)` record all remaining literal carrier
contacts.  For `Z=N_S(z)`, assigning `z` left adds only outer colour `j`,
while assigning it right adds only outer colour `k`.  Hence

\[
 \Lambda^{\rm L}(s)=M(s)\cup\{j\},\qquad
 \Lambda^{\rm R}(s)=M(s)\cup\{k\}
\]

for `s in Z`, and the two raw lists agree outside `Z`.  This is a literal
carrier statement: it does not propagate colours or identify a palette
symbol with an old model bag.

Both allocations are spanning three-carrier clique partitions.  In a
target-free exact-seven survivor their raw lists are nonempty, each palette
colour has support at least four, and no list is full by the promoted
full-list completion.  Under precisely these hypotheses, the enumeration in
Proposition 4.1 is exhaustive.

* If `i in M(s)`, membership of `j` would make the right list full and
  membership of `k` would make the left list full.  Therefore `M(s)={i}` and
  the switch is `(ij,ik)`.
* If `i notin M(s)`, the four possibilities
  `M(s)=emptyset,{j},{k},{j,k}` give respectively

\[
              (j,k),\quad(j,jk),\quad(jk,k),\quad(jk,jk).
\]

The three excluded subsets `{i,j},{i,k},{i,j,k}` produce a full list in at
least one allocation.  Hence there are exactly the five displayed switch
types, and the first occurs exactly when `i in M(s)`.

The exact forcing-digraph localization is the following.  A cut switch
changes raw lists only at vertices of `Z`; consequently it changes only

1. assignment nodes and singleton sources based at vertices of `Z`;
2. implication arcs incident with such assignment nodes; and
3. arcs to `bot` whose existence is caused by a switched singleton at a
   vertex of `Z`.

Any **fixed** directed certificate using none of these changed objects
persists verbatim.  Nothing proved so far selects one certificate canonically
when several exist.  Moreover, a changed arc `(u,q)\to\bot` caused by a
singleton at `z in Z` has its only assignment-literal endpoint at the
possibly outside vertex `u`.  Thus the informal sentence “the first changed
literal lies in `Z`” is not literally justified for an arbitrary chosen
certificate without either augmenting certificates by the singleton which
causes each `bot` arc or proving a reselection lemma.

This is not a flaw in Proposition 4.1 or Lemma 2.1, and Section 5 of the
forced-path draft correctly leaves the transport theorem open.  It is the
trust boundary for the next step: five local list types do not by themselves
show that a forced unit bicycle persists, reverses, or yields a fixed
two-vertex endgame.

## 9. Verdict on the stronger forced-path draft

Theorem 1.1, Lemma 2.1, the literal `HC_7` consequence through forced
certificate existence, and Proposition 4.1 are all **GREEN**.  The stronger
draft rigorously reduces every target-free crossed-chain allocation to one
of the two finite forcing-certificate types and rigorously describes every
local list switch by one of five ordered pairs.

It does not yet prove forced-bicycle transport.  In particular, the existence
of a certificate in each allocation does not identify the certificates,
order their first divergence, or give a common pair of literal vertices.
Those statements require the separately named operation-state lemma.
