# Accessible-bag saturation and the source-tight surplus branch

## 1. Local lexicographic normalization

Let \(G\) be a graph which is not \(r\)-colourable although every
proper minor is.  Fix \(v\), put \(H=G-v\), and let

\[
                 \mathcal M=(B,B_1,\ldots,B_s,\ldots)
\]

be a labelled \(K_r\)-model in \(H\).  Suppose \(B\) is a contacted
bag and \(I\) is an inclusion-minimal nonlinkable family of uncontacted
bag labels.  Put

\[
 c=\#\{\hbox{contacted bags}\},\qquad h=|I|.
\]

There are three ordered progress outcomes: more than \(c\) contacted
bags; at contact count \(c\), a Hall circuit of order below \(h\); or,
at the same coordinates \((c,h)\), a strict enlargement of \(B\).
When the first two outcomes are excluded in a fixed branch, choose
\(|B|\) maximum among all labelled model/circuit pairs with coordinates
\((c,h)\).

This is a **local** normalization.  It must not be confused with global
contact maximality: at a globally contact-maximal model every uncontacted
singleton is already nonlinkable, so a nontrivial minimal Hall circuit
cannot occur there.

## 2. Accessible-bag saturation

### Theorem 2.1 (external-neighbour absorption trichotomy)

Let

\[
 z\in N_H(B)\setminus V(\mathcal M).
\]

Then at least one of the following holds.

1. There is a labelled \(K_r\)-model with more contacted bags.
2. There is, at the same contact count, a Hall circuit of order smaller
   than \(|I|\).
3. Replacing \(B\) by \(B\cup\{z\}\) preserves the contact count and
   circuit \(I\), and strictly increases \(|B|\).

Consequently, after outcomes 1--2 have been excluded and \(|B|\) has
been locally maximized,

\[
 N_H(B)\subseteq V(\mathcal M).
\tag{2.1}
\]

Equivalently, the locally saturated accessible bag has no neighbour
outside the model.

#### Proof

Replace \(B\) by

\[
                         B^+=B\cup\{z\}.
\tag{2.2}
\]

The new set is connected, is disjoint from every other old branch bag,
and retains every old interbag edge.  Hence replacing \(B\) by \(B^+\)
gives another labelled \(K_r\)-model.  The set of contacted **bags** is
unchanged.  This remains true when \(z\in N_G(v)\), because \(B\) was
already contacted; it merely acquires an additional root.  The old label
family \(I\) still consists of uncontacted bags.

If \(I\) is linkable relative to the new model, absorb that linkage
into its terminal bags; this is outcome 1.  Otherwise choose an
inclusion-minimal nonlinkable set \(J\subseteq I\) for the new model.
It is a Hall circuit.  If \(|J|<|I|\), outcome 2 holds.  The only
remaining possibility is \(|J|=|I|\), and then \(J=I\).  Thus the new
model/circuit pair has the same first two coordinates, while

\[
                         |B^+|=|B|+1,
\]

which is outcome 3.  At a local maximum of the third coordinate it is
impossible, proving (2.1) under the stated exclusion of outcomes 1--2.
\(\square\)

### Corollary 2.2 (connected-set form)

No nonempty connected set

\[
 D\subseteq V(H)-V(\mathcal M)
\]

can have an edge to \(B\) after the two primary outcomes have been
excluded and \(|B|\) locally maximized.

#### Proof

The endpoint in \(D\) of such an edge already contradicts Theorem
2.1. \(\square\)

The statement deliberately concerns vertices, not contracted quotient
shores.  Edges from \(D\) to foreign model bags, to Hall-interface
vertices, or to other off-model components do not affect the absorption
move.

## 3. Application to the source-tight lock

Use the notation of the source-tight outcome of Theorem 4.4 in
`hadwiger_B_gated_capacity_state.md`.  Thus

\[
 R=N_G(v)-Q=X\mathbin{\dot\cup}Y,\qquad |Y|=2,
\]

\(Y\) separates \(X\) from the portal set \(P\subseteq B\), and
every component \(C\) of \(U-Y\) satisfies

\[
 N_G(C)\subseteq Y\cup P,
 \qquad N_G(C)\cap P\ne\varnothing.
\tag{3.1}
\]

The second assertion is Corollary 4.6 of that note; it does not require
\(|P|=r-1\).  Moreover

\[
 C\cap N_G(v)=\varnothing,
\tag{3.2}
\]

because every neighbourhood root outside the old model belongs to
\(X\cup Y\), while \(C\subseteq U-Y\) and \(U\cap X=\varnothing\).

### Theorem 3.1 (the source-tight lock forces a primary descent)

If the source-tight outcome has \(P\ne\varnothing\), then it yields one
of

1. a model with more contacted bags;
2. a Hall circuit of smaller order at the same contact count; or
3. a strict same-coordinate enlargement of \(B\).

In particular it cannot occur after outcomes 1--2 have been excluded and
\(|B|\) has been locally maximized.

#### Proof

By definition, \(P=N_H(U)\cap B\).  Choose an edge \(up\) with
\(u\in U\) and \(p\in P\subseteq B\).  The vertex \(u\) lies outside
the old model.  Apply Theorem 2.1 to \(u\).  Notice that no distinction
is needed between \(u\in Y\) and a root-free vertex of \(U-Y\): adding
an extra root to an already contacted bag does not change the contact
count. \(\square\)

### Corollary 3.2 (the portal-surplus multicomponent branch closes)

In particular, the source-tight branch with

\[
 |P|\ge r
\]

cannot survive the local contact/circuit/bag normalization (whether or
not \(U-Y\) is empty).  An occurrence of this branch yields one of

1. more contacted bags;
2. a Hall circuit of smaller order; or
3. a strict enlargement of the accessible bag with the first two
   potential coordinates unchanged.

Iterating the third outcome terminates because \(G\) is finite, although
an enlargement may leave the source-tight description before it
terminates.  The rigorous conclusion is the displayed descent, not by
itself a \(K_{r+1}\)-minor.  Thus no component-portal domination case
analysis is needed in a locally normalized portal-surplus branch.

## 4. Scope

The proof is uniform in \(r\).  It uses neither the number of portal
neighbours of a component nor the two-component omitted-bag packing.
It applies equally to \(|P|=r-1\), \(|P|\ge r\), and nonexact portal
sets.

The gate-only case \(U-Y=\varnothing\) is included: a gate in \(Y\)
adjacent to a portal of \(B\) is itself an absorbable external neighbour.
The Hall circuit may change after that absorption, but Theorem 2.1 records
that event exactly as contact augmentation or a smaller-circuit outcome;
it is not silently assumed away.
