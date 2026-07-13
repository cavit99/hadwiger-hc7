# Independent audit: one-hole height gap

## Verdict

**GREEN after correction.**  Theorem 1 and Corollary 2 hold in the
target-free near-model state space.  Corollary 3 now states only the safe
fixed-frame continuation proved by the height count.

No finite counterexample to the numerical height inequality exists: the
proof is a direct ownership count.  Corollary 3 needs the precise
single-gate rotation hypotheses (and a target-free branch) added; the
height inequality alone does not identify a second move as the named
endpoint-shadow construction.

## Model convention required

For the statements to be unambiguous, a `q=1` or `q=2` model must mean:

* seven pairwise disjoint nonempty connected bags;
* the six foreign bags form a literal `K_6` model;
* the centre is anticomplete to exactly `q` foreign bags and adjacent to
  every other foreign bag.

The minimum `mu` is over the noncomplete (`q=1,2`) models.  Equivalently,
one may allow `q=0` only while explicitly assuming that the host is
`K_7`-minor-free.  Without one of these conventions, Corollary 2(1)
does not syntactically exclude a complete seven-bag state at level
`mu`.

## Audit of Theorem 1

1. The family minimized in (1.2) is nonempty because the displayed
   `K_7^-` model is admissible.  The graph is finite, so the two minima
   used in the proof exist.  The minimum one-hole centre need not attain
   `mu`; the proof does not assume that it does.
2. Interpret `Omega_A(Y)` using all literal `A-F_i` edges (or a fixed
   nonempty set of witnessing model edges for every spoke).  If it is
   empty, every required row has a surviving contact in `A-Y`, so deleting
   `Y` is legal.  If it is `{i}`, then `F_i union Y` is connected through
   a `Y-F_i` edge; `A-Y` is connected; and a cut edge between `Y` and
   `A-Y` restores the centre--enlarged-row adjacency.  The original
   `F_i` preserves all foreign-row adjacencies.  Thus both smaller-centre
   moves are valid.
3. A leaf of any spanning tree is detachable because deleting it leaves
   that tree connected.  Monopoly sets of two different leaf singletons
   are disjoint: a nonempty spoke cannot have every centre endpoint equal
   to two distinct vertices.  Since each leaf owns at least two of five
   labels, every spanning tree has at most two leaves, hence exactly two
   when the centre is nonsingleton.
4. If `G[A]` had a vertex of degree at least three, three incident edges
   form a forest extendable to a spanning tree with degree at least three,
   and such a tree has at least three leaves.  Therefore `Delta(G[A])<=2`.
   The connected graph `G[A]` is a path or a cycle.  In a cycle every
   singleton is detachable; any three singleton monopoly sets would be
   disjoint and use at least six labels.  Hence the cycle case is
   impossible and `G[A]` is an induced path.
5. The endpoint monopoly sets are disjoint, each has size at least two,
   and their union has size at most five.  Hence one endpoint `x` owns
   exactly two rows, say `F_i,F_j`.
6. In the endpoint absorption, `F_i union {x}` is connected through an
   `x-F_i` edge.  The path edge from `x` to `A-x` supplies its contact to
   the new centre.  The residual centre loses `F_j`, retains every row
   not owned by `x`, and remains anticomplete to the old missing row `B`.
   The other foreign adjacencies survive inside the old `F_i`.  The new
   model therefore has exactly two missing spokes and centre order
   `|A|-1`.
7. If the minimum one-hole centre were a singleton, it would itself show
   `mu=1`.  Under `mu>=2`, the endpoint move is available and gives
   `mu<=|A|-1`, hence `|A|>=mu+1`.  This proves Theorem 1.

No step uses seven-connectivity.  `K_7`-minor-freeness is needed only to
make the intended noncomplete state-space convention automatic.

## Corollaries

Corollary 2 is **GREEN** in that state space.  A level-`mu` state cannot
have one hole by Theorem 1, so it has two; a mixed rotation ending at a
one-hole state raises the centre order to at least `mu+1`, and its literal
inverse returns to the lower state.

The earlier Corollary 3 was **RED** for two precision reasons.

* It omits the target-free alternative: a subsequent gate can complete a
  literal `K_7`, which is not one of its three bullets.
* The height theorem determines only the deficiency and order of a
  second fixed-frame singleton move.  It does not prove that this move is
  the separately named endpoint-shadow construction.  That identification
  requires the hypotheses and conclusion of the endpoint-shadow/rotation
  theorem to be cited explicitly.

The theorem now uses the following safe replacement:

> In a target-free single-gate rotation walk, suppose a level-`mu`
> two-hole centre uses a singleton gate and produces a one-hole centre.
> A second pivot through the enlarged old centre either is the exact
> inverse, uses a nonsingleton gate, or, if its gate is a different
> singleton, leaves a centre of order `mu`; that residual centre must have
> two holes.  A pivot through another foreign bag changes the five-row
> frame.

For the different-singleton case, the enlarged old centre has order
`mu+1`, so removing one vertex leaves order `mu`; Theorem 1 excludes one
hole, and target-freeness excludes zero holes.  This is the full
conclusion supplied by the height argument.  Calling the move an
endpoint-shadow move is legitimate only after a separate theorem proves
that identification.
