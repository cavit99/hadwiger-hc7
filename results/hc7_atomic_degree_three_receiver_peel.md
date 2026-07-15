# Atomic degree-three receiver peel

**Status:** proved and independently audited.

## 1. Setup

Use the connected-bipartite atomic interface of the asymmetric `(5,6)`
carrier theorem.  Let `v in A-{z}` satisfy

\[
                     A-v\text{ connected},
            \qquad d_{G[A]}(v)\le3.                         \tag{1.1}
\]

Put

\[
 X=\{v\},\qquad Y=A-v,
 \qquad D_X=S-N_S(X),\qquad D_Y=S-N_S(Y).                  \tag{1.2}
\]

### Theorem 1.1

At least one of the following holds.

1. The carriers `X,Y`, after deleting an empty or singleton clique
   reservoir from `S`, satisfy the adaptive clique-reservoir return and
   six-colour `G`.
2. All of the following necessary residual conditions hold:

   * `d_A(v)=3` and `|D_X|=3`;
   * `D_Y={q}`;
   * relative to the bipartition of `H=G[S]`, the three members of `D_X`
     occupy both classes and `q` lies in the class containing two of them;
   * `qv` is the unique edge from `A` to `q`; and
   *
     \[
        \Omega_v=\{v\}\cup(S-\{q\})=N_G(A-v)              \tag{1.3}
     \]
     is an actual order-seven boundary.  The shore `A-v` is connected and
     `Omega_v`-full, and contraction of the named edge `qv` legally attains
     an exact labelled state on the intact closed `(A-v)`-shore.

Outcome 2 is a **one-sided receiver certificate**, not a reflected state or
a recursive closure.

### Proof

Relative seven-connectivity applied to `X` and `Y` gives

\[
                         |D_X|\le d_A(v)\le3,
                   \qquad |D_Y|\le1.                       \tag{1.4}
\]

Since `X union Y=A` is `S`-full,

\[
                         D_X\cap D_Y=\varnothing.           \tag{1.5}
\]

Vertices in `D_X` are forced to the carrier `Y`, vertices in `D_Y` are
forced to `X`, and all other boundary vertices permit either carrier.  If
`|D_X|<=2`, Theorem 2.1 of the asymmetric `(5,6)` closure applies.

Assume `|D_X|=3`.  If `D_Y` is empty, delete a member of the minority
bipartition class of `D_X` when both classes occur; if all three lie in one
class, delete nothing.  The surviving prescriptions have one orientation.

Now let `D_Y={q}`.  Deleting `q` works whenever the three members of `D_X`
lie in one bipartition class.  If they have a `2:1` split and `q` lies in
the class containing only one member, delete that member.  All other
patterns with fewer than three members were already covered by the
`(5,6)` theorem.  Consequently failure of every such sufficient
list-colouring can remain only in the displayed `2:1` pattern with `q` in
the majority class.  This pattern is necessary, not asserted sufficient:
deleting a vertex may split `H` and allow further componentwise choices.

In the residue, `q notin D_X`, so `qv` is an edge, while `q in D_Y` says
that `q` has no neighbour in `A-v`.  Thus `qv` is the unique `A-q` edge.
Every member of `S-{q}` contacts `A-v`, and connectedness of `A` makes `v`
adjacent to `A-v`.  There is no `A-R` edge.  Hence (1.3) holds.  The far
open shore contains `R union {q}`, so `Omega_v` is an actual seven-cut and
`A-v` is full to it.

Contract `qv` toward the labelled boundary vertex `v`.  The minor is
proper and therefore has a six-colouring.  Nothing in `A-v` or
`Omega_v-{v}` is contracted.  Restricting the minor colouring to
`G[(A-v) union Omega_v]` is proper (the contraction only adds constraints
at `v`) and induces an exact labelled equality partition on `Omega_v`.
This proves the one-sided state certificate.  \(\square\)

## 2. Exact limitation

The theorem proves none of the following:

* a packet vector or packet orientation for the new separation;
* a demand bound or a paired/canonical form for the attained state;
* a relation between this state and the old boundary state;
* an intact colouring of the opposite closed shore;
* reflection, gluing, a rooted-model terminal, or a global descent rank.

Only the local shore order decreases from `|A|` to `|A|-1`; a later root
exchange may reverse that move.  The certificate is useful precisely
because it names the boundary, root map, and proper-minor operation that a
receiver theorem would have to compose.
