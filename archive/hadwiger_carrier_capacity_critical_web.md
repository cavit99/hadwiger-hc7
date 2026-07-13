# Carrier two-packets and the critical-web exchange gap

## 1. The label-free two-packet

Let \(D\) be connected and let

\[
 P_1,P_2,Q_1,Q_2\subseteq V(D)
\]

be nonempty portal sets. A **two-packet** is a pair of vertex-disjoint
paths

\[
                 P_1\longrightarrow P_2,\qquad
                 Q_1\longrightarrow Q_2.           \tag{1.1}
\]

A path may have order one when its two portal sets meet. Equivalently,
a two-packet is a pair of disjoint connected sets, the first meeting
\(P_1,P_2\) and the second meeting \(Q_1,Q_2\).

This is exactly the protected carrier split in
hadwiger_locked_carrier_dependency_spine.md after the already repaired
residue is contracted: one path is the detachable arm and the other is
the protected residue-to-helper connector. Thus a failed clean-gate
carrier is a capacity-zero two-packet, not an arbitrary rooted clique
problem.

## 2. The direction of exact state transfer

Let \(G\) be \(r\)-minor-critical and let \(S\) be a separator with two
full connected shores \(C,D\). Suppose \(S\) has an independent-set
partition

\[
 \Pi=P\mathbin{\dot\cup}Q\mathbin{\dot\cup}
     \{\{x\}:x\in R\},\qquad
 P=\{p_1,p_2\},\quad Q=\{q_1,q_2\},                 \tag{2.1}
\]

whose block-adjacency quotient is complete: between every two distinct
blocks there is at least one boundary edge. No vertex-completeness
between blocks is assumed.

For shore \(C\), use the four full portal sets
\[
 N_C(p_1),N_C(p_2),N_C(q_1),N_C(q_2).
\]

### Theorem 2.1 (one-way packet transfer)

If \(C\) has the two-packet (1.1), then the exact state \(\Pi\) extends
to an \(r\)-colouring of \(G[S\cup D]\).

If both shores have the two-packet, then \(G\) is \(r\)-colourable.

#### Proof

Let \(X_P,X_Q\subseteq C\) be the two disjoint connected packet
witnesses. Then

\[
 X_P\cup P,\qquad X_Q\cup Q
\]

are disjoint connected sets. Contract them separately, delete every
unused vertex of \(C\), and retain \(S\cup D\). The two images together
with the singleton vertices of \(R\) form a clique: every pair of
blocks has a surviving boundary edge. Colour this proper minor with
\(r\) colours and expand only the boundary vertices. The clique makes
the resulting state on \(S\) exactly \(\Pi\), proving the first
assertion.

If \(D\) also has the packet, the symmetric construction gives a
colouring of \(S\cup C\) with the same exact state. Align the block
colours and glue. \(\square\)

### Audit warning 2.2

The transfer is from a geometric packet in one shore to a colouring of
the opposite shore. A packet in \(C\) does not by itself colour \(C\).
This direction cannot be reversed silently.

There is one stronger special cell. If every vertex in different
members of \(\{P,Q,R\}\) is adjacent to every other, one linked side
already suffices by Theorem 3.1 of
hadwiger_uniform_contact_twoblock_adhesion.md. Moreover, when
\(|S|=t\), Theorem 2.4 of that note constructs a \(K_t\)-minor from
one full shore without any linkage. Therefore the palette-tight
complete-cross pair-pair cell is already closed and is not the genuine
carrier residual.

## 3. Capacity failure and state criticality live on opposite sides

Let \(\mathcal E_C,\mathcal E_D\) be the exact boundary-state extension
families of the two closed shores. Suppose

\[
                         \Pi\in\mathcal E_C
                         \setminus\mathcal E_D.     \tag{3.1}
\]

### Corollary 3.1 (the accepting shore is packet-deficient)

The shore \(C\) has no two-packet for the two blocks \(P,Q\).

#### Proof

A packet in \(C\) would transfer \(\Pi\) to \(D\) by Theorem 2.1,
contrary to (3.1). \(\square\)

Thus the Two Paths web lies in the shore which already accepts the
state. The minor-critical transition lies on the opposite shore:
for every internal label-preserving operation \(\mu\) in \(D\), there
is a state

\[
 \Sigma_\mu\in
 \mathcal E_C\cap
 \mathcal E_D^\mu\setminus\mathcal E_D.            \tag{3.2}
\]

The states \(\Sigma_\mu\) need not equal \(\Pi\), and their
nonsingleton blocks need not use the same portal pairs. This is the
precise state/capacity alignment gap. Static web geometry on \(C\) and
minor criticality on \(D\) cannot be combined until their boundary
blocks are identified.

The uniform witness in
hadwiger_exact_trace_interface_dichotomy.md makes one part of this
identification canonical. At every Dirac equality cell

\[
 d(v)=t+s,\qquad |I|=s+2,
\]

all interface-edge witnesses may be chosen with the same exact trace
\(I\). The remaining blocks can still vary.

## 4. The state-polarized special case

The cleanest exchange problem occurs when all transitions in (3.2) have
one fixed state \(\Pi\). Give the blocks of \(\Pi\) fixed pairwise
distinct colours from an \(r\)-palette. For \(x\in D\), define

\[
 L(x)=[r]\setminus
 \{\hbox{colours of boundary blocks having a neighbour at }x\}.
\tag{4.1}
\]

### Theorem 4.1 (fixed-list critical kernel)

Assume \(\Pi\notin\mathcal E_D\), but every internal vertex deletion,
edge deletion, and edge contraction in \(D\) admits \(\Pi\). Then \(D\)
is not \(L\)-colourable, every proper internal deletion is
\(L\)-colourable, and an edge contraction \(xy\) is colourable with
the contracted vertex receiving a colour in \(L(x)\cap L(y)\).

Consequently:

1. \(d_D(x)\ge |L(x)|\) for every \(x\in D\);
2. in every \(L\)-colouring of \(D-xy\), the ends \(x,y\) have the same
   colour; and
3. if that common colour is \(\alpha\), every colour of
   \(L(x)-\{\alpha\}\) appears in \(N_D(x)-\{y\}\), and symmetrically
   at \(y\).

#### Proof

An \(L\)-colouring of \(D\) is precisely an extension of the fixed
state \(\Pi\), so none exists. Palette permutations align every
transition colouring with the fixed block colours. Contraction forbids
at the identified vertex every boundary colour forbidden at either end,
giving the intersection list.

Colour \(D-x\). If fewer than \(|L(x)|\) colours occurred on
\(N_D(x)\), a colour of \(L(x)\) would be available at \(x\). This
proves assertion 1. If an \(L\)-colouring of \(D-xy\) gave \(x,y\)
different colours, restoring \(xy\) would colour \(D\), proving
assertion 2. If a colour
\(\gamma\in L(x)-\{\alpha\}\) were absent from
\(N_D(x)-\{y\}\), recolouring \(x\) with \(\gamma\) would make
\(xy\) proper and again colour \(D\). This proves assertion 3.
\(\square\)

### Lemma 4.2 (critical-web boundary charge)

Suppose \(D\) is a simple plane graph whose outer boundary is a cycle
of order \(\ell\). Put

\[
 b(x)=r-|L(x)|,
\]

the number of distinct boundary equality blocks adjacent to \(x\).
Then

\[
 \sum_{x\in D} b(x)\ge
 (r-6)|V(D)|+2\ell+6.                              \tag{4.2}
\]

#### Proof

Euler's inequality gives
\[
 |E(D)|\le3|V(D)|-\ell-3
\]
and hence
\[
 \sum_{x\in D}(6-d_D(x))\ge2\ell+6.                \tag{4.3}
\]
Theorem 4.1 gives \(d_D(x)\ge r-b(x)\), so
\[
 6-d_D(x)\le6-r+b(x).
\]
Sum and combine with (4.3). \(\square\)

For \(r=6\), (4.2) forces at least \(2\ell+6\) units of
boundary-block charge. For large \(t\), the linear term
\((r-6)|V(D)|\) says that a surviving planar web is almost completely
charged by boundary blocks on average. This is the label-free source of
the removable fans, portal intervals, and facial ears seen in the
\(C_6\) and Moser laboratories.

## 5. The minimal general lemma

The carrier and two-shore programmes now meet at the following statement.

> **Capacity--state web exchange lemma.** Let \(G\) be a
> minor-minimal counterexample, let \(S\) be an exact palette-tight
> adhesion with two full shores \(C,D\), and let
> \(\Pi\in\mathcal E_C-\mathcal E_D\). Suppose \(C\) has no geometric
> packet for the nonsingleton blocks of \(\Pi\). For every internal
> operation \(\mu\) in \(D\), take the exact transition state
> \(\Sigma_\mu\) in (3.2). Then either
>
> 1. the family of packet webs in \(C\), indexed by the nonsingleton
>    blocks of the \(\Sigma_\mu\)'s, contains a rooted augmentation of
>    the current clique model; or
> 2. the webs have a common actual adhesion \(X\) on which one
>    \(\Sigma_\mu\) is clique-realized from both sides; or
> 3. one shore has a proper \(S\)-rooted minor with the same extension
>    family.

Outcome 2 colours by portalized exact transfer. Outcome 3 contradicts
rooted state-minimality. Outcome 1 is the desired model augmentation.

This is weaker and more accurate than an unconditional critical-web
reducibility theorem. It explicitly retains the varying transition
states and the direction of geometric transfer. In the trace-stable
equality cell, every \(\Sigma_\mu\) shares the fixed block \(I\), so
only the helper blocks and portal-only decorations vary.

## 6. Adversarial boundary

The following checks delimit the lemma.

1. Static full attachment and web topology are insufficient. The wheel
   shore in hadwiger_reserved_w_majority_counterexample.md satisfies
   the sharp local cut inequalities but has a universal boundary
   extension family. It has no state-critical opposite shore.
2. Even state polarity, local degree inequalities, and every one-step
   transition are insufficient without minor exclusion. The order-five
   web in hadwiger_uniform_contact_twoblock_adhesion.md, Remark 4.9,
   has those properties but contains an explicit \(K_7\)-model.
3. The complete-cross pair-pair cell is not evidence for the lemma: it
   is already closed by a direct one-full-shore clique minor.
4. A tree portal skeleton alone is insufficient. Host edges outside the
   skeleton may be the web bridges carrying the packet, and a tree edge
   is not an ambient separator.
5. Abstract extension families are insufficient by the boundary-state
   realization counterexamples. The common adhesion in outcome 2 must
   consist of actual portal vertices and actual connected
   realizations.

The proved contribution toward the exchange lemma is the uniform
trace--edge alignment: every Dirac equality-cell interface operation
can be audited in one fixed trace, with either the \(t-2\) rainbow roots
or all \(t-2\) edge-critical Kempe detours. What remains is to turn the
first-hit pattern of those detours into outcome 1 or 2 above.
