# Atomic twin-seam gate chromatic fork

**Status:** proved and independently audited.  This theorem removes the
common palette gate as the only response-local certificate when the gate
edge is double-critical, and regenerates a second spanning `K_6` frame in
the complementary branch.  It does not complete the twin-seam decoder,
define a global rank, or supply a well-founded transition by itself.

## 1. Setup

Use the frozen twin seam and notation of the
[crossed-state theorem](hc7_atomic_twin_seam_crossed_states.md).  Thus

\[
 e=zu,\qquad f=dt,
\]

where `z in E`, `u in B_0`, `d in D`, and `t in Z`.  Put

\[
 I=T_D\cap T_E,\qquad K=Z\mathbin{\dot\cup}I,
\]

so `|K|=5`, and recall

\[
 N_G(D)=\Omega_D=Z\mathbin{\dot\cup}T_D,
 \qquad N_S(t)\subseteq I.                              \tag{1.1}
\]

Let `phi` be the fixed six-colouring of `G/e`, lifted to `G-e`.  Assume
that `f` is a separating edge of one `phi`-lock, so the audited separating
response bundle supplies a literal cycle `C` through `e,f` and its
bridge-swapped response `psi`.

The edge `e` is already known to be non-double-critical:

\[
                         \chi(G-\{z,u\})=6.             \tag{1.2}
\]

The theorem below determines the additional structure supplied by `f`.

## 2. The chromatic fork

### Theorem 2.1 (gate chromatic fork)

Exactly one of the following alternatives holds.

1. **Double-critical gate response.**
   \(\chi(G-\{d,t\})=5\).  There is a six-colouring `rho` of `G/f`,
   lifted to `G-f`, with the following simultaneous properties.

   * A colour `gamma` occurs precisely on the two literal vertices `d,t`.
     In particular, the exact restrictions of `rho` to both twin
     boundaries have the common singleton block `{t}`.
   * The exact partitions induced by `rho` mismatch the fixed `phi`
     partition on both `Omega_D` and `Omega_E`.  Their two response-side
     inequalities, together with the two fixed `phi`-side inequalities,
     are exactly the four strict packet-demand inequalities of the
     crossed-state theorem.
   * For each of the other five colours `i`, there is a distinct literal
     common neighbour `v_i` of `d,t` of colour `i`.  Every `v_i` lies in

     \[
                           D\cup(K-\{t\}),              \tag{2.1}
     \]

     and at least one `v_i` lies in `D`.
   * Consequently the full union of the five `gamma-i` layers of `rho`
     contains five internally vertex-disjoint literal `d-t` paths, namely

     \[
                            d-v_i-t.                    \tag{2.2}
     \]

     It has no internal common `gamma` palette gate.  More generally, for
     every nonempty ordered sequence of distinct old colours, there is a
     literal `d-t` path whose internal colours occur in exactly that order.

2. **Second model frame.**
   \(\chi(G-\{d,t\})=6\).  The graph `G-{d,t}` has a spanning `K_6`
   model

   \[
                         \mathcal N=(N_1,\ldots,N_6).   \tag{2.3}
   \]

   The cycle `C-f` has two vertex-disjoint end segments, one from `d` and
   one from `t`, whose first hits on `mathcal N` are distinct literal
   vertices.  If those first hits lie in one row, the rooted row-duty
   split theorem gives either a literal `K_7` or an actual separator of
   order at least seven.  Independently, (1.2) supplies the first spanning
   `K_6` frame in `G-{z,u}`.  Thus this alternative supplies two literal
   spanning frames and a first-hit split-or-separator test for each.
   Further contact maximization is required before a surviving pair may be
   called a two-frame row-duty lock.

### Proof

Vertex-criticality gives

\[
                       5\le \chi(G-\{d,t\})\le6.       \tag{2.4}
\]

Indeed, the upper bound follows by deleting vertices from the
seven-critical graph.  A four-colouring of `G-{d,t}` could be extended by
giving the adjacent vertices `d,t` two fresh colours, producing a
six-colouring of `G`.  This proves the lower bound and makes the two
alternatives exhaustive and exclusive.

Assume first that equality five holds.  Choose a five-colouring `kappa` of
`G-{d,t}` and give both `d,t` one new colour `gamma`.  This is a proper
six-colouring `rho` of `G-f`, hence, after identifying its equal-coloured
ends, of `G/f`.  The new colour appears nowhere else.  Since `t` belongs
to both twin boundaries and `d` belongs to neither, `{t}` is an exact
singleton block of both boundary restrictions.

The crossed-state theorem applies to **every** six-colouring of `G/f`.
Applying it to `rho` proves both simultaneous mismatches and all four
strict packet-demand inequalities when the two already fixed `phi`-side
inequalities are included.

Fix an old colour `i`.  If no colour-`i` vertex were adjacent to both
`d,t`, recolour all colour-`i` neighbours of `d` with `gamma`, give `d`
colour `i`, and leave `t` colour `gamma`.  The recoloured neighbours are
independent, and none is adjacent to `t` by assumption.  This would be a
six-colouring of `G`, a contradiction.  Hence a common neighbour `v_i`
exists.  Different colours give different vertices.

Every common neighbour of `d,t` lies in `D union Omega_D`, by (1.1).  If
it lies in the old boundary `T_D`, its adjacency to `t in Z` and (1.1)
put it in `I`; if it lies in `Z`, it is the other gate.  Therefore (2.1)
holds.  The set `K-{t}` has four vertices, while there are five distinct
`v_i`, so at least one belongs to `D`.

Because `gamma` occurs only at `d,t`, every `d-t` path in a `gamma-i`
layer has length two and uses a common colour-`i` neighbour.  The five selected
vertices give (2.2), and no internal vertex of colour `gamma` exists which
could be a common palette gate.  The generalized ordered-path statement
is the edge-local generalized Kempe-chain argument of
Kawarabayashi--Pedersen--Toft, Proposition 3.3: apply to `kappa` the colour
cycle

\[
                  (\gamma,i_1,\ldots,i_s).
\]

If the generalized component from `d` omitted `t`, rotating its colours
would make `d,t` different in a six-colouring of `G-f`, which would extend
to `G`.  A shortest occurrence of `t` in the component gives the stated
path.  This argument is edge-local; it needs only that `dt` is
double-critical, not that every edge of `G` is.

Now assume equality six in (2.4).  Hadwiger's conjecture for parameter six
gives a `K_6` minor in `G-{d,t}`.  This graph is connected (indeed,
five-connected), since `G` is seven-connected.  Enlarge the model to a
spanning one by repeatedly absorbing each unused component into an
adjacent model bag, giving (2.3).

The path `C-f` is a simple `d-t` path containing `e`, so it has at least
two internal vertices.  Starting at its two ends, stop immediately before
the first already encountered model vertex.  Since the model spans
`G-{d,t}`, these first hits exist; simplicity of the path makes them
distinct, and the two stopped end segments are vertex-disjoint.

If the hits lie in a common row, they are distinct neighbours in that row
of the two adjacent poles `d,t`.  The rooted row-duty split-or-separator
lemma applies verbatim with `(d,t)` in place of `(z,u)`: a split retaining
all five foreign-row duties gives seven literal branch sets, and failure
of a duty on one connected side makes its literal neighbourhood an actual
separator of order at least seven.  Finally (1.2), known `HC_6`, and
connectedness of `G-{z,u}` give the first spanning frame.  This proves
every assertion in alternative 2.  \(\square\)

### Corollary 2.2 (literal second gate contact)

In alternative 1, the gate `t` has two distinct neighbours `d,v` in the
same lobe `D`, with `dv in E(G)`.  Equivalently, `f=dt` lies in a literal
triangle `dvt` whose third vertex is internal to `D`.

### Proof

Choose one of the five vertices `v_i` which lies in `D`.  It is adjacent
to both `d,t` by construction and differs from `d,t`.  \(\square\)

### Lemma 2.3 (boundary-preserving edge--triangle chamber)

Retain alternative 1 and the literal triangle

\[
                             T=G[\{d,v,t\}]
\]

from Corollary 2.2.  Contract `e` and a spanning tree of `T`, retaining
the literal labels `u` and `t` at the two contracted images.  Let `c` be
any six-colouring of this proper minor and lift it to the original
vertices, with

\[
                       c(z)=c(u),\qquad c(d)=c(v)=c(t).
\]

For `x in {d,v}`, let `F_x` be the set of colours different from `c(t)`
which are absent from

\[
                         N_G(x)-\{d,v,t\}.              \tag{2.5}
\]

Then at least one of the following holds.

1. `z` sees all five colours different from `c(z)` in `N_G(z)-{u}`.
2. The two-set availability system `(F_d,F_v)` has matching number at
   most one.  Equivalently, one of `F_d,F_v` is empty, or

   \[
                              F_d=F_v=\{\eta\}          \tag{2.6}
   \]

   for one colour `eta`.

The lifted boundary state on both twins is unchanged throughout this
fork: a successful repair recolours only `z,d,v`; the literal boundary
vertex `t` retains its old colour.

### Proof

Suppose `z` has an available alternate colour and `(F_d,F_v)` has a
matching of order two.  Recolour `z` with its available colour and
recolour `d,v` with their two distinct matched colours, leaving `t` with
the old colour `c(t)`.  All three edges of `T` are now proper.

No vertex of `D` is adjacent to `z`, and `u` has no neighbour in
`D union {t}`: the former follows because `D,E` are distinct components
of `A-Z`, while the latter follows from `u in B_0` and
`N_S(t) subseteq I`.  The only possible edge between the two repaired
objects is therefore `zt`.  If that edge exists, the retained colour at
`t` was already different from `c(z)` in the contracted colouring, and
it is unavailable at `z`; hence the recolouring is still proper.
Every other incident edge is safe by the definitions of the free sets.
Restoring `e` and the triangle edges gives a six-colouring of `G`, a
contradiction.  Thus outcome 1 or the matching obstruction in outcome 2
must hold.

For the stated equivalent form, view the two free sets as the
neighbourhoods of two left vertices in a bipartite availability graph.
If both are nonempty and their union contains two colours, choosing one
colour from one set and a different colour from the other gives a matching
of order two.  Hence failure of such a matching says that one set is
empty, or both are the same singleton.  This proves the equivalence and
the lemma.  \(\square\)

### Corollary 2.4 (literal response-matched gate pair)

In the chamber of Lemma 2.3, suppose `z` is not saturated.  Then either

1. one of `d,v` is saturated outside the other two triangle vertices; or
2. (2.6) holds, and the two gate edges

   \[
                         f=dt,\qquad g=vt              \tag{2.7}
   \]

   have six-colour responses which agree **literally** on every vertex of
   both twin boundaries.

In outcome 2 these responses are obtained from the same colouring `c`:
recolour `z` with one available colour, then recolour `v` with `eta` to
obtain a colouring of `G-f`, or recolour `d` with `eta` to obtain a
colouring of `G-g`.  The first response has only `dt` improper before its
deletion, and the second has only `vt` improper.  In both responses the
boundary vertex `t` keeps its `c`-colour.

### Proof

Since `z` is not saturated, Lemma 2.3 gives its second outcome.  If one
free set is empty, its corresponding endpoint is saturated outside the
triangle.  Otherwise (2.6) holds.

In the latter case perform the two recolourings described above.  The
definition of `F_d,F_v` protects every edge leaving the triangle.  Inside
the triangle, recolouring `v` leaves exactly the equal-coloured pair
`d,t`, while recolouring `d` leaves exactly the equal-coloured pair
`v,t`.  Recolouring `z` restores `e`, and the cross-edge check in the
proof of Lemma 2.3 remains valid.  Hence the two colourings are proper on
`G-f` and `G-g`, respectively.  Only `z,d,v` were recoloured; none lies on
either twin boundary.  Their boundary colourings therefore both equal
the restriction of `c` literally.  \(\square\)

## 3. Exact progress and remaining gap

The theorem removes one previously live mechanism rather than merely
renaming it.  If `f` is double-critical, a common internal palette gate is
impossible in the canonical response: the lock-layer rank is at least
five, all five routes are literal and localized to the `D`-closed side,
and both twin states contain the named singleton `{t}`.  The bridge response
`psi` may still have its own common palette gate, but it now coexists with
this second exact singleton response.

If `f` is not double-critical, both named edges regenerate spanning
`K_6` frames, and the same literal cycle supplies the first-hit pair for
each frame.  The remaining theorem is therefore one of the following two
label-faithful promotions:

1. use the singleton-`t` response and the five localized two-edge routes
   to attain a common twin state or a fifth duty-carrying bag; or
2. show that the two model frames cannot both remain row-duty locked unless
   their actual separators identify one common fixed pair or a genuinely
   ranked exact-seven receiver.

Neither promotion is asserted here.  In particular, five palette colours
are still not five model-row or boundary-duty labels, and an actual
separator of order at least seven is not automatically a ranked handoff.

Primary source for the edge-local generalized Kempe-chain formulation:
K. Kawarabayashi, A. S. Pedersen and B. Toft,
[*Double-critical graphs and complete minors*](https://doi.org/10.37236/359),
Proposition 3.3 and Corollary 3.1.
