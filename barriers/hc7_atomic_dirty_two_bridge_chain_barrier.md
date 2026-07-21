# A dirty two-bridge replacement chain need not close locally

**Status:** explicit barrier to a local intermediate claim; written proof
and computer-assisted finite checks; separate internal audit GREEN.

This note tests one specifically motivated attachment pattern on the atomic
frame.  Two separate bridges compose through an interval of the frame to
give a dirty replacement chain, but the resulting canonical graph has no
`K_7` minor.  The graph is only three-connected and four-chromatic, so it
does not satisfy the full hypotheses of a minimal counterexample to `HC_7`.

The retained deterministic verifier is
[`hc7_atomic_dirty_two_bridge_chain_barrier_verify.py`](hc7_atomic_dirty_two_bridge_chain_barrier_verify.py).

## 1. The false local implication and the canonical graph

Let

\[
                 H_0=(K_7-\{ab,cd\})+\{xa,xb,xc,xd\}.
\]

Take a labelled subdivision `T` of `H_0`.  In the orientation used here,

\[
   T_{fg}=f-h-g,\quad T_{fa}=f-p-a,\quad T_{ga}=g-q-a,
   \quad T_{ac}=a-r-s-c.                                  \tag{1.1}
\]

Add `eh,hx` and the two edges `pr,sq`.  Call the resulting thirteen-vertex
graph `D_*`.  It has thirty-two edges.  The two added edges are separate
`T`-bridges.  Their composition

\[
                         f-p-r-s-q-g                         \tag{1.2}
\]

uses the frame edge `rs`; it is therefore a dirty replacement chain, not
itself one branch-vertex-avoiding `T`-path.

The graph refutes the following bare implication.

> **False two-bridge closure claim.**  The shared-hub edges `eh,hx` and two
> bridges `pr,sq` arranged as in (1.1) always close the atomic frame to a
> `K_7` minor.

Reversing the order on `T_ac` gives the isomorphic reflected instance; the
orientation in (1.1) fixes all labels used below.

## 2. A structural `K_7`-minor exclusion

### Theorem 2.1

The graph `D_*` has no `K_7` minor.

#### Proof

Put `J=D_*-e`.  The following bags form a tree decomposition of `J`:

\[
\begin{array}{c|l}
 U&b,c,d,f,g,x\\
 V&a,c,d,f,g,x\\
 H&f,g,h,x\\
 W&a,c,f,g,s\\
 Q&a,g,q,s\\
 R&a,f,r,s\\
 P&a,f,p,r.
\end{array}                                                  \tag{2.1}
\]

The decomposition tree has edges

\[
                         UV,UH,VW,WQ,WR,RP.                    \tag{2.2}
\]

Every edge of `J` is contained in a displayed bag, and the bags containing
each vertex induce a subtree.  Thus (2.1)--(2.2) is a width-five tree
decomposition.

Suppose that `J` has a `K_6` model.  Since `J` is connected, extend it to a
spanning model by absorbing every unused component into an adjacent branch
set.  For each branch set, the decomposition nodes whose bags meet that
branch set form a subtree of (2.2).  Two adjacent branch sets give
intersecting subtrees.  The six subtrees are pairwise intersecting, so the
Helly property for subtrees of a tree gives a common bag.  Six disjoint
branch sets require a bag of order at least six.  Hence the common bag is
`U` or `V`, and every branch set contains exactly one vertex of that bag.

We use the following immediate consequence.  If `u,v` are nonadjacent in
the common bag, the branch sets rooted at `u,v`, together with an edge
between them, contain a `u`--`v` path whose internal vertices avoid the
common bag.  Paths obtained from two disjoint pairs use four disjoint
branch sets and are vertex-disjoint.

First suppose the common bag is `U`.  The components of `J-U` are

\[
        \{h\},\qquad K=J[\{a,p,q,r,s\}],                       \tag{2.3}
\]

with attachment sets `\{f,g,x\}` and `\{c,d,f,g,x\}`, respectively.
The graph `J[U]` misses exactly

\[
                              cd,fg,fx,gx.                      \tag{2.4}
\]

The singleton `h` must belong to the branch set rooted at `f`, `g`, or
`x`.  If it belongs to the `f`-branch set, it supplies `fg,fx`; the missing
pairs `cd,gx` must then be realized by two vertex-disjoint paths through
`K`.  If it belongs to the `g`-branch set, the same argument uses the
missing pairs `cd,fx`.  Both alternatives are impossible: `d` and `x` each
have `a` as their unique neighbour in `K`, so the two paths both contain
`a`.

It remains that `h` belongs to the `x`-branch set.  It supplies `xf,xg`,
so `cd` and `fg` require vertex-disjoint paths through `K`.  A `c`--`d`
path contains both `s` and `a`, because those are the unique contacts from
`c,d` to `K`.  An `f`--`g` path must connect `p` to `q` inside `K`.  But

\[
             E(K)=\{ap,aq,ar,pr,rs,sq\},                       \tag{2.5}
\]

and `\{a,s\}` separates `p` from `q`.  The two paths therefore meet, again
a contradiction.

Now suppose the common bag is `V`.  The components of `J-V` are

\[
       \{b\},\qquad \{h\},\qquad L=J[\{p,r,s,q\}],             \tag{2.6}
\]

where `L` is the path `p-r-s-q`.  Their attachment sets in `V` are

\[
        \{c,d,f,g,x\},\qquad \{f,g,x\},
        \qquad \{a,c,f,g\}.                                  \tag{2.7}
\]

The missing pairs in `J[V]` are

\[
                         ac,af,ag,cd,fg,fx,gx.                  \tag{2.8}
\]

Only `b` can repair `cd`, so it belongs to the branch set rooted at `c` or
`d` and cannot repair a pair among `f,g,x`.  The path `L` has no attachment
to `x`.  Consequently `h` cannot belong to the `f`-branch set, which would
leave `gx` unrepairable, or to the `g`-branch set, which would leave `fx`
unrepairable.  It belongs to the `x`-branch set and supplies `xf,xg`.

The pairs `ac` and `fg` must now be realized by vertex-disjoint paths
through `L`.  The `a`--`c` path contains `s`, the unique contact of `c`
with `L`.  The `f`--`g` path is forced through

\[
                              f-p-r-s-q-g,
\]

and also contains `s`, a contradiction.  Thus `J` has no `K_6` minor.

Finally, a `K_7` model in `D_*` has at most one branch set containing `e`.
Discard that branch set, or any one branch set if `e` is outside the model.
The remaining six branch sets would give a `K_6` model in `D_*-e`, contrary
to the preceding conclusion.  \(\square\)

The verifier checks the tree decomposition directly and independently
exhausts every spanning six-bag model in `D_*-e`.

## 3. Connectivity, colouring, and two-apex status

### Proposition 3.1

The graph `D_*` has vertex-connectivity three and chromatic number four.  It
is not two-apex.

#### Proof

The neighbourhood `N(p)=\{a,f,r\}` is a three-vertex cut.  The verifier
checks that deletion of every set of order at most two leaves the graph
connected, proving `kappa(D_*)=3`.

The vertices `b,c,e,f` induce a `K_4`.  Conversely, the four independent
sets

\[
       \{e,x,p,q\},\quad \{a,b,h,s\},\quad
       \{c,d,r\},\quad \{f,g\}                                \tag{3.1}
\]

partition the vertices, proving `chi(D_*)=4`.

For each of the seventy-eight vertex pairs, the verifier deletes the pair,
obtains a Kuratowski subgraph, checks that it is a literal subgraph of the
remainder, and suppresses its degree-two paths to `K_5` or `K_{3,3}`.  It
finds 32 subdivisions of `K_5` and 46 subdivisions of `K_{3,3}`.  Hence no
pair planarizes `D_*`; a planarizing set of smaller order would remain
planar after one more deletion, so none exists.  \(\square\)

Thus the familiar two-apex certificate for several atomic barriers is
genuinely unavailable here.

## 4. The `K_2`-joined icosahedron does not contain the chain

Let `I` be the icosahedral graph and put `A=K_2\vee I`.  This is a
seven-connected `K_7`-minor-free graph: `I` is five-connected and planar,
and discarding the at most two branch sets containing the complete-factor
vertices from a hypothetical `K_7` model would leave a `K_5` model in `I`.
Unlike the earlier shared-hub graph, all vertices of `D_*` have degree at
most seven, so ambient degrees do not exclude a subdivision.

### Proposition 4.1 (computer-assisted finite result)

The graph `A` contains no subdivision of `D_*`.

#### Finite proof

Every one of the thirteen vertices of `D_*` has degree at least three and
must have a distinct image in a subdivision.  The host `A` has fourteen
vertices.  There is therefore room for at most one internal vertex on all
subdivided edge paths together.  An embedding is exactly one of the
following:

1. an injective edge-preserving map of `D_*` into `A`; or
2. for one of the thirty-two edges of `D_*`, an injective edge-preserving
   map after subdividing that edge once.

The verifier performs a deterministic injective-map backtracking search in
the literal case and in all thirty-two one-edge cases.  It checks all
adjacencies against the standard fourteen-vertex `K_2\vee I` and finds no
map in the thirty-three exhaustive cases.  \(\square\)

This targeted check rules out the standard seven-connected two-apex
guardrail as an exact host for the canonical chain.  It does not rule out a
longer subdivision in a larger seven-connected host.

## 5. Exact single-edge saturation

For each of the degree-three vertices `p,q,r,s` and the degree-four vertex
`h`, the following table classifies every incident nonedge.  The middle
column lists endpoints `v` for which adding the single edge to `v` produces
a `K_7` minor; the last column lists the surviving additions.

| vertex | `K_7` after one edge | still `K_7`-minor-free |
|---|---|---|
| `h` | `p,q,r` | `a,b,c,d,s` |
| `p` | `b,d,g,h,q` | `c,e,s,x` |
| `q` | `b,d,f,h,p` | `c,e,r,x` |
| `r` | `b,d,g,h` | `c,e,f,q,x` |
| `s` | `b,d` | `a,e,f,g,h,p,x` |

The verifier stores and checks explicit seven-branch-set models for every
positive entry.  It covers all negative entries by the following five
simultaneous augmentations:

\[
\begin{aligned}
 C_1&=\{hc,pc,qc,rc\},\\
 C_2&=\{px,qx,rx,hb\},\\
 C_3&=\{qr,rf,hd\},\\
 C_4&=\{sa,se,sf,sg,sh,sp,sx\},\\
 C_5&=\{ep,eq,er,es,ha\}.
\end{aligned}                                                \tag{5.1}
\]

Every negative single edge is contained in at least one `C_i`.  The exact
spanning-partition oracle finds no `K_7` model in `D_*+C_2`.  For each of
the other four augmentations it finds no `K_6` model after deleting `e`,
which excludes a `K_7` model before that deletion.  By subgraph monotonicity,
all individual negative entries are certified.

The table shows both sides of the local phenomenon.  Several attachments
close immediately, but every low-degree subdivision vertex also has
multiple nonterminal endpoint choices.  A valid host theorem must use the
simultaneous, internally disjoint paths supplied by seven-connectivity and
their literal first-hit endpoints; single-edge saturation alone does not
close the canonical pattern.

## 6. Scope

The barrier is deliberately local:

- `D_*` is three-connected, not seven-connected;
- it is four-colourable and is not contraction-critical;
- it contains the exact canonical vertices in (1.1), not arbitrary longer
  route subdivisions;
- its two added edges are two separate bridges whose composition uses a
  frame interval; and
- it does not refute the labelled first-hit theorem or any theorem that
  genuinely spends seven-connectivity and the proper-minor colouring
  responses.

Accordingly, the false inference is only that the two displayed bridges,
without host-level fan or first-hit information, already supply a `K_7`
minor.
