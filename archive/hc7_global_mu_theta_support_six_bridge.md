# Bridging the global minor-support and topological pair heights

**Status:** proved elementary global normalization; independent audit
pending.  It does not increase either height and is not a proof of `HC_7`.

## 1. The bridge theorem

Let `G` be a hypothetical minor-minimal counterexample to `HC_7`.  For a
two-set `P`, let

\[
 \mu(P)=\min\{|V(\mathcal M)|:\mathcal M\text{ is a }K_5
              \text{-model in }G-P\}
\]

and let

\[
 \theta(P)=\min\{|V(T)|:T\subseteq G-P\text{ is a subdivision of }K_5\}.
\]

Both values are finite in the hypothetical counterexample.  Suppose

\[
                         \max_{|P|=2}\mu(P)=6.             \tag{1.1}
\]

Choose a pair `R` maximizing `theta(R)`.  Then exactly one of the following
normalizations applies.

1. **Topological rung.**  `theta(R)=6`.  A shortest obstruction is a
   literal `K_5` with one edge subdivided once.  As a support-six model its
   deficiency type is one of

   \[
                         (1,1,2),\quad(1,2,1),\quad(1,3,0).
   \]
2. **Symmetric non-topological rung.**  `theta(R)>=7`, `mu(R)=6`, and
   every support-six `K_5` model in `G-R` has deficiency type

   \[
                              (2,2,0).                    \tag{1.2}
   \]

In particular, the four support-six normal forms never need to be attacked
simultaneously at a graph-global extremum.  Either literal path geometry is
available, or every minimum model has the unique symmetric form which is
not a six-vertex `TK_5`.

### Proof

Every subdivision of `K_5` is a `K_5` minor model on the same support, so

\[
                              \mu(P)\le\theta(P)           \tag{1.3}
\]

for every pair.  The audited literal-`K_5` transversal theorem and the
audited topological-height theorem give `theta(R)>=6`.

If equality holds, the audited six-vertex topological normal form gives
outcome 1.

Suppose, therefore, that `theta(R)>=7`.  Equation (1.1) gives
`mu(R)<=6`.  The value cannot be five, because a support-five `K_5` model
is a literal `K_5`, hence a five-vertex `TK_5`, contradicting
`theta(R)>=7`.  Thus `mu(R)=6`.

Take any support-six model in `G-R`.  Its bag sizes are
`(2,1,1,1,1)`.  Write the edge-bag as `xy` and the singleton clique as
`Q`.  If one endpoint, say `x`, contacted all of `Q`, then
`Q union {x}` would be a literal `K_5`, again contradicting
`theta(R)>=7`.  Hence the two deficiency sets `D_x,D_y` are nonempty;
they are disjoint because the edge-bag contacts every singleton row.

If one deficiency set were a singleton, say `D_x={q}`, then the five
branch vertices `x` and the four vertices of `Q`, together with `y` as the
sole internal vertex on the path `x-y-q`, would form a subdivision of
`K_5` on these six vertices.  This contradicts `theta(R)>=7`.  Therefore
both deficiency sets have order at least two.  They are disjoint subsets
of the four-set `Q`, so both have order exactly two and exhaust `Q`.  This
is (1.2).  Since the selected support-six model was arbitrary, every such
model has that type. \(\square\)

## 2. Exact use in the proof spine

Outcome 1 should be coupled to stable-bridge or segment rerouting of one
globally shortest `TK_5`; neutral reroutings still require a class-level
rank.  Outcome 2 should be coupled to the stateful contraction pullback:
the split edge has two complementary two-element deficiency rows, and any
small model which disappears under its contraction must use the split
endpoints in distinct named rows.

The theorem does not assert that either branch closes.  Its value is that
the topological and minor-support approaches are complementary rather than
competing: raising the topological height past six forces the one support
shape which topological rerouting cannot see.
