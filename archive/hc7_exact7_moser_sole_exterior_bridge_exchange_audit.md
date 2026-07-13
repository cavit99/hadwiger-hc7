# Independent audit: sole-exterior Moser bridge exchange

Audited file:
`archive/hc7_exact7_moser_sole_exterior_bridge_exchange.md`.

## Third-round verdict on Lemmas 5.4--5.7

The three new lemmas are **GREEN in the exact cell**, with one scope condition
that should remain explicit: `D_a,D_b` must be the two open shores and must
exhaust all vertices outside `T union {a,b,v}`.  This is part of the focused
exact-cell hypothesis in
`results/hc7_exact7_moser_order6_decorated_exchange.md`; it is also asserted
in the proof of Lemma 5.4.  If `D_a,D_b` meant merely two selected connected
terminal subgraphs while additional open-side vertices were allowed, the
degree identity would not follow.

Subject to that exact-cell interpretation:

* the degree identity and all four admissibility counts in Lemma 5.4 are
  correct;
* every row of (5.16) is a literal seven-bag `K_7` certificate;
* the five-cycle argument gives `|N_U(w)|<=3`; and
* the six triples in (5.15) are exactly the surviving triples; and
* the pendant-lobe surgery in Lemma 5.6 preserves connectivity,
  disjointness, pairwise adjacency, and exact literal traces; and
* the equality case in Lemma 5.7 really is an actual full order-seven
  adhesion, with the stated packet bound and orientation.

### Componentwise strengthening (5.10) — GREEN

Retain outcome 3 of Lemma 5.3 and let `L` be any component used in
`K_w`.  Write

\[
 D'=D-\bigl((E\cup F\cup R)\cap D\bigr).
\]

By definition, `L` is a component of `D'` and has a neighbour at `w`.
Distinct components of `D'` have no edge between them.  Consequently an
edge from `L` to another vertex of `D` either stays in `L` or ends in one
of the three deleted core blocks.  Since outcome 3 is reached under
`|tau_D(w)|<=1`, every core block met by any component of `K_w` is the
same named block `K`.  In particular, `L` has no neighbour in either of
the other two core blocks.  This also handles literal-root contacts:
`E cap T`, `F cap T`, and `R cap T` partition `U`, so an edge from `L` to
a root in `U` is an edge to that root's named core block.

The exact terminal-shore hypothesis gives

\[
                         N_G(D)\subseteq T\cup\{t\}.
\]

It excludes the opposite open shore and the opposite terminal.  Moreover
`D` contains no vertex of `S=N(v)`, so no vertex of `L` is adjacent to
`v`.  Combining these facts with `T=U dotcup {w}` yields

\[
                         N_G(L)\subseteq K\cup\{w,t\}.
\]

There is a genuine far side for the connectivity argument.  The set `L`
is nonempty, while `v` belongs to neither `L` nor `N_G(L)`.  Deleting
`N_G(L)` therefore leaves `L` and `v` in different components.  Seven-
connectivity gives `|N_G(L)|>=7`.  The core block `K` avoids the side
terminal and has trace contained in `U`, so it contains neither `w` nor
`t`.  At most those two vertices of `N_G(L)` lie outside `K`, and hence

\[
                         |N_G(L)\cap K|\ge 7-2=5.
\]

Thus both assertions in (5.10) hold for every component individually;
the five core attachments cannot arise only after taking the union of
several residual components.  This conclusion remains conditional on the
literal exact-six terminal-shore cell, as are the surrounding results in
Sections 4--5.

### Lemma 5.4: degree and admissibility

The neighbours of `w` are exhausted by its neighbours in `U,D_a,D_b`:
`w` misses `v` because `w notin N(v)`, and Lemma 5.1 gives `wa,wb` absent.
Therefore

\[
 d_G(w)=|N_U(w)|+|N_{D_a}(w)|+|N_{D_b}(w)|.
\]

The frozen contraction-critical kernel gives `d_G(w)>=7`, proving (5.12).
For a frame, `e|f|{r}` is a partition of `U` into blocks of sizes
`2,2,1`, and a decoration is admissible exactly when its block avoids
`N_U(w)`.  Thus one neighbour hits one block and leaves two admissible;
two neighbours leave two admissible exactly when both occupy the same
two-element frame block, and otherwise leave one; and three or more roots
cannot be contained in one frame block, so at most one block is admissible.
This proves every itemized count.

### Lemma 5.5: the four literal models

For each row, discard the `v`-bag and call the two shore bags the last two
bags.  The remaining four bags induce a clique by the following displayed
edges (an entry may list alternative fixed Moser edges):

| contact set | four nonshore bags | six clique adjacencies |
|---|---|---|
| `025` | `0; 2; 16; 5w` | `02,01,w0,12/26,w2,56` |
| `245` | `0; 4; 35; 2w` | `04,03,02,34/45,w4,w5` |
| `046` | `0; 4; 35; 6w` | `04,03,w0,34/45,w4,56` |
| `246` | `0; 2; 16; 4w` | `02,01,04,12/26,w2,w6` |

Every one of these four bags contains a literal vertex of `S`, so it sees
`{v}`.  Each shore bag is connected because its displayed boundary vertex
has a neighbour in the connected full shore; fullness makes it adjacent to
all four nonshore bags.  It also sees `{v}` through its displayed boundary
vertex.  Finally, although the two open shores are anticomplete, their two
bags are adjacent respectively through

\[
                         34,\quad16,\quad12,\quad35
\]

in the four rows.  The bags are plainly disjoint, while `16`, `35`, and
each required `w`--root edge establish connectivity of the other
non-singletons.  This checks all 21 bag pairs in every row without using an
unstated shore edge.

### Five-cycle conclusion

The three-vertex arcs of the missing cycle
`0-5-2-4-6-0` whose middle is not `0` are exactly

\[
                         025,\quad245,\quad246,\quad046.
\]

Every four-subset of a five-cycle contains one of these four arcs, so a
`K_7`-minor-free state has at most three `w`-neighbours in `U`.  The ten
three-subsets of `U` are

\[
024,025,026,045,046,056,245,246,256,456.
\]

Deleting the four positive rows leaves exactly
`024,045,026,056,256,456`, as asserted in (5.15).

### Secondary quotient probe

I independently ran
`results/hc7_exact6_w_boundary_quotient_probe.py`.  It returned the same
four inclusion-minimal positive contact sets and literal contracted-shore
bags as (5.16), and exactly the six stated triples among its negative
states.  The program enumerates every nonempty connected subset of the
eleven-vertex quotient and every ordered-up-to-symmetry collection of seven
disjoint pairwise adjacent such subsets, so its positive certificates are
sound and its negative result is exact for that quotient.  As the draft
correctly says, quotient negativity is only a falsification guardrail and
does not prove nonexistence of a model in an uncontracted shore.

### Lemma 5.6: pendant-lobe promotion

This lemma is **GREEN in its strengthened current form**.  Here `Q_L` is a
connected inclusion-minimal tree subgraph of `G[K]`, and `C` is a whole
component of `G[K]-V(Q_L)`.  Since `K` is connected, every such component
has an edge to `Q_L`.  Thus `K-C` consists of `Q_L` together with all the
other components, each attached to `Q_L`, and is connected.  It contains
`q_L`, so the protected `K-L` edge survives.

The component `C` is connected and, by hypothesis, has an edge to each of
`M` and `W`.  Hence `M union C union W` is connected.  An edge
from `C` to `Q_L` gives adjacency between the two new blocks; the old
`M-L` edge and the protected `K-L` edge give the other two adjacencies.
Disjointness is preserved because `C` is removed from `K` before being
adjoined to `M`, while `W` was disjoint from all three old blocks.

Finally, `Q_L` contains every vertex of `K cap T`, so `C` contains no
adhesion vertex.  Thus the first block retains exactly the old trace of
`K`, the `L` trace is unchanged, and the enlarged third block has exactly
the old `M` trace together with `{w}`.  Its stipulated independence makes
this a legal supported decoration.  The surgery also continues to avoid
the side terminal.  The later central-path/subdivided-`Y` description is a
correct contrapositive for each fixed admissible target, protected portal,
and inclusion-minimal protected tree; it is not, by itself, the unproved stable-rank promotion
of Section 6.

### Lemma 5.7: equality is an exact-seven packet adhesion

This lemma is **GREEN**.  Put `P=N_G(K_w) cap K`.  Lemma 5.3 gives

\[
                         N_G(K_w)\subseteq P\cup\{w,t\},
\]

and `w` is genuinely in this neighbourhood because every component used
to form the nonempty set `K_w` has a neighbour at `w`.  If `|P|=5`,
seven-connectivity forces the neighbourhood to use all seven available
vertices.  Thus `t` must be a neighbour and

\[
                         N_G(K_w)=P\cup\{w,t\}=:Q.
\]

The three parts are disjoint: the supported core avoids the side terminal,
its trace omits `w`, and `P subseteq K`.  Hence `|Q|=7`.  Otherwise the
already proved lower bound `|P|>=5` gives `|P|>=6`.

The pair `(K_w union Q,G-K_w)` is a literal separation: its sides cover
`G`, meet exactly in `Q`, and there is no edge from `K_w` to the other open
side by the definition of `Q`.  Both open shores are nonempty; `K_w` is
nonempty and `v` lies outside `K_w union Q`.  A component `C` of `K_w` has
`N_G(C) subseteq Q`, and the opposite open shore is nonempty, so
seven-connectivity gives `N_G(C)=Q`.  The identical argument applies to
every component of the opposite open shore, using nonempty `K_w` on the
far side.  Thus all those components are literal `Q`-full packets.

The audited exact-seven packet theorem applies because `G` retains the
frozen seven-connectivity, `K_7`-minor-freeness, and strong
contraction-criticality hypotheses, and the separation has two nonempty
open shores.  If `m` is the number of components of `K_w`, the inside
packing number is at least `m`, while the opposite packing number is at
least one.  Their sum is at most four, so `m<=3`.  If `m>=2`, the inside
packing number is at least two; the packet theorem's assertion that one
packing number equals one therefore orients the packet-thin side uniquely
to the opposite shore.  No small-transversal conclusion is being inferred.

## Second-round verdict on the corrected Sections 4--5

The revised exact-order-six cell is **GREEN**.  In particular:

* the new definition of a supported root decoration correctly includes
  literal independence of `{w} union trace(K)`;
* all three cases of Theorem 4.1 are valid;
* the seven branch sets in Lemma 5.1 form a literal `K_7` model;
* the revised `sigma_D(w)` records exactly supported admissible
  decorations, so Corollary 5.2 is valid; and
* all three outcomes of Lemma 5.3, including the whole-graph containment,
  the five-attachment count, and the literal separation in the closed
  shore, are valid.

This verdict is deliberately conditional.  Sections 4--5 assume an
**actual connector separation of exact order six** with

\[
                         T=U\mathbin{\dot\cup}\{w\}.
\]

Theorem 3.1 does not reduce its general separator to this cell.  Nothing in
this second-round verdict treats Section 6, its claimed obstruction list,
or stable-rank promotion as proved.

### Admissible decorations and Theorem 4.1

For a supported decoration `w->K`, admissibility now says precisely that
`{w} union (K cap T)` is independent.  Therefore merging the connected
carrier `W` with `K` preserves both the required boundary equality block
and its expansion to literal vertices.

In case 1, the two shores realize the same three independent blocks
`e,f,{r}`, with `w` adjoined to the same chosen block.  The three carriers
are connected and pairwise adjacent, so bilateral transfer with `q=3`
applies.

In case 2, a side supporting `w->*` has `W` adjacent to every core block.
It can therefore merge `W` with whichever admissible block is supported on
the other side.  Connectivity and the other two carrier adjacencies are
preserved, and the requested independence is a literal boundary condition,
so the case reduces to case 1.

In case 3, `E,F,R,W` realize four independent traces
`e,f,{r},{w}`.  They are pairwise adjacent, and the side-terminal edge to
`W` supplies the portal-only visibility required by the cited transfer
corollary.  No colour name is being identified with a pre-existing branch
bag in any of the three cases.

### Lemma 5.1

Assuming `wa` is an edge, the displayed sets

\[
 \{0\},\ \{a\},\ \{2\},\ \{b,5,6\},\ \{v,4\},\
 D_a,\ D_b\cup\{w\}
\]

are disjoint and connected.  The Moser edges certify every adjacency among
the first five bags stated in the proof; fullness of both terminal shores
certifies all remaining adjacencies.  In particular, `D_a` sees
`D_b union {w}` through `w`, while the assumed `wa` makes the last bag see
the singleton `{a}`.  Thus they are seven literal pairwise adjacent branch
sets.  The displayed Moser automorphism gives the `wb` case.  Hence
`wa,wb` are absent in a `K_7`-minor-free exact-six cell.

### Corollary 5.2

The corrected definition

\[
 \sigma_D(w)=\{K:E(W_w,K)\ne\varnothing\text{ and }
             \{w\}\cup(K\cap T)\text{ is independent}\}
\]

is exactly the set of supported admissible root-block decorations for the
fixed labelled core.  Two subsets of `{E,F,R}` of size at least two have a
common member, so Theorem 4.1(1) applies without the former
geometric-contact/independence gap.

### Lemma 5.3

If `|tau_D(w)|>=2`, every member of
`tau_D(w)-sigma_D(w)` is geometrically contacted but inadmissible.  Since
the core trace itself is independent, inadmissibility is equivalent to
`w` being adjacent to a literal root in that trace.  With
`|sigma_D(w)|<=1`, this proves outcome 1.

If `K_w` is empty, every open-shore neighbour of `w` is in the deleted core.
The bound `|tau_D(w)|<=1`, together with fullness and connectedness of the
terminal shore, places all such edges in one named core block, proving
outcome 2.

Finally suppose `K_w` is nonempty and `|tau_D(w)|<=1`.  Components left
after deleting the open-shore vertices of the three core blocks have no
mutual edges.  Hence every neighbour of `K_w` in `D-K_w` lies in the unique
raw-contact block `K`; connectedness supplies such a block.  All five roots
of `U` lie in the three core blocks, and a root contact in either other
block would be another raw contact.  The terminal-shore separation also
excludes the opposite shore and `v`.  Consequently

\[
                         N_G(K_w)\subseteq K\cup\{w,t\}.
\]

This whole-graph neighbourhood separates nonempty `K_w` from `v`, so
seven-connectivity gives `|N_G(K_w)|>=7`.  At most `w,t` lie outside `K`,
and therefore `|N_G(K_w)\cap K|>=5`.  In the closed shore `J`, putting
`Q=N_J(K_w)`, the sets `K_w union Q` and `J-K_w` cover `J`, intersect in
`Q`, and have no edge between their respective differences.  Thus they
form the asserted literal separation with `Q\subseteq K\cup\{w,t\}`.

## First-round record (superseded for revised Sections 4--5)

The following records the audit of the earlier draft.  Its RED conclusions
about decoration independence and `sigma` are repaired by the revised
definitions and are superseded by the second-round verdict above.  Its
warnings about the general separator and Section 6 remain live.

**First-round verdict:**

* Lemma 2.1: **GREEN**.
* Theorem 3.1: **GREEN**, with one omitted saturation argument made explicit
  below.
* The supported-core construction preceding Theorem 4.1: **GREEN**.
* Theorem 4.1(1): **RED as stated** — a merged `w`-trace need not be
  independent.
* Theorem 4.1(2): **RED as stated** for the same reason.
* Theorem 4.1(3): **GREEN**, conditional on the explicitly assumed exact
  portal adhesion.
* Corollary 5.1 and the rank-two conclusion: **RED as stated** — `sigma`
  records geometric contact, not admissible independent decorations.
* The claim that Sections 3--5 reduce every sole-exterior survivor to the
  two obstructions in Section 6: **RED/incomplete**.  The general separator
  from Theorem 3.1 has not been reduced to `T=U union {w}`, and crossed-frame
  sets on the two shores need not have a common frame.

The note remains useful: it proves a valid reserved-connector/full-separator
dichotomy and isolates a promising conditional decorated-transfer mechanism.
It does not yet prove the advertised rank-one endpoint for the general
sole-exterior branch.

## 1. Frozen setup and Lemma 2.1 — GREEN

With `S=N(v)` and `G-N[v]=C`, seven-connectivity makes `C` `S`-full.  It is
a component of `G-S`, and the far side required by the audited four-port
theorem contains `v`.

In the linkage outcome, the `1-3` and `2-4` paths have nonempty disjoint
interiors in `C`, because both pairs are literal nonedges.  Adjacent
enlargement in connected `C` gives carriers for `13|24`.

In the rural outcome, if one of the portal unions for `{1,2}` or `{3,4}`
had order at most one, that union together with the other five vertices of
`S` would be an at-most-six cut separating a nonempty part of `C` from `v`.
Starting from two-connected `C`, the literal edges `12,34` then give two
ears with distinct ends, so the four-root closure is two-connected.  Its
outer facial arcs give the carriers for `14|23`.  This is exactly the
already-audited two-connected four-corner argument and is valid with only
one exterior component.

## 2. Theorem 3.1 — GREEN

### Rooted model

Contract the star on `{v,a,b}` for `a=1,b=3`.  After deleting the connector
and expanding the independent pair `ab`, a proper-minor six-colouring gives
a colouring of `H=G-v`.

The draft omits one short but necessary reason why the five roots in `U`
have five distinct colours.  Every colour of the six-colour palette must
occur on `S`; otherwise a missing boundary colour can be assigned to `v`,
six-colouring `G`.  Since `ab` is one exact block and all other boundary
vertices avoid its representative colour, the five vertices of `U` must
use the other five colours one each.

The usual Kempe swap then forces every missing-root pair to lie in one
two-colour component: otherwise the swap removes one colour from `S` and
again leaves a colour for `v`.  The Kriesell--Mohr five-root theorem applies
to the missing-edge graph and produces a rooted `K5` model on `U`, using
only the five nonzero colour classes and hence avoiding `a,b`.

### Reserved connector or separator

Let `W` be the union of the five rooted bags.  If `a,b` lie in one component
of `H-W`, an `a-b` path there is disjoint from the bags.  For every root
`u`, at least one of `au,bu` is present because `alpha(G[S])<=2`; hence the
path bag is adjacent to every rooted bag.  Those six bags, together with
`{v}`, form a literal `K7` model.

Otherwise choose an inclusion-minimal `a-b` separator `Z subseteq W`.
Since `G` is seven-connected, `H=G-v` is six-connected, so `|Z|>=6`.
For every `z in Z`, minimality yields an `a-b` path meeting `Z` only at
`z`.  The two subpaths show that `z` has a neighbour in each distinguished
component `R_a,R_b` of `H-Z`.  Conversely those components have no external
neighbour outside `Z`.  Thus both are literally full to `Z`.  Distributing
at least six vertices of `Z` over five disjoint model bags gives the claimed
double hit.

No planarity, packet label, or colour-to-bag inference is hidden in this
argument.

## 3. The general separator does not yet yield the Section 4 adhesion

Theorem 3.1 produces

\[
             Z\subseteq W,\qquad |Z|\ge6,
\]

with no assertion that `Z` contains the five literal roots `U`, has order
six, or has the form

\[
                         T=U\mathbin{\dot\cup}\{w\}.
\]

Indeed a minimal separator may use internal vertices of several rooted
bags instead of their roots.  The portal-transfer theorem can be applied to
an adhesion containing `U` by enlarging to `Z union U`, but that adhesion
may have between six and eleven vertices and is not the special `T` used in
Sections 4--5.

Accordingly, Sections 4--5 are a valid *conditional exact-portal cell* only.
No argument in the draft reduces the general separator from Theorem 3.1 to
that cell.  This is independent of the decoration issue below.

## 4. Supported cores — GREEN

For a frame consisting of two disjoint missing-cycle edges `e,f` and the
remaining root `r`, two disjoint portal paths give connected disjoint blocks
with traces `e,f`.  The present complementary five-cycle supplies an edge
between them and an edge from each to the singleton root block `{r}`.
Thus `E,F,R` are a label-faithful supported core.

If `W` is connected, disjoint from the core, and has trace `{w}`, then a
geometric edge from `W` to a core block makes their union connected while
preserving pairwise adjacency to the other core blocks.  This geometric
coarsening statement is correct.  What it does **not** ensure is that the
new adhesion trace is independent.

## 5. Theorem 4.1 — itemized audit

### Case 1 — RED as stated

The bilateral portal-transfer theorem requires a partition of the adhesion
into **independent** blocks.  If `W` is merged into, say, `E`, the new trace
is

\[
                             e\cup\{w\}.
\]

Although `e` is a missing edge and hence independent, the definition of a
supported decoration only assumes `E(W,E) != empty`.  It does not require
`w` to be nonadjacent to both endpoints of `e`.  An edge from `w` to either
root makes `e union {w}` non-independent, so the contraction colour cannot
be expanded to that literal block.

Thus “common supported decoration” is insufficient.  A corrected statement
must require a **common admissible decoration**, meaning both geometric
support and

\[
                    E_G(w,\operatorname{trace}(K))=\varnothing.
\]

Under that added condition, the three connected pairwise adjacent
realizations have the same independent three-block partition on both sides,
and bilateral transfer with `q=3` is valid.

### Case 2 — RED as stated

A singleton-supported side is geometrically capable of merging `W` into
any core block, but the resulting literal trace still has to be independent.
Therefore it realizes every **admissible** root-block decoration, not every
supported one.  Case 2 becomes valid if the decoration on the opposite side
is explicitly admissible; as written it inherits the Case 1 defect.

### Case 3 — GREEN

Here `W` remains a separate portal-only block with singleton trace `{w}`.
The four traces `e,f,{r},{w}` are independent.  The definition of
`w->*` makes `W` adjacent to all three core blocks and to the appropriate
side terminal.  Hence the four realized blocks are pairwise adjacent, and
the portal-only block is adjacent to the contracted star `{v,a,b}` on each
side.  This is exactly the hypothesis of Corollary 2.3 of the bilateral
transfer theorem.  Palette alignment and the missing colour for `v` are
therefore legitimate in this case.

## 6. Corollary 5.1 — RED as stated

The set `W_w={w} union K_w` is indeed connected, disjoint from the core,
and has exact adhesion trace `{w}`.  The block names `E,F,R` are also
label-faithful when the same frame is fixed on both sides.

However,

\[
 sigma_D(w)=\{K:E(W_w,K)\ne\varnothing\}
\]

records only geometric contact.  It can count an edge from `w` directly to
a root in the trace of `K`; that very edge makes the merged trace
`{w} union trace(K)` non-independent.  Consequently two contact sets of
order at least two may intersect only in a block which is inadmissible on
one or both sides.  The set-intersection argument then cannot invoke
Theorem 4.1(1).

A valid replacement is the admissible contact set

\[
 sigma_D^{\rm adm}(w)=
 \{K:E(W_w,K)\ne\varnothing\text{ and }
       E_G(w,\operatorname{trace}(K))=\varnothing\}.
\]

If both admissible contact sets have order at least two, the intersection
argument is correct.  The current draft proves no lower bound on these
admissible ranks, so (5.4) does not follow for the presently defined
`sigma`.

## 7. Section 6 is not an exhaustive endpoint

Even after repairing admissibility, two further cases are missing from the
claimed final list.

1. The separator supplied by Theorem 3.1 may not reduce to the special
   exact adhesion `T=U union {w}`.  This is the gap in Section 3 of this
   audit.
2. Each terminal shore may contain a crossed frame while the two sets of
   crossed frames are disjoint.  Then neither shore is all-crossless, but
   there is no common bilaterally crossed frame to which Corollary 5.1
   applies.  No combinatorial intersection theorem for the two frame sets
   is proved.

The asserted stabilization of a “three-segment skeleton” also needs an
explicit path system of order at least three before Tutte's stable-bridge
theorem can be invoked.  A supported core is described as three connected
blocks, not yet as a specified indexed path system with three preserved
segments.  This does not affect Lemma 2.1 or Theorem 3.1, but it prevents
Section 6 from being treated as a proved exhaustive reduction.

The exact live programme after this audit is therefore broader than a
rank-one stable lock: first handle general `Z union U` adhesions or reduce
them to the six-portal cell; then require admissible decorations; and then
resolve nonintersecting crossed-frame families before applying stable-rank
promotion.
