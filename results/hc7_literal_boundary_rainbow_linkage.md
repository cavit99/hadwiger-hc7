# Rainbow first-hit linkages to a partitioned minimum boundary

**Status:** written proof; separate internal audit GREEN in
[`hc7_literal_boundary_rainbow_linkage_audit.md`](hc7_literal_boundary_rainbow_linkage_audit.md).
This parameter-uniform theorem is
the literal-boundary specialization of the labelled first-hit Rado
reduction.  It shows that the unused-label exposure obstruction disappears
when the terminal labels partition an actual minimum-size vertex set.  It
does not apply when a label is an unbounded branch set, and it does not prove
`HC_7`.

## Theorem 1 (partitioned-boundary linkage)

Let `G` be a `k`-connected graph, let `S` be a set of exactly `k` vertices,
and let

\[
                         S=S_1\mathbin{\dot\cup}\cdots
                           \mathbin{\dot\cup}S_m               \tag{1.1}
\]

be a partition into nonempty sets.  If
`P subseteq V(G)-S` and `|P|>=m`, then there are pairwise vertex-disjoint
paths `Q_1,...,Q_m` such that, for each `i`,

1. one end of `Q_i` is a distinct vertex of `P`;
2. the other end belongs to `S_i`; and
3. this terminal end is the only vertex of `S` on `Q_i`.

Thus the paths make pairwise distinct literal first hits in all prescribed
parts of the boundary.

### Proof

Apply the Rado--gammoid first-hit theorem with terminal classes
`S_1,...,S_m`.  Suppose that the desired paths do not exist.  Then some
nonempty `I subseteq [m]` has clean-linkage rank less than `|I|`, and the
directed terminal-avoiding network has a Menger set `Z` with

\[
                              |Z|\le |I|-1.                     \tag{1.2}
\]

Map `Z` back to the corresponding literal vertices of `G`.  Since
`|P|>=m>=|I|>|Z|`, at least one source vertex survives.  Let `C` be its
component in the nonterminal graph after the nonterminal members of `Z`
are deleted.  The host-neighbourhood calculation in the Rado reduction
gives

\[
 N_G(C)\subseteq \overline Z\ \cup\
                  \bigl(N_G(C)\cap(S-S_I)\bigr),
 \qquad S_I=\bigcup_{i\in I}S_i.                       \tag{1.3}
\]

Some vertex of `S_I` lies outside `C` and outside the right-hand side, so
that right-hand side is a genuine separator.  Its order is at most

\[
 \begin{aligned}
 |Z|+|S-S_I|
   &\le (|I|-1)+k-|S_I|\\
   &\le (|I|-1)+k-|I|=k-1,                            \tag{1.4}
 \end{aligned}
\]

where the second inequality uses the nonemptiness and disjointness of the
parts `S_i`.  This contradicts `k`-connectivity.  Hence the clean labelled
linkage exists. \(\square\)

## Corollary 2 (the exact-seven consequence)

In a seven-connected graph, let an actual seven-vertex boundary be
partitioned into at most five nonempty prescribed classes.  Any five
distinct source vertices outside the boundary can be linked disjointly to
distinct literal first hits in all five classes (discard unused sources if
there are fewer classes).

Consequently, a rank defect in the current `HC_7` first-hit programme
cannot persist when its five labels have already been represented by
disjoint nonempty subsets of the literal seven-boundary.  The remaining
obstruction is specifically the conversion of five *branch-set* labels to
such bounded literal terminal classes.

## Trust boundary

The theorem requires distinct unit-capacity source vertices.  It does not
permit several paths to share a connected source kernel before leaving
through distinct ports unless those ports are first supplied as the set
`P`.

Most importantly, the count in (1.4) uses `|S|=k`.  It is false with five
unbounded terminal branch sets in place of the parts of `S`: unused labels
may expose arbitrarily many literal vertices.  The audited first-hit
host-lift barrier realizes exactly that failure at connectivity seven.

## Dependency

- [Rado--gammoid first-hit reduction](hc7_labelled_first_hit_rado_reduction.md).
