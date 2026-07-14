# Prescribed portal extension or an exact-seven adhesion

**Status:** proved below; independent audit recorded beside this note.

This note isolates the Hall step needed by a state-preserving rooted-model
handoff.  The tiny-shore outcome is necessary: without it, even a
seven-connected graph may have a singleton full shore.

## 1. Literal setup

Let `G` be a finite seven-connected graph with a literal separation

\[
             V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
             \qquad |S|=7,                              \tag{1.1}
\]

where `L,R` are nonempty, `G[L]` is connected, and there is no `L-R`
edge.  Thus `L` is one component behind the actual boundary `S`.

For `U subseteq S`, write

\[
             N_L(U)=\{x\in L: xu\in E(G)
                         \text{ for some }u\in U\}.      \tag{1.2}
\]

A matching from `A subseteq S` into `L` always means a set of literal
`S-L` edges with pairwise distinct endpoints on both sides.

Seven-connectivity first gives

\[
                         N_G(L)=S.                       \tag{1.3}
\]

Indeed, `N_G(L) subseteq S`; if it had order at most six, deleting it
would separate the nonempty set `L` from the nonempty set `R`.

## 2. The extension-or-adhesion theorem

### Theorem 2.1 (prescribed portal extension)

Let `A subseteq S`, with `1 <= |A| <= 4`, let `s in A`, and prescribe a
literal portal edge `sz` with `z in L`.  Then at least one of the following
holds.

1. **Extension.**  The edge `sz` belongs to a matching from `A` into `L`
   that saturates `A`.
2. **Tiny shore.**  There are a nonempty set `U subseteq A-{s}` and
   `X=N_L(U)` such that
   \[
                    z\in X=L,\qquad |X|=|U|\le 3.        \tag{2.1}
   \]
3. **Exact-seven descent.**  There are a nonempty set
   `U subseteq A-{s}` and `X=N_L(U)` such that
   \[
          z\in X,qquad |X|=|U|\le3,qquad L-X\ne\varnothing. \tag{2.2}
   \]
   For
   \[
                       \Omega=(S-U)\cup X,               \tag{2.3}
   \]
   `Omega` is a literal separator of order seven.  More precisely, every
   component `C` of `G[L-X]` satisfies
   \[
                       N_G(C)=\Omega.                    \tag{2.4}
   \]
   Hence every such `C` is `Omega`-full and
   \[
       V(G)=C\mathbin{\dot\cup}\Omega
                 \mathbin{\dot\cup}\bigl(V(G)-(C\cup\Omega)\bigr) \tag{2.5}
   \]
   is an actual seven-separation whose `C`-side is strictly smaller than
   `L`.

#### Proof

Force `s` to be matched to `z`, and consider the bipartite graph of
literal edges from `A-{s}` to `L-{z}`.  If it has a matching saturating
`A-{s}`, adjoining `sz` gives outcome 1.

Otherwise Hall's theorem supplies a nonempty
`U subseteq A-{s}` with

\[
             |N_{L-{z}}(U)|<|U|.                         \tag{2.6}
\]

Choose `U` inclusion-minimal and put

\[
             Y=N_{L-{z}}(U),\qquad X=N_L(U).             \tag{2.7}
\]

For every `u in U`, minimality says that `U-{u}` satisfies Hall's
inequality.  Therefore

\[
 |U|-1\le |N_{L-{z}}(U-{u})|\le |Y|<|U|,
\]

and consequently

\[
                         |Y|=|U|-1.                      \tag{2.8}
\]

Since the only vertex removed from the right side was `z`,

\[
              X=Y\quad\text{or}\quad X=Y\cup\{z\}.      \tag{2.9}
\]

Also `|U| <= |A|-1 <= 3`.  Equation (1.3) ensures that every member of
`U` has a neighbour in `L`, so `X` is nonempty.

If `L=X`, then `z in X` because `z in L`.  Equations (2.8)--(2.9) give
`|X|=|U|<=3`, which is outcome 2.

Assume now that `L-X` is nonempty and define `Omega` by (2.3).  Let `C`
be any component of `G[L-X]`.  There is no edge from `C` to `R`.  There is
no edge from `C` to a member of `U`, because every `L`-neighbour of `U`
belongs to `X`.  Finally, different components of `G[L-X]` have no edge
between them.  Thus

\[
                       N_G(C)\subseteq\Omega.            \tag{2.10}
\]

The complement of `C union N_G(C)` is nonempty: it contains the original
nonempty shore `R`.  Hence `N_G(C)` is a vertex cut.  Seven-connectivity,
(2.8), and (2.9) now give

\[
  7\le |N_G(C)|\le |\Omega|
       =7-|U|+|X|\le7.                                  \tag{2.11}
\]

Equality holds throughout.  In particular `|X|=|U|`, so (2.8)--(2.9)
force `z in X`; also `|Omega|=7` and (2.10) becomes
`N_G(C)=Omega`.  This proves (2.2)--(2.5).  Since `X` is nonempty, every
component `C` has fewer vertices than `L`.  \(\square\)

### Corollary 2.2 (the live four-connected branch)

Under the hypotheses of Theorem 2.1, assume additionally that `G[L]` is
four-connected.  Then `|L|>=5`, outcome 2 is impossible, and in outcome 3
the graph `G[L-X]` is nonempty and connected.  Thus it is the unique new
`L`-side behind `Omega`, is `Omega`-full, and has strictly fewer vertices
than the old shore.

#### Proof

A four-connected graph has at least five vertices.  Outcome 2 has
`|L|<=3`, so it cannot occur.  In outcome 3, `|X|<=3`; four-connectivity
therefore makes `G[L-X]` connected, and `|L|>=5>|X|` makes it nonempty.
The remaining assertions follow from (2.4).  \(\square\)

## 3. Exact scope

The theorem preserves the prescribed literal edge `sz` in its extension
outcome.  In the descent outcome it gives the explicit boundary map

\[
       S\longmapsto\Omega=(S-U)\cup N_L(U):              \tag{3.1}
\]

the old literals in `U` move to the outer shore, while their equally many
literal `L`-neighbours `X` become the new gates.  Every surviving
`L-X` component meets every literal of this new boundary.

No colouring or equality state is asserted to pull back across (3.1).
That label/state transfer remains a separate obligation.  The tiny-shore
alternative also cannot be deleted without an additional hypothesis.
