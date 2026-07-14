# Barrier: surplus contacts do not force the width-two thin split

## Status

**Verified connectivity-only counterexample.**  An 18-vertex graph satisfies
the literal exact-seven separation, the actual paired-state tree boundary,
seven-connectivity, minimum degree seven, packet vector `(1,2)`, thirty-nine
surplus packet contacts, and every local Dirac neighbourhood inequality.  Its
thin packet nevertheless has no two disjoint connected carriers funding the
two bipartition duties of Lemma 5.2 in
`../results/hc7_exact7_connected_rich_width2_frontier.md`.

The graph deliberately contains a literal `K_7` and is not claimed
contraction-critical.  Thus it refutes a deduction from connectivity,
packet data, contact surplus, and static critical inequalities.  It does
not refute a theorem that uses `K_7`-minor-freeness or an actual proper-minor
state transition.

## 1. Paired frontier boundary

Let

\[
 S=\{c,a_1,t_1,a_2,t_2,a_3,t_3\},\qquad
 B_i=\{a_i,t_i\}.
\]

The boundary edges are

\[
 ca_1,\ ca_2,\ ca_3,\ a_1t_2,\ t_1a_3,\ a_2t_3.       \tag{1.1}
\]

They form a subdivided claw, so this is a connected bipartite tree in the
static frontier.  Each `B_i` is independent, `c` meets every pair, and the
last three edges give one literal edge between every two distinct paired
blocks.  Its bipartition is

\[
 A=\{c,t_1,t_2,t_3\},\qquad B=\{a_1,a_2,a_3\}.        \tag{1.2}
\]

## 2. The two shores

The thin shore `L` is the five-vertex wheel: outer cycle

```text
l0-l1-l2-l3-l0
```

and centre `l4` adjacent to all four outer vertices.  Every vertex of `L`
sees `c,a1,t1`.  Add the seven contacts

```text
l0-t2, l1-a2, l2-t3, l3-a3,
l0-a2, l1-t3, l2-a3.
```

The rich shore is a `K_6` on `r0,...,r5`.  The vertices `r0,r1` see all of
`S`; each of `r2,...,r5` sees `S-{c}`.  There are no edges between the open
shores.

The rich shore has packet number exactly two: `r0,r1` are disjoint full
singleton packets, and every full packet must contain one of them.  The
thin shore has packet number one.  Exhaustively, its inclusion-minimal full
packets are

```text
{l0,l1,l2}, {l0,l1,l3}, {l0,l2,l3}, {l0,l2,l4};
```

in particular every full packet contains `l0`.

## 3. Contact surplus

Use the adjacent connected full rich cover

\[
 P=\{r_0,r_2,r_3\},\qquad Q=\{r_1,r_4,r_5\}.
\]

The numbers of literal boundary contacts of `L,P,Q` are respectively

\[
                         22,\quad19,\quad19.
\]

Consequently the surplus over the three-packet baseline is

\[
                       22+19+19-3|S|=39,               \tag{3.1}
\]

far exceeding the proposed lower threshold fourteen.

## 4. Failure of the duty split

The inclusion-minimal connected `A`-carriers in `L` are

```text
{l0,l1}, {l0,l2,l3}, {l0,l2,l4}.
```

The inclusion-minimal connected `B`-carriers are

```text
{l1,l2}, {l0,l3}, {l0,l2,l4}, {l1,l3,l4}.
```

Every set in the first line intersects every set in the second.  Therefore
there are no vertex-disjoint `A`- and `B`-carriers at all, much less an
adjacent connected pair satisfying Lemma 5.2.  The verifier independently
enumerates every nonempty subset of the thin five-vertex wheel.

## 5. Connectivity and criticality-shaped static checks

The verifier gives

```text
vertices 18
edges 89
node_connectivity 7
minimum_degree 7
packet_vector (1,2)
```

The boundary `S` itself is a seven-cut, so the connectivity is exactly
seven.  For every literal vertex `x`, exhaustive maximum-independent-set
calculation also verifies

\[
                    \alpha(G[N(x)])\le d_G(x)-5,       \tag{5.1}
\]

the Dirac neighbourhood inequality at parameter seven.

## 6. Exact missing hypothesis

The obstruction is static.  The rich `K_6` together with the boundary
vertex `a1` is a literal `K_7`.  Hence any valid positive theorem must spend
at least one hypothesis absent here:

1. use `K_7`-minor-freeness to turn the crossed thin wheel into a forbidden
   model; or
2. use a genuine contraction-critical proper-minor transition which forces
   the attained equality state through the thin shore.

Neither the thirty-nine surplus contacts nor all local Dirac inequalities
encode that transition.  In particular, the proposed implication cannot be
inserted as a connectivity-only consequence in Section 7 of the active
frontier draft.

## 7. Reproduction

Run

```text
active/runtime/venv/bin/python \
  barriers/hc7_exact7_width2_surplus_thin_split_barrier_verify.py
```

The script checks every assertion above, including literal paired-state
incidences, exact packet numbers, all thin carriers, connectivity, surplus,
Dirac inequalities, and the trust-boundary `K_7`.
