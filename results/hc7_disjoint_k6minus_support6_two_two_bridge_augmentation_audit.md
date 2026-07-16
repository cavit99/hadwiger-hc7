# Independent audit: bridge augmentation for the minimal `2+2` contact form

**Audited source:**
`results/hc7_disjoint_k6minus_support6_two_two_bridge_augmentation.md`

**Audited SHA-256:**
`3c806883fdf15d0e5be5c5a3e5d74521c1622d84421e0e60b0b299d3f1998b7c`

**Verdict:** **GREEN.**  The four explicit minor-model constructions, the
shortest-path separator argument, the rooted-`K_4` invocation, and both
four-terminal web certificates are correct under the hypotheses stated in
the audited source.  The note also states the remaining six-terminal gap at
the correct strength: it does not promote quotient evidence or virtual web
completion edges to host-graph edges.

This is a separate internal mathematical audit, not external peer review.

After the mathematical audit, the source was moved from `active/` to
`results/` and only its status and adjacent-audit link were updated.  The
hash above binds the audit to that exact promoted revision; the audited
mathematical content is unchanged.

## 1. Canonical hypotheses

The audit used only the edges explicitly stated in (1.1)--(1.2):

- `Q={a_0,a_1,a_2,a_3}` is a clique;
- `xy`, `a_0x`, `a_1x`, `a_2y`, and `a_3y` are edges;
- `B` is complete except possibly for `pq`; and
- the six paths `P_0,...,P_5` are pairwise vertex-disjoint and otherwise
  avoid `A\cup B`.

No unstated edge between `x` or `y` and `Q` is used.

## 2. Theorem 2.1

The four sets in (2.1) really are connected and disjoint after splitting
`P_1` at `uu^+` and `P_j` at `v^-v`.  In particular:

- `S_L` contains the neighbour of `v` on `R`, so the last edge of `R`
  joins `S_L` to `T_R` (also when `R=uv`);
- `S_R` is connected by `b_0q`;
- `T_L` is connected by `s_jy`, which is respectively `a_2y`, `a_3y`,
  or `xy`; and
- `T_L` and `T_R` are adjacent along `v^-v`.

For the seven sets in (2.2), all remaining adjacencies were reconstructed.
The clique at the left supplies every adjacency from `S_L` except the two
split edges just noted.  The graph `B-pq` supplies the adjacencies among
`P_0,P_k,P_l,T_R,S_R`, with the inclusion of both `b_0` and `q` in `S_R`
removing any dependence on `pq`.  Finally the three rows of (2.4) are exact:

| `j` | `T_L`--`P_k` | `T_L`--`P_l` |
|---|---|---|
| 2 | `a_2a_3` | `yx` |
| 3 | `a_3a_2` | `yx` |
| 4 | `ya_2` | `ya_3` |

Thus (2.2) is a valid explicit `K_7`-minor model in all three cases.

## 3. Theorem 3.1

The deleted set `Z` has exactly six vertices.  Seven-connectivity therefore
makes `H=G-Z` connected.  The sets `U` and `T\cup X` are disjoint and
nonempty, and `T\cup X` is connected because all five truncated paths end
at the connected graph `B-b_0`, which is `K_5` with at most the edge `pq`
missing.

A shortest `U`--`(T\cup X)` path in `H` has no internal vertex in either end
set.  Moreover

```text
V(A\cup B) \cup V(P_0\cup...\cup P_5) = Z \cup U \cup T \cup X.
```

Consequently its interior avoids all six displayed paths and all support
vertices.  An end in `T` therefore satisfies Theorem 2.1, while an end in
`X` is precisely one of the two exceptional returns.  The same shortening
argument applied to a hypothetical `U`--`T` path in `H-X` proves that `X`
separates `U` from `T`.

The paragraph after the theorem is correct under the standard convention
that a `U`--`T` separator is disjoint from `U\cup T`.  Stating that
convention explicitly in a future editorial revision would remove a minor
terminological ambiguity; it is not used in any proved conclusion of this
note.

## 4. The `P_1`--`P_5` crossing

For Theorem 4.1, put

```text
C=(P_2-b_1) \cup (Q_5-b_0).
```

It is connected by `a_2y`.  The first five branch sets in (4.2) have all
pairwise adjacencies as follows:

- `P_0Q_1` uses `a_0a_1` (so it does not use the possibly missing `pq`);
- the adjacencies of `C` to `P_0,Q_1,P_3,P_4` use, respectively,
  `a_2a_0,a_2a_1,a_2a_3,yx`; and
- every other pair uses an edge of `B-pq`.

The singleton `b_0` is adjacent to `C` along the final edge of `Q_5`, and
the singleton `b_1` is adjacent to `C` along the final edge of `P_2`.
Both singletons are adjacent to every other branch set through `B-pq`.
Hence (4.2) is a valid `K_7`-minor model.

The opposite orders in Corollary 4.2 make the two concatenated paths
vertex-disjoint: their `P_1` subpaths and their `P_5` subpaths are disjoint,
and the two joining paths are disjoint by hypothesis.  They satisfy exactly
the exclusions required by Theorem 4.1.

For Corollary 4.3, deleting `D_5` leaves all of `P_1` and `P_5` but deletes
the other four displayed paths and every support vertex except
`a_1,b_0,q,y`.  Thus a crossing of the frame `(a_1,b_0,q,y)` is exactly an
`(a_1q,b_0y)` linkage eligible for Theorem 4.1.  In its absence, the Two
Paths Theorem gives a spanning web completion with that frame.  Completion
edges belong to the web completion, not necessarily to `G`, exactly as the
source records.

## 5. The `P_0`--`P_1` crossing

The cycle used in Theorem 4.4 is

```text
a_0 -- a_1 -- P_1 -- b_0 -- p -- reverse(P_0) -- a_0,
```

so its four nominated vertices occur in the cyclic order
`a_0,a_1,b_0,p`.  The paths `Q_0,Q_1` are an
`(a_0b_0,a_1p)` linkage.  This is precisely the hypothesis of
Fabila-Monroy--Wood, Lemma 7: a cycle through `a,b,c,d` in that order plus
an `(ac,bd)` linkage yields a `K_4` minor rooted at the four vertices.
The disjointness assumptions ensure that the four rooted branch sets avoid
`P_2,P_3,P_4,P_5`.

The three additional branch sets in (4.7) are disjoint and connected;
`P_2\cup P_5` is connected by `a_2y`.  They are pairwise adjacent via
`a_2a_3`, `b_1r`, and `b_2r`.  Each of the two branch sets rooted on the
left is adjacent to all three by the edges from `a_0` or `a_1` to
`a_2,a_3,x`; each of the two rooted on the right is adjacent to all three
by the edges from `b_0` or `p` to `b_1,b_2,r`.  Together with the rooted
`K_4`, these are seven pairwise adjacent branch sets.

The order check in Corollary 4.5 is the same disjoint-concatenation check as
in Corollary 4.2.  For Corollary 4.6, deleting `D_0` leaves precisely the
four relevant support vertices and the two named paths from the displayed
skeleton.  A crossing of `(a_0,a_1,b_0,p)` is exactly the linkage in
Theorem 4.4, so its absence gives the stated web completion.

## 6. Six-terminal limitation

The common cyclic order `(a_0,a_1,y,q,b_0,p)` restricts to
`(a_0,a_1,b_0,p)` and, after cyclic reversal, to `(a_1,b_0,q,y)`.  There
are `binom(6,4)=15` crossing types on six cyclically ordered terminals.
Only the two types proved above have a label-faithful host-graph decoder in
this note.

The source correctly declines to infer a host `K_7` minor from the
unpromoted contracted-quotient calculation: an arbitrary linkage can meet
the interiors of `P_0,P_1,P_5`, and an edge inserted in a web completion is
not an edge of the host graph.  Therefore the exact proved residual is two
overlapping four-terminal web certificates, not a six-terminal composition
theorem.

## 7. Scope

This audit verifies the theorem only after the canonical `2+2` form and the
six disjoint paths (1.2) have been obtained.  It does not audit the finite
classification producing that form, prove that the two web certificates
compose, prove the support-six transversal statement, or prove `HC_7`.
