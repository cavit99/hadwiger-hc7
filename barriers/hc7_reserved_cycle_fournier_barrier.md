# A sharp barrier to reserving the seventh branch set by cyclability

**Status:** elementary barrier to an intermediate claim.  This six-vertex
graph is not a counterexample to `HC_7` and is not asserted to realize the
full two-pair separation.

## 1. The false inference

Fournier's localized Chvatal--Erdos theorem says that if `H` is
two-connected and `X subseteq V(H)` satisfies

\[
                          \alpha_H(X)\le\kappa(H),       \tag{1.1}
\]

then one cycle of `H` contains every vertex of `X`.  In the degree-eight
equality case, three-connectivity and
`alpha_G(N_G(v))<=3` therefore put the five selected neighbours of `v` on
one cycle.

This does **not** imply that the cycle can avoid a prescribed connected
seventh branch set, even if that set is adjacent to all five selected
vertices.

## 2. Construction

Let

\[
                           F=K_{2,3},
\]

put `C=V(F)`, and add one vertex `d` adjacent to every vertex of `F`.
Thus

\[
                           H=K_1\vee K_{2,3},
             \qquad       D=\{d\}.                       \tag{2.1}
\]

The graph `H` is three-connected: deleting at most two vertices leaves
either the universal vertex `d`, or the connected graph obtained from
`K_{2,3}` by deleting at most one vertex.  Moreover,

\[
                              \alpha_H(C)=3.              \tag{2.2}
\]

There is a cycle containing all five vertices of `C`; if the bipartition
of `F` is `\{a_0,a_1\}` and `\{b_0,b_1,b_2\}`, one is

\[
                  d b_0 a_0 b_1 a_1 b_2 d.              \tag{2.3}
\]

However, every cycle containing `C` uses `d`.  Otherwise it would be a
Hamiltonian cycle of `K_{2,3}`, which is impossible because every cycle
in a bipartite graph uses equally many vertices from its two parts.

Consequently no cycle through `C` is disjoint from the connected set `D`,
although `D` is adjacent to every member of `C`.

## 3. Exact trust boundary

This refutes the bare implication

> three-connectivity, `alpha(C)<=3`, and complete contact from a connected
> set `D` to `C` produce a `D`-avoiding cycle through `C`.

It does not refute a theorem using the literal disk embedding, the five
named opposite-shore branch sets, contraction-critical colourings, or a
connectivity lower bound for `H-D`.

There is, however, a clean sharp fork.  Applying Fournier to `H-D` shows

\[
 \text{either a cycle in }H-D\text{ contains }C,
 \qquad\text{or}\qquad \kappa(H-D)\le2.                 \tag{3.1}
\]

Indeed, `alpha_{H-D}(C)=alpha_H(C)<=3`; hence three-connectivity of `H-D`
would give the first outcome.  Construction (2.1) has
`H-D=K_{2,3}` and makes the second outcome sharp.

Thus the valid unconditional conclusion in `H` is only the unreserved
cycle.  To use a cycle in the degree-eight contact-allocation theorem, the
proof must additionally eliminate the order-at-most-two separator in
(3.1), split the chosen seventh branch set after a forced traversal, or
replace it by a disjoint connected set retaining at least seven labelled
contacts.

## 4. Reference

The exact statement used above is Theorem 7 in Ronald J. Gould,
[*A look at cycles containing specified elements of a graph*](https://www.math.emory.edu/~rg/P136Y09.pdf),
Discrete Mathematics 309 (2009), 6299--6311.  Gould attributes the theorem
to I. Fournier's 1985 These d'Etat at Universite de Paris-Sud.
