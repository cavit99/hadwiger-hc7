# Literal portal peel from a non-singleton support-four lobe

**Status:** proved and independently audited.  This is a geometric peel
theorem, not a closure of the two-lobe capacity residue.

## 1. Exact-fragment setup

Let `G` be seven-connected.  Let `D` be a connected vertex set of order at
least two such that

\[
                     N_G(D)=T\mathbin{\dot\cup}A,
        \qquad |T|=3,\quad |A|=4.                    \tag{1.1}
\]

Assume that the far side of this separation is nonempty.  This is exactly
the situation of a support-four lobe behind a three-gate: `T` is the gate
and `A=N_S(D)` is its old-boundary support.

### Theorem 1.1 (literal portal peel)

There is a vertex `x in D` for which

1. `D-x` is nonempty and connected;
2. `M=N_A(x)` is nonempty;
3. `D-x` has a neighbour in `T`; and
4. either `M` is a proper subset of `A`, or
   `N_A(D-x)=A`.

Consequently, if `E` is a second connected lobe meeting every member of
`T`, then

\[
                 X=\{x\},\qquad
                 Y=(D-x)\cup T\cup E                 \tag{1.2}
\]

are disjoint adjacent connected carriers.  If
`C^+=N_S(T union E)`, then

\[
             N_S(X)=M,
             \qquad C^+\cup(A-M)\subseteq N_S(Y).     \tag{1.3}
\]

In the second outcome of item 4, `N_S(Y)` contains `A\cup C^+`.

#### Proof

Call a vertex of `D` removable when deleting it leaves `D` connected.
First suppose that `D` has no cutvertex.  Every vertex is removable.  There
are at least two vertices of `D` which contact `A`: if `x` were the unique
one, then `T\cup\{x\}` would separate the nonempty set `D-x` from the
nonempty far side, a cut of order at most four.

Now suppose that `D` has a cutvertex.  Its block-cut tree has at least two
leaf blocks.  If `B` is a leaf block and `w` is its unique cutvertex of
`D`, some vertex in `B-w` contacts `A`.  Otherwise `T\cup\{w\}` separates
the nonempty leaf-block side from the far side, again with order at most
four.  Every vertex of `B-w` is removable in `D`.  Applying this to two
different leaf blocks supplies two distinct removable vertices which
contact `A`.

Thus in either case there are two distinct removable `A`-portal vertices.
If one of them, say `x`, has nonempty proper `A`-row, choose it.  Otherwise
choose either one as `x`; its row is all of `A`, and the other portal vertex
remains in `D-x` and also has row `A`.  This proves items 1, 2 and 4.

If `D-x` had no neighbour in `T`, then `A\cup\{x\}` would separate the
nonempty connected set `D-x` from the far side.  This cut has order five,
contrary to seven-connectivity.  Hence item 3 holds.

The set `X` in (1.2) is connected.  The set `T\cup E` is connected because
`E` meets every gate vertex, and item 3 joins `D-x` to it, so `Y` is
connected.  Since `D` is connected and `D-x` is nonempty, `x` has a
neighbour in `D-x`; this is a literal `X-Y` edge.

Finally, if `a in A-M`, then `a` has no neighbour at `x` but has a neighbour
in `D`, and therefore has a neighbour in `D-x`.  This proves (1.3).  In the
full-row outcome, item 4 supplies all of `A` on the `Y` side.  \(\square\)

## 2. The full-row outcome really closes

Retain the hypothetical-counterexample setting: `G` is strongly
seven-contraction-critical, the opposite shore contains two disjoint
`S`-full packets, and the paired exact-seven width-two boundary satisfies

\[
 S=\{c\}\mathbin{\dot\cup}B_1\mathbin{\dot\cup}B_2
       \mathbin{\dot\cup}B_3,
\]

the three `B_i` are independent, `c` sees every `B_i`, every two blocks
have a cross-edge, and the boundary graph is a tree, a six-cycle with a
pendant vertex, or `K_{1,3} dotcup K_3`.  Suppose additionally that the
four-support `A` contains `c` and one member of every `B_i`, as for a
dutyless support-four lobe.  We are in the two-lobe setting, so
`L=D dotcup T dotcup E` is `S`-full.  In the full-row outcome of
Theorem 1.1 every label of `A` contacts `Y`, while every label outside `A`
has no contact in `D` and therefore contacts `T union E subseteq Y`.
Hence the two carriers in (1.2) are respectively `A`-full and `S`-full.

### Lemma 2.1 (one `A`-full and one `S`-full carrier allocate)

If two disjoint adjacent connected carriers have supports containing `A`
and `S`, respectively, then the adaptive clique-reservoir return theorem
six-colours `G`.

#### Proof

If the boundary is connected, let `Z_0,Z_1` be its bipartition.  Since
`|S-A|=3`, choose the index so that

\[
                         |Z_0-A|\le1.                 \tag{2.1}
\]

Put `U=Z_0-A`, `I=Z_0 cap A`, and `J=Z_1`.  (Here `cap` denotes set
intersection.)  The set `U` is an empty or
singleton clique, while `I,J` are independent.  Moreover `I` is nonempty.
Indeed, otherwise (2.1) makes `Z_0` a singleton outside `A`, so the
connected boundary is a star with that vertex as its centre.  Then `c`,
which lies in the opposite class, has only one neighbour and cannot meet
all three disjoint blocks `B_i`.

The `A`-full carrier contacts `I`, and the `S`-full carrier contacts `J`.
The adaptive theorem applies to `I|J|U`.

If the boundary is `K_{1,3} dotcup K_3`, its component containing `c` is
the claw with centre `c`.  Take `I={c}`, let `J` be the three claw leaves,
and take the triangle as `U`.  Again `I,J` are nonempty independent seed
sets, `U` is a clique, and the two advertised supports contact the two
seeds.  Apply the adaptive theorem.  \(\square\)

Theorem 1.1 and Lemma 2.1 therefore dispose of every non-singleton lobe for
which a removable portal vertex has the full row `A`.

## 3. Exact remaining implication

The proper-row outcome of Theorem 1.1 is not automatically compatible with
the clique-reservoir state.  In the connected frontier, choose a
bipartition `Z_0,Z_1` with `|Z_0-A|<=1` and put

\[
 I=Z_0\cap A,\qquad U=Z_0-A,\qquad J=Z_1.            \tag{3.1}
\]

For the carriers in (1.2), the adaptive return closes whenever

\[
       I\subseteq N_A(x)
       \quad\hbox{and}\quad
       J\subseteq C^+\cup N_A(D-x).                   \tag{3.2}
\]

In the disconnected frontier the corresponding target is

\[
 I=\{c\},\qquad J=\hbox{the claw leaves},qquad
 U=V(K_3).                                             \tag{3.3}
\]

Conditions (3.2) are a labelled two-block linkage condition inside `D`;
they do not follow from the existence of an arbitrary proper portal row.
The obstruction can force every connector meeting the `I`-portal classes
to consume the last portal of some label in `J-C^+`.  Equivalently, the live
geometric implication is:

> either `D` has an adjacent connected split whose first side meets all
> `I`-portals and whose second side retains all `(J-C^+)`-portals, or the
> resulting block-terminal Two-Paths web must decode to a literal cut of
> order at most six or a labelled `K_7^vee`/`K_7` model.

This is the minimal missing step.  Seven-connectivity proves the
unlabelled peel in Theorem 1.1, but it does not by itself choose the exact
duty row in (3.2).  A singleton lobe is a separate degree-seven local cell
and is not covered by Theorem 1.1.
