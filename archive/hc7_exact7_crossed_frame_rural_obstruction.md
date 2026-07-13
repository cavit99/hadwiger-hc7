# A supported crossed frame forbids the terminal-free disk outcome

**Status:** independently audited MIXED and corrected below.  Lemmas 2.1
and 3.1 are GREEN.  The former broad inference to a non-rural pole has been
retracted: a crossed frame forbids a single disk page with `U` on its
boundary, but both local pole societies may still be rural.

## 1. Exact crossed-frame setting

Let `U` be the literal five-set of the exact Moser cell.  Its present graph
`G[U]` is a five-cycle.  A supported frame core consists of three disjoint
connected pairwise adjacent sets

\[
                         K_0,A,B,
\]

whose traces partition `U` as two disjoint missing-cycle edges and the
remaining singleton.  Relabel the two pair traces as

\[
                    K_0\cap U=\{x,y\},\qquad
                    A\cap U=\{u,z\}.                         \tag{1.1}
\]

Thus `xy,uz` are disjoint nonedges of the present five-cycle.  The core is
contained in the terminal-free shore

\[
                         J_t^\circ=G[D_t\cup U].              \tag{1.2}
\]

This is exactly the protected core retained by the terminal-free
state-or-rural theorem and its low-cut descent.

## 2. A `U`-boundary disk page is impossible

### Lemma 2.1 (crossed-frame disk exclusion)

The graph `J_t^circ` has no embedding in a closed disk whose intersection
with the disk boundary is exactly the literal cycle `G[U]`.

#### Proof

On a five-cycle, the endpoints of two vertex-disjoint nonedges alternate.
Indeed, after writing the cycle in order, each nonedge is a diagonal; two
disjoint diagonals have alternating endpoints.  Hence the cyclic order of
the four vertices in (1.1), up to reversal, is

\[
                              x,u,y,z.                         \tag{2.1}
\]

Choose an `x-y` path in the connected set `K_0` and a `u-z` path in the
connected set `A`.  The two paths are vertex-disjoint because the core
blocks are disjoint.  In a disk embedding with `G[U]` as its boundary they
would be two disjoint arcs joining alternating boundary points (2.1),
contrary to the Jordan curve theorem.  \(\square\)

### Corollary 2.2 (exact cofacial obstruction)

The whole graph `J_t^circ` cannot be embedded in one closed disk with
`G[U]` as the boundary of that disk.

This does not contradict the audited terminal-free bilateral theorem.  Its
conditional implication

\[
 \text{two terminal-free disk pages}\Longrightarrow\chi(G)\le6.
\]

remains correct.  It also does **not** imply that either contracted pole has
a rotation obstruction.  Both pole societies may admit their prescribed
local disk substitutions, and the whole uncontracted shore may even be
planar, with `U` a separating rather than facial cycle.  Thus the obstruction
is global cofaciality, not induced-pole rurality.

## 3. Why the forced obstruction is not yet an attained-state exchange

Use a carrier-minimal rural triple

\[
              V(J_t^\circ)=K\mathbin{\dot\cup}X
                                      \mathbin{\dot\cup}Y,
\]

with `K_0 subseteq K`, `A union B subseteq X`, and the enlarged locked
region in `Y`.  Put

\[
 Q=(N_K(X)-\{x,y\}),\qquad P=(N_K(Y)-\{x,y\}).       \tag{3.1}
\]

The surviving rural branch has `Q cap P=empty` and no set-terminal cross:
there are no vertex-disjoint paths in `K`, one joining `x` to `y` and the
other joining a member of `Q` to a member of `P`.

The following elementary observation makes the duty mismatch exact.

### Lemma 3.1 (a carrier transfer would be a set-terminal cross)

Suppose `V(K)=R dotcup D`, both induced parts are connected,

\[
            x,y\in R,qquad q\in Q\cap D,qquad p\in P\cap D. \tag{3.2}
\]

Then `K` has a set-terminal cross.

#### Proof

Take an `x-y` path in `K[R]` and a `q-p` path in `K[D]`.  The two paths
are vertex-disjoint by the partition.  \(\square\)

Consequently one sharply defined transfer is impossible: a **single
connected** carrier set `D` cannot be moved to the target while `K-D`
remains connected and retains `x,y`, if `D` contains both an actual target
portal `q` and an actual locked attachment `p`.  Lemma 3.1 says nothing by
itself about simultaneous repartitions, pieces connected through a pole,
rerouting the retained pair through a pole, direct `w` contacts, reselecting
the model, or a proper-minor state transition.

The crossed-frame obstruction from Lemma 2.1 has a different type.  Its
second path lies in the **target pole** `X` (inside the old block `A`), not
in a connected carrier piece meeting `P`.  Equivalently, the tree-pole
rotation theorem can return two `Q-Q` carriers inside `X`, whereas the
attained decoration needs a `Q-P` carrier split across `K`.  Neither a
rooted `K_4` on four `Q`-ends nor a repeated `Q`-end collision by itself
supplies the missing literal `P` duty.

## 4. A concrete static countermechanism

The mismatch is not a wording artefact.  It occurs in literal rural triples
in which both local pole societies expand successfully.

Take a three-connected plane graph `K` with a facial cycle whose order is

\[
       x,Q,y,P,
\]

where `Q,P` are disjoint sets of at least three vertices each (and `P` may
be chosen of order at least five).  Add two connected anticomplete poles
`X,Y` so that

* every `X-K` edge ends in `Q` (apart from permitted root edges);
* every `Y-K` edge ends in `P`;
* `X` contains disjoint connected blocks with traces `{u,z}` and `{r}`;
  and
* `Y` is the connected locked region.

Choose the five boundary roots in cyclic order

\[
                              x,u,y,z,r,x,                       \tag{4.1}
\]

and retain the five literal cycle edges.  Inside `X`, join `u` to `z` by a
path disjoint from `K`.  The simple quotient obtained by contracting `X,Y`
is planar: the two pole stars occupy the two sides of the facial `x-y`
order.  It has no `xy | Q-P` linkage by the disk crossing theorem.

Nevertheless the uncontracted graph has no disk embedding with (4.1) on
the boundary, because the `x-y` path in `K` and the `u-z` path in `X` are
disjoint alternating arcs.  This is compatible with both pole societies
being rural: the graph can be planar with the five-cycle separating its two
crossed paths.  Lemma 3.1 excludes only the single connected carrier
transfer specified in Section 3, not every possible duty exchange.

This template is only a countermechanism to a **static** inference from a
planar rural quotient and a crossed frame to one `U`-boundary disk page.  It
is not asserted to be seven-contraction-critical or an `HC_7`
counterexample, and it does not rule out model reselection or a dynamic
state exchange.  The additional hypothesis which must now be spent is the
proper-minor transition family (or a literal `K_7` construction).

## 5. Correct next theorem

The task in this branch should therefore be stated as a dynamic conversion
theorem, not as forced failure of one pole expansion:

> **Crossed-pole duty conversion.**  In a carrier-minimal terminal-free
> rural page of the exact `HC_7` cell, the protected crossed frame,
> together with the full proper-minor transition family, yields a
> duty-correct carrier exchange, a literal `K_7`, an equality state
> supported on the opposite shore, or a coherent multi-page structure
> admitting the required six-colouring.

Without the transition family the rural template of Section 4 falsifies
the corresponding static implication.  Any carrier outcome must discharge
the attained decoration duty; a raw `Q-Q` or `Q-P` contact is not enough.
