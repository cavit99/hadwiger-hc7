# A local root condition closes a concentrated two-piece rotation

## Status and role

This is a theorem-local strengthening of the three-connected donor
argument.  It is **active and awaiting independent audit**.  It is not a
new terminal of the `HC_7` proof spine.

Its role is to identify the exact residue of a concentrated `q=2`
two-piece rotation.  Three-connectivity of the whole donor is more than is
needed: one selected root in a locally robust position already closes the
rotation.  Consequently, after the literal `K_7`, actual-adhesion, and
smaller-centre outputs have been excluded, every selected root is forced
onto the donor's block--2-cut skeleton.

## Lemma 1 (two-sided neighbour partition)

Let `H` be a 2-connected graph, let `s,t` be distinct vertices, and let
`Q` contain at least two vertices.  There is a partition

\[
                         V(H)=L\mathbin{\dot\cup}R
\]

such that `H[L]` and `H[R]` are connected, `s in L`, `t in R`, and both
`L` and `R` meet `Q`.

### Proof

Add `st` if necessary and take an `st`-numbering

\[
                        v_1=s,v_2,\ldots,v_n=t.
\]

Every proper prefix and suffix is connected.  This connectivity never
uses the possibly artificial edge `st`, because that edge has the first
and last vertices as its ends and lies in no proper prefix or suffix.

Let `p<q` be the least and greatest positions occupied by `Q`.  For any
`k` with `p<=k<q`, the prefix through `v_k` and the complementary suffix
give the required sets. \(\square\)

## Theorem 2 (local-root concentrated-rotation closure)

Let `mu>=2` be the minimum deficient-centre order among all labelled
`K_7^vee` models in `G`.  Suppose a transported labelled model has bags

\[
                     X,B,C,U,V_1,V_2,V_3
\]

with the following properties.

1. `B,C,U,V_1,V_2,V_3` form a `K_6` model.
2. `X` is connected, is anticomplete to `B,C`, and meets
   `U,V_1,V_2,V_3`.
3. Four distinct selected vertices of `N(X)` lie in `U`.
4. The comparison class permits any labelled near model constructed
   below to be compared with `mu`.

If one selected root `r in U` satisfies

\[
             G[U-r]\text{ is 2-connected},\qquad
             |N_U(r)|\ge2,                              \tag{2.1}
\]

then at least one of the following occurs.

1. `G` contains a `K_7` minor.
2. Some nonempty connected proper `Y subset U` has an actual separator
   `N_G(Y)` of order at least seven (and the usual full-contact property
   when its order is exactly seven).
3. There is a labelled `K_7^-` or `K_7^vee` model whose deficient centre
   is the singleton `{r}`, contradicting `mu>=2`.

### Proof

Choose two other selected roots `s,t`.  Apply Lemma 1 to

\[
                 H=G[U-r],\qquad Q=N_U(r).
\]

This gives connected `L,R` partitioning `U-r`, with `s in L`, `t in R`,
and with both `L,R` adjacent to `r`.  Thus

\[
                    U=\{r\}\mathbin{\dot\cup}L
                               \mathbin{\dot\cup}R       \tag{2.2}
\]

is a connected three-part partition, and both moved parts contain a
selected `X`-neighbour.

If `L` or `R` misses `B` or `C`, its open neighbourhood is an actual
separator: the moved part is a nonempty shore and the missed connected
twin bag is a nonempty far shore.  Seven-connectivity gives conclusion
2, including fullness at equality.

Otherwise both `L,R` meet both twins.  Assign `L` to `B` and `R` to `C`.
The enlarged twins are connected, the edges from `r` into both pieces
restore the two centre--twin spokes, and `r` meets `X` because it was a
selected root.  Hence

\[
              X,\ B\cup L,\ C\cup R,\ V_1,V_2,V_3
\]

are the six foreign bags of a near-`K_7` model centred at `{r}`.  The
singleton centre can miss only some of `V_1,V_2,V_3`.

If it misses none, the seven bags give `K_7`.  If it misses one or two,
they give `K_7^-` or `K_7^vee` with centre order one, contradicting
`mu>=2`.  If it misses all three, `N_G(r)` separates `{r}` from any one
of the connected `V_i`, giving conclusion 2.  These cases exhaust the
possibilities. \(\square\)

## Corollary 3 (exact surviving root condition)

In a target-free concentrated donor, every selected root `r` satisfies

\[
                 d_U(r)\le1
          \quad\hbox{or}\quad
                 G[U-r]\text{ is not 2-connected}.      \tag{3.1}
\]

Thus the remaining directed two-piece rotation is already localized to
cutvertices, 2-separations, and cycle torsos.  This corollary does not lift
virtual torso edges and is not itself a composition theorem.

## Trust boundary

The proof uses an actual selected root and literal donor edges.  It does
not say that an arbitrary virtual 3-connected torso is sufficient, and it
does not turn an internal 1- or 2-separation into a small separator of the
ambient graph without accounting for all external portal rows.
