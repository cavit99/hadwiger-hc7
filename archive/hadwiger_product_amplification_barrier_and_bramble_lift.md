# Product amplification, universal suspension, and the bramble-lift barrier

## Status and purpose

This note audits the following possible uniform strategy.

> Start with a graph satisfying \(\chi(G)>\eta(G)\), apply a graph product
> repeatedly, make the chromatic gap grow faster than the Hadwiger number,
> and contradict a known bound of the form
> \(\chi(F)=O(\eta(F)\log\log \eta(F))\).

The audit is negative for all standard products.  It gives three exact,
scalable facts:

1. join powers manufacture clique minors at a rate controlled by the **order**
   of the factor, and their chromatic-to-Hadwiger ratio is asymptotically at
   most two;
2. clique lexicographic blow-ups are exactly bounded-congestion clique
   brambles, and their colour parameter converges to fractional chromatic
   number rather than ordinary chromatic number;
3. congestion-two clique brambles have an unbounded integrality gap even in
   planar graphs.

There is also a positive exact theorem: joining with a universal clique
preserves both contraction-criticality and the Hadwiger defect
\(\chi-\eta\).  Thus a hypothetical counterexample generates arbitrarily
highly connected counterexamples, but no asymptotic contradiction.  Any
successful amplification must therefore be a new **minor-reflecting palette
tensor**, not a standard graph product.

Throughout, \(\eta(G)\) is the largest \(s\) for which \(G\) has a
\(K_s\)-minor.

## 1. Join powers dilute every ordinary gap

Write

\[
       J_n(G)=G_1\vee G_2\vee\cdots\vee G_n
\]

for the join of \(n\) disjoint copies of a graph \(G\).  Put
\(N=|V(G)|\) and \(k=\chi(G)\).

### Proposition 1.1 (complete multipartite floor)

For every \(n\ge2\),

\[
 \chi(J_n(G))=nk,
 \qquad
 \eta(J_n(G))\ge
 n+\left\lfloor\frac{n(N-1)}2\right\rfloor
 =\left\lfloor\frac{n(N+1)}2\right\rfloor .       \tag{1.1}
\]

#### Proof

Colours used in distinct join factors must be disjoint, giving the first
identity.

Ignoring all edges internal to the copies, \(J_n(G)\) contains the complete
\(n\)-partite graph with \(N\) vertices in each part.  Choose one vertex in
each part as a singleton branch set.  Pair all but possibly one of the
remaining \(n(N-1)\) vertices so that every pair has its two ends in
different parts.  Such a pairing exists: for \(n=2\) pair the two parts
directly; for \(n\ge3\), the largest part has size \(N-1\), at most half the
total, so a greedy cross-part matching leaves at most one vertex.

Every pair is a connected branch set.  Two paired branch sets are adjacent,
because each uses two different parts.  A singleton in part \(i\) is adjacent
to every pair, since the pair has an end outside part \(i\).  Singletons in
different parts are adjacent.  These branch sets form the claimed clique
minor. \(\square\)

Since \(N\ge k\), (1.1) gives

\[
 \limsup_{n\to\infty}
 \frac{\chi(J_n(G))}{\eta(J_n(G))}
 \le \frac{2k}{N+1}<2.                              \tag{1.2}
\]

In particular, no matter how large \(\chi(G)/\eta(G)\) might be, join powers
cannot contradict an \(O(\eta\log\log\eta)\) colouring bound.  They drive the
ratio below two using branch sets that alternate between copies.  If
\(N+1\ge2k\), the lower bound in (1.1) already gives
\(\eta(J_n(G))\ge\chi(J_n(G))\) for all sufficiently divisible \(n\).

The familiar lower bound
\(\eta(G\vee H)\ge\eta(G)+\eta(H)\) is therefore far from an upper bound.
For example, \(I_s\vee I_s=K_{s,s}\), whose Hadwiger number is \(s+1\),
whereas the sum of the factor Hadwiger numbers is two.

## 2. Universal-clique suspension is exact

The special join with a clique behaves completely differently.

### Theorem 2.1 (exact suspension)

For every graph \(G\) and every \(\ell\ge0\),

\[
 \chi(K_\ell\vee G)=\ell+\chi(G),
 \qquad
 \eta(K_\ell\vee G)=\ell+\eta(G).                 \tag{2.1}
\]

#### Proof

The chromatic identity is immediate.  The lower minor bound is obtained by
using the \(\ell\) clique vertices as singleton bags beside a maximum clique
model in \(G\).

Conversely, consider any \(K_s\)-model in \(K_\ell\vee G\).  At most
\(\ell\) of its disjoint branch sets contain a vertex of \(K_\ell\).  Delete
those branch sets.  Every remaining bag lies in \(G\), and the remaining bags
are still pairwise adjacent.  Hence at least \(s-\ell\) bags form a clique
model in \(G\), so \(s\le\ell+\eta(G)\). \(\square\)

Thus the Hadwiger defect

\[
                         \Delta(G)=\chi(G)-\eta(G)
\]

is invariant under universal-clique suspension.

### Theorem 2.2 (suspension preserves minor-criticality)

Suppose \(G\) is minor-minimal with chromatic number \(k\):
\(\chi(G)=k\), and every proper minor of \(G\) is \((k-1)\)-colourable.
Then \(K_\ell\vee G\) is minor-minimal with chromatic number \(k+\ell\).

#### Proof

Let \(M\) be an arbitrary proper minor, represented by disjoint connected
branch sets in a subgraph of \(K_\ell\vee G\).  Add back every available
edge between the branch sets; colouring this supergraph is enough.  Let
\(r\) branch sets meet \(K_\ell\).  They form a universal clique, and
\(r\le\ell\).  The branch sets lying wholly in \(G\) form a minor \(H\) of
\(G\).  Hence \(M\) is a subgraph of \(K_r\vee H\).

If \(r<\ell\), this supergraph uses at most
\((\ell-1)+k\) colours.  If \(r=\ell\) and some clique-meeting branch set
also consumes a vertex of \(G\), or the pure \(G\)-bags otherwise describe
a proper minor of \(G\), then \(\chi(H)\le k-1\), again giving the desired
bound.

The only remaining case has the \(\ell\) clique vertices and all vertices of
\(G\) as singleton branch sets, and properness comes solely from deleting at
least one edge.  If a deleted edge lies in \(G\), use a \((k-1)\)-colouring
of that proper subgraph plus \(\ell\) clique colours.  If it lies in the
clique, its ends may share a colour.  If it is a cross-edge \(ug\), colour
\(G-g\) with \(k-1\) colours, give \(u,g\) one new common colour, and give
the other \(\ell-1\) clique vertices fresh colours.  Further deleted edges
do not hurt these colourings. \(\square\)

### Consequence 2.3 (a sharp barrier to connectivity amplification)

If a minor-minimal counterexample \(G\) exists, then
\(K_\ell\vee G\) is a minor-minimal counterexample for every \(\ell\), with
the same defect.  Moreover

\[
 \delta(K_\ell\vee G)=\ell+\delta(G),
 \qquad
 \kappa(K_\ell\vee G)=\ell+\kappa(G)
\]

for noncomplete connected \(G\).  Hence both ratios to the chromatic number
tend to one as \(\ell\to\infty\).  A theorem based only on a connectivity
lower bound \((1-o(1))\chi\), a minimum-degree lower bound
\((1-o(1))\chi\), or bounded degree surplus cannot distinguish a
hypothetical counterexample from its suspensions.

This does not obstruct induction on the *least* failing chromatic number: a
least-parameter counterexample has no universal vertex, since deleting one
would give a counterexample one parameter lower.  It says that the useful
uniform principle has to be **suspension-normalized** and act on the
join-prime core.

The corresponding statement for arbitrary join factors is deliberately
one-sided.

### Proposition 2.4 (join factors inherit criticality; the converse fails)

Let \(A,B\) be nonempty, with chromatic numbers \(a,b\).  If \(A\vee B\)
is minor-minimal \((a+b)\)-chromatic, then \(A\) and \(B\) are minor-minimal
at their own chromatic numbers.

Indeed, a proper minor \(A'\) of \(A\) gives the proper minor
\(A'\vee B\), so \(\chi(A')+b\le a+b-1\).  The other factor is symmetric.

The converse is false.  Each \(C_5\) is minor-minimal 3-chromatic, but
\(C_5\vee C_5\) is not minor-minimal 6-chromatic.  Label the two cycles
\(a_0,\ldots,a_4\) and \(b_0,\ldots,b_4\).  Contract the two disjoint
cross-edges \(a_0b_0\) and \(a_2b_2\).  Their images are two universal,
adjacent vertices.  The three pure vertices left in each cycle induce a
2-chromatic graph, and the two pure sides remain joined.  The resulting
proper minor therefore still has chromatic number
\(2+2+2=6\).

Universal cliques are exceptional because every mixed branch set consumes
one unit of the same universal-clique budget.  With two arbitrary factors,
several cross contractions can recover all palette loss.

### Corollary 2.5 (least counterexamples are join-prime)

Let \(G\) be a counterexample at the least failing chromatic parameter.
Then \(G\) is not a nontrivial join.

Indeed, if \(G=A\vee B\), both factors have smaller chromatic number and
therefore satisfy Hadwiger at their respective parameters.  Their clique
models coexist across the join and form a
\(K_{\chi(A)+\chi(B)}=K_{\chi(G)}\)-model, a contradiction.

Thus a genuinely new rooted-model or bramble principle should be formulated
for least-parameter **join-prime** contraction-critical graphs; otherwise
Theorem 2.2 manufactures misleading high connectivity and degree at will.
Proposition 2.4 warns that one cannot obtain this normalization by freely
factoring and rebuilding critical graphs.

## 3. Clique blow-ups are bounded-congestion clique brambles

Let \(G[K_m]\) denote the lexicographic product obtained by replacing every
vertex of \(G\) by a clique of order \(m\), with complete joins between
fibres corresponding to edges of \(G\).

A depth-\(m\) clique bramble in \(G\) is a family
\(\mathcal B=(B_1,\ldots,B_s)\) of connected vertex sets such that

* every two \(B_i,B_j\) touch (they intersect or an edge joins them); and
* every vertex of \(G\) belongs to at most \(m\) members of \(\mathcal B\).

### Theorem 3.1 (exact lift/projection equivalence)

For all \(G,m,s\), the graph \(G[K_m]\) contains a \(K_s\)-minor if and only
if \(G\) contains a depth-\(m\) clique bramble of size \(s\).  Consequently,

\[
 \eta(G[K_m])=max\{|\mathcal B|:\mathcal B
        \text{ is a depth-}m\text{ clique bramble in }G\}.              \tag{3.1}
\]

#### Proof

Project every branch set of a clique model in \(G[K_m]\) onto the base
vertices whose fibres it meets.  A projected set is connected.  Adjacency of
two lifted bags says that their projections intersect or are joined by a
base edge, so the projections touch.  Since a fibre has only \(m\) vertices
and the lifted bags are disjoint, at most \(m\) projected sets contain any
base vertex.

Conversely, for every incidence \(v\in B_i\), assign to \(i\) a distinct
vertex of the \(K_m\)-fibre over \(v\); this is possible by the congestion
bound.  The assigned fibre vertices over all \(v\in B_i\) form a connected
set, because \(B_i\) is connected.  Different lifted sets are disjoint.  If
two base sets intersect, their assigned vertices in the common clique fibre
are adjacent; if a base edge joins them, the corresponding fibres are
completely joined.  Thus the lifts form a \(K_s\)-model. \(\square\)

This is the precise object hidden by lexicographic amplification.  It is not
an ordinary clique minor with replicated labels; it is a bounded-congestion
packing of pairwise-touching connected sets.

## 4. Generic bramble rounding fails already at congestion two

### Theorem 4.1 (planar wiring obstruction)

For every \(s\), there is a planar graph \(W_s\) containing a depth-two
clique bramble of size \(s\).  Hence

\[
                    \eta(W_s)\le4,
 \qquad
                    \eta(W_s[K_2])\ge s.             \tag{4.1}
\]

In particular, there is no function \(f\) such that every depth-two clique
bramble of size \(f(r)\) in an arbitrary graph can be rounded to a
\(K_r\)-minor.

#### Proof

Take a wiring diagram of \(s\) curves in a rectangle: their order at the
left boundary is \(1,2,\ldots,s\), their order at the right boundary is
reversed, every two curves cross exactly once, and no three cross at one
point.  Planarize the diagram by making every crossing a vertex.  Let
\(W_s\) be the resulting planar graph and let \(P_i\) be the graph path
traced by the \(i\)-th wire.

Every pair \(P_i,P_j\) intersects at its unique crossing.  A crossing vertex
belongs to exactly two of the paths, and every noncrossing vertex belongs to
one.  Thus \(\{P_1,\ldots,P_s\}\) is a depth-two clique bramble.  The first
claim in (4.1) follows from planarity and the second from Theorem 3.1.
If the asserted rounding function existed, choosing \(s\ge f(5)\) would
give a \(K_5\)-minor in a planar graph. \(\square\)

The example can be triangulated by adding planar edges without destroying
the bramble, so the obstruction is not the absence of local density.  What
it lacks is contraction-critical colour dynamics.

## 5. Colour growth in lexicographic powers is fractional

Let \(\chi_m(G)\) be the least size of a palette from which one can assign
an \(m\)-element colour set to every vertex of \(G\), with disjoint sets on
adjacent vertices.

### Proposition 5.1 (multicolouring identity)

For every graph \(H\),

\[
                     \chi(G[H])=\chi_{\chi(H)}(G).    \tag{5.1}
\]

In particular,

\[
                     \chi(G[K_m])=\chi_m(G),
 \qquad
                     \eta(G[K_m])\ge m\eta(G).       \tag{5.2}
\]

#### Proof

Each fibre over a base vertex needs \(\chi(H)\) colours, and adjacent fibres
must use disjoint palettes.  Conversely, a multicolouring of the base and a
fixed optimal colouring of each fibre realize exactly those palettes.  This
proves (5.1).  For the minor bound in (5.2), take a maximum clique model in
\(G\).  For every base branch set and every index in \([m]\), take the clones
with that fixed index.  These are connected; clones with different indices
over the same base bag are adjacent within a fibre, and base-bag adjacencies
give all cross adjacencies. \(\square\)

The standard rational linear-programming description of fractional
colouring gives

\[
                    \lim_{m\to\infty}\frac{\chi_m(G)}m=\chi_f(G).        \tag{5.3}
\]

Thus clique blow-ups replace \(\chi(G)\) by \(\chi_f(G)\).  More generally,
iterated lexicographic powers are governed by multichromatic, not ordinary
chromatic, growth.  An ordinary gap \(\chi(G)>\eta(G)\) supplies no
fractional gap.  Ordinary vertex- and one-edge contraction-criticality do
not repair this: odd cycles have those local criticality properties, but
\(\chi_f(C_{2r+1})=2+1/r<3=\eta(C_{2r+1})\).
They are **not** proper-minor-minimal, since they have a triangle minor;
accordingly this example is only a warning that a proof must use the full
proper-minor transition family, not a counterexample under that full
hypothesis.

Nor is there a useful upper multiplicativity for the Hadwiger number of a
general lexicographic or OR product.  For example,

\[
 K_2[\overline{K_s}]=K_{s,s},
\]

so its Hadwiger number is \(s+1\), while the product of the two factor
Hadwiger numbers is two.  The same example occurs for the disjunctive (OR)
product of \(K_2\) and \(\overline{K_s}\).

## 6. Product audit

The standard operations fail for complementary exact reasons.

| Operation | Colour behaviour | Minor obstruction |
|---|---|---|
| disjoint union | maximum | no amplification |
| Cartesian product | \(\chi(G\square H)=\max\{\chi(G),\chi(H)\}\) | no chromatic amplification |
| categorical product | \(\chi(G\times H)\le\min\{\chi(G),\chi(H)\}\) | no chromatic amplification |
| join | additive | complete multipartite cross-copy models force (1.1) |
| lexicographic product | multichromatic/fractional growth | depth-congestion brambles, with unbounded rounding gap |
| OR product | at most multiplicative | independent fibres already manufacture \(K_{s,s}\) minors |
| universal-clique suspension | exactly additive | exact defect preservation, not amplification |

Therefore a hypothetical one-unit gap cannot be exponentiated by any of
these operations and fed to a known \(O(\eta\log\log\eta)\) bound.

## 7. The materially new target exposed by the audit

A viable amplifier would need both properties below.

1. **Integral palette multiplication.**  Its chromatic number must retain
   the incompatible *integral* colour states of the factors, rather than
   converge to fractional multicolouring.
2. **Minor reflection.**  Every large clique model in the amplified graph
   must project to an ordinary clique model in a factor, rather than to a
   bounded-congestion wiring bramble.

Theorem 4.1 proves that minor reflection cannot follow from congestion,
pairwise touching, planarity, high local density, or a static rooted model.
The only presently available information capable of excluding the wiring
is the all-operations transition family of a contraction-critical graph.

This suggests the following research object, which is narrower than
Hadwiger itself and genuinely different from a static rooted-model
conjecture.

> **Operation-compatible bramble rounding.**  Start with a least-parameter,
> universal-vertex-free contraction-critical graph.  A depth-\(m\) clique
> bramble is operation-compatible if, after every deletion or contraction
> used by criticality, its incidence with the resulting exact colour trace
> admits the corresponding palette exchange.  Prove that a sufficiently
> large operation-compatible bramble contains a depth-one subbramble of the
> required order, or that one transition exposes a colour-gluable adhesion.

The suspension theorem explains the normalization (universal vertices carry
no defect), and the planar wiring theorem supplies the mandatory adversarial
test: a proposed exchange axiom must fail on that static wiring.  Without an
axiom involving several proper-minor colourings simultaneously, the target is
false.

## 8. Bottom line

Product amplification does **not** turn a hypothetical Hadwiger gap into a
contradiction with current asymptotic colouring bounds.  The failure is now
exact rather than heuristic:

* joins dilute the ratio below two;
* clique blow-ups fractionalize colour and lift minors to congestion
  brambles;
* congestion-two brambles have unbounded integrality gap in planar graphs;
* clique suspension preserves a counterexample and all its minor-critical
  dynamics while leaving the defect constant.

The positive reusable outputs are Theorems 2.1, 2.2, and 3.1.  The next
plausible uniform mechanism is not another product, but a multi-operation
rounding theorem on the suspension-prime core.
