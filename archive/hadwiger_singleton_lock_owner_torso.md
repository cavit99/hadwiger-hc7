# From a singleton Hall lock to one repeated-owner torso

## 1. Setup

Let `G` be seven-connected, let `S` be a seven-cut, and let `D` be a
globally minimum fragment behind `S`.  Suppose

\[
                         D=U_0\dot\cup U_1\dot\cup\cdots\dot\cup U_4 \tag{1.1}
\]

is a protected five-frame: its five parts are nonempty, connected and
pairwise adjacent.  For sets `X` disjoint from `S`, write

\[
                         P_S(X):=N_G(X)\cap S
\]

Fix `s in S`, put `T=S-{s}`, and assume

\[
 P_S(U_0)=\{s\},\qquad
 s\in P_S(U_i),\quad P_S(U_i)\cap T\ne\varnothing
                         \quad(1\le i\le4).          \tag{1.2}
\]

Thus `U_0` is the unique singleton-locked row and every other frame bag
is biportal for the split `{s}|T`.

Every component `R` of `G-S` other than `D` is full to `S`.  Indeed, if
some `x in S` had no neighbour in `R`, then `S-{x}` would separate `R`,
contrary to seven-connectivity.

Proposition 5.1 of `hadwiger_two_pool_hall_lock.md` gives an index
`j in {1,2,3,4}` and two distinct vertices of `U_j` adjacent to `U_0`.
Fix such an owner `U_j`.

## 2. The exact five portal classes inside the repeated owner

Inside `U_j`, define

\[
\begin{aligned}
 A_0&=N_{U_j}(U_0),\\
 A_i&=N_{U_j}(U_i)\quad(i\in\{1,2,3,4\}-\{j\}),\\
 A_T&=N_{U_j}(T).
\end{aligned}                                      \tag{2.1}
\]

Here `N_{U_j}(Y)` denotes the vertices of `U_j` having a neighbour in
`Y`.

These are five nonempty portal sets.  The collision gives `|A_0|>=2`;
the protected-frame edges give the three sets `A_i`; and (1.2) gives
`A_T`.

### Theorem 2.1 (five-rainbow owner split closes the lock)

If `U_j` contains two vertex-disjoint connected subgraphs each meeting
all five sets in (2.1), then `G` contains a `K_7` minor.

#### Proof

Extend the two disjoint rainbow subgraphs to an adjacent connected
bipartition

\[
                              U_j=X\dot\cup Y        \tag{2.2}
\]

using Lemma 2.1 of `hadwiger_rainbow_block_helly_core.md`.  Both `X,Y`
meet `U_0`, every `U_i` with `i notin {0,j}`, and `T`.

Let `R` be a component of `G-S` distinct from `D`.  Use the seven bags

\[
 \boxed{U_0\cup\{s\}},\quad X,\quad Y,\quad
 \bigl(U_i:i\in\{1,2,3,4\}-\{j\}\bigr),\quad
 \boxed{R\cup T}.                                  \tag{2.3}
\]

They are disjoint and connected.  The six frame-derived bags are
pairwise adjacent: old frame edges supply every pair not involving both
new sides, the five portal conditions give all edges from each of `X,Y`,
and (2.2) gives `XY`.  The bag `R union T` is connected by fullness.  It
sees `U_0 union {s}` through an `R-s` edge and sees the other five bags
through their `T`-portals.  Hence (2.3) is a `K_7` model.  \(\square\)

This is the exact owner-splitting form of the two-pool completion.  It
uses every boundary vertex only once: `s` is owned by the locked bag and
all of `T` is owned by the full-shore bag.

## 3. Failure is one bounded-adhesion torso

### Corollary 3.1 (gate, cycle, or 3-connected repeated-owner core)

If `G` has no `K_7` minor, the five-set rooted graph

\[
                    (U_j;A_0,(A_i)_{i\ne0,j},A_T)    \tag{3.1}
\]

is portal-indecomposable.  Consequently its Tutte decomposition has a
bag `B_j` meeting every connected transversal of the five portal sets,
and exactly one of the following torso types occurs:

1. `|B_j|<=2`;
2. the torso on `B_j` is a cycle; or
3. the torso on `B_j` is 3-connected.

Every component of `U_j-B_j` misses at least one of the five portal
classes and has at most two neighbours in `B_j`.

#### Proof

Two disjoint rainbows would give `K_7` by Theorem 2.1.  Apply Corollary
2.1 of `hadwiger_rainbow_torso_helly_core.md` to their absence.  \(\square\)

Thus the seven-contact collision does not leave an arbitrary repeated
owner.  Either it immediately closes, or all five-way portal complexity
is concentrated in one adhesion-two gate/cycle/3-connected torso.  Any
remaining proof must act on that one torso: a rooted model/cross supplies
the split in Theorem 2.1, while a crossless outcome must make its five
portal orders compatible with one web state.

## 4. Exact scope

The unique-lock hypothesis in (1.2) is necessary for this formulation.
If another frame bag also has no `T`-portal, the last bag in (2.3) need
not see it.  Likewise the equality (1.1), not merely containment of a
five-frame in `D`, is what permits the minimum-fragment collision used to
choose `U_j`.

Corollary 3.1 is a genuine infinite-family reduction, not a closure of
the torso outcomes.  In the order-at-most-two case, the gate must still
be lifted through the actual combined carrier network.  In the
3-connected case, virtual edges must be expanded before any rooted model
is used.  These are the same boundary-faithful qualifications as in the
audited carrier-lift programme.
