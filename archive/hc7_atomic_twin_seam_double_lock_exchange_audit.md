# Adversarial audit: atomic twin-seam double-lock target

## Verdict

**GREEN as a precise theorem statement; OPEN as a theorem.**  The original
version was RED because its third outcome merely asked for a “declared
nonreversible rank.”  That undefined outcome is no longer in the audited
source.  The current target fixes one certificate class,
`mathcal F_12(G)`, one rank `rho(L,S,R)=|L|`, a globally minimum source,
and a receiver in the same class with strictly smaller rank.  The three
outcomes are therefore literal and independently checkable.

The new common edge-deletion and double-contraction inputs are also
correctly cited and used.  They place both named operations in one
connected six-chromatic host with a spanning `K_6` model, prove the two
opposite one-restoration signatures, and supply a simultaneous
`(equal,equal)` colouring.  In that shared colouring one named edge has at
least three bichromatic locks, or at least four when the equality colours
differ; separately, each named edge has four common-host locks in its own
one-restoration response.  These conclusions do not allocate the four
endpoints, lock paths or either exact twin state to model rows.
Consequently the repaired target still does **not** follow from the
current audited inputs.

**Audited source:**
[`hc7_atomic_twin_seam_double_lock_exchange_goal.md`](hc7_atomic_twin_seam_double_lock_exchange_goal.md).

**Source SHA-256:**
`4b4e25c21ab5a93fbda378f62b841e741db600d354892cb3a03ff2a6d180ff8d`.

This audit does not exhibit a graph satisfying the full hypothetical
counterexample kernel and avoiding all three outcomes.  Such a graph would
be an `HC_7` counterexample, not a local falsifier.

## 1. Literal hypothesis package

The target now includes the data needed to interpret every outcome.

1. `G` is seven-connected, strongly seven-contraction-critical and
   `K_7`-minor-free, with the connected-bipartite atomic separation,
   unique edge `e=zu`, two old full packets and the twin-seam decomposition.
2. The old separation is explicitly oriented as

   \[
       (A,S,R)\in\mathcal F_{12}(G),
       \qquad (\nu_A^S,\nu_R^S)=(1,2).               \tag{1.1}
   \]

3. The order of `A` is minimum among the packet-one shores of **all**
   members of `mathcal F_12(G)`, not merely among paired, bipartite or
   twin-seam representatives.
4. The named operations are the contractions of the vertex-disjoint edges

   \[
                            e=zu,\qquad f=dt,          \tag{1.2}
   \]

   with literal labels and legal six-colour responses.
5. The twin boundaries are the actual seven-sets

   \[
      \Omega_D=K\mathbin{\dot\cup}A_0,
      \qquad
      \Omega_E=K\mathbin{\dot\cup}B_0,               \tag{1.3}
   \]

   where `|K|=5` and both exclusive sets have order two.

The packet-transfer theorem either closes a `(1,3)` twin, returns a strict
lobe-oriented `(1,2)` cell, or reduces the genuinely local residue to
simultaneous `(1,1)/(1,1)`.  Under the global choice in item 3, the strict
lobe cell is already impossible.  Thus the double-lock decoder may be
studied in the `(1,1)/(1,1)` residue without treating an unranked `(1,1)`
receiver as an outcome.

There remains an upstream qualification, which the source states
correctly: choosing a global minimum does not itself prove that this member
has the paired, connected-bipartite and twin-seam normal form.  Every
normalization used before this target must preserve the globally selected
`A` or return an even smaller member of the same family.

## 2. The global rank repair

The cited global thin-shore theorem defines `mathcal F_12(G)` as the set of
all actual decompositions

\[
        V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
        \qquad |S|=7,
        \qquad (\nu_L^S,\nu_R^S)=(1,2),               \tag{2.1}
\]

with nonempty anticomplete open shores.  Since `G` is finite, this family
is finite.  Its intrinsic orientation makes

\[
                           \rho(L,S,R)=|L|             \tag{2.2}
\]

a fixed well-founded rank.

Outcome 3 of the repaired target requires an actual receiver

\[
       (L',S',R')\in\mathcal F_{12}(G),
       \qquad |L'|<|A|.                               \tag{2.3}
\]

Thus source and receiver lie in one fixed domain and (2.3) is a literal
strict decrease.  At the globally minimum source it is contradictory.  No
relation between the old and new equality partitions is needed because
membership in `mathcal F_12(G)` is state-free.

The exclusions in the target are essential and correct.  The rank does
not apply to:

* a `(1,1)` receiver;
* a reversed cell whose smaller lobe is packet-two;
* lower bounds on packet numbers without an exact `(1,2)` vector;
* a boundary of order other than seven;
* a near-model rotation; or
* a representative-local portal, bag or centre order.

Section 2 now states the rank boundary accurately: no noncycling rank is
claimed for an unranked `(1,1)` receiver or a near-model rotation, while
the only rank used by the target is the global `mathcal F_12(G)`
shore-order rank.  This agrees with the formal outcome in Section 3 and
removes the prior linguistic ambiguity.

## 3. Common edge-deletion `K_6` fork and lock allocation

The link to
`../results/hc7_common_edge_deletion_k6_fork.md` is valid, and the claims
drawn from it are exact.

In the twin seam the four endpoints `z,u,d,t` are distinct, and the two
named edges are vertex-disjoint.  Moreover `z in E` and `d in D`, where
`D,E` are distinct components of `A-Z`, so the cross-edge `zd` is absent.
Put

\[
                         H=G-\{e,f\},                  \tag{3.1}
\]

where the braces denote deletion of the two edges.  Seven-connectivity
implies edge-connectivity at least seven, so deleting two edges leaves `H`
connected.

The audited chromatic fork gives

\[
                         \chi(H)=6.                    \tag{3.2}
\]

Indeed, if `chi(H)=5`, the one-spare-colour lemma would make the four
endpoints a literal `K_4`, contradicting the absent cross-edge `zd`.
Known `HC_6` then gives a `K_6` minor in `H`, and connectedness permits
unused components to be absorbed until its six bags span `H`.

The one-edge restorations have the exact chromatic equalities

\[
 \chi(H)=\chi(H+e)=\chi(H+f)=6,
 \qquad \chi(H+e+f)=7.                                \tag{3.3}
\]

Consequently every six-colouring of `H+e` restricts on `H` to the signature

\[
                         (e,f)=(\mathrm{proper},\mathrm{equal}),
\]

and every six-colouring of `H+f` gives

\[
                         (e,f)=(\mathrm{equal},\mathrm{proper}).
\]

Both signatures occur, while `(proper,proper)` is impossible.  The common
edge-deletion fork alone does not establish `(equal,equal)`; the legal
double contraction audited below does.  Identifying the equal pair makes
the two one-restoration colourings legal `G/f` and `G/e` contraction
responses respectively.

This is a genuine common-host coupling.  It does **not** prove:

* which model rows contain the four endpoints;
* that a multiply hit row has a duty-preserving split;
* that either response colouring is constant or prescribed on a row;
* that the two responses induce one common exact twin partition; or
* that a fixed pair or smaller `mathcal F_12(G)` receiver exists.

The source accurately calls the common model and signatures an allocation
substrate, not a completed decoder.

The additional link to
`../results/hc7_common_host_double_contraction_lock_allocation.md` is also
valid.  Since `e,f` are vertex-disjoint, `G/e/f` is a proper minor.  A
six-colouring of that minor expands to an `(equal,equal)` colouring of
`H`.  The audited whole-component switching argument then gives exactly
the advertised alternatives:

* if the two equality colours coincide, the five alternate colours each
  lock at least one named pair, so one pair receives at least three lock
  incidences;
* if the equality colours differ, the distinct-palette switching argument
  gives one named pair at least four lock incidences; and
* in a colouring of either one-edge restoration, the still-equal pair is
  locked in all five alternate palettes before the restored edge is
  deleted, and deleting that edge can destroy at most one such lock.
  Hence at least four literal locks remain in `H`, symmetrically for each
  named pair in its own response colouring.

The last two four-lock systems may come from unrelated colourings.  Lock
paths of different palettes need not be internally disjoint, and palette
colours are not boundary duties or model-row labels.  Thus the source's
three-/four-lock claims are exact, including their stated limitations.

## 4. Audit of the three target outcomes

### 4.1 Common state

If two explicitly named complementary-side responses induce the same exact
partition on `Omega_D` or `Omega_E`, a palette permutation makes their
literal boundary colourings agree.  The relevant missing edge lies wholly
on the opposite intact side in each response, and the two open shores are
anticomplete.  The standard palette-alignment gluing therefore six-colours
`G`.  This outcome is precise.

### 4.2 Terminal model

A displayed literal `K_7` model contradicts the kernel directly.  A pair
`{a,b}` with `G-{a,b}` `K_5`-minor-free is also a valid terminal.  In a
seven-critical graph,

\[
                         \chi(G-\{a,b\})\ge5:          \tag{4.1}
\]

a four-colouring could be extended by assigning two fresh colours to
`a,b`, six-colouring `G`.  Known `HC_5` then forces a `K_5` minor in
`G-{a,b}`, contradicting the proposed fixed pair.

### 4.3 Strict receiver

Outcome 3 is exactly (2.3), with the literal boundary map and exact packet
vector recorded.  Global minimality makes it contradictory.  An unranked
`(1,1)` cell, a high-demand state without a verified packet vector, or a
near-model rotation is explicitly not accepted.  This outcome is now a
mathematical predicate, unlike the original “declared rank” wording.

Thus, if the repaired target theorem were proved under its frozen input,
each of its outcomes would close that twin seam.

## 5. Why the current inputs do not prove the target

The repair validates the **destination** of a transition; it does not
manufacture one.

1. The crossed-state theorem proves disagreement and four demand
   inequalities, not an exclusive `A_0`/`B_0` trace or a common state.
2. The two mismatch paths may coincide.  The audited excursion accounting
   can instead yield a final rich connector, a closed two-portal excursion,
   or a singleton boundary detour.  None duplicates all five common
   `K`-duties.
3. The response bundle gives several literal paths or a common palette
   gate with mixed escape channels.  Palette colours are not boundary or
   model-row labels.
4. The bridge-square is an exact involution, so it supplies no descent.
5. Third responses and endpoint saturation add named proper-minor states,
   but no theorem assigns an exclusive duty or preserves five foreign-row
   adjacencies through a split.
6. The common spanning `K_6` model is unrooted relative to the response
   signatures.  Opposite values of the two edge bits do not determine a
   row split or a twin-boundary equality partition.
7. The new three-/four-lock allocation counts palette incidences.  It
   neither makes the lock paths internally disjoint nor assigns their
   endpoints to the six model rows or the seven boundary duties.
8. The global `mathcal F_12(G)` rank rejects a smaller receiver once one is
   displayed; it supplies no separator, packet vector or boundary map from
   the lock geometry.

The existing finite state/path barriers remain relevant to this logical
nonimplication: exact response mismatches can stay wholly inside `K`, and
all lock layers can pass through one unlabelled palette gate.  Those are
mechanism barriers, not realizations of the full counterexample kernel.

## 6. Exact remaining theorem-strength gap

For a globally minimum member of `mathcal F_12(G)` which has reached the
simultaneous `(1,1)/(1,1)` twin seam, prove one literal allocation:

* reproduce an exact state on complementary closed sides;
* split or reselect the common-host `K_6` model while retaining all five
  foreign-row duties, producing `K_7`;
* identify one fixed pair meeting every `K_5` model; or
* construct an actual smaller member of `mathcal F_12(G)`.

The common-host and lock-allocation theorems remove the need to construct
separate unrooted models or a simultaneous equality colouring for the two
responses, but the palette-to-labelled-carrier gap is unchanged.  The
repaired goal is therefore a sound, sharply stated open allocation
theorem—not an established consequence of the current spine.
