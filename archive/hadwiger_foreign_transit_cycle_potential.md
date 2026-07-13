# Foreign-transit cycles: the exact lexicographic termination lemma

## 1. Scope

This note isolates what can, and what cannot, be obtained from the binary
transition-tree theorem by choosing a spanning, contact-maximal clique
model with inclusion-minimal bags.

There is a genuine finite potential.  It rules out every directed cycle
of **safe lobe transfers**.  Consequently a cycle of named foreign-bag
transits must expose either a multiply owned lobe or a contact-protected
lobe.  This is the precise positive dependency-cycle lemma.

The last section gives an explicit two-complex-bag counterarchitecture.
It is spanning, contact-maximal, has inclusion-minimal bags, has a directed
two-cycle of foreign transits, and is `K_7`-minor-free.  Thus foreign
transits themselves cannot be treated as model moves.  The extra owner or
minor-transition data are indispensable.

## 2. Lexicographically minimal contact models

Fix a vertex `v`, put `H=G-v`, and let

\[
                 \mathcal B=(B_1,\ldots,B_r)                 \tag{2.1}
\]

be a labelled spanning `K_r`-model in `H`.  A bag is contacted when it
meets `N_G(v)`.  First maximize the number of contacted bags.  Among all
spanning labelled models attaining that maximum, fix one minimizing

\[
                 (|B_1|,|B_2|,\ldots,|B_r|)                 \tag{2.2}
\]

lexicographically.  The order of the labels is fixed before making this
choice.

For `i\ne j`, an **admissible lobe transfer from `i` to `j`** consists of
a nonempty set `C\subsetneq B_i` such that

1. `H[C]` and `H[B_i-C]` are connected;
2. `C` is adjacent to `B_j`;
3. `B_i-C` is adjacent to every `B_k`, `k\notin\{i,j\}`; and
4. replacing
   \[
      B_i\longmapsto B_i-C,\qquad B_j\longmapsto B_j\cup C \tag{2.3}
   \]
   does not decrease the number of contacted bags.

The edge between `C` and `B_i-C` makes the two new bags adjacent.  Thus
(2.3) is a labelled spanning `K_r`-model.

### Theorem 2.1 (safe-transfer cycles are impossible)

In the model chosen above, the directed graph whose arcs are admissible
lobe transfers is acyclic.

#### Proof

Suppose it contains a directed cycle and let `i` be the least label on
that cycle.  Its outgoing arc has the form `i\to j` with `j>i`.  Apply
the corresponding transfer (2.3).  It preserves spanning, the clique
model, and does not decrease contact.  Maximality of the original contact
count forces equality.  All coordinates before `i` in
(2.2) are unchanged, while the `i`-th coordinate strictly decreases.
This contradicts the choice of the model.  \(\square\)

The proof uses no summation potential and hence is insensitive to the
relative sizes of the two bags.  This is why the labelled lexicographic
potential, rather than `sum |B_i|^2`, is the correct finite potential.

## 3. The exact blocker exposed by a foreign transit

Let `T_i` be a spanning tree of `H[B_i]`, let `e` be an edge of `T_i`,
and let `C` be one component of `T_i-e`.  Then `B_i-C` is connected.
Define the owner set

\[
 \Omega_i(C)=\{k\ne i:\text{ every edge from }B_i\text{ to }B_k
                    \text{ has its }B_i\text{-end in }C\}.             \tag{3.1}
\]

Call `C` **contact-protected relative to `j`** when `B_i` is contacted,
all its feet lie in `C`, and `B_j` is already contacted.  This is exactly
the case in which transferring `C` to `B_j` loses one contact without
gaining one.

We call `C` **root-safe relative to `j`** when it is not
contact-protected relative to `j`.

### Lemma 3.1 (owner-or-transfer)

If `C` is adjacent to `B_j`, is not contact-protected relative to `j`,
and

\[
                         \Omega_i(C)\subseteq\{j\},       \tag{3.2}
\]

then `i\to j` is an admissible lobe transfer.

#### Proof

The two tree pieces are connected, and the assumed `C`--`B_j` edge makes
the enlarged target connected.  For every `k\notin\{i,j\}`, condition
(3.2) says that some old `B_i`--`B_k` edge has its `B_i`-end outside
`C`; hence the residual source retains that adjacency.  The tree edge
`e` supplies the new source--target adjacency.  All other model
adjacencies are unchanged.

It remains only to count contacts.  If a foot of `B_i` remains outside
`C`, the source stays contacted.  If all source feet lie in `C`, the
target becomes contacted unless it already was; the sole contact-losing
case is precisely the excluded contact-protected case.  Thus (2.3) does
not decrease contact. \(\square\)

In a spanning model, the first hit of a binary-theorem foreign transit is
an actual edge from its source lobe to the named foreign bag: there is no
unused internal vertex before the first foreign bag.  Lemma 3.1 therefore
applies directly to that lobe.

### Corollary 3.2 (foreign-transit cycle obstruction)

Consider a directed cycle of named foreign transits

\[
                   i_1\to i_2\to\cdots\to i_m\to i_1,   \tag{3.3}
\]

and let `C_s` be the source lobe of the transit `i_s\to i_{s+1}`.  In the
lexicographically minimal contact-maximal model, at least one `C_s`
satisfies

\[
 \bigl|\Omega_{i_s}(C_s)-\{i_{s+1}\}\bigr|\ge1          \tag{3.4}
\]

or is contact-protected relative to `i_{s+1}`.

#### Proof

Otherwise Lemma 3.1 makes every arc of (3.3) admissible, contradicting
Theorem 2.1. \(\square\)

There is a useful label-free refinement.  If a root-safe lobe has exactly
one owner `k`, then transferring it to `B_k` is admissible, whether or not
`k` was the first foreign bag.  Hence:

### Corollary 3.3 (unique-owner dependency cycles terminate)

There is no nonempty family of root-safe lobes `C_i\subsetneq B_i` and a
map `f` of their bag labels to themselves such that

\[
                         \Omega_i(C_i)=\{f(i)\}.          \tag{3.5}
\]

Indeed the functional digraph of `f` contains a directed cycle, and the
associated transfers contradict Theorem 2.1.  Consequently every closed
foreign-transit/owner descent reaches a lobe which either owns at least two
bag labels or is contact-protected.

This is an actual termination theorem.  It does not claim that a
multi-owner or protected lobe is already a rooted clique model; those are
the two exact dynamic residues.

## 4. Two complex bags: ear closure or an exact quotient deficit

The relative-ear theorem for a spanning singleton society extends to two
complex bags with one sharp alternative.  This is the useful way to
combine ear absorption with a foreign transit: contract the foreign bag.

### Theorem 4.1 (two-complex quotient dichotomy)

Let `H` be `r`-connected and let

\[
             (A,B,\{s_1\},\ldots,\{s_{r-2}\})           \tag{4.1}
\]

be a spanning `K_r`-model.  Contract `B` to a labelled vertex `b`, and
write `Q_B=H/B`.  At least one of the following holds.

1. `H` has a `K_{r+1}` minor.
2. For every connected `C_0\subseteq A` of order at least two, there is
   a relative ear chain
   \[
       C_0\subsetneq C_1\subsetneq\cdots\subsetneq C_m=A, \tag{4.2}
   \]
   where `C_{t+1}-C_t` is a component of `A-C_t` having at least two
   distinct neighbours in `C_t`.
3. There is a set `X\subseteq V(H)-B` with `|X|\le r-2` such that
   `H-(B\cup X)` has at least two components and, for every such component
   `D`,
   \[
                  N_H(D)\subseteq B\cup X,
             \qquad N_H(D)\cap B\ne\varnothing.          \tag{4.3}
   \]

Outcome 3 is an exact **`B`-gated quotient deficit**.  The symmetric
statement holds after contracting `A`.

#### Proof

If `Q_B` is `r`-connected, then

\[
           (A,\{b\},\{s_1\},\ldots,\{s_{r-2}\})         \tag{4.4}
\]

is a spanning one-complex-bag `K_r`-model in `Q_B`.  Corollary 4.1 of
`hadwiger_spanning_singleton_core_exchange_dichotomy.md` gives either a
`K_{r+1}` minor in `Q_B` or the ear chain (4.2).  A minor in `Q_B` lifts
through the contraction of `B`, giving outcome 1 in `H`.

Suppose instead that `Q_B` is not `r`-connected.  Choose a separator
`Z` of order at most `r-1`.  Necessarily `b\in Z`.  Indeed, if `b\notin Z`,
then connectedness of `H-Z` would imply connectedness of its contraction
`Q_B-Z`, contrary to the choice of `Z`; while `H-Z` is connected because
`H` is `r`-connected.

Put `X=Z-\{b\}`.  Then `|X|\le r-2`, and the components of
`Q_B-Z` are exactly the components of `H-(B\cup X)`.  There are no edges
between distinct such components, so their neighbours lie in `B\cup X`.
Finally every component has a neighbour in `B`: otherwise its whole
neighbourhood would lie in `X`, and deleting at most `r-2` vertices would
disconnect `H`.  This proves (4.3). \(\square\)

### Corollary 4.2 (every quotient shore has real portal capacity)

In outcome 3, put `q=r-|X|`.  Then `q\ge2`, and every component `D` of
`H-(B\cup X)` satisfies

\[
                         |N_B(D)|\ge q.                  \tag{4.5}
\]

#### Proof

Choose a different component `D'`.  The set `X\cup N_B(D)` separates
`D` from `D'`: all neighbours of `D` lie in `B\cup X`, and after deleting
its `B`-neighbours it has no route through `B`.  The `r`-connectivity of
`H` gives

\[
                      |X|+|N_B(D)|\ge r,
\]

which is (4.5). \(\square\)

Thus a failed contraction does not merely name the complex gate bag.  It
supplies at least two distinct portal vertices in that bag from every
quotient shore.  Those are precisely the two endpoints needed for a
binary-tree bypass or a relative ear; the remaining issue is allocation
among the gate bag's model-label owners.

### Corollary 4.3 (where a two-bag foreign-transit cycle can live)

In a target-minor-free two-complex-bag cell, either both bags are relative
ear closures after contracting the other, or at least one contraction
exposes a gated quotient deficit (4.3).  Thus an infinite sequence of
clean ear absorptions strictly terminates by `|C_t|`, while a named
foreign-bag transit which cannot be absorbed is confined to a shore of an
explicit quotient separation of order at most `r-2` outside the foreign
bag.

This is an actual Hall-type output: the separator is small after the one
named complex bag is contracted.  It does not falsely count the vertices
of that bag as a small adhesion in `H`.

### Proposition 4.4 (why arbitrary clean rotations have no model potential)

Let `T_i` be a spanning tree of `B_i` in a spanning model.  A clean path
returned by Lemma 3.2 of `hadwiger_binary_transition_tree.md`, after taking
the subpath between consecutive visits to `T_i`, is a single non-tree edge
of `H[B_i]`.

Consequently a clean rotation changes only the chosen spanning tree.  It
does not change any branch set, contact, portal class, Hall circuit, or
minor-transition adhesion.  Clean rotations can cycle (the three spanning
trees of a triangle already form such a cycle), so no strict potential
defined only on the clique model can decrease under every clean rotation.

#### Proof

The interior of the clean subpath avoids `T_i` and every foreign bag.
But `V(T_i)=B_i`, and every vertex of `H` belongs to some bag because the
model is spanning.  Hence the subpath has no internal vertex and is a
single chord of `B_i`.  A fundamental-cycle exchange changes only the
edge set of the spanning tree.  The triangle example proves the final
assertion. \(\square\)

Thus the correct finite clean-ear potential is not the number or shape of
the spanning tree.  In the one-complex quotient cell, use the chain (4.2):
each ear absorption strictly increases `|C_t|` and therefore terminates at
the full bag.  At the full bag, an internal chord rotation must be spent
immediately on a labelled split, or else the proof must pass to the named
foreign transit / quotient-deficit / crossed-state alternatives.  Merely
rotating again cannot constitute progress.

## 5. A sharp two-complex-bag counterarchitecture

The residues in Corollaries 3.2--3.3 cannot be removed by geometry,
spanning, inclusion-minimality, or contact maximality alone.

Let

\[
 A=a_La_0a_R,\qquad B=b_Lb_0b_R                         \tag{5.1}
\]

be two disjoint three-vertex paths.  Add the two rung edges

\[
                         a_Lb_L,\qquad a_Rb_R.           \tag{5.2}
\]

Let `S={s_1,s_2,s_3,s_4}` induce `K_4`.  Join `s_1,s_2` to both
`a_L,b_L`, and join `s_3,s_4` to both `a_R,b_R`; add no other edges.
Call this ten-vertex graph `H`.  Finally add `v` adjacent exactly to
`a_0,b_0`, and call the resulting graph `G`.

Then

\[
               (A,B,\{s_1\},\{s_2\},\{s_3\},\{s_4\})   \tag{5.3}
\]

is a spanning `K_6`-model.

### Proposition 5.1

The model (5.3) has all of the following properties.

1. It is contact-maximal.
2. Both complex bags are inclusion-minimal while the other five bag
   labels are fixed.
3. There is a directed two-cycle of foreign transits and no clean
   intra-bag bypass:
   \[
   a_L-b_L-b_0-b_R-a_R\subseteq H-a_0,
   \quad
   b_L-a_L-a_0-a_R-b_R\subseteq H-b_0.                 \tag{5.4}
   \]
4. The two complex bags cannot be replaced by three pairwise adjacent
   connected bags while retaining the four singleton bags.
5. `G` has no `K_7` minor.

#### Proof

Only the two vertices `a_0,b_0` belong to `N_G(v)`.  Disjoint branch
sets therefore give at most two contacted bags, and (5.3) attains two.
This proves contact maximality.

In `A`, the left endpoint is the only vertex adjacent to `s_1,s_2`, the
right endpoint is the only vertex adjacent to `s_3,s_4`, and the middle
vertex is needed to connect them.  Thus no proper connected subset of `A`
can replace it while keeping all five other labels.  The same argument
applies to `B`.  The paths in (5.4) prove the two foreign transits, while
`A-a_0` and `B-b_0` each have two isolated vertices, so there is no clean
intra-bag bypass.

Any new branch set adjacent to both `s_1` and `s_3` must contain at least
one vertex of

\[
                         \{a_L,b_L\}                    \tag{5.5}
\]

and at least one vertex of

\[
                         \{a_R,b_R\}.                   \tag{5.6}
\]

There are only two vertices in each of (5.5) and (5.6), so at most two
pairwise disjoint branch sets can be adjacent to all four singleton bags.
This proves item 4.

For item 5, the following elimination order has at most five later
neighbours at every step (fill edges are included when counting):

\[
 v,a_0,b_0,a_L,b_L,a_R,b_R,s_3,s_4,s_1,s_2.            \tag{5.7}
\]

The successive later-neighbour counts are

\[
                         2,3,4,5,4,5,4,3,2,1,0.         \tag{5.8}
\]

Thus `tw(G)\le5`.  Since `tw(K_7)=6` and treewidth is minor-monotone,
`G` has no `K_7` minor. \(\square\)

At each end lobe in (5.4), two singleton labels are wholly owned.  This is
exactly the multi-owner alternative of Corollary 3.2.  The example is not
minor-critical (indeed it is only a static model architecture), so it does
not refute a theorem using the full edge-transition states.  It proves the
sharper negative statement needed here:

\[
\boxed{\text{spanning + contact maximal + minimal bags + a foreign-transit
cycle does not imply a model augmentation.}}
\]

## 6. Consequence for the uniform rooted-model programme

Clean tree rotations can be normalized away by passing to the fixed bag
and its block structure; they do not change the bag vertex set.  Named
foreign transits become useful only after Lemma 3.1 tests whether their
source lobes are transferable.  The lexicographic potential then closes
all safe dependency cycles.

The exact remaining operation-sensitive theorem is therefore narrower
than an unrestricted foreign-transit termination claim:

> In a proper-minor-minimal non-`r`-colourable graph, a multiply owned or
> contact-protected lobe exposed by Corollary 3.2 either admits a
> label-preserving split, produces a smaller Hall circuit, or supports the
> same marked state as a faithful operation on the opposite side of its
> actual ambient adhesion.

The counterarchitecture fails precisely the last hypothesis: it has no
minor-transition novelty or crossed-state system.  Thus the next proof
must spend that dynamic information on the multi-owner/protected residue,
not on another round of spanning-tree rotations.
