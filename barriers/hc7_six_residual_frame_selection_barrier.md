# Equal-extremum normalized frames can have opposite edge strata

**Status:** barrier/counterexample to an intermediate frame-selection
claim. The example is seven-vertex-critical and eight-connected, but it
has a `K_7` minor and is not strongly seven-contraction-critical. It does
not refute closure under the full hypothetical-counterexample assumptions.

## 1. Claim refuted

The following rule is false under chromatic criticality and high
connectivity alone:

> For a six-residual edge `e`, choose a normalized dominating `K_5` frame
> in `G-V(e)` with minimum total branch-set order and then a shortest
> terminal cycle. Every such frame has a six-residual terminal edge.

Thus model size and cycle length cannot replace global minor exclusion.

## 2. Construction and edge strata

Let

\[
                         G=K_1\vee C_5\vee C_5.
\]

Write `h` for the `K_1` vertex and the cycles as
`a_0a_1a_2a_3a_4a_0` and `b_0b_1b_2b_3b_4b_0`.

The join formula gives `chi(G)=1+3+3=7`. Deleting any vertex lowers the
chromatic number to six, so `G` is seven-vertex-critical. Every cycle
vertex has degree eight. Removing at most seven vertices leaves two
nonempty join factors, hence a connected graph, unless only one cycle
factor remains; then at most one of its vertices was removed. Thus `G` is
eight-connected.

Deleting the ends of a cycle edge leaves a three-vertex path in that
factor, so the remaining chromatic number is `1+2+3=6`. All ten cycle
edges are six-residual. Deleting the ends of an edge between two join
factors lowers the chromatic number of each affected critical factor by
one, giving five. All join edges are double-critical.

## 3. Equally extremal frames

Take `e=a_0a_1`. In `G-{a_0,a_1}`,

\[
 (\{a_3\},\{b_1\},\{a_2\},\{h\},\{b_0\})                 \tag{3.1}
\]

is a normalized all-singleton dominating `K_5` model. Its terminal
triangle `a_2hb_0a_2` consists entirely of join edges and is therefore
all double-critical.

In the same host,

\[
 (\{a_3\},\{h\},\{a_2\},\{b_0\},\{b_1\})                \tag{3.2}
\]

is another normalized all-singleton frame. Its terminal triangle contains
the six-residual edge `b_0b_1`.

Both models have the minimum possible support order five and both terminal
cycles have the minimum possible length three. The selection rule cannot
distinguish them.

## 4. Scope

The clique number is `1+2+2=5`, so (3.1) does not expose a `K_7`
subgraph. Each `C_5` nevertheless contracts to a `K_3`; those two
triangle models plus `{h}` form an explicit `K_7`-minor model. Hence `G`
is not strongly seven-contraction-critical: it has a proper
seven-chromatic minor.

The example therefore does not refute a proof using the full hypotheses.
It shows exactly that minimum support and shortest-cycle extremization
cannot perform the existential reselection; a valid proof must use global
minor geometry or a stronger label-preserving invariant.
