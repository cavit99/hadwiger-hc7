# Independent audit: side-terminal-free state-or-rural theorem

Audited file: `results/hc7_exact7_terminal_free_state_or_rural.md`.

## Verdict

**GREEN after four repairs now incorporated in the source.**  The theorem
is a valid composition of the exact-six shore identities, component
absorption, the spanning-rural quadrichotomy, the pair-carrier peel, and
the set-terminal cross rotation.

Its exact advance is state-level normalization.  Instead of trying to turn
a selected endpoint adjacent to an absorbed pole piece into a literal edge
to the originally chosen subregion `L`, it enlarges `L` to its whole
component `Y`.  The set `W'={w} union Y` is connected, has the same
adhesion trace `{w}`, and makes every member of `P(K,Y)` a genuine marked
attachment.  Deleting the side terminal before component absorption makes
the resulting carrier eligible as a supported core.  No raw contact is
identified with attained duty.

The theorem does **not** close the low-carrier-cut or rural-page outcomes,
reinsert the side terminal into the rural page, force a prescribed one of
the two target labels, or by itself produce a common bilateral state.

## 1. Terminal-free host and exposure

The exact cell gives

\[
 N_G(D_t)=U\mathbin{\dot\cup}\{w,t\}.
\]

The open shore `D_t` is connected and every vertex of `U` has a neighbour
in it.  Hence the induced graph

\[
                         J^\circ=G[D_t\cup U]
\]

is connected.  With `Z=V(D_t) union {x,y}`, every nonempty set
`C subseteq Z-{x,y}` lies wholly in `D_t`.  It has no neighbour at `v`,
in the opposite open shore, or at a boundary vertex outside
`U union {w,t}`.  Since `U subseteq V(J^circ)`, this proves the literal
exposure bound

\[
                   N_G(C)-V(J^\circ)\subseteq\{w,t\}.
\]

This is exactly the two-outside-neighbour hypothesis of the audited
spanning-rural theorem.  The proof does not need an assertion about a set
containing `x` or `y`, because those roots are removed in the exposure
hypothesis.

## 2. Components and traces

The traces of `K_0,A,B` partition `U`, with the whole pair trace in `K_0`.
Consequently every component of `J^circ-V(K_0)` other than the one
containing `A union B` contains no vertex of `U`; the same is true of every
vertex added to `K_0` by component absorption.  Thus the absorbed carrier
has trace exactly `{x,y}`.

If `A union B` and `L` occur in the same component, a shortest
`(A union B)-L` path has no internal vertex in `A union B`, `L`, or `K_0`.
It contains no vertex of `U`, because all of `U` already lies in the three
core traces.  Absorbing its target-side prefix therefore preserves the
target trace and gives a literal second contact for the original `W`.
Admissibility is decided by the unchanged target trace; failure is the
already isolated boundary-incompatibility certificate.

If the two sets occur in distinct components `X,Y`, absorbing all other
components into `K_0` gives connected `K,X,Y`, with `X,Y` anticomplete and
spanning `J^circ`.  Every absorbed component has an edge to `K_0`, since
`J^circ` is connected.  The old target and locked contacts remain members
of `Q(K,X)` and `P(K,Y)`, respectively, so both sets have the required
order at least three.

The carrier has at least five vertices (indeed it contains two roots and
one portal set of order at least three).  Hence if it is not
three-connected, the usual definition gives an actual vertex cut of order
at most two.  The low-cut wording is therefore literal, not merely a
failure of a convention for very small graphs.

## 3. Partitioning the target pole

Lemma 2.1 is correct after explicitly retaining adjacency of the two
parts.  Contract `A` and `B`, choose a spanning tree containing one fixed
literal `A-B` edge, and delete that tree edge.  The lifted components are
connected, cover `X`, contain `A` and `B` respectively, and remain
adjacent through the deleted literal edge.  Since every adhesion vertex of
`X` was already in `A union B`, neither trace changes.

This assigns a selected `X`-neighbour of a portal to **one** of the two
original named labels after trace-preserving enlargement.  It does not
promise assignment to a preselected label.  That distinction remains
relevant if only one target state is supported on the opposite shore.  It
is already necessary for the three-vertex pole path `A-B-u`: a connected
part containing `A,u` cannot avoid the fixed block `B`, so `u` can only be
assigned to the `B` side while both original blocks remain disjoint.

## 4. Enlarging the marked pole

Put `L'=Y` and `W'={w} union Y`.  These substitutions are legal:

* `Y` is connected and contains the original `L`, while `w` has a literal
  neighbour in `L`, so `W'` is connected;
* `Y` contains no vertex of `U`, so `W' cap T={w}`;
* `t` is absent from `J^circ`, so `W'` and all three new core blocks avoid
  the side terminal;
* `X,Y` are anticomplete, so `Y` is anticomplete to both enlarged target
  blocks; and
* by definition, the full marked set for `L'` is exactly
  `N(Y) cap K=P(K,Y)`.

Thus the enlargement preserves the attained equality block `{w}`.  It is
stronger than retaining only raw contact, but weaker than manufacturing an
edge from the selected endpoint to the original proper subset `L`.

## 5. Shared portal and cross

For a shared portal `q`, the target partition puts an `X`-neighbour of
`q` in a named target block.  Simultaneously
`q in N(Y) cap K`, and `q` is a nonroot.  With `K` three-connected and
`|P(K,Y)|>=3`, every hypothesis of the audited pair-carrier peel holds.
The peel gives `W'` literal contacts with the retained pair carrier and the
named target, with all traces unchanged.

For the cross branch, first exclude the shared-portal branch.  Then
`Q(K,X) cap P(K,Y)=empty`, so its `Q`-endpoint `q` is outside the full
marked set.  The target partition creates a literal `q`--target edge, and
the other endpoint `p` belongs to the exact full set
`N(Y) cap K`.  The carrier and the poles avoid `t`.  These are precisely
the three qualifications missing from a direct application of the local
cross-rotation theorem.  It returns either the labelled peel or a rotation
which moves every **`Y`-based** carrier contact into the named target.

A direct `w`--carrier edge may remain after the rotation.  The source now
states only the exact `Y`-contact transfer and concludes support of the
named state from its unchanged admissible trace.  It does not repeat the
previously audited false uniqueness claim.

## 6. Exact scope and guardrail

The strongest valid conclusion is

\[
\begin{array}{c}
\text{terminal-free component absorption plus a shared portal or cross}
\\[2mm]\Downarrow\\[2mm]
\text{state-faithful labelled peel or named decoration rotation.}
\end{array}
\]

It is generally unjustified to demand that the selected `P(K,Y)` endpoint
already lie in `N(L) cap K`.  An absorbed path can end at a vertex of
`Y-L`; the local graph has no operation which creates a new literal edge
from that endpoint to the fixed proper subgraph `L`.  Enlarging the branch
set from `L` to `Y` is the label-faithful operation: it preserves
connectivity, disjointness, and the exact trace while making the selected
endpoint genuine.

Likewise, deleting `t` here does not embed or colour it later.  The two
surviving outcomes are exactly an actual carrier cut of order at most two
and a planar quotient spanning `D_t union U`.  Low-cut conversion,
induced-pole expansion, reinsertion of `t`, and bilateral state matching
remain separate proof obligations.
