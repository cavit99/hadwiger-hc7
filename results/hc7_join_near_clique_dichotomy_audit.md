# Independent audit: the complete-factor join dichotomy

**Verdict:** **GREEN.**  The parameterized theorem and the new colouring
Corollary 2.2 are correct for every integer `r>=0`, including `r=0`, under
the standard conventions that `eta` of the empty graph is zero and that a
`k`-connected graph has more than `k` vertices.  The unchanged verification
script checks only the displayed `r=2` sharpness example; it ran
successfully, and an independent check of the displayed ordered dominating
model and chromatic assertion also passed.

**Audited theorem revision (SHA-256):**

```text
07e449add76ed476514ad0899b04d3c7f0b1eea751918cba7e5a599c8b120b6c  hc7_join_near_clique_dichotomy.md
c8b2bae5e103b010002cc5c69d7d651ea063fb36ca517e0e1294bdcd799aaa0a  hc7_join_near_clique_dichotomy_verify.py
```

## 1. Lemma 1.1

The identity

\[
                  \eta(K_r\vee H)=r+\eta(H)
\]

is valid for every `r>=0`, including `r=0` and an empty factor `H`.
For the reverse inequality, disjointness of the branch sets implies that at
most `r` of them meet the `K_r` factor.  After those branch sets are removed,
all remaining branch sets lie in `H`; their internal connecting edges and
their mutual adjacency edges are therefore edges of `H`, not merely join
edges.  If `s<=r` branch sets were removed, this gives a `K_{t-s}` model in
`H`, and hence a `K_{t-r}` model after discarding surplus branch sets when
`t>r`.  When `t<=r`, the required inequality is immediate.  No branch-set
case is omitted.

## 2. Theorem 2.1

Fix `r>=0`, write `G=K_r\vee F`, and assume that `G` is
`(r+5)`-connected but has no `K_{r+5}` minor.  Lemma 1.1 correctly reduces
this to `F` being `K_5`-minor-free.

Let `R` be the `r`-vertex complete factor.  If a set `Z` of at most four
vertices disconnects `F`, then `R\cup Z` disconnects `G` and has order at
most `r+4`, contrary to `(r+5)`-connectivity.  The order condition in that
definition also gives

\[
               |V(G)|\ge r+6\quad\text{and hence}\quad |V(F)|\ge6.
\]

Thus `F` is genuinely five-connected for every `r`, not merely resistant
to small cuts.  This argument remains exact when `r=0`: then `G=F`, `R` is
empty, and the hypothesis directly says that `F` is five-connected.
Wagner's four-connected form therefore makes `F` planar.

Planarity gives a vertex `v` of degree at most five and five-connectivity
gives degree at least five, so `d_F(v)=5`.  The only remaining minimum-order
case is `|F|=6`; minimum degree five would then make `F=K_6`, contradicting
`K_5`-minor-freeness.  Hence `|F|>=7` and `F-N_F[v]` is nonempty.  The set

\[
                         R\cup N_F(v)
\]

has exactly `r+5` vertices.  Its deletion isolates `v` and leaves at least
one vertex of `F-N_F[v]`, so both open sides are nonempty and the separation
is actual.  This verifies the full range `r>=0` and all small-order cases.

The stated consequences have the correct scope: the theorem eliminates all
complete-factor joins from the parameterized minor-or-exact-separator
counterexample family.  For `r=2` it specializes to the active near-`K_7`
dichotomy, but it never removes the separator alternative.

## 3. Corollary 2.2

Lemma 1.1 gives

\[
 \eta(K_r\vee F)=r+\eta(F).
\]

Consequently, exclusion of a `K_{r+5}` minor from the join implies
`eta(F)<=4`, equivalently that `F` is `K_5`-minor-free.  The established
`t=5` case of Hadwiger's conjecture then supplies a proper four-colouring
of `F`.  Since every complete-factor vertex is adjacent to every vertex of
`F` and to every other complete-factor vertex, assigning those `r`
vertices pairwise distinct colours not used on `F` is a proper
`(r+4)`-colouring.  The argument also covers an empty `F` and `r=0`.

The particular conclusion for `r=2` is therefore exact: every
`K_7`-minor-free graph of the form `K_2\vee F` is six-colourable, without a
connectivity hypothesis.  This corollary uses only Lemma 1.1 and the known
four-colourability of `K_5`-minor-free graphs; it does not depend on the
finite verifier or on the separator theorem.

## 4. Icosahedral sharpness example

Inspection of the seven displayed bags and the independent verifier confirm
that they partition the fourteen vertices, are connected, and have exactly
one nonadjacent pair, namely the singleton bags `{0}` and `{2}`.  Thus this
is a spanning singleton-root `K_7`-minus-one-edge model.

The ordered tuple

```text
({p}, {q}, {1}, {5}, {6})
```

has the claimed dominating-`K_5` semantics: every later singleton is
adjacent to every earlier singleton.  The last three vertices induce the
triangle `1-5-6-1`, so the normalized induced-cycle formulation is also
exact.

The parameterized theorem is proved symbolically above; the accompanying
script is deliberately narrower.  Running

```bash
python3 results/hc7_join_near_clique_dichotomy_verify.py
```

checks the original `r=2` icosahedral example: a spherical triangulation
certificate for the factor, exhaustive resistance to deletion of fewer
than five vertices, seven-connectivity of `K_2\vee I`, all model
adjacencies, and the stated seven-vertex separator.  It completed with:

```text
icosahedral factor: spherical triangulation and 5-connectivity verified
join: 7-connectivity verified
spanning singleton-root K7-minus-one-edge model verified
normalized dominating-cycle substrate verified
actual order-seven separator verified
ALL CHECKS PASSED
```

Separately, exhaustive colouring backtracking found no three-colouring of
the displayed icosahedral graph and produced a four-colouring.  Hence the
factor is four-chromatic and its join with `K_2` is six-chromatic, as
stated.  Planarity excludes a `K_5` minor in the factor, so Lemma 1.1
correctly excludes a `K_7` minor in the join.

## 5. Trust boundary

The example proves that the order-seven alternative cannot be removed from
the `r=2` structural theorem using only the displayed near-clique model and
one normalized dominating model.  The verifier is not computational
evidence for all `r`; the written argument supplies that generality.  The
example is not strongly seven-contraction-critical and therefore does not
test a theorem which additionally uses that global hypothesis.  The source
states this limitation explicitly.
