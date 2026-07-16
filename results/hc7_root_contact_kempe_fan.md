# Root-contact Kempe fans and a rainbow-transition min--max theorem

**Status:** written proof; separately internally audited in
[`hc7_root_contact_kempe_fan_audit.md`](hc7_root_contact_kempe_fan_audit.md).
The results in this note do not prove `HC_7`.  They convert the colour-dominating witnesses at
two nonadjacent vertices into rooted paths with a literal endpoint, without
assuming that two arbitrary colourings are Kempe-equivalent.

## 1. Colour-dominating roots

Let `J` be a graph with a proper colouring `c` using the palette
`[q]={1,...,q}`.  Let `a,b` be two vertices outside `J`, with specified
neighbourhoods in `J`.  A root `r in {a,b}` is **colour-dominating** in
`c` when `N_J(r)` meets every colour class of `c`.

For a colour `i`, put

\[
 C_i=c^{-1}(i),\qquad A_i=N_J(a)\cap C_i,
 \qquad B_i=N_J(b)\cap C_i.                         \tag{1.1}
\]

### Theorem 1.1 (one witness for every other colour)

Assume that every proper `q`-colouring of `J` makes at least one of
`a,b` colour-dominating.  Suppose that `a` is colour-dominating in `c`
and that `b` misses a colour `gamma`, so `B_gamma=emptyset`.

For every `theta!=gamma`, some component of

\[
                    J[C_\gamma\cup C_\theta]          \tag{1.2}
\]

meets both `A_gamma` and `A_theta union B_theta`.  It therefore contains
a path `P_theta` from `A_gamma` to `A_theta union B_theta`.

If the second end of `P_theta` lies in `A_theta`, adjoining its two
incident root edges produces a cycle through `a`.  If it lies in
`B_theta`, adjoining the two root edges produces an `a-b` path.  Witnesses
for distinct colours `theta,phi` can intersect in `J` only at vertices of
`C_gamma`.

#### Proof

Fix `theta!=gamma` and suppose that no component in (1.2) has both kinds
of contact.  Interchange `gamma` and `theta` on every component of (1.2)
which meets `A_gamma`.  Switching an arbitrary collection of whole
bichromatic components preserves properness.

Every `gamma`-coloured neighbour of `a` is switched away.  By the
supposition, none of the switched components meets `A_theta`, so no new
`gamma`-coloured neighbour of `a` is created.  Thus `a` misses `gamma`
after the switches.  The root `b` had no `gamma`-coloured neighbour, and
no switched component meets `B_theta`; hence `b` still misses `gamma`.
This contradicts the hypothesis on every `q`-colouring of `J`.

The asserted path lies in the component just found.  Adding the indicated
root edges gives the cycle or cross-root path.  For distinct non-`gamma`
colours, the vertex sets of the two induced bichromatic graphs intersect
only in `C_gamma`, proving the last assertion.  \(\square\)

## 2. A rainbow-transition min--max formula

Let `T_gamma` be the spanning subgraph of `J` containing exactly those
edges with one endpoint in `C_gamma`.  Thus its edges join `C_gamma` to
the other colour classes.  Let `nu_gamma` be the maximum order of a family
of pairwise vertex-disjoint paths in `T_gamma` such that

1. every path starts in `A_gamma`;
2. every path ends in some `A_theta union B_theta`, with
   `theta!=gamma`; and
3. the terminal colours `theta` are distinct across the family.

For `Z subseteq V(J)`, let `r_gamma(Z)` be the number of colours
`theta!=gamma` for which `T_gamma-Z` has a path from
`A_gamma-Z` to `(A_theta union B_theta)-Z`.

### Theorem 2.1 (rainbow-transition min--max)

Under the hypotheses of Theorem 1.1,

\[
 \boxed{\displaystyle
 \nu_\gamma=\min_{Z\subseteq V(J)}
       \bigl(|Z|+r_\gamma(Z)\bigr).}                    \tag{2.1}
\]

Moreover either `nu_gamma=q-1`, or every minimizing set in (2.1)
contains a vertex of `C_gamma`.

#### Proof

Fix `Z`.  At most `|Z|` paths of a vertex-disjoint rainbow family meet
`Z`.  Every remaining path has one of the `r_gamma(Z)` terminal colours,
and those colours are distinct.  Hence

\[
                  \nu_\gamma\le |Z|+r_\gamma(Z).       \tag{2.2}
\]

For the reverse inequality, vertex-split `T_gamma`, giving the arc through
each original vertex capacity one.  Join a source to every vertex of
`A_gamma` by an infinite-capacity arc.  For every `theta!=gamma`, join
the vertices of `A_theta union B_theta` to a new colour vertex `t_theta`
by infinite-capacity arcs, and give the arc from `t_theta` to a common sink
capacity one.  Integral max-flow gives exactly a family counted by
`nu_gamma`.

For each `Z`, cut the capacity-one vertex arcs belonging to `Z` and the
sink arc of every terminal colour still reachable after deleting `Z`.
This is a finite cut of capacity `|Z|+r_gamma(Z)`.

Conversely, let `C` be any finite cut and let `Z` be the set of original
vertices whose capacity-one vertex arcs belong to `C`.  Every terminal
colour reachable in `T_gamma-Z` is reachable from the source without using
an arc of `C`, except possibly for its capacity-one sink arc.  That sink
arc must therefore belong to `C`.  Hence

\[
                 \operatorname{cap}(C)\ge |Z|+r_\gamma(Z).
\]

Taking minima in the two inequalities and applying max-flow/min-cut proves
(2.1).

Now suppose `Z` avoids `C_gamma`.  For each colour `theta` not counted by
`r_gamma(Z)`, the bichromatic path supplied by Theorem 1.1 must meet
`Z cap C_theta`.  Distinct missed terminal colours require distinct
vertices of `Z`.  Consequently

\[
 |Z|\ge(q-1)-r_\gamma(Z),
 \qquad |Z|+r_\gamma(Z)\ge q-1.                         \tag{2.3}
\]

Since at most one path can be assigned to each of the `q-1` terminal
colours, `nu_gamma<=q-1`.  Equations (2.1)--(2.3) give the final
assertion.  \(\square\)

### Corollary 2.2 (two disjoint transitions or one bottleneck)

If `q>=3`, exactly one of the following alternatives is forced.

1. There are two vertex-disjoint paths in `T_gamma`, starting in
   `A_gamma` and ending in target sets of two distinct colours.  After
   adding root edges they give two `J`-disjoint structures, each an
   `a`-cycle or an `a-b` path.
2. There is a vertex `z in C_gamma` such that `T_gamma-z` contains no path
   from `A_gamma-{z}` to any
   `(A_theta union B_theta)-{z}`, `theta!=gamma`.

#### Proof

If `nu_gamma>=2`, take two paths from a maximum family.  Otherwise,
Theorem 1.1 gives `nu_gamma>=1`, so `nu_gamma=1`.  Since `q>=3`, this is
strictly smaller than `q-1`; hence Theorem 2.1 says that a minimizing set
contains a `gamma`-coloured vertex.  Its total cost is one, so it is a
singleton `{z}` and `r_gamma({z})=0`.  This is the second outcome.  The
outcomes are exclusive because in the second outcome every transition
path contains `z`, so two such paths cannot be vertex-disjoint.  \(\square\)

The bottleneck in Corollary 2.2 separates the specified transitions in
`T_gamma`; it need not be a separator of `J`.

## 3. Contraction-critical exact-root form

Say that `G` is **strongly `(q+1)`-contraction-critical** when

\[
 \chi(G)=q+1
 \quad\text{and every proper minor of }G\text{ is }q\text{-colourable}.
                                                               \tag{3.1}
\]

### Theorem 3.1 (a chosen root edge anchors a Kempe fan)

Let `G` satisfy (3.1), let `a,b` be distinct nonadjacent vertices, and put
`J=G-{a,b}`.  Fix any neighbour `s in N_J(a)`.  There is a proper
`q`-colouring `c_s` of `J` and colours

\[
                         \lambda=c_s(s),\qquad \gamma,  \tag{3.2}
\]

such that

1. `s` is the unique `lambda`-coloured neighbour of `a`;
2. `a` is colour-dominating in `c_s`;
3. `b` misses `gamma` in `c_s`; and
4. if `lambda!=gamma`, then for every `theta` outside
   `{lambda,gamma}`, the
   `lambda-theta` component containing `s` also contains a
   `theta`-coloured neighbour of `a`.

Consequently, if `lambda!=gamma`, the edge `as` lies on at least `q-2`
cycles through `a`, one using only `lambda,theta` on its internal
vertices for each `theta notin {lambda,gamma}`.  Outside the root `a` and
the `lambda`-coloured vertices, these cycles are pairwise vertex-disjoint.

If `lambda=gamma`, then for every `theta!=lambda` the
`lambda-theta` component containing `s` contains either a
`theta`-coloured neighbour of `a` or a `theta`-coloured neighbour of `b`.
Thus it produces respectively an `a`-cycle through `as` or an `a-b` path
through `as`.

In particular, if `s` is a common neighbour of `a,b`, then
`lambda!=gamma`; for `q=6`, the literal edge `as` lies on four
colour-distinguished cycles of the stated form.

#### Proof

Let `H=G/as`, let `w` be the vertex produced by the contraction, and take
a proper `q`-colouring `d` of `H`.  Define a colouring `c_s` of `J` by

\[
 c_s(s)=d(w),\qquad c_s(v)=d(v)
       \quad(v\in V(J)-\{s\}).                          \tag{3.3}
\]

Thus `c_s` is obtained by restoring `s` and deleting `a` and `b` from the
coloured contraction minor.  It is proper.  Put

\[
                         \lambda=d(w),\qquad \gamma=d(b).
\]

Every other neighbour of `a` was adjacent to the contraction image and
therefore has colour different from `lambda=c_s(s)`.  This proves item 1.

The vertex `b` is present in `H`; properness says that its
`J`-neighbourhood has no vertex of colour `gamma=d(b)`.  Thus item 3 holds.
Every proper `q`-colouring of `J` makes at least one root
colour-dominating: otherwise assign to each of `a,b` a colour absent from
its neighbourhood; their nonadjacency makes this a proper `q`-colouring of
`G`, contrary to (3.1).  Since `b` is not colour-dominating in `c_s`,
`a` is, proving item 2.

Assume first that `lambda!=gamma`.  Fix
`theta notin {lambda,gamma}` and let `K_theta` be the
`lambda-theta` component containing `s`.  If it contained no
`theta`-coloured neighbour of `a`, switch its two colours.  The root `a`
would lose `lambda`, because `s` was its unique neighbour of that colour,
and it would gain no replacement `lambda` contact.  The root `b` would
still miss `gamma`, which is untouched by the switch.  This contradicts
the universal root-domination property just proved.  Hence item 4 holds,
and a path inside `K_theta` between the two root contacts, together with
the root edges, is the asserted cycle.

Suppose instead that `lambda=gamma`, fix `theta!=lambda`, and perform the
same switch.  Unless `K_theta` contains a `theta`-coloured neighbour of
`a`, the root `a` loses `lambda`.  The only way for `b`, which initially
misses `lambda`, to become colour-dominating is for `K_theta` to contain a
`theta`-coloured neighbour of `b`, which changes to `lambda`.  Otherwise
neither root would dominate, a contradiction.  This proves the stated
alternative.

Finally, if `s` is adjacent to `b`, then the contraction image of `as` is
adjacent to `b`, so properness of the minor colouring gives
`lambda!=gamma`.  The numerical assertion follows by putting `q=6`.
\(\square\)

## 4. Sharpness and exact limitation

Take `J=K_q`, let `a` be complete to `J`, and let `b` be adjacent to all
vertices of `J` except the vertex of colour `gamma`.  In every proper
`q`-colouring, `a` is colour-dominating.  The transition graph
`T_gamma` is a star centred at the `gamma`-coloured vertex.  Hence
`nu_gamma=1`, and that centre is unavoidable in every transition, although
it is not a cutvertex of `J` when `q>=3`.

Thus the min--max theorem cannot by itself produce an ambient separator.
Likewise, the colour-distinguished paths and cycles are not branch-set
labels.  In the exact order-eight `HC_7` residue, Theorem 3.1 can anchor a
fan at a selected neighbour inside a named branch set, but another theorem
is still required to turn either two disjoint transitions or the common
bottleneck into a label-preserving split of the spanning near-`K_7` model.
