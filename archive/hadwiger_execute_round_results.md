# Audited results of the decisive continuation round

## Status

This round does **not** prove Hadwiger's Conjecture or all of
$\mathrm{HC}_7$.  It does meet the run's highest-priority success
criterion: the pure-Moser two-exterior-component case is completely
resolved.  With a dependency-free finite neighbourhood classification,
this closes every degree-seven case having exactly two exterior
components.

## 1. Reusable exact boundary-state transfer

Theorem `hadwiger_exact_boundary_state_transfer.md` is valid for every
$t$.  In a proper-minor-minimal counterexample, suppose

\[
G-N[v]=C_1\mathbin{\dot\cup}C_2.
\]

Let $\Pi$ be a partition of $N(v)$ into independent blocks.  If one
side, using vertices of that side and possibly $v$, realizes the blocks
as disjoint connected pairwise adjacent contraction sets, then every
proper-minor colouring transfers to the opposite side and induces
**exactly** $\Pi$ on the boundary.  If both sides realize the same
partition with at most $t-2$ blocks, the two colourings align and glue,
and an absent boundary colour can be assigned to $v$.

This is a genuine advance on the uniform model-meeting obstruction: it
turns label-preserving branch-set surgery on one side into a prescribed
colour-extension state on the other.  It is not a proof that an arbitrary
unrooted $K_{t-1}$-model can always be made to meet $N(v)$.

## 2. Complete pure-Moser two-component closure

For the repeated pair $13$, the five uniquely coloured roots have missing
pentagon

\[
05,25,24,46,06.
\]

If two vertex-disjoint pentagon edges are supported in one exterior
component, their bichromatic paths are disjoint.  Joining the paths by a
shortest internal connector and contracting the two resulting terminal
blocks together with the star $\{v,1,3\}$ realizes an exact four-block
boundary state on the opposite side.  This is the supported-pair transfer
lemma.

Combining transfer with exact-state exclusivity, two-anchor coverage, and
the one-swap state eliminates every one of the fourteen genuinely mixed
support-word orbits.  A non-mixed word confines all five pentagon edges to
one component; the Kriesell--Mohr pseudoforest construction gives a rooted
$K_5$ there, while the other full-attachment component together with
$\{1,3\}$ is the sixth bag.  Hence:

> A degree-seven vertex with pure-Moser neighbourhood cannot have two
> exterior components in a proper-minor-minimal counterexample to
> $\mathrm{HC}_7$.

The hand proof is in
`hadwiger_moser_supported_pair_transfer_closure.md`; the independent state
replay is `moser_supported_pair_transfer_verify.py`.

The dependency-free verifier
`degree7_neighborhood_labeled_verify.py` exhausts all $2^{21}$ labelled
seven-vertex graphs.  Among the $133{,}501$ graphs with independence
number at most two, the only failures of the usable local
$K_4$-plus-two-adjacent-anchors certificate are exactly the isomorphism
orbits of the Moser spindle and $M+13$.  The latter is eliminated by the
two-anchor colour-gluing lemma, and the former by supported-pair transfer.
Therefore:

\[
\boxed{d(v)=7\quad\Longrightarrow\quad
       G-N[v]\text{ does not have exactly two components}.}
\]

## 3. Sole-exterior pure-Moser families

For a sole exterior $C$ behind the pure-Moser boundary, certified shore
packing now eliminates every:

* tree exterior;
* unicyclic exterior; and
* bicyclic exterior.

The unicyclic proof contracts $C$ to one of the thirteen simple connected
six-vertex unicyclic quotients.  The bicyclic proof uses a safe
nontriangle-edge contraction lemma and the nineteen simple connected
six-vertex seven-edge quotients.  Seven-connectivity supplies the exact
row-defect inequalities, and the finite certificates supply an
$N$-meeting $K_6$-model.

Thus the current pure-Moser sole-exterior residual satisfies

\[
\rho(C)=|E(C)|-|V(C)|+1\ge3,
\qquad |E(C)|\ge|V(C)|+2.
\]

A further verified theorem closes every tricyclic exterior that safely
contracts to a simple six-shore tricyclic quotient (all twenty-two
six-vertex types; 64,044 model clauses).  The safe-contraction
classification leaves exactly two unresolved tricyclic families: exteriors
contracting to the seven-vertex friendship graph of three triangles or to
the chain of three triangle blocks.  Hence a surviving exterior either has
cyclomatic number at least four or lies in one of those two exact cactus
families.  Complete tricyclic elimination is **not** claimed.

The proof notes are `hadwiger_moser_one_component_infinite_classes.md`,
`hadwiger_moser_unicyclic_exteriors.md`, and
`hadwiger_moser_bicyclic_exteriors.md`; the partial tricyclic extension is
`hadwiger_moser_tricyclic_exteriors.md`.  Their independent replays are
the corresponding `*_verify.py` files.

## 4. Degree eight and degree nine

Two finite-boundary colour-gluing theorems were independently verified:

\[
\boxed{
d(v)=8\Rightarrow \#\operatorname{comp}(G-N[v])\le2,
\qquad
d(v)=9\Rightarrow \#\operatorname{comp}(G-N[v])\le3.
}
\]

The degree-eight verifier covers the three miss patterns with 422 quotient
templates.  The degree-nine verifier covers all twenty-three isomorphism
types of four two-vertex miss sets with 423 templates.  The proofs combine
an explicit $N$-meeting $K_6$ quotient model with exact four- or five-block
anchor partitions whose proper-minor colourings align across retained
components.

The notes are `hadwiger_degree8_three_component_closure.md` and
`hadwiger_degree9_four_component_closure.md`.

## 5. Further verified local facts

* No component of $G-N[v]$ is a singleton in any proper-minor-minimal
  counterexample, for any $t$: colour $G-x$ and give the isolated exterior
  singleton the colour of $v$.
* In the two-component pure-Moser setting, direct finite certificates
  eliminate a $K_2$, $K_3$, or $K_4$ exterior from the seven-connectivity
  subset inequalities.  This is now subsumed by the full two-component
  closure but remains a reusable shore certificate.
* Coarse degree-eight cutvertex-shore data do **not** suffice.  Explicit
  quotient and portal counterexamples survive all currently encoded
  five-block anchor gluings, so any claimed closure of that family needs
  genuine portal-sensitive minor transitions or internal linkage.

## 6. Exact gaps after this round

The unresolved $t=7$ work includes:

1. the one-exterior degree-seven nonseparating rooted-$K_5$ / reserved
   connector problem (with the pure-Moser exterior now either of
   cyclomatic number at least four or in one of two exact tricyclic cactus
   families);
2. the remaining one- and two-component degree-eight cells;
3. the remaining one-, two-, and three-component degree-nine cells; and
4. the exceptional $K_3\mathbin{\dot\cup}K_4$ sole-exterior cell.

For general $t$, the main obstruction remains converting saturation and
an unrooted $K_{t-1}$-model into an $N(v)$-meeting model.  Exact
boundary-state transfer supplies a new mechanism when a suitable
two-sided realization is available, but it does not yet produce that
realization uniformly.

Accordingly, neither $\mathrm{HC}_7$ nor Hadwiger's Conjecture in full is
claimed here.
