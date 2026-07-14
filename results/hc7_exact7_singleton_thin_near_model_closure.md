# Singleton-thin Moser packet paths force a labelled near model

**Status:** proved and independently audited.

This note closes the packet-entanglement residue left by the audited
singleton-thin Moser-extension escape theorem.  The conclusion is a literal
`K_7` or `K_7^-` model, not a claim that the two packets can be rerouted.
The proof works for both the pure Moser spindle and its one-edge extension,
and does not require an edge between the packets.

The earlier avoiding-path branch is recorded in
`hc7_exact7_singleton_thin_moser_extension_escape.md`; the new ingredient
here is the first-packet-hit truncation in Lemma 4.1.

## 1. Setup

Let

\[
 V(G)=\{q\}\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad |S|=7,                                         \tag{1.1}
\]

where `q` is anticomplete to `R` and `N(q)=S`.  Assume that `G` is not
six-colourable and every proper minor of `G` is six-colourable.  Let
`P_1,P_2 subseteq R` be vertex-disjoint connected `S`-full packets; no
`P_1-P_2` edge is assumed.

Use the standard labels `S={0,1,...,6}` and assume

\[
 E(M)=\{01,02,03,04,12,16,26,34,35,45,56\}
       \subseteq E(G[S])\subseteq E(M+13).              \tag{1.2}
\]

Thus `G[S]` is either `M` or `M+13`.  Only the common edges displayed in
(1.2) are used below.

## 2. A forced literal `4-6` path

### Lemma 2.1 (exact-trace path)

There is a literal `4-6` path `W` whose internal vertices all lie in `R`.

#### Proof

The pair `25` is independent in both boundary graphs.  Contract the
connected star `q union {2,5}` and six-colour the resulting proper minor.
Delete the contracted connector and expand `2,5` with its colour on
`G-q`.  Since the contracted representative was adjacent to every member
of `S-{2,5}`, the pair `25` is an exact boundary colour block.

All six colours occur on `S`.  Otherwise a colour absent from `S` can be
assigned to `q`, which has no neighbour in `R`, yielding a six-colouring
of `G`.  Consequently the remaining vertices

\[
                         0,1,3,4,6                     \tag{2.1}
\]

are singleton boundary blocks of five distinct colours.

The pair `46` is also independent.  If `4` and `6` lie in distinct
components of the subgraph induced by their two colours, swap those colours
in the component containing `4`.  This merges exactly the two singleton
blocks `4,6`; the boundary then uses only five colours, and the unused
sixth colour again extends to `q`.  Hence `4` and `6` lie in one
bichromatic component.  A path between them in that component has no other
boundary vertex internally, by (2.1), and it cannot contain `q`, which is
absent from the expanded colouring.  Its internal vertices therefore lie
in `R`.  \(\square\)

## 3. Escape gives `K_7`

### Lemma 3.1 (packet-avoiding path)

If the interior `X` of `W` is disjoint from `P_1 union P_2`, then `G`
contains a literal `K_7` model.

#### Proof

Use the seven branch sets

\[
 \{1\},\quad \{2\},\quad \{6\},\quad \{3,q\},\quad
 \{5\}\cup P_1,\quad P_2,\quad \{0,4\}\cup X.        \tag{3.1}
\]

They are disjoint and connected.  The first three form the triangle
`126`.  The last set is connected through `04` and the path `W`, and its
last path edge meets `{6}`.  The bags containing `q,P_1,P_2` meet every
bag carrying a boundary literal by fullness.  In particular
`P_2` meets `P_1 union {5}` through literal `5`, so no packet-packet edge
is being inferred.  Finally `01,02,03,04,34,35,45` supply the remaining
literal boundary adjacencies.  Thus all twenty-one bag pairs are adjacent.
\(\square\)

## 4. A first packet hit gives `K_7^-`

### Lemma 4.1 (packet-hit truncation)

If the interior of `W` meets `P_1 union P_2`, then `G` contains a literal
`K_7^-` model, and hence a labelled `K_7^vee` model.

#### Proof

Orient `W` from `4` to `6`, and let `w` be its first internal vertex in
`P_1 union P_2`.  Write `P_h` for the unique packet containing `w` and
`P_o` for the other packet.  Let `Z` be the internal vertices of the
initial `4-w` subpath, excluding `w`.  By the first-hit choice,

\[
                         Z\cap(P_1\cup P_2)=\varnothing. \tag{4.1}
\]

Use the seven bags

\[
 \begin{aligned}
 A&=\{0,4\}\cup Z,            &B&=P_h\cup\{5\},\\
 C&=\{6\},                    &D&=P_o,\\
 E&=\{3,q\},                  &F&=\{1\},
                                      &G&=\{2\}.       \tag{4.2}
 \end{aligned}
\]

They are pairwise disjoint.  The bag `A` is connected through `04` and
the initial path segment; `B` is connected because `P_h` is full to the
literal `5`; and the other bags are plainly connected.  The last edge of
the truncated segment gives `A-B`.

The six bags

\[
                         B,C,D,E,F,G                    \tag{4.3}
\]

form a literal `K_6`.  Indeed, `B,D` meet every boundary-anchored bag by
packet fullness, and `B-D` is witnessed by the contact of `P_o` with the
literal `5` in `B`.  The bag `E` contains the universal-to-`S` vertex `q`.
The remaining three singleton pairs are the triangle edges

\[
                         16,\quad26,\quad12.            \tag{4.4}
\]

The bag `A` meets `B` by the truncated path, meets `D` by fullness at
`0`, meets `E` through `q0`, and meets `F,G` through `01,02`.  Its only
possibly missing rim adjacency is `A-C`.  Hence (4.2) is a literal
`K_7^-` model.  Deleting one further edge incident with `A`, if necessary,
exhibits the normalized labelled `K_7^vee`.  \(\square\)

## 5. Terminal singleton theorem

### Theorem 5.1 (singleton-thin near-model closure)

Under the setup of Section 1, `G` contains a literal `K_7` minor or a
literal labelled `K_7^vee` model.

#### Proof

Take the path from Lemma 2.1.  Lemma 3.1 applies if its interior avoids
both packets, and Lemma 4.1 applies at its first packet hit otherwise.
\(\square\)

In the frozen adaptive `(1,2)` residual, Dirac's neighbourhood inequality
and the audited singleton-boundary extraction say that a singleton thin
shore has exactly one of the two boundary graphs in (1.2).  Theorem 5.1
therefore closes the entire singleton-thin residual as an `S1` near-model
handoff.  It is uniform in the order and internal geometry of the opposite
shore.

The theorem does not close a nonsingleton support-four lobe, and a
`K_7^vee` model is a handoff rather than by itself a contradiction to
`K_7`-minor-freeness.
