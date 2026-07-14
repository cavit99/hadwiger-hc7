# Four-connected basis-cover closure

**Status:** proved below and independently audited beside this note.

This note strengthens the audited four-connected portal-exchange theorem.
Seven-connectivity makes every boundary four-set matchable into the thin
shore.  A minimal Hall witness then shows that every literal portal vertex
belongs to some transversal basis, even when its own prescribed portal edge
cannot be forced.  Basis coverage, rather than edge-by-edge extendability,
is exactly what the rooted-face argument needs.

## 1. Literal setup

Let

\[
             V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
             \qquad |S|=7,                              \tag{1.1}
\]

be an actual separation in a finite simple seven-connected graph.  Assume:

1. `G[L]` is four-connected;
2. `P,Q subseteq R` are disjoint connected `S`-full packets joined by a
   literal edge; and
3. there are distinct `c,d_1,d_2 in S` with
   `cd_1,cd_2 in E(G[S])`.

For `a in S`, put

\[
                         \mathcal P_a=N_L(a).            \tag{1.2}
\]

For `A subseteq S`, an **`A`-basis** is a set `Z subseteq L` for which
the literal bipartite graph between `A` and `Z` has a matching saturating
`A` and `Z`.  Thus `|Z|=|A|`.

## 2. Boundary matchability

### Lemma 2.1 (every four-set is matchable)

Every `A subseteq S` with `|A|<=4` has a matching into `L` saturating
`A`.

#### Proof

If Hall fails, choose a nonempty `W subseteq A` with

\[
                         |N_L(W)|<|W|\le4.              \tag{2.1}
\]

A four-connected graph has at least five vertices, whereas (2.1) gives
`|N_L(W)|<=3`; hence `L-N_L(W)` is nonempty.  The set

\[
                         (S-W)\cup N_L(W)               \tag{2.2}
\]

separates `L-N_L(W)` from the nonempty shore `R`: there is no `L-R` edge,
and no vertex of `L-N_L(W)` is adjacent to a member of `W`.  Its order is

\[
              7-|W|+|N_L(W)|\le6,                     \tag{2.3}
\]

contrary to seven-connectivity.  Hall's theorem proves the claim.
\(\square\)

## 3. Failed forcing still covers the prescribed root

### Lemma 3.1 (portal-root basis exchange)

Let `A subseteq S`, `1<=|A|<=4`, let `s in A`, and let `sz` be a literal
edge with `z in L`.  Then some `A`-basis contains the literal vertex `z`.

#### Proof

Try to match `A` into `L` while forcing `s` to `z`.  Equivalently, seek a
matching from `A-{s}` into `L-{z}`.  If it exists, adjoining `sz` gives an
`A`-basis containing `z`.

Otherwise choose an inclusion-minimal nonempty Hall witness
`U subseteq A-{s}` and put

\[
                Y=N_{L-\{z\}}(U).                      \tag{3.1}
\]

Minimality gives

\[
 |Y|=|U|-1,
 \qquad
 |N_Y(W)|\ge |W|
       \quad(\varnothing\ne W\subsetneq U).            \tag{3.2}
\]

Lemma 2.1 says that `U` is matchable into `L`.  Since it has only
`|U|-1` neighbours in `L-{z}`, the vertex `z` has a neighbour
`u_0 in U`.  Put

\[
                         X=N_L(U)=Y\cup\{z\}.           \tag{3.3}
\]

By (3.2), Hall matches `U-{u_0}` into `Y`.

We next claim that `A-U` is matchable into `L-X`.  If not, Hall supplies
`W subseteq A-U` with

\[
                         |N_{L-X}(W)|<|W|.              \tag{3.4}
\]

Using `N_L(U)=X`, we obtain

\[
 \begin{aligned}
 |N_L(U\cup W)|
   &=|X\cup N_{L-X}(W)|\\
   &<|U|+|W|=|U\cup W|,
 \end{aligned}                                         \tag{3.5}
\]

contrary to Lemma 2.1 applied to the subset `U union W subseteq A`.

Combine the matching of `U-{u_0}` into `Y`, a matching of `A-U` into
`L-X`, and the literal edge `u_0z`.  Their left sides partition `A` and
their right sides lie respectively in the pairwise disjoint sets
`Y`, `L-X`, and `{z}`.  Their union is a matching saturating `A` whose
root set contains `z`.  Notice that `z` represents `u_0`, not necessarily
the originally prescribed label `s`.  \(\square\)

This proof also disposes of the apparent tiny-shore exception: the
matching of the nonempty set `A-U` (which contains `s`) into `L-X` proves
that `L-X` is nonempty.

### Corollary 3.2 (complete basis coverage)

For every four-set `A subseteq S`, every vertex in

\[
                         N_L(A)=\bigcup_{a\in A}\mathcal P_a \tag{3.6}
\]

belongs to an `A`-basis.

#### Proof

Given `z in N_L(A)`, choose `s in A` with `sz in E(G)` and apply
Lemma 3.1.  \(\square\)

## 4. The weaker rooted-face hypothesis

### Lemma 4.1 (basis-cover rooted-face principle)

Let `A subseteq S` have order four.  If every vertex of `N_L(A)` belongs
to an `A`-basis, then either

1. some `A`-basis is the root set of a rooted `K_4` model in `G[L]`; or
2. `G[L]` is planar and one face contains all of `N_L(A)`.

#### Proof

The `A`-bases are exactly the bases of the rank-four transversal matroid
on ground set `N_L(A)`.  Its basis-exchange graph is connected, with
adjacent bases sharing three literal vertices.

If one basis roots a `K_4`, outcome 1 holds.  Otherwise the
four-connected rooted-`K_4` theorem makes `G[L]` planar and puts the four
vertices of every basis on one face.  Fix the unique plane embedding of
the three-connected graph `G[L]`.  Two distinct faces share at most two
vertices, while consecutive bases share three, so consecutive bases lie
on the same face.  Connectedness of the basis graph gives one face for
all bases.  Basis coverage puts all of `N_L(A)` on that face.  \(\square\)

## 5. Closure

### Theorem 5.1 (four-connected thin shore gives a labelled near model)

Under the setup of Section 1, `G` contains a literal labelled
`K_7^vee` model.

#### Proof

Put

\[
 D=\{d_1,d_2\},\qquad W=S-(D\cup\{c\}),
 \qquad A_Y=D\cup Y\quad(Y\in {W\choose2}).             \tag{5.1}
\]

Apply Corollary 3.2 and Lemma 4.1 to every `A_Y`.

Suppose some `A_Y`-basis roots a `K_4` in `G[L]`.  Match the four labels
of `A_Y` to its four roots and enlarge each rooted branch set by its
matched boundary label.  These four bags together with `P,Q` form a
literal `K_6`: both packets meet every boundary anchor, and `P-Q` is a
literal edge.  The singleton `{c}` meets `P,Q` and the two bags anchored
at `d_1,d_2`.  Hence it misses at most two rim bags, both missing pairs
are incident with `{c}`, and the seven bags form a literal labelled
`K_7^vee` model.

It remains that for every `Y`, one face `F_Y` contains `N_L(A_Y)`.  If
two two-sets `Y,Y' subseteq W` share one label, an `A_Y`-basis has three
distinct representatives for the three labels of `A_Y cap A_{Y'}`.
Those three vertices lie on both `F_Y` and `F_{Y'}`, so the faces are
equal.  The intersection graph of the two-subsets of the four-set `W` is
connected.  All `F_Y` are therefore one face `F`, and

\[
                         N_L(S-\{c\})\subseteq V(F).    \tag{5.2}
\]

The audited cofacial-portal degree theorem applied to (5.2) gives a
vertex of `G` of degree at most six, contradicting seven-connectivity.
Thus the rooted-model outcome must occur, and it gives the stated
`K_7^vee`.  \(\square\)

## 6. Scope

The theorem is purely structural.  It uses neither contraction-criticality
nor an attained equality state, and it invokes no recursive adhesion.  It
closes the whole four-connected thin-shore branch as a labelled
near-model handoff.  The exact remaining local geometry is a
three-connected, non-four-connected thin shore and the composition of its
three-cut descent.
