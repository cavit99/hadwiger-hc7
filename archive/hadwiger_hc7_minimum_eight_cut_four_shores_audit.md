# Audit: high-component minimum-cut theorem

## Verdict

`GREEN`, with the new Sections 4--5 checked as stated.

## Theorem 1

The component cap `m<=t-3` is sound.

* Minimum-cardinality of `S` makes every component of `G-S` full to
  `S`.
* `m>=t` gives `t` shore bags using `t-1` boundary reserves.
* `m=t-1` adds a singleton boundary core and uses `m-1` further
  reserves.
* `m=t-2` uses a boundary edge (forced by `chi(G[S])>=m`) as a `K_2`
  core and `m-1` reserves.  The inequality `c-2>=m-1` follows from
  `c>=2m`.

The quadratic bound in the row `m=t-3` is also sound.  A critical
boundary subgraph has minimum degree at least `m-1`; girth at least five
therefore forces at least

\[
                 1+(m-1)+(m-1)(m-2)=m^2-2m+2
\]

vertices.  A shorter cycle supplies a `K_3` model on at most four
vertices, leaving the required `m-1` reserves because
`c-4>=2m-4>=m-1`.

No contraction-critical neighbourhood-independence statement is used
for the merely vertex-critical boundary subgraph.

## New small-support extension

Lemma 4.1 is the standard random-induced-subgraph conversion of the
sharp extremal bound `e(F)<=2|F|-3` for `K_4`-minor-free graphs.

For the row `m=t-4`, the support allowance is exactly
`r=c-m+1`.  A `K_4` model on at most `r` vertices leaves `m-1`
reserves, so the lift really has `m+4=t` branch bags.

For `m>=8`, after writing `a=c-m>=m`, the sufficient inequality has
difference

\[
                  (m-5)a^2+(-3m+5)a+2m-2.
\]

It is increasing on `a>=m` and positive from `(m,a)=(8,8)` onward.
For `m=7`, Dirac's critical-edge bound reduces the difference to

\[
                       2(a^3+a^2-48a+42),
\]

positive and increasing for `a>=7`.  Thus that part of the row is
eliminated at every cut order.  The theorem correctly retains the
possible exceptional row `m=t-3`; it does not incorrectly infer a
monotone component cap from eliminating `m=t-4`.

For `m=6`, the same calculation is positive from `c-6>=10`, leaving
`12<=c<=15` before the final structural argument.  Known `HC_6` gives
a six-bag `K_6` model in the 6-chromatic boundary.  For `13<=c<=15`,
the four smallest bags use at most `floor(2c/3)<=c-5` vertices.  At
`c=12`, either four bags use at most seven vertices, or all six bags
have order two; in the latter case one endpoint of one bag contacts at
least three other bags and yields a seven-vertex `K_4` model.  This
closes `m=6` without a new finite enumeration.

## Uniform density conversion

Theorem 5.1 is sound.  Sampling `r=c-m+1` vertices of a critical
boundary subgraph gives expected average degree at least

\[
                  (m-1)\frac{c-m}{c-1}
                  \ge\frac{m(m-1)}{2m-1}.
\]

A density-forced `K_q` model on that support, together with `m-1`
reserves and `m` full shores, gives `K_{q+m}=K_t`.  The elementary and
Kostochka--Thomason corollaries follow by direct substitution.

## Exact remaining limitations

1. The proof applies to a **minimum-cardinality** cut.  Fullness is not
   automatic for an arbitrary adhesion.
2. The `m=7` improvement uses the named Dirac critical-edge theorem;
   the `m>=8` part is elementary from minimum degree.
3. The `m=6` closure additionally invokes known `HC_6`.  The method
   does not close `m=t-4<=5` or the smaller fixed-deficit rows.

## Named theorem dependency ledger

* `e(F)<=2|V(F)|-3` for simple `K_4`-minor-free graphs (the sharp
  elementary extremal theorem for series-parallel graphs).
* Dirac's critical-edge bound
  `2e(F)>=(q-1)|V(F)|+q-3` for a noncomplete `q`-critical graph
  (automatically of order at least `q+2`).
* `HC_4` in the trivial whole-support subcase.
* Known `HC_6` (Robertson--Seymour--Thomas, depending on the Four Color
  Theorem) only for the finite-width `m=6`, `12<=c<=15` bag argument.
* The elementary Mader density bound `B_q=2^{q-2}` only for Corollary
  5.2.
* The Kostochka--Thomason asymptotic density threshold, with natural
  logarithm, only for Corollary 5.3.

The component cap, the quadratic extremal-row bound, the reserve lift,
and the general density-to-support conversion are otherwise proved in
the workspace package rather than imported.
