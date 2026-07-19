# Independent internal audit of the paired-source path transfer

**Verdict:** GREEN for the exact source revision

```text
results/hc7_paired_source_path_transfer.md
SHA-256 f4d36ad58b3ea690a4e77a58cd9f912e2cbf235b2427d1e82dcaf38b0e5ae943
```

The change from the initially checked source is limited to the opening
status line recording this GREEN audit; the mathematics is unchanged.

This is a separate internal mathematical audit, not external peer review.
It checks the literal lift of the fan separator, both branch-set transfers,
preservation of the relaxed first-hit rank, and the extreme two-pole
attachment pattern.  The audit does not strengthen the theorem's stated
trust boundary.

## 0. Imported hypotheses and notation

The audited three-owner concentration theorem supplies the facts used by the
draft:

* the seven labelled branch sets form a spanning model of `K_7` with only
  `X-Y` possibly absent;
* `U=U_0 dotcup C`, where `U_0` and `C` are connected, `U_0` contains the
  prescribed root and the endpoint of the fixed response edge, and `C` is
  adjacent to `U_0` through `k_1,k_2 in U_0`;
* the full host neighbourhood of `C` consists of `k_1,k_2` and exactly one
  representative in each of the six outside branch sets;
* the complete owner set consists of the three named branch sets
  `R_1,R_2,R_3`, so every nonowner contact needed by `U` already survives in
  `U_0`;
* the edges `a_1s_1,a_2s_2` have distinct donor endpoints and distinct owner
  labels and carry the three stated deletion signatures; and
* compatible models are chosen by maximum relaxed literal first-hit rank and
  then minimum donor order.

The fixed response subgraph lies in `D`, which is not one of the three owner
branch sets.  Hence neither transfer modifies that subgraph or its fixed edge
into `U_0`.

## 1. Failure of the five-fan lifts to a literal order-seven separation

Only the path `P` is contracted in

\[
                         H=G[C\cup T]/P.
\]

The Menger separator `Z` excludes its image `r`.  Every member of `Z` therefore
has a unique literal preimage: it is either a vertex of `C-P` or one of the
five displayed terminals.  No contracted branch set is counted as one
separator vertex.

The images of the two designated edges are the direct edges `rs_1,rs_2`.
If either `s_i` survived outside `Z`, that edge would contradict separation
of `r` from `T-Z`.  Thus `s_1,s_2 in Z`.

Let `A` be the lift of the `r`-component of `H-Z`.  Componenthood inside
`C union T`, together with the exact eight-vertex neighbourhood of `C`, gives

\[
                  N_G(A)\subseteq (S-T)\cup Z.
\]

The two sets on the right are disjoint and have total order at most
`3+4=7`.  Since `|T|=5>|Z|`, some terminal `t in T-Z` remains.  Separation
shows that `t` is not adjacent to `A`, while the equality `N_G(C)=S` gives a
neighbour of `t` in `C-A`.  Hence `A` is a nonempty proper subset of `C` and
the displayed set is a genuine host separator with a nonempty opposite side.
Seven-connectivity forces equality throughout:

\[
 |Z|=4,\qquad N_G(A)=(S-T)\mathbin{\dot\cup}Z,
 \qquad |N_G(A)|=7.
\]

Both `a_1,a_2` lie in `P subseteq A` and both `s_1,s_2` lie in `Z`, so the
two designated edges cross this literal separation.  Restriction of each
proper-minor colouring preserves its endpoint signature.  In particular,
the one-edge deletion colouring belonging to either crossing edge supplies a
legal selected response on the new closed shore.  The source correctly makes
no claim that the same partition colours the intact opposite shore.

## 2. Lifting a successful fan

A five-fan to the five-element set `T` has all five vertices of `T` as
distinct endpoints.  Replacing the paths to `s_1,s_2` by the direct edges
does not meet any other fan path.  After expanding `P`, the other three paths
meet one another only in `P`; truncating each at its first point of `P` makes
its part outside `P` disjoint from the other two and from `s_1,s_2`.

Thus the two paths to `k_1,k_2` and the path to `s_3` have exactly the
disjointness properties claimed in the draft.  No palette colour is used to
identify a branch-set label.

## 3. Case A: the third-owner path has an internal part

The set `D_0` consists of `P` and the two lifted paths to `k_1,k_2`; it is
connected and meets `U_0` through those two terminal edges.  The nonempty
internal part `L_3` of the third path is connected, is disjoint from `D_0`,
and has an edge both to `D_0` and to the old branch set `R_3`.

Every remaining component of `C-(D_0 union L_3)` has an edge to at least one
seed because `C` is connected.  Assigning each component to an adjacent seed
therefore yields two nonempty connected sets `D'_0,L'_3` which partition `C`
and remain adjacent.

After replacing

\[
 U\longmapsto U_0\cup D'_0,
 \qquad R_3\longmapsto R_3\cup L'_3,
\]

all seven sets remain nonempty, connected, pairwise disjoint and spanning.
The direct edges retain the `U-R_1` and `U-R_2` contacts; the edge between the
two new pieces retains `U-R_3`; `U_0` retains every nonowner contact; and the
old `R_3` retains all its foreign contacts.  Hence no labelled adjacency is
lost.  An additional `X-Y` contact is terminal; otherwise the same labelled
near-complete model remains.  Since `L'_3` is nonempty, the donor strictly
shrinks.

## 4. Case B: the third-owner path is direct

Let `p_3s_3` be the direct third-owner edge.  Choosing an endpoint `a_i` of
`P` different from `p_3` is always possible, including when `p_3` is internal
to `P`.  If `a_j` is the other endpoint, then `P-a_i` and `p_3` lie in the
component `C'` of `C-a_i` containing `a_j`.  The complement

\[
                              L=C-C'
\]

is connected: it contains `a_i`, and every other component of `C-a_i` has an
edge to `a_i` because `C` is connected.

If `C'` has no neighbour in `{k_1,k_2}`, componenthood and the exact
neighbourhood of `C` give

\[
 N_G(C')\subseteq
 \{a_i\}\cup\{s_D,s_X,s_Y,s_{F_1},s_{F_2},s_{F_3}\}.
\]

The nonempty set `U_0` lies on the opposite side.  Seven-connectivity makes
this inclusion an exact order-seven separation.  The edge `a_js_j` crosses
it, as does the direct third-owner edge `p_3s_3`; one designated deletion
colouring therefore gives the generic response claimed by the theorem.

If `C'` has a neighbour in `{k_1,k_2}`, the replacement

\[
 U\longmapsto U_0\cup C',
 \qquad R_i\longmapsto R_i\cup L
\]

is connected on both sides.  The first edge of `P` at `a_i` supplies their
mutual adjacency.  The direct edges `a_js_j` and `p_3s_3` preserve the other
two owner contacts, while `U_0` preserves every nonowner contact and the
fixed response edge.  Again the model is spanning and loses no labelled
adjacency, and `L` is nonempty, so the donor strictly shrinks.

The argument covers every location of `p_3`: an endpoint of `P` or an
internal vertex.  Pairwise disjoint fan paths may have different attachment
vertices on `P`; the proof never assumes otherwise.

## 5. Relaxed first-hit rank

For either transfer, a ranked path with terminal label different from `U`
avoided all of the old ranked branch set `U`, and hence avoids every moved
vertex.  Such paths survive unchanged.  If the unique path with terminal
label `U` ended in material moved out of `U`, replace it from its same port
by a path inside the fixed connected response subgraph in `D`, followed by
the fixed edge into `U_0`.

The rank permits paths to overlap inside that fixed response subgraph and
requires disjointness only outside it.  The replacement first meets a ranked
branch set at its endpoint in `U_0`.  This is precisely the hypothesis and
construction of the audited rank-preserving transfer theorem, so the relaxed
rank does not decrease.  The prescribed roots and selected partition remain
fixed.

## 6. Atomic quotient stress test

The smallest labelled quotient which blocks an unconditional strict transfer
has ten vertices.  Its six outside singleton labels

\[
                    X,Y,F_1,F_2,F_3,D
\]

induce `K_6-XY`.  Put `U_0={k_1,k_2}` and `C={a_1,a_2}`, with edges

\[
\begin{aligned}
 &k_1k_2,quad k_1F_2,quad k_1F_3,quad k_1D,\\
 &a_1a_2,quad a_2k_1,quad a_2k_2,\\
 &a_1X,quad a_2Y,quad a_1F_1,quad
   a_2F_2,quad a_2F_3,quad a_2D.
\end{aligned}
\]

The seven labelled sets `U={k_1,k_2,a_1,a_2}` and the six outside
singletons form a spanning `K_7`-minus-`XY` model.  Contracting the path
`a_1a_2` exposes a five-fan to `k_1,k_2,X,Y,F_1`.  Nevertheless an exhaustive
check of all assignments of `a_1,a_2` to the seven fixed labels finds that
only the original assignment preserves the labelled near-complete model.
Thus the five-fan alone does not imply strict transfer.

The draft does not make that false claim.  Here the third owner `F_1` and
the selected owner `X` attach at `a_1`, while both internal-transversal
vertices and owner `Y` attach at `a_2`.  Case B chooses `a_i=a_2`; the
component `C'={a_1}` has no neighbour in `{k_1,k_2}`.  Its displayed
seven-vertex neighbourhood is the exact separator alternative in the
theorem.  The quotient itself has connectivity two and chromatic number
five, so it is not an `HC_7` host; it serves only as a sharp test that the
proof handles the two-pole geometry without an unsupported transfer.

## 7. Exact trust boundary

The theorem is a correct unbounded host-level continuation of the
concentrated three-owner order-eight configuration.  It proves a strict
label-preserving transfer or returns an actual order-seven separation
carrying one or both selected operation-specific edge responses.

It does **not** prove that either returned boundary partition extends through
the intact smaller shore, synchronize the two closed-shore colourings,
eliminate a generic singleton shore, reduce positive separator excess, or
eliminate a shore-filling positive-excess list-critical core.  It therefore
does not prove `HC_7` and must not be cited as a terminal colour-gluing
theorem.
