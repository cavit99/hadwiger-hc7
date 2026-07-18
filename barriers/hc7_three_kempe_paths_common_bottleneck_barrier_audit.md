# Audit: three colour-indexed paths need not have a common bottleneck

## Verdict

**GREEN** at the exact source revision

```text
fe7cc2f3596e305c36a220c3e65039b737b756232051017b4533287769736354  barriers/hc7_three_kempe_paths_common_bottleneck_barrier.md
```

The finite construction is properly coloured, realizes the three stated
two-colour paths, has neither three internally vertex-disjoint `b-I` paths
nor a common internal vertex, and has minimum internal `b-I` separator
order two.  The second construction correctly shows that even an actual
common vertex of the three selected two-colour paths need not separate the
host once paths in the other colours are allowed.  This is a barrier only
to the displayed abstract inference, not to `HC_7` or to the conditional
Kempe theorem.

## 1. Colouring and path intersections

Along each displayed path `P_k`, alpha-coloured and private
`beta_k`-coloured vertices alternate.  Shared vertices are among
`b,i_0,i_1,x_12,x_23,x_31`, all of which have colour alpha.  Thus the
specified colouring is proper even at the shared vertices.

The internal intersections are exactly arranged in a three-cycle:

```text
P_1 and P_2 share x_12,
P_2 and P_3 share x_23,
P_3 and P_1 share x_31.
```

No one of these vertices lies on all three paths.  The further common
vertices are allowed ends: all three paths start at `b`, and `P_1,P_3`
both end at `i_0`.

## 2. No three internally disjoint paths

The neighbours of `b` in the union are precisely `u_1,u_2,u_3`.  Any
family of three internally vertex-disjoint `b-I` paths must therefore use
all three initial edges.  The paths beginning through `u_1` and `u_2`
must both next pass through `x_12`, because each of these two private
vertices has neighbours only `b` and `x_12`.  They cannot be internally
disjoint.  Hence the maximum packing has order at most two; two of the
the two paths

```text
b-u_1-x_12-v_1-x_31-w_1-i_0
b-u_3-x_23-w_2-i_1
```

are internally disjoint, so the maximum packing has order exactly two.

## 3. Minimum internal separator

Deleting `{x_12,x_23}` separates `b` from both vertices of `I`: each of the
three neighbours of `b` then lies in a component cut off before reaching
`i_0` or `i_1`.

No single internal vertex separates `b` from `I`:

- after deleting `x_12`, `x_23`, or `x_31`, respectively, the intact path
  `P_3`, `P_1`, or `P_2` remains; and
- after deleting a private-colour vertex, at least the other two displayed
  paths remain.

These categories exhaust the internal vertices.  The minimum internal
separator therefore has order exactly two.

## 4. The common-vertex warning

In the second construction every alpha--`beta_k` path displayed uses the
common alpha vertex `x`.  The added path `b-s-t-i_0` uses neither alpha nor
any `beta_k` on its internal vertices, so it adds no edge or vertex to any
of the three relevant alpha--`beta_k` induced subgraphs.  Nevertheless it
survives deletion of `x`.  Thus `x` is not a host separator, and arbitrarily
many other-colour bypasses can be added without changing the selected
two-colour subgraphs.

## 5. Exact scope

The barrier refutes only the claim that the intersection pattern of three
selected colour-indexed paths by itself gives either a three-path packing
or one common host separator.  It does not satisfy, and does not purport to
satisfy, seven-connectivity, contraction-criticality, `K_7`-minor
exclusion, the five labelled row structure, or the universal proper-minor
responses of the active `HC_7` setting.
