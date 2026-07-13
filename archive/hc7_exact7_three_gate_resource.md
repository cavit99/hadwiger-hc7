# Superseded: literal three-gate resource exchange

This note is retained for provenance.  Its audited content is strictly
subsumed by `../results/hc7_exact7_three_gate_resource_exchange.md`, which
also closes the formerly residual three-lobe cell.

## Status and purpose

This proved and independently audited note attacks the nonplanar three-connected residue left by
`../results/hc7_exact7_rooted_portal_face_closure.md`.  A web completion
may supply a virtual triangle whose edges are absent from the graph.  The
construction below never uses those virtual edges.  It spends actual
components behind the three-vertex gate to repair missing gate adjacencies
inside branch bags.

## 1. Setup

Let `G` be seven-connected with a literal partition

\[
                    V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
                    \qquad |S|=7,                          \tag{1.1}
\]

where there are no `LR` edges.  Suppose `R` contains three pairwise
disjoint connected `S`-full packets `P_1,P_2,P_3`.  Assume `G[L]` is
three-connected and let

\[
                         T=\{t_1,t_2,t_3\}                 \tag{1.2}
\]

be a vertex cut of `L`.  Write `C_1,...,C_c` for the components of
`L-T`, and put

\[
                         Z(X)=N_S(X).                       \tag{1.3}
\]

### Lemma 1.1 (every gate lobe has four labels)

For every `i`,

\[
                         N_L(C_i)=T,
                         \qquad |Z(C_i)|\ge4.              \tag{1.4}
\]

#### Proof

The neighbourhood of `C_i` inside `L` is contained in `T`.  Since `L` is
three-connected and another component of `L-T` exists, fewer than three
gate neighbours would separate `C_i`; hence `N_L(C_i)=T`.

In the whole graph,

\[
                         N_G(C_i)=T\cup Z(C_i),             \tag{1.5}
\]

because the open shores are anticomplete.  This is an actual separator:
another gate lobe and the nonempty opposite shore lie outside
`C_i\cup N_G(C_i)`.  Seven-connectivity gives
`3+|Z(C_i)|\ge7`, proving (1.4). \(\square\)

## 2. Components repair virtual gate edges

Call `U\subseteq T` a **literal gate clique** when `G[U]` is complete;
the empty set and a singleton are allowed.  Say that `U` has portal rank
`|U|` when the family `(Z(u):u\in U)` has a system of distinct
representatives in `S`.

### Theorem 2.1 (gate clique plus lobe budget)

If a literal gate clique `U\subseteq T` satisfies

\[
                         c\ge4-|U|                         \tag{2.1}
\]

and has portal rank `|U|`, then `G` contains a literal `K_7` minor.

#### Proof

Choose one gate lobe `C_0`.  For every vertex
`t\in T-U`, choose a further distinct gate lobe `C_t`.  This is possible
because the number of required lobes is

\[
                         1+|T-U|=4-|U|\le c.               \tag{2.2}
\]

Consider the following four connected sets before adding boundary
anchors:

\[
 C_0,\qquad C_t\cup\{t\}\ (t\in T-U),
       \qquad \{u\}\ (u\in U).                            \tag{2.3}
\]

They are pairwise disjoint.  They are also pairwise adjacent.  The
central lobe `C_0` meets every gate vertex.  If one of two gate bags is
an enlarged bag `C_t\cup\{t\}`, its lobe meets the other gate vertex.
If both are singleton gate bags, their vertices lie in the literal clique
`U`.

The portal-choice sets of `C_0` and of every enlarged gate bag contain
`Z(C_0)` and `Z(C_t)`, respectively, and hence have order at least four
by Lemma 1.1.  The portal-choice sets of the singleton gate bags are
the sets `Z(u)`, `u\in U`.  These four choice sets have a system of
distinct representatives.  Indeed, a subfamily containing a lobe set has
union order at least four, at least its total number of members; a
subfamily consisting only of singleton gate sets satisfies Hall by the
portal-rank hypothesis.

Choose distinct representatives `s_B\in S`, one adjacent to each set
`B` in (2.3), and enlarge that set by `s_B`.  The four enlarged sets
remain disjoint, connected and pairwise adjacent.  Anchor the three
opposite full packets at the remaining three vertices of `S`.  The packet
bags are pairwise adjacent by fullness, and every packet bag meets every
one of the first four bags through its literal boundary anchor.  These are
seven literal clique branch sets. \(\square\)

The theorem repairs a missing gate edge by absorbing a whole lobe into
one of its endpoint bags.  No edge of a web completion is used.

## 3. Exact consequences

### Corollary 3.1 (four or more gate lobes close)

If `c\ge4`, take `U=\varnothing` in Theorem 2.1.  Thus a surviving
three-gate web has at most three lobes.

### Corollary 3.2 (the three-lobe gate has no literal boundary portal)

If `c=3` and some `u\in T` has a neighbour in `S`, take `U=\{u\}`.
Consequently a surviving three-lobe gate satisfies

\[
                             N_S(T)=\varnothing.            \tag{3.1}
\]

### Corollary 3.3 (usable literal gate edges close the two-lobe cell)

If `c=2`, `uv` is a literal edge of `G[T]`, and `Z(u),Z(v)` have distinct
representatives, take `U=\{u,v\}`.  Hence in a surviving two-lobe gate,
the endpoint portal sets of every literal gate edge fail Hall:

\[
       |Z(u)|=0\quad\hbox{or}\quad |Z(v)|=0
       \quad\hbox{or}\quad |Z(u)\cup Z(v)|\le1.            \tag{3.2}
\]

More precisely, failure of a two-set SDR means that one endpoint set is
empty or their union has order one.

### Corollary 3.4 (literal-triangle gate has rank at most one)

If `c\ge2` and `G[T]` is a triangle, then any two gate portal sets with
distinct representatives invoke Theorem 2.1 with a two-vertex gate
clique.  Thus a surviving literal
triangle gate has transversal rank at most one on `(Z(t):t\in T)`.

## 4. Exact remaining gate cells

For the web gate returned by the audited rooted-portal theorem, at least
two lobes exist: the chosen nonempty cell lobe and a lobe containing one
of the four nominated roots outside the three gate vertices.  Theorem 2.1
therefore leaves only:

1. exactly two gate lobes, with no literal gate edge whose endpoints have
   two distinct boundary representatives; or
2. exactly three gate lobes and no direct gate-to-`S` edge at all.

Closing these cells requires splitting one gate lobe into two anchor-bearing
pieces, or producing the matching proper-minor state.  The theorem does not
infer such a split from three-connectivity alone.
