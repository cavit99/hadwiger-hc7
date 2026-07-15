# Atomic literal two-gate normal form

**Status:** proved and independently audited.

## 1. Setup

Use the connected-bipartite atomic exact-seven interface

\[
 V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad S=W\mathbin{\dot\cup}\{u\},\qquad |S|=7,
\]

where `G` is seven-connected, strongly seven-contraction-critical and
`K_7`-minor-free, there is no `A-R` edge, `A` is two-connected and
`S`-full, `zu` is the unique `A-u` edge, `H=G[S]` is connected and
bipartite, and `R` contains two disjoint connected `S`-full packets.

Let `Z={p,q}` be a vertex cut of `G[A]`.

## 2. Literal two-gate normal form

### Theorem 2.1

At least one of the following holds.

1. `G` is six-colourable by the unordered asymmetric `(5,6)` carrier
   theorem.
2. The graph `A-Z` has exactly two components `D,E`, with `z in E`, and,
   writing

   \[
              T_D=N_S(D),\qquad T_E=N_S(E),
   \]

   one has

   \[
       |T_D|=|T_E|=5,\qquad
       T_D\cup T_E=S,\qquad |T_D\cap T_E|=3,             \tag{2.1}
   \]

   and

   \[
                  N_S(p)\cup N_S(q)\subseteq T_D\cap T_E. \tag{2.2}
   \]

   In particular `u in T_E-T_D`, and both

   \[
       \Omega_D=Z\mathbin{\dot\cup}T_D=N_G(D),
       \qquad
       \Omega_E=Z\mathbin{\dot\cup}T_E=N_G(E)             \tag{2.3}
   \]

   are literal order-seven receiver boundaries.

Thus every literal two-gate leaves the rural geometry either terminally or
through a **twin exact-seven seam**.  Outcome 2 is not asserted to be an
accepted recursive `S3/S4` state.

### Proof

Every component `C` of `A-Z` has a neighbour at both `p` and `q`.
Otherwise one member of `Z` would separate `C` from the other components,
contrary to two-connectivity of `A`.  Since `R` is nonempty and there is no
`A-R` edge, the literal set

\[
                         Z\cup N_S(C)=N_G(C)
\]

separates `C` from `R`.  Seven-connectivity therefore gives

\[
                         |N_S(C)|\ge5.                    \tag{2.4}
\]

Let the components be `C_1,...,C_k`.  For every nonempty proper index set
`I`, put

\[
 X=\{p\}\cup\bigcup_{i\in I}C_i,
 \qquad
 Y=\{q\}\cup\bigcup_{i\notin I}C_i.                    \tag{2.5}
\]

Both sets are connected and adjacent, cover `A`, and each contains a
component with support at least five.  Interchanging `p,q` gives a second
legal allocation for the same component split.  Whichever carrier contains
the compulsory root may be named `Y`; the unordered `(5,6)` theorem closes
as soon as either support in (2.5) has order at least six.

Assume no allocation closes.  Every support in every allocation therefore
has order exactly five.  A singleton choice `I={i}`, used with both gate
allocations, gives

\[
        |N_S(C_i)|=5,
        \qquad N_S(p)\cup N_S(q)\subseteq N_S(C_i).      \tag{2.6}
\]

If `k>=3`, applying (2.5) to a two-component proper subfamily forces the
two corresponding five-sets to be equal.  Varying the subfamily shows that
all component supports equal one five-set `T`; (2.6) then puts both gate
supports in `T`.  This contradicts `S`-fullness of `A`.  Hence `k=2`.

Name the off-frame component `D` and the other component `E`.  Formula
(2.6) gives the two support sizes and puts both gate supports in their
intersection.  Fullness now gives `T_D union T_E=S`, and two five-subsets
of a seven-set with union seven have intersection three.  This proves
(2.1)--(2.2).

The root `z` cannot belong to `Z`: otherwise its literal neighbour `u`
would lie in both component supports by (2.2), whereas uniqueness of `zu`
prevents either component from meeting `u`.  Thus `z in E`, after naming
`D` as the off-frame component, and uniqueness gives `u in T_E-T_D`.

Finally, the definition of the two components and the absence of `A-R`
edges give (2.3).  Each boundary has order seven, separates its component
from the other component and the old rich shore, and is therefore an actual
receiver boundary.  This proves outcome 2.  \(\square\)

## 3. Receiver boundary

For either `Omega_C`, choose an edge from `C` to its gate and contract it
toward the literal gate label.  A six-colouring of that proper minor
returns an exact state on the boundary, intact on the opposite closed
shore.  Exact packet reflection proves that its demand exceeds the packet
number of that opposite shore.

Every component of `G-Omega_C` is `Omega_C`-full, so the exact-seven packet
theorem recognizes the new vector as `(1,1)`, `(1,2)` or `(1,3)`, up to
orientation.  The `(1,3)` vector is terminal by audited adaptive reflection.
In a `(1,2)` vector, contracting a boundary edge on the actual packet-one
shore regenerates a state of demand at least three on the packet-two closed
shore.  The `(1,1)` vector retains a named state and packet-sum drop, but no
well-founded `S4` rank is known.

Consequently Theorem 2.1 removes all unbounded **two-gate geometry** and
leaves one exact twin-state composition problem.  It does not solve that
composition problem.  Old `S`-full packets are not automatically full to a
new boundary, because the boundary contains the two literal gate vertices
in `A`.
