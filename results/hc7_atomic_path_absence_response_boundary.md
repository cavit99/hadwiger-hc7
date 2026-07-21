# Response boundary when the atomic return path is absent

**Status:** written proof; separate internal audit GREEN.

This note upgrades the bounded-separator alternative in the arbitrary
subdivision first-hit theorem.  In a hypothetical minor-minimal
counterexample to `HC_7`, an inclusion-minimal separator of order at most
nine is full on both distinguished sides, has a four-colourable boundary,
and carries both exact independent-block responses and a selected
edge-deletion response.  Applied to the atomic first-hit setup, this closes
the branch in which no branch-avoiding path returns from the marked root to
the common `fg` vertex as a literal bounded response interface.

It does not turn that interface into an exact order-seven interface or prove
a strict same-form reduction.

## 1. Small minimal separators

Let `G` satisfy

\[
 \kappa(G)\ge 7,\qquad \chi(G)=7,\qquad
 K_7\not\preccurlyeq G,
 \qquad \chi(M)\le 6\text{ for every proper minor }M\text{ of }G.
 \tag{1.1}
\]

Assume the established case `HC_5`.  Let `r,t` be distinct vertices, let
`Z\subseteq V(G)-\{r,t\}` be an `r`--`t` separator with `|Z|<=9`, and let

\[
                         S\subseteq Z                    \tag{1.2}
\]

be an inclusion-minimal `r`--`t` separator.  Denote by `A` and `B` the
components of `G-S` containing `r` and `t`, respectively.

### Theorem 1.1 (full response boundary)

Under (1.1)--(1.2), all of the following hold.

1. `7<=|S|<=9`, and both `A` and `B` are adjacent to every literal vertex
   of `S`.  In particular,

   \[
    N_G(A)=S
   \quad\text{and}\quad
    \bigl(G[A\cup S],G-A\bigr)                         \tag{1.3}
   \]

   is an actual separation with two nonempty open sides.
2. The boundary is four-colourable:

   \[
                              \chi(G[S])\le4.            \tag{1.4}
   \]
3. For every nonempty independent set `I` of `G[S]`, each closed shore in
   (1.3) has a proper six-colouring in which `I` is an exact colour block
   on `S`: all vertices of `I` receive one colour and no vertex of `S-I`
   receives that colour.
4. Let `e=as` be any edge with `a in A` and `s in S`, and let `c_e` be any
   proper six-colouring of `G-e`.  The equality partition induced by `c_e`
   on `S` is realized on the unchanged far shore `G-A` but is not realized
   by any proper six-colouring of the unchanged near shore `G[A\cup S]`.
   The symmetric assertion holds for every edge from `B` to `S`.

#### Proof

For each `s in S`, inclusion-minimality says that `G-(S-{s})` contains an
`r`--`t` path.  Such a path uses `s` and no other vertex of `S`.  The
section before `s` lies in `A`, and the section after `s` lies in `B`.
Thus `s` has a neighbour in each of `A,B`.  Since `A` is a component of
`G-S`, this also gives `N_G(A)=S`.  Seven-connectivity gives `|S|>=7`,
while (1.2) gives `|S|<=9`.  This proves item 1.

We next prove (1.4).  If `|S|=7`, choose an edge from `A` to `S` and a
six-colouring of its deletion, which exists by (1.1).  The generic
exact-seven response-interface theorem applies to (1.3); its automatic
response properties give `chi(G[S])<=4`.

Suppose `|S|` is eight or nine.  The two-full-shore boundary-absorption
theorem, applied to `A,B,S`, gives (1.4) at order eight.  At order nine it
gives (1.4) unless

\[
                              G[S]\cong K_2\vee C_7.     \tag{1.5}
\]

Assume (1.5), write the universal edge as `pq`, and label the induced
cycle in cyclic order by `0,1,...,6`.  If `A,B` are the only components of
`G-S`, then

\[
                   \chi(G-\{p,q\})\ge\chi(G)-2=5.
\]

By `HC_5`, this graph contains a `K_5` minor.  The cycle-boundary completion
theorem, with the two connected full components `A,B`, now gives a `K_7`
minor, contrary to (1.1).

Otherwise choose a third component `D` of `G-S`.  Its neighbourhood is
contained in `S`, and seven-connectivity gives `|N_G(D)|>=7`.  Hence `D`
misses at most two vertices of `S`.  After swapping `p,q` and applying a
dihedral symmetry of the cycle, its missed set is one of

\[
 \varnothing,\ \{p\},\ \{0\},\ \{p,q\},\ \{p,0\},
 \ \{0,1\},\ \{0,2\},\ \{0,3\}.                       \tag{1.6}
\]

In every case `D` has neighbours at `4`, at `6`, and at at least one of
`p,0,1`.  The seven sets

\[
 \{p,0,1\},\quad \{q\},\quad A\cup\{2\},\quad
 B\cup\{3\},\quad D\cup\{4\},\quad \{5\},\quad \{6\}
 \tag{1.7}
\]

are disjoint and connected.  The universal vertices, fullness of `A,B`,
the three displayed contacts of `D`, and the cycle edges make them pairwise
adjacent.  Thus (1.7) is a `K_7`-minor model, again a contradiction.  This
excludes (1.5) and proves item 2.

Fix a nonempty independent set `I` of `G[S]`.  The connected set
`B\cup I` can be contracted to one vertex `w`; this gives a proper minor,
so it has a six-colouring.  Restrict that colouring to `G[A\cup S]` and
give every vertex of `I` the colour of `w`.  This is proper: `I` is
independent, and every edge from `I` to a retained vertex becomes an edge
at `w` under the contraction.  Moreover, `w` is adjacent to every vertex
of `S-I`, because `B` is full to `S`.  Hence `I` is an exact colour block
on `S`.  Contracting `A\cup I` instead and restricting the resulting
colouring to `G-A` gives the same exact block on the other closed shore.
This proves item 3.

Finally fix `e=as` as in item 4.  The restriction of `c_e` to `G-A` is
proper, because the only deleted edge has its other end in `A`.  Suppose
its equality partition on `S` were also realized by a proper six-colouring
of `G[A\cup S]`.  Permute the colour names on one shore so that the two
colourings agree on `S`, and glue them.  The result is a proper
six-colouring of `G`, contrary to (1.1).  This proves the selected response;
the proof with `A,B` interchanged is identical.  \(\square\)

## 2. Application to the arbitrary atomic subdivision

Use the notation and hypotheses of the audited arbitrary-subdivision
first-hit theorem.  Thus `T` is a labelled subdivision of

\[
 H_0=(K_7-\{ab,cd\})+\{xa,xb,xc,xd\},
\]

with marked vertices

\[
 q\in\operatorname{int}(T_{ad}),\qquad
 q'\in\operatorname{int}(T_{bc}),\qquad
 h\in\operatorname{int}(T_{fg}),
\]

and with literal edges `eh,hx`.  Put

\[
                         Z=\{a,b,c,d,e,f,g,x,q\}.        \tag{2.1}
\]

### Corollary 2.1 (path-absence response)

Assume (1.1).  If there is no `q'`--`h` path whose internal vertices avoid
the eight branch vertices of `T` and avoid `q`, then `G` has an actual
separation of order seven, eight, or nine satisfying every conclusion of
Theorem 1.1.  Its boundary is an inclusion-minimal `q'`--`h` separator
contained in the literal set `Z`.

If the `K_7` and order-seven alternatives of the first-hit theorem have
already been excluded, the returned boundary has order eight or nine.

#### Proof

The absence of the displayed path says exactly that `Z` separates `q'`
from `h`.  Choose an inclusion-minimal `q'`--`h` separator `S\subseteq Z`
and apply Theorem 1.1.  The last assertion follows from the order-seven
alternative in the first-hit theorem.  \(\square\)

## 3. Trust boundary

Corollary 2.1 returns a boundary contained in the named literal set `Z` and
a named edge-deletion response on either distinguished component.
It therefore removes the response gap from the path-absence branch of the
first-hit normal form.

It does not synchronize the two closed-shore colourings, force the boundary
to have order seven, preserve the old subdivision branch sets inside one
shore, or prove that either distinguished component is a same-form atomic
collision instance.  In particular, the order-eight or order-nine outcome
is a bounded response interface, not yet the strict host-component descent
required by the full single-collision theorem.

## 4. Audited dependencies

- [arbitrary-subdivision first-hit theorem](hc7_atomic_subdivision_first_hit_boundary.md)
- [generic exact-seven response restart](hc7_generic_exact7_response_restart.md)
- [two-full-shore boundary absorption](hc7_two_full_shore_boundary_absorption.md)
- [cycle-boundary completion theorem](hc7_cycle_boundary_completion.md)
