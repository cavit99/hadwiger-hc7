# Fixed private extensions force one coherent active face

## 1. Setting

Let `W` be either a four-connected graph or a planar three-connected
graph.  Outside `W`, fix four pairwise disjoint connected sets

\[
                         E_1,E_2,E_3,E_4
\]

which are disjoint from `W`.  Put

\[
                         P_i=N_W(E_i).
\]

Assume the four fixed sets, together with fixed reserve and pool bags,
satisfy every off-torso hypothesis of the uniform biportal rooted-core
theorem.  Thus, whenever distinct roots `p_i in P_i` have a rooted
`K_4` model in `W`, adjoining each `p_i` to `E_i` makes that rooted
model a literal `K_7` model.

Call a four-set `B subseteq V(W)` **feasible** when the bipartite portal
graph between `B` and `{E_1,...,E_4}` has a matching saturating all four
extensions.

## 2. Transversal-matroid face theorem

### Theorem 2.1 (fixed-extension facial coherence)

Assume at least one feasible four-set exists. If `G` has no `K_7` minor,
then one face in the unique plane embedding
of `W` contains every vertex which belongs to a feasible four-set.

### Proof

The feasible four-sets are the bases of the rank-four transversal
matroid defined by the four portal sets `P_i`.  Its basis graph is
connected: for two bases `A,B`, ordinary basis exchange replaces an
element of `A-B` by an element of `B-A` while retaining a basis, and
iteration decreases `|A-B|`.  Consecutive bases therefore share three
actual vertices.

For a feasible basis choose a saturating matching and assign its four
roots to the fixed extensions.  It is an active quadruple in the sense
of `hc7_near_k7_active_root_face_exchange.md`.  All feasible bases
lie in one connected component of the three-overlap graph.  If one had a
rooted `K_4` in `W`, the fixed private extensions and the biportal
completion would give `K_7`.  Otherwise the three-overlap facial-
coherence theorem puts every vertex occurring in every feasible basis on
one common face.  QED.

### Corollary 2.2 (a rotation conflict is an extension collision)

A target-free rural rotation **inside the same page `W`** cannot change
while the same four disjoint private extensions remain available.  Nor
can it change merely because the chosen portal root inside one of those
extensions changes.  At the first genuine conflict which remains in
`W`, the off-torso extension system itself changes:
some set of four required extensions has no common disjoint realization,
or one of the pool/reserve contacts needed by the completion is lost.

Thus the two-coordinate residue of the active-root theorem is a genuine
carrier-capacity failure, not a failure of facial order among freely
selectable roots.

## 3. Scope

The theorem does not assert that four suitable fixed extensions exist.
Two state coordinates may require the same lobe, or a lobe may be the
unique carrier of a reserve contact.  Splitting such a shared lobe is the
remaining task.  The full-state shore/bi-Helly theorem gives the exact
next dichotomy: a typed split restores disjoint fixed extensions, while
failure localizes all carriers of one state half in one gate, cycle, or
three-connected torso.  Converting that localized collision into an
exact seven-adhesion or a common faithful colour state is not proved here.
