# Atomic low-root-degree closure

**Status:** proved and independently audited.

This note closes every nonsingleton compulsory atom with connected
bipartite frontier and thin-root internal degree at most two.  The proof
uses a singleton clique reservoir to remove the entire two-list parity
obstruction; no path, web, or `st`-numbering is needed.

## 1. A two-defect reservoir lemma

Let `H` be a connected bipartite graph on a set `S` of order at least four.
Let `u in S`, and let `D subseteq S-{u}` have order at most two.  Give the
vertices the lists

\[
 \Lambda(u)=\{0\},\qquad
 \Lambda(d)=\{1\}\ (d\in D),\qquad
 \Lambda(s)=\{0,1\}\ (s\notin D\cup\{u\}).             \tag{1.1}
\]

### Lemma 1.1 (one singleton reservoir resolves two defects)

There is a clique `U subseteq S` of order at most one such that `H-U` has
a proper `Lambda`-list-colouring using both labels `0,1`.

#### Proof

Fix a bipartition of `H` and let `B_u` be the side containing `u`.  Put

\[
                         D_{\rm bad}=D\cap B_u.
\]

The prescribed value `0` at `u` asks for the orientation which gives label
`0` to `B_u`.  A prescribed value `1` is compatible with this orientation
exactly at members of `D-D_bad`.

Choose the singleton reservoir by

\[
 U=
 \begin{cases}
  \varnothing,&|D_{\rm bad}|=0,\\
  D_{\rm bad},&|D_{\rm bad}|=1,\\
  \{u\},&|D_{\rm bad}|=2.
 \end{cases}                                             \tag{1.2}
\]

In the first two cases every surviving prescribed vertex agrees with the
orientation which gives `u` label `0`.  In the last case the two surviving
members of `D` lie in the same bipartition side and both prescribe label
`1`.  Thus, in every component of `H-U` containing a prescribed vertex,
all prescriptions choose one common orientation.  Orient components with
no prescribed vertex arbitrarily.  This gives a proper list-colouring.

It remains only to ensure that both labels occur.  If `H-U` has an edge,
the component containing it uses both labels.  If `H-U` is independent,
then `U` cannot be empty because the connected graph `H` has an edge.
Thus `U` is a singleton, `|S-U|>=|S|-1>=3`, and at most two surviving
vertices have singleton lists.  A flexible isolated vertex can therefore
be assigned whichever label is missing.  Both colour classes can be made
nonempty.  Finally, `U` is empty or a singleton, hence is a clique.
\(\square\)

The connectedness hypothesis can be weakened to a componentwise condition,
but the displayed form is exactly what the atomic connected frontier needs.

## 2. Literal carrier consequence

Use an actual separation

\[
 V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad S=W\mathbin{\dot\cup}\{u\},\qquad |S|=7,
\]

with no `A-R` edge.  Assume:

1. `G` is seven-connected, is not six-colourable, and every proper minor
   is six-colourable;
2. `G[S]` is connected and bipartite;
3. `A` is connected and `S`-full, `|A|>=2`, and `zu` is the unique
   `A-u` edge; and
4. `R` contains two disjoint connected `S`-full packets.

The audited root-deletion theorem gives

\[
                         A-z\text{ connected},
                  \qquad N_S(A-z)=W.                   \tag{2.1}
\]

### Theorem 2.1 (a surviving root has internal degree at least three)

If

\[
                              d_{G[A]}(z)\le2,          \tag{2.2}
\]

then `G` is six-colourable.  Consequently every hypothetical survivor with
connected bipartite frontier satisfies

\[
                              d_{G[A]}(z)\ge3.          \tag{2.3}
\]

#### Proof

The relative seven-connectivity inequality applied to the connected set
`{z}` gives

\[
                  d_{G[A]}(z)+|N_S(z)|\ge7.
\]

Under (2.2), `z` therefore meets at least five literal boundary vertices.
Put

\[
                         C_0=\{z\},\qquad C_1=A-z.
\]

The two sets are nonempty, disjoint and connected by (2.1), and they are
adjacent because `A` is connected.  The unique-portal condition and (2.1)
give

\[
 N_S(C_1)=S-\{u\},
 \qquad
 D:=S-N_S(C_0)\subseteq S-\{u\},
 \qquad |D|\le2.                                      \tag{2.4}
\]

The literal carrier lists are exactly (1.1): `u` is forced to `C_0`, every
member of `D` is forced to `C_1`, and every other boundary vertex contacts
both carriers.  Apply Lemma 1.1.  Its two nonempty independent colour
classes are contacted by the correspondingly labelled carriers, and its
set `U` is a clique reservoir of order at most one.  The audited adaptive
clique-reservoir return theorem, using the two full packets in `R`, now
six-colours `G`.  \(\square\)

## 3. Scope

The theorem is stronger than a prefix/suffix assertion for one
`st`-numbering: it uses the canonical first split `{z}|(A-z)` and works for
every connected bipartite frontier.  It also explains why raw interval
counterexamples disappear once the permitted clique reservoir is used.

The disconnected exceptional frontier

\[
                         K_{1,3}\mathbin{\dot\cup}K_3
\]

is not covered.  There, deleting one retained triangle vertex leaves two
components and the remaining forced claw leaves can still demand opposite
orientations.  That residue must use the separate rooted-`K_5`/literal
`K_7` alternative; it may not be silently included in Theorem 2.1.
