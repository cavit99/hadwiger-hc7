# Independent audit: deficient component of a contact-maximal rooted `K_4` model

**Audited file:**
[`hc7_maximal_rooted_k4_deficient_component_separator.md`](hc7_maximal_rooted_k4_deficient_component_separator.md)

**Audited source SHA-256:**
`fe5bff7d881faeda5c259750e8f634d8b0f59892cf76dd461e40489d26629c59`

**Verdict:** **GREEN.**

The maximality augmentation, the definition and use of `C_j`, the exact
full-neighbourhood identity, both open sides of the resulting separation,
the seven-connectivity bound, and the proper-minor colouring observation are
all correct.  No repair to the source is required.

This is a deductive audit; no finite computation is used as evidence.

The independent audit was performed on source hash
`bcaf984721fda69022094a6cb0799ef6636566a8d9147de2e72521d17d78b70e`.
The only subsequent source change replaced the status phrase “separate
internal audit pending” by “separate internal audit GREEN”; the theorem,
proof, quotient observation, and scope are unchanged.

## 1. Maximal rooted model and the component `C_j`

The source conditionally starts with an `S`-rooted `K_4`-minor model in the
finite graph `R`.  Hence a model maximizing the integer score `tau` exists.
The four branch sets are pairwise disjoint, and

\[
                         U_j=\bigcup_{i\ne j}D_i
\]

is disjoint from the whole branch set `D_j`.

Because `D_j` is connected, all its vertices lie in one component of
`R-U_j`.  Thus the phrase “the component `C_j` containing `D_j`” is
well-defined and means

\[
                              D_j\subseteq C_j,
\]

not merely that `C_j` meets `D_j`.  This full containment is exactly what
the augmentation and the later `z`-contact require.

## 2. Augmentation and maximality

Suppose `t in C_j cap T`.  Connectedness of `C_j` gives a path in `C_j`
from a vertex of `D_j` to `t`.  Replacing `D_j` by its union with the path
preserves every branch-set requirement:

- the enlarged set is connected;
- it remains disjoint from `D_i` for `i != j`, since all added vertices lie
  in the component `C_j subseteq R-U_j`;
- it retains every old adjacency to those three branch sets;
- it retains its original vertex in `S`; and
- it now contains `t in T`.

No other branch set changes.  Since the original `D_j` was `T`-deficient,
the score `tau` increases by exactly one, contradicting maximality.  Hence
`C_j cap T` is empty.  The argument does not require the augmenting path to
avoid `D_j` internally; taking its union with `D_j` is sufficient.

## 3. Boundary inside `R`

Since `C_j` is a component of `R-U_j`, a neighbour of `C_j` in `R` that
does not belong to `U_j` would lie in `R-U_j` and join the same component.
Therefore

\[
                              N_R(C_j)\subseteq U_j.
\]

This is a literal vertex-neighbourhood statement.  It does not claim that
all three other branch sets meet the boundary, and no such stronger fact is
used.

## 4. Exact full neighbourhood and the opposite side

The vertex partition and the definition `R=Q-{z,u}` give

\[
                  V(G)=X\mathbin{\dot\cup}V(R)
                         \mathbin{\dot\cup}\{z,u\}.
\]

Every neighbour of `C_j` must consequently lie in `R`, in `X`, or be one
of the two displayed vertices.  Each part is determined exactly:

- the neighbours in `R` are `N_R(C_j)`;
- the neighbours in `X` are `N_X(C_j)` by definition;
- `z` is a neighbour because the entire `S`-rooted branch set
  `D_j subseteq C_j` meets `S=N_R(z)`; and
- `u` is not a neighbour because `C_j cap T` is empty and
  `T=N_R(u)`.

The four ambient vertex classes are disjoint, so this proves the exact
disjoint union

\[
       N_G(C_j)=N_R(C_j)\mathbin{\dot\cup}N_X(C_j)
                    \mathbin{\dot\cup}\{z\}.
\]

In particular, the source does not omit an unclassified `Q`-neighbour and
does not accidentally include `u` in the boundary.

With

\[
       A=C_j\cup N_G(C_j),\qquad B=V(G)-C_j,
\]

one has `A union B=V(G)`, `A cap B=N_G(C_j)`, and no edge joins
`A-B=C_j` to `B-A=V(G)-(C_j union N_G(C_j))`.  The first open side is
nonempty because it contains `D_j`.  The second is nonempty because it
contains `u`, which lies outside `C_j` and is not adjacent to it.  This is
therefore an actual graph separation.

Seven-connectivity gives

\[
                         |N_G(C_j)|\ge 7.
\]

Substitution of the disjoint boundary identity yields (2.2).  Equality
makes the displayed separation an actual order-seven separation; no upper
bound follows, exactly as the source warns.

## 5. Proper-minor colouring record

Under the additional star-Kempe host hypotheses, `X` consists of two
nonempty colour classes and is connected, so contracting it to `x` is a
nontrivial minor operation.  Contracting the four connected branch sets and
deleting the unused vertices of `R` gives the seven retained vertices

\[
                       x,z,u,d_1,d_2,d_3,d_4.
\]

The six vertices `x,z,d_1,...,d_4` form a `K_6`:

- the four `d_i` are pairwise adjacent by the original `K_4` model;
- `z` is adjacent to each `d_i` because every `D_i` meets `S`;
- domination of `Q` by `X` makes `x` adjacent to `z` and to every `d_i`.

The vertex `u` is adjacent to `x` by domination, to `z` through the edge
`zu`, and to `d_i` exactly when `D_i` meets `T=N_R(u)`.  A proper
six-colouring gives the displayed `K_6` six distinct colours, so `u` must
repeat the colour of one of its nonneighbours among the `d_i`, precisely a
`T`-deficient branch set.

Finally, `N_R(C_j) subseteq U_j` means its vertices contract to at most the
three labels `d_i` with `i != j`; all vertices of `N_X(C_j)` contract to
`x`, and the remaining boundary label is `z`.  The quotient therefore
forgets boundary multiplicities exactly as claimed and cannot supply an
upper bound on the literal separator order.

## 6. Scope

The result assumes the existence of an `S`-rooted `K_4` model and then
chooses one maximizing `T`-contact; it does not prove that rooted model's
existence in the abstract setup.  It returns a separator only when the
maximizing model still has a `T`-deficient branch set.  It does not prove
order seven, a compatible colouring across the separation, a simultaneously
`S,T`-rooted `K_4` model, or a `K_7` minor.  These limitations are stated
consistently in the source.
