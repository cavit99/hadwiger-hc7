# Barrier: a fully crossed selected core does not make the thin shore 2-connected

**Status:** verified geometry-only barrier.  The graph is exactly
seven-connected and has packet vector `(1,2)`, but it contains a literal
`K_7` and no legal equality-state transition is claimed.  It does not
falsify the atomic residual parity-repair lemma.

The dependency-free verifier is
[`hc7_atomic_fully_crossed_cutvertex_barrier_verify.py`](hc7_atomic_fully_crossed_cutvertex_barrier_verify.py).

## Construction

Use the paired-tree boundary

\[
 S=\{c,a_1,t_1,a_2,t_2,a_3,t_3\}
\]

with edges

\[
 ca_1,ca_2,ca_3,a_1t_2,t_1a_3,a_2t_3.                 \tag{1.1}
\]

Put `u=t1` and `W=S-{u}`.  The thin shore has vertices

\[
                         A=\{z,v,w,x\}.
\]

Its internal edges are the triangle `zvwz` and the pendant edge `vx`.
Every thin vertex is complete to `W`, while `z` is the unique thin
neighbour of `u`.

The rich shore is a `K_6` on `r0,...,r5`.  The vertices `r0,r1` are
complete to `S`; each other rich vertex sees `S-{c}`.  There are no
thin--rich edges.

Exhaustive vertex-cut and connected-packet enumeration gives

\[
                         \kappa(G)=7,qquad
                         (\nu_A,\nu_R)=(1,2).           \tag{1.2}
\]

The compulsory portal is the unique edge `zu`.  Moreover `A-z` is
connected and `W`-full, exactly as required by root-deletion normalization.

## Fully crossed core but a cutvertex

Select the rooted path

\[
                              T=z-v-w.
\]

The omitted chord `zw` is a trivial `T`-bridge.  Its attachments lie on
opposite sides of each of the two edges of `T`, so every selected-core edge
is crossed.

Nevertheless `v` is a cutvertex of `G[A]`: deleting it isolates `x` from
the edge `zw`.  Thus the implication

```text
every edge of the selected path/Y core is crossed
    => the whole thin shore is 2-connected
```

is false even after exact seven-connectivity, the packet vector, the
paired width-two frontier, the unique portal, and root-deletion
normalization are imposed.

The example also shows the correct geometric replacement.  The
one-attachment bridge `{x}` is `W`-full, and

\[
                          N_G(x)=W\cup\{v\}             \tag{2.1}
\]

is an actual seven-boundary.  Equation (2.1) does not transport an equality
state, so it is only the geometric input to a possible descent.

## Trust boundary

The seven vertices

\[
                         \{r_0,\ldots,r_5,a_1\}
\]

form a literal clique.  Hence the construction is eliminated by the
`K_7` terminal and says nothing against the full-kernel theorem.  Its exact
lesson is that a fully crossed bridge-hull proof must retain the alternatives

* an internal cut producing a support-six exact-seven lobe; or
* a genuinely 2-connected terminal hull.

It may not infer the second alternative from crossing of the selected
tree edges alone.  To recurse through the first alternative, a separate
named proper-minor response must still attain a state on the new boundary;
the geometry does not do so.
