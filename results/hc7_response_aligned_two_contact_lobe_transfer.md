# Response-aligned transfer from two contacts into one branch set

**Status:** written proof; separate internal audit GREEN in
[`hc7_response_aligned_two_contact_lobe_transfer_audit.md`](hc7_response_aligned_two_contact_lobe_transfer_audit.md).
This is a label-preserving branch-set
exchange inside one fixed graph.  It applies to either the independent edge
pair or the incident edge pair returned by the labelled first-hit exposure
compression theorem.  It proves that a root-free connected/co-connected
split separating the two contact endpoints always exists.  It does not
reduce the resulting owner set, synchronize colourings across opposite
shores, or prove `HC_7`.

## 1. Setting

Let `G` have a spanning labelled `K_7`-minus-one-edge model with branch
sets

\[
                 X,\ Y,\ D,\ U,\ F_1,\ F_2,\ F_3.       \tag{1.1}
\]

Thus these seven sets partition `V(G)`, each induces a connected subgraph,
and every two are adjacent except possibly `X` and `Y`.  Fix a prescribed
root `r_B` in every branch set `B`.  Let `Pi` be a selected equality
partition on a fixed literal boundary, and let `Z` be a fixed connected
response kernel contained in `D`.  The partition and kernel are literal
objects in `G`; changing only the ownership of vertices between the branch
sets in (1.1) does not change them.

Suppose there are two distinct edges

\[
                         c_1u_1,\ c_2u_2,                \tag{1.2}
\]

where `c_1,c_2` belong to `Z` and `u_1,u_2` are distinct vertices of `U`.
The vertices `c_1,c_2` may coincide.  Thus (1.2) includes both an
independent exposure pair and an incident exposure pair.

Let `W` be a nonempty proper subset of `U` such that

1. `G[W]` and `G[U-W]` are connected;
2. `r_U` does not belong to `W`; and
3. after possibly interchanging the subscripts in (1.2),

   \[
                             u_2\in W,
                 \qquad      u_1\in U-W.                \tag{1.3}
   \]

The **owner set** of `W` is

\[
 \Omega(W)=
 \{R\in\{X,Y,F_1,F_2,F_3\}:E_G(U-W,R)=\varnothing\}.    \tag{1.4}
\]

Equivalently, `R` lies in `Omega(W)` precisely when moving `W` out of `U`
would remove the old `U`--`R` adjacency unless that adjacency is rebuilt by
the exchange.  Since the old model contains a `U`--`R` edge, every member
of `Omega(W)` is adjacent to `W`.

## 2. Two-contact transfer theorem

### Theorem 2.1 (response-aligned lobe transfer)

In the setting above, if

\[
                              |\Omega(W)|\le 1,           \tag{2.1}
\]

then one of the following holds.

1. The seven displayed sets can be changed explicitly into a `K_7`-minor
   model in `G`.
2. They can be changed explicitly into another spanning labelled
   `K_7`-minus-one-edge model with the same possible missing pair `X,Y`,
   the same prescribed roots, the same selected partition `Pi`, and the
   same response kernel `Z`, but with `U` replaced by the proper connected
   subset `U-W`.

In particular, outcome 2 strictly decreases the order of the branch set
labelled `U` while preserving the selected colouring response literally.

#### Proof

If `X` and `Y` are adjacent in the original model, the seven sets in
(1.1) already form a `K_7`-minor model.  Hence assume that `X` and `Y` are
anticomplete.

First suppose that `Omega(W)` is empty.  Use the following seven branch
sets:

\[
       X,\quad Y,\quad D\cup W,\quad U-W,
       \quad F_1,\quad F_2,\quad F_3.                    \tag{2.2}
\]

The set `D union W` is connected through the edge `c_2u_2`, and `U-W` is
connected by hypothesis.  The edge `c_1u_1` realizes the adjacency between
these two new branch sets.  For every
`R in {X,Y,F_1,F_2,F_3}`, the adjacency from `U-W` to `R` survives because
`Omega(W)` is empty.  Enlarging `D` cannot destroy any of its old
adjacencies, and all remaining adjacencies are unchanged.  The root `r_U`
remains in `U-W`; all other prescribed roots remain in their old sets.
Thus (2.2) is the required smaller spanning labelled model.

Now suppose that `Omega(W)={R}`.  Replace `R` and `U` by

\[
                             R'=R\cup W,
                 \qquad      U'=U-W.                    \tag{2.3}
\]

The seven branch sets are therefore, according to the value of `R`,

\[
\begin{array}{ll}
 X,\ Y,\ D,\ U',\ F_k\cup W,\ F_\ell,\ F_m,
   &\text{if }R=F_k\text{ and }\{k,\ell,m\}=\{1,2,3\};\\[2mm]
 X\cup W,\ Y,\ D,\ U',\ F_1,\ F_2,\ F_3,
   &\text{if }R=X;\\[2mm]
 X,\ Y\cup W,\ D,\ U',\ F_1,\ F_2,\ F_3,
   &\text{if }R=Y.
\end{array}                                             \tag{2.4}
\]

The set `R'` is connected because `W` is connected and, by (1.4), `W` is
adjacent to `R`.  The set `U'` is connected by hypothesis.  Because `U`
is connected and both sides of its partition are nonempty, there is an
edge between `W` and `U-W`; this realizes the new `R'`--`U'` adjacency.
The companion edge `c_1u_1` retains the `D`--`U'` adjacency.  Every
`U'`--`R_0` adjacency with `R_0 != R` survives by the definition of
`Omega(W)`.  Enlarging `R` preserves all of its old required adjacencies,
and every other model adjacency is unchanged.

If `R=F_k`, the first line of (2.4) is therefore a smaller spanning
labelled `K_7`-minus-one-edge model with possible missing pair `X,Y`.
If `R=X` and `W` is adjacent to `Y`, the second line of (2.4) is a
`K_7`-minor model; if `W` is anticomplete to `Y`, it is instead the same
labelled `K_7`-minus-one-edge model.  The case `R=Y` is symmetric.

No prescribed root is moved out of its labelled branch set: the only root
which could lie in `W` is `r_U`, and it was excluded by hypothesis.  In
every nonterminal case `U'=U-W` is proper.  Finally, neither the graph nor
the fixed boundary colouring is altered, and `Z` remains a connected
subgraph of the branch set labelled `D`.  Hence `Pi` and `Z` persist
literally.  This proves the theorem. \(\square\)

## 3. Extremal consequence

Fix `G`, the labels and roots in (1.1), the selected partition `Pi`, and the
response kernel `Z`.  Consider all spanning labelled
`K_7`-minus-one-edge models compatible with these fixed data, and choose one
with `|U|` minimum.  Suppose that this chosen model contains the two edges
in (1.2).  The competing model produced below need not retain that edge
pair; it only has to retain the fixed trace, kernel, labels, and roots.

### Lemma 3.1 (a root-free connected split always exists)

There is a nonempty proper subset `W` of `U` such that

1. `G[W]` and `G[U-W]` are connected;
2. `W` does not contain `r_U`; and
3. `W` contains exactly one of `u_1,u_2`.

#### Proof

Take a spanning tree `T` of the connected graph `G[U]`, and let `P` be its
unique `u_1`--`u_2` path.  Choose any edge `e` of `P`.  The two components
of `T-e` are nonempty, one contains `u_1`, and the other contains `u_2`.
Exactly one of them does not contain `r_U`; let `W` be its vertex set.
The trees `T[W]` and `T[U-W]` show that both induced host subgraphs are
connected.  Thus `W` has all three stated properties. \(\square\)

### Corollary 3.2 (multi-owner or root trap)

Assume that `G` has no `K_7` minor.  For every connected bipartition

\[
                             U=W\mathbin{\dot\cup}(U-W)  \tag{3.1}
\]

which separates `u_1` from `u_2`, orient the bipartition so that `W` is the
side not containing `r_U`.  Then

\[
                              |\Omega(W)|\ge2.           \tag{3.2}
\]

Consequently, in a minimum model every root-free connected/co-connected
piece separating the two persistent `U`-endpoints wholly owns at least two
of the five adjacencies from `U` to
`X,Y,F_1,F_2,F_3`.  Any attempted transfer which does not expose this
multi-owner obstruction must instead fail because the proposed piece
contains the prescribed root or because it is not connected and
co-connected in `U`.  Moreover, Lemma 3.1 shows that at least one such
root-free connected/co-connected piece always exists, so a minimum
`K_7`-minor-free model necessarily contains an actual multi-owner piece.

#### Proof

The root belongs to exactly one side of (3.1), so the stated orientation is
well-defined.  Relabel the two edges in (1.2), if necessary, so that (1.3)
holds.  If `|Omega(W)|<=1`, Theorem 2.1 gives either a `K_7`-minor model or
a compatible spanning labelled model with branch set `U-W` in place of
`U`.  The first outcome contradicts the hypothesis and the second
contradicts the minimality of `|U|`.  Hence (3.2) holds. \(\square\)

## 4. Exact contribution and remaining gate

The theorem is a strict, label-and-response-preserving descent whenever a
root-free connected split separating the two persistent contact endpoints
owns at most one other model adjacency.  Its obstruction is exact: every
such split must own at least two named adjacencies, or the split is blocked
by the prescribed root or by internal connectivity.

Once labelled first-hit exposure compression supplies the two persistent
contacts, Lemma 3.1 produces a set `W` satisfying the connectivity and root
hypotheses.  In a minimum `K_7`-minor-free model Corollary 3.2 then forces
`|Omega(W)|>=2`.  What remains unproved is any mechanism that releases one
of these owned adjacencies.  The remaining cross-shore gate is therefore to
use the family of proper-minor colouring responses to do one of the
following:

1. create a split with owner set of order at most one, activating Theorem
   2.1;
2. turn the full neighbourhood of an owner piece into an exact order-seven
   separation carrying a boundary partition extendable through both
   closed shores; or
3. allocate five response paths to five distinct literal model labels and
   invoke the existing labelled absorption theorem.

This note proves none of those three alternatives by itself.
