# Independent audit of compact-model completion at an almost-universal boundary vertex

## Verdict and exact revision

**GREEN.**  This audit checks
[`hc_almost_universal_straddling_completion.md`](hc_almost_universal_straddling_completion.md)
at exact SHA-256

```text
e956d08b9c0c7fadb76b01f0b82ea5f231fe2148a376c431487b9fb5481c0731
```

Theorem 1.1 and Lemma 2.1 are correct under their stated hypotheses.
Corollary 3.1 is correct conditional on the cited mixed-shore normalization;
this audit checks the implication from that normalization, including the
singleton-side alternative, but does not re-prove the upstream normalization.
None of these statements or their combination proves `HC_7`: an order-`k`
separation is an allowed conclusion and is not ranked or oriented here.

The pre-audit draft had SHA-256

```text
4e55ab3acfaa330dcd9903722e52e9f35891fd342be444c050c36cd7eecc4a49
```

One proof sentence in its second case incorrectly suggested that the total
support after path enlargement remains at most `m`.  Internal path vertices
can increase total support.  The audited revision replaces that sentence by
the exact statement needed and proved: the enlarged model uses at most
`m-1` vertices of `B`.  The theorem statement and all other mathematical
content are unchanged.

## 1. The component neighbourhood and the first separator

Let `C` be a component of `V-v`.  Because `V` is a component of `G-S`, a
vertex of `C` has no neighbour outside `V union S`.  Because `C` is a
component after deleting `v`, its only possible neighbour in `V-C` is `v`.
Connectedness of `V` ensures that such a neighbour exists.  Hence

```text
N_G(C)={v} union N_S(C).
```

If `|N_S(C)|<=k-1`, this neighbourhood has order at most `k`.  Order below
`k` contradicts `k`-connectivity.  At order `k`, deleting it leaves the
nonempty set `C` and the distinct nonempty component `U` on opposite sides,
so the separation is actual.  Therefore the proof may assume
`|N_S(C)|>=k`, and `C` misses at most one of the `k+1` boundary vertices.

No assumption that `U,V` are the only components of `G-S` is needed here.
The distinct full component `U` is used only to certify the nonempty opposite
side of each separator.

## 2. Case in which `C` is adjacent to `p`

Let `y` be the unique missed boundary vertex if one exists.  The set `W`
defined in (1.3) has order at least `k-2`, is contained in `B`, and every
one of its vertices is adjacent both to `C` and to `p`:

- `p` is adjacent to all of `B` by hypothesis;
- if `C` misses a vertex of `B`, that vertex is deleted from `W`; and
- if its missed vertex is `p`, `x`, or nonexistent, `C` sees all of `B`.

Let `q` model branch sets avoid `W`.  One selected vertex from each gives
`q` distinct support vertices outside `W`.  The model vertex `v` is another
support vertex outside `W`.  It is distinct from all selected vertices:

- if its branch set meets `W`, that branch set is not selected; and
- if its branch set avoids `W`, the fact that it also contains `t in B`
  forces `t=y`, and the proof selects `t`, not `v`.

Consequently

```text
|V(mathcal M) cap W| <= m-q-1,
|T| >= |W|-m+q+1 >= q.
```

The deleted set has exact order

```text
|Z|=(m-q)+2=m-q+2,
```

since the model avoids `p,x`.  If `q>0` and the linkage fails, set-Menger
gives an `A`--`T` separator `X` in `G-Z` with `|X|<=q-1`.  Because
`|A|=q` and `|T|>=q`, neither terminal set is swallowed by `X`.  Thus
`Z union X` really disconnects two nonempty sets, and

```text
|Z union X| <= m+1 <= k.
```

This is either a contradiction to connectivity or an actual order-`k`
separation.  The count remains valid when equality occurs at every bound.

In the linkage outcome, exactly `q` disjoint paths use all `q` starts.
Stopping each path on its first visit to `W` gives a terminal in `T`: every
old model vertex in `W` belongs to `Z`.  The stopped paths avoid `C`.
Indeed, every entrance into `C` is through `v` or `S`; the vertices
`v,p,x` are deleted, a possible `y` has no neighbour in `C`, and every
other possible boundary entrance is in `W`, where the path stops.
They meet the old model only at their assigned starts because all remaining
old support vertices are deleted.

After enlargement, every one of the `k-2` old branch sets contains a
distinct vertex of `W` and avoids `C`.  The branch sets

```text
mathcal M, V(C), {p}
```

are disjoint and connected.  Old rows retain their clique adjacencies;
both new branch sets are adjacent to every old row through its `W` vertex;
and `C` is adjacent to `p` in this case.  These are all adjacencies of a
`K_k` model.  If `q=0`, the same conclusion holds without enlargement.

## 3. Case in which `C` is not adjacent to `p`

Now `p` is the unique boundary vertex missed by `C`, so `C` is adjacent to
every vertex of `B`.  A branch set avoiding `B` cannot be the branch set
containing `v`, because that branch set also contains `t in B`.  Hence `v`
is not selected and belongs to `Z`.

The `q` selected roots and `v` are `q+1` distinct support vertices outside
`B`.  Therefore

```text
|T| >= (k-1)-m+q+1 >= q+1.
```

The same deleted-set and failed-linkage calculation again gives a separator
of order at most `m+1<=k`.  The stopped paths avoid `C`: its possible
entrances are `v` and the boundary, with `v,p,x` deleted and every other
boundary vertex in the stopping set `B`.

Before enlargement at most `m-q-1` support vertices lie in `B`.  The `q`
stopped paths each add exactly one vertex of `B`, their distinct terminal,
because each is stopped on its first visit to `B`.  Thus at most `m-1`
vertices of `B` are used after enlargement.  Since `m<=k-1` and
`|B|=k-1`, there is an unused `z in B`.

For the final model

```text
mathcal M, V(C) union {z}, {p},
```

the middle set is connected because `C` is adjacent to `z`.  It and `p`
are adjacent to every old row through that row's distinct `B` vertex, and
their mutual adjacency is the edge `pz`.  Disjointness follows from the
choice of unused `z`, the old model's avoidance of `C`, and deletion of
`p,x` from the original model.  This verifies every required adjacency.

## 4. Lemma 2.1

Let `m` be the support order, let `q` branch sets avoid the chosen common-
neighbour set `W`, and retain one root from each.  With

```text
Z=(old support minus retained roots) union {a,b},
T=W minus old support,
```

one has `|Z|=m-q+2` and

```text
|T| >= (k-1)-(m-q) >= q.
```

For `q>0`, a failed linkage supplies a separator of order at most `q-1`.
Both terminal sets retain a vertex, and the resulting separator in `G` has
order at most `m+1<=k`; it is therefore either forbidden or actual.  In a
successful linkage, stopping at the first visit to `W` prevents entry into
an already used common neighbour.  Every other old model vertex and both
`a,b` are deleted, so path enlargement preserves model disjointness.  All
old rows then meet distinct common neighbours of the adjacent vertices
`a,b`, and adjoining `{a},{b}` gives all adjacencies of a `K_k` model.
The case `q=0` is exactly the already-anchored case.

## 5. Corollary 3.1, including the singleton side

The non-singleton alternative imports the following precise data from the
mixed-shore normalization:

- an order-eight boundary `S` and two connected boundary-full open shores;
- vertices `p,x in S` with `p` adjacent to `S-{p,x}`;
- a support-six `K_5` model in `G-{p,x}`;
- exactly one support vertex `v` in one shore; and
- a vertex `t in S-{p,x}` in the same branch set as `v`.

If that shore contains another vertex, these are exactly Theorem 1.1's
`k=7` hypotheses.  No property of the six-vertex theta graph is used by the
completion theorem itself.

If the shore is the singleton `{v}`, boundary fullness gives `pv in E(G)`
and makes every one of the six vertices in `S-{p,x}` a common neighbour of
`p,v`: `v` sees all of `S`, while `p` sees all of `S-{p,x}`.  The hypothesis
on every two-vertex deletion supplies a support-at-most-six `K_5` model in
`G-{p,v}`.  Lemma 2.1 with `k=7`, `a=p`, and `b=v` therefore applies
exactly.  The singleton argument does not require the original mixed-shore
model after this point.

The corollary is not standalone: the phrase “forced-theta outcome” imports
the normalization listed above.  This audit has not re-audited its separate
proof.  Subject to that explicit dependency, both branches of the corollary
are GREEN.

## 6. Adversarial scope check

Attempts to remove the main hypotheses identify why each is used rather
than a counterexample to the stated theorem:

- without the support bound `m<=k-1`, a failed linkage may give a separator
  larger than `k`, and the unused vertex `z` need not exist;
- without the common branch set containing `v,t`, the vertex `v` can be the
  only selectable root of a branch set avoiding `W`, destroying the extra
  unit in (1.5);
- without boundary fullness, neither the component-neighbourhood count nor
  the final adjacencies are forced;
- without adjacency from `p` to every vertex of `B`, the anchored old rows
  need not be adjacent to `{p}`; and
- if `V-v` is empty, Theorem 1.1's component argument is unavailable, which
  is exactly why Lemma 2.1 handles the singleton case separately.

No construction satisfying all stated hypotheses avoids both conclusions.
All separator outcomes retain nonempty vertices on both sides, all path
truncations preserve labels and disjointness, and all final branch-set
adjacencies have been checked explicitly.
