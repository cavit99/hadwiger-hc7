# Candidate: the minimum twin shell closes before the double lock

**Status:** scope diagnosis with an elementary proof and a deletion-minimal
Z3 core; independent audit pending.  This is a bounded instance of the
already-audited degree-three carrier peel, not a new double-lock theorem.

## 1. Literal shell

Use the `double_conflict` boundary in the separating-decoder falsifier:

\[
 S=\{0,1,2,3,4,5,6\},\qquad u=0,
\]

\[
 I=\{3,5,6\},\quad A_0=\{1,2\},\quad B_0=\{0,4\},
\]

and

\[
 E(H)=\{04,12,16,35,36,46\}.
\]

The minimum twin shore consists of two edges
`D={d0,d1}`, `E={z,e1}` and two gates `Z={p,q}`.  Each gate is adjacent
to every vertex of both lobes, `zu` is the unique old-boundary edge at
`u`, and there is no gate--gate edge.  The normal form gives the contact
containments

\[
 N_S(D)\subseteq I\cup A_0,
 \quad N_S(E)\subseteq I\cup B_0,
 \quad N_S(p)\cup N_S(q)\subseteq I.
\tag{1.1}
\]

## 2. Static closure

### Lemma 2.1

In a seven-connected host satisfying (1.1), the minimum twin shell admits
the adaptive two-carrier return.  No colouring response or lock is needed.

### Proof

Apply seven-connectivity to the following three connected thin sets.

For `X={p}`, the four vertices `d0,d1,z,e1` are all its internal
neighbours.  There is no edge from the thin shore to the old opposite
shore, so

\[
                 |N_S(p)|\ge 7-4=3.
\]

By (1.1), \(N_S(p)\subseteq I\), where \(|I|=3\).  Hence `p` contacts all of
`3,5,6`.

For `X=D`, its only internal external neighbours are `p,q`.  Therefore

\[
                 |N_S(D)|\ge 7-2=5.
\]

The allowed set \(I\cup A_0\) has order five, so `D` contacts all of
`1,2,3,5,6`.

Finally, for `X={e1}`, its internal neighbours are `z,p,q`.  The unique
edge at `u=0` is `zu`, so `e1` can contact only the four labels
`3,4,5,6`.  Seven-connectivity forces

\[
                 |N_S(e1)|\ge 7-3=4,
\]

and hence `e1` contacts all four.

Now put

\[
 C_1=\{p,z\},\qquad C_2=D\cup\{e1,q\}.
\]

These sets are disjoint, connected and adjacent.  They fund respectively
the independent seeds

\[
 J_1=\{0,5,6\},\qquad J_2=\{2,3,4\},
\]

while `U={1}` is a clique reservoir.  Indeed `z` contacts `0`, `p`
contacts `5,6`, `D` contacts `2,3`, and `e1` contacts `4`.  Both displayed
seed sets are independent in `H`.  Thus

\[
                    S=J_1\mathbin{\dot\cup}J_2
                         \mathbin{\dot\cup}U
\]

is an adaptive two-carrier allocation.  The audited adaptive
clique-reservoir theorem then six-colours the host.  \(\square\)

## 3. Machine core and falsifier consequence

Run

```text
HC7_ROOT_FULL=0 HC7_CORE_CUTS=1 python3 -u \
  active/hc7_atomic_twin_seam_static_core_probe.py
```

The solver returns `UNSAT` and deletion-minimizes to exactly four clauses:

```text
cut X={p} needs 3 old contacts
cut X={d0,d1} needs 5 old contacts
cut X={e1} needs 4 old contacts
forbid the carrier return
  {p,z} | {d0,d1,e1,q}
  on {0,5,6} | {2,3,4} | {1}
```

This is precisely the proof above.  In particular the existing
`hc7_atomic_twin_seam_separating_decoder_falsifier.py` reports no survivor
before it asks for a bridge lock, a `G/f` response, or a double-contraction
state.  Its negative output on this shell is therefore **not evidence for
the double-lock decoder**.  A useful decoder falsifier must begin with a
larger literal twin topology that survives every static adaptive return.

The statement is bounded to this minimum shell and this boundary form.  It
does not imply the active unbounded theorem and supplies no strict global
rank.

The mechanism is not new: `e1` has thin degree three and `A-e1` is
connected, so this shell lies in the hypotheses of the audited
degree-three receiver peel.  The explicit allocation above certifies that
its outcome is the already-closed adaptive-return branch.  Consequently a
meaningful double-lock falsifier must exclude every such static peel at the
input, rather than crediting its `UNSAT` result to response coupling.
