# Shore-capacity packing at a critical adhesion

## 1. Exact capacity families

Let \(G\) be \(r\)-minor-critical: \(G\) is not \(r\)-colourable and
every proper minor of \(G\) is \(r\)-colourable.  Let \(S\) be a
separator and write

\[
 G-S=D_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}D_m,
 \qquad N(D_i)=S\quad(i\in[m]).                    \tag{1.1}
\]

Fix an optimal colouring of \(J=G[S]\), with equality blocks

\[
 \Pi=\{A_1,\ldots,A_p\},\qquad p=\chi(J).          \tag{1.2}
\]

The colour-class quotient is complete: for distinct \(h,k\), there is
an edge between \(A_h\) and \(A_k\), since otherwise those two classes
could be merged.  Let

\[
 B=\{h\in[p]:|A_h|\ge2\}                           \tag{1.3}
\]

index the non-singleton blocks.

For a shore \(D_i\), define its **capacity family** \(\mathcal R_i\) to
be the collection of sets \(I\subseteq B\) for which there are pairwise
vertex-disjoint connected sets

\[
 X_h\subseteq D_i\qquad(h\in I)                    \tag{1.4}
\]

such that every vertex of \(A_h\) has a neighbour in \(X_h\).
The empty set belongs to every \(\mathcal R_i\), and fullness makes every
singleton \(\{h\}\), \(h\in B\), a member of every
\(\mathcal R_i\).

## 2. The exact packing theorem

### Theorem 2.1 (shore-capacity gluing)

Suppose that for every target index \(i\in[m]\), the set \(B\) has a
partition

\[
 B=I_1^{(i)}\mathbin{\dot\cup}\cdots
     \mathbin{\dot\cup}I_{i-1}^{(i)}
     \mathbin{\dot\cup}I_{i+1}^{(i)}\mathbin{\dot\cup}\cdots
     \mathbin{\dot\cup}I_m^{(i)},                 \tag{2.1}
\]

where \(I_j^{(i)}\in\mathcal R_j\) for every \(j\ne i\).  Then \(G\)
is \(r\)-colourable, a contradiction.

#### Proof

Fix \(i\), and choose the carriers (1.4) for the packets in (2.1).  For
each \(h\in B\), let \(j(h)\ne i\) be the shore to which its packet is
assigned and put

\[
 Q_h=X_h\cup A_h.                                  \tag{2.2}
\]

The sets \(Q_h\), \(h\in B\), are disjoint and connected.  Contract
them, delete all unused vertices of the opposite shores, and retain
\(D_i\) and every singleton boundary block.

The contracted images and the retained singleton boundary vertices form
a \(K_p\).  Indeed, an edge exists between every two distinct colour
blocks of the optimal partition (1.2), and that boundary edge survives
between their two representatives.  Thus every \(r\)-colouring of the
proper minor gives these \(p\) representatives distinct colours.

Expand only the boundary part of (2.2).  The resulting colouring of
\(G[S\cup D_i]\) induces exactly the labelled equality partition
\(\Pi\) on \(S\).  The construction works for every target \(i\).
Permute colour names so that the side colourings agree on all blocks of
\(\Pi\), and glue them.  The components of \(G-S\) are pairwise
anticomplete, so this is an \(r\)-colouring of \(G\), a contradiction.
\(\square\)

### Corollary 2.2 (baseline full-shore pressure)

If \(|B|\le m-1\), then \(G\) is \(r\)-colourable.  Consequently every
surviving optimal boundary colouring has at least \(m\) non-singleton
colour classes.

#### Proof

For a fixed target, assign the at most \(m-1\) indices of \(B\)
injectively to the other shores and use their guaranteed singleton
capacity packets.  Apply Theorem 2.1. \(\square\)

This contains the singleton and clique-residual forms of full-shore
block gluing.  Since \(|S|\ge2|B|+(p-|B|)=p+|B|\), it also recovers the
corresponding boundary-size pressure.

### Corollary 2.3 (one unit above baseline)

Suppose \(|B|=m\).  Call a shore **boosted** if its capacity family
contains some two-element subset of \(B\).  If at least two shores are
boosted, then \(G\) is \(r\)-colourable.

#### Proof

For a target \(D_i\), choose a boosted shore \(D_j\) with \(j\ne i\),
assign its two-block packet to \(D_j\), and assign the remaining
\(m-2\) block indices bijectively to the other \(m-2\) non-target
shores.  Theorem 2.1 applies. \(\square\)

For a three-shore seven-cut, the patterns \((3,2,2)\) and
\((2,2,2,1)\) both have \(|B|=m=3\).  Corollary 2.3 is precisely the
label-free source of the two-block theorem in
`hadwiger_three_shore_block_capacity.md`.

## 3. Hall form and the exact obstruction

For a fixed target \(i\), form the packet-cover problem

\[
 \text{partition }B\text{ into }I_j\in\mathcal R_j
 \quad(j\ne i).                                    \tag{3.1}
\]

Theorem 2.1 says that a critical adhesion must fail (3.1) for at least
one target.  This is the exact finite-boundary obstruction; it is not a
surrogate clique-minor conjecture.

When every capacity family is a uniform family

\[
 \{I\subseteq B:|I|\le c_j\}\subseteq\mathcal R_j,
\]

ordinary capacitated Hall assignment gives a cover for target \(i\)
whenever

\[
 \sum_{j\ne i}c_j\ge |B|.                          \tag{3.2}
\]

For nonuniform families, failure of (3.1) records exactly which block
subsets cannot be linked disjointly inside which shores.  At capacity
two these failures lie in the scope of the Two Paths Theorem; at higher
capacity they are rooted disjoint-Steiner-tree obstructions.  Thus the
uniform model-meeting problem has the following sharpened form:

\[
 \boxed{
 \begin{array}{c}
 \text{enough shore capacity gives a common exact colouring state;}\\
 \text{capacity failure must yield a colour-gluable small adhesion.}
 \end{array}}
\]

The first line is Theorem 2.1.  The missing all-\(t\) theorem is now
precisely the second line: a contact-or-gluable-adhesion theorem for the
rooted capacity families \(\mathcal R_i\).

## 4. Relation to the model-meeting obstruction

A block \(A_h\) is a prescribed set of boundary roots which must be
made connected without consuming another boundary block.  A packet in
\(\mathcal R_i\) is therefore a label-preserving partial branch-set
model.  Unlike an unrooted clique model, it remembers exactly which
boundary equality state the contraction will force on the opposite
side.

This identifies the scalable invariant emerging from the \(C_6\),
Moser, and rooted-\(K_{2,4}\) laboratories:

\[
 \text{portal placement}
 \longrightarrow
 \text{shore capacity family}
 \longrightarrow
 \text{exact state transfer}
 \longrightarrow
 \text{colour gluing}.
\]

Finite boundary casework is needed only to identify the minimal
capacity-deficient packets.  A complete general proof would eliminate
all of them at once by showing that a minimal failed packet cover either
augments through a rooted linkage or exposes a knitted adhesion on which
the same equality blocks can be realized from both sides.
