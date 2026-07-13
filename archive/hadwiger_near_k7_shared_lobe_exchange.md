# Shared dark-lobe exchange: exact-seven descent and the sharp 2-apex boundary

## 1. Taxonomy correction

Three logically different objects were previously called a
"shared-lobe residue".

1. **Rooted-extension collision.**  One dark off-torso lobe `D`, with
   two actual torso poles `p,q`, is the only named lobe available for two
   private extension roles.  A copy rooted at either pole must retain the
   same literal pool/reserve rows.  This is the active-root residue treated
   below.
2. **Reserve consumption.**  Four private rooted extensions have already
   been selected, but every connected reserve with a positive row against
   the four protected bags and the two pools consumes one of those bags.
   This is the zero-row state of
   `hadwiger_four_common_owner_biportal_application.md`.  It is not
   settled by splitting the lobe in item 1.
3. **Carrier localization.**  The full-state bi-Helly theorem localizes
   intersecting carrier families in one block/cycle/3-connected torso.
   This is a mechanism leading to item 1 or 2, not a third terminal.

The unusable-incidence theorem concerns four **distinct** lobes and does
not address item 1.  Conversely, the theorem below does not claim to fill
the reserve zero row in item 2.

## 2. Literal shared-extension data

Let `G` be seven-connected.  Let `D` be a component behind an exact
seven-boundary

\[
             S=\{p,q,s_1,s_2,s_3,s_4,s_5\},
             \qquad N_G(D)=S.                                  \tag{2.1}
\]

In the one-complex shell, `p,q` are the two actual torso poles of a dark
lobe and the five `s_i` are precisely the literal singleton labels seen
by that lobe.  Fix three distinct common pool/reserve labels, say
`s_1,s_2,s_3`, and put

\[
 A_p=N_D(p),\quad A_q=N_D(q),\quad
 R_i=N_D(s_i)\quad(1\le i\le3).                                \tag{2.2}
\]

A **`p`-extension carrier** is a connected subgraph of `D` meeting
`A_p,R_1,R_2,R_3`; a **`q`-extension carrier** is defined symmetrically.
Two disjoint such carriers, after adjoining `p` and `q`, give two private
extensions which both retain the three common literal contacts required
by the biportal completion.  The other two private extensions and the
rest of the completion are held fixed.

The restriction to literal common rows is important.  If one of the
three required contacts is itself a composite reserve carrier, its
consumption is taxonomy item 2, not the statement below.

## 3. The block tree cannot carry the collision

### Theorem 3.1 (shared lobe: split or exact-seven block descent)

In the setting of Section 2, at least one of the following holds.

1. `D` contains disjoint `p`- and `q`-extension carriers.
2. One bag `Z` of the block decomposition of `D` meets every carrier of
   one of the two roles.  For every component `K` of `D-Z` there is a
   named required boundary vertex `t` for that role such that
   \[
           N_G(K)=(S-\{t\})\mathbin{\dot\cup}\{z_K\},           \tag{3.1}
   \]
   where `z_K` is the unique attachment of `K` in `Z`.

In particular every nonempty off-core component is behind a new literal
exact seven-cut.  Thus an unsplit collision cannot propagate through an
arbitrary block tree: repeated descent terminates in one 2-connected
block, one edge block, or a singleton capacity core.

#### Proof

Apply Theorem 2.1 of `hadwiger_full_state_shore_bihelly.md` to the two
carrier families and the standard block tree decomposition of `D`, whose
adhesion has order at most one.  In that theorem take the neutral rows to
be `Q_1=R_1,Q_2=R_2`, and take

\[
                         A=A_p,\qquad B=R_3,\qquad C=A_q,
\]

with state type zero.  Its left carriers are exactly the `p`-extension
carriers and its right carriers are exactly the `q`-extension carriers.
If two carriers are disjoint, outcome 1 holds.  Otherwise one block bag
`Z` meets every carrier of one role.

Take a component `K` of `D-Z`.  The bi-Helly theorem says that `K` misses
one portal row required by the obstructed role and has at most one
neighbour in `Z`.  Let `t` be the corresponding member of
`{p,s_1,s_2,s_3}` or `{q,s_1,s_2,s_3}`.  As `D` is a component of
`G-S`,

\[
                 N_G(K)\subseteq(S-\{t\})\cup\{z_K\},          \tag{3.2}
\]

where the last set has order at most seven.  The vertex `t` lies outside
`K` and is not adjacent to it, so `N_G(K)` genuinely separates `K` from
`t`.  Seven-connectivity gives `|N_G(K)|>=7`.  Equality therefore holds
throughout (3.2): `K` has one actual attachment `z_K`, sees all six other
vertices of `S`, and (3.1) follows.  QED.

No torso edge is used in this proof.  Every edge certifying (3.1) is an
edge of the original graph.

### Corollary 3.2 (the 2-connected residue is exact seven/eight or one torso)

Suppose the two carrier roles still have no disjoint representatives.
Refine the block decomposition of `D` by a Tutte decomposition inside
each 2-connected block, attaching every old block-tree branch at a bag
which contains its cutvertex.  Apply cross-Helly to this adhesion-at-most-
two decomposition of the **whole graph `D`**.  Then one
gate/cycle/3-connected torso `W` meets every carrier of one role.  Every
component `K` of `D-W` misses a named required boundary row and satisfies

\[
                         7\le |N_G(K)|\le8.                    \tag{3.3}
\]

Consequently it lies behind an exact seven-cut or an exact order-eight
two-gate.  In the latter case it sees the other six vertices of `S` and
has two actual attachments in `W`.

#### Proof

The refined decomposition is a tree decomposition of all of `D`, not
only of the bare block core; this keeps old exact-seven branches inside
the relevant component rather than counting their attachment as a new
external neighbour.  It has adhesion at most two.  As above, a component
off the common torso misses one boundary vertex `t`, and hence

\[
                  N_G(K)\subseteq(S-\{t\})\cup Z_K,
                  \qquad |Z_K|\le2.
\]

This is a genuine separator.  Seven-connectivity gives the lower bound
in (3.3), and the displayed containment gives the upper bound.  If the
order is seven or eight, deleting unused displayed vertices gives the
stated exact boundary.  An order-seven boundary need not contain all six
vertices of `S-{t}`: it may use both gate vertices and omit one further
old boundary contact.  Only in the order-eight case does equality force
all six remaining boundary contacts and both actual gate attachments.
QED.

Thus the rooted-extension collision has a sharp uniform form:

```text
two private carriers
    or nested exact 7
    or exact 8 two-gate
    or one cycle/3-connected shared-role torso.
```

The first outcome re-enters the active-root facial theorem.  The second
is a faithful minimum-separator descent.  The last two outcomes are the
genuine operation-sensitive residue; ordinary connectivity cannot remove
them.

## 4. A 7-connected coherent-2-apex witness

The coherent-2-apex alternative is necessary even with an actual
singleton dark lobe.

Let `I` be the icosahedral graph on vertices `0,...,11`, with edge set

\[
\begin{split}
&01,05,07,08,0\,11,12,15,16,18,23,26,28,29,34,36,39,3\,10,\\
&45,46,4\,10,4\,11,56,5\,11,78,79,7\,10,7\,11,89,9\,10,10\,11.
\end{split}                                                     \tag{4.1}
\]

Let `u,v` be adjacent new vertices, each adjacent to every vertex of
`I`, and put

\[
                         G=K_2\vee I.                           \tag{4.2}
\]

### Proposition 4.1 (sharp shared-lobe counterarchitecture)

The graph `G` has all of the following properties.

1. `G` is seven-connected and has no `K_7` minor.
2. The six singleton vertices
   \[
          a=4,\quad b=0,\quad c=1,\quad r_1=u,\quad r_2=v,
          \quad r_3=5
   \]
   induce exactly `K_6-{ab,ac}`.
3. With
   \[
                       B=\{2,3,6,7,8,9,10,11\},                \tag{4.3}
   \]
   the six singleton bags and the connected bag `B` form a spanning
   `K_7^\vee` model.
4. `D={11}` is a dark exact-seven lobe of `B` with torso poles `7,10`:
   \[
       N_B(11)=\{7,10\},\qquad
       N_{\{a,b,c,r_1,r_2,r_3\}}(11)
          =\{a,b,r_1,r_2,r_3\}.                                \tag{4.4}
   \]
   Hence `D` may be rooted at either pole and has any three common
   literal pool/reserve contacts chosen from the five displayed rows,
   but it cannot be split into two nonempty private carriers.
5. Deleting `u,v` leaves the planar graph `I`; the obstruction is
   therefore exactly in the coherent-2-apex branch.

#### Proof

The icosahedral graph is planar and five-connected.  Deleting at most six
vertices of `G` leaves a universal apex unless both `u,v` were deleted;
in the latter case at most four vertices of `I` were deleted, and
five-connectivity keeps the remainder connected.  Conversely, deleting
`u,v` and the five neighbours in `I` of any icosahedral vertex isolates
that vertex.  Thus `kappa(G)=7`.

If `G` had a `K_7` model, at most two of its branch bags could contain
`u,v`.  The other five bags would be connected subgraphs of `I` and
would remain pairwise adjacent inside `I`, giving a `K_5` minor in the
planar graph `I`, a contradiction.

The remaining assertions follow directly from (4.1).  The only absent
edges among the six displayed singleton vertices are `40` and `41`.
The induced graph `G[B]` is connected, and every singleton label has a
neighbour in `B`.  Finally vertex `11` has icosahedral neighbours
`0,4,5,7,10` and is adjacent to both join apices, giving exactly (4.4)
and its seven-vertex neighbourhood.  QED.

The proposition does not assert that this named lobe is the unique
global way to choose all four extensions; it is a counterexample to any
**local** theorem claiming that exact-seven darkness and
seven-connectivity alone split the named lobe or force `K_7`.

## 5. Exact remaining theorem

After the occurrence closure and Theorem 3.1, the only plausible uniform
rooted-model principle for taxonomy item 1 is now:

> **Atomic shared-lobe exchange.**  In a 7-contraction-critical
> one-complex shell, an unsplittable 2-connected exact-seven lobe with
> three literal common rows either (i) realizes the two private carriers,
> (ii) has a faithful proper-minor state which glues across one of the
> exact order-eight gates of Corollary 3.2, or (iii) all of its active
> torso and lobe occurrences admit one compatible rural disk expansion,
> yielding the coherent-2-apex alternative.

Proposition 4.1 shows why outcome (iii) cannot be omitted.  Corollary 3.2
shows that a proof need only handle one 2-connected torso and exact
order-eight gates; it does not need to enumerate arbitrary block trees.
Reserve-zero-row consumption remains a separate operation-state problem.
