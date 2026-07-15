# Global topological-`K_5` pair height

**Status:** proved and independently audited.  The exchange theorem in
Section 5 is open.  This note tests a genuinely graph-global
replacement for the local twin-seam ranks; it is not a proof of `HC_7`.

## 1. Definition

Let `G` be seven-connected.  For a two-vertex set `P`, define

\[
 \theta_G(P)=\min\{|V(T)|:T\subseteq G-P\text{ is a subdivision of }K_5\},
 \tag{1.1}
\]

with value infinity if no such subdivision exists.  Put

\[
                         \Theta_5(G)=\max_{|P|=2}\theta_G(P). \tag{1.2}
\]

Unlike a portal count or a selected model contact profile, `theta_G(P)` is
defined from the whole graph after deleting the literal pair `P`.  Reselecting
the pair can strictly increase it.  Changes of a local adhesion, model, or
colouring while retaining the same pair do not.

## 2. The terminal value is exact

### Proposition 2.1

For every seven-connected graph `G` and every two-set `P`, the following are
equivalent:

1. `theta_G(P)=infinity`;
2. `G-P` is planar;
3. `G-P` is `K_5`-minor-free.

### Proof

Deleting two vertices from a seven-connected graph leaves a five-connected
graph.  A planar graph contains no subdivision of `K_5`, so 2 implies 1.
Conversely, the Kelmans--Seymour theorem says that every five-connected
nonplanar graph contains a subdivision of `K_5`; hence 1 implies 2.

Planarity implies `K_5`-minor-freeness.  Conversely, `G-P` is
five-connected and therefore four-connected.  Wagner's four-connected form
of his theorem says that a four-connected `K_5`-minor-free graph is planar.
Thus 2 and 3 are equivalent.  \(\square\)

Consequently an infinite value is exactly the valid fixed-pair terminal used
throughout the proof spine.  No separate conversion from a topological model
to a minor transversal is needed at the endpoint.

## 3. Application to a hypothetical counterexample

### Proposition 3.1

Let `G` be a hypothetical minor-minimal counterexample to `HC_7`.  Then

1. `theta_G(P)` is finite for every two-set `P`;
2. `Theta_5(G)>=6`; and
3. any pair maximizing `theta_G(P)` is a globally selected witness pair,
   independent of every near model, exact-seven adhesion, or returned
   colouring state.  The maximizing pair need not be unique.

### Proof

For every two-set `P`, deleting its vertices lowers chromatic number by at
most two, so

\[
                         \chi(G-P)\ge5.                 \tag{3.1}
\]

The Four-Colour Theorem implies that `G-P` is nonplanar.  Since it is
five-connected, Kelmans--Seymour supplies a `TK_5`, proving finiteness.

The audited literal-`K_5` transversal theorem supplies a pair `P_0` meeting
every literal `K_5` in the `K_7`-minor-free host `G`.  Thus `G-P_0` has no
five-vertex `TK_5`, because such a subdivision is a literal `K_5`.  It still
has a `TK_5` by the preceding paragraph, so

\[
                         \theta_G(P_0)\ge6.              \tag{3.2}
\]

Taking the maximum proves item 2, while finiteness of the set of pairs proves
item 3.  \(\square\)

## 4. The first finite rung

### Proposition 4.1

Suppose `P` satisfies `theta_G(P)=6`, and let `T` be a six-vertex shortest
`TK_5` in `G-P`.  Then `T` is obtained from a literal `K_5` by subdividing
exactly one edge once.  More explicitly, there are branch vertices

\[
                         a,b,c,d,e
\]

and one internal vertex `w` such that all branch-vertex edges except `ab`
belong to `T`, while `a-w-b` replaces `ab`.

If `P` meets every literal `K_5`, viewing `aw` as the two-vertex bag
(equivalently, contracting it to expose the corresponding literal `K_5` in
the proper minor) gives the support-six normal form of the global contraction
dichotomy with

\[
 D_a=\{b\},\qquad
 \varnothing\ne D_w\subseteq\{c,d,e\}.                 \tag{4.1}
\]

Hence, up to orientation, its deficiency triple is one of

\[
                         (1,1,2),\quad(1,2,1),\quad(1,3,0), \tag{4.2}
\]

and the `(2,2,0)` split cannot be the displayed shortest topological rung.

### Proof

A subdivision of `K_5` has five branch vertices.  With six vertices total,
exactly one of its ten branch-to-branch paths has one internal vertex and all
other paths are edges.  This gives the displayed labelling.

Because `G-P` contains no literal `K_5`, the chord `ab` is absent.  Use
`{a,w}` as the two-vertex bag, with singleton clique
`Q={b,c,d,e}`.  The vertex `a` misses exactly `b` inside `Q`, while `w` is
adjacent to `b`.  Thus `D_a={b}` and `D_w` is contained in `{c,d,e}`.  If
`D_w` were empty, `Q union {w}` would be a literal `K_5` disjoint from `P`.
So `1<=|D_w|<=3`, giving exactly (4.2).  \(\square\)

This is a real global normalization: the selected pair and the shortest
topological obstruction are carried together.  It does not close any of the
three cases in (4.2).

## 5. The missing monotone exchange

The theorem which would turn (1.1) into a proof engine is:

> **Topological pair-exchange target.**  Let `P` maximize `theta_G(P)` in a
> hypothetical minimal `HC_7` counterexample, and let `T` be a shortest
> `TK_5` in `G-P`.  Then a proper-minor response and a label-faithful
> rerouting of `T` produce a literal `K_7`, an infinite-value pair, or a pair
> `P'` with
> \[
>                         \theta_G(P')>\theta_G(P).       \tag{5.1}
> \]

At a maximizing pair the last alternative is impossible, and the first two
are terminal.  Thus this target is `HC_7`-strength and is **not proved** by
the definition of `theta`.

The advantage over `h_5(G)` is operational rather than logical.  A shortest
`TK_5` has ten literal segments and a bridge structure on which shortening,
stable-bridge rerouting, and pair exchange can be stated.  By contrast,
`h_5(G)` is constant under every within-`G` local move and records no carrier
geometry.  The advantage over `mu(P)` is that infinity is still the exact
terminal, while the finite witness is a labelled path system rather than an
arbitrary collection of branch bags.

The limitations are equally important.

* A neutral rerouting to another shortest `TK_5` does not increase (1.1).
  Such reroutings must be quotiented or shown to expose one coherent pair.
* A small `K_5` minor need not contain a `TK_5` on the same support.  Although
  `mu(P)<=theta(P)` whenever both are finite, a lower bound on `theta(P)`
  therefore gives no corresponding lower bound on the minor-model parameter
  `mu(P)`.
* Kelmans--Seymour supplies existence, not the pair-exchange (5.1).
* No local twin-seam receiver is admissible here unless it specifies the new
  literal pair `P'` and proves that **every** smaller `TK_5` avoids it.

Accordingly the immediate proof test is the first-rung version of (5.1),
starting from (4.2).  If the proper-minor colouring data cannot be coupled to
the selected pair and shortest subdivision, this potential must be demoted
rather than supplemented by more local gate cases.

## 6. Literature boundary

The terminal equivalence uses the Kelmans--Seymour theorem, proved by
Dawei He, Yan Wang and Xingxing Yu in the four-paper series culminating in
*The Kelmans--Seymour conjecture IV: A proof*, Journal of Combinatorial
Theory, Series B 144 (2020), 309--358; preprint
<https://arxiv.org/abs/1612.07189>.

The elementary observation that a five-connected graph containing a literal
`K_4` has a `TK_5` also appears at the start of Jie Ma and Xingxing Yu,
*K_5-subdivisions in graphs containing `K_4^-`*, Journal of Combinatorial
Theory, Series B 103 (2013), 713--732.  Neither source supplies a
two-vertex pair exchange or preserves contraction-critical colouring states.
