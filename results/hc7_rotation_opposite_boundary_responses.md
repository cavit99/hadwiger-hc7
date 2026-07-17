# Oppositely oriented boundary-colouring responses at a connected-subgraph rotation

**Status:** written proof; separate internal audit GREEN.

This note strengthens the colouring part of the connected
one-missing-adjacency trichotomy.  Every near-complete minor model returned
by its mutually unavoidable-vertex branch has a unique donor-side
attachment vertex between the transferred subgraph and the residual
deficient branch set.  A critical edge through that attachment and a
contact edge to any newly missed branch
set lie on opposite closed sides of one actual separation.  Their
six-colouring response languages are therefore oppositely oriented on the
same literal boundary.

The theorem does **not** force those two response languages to intersect.
It isolates that intersection as the exact remaining colouring implication
at one reversible rotation.

## 1. Setup from the connected-subgraph trichotomy

Let `G` be a graph which is not six-colourable and for which every proper
minor is six-colourable.  Let

\[
                         A,R,F_1,\ldots,F_5                         \tag{1.1}
\]

be pairwise disjoint nonempty connected vertex sets such that

1. `R,F_1,...,F_5` form a `K_6`-minor model;
2. `A` is anticomplete to `R` and adjacent to every `F_i`; and
3. `N_G(A)\subseteq F_1\cup\cdots\cup F_5`.

Fix one donor `U=F_i`.  Suppose that the mutually unavoidable-vertex
branch of the proof of the connected one-missing-adjacency trichotomy has
selected distinct vertices

\[
                         r,s\in U\cap N_G(A),                       \tag{1.2}
\]

and has defined `W` to be the component of `G[U-s]` containing `r` and

\[
                              Z=U-W.                                \tag{1.3}
\]

Thus `Z` and `W` are nonempty connected adjacent sets and `s\in Z`.
Use as the five fixed branch sets

\[
                 \mathcal F=\{R\}\cup\{F_j:j\ne i\}.              \tag{1.4}
\]

For `H\in\mathcal F`, put `P_H=N_U(H)`.  Assume, as in the
near-complete-model outcome of that trichotomy, that `Z` is adjacent to
`R` and that

\[
 \Omega=\{H\in\mathcal F:P_H\subseteq Z\}                         \tag{1.5}
\]

is nonempty.  In the trichotomy one also has `|\Omega|\le2`, but the
colouring conclusion below does not need that upper bound.  The seven
sets

\[
                 W,\quad A\cup Z,\quad \mathcal F                  \tag{1.6}
\]

then form a labelled near-`K_7` model whose only possibly missing
adjacencies are from `W` to the members of `\Omega`.

For a graph `Q` containing a labelled vertex set `S`, write
`Ext(Q,S)` for the equality partitions of `S` induced by proper
six-colourings of `Q`.

## 2. The one-vertex donor interface and the actual separation

### Lemma 2.1 (the transferred subgraph has one donor-side attachment)

One has

\[
                              N_U(W)=\{s\}.                         \tag{2.1}
\]

Moreover, `s` has a neighbour in `A`, `W` has a neighbour in `A`, and
`s` has a neighbour `w\in W`.

#### Proof

The set `W` is a component of `G[U-s]`.  Hence no vertex of another
component of `G[U-s]` is adjacent to `W`, and every edge from `W` to
`U-W=Z` has its end in `Z` equal to `s`.  Since `G[U]` is connected,
there is at least one such edge.  This proves (2.1) and permits the choice
of `w`.

Both `r` and `s` belong to `N_G(A)` by (1.2).  Since `r\in W` and
`s\in Z`, this gives the two asserted contacts with `A`.  \(\square\)

Put

\[
       S=N_G(W),\qquad C=G[W\cup S],\qquad O=G-W.                  \tag{2.2}
\]

### Lemma 2.2 (location of the two critical edges)

The pair `(C,O)` is an actual separation with intersection `S` and two
nonempty open sides.  The edge `sw` belongs to `C` and has its other end
`w` in the open `W`-side.

For every `H\in\Omega`, choose an edge

\[
                              t_Hf_H                                \tag{2.3}
\]

with `t_H\in Z` and `f_H\in H`.  Such an edge exists.  It belongs to
`O`, does not belong to `C`, and `f_H` lies in the open side
`V(G)-(W\cup S)`.

#### Proof

Because `H\in\Omega`, every `U-H` contact has its `U`-end in `Z`.
The old `K_6` model makes `U` adjacent to `H`, so (2.3) exists.  The
definition of `\Omega` also says that `W` is anticomplete to `H`.
Consequently every vertex of `H`, including `f_H`, is outside
`W\cup S`.

The open side `W` is nonempty, and `f_H` proves that the opposite open
side is nonempty.  Thus (2.2) is an actual separation.  Lemma 2.1 gives
the edge `sw` with `s\in S` and `w\in W`.

Both ends of (2.3) lie outside `W`, so that edge belongs to `O`.  Its end
`f_H` is outside `W\cup S`, so the edge is not an edge of the induced
subgraph `C`, regardless of whether `t_H=s` or `t_H\notin S`.
\(\square\)

The last sentence includes the only two possibilities for `t_H` inside
`Z`: by (2.1), a vertex of `Z` belongs to `S=N_G(W)` exactly when it is
`s`.

## 3. Oppositely oriented equality-partition responses

For an edge `e`, let `Resp(e,S)` be the set of equality partitions of
`S` induced by proper six-colourings of `G-e`.  Edge deletion is a proper
minor operation here, so every displayed response set is nonempty.
If `e` has one end in `S`, retain the contracted image of that end as the
same labelled boundary vertex; neither displayed edge has both ends in
`S`.

### Theorem 3.1 (opposite-side response theorem)

With the notation above,

\[
 \begin{aligned}
   Resp(sw,S)&\subseteq Ext(O,S)\setminus Ext(C,S),\\
   Resp(t_Hf_H,S)&\subseteq Ext(C,S)\setminus Ext(O,S)
                       \qquad(H\in\Omega).                       \tag{3.1}
 \end{aligned}
\]

In addition, in every six-colouring of either edge-deleted graph the ends
of the deleted edge have the same colour.  Consequently `Resp(e,S)` is
also exactly the equality-partition language induced on `S` by proper
six-colourings of `G/e`, with the preceding boundary-label convention, for
each displayed edge

\[
                         e\in\{sw,t_Hf_H:H\in\Omega\}.              \tag{3.2}
\]

#### Proof

Take a six-colouring `c` of `G-sw`, and let `Pi` be its equality
partition on `S`.  The graph `O` does not contain `w`, so its edge set is
unchanged when `sw` is deleted.  Hence `c|_O` is a proper six-colouring
and `Pi\in Ext(O,S)`.

If `Pi` also belonged to `Ext(C,S)`, choose a six-colouring of `C`
inducing `Pi`.  Permute its six colour names so that it agrees literally
with `c|_O` at every vertex of `S`.  The two colourings would then glue
to a proper six-colouring of `G`, contrary to the hypothesis.  Therefore
`Pi\notin Ext(C,S)`, proving the first inclusion.

Now take a six-colouring `d` of `G-t_Hf_H`, with boundary partition
`Sigma`.  Lemma 2.2 says that `t_Hf_H` is not an edge of `C`, so `C` is
unchanged by this deletion.  Thus `d|_C` is proper and
`Sigma\in Ext(C,S)`.  If `Sigma\in Ext(O,S)`, align a corresponding
colouring of `O` with `d|_C` on `S` and glue.  This again six-colours
`G`, so `Sigma\notin Ext(O,S)`.  The second inclusion follows.

Finally, if the ends of either deleted edge received different colours,
restoring that edge in the same colouring would give a proper
six-colouring of `G`.  They must therefore receive one common colour.
Colourings of `G-e` in which the two ends of `e` have a common colour are
in canonical bijection with colourings of `G/e`: identify the two ends in
one direction, and assign the contracted image's colour to both ends in
the other.  At most one end of each displayed edge lies in `S`, by Lemma
2.2, so this bijection preserves every literal boundary label under the
stated convention.  This proves (3.2).
\(\square\)

### Corollary 3.2 (a response collision is terminal)

For every `H\in\Omega`,

\[
                         Resp(sw,S)\cap Resp(t_Hf_H,S)=\varnothing. \tag{3.3}
\]

Equivalently, if proper-minor arguments force one equality partition of
`S` to occur in both response languages, then `G` is six-colourable.

#### Proof

The two sets in (3.1) lie in opposite set differences.  Alternatively,
colour `C` using the `t_Hf_H` response and `O` using the `sw` response,
align their common equality partition by a permutation of the six
colours, and glue.  \(\square\)

### Corollary 3.3 (five colour-restricted connections on both sides)

Fix a six-colouring of either `G-sw` or `G-t_Hf_H`, and call the common
endpoint colour `0`.  For every other colour `j`, the two ends of the
deleted edge lie in the same component of the subgraph induced by colours
`0,j`.

For `sw`, traversing such a path from `w` to its first vertex outside
`W` produces a path whose internal vertices lie in `W` and whose other
end is a literal vertex of `S`.  Thus each partition in `Resp(sw,S)` comes
with five colour-distinguished entrances into the `W`-side.

#### Proof

If the two ends lay in different `0,j` components, interchange colours
`0,j` on the component containing one end.  The deleted edge would then
have differently coloured ends and could be restored, six-colouring `G`.
The entrance assertion follows by stopping the resulting `s-w` path at
its first vertex outside `W`.  \(\square\)

## 4. Exact consequence for the active exchange problem

The connected-subgraph trichotomy did not previously attach compulsory
colouring data to its reversible near-complete-model outcome.  Lemmas
2.1--2.2 and Theorem 3.1 show that every such outcome carries, on one
literal boundary `S=N_G(W)`, two nonempty and oppositely oriented families
of equality partitions:

* the response to the donor-interface edge `sw` on the `W`-closed side;
  and
* for each newly missed labelled branch set `H`, the response to a named
  contact edge `t_Hf_H` on the opposite closed side.

This is label-faithful: the second edge has one endpoint in the precise
fixed branch set whose adjacency was lost in the rotation.  It is also
host-level: no auxiliary quotient edge or recolouring label is used.

What remains unproved is an intersection theorem for these two response
languages, or a replacement conclusion producing an explicit `K_7`-minor
model, an exact order-seven separation with a common boundary partition,
or a new full valid defect-one configuration with a smaller lifted
simplicial component.  Reversibility of the branch-set rotation alone
does not force (3.3) to fail.

## 5. Dependencies

- [connected one-missing-adjacency trichotomy](../results/hc7_connected_one_hole_trichotomy.md)
- [critical shared-pinch boundary state](../results/hc7_near_k7_critical_pinch_state.md)
- [exact reversibility of a connected-subgraph rotation](../results/hc7_near_k7_rotation_edge.md)
