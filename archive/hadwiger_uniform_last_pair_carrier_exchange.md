# Uniform last-pair carriers, clique packets, and the exact relative obstruction

## 1. Equality-layer setting

Let `G` be a `k`-contraction-critical graph in the strong minor-minimal
sense, let `S` be a minimum cut, and suppose

\[
 |S|=2m,\qquad G-S=D_1\dot\cup\cdots\dot\cup D_m .
\tag{1.1}
\]

Every `D_i` is connected and full to `S`.  By the uniform cut
inequality, `chi(G[S])=m`.  Fix an optimal equality partition

\[
 \Pi=A_1\mid\cdots\mid A_m,
 \qquad A_i=\{x_i,y_i\}.
\tag{1.2}
\]

For a shore `D` put

\[
 P_z(D)=N_D(z)\qquad(z\in S).
\tag{1.3}
\]

An `A_i`-carrier in `D` is a nonempty connected set meeting both
`P_{x_i}(D)` and `P_{y_i}(D)`.  A `q`-packet for distinct pair indices
`i_1,...,i_q` is a family of disjoint, pairwise adjacent carriers
`U_1,...,U_q`, where `U_h` is an `A_{i_h}`-carrier.

The purpose of keeping carriers inside the open shore is that both
boundary vertices remain available separately.  This is the reserve
which the quotient-state argument does not see.

## 2. State rejection forces a clean Kempe carrier

### Lemma 2.1 (last-pair Kempe carrier)

Let `H=G[S union D]` be a closed side.  Suppose `Pi` does not extend to
a `(k-1)`-colouring of `H`, but the one-split state `Pi^j` does.  In
every `(k-1)`-colouring of `H` with trace `Pi^j`, the two boundary
vertices `x_j,y_j` lie in one bichromatic Kempe component.  This
component meets `S` exactly in `A_j`.  Consequently it contains an
`x_j-y_j` path with all internal vertices in `D`, and those internal
vertices form an `A_j`-carrier in `D`.  Moreover, if `K` is the whole
bichromatic component, then

\[
             \chi\bigl(H[N_H(K)]\bigr)\le k-3.               \tag{2.1}
\]

#### Proof

Let `alpha,beta` be the respective colours of `x_j,y_j`.  Exactness of
the trace says that these colours occur nowhere else on `S`.  If the
vertices lay in different components of the graph induced by colours
`alpha,beta`, interchange the two colours on the component containing
`x_j`.  The colouring remains proper, no other boundary colour class
changes, and now `x_j,y_j` have one colour.  This is an extension of
`Pi`, a contradiction.

Thus they lie in one bichromatic component `K`.  Since neither colour
occurs on `S-A_j`, `K cap S=A_j`.  A path in `K` between its two
boundary vertices consequently has all its internal vertices in `D`.
The pair is independent, so the internal set is nonempty; it is
connected and meets both portal sets.

Finally, no vertex outside `K` which is adjacent to `K` can have colour
`alpha` or `beta`; such a vertex would lie in the same bichromatic
component.  The given colouring therefore restricts to a proper
colouring of `H[N_H(K)]` with the other at most `k-3` colours, proving
(2.1).  QED.

In the equality layer, Theorem 1.1 of
`hadwiger_uniform_equality_state_barrier.md` says that a side rejecting
`Pi` accepts every `Pi^j`.  Hence Lemma 2.1 supplies a colour-certified
carrier for **every** pair, although the carriers initially arise in
different colourings and are not automatically simultaneous.

Thus state rejection supplies more than an unlabelled path: it supplies
a connected carrier region with a boundary whose palette is smaller by
two.  Its order need not be small, so this is a colour-separator rather
than an ordinary low-order separator.

### Lemma 2.2 (double-rainbow contraction interface)

Let `B` be any connected vertex set of a strongly
`k`-contraction-critical graph `G`, with `|B|>=2`, such that `G[B]` is
bipartite with parts `L,R`.  Contract `B` to a vertex `b`, and let `d`
be any `(k-1)`-colouring of `G/B`.  If `gamma=d(b)`, then, for every
other colour `delta`,

\[
 \begin{split}
 N_G(L)-B&\text{ contains a vertex of colour }\delta,\\
 N_G(R)-B&\text{ contains a vertex of colour }\delta.
 \end{split}                                                   \tag{2.2}
\]

Here colours on vertices outside `B` are those inherited from `d`.

#### Proof

Every outside neighbour of `B` is adjacent to the contracted vertex
`b`, so no such vertex has colour `gamma`.  If colour `delta` were
absent from `N_G(R)-B`, expand the contraction by colouring `L` with
`gamma` and `R` with `delta`.  This is proper on `G[B]`; colour `gamma`
is absent from every outside neighbour of `B`, and colour `delta` is
absent from every outside neighbour of `R`.  It is therefore a proper
`(k-1)`-colouring of `G`, a contradiction.  Hence `delta` occurs next
to `R`.  Interchanging `L,R` proves that it also occurs next to `L`.
QED.

Applied to the Kempe component in Lemma 2.1 (or just to one of its
`x_j-y_j` paths), Lemma 2.2 gives a double-rainbow interface on the two
sides of the last-pair carrier.  This is operation-level information:
it is not determined by the equality-state extension family.  In
particular each bipartition side has at least `k-2` distinct outside
neighbours, although these contacts can still be distributed among
different full shores and boundary lobes.

## 3. The full-shore packet lift

### Theorem 3.1 (uniform clique-packet lift)

Suppose one shore, say `D_1`, contains a `q`-packet, where
`1<=q<=m`.  Then

\[
                         K_{m+q-1}\preccurlyeq G.
\tag{3.1}
\]

#### Proof

Relabel so that the packet carriers `U_1,...,U_q` correspond to
`A_1,...,A_q`.  Use the main bags

\[
                         U_i\cup\{x_i\}\quad(1\le i\le q).
\tag{3.2}
\]

They are connected, disjoint and pairwise adjacent.  From the other
`m-1` shores choose `m-q` of them, say `E_{q+1},...,E_m`, and use

\[
                         E_h\cup A_h\quad(q<h\le m)
\tag{3.3}
\]

as the remaining `m-q` main bags.  These are connected.  Fullness makes
every two bags in (3.2)--(3.3) adjacent: a shore in (3.3) sees every
boundary vertex, while two bags of (3.2) are adjacent through their
packet carriers.

Exactly `q-1` opposite shores remain unused.  Match them to
`y_1,...,y_{q-1}` and form the extra bags

\[
                         R_i\cup\{y_i\}\quad(1\le i<q).
\tag{3.4}
\]

They are connected.  Two such bags are adjacent because either full
shore sees the other bag's boundary vertex.  Each sees every bag in
(3.2)--(3.3), again by fullness.  For its paired main bag there is also
the carrier edge from `U_i` to `y_i`.  All displayed bags are disjoint:
every open shore is used once and every boundary vertex is used once.
There are

\[
                 q+(m-q)+(q-1)=m+q-1
\]

of them, proving (3.1).  QED.

### Corollary 3.2 (the forbidden packet size)

If `G` is `K_k`-minor-free and

\[
                    q_*:=k-m+1\le m,
\tag{3.5}
\]

then no shore contains a `q_*`-packet.  Numerically, `k=7,m=4` would
forbid a four-packet and `k=7,m=5` would forbid a three-packet.  The
new high-component theorem in
`hadwiger_hc7_minimum_eight_cut_four_shores.md` independently excludes
both equality-cut rows in an actual hypothetical `HC_7` counterexample;
these numbers are therefore illustrations of the lift, not surviving
`HC_7` cases.

The statement is useful exactly in the range `k<=2m-1`.  When
`k>2m-1`, even a packet for all `m` pairs yields only `K_{2m-1}`; a
different rooted core is then genuinely necessary.

## 4. Exact extension or relative component defect

The next lemma records all the geometry lost when one says merely that
the next carrier does not exist.

### Lemma 4.1 (packet extension or component-defect certificate)

Let `U_1,...,U_r` be an `r`-packet in a connected shore `D`, and let
`A=\{x,y\}` be another boundary pair.  Put

\[
                         W=U_1\cup\cdots\cup U_r.
\tag{4.1}
\]

Exactly one of the following holds.

1. The packet extends: there is an `A`-carrier `U` disjoint from and
   adjacent to every `U_h`.
2. Every component `C` of `D-W` has at least one of the following
   defects:
   \[
   C\cap P_x(D)=\varnothing,\quad
   C\cap P_y(D)=\varnothing,\quad
   E(C,U_h)=\varnothing\text{ for some }h\in[r].
   \tag{4.2}
   \]

The second outcome is an exact relative separator: the carrier skeleton
`W` distributes the two last-pair portal classes and the `r` adjacency
classes among mutually disconnected lobes, with no lobe carrying all
`r+2` requirements.

#### Proof

If a component `C` of `D-W` has none of the defects in (4.2), choose in
`C` one vertex from each of `P_x(D),P_y(D)` and one endpoint in `C` of
an edge to each `U_h`.  A minimal connected subgraph of `C` containing
the selected vertices is an `A`-carrier and is adjacent to every
`U_h`; it extends the packet.

Conversely, a connected carrier disjoint from `W` lies in one component
`C` of `D-W`.  If it is adjacent to every `U_h`, that component has
none of the displayed defects.  The alternatives are therefore exact
and exclusive.  QED.

For `r=1`, shrink `U_1` inclusion-minimally.  It is a path between the
two portal classes of its pair.  Lemma 4.1 then has the familiar
crossed-frame form: either there are two disjoint adjacent pair carriers,
or this carrier path captures one portal class of the other pair,
separates its two residual portal classes into different components, or
the relevant lobe has no attachment back to the carrier.  The last
possibility disappears for every component of `D-U_1` only when that
component actually has a neighbour in `U_1`; it must not be silently
discarded.

### Theorem 4.2 (iterated carrier-web obstruction)

Assume `G` is `K_k`-minor-free, (3.5) holds, and a closed side rejects
`Pi`.  Start with any ordered list of distinct pair indices.  Lemma 2.1
supplies the first carrier.  Repeatedly apply Lemma 4.1.  Before a
`q_*`-packet is formed, the process must stop at some `r<q_*`, and its
carrier skeleton certifies (4.2) for the next pair.

#### Proof

The only alternative to stopping is a `q_*`-packet.  Theorem 3.1 would
then give a `K_{m+q_*-1}=K_k` minor.  QED.

This is a genuine geometric consequence of clique-minor exclusion.  It
does not assert that the relative skeleton is a global cut: paths may
run through the other full shores, exactly as in the relative
Hall--Menger warning.  The next uniform step must combine several such
ordered skeleton certificates, forced by the one-split colourings, and
either exchange their lobes or turn one into a smaller full adhesion.

### Corollary 4.3 (uniform dense-component band)

Let `G` be a least counterexample to `HC_t`, `t>=7`, at an equality cut
`|S|=2m`.  The high-component theorem gives `m<=t-4`.  If also

\[
                         2m\ge t+1,                            \tag{4.3}
\]

then `q_*=t-m+1<=m`, and every side rejecting `Pi` has the following
uniform structure: for every ordering of `q_*` distinct pair blocks,
an iterated carrier construction stops at a labelled component-defect
certificate (4.2) after fewer than `q_*` carriers; its first carrier can
be chosen bichromatic and has the double-rainbow interface of Lemma 2.2.

Thus the entire parameter band

\[
              \left\lceil\frac{t+1}{2}\right\rceil
              \le m\le t-4                                  \tag{4.4}
\]

is reduced to one label-preserving carrier-web exchange theorem.  For
`m<(t+1)/2`, even a packet containing all `m` pair blocks is too small
for Theorem 3.1 to reach `K_t`; that lower-component range needs an
additional rooted core and is not claimed here.

## 5. Sharpness and falsified strengthenings

Three tempting upgrades are not justified.

1. **A carrier is not automatically a packet.**  A single shore may
   route each pair separately while every carrier for one pair separates
   the portal classes of another.  This is precisely the two-path/web
   obstruction, not an ordinary one-pair Menger failure.
2. **The skeleton need not be small.**  Inclusion-minimal carriers are
   paths, but their lengths are unbounded.  Lemma 4.1 controls labelled
   component incidence, not the order of a global vertex cut.
3. **Minimum-cut fullness does not remove captures.**  Take boundary
   `K_{2,...,2}` and `m` singleton open shores, every one adjacent to all
   `2m` boundary vertices.  The glued graph is `2m`-connected and the
   boundary is a minimum cut, yet a singleton carrier captures every
   portal class and cannot split into a two-packet.  This example is not
   claimed to be `K_k`-minor-free or contraction-critical; it proves that
   connectivity and fullness alone cannot replace the `K_k`-exclusion
   step in Theorem 4.2.

Thus the sound endpoint is the packet-or-labelled-relative-separator
theorem above.  Promoting (4.2) to a smaller full separator requires
additional information about how the lobes meet `S` and about the
proper-minor colouring transitions.  Those hypotheses cannot be omitted
or treated as routine.
