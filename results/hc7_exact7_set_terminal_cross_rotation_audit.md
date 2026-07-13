# Independent audit: set-terminal cross rotation

Audited file: `results/hc7_exact7_set_terminal_cross_rotation.md`.

## Verdict

**Theorem 2.1 is GREEN as a local trace-preserving surgery.  Corollary
3.1 is GREEN in the original supported bilateral core.  The final claimed
application to an arbitrary cross from the spanning-rural theorem needs
two additional endpoint/scope hypotheses.**

The local proof correctly turns a cross with

* `q` a literal portal to the named block `A`, and
* `p` an actual member of the fixed set `N_G(L) cap V(K)`

into either the audited labelled peel or an exact move of all `L`-contacts
from the pair carrier to `A`.  It preserves every adhesion trace and all
three pairwise core adjacencies.

A cross from the spanning theorem uses

\[
 Q(K,X)=N_K(X)-\{x,y\},\qquad P(K,Y)=N_K(Y)-\{x,y\}.
\]

Even if its `Q` endpoint is labelled to the original `A`, its `P` endpoint
may see only `Y-Y_0` and need not lie in `N(L) cap K`.  Moreover the
spanning carrier may contain the side terminal `t`.  In either situation
Theorem 2.1 does not yet yield a supported bilateral state.  The last
paragraph must retain these as attained-duty conditions rather than say
the cross is discharged completely.

One wording qualification is also needed: under the hypotheses as stated,
the theorem moves the **`L`-based contact** exactly.  Calling it the
“unique raw decoration” additionally assumes the inherited raw-rank-one
condition for `W={w} union L`; `L`-anticompleteness alone does not exclude
raw `w`-contacts to `A` or `B`.

## 1. Connected-pair conversion

The paths in (2.1) are vertex-disjoint.  Consequently the four relevant
terminals are distinct; in particular the chosen `p` cannot be `x` or
`y`, even if the full set `P` contains a trace root.

The audited connected-pair lemma applies in the three-connected induced
carrier.  It returns a nonseparating `x-y` path `R` avoiding `q,p`, with

\[
                         C=K-V(R)
\]

connected and containing the entire connected side which held the
`q-p` path.  Hence `q,p in C`.  No planarity or completion edge is used in
this conversion.

This is exactly the strength needed below: `R` contains both trace roots,
while `C` contains a named portal and at least the selected marked
attachment.

## 2. Peel branch

If `R cap P` is nonempty, the partition

\[
                         V(K)=C dotunion V(R)
\]

satisfies every clause of the audited pair-carrier peel.

* `K[C]` is connected by nonseparation and `K[V(R)]` is connected because
  `R` is a path.
* Both trace roots lie in the retained `R` side.
* `C` has the literal `q-A` edge.
* The marked set meets `C` at `p` and meets `R` by hypothesis.

Thus enlarging `A` by `C` and retaining `R` as the pair block preserves
the traces and all named adjacencies exactly as in the already-audited peel
theorem.  Both resulting blocks have literal contact with `L`.  Outcome 1
is GREEN.

## 3. Exact rotation branch

Assume `R cap P=empty`.  Since `P=N_G(L) cap V(K)` and `R,C` partition
`K`, every old carrier neighbour of `L` lies in connected `C`.  Put

\[
 K'=G[V(R)],\qquad A'=G[V(A) union C].
\]

The following checks are literal.

### Connectivity and disjointness

`K'` is connected.  The set `A'` is connected because `C` is connected,
`q in C`, and `q` has an actual edge to connected `A`.  The two blocks are
disjoint, as are both from unchanged `B` and `L`.

The connected graph `K` has an edge between its two nonempty parts
`R,C`; hence `K'` and `A'` are adjacent.

### Pairwise core adjacencies

The old `A-B` edge gives `A'-B`.  The whole pair trace `{x,y}` remains in
`K'`; its literal trace edges to the traces of both target blocks therefore
give `K'-B` and `K'-A subseteq A'`.  No completion edge is used.

### Traces

Every adhesion vertex of `K` is one of `x,y`, and both lie on `R`.
Therefore `C` contains no adhesion vertex.  The trace of `K'` is still
`{x,y}`, the trace of `A'` is exactly the old trace of `A`, and `B` is
unchanged.

### Exact transfer of the locked contact

Because `R cap P=empty` and `P` is the **full** set of `K`-neighbours of
`L`,

\[
                         N_G(L) cap V(K')=empty.
\]

Because `P subseteq C` and `P` is nonempty,

\[
                         E_G(L,A') ne empty.
\]

The standing anticompleteness of `L` to old `A union B` then says the
`L`-based decoration has moved from the pair block to the named target,
not merely acquired an abstract colour label.

Thus outcome 2 and equation (2.2) are GREEN.

## 4. Admissibility and raw-contact wording

The trace of `A'` is unchanged.  Hence the new geometric `W-A'` contact is
a supported decoration exactly when

\[
                         \{w\} union (A cap T)
\]

is independent.  If it is not, the offending literal `w`--trace edge is
the stated boundary-incompatibility certificate.  This caveat is exact.

However, `E(L,A union B)=empty` does not imply that `W={w} union L` has
raw contact only with `K`: `w` itself may see a trace vertex of `A` or
`B`.  Therefore the phrase “the unique raw decoration has moved” is valid
only under the inherited raw-rank-one hypothesis.  Without explicitly
importing that hypothesis, say instead:

> all literal contacts supplied by the locked region `L` have moved from
> the pair carrier to the named target `A`.

The formal theorem equations are unaffected.

## 5. Bilateral corollary

In Corollary 3.1, the original first-side core is supported and avoids the
side terminal.  The opposite shore supports the same labelled trace
`w->A`.  Admissibility depends only on the global literal edges from `w`
to that common trace, so the trace is admissible on the first shore as
well.

In the peel branch, the first side supports `w->A` through the new
`L-C-A` contact while retaining its pair decoration.  In the rotation
branch it supports `w->A` through `A'`.  All traces are unchanged, so in
both cases the bilateral decorated-overlap theorem receives exactly the
same equality state on both shores.  The six-colouring conclusion follows.

Thus Corollary 3.1 is GREEN under its stated supported-core hypotheses.

## 6. Scope for a spanning-rural cross

The final paragraph presently requires only that the cross portal `q` be
labelled to `A` or `B`.  That is necessary but not sufficient.

### Marked-end duty

The spanning pole `Y` may strictly contain `Y_0=L`.  A vertex

\[
                         p in P(K,Y)
\]

can have its only pole edge to `Y-L`; it need not belong to
`P_0=N_G(L) cap V(K)`.  The local proof then loses its dichotomy:

* although `C` contains the selected `p`, it need not contain an old
  `L`-attachment, so `R cap P_0 ne empty` does not necessarily give a peel
  with both sides meeting `P_0`; and
* if `R` avoids that selected new `p`, it need not avoid all of `P_0`, so
  equation (2.2) need not hold.

Therefore direct application requires

\[
 q\text{ has a literal edge to the named original target},
 \qquad p in N_G(L) cap V(K).
\]

Otherwise the cross is only a topological spanning-pole linkage and still
needs a label-assignment or endpoint-transfer lemma.

### Side-terminal duty

The spanning carrier is allowed to contain the side terminal `t`.  The
path partition puts `t` in either `R` or `C`, so after surgery it belongs
to `K'` or `A'`.  Earlier supported frame cores were required to avoid
`t`; hence the bilateral supported-state theorem cannot then be invoked
without a separate reassignment of `t`.

It is safe to apply Theorem 2.1 as a supported decoration rotation when
the relevant spanning carrier avoids `t`.  If it contains `t`, the theorem
still gives a connected trace-preserving **topological** three-block
surgery, but not automatically an eligible supported-core realization.

## 7. Corrected final implication

The audited local implication is

\[
\begin{array}{c}
xy\mid qp\text{ in a three-connected pair carrier},\\
q\text{ labelled to }A,\quad p in N_G(L) cap K\\
\Downarrow\\
\text{labelled peel or exact `L`-decoration rotation to }A.
\end{array}
\]

For a cross returned by the spanning-rural theorem, add the attained-duty
conditions

\[
 p in N_G(L) cap K,qquad t notin K,
\]

or separately prove how to transfer the marked endpoint and side terminal.
With those qualifications, no palette-to-label inference remains hidden.
