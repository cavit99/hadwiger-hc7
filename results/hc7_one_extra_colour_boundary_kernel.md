# A one-extra-colour critical kernel at a boundary edge

**Status:** written proof; separate internal audit GREEN in
[`hc7_one_extra_colour_boundary_kernel_audit.md`](hc7_one_extra_colour_boundary_kernel_audit.md).

This note records the list-critical structure forced by deleting one edge
between a connected open side and its boundary.  The deleted edge restores
one colour to exactly one vertex list.  A vertex-minimal obstruction then
has one of three forms: an ordinary Gallai tree, one of the one-root
exceptional graphs classified by Cranston--Rabern, or a nonempty set of
vertices with genuine list-degree excess.

At an actual seven-vertex boundary whose colouring has one two-vertex
colour class and five singleton classes, the first two forms expose an
actual order-seven separation whenever the critical kernel fills the open
side.  In the remaining form every vertex has positive list-degree excess;
vertices not adjacent to both members of the repeated boundary pair have
excess at least two.

Nothing here constructs a `K_7`-minor model or synchronizes the two closed
sides of the returned separation.

## 1. Abstract one-extra-colour kernel

Let `H` be a graph, let `L` be a list assignment on `H`, and let
`w in V(H)`.  Let `theta` be a colour not in `L(w)`, and define

\[
 L^+(w)=L(w)\cup\{\theta\},\qquad
 L^+(u)=L(u)\quad(u\ne w).                         \tag{1.1}
\]

Assume that

1. `H` is not `L`-colourable;
2. every proper induced subgraph of `H` is `L`-colourable; and
3. `H` is `L^+`-colourable.

Put

\[
             \varepsilon(u)=d_H(u)-|L(u)|.             \tag{1.2}
\]

For a graph `J` and a vertex `z`, write `h_z(z)=1` and
`h_z(y)=0` for `y ne z`.  Thus the pair `(J,h_z)` is choosable when
`J` is colourable from every list assignment having list order
`d_J(z)-1` at `z` and `d_J(y)` at every other vertex.

### Theorem 1.1 (one-extra-colour trichotomy)

Under the preceding assumptions, `H` is connected, every
`epsilon(u)` is nonnegative, and every `L^+`-colouring gives `w` the
colour `theta`.  Exactly one of the following structural alternatives
holds.

1. **Degree-list case.**  `epsilon(u)=0` for every vertex.  Then `H` is
   a Gallai tree: every block is a complete graph or an odd cycle.
2. **One-root case.**

   \[
      \varepsilon(w)=1,\qquad
      \varepsilon(u)=0\quad(u\ne w).                   \tag{1.3}
   \]

   The displayed list assignment witnesses that `(H,h_w)` is not
   choosable.  Consequently `H,w` belongs to the exact exceptional class
   of Cranston--Rabern, Theorems 4.1 and 3.6: it is one of the five
   block/lobe configurations in their Theorem 3.6 (equivalently,
   `(H,h_w)` is not Alon--Tarsi).  In cases (4) and (5)(iii) of that
   theorem, the distinguished block belongs to their stretched family
   `mathcal D`; the degree-two case (3) is a separate possibility.
3. **Positive-excess case.**  The set

   \[
      P=\{u\ne w:\varepsilon(u)\ge1\}
        \ \cup\
        \begin{cases}
          \{w\},&\varepsilon(w)\ge2,\\
          \varnothing,&\varepsilon(w)\le1
        \end{cases}                                    \tag{1.4}
   \]

   is nonempty.  The only possibility not recorded in `P` is that
   `epsilon(w)=0`; in that subcase some vertex outside `w` belongs to
   `P`, unless alternative 1 holds.

In every `L`-colouring of `H-w`, all colours of `L(w)` occur on
`N_H(w)`.

#### Proof

If `H` were disconnected, one of its components would be a proper induced
non-`L`-colourable subgraph, contrary to vertex-minimality.  The usual
extension argument gives

\[
                         d_H(u)\ge |L(u)|               \tag{1.5}
\]

for every `u`: otherwise an `L`-colouring of `H-u` would leave an
available colour for `u`.  Thus every `epsilon(u)` is nonnegative.

An `L^+`-colouring cannot give `w` a colour in `L(w)`, since it would
then be an `L`-colouring of all of `H`.  Hence it gives `w` the sole new
colour `theta`.

If every vertex is tight in (1.5), the Borodin--Erdos--Rubin--Taylor
degree-choosability theorem implies that `H` is a Gallai tree.  This is
alternative 1.

Suppose (1.3) holds.  The given noncolourable assignment has list order

\[
 |L(w)|=d_H(w)-1,\qquad |L(u)|=d_H(u)\quad(u\ne w).
\]

It is therefore a witness that `(H,h_w)` is not choosable.
Cranston--Rabern, Theorem 4.1, says that a connected pair `(H,h_w)` is
not choosable exactly when it is not Alon--Tarsi.  Their Theorem 3.6 gives
the asserted complete block/lobe classification.  This proves alternative
2.

If neither of the first two alternatives holds, then either some vertex
other than `w` has positive excess or `epsilon(w)>=2`, except possibly
when `epsilon(w)=0`.  In that exceptional subcase failure of alternative
1 supplies a positive-excess vertex outside `w`.  Hence `P` is nonempty,
which proves alternative 3.  The alternatives are exclusive by their
degree profiles.

Finally, colour `H-w` from `L`.  If some colour of `L(w)` were absent
from the coloured neighbourhood, assigning that colour to `w` would
colour `H` from `L`.  This proves the last assertion. \(\square\)

## 2. The boundary-edge construction

Let `G` be a graph which is not six-colourable, let `W` be a nonempty
connected vertex set, and put

\[
                         S=N_G(W).                       \tag{2.1}
\]

Assume that `G-(W union S)` is nonempty.  Choose `s in S`, `w in W`
with `sw in E(G)`, and let `c` be a proper six-colouring of `G-sw`.
Necessarily

\[
                         c(s)=c(w)=\theta,               \tag{2.2}
\]

since otherwise the edge could be restored.  Define, for `u in W`,

\[
                  L(u)=[6]-c(N_G(u)\cap S),             \tag{2.3}
\]

where the expression subtracted is a set of distinct colours.

### Proposition 2.1 (the deleted edge enlarges one list)

The graph `G[W]` is not `L`-colourable.  It has a connected induced
vertex-minimal non-`L`-colourable subgraph `K`, and `w in V(K)`.  On `K`,
the restriction of `c` is a colouring from the lists

\[
       L^+(w)=L(w)\cup\{\theta\},\qquad L^+(u)=L(u) (u\ne w). \tag{2.4}
\]

Thus Theorem 1.1 applies to `K,w`.

#### Proof

If `G[W]` had an `L`-colouring, it would glue to the restriction of `c`
on `G-W`: definition (2.3) excludes every conflict across `W-S`, while
the only deleted edge has one end in `W`.  This would six-colour `G`, a
contradiction.  Choose an induced noncolourable subgraph minimal by vertex
inclusion; it is connected.

For each `u ne w`, all edges from `u` to `S` are present in `G-sw`, so
`c(u) in L(u)`.  At `w`, the only possible boundary conflict in `c` is
the deleted edge `sw`.  In particular `s` is the only neighbour of `w`
in `S` coloured `theta`, and

\[
                         c(w)=\theta\in L^+(w).
\]

If `w` were not in `K`, the restriction of `c` would be an `L`-colouring
of `K`, a contradiction.  Hence (2.4) colours `K` and Theorem 1.1
applies. \(\square\)

## 3. Exact degree identity

For `u in K`, define

\[
\begin{aligned}
 q(u)&=|c(N_G(u)\cap S)|,\\
 \rho(u)&=|N_G(u)\cap S|-q(u),\\
 \sigma(u)&=|N_G(u)\cap(W-V(K))|,\\
 \varepsilon(u)&=d_K(u)-|L(u)|.
\end{aligned}                                           \tag{3.1}
\]

### Proposition 3.1 (pinch-kernel degree identity)

For every `u in K`,

\[
             d_G(u)=6+\varepsilon(u)+\rho(u)+\sigma(u). \tag{3.2}
\]

#### Proof

There are no edges from `W` to `G-(W union S)`, and `K` is induced in
`G[W]`.  Also `|L(u)|=6-q(u)`.  Therefore

\[
\begin{aligned}
d_G(u)
 &=d_K(u)+\sigma(u)+|N_G(u)\cap S|\\
 &=6-q(u)+\varepsilon(u)+\sigma(u)+q(u)+\rho(u),
\end{aligned}
\]

which is (3.2). \(\square\)

## 4. Exact-seven boundary with one repeated pair

Assume now that

1. `G` is seven-connected;
2. `|S|=7`;
3. the equality partition induced by `c` on `S` consists of one
   two-vertex block `{a,b}` and five singleton blocks; and
4. the critical kernel fills the shore: `K=G[W]`.

The fourth assumption makes `sigma(u)=0` in (3.2).

### Theorem 4.1 (one-pair excess or an exact separation)

For every `u in W`,

\[
 \rho(u)\le1,
 \qquad
 \rho(u)=1\quad\Longleftrightarrow\quad
                    \{a,b\}\subseteq N_G(u).           \tag{4.1}
\]

If `epsilon(u)=0`, then

\[
                         d_G(u)=7,
 \qquad                  \rho(u)=1,                     \tag{4.2}
\]

and `N_G(u)` is the boundary of an actual order-seven separation.

Consequently each of alternatives 1 and 2 of Theorem 1.1 returns such an
order-seven separation.  More precisely, in alternative 2 there is a
vertex `u ne w` satisfying (4.2).

If no actual order-seven separation is admitted, then every vertex of
`W` has positive excess and

\[
 \begin{cases}
   \varepsilon(u)\ge1,&\{a,b\}\subseteq N_G(u),\\
   \varepsilon(u)\ge2,&\{a,b\}\nsubseteq N_G(u).
 \end{cases}                                             \tag{4.3}
\]

Thus the only surviving branch is a literal positive-excess kernel; its
excess-one vertices are all adjacent to both members of the repeated
boundary pair.

#### Proof

Only one colour is repeated on `S`, and it is repeated exactly at `a,b`.
For any subset of `S`, deleting duplicate colour occurrences therefore
decreases its order by at most one.  Equality occurs precisely when the
subset contains both `a,b`.  This proves (4.1).

Suppose `epsilon(u)=0`.  Equations (3.2), (4.1), and `sigma(u)=0` give

\[
                         d_G(u)\le7.
\]

Seven-connectivity gives the reverse inequality, so equality holds and
`rho(u)=1`.  The nonempty graph `G-(W union S)` is anticomplete to `u`.
After deleting `N_G(u)`, both `u` and at least one vertex of that far side
remain in different components.  Hence `N_G(u)` is an actual separator,
and its order is seven.  This proves (4.2).

Alternative 1 has a tight vertex, so it gives (4.2).  In alternative 2,
`d_K(w)=|L(w)|+1`, which implies `d_K(w)>=1`; hence `K` has a vertex
`u ne w`.  Every such vertex is tight by (1.3), and again (4.2) applies.

Finally, if no order-seven separation occurs, the preceding paragraph
excludes every tight vertex.  In fact every `u in W` has `d_G(u)>=8`,
because a degree-seven vertex would have the same full-neighbourhood
separator just exhibited.  Equation (3.2) now gives

\[
                         \varepsilon(u)+\rho(u)\ge2.
\]

Combining this with (4.1) proves (4.3). \(\square\)

## 5. Scope and use

The theorem gives a sharp replacement for attempting to split five
bichromatic paths at the deleted boundary edge.  In the shore-filling
one-pair case, either a tight vertex exposes another actual order-seven
boundary, or the obstruction has positive internal list-degree excess at
every vertex.  The excess is literal: an excess-one vertex must contact
both vertices in the repeated boundary block, and every other vertex has
excess at least two.

The theorem does not show that the returned order-seven boundary has a
common full equality partition on both closed sides.  Nor does positive
excess identify the five colours with five branch-set labels.  Those are
the remaining composition obligations.

## 6. References

- Borodin and, independently, Erdos--Rubin--Taylor: the
  degree-choosability characterization of Gallai trees.
- Daniel W. Cranston and Landon Rabern,
  *Beyond Degree Choosability*, Electronic Journal of Combinatorics
  **24** (2017), #P3.29, Theorems 3.6 and 4.1,
  <https://doi.org/10.37236/6179>.
