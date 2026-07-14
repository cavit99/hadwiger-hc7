# Four-connected portal exchange

**Status:** proved and independently audited.

This note closes the whole four-connected thin-shore branch of the paired
exact-seven cell as a transition: either it supplies a literal labelled
`K_7^vee`, or a failed prescribed portal choice exposes a strictly smaller
actual seven-adhesion.  The proof uses complete portal sets, not one selected
representative from each set.

## 1. Literal setup

Let

\[
             V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
             \qquad |S|=7,
\]

be a literal separation in a finite simple seven-connected graph.  Thus
`L,R` are nonempty and there is no `L-R` edge.  Assume:

1. `G[L]` is four-connected;
2. `P,Q subseteq R` are disjoint connected `S`-full packets joined by a
   literal `P-Q` edge; and
3. there are distinct literals `c,d_1,d_2 in S` with
   `cd_i in E(G[S])` for `i=1,2`.

For `s in S`, write

\[
                         \mathcal P_s=N_L(s).
\]

Every `mathcal P_s` is nonempty: otherwise the other six boundary vertices
would separate the nonempty shore `L` from the nonempty shore `R`.

## 2. Four complete portal systems

We use the following audited rooted-face principle.  Let
`A={s_1,s_2,s_3,s_4} subseteq S`.  Suppose every literal portal edge
`s_i z`, with `z in mathcal P_{s_i}`, extends to a matching from `A` into
`L` saturating `A`.  Then either

1. some such system of distinct representatives is the root set of a
   rooted `K_4` model in `G[L]`; or
2. `G[L]` is planar and one face contains
   `mathcal P_{s_1} union ... union mathcal P_{s_4}`.

Indeed, the images of saturating matchings are the bases of a rank-four
transversal matroid.  Their basis-exchange graph is connected by
one-element exchanges, so consecutive root sets share three actual
vertices.  The four-connected rooted-`K_4` theorem puts every root set
without a rooted model on a face.  In the unique embedding of a
three-connected planar graph, two distinct faces share at most two vertices;
hence all bases use one face.  Since every portal edge extends, every portal
vertex occurs in a basis.  This is the SDR facial-coherence theorem proved
in `hc7_near_k7_active_root_face_exchange.md`.

## 3. The exchange theorem

### Theorem 3.1 (rooted model or smaller exact-seven shore)

Under the setup above, at least one of the following holds.

1. **Labelled near model.**  `G` contains a literal labelled `K_7^vee`
   model.
2. **Exact-seven descent.**  There are a set `A subseteq S` of order four,
   a nonempty `U subseteq A` of order at most three, and
   `X=N_L(U)` with
   \[
                       |X|=|U|,\qquad 1\le |X|\le3,
   \]
   such that
   \[
                       \Omega=(S-U)\cup X
   \]
   is an actual seven-boundary.  The graph `G[L-X]` is nonempty and
   connected, its vertex set is `Omega`-full, and it has fewer vertices
   than `L`.

#### Proof

Put

\[
 D=\{d_1,d_2\},\qquad W=S-(D\cup\{c\}).
\]

Thus `|W|=4`.  For every two-set `Y subseteq W`, set

\[
                         A_Y=D\cup Y.                   \tag{3.1}
\]

Fix such a `Y`, a label `s in A_Y`, and a portal
`z in mathcal P_s`.  Apply the prescribed-portal extension theorem to
`A_Y` and the literal edge `sz`.
Its tiny-shore outcome is impossible because a four-connected graph has at
least five vertices.  If its exact-seven descent occurs, its corollary says
that `G[L-X]` is the unique connected, nonempty, strictly smaller full shore
behind the displayed boundary `Omega`; this is outcome 2.

We may therefore assume that no such descent occurs for any of the displayed
choices.  Every portal edge for every family `A_Y` then extends to a
saturating matching.  Apply the complete-portal rooted-face principle of
Section 2 to each `A_Y`.

Suppose first that one representative quadruple for some `A_Y` has a rooted
`K_4` model with bags `B_s`, `s in A_Y`, where the bag `B_s` contains the
representative chosen from `mathcal P_s`.  Enlarge each bag to

\[
                              B_s\cup\{s\}.
\]

These four bags remain connected, disjoint and pairwise adjacent.  Together
with `P` and `Q` they form a literal `K_6`: both packets meet every boundary
anchor and the assumed `P-Q` edge supplies their mutual adjacency.  The
singleton `{c}` meets `P,Q` and the two bags anchored at `d_1,d_2`.
Thus it misses at most two of the six rim bags, and both missing pairs are
incident with `{c}`.  After ignoring surplus adjacencies, the seven bags
form a labelled `K_7^vee`.  This is outcome 1.

It remains to assume that no representative quadruple has a rooted `K_4`.
For each two-set `Y subseteq W`, the rooted-face principle gives a face
`F_Y` containing

\[
                    \bigcup_{s\in A_Y}\mathcal P_s.    \tag{3.2}
\]

If two two-sets `Y,Y'` share one member, then `A_Y cap A_{Y'}` has three
labels.  A saturating matching for `A_Y` supplies three distinct portal
vertices for those common labels, and (3.2) puts all three on both `F_Y`
and `F_{Y'}`.  Distinct faces of a three-connected plane graph share at
most two vertices, so `F_Y=F_{Y'}`.  The graph on the two-subsets of the
four-set `W`, adjacent when they share one member, is connected.  Hence all
the faces `F_Y` are one face `F`.  Since

\[
                 S-\{c\}=D\cup W,
\]

equation (3.2) now gives

\[
                         N_L(S-\{c\})\subseteq V(F).    \tag{3.3}
\]

The cofacial portal degree theorem applied to (3.3) produces a vertex
`v in L-V(F)` with `d_G(v)<=6`, contradicting seven-connectivity.  This
last case is impossible, and the proof is complete.  \(\square\)

## 4. Exact scope

The descent outcome preserves the literal boundary map and strict shore
order, but this theorem does **not** claim that the paired equality state or
the packet vector is preserved.  It therefore closes the four-connected
geometry as an `S1`/adhesion handoff, not by itself as a recursive `S3`
colouring argument.

The remaining local thin-shore geometry is three-connected but not
four-connected.  Its three-separators must now either supply the analogous
labelled near model or carry enough exact state to make the smaller
seven-adhesion terminal.
