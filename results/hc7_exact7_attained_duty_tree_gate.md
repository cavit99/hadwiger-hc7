# Attained-duty packet split or a literal Helly gate

**Status:** proved and independently audited.  This is a uniform
state-specific exchange in the exact-seven `(1,2)` cell.  It eliminates
every attained state whose duty hulls separate inside either full packet.
It does not prove that the two residual gate vertices form a global apex
pair.

## 1. Exact state and duty

Let

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad |S|=7,
 \qquad (\nu_L,\nu_R)=(1,2),
\]

be an actual separation in a seven-connected, strongly
seven-contraction-critical, `K_7`-minor-free graph.  Let
`H=G[S]`, and let `P_1,P_2` be disjoint connected `S`-full packets in
the rich shore `R`.

Suppose a legal proper-minor operation in the thin shore returns an exact
proper equality partition `Pi` of `S`.  Choose a maximum clique `C` among
the literal singleton blocks of `Pi` and suppose

\[
                 d_H(\Pi)=|\Pi|-|C|=3.
\]

Write `B_1,B_2,B_3` for the three blocks not represented by the retained
singletons in `C`.  For each `i`, define the attained duty

\[
 D_i=D_{\Pi,C}(B_i)
    :=B_i\cup\{c\in C:N_H(c)\cap B_i=\varnothing\}.       \tag{1.1}
\]

Thus a connected rich-shore carrier `X` funds `B_i` whenever it contacts
every literal vertex of `D_i`: the contacts at `B_i` make `X union B_i`
connected, and the remaining contacts make its representative adjacent to
every retained singleton in `C`.

This is exactly the state-specific specialization of the audited labelled
carrier-reflection lemma in
`hc7_exact7_rich_cutpacket_exchange.md`.

## 2. Portal trees and duty hulls

Let `P` be either full packet.  For every `i` and every `s in D_i`, choose
a literal, **duty-specific** portal witness

\[
                         p_i(s)\in V(P)\cap N_G(s),
\]

allowing witnesses for a shared boundary label in two different duties to
be equal or different.  This duty-specific freedom is essential: a common
choice `p(s)` could manufacture a false collision when the packet has two
distinct portals to the same retained singleton.  Choose a tree
`T subseteq P` containing all selected witnesses.  For each `i`, let

\[
                  K_i=T[\{p_i(s):s\in D_i\}]           \tag{2.1}
\]

denote the unique inclusion-minimal subtree of `T` containing those
witnesses.  Call `K_i` the selected **duty hull** of `B_i` in `T`.
It is nonempty because `B_i subseteq D_i` and `B_i` is nonempty.

## 3. Split-or-gate theorem

### Theorem 3.1 (attained-duty tree split or literal gate)

For the attained state `Pi` and either selected full-packet tree `T`, one
of the following holds.

1. The state `Pi` reflects across the rich shore, and hence `G` is
   six-colourable.
2. There is a literal vertex

   \[
                            g\in K_1\cap K_2\cap K_3.   \tag{3.1}
   \]

In particular, if any two duty hulls are vertex-disjoint, outcome 1 holds.

#### Proof

Suppose `K_i` and `K_j` are disjoint, and let `k` be the remaining index.
The unique `K_i-K_j` path in `T` has one end `u in K_i` and the other
`v in K_j`.  Choose any edge `xy` of this path, oriented with `x` toward
`K_i` and `y` toward `K_j`.  Let

\[
 X=K_i\cup uTx,
 \qquad
 Y=K_j\cup yTv.                                      \tag{3.2}
\]

The sets `X,Y` are nonempty, connected, vertex-disjoint, and adjacent by
the literal edge `xy`.  Every selected witness for `D_i` lies in `X`, and
every selected witness for `D_j` lies in `Y`; hence `X` contacts all of
`D_i` and `Y` contacts all of `D_j`.

Use the other full packet `Q` to fund `B_k`.  Contract

\[
          X\cup B_i,\qquad Y\cup B_j,\qquad Q\cup B_k. \tag{3.3}
\]

The first two sets are adjacent through `xy`.  The full packet `Q` is
adjacent to both through the nonempty literal blocks `B_i,B_j` and funds
all of `D_k`.  Definition (1.1) makes the first two representatives
adjacent to every retained singleton in `C`; fullness does the same for the
third.  Thus the three representatives together with `C` form a clique
indexed exactly by the blocks of `Pi`.

The contraction is proper.  A six-colouring of that minor expands on the
untouched thin closed shore to the exact state `Pi`, aligns with the
colouring which originally returned `Pi`, and glues across `S`.  This is
outcome 1.

Consequently, if outcome 1 does not hold, the three subtrees
`K_1,K_2,K_3` meet pairwise.  Subtrees of a tree have the Helly property.
For completeness, choose

\[
 x\in K_1\cap K_2,
 \quad y\in K_1\cap K_3,
 \quad z\in K_2\cap K_3.
\]

The median of `x,y,z` in `T` lies on `xTy`, `xTz`, and `yTz`.
Connectedness puts those three paths respectively in `K_1,K_2,K_3`, so
the median belongs to all three hulls.  It is the literal gate `g` in
(3.1).  \(\square\)

### Corollary 3.2 (two literal packet gates)

Apply Theorem 3.1 first to a selected portal tree in `P_1`, using `P_2`
as the completing full packet, and then symmetrically.  Either `Pi`
reflects, or there are distinct literal vertices

\[
                         g_1\in P_1,
                         \qquad g_2\in P_2,           \tag{3.4}
\]

such that every selected duty hull in the corresponding packet tree
contains its gate.

The vertices are distinct because the packets are disjoint.  The witness
systems may be chosen independently in the two packets.

## 4. Exact scope and surviving web target

The gate conclusion is stronger than a contact count and weaker than a
two-apex theorem.  A duty hull may contain its gate as a leaf, and a bridge
outside the selected tree may bypass the gate.  Therefore (3.4) alone does
not imply that `{g_1,g_2}` is a separator, that deleting it makes the rich
shore planar, or that `G-{g_1,g_2}` is `K_5`-minor-free.

The unqualified assertion that every bridge bypassing a gate separates two
duty hulls is false.  The audited certificate in
`../barriers/hc7_exact7_gate_bypass_falsifier.md` has six private portals in
the cyclic order `A B D A B D`: every packet tree has a bypassed Helly gate,
but every pair of duty-correct carriers intersects.

Thus the next valid target is a **label-compatible bypass-or-web theorem**.
A compatible bridge must reroute two attained-duty hulls to become disjoint,
giving Theorem 3.1(1).  Failure must retain the alternating block-terminal
web as a literal adhesion certificate, and the second full packet plus
minor-critical state transitions must then yield a common exact state, a
literal `K_7`, or the fixed-pair `K_5`-minor-free endgame.  That web-to-global
conclusion is not proved here.
