# Audit of clean root capture

## Verdict

The clean-capture theorem, its lift to the contact-maximal model, the
ordinary-gate attachment count, and the icosahedral sharpness example are
sound after one necessary precision repair: the contracted free carriers
must be absorbing vertices in a directed auxiliary graph.  A separator
which is itself a contracted sink is a target-reachability failure, not
an assertion that one internal vertex of the lifted carrier is an
undirected cutvertex.  The main note has been patched accordingly.

## 1. Source--sink Menger and lifting

The four objects \(a,z,c_1,c_2\) are distinct.  Unit capacity on sources
and sinks implies that a linkage of order two uses both sources and both
sinks.  Making the two targets absorbing prevents one free carrier from
being used internally on a route to the other.  When the contractions are
lifted, each path meets its assigned carrier for the first time at its
last edge, so absorbing the path produces two disjoint connected sets.

The component hypothesis is imposed on the original undirected \(R\),
separately from the directed-sink construction.  This distinction is
necessary because deleting all arcs out of two adjacent sinks deletes
both orientations of their mutual edge.  Both enlarged carriers meet the
same underlying component of \(R\); a shortest
path between the two sets has no internal vertex in either.  Absorbing
its interior makes the sets adjacent and cannot meet a terminal branch,
because the four \(T_i\)'s were deleted in the definition of \(R\).

## 2. Terminal lifting and contact count

Each prescribed terminal \(t_i\) is the contraction of the corresponding
original retained clique bag.  Hence a rooted branch set \(T_i\)
containing \(t_i\) lifts to a branch set containing that entire original
bag.  The four terminal branch sets remain pairwise adjacent through the
terminal \(K_4\).  Each free carrier is adjacent to every \(T_i\) by the
rooted \(K_{2,4}\)-model, and the connector supplies the last free--free
adjacency.

If the promoted bag was one contacted bag containing \(a,z\), the new
two rooted carriers contribute two contacts in its place.  Every retained
contacted bag keeps its old root, and the dropped bag was uncontacted.
Thus the contact count increases by exactly one, irrespective of how many
of the other four retained bags were contacted.

## 3. Ordinary gate count

Under the three explicit Hall-region hypotheses of Lemma 5.1,

\[
 N_G(W)\subseteq \{v,s\}\cup\bigcup_{i=1}^4P_i .
\]

The set on the right separates nonempty \(W\) from the two nonempty free
carriers.  Its displayed pieces are disjoint, so seven-connectivity gives
\(\sum_i|P_i|\ge5\).  Equality gives a genuine separator of order seven;
strict inequality gives at least six actual terminal attachment vertices.
Pigeonhole then gives a multiply hit terminal carrier.  These conclusions
must not be applied to an arbitrary clean packing unless the three
Hall-region hypotheses have first been verified.

The new note hadwiger_clean_gate_minimal_bypass.md strengthens this:
an innermost internal gate automatically supplies the two root-side paths
needed to use any detachable terminal arm, and a sink target failure plus
a detachable arm either opens or exposes a closer ordinary gate.

## 4. Icosahedral sharpness

For the icosahedral graph \(I\),

\[
 \kappa(K_2\vee I)=7,\qquad
 \delta(K_2\vee I)=7,\qquad
 \chi(K_2\vee I)=2+\chi(I)=6.
\]

Moreover \(\eta(I)=4\), since \(I\) is planar and contains a
\(K_4\)-minor, so

\[
 \eta(K_2\vee I)=6.
\]

The six displayed bags in the main note are connected and pairwise
adjacent.  Their five contacts are \(u_0,u_1,u_2,p,q\), while
\(\{b\}\) is uncontacted.  The unused-root component
\(\{u_3,u_4\}\) has no portal to \(\{b\}\), and the listed portal sets
follow directly from the standard icosahedral adjacencies.

After promotion, the two nontrivial portal classes are
\(\{u_4,w_4\}\) and \(\{u_2,w_2\}\).  A rooted split would have to put
\(w_2\) with the \(u_3\)-side and divide \(u_4,w_4\) between the two
sides.  Either division disconnects the \(u_2\)-side, so the literal
split is impossible.  The clean quotient model in the note is valid:
both \(u_4,w_4\) see the branch
\(\{t_2,w_2,w_3\}\), and each sees the other three terminal vertices.

Deleting the four terminal branches leaves

\[
 u_2-u_3-u_4-w_4.
\]

Here \(u_3\) is an ordinary one-vertex gate.  If \(u_4\) is chosen as a
contracted absorbing carrier, it is instead the sink
target-reachability obstruction.  The latter wording is not a cutvertex
claim inside a lifted multi-vertex carrier.

## 5. Exact audit boundary

The audited theorem does not prove existence of a clean rooted
\(K_{2,4}\) packing.  Nor does seven-connectivity eliminate an ordinary
or sink gate: the icosahedral graph realizes both while remaining
six-colourable.  The extra hypothesis still needed for complete
elimination is the negative one-step state of a seven-contraction-critical
graph.  Any use of an edge-critical Kempe detour must verify avoidance of
all reserved branch sets and of the fixed capture paths; merely knowing
that five bichromatic detours exist is insufficient.
