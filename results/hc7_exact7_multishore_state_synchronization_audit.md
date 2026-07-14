# Independent audit: exact-seven multishore state synchronization

Audited file:
`results/hc7_exact7_multishore_state_synchronization.md`.

Audited SHA-256:
`b5b60a152bb1c769d382baa08fbd8a5af413d44135cdef4ed59cdd2535ec7a7c`.

The post-audit change only promoted the status line from “pending
independent audit” to “proved and independently audited”; the mathematical
text is identical to the version audited under SHA-256
`0c569627f9178ab9defad0414d14ca9558e784a166425cd57b250b643a23c767`.

**Verdict:** **GREEN.**

The initial two-component contraction returns an exact actual state on the
distinguished component side.  The proof then reproduces that same state,
by a separate proper minor, on every other component side.  Both possible
partitions of the three residual boundary vertices give the claimed clique
models, and all component-side palettes align and glue.  The complementary
lock application, duty-aware extension, and one-edged-defect corollary are
also valid at their stated scopes.

## 1. Initial exact state

Choose full components `A,Q` distinct from `C`.  The sets

\[
                         A\cup I,\qquad Q\cup J
\]

are disjoint and connected because `A,Q` are connected and `S`-full and
`I,J` are nonempty.  Their images are adjacent: `A` contacts every vertex
of `J` and `Q` contacts every vertex of `I`.  Each image is adjacent to
every literal vertex of `W` by fullness.

The contraction is proper because it contracts packet--boundary edges.
Restricting its six-colouring to the untouched original closed `C`-side and
expanding only `I,J` is proper because those sets are independent.  The two
contracted images are adjacent to one another and to all of `W`, so neither
`I` nor `J` can share a colour with another boundary block.  Thus the exact
partition is

\[
                         \Sigma=I\mid J\mid\Theta,
\]

where `Theta` is the actual proper equality partition induced on `W`.
Since `|W|=3` and `G[W]` has an edge, `Theta` has exactly two or three
blocks.

## 2. Reproduction on every component

Fix any component `R ne C`.  Because `G-S` has at least three components,
there is a full component `F` distinct from both `C` and `R`.  Every
reproduction minor uses only `C`, `F`, and boundary vertices, so the
original closed `R`-side is untouched.

### Two-block residual state

Write

\[
                         \Theta=K\mid\{w\},
\]

where `K` is an independent pair.  The four branch sets are

\[
              X\cup I,\qquad Y\cup J,\qquad F\cup K,
              \qquad\{w\}.
\]

They are disjoint and connected.  All six clique adjacencies are literal:

* the first two meet through the assumed `X-Y` edge;
* `F` contacts the nonempty sets `I,J`, joining its branch set to both
  carrier branch sets;
* `F` contacts `w`; and
* the complete contact condition on `W` joins both carriers to `w`.

This is a `K_4` with one representative for every block of `Sigma`.

### Three-block residual state

When `Theta` consists of three singleton blocks, choose a literal edge
`uv` of `G[W]` and let `w` be the third vertex.  The five branch sets are

\[
        X\cup I,\qquad Y\cup J,\qquad F\cup\{w\},
        \qquad\{u\},\qquad\{v\}.
\]

The carrier sets are adjacent; fullness of `F` supplies its adjacencies to
both carrier representatives and both retained vertices; complete carrier
contact with `W` supplies the four carrier-to-`u,v` adjacencies; and `uv`
is literal.  Hence the five representatives form a `K_5`, again indexed
exactly by the blocks of `Sigma`.

In both cases at least one edge is contracted, so the operation is a proper
minor.  Its six-colouring restricts to the original closed `R`-side, where
expanding the independent boundary blocks is proper.  The displayed clique
forces exactly `Sigma`, not a coarsening.

Repeating this construction for every `R ne C` leaves no component
uncoloured.  Each component-side colouring induces the same exact partition
of `S`.  Its injective block-to-colour map can be aligned with a fixed
reference map by a permutation of the six colours.  Components of `G-S`
are pairwise anticomplete, so the aligned original-side colourings glue to
a six-colouring of `G`.

## 3. Complementary-lock application

Section 2 explicitly continues under the hypotheses of Theorem 1.1.  With

\[
 P=\{a_1,a_2\}=\Delta(X),\qquad
 T=\{t_1,t_2\}=\Delta(Y),
\]

the choice

\[
                         I=T,\qquad J=P,
                         \qquad W=B_3\cup\{c\}
\]

has the correct orientation: `X` contacts all of `T`, while `Y` contacts
all of `P`.  Both carriers contact every vertex of `W`.  The assumptions of
the corollary make `I,J` independent, and the named `c-B_3` adjacency gives
an edge in the three-vertex graph `G[W]`.  Theorem 1.1 therefore proves the
first assertion of Corollary 2.1.  Its displayed necessary condition is the
valid contrapositive for a surviving non-six-colourable lock.

## 4. Duty-aware synchronization

For a retained vertex `w in W`, the representative of `X union I` is
adjacent to `w` exactly when either `X` contacts `w` or a literal vertex of
`I` is adjacent to `w`.  Thus

\[
 R_X=W\cap\bigl(N_S(X)\cup N_{G[S]}(I)\bigr)
\]

is the exact retained-singleton adjacency set for that representative;
`R_Y` has the symmetric meaning, and \(R=R_X\cap R_Y\) is precisely the set
seen by both representatives.

If the actual residual state is `(W-{w})|{w}`, properness makes `W-{w}`
independent.  Condition 2 of Theorem 4.1 therefore places `w` in `R`, which
supplies exactly the two carrier-to-singleton adjacencies needed by the
`K_4`; the full component funds the independent pair.

If the residual state has three singleton blocks, Condition 1 supplies an
edge `uv` of `G[R]`.  Both endpoints lie in `R`, so both labelled carrier
representatives see both retained vertices.  The full component funds the
third singleton, and the resulting representatives form the same `K_5` as
in Theorem 1.1.  Componentwise reproduction, exactness, palette alignment,
and gluing are consequently unchanged.  The two conditions cover every
possible actual partition of the three-vertex set `W`.

## 5. One-edged-defect corollary

In Corollary 4.2, take `P={p,q}` with literal edge `pq`, let `T` be
independent, and choose

\[
                         I=T,\qquad J=B_3,
                         \qquad W=P\cup\{c\}.
\]

Since `Delta(X)=P`, the carrier `X` contacts `c` but neither member of `P`;
the assigned block `T` contributes precisely

\[
                         D=N_{G[S]}(T)\cap P.
\]

Hence the representative `X union T` sees exactly `{c} union D` inside
`W`.  Since `Delta(Y)=T`, `Y` itself sees all of `W`.  Therefore

\[
                              R=\{c\}\cup D,
\]

as claimed.

If `D=P`, then `R=W`; the edge `pq` proves Condition 1 and every possible
retained singleton lies in `R`.  If `D={p}` and `cp` is literal, then
`R={c,p}` contains the edge `cp`.  The only vertex outside `R` is `q`, and
`W-{q}={c,p}` is not independent, so Condition 2 does not require `q`.
Every vertex which it does require belongs to `R`.  Theorem 4.1 applies in
both cases.

These cases exhaust the asserted positive outcomes.  Their contrapositive
is exactly

\[
 |D|\le1,\qquad D=\{p\}\Longrightarrow cp\notin E(G)
\]

for a survivor.  Interchanging `P,T` together with `X,Y` gives the symmetric
statement.

## 6. Scope

No finite boundary census, chosen colouring, planarity assumption, or
bounded component count is used.  The proof synchronizes the actual state
returned by the first minor across every component of the cut.  Arbitrary
additional boundary edges do not invalidate any branch: they either occur
between distinct equality blocks or preclude the corresponding equality
state from arising in the initial proper colouring.
