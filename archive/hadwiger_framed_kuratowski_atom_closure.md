# Closure of the full-deletion framed Kuratowski atom

## 1. Result

The framed Kuratowski atom isolated in
`hadwiger_critical_rural_operation_composition.md` cannot occur when its
live torso is the minimum full shore in the sharp
`C_6 dotunion K_1` exact-seven cell.

This is a hand packing theorem; no finite graph enumeration is used.

### Theorem 1.1 (full-deletion Kuratowski-atom closure)

Let `G` be seven-connected, have minimum degree at least seven, and have
no `K_7` minor.  Let `S` be a seven-cut with

\[
             \overline{G[S]}=C_6\mathbin{\dot\cup}K_1,       \tag{1.1}
\]

and let `D` be a minimum-order component behind any seven-cut, chosen as
one of the full components of `G-S`.  Assume:

1. one vertex deletion leaves `D` full to `S`;
2. the audited singleton/full-body atlas applies, so for every
   full-deletion vertex `u in D`,
   \[
          |N_S(u)|\le4;                                     \tag{1.2}
   \]
3. the live graph `G[D]` is a framed Kuratowski atom in the sense of
   Theorem 3.1 of
   `hadwiger_critical_rural_operation_composition.md`; in particular
   \[
          |V(D)|\le6,\qquad |E(G[D])|\le10.                 \tag{1.3}
   \]

Then `G` contains a `K_7` minor, a contradiction.

The assumptions are exactly those supplied when the all-operations-rural
branch of the repeated-owner/joint-edge warehouse descends to the chosen
minimum `C_6 dotunion K_1` shore without losing its active roles.

## 2. Numerical collapse to a five-clique

By the full-deletion propagation theorem, assumption 1 implies that
**every** vertex of `D` is a full-deletion vertex.  In particular every
boundary portal class has multiplicity at least two and (1.2) holds for
every vertex of `D`.

The minimum-fragment theorem gives, for each vertex `u in D`, the strict
singleton surplus

\[
                |N_S(u)|+d_D(u)\ge8.                        \tag{2.1}
\]

The minimum `C_6 dotunion K_1` shore is three-connected, so
`m=|V(D)|>=4`.

### Lemma 2.1

Under (1.2)--(2.1) and (1.3),

\[
                            |V(D)|=5,qquad G[D]\cong K_5,  \tag{2.2}
\]

and every vertex of `D` has exactly four neighbours in `S`.

#### Proof

If `m=4`, then for any `u in D`,

\[
 |N_S(u)|+d_D(u)\le4+3=7,
\]

contrary to (2.1).

If `m=6`, (1.2) and (2.1) give `d_D(u)>=4` for every `u`.  Therefore

\[
                         |E(G[D])|\ge\frac{6\cdot4}{2}=12,
\]

contrary to the ten-edge Kuratowski-atom bound (1.3).

Thus `m=5`.  Now `d_D(u)<=4`, while (1.2) and (2.1) force equality in
both bounds:

\[
                         d_D(u)=4,qquad |N_S(u)|=4.
\]

This holds for every `u`, proving (2.2).  \(\square\)

The six-vertex case is where the dynamic rural theorem is essential.
Strict surplus alone only says that the live graph has minimum degree
four; the framed Kuratowski theorem says simultaneously that it has at
most ten edges, and those inequalities are incompatible.

## 3. Two connected boundary dominators

Write

\[
                        S=C\mathbin{\dot\cup}\{z\},
       \qquad C=\{c_0,c_1,\ldots,c_5\},                    \tag{3.1}
\]

where the missing edges on `C` form the cycle
`c_0c_1...c_5c_0`, and `z` is universal in `G[S]`.

For `u in D`, put

\[
                              P_u=N_S(u).
\]

Lemma 2.1 says that the five sets `P_u` all have order four.

### Lemma 3.1 (connected dominating bipartition)

There is a partition

\[
                              S=X\mathbin{\dot\cup}Y       \tag{3.2}
\]

such that:

1. `G[X]` and `G[Y]` are connected;
2. `E(X,Y)` is nonempty; and
3. every `P_u` meets both `X` and `Y`.

#### Proof

For each two-set `T subseteq C`, consider

\[
                       X_T=\{z\}\cup T,
             \qquad   Y_T=C-T.                            \tag{3.3}
\]

There are `binom(6,2)=15` choices of `Y_T`, while there are only five
portal sets `P_u`.  Choose `T` so that

\[
                              Y_T\ne P_u
                              \quad(u\in D).               \tag{3.4}
\]

The set `X_T` is connected because `z` is adjacent to every cycle
vertex.

The four-set `Y_T` is also connected in `G[S]`.  Indeed every vertex of
`K_6-C_6` has only two nonneighbours, so the induced graph on `Y_T` has
minimum degree at least one.  If it were disconnected it would therefore
be `2K_2`.  Its complement on those four vertices would be a four-cycle.
But that complement is an induced subgraph of the chordless six-cycle,
and no proper four-vertex induced subgraph of a chordless six-cycle is a
four-cycle.  This contradiction proves connectedness.

The edge set between `X_T` and `Y_T` is nonempty because `z in X_T` is
adjacent to every member of `Y_T`.

Finally, `P_u` and `Y_T` are two four-subsets of a seven-set, so they
intersect.  If `P_u` did not meet `X_T`, then, since both `P_u` and
`Y_T=S-X_T` have order four, they would be equal, contrary to (3.4).
Thus every `P_u` meets both sides.  \(\square\)

## 4. The seven branch sets

### Completion of Theorem 1.1

Use as branch sets the five singleton vertices of the clique `D`,
together with the two sets `X,Y` from Lemma 3.1:

\[
                         \{u\}\quad(u\in D),
                         \qquad X,\qquad Y.                \tag{4.1}
\]

The five singleton bags are pairwise adjacent because `G[D]=K_5`.
Both `X` and `Y` are connected.  Lemma 3.1 says that every singleton
bag has an edge to each of `X,Y`, and it also supplies an `X-Y` edge.
Thus the seven sets in (4.1) are pairwise adjacent disjoint connected
branch sets, a `K_7` model.  \(\square\)

## 5. Consequence for the dynamic rural route

Combine Theorem 1.1 with the critical rural-operation trichotomy.
Whenever the localized repeated-owner society is the chosen minimum
`C_6 dotunion K_1` full shore and all its internal edge deletions and
contractions preserve the active four-role frame, the three alternatives
are now:

```text
some operated society is nonrural
    -> labelled rooted split -> K7;
all operated societies and the original society are rural
    -> compatible disk substitution -> two-apex -> six-colourable;
all operated societies are rural but the original is nonrural
    -> framed Kuratowski atom -> Theorem 1.1 -> K7.
```

Hence that entire all-operations-rural minimum-shore family is closed.
The remaining dynamic gate is precisely the one excluded from the
hypotheses: an internal operation which destroys two active extension
roles, or a repeated-owner torso which has not yet been transported to
the minimum full `C_6 dotunion K_1` shore.  Those cases require the
bilateral exact-seven/two-coordinate state-forcing exchange, not further
rural atom analysis.

