# Exact two-carrier clique-OCT obstruction and gate reassignment

## Status

**Status:** proved and independently audited.

This note isolates the exact obstruction left by two labelled connected
carriers.  It also records the precise effect of moving one literal carrier
piece.  Relative to the stated uniform carrier-list theorem, the formulation
below drops spanning of the carrier shore.  That nonspanning contraction
mechanism is not new: it already appears, and is explicitly audited, in the
two-block splice inside `hc7_exact7_thin_shore_exchange`.  The present note
packages that mechanism with the exact two-list parity and reassignment
criterion.

## 1. Geometric setup

Let `G` be strongly seven-contraction-critical:

\[
 \chi(G)=7,
 \qquad\text{and every proper minor of }G\text{ is six-colourable}.
\]

Let

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R
\]

where `S` is nonempty, `L,R` are nonempty, and there are no `LR` edges.
Assume that `R` contains two vertex-disjoint connected `S`-full packets
`P_1,P_2`.

Suppose `C_1,C_2` are vertex-disjoint nonempty connected subgraphs of
`G[L]`, and that there is a literal edge between `C_1` and `C_2`.  They are
not required to cover `L`.  Put `H=G[S]` and define the nonempty lists

\[
 \Lambda(s)=\{i\in\{1,2\}:N_L(s)\cap C_i\ne\varnothing\}.
 \tag{1.1}
\]

Nonemptiness of every list is an explicit hypothesis.

## 2. Nonspanning two-carrier synchronization

### Theorem 2.1

If `H` has a proper `Lambda`-list-colouring, then `G` is six-colourable.

### Proof

Let `phi:S->{1,2}` be proper with `phi(s) in Lambda(s)`, and put

\[
 I_i=\phi^{-1}(i).
\]

On the carrier shore, contract each

\[
 A_i=C_i\cup I_i.
\]

The two sets are disjoint and connected.  At least one `I_i` is nonempty,
so at least one `A_i` has at least two vertices; hence this is a proper
minor.  The two contracted images are adjacent because `C_1` and `C_2`
are adjacent.  A six-colouring of the minor, restricted to `R` and
expanded over `S`, properly colours `G[R union S]` and induces exactly the
nonempty blocks among `I_1,I_2` on the literal boundary.  Vertices of
`L-(C_1 union C_2)` are simply discarded when the colouring is restricted;
this is why spanning is unnecessary.

On the packet shore, assign distinct packets to the nonempty `I_i` and
contract `P_i union I_i`.  These are disjoint connected nontrivial sets.
Their images are adjacent whenever both blocks are nonempty, because every
packet is `S`-full.  A six-colouring of this proper minor, restricted to
`L` and expanded over `S`, induces the same exact boundary partition.
No contraction is made for an empty block, and its unused packet is left
intact.

The block colours on the two closed shores are pairwise distinct.  A
permutation of the six-colour palette aligns the colours of corresponding
blocks, after which the two colourings glue because there are no `LR`
edges.  This gives a six-colouring of `G`.  `square`

### Remark 2.2 (one used carrier)

If one `I_i` is empty, the exact boundary state has one block and uses only
one opposite packet.  The proof remains valid.  If `H` has an edge, every
proper two-colouring uses both indices, so both blocks are automatically
nonempty.

## 3. Exact two-list obstruction

For `s in S`, call `s` **forced** when `Lambda(s)` is a singleton and
**flexible** when `Lambda(s)={1,2}`.

### Theorem 3.1 (parity form)

The instance `(H,Lambda)` is list-colourable if and only if:

1. `H` is bipartite; and
2. in every connected component of `H`, all forced vertices impose the
   same bipartition orientation.

Equivalently, list-colourability fails exactly when either:

* `H` contains an odd cycle; or
* some forced vertices `x,y` in one component have incompatible parity:
  they have the same singleton list and odd `H`-distance, or they have
  different singleton lists and even `H`-distance.

### Proof

If `H` is not bipartite, no proper colouring with the two values `1,2`
exists.  Assume it is bipartite.  In each component `K`, choose a function

\[
 p_K:V(K)\longrightarrow\{0,1\}
\]

whose values are the two bipartition classes.  The only two proper
two-colourings of a nontrivial connected component, and also the two
possible colours of an isolated vertex, are

\[
 \phi_\epsilon(s)=1+(p_K(s)\mathbin{\mathsf{xor}}\epsilon),
 \qquad \epsilon\in\{0,1\}.
 \tag{3.1}
\]

A flexible vertex permits both orientations.  A forced vertex with
`Lambda(s)={c_s}` permits exactly

\[
 \epsilon=p_K(s)\mathbin{\mathsf{xor}}(c_s-1).
 \tag{3.2}
\]

Thus the component is list-colourable exactly when all its forced vertices
that exist prescribe one common value of `epsilon`.  Distinct components
may choose their orientations independently.

For forced `x,y` in one component, their prescriptions agree exactly when

\[
 p_K(x)\mathbin{\mathsf{xor}}p_K(y)
   =(c_x-1)\mathbin{\mathsf{xor}}(c_y-1).
\]

The left side is the parity of every `x-y` path.  This gives the displayed
same-list/odd-distance and different-list/even-distance obstructions.
`square`

### Corollary 3.2

In the geometric setup of Section 1, a hypothetical counterexample can
retain the two carriers only if `H` has an odd cycle or the lists contain
one of the forced-parity conflicts in Theorem 3.1.

This is an exact alternative, not merely a sufficient test.

## 4. One literal piece reassignment

Let `Z` be a nonempty vertex set contained in `C_1`, and define

\[
 C'_1=C_1-Z,
 \qquad C'_2=C_2\cup Z.
 \tag{4.1}
\]

Call (4.1) a **legal reassignment** when `C'_1,C'_2` are nonempty,
vertex-disjoint, connected, and adjacent.  Define the new lists from
literal contacts:

\[
 \Lambda'(s)=\{i:N_L(s)\cap C'_i\ne\varnothing\}.
 \tag{4.2}
\]

They are automatically nonempty if the old lists were nonempty: a vertex
not adjacent to `Z` keeps its old contacts, while a vertex adjacent to `Z`
contacts `C'_2`.

For every `s in S`, the exact update is

\[
\begin{aligned}
 1\in\Lambda'(s)&\iff N_L(s)\cap(C_1-Z)\ne\varnothing,\\
 2\in\Lambda'(s)&\iff
       N_L(s)\cap C_2\ne\varnothing\text{ or }N_L(s)\cap Z\ne\varnothing.
\end{aligned}
\tag{4.3}
\]

In particular, only vertices in `N_S(Z)` can change lists.

### Theorem 4.1 (exact repair criterion)

Let

\[
 A=\{s\in S:\Lambda(s)\ne\Lambda'(s)\}.
\]

A legal reassignment makes the carrier state glue if and only if `H` is
bipartite and, for every component `K` of `H`, there is an orientation
`epsilon_K in {0,1}` such that

\[
\begin{cases}
1+(p_K(s)\mathbin{\mathsf{xor}}\epsilon_K)\in\Lambda(s),
    &s\in V(K)-A,\\
1+(p_K(s)\mathbin{\mathsf{xor}}\epsilon_K)\in\Lambda'(s),
    &s\in V(K)\cap A.
\end{cases}
\tag{4.4}
\]

Equivalently, in every component all unchanged forced vertices must demand
one common orientation, and every changed vertex must permit that
orientation under its new list.  If two opposite forced orientations
remain outside `A`, the reassignment cannot repair the state.  An odd cycle
can never be repaired by a carrier reassignment because `H` itself is
unchanged.

### Proof

Formula (4.4) is Theorem 3.1 applied to the recomputed lists `Lambda'`, with
the unchanged lists written separately.  When it holds, Theorem 2.1 gives
the six-colouring.  When it fails, no proper `Lambda'`-list-colouring exists,
so the two-carrier synchronization mechanism cannot glue.  `square`

### Corollary 4.2 (one changed boundary vertex)

Suppose `A={x}`.  The reassignment repairs a previously uncolourable
bipartite instance exactly when:

1. every component not containing `x` was already consistent;
2. all forced vertices of the component of `x`, other than `x`, demand one
   common orientation `epsilon`; and
3. `Lambda'(x)` permits the colour
   `1+(p(x) xor epsilon)`.

Thus a one-vertex change can repair a parity conflict only when `x` is the
sole remaining representative of one of the two conflicting orientation
demands.

## 5. Palette-to-labelled-carrier audit

There is **no palette-to-labelled-carrier gap** in Theorem 2.1.  The values
`1,2` are labels of the literal carriers, not names of colours in a
pre-existing six-colouring.  Contracting `C_i union I_i` manufactures the
carrier-side equality blocks, and the opposite full packets manufacture
the same labelled blocks.  Only afterwards is an arbitrary permutation of
the six-colour palette used to align them.

There is, however, a sharp geometric gap in any argument that operates only
on the abstract lists.  A proposed gate move is valid only after checking
that it is realized by actual vertex sets satisfying all of the following:

* the two new carriers are disjoint, nonempty, and connected;
* a literal edge remains between them;
* the lists are recomputed by literal contacts as in (4.2), rather than
  changed by an abstract palette switch.

If connectedness or adjacency fails, the carrier contractions need not be
connected or differently coloured.  If an asserted list change has no
literal carrier move behind it, its indices have no labelled geometric
meaning.  The parity criterion alone does not supply such a move.

## 6. Consequence for the active gate programme

The two-carrier branch has a complete finite state description:

* an odd cycle is an immutable obstruction for every two-carrier
  reassignment;
* on a bipartite boundary, the entire obstruction is one bit of orientation
  per connected component;
* a moved gate or lobe repairs the state exactly when its affected boundary
  set meets every conflicting orientation and the literal contact update
  leaves one common orientation.

What remains geometric is not two-list colouring.  It is proving that an
available gate/lobe can be legally reassigned with the required affected
set while preserving the two labelled carriers.

## 7. Exact clique-OCT extension

Retain the separation, packets, and literal carriers from Section 1.  Let
`U subseteq S` induce a clique, assume `|U|<=4`, and put

\[
                         F=H-U.
\]

Assume `F` is nonempty.  Define the carrier lists only on `F`:

\[
 \Lambda(s)=\{i\in\{1,2\}:N_L(s)\cap C_i\ne\varnothing\},
 \qquad s\in V(F),                                    \tag{7.1}
\]

and assume every list is nonempty.  Let `phi` be a proper
`Lambda`-list-colouring of `F`, with blocks

\[
                         I_i=\phi^{-1}(i).
\]

For a nonempty block `I_i`, define its exact retained-clique duty by

\[
 D_U(I_i)=I_i\cup
   \{u\in U:N_H(u)\cap I_i=\varnothing\}.              \tag{7.2}
\]

Because the list condition already gives `I_i subseteq N_S(C_i)`, the
condition

\[
                         D_U(I_i)\subseteq N_S(C_i)     \tag{7.3}
\]

says precisely this: whenever the assigned block itself supplies no edge
to a retained singleton `u`, the literal carrier `C_i` supplies that edge.
Equivalently,

\[
 N_G(u)\cap(C_i\cup I_i)\ne\varnothing
 \quad\text{for every }u\in U                         \tag{7.4}
\]

and every nonempty `I_i`.  No duty is imposed on an unused carrier whose
block is empty.

### Theorem 7.1 (two carriers fund an exact clique-OCT state)

If (7.3) holds for every nonempty block, then `G` is six-colourable.

### Proof

For every nonempty `I_i`, contract

\[
                         A_i=C_i\cup I_i
\]

on the carrier shore.  These sets are disjoint, connected, and nontrivial.
If both occur, their images are adjacent through the literal `C_1C_2`
edge.  By (7.4), every image is adjacent to every retained vertex of `U`,
and `U` is a clique.  Thus the contracted images together with the literal
vertices of `U` form a clique of order at most

\[
                         2+|U|\le6.
\]

This is a proper minor.  A six-colouring restricted to `R union S` and
expanded over the `I_i` therefore induces the exact boundary partition

\[
       \{I_i:I_i\ne\varnothing\}
         \cup\{\{u\}:u\in U\}.                         \tag{7.5}
\]

On the packet shore, assign distinct full packets to the nonempty `I_i`
and contract `P_i union I_i`.  Packet fullness makes the resulting images
pairwise adjacent and adjacent to every literal vertex of `U`; the vertices
of `U` are pairwise adjacent in `H`.  Hence a six-colouring of this proper
minor, restricted to `L union S` and expanded over the blocks, induces the
same exact partition (7.5).

The at most six block colours can be aligned by a permutation of the full
six-colour palette.  The two closed-shore colourings then glue over `S`.
`square`

### Exactness of the duty condition

For the displayed carrier contraction, (7.4) is exactly the condition that
the image of `C_i union I_i` be adjacent to the retained literal `u`.
If `I_i` already contains a neighbour of `u`, no carrier-to-`u` contact is
needed.  If it does not, such a contact is required to force the two exact
boundary blocks to receive different colours.  This is the attained duty

\[
 I_i\cup\{u\in U:N_H(u)\cap I_i=\varnothing\},
\]

not an unconditional defect bound on the carrier.

The theorem does not claim that (7.3) is necessary for every conceivable
proper-minor construction of the same state.  It is necessary and
sufficient for the named representative-to-singleton adjacency in this
literal two-carrier contraction.

## 8. Automatic duty in the connected-rich width-two frontier

The width-two frontier has exactly the following two forms relevant here.

### Proposition 8.1

In each form below, every proper colouring of `F=H-U` from the literal
carrier lists automatically satisfies the retained-clique duty (7.3) for
both nonempty colour classes.

1. `H` is connected and bipartite, and `U` is empty.
2. `H=K_{1,3} dotcup K_3`, and `U={u}` consists of any one triangle
   vertex.

### Proof

In the first form there is no retained vertex, so the extra duty is
vacuous.

For the second form, name the other two triangle vertices `x,y`.  Then

\[
                         F=K_{1,3}\mathbin{\dot\cup}xy.
\]

Every proper two-colouring of `F` assigns different colours to `x` and
`y`.  Hence each of its two colour classes contains one of `x,y`, and both
are neighbours of `u` in `H`.  Therefore

\[
                         N_H(u)\cap I_i\ne\varnothing
\]

for `i=1,2`, regardless of the independent orientations chosen on the claw
and on the edge.  Formula (7.2) adds no retained vertex to either duty, so
the original list contacts `I_i subseteq N_S(C_i)` already imply (7.3).
`square`

### Corollary 8.2 (frontier gluing criterion)

In either frontier form, an exact clique-OCT state obtained by assigning
each vertex of `F` to one of these two literal carriers is available exactly
when `F` has a proper colouring from the literal carrier lists.  Whenever
it is available, the two opposite full packets reflect it and `G` is
six-colourable.

The equivalence is deliberately confined to this named state mechanism.
It does not say that failure of the list instance excludes every other
proper-minor state or every other route to a six-colouring.

## 9. Exact frontier parity after a legal gate reassignment

Perform a legal reassignment `Z:C_1 -> C_2` as in Section 4, but define the
old and new lists only on `F=H-U`.  Put

\[
 A_F=\{s\in V(F):\Lambda(s)\ne\Lambda'(s)\}.
\]

The literal update remains

\[
\begin{aligned}
 1\in\Lambda'(s)&\iff N_L(s)\cap(C_1-Z)\ne\varnothing,\\
 2\in\Lambda'(s)&\iff
 N_L(s)\cap C_2\ne\varnothing\text{ or }N_L(s)\cap Z\ne\varnothing,
\end{aligned}                                          \tag{9.1}
\]

and `A_F subseteq N_S(Z) cap V(F)`.  Contacts from the moved piece to `U`
may also change, but Proposition 8.1 makes them irrelevant to the retained
duty in these two frontier forms.

Choose a bipartition indicator

\[
 p_K:V(K)\longrightarrow\{0,1\}
\]

for every connected component `K` of `F`.  A post-move singleton list
`Lambda'(s)={c_s}` demands the orientation

\[
                         \epsilon_s=p_K(s)\mathbin{\mathsf{xor}}(c_s-1).
\tag{9.2}
\]

### Theorem 9.1 (exact reassignment obstruction in the frontier)

After the legal reassignment, the clique-OCT state fails to glue by the
two-carrier mechanism if and only if some component of `F` contains two
post-move forced vertices demanding different values in (9.2).

Equivalently, some forced pair in one component has the same singleton list
at odd `F`-distance, or different singleton lists at even `F`-distance.

Relative to the affected set `A_F`, the move repairs a previously failed
state if and only if, in every component `K`, there is an orientation
`epsilon_K` such that

\[
\begin{cases}
1+(p_K(s)\mathbin{\mathsf{xor}}\epsilon_K)\in\Lambda(s),
   &s\in V(K)-A_F,\\
1+(p_K(s)\mathbin{\mathsf{xor}}\epsilon_K)\in\Lambda'(s),
   &s\in V(K)\cap A_F.
\end{cases}                                             \tag{9.3}
\]

Thus, in every formerly inconsistent component, all old forced vertices
left outside `A_F` must demand one common orientation.  If two opposite
forced demands remain outside `A_F`, no legal contact update supported on
`Z` can repair the state.

### Proof

Both frontier graphs `F` are bipartite.  Proposition 8.1 shows that every
proper two-colouring automatically discharges all retained duties, before
and after the carrier move.  Corollary 8.2 therefore reduces gluing exactly
to list-colourability of `(F,Lambda')`.  The componentwise orientation
calculation in Theorem 3.1 gives (9.2), the forced-pair obstruction, and the
mixed old/new criterion (9.3).  `square`

### Concrete specializations

* In the connected bipartite form, `F=H` has one component, so the entire
  obstruction is one inconsistent orientation bit.
* In the `K_{1,3} dotcup K_3` form, `F` has the claw component and the edge
  `xy` as two independently orientable components.  On the edge component,
  failure occurs exactly when both endpoints are forced to the same carrier.

The remaining difficulty is therefore literal gate geometry: producing a
legal reassignment whose affected set hits the conflicting parity demands.
The retained clique creates no additional obstruction in the audited
width-two frontier.
