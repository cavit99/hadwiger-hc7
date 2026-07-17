# A reachability-maximal normal form for the two-edge Kempe fork

**Status:** written proof, independently audited in
[`hc7_reachability_maximal_kempe_normal_form_audit.md`](hc7_reachability_maximal_kempe_normal_form_audit.md).
This is a uniform colouring lemma.  It supplies a genuinely well-founded
reachability measure for one cyclic orientation, but it does not by itself
construct a clique minor or eliminate the balanced order-eight case.

## 1. Setup

Let `q>=3`, let `G` be a graph which is not `q`-colourable, and let

\[
                         e=ab,\qquad f=cd
\]

be vertex-disjoint edges.  Put `H=G-{e,f}`.  Fix a three-element set of
colours `Omega` and a cyclic permutation `sigma` of `Omega`.  Let `R` be a
set of vertices and fix a colouring `rho` of `R` using no colour of
`Omega`.

Let `mathcal E` be the family of proper `q`-colourings `kappa` of `H` such
that:

1. `kappa|_R=rho`;
2. `kappa(a)=kappa(b)` is a colour in `Omega`; and
3. `kappa(c)=kappa(d)`.

Assume `mathcal E` is nonempty.  For `kappa in mathcal E`, orient every
edge of `H[kappa^{-1}(Omega)]` from `u` to `v` when

\[
                         \kappa(v)=\sigma(\kappa(u)).  \tag{1.1}
\]

Because `sigma` is a three-cycle and `kappa` is proper, this orients every
edge of the induced three-colour graph in exactly one direction.  Denote
the resulting digraph by `D_kappa`, and let `F_kappa` be the set reachable
from `a` in `D_kappa`.

## 2. Reachability-maximal normal form

### Theorem 2.1

Choose `kappa in mathcal E` so that `|F_kappa|` is maximum.  Then at least
one of the following holds.

1. Rotating the colours on `F_kappa` by `sigma` gives a proper
   `q`-colouring of `G-f`; in its restriction to `H`, the ends of `e` are
   different and the ends of `f` remain equal.
2. Rotating the colours on `F_kappa` by `sigma` gives a proper
   `q`-colouring of `G-e`; in its restriction to `H`, the ends of `e`
   remain equal and the ends of `f` are different.
3. The vertex `b` belongs to `F_kappa`, and `F_kappa` is exactly the
   connected component of `H[kappa^{-1}(Omega)]` containing `a`.  In
   particular, `a` reaches every vertex of that whole three-colour
   component in the cyclic orientation.

#### Proof

Rotate by `sigma` the colour of every vertex in `F_kappa`, and call the
resulting colouring `kappa'`.  The reachable-set argument in the
generalized two-edge Kempe fork shows that `kappa'` is proper on `H`.
The set `R` is unchanged because its colours lie outside `Omega`.

Suppose first that `b` does not belong to `F_kappa`.  Exactly one end of
`e` is rotated, so `e` becomes proper.  If `f` also became proper,
`kappa'` would extend to a `q`-colouring of all of `G`, contrary to the
hypothesis.  Hence the ends of `f` remain equal, giving outcome 1.

Now suppose that `b` belongs to `F_kappa`.  Both ends of `e` are rotated
by the same permutation and remain equal.  If the ends of `f` become
different, outcome 2 holds.  We may therefore suppose that they remain
equal.  Then `kappa'` again belongs to `mathcal E`.

Every directed path from `a` to a vertex of `F_kappa` lies wholly in
`F_kappa`.  Applying the same permutation to all its vertex colours
preserves every orientation in (1.1).  Hence, in `D_{kappa'}`, the vertex
`a` still reaches every vertex of `F_kappa`.

Suppose an edge `uv` of the induced three-colour graph has
`u in F_kappa` and `v notin F_kappa`.  It cannot be oriented from `u` to
`v` under `kappa`, since then `v` would be reachable.  It is therefore
oriented from `v` to `u`, so

\[
                         \kappa(u)=\sigma(\kappa(v)).   \tag{2.1}
\]

After rotating the colour of `u`,

\[
 \kappa'(u)=\sigma^2(\kappa(v)),\qquad
 \kappa'(v)=\kappa(v).
\]

Since `sigma` has order three, the same edge is now oriented from `u` to
`v`.  Thus `a` reaches `v` under `kappa'`.  Consequently any edge of the
three-colour graph crossing from `F_kappa` to its complement would give

\[
                         |F_{\kappa'}|>|F_\kappa|,
\]

contrary to the maximal choice of `kappa` in `mathcal E`.

There is therefore no such crossing edge.  The set `F_kappa` is connected
in the underlying graph, contains `a`, and is a union of connected
components of the induced three-colour graph.  It must be exactly the
component containing `a`.  It also contains `b`, proving outcome 3.
\(\square\)

### Corollary 2.2 (the mutual-lock branch is a source component)

In outcome 3, suppose in addition that `H` has a directed `a-b` path for
the reverse cyclic order `sigma^{-1}` under the same colouring `kappa`.
Then `a,b` lie in one strongly connected component of `D_kappa`.  That
strong component is the unique source component in the condensation of
the connected three-colour component `F_kappa`.

#### Proof

A directed `a-b` path for `sigma^{-1}`, read backwards, is a directed
`b-a` path for `sigma`.  Outcome 3 already gives a directed `a-b` path,
so `a,b` lie in one strongly connected component `Z`.

Moreover `a` reaches every vertex of `F_kappa`, so `Z` reaches every
component of the condensation.  No different strong component can reach
`Z`, since that would make it mutually reachable with `Z`.  Hence `Z` is
a source, and it is the unique source because it reaches every other
component.  \(\square\)

## 3. Balanced order-eight specialization and trust boundary

In the balanced order-eight configuration, take

\[
                   e=\ell_e\ell_f
\]

and let `R` be the reserved triangle of the original five-clique.  In an
`(equal,equal)` colouring of the two-edge-deletion host, the three colours
on `R` are distinct.  The complementary three-colour set `Omega` consists
of the common colour on `ell_e,ell_f` and the two colours absent from that
five-clique.  Hence the hypotheses involving `R` are preserved by every
rotation in Theorem 2.1.

The theorem gives a finite, strictly increasing process for either cyclic
orientation: unless a one-edge response is produced, each nonterminal
rotation strictly enlarges the reachable set until the whole relevant
three-colour component is reached.  This replaces an unranked sequence of
path choices by the global integer `|F_kappa|`.

It does not finish the required branch-set composition.  The strengthened
canonical-web counterexample in
[`../barriers/hc7_balanced_order8_two_missing_colour_paths.md`](../barriers/hc7_balanced_order8_two_missing_colour_paths.md)
has an exact simultaneous-equality colouring in which the entire
three-colour component containing the two clique vertices is already
strongly connected, while the rooted linkage is still absent.  That
example is only five-connected and six-colourable and uses contracted
defect vertices.  Thus a positive completion theorem must still use the
literal endpoint distribution together with seven-connectivity or the
incompatibility of proper-minor response traces.
