# Boundary-state saturation at a contracted edge

## 1. General lemma

Let (G) be (r)-minor-critical: (G) is not (r)-colourable, while
every proper minor is.  Let (D) be a nonempty side with labelled boundary
(L), so

\[
 N_G(D)\subseteq D\cup L.
\]

Fix an internal edge (xy\in E(G[D])), and let (c) be any proper
(r)-colouring of (G/xy).  Write (alpha) for the colour of the
contracted vertex.  For (u\in\{x,y\}), put

\[
 b_c(u)=|c(N_L(u))|,
\]

the number of distinct boundary colours seen by (u).

### Theorem 1.1 (contraction-state saturation)

For each (u\in\{x,y\}),

\[
 d_D(u)+b_c(u)\ge r.                              \tag{1.1}
\]

If equality holds, then the vertices of
(N_D(u)-\{x,y\}) have pairwise distinct colours, none of those colours
occurs on (N_L(u)), and together the two sets realize all
(r-1) colours different from (alpha).

### Proof

Uncontract (xy) and temporarily give both ends colour (alpha).  The
only monochromatic edge is (xy).  If some colour
(eta\ne\alpha) were absent from

\[
 N_G(u)-\{x,y\},
\]

then recolouring (u) with (eta) would give a proper (r)-colouring
of (G), a contradiction.  Thus all (r-1) other colours occur among
the at most (d_D(u)-1) internal neighbours different from the other end
and the boundary neighbours, which use (b_c(u)) colours.  Hence

\[
 r-1\le (d_D(u)-1)+b_c(u),
\]

which is (1.1).  In the equality case every term in this elementary
capacity bound must be used without repetition, giving the stated colour
rigidity.  \(□\)

This lemma is label-free and applies at every (t).  It converts the
qualitative fact that a safe contraction creates a new boundary state into
a quantitative restriction on that state at both ends of the contracted
edge.

## 2. Immediate Moser-web consequences

In the all-crossless reserved Moser shore, disk curvature supplies the
three local profiles recorded in
`hadwiger_moser_pentagram_curvature.md`.

* At an ordinary facial curvature vertex (x), (d_D(x)=3) and
  (N_L(x)=\{s,t,w,a\}), where (st\in E(G[U])).  Any state created by
  contracting an edge incident with (x) must use at least three distinct
  colours on this four-set.  In particular the case in which (a,w) both
  reuse the two colours of (s,t) lifts immediately and cannot be a new
  state.
* At a triple-lock facial vertex, again (d_D(x)=3).  Its five boundary
  neighbours must use at least three colours in every genuinely new
  contraction state.
* At an interior curvature vertex, (d_D(x)=5) and
  (N_L(x)=\{w,a\}).  When (a,w) have one common colour, equality holds
  in (1.1): the other four shore neighbours use the remaining four colours
  bijectively and avoid the (a,w) colour.  This is an exact Kempe-exchange
  configuration, not an arbitrary high-state residue.

These conclusions do not by themselves close the three profiles.  They
remove every transition with insufficient local palette pressure and turn
the equality cases into explicitly rainbow neighbour configurations to
which the edge-deletion/Kempe detour machinery can be applied.

## 3. Scope

The theorem concerns the particular boundary state produced by a colouring
of (G/xy); it does not say that every abstract state satisfying (1.1)
extends across the contracted shore.  It is compatible with the thirty
high-root/nonstar Moser traces in `moser_safe_transition_state_probe.py`.
The remaining conversion must combine the saturation at both edge ends
with a crossed opposite shore or with a tight exact adhesion.
