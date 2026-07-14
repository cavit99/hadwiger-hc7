# Independent audit: four-connected portal exchange

**Verdict:** GREEN.

**Audited source:**
`results/hc7_exact7_four_connected_portal_exchange.md`

**Source SHA-256:**
The mathematical body audited before promotion had SHA-256
`5cc92bb8e67e80c127446d5eb5673e6886b5e1e76ae65a7e2698a9c2ce983eda`.
Promotion changed only the status line and file location.
The promoted source hash is
`1a799ca2eba62b2d344ab647c4e4ecad62f9d8c5ce49c35a045f109dc2ee875b`.

**Pinned dependencies:**

* prescribed portal extension:
  `466089f128c9e7352828c8bda05ea61a19efe9b06747489d550f38f29551bc3a`;
* active-root SDR facial coherence:
  `2209d090ec526ad0ae383cf2599bfe1cb3917c2784d7ffc5d6b73119d4ccfbd1`;
* cofacial portal degree obstruction:
  `436d7875339e16401ed98d476e4d60f8ecaff265c495fc53cbcb375e7d4bfbc2`.

## 1. Literal setup and portal quantifiers

If `mathcal P_s=N_L(s)` were empty, then `N_G(L) subseteq S-{s}`;
deleting those at most six vertices would separate the nonempty shore `L`
from the nonempty shore `R`.  Thus seven-connectivity makes every portal
set nonempty.

For every two-set `Y subseteq W`, every `s in A_Y=D union Y`, and every
literal portal `z in mathcal P_s`, the source applies the
prescribed-portal theorem to the exact four-set `A_Y` and the prescribed
edge `sz`.  Four-connectivity
gives `|L|>=5`, so that theorem's `X=L`, `|X|<=3` alternative is
impossible.  Its descent alternative gives exactly the source's outcome
2: `U subseteq A_Y-{s}`, hence `U subseteq A_Y`; `1<=|U|=|X|<=3`;
`Omega=(S-U) union X` is an actual seven-boundary; and `L-X` is the
unique connected, nonempty, full, strictly smaller shore.

Consequently, if no descent occurs, the extension conclusion holds for
**every** portal edge of each of the six families `A_Y`, not merely for
one selected representative.  This is precisely the hypothesis needed by
the SDR facial-coherence theorem.  Overlap among portal sets causes no
problem: the images of the saturating matchings are the bases of the
rank-four transversal matroid, and every portal vertex of a displayed
family occurs in a basis because its own incident edge can be prescribed.

## 2. Rooted-model branch

Let the rooted `K_4` bags be `B_s`, `s in A_Y`, with the selected portal
representative of label `s` lying in `B_s`.  The enlarged bags

`B_s union {s}`

are connected through literal portal edges, remain pairwise disjoint, and
remain pairwise adjacent.  They are disjoint from the packet bags `P,Q`
and from `{c}` because `A_Y subseteq S-{c}`, the rooted bags lie in `L`,
and the packets lie in `R`.

All adjacencies among the six rim bags are literal:

* the four enlarged rooted bags inherit their `K_4` adjacencies;
* each of `P,Q` meets each enlarged rooted bag through the bag's boundary
  anchor, by `S`-fullness; and
* `P,Q` meet through the assumed literal packet edge.

Thus they form a literal `K_6`.  The singleton `{c}` meets `P,Q` by
fullness and meets the two bags anchored at `d_1,d_2` through the literal
edges `cd_i`.  It may miss only the two rooted bags anchored at the two
members of `Y`.  Hence at most two rim adjacencies are absent, and both
are incident with `{c}`.  Ignoring surplus edges yields exactly the
permitted labelled `K_7^vee` pattern.

## 3. Johnson-family face synchronization

In the no-rooted-model branch, facial coherence supplies, for each
two-set `Y subseteq W`, a face `F_Y` containing the **complete** portal
union

\[
             \mathcal P_{d_1}\cup\mathcal P_{d_2}
             \cup\bigcup_{y\in Y}\mathcal P_y.
\]

If `Y,Y'` share one member, then `A_Y` and `A_Y'` share the three labels
`d_1,d_2` and that common member.  A saturating matching for `A_Y`
supplies three distinct actual representatives of those labels.  Both
faces contain the three **complete** common portal sets, so those same
three vertices lie on both `F_Y` and `F_Y'`.  The rooted-face alternative
places all faces in the unique plane embedding of the same four-connected
graph `G[L]`.  In a three-connected plane graph two distinct faces share
at most an edge, hence at most two vertices.  Therefore `F_Y=F_Y'`.

The intersection graph of the two-subsets of a four-set—equivalently the
Johnson graph `J(4,2)`—is connected.  Hence all six faces `F_Y` are one
face `F`.  The fixed labels `d_1,d_2` have their complete portal sets on
every `F_Y`, and every label in `W` occurs in at least one two-set `Y`, so
its complete portal set lies on `F_Y=F`.  Since `D union W=S-{c}`, this
proves the exact complete-set inclusion

\[
                       N_L(S-\{c\})\subseteq V(F).
\]

It does not substitute cofacial selected representatives for complete
portal sets.

## 4. Curvature closure and scope

The pinned cofacial-degree theorem now gives an off-face vertex of
`G[L]` with `L`-degree at most five and with no boundary neighbour outside
`{c}`.  It has no neighbour in `R` by the literal separation, so its total
degree in `G` is at most six, contrary to seven-connectivity.

Thus the stated dichotomy—labelled `K_7^vee` or a strictly smaller actual
seven-adhesion—is valid.  The source correctly does not claim that the
paired colouring state or packet vector survives the boundary descent;
the near model and smaller adhesion are handoffs, not completion of
`HC_7` by themselves.
