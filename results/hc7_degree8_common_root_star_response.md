# A degree-eight common-root fork has an aligned root-star response

**Status:** written proof; separately audited GREEN.  This theorem
does not prove `HC_7`.

## 1. Setup

Let `G` be a finite simple graph which is seven-connected and
seven-chromatic, has no `K_7` minor, and whose every proper minor is
six-colourable.  Let `u` have degree eight, put `X=N_G(u)`, and assume the
exact two-full-component singleton-rejection common-root residue of the
[synchronized flip-cube theorem](hc7_common_root_flip_cube_fork.md), with
exterior components `E,F`.  In particular both components are adjacent to
every vertex of `X`.  By the
[short-trace classification](hc7_common_root_short_trace_classification.md#theorem-4-the-degree-eight-fork-retains-the-literal-root),
choose a boundary colouring `theta` at one endpoint of the original
coordinate-zero rejection-cut edge so that the two changing coordinates
are `0,j`, where

\[
                         W_0=\{x\}.                    \tag{1.1}
\]

Orient the edge so that `theta` extends through `F`, while
`theta^{\{0\}}` extends through `E`.  Fix extensions `c_F,c_E` through
those two literal components.  Write

\[
                \theta(x)=\alpha,
        \qquad \theta^{\{0\}}(x)=\beta.                \tag{1.2}
\]

## 2. The exact root-star response square

Put

\[
\begin{aligned}
 L_F&=N_G(x)\cap F\cap c_F^{-1}(\beta),
   &D_F&=\{xv:v\in L_F\},\\
 L_E&=N_G(x)\cap E\cap c_E^{-1}(\alpha),
   &D_E&=\{xv:v\in L_E\}.
\end{aligned}                                         \tag{2.1}
\]

### Theorem 2.1 (three positive response signatures)

The sets `L_F,L_E` are nonempty, and `D_F union D_E` is an induced star
centred at `x`.  There are proper six-colourings with all three signatures

\[
 \begin{array}{c|cc|c}
   &D_F&D_E&\text{boundary trace on }X\\ \hline
 d_F&\text{monochromatic}&\text{proper}&\theta^{\{0\}}\\
 d_E&\text{proper}&\text{monochromatic}&\theta\\
 d_{FE}&\text{monochromatic}&\text{monochromatic}&\text{unspecified}
 \end{array}                                           \tag{2.2}
\]

on the corresponding common deletions.  The missing signature in which
both edge sets are proper is impossible.

#### Proof

If `L_F` were empty, recolouring only `x` from `alpha` to `beta` in `c_F`
would be proper: `W_0={x}` says that no boundary neighbour of `x` has
colour `alpha` or `beta`, and no vertex of `F` adjacent to `x` would have
colour `beta`.  This would extend `theta^{\{0\}}` through `F`, contrary to
the rejection change.  Thus `L_F` is nonempty; the proof for `L_E` is
symmetric.

Each leaf set is independent because all of its vertices have one colour
in a proper shore colouring.  The two leaf sets lie in distinct components
of `G-N[u]`, so they are anticomplete.  This proves the induced-star claim.

Recolour `x` from `alpha` to `beta` in `c_F`.  The only resulting conflicts
are the edges `D_F`; its boundary trace is now `theta^{\{0\}}`, so it glues
to `c_E`.  Give `u` the sixth colour absent from the five-coloured boundary.
The result is `d_F`, a proper colouring of `G-D_F`.  Its `D_F` edges are
monochromatic, while every `D_E` edge is present and proper.  Reversing the
roles of the shores gives `d_E`.

Contract the entire induced star `D_F union D_E`.  A six-colouring of this
proper minor expands to a proper colouring of
`G-(D_F union D_E)` in which every edge of both sets is monochromatic.  This
is `d_{FE}`.  Finally, a colouring in which both sets were proper would be
a proper six-colouring of the original graph `G`, which is impossible.
\(\square\)

## 3. Minimal aligned root-edge response

Choose an inclusion-minimal nonempty set `J_F subseteq D_F` for which
`G-J_F` has a proper six-colouring inducing `theta^{\{0\}}` on `X`.
Define `J_E subseteq D_E` symmetrically for trace `theta`.

### Theorem 3.1 (single aligned edge or a minimal multi-edge obstruction)

For each `Q in {E,F}`, exactly one of the following holds.

1. `J_Q=\{h\}` is one edge.  Its one-edge proper-minor response retains
   the prescribed opposite-shore boundary trace.  Applying the audited
   order-eight operation-coupled response theorem gives either:

   - the clean five-path fan in `Q` associated with the aligned response at
     `h`, preserving the five prescribed first edges at the shore endpoint
     of `h`; or
   - a nonempty connected proper subset `A subsetneq Q` with

     \[
                         |N_G(A)|=7.                  \tag{3.1}
     \]

     Choosing any boundary-to-`A` edge gives a generic exact-seven
     selected-response interface with shore order strictly smaller than
     `|Q|`.
2. `|J_Q|>=2`.  No proper subset of `J_Q` admits the prescribed aligned
   trace, and every edge of `J_Q` is monochromatic in every aligned
   colouring of `G-J_Q`.

#### Proof

The colourings `d_F,d_E` from Theorem 2.1 show that the defining families
of deletion sets are nonempty.  The empty set is excluded because `G` is
not six-colourable, so inclusion-minimal nonempty choices exist.

Let `e in J_Q` and let `d` be any aligned colouring of `G-J_Q`.  If `e`
were proper under `d`, restoring it would give an aligned colouring of
`G-(J_Q-\{e\})`, contrary to minimality.  Hence every deleted edge is
monochromatic in every aligned response.  This proves outcome 2 whenever
the set has at least two edges.

Suppose `J_Q=\{h\}`.  The components of `G-X` are exactly

\[
                         \{u\},E,F,                    \tag{3.2}
\]

and all three are adjacent to every vertex of `X`.  The edge `h` joins its
root `x in X` to a vertex of `Q`, and the aligned colouring is a proper
six-colouring of `G-h`.  The hypotheses of the
[clean-fan-or-generic-restart theorem](hc7_order8_clean_fan_or_generic_restart.md)
therefore hold with `C_0=Q`.  Its two conclusions are exactly outcome 1;
the returned set satisfies `A subsetneq Q`, so its literal shore order is
strictly smaller.  \(\square\)

## Exact trust boundary

The theorem couples the retained singleton trace `W_0={x}` to literal
edge-deletion responses.  It is stronger than the bilateral or atomic
trace geometry alone: a singleton minimal response either enters the
existing clean five-path machinery or produces an actual order-seven
interface, while a nonsingleton response is an exact minimal deletion
obstruction.

Neither outcome is terminal for the global bounded-interface theorem.  A
generic exact-seven interface enters the still-open degree-seven terminal
decoder; it is not automatically a component of the original `G-N[u]`.
The clean fan may first hit the third atomic trace rather than the intended
bilateral endpoint, and its five endpoints or inherited branch-set labels
need not be distinct.  In the multi-edge outcome no single edge retains the
prescribed trace.  Closing precisely those two label-preserving failures is
the next degree-eight task.

## Inputs

- [low-degree common-root short-trace classification](hc7_common_root_short_trace_classification.md)
- [boundary-full order-eight clean fan or generic restart](hc7_order8_clean_fan_or_generic_restart.md)
