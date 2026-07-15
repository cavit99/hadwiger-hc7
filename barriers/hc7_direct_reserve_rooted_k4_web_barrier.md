# Direct-reserve rooted-`K_4` web barrier

**Status:** exact local barrier with a solver-free verifier.  This is not an
`HC_7` counterexample and does not satisfy the rich-shore or global
minor-critical hypotheses.  It falsifies only the shortcut which tries to
upgrade the regenerated rooted diamond using the old bad paths and the two
automatic contacts of the reserved component.

## The substituted host

Let the ordered roots be `(z,x,y,r)`.  Take three internal vertices
`t1,t3,t5` and the edges

```text
x-t1, x-t3, x-y, x-t5,
t1-z, t1-t5, t1-r,
z-t3, z-t5,
t3-y, t3-t5.
```

Thus the four vertices `x,t1,z,t3` form an outer cycle and `t5` is its
hub.  The vertex `y` is added outside the edge `x-t3`, and `r` is a leaf at
`t1`.  This gives a planar embedding with `z,x,y,r` incident with one face
(the face boundary may repeat `t1` at the bridge `t1-r`).

The bags

```text
Bz = {z,t3,t5},  Bx = {x},  By = {y},  Br = {r,t1}
```

form a rooted `K_4^-`, missing only `By-Br`.  An exhaustive assignment of
the three internal vertices to four rooted bags proves that no rooted
`K_4` exists.  Notice the features that were supposed to repair it:

- the old direct connector `xy` is literal and is not the missing pair;
- `z` is nonadjacent to `x,y,r`;
- the closed-shore graph on `{z,t1,t3,t5}` is `K_4` minus `t1-t3`, hence
  is 2-connected and noncyclic, and `d_A(z)=3`;
- the rooted host is internally four-connected in the relevant sense:
  after deleting fewer than four vertices, every remaining component
  contains a surviving root.

This is the precise cofacial/web obstruction left by the rooted-minor
theory.  Fabila-Monroy--Wood prove that a 3-connected graph has a rooted
`K_4` exactly when it is not a spanning subgraph of a four-root web, and
give the complete six-class characterization without 3-connectivity
([paper](https://doi.org/10.37236/3476), Theorems 8 and 15).  The host here
is only internally four-connected relative to its roots—`r` may have
degree one—so the ordinary 3- or 4-connected corollaries cannot be invoked.

## Literal bad-path extension

Let the seven boundary vertices induce the path

```text
x-y-b-c-r-a-u.
```

Keep the contacts above, add the unique `A-u` edge `zu`, and make each of
`a,b,c` adjacent to every vertex of `A={z,t1,t3,t5}`.  Then:

- `xy` is the direct bad path;
- `r-a-u` is a nontrivial bad path, with retained root `r`;
- in `H-{x,y,r}`, the component `C={a,u}` containing `u` contacts the
  `z`-root through `uz` and the `r`-root through `ar`;
- `A-z` is connected and meets every vertex of `W=S-{u}`;
- every connected nonempty `D subseteq A` satisfies the necessary
  relative seven-cut inequality
  `|N_A(D)|+|N_S(D)| >= 7`.

Nevertheless the substituted host still has no rooted `K_4`.  Therefore
the direct edge, nontrivial old path, unique `zu`, and the two forced
contacts of `C` do **not** by themselves repair the rooted diamond.

The same extension is not a counterexample to the active exchange theorem:
it already has adjacent duty-faithful carriers

```text
C0={t1}, C1={t3,z}, U={r},
I0={x,b,a}, I1={y,c,u}.
```

The two `I`-sets are independent in `H-U`; each carrier meets every member
of its assigned set, and `C0` is adjacent to `C1` through `t1-z`.  Hence
this instance exits through the permitted adaptive-carrier terminal.

## Sharp replacement target

The active proof must not assert `rooted K_4^- + C with two contacts =>
rooted K_4`.  The correct next lemma has to use the *omitted boundary
labels and all literal bridges*:

> **Web-crossing-or-return target.**  In the frozen direct-reserve atom,
> if the substituted four-root host is contained in a rooted web, then an
> omitted-label bridge either crosses the rooted face order and yields a
> rooted `K_4`, yields two adjacent duty-faithful carriers, or is confined
> behind an actual separation returned with the exact equality/near-model
> data required by the active handoff.

Two contacts from the canonical reserved component are below the sharp
threshold: the example realizes them on one side of the web.  A proof must
extract a third suitably ordered contact, a second independent bridge, or
the adaptive carrier/gate certificate.  That is a genuine bridge-exchange
principle; a static contact-count argument cannot close the cell.
