# Barrier to two forced-hub transit labels in the atomic core

**Status:** barrier/counterexample to an intermediate claim and
computer-assisted finite result; separate internal audit GREEN.

This note tests one precise prerequisite of the proposed order-nine
path-absence continuation.  That continuation needs two distinct retained
labels which can occur on a `q`--`x` path without changing the final
branch-set ownership.  Under the natural forced-hub interpretation, the
exact two-bridge core supplies only one such label.

The adjacent deterministic verifier is
[`hc7_atomic_two_safe_transit_label_barrier_verify.py`](hc7_atomic_two_safe_transit_label_barrier_verify.py).

## 1. Exact forced-hub assertion

Let `C` be the thirteen-vertex graph in the audited
[exact-core seven-fan theorem](../results/hc7_atomic_two_bridge_exact_core_seven_fan_closure.md).
For each

\[
                       v\in V(C)-\{q,x\},
\]

let

\[
                         C_v=C+qv+vx+qe.                 \tag{1.1}
\]

Repeated edges in (1.1) are ignored.  The edges `qv,vx` are the canonical
contractions of the two externally clean pieces of a `q`--`x` path whose
only retained internal label is `v`; `qe` is the other clean connection.
Call `v` **forced-hub admissible** when `C_v` has a `K_7`-minor model in
which `q,v,x` all belong to one branch set.

The intermediate claim under test was that two distinct labels are
forced-hub admissible.

### Proposition 1.1 (exact forced-hub classification)

Among the eleven candidates in \(V(C)-\{q,x\}\), the forced-hub admissible
labels are exactly

\[
                               \{p\}.                    \tag{1.2}
\]

In particular, the proposed two-label prerequisite is false.

#### Finite proof

For each candidate `v`, the verifier contracts the connected prescribed
set \(\{q,v,x\}\) in \(C_v\), and then enumerates every canonical spanning
partition of the contracted graph into seven nonempty sets.  It checks that
each set is connected and that every pair of sets is adjacent.  Exactly the
candidate `p` succeeds.

The spanning restriction loses no model.  Each contracted graph is
connected, and any unused vertices of a nonspanning clique-minor model can
be assigned along a forest rooted at its branch sets, preserving their
connectedness and pairwise contacts.

For the positive case, an explicit model in \(C_p\) is

\[
 \{p,q,x\},\quad \{a,c,r,s\},\quad \{b\},\quad \{d\},
 \quad \{e\},\quad \{f,h\},\quad \{g\}.                \tag{1.3}
\]

The first set is connected by the added edges `qp,px`, the second contains
the path `a-r-s-c`, and `\{f,h\}` contains `fh`.  One contact for every
pair is

| first set | contacts with later sets |
|---|---|
| `\{p,q,x\}` | `qa`, `xb`, `xd`, `qe`, `pf`, `qg` |
| `\{a,c,r,s\}` | `cb`, `ad`, `ae`, `cf`, `cg` |
| `\{b\}` | `bd`, `be`, `bf`, `bg` |
| `\{d\}` | `de`, `df`, `dg` |
| `\{e\}` | `ef`, `eg` |
| `\{f,h\}` | `hg` |

The verifier independently checks connectedness and all 21 contacts in
(1.3).  This proves (1.2).  \(\square\)

## 2. Consequence and scope

The envisioned order-nine continuation required two distinct labels with
the property above.  Since only `p` has it, that specific continuation
cannot be justified by absorbing a single retained transit label into the
`q,x` branch set.

This is an exact finite barrier to that ownership rule, not a negative
statement about the ambient seven-connected problem.  In particular, it
does not assert that \(C_v\) lacks every `K_7` model when \(v\ne p\); it excludes
only models with the prescribed common branch set.  It also does not cover
paths with several retained labels, a different allocation of the path,
or additional host structure.  Those remain legitimate ways to obtain a
bounded response interface or a strict reduction.
