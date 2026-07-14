# Atomic root-deletion normalization

**Status:** proved and independently audited.

This note removes one whole family of false obstructions from the active
`z`-rooted connector composition.  In every nonsingleton compulsory atom,
the root `z` is not a cutvertex of the thin shore and deleting it leaves a
connected packet meeting all six other boundary literals.  Hence the
localized opposite-shore connector may be chosen to avoid `z`, and its
minimal union with `z` is a literal path or one `Y` with `z` as a leaf.

The result does not itself allocate all boundary duties between two
carriers.  Its exact remaining obstruction is the placement of the
`T`-bridges around this normalized path/`Y`.

## 1. Setup

Let

\[
 V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad S=W\mathbin{\dot\cup}\{u\},\qquad |W|=6,
\]

be a separation with no `A-R` edge and with both open shores nonempty.
Assume:

1. `G` is seven-connected, is not six-colourable, and every proper minor
   of `G` is six-colourable;
2. `A` is connected and `S`-full;
3. `zu` is the unique `A-u` edge; and
4. `R` contains two disjoint connected `S`-full packets.

Assume the width-two frontier is either connected bipartite, or is
`K_{1,3} dotunion K_3`.  In the first case put `U=emptyset` and `F=G[S]`.
In the second choose the retained triangle vertex `U={k}` as in the
audited atomic trace theorem, so that `u notin U`, and put

\[
                  F=G[S]-U=K_{1,3}\mathbin{\dot\cup}K_2.
\]

The audited two-carrier clique-OCT theorem applies to proper literal
two-list colourings of `F`; in both forms its retained duty is automatic.

## 2. Root deletion

### Theorem 2.1 (the root is not a thin-shore cutvertex)

If `|A|>=2`, then `A-z` is connected.

#### Proof

Suppose that `A-z` has at least two components.  Let `X` be any one of
them.  Since `zu` is the unique `A-u` edge, `X` has no neighbour at `u`.
Distinct components of `A-z` are anticomplete, there is no `A-R` edge,
and every neighbour of `X` outside `X` therefore lies in

\[
                             W\cup\{z\}.
\]

This set has order seven.  It separates the nonempty set `X` from the
nonempty old opposite shore `R`.  Seven-connectivity forces equality:

\[
                         N_G(X)=W\cup\{z\}.             \tag{2.1}
\]

Thus every component of `A-z` is `W`-full and is adjacent to `z`.

Use the two literal carriers

\[
                         C_2=X,\qquad C_1=A-X.
\]

The first is connected.  The second consists of `z` together with all
other components of `A-z`; each such component is adjacent to `z`, so it
too is connected.  They are disjoint and adjacent.  The carrier `C_2` is
`W`-full by (2.1), while `C_1` is `S`-full: another component of `A-z` is
`W`-full and `z` supplies the edge to `u`.

Consequently every vertex of `F-\{u\}` has both carrier labels available,
while `u` has label `1`.  Properly two-colour the component of `F`
containing `u` with `u` assigned label `1`, and orient every other
component arbitrarily.  This is a proper colouring from the literal
carrier lists.  In the exceptional frontier the retained duty is automatic
by the audited clique-OCT proposition.  The two-carrier synchronization
theorem, using the two full packets in `R`, now six-colours `G`, a
contradiction.  Hence `A-z` is connected.  \(\square\)

### Theorem 2.2 (the deleted-root shore is `W`-full)

If `|A|>=2`, then

\[
                           N_S(A-z)=W.                  \tag{2.2}
\]

#### Proof

Theorem 2.1 makes `A-z` nonempty and connected.  It has no neighbour at
`u`, because `zu` is the unique `A-u` edge.  Suppose some `w in W` also
had no neighbour in `A-z`.  Every neighbour of `A-z` outside that set
would then lie in

\[
                         \{z\}\cup(S-\{u,w\}),
\]

which has order six.  This set separates `A-z` from the nonempty old
opposite shore `R`, contradicting seven-connectivity.  Thus every member
of `W` has a neighbour in `A-z`, and `u` does not, proving (2.2).
\(\square\)

## 3. Normalized connector

### Corollary 3.1 (every two non-`u` labels connect away from `z`)

For arbitrary disjoint nonempty sets `B,C subseteq W`, there is a literal `B-C`
path whose internal vertices lie in `A-z`.

#### Proof

Choose `b in B,c in C`.  By Theorem 2.2 choose neighbours
`p_b,p_c in A-z`; they may coincide.  Theorem 2.1 supplies a
`p_b-p_c` path in `A-z`.  Adding the two boundary incidence edges and
simplifying gives the required path.  \(\square\)

Thus the opposite-shore connector furnished by atomic bichromatic-edge
localization may be replaced geometrically by a connector avoiding `z`.
This replacement is a branch-set normalization only; it is not asserted
to remain bichromatic in the localization colouring.

### Corollary 3.2 (literal path-or-`Y` core with rooted leaf)

Let `P` be a `B-C` path from Corollary 3.1, chosen with its internal path
`Q=P-S` inclusion-minimal.  Choose a shortest path `Z` in `A` from `z` to
`Q`, and truncate it at its first vertex `r in Q`.  Then

\[
                              T=Q\cup Z                 \tag{3.1}
\]

is a tree, `z` is a leaf of `T`, and `T` has maximum degree at most three
and at most one vertex of degree three.  Hence `T` is a path or a
subdivision of `Y`.

#### Proof

The internal vertices of `P` form a path `Q` contained in `A-z`.
Minimality of `Z` gives `V(Z) cap V(Q)={r}`.  The union of two paths with
exactly one common vertex is a tree.  Only `r` can have degree three; all
other vertices have degree at most two.  Since `z notin Q` and is an end
of `Z`, it is a leaf of `T`.  \(\square\)

## 4. Exact bridge certificate

For a component `D` of `A-T`, put

\[
       X_D=N_T(D),\qquad A_D=N_S(D).
\]

### Lemma 4.1 (bridge support inequality)

Every such component satisfies

\[
                         |X_D|+|A_D|\ge7.               \tag{4.1}
\]

Moreover, if equality holds then

\[
                         \Omega_D=X_D\mathbin{\dot\cup}A_D
                                                                  \tag{4.2}
\]

is the literal neighbourhood of `D` and is an actual seven-separation
boundary with nonempty opposite shore.  In particular, a component with
at most three attachments to `T` has boundary support at least four.

#### Proof

Distinct components of `A-T` are anticomplete, and there is no `A-R`
edge.  Hence

\[
                         N_G(D)=X_D\mathbin{\dot\cup}A_D.
\]

This set separates nonempty `D` from nonempty `R`.  Seven-connectivity
gives (4.1).  Under equality it has order seven and is literally the whole
neighbourhood of `D`, proving (4.2) and the final assertion.  \(\square\)

## 5. Consequence for the active proof

The connector programme no longer has to handle a cutvertex hub at `z`,
a direct-only wrong-duty portal, or an arbitrary minimal core: all six
non-`u` labels have portals in the one connected graph `A-z`, and the
core is the rooted-leaf path/`Y` in Corollary 3.2.

The remaining theorem is genuinely a `T`-bridge allocation theorem.  It
must either allocate selected bridges to two adjacent connected carriers
whose literal lists colour `F`, or use a component satisfying (4.2) to
transport an attained state to the new boundary (or return one of the
allowed terminal/handoff outcomes).  Lemma 4.1 alone supplies no equality
state on `Omega_D`, so it is not a state-carrying descent.
