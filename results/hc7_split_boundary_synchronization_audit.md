# Independent audit: split-boundary colour synchronization

**Verdict:** **GREEN** at the exact source revision recorded below, conditional
only on the separately audited bounded-interface reduction invoked in Section
3.  The Property-B theorem itself is elementary and unconditional under its
stated hypotheses.  The corollary closes the split-boundary branch of that
reduction; it does not prove `HC_7`.

## Exact revision audited

```text
f4d556d4bdb01f65cc98fbb3503dba03a8959fcfac023f4177e46649a066f233  audited theorem content before status-only promotion
```

Promotion changed only the status line.  The promoted source hash is

```text
3e3030d6e206fd81b3a79256be2d94cb4a4aac5ad5985fb95008488d9412edf8  results/hc7_split_boundary_synchronization.md
```

Any mathematical change to the source invalidates this audit until the hash
and the arguments below are checked again.

## Statement checked

For a nonempty graph `H` and a positive integer `r`, let
`P_r(H)` be the partitions of `V(H)` into at most `r` nonempty independent
blocks.  For every nonempty independent set `I`, let `C_I` be the set of such
partitions having `I` as an exact block.  Under

```text
chi(H) <= r-2,
```

the source proves that the cylinder hypergraph with vertex set `P_r(H)` and
hyperedges `C_I` has Property B if and only if `H` is nonsplit.  For a
nonsplit graph, parity of the number of blocks supplies the two-colouring.

Applied to the two six-colour extension languages on a bounded `HC_7`
interface, this implies that a split boundary has a common equality
partition and hence the two shore colourings glue.

Both claims are correct.

## 1. Definitions and preliminary edge cases

The chromatic slack implies `r>=3`, since `H` has at least one vertex and
therefore `chi(H)>=1`.  In particular, `P_r(H)` is nonempty.  Every cylinder
used in the theorem is also nonempty: colouring `H-I` with at most `chi(H)`
colours and adjoining `I` as one block uses at most `r-1` blocks.

The stated version of Property B is equivalent to the usual one.  A
two-colouring gives two disjoint colour classes, each meeting every
hyperedge.  Conversely, if two disjoint sets each meet every hyperedge, give
them opposite colours and colour all remaining vertices arbitrarily; the two
already present witnesses keep every hyperedge bichromatic.

The degenerate graph shapes cause no exception:

- If `H` is edgeless and nonempty, it is split (take the clique part empty or
  a singleton), and the cylinder for `I=V(H)` contains only the one-block
  partition.
- If `H` is complete, including `K_1`, choose a split decomposition with an
  independent part consisting of one vertex.  The corresponding cylinder
  contains only the all-singleton partition.  This also covers the case in
  which the complement has no edges.
- Empty clique or independent parts in a split decomposition are harmless.
  The source explicitly makes the independent part nonempty before using its
  cylinder.

Thus the hypotheses and definitions cover all small and extreme cases.

## 2. Split graphs have no Property B

Fix a split partition

```text
V(H) = K dotunion J,
```

with `K` a clique and `J` a nonempty independent set.  If the initially
chosen `J` is empty, then `H` is complete, and moving one vertex from `K` to
`J` preserves both requirements.

In any partition belonging to `C_J`, the block containing `J` is exactly
`J`.  No two vertices of `K` can share a block because `K` is a clique, and
none may be inserted into the exact block `J`.  Hence

```text
{J} union {{x}: x in K}
```

is the unique member of `C_J`.  This partition lies in `P_r(H)` because

```text
|K| <= omega(H) <= chi(H) <= r-2,
```

so it has `|K|+1<=r-1` blocks.  A singleton hyperedge cannot contain both
colours.  The forward obstruction is therefore valid, including when `K` is
empty or `H` is complete.

## 3. Nonsplit graphs have the parity Property-B colouring

Fix any nonempty independent set `I` and put `F=H-I`.  If `F` were a clique,
then `V(H)=V(F) dotunion I` would itself be a split decomposition.  Since `H`
is nonsplit, `F` is not a clique.  In particular, `F` is nonempty and has at
least two vertices.

Let `q=chi(F)` and take an optimal partition of `F` into `q` nonempty
independent blocks.  A noncomplete graph satisfies `q<|V(F)|`; hence at least
one of those blocks has at least two vertices.  Dividing that block into two
nonempty subsets preserves independence and gives a partition of `F` into
`q+1` blocks.

After adjoining `I` as its own exact block, the two resulting members of
`C_I` have `q+1` and `q+2` blocks.  Both are allowed because

```text
q <= chi(H) <= r-2.
```

Their block counts have opposite parity.  Since `I` was arbitrary, every
cylinder has one vertex of each parity, proving Property B.  No compatibility
between the choices for different `I` is needed because the global colour of
a partition is defined solely by its block-count parity.

As a nonessential sanity check, this construction and the singleton-cylinder
obstruction were exhaustively tested for every graph on one through five
vertices at `r=chi(H)+2`; all 1,099 graphs passed.  The written argument above,
not this finite check, proves the unbounded theorem.

## 4. The bounded-interface corollary

Let `H=G[S]`.  Every equality partition induced on `S` by a proper
six-colouring of either closed shore belongs to `P_6(H)`.  The audited
bounded-interface theorem supplies, for every nonempty independent `I` in
`H`, a member of `E(A,S) cap C_I` and a member of `E(B,S) cap C_I`.

Assume the two extension languages are disjoint.  Colour every member of
`E(A,S)` red and every member of `E(B,S)` blue, then colour the remaining
vertices of `P_6(H)` arbitrarily.  Disjointness makes this assignment
consistent, while the two exact-block witnesses make every cylinder
bichromatic.  It is therefore a Property-B colouring.

The boundary theorem gives `chi(H)<=4=6-2`.  If `H` is split, Theorem 2.1
forbids the Property-B colouring.  Thus the languages intersect.

Finally, a common equality partition really is enough to glue.  Choose one
six-colouring from each shore inducing that partition.  The colours used on
`S` are in bijection block by block; this bijection extends to a permutation
of the full six-colour palette, even if some colours are unused on `S` or are
used only away from `S`.  After permuting one shore colouring, the two
colourings agree vertexwise on `S`.  The closed shores cover `G`, intersect
exactly in `S`, and have no edge between their open sides, so their union is a
proper six-colouring of `G`.  This contradicts the hypothetical
counterexample setup.

## 5. Trust boundary and nonclaims

The audit independently checks the complete Property-B proof and the gluing
deduction.  It relies on the already audited bounded-interface theorem only
for these inputs:

1. `7<=|S|<=9` and `chi(G[S])<=4`;
2. both closed shores are six-colourable; and
3. both shore languages meet every exact-block cylinder.

The parity construction on a nonsplit boundary is correctly presented only
as an abstract sharpness example.  It does not assert that the two parity
languages are realizable as extension languages of actual shores, and it
does not obstruct a host-level synchronization theorem using
contraction-criticality or minor exclusion.

No unresolved mathematical gap was found in the source at the audited hash.
