# Sole-exterior Moser: reserved connector, decorated carrier overlap, or a rank-one bridge lock

**Status:** theorem-level partial closure.  Sections 2--3 are proved from the
frozen audited kernel; Sections 4--5 are proved conditionally for an actual
exact order-six connector adhesion.  Section 6 states the exact remaining
bridge-exchange gaps; the sole-exterior branch is not claimed closed.

## 1. Frozen setting

Let `G` be seven-connected, `K_7`-minor-free, and proper-minor-minimal
subject to not being six-colourable.  Let `v` have degree seven and let

\[
 S=N(v)=\{0,1,2,3,4,5,6\},
 \qquad
 E(G[S])=\{01,02,03,04,12,16,26,34,35,45,56\}.
 \tag{1.1}
\]

Assume that

\[
                         G-N[v]=C
\]

is connected.  Put `H=G-v`.  The graph `H` is six-connected.  Every
proper minor of `G` is six-colourable.

For the exact trace `ab=13`, put

\[
                         U=S-\{a,b\}=\{0,2,4,5,6\}.
\]

The present graph `G[U]` and its missing-edge graph are both five-cycles.
A frame consists of two vertex-disjoint edges `e,f` of the missing cycle;
the fifth root is denoted by `r`.

## 2. The one-call four-corner seed

The one-call dichotomy in
`../results/hc7_exact7_moser_four_corner_exchange.md` has a part which does
not require a second exterior component.

### Lemma 2.1 (sole-shore complementary carrier seed)

If `C` is two-connected and has order at least three, then it contains
disjoint adjacent connected sets `X,Y` which contact one of

\[
                         13\mid24,
                  \qquad 14\mid23.                  \tag{2.1}
\]

#### Proof

Apply the audited seven-boundary four-port theorem to the component `C` of
`G-S`, with ordered roots `(1,2,3,4)`.  The far side contains `v`.

In the linkage outcome it returns disjoint `1-3` and `2-4` paths with
interiors in `C`.  The two boundary pairs are nonedges, so their interiors
are nonempty.  Adjacent enlargement inside connected `C` gives (2.1) with
matching `13|24`.

In the rural outcome, `G[C union {1,2,3,4}]` has a disk embedding with
literal boundary order `1,2,3,4`.  Seven-connectivity gives

\[
 |N_C(\{1,2\})|\ge2,\qquad |N_C(\{3,4\})|\ge2:       \tag{2.2}
\]

otherwise the relevant portal union together with the other five vertices
of `S` is a cut of order at most six.  Starting with the two-connected graph
`C`, the literal edges `12,34` and distinct portal representatives give two
ears, so the four-root closure is two-connected.  Its outer facial cycle
has disjoint nonempty open arcs joining the consecutive nonedges `14` and
`23`; adjacent enlargement gives the other matching in (2.1). \(\square\)

The second exterior component was used in the earlier theorem only to
reflect a colour state.  Lemma 2.1 retains the literal carrier skeleton but
does not by itself colour the sole-exterior graph.

## 3. A literal reserved-connector-or-adhesion reduction

The following installs an actual internal separation before any bridge
analysis.

### Theorem 3.1 (rooted connector or full internal adhesion)

For the exact trace `ab=13`, either `G` has a `K_7` minor, or `H` contains
a rooted `K_5` model

\[
                         \mathcal B=(B_u:u\in U)
\]

and an inclusion-minimal `a-b` separator

\[
                    Z\subseteq\bigcup_{u\in U}B_u,
                    \qquad |Z|\ge6,                 \tag{3.1}
\]

such that the components `R_a,R_b` of `H-Z` containing `a,b` are both full
to literal `Z`.  Some rooted bag contains at least two vertices of `Z`.

#### Proof

Contract the star `vab`.  A six-colouring of that proper minor expands to
a six-colouring of `H` in which `a,b` have one colour and the five roots in
`U` have five distinct other colours.  Kempe connectivity between every
nonadjacent root pair, together with the Kriesell--Mohr five-root theorem,
gives a rooted `K_5` model on `U` avoiding `a,b`; this is the audited exact
trace construction used in
`../archive/hadwiger_reserved_connector_adhesion_principle.md`, Theorem 2.1.

Let `W` be the union of its five bags.  For each root `u`, at least one of
`au,bu` is present, since `alpha(G[S])<=2`.  If `a,b` lie in the same
component of `H-W`, an `a-b` path in that component is a sixth branch set
adjacent to every rooted bag.  Together with `{v}` it gives `K_7`.

Otherwise choose an inclusion-minimal subset `Z subseteq W` separating
`a,b`.  Six-connectivity of `H` gives `|Z|>=6`.  Minimality gives, for every
`z in Z`, an `a-b` path meeting `Z` only at `z`; hence `z` has a neighbour
in each of `R_a,R_b`.  Thus both distinguished components are full to `Z`.
Since `Z` lies in five disjoint bags and has at least six vertices, one bag
is hit twice. \(\square\)

This is an actual separation of `H`, not an abstract rooted-minor failure.
For the portal-transfer form, put `T=Z union U`, take the component `Q_a` of
`H-T` containing `a`, and set

\[
 A=Q_a\cup T,\qquad B=V(H)-Q_a.
\]

Then `(A,B)` is a literal separation with adhesion `T`, with `a in A-T` and
`b in B-T`.  If a bilateral block realization is found on these two closed
sides, the audited transfer theorem
`../archive/hadwiger_reserved_connector_portal_transfer.md`, Theorem 2.1,
handles the apex path `avb` and glues the colours.

Theorem 3.1 does **not** imply that this adhesion has order six.  In
general `Z` may have more than six vertices and may contain roots from
`U`, so `T=Z union U` may be much larger.  Sections 4--5 below are the
conditional exact-order-six specialization: they apply when an actual
connector separation has adhesion precisely `U dotcup {w}`.  No reduction
from an arbitrary separator (3.1) to that specialization is being assumed.

## 4. Crossed-frame carrier states on an exact portal adhesion

We now isolate the constructive exchange which was missing from the older
portal-transfer formulation.  **Conditionally on an exact order-six
connector separation**, use the notation

\[
                         T=U\mathbin{\dot\cup}\{w\},   \tag{4.1}
\]

with terminal `a` on one open side and terminal `b` on the other.  A
terminal shore is a connected graph `D`, anticomplete to the opposite open
shore, with all neighbours in `D union T union {a}` (or with `b`), and full
to those seven displayed labels.

Fix a frame `(e,f;r)`, where `e,f` are disjoint missing-cycle edges and `r`
is the remaining root.  A **supported frame core** in a closed terminal
shore is a triple of disjoint connected pairwise adjacent sets, each
avoiding the side terminal,

\[
                         E,F,R                         \tag{4.2}
\]

with literal adhesion traces `e,f,{r}`.  A crossed frame supplies such a
core: take its two disjoint portal paths for `e,f`; the present Moser cycle
gives an edge between the two path blocks and gives the leftover root an
edge to each.

Let `W` be any connected set, disjoint from (4.2) and from the side
terminal, with

\[
                         W\cap T=\{w\}.                \tag{4.3}
\]

For `K in {E,F,R}`, say that the decoration `w->K` is **admissible** when
`{w}` together with the adhesion trace of `K` is independent, and say it is
**supported** when it is admissible and `W` is adjacent to `K`.  Then
replacing `K` by `K union W` gives three disjoint connected pairwise adjacent
blocks whose traces are obtained by adjoining `w` to the trace of `K`.

Say the singleton decoration `w->*` is supported if `W` is adjacent to all
three core blocks and to the side terminal.  Then `E,F,R,W` are four
pairwise adjacent blocks, and the last adjacency makes the portal-only
block visible to the contracted star in Corollary 2.3 of the bilateral
transfer theorem.

### Theorem 4.1 (decorated carrier overlap)

Suppose the same frame has supported cores on both terminal shores.

1. If both sides support a common root-block decoration among
   `w->E,w->F,w->R`, then `G` is six-colourable.
2. If one side supports `w->*` and the other supports any admissible
   root-block
   decoration, then `G` is six-colourable.
3. If both sides support `w->*`, then `G` is six-colourable.

#### Proof

In case 1, use on each side the same three-block partition of `T`: the
blocks are `e,f,{r}`, with `w` adjoined to the common chosen block.  All
three blocks are independent and meet `U`; the displayed supported sets
realize them as pairwise adjacent connected blocks.  The bilateral
four-block transfer theorem (with `q=3`) six-colours `G`.

For case 2, the singleton side can realize every admissible root-block
decoration: merge its connected singleton carrier `W` with the requested
core block.  The union is connected because `W` is adjacent to that block,
and it remains adjacent to the other two blocks because the original core
was pairwise adjacent.  Reduce to case 1.

In case 3 use the four blocks `E,F,R,W` on both sides.  The first three meet
`U`; the fourth is portal-only and is adjacent to the star through the side
terminal.  Corollary 2.3 of the bilateral transfer theorem applies. \(\square\)

The important point in case 2 is monotonicity under **geometric coarsening**,
not an identification of colour names with branch bags.

## 5. The rank-two bridge closure

The exact separation first forces a useful literal nonadjacency.

### Lemma 5.1 (the extra portal misses both terminals)

In a `K_7`-minor-free exact order-six connector separation,

\[
                              wa,wb\notin E(G).       \tag{5.1}
\]

#### Proof

Suppose `wa` is an edge.  Let `D_a,D_b` be the two connected full terminal
shores.  The following seven sets are disjoint connected branch sets:

\[
 \{0\},\quad \{a\},\quad \{2\},\quad
 \{b,5,6\},\quad \{v,4\},\quad D_a,\quad D_b\cup\{w\}.
 \tag{5.2}
\]

The first three form the Moser triangle `012`.  The set `{b,5,6}` sees
them through `03,16,26`, and `{v,4}` sees them through `04,v1,v2` and
sees `{b,5,6}` through `34` (also through `45`).  Full attachment of
`D_a` to `T union {a}` and of `D_b` to `T union {b}` supplies every
remaining adjacency; in particular `D_a` sees the last bag through `w`,
and the assumed edge `wa` makes the last bag see `{a}`.  Thus (5.2) is a
literal `K_7` model, a contradiction.

The Moser automorphism

\[
             a\leftrightarrow b,\qquad 2\leftrightarrow4,
             \qquad 6\leftrightarrow5
\]

fixing `0,v,w` gives the same conclusion from `wb`. \(\square\)

For a supported core (4.2), remove its open-shore vertices from `D`.  Let
`K_w` be the union of all remaining components having a neighbour at `w`,
and put

\[
                         W_w=\{w\}\cup K_w.            \tag{5.3}
\]

This set is connected (all its components attach to `w`) and has trace
exactly `{w}`.  Define its admissible core-contact set

\[
 sigma_D(w)=\{K\in\{E,F,R\}:E(W_w,K)\ne\varnothing
       \text{ and }\{w\}\cup(K\cap T)\text{ is independent}\}. \tag{5.4}
\]

Each member of `sigma_D(w)` is a supported root-block decoration.

### Corollary 5.2 (two admissible contacts on both sides close)

If a common crossed frame has

\[
             |sigma_{D_a}(w)|\ge2,
             \qquad |sigma_{D_b}(w)|\ge2,             \tag{5.5}
\]

then `G` is six-colourable.

#### Proof

Two subsets of the three-element set `{E,F,R}`, each of order at least two,
intersect.  A common member is a common root-block decoration, so Theorem
4.1(1) applies. \(\square\)

Consequently every surviving **bilaterally crossed** frame has a side with

\[
                         |sigma_D(w)|\le1.              \tag{5.6}
\]

This is a literal bridge-placement statement.  It is stronger than saying
that two unnamed equality states differ.

The all-crossless alternative is already closed by
`../results/hc7_exact7_moser_one_component_allweb_closure.md` before the
internal separation, and by the bilateral web-gluing theorem
`../archive/hadwiger_reserved_connector_bilateral_allweb_closure.md` after
an exact portal separation.  Hence a survivor has a crossed frame somewhere;
if the same frame occurs on both sides, (5.6) is forced.

The distinction between geometric contact and an admissible colour block is
now essential.  Define the raw contact set

\[
 tau_D(w)=\{K\in\{E,F,R\}:E(W_w,K)\ne\varnothing\}.   \tag{5.7}
\]

Thus `sigma_D(w)` is obtained from `tau_D(w)` by deleting precisely those
blocks whose literal trace has a neighbour at `w`.

### Lemma 5.3 (rank-one portal exhaustion)

Assume `|sigma_D(w)|<=1` on a terminal shore with supported core
`E,F,R`.  Then at least one of the following concrete certificates occurs.

1. **Boundary incompatibility.**  `|tau_D(w)|>=2`, and all but at most one
   member `K` of `tau_D(w)` has a literal root in `K cap T` adjacent to
   `w`.
2. **Direct-core lock.**  `K_w` is empty, and every edge from `w` into the
   open shore lands in one named core block.
3. **Five-attachment lock.**  `K_w` is nonempty and there is a named block
   `K in {E,F,R}` such that

   \[
       N_G(K_w)\subseteq K\cup\{w,t\},
       \qquad |N_G(K_w)\cap K|\ge5,                  \tag{5.8}
   \]

   where `t` is the side terminal.  Moreover, in the closed terminal shore
   `J=D union T union {t}`, the sets

   \[
       A_w=K_w\cup Q,\qquad B_w=J-K_w,
       \qquad Q=N_J(K_w),                            \tag{5.9}
   \]

   form an actual separation with adhesion `Q subseteq K union {w,t}`.

#### Proof

If `|tau_D(w)|>=2`, every member of
`tau_D(w)-sigma_D(w)` is inadmissible.  The trace of each core block is
itself independent, so inadmissibility says exactly that `w` is adjacent
to a literal root in that trace.  This proves outcome 1.

Suppose `|tau_D(w)|<=1`.  If `K_w` is empty, outcome 2 is just the
definition of `tau_D(w)`.  Now assume `K_w` is nonempty.  After the
open-shore vertices of the core are deleted, different remaining
components have no edges between them.  Hence every neighbour of `K_w`
inside `D-K_w` lies in the unique raw-contact block `K` (if there were no
such block, connectedness of `D` supplies one).  Every vertex of `U` lies
in one of the three core blocks.  Therefore every external neighbour of
`K_w` in the whole graph lies in `K union {w,t}`: there is no edge to the
opposite open shore or to `v`, and Lemma 5.1 excludes `wt` but is not even
needed for the displayed containment.

The set `N_G(K_w)` separates the nonempty set `K_w` from `v`.  Seven-
connectivity gives `|N_G(K_w)|>=7`.  At most the two vertices `w,t` lie
outside `K`, proving the second inequality in (5.8).  Finally, by the
definition of `Q`, there is no edge from `K_w` to
`J-(K_w union Q)`.  The two sets in (5.9) cover `J` and intersect exactly
in `Q`, proving the asserted literal separation. \(\square\)

Lemma 5.3 is the promised portal-exhaustion output: a low admissible rank
cannot be recorded merely as a missing state.  It is witnessed either by
literal `w`--root edges, by direct concentration in one named carrier, or
by at least five distinct attachments to one named carrier behind an
actual recursive adhesion.

The five-attachment conclusion is componentwise.  If `L` is any component
of the nonempty set `K_w` in outcome 3, then

\[
 N_G(L)\subseteq K\cup\{w,t\},
 \qquad |N_G(L)\cap K|\ge5.                         \tag{5.10}
\]

Indeed `L` has a neighbour at `w` by the definition of `K_w`, and it has no
neighbour in another component left after deleting the core.  The same
containment proof as in Lemma 5.3 applies to `L`; its neighbourhood
separates it from `v`, so seven-connectivity supplies the same count.
Thus every connected attachment region individually meets the hypotheses
of the singleton/pair carrier bypass theorems; the five contacts cannot be
hidden by distributing them among several components.

There is also a useful global accounting identity.  For a fixed frame put

\[
 I_w(e,f;r)=\{K\in\{E,F,R\}:\{w\}\cup(K\cap T)
                         \text{ is independent}\}.   \tag{5.11}
\]

This admissibility set is determined by the literal edges from `w` to `U`;
it is the same on both shores.  Only the geometric raw sets `tau_D(w)` can
differ, and

\[
                         sigma_D(w)=tau_D(w)\cap I_w(e,f;r). \tag{5.12}
\]

### Lemma 5.4 (palette obstruction versus shore surplus)

Let `k=|N_U(w)|`.  In the exact order-six cell,

\[
 |N_{D_a}(w)|+|N_{D_b}(w)|=d_G(w)-k\ge7-k.          \tag{5.13}
\]

For every frame, `|I_w(e,f;r)|` is the number of its three trace blocks
which avoid `N_U(w)`.  In particular:

* if `k=0`, all three decorations are admissible;
* if `k=1`, exactly two are admissible;
* if `k=2`, two are admissible precisely when the two neighbours form one
  of the two missing-edge blocks of that frame, and otherwise exactly one
  is admissible; and
* if `k>=3`, at most one is admissible.

#### Proof

The exact separation exhausts the vertices outside
`T union {a,b}` by `D_a,D_b`.  The vertex `w` is not adjacent to `v`
because `w notin N(v)`, and Lemma 5.1 excludes `wa,wb`.  This proves the
identity in (5.12); minimum degree gives its inequality.  The remaining
claims just count which blocks of the partition `e|f|{r}` meet the set
`N_U(w)`. \(\square\)

Thus the sharp obstruction has two complementary forms.  Sparse literal
contact of `w` with `U` leaves at least five or six actual shore contacts
which a rerouting argument can exploit.  Contact spread over at least three
roots destroys all but one independent decoration, but records that failure
as a common literal boundary-edge pattern on both sides rather than as
uncontrolled palette drift.

Most dense boundary patterns in fact give the minor immediately.  In the
missing-edge cycle

\[
                         0,5,2,4,6,0,                \tag{5.14}
\]

the root `0` is distinguished by being adjacent to both terminals `a,b`.

### Lemma 5.5 (dense extra-portal contacts close)

If `N_U(w)` contains three consecutive vertices of (5.13) whose middle
vertex is not `0`, then `G` has a `K_7` minor.  Consequently a
`K_7`-minor-free exact order-six cell satisfies

\[
 |N_U(w)|\le3.                                      \tag{5.15}
\]

If equality holds, then `N_U(w)` is one of

\[
 024,\quad045,\quad026,\quad056,\quad256,\quad456. \tag{5.16}
\]

#### Proof

Contract each connected full terminal shore only for the purpose of reading
the following certificates.  Write the shore itself in the displayed bag,
so no contraction is needed in the actual model.  The four possible
three-vertex arcs of (5.13) with middle different from `0` have these seven
branch sets:

\[
\begin{array}{c|lllllll}
N_U(w)&\multicolumn{7}{c}{\text{branch sets}}\\ \hline
025&\{0\}&\{2\}&\{1,6\}&\{v\}&\{5,w\}&\{4\}\cup D_a&\{3\}\cup D_b\\
245&\{0\}&\{4\}&\{3,5\}&\{v\}&\{2,w\}&\{1\}\cup D_a&\{6\}\cup D_b\\
046&\{0\}&\{4\}&\{3,5\}&\{v\}&\{6,w\}&\{1\}\cup D_a&\{2\}\cup D_b\\
246&\{0\}&\{2\}&\{1,6\}&\{v\}&\{4,w\}&\{5\}\cup D_a&\{3\}\cup D_b.
\end{array}                                           \tag{5.17}
\]

Every displayed set is connected: the only nontrivial checks use the listed
`w`--root edge and full attachment of `D_a,D_b`.  Every two displayed sets
are adjacent by the fixed Moser edges (1.1), by an edge from `v` to a root,
or by full shore attachment to `U union {w}` and the appropriate terminal.
Thus each row is a literal `K_7` model.  Extra `w`--root edges cannot destroy
it.

Every four-element subset of the five-cycle contains a three-vertex arc
whose middle is not `0`; hence (5.14).  Of the ten triples of `U`, the four
rows in (5.16) are excluded.  The other six are exactly (5.15). \(\square\)

The dependency-free exact branch-set search in
`hc7_exact6_w_boundary_quotient_probe.py` independently regenerates these
four inclusion-minimal positive contact sets and verifies that the six
triples in (5.15), as bare contracted-shore quotients, do not already have a
`K_7` model.  The negative output is used only as a falsification guardrail;
the positive theorem is proved by the explicit bags (5.16).

Combining Lemmas 5.4 and 5.5, every sharp survivor has at least four literal
edges from `w` into `D_a union D_b`; it has at least five unless its root
neighbourhood is one of the six triples (5.15).

The five-attachment lock admits a first label-faithful surgery.  The next
lemma is deliberately stated for arbitrary connected branch sets; it is not
Moser-specific.

### Lemma 5.6 (pendant-lobe decoration promotion)

Let `K,L,M` be three disjoint connected pairwise adjacent blocks with fixed
literal traces in an adhesion.  Let `W` be a connected set disjoint from
them and from the side terminal, with adhesion trace `{w}`, and suppose
`W` is adjacent to `K`.  Assume that adjoining `w` to the trace of `M` is
independent.

Choose an endpoint `q_L in K` of an edge from `K` to `L`, and let `Q_L` be
an inclusion-minimal tree in `G[K]` containing

\[
                         (K\cap T)\cup\{q_L\}.       \tag{5.18}
\]

If some component `C` of `G[K]-V(Q_L)` contains both

* an endpoint in `K` of an edge from `W` to `K`, and
* an endpoint in `K` of an edge from `K` to `M`,

then replacing

\[
 K\longmapsto K-C,\qquad
 M\longmapsto M\cup C\cup W                         \tag{5.19}
\]

produces three disjoint connected pairwise adjacent blocks with the same
traces as `K,L,M`, except that `w` is adjoined to the trace of `M`.

#### Proof

The tree `Q_L` is connected.  Every component of
`G[K]-V(Q_L)` has a neighbour in `Q_L`, because `K` is connected.
Consequently `K-C` is connected: it contains `Q_L`, and every other
component of `G[K]-V(Q_L)` attaches to that tree.  It contains the whole
old trace `K cap T` and remains adjacent to `L` through the protected
vertex `q_L`.

The set `M union C union W` is connected: the two assumed endpoint
conditions give an edge from `C` to each of `M,W`.  It is adjacent to
`K-C` through an edge from `C` to `Q_L`, and it remains adjacent to
`L` through the old `L-M` adjacency.  The old block `K-C` remains adjacent
to `L`, so the three new blocks are pairwise adjacent.  The component `C`
contains no adhesion vertex of `K`, because all of `K cap T` lies in
`Q_L`.  Thus (5.18) changes the literal traces only by adjoining `w` to
the trace of `M`; that trace is independent by hypothesis. \(\square\)

Applied on one shore of the exact Moser cell, Lemma 5.6 creates the
supported decoration `w->M`, hence closes whenever the opposite shore
supports the same decoration by Theorem 4.1.  It eliminates an infinite
family of five-attachment locks: every lock in which a `W`-attachment and
an admissible foreign-block portal share a pendant lobe.

Accordingly, failure of the promotion has a much sharper tree form.  For
every admissible target block `M`, every protected choice of the third block
portal `q_L`, and every inclusion-minimal protected tree `Q_L`, each
component of `G[K]-V(Q_L)` which contains a `W`-attachment contains no
`K-M` portal.  Since
`Q_L` spans at most the two roots of `K` and one protected portal, its
suppressed shape is a path or a subdivided `Y`.  Thus all foreign labelled
portals are forced either into that central path/`Y` or into pendant lobes
which contain no `W`-attachment.  This is the precise central-core lock
left after the first surplus exchange.

The numerical equality case of the five-attachment lock is not a new
unstructured cell: it is literally an exact-seven packet adhesion.

### Lemma 5.7 (five equals exact seven; otherwise six-surplus)

Retain outcome 3 of Lemma 5.3, put

\[
                         P=N_G(K_w)\cap K,
\]

and let `t` be the side terminal.  Then exactly one of the following holds.

1. `|P|>=6`; or
2. `|P|=5`, `K_w` is adjacent to `t`, and

   \[
                        Q=N_G(K_w)=P\cup\{w,t\}      \tag{5.20}
   \]

   is an actual adhesion of order seven.  Every component of `K_w` is
   `Q`-full, as is every component on the opposite open side of the
   separation `(K_w union Q, G-K_w)`.

In outcome 2, if `m` is the number of components of `K_w`, then `m<=3`.
If `m>=2`, the opposite side has packet number one.

#### Proof

By Lemma 5.3,

\[
                   N_G(K_w)\subseteq P\cup\{w,t\}.
\]

The vertex `w` belongs to `N_G(K_w)` by the definition of `K_w`.
Seven-connectivity gives `|N_G(K_w)|>=7`.  Thus `|P|=5` is possible only
when `t` is also a neighbour, and then equality holds throughout, proving
(5.19).  Otherwise `|P|>=6`.

Assume (5.19), and let `C_0` be a component of `K_w`.  It has no neighbour
outside `Q`, while its neighbourhood has order at least seven by
seven-connectivity.  Hence `N_G(C_0)=Q`; that is, `C_0` is a full packet.
The same argument applies to every component of either open shore of the
literal separation with adhesion `Q`.

The audited exact-seven packet theorem gives total packet number at most
four and says that one of the two shore packet numbers equals one.  The
inside packet number is at least `m`, and the opposite side has at least one
packet.  Hence `m<=3`; if `m>=2`, the side whose packet number equals one
must be the opposite side. \(\square\)

Thus the central path/`Y` lock after Lemma 5.6 has only two capacities:
six or more labelled attachments, or an exact-seven interface already
governed by the packet theorem.  No inference from packet number one to a
small vertex transversal is made.

## 6. Exact remaining bridge-exchange gaps

No Tutte stabilization is silently available from (4.2).  A supported
three-block core is not itself a path system of order at least three.  To use
the audited stable-bridges theorem one must first exhibit at least three
internally disjoint paths with prescribed endpoint pairs inside a
three-connected terminal shore and then prove that rerouting preserves the
three literal block traces.  That additional construction has not yet been
proved.  In particular, attachments on two unnamed skeleton segments may
still belong to one named core block.

There are two levels of remaining obstruction.

### 6.1 The general connector separation

For the separator supplied by Theorem 3.1, the adhesion `T=Z union U` can
have arbitrary order at least six.  The unresolved general step is to find a
partition of this whole literal adhesion into at most four independent
blocks which is realized on both closed sides.  None of the exact-order-six
arguments removes surplus vertices of `Z`.

### 6.2 The conditional exact-order-six cell

Even in the exact specialization `T=U dotcup {w}`, a survivor must exhibit
at least one of the following explicit failures:

1. **frame mismatch:** no frame has a crossed supported core on both sides.
   This includes the case that one shore is all-crossless, but also permits
   both shores to be crossed on different frames;
2. **decorated-state mismatch:** a common crossed frame exists, but its two
   admissible decoration sets are disjoint, neither singleton carrier can
   coarsen to a decoration on the other side, and they are not both
   singleton-supported; and
3. on the low-rank side forced by item 2, one of the three literal
   certificates in Lemma 5.3 occurs: boundary incompatibility, a direct-core
   lock, or a five-attachment lock behind the displayed recursive adhesion.

The constructive theorem still needed in the sharp cell is therefore:

> **Labelled surplus exchange.**  Starting from a certificate in Lemma 5.3,
> use the direct contacts or the five attachments in the named block to
> reroute a supported core, preserving its literal frame trace, so as to
> create a decoration also supported on the opposite shore; or produce a
> proper internal separation together with the same independent block
> partition and explicit connected pairwise-adjacent realizations on both
> closed sides.

The promotion outcome closes by Theorem 4.1 and Corollary 5.2; the recursive
outcome closes by bilateral portal transfer.  A proposed proof must name the
actual separator and the realizing sets.  A bare web order, attachments on
unnamed segments, or an arbitrary proper-minor colour state does not
discharge this gap.

This is the exact endpoint of the present constructive round.
