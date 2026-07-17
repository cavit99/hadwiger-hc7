# Audit: low-internal-degree exact-seven handoff

**Verdict:** GREEN.

**Source before promotion:** the former active copy is not separately
retained; its content is preserved in the promoted source below.

**Promoted source:**
`results/hc7_exact7_low_internal_degree_handoff.md`

**Audited SHA-256:**
`80e8b69359fe0641d30174474c4ae23cc09929e1437dff2a9f82c82ef97054c6`

**Promoted-source SHA-256:**
`b9901350182cb92ea58e6da8cb84882f1a993184e503e8d421ac1adb6b59be5a`

Promotion changed only the status line and path; the audited mathematics is
unchanged.  The second hash records the promoted file exactly.

The repaired setup explicitly assumes that `G[L]` is connected.  This is
the hypothesis missing from the preceding draft, and it repairs the sole
gap in Theorem 2.2: when `L-v` is nonempty, `v` now has a neighbour in
`L-v`, so the two carriers used in Lemma 2.1 are genuinely adjacent and
`v` contributes one vertex to the boundary of `L-v`.

## 1. Lemma 2.1

The seven displayed bags are disjoint:

- `X,Y` are disjoint subsets of the open shore `L`;
- `P,Q` are disjoint subsets of the opposite open shore `R`;
- `a,b,x,y,t` are five distinct boundary literals by the anchor choices;
- the literal separation makes the three vertex regions disjoint.

The first two bags are connected through their respective anchor edges,
and `P,Q` are connected by hypothesis.  Their six mutual adjacencies are
literal: `X-Y` and `P-Q` are assumed edges, while fullness of each packet
at `a` and `b` supplies all four cross-shore incidences.  Each of these
four bags is adjacent to each singleton `x,y,t`; for the first two this is
the definition of the common support, and for the packet bags it is
fullness.  The literal edge `xy` leaves only `xt,yt` potentially absent.
Those two pairs share the singleton bag `{t}`, exactly the allowed
deficiency of `K_7^vee`.

If both supports have order at least five, deleting `x,y,t` leaves an
anchor for `X`; deleting those three literals and that first anchor leaves
an anchor for `Y`.  The automatic-anchor sentence is therefore valid.

## 2. Theorem 2.2

Because `R` is nonempty and anticomplete to `v`, deleting `N_G(v)` leaves
`v` and vertices of `R` in different components.  Seven-connectivity gives

`d_G(v)=|N_S(v)|+d_L(v)>=7`.

Put `Y=L-{v}`.  The repaired assumption that `G[L]` is connected, together
with nonempty `Y`, gives a literal `v-Y` edge.  Since `Y` is connected and
has no neighbour in `R`, its complete external neighbourhood is

`N_G(Y)=N_S(Y) union {v}`.

This set separates `Y` from nonempty `R`; hence `|N_S(Y)|>=6`.  Inclusion--
exclusion in the literal seven-set then gives

`|N_S(v) cap N_S(Y)| >= |N_S(v)|-1`.

If that common support were independent, it would be an independent set
inside `G[N_G(v)]`.  Dirac's inequality and `d_L(v)<=3` would give the
contradictory bounds

`|N_S(v)|-1 <= alpha(G[N_G(v)]) <= |N_S(v)|-2`.

Thus the common support contains a literal edge `xy`; it has order at
least three, so `t` exists.  The support at `v` has order at least four, so
`a` exists.  The support of `Y` has order at least six, so after forbidding
`x,y,t,a`, at least two choices remain for `b`.  All hypotheses of Lemma
2.1 now hold, including the repaired literal adjacency between `{v}` and
`Y`.  The seven bags in (2.9) therefore form `K_7^vee`.

For Corollary 3.1 the intended frontier scope is a hypothetical minimal
counterexample, so Dirac's inequality holds at every selected low-degree
vertex, not merely at one predesignated vertex.  The thin packet is
connected, cutvertex-free and nonsingleton; hence `L-v` is nonempty and
connected for every `v`.  Applying Theorem 2.2 to any vertex of internal
degree at most three proves the claimed `delta(G[L])>=4` alternative.

## 3. Theorem 4.1

Let `D_i` be three components behind the two-cut `{u,v}`.  Each component
has a neighbour at both gate vertices: otherwise the other gate vertex
alone disconnects that component, contradicting cutvertex-freeness.
Consequently

`N_G(D_i)=N_S(D_i) union {u,v}`,

and seven-connectivity gives `|N_S(D_i)|>=5`.  Each defect set therefore
has order at most two.

The three defect sets have at most six incidences.  Hence one literal `x`
is in none of them.  Over the remaining six literals, their total
incidence remains at most six, so one literal `y` belongs to at most one
defect.  Every lobe contacts `x`, and at least two lobes contact `y`.

After deleting `x,y`, each lobe support is a subset of the same five-set
and has order at least three.  Hall's condition is valid: one such set has
union size at least three, any two have union size at least three, and all
three have union size at least three.  Thus the three distinct anchors in
(4.3) exist.

The bags in (4.4) are disjoint and connected.  Their lobe bags are
pairwise adjacent: `u` meets every lobe and supplies the first--second and
first--third adjacencies, while `v` supplies the second--third adjacency.
The distinct anchors join every lobe bag to each full packet, and `P-Q` is
an assumed edge, so the first five bags form a clique.  They all meet
`{x}`.  The two packet bags and at least two lobe bags meet `{y}`.  Hence
the only possible missing pairs are `xy` and one lobe--`y` pair; both are
incident with `{y}`.  This is precisely a labelled `K_7^vee` model.  It is
not claimed to be a `K_7` model.

## 4. Exact scope

The audited conclusions require:

- a literal order-seven separation with nonempty anticomplete open shores;
- connected `G[L]`;
- two disjoint adjacent connected `S`-full packets in `R`;
- seven-connectivity of `G`;
- for Theorem 2.2, connected nonempty `L-v`, `d_L(v)<=3`, and Dirac's
  inequality at that vertex;
- for Theorem 4.1, cutvertex-free `G[L]` and at least three components
  behind the chosen two-cut.

The note proves a near-model handoff only.  It neither proves a literal
`K_7` nor closes the remaining internal-minimum-degree-four, two-lobe
width-two residue without the separate `S1` machinery.
