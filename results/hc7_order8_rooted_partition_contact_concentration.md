# Rooted connected partitions concentrate the enlarged-boundary contacts

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_rooted_partition_contact_concentration_audit.md`](hc7_order8_rooted_partition_contact_concentration_audit.md).
This is an
unbounded conditional reduction inside the ordered order-eight
opposite-response interface.  It does not prove `HC_7`.

## 1. Setting

Let `G` be a seven-connected graph satisfying

\[
 \chi(G)=7,\qquad K_7\not\preccurlyeq G,
 \qquad \chi(M)\le 6\text{ for every proper minor }M\text{ of }G.
 \tag{1.1}
\]

Suppose

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad E_G(L,R)=\varnothing,
 \tag{1.2}
\]

where `G[L]` and `G[R]` are connected and

\[
 S=\{d,e,x_d,y_d,x_e,y_e,x_0,y_0\}.
 \tag{1.3}
\]

Assume that `G[S]` contains the two vertex-disjoint triangles

\[
                  d x_d y_d d,
              \qquad e x_e y_e e.                     \tag{1.4}
\]

Let `P_0,P_1` be vertex-disjoint adjacent connected subgraphs of `G[R]`,
each adjacent to every literal vertex of `S`.  Suppose

\[
                         L=E\mathbin{\dot\cup}D,        \tag{1.5}
\]

where `G[E]` and `G[D]` are connected and adjacent, and

\[
 N_G(E)\cap S=S-\{e\},
 \qquad
 N_G(D)\cap S=S-\{d\}.                                \tag{1.6}
\]

Put

\[
 W=N_G(E)\cap D,
 \qquad
 B=N_G(E)=(S-\{e\})\mathbin{\dot\cup}W,
 \qquad |W|\ge2.                                      \tag{1.7}
\]

Assume the final structural outcome of the audited
[positive-boundary-excess reduction](../results/hc7_order8_positive_excess_frozen_outer_shore.md):
the graph `G-B` has exactly two components, `E` and a connected set `C`, and
the component `C` is adjacent to every vertex of `B` and contains
`P_0\cup P_1`.  Now let

\[
                         C=Q_0\mathbin{\dot\cup}Q_1     \tag{1.8}
\]

be any partition such that `G[Q_0]` and `G[Q_1]` are connected and
`V(P_i)\subseteq Q_i` for `i=0,1`.

For `A\subseteq V(G)` and `X\subseteq V(G)-A`, say that `A` is **full to
`X`** when every vertex of `X` has a neighbour in `A`.

## 2. The contact-concentration theorem

### Theorem 2.1

Under the hypotheses of Section 1, let `j` be the unique index for which
`e\in Q_j`.  Then

\[
              D-W\subseteq Q_j,
        \qquad Q_{1-j}\subseteq R,                     \tag{2.1}
\]

and the two rooted parts have the exact boundary contacts

\[
 N_G(Q_j)\cap B=B,
 \qquad
 N_G(Q_{1-j})\cap B=S-\{e\}.                          \tag{2.2}
\]

Consequently every member of `W` has neighbours in exactly one of the two
parts, namely `Q_j`.  In particular:

1. no rooted connected partition satisfying (1.8) shares even one `W`
   contact between its two parts;
2. changing which labelled rooted side contains `e`, when both choices are
   admissible, reverses the owner of all `W` contacts simultaneously; and
3. maximizing the number of shared `W` contacts, with any secondary rank
   based only on the two part orders, cannot give a contact-improving
   connected repartition.

#### Proof

Removing `B` from the vertex partition (1.2), (1.5) leaves

\[
 V(G)-B=E\mathbin{\dot\cup}(D-W)
              \mathbin{\dot\cup}\{e\}\mathbin{\dot\cup}R. \tag{2.3}
\]

The only component in (2.3) other than `E` is `C`.  Hence

\[
                  C=(D-W)\mathbin{\dot\cup}\{e\}
                         \mathbin{\dot\cup}R.           \tag{2.4}
\]

There are no edges from `D-W` to `R`, by (1.2).  Thus every path in `G[C]`
from a vertex of `D-W` to a vertex of `R` contains `e`.

The set `Q_{1-j}` contains the nonempty subgraph `P_{1-j}` of `R`.  If it
also contained a vertex of `D-W`, its connectedness would give a path in
`G[Q_{1-j}]` from `D-W` to `R`.  Such a path would contain `e`, contrary to
`e\in Q_j`.  Therefore `Q_{1-j}\subseteq R`, and (2.4) gives
`D-W\subseteq Q_j`.  This proves (2.1).

Each `P_i` supplies `Q_i` with a neighbour at every literal vertex of `S`.
Now let `w\in W`.
The set `C` is full to `B`, so `w` has a neighbour in `C`.  The absence of
`L`--`R` edges gives

\[
                         N_G(w)\cap C
                    \subseteq (D-W)\cup\{e\}.           \tag{2.5}
\]

The right side of (2.5) lies in `Q_j`, while `Q_{1-j}\subseteq R` has no
neighbour at `w`.  Hence `Q_j` is full to `W` and `Q_{1-j}` misses every
member of `W`.  Together with the contacts supplied by `P_i`, this is
exactly (2.2).
The three consequences follow for every admissible rooted connected
partition, so they are independent of how the partition is optimized.
\(\square\)

## 3. Exact Hall consequence and response provenance

Let `uv` be an edge with `u\in E` and `v\in B`, let `psi` be a proper
six-colouring of `G-uv`, and let `Sigma` be its equality partition on `B`.
Choose a maximum clique `U` among the singleton blocks of `Sigma`, list the
remaining blocks as `C_1,\ldots,C_t`, and put

\[
 F_i=C_i\cup\{z\in U:E_G(z,C_i)=\varnothing\}.          \tag{3.1}
\]

Thus `t` is the full-subgraph demand and `F_i` is the required literal
boundary set for the block `C_i`.  Join `Q_k` to `C_i` in the incidence
graph precisely when `Q_k` is full to `F_i`.

### Proposition 3.1

The partition `Sigma` extends through `G[C\cup B]` and is rejected by the
intact graph `G[E\cup B]`.  Its incidence graph has no matching saturating
`C_1,\ldots,C_t`.  Moreover:

1. `Q_j` is incident with every `C_i`;
2. `Q_{1-j}` is incident with `C_i` if and only if `F_i\cap W=\varnothing`;
3. one has `t\ge2`; and
4. when `t=2`, Hall failure occurs if and only if

   \[
                         F_1\cap W\ne\varnothing,
                   \qquad F_2\cap W\ne\varnothing.     \tag{3.2}
   \]

In particular the alternative in which one required boundary set is
supported by neither rooted part, including its crossed two-contact form,
cannot occur.

#### Proof

Such a colouring exists because `G-uv` is a proper minor.  Every proper
six-colouring of `G-uv` gives `u,v` one colour; otherwise the
edge `uv` could be restored and would six-colour `G`.  The deleted edge has
an endpoint in `E`, so `psi|G[C\cup B]` is proper and induces `Sigma`.
If `Sigma` extended through the intact graph `G[E\cup B]`, a permutation of
the six colour names would align the two boundary assignments and glue them
to a proper six-colouring of `G`.  Thus the asserted response orientation is
exact.

The demand is nonzero: `|B|=7+|W|\ge9`, while `Sigma` has at most six
blocks, so at least one block is nonsingleton and therefore is not
represented in the singleton clique `U`; hence `t\ge1`.  Also, because
`G[C]` is connected and `C=Q_0\mathbin{\dot\cup}Q_1`, the two connected
supports `Q_0,Q_1` are adjacent.  The transported-partition Hall reflection
theorem, applied with coloured shore `C`, opposite shore `E`, and these two
supports, says that
a matching saturating all `C_i` would extend `Sigma` through the intact
`E`-shore.  Hence no such matching exists.

By (2.2), `Q_j` is full to `B`, so it is incident with every `C_i`.
The other part is full to `S-\{e\}` and misses all of `W`; since
`B=(S-\{e\})\dot\cup W`, it is full to `F_i` exactly when `F_i` contains no
member of `W`.  This proves items 1 and 2.

For `t=1`, the universal support `Q_j` gives a saturating matching, contrary
to the preceding Hall failure.  Hence `t\ge2`.  When `t=2`, the universal
support can be assigned to either block.  A matching saturating both blocks
exists exactly when `Q_{1-j}` is incident with at least one of them.  Item 2
therefore gives (3.2).  Since every block has the universal support `Q_j`,
no block is isolated in the incidence graph. \(\square\)

## 4. Components on the `D-W` side

Put

\[
                         T=(S-\{d\})\mathbin{\dot\cup}W. \tag{4.1}
\]

Notice that

\[
                              |T|=7+|W|=|B|.             \tag{4.2}
\]

### Theorem 4.1

Let `Z` be a component of `G[D-W]`.  Then

\[
                              N_G(Z)\subseteq T.         \tag{4.3}
\]

The set `N_G(Z)` is the boundary of an actual separation, and

\[
                              7\le |N_G(Z)|\le |B|.      \tag{4.4}
\]

For every edge `xy` with `x\in Z` and `y\in N_G(Z)`, every proper
six-colouring of `G-xy` has `x,y` in one colour.  Its equality partition on
`N_G(Z)` extends both through `G-Z` and through
`G[Z\cup N_G(Z)]-xy`, and is rejected by the intact graph
`G[Z\cup N_G(Z)]`.

Consequently at least one of the following holds.

1. `|N_G(Z)|=7`, giving a generic exact order-seven response interface.
2. `8\le |N_G(Z)|<|B|`, giving a strict boundary-order response descent
   from `B`.
3. `N_G(Z)=T`; in this equality case `Z` is full to every vertex of
   `(S-\{d\})\cup W`.

If distinct components `Z_0,Z_1` of `G[D-W]` both have the equality in
outcome 3, then `G` contains the following explicit `K_7`-minor model:

\[
\begin{array}{c}
 Z_0\cup\{x_d\},\quad Z_1\cup\{y_d\},\quad
 V(P_0)\cup\{x_0\},\quad V(P_1)\cup\{y_0\},\\[2mm]
 \{e\},\quad\{x_e\},\quad\{y_e\}.
\end{array}                                             \tag{4.5}
\]

Thus, outside an explicit `K_7`-minor model, an exact order-seven response,
or a strict boundary-order response descent, either `D-W` is empty or
`G[D-W]` is connected and

\[
                          N_G(D-W)=T.                    \tag{4.6}
\]

#### Proof

A vertex of `Z` has no neighbour in `E`, since every vertex of `D` with an
`E`-neighbour belongs to `W`.  It has no neighbour in `R` by (1.2), no
neighbour in another component of `G[D-W]`, and no neighbour at `d` by
(1.6).  Every remaining possible neighbour lies in `(S-\{d\})\cup W`.
This proves (4.3).

The nonempty set `R` has no neighbour in `Z`, so it survives outside
`Z\cup N_G(Z)`.  Hence `N_G(Z)` is an actual separation boundary.
Seven-connectivity and (4.2)--(4.3) give (4.4).

Fix a crossing edge `xy` and any proper six-colouring of `G-xy`; at least one
exists by (1.1) because `G-xy` is a proper minor.  Its ends have one colour,
since otherwise restoring `xy` would six-colour `G`.  The
outside restriction colours `G-Z`, and its inside restriction colours
`G[Z\cup N_G(Z)]-xy`.  If their equality partition on `N_G(Z)` extended
through the intact graph `G[Z\cup N_G(Z)]`, a global permutation
of colour names would align the two boundary assignments and glue them,
again six-colouring `G`.  This proves the response statement.

If (4.3) is proper, then `|N_G(Z)|<|T|=|B|`; (4.4) gives outcomes 1 or 2.
Otherwise equality holds throughout (4.3), giving outcome 3.

Now suppose `Z_0,Z_1` are two equality components.  Each of the four
connected subgraphs

\[
                            Z_0,\quad Z_1,\quad P_0,\quad P_1             \tag{4.7}
\]

is adjacent to every vertex of `S-\{d\}`.  Adjoin the four distinct vertices
`x_d,y_d,x_0,y_0` bijectively as displayed in (4.5).  The four resulting
sets are disjoint and connected.  Any two are adjacent because the
underlying connected subgraph of either one has a neighbour at the boundary
vertex adjoined to the other.  Each is adjacent to the three singleton
sets `e,x_e,y_e`, and those singleton sets form the triangle in (1.4).
Therefore (4.5) consists of seven pairwise adjacent connected branch sets.

If there is no terminal model or response descent, every component of
`G[D-W]` has outcome 3 and there cannot be two of them.  This proves (4.6).
\(\square\)

## 5. The existing cycle-completion theorem applies

Put

\[
                              F=S-\{d,e\}.                \tag{5.1}
\]

### Corollary 5.1

There is a partition

\[
                         R=R_0\mathbin{\dot\cup}R_1      \tag{5.2}
\]

such that `G[R_0]` and `G[R_1]` are connected and adjacent and
`V(P_i)\subseteq R_i` for `i=0,1`.  For any such partition, the four sets

\[
             R_0,\qquad R_1,\qquad E\cup\{d\},\qquad D\cup\{e\}             \tag{5.3}
\]

are pairwise disjoint connected branch sets, are pairwise adjacent, and are
each adjacent to every literal vertex of `F`.

Consequently the standing hypothesis `K_7\not\preccurlyeq G` forces `G[F]`
to be a forest.

#### Proof

Apply the audited
[cycle-completion theorem](../results/hc7_adjacent_full_pair_cycle_completion.md)
with its two one-defect subgraphs chosen as `A_d=D` and `A_e=E`, and its
two boundary-full rooted subgraphs chosen as `P_0,P_1`.  Its adjacent-cover
normalization gives (5.2), and its four off-cycle branch sets are precisely
the four sets in (5.3).  Its Theorem 3.1 converts any cycle in `G[F]` into
the remaining three branch sets of an explicit `K_7`-minor model.  The
`K_7`-minor-free hypothesis therefore makes `G[F]` a forest. \(\square\)

## 6. Exact contribution and trust boundary

Theorem 2.1 shows that the proposed rooted connected-bipartition exchange
cannot increase shared `W` contacts: the exact `L`--`S`--`R` geometry makes
that objective identically zero.  Proposition 3.1 removes the crossed
isolated Hall form and identifies the complete demand-two residue: both
required boundary sets must contain a literal member of `W`.

Theorem 4.1 supplies the available host-level descent.  Every component of
`D-W` gives an exact order-seven response or a smaller response boundary
unless it is full to the reversed literal boundary `(S-\{d\})\cup W`; two
such equality components already give the explicit model (4.5).  The sole
structural survivor has `D-W` empty, or has one connected equality component
which is a strict vertex subset of `D` because `W` is nonempty.

Corollary 5.1 is independent of that residual case analysis: throughout the
whole setting of Section 1, the six-vertex boundary graph
`G[S-\{d,e\}]` is a forest.  A single cycle there combines with four literal
connected branch sets to give an explicit `K_7`-minor model.

That strict vertex containment is **not** a recursive rooted order-eight
interface.  The equality boundary replaces `d` by `e`, the connected set
`D-W` contains neither prescribed subgraph `P_0,P_1`, and every rooted
partition still places it on the side containing `e`.  The result does not
produce compatible closed-shore colourings, repair demand at least three,
or close the final two-piece Hall obstruction.  Any further theorem must use
the operation-specific proper-minor responses or additional literal
branch-set geometry, rather than shared-contact repartition alone.

## 7. Dependencies

- [positive boundary excess with one partitioned opposite component](../results/hc7_order8_positive_excess_frozen_outer_shore.md)
- [transported-partition Hall reflection](../results/hc7_transported_partition_hall_reflection.md)
- [generic exact-seven response restart](../results/hc7_generic_exact7_response_restart.md)
- [cycle completion from two connected shores](../results/hc7_adjacent_full_pair_cycle_completion.md)
- seven-connectivity and proper-minor six-colourability
