# Audit: marked-edge response coupling

## Verdict

**GREEN in the stated nonterminal scope.** This is an independent cold audit
of `hc7_marked_edge_response_coupling.md` at SHA-256

```text
e27d4ddaa733a9a09e72bfa8e7fc79f525be6fb56829626d6e1add0130ab96d1
```

The audit was completed on 21 July 2026. It is an internal mathematical
audit, not external peer review. The deletion/contraction identification,
simultaneous-contraction list argument, marked-edge lattice, literal
separator lift and response-side gluing are correct. The note explicitly
does not preserve the original boundary language, prove a strict decrease or
prove `HC_7`.

## 1. Single-edge and simultaneous-contraction claims

If a `q`-colouring of `G-xy` separates the colours of `x,y`, it already
colours `G`; hence every such colouring identifies them. Identifying
equal-coloured endpoints and expanding a contraction vertex are inverse
operations on labelled colourings, so Lemma 1.1 is exact.

In Theorem 2.1 the two nontrivial contractions give a proper minor. A
hypothetical `(q-1)`-colouring expands both bipartite sets by reusing each
contraction colour on one bipartition class and one common fresh colour on
the other classes. Outside neighbours avoid the corresponding contraction
colour, and anticompleteness permits the fresh colour on both sets. This
would `q`-colour `G`, proving `chi(G/X/Y)=q`.

Every displayed list contains its contraction colour. If both list systems
were colourable, their colourings would splice independently with the fixed
exterior state. Thus at least one is uncolourable. For a returned tree shore
`Z'`, De Morgan's law gives

\[
 \bigcap_{x\in Z'}L_Z(x)
 =Q-c\bigl(N_G(Z')-(X\cup Y)\bigr).
\]

The singleton intersection from the audited poor-edge lemma is therefore
exactly the full secondary-colour exposure asserted on both pieces. Expanding
the other side when it is list-colourable gives the stated one-contraction
colouring. No bilateral conclusion for both interiors is inferred.

## 2. Weighted separation lattice

The original separation is anchored and has weight `|S|`, so the minimum
exists and is at most nine. For any anchored separation of `H`, a crossing
`g=pv` has `p` right-open because `v` is fixed left-open; moving `p` into the
separator repairs precisely that missing edge. A crossing `h=qw` is repaired
symmetrically by moving `q`, not `w`. Vertex-disjointness of the marked edges
makes the separator order exactly `lambda`. All anchors survive, and
seven-connectivity gives the lower bound seven.

Meet and join preserve the anchors. Vertexwise, their two states are the two
extrema of the original left/separator/right states, so the total ordinary
separator contribution is preserved. In fact, on the anchored family the
`g` contribution is `1[p notin A]` and the `h` contribution is
`1[q notin B]`; the corresponding OR/AND identities preserve each pair of
indicators. The displayed submodular inequality follows. Minimality then
forces both corners of two weight-`m` members to have weight `m`, producing
the finite lattice and its canonical least member.

The qualification in Theorem 3.1(2) is essential and correct. When
`m=|S|`, the original separation is minimum, so the least member lies below
it and its left open shore is contained in `C`. When `m<|S|`, the original
separation is not in the minimum family and no such containment is claimed.

The endpoint repair gives a literal order-`m` separation of `G`. The edge
`g` belongs wholly to its left closed shore, while `h,uz` belong wholly to
its right. A colouring of `G-g` restricts to the intact right shore. If the
same equality partition extended through the intact left shore, a palette
permutation matching boundary classes followed by gluing would six-colour
`G`. The arguments for `G-h` and `G-uz` are symmetric. This preserves only
operation-side orientation on the new separator, exactly as stated.

## 3. Gate and trust boundary

The stop decision is justified. A minimum lift may be the original
separation; deleted-edge separations differing only by movement across a
deleted edge may lift to that same separation; and a new separator carries
fresh traces rather than the original exact-block data. In the literal
degree-seven branch the opposite-shore path premise is empty because
`G-N[u]=C`. Therefore the result supplies neither a strict same-host descent
nor a new bounded interface preserving the original labelled response.

The conclusion declines Cycle 2 using these Cycle-1 outputs. It does not
claim that an unrelated future order-eight, order-nine or pole argument is
impossible. No unresolved assumption remains inside the stated theorems.
