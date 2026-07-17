# An exact list-colouring obstruction on a contracted path

**Status:** written proof; separate internal audit GREEN.  The theorem is
uniform in the chromatic number.  Its `HC_7` corollary supplies a new
minor-critical invariant on every shortest colour-matched repair path, but
does not by itself produce a clique minor.

## 1. General theorem

### Theorem 1.1

Let `k>=3`, let `G` be a `k`-chromatic graph whose every proper minor is
`(k-1)`-colourable, and let

\[
                         P=v_1v_2\cdots v_n           \tag{1.1}
\]

be a proper induced path with at least one edge.  Contract all of `P` to
one vertex `p`, fix a proper `(k-1)`-colouring `psi` of `G/P`, and rename
the colours so that `psi(p)=0`.  For every `v in V(P)`, define

\[
 L(v)=[k-1]\setminus
       \psi\bigl(N_G(v)-V(P)\bigr).                   \tag{1.2}
\]

Here `[k-1]` denotes the colour set and contains `0`.

Then `P` has a subpath

\[
                         v_aP v_b                     \tag{1.3}
\]

of odd edge-length with the following exact list pattern:

1. `L(v_a)=L(v_b)={0}`;
2. the internal vertices occur in consecutive pairs; and
3. for each such pair there is a nonzero colour `c_i` for which both
   vertices of the pair have list `{0,c_i}`.

Consequently, both ends of (1.3) have neighbours of every nonzero colour
outside `P`.  Each internal pair has outside neighbours of every nonzero
colour except its associated `c_i`.

### Proof

Every neighbour outside `P` of any vertex of `P` becomes a neighbour of
the contracted vertex `p`.  Hence colour `0` is absent from all the sets
in (1.2), and

\[
                            0\in L(v_i)               \tag{1.4}
\]

for every `i`.

The path `P` has no proper colouring from these lists.  Otherwise, combine
such a list-colouring with `psi` restricted to `G-V(P)`.  Equation (1.2)
prevents conflicts across the boundary of `P`, and the assumption that
`P` is induced means that the path edges are all the constraints internal
to `P`.  This would give a `(k-1)`-colouring of `G`, a contradiction.

For `1<=i<=n`, let `S_i` be the set of colours which can occur on `v_i`
in a proper list-colouring of the prefix `v_1Pv_i`.  Thus

\[
 S_1=L(v_1),
 \qquad
 S_i=\{c\in L(v_i):S_{i-1}-\{c\}\ne\varnothing\}.    \tag{1.5}
\]

Let `b` be the least index for which `S_b` is empty.  Such an index exists
because the whole path is not list-colourable, while `b>=2` by (1.4).
The recurrence (1.5) and (1.4) imply

\[
                         S_{b-1}=L(v_b)=\{0\}.         \tag{1.6}
\]

Indeed, if `S_{b-1}` contained two colours, every member of `L(v_b)` would
have a different predecessor colour.  If `S_{b-1}={c}`, then failure says
`L(v_b)={c}`; (1.4) forces `c=0`.

Let `a<b` be the largest index with `L(v_a)={0}`.  Such an index exists:
tracing the singleton set `S_{b-1}={0}` backwards through (1.5) must
eventually reach either `S_1=L(v_1)={0}` or an earlier singleton list
`{0}`.  By minimality of `b`, one has `S_a={0}`.

No `S_i` with `a<i<b` can have two or more colours.  Once a set in the
recurrence has at least two colours, the next set equals its whole
nonempty list; in the absence of another singleton list `{0}`, the
recurrence cannot later return to the singleton `{0}` required by (1.6).
Thus all the intervening `S_i` are singletons.

Starting with `S_a={0}`, recurrence (1.5) now forces the lists in pairs.
If `S_{i-1}={0}`, the only way to obtain another singleton without a list
`{0}` is

\[
                  L(v_i)=\{0,c\},\qquad S_i=\{c\}
\]

for some nonzero `c`.  From `S_i={c}`, the only way for the next set to be
a singleton and eventually return to `{0}` is

\[
                  L(v_{i+1})=\{0,c\},\qquad
                  S_{i+1}=\{0\}.
\]

Iterating gives consecutive equal-list pairs between `v_a` and `v_b`.
Their number of internal vertices is even, so `v_aPv_b` has odd
edge-length.  The endpoint lists are `{0}` by the definitions of `a,b`.

Finally, (1.2) translates a list `{0}` into the presence of every nonzero
colour on the outside neighbourhood, and a list `{0,c_i}` into the
presence of every nonzero colour except `c_i`.  This proves the theorem.
\(\square\)

## 2. Application to the `HC_7` repair path

### Corollary 2.1

In the unique-deficiency star--Kempe setup, choose a colour-matched repair
path `P` lexicographically by

1. the number of vertices it uses from `X union D_1 union D_2 union D_3`;
2. its length.

Then `P` is induced.  Contracting it and applying Theorem 1.1 with `k=7`
gives an odd subpath whose two ends each see all five nonzero contraction
colours outside `P`, and whose internal vertices have the paired list
pattern of Theorem 1.1.  One end of this subpath lies in the original
colour class `A` and the other in `V_gamma`.

#### Proof

A chord of `P` would shortcut a subpath.  The shortcut remains in the
induced two-colour graph and, because `P` has no internal vertex in
`C union T`, remains an admissible colour-matched repair path.  It either
uses fewer protected vertices or uses the same protected vertices and is
shorter, contradicting the lexicographic choice.  Thus `P` is induced,
and Theorem 1.1 applies.

The original path alternates between `A` and `V_gamma`.  The locked
subpath has odd edge-length, so its ends lie in opposite sides of this
bipartition.  \(\square\)

## 3. Exact scope

The theorem replaces an arbitrary failure to expand a contraction
colouring across the repair path by a canonical finite word of lists.  In
the `HC_7` application, its two saturated endpoints each have outside
neighbours in all five remaining contraction colours.

Those five colours are not yet identified with the five protected
minor-model branch sets.  The remaining problem is a label-preserving
one: either align the five saturated colour contacts with the five
required branch-set adjacencies, or show that failure yields one of the
actual separators in the exchange-or-separator theorem with compatible
boundary colourings.

## 4. Dependencies

- [colour-matched repair path](../results/hc7_colour_matched_repair_path.md)
- [path exchange or actual separation](hc7_colour_matched_path_exchange_or_separator.md)
