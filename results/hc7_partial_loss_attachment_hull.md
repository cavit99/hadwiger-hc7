# Attachment hulls at a first connectivity-losing forest contraction

**Status:** written proof; separate internal audit GREEN.

This note records the exact host information supplied by a six-cut at an
inclusion-minimal first connectivity loss.  It also gives a chromatic
strengthening when the unique contracted fibre is bipartite.  Neither result
by itself closes the atomic common-frame theorem.

## 1. Setup

Let `G` be seven-connected, let `F_0` be a nonempty forest in `G`, and put

\[
                              P=G/F_0.
\]

Assume that `P` is not seven-connected, while `G/F'` is seven-connected for
every proper edge subset `F'` of `F_0`.  Let `T` be a separator of `P` of
order six.  The minimal partial-loss lemma implies that every nontrivial
component of `F_0` has its image in `T`.

Write these nontrivial tree components as

\[
                      R_1,\ldots,R_q
\]

and their images in `P` as `z_1,...,z_q`.  Put

\[
                Z=\{z_1,\ldots,z_q\},\qquad O=T-Z.
\]

Thus `|O|=6-q`, and the vertices of `O` are literal vertices of `G` because
they are not images of nontrivial `F_0`-components.  A component of `P-T`
has the same literal vertex set in `G`; call such a lifted component `C`.
For each `j`, define

\[
             A_j(C)=\{v\in V(R_j):v\text{ has a neighbour in }C\}.
                                                               \tag{1.1}
\]

## 2. Every attachment set spans its whole forest tree

### Theorem 2.1 (attachment-hull theorem)

For every lifted component `C` of `P-T`:

1. its literal host neighbourhood is

   \[
                   N_G(C)=O\mathbin{\dot\cup}
                           \bigcup_{j=1}^q A_j(C);       \tag{2.1}
   \]

2. for every `j` and every edge `h` of `R_j`, the set `A_j(C)` meets both
   components of `R_j-h`;
3. equivalently, the minimal subtree of `R_j` containing `A_j(C)` is all of
   `R_j`; in particular, every leaf of `R_j` belongs to `A_j(C)`; and
4. consequently

   \[
                    |N_G(C)|=6-q+
                         \sum_{j=1}^q |A_j(C)|\ge7.      \tag{2.2}
   \]

#### Proof

The graph `P` is six-connected.  Since `N_P(C)` is a separator contained in
the six-set `T`, it follows that

\[
                              N_P(C)=T.                 \tag{2.3}
\]

Every nontrivial contracted fibre lies in `T`.  Expanding all of them does
not change the open components, so every host neighbour of `C` lies in
`O` or in one of the trees `R_j`.  Equation (2.3) shows that every member
of `O` has a neighbour in `C`.  This proves (2.1).

Fix `j` and an edge `h` of `R_j`.  In

\[
                         H_h=G/(F_0-\{h\}),             \tag{2.4}
\]

the image `z_j` is replaced by two adjacent vertices `u_h,v_h`, representing
the two components of `R_j-h`.  Inclusion-minimality makes `H_h`
seven-connected.  The set

\[
                   S_h=(T-\{z_j\})\cup\{u_h,v_h\}       \tag{2.5}
\]

has order seven and separates the same open components as `T`.  The
neighbourhood in `H_h` of `C` is a separator contained in `S_h`; hence
seven-connectivity forces it to equal `S_h`.  In particular, `C` has a
neighbour in each of the two split sides.  On expansion, this says that
`A_j(C)` meets both components of `R_j-h`.

A vertex set in a tree meets both sides of every edge exactly when its
minimal spanning subtree is the whole tree.  Applying the preceding
conclusion to a leaf edge also shows directly that its leaf belongs to
`A_j(C)`.  Finally, (2.2) follows from (2.1) and seven-connectivity of `G`.
\(\square\)

### Corollary 2.2 (the one-tree form)

Suppose `q=1`, write `R=R_1`, and put `A_C=A_1(C)`.  Then

\[
                         N_G(C)=O\mathbin{\dot\cup}A_C,
            \qquad |O|=5,\qquad |N_G(C)|=5+|A_C|.       \tag{2.6}
\]

Every leaf of `R` is a literal neighbour of every lifted component of
`P-T`.  Thus the leaves are common contacts, but Theorem 2.1 does not
identify them with endpoint supports in the fixed atomic `H_0`
subdivision.

## 3. The exact response supplied by one lifted component

Assume now that `G` is strongly seven-contraction-critical: `G` is
seven-chromatic and every proper minor is six-colourable.

### Proposition 3.1 (one-sided exact-block response)

Let `C` be a lifted component and put `S_C=N_G(C)`.  For every nonempty
independent set `I` of `G[S_C]`, the graph `G-C` has a proper
six-colouring in which `I` is exactly one colour class on `S_C`.

If `D` is another lifted component satisfying

\[
                         A_j(C)\subseteq A_j(D)
                         \quad(1\le j\le q),            \tag{3.1}
\]

then `D` is also adjacent to every vertex of `S_C`.  In that case both
closed shores of the separation with boundary `S_C` have the corresponding
exact-block six-colourings.

#### Proof

The connected graph `G[C\cup I]` can be contracted to one vertex.  The
result is a proper minor because another component of `P-T` remains.
Six-colour that minor, expand the independent set `I` with the colour of
the contracted vertex, and restrict to `G-C`.  Every vertex of `S_C-I`
has a neighbour in `C`, so it is adjacent to the contracted vertex and
avoids that colour.  Hence `I` is the exact boundary colour block.

Every lifted component is adjacent to each ordinary vertex in `O` by
(2.3).  Under (3.1), `D` is also adjacent to every vertex in every
`A_j(C)`, and therefore to all of `S_C` by (2.1).  Contracting `D\cup I`,
expanding `I`, and restricting to `G[C\cup S_C]` gives the response on the
other closed shore.  \(\square\)

In the one-tree case, an attachment set of order at most four gives a host
separator of order at most nine.  It is a two-sided full response interface
only when the comparability condition in Proposition 3.1 (or another
literal opposite full subgraph) is also available.  Attachment count alone
does not provide that missing pole.

## 4. A bipartite one-tree fibre is exactly six-chromatic after contraction

Continue to assume `q=1`, and let `z` be the image of `R` in `P`.

### Theorem 4.1 (bipartite-fibre chromatic saturation)

If the induced graph `G[V(R)]` is bipartite, then

\[
                              \chi(P)=6.                \tag{4.1}
\]

Let `(X,Y)` be its bipartition.  In every proper six-colouring `phi` of
`P`, put `alpha=phi(z)`.  For every colour `beta` different from `alpha`,
each of `X` and `Y` has a neighbour in `V(G)-V(R)` whose image in `P` has
colour `beta`.

#### Proof

The graph `P` is a proper minor of `G`, so it is six-colourable.  Suppose
first that `P` has a proper colouring with at most five colours, and let
`alpha` be the colour of `z`.  Retain that colouring outside `R`, colour
all vertices of `Y` with `alpha`, and colour all vertices of `X` with one
fresh sixth colour.  Every external neighbour of `R` is represented by a
neighbour of `z` in `P`, and therefore avoids `alpha`; the fresh colour is
absent outside `R`.  All internal edges cross `(X,Y)`.  This is a proper
six-colouring of `G`, a contradiction.  Hence (4.1) holds.

Now fix `phi` and a colour `beta` different from `alpha`.  If `X` had no
external neighbour of colour `beta`, retain `phi` outside `R`, colour `X`
with `beta`, and colour `Y` with `alpha`.  The same adjacency check gives a
proper six-colouring of `G`, again a contradiction.  Thus `X` has the
asserted contact.  Interchanging `X` and `Y` proves the statement for the
other side.  \(\square\)

The theorem converts the bipartite one-tree branch into a literal
five-colour contact condition on both sides of the fibre.  It does not turn
those colour classes into atomic branch-set labels, and it does not by
itself produce a `K_7` model, a two-vertex dominating-model transversal, or
a smaller same-form instance.

## 5. Trust boundary

The attachment-hull conclusion is host-level and literal.  Its leaves are
actual neighbours of every lifted component.  Nevertheless:

- attachment sets belonging to two components may be incomparable, so an
  opposite full pole for `N(C)` is not automatic;
- a leaf of an `F_0`-tree need not lie on the fixed `H_0` subdivision or
  carry a distinct clean-root endpoint support; and
- Theorem 4.1 requires the whole induced fibre `G[V(R)]` to be bipartite.
  A colouring of a contraction does not in general expand through a
  non-bipartite or chorded fibre.

The
[adjacent barrier note](../barriers/hc7_partial_loss_chromatic_lift_barriers.md)
makes the last two failures explicit.
