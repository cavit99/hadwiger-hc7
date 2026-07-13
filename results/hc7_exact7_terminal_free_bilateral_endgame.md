# Terminal-free bilateral planar endgame

**Status:** proved and independently audited.  This replaces the
stronger fixed-`{v,w}` two-apex target inside the exact Moser cell.  The
side terminals do not need to be reinserted into either disk page.

## 1. Exact cell

Use the notation of
`../results/hc7_exact7_moser_order6_decorated_exchange.md`:

\[
 a=1,\qquad b=3,\qquad U=\{0,2,4,5,6\}.
\]

The exact cell has two anticomplete open shores `D_a,D_b`, and all vertices
of `G` are accounted for by

\[
 V(G)=D_a\mathbin{\dot\cup}D_b\mathbin{\dot\cup}
       U\mathbin{\dot\cup}\{v,w,a,b\}.                         \tag{1.1}
\]

Put

\[
 J_a^\circ=G[D_a\cup U],\qquad
 J_b^\circ=G[D_b\cup U].                                      \tag{1.2}
\]

The graph `G[U]` is the literal five-cycle common to the two shores.

## 2. Colouring endgame

### Theorem 2.1 (two terminal-free disk pages six-colour `G`)

Suppose each `J_t^circ`, for `t in {a,b}`, has a plane embedding in a
closed disk whose boundary meets the graph exactly in the same literal
cycle `G[U]`.  Then `G` is six-colourable.

#### Proof

Draw `J_a^circ` inside the cycle `G[U]` and, after reflection if needed,
draw `J_b^circ` outside it.  The two drawings agree on their literal common
cycle, and the exact shores are anticomplete.  Hence their union is a plane
drawing of

\[
                         G-\{v,w,a,b\}.                          \tag{2.1}
\]

By the Four Colour Theorem, colour (2.1) with colours `1,2,3,4`.

The Moser boundary has `ab notin E(G)`.  The audited exact-cell portal
lemma gives

\[
                         wa,wb\notin E(G).                       \tag{2.2}
\]

Thus `{a,b,w}` is an independent set.  Give all three vertices colour `5`
and give `v` colour `6`.  Every edge from those four deleted vertices to
the planar core has differently coloured ends; the only edges internal to
the four-vertex set which can occur are incident with `v`, whose colour is
different from colour `5`.  This is a proper six-colouring of `G`.
\(\square\)

## 3. Exact consequence for the rural spine

After the terminal-free state-or-rural normalization and low-cut descent,
the rural branch needs only the following statement on each side:

> expand the two connected poles of the planar quotient to a disk embedding
> of the whole graph `J_t^circ` with boundary `G[U]`, or turn a pole-society
> obstruction into a literal `K_7`, a common attained state, or another
> direct six-colouring.

No embedding of the side terminal `t` is required.  The three vertices
`a,b,w` form one new colour class globally, so the former side-terminal
reinsertion obligation was stronger than the colouring argument needs.
