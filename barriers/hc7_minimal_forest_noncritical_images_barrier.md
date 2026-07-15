# Minimal forest saturation does not force a critical image

**Status:** explicit counterarchitecture; verifier supplied.

This note tests the proposed next step after the minimal contraction-forest
saturation theorem:

> if a minimal forest contraction first makes a two-shore residue
> five-colourable, must some nontrivial forest-component image `z` satisfy
> `chi(K-z)=4`?

The answer is **no from the local two-shore and minimal-forest hypotheses
alone**.  The 13-vertex construction below has an order-eight four-colour
boundary, two full connected anticomplete shores, an inclusion-minimal
two-edge forest contraction to a five-chromatic graph, and the exact
six-chromatic predecessor ladder.  Nevertheless, deletion of its
nontrivial contraction image leaves a literal `K_5`.

This is not a counterexample under the full hypothetical-`HC_7` kernel: the
construction contains a literal `K_7`, has vertices of degree two, and is not
minor-critical.  It identifies the global hypotheses that a positive theorem
would have to use rather than deriving the conclusion from palette saturation.

## 1. Construction

Let

\[
 S=\{s_1,s_2,s_3,s_4,t_1,t_2,t_3,t_4\},
 \quad A=\{a,x,y,z\},
 \quad B=\{b\}.
\]

There are no edges between `A` and `B`.  Put a clique on
`{s_1,s_2,s_3,s_4}`, leave the four `t_j` independent in `G[S]`, and add
the following edges.

1. The set `Q={a,s_1,s_2,s_3,s_4}` is a `K_5`.
2. The set `P={x,y,z}` induces a triangle.
3. Every vertex of `P` is adjacent to `Q-{s_1}`.
4. Each `t_j` is adjacent to `a` and `b`, and `b` is adjacent to every
   vertex of `S`.

Then `G[A]` and `G[B]` are nonempty and connected, the shores are
anticomplete, and every literal vertex of `S` has a neighbour in each shore.
Moreover `G[S]` is four-colourable.

Let

\[
                         F_0=\{xy,yz\}.
\]

This is a forest contained in a spanning tree of `G[A]`: use the three
edges

\[
                            xy,\quad yz,\quad ax.
\]

Write `w` for the image of `P` after the two forest edges are contracted
and put `K=G/F_0`.

## 2. Exact chromatic ladder

The seven vertices

\[
                        P\cup\{a,s_2,s_3,s_4\}
\]

form a literal `K_7`, so `chi(G)>=7`.  For an explicit seven-colouring,
give `a,s_2,s_3,s_4,x,y,z` seven distinct colours, give `s_1` the colour
of `x`, give `b` the colour of `y`, and give all `t_j` the colour of
`s_2`.  Hence `chi(G)=7`.

The quotient `K` is five-colourable.  Give the five vertices of `Q` five
distinct colours, give `w` the colour of `s_1`, give `b` the colour of
`a`, and give every `t_j` a colour different from the colour of `a` and
`b`.  Since `Q` is a `K_5`,

\[
                              \chi(K)=5.              \tag{2.1}
\]

If either one of `xy,yz` is contracted, the triangle `P` becomes an edge.
Both ends see the four vertices of `Q-{s_1}`.  In any five-colouring of
`Q` they would both be forced to use the colour of `s_1`, which their edge
forbids.  Consequently each predecessor is not five-colourable.  Giving one
endpoint a sixth colour proves that it is exactly six-chromatic.  Thus
`F_0` is inclusion-minimal among subsets of itself whose contraction is
five-colourable, and every one-edge predecessor has chromatic number six,
exactly as in the saturation theorem.

However, the literal `K_5=K[Q]` survives deletion of `w`.  The displayed
five-colouring of `K` restricts after that deletion, so

\[
                              \chi(K-w)=5.            \tag{2.2}
\]

The unique nontrivial contraction-component image is not critical.

## 3. What the example blocks

The saturation theorem correctly forces both sides of each uncontracted
forest edge to see all four colours other than the image colour.  This
example shows that those contacts can coexist with a **redundant
five-chromatic core** disjoint from every contraction image.  Palette
contacts do not themselves make any image vertex-essential.

Therefore a proof of a critical-image lemma in the actual `HC_7` residue
must use a global hypothesis that this architecture deliberately violates:

* exclusion of a `K_7` minor, to prevent the split colour-forcing gadget
  from completing around a persistent `K_5` core;
* seven-connectivity/minimum degree, to prevent low-degree boundary padding
  and detachable gadgets; and/or
* full minor-criticality, to prevent vertices and substructures that remain
  irrelevant after the seven-chromatic obstruction has already formed.

The construction does not decide whether these full hypotheses force a
critical image.  It decisively falsifies the proposed step as a consequence
of the new minimal-forest saturation invariant alone.

## 4. Reproducibility

Run

```text
python3 barriers/hc7_minimal_forest_noncritical_images_barrier_verify.py
```

The checker constructs the labelled graph, computes the exact chromatic
numbers by DSATUR, checks the shore and boundary conditions, performs the
relevant contractions, and verifies the literal `K_7` witness.
