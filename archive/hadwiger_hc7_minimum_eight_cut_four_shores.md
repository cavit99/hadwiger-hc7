# A uniform high-component closure at the equality cut

## Theorem 1 (component cap and extremal quadratic cut bound)

Let `t>=7`, and let `G` satisfy

\[
 \chi(G)=t,\qquad \chi(H)\le t-1\text{ for every proper minor }H<G,
 \qquad \eta(G)\le t-1.
\tag{1.1}
\]

Suppose a minimum vertex cut `S` has order `c`, and `G-S` has exactly
`m>=2` components.  Then

\[
                              m\le t-3.                       \tag{1.2}
\]

Moreover, in the extremal row `m=t-3`,

\[
             c\ge m^2-2m+2=t^2-8t+17.                       \tag{1.3}
\]

### Proof

The uniform full-cut inequality gives

\[
                         m\le \chi(G[S]),\qquad c\ge2m.       \tag{1.4}
\]

First suppose `m>=t`.  Choose `t` of the full components and `t-1`
distinct boundary vertices.  The shore bags in the full-shore reserve
construction already form a `K_t` model, a contradiction.  If `m=t-1`,
use one boundary vertex as a `K_1` core and the other `m-1` reserves; the
reserve lift again gives `K_t`.  If `m=t-2`, (1.4) says that `G[S]` has an
edge.  Use that edge as a `K_2` core.  Since

\[
                           c-2\ge2m-2\ge m-1,
\]

there are enough reserves, and the lift gives `K_t`.  Hence (1.2) holds.

It remains to prove (1.3).  Put `m=t-3`; then `m>=4`.  Suppose for a
contradiction that `c<m^2-2m+2`.  Choose a critical subgraph `Q` of
`G[S]` with chromatic number `chi(G[S])`.  By (1.4),
`delta(Q)>=chi(G[S])-1>=m-1`.  We claim that `Q` contains a cycle of
length at most four.  Otherwise its girth is at least five.  A vertex `x`
has at least `m-1` distinct neighbours, each with at least `m-2` further
neighbours.  The absence of triangles and 4-cycles makes all vertices in
these two distance layers distinct, so

\[
 |V(Q)|\ge1+(m-1)+(m-1)(m-2)=m^2-2m+2,
\]

contrary to `Q subseteq G[S]` and `|S|=c<m^2-2m+2`.

A cycle of length three or four contains a `K_3` model supported on at
most four vertices.  Hence at least `c-4>=2m-4>=m-1` vertices of `S`
avoid that model.  Choose `m-1` of them as reserves.  The `m` components
of `G-S` are connected, pairwise anticomplete, and full to `S`, because
`S` is a minimum cut.  The full-shore reserve lift now gives a
`K_{m+3}=K_t` minor, a contradiction.  This proves (1.3).  \(\square\)

### Corollary 1.1 (equality cut)

If `c=2m` and `m>=4`, then `m<=t-4`.  Indeed the only additional row
allowed by (1.2) is `m=t-3`, but for `m>=4` one has

\[
                         2m<m^2-2m+2,
\]

contradicting (1.3).

## Corollary 2 (minimum-eight four-shore closure for `HC_7`)

Let `G` be a graph satisfying

\[
 \chi(G)=7,\qquad \chi(H)\le 6\text{ for every proper minor }H<G,
 \qquad \eta(G)\le6.
\tag{2.1}
\]

Suppose `S` is a minimum vertex cut of order eight and `G-S` has four
components.  Then these assumptions are inconsistent.  Equivalently, a
minor-minimal counterexample to `HC_7` cannot have a minimum eight-cut
with four components.

### Proof

This is Theorem 1 with `t=7` and `m=4`, since (1.3) requires `c>=10`.
For completeness, the literal order-eight argument follows.

Write

\[
                         G-S=D_1\dot\cup D_2\dot\cup D_3\dot\cup D_4.
\tag{2.2}
\]

Every `D_i` is connected and full to `S`: its neighbourhood is a vertex
cut contained in the minimum cut `S`, so it is all of `S`.

Apply Theorem 3.1 of `hadwiger_uniform_full_cut_inequalities.md` with
`k=7`, `c=8`, and `m=4`.  It gives

\[
                         4\le \chi(G[S])\le 8-4=4.
\tag{2.3}
\]

Thus `chi(G[S])=4`.  Choose a 4-critical subgraph `Q` of `G[S]`.  Every
vertex of `Q` has degree at least three in `Q`.

We claim that `Q` contains a cycle of length at most four.  Otherwise its
girth is at least five.  Choose a vertex `x` and three distinct neighbours
`x_1,x_2,x_3`.  Each `x_i` has two neighbours other than `x`.  These six
vertices are all distinct: a coincidence between the choices at two
different `x_i` creates a 4-cycle, and a choice lying among
`x_1,x_2,x_3` creates a triangle.  They are also different from `x`.
Consequently

\[
                         |V(Q)|\ge1+3+6=10,
\]

contrary to `Q subseteq G[S]` and `|S|=8`.  This proves the claim.

Let `C` be such a cycle.  A triangle is already a `K_3`; a 4-cycle
becomes a `K_3` after contracting one of its edges.  Hence `G[S]` has a
`K_3` model whose support uses at most four boundary vertices.  At least
four vertices of `S` lie outside that support; choose three of them as a
reserve set `Z`.

The four sets `D_1,D_2,D_3,D_4` are pairwise anticomplete connected full
shores.  The residual boundary `G[S-Z]` still contains the displayed
`K_3` model.  The full-shore reserve lift, with `m=4` and `q=3`, therefore
gives a `K_7` minor in `G`, contradicting (2.1).  \(\square\)

## Corollary 3 (all minimum cuts in an `HC_7` counterexample)

Under the hypotheses of Corollary 2, every minimum vertex cut has two or
three components behind it, and

\[
                              \kappa(G)\in\{7,8,9\}.          \tag{3.1}
\]

### Proof

Mader's sharp extremal bound for `K_7` minors gives

\[
                              |E(G)|\le5|V(G)|-15.
\]

Thus the average degree is strictly below ten, so `delta(G)<=9` and
`kappa(G)<=9`.  The standard connectivity theorem for a noncomplete
7-contraction-critical graph gives `kappa(G)>=7`, proving (3.1).

Let `S` be a minimum cut and let `m` be the number of components of
`G-S`.  Theorem 1 gives `m<=7-3=4`.  If `m=4`, its extremal clause gives

\[
                              |S|\ge4^2-2\cdot4+2=10,
\]

contrary to `|S|=kappa(G)<=9`.  Hence `m<=3`.  Since `S` is a vertex cut,
`m>=2`.  \(\square\)

## Literal branch-set check

If `Z={z_2,z_3,z_4}` and `Q_1,Q_2,Q_3` are the three residual model
bags, the seven bags are

\[
 D_1,\quad D_2\cup\{z_2\},\quad D_3\cup\{z_3\},\quad
 D_4\cup\{z_4\},\quad Q_1,\quad Q_2,\quad Q_3.
\]

They are disjoint and connected.  Fullness supplies every shore--shore
and shore--core adjacency, while the last three bags are pairwise
adjacent by the `K_3` model.  No edge between two open shores is used.

## Scope

The proofs close unbounded graph families, not merely finite boundary
enumerations.  Minimum-cardinality of the cut is essential for the uniform
cut inequality and for fullness of all components.  The argument does not
assert the same conclusion for an arbitrary nonminimum adhesion.

---

## 4. The next component row: a uniform small-support argument

The preceding proof used a short cycle to obtain a small `K_3` core.
For the next row one needs a `K_4` core, and there is a clean density
substitute for the short-cycle argument.

### Lemma 4.1 (random small support)

Let `F` be a graph on `n` vertices with minimum degree at least `d`, and
let `2<=r<=n`.  If

\[
                    d r(r-1)>2(n-1)(2r-3),                  \tag{4.1}
\]

then `F` contains a `K_4` minor supported on at most `r` vertices.

#### Proof

Choose an `r`-set `R` uniformly at random.  Since
`e(F)>=nd/2`,

\[
 \mathbb E e(F[R])
   =e(F)\frac{r(r-1)}{n(n-1)}
   \ge \frac{d r(r-1)}{2(n-1)}>2r-3.                        \tag{4.2}
\]

Thus some `R` satisfies `e(F[R])>2r-3`.  Every simple
`K_4`-minor-free graph on `r` vertices has at most `2r-3` edges, so
`F[R]` contains a `K_4` minor.  Its support is contained in `R`. \(\square\)

We will also use the standard Dirac critical-edge bound: if `F` is a
noncomplete `q`-critical graph on `n` vertices, then

\[
                         2e(F)\ge(q-1)n+q-3.                 \tag{4.3}
\]

### Theorem 4.2 (closure of the row `m=t-4` for `m>=6`)

Under the hypotheses of Theorem 1, the case

\[
                             m=t-4\ge6                       \tag{4.4}
\]

is impossible.  Consequently, if `t>=10`, every minimum cut has either
at most `t-5` components, or exactly `t-3` components; in the latter
case Theorem 1 additionally forces the quadratic lower bound (1.3).

#### Proof

Suppose `m=t-4`, put `c=|S|`, and choose a `p`-critical subgraph `Q` of
`G[S]`, where `p=chi(G[S])`.  The full-cut inequality gives

\[
                     p\ge m,\qquad c\ge2m.                   \tag{4.5}
\]

Set

\[
                         r=c-m+1.                            \tag{4.6}
\]

It is enough to find a `K_4` model in `Q` supported on at most `r`
vertices: at least `c-r=m-1` boundary vertices then remain as reserves,
and the full-shore reserve lift produces a
`K_{m+4}=K_t` minor.

Write `n=|Q|`.  If `n<=r`, the conclusion follows from `chi(Q)>=4` and
the elementary case `HC_4`.  We may therefore assume `r<n<=c`.

First let `m>=8`.  Since `delta(Q)>=p-1>=m-1`, Lemma 4.1 applies once

\[
             (m-1)r(r-1)>2(c-1)(2r-3).                      \tag{4.7}
\]

Writing `a=c-m`, so `a>=m` and `r=a+1`, the left side minus the right
side in (4.7) is

\[
       (m-5)a^2+(-3m+5)a+2m-2.                              \tag{4.8}
\]

For `m>=8` this quadratic is increasing for `a>=m`, and at `a=m` it
equals

\[
                         m^3-8m^2+7m-2>0.                    \tag{4.9}
\]

(The value at `m=8` is `54`, and the polynomial is increasing from
there.)  This proves (4.7) and closes all `m>=8`.

Next treat `m=7`.  If `Q` is complete, it contains a literal
`K_4`.  Otherwise Dirac's bound (4.3), together with `p>=7`, gives

\[
                         2e(Q)\ge6n+4.                       \tag{4.10}
\]

The function `(6n+4)/(n(n-1))` decreases with `n`, so sampling an
`r`-set from `Q` gives more than `2r-3` expected edges provided

\[
                 (6c+4)r(r-1)>2c(c-1)(2r-3).                \tag{4.11}
\]

Put `a=c-7>=7`, so again `r=a+1`.  The left side minus the right side
of (4.11) is

\[
                     2(a^3+a^2-48a+42),                     \tag{4.12}
\]

which is positive at `a=7` and strictly increasing for `a>=7`.
Hence some induced `r`-vertex subgraph has more than `2r-3` edges and
contains a `K_4` minor.

Finally let `m=6`, so `t=10`.  In the same Dirac-sampling calculation,
writing `a=c-6`, the sufficient strict inequality has difference

\[
                         a^3-4a^2-65a+60,                    \tag{4.13}
\]

which equals ten at `a=10` and is strictly increasing thereafter.  Thus
it closes every `c>=16` and
only `12<=c<=15` remain.  Since `chi(G[S])>=6`, an inclusion-minimal
subgraph not 5-colourable is 6-critical.  Known `HC_6` supplies a `K_6`
model in it; let its six bag orders be

\[
                         a_1\le\cdots\le a_6,
                         \qquad \sum_i a_i\le c.             \tag{4.14}
\]

The four smallest bags give a `K_4` model supported on at most
`floor(2c/3)` vertices.  For `13<=c<=15`,

\[
                         \lfloor2c/3\rfloor\le c-5=r,        \tag{4.15}
\]

so the reserve lift closes these cases.

Let `c=12`.  If `a_1+\cdots+a_4<=7`, the same lift applies.  Otherwise
the ordering and (4.14) force

\[
                              a_1=\cdots=a_6=2.              \tag{4.16}
\]

Indeed the first four sum to at least eight, while the last two are each
at least `a_4`; total order at most twelve leaves only six 2-vertex bags.
Fix one bag `B={u,v}`.  For each of the other five bags, assign its model
adjacency to an endpoint of `B` incident with such an edge.  One of `u,v`
is assigned at least three bags.  That singleton endpoint together with
those three 2-vertex bags is a `K_4` model supported on
`1+3\cdot2=7=r` vertices.  Five reserves remain, and the six shores lift
it to `K_{6+4}=K_{10}`.  This closes `m=6` and completes the proof.
\(\square\)

### Proposition 4.3 (the next row is bounded at `t=9`)

Under the hypotheses of Theorem 1, if

\[
                              m=t-4=5,                       \tag{4.17}
\]

then

\[
                              10\le c\le15.                  \tag{4.18}
\]

### Proof

The lower bound is `c>=2m`.  Suppose `c>=16`.  Since
`chi(G[S])>=5`, the boundary contains a 5-critical subgraph, and known
`HC_5` supplies a `K_5` model in it.  Let the total support order be `s`
and the largest bag order be `b`.  Then

\[
                              b\ge\lceil s/5\rceil.
\]

The number of unused boundary vertices plus `b` is

\[
                    (c-s)+b\ge(c-s)+\lceil s/5\rceil\ge4.   \tag{4.19}
\]

For the last inequality, if `c-s>=4` it is immediate; otherwise put
`u=c-s in {0,1,2,3}` and use
`u+ceil((c-u)/5)>=4` for `c>=16`.  Omit the largest model bag.  The other
four bags form a `K_4` model supported on at most `c-4=c-m+1` vertices.
The remaining four boundary vertices are reserves, and the five full
shores lift this core to a `K_9`, a contradiction.  Hence `c<=15`.
\(\square\)

---

## 5. Uniform density-to-support conversion

The sampling argument is not special to `K_4`.  It converts any
extremal density theorem for clique minors into a restriction on the
number of full components behind a minimum cut.

For `q>=2`, let `B_q` be any number with the property

\[
 \text{every graph of average degree greater than `B_q` has a `K_q`
 minor}.                                                     \tag{5.1}
\]

### Theorem 5.1 (fixed-deficit component exclusion)

Under the hypotheses of Theorem 1, put

\[
                             q=t-m.                          \tag{5.2}
\]

If

\[
                    \frac{m(m-1)}{2m-1}>B_q,                \tag{5.3}
\]

then the minimum cut `S` cannot exist.

#### Proof

Let `p=chi(G[S])` and choose a `p`-critical subgraph `Q` of `G[S]`.
As before,

\[
                         p\ge m,qquad delta(Q)\ge m-1,
                         \qquad c=|S|\ge2m.                  \tag{5.4}
\]

Put `r=c-m+1` and `n=|Q|`.  If `n<=r`, then the average degree of `Q`
is at least `m-1`, which is strictly larger than the left side of
(5.3), hence larger than `B_q`.  Thus `Q` itself contains a `K_q`
minor supported on at most `r` vertices.

Suppose instead that `n>r`, and choose a uniform random `r`-set `R` of
`V(Q)`.  Its expected average degree satisfies

\[
 \mathbb E\,\overline d(Q[R])
   =\frac{2e(Q)}n\frac{r-1}{n-1}
   \ge(m-1)\frac{r-1}{n-1}
   \ge(m-1)\frac{c-m}{c-1}.                                 \tag{5.5}
\]

For `c>=2m`, the last expression is minimized at `c=2m`, where it is
exactly the left side of (5.3).  Hence some `Q[R]` has average degree
greater than `B_q` and contains a `K_q` minor.

In either case there is a `K_q` model in `G[S]` supported on at most
`r=c-m+1` vertices.  The other at least `m-1` boundary vertices are
reserves.  Combining the core model with the `m` full shores gives a
`K_{q+m}=K_t` minor, a contradiction. \(\square\)

### Corollary 5.2 (elementary infinite range)

Using the elementary Mader bound `B_q=2^{q-2}`, the row `m=t-q` is
impossible whenever

\[
                         m\ge2^{q-1}+1.                      \tag{5.6}
\]

Indeed, writing `B=2^{q-2}`, substitution of `m=2B+1` into the
strict inequality in (5.3), after clearing the denominator, leaves the
positive quantity `B`; the left side of (5.3) increases with `m`.

In particular, the formerly extremal row `m=t-3` is impossible for
every `m>=5`.  Thus for `t>=8` it does not survive at any cut order,
not merely below the quadratic bound (1.3).

### Corollary 5.3 (asymptotic component deficit)

Using a Kostochka--Thomason threshold

\[
                 B_q=(0.63817\ldots+o(1))q\sqrt{\log q},    \tag{5.7}
\]

the existence of a minimum cut with `m` components forces

\[
                 m<(1.27634\ldots+o(1))q\sqrt{\log q},
                 \qquad q=t-m.                              \tag{5.8}
\]

Consequently

\[
                         q=\Omega\!\left(
                           \frac{t}{\sqrt{\log t}}\right),   \tag{5.9}
\]

uniformly over all minimum cuts in a hypothetical least counterexample.
This does not prove Hadwiger's conjecture, but it rules out every cut
whose number of full components lies within
`o(t/sqrt(log t))` of `t`.

### Corollary 5.4 (first exact uniform caps)

For every `t>=8`, every minimum cut has at most `t-4` components.  For
every `t>=10`, every minimum cut has at most `t-5` components.

### Proof

Theorem 1 excludes `m>=t-2`.  Corollary 5.2 with `q=3` excludes
`m=t-3` for `m>=5`, which is exactly `t>=8`.  Theorem 4.2 additionally
excludes `m=t-4` once `m>=6`, which is exactly `t>=10`.  \(\square\)
