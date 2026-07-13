# Matching versus portal concentration at a surplus interface

## 1. Setting

Let \(G\) be seven-connected, let \(S\) be a seven-cut, and choose a
minimum fragment \(D\) behind \(S\). Suppose

\[
 D=X\mathbin{\dot\cup}Y
\]

is a connected covering split. Let \(H\) be the bipartite graph whose
parts are \(X,Y\) and whose edges are exactly the interface edges.

The point of this note is to replace the raw parameter
\(|E(H)|\ge3\) by a structural alternative which scales to arbitrarily
many interface edges.

## 2. Matching-or-concentrated-portals theorem

### Theorem 2.1

Exactly one of the following structural branches is available.

1. \(H\) has a matching \(M\) of order three.
2. \(H\) has a vertex cover \(Z\) of order at most two. For every
   component \(K\) of \(D-Z\),

   \[
   |N_S(K)|\ge 8-|Z|.                             \tag{2.1}
   \]

   Thus a one-vertex cover leaves only full \(S\)-rows, while a
   two-vertex cover leaves rows of boundary defect at most one.

#### Proof

By König's theorem, if \(H\) has no matching of order three, it has a
vertex cover \(Z\) of order at most two.

Fix a component \(K\) of \(D-Z\). Since every interface edge has an end
in \(Z\), and \(K\) is a component after all of \(Z\) is removed, every
neighbour of \(K\) in \(D-K\) belongs to \(Z\). Hence

\[
 N_G(K)=N_S(K)\mathbin{\dot\cup}N_D(K),
 \qquad N_D(K)\subseteq Z.                        \tag{2.2}
\]

The far shore behind \(S\) is anticomplete to \(D\). Thus the set in
(2.2) separates the connected set \(K\) from that far shore.
Seven-connectivity gives order at least seven. Equality would make
\(K\) a fragment behind a seven-cut. Since \(K\subsetneq D\), this
contradicts the choice of \(D\) as a minimum fragment. Therefore

\[
 |N_S(K)|+|N_D(K)|\ge8.
\]

Using \(|N_D(K)|\le|Z|\) proves (2.1). \(\square\)

This conclusion uses the global minimum-fragment choice in an essential
way. Without it, equality exports an exact seven-cut rather than giving
the strict bound (2.1).

## 3. The three-matching branch retains the state transition

Suppose outcome 1 holds and choose a three-edge matching \(M\). If
\(F=E(H)-M\) is nonempty, delete all edges of \(F\). The graph
\(G-F\) is a proper minor and is six-colourable. Its boundary state
\(\Phi_F\):

* extends the unchanged far shore;
* extends the operated shore with interface exactly \(M\);
* does not extend the original shore \(D\); and
* has the same two covering portal rows \(P_X,P_Y\).

The nonextension assertion is the usual exact-state gluing argument:
an extension over the original \(D\), aligned with the fixed colouring
of the far side, would six-colour \(G\).

Whenever \(\Phi_F\) is a four-block matching state, Theorem 2.1 of
hadwiger_three_interface_packet_reduction.md applies. It gives either
a genuine two-block carrier packet or the unique complementary split
row

\[
 P_X=A\cup\{b_1,c_1,r\},\qquad
 P_Y=A\cup\{b_2,c_2,r\}.                          \tag{3.1}
\]

If \(F\) is empty, the original interface is itself a three-edge
matching, and the same packet-or-row conclusion applies to every
available four-block transition state.

## 4. The concentrated branch is an ownership problem

Outcome 2 does not leave an arbitrary high-degree interface. Removing
at most two portal vertices decomposes it into mutually anticomplete
pieces, each full or almost full to the seven-label boundary. These are
not literally components of (G-S): they may all attach to the common
set (Z). Therefore the existing full-shore ownership theorem cannot be
applied without modification. What has been proved is that all unbounded
edge multiplicity is compressed into at most two internal portal
vertices; the remaining theorem must be a portal-aware version of
ownership.

The remaining theorem can therefore be stated without an edge count:

> **Two-portal ownership exchange.** A family of full or defect-one
> \(S\)-shores attached through at most two internal portal vertices
> either supplies the boundary blocks of a transition state in disjoint
> shores, or one portal vertex owns all missing blocks; in the latter
> case deleting or contracting an incident edge gives a rooted-state
> reduction or a smaller exact adhesion.

Theorem 2.1 is the structural reduction needed before attacking that
statement. It treats all \(|E(H)|\ge3\) simultaneously and shows why
enumerating interface-edge counts cannot be the final method.
