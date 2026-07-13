# Adaptive flag choice: the exact matching-linkage quantifier gap

## Status

This note records the strongest uniform adaptive statement currently proved
from colourfulness and exact independent traces.  For every **fixed**
matching of palette colours, one can choose a rainbow boundary transversal
and mutually disjoint Kempe connectors for that matching.  Applied at a
private-colour descent, the transversal can be required to contain the
current distinguished root.

The choices need not be coherent for different matchings or different
levels of an elimination flag.  The full exact-trace counterexample in
`hadwiger_colourful_elimination_flag_counterexample.md` shows that a
preselected flag can fail this coherence, uniformly in every order
`k>=4`.  It does not refute the genuinely adaptive assertion that *some*
flag always works.

## 1. Definitions

Let `H` be `k`-colourable and let \(X\subseteq V(H)\) be `k`-colourful.
Say that `(H,X)` has the **full independent-trace property** if, for every
nonempty independent set \(S\subseteq X\), there is a proper `k`-colouring
`c` and a colour `alpha` such that

\[
                       c^{-1}(\alpha)\cap X=S.          \tag{1.1}
\]

Distinct terminals `(r_1,...,r_k)` are **matching-linked** if, for every
matching `M` on a subset of `[k]`, there are pairwise vertex-disjoint
paths joining `r_i` to `r_j` for `ij in M`, with every path avoiding all
terminals other than its own ends.

## 2. Exact independent traces are automatic in critical graphs

### Lemma 2.1

If `H` is `k`-vertex-critical, then `(H,V(H))` has the full
independent-trace property.

#### Proof

Let `S` be a nonempty independent set and choose `s in S`.  Since `H` is
vertex-critical, `H-s` is `(k-1)`-colourable, and therefore so is the
induced subgraph `H-S`.  Colour `H-S` with `k-1` colours and give every
vertex of `S` one new colour.  Independence of `S` makes this proper, and
the new colour class is exactly `S`.  \(\square\)

Consequently the full independent-trace property, by itself, is not extra
structure beyond the usual minimal-counterexample reduction.  Any uniform
rooted theorem based only on this property must cope with every
vertex-critical graph.

## 3. A fixed matching can always be routed adaptively

### Theorem 3.1 (matching-by-matching Kempe transversal)

Let `X` be `k`-colourful in `H`, and fix a proper `k`-colouring `c` with
colour classes `C_1,...,C_k`.  For every matching `M` on a subset of
`[k]`, there are vertices

\[
                    r_i\in X\cap C_i\qquad(1\le i\le k) \tag{3.1}
\]

and, for every `ij in M`, an `r_i`--`r_j` path `P_{ij}` in
\(H[C_i\cup C_j]\), such that the paths `P_{ij}` are pairwise
vertex-disjoint and avoid all selected roots other than their own ends.

#### Proof

Fix `ij in M`.  We first show that some component of
\(H[C_i\cup C_j]\) meets both \(X\cap C_i\) and \(X\cap C_j\).

Otherwise switch colours `i,j` in every bichromatic component which
meets \(X\cap C_i\).  All vertices of `X` formerly coloured `i` change to
`j`.  By the supposition, none of the switched components contains a
vertex of `X` formerly coloured `j`, so no vertex of `X` acquires colour
`i`.  The resulting proper `k`-colouring omits colour `i` on `X`,
contrary to colourfulness.

Choose such a component, choose one boundary vertex of each of its two
colours, and join them by a path in the component.  Do this independently
for every edge of `M`.  Distinct edges of a matching use disjoint pairs
of colour classes, so their bichromatic induced subgraphs, and hence the
chosen paths, are vertex-disjoint.  For every unmatched colour choose an
arbitrary vertex of \(X\cap C_i\), which is nonempty by colourfulness.
No chosen path can contain a selected root of a third colour.  \(\square\)

### Corollary 3.2 (the exact local statement at every flag level)

At level `i` of a colourful elimination flag, let `c_i` be the selected
private-colour colouring and let `x_i` be its distinguished root.  For
every matching of the `i` palette colours, Theorem 3.1 gives a rainbow
transversal of `X_i` and disjoint Kempe connectors for that matching; the
transversal can always be chosen to contain `x_i`.

Indeed, the private colour has trace `{x_i}` on `X_i`.  If it is matched,
the endpoint selected in its colour class is forced to be `x_i`; if it is
unmatched, select `x_i` as its arbitrary representative.

This corollary uses the complete private-colour state at each descent, not
merely abstract pairwise connectivity.  It is nevertheless only a local,
matching-by-matching assertion.

### Corollary 3.3 (use of a prescribed independent trace)

If `(H,X)` has the full independent-trace property, then for every
nonempty independent \(S\subseteq X\) and every palette matching `M`, one
may first choose a colouring satisfying (1.1) and then apply Theorem 3.1.
The resulting transversal has its representative of the trace colour in
`S`, and it routes all pairs of `M` disjointly.

### Lemma 3.4 (private-neighbourhood descent)

Let `c` be a proper `k`-colouring of `H`, let `A` be a colour class of
`c`, and suppose

\[
                         A\cap X=\{x\}.                 \tag{3.2}
\]

Put `H'=H-A` and `Y=N_H(x)` (which is automatically contained in
`V(H')`).  Then `Y` is `(k-1)`-colourful in `H'`.

#### Proof

Use on `H'` the palette obtained by deleting the colour of `A`.  Suppose
a proper colouring `phi` from this palette omitted a colour `gamma` on
`Y`.  Colour every vertex of `A-{x}` with the deleted colour, colour `x`
with `gamma`, and use `phi` on `H'`.

The set `A` is independent.  The neighbours of `x` avoid `gamma` by
assumption, while every external neighbour of `A-{x}` avoids the deleted
colour because that colour is absent from the palette of `phi`.  Hence
this is a proper `k`-colouring of `H`.  But the deleted colour is absent
from `X`, by (3.2), contradicting the colourfulness of `X`.  \(\square\)

Thus one private descent produces two simultaneous `(k-1)`-colourful
sets in `H'`:

\[
                         X-\{x\},\qquad N_H(x).          \tag{3.3}
\]

The first retains the old boundary and supports a nested flag.  The
second is adjacent to the new root and supports the usual Strong-Hadwiger
induction.  The missing compatibility is to package or transport these
two colourful boundaries simultaneously.  Their intersection need not be
colourful; if it were colourful at every descent, the selected roots
would form an actual clique, which is impossible already in triangle-free
four-chromatic graphs.

Lemma 3.4 also makes the theorem-strength boundary transparent: Strong
Hadwiger at parameter `k-1`, applied to the colourful set `N_H(x)` in
`H'`, gives a rooted `K_{k-1}`-model all of whose bags are adjacent to the
singleton `{x}`, and hence an ordinary `K_k`-minor.  What is absent is a
weaker, provable two-boundary packaging theorem with a usable separator
alternative.

### Proposition 3.5 (universal realization of the two residual boundaries)

Let `J` be `q`-colourable and let \(P,Q\subseteq V(J)\) both be
`q`-colourful.  There is a `(q+1)`-colourable graph `H`, a
`(q+1)`-colourful set `X`, a vertex \(x\in X\), and a colour class `A`
such that

\[
 A\cap X=\{x\},\qquad H-A=J,\qquad X-\{x\}=P,
 \qquad N_H(x)=Q.                                      \tag{3.4}
\]

If `P` is inclusion-minimal `q`-colourful, then `X` is inclusion-minimal
`(q+1)`-colourful.

#### Proof

Add two nonadjacent vertices `b,x` to `J`.  Make `b` complete to `J`,
and give `x` precisely the neighbourhood `Q`.  Put

\[
                              X=P\cup\{x\}.             \tag{3.5}
\]

Colour `J` with `q` colours and give `b,x` one new colour.  This is a
proper `(q+1)`-colouring, and its new colour class is
`A={b,x}`, which gives (3.4).

In any proper `(q+1)`-colouring of `H`, the colour on `b` is absent from
`J`.  The graph `J` is `q`-chromatic because it has a `q`-colourful set,
so it uses all other `q` colours.  Both `P` and `Q` see all of them.
The vertex `x`, which is complete to `Q`, must therefore receive the
colour of `b`.  Hence `X` sees all `q+1` colours in every colouring and
is colourful.

If `P` is inclusion-minimal, then for each \(p\in P\) there is a
`q`-colouring of `J` omitting a colour on `P-{p}`.  Extend it by giving
`b,x` a new colour; the same colour is omitted on `X-{p}`.  Also the
displayed canonical colouring omits the new colour on `X-{x}=P`.
Thus `X` is inclusion-minimal.  \(\square\)

This proposition shows that the simultaneous colourfulness of the two
sets in (3.3), and their origin in one private-colour descent, impose no
restriction on the abstract pair `(J;P,Q)`.  A useful two-boundary theorem
must additionally use the full trace family, ambient minor transitions,
or separator geometry.

The construction does not in general preserve the full independent-
trace property on `X`: if \(p\in P-Q\), then `{x,p}` is independent, while
the forcing vertex `b` makes `x` use the unique colour absent from `J` in
every `(q+1)`-colouring.  This identifies exactly where the all-trace
hypothesis may still contribute beyond bare two-boundary colourfulness.

## 4. Why this does not yet give one adaptive flag

Theorem 3.1 has the quantifier order

\[
       \forall c\ \forall M\ \exists R(c,M)\ \exists\mathcal P(c,M),
                                                        \tag{4.1}
\]

where `R` is the selected transversal and \(\mathcal P\) the linkage.  A
single matching-linked flag would require

\[
       \exists\text{ one nested flag with roots }R\quad
       \forall M\ \exists\mathcal P_M.                 \tag{4.2}
\]

There are two independent coherence demands in (4.2).

1. The representative chosen in a bichromatic component must be the
   distinguished root which survives all later private-colour descents.
2. The same root set must work for all matchings simultaneously.

Neither follows by interchanging the quantifiers in (4.1).  In
particular, the endpoint supplied by a Kempe component at level `i` need
not belong to the later minimal colourful set `X_{i-1}`, exactly as noted
in the original elimination-flag construction.

## 5. Exact-trace falsification boundary

The seven-vertex graph in
`hadwiger_colourful_elimination_flag_counterexample.md` is
four-vertex-critical.  By Lemma 2.1 it realizes every independent exact
trace.  Nevertheless it has a full flag with roots `(5,4,0,1)` which is
not matching-linked: the matching `{{0,1},{4,5}}` requires two paths both
forced through vertex `3`.

Joining this graph with `K_{k-4}` gives the same phenomenon for every
`k>=4`, while preserving vertex-criticality and hence every independent
trace.  Therefore

> full independent traces do not make an arbitrarily selected nested
> flag matching-linked.

The same graph also has a different valid flag, with roots `(1,5,6,0)`,
which is the root set of an explicit `K_4`-model.  Thus it does **not**
refute the adaptive existential statement (4.2).

## 6. Computation used only as falsification

The scripts

* `experiments/search_colourful_flags.py`, and
* `experiments/search_adaptive_exact_trace.py`

exhaustively tested all graphs in the NetworkX atlas (at most seven
vertices), and all eight isomorphism classes of four-vertex-critical
graphs on eight vertices generated by one-vertex extension.  No instance
was found in which every legal elimination flag failed matching-linkage.

This is evidence for formulating (4.2), not a proof of it.  The
computation did find the smaller, quantifier-sharp bad flag recorded in
Section 5; every fact used from that example now has a hand proof.

## 7. The strongest live adaptive target

The surviving statement is:

> **Adaptive matching-linked flag conjecture.**  If `(H,X)` is
> `k`-colourful and has the full independent-trace property, with `X`
> inclusion-minimal colourful, then some colourful elimination flag
> starting at `(H,X)` has matching-linked distinguished roots.

This is strictly weaker in its conclusion than flag-packaging: a
matching-linked terminal set need not be the root set of a clique model.
It is also the strongest form supported by the small exhaustive audit.

No proof is installed.  Lemma 2.1 shows why it is still theorem-strength:
on `X=V(H)` it applies to every vertex-critical graph.  A proof must use a
new coherent-selection or separator-exchange mechanism, not merely repeat
the exact traces.  The precise next dichotomy is:

\[
 \boxed{\text{coherent root selection for all matchings}}
 \quad\text{or}\quad
 \boxed{\text{a labelled capacity cut permitting recolouring/gluing}}.
                                                        \tag{7.1}
\]
