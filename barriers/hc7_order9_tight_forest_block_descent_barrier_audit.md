# Independent audit of the tight-forest block-descent barrier

## Verdict and audited revision

**Verdict: GREEN.**

This audit checks the complete barrier
[`hc7_order9_tight_forest_block_descent_barrier.md`](hc7_order9_tight_forest_block_descent_barrier.md)
at SHA-256

```text
82dfef088a2ab572415a2c59cb68f712ac5da976d068c020475a708af16f1a79
```

The final revision changes only the source status paragraph to link this
audit; the audited mathematics is unchanged.  The boundary-induced lists, non-list-colourability, vertex-minimality,
tight/excess calculation, two-shore realization, degree counts, boundary
fullness, and order-ten full neighbourhood of the unique nontrivial tight
block are all correct.  The example refutes only the displayed local
block-boundary inference.  It does not satisfy the global hypotheses of a
hypothetical `HC_7` counterexample.

## 1. Boundary trace and the two shores

The boundary has nine vertices in six colour classes of orders

```text
2,2,2,1,1,1.
```

It is edgeless, so assigning one colour to each displayed class is proper.
Every four-cycle vertex is adjacent to all six vertices in the three
two-vertex classes.  Its additional singleton neighbours give exactly

```text
L(u)={p,a},  L(v)={p,b},  L(x)={a},  L(y)={b}.
```

Indeed, `u` sees only singleton `b`, `v` sees only `a`, `x` sees `p,b`, and
`y` sees `p,a`.  These are precisely the boundary colours absent from the
respective boundary neighbourhoods.

The added opposite-shore vertex `d` is adjacent to all nine boundary
vertices and is anticomplete to the four-cycle.  Its boundary-induced list
is therefore empty, so its one-vertex shore is non-list-colourable, while
deleting its only vertex leaves the empty colourable graph.  It is a
spanning vertex-minimal list obstruction.

The four-cycle shore is collectively full to the boundary.  Each repeated-
colour vertex is adjacent to every shore vertex; `p` is met by `x,y`, `a`
by `v,y`, and `b` by `u,x`.  The singleton shore `{d}` is individually full.
Thus the two shores are anticomplete, boundary-full, and use the same fixed
boundary trace, exactly as claimed.

## 2. Non-list-colourability and vertex-minimality

On the cycle `x-u-v-y-x`, the singleton lists force

```text
x=a and y=b.
```

The edge `xu` then forces `u=p`, and the edge `yv` forces `v=p`.  This
violates the edge `uv`, so the shore is not `L`-colourable.

The four displayed one-vertex-deletion colourings are proper and respect
all lists:

```text
delete x: (u,v,y)=(a,p,b),
delete y: (x,u,v)=(a,p,b),
delete u: (x,v,y)=(a,p,b),
delete v: (x,u,y)=(a,p,b).
```

Checking the surviving cycle edges in each row gives unlike colours at
their ends.  Every still smaller induced subgraph is colourable by
restricting one of these colourings.  Hence the four-cycle is vertex-minimal
non-`L`-colourable, not merely deletion-critical for a selected vertex.

## 3. Tight vertices, excess, and degrees

Every cycle vertex has internal degree two.  Therefore

```text
epsilon(u)=2-|L(u)|=0,
epsilon(v)=2-|L(v)|=0,
epsilon(x)=2-|L(x)|=1,
epsilon(y)=2-|L(y)|=1.
```

The tight-vertex induced graph is exactly the edge `uv`, hence a forest,
and the total excess is two.

The sentence in the source about the degree lower bound concerns every
**shore** vertex.  Their literal degrees in the graph formed by the cycle
and boundary are

```text
d(u)=d(v)=2+6+1=9,
d(x)=d(y)=2+6+2=10.
```

Adding the anticomplete opposite vertex does not change these values.  Thus
the local degree-nine lower bound used in the refuted inference really is
satisfied at every vertex of the list-critical shore.

## 4. The unique tight block and its full neighbourhood

The only nontrivial block of the tight graph is `H=G[{u,v}]`.  Inside the
four-cycle, `u` has the outside neighbour `x` and `v` has the outside
neighbour `y`, so the internal attachment set is exactly `{x,y}`.

On the boundary, both `u` and `v` meet all six vertices of the repeated
classes.  Their singleton contacts have union `{a,b}`; both miss `p`.
The opposite-shore vertex `d` is anticomplete to them.  Consequently

```text
N(H)={x,y} disjoint-union (B-{p}),
|N(H)|=2+8=10.
```

Thus no nontrivial tight block in this example has full-neighbourhood order
at most nine.  At the same time the companion positive theorem is not
contradicted: each individual tight endpoint has degree nine and yields its
own singleton-side response under the stronger proper-minor host
hypotheses.

## 5. Exact scope

The construction supplies the following local ingredients:

- one order-nine fixed boundary trace using all six colours;
- two anticomplete boundary-full shores;
- a spanning vertex-minimal list obstruction on each shore;
- a nonempty tight forest and positive total list-degree excess; and
- shore minimum degree at least nine.

It does not supply seven-connectivity, seven-chromaticity,
contraction-criticality, `K_7`-minor exclusion, or all operation-specific
proper-minor colourings.  Therefore it is a valid counterexample to the
stated local small-*block*-boundary inference and to no stronger host-level
claim.
