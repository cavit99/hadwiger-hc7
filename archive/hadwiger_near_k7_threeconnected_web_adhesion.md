# RETRACTED OVERREACH: a web gate need not induce a literal triangle

## 1. Status

**Retracted.**  Fabila--Monroy--Wood returns a spanning subgraph of a web,
so the three edges of a facial triangle may be completion edges absent from
the original graph.  The valid replacement and an explicit counterexample
are in `../results/hc7_exact7_rooted_portal_face_closure_audit.md`, Section 6.
Only the existence of a literal three-vertex gate survives without an
additional clique hypothesis.

This note removes the phrase "a merely three-connected nonplanar torso"
from the near-`K_7` rooting problem.  It does **not** prove `HC_7`.

The point is that the nonplanar alternative in the three-connected
rooted-`K_4` theorem is not an arbitrary nonplanar graph.  In a spanning
one-complex near-clique shell it contains a literal nonempty component
behind three actual gate vertices.  Seven-connectivity then forces that
component to have at least four literal contacts with the six singleton
shell labels.  With exactly four shell contacts it is already behind an
actual exact seven-cut.

Thus the active-torso route has the following uniform output:

```text
rooted active K4 -> labelled K7;
planar torso      -> one active face (and, with occurrence coverage,
                     the coherent two-apex expansion);
nonplanar torso   -> a triangle gate exposing an order-7/8 adhesion lobe.
```

No portal enumeration is used.

## 2. The web-cell lemma

We use the standard definition of Fabila--Monroy and Wood.  If `R` is a
plane graph whose internal faces are triangles and every triangle of `R`
is facial, form `R^+` by assigning to each facial triangle `T` a possibly
empty clique `X_T`, disjoint from `R` and from all other such cliques, and
making every vertex of `X_T` adjacent to every vertex of `T`.  An
`(a,b,c,d)`-web is such an `R^+` with `a,b,c,d` on the outer face in that
order.  A graph is a spanning subgraph of the web: edges of `R^+` need not
all be present in the graph under consideration.

### Lemma 2.1 (nonplanarity exposes a nonempty facial cell)

Let `H` be a three-connected graph and let `a,b,c,d` be distinct vertices.
If `H` has no `K_4` minor rooted at `a,b,c,d`, then one of the following
holds.

1. `H` is planar and `a,b,c,d` lie on one face.
2. There are a triangle `T={t_1,t_2,t_3}` and a nonempty component `K`
   of `H-T`, disjoint from the four roots, such that
   
   \[
                         N_H(K)=T.                            \tag{2.1}
   \]

#### Proof

By Theorem 8 of Fabila--Monroy and Wood, `H` is a spanning subgraph of an
`{a,b,c,d}`-web `R^+`.  The four roots belong to the outer face of the rib
`R`.

If every web cell were empty, `H` would be a spanning subgraph of the
plane rib and hence planar.  Thus in the nonplanar branch some cell
`X_T` is nonempty.  Let `K` be a component of `H-T` which meets that
cell.  A web-cell vertex has no neighbour outside its cell and the three
vertices of the associated triangle, so `N_H(K) subseteq T`.
Three-connectivity and the outer root outside `T` force every vertex of
`T` to have a neighbour in `K`; otherwise at most two vertices separate
`K` from the outer roots.  This proves (2.1).  Cell vertices are disjoint
from the rib, so no nominated outer-face root lies in `K`.  QED.

The lemma makes no assertion about the distribution of the three gate
contacts among vertices of `K`.  In particular it does not infer two
vertices complete to `T`: cross-edges among partially attached cell
vertices make that inference false.

## 3. Active roots make the theorem label-preserving

Retain the active-extension notation of
`hadwiger_near_k7_active_root_face_exchange.md`.  Thus four disjoint
connected extensions `E_1,...,E_4` meet a torso `H` only at distinct roots
`p_1,...,p_4`, and the common pool/reserve bags have exactly the literal
contacts required by the uniform biportal completion.

### Theorem 3.1 (three-connected active-torso trichotomy)

Let `H` be three-connected and suppose the four selected extensions form
an active quadruple.  Then at least one of the following holds.

1. The ambient graph contains the labelled `K_7` model supplied by the
   biportal completion.
2. `H` is planar and `p_1,p_2,p_3,p_4` lie on one face.
3. `H` has the literal triangle-gated component of Lemma 2.1, disjoint
   from the four private extensions except possibly through its three gate
   vertices.

If the portal family of four fixed disjoint extensions has rank four,
outcome 2 puts **every usable portal occurrence** on one common face,
unless outcome 1 or 3 occurs for some active transversal.

#### Proof

If `H` contains a rooted `K_4` at the active quadruple, adjoin the four
private extensions to its four rooted bags and apply the uniform biportal
rooted-core theorem.  This is outcome 1.  Otherwise Lemma 2.1 gives outcome
2 or 3.

For the final assertion take all role-respecting SDRs of the four portal
sets.  Their underlying four-sets are the bases of a rank-four transversal
matroid and its basis-exchange graph is connected.  If outcome 3 never
occurs, every active transversal lies in the planar branch.  The
three-overlap facial-coherence proof then puts adjacent bases, and hence
all bases, on one face; every usable occurrence lies in some base.  QED.

This theorem extends the earlier active-face theorem from
"four-connected or planar three-connected" to **all** three-connected
torsos.  The price is the literal triangle lobe in outcome 3; there is no
unstructured nonplanar residue.

## 4. Seven-connectivity turns the cell into an order-7/8/9 adhesion

Now use the spanning one-complex shell

\[
                         V(G)=L\mathbin{\dot\cup}B,
                         \qquad |L|=6,                       \tag{4.1}
\]

where `L` is the set of six singleton labels of a `K_7^vee` model and
`B` is connected.  Suppose `B` is the three-connected torso to which
Theorem 3.1 is applied.

### Theorem 4.1 (literal triangle-adhesion output)

Assume `G` is seven-connected and outcome 3 of Theorem 3.1 occurs in
`B`.  Put

\[
                         Z=T\mathbin{\dot\cup}N_L(K).          \tag{4.2}
\]

Then

\[
                         N_G(K)=Z,
                         \qquad |N_L(K)|\in\{4,5,6\}.         \tag{4.3}
\]

Thus the actual adhesion order is `7`, `8`, or `9`.  In the order-seven
case every component behind the separator is full to all seven vertices
of `Z`.

#### Proof

Equation (2.1) gives all neighbours of `K` inside `B`.  Since (4.1) is
spanning, every remaining neighbour lies in `L`, proving the equality in
(4.3).  The outer rib contains the four active roots, so it contains a
vertex outside `K union Z`; consequently `Z` is an actual separator.
Seven-connectivity gives `|Z|>=7`, and `|T|=3`, whence
`|N_L(K)|>=4`.  The opposite inequality is `|L|=6`.

If `|Z|=7` and a component `C` of `G-Z` missed some `z in Z`, then at
most the other six vertices of `Z` separate `C` from `z`, contradicting
seven-connectivity.  Hence every component is full to `Z`.  QED.

### Theorem 4.2 (the order-nine cell has an order-seven/eight partner)

Assume in addition that `G` has no `K_7` minor.  For the triangle `T`
returned by Theorem 3.1, some component `D` of `B-T` satisfies

\[
                         7\le |N_G(D)|\le8.                    \tag{4.4}
\]

#### Proof

If the component `K` from Theorem 4.1 has boundary at most eight, take
`D=K`.  Otherwise `K` is full to all six singleton labels and
`N_G(K)=T union L` has order nine.

At least one other component of `B-T` contains an outer-face active root
not in `T`; call such a component `D`.  Seven-connectivity gives
`|N_G(D)|>=7`, while every neighbour of `D` lies in `T union L`, so the
order is at most nine.  If it were nine, both `K` and `D` would be full to
`L`.  Write

\[
                       L=\{v,b_1,b_2,b_3,b_4,b_5\},             \tag{4.5}
\]

where the five `b_i` form the clique in the literal `K_7^vee` shell.
Then

\[
                 K\cup\{v\},\quad D,\quad
                 \{b_1\},\ldots,\{b_5\}                       \tag{4.6}
\]

are seven pairwise adjacent connected bags.  Indeed `K` and `D` both
see every member of `L`; the edge from `D` to `v` supplies the adjacency
between the first two bags, and the five singleton bags form a clique.
This is a `K_7` model, contrary to the hypothesis.  Hence the selected
partner `D` has boundary at most eight, proving (4.4).  QED.

This is the web-specialized form of the general three-cut conclusion in
Theorem 8.3 of `hadwiger_k7vee_constant_owner_corridor.md`.  The proof is
included to audit that the returned order-seven/eight shore uses actual
vertices and literal shell adjacencies; no virtual torso edge is used.

## 5. Consequence for arbitrary `K_7^vee` rooting

Combine the ordered-source theorem, the constant-owner corridor collapse,
and the literal-row ear collapse.

* The ordered source has a bounded event kernel joined by induced bridge
  corridors.
* A corridor either enters an actual exact seven-boundary or lies in the
  two-connected ear closure of the enlarged sole complex bag.
* Applied recursively, the ear closure either descends again through an
  exact seven-boundary or reaches a cell in which the enlarged spanning
  complex bag itself is three-connected.  This is the branch used below;
  no virtual torso edge is treated as a literal edge.
* For four fixed private roles of rank four, Theorems 3.1 and 4.2 replace
  that last torso by a labelled `K_7`, one active planar face, or a
  triangle-gated order-7/8 lobe.

If the planar face contains every occurrence used by the retained quotient,
the existing port-labelled disk expansion gives the coherent two-apex
outcome.  If it does not, the first uncovered occurrence is again a shared
role or exact-adhesion event.

Accordingly, once the descent has reached a **literal spanning**
three-connected bag, the phrase "one remaining three-connected nonplanar
torso" is no longer an exact frontier.  The exact frontier after this note
is:

> an actual order-seven/eight state shore, or a prior failure to extract
> four disjoint active extensions.

At four labels the web lobe itself is an exact-seven state shore.  At five
labels it has order eight.  If it has all six labels, Theorem 4.2 returns
a different order-seven/eight component at the same triangle.  Closing
those state shores requires the faithful minor-state exchange; ordinary
rooted-model or connectivity arguments have now been exhausted at the
torso level.

## 6. The resulting split-versus-rural theorem

The preceding argument can be stated as one reusable conditional theorem.

### Theorem 6.1 (active near-clique split versus coherent two-apex)

Let `G` be seven-connected and `K_7`-minor-free and let

\[
                  V(G)=L\mathbin{\dot\cup}B,
                  \qquad |L|=6,
\]

be a spanning literal one-complex `K_7^vee` shell.  Assume that four
pairwise disjoint private extension roles have been selected in `B` and
have the common pool/reserve contacts of the uniform biportal completion.
Assume also that:

1. their portal family has rank four;
2. every attachment occurrence used by the reconstruction after deleting
   two fixed singleton labels belongs to an active transversal; and
3. all pieces outside the active core have rural drawings in the prescribed
   quotient rotations.

Then at least one of the following holds.

1. `G` contains the labelled `K_7` supplied by the active rooted model;
2. a nonempty proper shore of `B` has an actual boundary of order seven or
   eight in `G`;
3. deleting the same two fixed singleton labels leaves a planar graph.

#### Proof

Apply the literal-row ear collapse.  A two-cut either supplies outcome 2
(an order-eight full lobe is allowed) or the enlarged spanning bag is
three-connected.  Apply the audited three-cut theorem, including the
`K_4` edge case in
`hadwiger_k7vee_threecut_active_torso_audit.md`.  It supplies outcome 1 or
2, or leaves a genuinely four-connected active bag.

In the latter case choose any active SDR.  The four-connected rooted-`K_4`
theorem supplies a rooted model, which is outcome 1 after adjoining the
private extensions, or makes the bag planar with the four roots on one
face.  Basis exchange and the active-face theorem put every usable
occurrence on that same face.  Hypothesis 2 says these are all occurrences
needed by the retained reconstruction, and hypothesis 3 supplies rural
drawings for all remaining pieces in their fixed rotations.  Port-labelled
disk substitution therefore draws the whole graph minus the two fixed
labels in the plane, which is outcome 3.  QED.

The theorem identifies the exact missing input for an unconditional
arbitrary-model result.  It is not another nonplanar-torso theorem.  It is
the extraction/operation theorem which must either produce the four active
private roles with occurrence coverage, or descend through the actual
order-seven/eight shore in outcome 2.  This is precisely the bilateral
two-role-loss exchange being pursued on the faithful-state route.
