# Robust independent-triple concentration at a bounded interface

**Status:** written proof; separate internal audit **GREEN** in
[`hc7_bounded_interface_robust_triple_response_audit.md`](hc7_bounded_interface_robust_triple_response_audit.md).
This is a nonterminal strengthening of the audited exact-block Kempe reduction.  It
does not put two responses in one colouring, make their paths internally
disjoint, produce a `K_6` boundary model, synchronize the two closed shores,
or give a strict same-form restart.

## 1. Setup

Let `G` be a hypothetical minor-minimal counterexample to `HC_7`.  Thus
`G` is seven-connected and seven-chromatic, has no `K_7` minor, and every
proper minor of `G` is six-colourable.  Let `u` be a vertex with

\[
                         7\le d_G(u)\le9,
\]

let `C` be a component of `G-N[u]`, and put

\[
 S=N_G(C)\subseteq N(u),\qquad
 A=G[C\cup S],\qquad B=G-C .                            \tag{1.1}
\]

Assume the bounded-interface conclusions already proved in
[`hc7_bounded_interface_exact_block_kempe_reduction.md`](hc7_bounded_interface_exact_block_kempe_reduction.md):

\[
                         7\le |S|\le d_G(u)\le9,         \tag{1.2}
\]

and the contraction-critical neighbourhood bound

\[
 \alpha(G[S])\le \alpha(G[N(u)])
                    \le d_G(u)-5\le4.                  \tag{1.3}
\]

For every nonempty independent set `I` of `G[S]`, each closed shore
has a proper six-colouring in which `I` is exactly one boundary colour
class.  Any two such labelled boundary colourings which give `I` the same
colour name are joined by boundary Kempe interchanges which never use that
colour.  Equivalently, arbitrary endpoints may first be globally relabelled
to align the colour on `I`.  In particular, every such `I` satisfies
`|S-I|\ge |S|-4\ge3`.

## 2. A pole-free response for every independent block

### Theorem 2.1 (independent-block response)

For every nonempty independent set `I` of `G[S]`, there are a nonedge

\[
                         f_I\in\binom{S-I}{2}             \tag{2.1}
\]

of `G[S]` and an `f_I`-path `P_I` such that

1. no internal vertex of `P_I` belongs to `S\cup\{u\}`; and
2. all internal vertices of `P_I` lie either in `C` or in
   `B-(S\cup\{u\})`.

The colouring, Kempe sequence, path, endpoint pair, and open shore may
depend on `I`.

### Proof

Contract the connected star on `\{u\}\cup I` to one vertex `w`.  Six-colour
the resulting proper minor.  Expanding `w` gives a proper six-colouring
`phi` of

\[
                     G-E_I,\qquad E_I=\{ui:i\in I\},     \tag{2.2}
\]

in which `u` and every vertex of `I` have one colour, say `gamma`.
Expansion is proper because `I` is independent and precisely the edges in
`E_I` were removed.  Since `u` is adjacent to every vertex of `S-I`, the
set `I` is exactly the `gamma`-class on `S`.

Choose a proper six-colouring `psi` of the original closed shore `B` in
which `I` is an exact boundary colour class, and rename colours so that
this class also has colour `gamma`.  Exact-block cylinder connectivity
gives a boundary Kempe sequence from `phi|S` to `psi|S` which never uses
`gamma`.

Starting with `phi`, try to lift this sequence in `G-E_I`.  A boundary
interchange lifts unless a full two-colour component meeting the selected
boundary component also meets another boundary component.  At the first
failure, a shortest path in such a full component between the two boundary
components has no internal vertex in `S`.  It avoids `u` and `I`, because
their fixed colour `gamma` is absent from every interchange.

If every interchange lifted, the resulting colouring restricted to `A`
would be a proper colouring of the original graph `A`: none of the deleted
edges `E_I` lies in `A`.  Its boundary colouring would be `psi|S`, so it
could be glued to `psi` on the original graph `B`, producing a proper
six-colouring of `G`.  This is impossible.  A failed lift therefore exists.

There is no edge between `C` and `B-S`.  Hence the internal vertices of
the shortest failed-lift path lie wholly in one of the two open shores;
avoidance of `u` gives the stated localization on the `B`-side.  Both ends
avoid `I`.  They lie in distinct two-colour components of `G[S]`, so they
are nonadjacent in `G[S]`.  Their pair is the required `f_I`.  \(\square\)

## 3. Robust singleton families have one global triple

For `x\in S`, let `\mathcal E_x` be the set of all endpoint pairs returned
by Theorem 2.1 with `I=\{x\}`, ranging over every permitted minor colouring,
exact-singleton target colouring, Kempe sequence, and first failed lift.
Every `\mathcal E_x` is nonempty, and

\[
 e\subseteq S-\{x\},\qquad e\notin E(G[S])
                 \quad(e\in\mathcal E_x).               \tag{3.1}
\]

### Theorem 3.1 (globalization of robust concentration)

Assume the literal robust failure of disjoint endpoint selection:

\[
 \begin{split}
 &\text{for all distinct }x,y\in S,\text{ all }e\in\mathcal E_x,
   \text{ and all }f\in\mathcal E_y,\\
 &\hspace{42mm}e\cap f\ne\varnothing .                 \tag{3.2}
 \end{split}
\]

Then there is one independent set `Q\subseteq S` of order three such that

\[
       \mathcal E_x\subseteq\binom Q2\quad(x\in S),
       \qquad \mathcal E_q=\{Q-\{q\}\}\quad(q\in Q).  \tag{3.3}
\]

### Proof

Choose one baseline pair `e_x\in\mathcal E_x` for every `x\in S`.  By
(3.2), these two-sets are pairwise intersecting.  They include at least two
distinct sets: if their only value were `\{a,b\}`, then `e_a` would contain
its forbidden root `a`, contrary to (3.1).

A pairwise-intersecting family of two-sets with at least two distinct
members is contained either in a star or in the three edges of a triangle.
The star alternative is impossible, because the pair selected for its
centre would contain its own root.  Thus all baseline pairs lie in
`\binom Q2` for a three-set `Q`.  For `q\in Q`, avoidance in (3.1) forces

\[
                             e_q=Q-\{q\}.                \tag{3.4}
\]

All three pairs in (3.4) are nonedges of `G[S]`, so `Q` is independent.

Now fix `x\in S` and replace only the baseline pair `e_x` by an arbitrary
pair `e\in\mathcal E_x`.  Condition (3.2) again makes the resulting
selection pairwise intersecting, so the preceding argument puts it in the
edges of some three-set `Q'`.  If `x\notin Q`, the unchanged pairs indexed
by the three members of `Q` are all three edges of `Q`, forcing `Q'=Q`.
If `x\in Q`, the two unchanged pairs indexed by `Q-\{x\}` already have
union `Q`, again forcing `Q'=Q`.  Hence every `e\in\mathcal E_x` belongs
to `\binom Q2`.  For `x=q\in Q`, (3.1) leaves only `Q-\{q\}`, proving
(3.3).  \(\square\)

## 4. The exact-`Q` response leaves the triple

### Corollary 4.1

Under the hypotheses of Theorem 3.1, there is a boundary nonedge

\[
                         f_Q\in\binom{S-Q}{2}            \tag{4.1}
\]

and a corresponding path `P_Q` satisfying Theorem 2.1.  In particular,

\[
                  f_Q\cap e=\varnothing
       \quad\text{for every }x\in S\text{ and }e\in\mathcal E_x. \tag{4.2}
\]

### Proof

The set `Q` is nonempty and independent, so apply Theorem 2.1 with `I=Q`.
It returns (4.1).  Theorem 3.1 puts every singleton endpoint pair inside
`Q`, which proves (4.2).  \(\square\)

Applying Theorem 2.1 instead with `I=Q-\{q\}` similarly gives, for each
`q\in Q`, a path whose endpoint pair is disjoint from the forced singleton
pair `Q-\{q\}`.

## 5. Exact trust boundary

The quantifier in (3.2) is essential.  Three selected witnesses with pairs
`Q-\{q\}` may come from three unrelated colourings and do not control any
other attainable witness.  Theorem 3.1 globalizes only because one
arbitrary witness can be substituted while all other baseline choices are
held fixed.

Corollary 4.1 gives disjoint **terminal pairs**, not internally disjoint
paths.  A singleton path and `P_Q` may lie in the same open shore and may
have arbitrary internal intersection.  Even when they lie in opposite
open shores, replacing their endpoint pairs by edges proves a `K_7` minor
only after a separately justified labelled minor construction, such as a
`K_6` model in the appropriately augmented boundary.  No such boundary
model follows here.

Nor does the argument produce a common equality partition.  Its paths are
obtained from different exact-block cylinders and generally from different
proper-minor colourings.  Finally, cutting `C` around intersecting paths can
introduce boundary vertices inside `C`, which need not be adjacent to `u`.
Seven-connectivity only lower-bounds the resulting neighbourhood; it does
not give a boundary of order at most nine, preserve the named aligned
vertex, or decrease the order of a component of `G-N[u]`.  Thus no strict
same-form restart is asserted.
