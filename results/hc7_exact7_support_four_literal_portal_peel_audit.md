# Audit: literal portal peel from a non-singleton support-four lobe

**Verdict:** GREEN at frozen source SHA-256
`644ffb60abc71884354f18fe92b043f8f1ec55207523f3a0527982729a8f9179`.
The only change from the source audited line by line was the status line,
updated from locally proved to independently audited.

The removable-portal theorem, its two-carrier consequence, and the
full-row allocation are correct in the exact-fragment setting stated in
the note.  Every cut used in the proof is a literal cut in `G`; no quotient
edge, palette-to-label lift, or connectivity above seven is used.

## 1. Scope and literal separation

The hypothesis

\[
 N_G(D)=T\mathbin{\dot\cup}A,
 \qquad |T|=3,\quad |A|=4
\]

and the nonempty far side mean precisely that
`G-(D union T union A)` is nonempty.  Thus `T union A` is an actual
seven-boundary for the nonempty connected set `D`.

In the carrier consequence, "a second lobe" has its standard meaning from
the surrounding exact-fragment setup: `D,E` are distinct components of
`G[L]-T`, while `S` is the old literal boundary, `A=N_S(D)`, and
`L=D dotunion T dotunion E`.  Hence `D,E,T,S` have the required literal
disjointness.  Section 2 states this two-lobe decomposition explicitly.
Under this convention, every support identity in (1.3) is well-defined.
For a standalone version, binding `S` and spelling out this lobe convention
in the first paragraph would improve presentation, but it introduces no
extra hypothesis in the active HC7 application.

## 2. Removable vertices and the no-cutvertex branch

If connected `G[D]` has no cutvertex, every `x in D` is removable; this
includes the extremal case `G[D]=K_2`, since deleting either endpoint
leaves a nonempty connected singleton.

There must be at least two distinct vertices of `D` with neighbours in
`A`.  If `x` were the unique one, then after deleting `T union {x}`:

* `D-x` would be nonempty and connected;
* it would have no remaining edge to `A` by uniqueness of `x`;
* it would have no edge outside `D union T union A` by the displayed
  neighbourhood equality; and
* the stipulated far side would remain nonempty.

Thus `T union {x}` would be a literal cut of order four, contrary to
seven-connectivity.  No edge through an undeleted boundary vertex has been
overlooked.

## 3. Leaf blocks and the cutvertex branch

If `G[D]` has a cutvertex, its block-cut tree has at least two leaf blocks.
For a leaf block `B`, let `w` be its unique cutvertex of `D`.  The set
`B-w` is nonempty, and its vertices have no neighbour in `D-B` except
through `w`.

If no vertex of `B-w` contacted `A`, deleting `T union {w}` would separate
the nonempty leaf-block side from the nonempty far side.  This is again a
literal cut of order at most four.  Therefore some vertex of `B-w`
contacts `A`.

Every vertex of `B-w` is removable in `D`: a nontrivial leaf block is
either a two-connected block, in which deletion of a non-cutvertex leaves
the block connected, or a bridge block `K_2`, in which deletion of its leaf
leaves `w`; all other blocks remain joined through `w`.  Distinct leaf
blocks give distinct vertices outside their respective attachment
cutvertices.  Consequently the proof really obtains two distinct
removable `A`-portal vertices.  This also verifies the smallest path and
leaf-`K_2` configurations.

## 4. Row dichotomy and the second literal cut

Each of the two removable portal vertices has a nonempty row in `A`.  If
one row is proper, choosing that vertex gives
`emptyset ne M=N_A(x) proper subset A`.  Otherwise both displayed portal
vertices have row all of `A`; choosing either gives the stronger full-row
facts

\[
                    M=A,\qquad N_A(D-x)=A.
\]

Thus the proof establishes the intended exclusive alternatives, slightly
stronger than item 4's wording.

If `D-x` had no neighbour in `T`, deletion of `A union {x}` would isolate
the nonempty connected set `D-x` from the nonempty far side: its only
possible neighbours outside `D` lie in `T union A`, it has no `T` contact
by assumption, and any route through `x` is deleted.  This is a literal cut
of order five, contradicting seven-connectivity.  Hence item 3 is valid.

## 5. Carrier construction and supports

The sets

\[
 X=\{x\},\qquad Y=(D-x)\cup T\cup E
\]

are disjoint in the two-lobe setup.  The singleton `X` is connected.
The connected lobe `E` meets all three members of `T`, so `T union E` is
connected; the newly proved `D-x`--`T` edge then makes `Y` connected.
Because `D` is connected and `D-x` is nonempty, `x` has a literal neighbour
in `D-x`, supplying the claimed `X-Y` edge.

Since `A=N_S(D)`, the singleton support is exactly

\[
                         N_S(X)=N_A(x)=M.
\]

The definition `C^+=N_S(T union E)` puts all of `C^+` in `N_S(Y)`.  If
`a in A-M`, then `a` has a neighbour somewhere in `D` but not at `x`, so it
has a neighbour in `D-x subseteq Y`.  Hence

\[
                 C^+\cup(A-M)\subseteq N_S(Y).
\]

In the actual full-row branch, both `M=A` and `N_A(D-x)=A`; therefore `X`
is `A`-full and `Y` contains all of `A union C^+` in its support.

## 6. Why the full-row carrier is `S`-full

In Section 2, the whole two-lobe thin shore
`L=D dotunion T dotunion E` is `S`-full.  A literal label outside
`A=N_S(D)` has no neighbour in `D`, so its required thin-shore contact lies
in `T union E subseteq Y`.  Labels in `A` contact `D-x subseteq Y` in the
full-row branch.  Thus `Y` is genuinely `S`-full, while `X` is `A`-full.
The two carriers remain disjoint, connected and adjacent as checked above.

## 7. Allocation in all three width-two boundary forms

The connected frontier alternatives are a tree and a six-cycle with one
pendant vertex.  Both are connected bipartite graphs.  Let `Z_0,Z_1` be a
bipartition.  Since `|S-A|=3`, one class can be named so that
`|Z_0-A|<=1`.  Set

\[
 U=Z_0-A,\qquad I=Z_0\cap A,\qquad J=Z_1.
\]

Then `U` is an empty or singleton clique, and `I,J` are independent.  The
class `J` is nonempty.  The class `I` is also nonempty: otherwise connectedness
would force `Z_0` to be a singleton outside `A` and the whole boundary to
be a star centred at that singleton.  Since `c in A` would then be a leaf,
it would have degree one, contradicting that it has a neighbour in each of
the three disjoint blocks `B_i`.  The `A`-full carrier contacts `I`, and
the `S`-full carrier contacts `J`, so the adaptive two-carrier theorem
applies.  This argument covers both connected frontier forms uniformly.

For the disconnected frontier `K_{1,3} dotunion K_3`, paired-state
incidence forces `c` to be the claw centre: `c` has at least three distinct
neighbours, whereas a triangle vertex and a claw leaf have degree two and
one respectively.  Taking

\[
 I=\{c\},\qquad J=\{\text{the three claw leaves}\},
 \qquad U=V(K_3)
\]

gives two nonempty independent seeds and a clique reservoir.  The
`A`-full carrier contacts `I`, the `S`-full carrier contacts `J`, and the
adaptive theorem again applies.

Hence Lemma 2.1 covers all three width-two boundary types and legally
six-colours the strongly contraction-critical host in the full-row branch.

## 8. Trust boundary

The theorem does not close the proper-row case.  There one still needs a
label-faithful split satisfying (3.2), or a literal small cut/near-model
output.  The proof also deliberately excludes singleton lobes.  Neither
restriction is weakened by this audit.
