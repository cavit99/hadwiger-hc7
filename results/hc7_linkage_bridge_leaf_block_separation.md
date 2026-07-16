# Leaf blocks of components outside a fixed linkage

**Status:** written proof; separately internally audited GREEN in the
adjacent audit. This note records a
uniform consequence of seven-connectivity.  It applies to any fixed system
of six disjoint paths; it does not use the special endpoint adjacencies of
the canonical `3+1` configuration.

## 1. Setup

Let `G` be a seven-connected graph, let

\[
                 \Sigma=P_0\cup\cdots\cup P_5
\]

be the union of six pairwise vertex-disjoint paths, and let `C` be a
component of $G-V(\Sigma)$.  In the intended application the twelve ends of
the paths are distinct.  We make this an explicit standing hypothesis:
all twelve path ends are pairwise distinct.

Suppose that the block--cutvertex tree of `C` has more than one block.  A
**leaf-block interior** is the set

\[
                         L=V(B)-\{c\},                 \tag{1.1}
\]

where `B` is a leaf block and `c` is the unique cutvertex of `C` contained
in `B`.  Blocks of order two are allowed.  Thus `L` is nonempty and
connected.

Write

\[
             N_\Sigma(L)=N_G(L)\cap V(\Sigma).          \tag{1.2}
\]

## 2. The leaf-block separation lemma

### Lemma 2.1

Every leaf-block interior satisfies

\[
                         |N_\Sigma(L)|\ge 6.             \tag{2.1}
\]

If equality holds, then

\[
                         X=\{c\}\cup N_\Sigma(L)        \tag{2.2}
\]

is the boundary of an actual order-seven separation.  Its first open shore
is `L`, and the closed opposite shore contains all six original paths
`P_0,...,P_5` with their labels and vertex sets unchanged.

#### Proof

The standard block--cutvertex-tree description gives

\[
                         N_C(L)\subseteq\{c\}.           \tag{2.3}
\]

Indeed, an edge from a vertex of `L` to a vertex of `C-V(B)` would belong
to a block other than `B` incident with a second cutvertex of `B`, contrary
to `B` being a leaf block.  Since `C` is a component of
$G-V(\Sigma)$, (2.3) implies

\[
                         N_G(L)\subseteq
                         \{c\}\cup N_\Sigma(L).          \tag{2.4}
\]

The set `L` is nonempty.  If $|N_\Sigma(L)|\le5$, then the set on the
right of (2.4) has order at most six.  At most five of the twelve distinct
path ends lie in that set, so its deletion leaves both `L` and a path end
outside `L`; these lie in different components by (2.4).  This contradicts
seven-connectivity.  Hence

\[
                         |N_\Sigma(L)|\ge6,
\]

which proves (2.1).

Now assume equality in (2.1).  Every neighbour of `L` belongs to the
seven-vertex set `X` in (2.2).  Consequently

\[
        (\,G[L\cup X],\;G[V(G)-L],)                    \tag{2.5}
\]

is a separation (with any missing edges inside either closed side restored
in the usual subgraph notation), and its intersection is exactly `X`.
The first open shore is the nonempty set `L`.  The second open shore is
also nonempty: `X` contains at most six vertices of $\Sigma$, whereas the
six paths have twelve distinct ends.  At least six of those ends therefore
lie in `V(G)-(L\cup X)`.  Finally, `L` is disjoint from $\Sigma$, so every
path `P_i` is wholly contained in the closed second side `G[V(G)-L]`.
No path is contracted, rerouted, relabelled, or split between the two
closed sides.  Thus (2.5) is the claimed actual order-seven separation and
preserves the named linkage.  \(\square\)

### Corollary 2.2 (the one-block case)

If `C` has no cutvertex, then

\[
                         |N_\Sigma(C)|\ge7.              \tag{2.6}
\]

If equality holds, $N_\Sigma(C)$ is the boundary of an actual order-seven
separation whose closed opposite shore contains all six named paths.

#### Proof

Here $N_G(C)=N_\Sigma(C)$ because `C` is a component of
$G-V(\Sigma)$.  The same vertex-cut argument gives (2.6), and equality gives
the separation

\[
       (\,G[C\cup N_\Sigma(C)],\;G[V(G)-C],).
\]

Its opposite open shore is nonempty because seven boundary vertices cannot
contain the twelve distinct path ends.  \(\square\)

## 3. Exact scope

The lower bound is six rather than seven for a leaf-block interior because
its unique block cutvertex can be the seventh neighbour.  When the number
of skeleton neighbours is greater than six, connectivity alone supplies no
bounded separation.  Closing that branch requires the labelled endpoint
and attachment-order information of the canonical six-linkage.
