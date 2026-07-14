# Independent audit: common-exit three-gate closure

## Verdict: GREEN

The theorem
`hc7_exact7_common_exit_gate_closure.md` and its verifier
`hc7_exact7_common_exit_quotient_verify.py` are correct after the
audit-time repairs recorded below.  I found no remaining mathematical,
enumerative, encoding, or lifting defect.

The result proved is exactly the advertised local result: in the
minimal-`HC_7` counterexample kernel, a common-exit three-gate with at least
two sibling lobes closes by a literal `K_7` minor, except that the
three-sibling equal-support branch may equivalently close through the audited
`(1,3)` adaptive reflection.  Combined with the audited exit-matching theorem,
only the separate one-sibling gate remains.

## Audit-time repairs already incorporated

Two precision defects were found during this audit and repaired in the frozen
candidate before this verdict.

1. The first draft imported only the state-free exit-matching setup before
   invoking packet reflection.  That setup alone does not supply proper-minor
   six-colourability.  Section 1 now explicitly assumes the hypothetical
   minimal-`HC_7` kernel: `K_7`-minor-freeness, `chi(G)=7`, and six-colourability
   of every proper minor.
2. The first draft described the verifier as Z3-driven and counted the
   three-sibling census as an essential dependency.  The frozen architecture
   is now stated accurately: the default proof check is solver-free and
   replays a frozen literal catalogue; Z3 is used only by optional
   `--regenerate`; and only the `11,520+13,824` two-sibling cases are essential
   to the proof as written.  The `10,240` three-sibling replay is a redundant
   guardrail for the hand proof.

The candidate now also displays the exact `11,520` count breakdown.  No
further correction is required.

## 1. Normalized hypotheses

The hypotheses imported from the two cited audited results match the uses in
the candidate.

- The exit-matching theorem supplies an actual order-seven separation
  `L dotcup S dotcup R`, the connected `S`-full packet `P subseteq L`, the
  component `C` of `G[R]`, the connected `S`-full packet
  `Q subseteq R-C`, a three-connected `C`, a three-cut `X`, and a component
  `K` of `C-X` with `|N_S(K)|=4` and complete literal contact from `K` to `X`.
- Its common-exit outcome has at least two siblings, makes every sibling
  non-self-full, and gives one common literal `t in S-N_S(K)` as the entire
  exit set of every sibling.
- The attained binary-duty result supplies the exact partition

  \[
  \{\{a_1,t_1\},\{a_2,t_2\},\{a_3,t_3\},\{c\}\},
  \]

  independence of each pair, a literal edge between every two pairs, a
  literal `c`-neighbour in each pair, and the dutyless support

  \[
  N_S(K)=A=\{c,a_1,a_2,a_3\}.
  \]

- Relabelling the duties so that the common exit is `t=t_1` is legitimate.
  The other two complementary literals are `u=t_2` and `v=t_3`.

There is no hidden contact assumption.  Since `C` is a component of the old
open shore, `N_G(C) subseteq S`; this neighbourhood separates nonempty `C`
from nonempty `L`.  Seven-connectivity and `|S|=7` force `N_G(C)=S`, so `C`
is literally `S`-full.  Neither `K` nor a sibling contacts `u` or `v`:
`K` has support `A`, and every sibling's support outside `A` is exactly
`{t}`.  As

\[
C=X\mathbin{\dot\cup}\bigcup\{J:J\text{ is a component of }C-X\},
\]

the required contacts of `u,v` with `C` must occur in `X`.  They may occur at
the same gate vertex, which both the statement and verifier allow.

## 2. Exact sibling support

For a sibling `J`, the audited exit theorem gives `|N_S(J)|>=4`.  Common exit
puts its entire support inside the five-set `A union {t}`, and non-self-fullness
makes it omit at least one member of the four-set `A`.  Omitting two members
would leave at most three available support vertices.  Thus it omits exactly
one label `a(J) in A` and uses every other available contact:

\[
N_S(J)=\{t\}\cup(A-\{a(J)\}).
\]

The missing label is unique.  This proves Lemma 2.1 exactly; no equality is
being inferred merely from a lower bound without using the five-vertex
support cap.

## 3. Human three-sibling proof

### Three equal missing labels

For common missing label `a`, put

\[
\Omega_a=X\cup\{t\}\cup(A-\{a\}).
\]

For a selected sibling `J_a^0`, componenthood of `C-X`, componenthood of `C`
in the old shore, full gate contact, and the exact support formula give the
literal equality `N_G(J_a^0)=Omega_a`.  Hence it is one full shore of an
actual seven-separation.

The other two selected siblings are disjoint `Omega_a`-full packets.  The
third packet

\[
P\cup\{a\}\cup K
\]

is connected by the literal `a-P` and `a-K` edges, is disjoint from those
siblings, meets `A-{a}` and `t` through `P`, and meets all of `X` through
`K`.  Thus the opposite shore has three disjoint full packets.  The exact
packet theorem makes the vector `(1,3)`, and the now-explicit minimal-kernel
hypothesis permits the audited adaptive reflection theorem to close it.

### Three distinct missing labels

For distinct `alpha,beta,gamma in A` and remaining label `r`, the seven bags
displayed in the candidate are nonempty, disjoint, and connected.  Their
seven boundary anchors are exactly

\[
u,v,\alpha,\beta,\gamma,t,r.
\]

The two packet bags see one another and every anchored bag by fullness.
Among the other five bags the ten adjacencies are witnessed, in order, by

- `K-beta`, `K-gamma`, `alpha-J_gamma`, and `K-r` from the `K` bag;
- `J_alpha-gamma`, `J_alpha-t`, and `J_alpha-r` from the first sibling bag;
- `J_beta-t` and `J_beta-r` from the second sibling bag; and
- `J_gamma-r` for the final pair.

All are literal support edges.

### Exactly two missing labels

For multiset `alpha,alpha,beta` and
`A={alpha,beta,r,s}`, the same check applies to the candidate's displayed
bags.  The last five bags have their ten adjacencies through

- `K-beta`, `K-s`, `alpha-J_beta`, and `K-r`;
- `J_alpha^1-s`, `J_alpha^1-t`, and `J_alpha^1-r`;
- `J_alpha^2-t` and `J_alpha^2-r`; and
- `J_beta-r`.

The three multiset types are exhaustive, and extra siblings are unused.  I
also instantiated the two displayed literal models directly in the ordinary
branch-set checker using only their structural edges; both passed.

## 4. Two-sibling quotient and the human templates

After contracting `P,Q,K,J_alpha,J_beta`, the quotient has exactly fifteen
vertices: seven literals of `S`, three literals of `X`, and five contracted
resource vertices.  Its stated incidence is exact after surplus-edge
deletion:

- the paired-triangle boundary provides the three independent pairs and the
  six required classes of boundary adjacency;
- `P,Q` are complete to `S` and are nonadjacent because `P subseteq L` and
  `Q subseteq R`;
- `K,J_alpha,J_beta` are pairwise nonadjacent components behind `X`, each is
  complete to `X`, and their boundary supports are exact; and
- the forced `u-X` and `v-X` contacts survive literally.

For distinct missing labels, if the two remaining `A`-labels `r,s` are
adjacent, the seven bags in the candidate's preliminary template are valid.
The packet bags supply all packet adjacencies.  Among the remaining five,
`K` sees `beta,r,s`, `J_beta` sees `alpha`, `J_alpha` sees `t,r,s`,
`J_beta` sees `r,s`, and the last pair is the literal edge `rs`.

The two representative hard-case templates now numbered (4.7) and (4.8)
were also replayed separately using only their advertised edges:

- in the same-gate template, connectivity uses `ct_3`, `t_2x_2`, and
  `t_3x_2`, together with structural lobe/gate edges;
- in the distinct-gate template, connectivity uses `ct_3`, `t_2x_1`, and
  `t_3x_2`.

Both have seven disjoint connected bags and all 21 literal cross-adjacencies.
The displayed human templates for the three-sibling and easy two-sibling
branches passed the same direct replay.

## 5. Exhaustiveness of the finite census

### Minimal boundary witnesses

For each of the three pairs `B_i`, one retains one of the two possible
`c-B_i` witnesses.  For each of the three unordered pair-pairs, one retains
one of four cross-edges.  These six choice groups are edge-disjoint, so the
number of distinct minimal boundaries is exactly

\[
2^3 4^3=512.
\]

Every actual paired-triangle boundary contains at least one selection of this
form.  Deleting its other edges is monotone in the correct direction: a
`K_7` model in the retained subgraph remains a `K_7` model after the deleted
edges are restored.

The selected neighbours of labelled `u=t_2` and `v=t_3` may independently be
any vertices of the three-set `X`.  The same gate is allowed, giving exactly
`3*3=9` ordered placements.

### Missing-label orbits

Fixing `B_1` leaves only the involution swapping the paired duties `B_2,B_3`,
equivalently swapping `a_2,a_3` and `t_2,t_3` while fixing `c,a_1,t_1`.

- On equal labels in `A`, its three orbits are represented by
  `c,a_1,a_2`.
- On unordered distinct pairs from `A`, its four orbits are represented by
  `{c,a_1}`, `{c,a_2}`, `{a_1,a_2}`, and `{a_2,a_3}`.

Sibling order is immaterial, and the full 512-boundary and nine-contact
censuses are closed under the involution.  Hence no labelled case is lost.

For three siblings there are

\[
\binom{4+3-1}{3}=20
\]

missing-label multisets, giving `20*512=10,240` replay cases.

For equal two-sibling labels there are
`3*512*9=13,824` cases.  In the four distinct-label representatives, excluding
the easy `rs` edge leaves respectively `384,384,256,256` minimal boundaries:
an `a_i-a_j` witness occupies one choice in a four-edge group, whereas a
`c-a_i` witness occupies one choice in a two-edge group.  Therefore the hard
count is exactly

\[
(384+384+256+256)\,9=11,520.
\]

This is complete coverage, not a sample or a shore-order cutoff.

## 6. Verifier audit

### Solver-free proof path

The default verifier imports the frozen catalogue without importing Z3.  Its
data flow is:

1. `minimal_boundaries` and the three case constructors generate the exact
   finite families above.
2. `Case.structural_edges` installs only forced packet, lobe-support, and
   lobe-gate edges.  `Case.optional_edges` contains the selected boundary and
   gate-contact witnesses.
3. `verify_case_hypotheses` independently rechecks pair independence,
   required paired-triangle adjacencies, exact lobe supports, full gate
   incidence, lobe nonadjacency, packet fullness/nonadjacency, the two forced
   gate contacts, old-component fullness in the quotient, and the hard-case
   common nonedge.
4. `Template.covers` permits all six gate renamings, requires the template's
   advertised optional predicate to be present, and then calls
   `verify_literal_model` on **only** the structural edges plus that predicate.
   It cannot borrow an unadvertised surplus case edge.
5. The final loop checks that some independently validated template covers
   every generated case.

The ordinary checker itself is exact.  `connected` performs a graph search
inside each bag.  `verify_literal_model` requires exactly seven bags, bag
orders from one through three, membership in the quotient vertex set,
pairwise disjointness, connectivity of every bag, and a crossing literal edge
for each of the 21 bag pairs.  Unused quotient vertices are correctly allowed.
No minor-model condition is omitted.

The frozen records are inert tuples.  Every one of the 21 three-sibling, 20
hard-distinct, and 17 equal-label frozen templates was additionally confirmed
to cover at least one case; the proof does not rely on an unchecked or dead
record.

### Optional SMT regeneration

Z3 is confined to `--regenerate`.  The encoding is sound block by block:

- a pseudo-Boolean at-most-one constraint assigns each quotient vertex to at
  most one bag, enforcing disjointness;
- each of seven bags has exactly one assigned root and at most three assigned
  vertices, enforcing nonemptiness and the bag-order cap;
- every assigned nonroot has an active-edge parent of strictly lower
  nonnegative depth, so repeated descent terminates at the unique root and
  proves connectivity;
- strictly increasing root indices remove only the irrelevant permutation of
  the seven bag names;
- every pair of bags is constrained to have an active edge crossing it; and
- solver assumptions set every optional edge exactly according to the current
  minimal case.

After model extraction, the same ordinary checker rechecks the concrete bags.
Template extraction chooses literal internal trees and literal crossing
edges, records every optional edge it used, and the hardened
`Template.covers` revalidates the resulting monotone certificate without
case surplus.  The final set-cover optimization affects catalogue size only,
not soundness; all selected templates undergo final exhaustive coverage.

There are no external state changes or untrusted network calls.  The relevant
dependency risks are all controlled: missing Z3 affects only regeneration,
a stale or malformed frozen catalogue fails the ordinary assertions, and an
SMT encoding error cannot validate an invalid branch-set certificate because
the ordinary replay is separate.

## 7. Executed checks

The frozen default verifier completed successfully with:

```text
minimal_paired_boundaries=512
three_sibling_cases=10240
three_sibling_symbolic_templates=21
three_sibling_all_literal_k7=True
hard_two_sibling_cases=11520
hard_two_sibling_symbolic_templates=20
hard_two_sibling_all_literal_k7=True
equal_two_sibling_cases=13824
equal_two_sibling_symbolic_templates=17
equal_two_sibling_all_literal_k7=True
total_cases=35584
total_symbolic_templates=58
solver_free=True
independent_branch_set_checks=True
```

The complete `--regenerate` run also passed all 35,584 cases and printed
`solver_free=False`; it found another valid 78-template cover.  Equality of
the regenerated and frozen catalogue sizes is neither asserted nor needed.

As a further independence check, I wrote a separate in-memory replay which
did not call the verifier's `connected`, `bags_adjacent`,
`verify_literal_model`, or `Template.covers` routines.  It reconstructed each
advertised subgraph, used its own adjacency maps and depth-first searches, and
rechecked disjointness plus all 21 bag adjacencies.  It independently covered
exactly `10,240`, `11,520`, and `13,824` cases.  Both Python files also compile
cleanly.

## 8. Quotient contraction and literal lift

The five contracted host sets are connected and pairwise disjoint:
`P` lies in `L`, `Q` lies in `R-C`, and `K,J_alpha,J_beta` are distinct
components of `C-X`.  They are disjoint from the retained literal sets `S`
and `X`.  Contracting an internal spanning tree in each therefore produces a
legitimate minor while leaving all boundary and gate literals distinct.

Every quotient edge used by a certificate is the image of a literal host
edge.  To lift a quotient branch bag, replace each contracted resource vertex
by its original connected host set.  Quotient-bag connectivity lifts along
those literal edges; different bags remain disjoint because the five host
sets were disjoint; and every quotient cross-edge lifts to a host cross-edge.
Thus the quotient `K_7` model gives a literal `K_7` minor of `G`.  This is also
an immediate application of transitivity of the minor relation.

## 9. Precise trust boundary and role of computation

Computer assistance is **essential to the proof as currently presented**, but
only at the fixed two-sibling quotient:

- the `11,520` hard distinct-label and `13,824` equal-label cases are covered
  by a frozen, solver-free catalogue and ordinary exhaustive replay;
- the `10,240` three-sibling computation is redundant because Section 3 has a
  complete human proof; and
- Z3 is not part of the trusted proof path.  It is a discovery/regeneration
  aid only.

The trusted computational kernel is therefore small and explicit: Python's
finite tuple/set operations, the ordinary graph-search checker, the frozen
58-template data, and exhaustive coverage of the fixed fifteen-vertex case
space.  A future human compression of the two-sibling quotient could remove
this dependency; none is currently supplied.

Finally, this theorem does not preserve an attained equality state on a new
boundary, does not provide a well-founded descent measure, and does not touch
the one-sibling gate, arbitrary `(1,1)` cells, larger adhesions, or rotation
components.  It closes exactly the common-exit residue with at least two
siblings and no more.
