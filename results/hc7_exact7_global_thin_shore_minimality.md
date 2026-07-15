# Global thin-shore minimality closes every strict `(1,2)` receiver

## Status

Proved.  This is a global rank on **actual oriented exact-seven `(1,2)`
separations**.  It does not use, preserve, or compare boundary colouring
states.

## 1. Setup

Fix a finite graph `G`.  For an actual order-seven separation write

\[
             V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
             \qquad |S|=7,                              \tag{1.1}
\]

where `L,R` are nonempty and anticomplete.  Let `nu_L^S` and `nu_R^S`
denote the maximum numbers of pairwise vertex-disjoint connected `S`-full
packets in the two open shores.

Let `F_12(G)` be the set of ordered triples (1.1) satisfying

\[
                         \nu_L^S=1,\qquad \nu_R^S=2.    \tag{1.2}
\]

The orientation in (1.2) is intrinsic: reversing the same separation has
vector `(2,1)`, not `(1,2)`.

Assume `F_12(G)` is nonempty and choose a member with `|L|` minimum over
the whole family.

## Theorem 2.1 (state-free strict-receiver exclusion)

There is no actual order-seven separation

\[
             V(G)=L'\mathbin{\dot\cup}S'
                         \mathbin{\dot\cup}R'           \tag{2.1}
\]

such that

\[
 \nu_{L'}^{S'}=1,\qquad \nu_{R'}^{S'}=2,
 \qquad |L'|<|L|.                                      \tag{2.2}
\]

The conclusion is independent of every exact equality partition, named
minor operation, and returned colouring state on `S'`.

### Proof

Conditions (2.1)--(2.2) say exactly that `(L',S',R')` is another member
of `F_12(G)`, with its orientation already fixed by the asymmetric packet
vector and with a smaller minimizing coordinate.  This contradicts the
global choice of `(L,S,R)`.  No colouring datum occurs in the argument.
\(\square\)

### Corollary 2.2 (the atomic strict-lobe branch is excluded)

Suppose the atomic twin-seam analysis is run with its old open shore `A`
equal to the globally minimal `L` above.  Outcome 2 of
`hc7_atomic_twin_seam_packet_transfer.md` cannot occur: that outcome
certifies a literal lobe `D` or `E` which

1. is the packet-one shore of an actual `(1,2)` exact-seven separation;
2. has an opposite packet-two shore; and
3. is a proper subset of `A`.

Thus this branch is rejected before asking whether its returned
high-demand state has paired-triangle form.

### Proof

The three listed facts instantiate (2.1)--(2.2) with `L'=D` or `E` and
`L=A`.  Apply Theorem 2.1. \(\square\)

## 3. Exact scope

The theorem is deliberately narrow.

* A receiver with vector `(1,1)` is not in `F_12(G)`.
* If the new lobe is packet-two and the opposite shore is packet-one, the
  intrinsic `(1,2)` orientation points away from the lobe; no subset
  comparison follows.
* Lower bounds on packet numbers are insufficient.  The new vector must be
  verified literally and exactly relative to `S'`.
* A labelled `K_7^-`/`K_7^vee` rotation is not an actual separation and is
  outside the theorem.
* An order other than seven is outside the theorem.
* Minimizing only among cells with one particular attained colouring state,
  boundary graph, or local normal form is weaker.  A state-changing receiver
  need not remain in that subclass.  The minimization here is over **all**
  actual oriented `(1,2)` seven-separations in `G`.

Consequently the result supplies a genuine well-founded rank for strict
lobe-oriented `(1,2)` handoffs and nothing more.  It neither ranks `(1,1)`
receivers nor terminates `S1` near-model rotation components.

## 4. Recommended state-uniform closure formulation

The global theorem which would exploit this rank should be stated over the
whole family `F_12(G)`, not over one boundary graph or attained partition.
The required local input is the following.

> **State-uniform `(1,2)` closure target.**  For every oriented actual
> exact-seven `(1,2)` cell `(L,S,R)`, perform the canonical thin-side
> proper-minor operation and let `Pi` be any exact state it legally
> returns.  Then either the two shores reproduce one common state and
> six-colour `G`, a literal `K_7` or valid fixed-pair terminal occurs, or
> there is another actual oriented `(1,2)` cell `(L',S',R')` with
> `|L'|<|L|`.  No relation between `Pi` and the state later attained on
> `S'` is required.

If this target is proved, choose a global `|L|`-minimum before running the
canonical operation.  The smaller-cell outcome is excluded by Theorem
2.1, so a terminal outcome follows.  This is the clean way to make the
current local machinery state-agnostic: every normalization used before
the atomic decoder must apply to an arbitrary globally minimal member of
`F_12(G)`, or itself return a smaller member of that same family.

The presently audited atomic twin-seam theorem does not yet establish this
uniform input.  Its paired-triangle/connected-rich hypotheses have not been
derived for an arbitrary global minimum without restricting the attained
state.  That is the precise remaining upstream closure obligation.
