# Unique portals force exact-cut descent

## 1. Label-free descent lemma

Let (G) be (k)-connected, let (S) be a vertex cut of order (k),
and let (C) be a component of (G-S).  Assume that (G-S) has a
component other than (C).  For (sin S), call (xin C) a unique
(C)-portal of (s) when

\[
                         N_C(s)=\{x\}.
\]

### Theorem 1.1 (unique-portal descent)

If (x) is the unique (C)-portal of (s), exactly one of the
following holds.

1. (C=\{x\}).  Then the singleton is full to (S),
   (N_G(x)=S), and (d_G(x)=k).
2. (C-\{x\}\ne\varnothing), and
   
   \[
                   T=(S-\{s\})\cup\{x\}             \tag{1.1}
   \]
   
   is another cut of order (k).  Moreover
   
   \[
                         N_G(C-\{x\})=T,             \tag{1.2}
   \]
   
   and every component of (C-x) is a component of (G-T), hence a
   strictly smaller fragment than (C).

#### Proof

Every component behind a (k)-cut in a (k)-connected graph is full to
the cut.  Indeed, if a component missed (zin S), its neighbourhood
would be contained in (S-\{z\}), a separator of order at most
(k-1).

If (C=\{x\}), fullness gives all (k) edges from (x) to (S).
Different components of (G-S) are anticomplete, so these are all
neighbours of (x).  This proves outcome 1.

Assume (Y=C-\{x\}\ne\varnothing).  No vertex of (Y) is adjacent to
(s), by uniqueness of the portal, and every neighbour of (Y) outside
(Y) lies in (S\cup\{x\}).  Therefore

\[
                         N_G(Y)\subseteq T.
\]

The component of (G-S) different from (C) lies outside
(Y\cup N_G(Y)).  Hence (N_G(Y)) separates a nonempty set from a
nonempty far side.  Connectivity gives

\[
                  k\le |N_G(Y)|\le |T|=k,
\]

so equality holds and (1.2) follows.  Thus (T) is a (k)-cut.

There are no edges between different components of (C-x), and all of
their external neighbours lie in (T).  Conversely, after deleting
(T), none can join the far side.  They are therefore components of
(G-T).  Each is a proper subset of (C), proving the strict descent.

\(\square\)

### Corollary 1.2 (atomic portal multiplicity)

If (C) is a minimum fragment among all components behind (k)-cuts,
then every boundary vertex has at least two neighbours in (C), unless
(C) is a singleton.  Equivalently, an atomic nonsingleton shore has no
unique boundary portal.

This conclusion uses only connectivity.  It is independent of colouring,
minor exclusion, planarity, and the graph induced by (S).

## 2. Antipodal-gate specialization

In the antipodal (HC_7) gate, the exact cut is

\[
                         L=\{v\}\cup X\cup\{p,q\},
\]

and its (K_0)-shore (C_0) contains (0).  Since (d(v)=7), its
only neighbour in (C_0) is (0).  Theorem 1.1, with (s=v,x=0),
gives the exact dichotomy

\[
\begin{array}{ll}
|C_0|\ge2:&
  (L-\{v\})\cup\{0\}\text{ is a nested exact seven-cut};\\[1mm]
C_0=\{0\}:&
  N_G(0)=L,\ d_G(0)=7.
\end{array}                                            \tag{2.1}
\]

The gate cut has exactly two shores.  Consequently, in the singleton
case the opposite shore is the sole component of (G-N_G[0]).  Thus an
atomic antipodal gate does not contain an unbounded two-path web: it
re-roots the problem at a degree-seven vertex with one exterior
component.

## 3. Scalable content

The operative statement does not mention the Moser spindle or the number
seven.  In any (k)-connected counterexample programme, a contact or web
obstruction with a uniquely exposed boundary portal has only two possible
endpoints:

\[
   \text{strict exact-cut descent}
   \quad\text{or}\quad
   \text{a degree-}k\text{ singleton re-rooting}.
\]

This is the structural invariant hidden by a quotient that records only
whether a portal class is nonempty.
