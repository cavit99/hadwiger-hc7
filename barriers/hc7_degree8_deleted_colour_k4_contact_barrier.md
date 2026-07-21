# Complete five-root routing does not force three contacts for a prescribed deleted colour

**Status:** barrier/counterexample to an intermediate claim; written proof
with a computer-assisted finite check.  The deterministic verifier is
[`hc7_degree8_deleted_colour_k4_contact_barrier_verify.py`](hc7_degree8_deleted_colour_k4_contact_barrier_verify.py).
This is not a counterexample to `HC_7`, to the degree-eight bridge theorem,
or to the existence of a `U`-rooted `K_5` in the displayed graph.

## 1. The refuted shortcut

The fixed-colouring theorem for the degree-eight `2K_2+K_1` residue gives a
five-chromatic graph `X`, a proper five-colouring `phi`, and five roots
`U={e,a,b,c,d}` which are colourful in `X`: every proper five-colouring of
`X` uses all five colours on `U`.  The routing graph on `U` in `phi` is
therefore complete.

For `x\in U`, let `A_x` be its `phi`-colour class and put `H_x=X-A_x`.
Then `H_x` is four-chromatic and `U-{x}` is colourful in `H_x`.
Martinsson--Steiner's Strong Hadwiger theorem for four colours consequently
gives a `(U-{x})`-rooted `K_4` model in `H_x`.

A tempting fixed-deletion shortcut is:

> For a prescribed `x\in U`, when `G[U]=ab+cd+e` and the fixed routing
> graph is complete, one can choose the `(U-{x})`-rooted `K_4` model so that
> at least three of its bags are adjacent to `x`.

This would make the singleton `{x}` and the four rooted bags a `U`-rooted
`K_5` model with at most one missing adjacency.  The assertion is false.
The graph below satisfies every stated five-colour-core condition, including
the two prescribed disjoint shortest bichromatic paths, but for `x=e` every
`(U-{e})`-rooted `K_4` model in `H_e` has at most one bag adjacent to `e`.

## 2. Construction

Put

```text
U={e,r1,r2,r3,r4},
W={w1,w2,w3,w4},
T={t1,t2,t3,t4},
P={p1,p2,p3,p4},
```

and add one further vertex `q`.  The graph `X` has vertex set

\[
                         U\cup W\cup T\cup P\cup\{q\}.           \tag{2.1}
\]

Its edges are exactly the following:

1. `W` and `T` each induce a `K_4`;
2. the only `W`--`T` edge is `w1t2`;
3. `q` is complete to `W\cup T\cup\{r1,r2,r3,r4\}`;
4. `e` is complete to `T`;
5. `p_i t_i` and `p_i r_i` are edges for every `i`;
6. `r_i w_j` is an edge exactly when `i\ne j`; and
7. the only edges among the five roots are `r1r2` and `r3r4`.

There are no other edges.  Thus, on identifying

```text
a=r1, b=r2, c=r3, d=r4,
```

the literal root graph is exactly `ab+cd+e`.

## 3. The exact five-colour core

Use the five colour classes

\[
 A_e=\{e,q,p_1,p_2,p_3,p_4\},\qquad
 A_i=\{r_i,w_i,t_i\}\quad(1\le i\le4).                \tag{3.1}
\]

The displayed edge list shows directly that (3.1) is a proper colouring.
The set `\{q\}\cup W` induces a `K_5`, so `chi(X)=5`.

### Proposition 3.1

The set `U` is colourful in `X`: every proper five-colouring of `X` uses
all five colours on `U`.

### Proof

Fix a proper five-colouring.  The clique `\{q\}\cup W` uses all five
colours.  Since `q` is adjacent to every vertex of `T` and `T` is a
`K_4`, the vertices of `T` use the four colours different from the colour
of `q`.  The clique `\{e\}\cup T` then forces `e` to have the same fifth
colour as `q`.

For each `i`, the vertex `r_i` is adjacent to `q` and to the three vertices
of `W-{w_i}`.  Those four neighbours have the four colours different from
the colour of `w_i`.  Hence `r_i` has the colour of `w_i`.  The four roots
`r_1,...,r_4` therefore use four distinct colours, all different from the
colour of `e`.  Thus `U` is colourful.  \(\square\)

The usual component-interchange argument now shows that the routing graph
on `U` in the fixed colouring (3.1) is complete.  Here the paths are also
explicit.  For every `i`,

\[
                         e-t_i-p_i-r_i                         \tag{3.2}
\]

is an `A_e\cup A_i` path.  For distinct `i,j`, either `r_ir_j` is one of
the two literal root edges, or

\[
                         r_i-w_j-w_i-r_j                       \tag{3.3}
\]

is an `A_i\cup A_j` path.  Every nontrivial path in (3.2)--(3.3) has
length three and is shortest in its two-colour subgraph: its ends have no
common neighbour in those two colour classes.

In particular, the paths

\[
             P_{ea}=e-t_1-p_1-r_1,qquad
             P_{bc}=r_2-w_3-w_2-r_3                         \tag{3.4}
\]

are shortest and vertex-disjoint.  Together with the literal edges
`r1r2,r3r4`, they form the rooted subdivision
`e-r1-r2-r3-r4` required by the matching residue.

## 4. The unique-bridge contact obstruction

Delete the colour class `A_e` and write

\[
                         H_e=X-A_e.                              \tag{4.1}
\]

Thus `V(H_e)=\{r_1,...,r_4\}\cup W\cup T`.  The clique `W` proves that
`chi(H_e)=4`.  In every proper four-colouring, each `r_i` is forced to have
the colour of `w_i`, because it is adjacent to `W-{w_i}`.  Hence
`\{r_1,...,r_4\}` is colourful in `H_e`.  Also

\[
                         N_{H_e}(e)=T,                            \tag{4.2}
\]

and `T` is colourful because it induces a `K_4`.

The edge `w1t2` is the unique edge joining the `W` side of `H_e` to the
`T` side.  All four roots lie on the `W` side.  Consequently, every
connected subgraph of `H_e` which contains a root `r_i` and meets `T` must
contain both `w1` and `t2`.  Pairwise disjoint rooted branch sets therefore
permit at most one bag to meet `T`, equivalently at most one bag to be
adjacent to `e`.

The upper bound is attained.  With indices modulo four, put

\[
                         D_i=\{r_i,w_{i+1}\}\quad(1\le i\le4),  \tag{4.3}
\]

where `w_5=w_1`, and enlarge `D_4` by `t_2`.  Each bag is connected, the
four bags are pairwise adjacent through the clique `W`, and only `D_4`
meets `T`.  Thus the maximum contact number is exactly one.

This obstruction is specific to the prescribed deletion `x=e`.  Indeed,
for every `i`, delete `A_i={r_i,w_i,t_i}` and list the remaining three
indices cyclically as `j_1,j_2,j_3`.  The four bags

\[
 \{e,q,t_{j_1}\},\quad
 \{r_{j_1},w_{j_2}\},\quad
 \{r_{j_2},w_{j_3}\},\quad
 \{r_{j_3},w_{j_1}\}                                      \tag{4.4}
\]

form a `(U-{r_i})`-rooted `K_4` model in `H_{r_i}`.  The first bag is
adjacent to `r_i` through `q`, and each other bag is adjacent to `r_i`
through its displayed `W-{w_i}` vertex.  Hence all four bags contact
`N_{H_{r_i}}(r_i)`.  Since a rooted `K_4` model has only four bags, this is
optimal.  In root order `(e,r1,r2,r3,r4)`, the exact vector of maximum
contact numbers is therefore

\[
                              (1,4,4,4,4).                     \tag{4.5}
\]

This is the mechanism behind the failure: complete bichromatic routing is
present in `X`, but deleting `A_e` removes every internal `A_e` vertex of
the paths (3.2).  Inside `H_e`, all access from the rooted side to
`N_{H_e}(e)` is concentrated on one literal bridge.  The remaining routing
paths do not turn that bridge into three disjoint bag contacts.

## 5. Why this is not a target counterexample

The graph `X` already has a `U`-rooted `K_5` model.  Take

\[
 B_e=\{e,t_1,q\},\qquad
 B_i=\{r_i,w_{i+1}\}\quad(1\le i\le4),                \tag{5.1}
\]

again with cyclic indices.  The first bag is connected through `t1`, the
other four are connected by the edges `r_iw_{i+1}`, and they are pairwise
adjacent through the clique `W`.  The vertex `q` makes `B_e` adjacent to
each of the other four bags.

Thus the example refutes only the fixed-deletion inference

```text
complete routing + the Martinsson--Steiner rooted K4 for a prescribed deletion
    => at least three deleted-root contacts.
```

By (4.4), it does not refute the weaker existential inference that *some*
choice of `x` has at least three contacts.  Nor does it refute a disjunction
whose first outcome is an independently constructed `U`-rooted `K_5`.  It
also is not embedded in a
seven-connected, seven-chromatic, contraction-critical, `K_7`-minor-free
host.  In particular, the unique bridge in `H_e` is not an aligned strict
restart in a component of `G-N[u]`.  The witness supplies no pole, robust
triple, smaller literal anti-neighbourhood component, or lift.

The precise remaining requirement is therefore model-relative: a positive
trace-switching theorem must use the absence of every global `U`-rooted
`K_5` (or the full host's minor exclusion and criticality) before forcing
three contacts in one deletion-rooted `K_4` model.  Complete routing by
itself is insufficient.

## 6. Exhaustive check

The verifier independently enumerates all `253,200` labelled proper
five-colourings and confirms that every one makes `U` colourful.  It also
enumerates all `5^8=390,625` assignments of the eight nonroot vertices of
`H_e` to four fixed rooted bags or to no bag.  Exactly `927` assignments
form a rooted `K_4` model, and their maximum number of `T`-meeting bags is
one.  It separately checks the explicit four-contact model (4.4) for every
other deleted root, thereby asserting the exact vector (4.5).  It also
checks the complete fixed routing, shortestness and disjointness in (3.4),
the displayed extremal model (4.3), and the rooted `K_5` in (5.1).

Run:

```text
.venv/bin/python barriers/hc7_degree8_deleted_colour_k4_contact_barrier_verify.py
```

The final output is

```text
five_colourings=253200 colourful_on_U=253200
routing_pairs=10 designated_paths=shortest_disjoint
rooted_K4_models=927 maximum_contact_vector_e_r1_r2_r3_r4=(1,4,4,4,4)
explicit_U_rooted_K5=PASS
scope=fixed-deletion contact shortcut only; existential deletion survives
```

## 7. External input

The shortcut starts from A. Martinsson and R. Steiner,
[*Strengthening Hadwiger's conjecture for 4- and 5-chromatic graphs*](https://doi.org/10.1016/j.jctb.2023.08.009),
Journal of Combinatorial Theory, Series B 164 (2024), 1--16, Theorem 1.3.
That theorem correctly supplies a rooted `K_4` for one colourful set; it
does not assert the additional contact property refuted here.
