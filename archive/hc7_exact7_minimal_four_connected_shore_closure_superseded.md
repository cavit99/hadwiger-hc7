# Minimal four-connected thin-shore closure

**Status:** superseded.  The global-minimum comparison below has a selection
gap: a minimum `(1,2)` cell need not retain the local hypotheses.  The
audited basis-cover theorem removes that comparison entirely.  This file is
retained only as research history.  It depended on the audited
exact-seven packet theorem, adaptive `(1,3)` reflection, prescribed-portal
descent, and four-connected rooted-face machinery, together with the draft
Hall-descent packet classification.

This note removes the equality-state pullback obligation from the
four-connected branch.  A failed prescribed portal either gives a smaller
`(1,2)` shore, gives a labelled `K_7^vee`, or merely swaps which boundary
label the prescribed portal represents in a transversal basis.

## 1. Setup and terminal outcomes

Let `G` lie in the hypothetical minimal-`HC_7` counterexample kernel.  Let

\[
             V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
             \qquad |S|=7,                              \tag{1.1}
\]

be an actual exact-seven `(1,2)` separation.  Assume:

1. `G[L]` is four-connected;
2. `R` contains disjoint connected `S`-full packets `P,Q` joined by a
   literal edge; and
3. the attained paired-triangle boundary supplies distinct
   `c,d_1,d_2 in S` with `cd_1,cd_2 in E(G[S])`.

Orient every exact-seven `(1,2)` separation in `G` toward its packet-thin
shore, and choose (1.1) with `|L|` minimum among **all** such oriented
separations.  Only after making this global minimum choice do we assume
the three displayed local conditions.  This distinction is essential:
a descended shore need preserve neither four-connectivity nor the attained
boundary state.

The terminal outcomes in this note are a literal labelled `K_7^vee` model
or a legal six-colouring obtained by exact packet reflection.  Thus, while
proving the local theorem, assume that neither terminal outcome occurs.

For `a in S`, put `mathcal P_a=N_L(a)`.  For a four-set `A subseteq S`,
call a four-set `Z subseteq L` an **`A`-basis** when literal `A-L` edges
contain a matching between `A` and `Z`.

## 2. The compulsory portal is a basis exchange

### Lemma 2.1 (unforced boundary matchability)

Every set `A subseteq S` of order at most four has a matching into `L`
saturating `A`.

#### Proof

Suppose Hall fails for a nonempty `W subseteq A`.  Then

\[
                         |N_L(W)|<|W|\le4.              \tag{2.1}
\]

A four-connected graph has at least five vertices, so
`L-N_L(W)` is nonempty.  The set

\[
                         (S-W)\cup N_L(W)               \tag{2.2}
\]

separates that nonempty set from the nonempty old shore `R`, and by (2.1)
has order at most six.  This contradicts seven-connectivity.  Hall's
theorem proves the claim.  \(\square\)

### Lemma 2.2 (compulsory-portal swap)

Fix `A subseteq S`, `1<=|A|<=4`, `s in A`, and a literal portal edge
`sz` with `z in L`.  Suppose the minimal forced-Hall witness has

\[
 U\subseteq A-\{s\},\quad
 Y=N_{L-\{z\}}(U),\quad
 X=N_L(U)=Y\cup\{z\},\quad
 |Y|=|U|-1,                                             \tag{2.3}
\]

and suppose `z` has the unique neighbour `u_* in U`.  Then some `A`-basis
contains `z`.  More precisely, there is a matching saturating `A` in
which `u_*` is matched to `z`, `U-{u_*}` is matched to `Y`, and `A-U` is
matched into `L-X`.

#### Proof

Inclusion-minimality of `U` gives

\[
 |N_Y(W)|\ge |W|\qquad
       (\varnothing\ne W\subsetneq U).                 \tag{2.4}
\]

In particular Hall matches `U-{u_*}` into `Y`.

We claim that `A-U` can be matched into `L-X`.  Otherwise there is
`W subseteq A-U` with

\[
                         |N_{L-X}(W)|<|W|.              \tag{2.5}
\]

Because `N_L(U)=X`,

\[
 |N_L(U\cup W)|
   =|X\cup N_{L-X}(W)|
   <|U|+|W|=|U\cup W|,                                 \tag{2.6}
\]

contrary to Lemma 2.1.  The three displayed matchings use the disjoint
right-hand sets `{z}`, `Y`, and `L-X`, so their union is the required
matching.  \(\square\)

The important point is that the failed edge `sz` need not itself extend.
The same literal root `z` survives in a transversal basis with its label
rotated from `s` to `u_*`.

## 3. Every portal root lies in a basis

Fix the paired-triangle notation used by the audited four-connected portal
exchange theorem.  Put

\[
 D=\{d_1,d_2\},\qquad W=S-(D\cup\{c\}),
 \qquad A_Y=D\cup Y\quad(Y\in {W\choose2}).             \tag{3.1}
\]

### Lemma 3.1 (basis coverage at minimum shore order)

For every `Y in {W choose 2}`, every `s in A_Y`, and every
`z in mathcal P_s`, the vertex `z` belongs to an `A_Y`-basis.

#### Proof

Apply the prescribed-portal extension theorem to `A_Y` and `sz`.  Its tiny
shore outcome is impossible because `G[L]` is four-connected and hence
has at least five vertices.

An extension directly supplies the desired basis.  Consider an exact-seven
descent.  Its Hall data satisfy the hypotheses of the Hall-descent packet
classification: `C=L-X` is connected and full to
`Omega=(S-U) union X`, while the old adjacent full packets `P,Q` lie in the
opposite descended shore.

If two adjacent `Omega`-full packets pull through, the exact-seven packet
theorem orients the new cell as `(1,2)` or `(1,3)`, with `C` on its
packet-thin side.  The `(1,3)` case is terminal by adaptive reflection.
The `(1,2)` case has `|C|<|L|`, contrary to the global minimum choice in
Section 1.  No connectivity or equality state on `C` is needed for that
contradiction.

The alternating six-cycle outcome is terminal by the labelled
`K_7^vee` handoff in the Hall-descent packet classification.  The only
remaining outcome is a compulsory portal, and Lemma 2.2 supplies an
`A_Y`-basis containing `z`.  \(\square\)

## 4. Rooted-face synchronization and closure

### Lemma 4.1 (basis-cover rooted-face principle)

Let `A subseteq S` have order four.  Suppose every vertex of

\[
                         N_L(A)=\bigcup_{a\in A}mathcal P_a \tag{4.1}
\]

belongs to an `A`-basis.  Then either some `A`-basis is the root set of a
rooted `K_4` model in `G[L]`, or `G[L]` is planar and one face contains
all of `N_L(A)`.

#### Proof

The `A`-bases are the bases of the rank-four transversal matroid on
`N_L(A)`, so their basis-exchange graph is connected by exchanges of one
literal root.  If one basis roots a `K_4`, the first outcome holds.

Otherwise the four-connected rooted-`K_4` theorem makes `G[L]` planar and
puts each basis on a face.  The embedding is unique because `G[L]` is
three-connected.  Consecutive bases share three actual vertices, whereas
two distinct faces of a three-connected plane graph share at most two.
Thus consecutive bases use the same face, and connectedness of the basis
graph gives one face for all bases.  Basis coverage then puts every vertex
of (4.1) on that face.  \(\square\)

### Theorem 4.2 (minimal four-connected thin-shore closure)

Under the setup of Section 1, `G` contains a literal labelled `K_7^vee`
model or the attained state reflects and `G` is six-colourable.

#### Proof

Apply Lemmas 3.1 and 4.1 to every `A_Y` in (3.1).  If some basis roots a
`K_4`, enlarge its four rooted bags by the four boundary labels matched to
their roots.  These four bags together with `P,Q` form a literal `K_6`.
The singleton `{c}` meets `P,Q` and the bags anchored at `d_1,d_2`, so it
misses at most two rim bags, with both missing edges incident with `{c}`.
This is a labelled `K_7^vee`, a terminal outcome.

Otherwise, for every `Y`, one face `F_Y` contains `N_L(A_Y)`.  If two
two-sets `Y,Y' subseteq W` share a member, any `A_Y`-basis supplies three
distinct roots representing the three labels in `A_Y cap A_{Y'}`.  Those
three vertices lie on both `F_Y` and `F_{Y'}`, so the faces are equal.
The intersection graph of the two-subsets of the four-set `W` is
connected.  Hence all `F_Y` are a single face `F`, and

\[
                         N_L(S-\{c\})\subseteq V(F).    \tag{4.2}
\]

The audited cofacial-portal degree theorem applied to (4.2) gives a vertex
of `G` of degree at most six, contradicting seven-connectivity.  Therefore
one of the terminal outcomes must occur.  \(\square\)

## 5. Scope

The theorem is state-free across descent: it never asserts that an equality
partition pulls back from `S` to `Omega`.  Minimum thin-shore order is the
well-founded measure.  The compulsory-portal residue is used as a
transversal-basis exchange, while the two-packet residue is the only
recursive transition.

This closes the four-connected branch only.  A three-connected thin shore
with a three-cut still needs an analogous composition analysis for the
support-four lobe descent; that descent is not generally a forced-Hall map.
