# Cross-lobe rooted-`K_4` handoff

**Status:** proved and independently audited.  The structural reduction is
literal.  A frozen catalogue of 293 monotone certificates covers all 2,048
minimal quotients and is replayed without a solver by
`hc7_exact7_cross_lobe_rooted_k4_handoff_replay.py`.

## 1. Input and purpose

Use the attained paired state

\[
 S=\{c,a_1,t_1,a_2,t_2,a_3,t_3\},\qquad
 \Pi=\bigl\{\{a_i,t_i\}:i\in[3]\bigr\}\cup\{\{c\}\}.
 \tag{1.1}
\]

Thus every `a_i-t_i` is a nonedge, `c` has a literal neighbour in each
pair, and every two different pairs have a literal edge between them.
Let `P,Q` be disjoint connected `S`-full packets.  They need not be
adjacent.

The cross-lobe facial word is, after relabelling and reversing the face,

```text
a1 a2 a3 t1 t2 t3.
```

Any three-linkage between the three displayed `a` portals and the three
displayed `t` portals in the disk therefore has the reversed pairing

\[
                 a_1t_3,\qquad a_2t_2,\qquad a_3t_1.
\tag{1.2}
\]

The candidate theorem below discharges the branch in which this reversed
linkage has a rooted `K_4` expansion.  It does **not** assert that every
crossless web has such an expansion.

## 2. Rooted expansion

Call four pairwise disjoint connected sets

\[
                         R,H_1,H_2,H_3                 \tag{2.1}
\]

a **reversed rooted-`K_4` expansion** when they are pairwise adjacent and

\[
\begin{array}{c|c}
H_1& a_1,t_3\\
H_2& a_2,t_2\\
H_3& a_3,t_1
\end{array}                                             \tag{2.2}
\]

lists literal boundary vertices having a neighbour in that set.  Require
also that `c` has a neighbour in at least one member of (2.1).  All four
sets are disjoint from `S union P union Q`.

### Candidate Theorem 2.1 (rooted-`K_4` gives the `S1` handoff)

Under (1.1)--(2.2), `G` contains a literal `K_7^vee` model, where
`K_7^vee` denotes `K_7` with two incident edges deleted.

The output is label-faithful: every returned branch set is the expansion
of an explicitly named quotient bag using only

```text
c,a1,t1,a2,t2,a3,t3,R,H1,H2,H3,P,Q.
```

The quotient verifier designates one branch as the deficient row and two
other branches as its only permitted nonneighbours.  Expanding `R,H_i,P,Q`
back to their literal connected sets therefore gives a named near-`K_7`
model, suitable as an `S1` handoff.

## 3. Finite monotone proof reduction

Contract each of `R,H_1,H_2,H_3,P,Q` to a named quotient vertex
`r,h1,h2,h3,p,q`.  Retain only:

* the six edges of the `K_4` on `r,h1,h2,h3`;
* `h1-a1,h1-t3`, `h2-a2,h2-t2`, and `h3-a3,h3-t1`;
* one edge from `c` to one of `r,h1,h2,h3`;
* every `p-S` and `q-S` edge; and
* one witness edge for each of the six requirements in (1.1).

There are

\[
                  4\cdot 2^3\cdot4^3=2048             \tag{3.1}
\]

minimal quotients.  Additional literal edges are harmless by
minor-monotonicity.

The discovery verifier checks all 2048 cases.  For each uncovered minimal
boundary it asks for seven disjoint connected quotient bags which are
pairwise adjacent except possibly for two pairs sharing one designated
deficient bag.  It then independently checks the returned bags using
ordinary adjacency and connectedness routines.  A certificate is reused
for another boundary only after deleting every unadvertised optional edge
and checking the same literal bags in that smaller graph.

The frozen catalogue
`hc7_exact7_cross_lobe_rooted_k4_handoff_catalogue.json` contains 293 such
monotone certificates.  The independent solver-free replay reconstructs
the 512 boundary choices for each of the four possible `c` contacts, checks
every advertised bag for connectedness, disjointness, and the nineteen
required adjacencies, and confirms monotone coverage of all 2,048 cases.
All checks use explicit exceptions rather than Python assertions and remain
active under `python -O`.

This is stronger than a finite-order graph census: the four rooted sets and
two packets may have arbitrary order, because the quotient model expands
literally.

The conclusion cannot be upgraded to `K_7` from these static hypotheses.
The explicit width-five quotient in
`../barriers/hc7_exact7_rooted_k4_k7_upgrade_barrier.md` satisfies every
input above and contains the advertised `K_7^vee`, but has no `K_7` minor.
Dynamic criticality or a genuine composition theorem is therefore required
after this handoff.

## 4. Exact remaining implication

Combined with the crossless common-face reduction, the only unhandled
cross-lobe geometry is now:

> a three-connected planar society with facial word
> `a1 a2 a3 t1 t2 t3` in which every reversed three-linkage has no rooted
> `K_4` expansion preserving its three named traces.

This is the parallel/vital-strip branch of the six-terminal web.  The
present theorem does not transfer the attained state through its first
composition split and does not close that branch.  It isolates the exact
state-preserving strip implication; arbitrary cofacial societies no longer
need to be treated together with the rooted-expansion outcome.
