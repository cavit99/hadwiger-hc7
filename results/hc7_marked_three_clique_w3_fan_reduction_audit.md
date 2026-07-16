# Cold audit of the balanced `|W|=3` fan reduction

**Verdict: GREEN.**  The proved statements in
[`hc7_marked_three_clique_w3_fan_reduction.md`](hc7_marked_three_clique_w3_fan_reduction.md)
are valid under the standing balanced equality cell stated there.  In
particular, the proof establishes the exact row--cell incidence, connected
large cells, the terminalizing three-fan, the literal `K_6`, the conditional
reserved-hub `K_7`, the strict inward gate shift, and the marked-tail
connectivity lemma.  It does **not** establish the open reserved-hub
three-fan lemma or exclude the full `|W|=3` cell.

This audit checks the certificate incidence, the component and fullness
claims, the set-Menger application, every branch-set adjacency, the shifted
cut and rank, and the literal/virtual distinction in the completed tail
torso.

## 1. Standing row and component data

The balanced cell has three disjoint rows `B_i` and three disjoint large
traces `X_j`, all of order three, partitioning the same nine vertices.  The
source separation makes

\[
                         S_i=W\cup B_i
\]

a six-separator separating the nonempty set `P_i=A_i-B_i` from the
nonempty complementary shore.  The marked binary-cut corollary therefore
gives exactly two components of `H-S_i`.  Since `P_i` is a union of such
components, it is one connected component.  Minimum-cut fullness gives
`N_H(P_i)=S_i`.  The source separations and disjointness of the auxiliary
rows give pairwise disjoint, pairwise anticomplete packets `P_i`.

These deductions use only the certificate axioms through Niu's claims
3.2.4--3.2.18 and the independently proved binary-cut corollary.

## 2. Exact incidence and connected cells

For `r=|B_i cap X_j|>=2`, the set

\[
 T=W\cup(B_i\mathbin\triangle X_j)
\]

has order `9-2r<=5`.  The proposed separated set

\[
 (B_i\cap X_j)\cup P_i\cup(Y_j-X_j)
\]

has no neighbour outside itself and `T`:

* `P_i` can leave only through `W union B_i`;
* `Y_j-X_j` can leave `Y_j` only through `W`; and
* an edge from `B_i cap X_j` to another cell survives in the auxiliary
  graph, so its other endpoint remains in `A_i`, hence in
  `(B_i-X_j) union P_i`.

The separated set is nonempty.  At most one of the six vertices in the
other two rows lies in `X_j-B_i`, so a vertex also survives on the other
side.  Thus `T` would be a genuine separator of order at most five.  This
proves `|B_i cap X_j|<=1`; the two order counts then force equality in all
nine positions.

If `H[Y_j]` were disconnected, splitting `Y_j` into its graph components
preserves the Mader boundary, terminal, and good-path conditions.  The
new floor contribution is at most

\[
 \sum_C\left\lfloor |X_j\cap C|/2\right\rfloor
 \le \left\lfloor3/2\right\rfloor=1.
\]

An `X_j`-empty component would have all its neighbours in the three-set
`W`, contrary to six-connectivity.  The refinement therefore increases
the number of nonempty cells without changing the maximal `W`, contrary
to secondary maximality.  Lemma 2.1 is GREEN.

## 3. Terminalizing fan

The graph `J=H-W` is three-connected.  For
`I=Q_h cap B_h`, deletion of `I` leaves a
`(3-|I|)`-connected graph.  The set form of Menger therefore gives the
required `3-|I|` disjoint paths between `Q_h-I` and `B_h-I`; the members
of `I` supply the remaining trivial paths.  Shortening at the first
`B_h` vertex keeps every nontrivial interior in the component `P_h` of
`J-B_h`.

Minimizing total length and shortening from the last extra `Q_h` vertex
shows that each path contains exactly its own `Q_h` start.  The three paths
therefore use exactly three of the four clique vertices, and the unused
one lies in `Q_h cap P_h`.  No path or endpoint collision is hidden in
this argument.

The enlarged column bags `E_j=H[Y_j union V(R_j)]` are connected and
disjoint: their only large-cell endpoint is `x_{hj}`, while every
nontrivial path interior lies in `P_h`, which is disjoint from all three
large cells.  Their distinct `Q_h` roots make the three bags pairwise
adjacent.  Lemma 3.1 is GREEN.

## 4. Literal clique models

For Theorem 3.2 the six bags are

\[
 P_a\cup\{z_a\},\quad P_b\cup\{z_b\},\quad\{z_h\},
 \quad E_1,E_2,E_3.
\]

They are disjoint and connected.  The first three are pairwise adjacent
by packet fullness at `W`; the `E_j` are pairwise adjacent through their
distinct `Q_h` roots; and `E_j` contacts the first two packet bags through
`x_{aj}` and `x_{bj}` and contacts `z_h` through its clique root.  These
are all fifteen pairs, so the model is a literal `K_6`.

For Theorem 4.1, the component `C_h` containing the unused clique root
is disjoint from the fan portions of all `E_j`.  Its unused root is
adjacent to the three used clique roots and to `z_h`.  Hypothesis (4.2)
supplies its remaining two contacts.  Adding it to the six bags therefore
accounts for all twenty-one pairs of a literal `K_7` model.  When three
members of `Q_h` lie in `B_h`, all fan paths are trivial, so `C_h=P_h`
and fullness supplies (4.2).  The decoder and Corollary 4.2 are GREEN.

## 5. Gate shift and strict rank

Let `B_i={b,c,d}`, with `b notin Q_i`, and
`K=Q_i cap P_i`.  The live inequality `|Q_i cap B_i|<=2` gives `|K|>=2`.
If the two-fan from `b` to distinct members of `K` fails in
`J-{c,d}`, the fan form of Menger supplies a vertex `p` separating `b`
from `K-{p}`.  A `b`--`k` path through the connected packet exists for
every `k in K`; choosing `k ne p` forces `p in P_i`.

In `J-{c,d,p}`, the clique `K-{p}` lies in one component.  That component
cannot use the remaining gate `b`, and `P_i` can otherwise leave only
through `B_i`; it is consequently contained in `P_i-p`.  Thus

\[
 W\cup\{c,d,p\}
\]

is a literal six-separator, the new clique-side component is strictly
smaller than `P_i`, and the rank `|V(P_i)|` decreases.  The whole `K_4`
remains in the new closed shore because `b` was chosen outside `Q_i` and
`K-{p}` is connected.  Minimum-cut fullness applies to the new component.
Lemma 5.1 and its stated handoff boundary are GREEN.

## 6. Literal tail and virtual torso

If `D` is a component of `P-p` missing a marked contact, then

\[
 B\cup\{p\}\cup N_W(D)
\]

is a separator of order at most six.  Order at most five contradicts
six-connectivity; order six omits a mark and contradicts the marked-cut
law.  Hence every component sees all three marks.  Similarly, a component
of `P-{p,q}` with at most one marked contact produces the separator

\[
 B\cup\{p,q\}\cup N_W(D)
\]

of order at most six, giving the same contradiction.  (Here `p,q` are
distinct.)

These two assertions prove that the literal graph `H[P union W]` remains
connected after deletion of one vertex.  After completing `W` to a
triangle, the same assertions show connectivity after deletion of any
two vertices.  Thus the literal tail is two-connected and the completed
torso is three-connected.

The three edges completing `W` are virtual.  The note explicitly records
this and does not use the completed torso in any proved clique-model
decoder.  No virtual adjacency is lifted as a host edge.  Lemma 6.1 is
GREEN.

## 7. Trust boundary

The only unresolved implication is simultaneous reservation of the two
outside marked contacts in one three-fan, or a valid smaller-state/model
handoff replacing it.  This audit does not promote that open assertion,
exclude the balanced `|W|=3` cell, or prove the marked three-clique or
global support-six theorem.
