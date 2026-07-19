# Independent internal audit of the degree-eight singleton label obstruction

**Verdict:** **GREEN** for the complete source revision identified below,
under its explicit extremal and boundary-full hypotheses.

This is a separate internal mathematical audit, not external peer review.  It
checks every branch-set replacement, all required adjacencies and
disjointness, preservation of the fixed roots and response data, preservation
of the relaxed first-hit rank, the three-owner classification, and the
`K_5`-minor exclusion on a vertex-deleted boundary.

## Audited revision

The audited source is
[`hc7_order8_singleton_label_obstruction.md`](hc7_order8_singleton_label_obstruction.md)
at SHA-256

```text
2dd29f27ea1dce603e162747e968d33e9c81e5e4d21678ab86cfef9dcafc614a
```

Relative to the proof revision checked line by line, the final source changes
only its opening status paragraph from pending to a link to this completed
audit.  Restoring the pending-status paragraph reproduces SHA-256
`4012f6785e61adea34cf21011b9b74ae80108ca6a4a054d639086557a9f7f7fc`.
That proof revision included the typographical correction `Q,quad` to
`Q,\quad` in display (4.3).  The status link changes no mathematics.

## 1. Imported setting and fixed data

The source assumes a spanning partition into the seven connected labelled
branch sets

```text
X, Y, D, U, F_1, F_2, F_3,
```

with every required adjacency except possibly `X-Y`.  The singleton `v` is a
component of `G-S`, so it is not a boundary vertex.  Its eight neighbours are
exactly the two displayed vertices of `U_0` and one literal representative
in each of the six foreign branch sets.  The decomposition
`U=U_0 dotunion {v}` is disjoint, `U_0` is connected, and both the prescribed
`U`-root and `u_0` remain in `U_0`.

The edge `z_0u_0`, with `z_0 in Z_0 subseteq D`, proves
`E_G(U_0,D) ne emptyset`; hence `D notin Omega`.  The ranked labels exclude
`D` and include `U`, exactly as required by the cited relaxed first-hit rank.
No chromatic or contraction-critical hypothesis is silently used in this
note.

## 2. Audit of Theorem 2.1

### 2.1 Empty lost-label set

When `Omega` is empty, replacing `U` by `U_0` and `D` by
`D union {v}` preserves a spanning partition.  The new `U` set is connected
by hypothesis; the enlarged `D` set is connected through `vs_D`.  The edge
`vk_1` supplies the new `U_0`--`D union {v}` adjacency.  By
`Omega=emptyset`, `U_0` retains an edge to each of the other five foreign
branch sets.  Enlarging `D` cannot destroy any old foreign--foreign
adjacency, so the only possible missing adjacency remains `X-Y`.

### 2.2 One lost label

Suppose `Omega={R}`.  The edge `vs_R` makes `R union {v}` connected, and
`vk_1` restores its adjacency to `U_0`.  For every foreign label other than
`R`, the definition of `Omega` leaves an old edge from `U_0` to that branch
set.  The enlarged `R` retains all of its old foreign adjacencies.

The only exceptional old foreign adjacency could be `X-Y`.  If `R` is `X`
or `Y`, the edge from `v` to the representative in the opposite polar branch
set repairs that adjacency, while `vk_1` supplies the `R`--`U_0` adjacency;
all seven replacement sets are therefore pairwise adjacent.  This is an
explicit `K_7`-minor model.  If `R` is one of the `F_i`, the possible
`X-Y` deficiency is unchanged and the replacement is another labelled
`K_7`-minus-one-edge model.  The case `R=D` is impossible because of the
fixed edge `z_0u_0`.

### 2.3 Roots, response data, and rank

No prescribed root is moved: the only transferred vertex is `v`, and the
prescribed root of its old branch set `U` lies in `U_0`.  The graph, the
literal boundary and its selected partition, `Z_0`, its designated ports,
and the fixed edge `z_0u_0` are unchanged.  In the empty-owner case `Z_0`
remains a subgraph of the enlarged `D` branch set.

A ranked path with terminal label different from `U` avoided every vertex
of the old ranked branch set `U`; in particular it avoided `v` and survives
either transfer.  A ranked `U`-path ending in `U_0` also survives.  If it
ended at `v`, a path inside connected `Z_0` from its retained designated port
to `z_0`, followed by `z_0u_0`, first meets the ranked branch sets at `u_0`.
Overlap inside `Z_0` is allowed.  Outside `Z_0` the replacement contains only
`u_0`, which every other ranked path avoided because it belonged to the old
`U`.  The designated ports remain distinct and pairwise disjointness outside
`Z_0` is preserved.  Thus the relaxed first-hit rank cannot decrease.

Every nonterminal replacement consequently belongs to the same compatible
class, has maximum rank, and has strictly smaller `U`, contradicting the
secondary extremal choice.  This proves `|Omega|>=2`.

## 3. Audit of Theorem 3.1 and Corollary 3.2

If neither polar label is in `Omega`, the set `U_0 union X` is connected and
is adjacent to `Y` through an `U_0-Y` edge.  It is adjacent to
`D,F_1,F_2,F_3` through the old `X` branch set.  The singleton `v` is
adjacent to `U_0 union X` through `vk_1` (also through `vs_X`) and to each of
the other five branch sets through its displayed boundary neighbours.
Finally `Y,D,F_1,F_2,F_3` are pairwise adjacent in the old model.  The seven
sets in (3.2) are disjoint, connected and pairwise adjacent, so they give the
claimed `K_7`-minor contradiction.  Therefore at least one of `X,Y` lies in
`Omega`.

Under the additional hypothesis `|Omega|=3`, the fixed edge excludes `D`.
The remaining universe is `{X,Y,F_1,F_2,F_3}` and contains at least one of
`X,Y`.  Up to exchanging the two polar labels and permuting the three
`F_i`, there are exactly two possibilities: both polar labels and one
`F_i`, or one polar label and two `F_i`.  These are precisely the two
patterns in (3.3).  The corollary does not assert that the provenance always
gives `|Omega|=3`.

## 4. Audit of Theorem 4.1

Let `Q` be a component of `G-S` different from `{v}`, with `N_G(Q)=S`, and
fix `w in S`.  A `K_5`-minor model `M_1,...,M_5` in `G[S-w]` is disjoint from
both `Q` and `{v,w}`.  These seven sets are connected: `Q` and the `M_i` by
definition, and `{v,w}` through the edge `vw`.

All required adjacencies are literal:

- `{v,w}` meets each `M_i` because `v` is adjacent to every vertex of `S`;
- `{v,w}` meets `Q` because `w in N_G(Q)=S`;
- `Q` meets each nonempty `M_i` because `Q` has a neighbour at every literal
  boundary vertex; and
- the five `M_i` are pairwise adjacent by the assumed `K_5` model.

Thus the seven displayed sets form an explicit `K_7`-minor model, proving
`K_5 notpreccurlyeq G[S-w]` for every `w in S`.  The argument correctly
repartitions the relevant vertices and does not reuse inherited branch-set
vertices.

## 5. Trust boundary

The note proves only the following conditional facts about the singleton
outcome:

1. at least two foreign adjacencies of `U_0` are lost;
2. at least one lost label is `X` or `Y`;
3. if exactly three labels are lost, only the two stated label patterns
   remain; and
4. in the presence of another boundary-full component, every
   vertex-deleted boundary is `K_5`-minor-free.

It does not prove that `|Omega|=3`, produce a common boundary colouring,
repartition the opposite component into the inherited six labels, invoke the
degree-eight cyclic-contact theorem, eliminate the singleton, or prove
`HC_7`.  No hidden use of palette-colour/branch-label identification, higher
connectivity, or contraction-criticality was found.
