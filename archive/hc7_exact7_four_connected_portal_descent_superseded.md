# Four-connected portal closure or a strict exact-seven descent

**Status:** constructive draft for independent audit.

This note closes the common-face outcome in the connected-rich exact-seven
`(1,2)` branch.  It uses no boundary census and no palette-to-model
identification.  A prescribed portal which cannot be incorporated into the
rooted construction yields a smaller literal seven-adhesion; if every
prescribed portal can be incorporated, all six non-singleton-label portal
sets lie on one face, where a planar degree count is contradictory.

## 1. Setup

Let `G` be a finite seven-connected graph with a literal separation

\[
             V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
             \qquad |S|=7,                              \tag{1.1}
\]

where `L,R` are nonempty, there is no `L-R` edge, and `G[L]` is
four-connected.  Let `P,Q subseteq R` be disjoint connected `S`-full
packets joined by a literal `P-Q` edge.

Fix a distinguished literal `c in S`, put

\[
                 U=S-\{c\},\qquad A=N_{G[S]}(c),         \tag{1.2}
\]

and suppose

\[
                         |A|\ge3.                        \tag{1.3}
\]

In the attained paired-triangle state, (1.3) follows from the three
literal `c-B_i` requirements.  No other boundary edge is used below.

For `s in S`, write

\[
                         Q_s=N_L(s).                     \tag{1.4}
\]

A four-set `T subseteq U` is **admissible** when

\[
                         |T\cap A|\ge2.                  \tag{1.5}
\]

Fix three distinct labels

\[
                    H_0=\{h_1,h_2,h_3\}\subseteq A,    \tag{1.6}
\]

and, for each `x in U-H_0`, put

\[
                         T_x=H_0\cup\{x\}.              \tag{1.7}
\]

Each `T_x` is admissible; these three fixed four-label views will suffice.

## 2. The literal rooted lift

### Lemma 2.1 (an admissible rooted `K_4` gives the near model)

Let `T` be admissible, and let four distinct vertices `(x_s:s in T)`
satisfy `x_s in Q_s`.  If `L` has a `K_4` model with one branch bag rooted
at each `x_s`, then `G` has a literal labelled `K_7^vee` model.

#### Proof

Let `(B_s:s in T)` be the four rooted bags and enlarge them to

\[
                         B_s'=B_s\cup\{s\}.              \tag{2.1}
\]

They remain disjoint, connected, and pairwise adjacent.  Write

\[
                         U-T=\{r_P,r_Q\}.                \tag{2.2}
\]

Use the seven bags

\[
 (B_s':s in T),\qquad P\cup\{r_P\},\qquad
 Q\cup\{r_Q\},\qquad\{c\}.                            \tag{2.3}
\]

The packet bags are connected and adjacent through the literal `P-Q`
edge.  Fullness makes both packet bags adjacent to every rooted bag and to
`{c}`.  The four rooted bags form a clique.  Finally `{c}` is adjacent to
at least the two rooted bags whose labels lie in `T cap A`.  Thus the only
possibly missing pairs in (2.3) are at most two pairs incident with
`{c}`.  The bags form a literal labelled `K_7^vee` model.  \(\square\)

Every adjacency used here is a literal host edge; no quotient-completion
edge or color name is expanded as a model bag.

## 3. Matching facts forced by seven-connectivity

The following elementary fact will synchronize faces belonging to
different label sets.

### Lemma 3.1 (five prescribed labels have distinct portals)

Every set `W subseteq S` with `|W|<=5` has a matching into `L` in the
literal portal graph.

#### Proof

Suppose Hall fails.  There is a nonempty `I subseteq W` with

\[
                         |N_L(I)|\le |I|-1\le4.          \tag{3.1}
\]

A four-connected graph has at least five vertices, so `L-N_L(I)` is
nonempty.  Delete

\[
                         N_L(I)\cup(S-I).                \tag{3.2}
\]

This set has order at most

\[
                     (|I|-1)+(7-|I|)=6.                 \tag{3.3}
\]

No vertex of `L-N_L(I)` sees `I`; the other boundary literals were
deleted; and there is no `L-R` edge.  Hence (3.2) separates the nonempty
set `L-N_L(I)` from the nonempty set `R`, contradicting
seven-connectivity.  \(\square\)

We also use the audited prescribed-portal theorem:

> If `T subseteq S`, `1<=|T|<=4`, and a literal portal edge `sx` with
> `s in T` is prescribed, then either it extends to a matching saturating
> `T`, or there is a strict exact-seven descent with new boundary
> `(S-I) union N_L(I)` for some nonempty `I subseteq T-{s}`.  The tiny-shore
> alternative is impossible when `L` is four-connected.

This is Theorem 2.1 and Corollary 2.2 of
`../results/hc7_exact7_prescribed_portal_extension_or_adhesion.md`.

## 4. All six portal systems synchronize

### Lemma 4.1 (admissible matching or strict descent)

At least one of the following holds.

1. There is a strict actual order-seven adhesion whose connected `L`-side
   has fewer vertices than the old shore `L`.
2. For every `x in U-H_0`, every `s in T_x`, and every literal portal
   occurrence `sz` with `z in Q_s`, that prescribed occurrence belongs to
   a matching saturating `T_x`.

#### Proof

Apply the prescribed-portal theorem to each such triple `(T_x,s,z)`.  Its
tiny-shore outcome is excluded by four-connectivity.  Any descent is
outcome 1; if none occurs, every prescription extends, which is outcome 2.
\(\square\)

### Lemma 4.2 (one common face)

If the strict descent in Lemma 4.1 does not occur and `G` has no labelled
`K_7^vee` model, then `L` is planar and one face `F` of its unique plane
embedding contains

\[
                         N_L(U)=\bigcup_{s in U}Q_s.      \tag{4.1}
\]

#### Proof

Fix `x in U-H_0`.  The root sets of matchings saturating `T_x` are the
bases of the rank-four transversal matroid presented by
`(Q_s:s in T_x)`.  Its basis-exchange graph is connected, and consecutive
bases share three actual portal vertices.

For every such basis, the rooted-`K_4` theorem of Fabila-Monroy and Wood
gives a rooted `K_4`, or makes the four roots cofacial in a plane embedding
of `L`.  The rooted outcome gives `K_7^vee` by Lemma 2.1, so it is absent.
Thus `L` is planar.  Four-connectivity makes its plane embedding unique up
to reflection, and distinct faces share at most two vertices.  Consecutive
bases therefore lie on the same face.  Call this face `F_x`.

Lemma 3.1 gives distinct portal representatives `y_i in Q_{h_i}` for the
three labels in `H_0`.  Lemma 4.1(2) says that every literal portal
occurrence belonging to a label in `T_x`, including each `h_i y_i`, occurs
in a root basis for `T_x`.  Hence

\[
                         y_1,y_2,y_3 in V(F_x)           \tag{4.2}
\]

for each of the three choices of `x`.  Distinct faces in a
three-connected plane graph share at most two vertices, so the three
faces `F_x` are one common face `F`.

Every label `s in U` belongs to at least one `T_x`: the labels outside
`H_0` belong to their own view, while each `h_i` belongs to all three.
For every literal occurrence `sz`, Lemma 4.1(2) therefore extends `sz` to
a root basis in one such view.  That basis lies on `F`, so `z in V(F)`.
This proves (4.1).  \(\square\)

## 5. The common face is impossible

### Lemma 5.1 (one unplaced label still violates the degree budget)

The common-face outcome of Lemma 4.2 is impossible.

#### Proof

Take `F` as the outer face of the simple plane graph `L`, and put

\[
 f=|V(F)|,\qquad h=|V(L)-V(F)|,\qquad
 n=f+h,\qquad m=|E(L)|.                                \tag{5.1}
\]

Four-connectivity gives `d_L(v)>=4` for every `v in V(F)`.  A vertex
`z notin V(F)` has no neighbour in `U`, by Lemma 4.2, and no neighbour in
`R`, by the separation.  Its only possible neighbour outside `L` is the
single literal `c`.  Seven-connectivity gives `d_G(z)>=7`, and hence

\[
                         d_L(z)\ge6.                     \tag{5.2}
\]

It follows that

\[
                         2m\ge4f+6h.                     \tag{5.3}
\]

On the other hand, Euler's formula with outer-face length `f` gives

\[
                         m\le3n-3-f,
 \qquad\text{so}\qquad 2m\le4f+6h-6.                   \tag{5.4}
\]

Equations (5.3) and (5.4) are contradictory.  \(\square\)

## 6. Infinite-family dichotomy

### Theorem 6.1 (four-connected exact-seven portal closure)

Under (1.1)--(1.3), at least one of the following holds.

1. `G` contains a literal labelled `K_7^vee` minor.
2. There is a strict actual order-seven adhesion whose connected side is a
   nonempty proper subset of `L` and is full to its new literal boundary.

In outcome 2 the boundary map is explicit:

\[
             S\longmapsto \Omega=(S-I)\cup N_L(I),       \tag{6.1}
\]

where `I` is a nonempty subset of one of the four-sets `T_x`, has order at
most three, and

\[
                         |N_L(I)|=|I|.                   \tag{6.2}
\]

#### Proof

If a prescribed matching fails, Lemma 4.1 and the prescribed-portal
theorem give outcome 2, including fullness and strict descent.  Otherwise
Lemma 4.2 gives the labelled near model or the common facial outcome.
Lemma 5.1 excludes the latter, leaving outcome 1.  \(\square\)

This theorem eliminates an unbounded connectivity class through one
literal rooted-model principle.  It does not assert that the old attained
equality partition pulls back through (6.1); the output is instead a named
strict exact-seven adhesion handoff.  If state preservation is required by
the global induction, it remains an independent obligation at that
handoff.
