# Four-connected carrier with five facial roots and up to two extra terminals

## Status

Proved from the audited four-connected rooted clique-or-fan theorem.  This
is a general rooted-model statement, independent of `HC_7`.

## Theorem 1.1

Let `H` be a simple four-connected graph.  Let `W` be five prescribed
vertices, and let `B` be a disjoint set of at most two further prescribed
vertices.  Then one of the following holds.

1. Four members of `W` root a `K_4` minor in `H`.
2. The graph `H` is planar and one facial cycle `C` contains all of `W`.
   Moreover:

   * if `B subseteq V(C)`, cutting `C` at `W union B` and adding the
     peripheral remainder to any prescribed boundary bag gives a rooted
     `K_1 join P_{|W union B|-1}` model with any chosen universal root;
   * if `b in B-V(C)`, put

     ```text
     D=(H-b)-V(C).
     ```

     Then `D` is nonempty and connected, every vertex of `C` has a
     neighbour in `D`, and `b` has a neighbour in `D`.  The boundary-arc
     bags rooted at `(W union B) cap V(C)`, the singleton bag `{b}`, and
     the bag `D` are pairwise disjoint, with the following literal
     adjacencies:

     ```text
     boundary arcs form a cycle;
     D is adjacent to every boundary arc and to {b}.
     ```

     If the other member of `B`, when present, is also off `C`, it belongs
     to `D`; hence the two bad terminals still lie in distinct bags.

The last carrier may include one unrooted bag `D` when `B={b}`.  When both
members of `B` are off the face, `D` is rooted at the other member and all
displayed bags are terminal-rooted.

## Proof

Apply the audited four-connected terminal clique-or-fan theorem to `W`.
Its rooted-`K_4` outcome is item 1.  Otherwise `H` is planar and all five
members of `W` lie on one facial cycle `C`.

If every member of `B` also lies on `C`, partition the facial cycle into
terminal-rooted arcs in cyclic order.  Its peripheral remainder is
connected and meets every boundary vertex.  Adding that remainder to any
prescribed arc bag makes the bag universal, while the other arc bags form
a path.  This is the first subcase of item 2.

Now fix `b in B-V(C)`.  The graph `H-b` is three-connected.  Since `b` is
not on `C`, deleting it does not destroy the face bounded by `C`, so `C`
remains a facial cycle in `H-b`.  Facial cycles of three-connected plane
graphs are peripheral.  Therefore

```text
D=(H-b)-V(C)
```

is connected.  It is nonempty: otherwise `H-b=C`, a cycle of order at
least five, contrary to three-connectivity.  The cycle `C` is induced in
`H-b`, and minimum degree there is at least three, so every vertex of `C`
has a neighbour in `D`.

The original peripheral remainder

```text
H-V(C)=D union {b}
```

is connected.  Since `D` is nonempty, an edge joins `b` to `D`.  Cut `C`
at the prescribed vertices lying on it.  The resulting arc bags, `{b}`,
and `D` now have exactly the adjacencies asserted in item 2.  If a second
bad terminal `b'` is off `C`, then `b' in D`; it is distinct from the
singleton root `b`.  All bags are literal, connected, and disjoint.
\(\square\)

## Trust boundary

No adjacency from the singleton off-face root to a boundary bag is
asserted.  No contact from a later local core to `D` is asserted.  A
composition decoder may use only the boundary-cycle edges, the `D`-to-rim
edges, and `bD`, in addition to its original literal edges.
