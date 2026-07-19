# Independent internal audit of the six-label donor-fan reduction

**Verdict:** GREEN for the theorem and corollary under their explicit
conditional hypotheses and trust boundary.

## Audited revision and verdict

This audit checks the complete source file
[`hc7_order8_six_label_donor_fan_reduction.md`](hc7_order8_six_label_donor_fan_reduction.md)
at SHA-256

```text
c12d8b83a64b8ff7d6e02d55a6eb21b9a5ef513c2036997318be6c7083d725f8
```

Relative to the proof revision checked below, the final source also changes
only its opening status paragraph from pending to a link to this completed
audit.  Restoring the pending-status line reproduces SHA-256
`e01ea5e3601dc179051adb06f5f5f18a467ec587476c1a656239eaedf4f426d6`.
That preceding revision had added only the explicit sentence that each rank
path is trimmed at its first ranked hit.  Replacing that sentence by the
previous wording reproduces the earlier proof revision, SHA-256
`35834077d30e63e3545a76f211305df9559cbe85aa03b17441a8a47f62ed294c`.
The status link changes no mathematics, and the first-hit clarification
states the normalization already used in the proof.  Neither changes any
hypothesis or deduction.

**Verdict: GREEN for Theorem 2.1 and Corollary 3.1 with their explicit
conditional hypotheses and trust boundary.**  This is a separate internal
mathematical audit, not external peer review.

The theorem closes only the donor-contained case in which `U-C` is connected
and the selected model is already extremal for the stated relaxed first-hit
rank.  Its separator outcome carries no common equality partition, and its
other outcome is a degree-eight singleton rather than a contradiction.

## 1. Audit of the no-fan separation

The graph used for Menger is the literal induced graph `G[C union T]`, where
`T` consists of the six boundary representatives outside `U`.  If there is
no six-fan from `v` to `T`, the fan form of Menger gives a set
`Z subseteq V(H)-{v}` of order at most five whose deletion separates `v`
from `T-Z`.

Let `A` be the `v`-component of `H-Z`.  Since `C` is a component of `G-S`,
the only possible neighbours of `A` not represented in `H` are the two
vertices `k_1,k_2`.  Componenthood in `H-Z` therefore gives

```text
N_G(A) subseteq Z union {k_1,k_2}.
```

The set `T-Z` is nonempty.  Every one of its vertices has a neighbour in
`C`, by `N_G(C)=S`, but none can have a neighbour in `A`, since it is outside
both `Z` and the `v`-component.  Hence `A` is a proper nonempty connected
subset of `C`.  The assumed other component of `G-S` lies outside
`A union N_G(A)`, so the full neighbourhood is an actual separator with two
nonempty open sides.  Seven-connectivity now yields

```text
7 <= |N_G(A)| <= |Z|+2 <= 7.
```

Thus the separator has order exactly seven.  Equality also implies
`|Z|=5` and `N_G(A)=Z dotunion {k_1,k_2}`, as used later in Corollary 3.1.

## 2. Audit of the six-fan branch-set transfer

### 2.1 Partitioning the donor component

A six-fan has one path `P_R` to every member `s_R` of the six-set `T`, and
the paths meet only at `v`.  Their internal vertex sets `L_R^0` are therefore
pairwise disjoint connected subsets of `C`.  After removing `v` and all
nonempty `L_R^0`, every remaining component of `G[C]` has an edge to `v` or
to at least one `L_R^0`; otherwise connectedness of `C` would fail.  Assigning
each component to one adjacent recipient gives the asserted connected
partition

```text
C = C_0 dotunion (dotunion_R L_R),   v in C_0.
```

No vertex of the boundary or of another old branch set is moved in this
partition.

### 2.2 Connectivity, disjointness and all model adjacencies

The retained donor `U^*=U_0 union C_0` is connected through the prescribed
edge `v k_1`.  For each nonempty fan interior, `R union L_R` is connected
through the last edge of `P_R`; the first edge of that path joins it to
`U^*`.  If the interior is empty, the direct edge `v s_R` gives the same
`U^*-R` adjacency.

All original vertices of every outside branch set remain in that set.
Consequently enlarging it destroys none of its old adjacencies, including
all adjacencies between the six outside branch sets.  The construction
partitions the old donor and changes no other vertex assignment, so the
seven new branch sets are nonempty, connected, pairwise disjoint, and span
`V(G)`.  Every pair is adjacent except possibly `X,Y`.  If the transfer has
created that last adjacency, the seven sets are an explicit `K_7`-minor
model; otherwise they are a spanning labelled `K_7`-minus-one-edge model
with the same possible missing pair.

The prescribed roots remain in their old labelled sets: the `U` root lies
in `U_0`, while every other old branch set is retained.  The response
subgraph `Z_0 subseteq D`, its permitted ports, the edge `z_0u_0`, and every
literal boundary vertex in (1.6) remain in their prescribed labelled sets.
The fixed boundary partition is a colouring datum on unchanged literal
vertices and is therefore unchanged by the branch-set reassignment.

## 3. Audit of relaxed first-hit-rank preservation

Normalize every ranked path by stopping it at its first vertex in the union
of the ranked branch sets.  A path whose first-hit label is not `U` then
avoids the entire old branch set `U`, and hence avoids every subset of `C`
transferred to an outside branch set.  It remains a valid first-hit path for
the same label.  A path ending in retained `U_0` also remains unchanged.

There is at most one path whose first-hit label is `U`.  If it ended in a
transferred subset of `C`, retain its distinct designated port `p`, take a
`p-z_0` path inside connected `Z_0`, and append `z_0u_0`.  The replacement
may overlap the other paths only inside `Z_0`, which the rank definition
allows.  Outside `Z_0` it consists only of `u_0`; all other ranked paths
avoided old `U`, so none uses that vertex.  Since `D` is not among the ranked
labels, the replacement first meets a ranked branch set at `u_0 in U_0`.
It preserves its designated port and the size of the family.

Therefore every nonterminal transferred model has rank at least the old
maximum.  Extremality makes the ranks equal, while any nonempty fan interior
strictly decreases `|U|`.  This contradicts the secondary minimum.  It is
therefore valid to conclude that every fan path is the direct edge
`v s_R`.

## 4. Audit of the final singleton reduction

Let `Q` be a component of `G[C-v]`.  Its neighbours inside `C` but outside
`Q` can only include `v`.  Its neighbours outside `C` lie in `S`.  If it
missed all six vertices of `T`, then

```text
N_G(Q) subseteq {v,k_1,k_2},
```

contradicting seven-connectivity.  Thus every such component has an edge to
some `s_R` and may be assigned to that outside branch set.  Each enlarged
outside set is connected through its literal `s_R` contact; `U_0 union {v}`
is connected through `v k_1`; and the six direct fan edges retain every
donor-to-outside adjacency.  The same spanning-model and rank-preservation
checks from Sections 2--3 apply.  If `C-v` were nonempty, the result would be
a forbidden `K_7` model or a compatible extremal model with smaller `U`.
Hence `C={v}`, and `N_G(C)=S` gives `N_G(v)=S` and `d_G(v)=8`.

## 5. Audit of incident response preservation

If the selected incident edges are `v s_R` and `v s_{R'}`, replacing the
corresponding fan paths by these direct edges preserves the fan.  In the
separator branch, both terminals must belong to `Z`: otherwise their edge
to `v in A` would put them in the `v`-component of `H-Z`.  The equality case
above then gives

```text
N_G(A)=Z dotunion {k_1,k_2},
```

so both operated edges cross the new literal boundary and retain their
branch-set labels.

Each one-edge deletion colouring is proper on the intact opposite closed
shore because its only possibly monochromatic edge has its inner end in
`A`.  Its restriction to the edge-operated `A`-shore is also proper, so the
two one-edge responses survive unconditionally.

For the simultaneous contraction, expansion assigns one colour to
`v,s_R,s_{R'}`.  On the opposite closed shore the only additional edge that
can thereby become monochromatic is `s_Rs_{R'}`.  Accordingly the source now
claims a proper literal opposite-shore response only when this edge is
absent.  When it is present, the source correctly records merely an
identified-boundary trace and makes no common-partition claim.  This repaired
scope is exact.

## 6. Invocation from the reserved-component normal form

The cited reserved-component theorem supplies the following literal data in
its three-owner, order-eight branch:

- `C subseteq W subseteq U`, `N_G(C)=S`, and another component containing
  the retained donor `U'`;
- the two vertices `k_1,k_2` outside `C` and exactly one boundary vertex in
  each of the six old branch sets outside `U`;
- the prescribed `U` root and the persistent response endpoint `u_0` in
  `U'`; and
- the spanning labelled `K_7`-minus-one-edge model.

Although that source does not state `U-C` connected as a separate item, it
follows from its audited rank-two linkage geometry.  In any two-owner
linkage, the two paths start in `B=N_G(U') cap W` and use the two vertices
`k_1,k_2` separately.  The `B-k_i` initial subpath avoids `C`: before reaching
`K` it lies in one component of `W-K`, while `B` and `C` lie in different
components.  Thus each `k_i` is connected to `U'` in `U-C`.  Every other
component of `W-K` has a neighbour in `K` because `W` is connected.  Hence
`U-C=U' union (W-C)` is connected.

The reserved-component theorem does **not**, by itself, supply the global
choice maximizing the relaxed first-hit rank and then minimizing `|U|`, nor
does its statement independently supply every selected partition and port
datum of Section 1.  Those are explicit additional hypotheses of the present
theorem and must be established by the upstream invocation.  In particular,
one may not take an arbitrary reserved-component model and silently infer
that it is extremal in the broader compatibility class.

## 7. Exact trust boundary

The audit proves the conditional reduction exactly as stated.  It does not
prove that every order-eight component lies in one old branch set, that
deleting it leaves the donor connected, or that every reserved-component
normal form is automatically compatible with the extremal model choice.
It also does not eliminate the degree-eight singleton, preserve a
simultaneous response across an adjacent pair of boundary terminals, produce
a common equality partition on an order-seven boundary, or prove `HC_7`.
