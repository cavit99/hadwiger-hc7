# Surplus-sensitive density at an exact seven-boundary

**Status:** written proof; separate internal audit GREEN in
[`hc7_direct_entry_surplus_density_audit.md`](hc7_direct_entry_surplus_density_audit.md).

This note refines the density calculation in
[`hc7_tight_shore_order_bound.md`](hc7_tight_shore_order_bound.md).  It
retains the total internal list-degree excess, all edges of the literal
seven-vertex boundary, and the number of boundary-colour incidences in the
open shore.  The last quantity is particularly useful when the open shore
contains two disjoint connected subgraphs adjacent to every boundary
vertex.  The result is an order bound, not a colouring synchronization
theorem, and it does not prove `HC_7`.

## 1. Setting and notation

Let `G` be a seven-connected graph with no `K_7` minor and suppose

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad |S|=7,\qquad E_G(L,R)=\varnothing,             \tag{1.1}
\]

where `L,R` are nonempty.  Let `psi:S->[6]` be the boundary restriction of
a proper six-colouring of a subgraph containing `G[S]`, and define

\[
 A(v)=[6]\setminus
 \{\psi(s):s\in N_G(v)\cap S\}
 \qquad(v\in R).                                      \tag{1.2}
\]

Assume that `G[R]` is connected, is not `A`-colourable, and is minimal by
vertex inclusion with that property.  Put

\[
\begin{aligned}
 c(v)&=\bigl|\{\psi(s):s\in N_G(v)\cap S\}\bigr|,\\
 \rho(v)&=|N_G(v)\cap S|-c(v),\\
 \varepsilon(v)&=d_{G[R]}(v)-|A(v)|,\\
 C&=\sum_{v\in R}c(v),\qquad
 P=\sum_{v\in R}\rho(v),\qquad
 E=\sum_{v\in R}\varepsilon(v),\\
 \Delta&=\sum_{v\in R}(d_G(v)-9),\\
 r&=|R|,\qquad s=|E(G[S])|,\qquad
 a=\operatorname{comp}(G[L]).
\end{aligned}                                         \tag{1.3}
\]

Minimal list-uncolourability gives

\[
 d_{G[R]}(v)\ge |A(v)|=6-c(v),
\]

so every `epsilon(v)` is a nonnegative integer.  Let `b` be the number of
colours used by `psi` on `S`.

## 2. The exact density inequality

### Theorem 2.1 (surplus-sensitive shore bound)

Under (1.1)--(1.3), either some vertex of `R` has degree seven or eight in
`G`, or `Delta>=0` and

\[
       r\le 20-2a-s-\frac C2+\frac E2-\Delta.         \tag{2.1}
\]

The right side of (2.1) is an integer.  Since `a>=1`, in particular

\[
       r\le 18-s-\frac C2+\frac E2-\Delta
        \le18-s+\frac E2.                             \tag{2.2}
\]

If `G[R]` contains `t` pairwise vertex-disjoint connected subgraphs, each
adjacent to every literal vertex of `S`, then

\[
       C\ge tb
\]

and hence

\[
       r\le
       \left\lfloor20-2a-s-\frac{tb}{2}
                    +\frac E2-\Delta\right\rfloor.   \tag{2.3}
\]

In the direct-entry orientation with two such connected subgraphs, the
weaker component-free consequence is

\[
       r\le 18-s-b+\frac E2-\Delta.                   \tag{2.4}
\]

In particular, since the nonempty boundary uses at least one colour,

\[
       r\le17-s+\frac E2-\Delta                       \tag{2.5}
\]

holds in that orientation without knowing its exact boundary partition.
Still in this two-subgraph orientation, `psi|S` is proper, so one also has
the assignment-free form

\[
       r\le18-s-\chi(G[S])+\frac E2-\Delta.            \tag{2.6}
\]

#### Proof

If `v in R` has degree at most eight, seven-connectivity gives
`7<=d_G(v)<=8`.  Since `v` has no neighbour in the nonempty set `L`, its
full neighbourhood separates `{v}` from `L`.  This is the first outcome.

Assume from now on that every vertex of `R` has degree at least nine.  The
definitions give the exact identities

\[
\begin{aligned}
 2|E(G[R])|
   &=\sum_{v\in R}(6-c(v)+\varepsilon(v))
     =6r-C+E,                                         \tag{2.7}\\
 |E_G(R,S)|&=C+P,                                     \tag{2.8}\\
 d_G(v)&=6+\varepsilon(v)+\rho(v).                    \tag{2.9}
\end{aligned}
\]

The degree assumption makes `Delta` nonnegative.  Summing (2.9) gives the
exact identity

\[
                         E+P=3r+\Delta.                \tag{2.10}
\]

Every component of `G[L]` has neighbourhood contained in `S` and separates
itself from the nonempty set `R`.  Seven-connectivity therefore makes every
one of the `a` components adjacent to all seven vertices of `S`.  Contract
each component to one vertex and suppress loops and parallel edges.  The
resulting simple minor `H` has `r+7+a>=9` vertices.  No edge counted below
is lost:

\[
\begin{aligned}
 |E(H)|
  &=|E(G[R])|+|E_G(R,S)|+|E(G[S])|+7a\\
  &=3r+\frac C2+\frac E2+P+s+7a\\
  &=6r+\frac C2-\frac E2+\Delta+s+7a,                 \tag{2.11}
\end{aligned}
\]

where the last line uses (2.10).  Mader's exact small-clique-minor bound
applies to the `K_7`-minor-free graph `H`:

\[
 |E(H)|\le5|V(H)|-15=5r+20+5a.                        \tag{2.12}
\]

Combining (2.11) and (2.12) gives the sharp counted inequality

\[
       2r+C-E+2s+2\Delta+4a\le40,                     \tag{2.13}
\]

and proves (2.1).  Equation (2.7) shows that
`E-C` is even, so the right side of (2.1) is indeed integral.  Dropping
the nonnegative terms `C/2` and `Delta`, and using `a>=1`, proves (2.2).

Finally, fix one colour used on `S` and one of the `t` disjoint
boundary-full connected subgraphs.  Some vertex of that subgraph is
adjacent to a boundary vertex of the fixed colour, and hence contributes
one incidence to `C`.  Doing this for all `b` colours and all `t`
vertex-disjoint subgraphs gives `C>=tb`.  Substitution proves (2.3) and
(2.4).  Finally `b>=chi(G[S])` because the boundary assignment is proper;
this proves (2.6).  \(\square\)

## 3. What the two residual partitions do and do not imply

Suppose that the **same list-defining assignment `psi`** induces one of the
two high-demand direct-entry partitions

\[
\begin{aligned}
 \Pi_A&=D\mid E_0\mid\{x\}\mid\{y\},\\
 \Pi_B&=D\mid E_0\mid\{x,y\},
 \qquad |D|=3,\quad |E_0|=2.                          \tag{3.1}
\end{aligned}
\]

If the shore contains two disjoint boundary-full connected subgraphs, then
(2.4) gives the concrete bounds

\[
\begin{array}{c|c|c}
 \text{partition}&b&\text{order bound}\\
 \hline
 \Pi_A&4&r\le14-s+E/2-\Delta,\\
 \Pi_B&3&r\le15-s+E/2-\Delta.
\end{array}                                           \tag{3.2}
\]

In the all-tight case `E=0`, these become `r<=14-s-Delta` and
`r<=15-s-Delta`, respectively; when every shore vertex has degree exactly
nine, `Delta=0`.

There is an important state-provenance qualification.  In the current
direct-entry application, the two partitions in (3.1) belong to the
original one-shore colouring, whereas the lists (1.2) are defined from the
new colouring obtained after simultaneously contracting the first and last
path edges.  The two-edge list-critical theorem proves that these two
boundary partitions are different; it does not prove that the new partition
is the other member of (3.1).  Thus (3.2) is a valid conditional
specialization, but it cannot presently be substituted into the proof spine
without an additional state-transfer theorem.

Both partitions in (3.1) only give the boundary-edge restriction

\[
 E(G[D])=E(G[E_0])=\varnothing,
 \qquad xy\notin E(G),
 \qquad s\le16.                                      \tag{3.3}
\]

The upper bound in (3.3) does not improve (2.1), whose right side decreases
as `s` increases.  No positive lower bound on `s` follows from the equality
partition alone.

## 4. Two marked exceptions do not bound the total excess

The separate
[odd-wheel barrier](../barriers/hc7_two_mark_list_excess_barrier.md)
constructs vertex-minimal uncolourable list instances with exactly two
`A^+` exceptions and `E` arbitrarily large.  It realizes the lists through
two deleted crossing edges at a literal exact-seven separation, and the
resulting host is seven-connected.  That host has an explicit `K_7` minor
and is not contraction-critical.  Thus the local list-critical data and the
two marked exceptions do not bound `E`; any further bound must use the
global minor exclusion or proper-minor colouring dynamics.

## 5. External input and trust boundary

The only external extremal input is Mader's theorem for `p<=7`: a simple
`K_p`-minor-free graph on `n>=p` vertices has at most

\[
                    (p-2)n-\binom{p-1}{2}
\]

edges.  Here `p=7` and the constructed minor has `r+7+a>=9` vertices, so
there is no small-order exception.

The theorem does not bound `E` under the full global hypotheses, eliminate
the bounded shore, synchronize the two closed-shore colourings, or preserve
the five named branch-set labels.  Its strongest unconditional contribution
to the current direct-entry branch is the exact inequality (2.1), together
with (2.4) when the number of colours in the list-defining boundary
assignment is known.
