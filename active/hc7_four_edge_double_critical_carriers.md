# Four edge-local double-critical pairs and three full carriers

**Status:** proved and independently cold-audited in
[`hc7_four_edge_double_critical_carriers_audit.md`](hc7_four_edge_double_critical_carriers_audit.md).
Lemma 2.1 is the
edge-local content of Kawarabayashi--Pedersen--Toft, Proposition 3.3 and
Corollary 3.1; the proof in that paper uses double-criticality only for the
selected edge.  Proposition 4.1 is an elementary Menger consequence.  The
note does not prove `HC_7`.

The purpose of the note is to record exactly what four local
double-critical edges supply in the exact-two-row cell.  The output is three
disjoint connected carriers meeting a literal four-clique.  Pairwise
adjacency of those carriers is a separate, essential requirement.

## 1. Edge-local terminology

Let `G` be a graph with `chi(G)=k`, and let `xy` be an edge.  Call `xy`
**edge-locally double-critical** when

\[
                         \chi(G-\{x,y\})=k-2.
\]

No condition is imposed on the other edges of `G`.

## 2. Ordered paths from one edge

### Lemma 2.1 (edge-local ordered-colour path)

Let `xy` be edge-locally double-critical, let `phi` be a proper
`(k-2)`-colouring of `G-{x,y}`, and let

\[
                         j_1,j_2,\ldots,j_r
\]

be a nonempty ordered sequence of distinct colours of `phi`.  Then `G`
contains an `xy`-path

\[
                         x v_1v_2\cdots v_r y          \tag{2.1}
\]

with `phi(v_i)=j_i` for every `i`.

In particular, for every colour `j` there is a common neighbour of `x` and
`y` having colour `j`.  Common neighbours selected for distinct colours are
distinct.

#### Proof

Extend `phi` to a proper `(k-1)`-colouring of `G-xy` by assigning one new
colour `star` to both `x` and `y`.  Let `pi` be the cyclic permutation

\[
                         (\mathord{\star},j_1,\ldots,j_r)
\]

and fix every other colour.  Starting at `x`, form the generalized Kempe
chain for `pi`: from a vertex of one colour, retain neighbours of the next
colour under `pi`, and continue through the cyclic sequence.

If this generalized chain omits `y`, rotate the colours by `pi` on the
chain.  This remains a proper `(k-1)`-colouring of `G-xy`, changes the colour
of `x`, and leaves `y` with colour `star`.  The deleted edge `xy` can then be
restored, giving a `(k-1)`-colouring of `G`, contrary to `chi(G)=k`.

Thus the generalized chain contains `y`.  The only vertices with colour
`star` are `x` and `y`; following the layers from `x` until the first return
to colour `star` therefore gives (2.1), with the displayed colours in the
specified order.  Taking `r=1` proves the common-neighbour assertion.  This
is precisely the proof of Proposition 3.3 in the cited paper, and the proof
uses the chromatic-drop hypothesis only for the fixed edge `xy`.  \(\square\)

## 3. Application to the exact-two-row four-clique

Assume now that:

1. `chi(G)=7` and `G` is seven-connected;
2. `C={a,b,c,d}` induces a literal `K_4`;
3. each of `ac,ad,bc,bd` is edge-locally double-critical; and
4. `H=G-C`.

The division into rows is `ab | cd`.  The four locally double-critical
edges are exactly the cross-edges between the two rows.

For a cross-edge `xy`, put

\[
             X_{xy}=N_G(x)\cap N_G(y)\cap V(H).
\]

### Lemma 3.1 (three outside common neighbours and an ordered outside path)

For every cross-edge `xy`, one has

\[
                              |X_{xy}|\ge 3.            \tag{3.1}
\]

More precisely, in every proper five-colouring of `G-{x,y}`, let the two
vertices of `C-{x,y}` receive colours `alpha` and `beta`.  They are adjacent,
so `alpha != beta`.  For every ordering `j_1,j_2,j_3` of the other three
colours, there is a path

\[
                         x v_1v_2v_3 y                 \tag{3.2}
\]

whose three internal vertices lie in `H` and have colours
`j_1,j_2,j_3`, respectively.

#### Proof

Apply Lemma 2.1 to `xy`.  For each of the three colours outside
`{alpha,beta}`, its one-colour instance supplies a common neighbour of `x`
and `y`.  Such a neighbour cannot be either vertex of `C-{x,y}`, because
those two vertices have colours `alpha,beta`; it is not `x` or `y`, which
are absent from the colouring.  Hence it lies in `H`.  The three witnesses
have distinct colours and therefore are distinct, proving (3.1).

Applying the ordered-path part of Lemma 2.1 to all three remaining colours
gives (3.2).  Its internal vertices again avoid `C-{x,y}` by their colours,
and avoid `x,y` by definition, so all lie in `H`.  \(\square\)

This lemma is deliberately local: the five-colouring used for `ac` need not
be the five-colouring used for `bd`.

## 4. The complementary-pair carrier consequence

Choose the two vertex-disjoint cross-edges `ac` and `bd`.

### Proposition 4.1 (three disjoint `C`-full carriers)

There are three pairwise vertex-disjoint connected subgraphs

\[
                              P_1,P_2,P_3\subseteq H
\]

such that every `P_i` has a neighbour in each of `a,b,c,d`.

If, in addition, the three subgraphs are pairwise adjacent, then

\[
                    \{a\},\{b\},\{c\},\{d\},P_1,P_2,P_3        \tag{4.1}
\]

are the branch sets of a literal `K_7` model.

#### Proof

First, `H` is three-connected.  Indeed, if
`Z \subseteq V(H)` with `|Z|\le 2` disconnected `H`, then deleting
`C \cup Z`, a set of order at
most six, would disconnect `G`, contrary to seven-connectivity.

By Lemma 3.1, both `X_ac` and `X_bd` have order at least three.  The set
form of Menger's theorem in the three-connected graph `H` gives three
pairwise vertex-disjoint `X_ac-X_bd` paths.  Trivial paths are allowed when
the two sets intersect.  For completeness, otherwise Menger would give a
set `Z` of order at most two such that no vertex of `X_ac-Z` can reach a
vertex of `X_bd-Z` in `H-Z`.  Both differences are nonempty, so `H-Z`
would be disconnected, contrary to three-connectivity.  Let the vertex
sets of the three paths be `P_1,P_2,P_3`.

Each `P_i` is connected.  Its `X_ac` end is adjacent to both `a` and `c`,
and its `X_bd` end is adjacent to both `b` and `d`.  If the path is trivial,
its one vertex belongs to both common-neighbour sets and has all four
contacts.  Thus every `P_i` is `C`-full.

For the final assertion, the four singleton branch sets in (4.1) are
pairwise adjacent because `C` is a literal `K_4`.  Every path bag is
adjacent to all four singleton bags by the preceding paragraph.  The path
bags are mutually adjacent by the additional hypothesis.  All seven bags
are nonempty, connected and pairwise vertex-disjoint, so (4.1) is a
`K_7` model.  \(\square\)

### Exact remaining gap

Proposition 4.1 supplies disjointness and all four labelled contacts, but
not adjacency among the three carriers.  Neither ordinary
three-connectivity nor the edge-local KPT lemma supplies simultaneous
control of the three paths, nor does the proposition couple them to a fixed
four-linkage between pre-existing model cores.  The companion barrier note
`barriers/hc7_four_edge_double_critical_packaging_barrier.md` shows that
this missing packaging step is real.

## Reference

K. Kawarabayashi, A. S. Pedersen and B. Toft,
[*Double-critical graphs and complete minors*](https://doi.org/10.37236/359),
Electronic Journal of Combinatorics **17** (2010), R87, Proposition 3.3 and
Corollary 3.1.
