# Exact type-2 degree-nine shores: cutvertices close, split sides expose capacity

## 1. Boundary and exact-shore state

Let

\[
 E(A)=\{01,02,12,25,45,37,68\}                   \tag{1.1}
\]

on the boundary \(N=\{0,1,\ldots,8\}\), and put

\[
 M_1=\{0,1\},\qquad M_2=\{0,2\},\qquad
 M_3=\{1,2\},qquad F_i=N-M_i.                    \tag{1.2}
\]

Additional boundary edges only help all minor certificates below.  A shore
is in the **exact state** when its boundary neighborhood is exactly \(F_i\),
not merely when \(M_i\) was obtained by artificially deleting extra
contacts.

## 2. Certified four-piece packing

### Lemma 2.1 (two six-contact pieces close the state)

Fix \(i\in\{1,2,3\}\).  Let \(D_1,D_2,C_j,C_k\) be four pairwise disjoint
connected pieces outside \(N\), where \(\{i,j,k\}=\{1,2,3\}\).  Suppose

\[
 N_N(C_j)\supseteq F_j,\qquad N_N(C_k)\supseteq F_k,          \tag{2.1}
\]

and

\[
 N_N(D_1),N_N(D_2)\subseteq F_i,qquad
 |N_N(D_1)|,|N_N(D_2)|\ge6,qquad
 N_N(D_1)\cup N_N(D_2)=F_i.                                \tag{2.2}
\]

Edges between the four pieces may be present or absent.  Then the graph
contains an \(N\)-meeting \(K_6\)-model.

#### Certified proof

Every row in (2.2) is either \(F_i\) or \(F_i-\{d\}\).  Up to interchanging
\(D_1,D_2\), the row states are

\[
 (F_i,F_i),\quad (F_i,F_i-d),\quad
 (F_i-d,F_i-e)\quad(d\ne e).                    \tag{2.3}
\]

For each fixed \(i\), this gives

\[
                         1+7+\binom72=29          \tag{2.4}
\]

states, and 87 states over the three possible split shores.

`degree9_type2_cutvertex_certificate.txt` supplies six explicit bags for
every state.  In every certificate the first four bags consist of one of
the four pieces together with a boundary root; the last two are boundary
singletons.  The independent verifier
`degree9_type2_cutvertex_verify.py` reconstructs (1.1)--(1.2), checks that
the 87 keys are exactly the states in (2.3), and checks bag disjointness,
boundary meeting, connectedness, and all fifteen pairwise bag adjacencies.
It reports

```text
verified 87 exact-miss lobe states and sharp width-four residue
```

The verifier uses only Python integer sets and bitmasks; it has no SAT/SMT
or discovery-program dependency.  The formal trust boundary is the Python
interpreter, the 87 certificate tuples, and the short verifier. \(\square\)

## 3. Cutvertex closure

### Theorem 3.1 (an exact type-2 shore has no cutvertex)

Let \(G\) be seven-connected, let \(v\) have boundary \(N\), suppose
\(G[N]\) contains the edges (1.1), and let \(C_1,C_2,C_3\) be the three
components of \(G-N[v]\).  If

\[
                         N_N(C_h)=F_h\quad(h=1,2,3),           \tag{3.1}
\]

then a cutvertex in any \(G[C_i]\) forces a \(K_7\)-minor.

#### Proof

Let \(q\) be a cutvertex of \(C_i\).  For every component \(L\) of
\(C_i-q\),

\[
                         N_G(L)\subseteq N_N(L)\cup\{q\}.     \tag{3.2}
\]

Indeed, distinct exterior components are anticomplete and distinct
components of \(C_i-q\) have no edge.  Since another lobe and \(v\) lie
beyond the set in (3.2), seven-connectivity gives

\[
                         |N_N(L)|\ge6.                        \tag{3.3}
\]

By the exact-state assumption, \(N_N(L)\subseteq F_i\), so each lobe row
is full or misses one label of \(F_i\).

Choose two lobes whose rows have different missing labels, if possible.
Their rows then cover \(F_i\).  If one lobe is full, choose it and any
other lobe.  The only remaining case is that every lobe misses the same
label \(d\).  Because \(C_i\) itself contacts \(d\), the cutvertex \(q\)
contacts \(d\).  Absorb \(q\) into one chosen lobe.  The enlarged piece is
connected and full to \(F_i\), while a second lobe still has at least six
contacts.  Thus in every case two disjoint connected pieces satisfy (2.2).

Apply Lemma 2.1 to these two pieces and the other two exterior components.
It gives an \(N\)-meeting \(K_6\)-model in \(G-v\); \(\{v\}\) is the
seventh branch set. \(\square\)

The exact-state qualifier is essential to this proof.  If contacts to an
artificially declared missed vertex are restored, (3.3) does not imply six
contacts **inside** \(F_i\).  Such extra-contact states require a larger
certificate rather than being silently covered by this theorem.

## 4. Multiplicity forces the split-side residue

In the exact state, minimum degree forces many repeated portals.  The
triangle vertices satisfy

\[
 |N_{C_3}(0)|\ge4,qquad |N_{C_2}(1)|\ge4,qquad
 |N_{C_1}(2)|\ge3.                                  \tag{4.1}
\]

Every vertex in \(\{3,4,6,7,8\}\) has one boundary neighbor, and vertex
\(5\) has two.  Counting its neighbors across the three shores shows that
each of the six vertices \(3,\ldots,8\) is repeated in at least one shore.
Assign each to one such shore.  Some shore repeats at least two of them,
in addition to its unique triangle root.

Apply the double-root split-or-cutvertex theorem from
`hadwiger_root_multiplicity_split.md` inside that shore, taking its allowed
seven-set \(F_i\) as boundary.  The cutvertex outcome is impossible by
Theorem 3.1.  Hence the only exact-state residue is a connected adjacent
partition

\[
                         C_i=P\mathbin{\dot\cup}Q             \tag{4.2}
\]

whose two contact rows cover \(F_i\) and share two prescribed repeated
labels.

If both rows have order at least six, Lemma 2.1 again gives \(K_7\).
Therefore every surviving split has

\[
                 \min\{|N_N(P)|,|N_N(Q)|\}\le5.              \tag{4.3}
\]

## 5. Exact remaining capacity-state lemma

For a side \(P\) of (4.2), put

\[
                         I_P=N_Q(P).                           \tag{5.1}
\]

The set \(N_N(P)\cup I_P\) separates \(P\) from the other exterior
components.  Seven-connectivity gives the capacity inequality

\[
                         |N_N(P)|+|I_P|\ge7.                  \tag{5.2}
\]

Consequently, a residual row of order at most five has at least two
distinct interface vertices on the opposite side.  The next required
statement is precisely:

> **Type-2 interface-capacity exchange.**  In the exact state
> (1.1)--(1.2), let (4.2) be a connected adjacent double-root split.  If
> one contact row has order at most five, then its two-or-more opposite-side
> interface vertices either permit a further label-preserving peel that
> raises both row orders to six, lie behind a separation of order at most
> six, or give an exact seven-adhesion \(X\) for which the two proper-side
> six-colorings can be chosen so that their restrictions to \(X\) agree
> after one permutation of the palette.

The small-separator outcome contradicts seven-connectivity; the peel outcome
is closed by Lemma 2.1; and the stated exact-seven outcome is color-gluable
by its definition.
This is a local two-shore capacity-state lemma, not a new static boundary
enumeration.  The exact-seven clause is necessary because equality in
(5.2) is compatible with seven-connectivity and cannot simply be called a
contradiction.

The threshold six is sharp for the current contact data.  For example, for
the split shore \(F_1=\{2,3,4,5,6,7,8\}\), the adjacent rows

\[
 \{2,3,4,5,6\},qquad \{2,3,6,7,8\}                 \tag{5.3}
\]

cover \(F_1\), share three labels, and each have order five, yet the
resulting four-piece quotient has a width-four tree decomposition and no
\(K_6\)-minor.  The verifier checks this second decomposition explicitly:
its nine bags all have order at most five and satisfy edge coverage and the
running-intersection property.  Thus “two shared roots and row order five”
cannot replace the interface-capacity exchange.

## 6. Capacity upgrades to a label-preserving linkage

The numerical inequality (5.2) can be strengthened without any finite
enumeration.

### Lemma 6.1 (interface-capacity linkage)

Let \(G\) be \(k\)-connected, let \(S\) be a vertex set, and let \(C\)
be a component of \(G-S\) with exact boundary neighbourhood
\(F=N_S(C)\), where \(|F|=k\).  Suppose

\[
 C=P\mathbin{\dot\cup}Q,
\]

where \(P,Q\) are nonempty connected sets.  Put

\[
 R=N_S(P),\qquad D=F-R,qquad I=N_Q(P).
\]

Then the graph \(G[Q\cup D]\) contains \(|D|\) pairwise
vertex-disjoint paths from \(D\) to \(I\).  Consequently every vertex
of \(D\) is the initial vertex of one path, the terminal vertices in
\(I\) are distinct, and all internal vertices lie in \(Q\).

#### Proof

Assume that such a linkage does not exist.  By the endpoint-allowed
set form of Menger's theorem there is
a set

\[
 Z\subseteq Q\cup D,\qquad |Z|<|D|,
\]

such that \(G[Q\cup D]-Z\) has no path from \(D-Z\) to \(I-Z\).
We claim that \(R\cup Z\) separates \(G\).

After deleting \(R\cup Z\), take the union \(A\) of \(P\) with all components
of \(G[Q\cup D]-Z\) that meet \(I-Z\).  (If \(I\subseteq Z\), just
take \(P\).)  No edge of \(G-(R\cup Z)\) leaves \(A\).  Indeed, every edge from \(P\)
to \(S\) ends in \(R\), and every edge from \(P\) to \(Q\) ends in
\(I\).  A vertex of \(Q\) has no neighbour outside \(C\cup F\), since
\(C\) is a component of \(G-S\) with exact neighbourhood \(F\).
An edge from the selected \(Q\)-components to \(D-Z\) would give a
forbidden \(I-Z\)--\(D-Z\) path.

The selected side is nonempty because it contains \(P\).  The other
side is also nonempty: \(|Z|<|D|\) leaves a vertex of \(D-Z\).  Finally,

\[
 |R\cup Z|\le |R|+|Z|<|R|+|D|=|F|=k,
\]

contradicting \(k\)-connectivity.  Hence the linkage exists.  Since it
has \(|D|\) disjoint paths and the start set itself has order \(|D|\),
the stated endpoint properties follow. \(\square\)

### Corollary 6.2 (exact type-2 residue)

For a residual split (4.2), if \(|N_N(P)|=r\le5\), then there are
\(7-r\) vertex-disjoint paths in \(G[Q\cup(F_i-N_N(P))]\), one from
each missing boundary label to a distinct vertex of \(N_Q(P)\), with
all internal vertices in \(Q\).  In particular,
the sharp row-five residue carries two disjoint, label-preserving
cross-interface paths.  Any completion theorem may therefore assume
this linkage; mere interface cardinality is no longer the exact gap.
