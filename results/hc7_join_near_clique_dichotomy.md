# A sharp connectivity dichotomy for joins with a complete graph

**Status:** written proof; the parameterized form is separately internally
audited in the adjacent audit note.  The theorem disposes of every
complete-factor join as a source of highly connected counterexamples without
the corresponding exact separator.  The accompanying icosahedral example
shows that the separator outcome is sharp.

Throughout, `K_r \vee H` denotes the graph join of a complete graph `K_r`
and a vertex-disjoint graph `H`.

## 1. Complete joins add exactly their order to the Hadwiger number

### Lemma 1.1

For every graph `H` and integer `r>=0`,

\[
                    \eta(K_r\vee H)=r+\eta(H).
\]

### Proof

The lower bound follows by taking the `r` vertices of `K_r` as singleton
branch sets and adjoining them to any complete-minor model in `H`.

Conversely, let `\mathcal M` be a `K_t`-minor model in `K_r\vee H`.  At most
`r` branch sets of `\mathcal M` meet the `K_r` side.  Delete those branch
sets.  Every remaining branch set lies wholly in `H`, remains connected in
`H`, and every two remaining branch sets are adjacent by an edge of `H`.
Thus `H` contains a `K_{t-r}` minor whenever `t>r`, and in all cases
`t<=r+\eta(H)`.  This proves the reverse inequality. \(\square\)

## 2. The join dichotomy

### Theorem 2.1 (complete-factor join dichotomy)

Let `r>=0`, let `F` be a graph, and put

\[
                         G=K_r\vee F.
\]

If `G` is `(r+5)`-connected, then at least one of the following holds:

1. `G` contains a `K_{r+5}` minor;
2. `G` has an actual separation of order `r+5`.

Here an actual separation means that deleting the separator leaves at
least two nonempty components.

### Proof

Let `R` be the `r` vertices on the complete side of the join.  If `F` has a
`K_5` minor, Lemma 1.1 gives a `K_{r+5}` minor in `G`.  We may therefore
assume that `F` is `K_5`-minor-free.

The `(r+5)`-connectivity of `G` implies that `F` is five-connected.
Indeed, if a set `Z subseteq V(F)` of order at most four disconnected `F`,
then `Z union R` would be a cut of `G` of order at most `r+4`.  The order
condition in the definition of connectivity also ensures that `F` has
enough vertices for this statement.

By Wagner's theorem in its four-connected form, every four-connected
`K_5`-minor-free graph is planar.  Hence `F` is planar.  A planar graph has
a vertex `v` of degree at most five, while five-connectivity gives
`d_F(v)>=5`; consequently `d_F(v)=5`.

The graph `F` has at least seven vertices.  Otherwise five-connectivity
would force a graph on six vertices to be complete, contradicting either
planarity or the exclusion of a `K_5` minor.  Therefore

\[
                       S=R\cup N_F(v)
\]

has order `r+5`, and `G-S` contains both the isolated vertex `v` and at
least one further vertex of `F-N_F[v]`.  Thus `S` is an actual separator
of order `r+5`. \(\square\)

For `r=2`, this says exactly that a seven-connected graph `K_2\vee F`
contains a `K_7` minor or has an actual separation of order seven.

### Corollary 2.2 (Hadwiger colouring for complete-factor joins)

For every `r>=0`, if `K_r\vee F` has no `K_{r+5}` minor, then it is
`(r+4)`-colourable.

### Proof

Lemma 1.1 implies that `F` has no `K_5` minor.  The known `t=5` case of
Hadwiger's conjecture gives a proper four-colouring of `F`.  Give the `r`
vertices of the complete factor distinct new colours.  This is a proper
`(r+4)`-colouring of the join. \(\square\)

In particular, a `K_7`-minor-free graph `K_2\vee F` is six-colourable,
whether or not it is seven-connected.

### Consequence for the active programme

No graph of the form `K_2\vee F` can refute the conjectural statement

\[
 \text{seven-connected + spanning singleton-root }K_7^-\text{ model}
 \Longrightarrow K_7\text{ minor or an order-seven separation}.
\]

The structural conclusion holds for the entire join family without using
the near-complete model, a colouring hypothesis, or contraction-criticality.
Corollary 2.2 further shows that no `K_7`-minor-free graph in the `K_2`-join
family can be a seven-chromatic counterexample at all.  More generally, no
complete-factor join can violate the corresponding parameterized colouring
or minor-or-exact-separator conclusion.  Such joins remain useful tests for
unsafe colour-to-branch-set assertions, but not as counterexamples to these
conclusions.

## 3. Sharpness: the icosahedral join

Let `I` be the icosahedral graph with edge set

```text
01 05 07 08 0(11)
12 15 16 18
23 26 28 29
34 36 39 3(10)
45 46 4(10) 4(11)
56 5(11)
78 79 7(10) 7(11)
89 9(10) (10)(11).
```

Put `G=K_2\vee I`, and denote the complete-side vertices by `p,q`.  Choose
the nonadjacent roots

\[
                           a=0,\qquad b=2.
\]

Then the following seven sets partition `V(G)`:

\[
 \{a\},\ \{b\},\ \{p\},\ \{q\},\
 \{1,3,4,5,6\},\ \{7,8\},\ \{9,10,11\}.               \tag{3.1}
\]

They form a spanning `K_7`-minus-one-edge model whose unique missing pair
is `\{a\},\{b\}`.  In

\[
                            J=G-\{a,b\},
\]

the sets

\[
                       X=\{p\},\qquad Y=\{q\}
\]

are connected, every vertex of `Y` has a neighbour in `X`, and the triangle

\[
                              C=1\,5\,6\,1
\]

is an induced cycle disjoint from them and every one of its vertices has a
neighbour in each of `X,Y`.
Thus this example has exactly the normalized dominating-`K_5` substrate
used by the active exchange programme: explicitly,

\[
                  (\{p\},\{q\},\{1\},\{5\},\{6\})
\]

is the corresponding ordered dominating model.

Nevertheless `G` has no `K_7` minor.  The graph `I` is planar and hence
has no `K_5` minor, so Lemma 1.1 gives `\eta(G)<=6`.  The graph is
seven-connected because `I` is five-connected.  Finally,

\[
             \{p,q\}\cup N_I(0)=\{p,q,1,5,7,8,11\}
\]

is an actual order-seven separator: its deletion isolates `0` and leaves
six other icosahedral vertices.

This is not a counterexample to Theorem 2.1.  It proves instead that even
the simultaneous presence of the spanning singleton-root near-clique model
and the normalized dominating-cycle substrate cannot remove the
order-seven alternative.  The graph is six-chromatic, not strongly
seven-contraction-critical, so the example makes no sharpness claim after
that additional global hypothesis is imposed.

## 4. Verification

Run

```bash
python3 results/hc7_join_near_clique_dichotomy_verify.py
```

The script checks the displayed icosahedral embedding certificate,
five-connectivity of `I`, seven-connectivity of the join, all branch-set
and substrate adjacencies, and the stated order-seven cut.
