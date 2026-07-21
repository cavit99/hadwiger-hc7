# Seven-fan closure of the exact two-path atomic core

**Status:** written proof; separate internal audit GREEN.

This note closes an exact thirteen-vertex residue of the atomic
`H_0`-subdivision programme in every seven-connected ambient graph.  It
also states precisely why the same fan count does not yet close an arbitrary
subdivision: internal vertices of the owned paths become additional possible
fan endpoints.

The theorem is an unbounded host result.  The ambient graph may have
arbitrarily many vertices and edges; only the retained thirteen-vertex
subgraph is exact.

## 1. The retained graph

Start with

\[
 H_0=(K_7-\{ab,cd\})+\{xa,xb,xc,xd\}
\]

on branch vertices `a,b,c,d,e,f,g,x`.  Form `C` as follows.

1. Replace `fa`, `ga`, and `fg` by `f-p-a`, `g-q-a`, and `f-h-g`.
2. Replace `ac` by `a-r-s-c`, in that order.
3. Add the literal edges `eh,hx,pr,sq`.

Thus

\[
 V(C)=\{a,b,c,d,e,f,g,x,h,p,q,r,s\}.                 \tag{1.1}
\]

The two last edges `pr,sq` are the suppressed versions of the two
internally `T`-clean paths in the surviving one-sided bridge pattern.

The adjacent deterministic checker
[`hc7_atomic_two_bridge_exact_core_seven_fan_closure_verify.py`](hc7_atomic_two_bridge_exact_core_seven_fan_closure_verify.py)
constructs this graph, checks the five minor models used below, and checks
the final model together with one named edge for each of its 21
adjacencies.  Run it from the repository root with

```text
.venv/bin/python -B active/hc7_atomic_two_bridge_exact_core_seven_fan_closure_verify.py
```

## 2. Five terminal fan endpoints at `q`

Put

\[
 U=\{b,d,f,h,p\},\qquad A=\{a,c,e,g,r,s,x\}.          \tag{2.1}
\]

These sets partition `V(C)-{q}`, and `|A|=7`.

### Lemma 2.1

For every `u in U`, the graph `C+qu` contains a `K_7` minor.

#### Proof

The following row gives seven branch sets for each added edge.  A string
inside braces denotes the set of its named vertices.

| added edge | seven branch sets |
|---|---|
| `qb` | `{a,p,q,r}`, `{b}`, `{c,f,s}`, `{d}`, `{e}`, `{g}`, `{x,h}` |
| `qd` | `{a,x,p,r}`, `{b}`, `{c,s}`, `{d,q}`, `{e}`, `{f}`, `{g,h}` |
| `qf` | `{a,d,p,r}`, `{b}`, `{c,s}`, `{e}`, `{f,q}`, `{g}`, `{x,h}` |
| `qh` | `{a,p,r}`, `{b,x}`, `{c,s}`, `{d,g}`, `{e}`, `{f}`, `{h,q}` |
| `qp` | `{a,d,r}`, `{b}`, `{c,s}`, `{e}`, `{f,p}`, `{g,q}`, `{x,h}` |

Every row is a spanning partition of (1.1).  Connectivity follows from the
displayed path edges and the added edge where it occurs.  Pairwise adjacency
is a direct check in `C+qu`; the checker tests all 21 pairs in every row.
Hence every row is an explicit
`K_7`-minor model.  \(\square\)

The lemma is purely positive: the proof below does not require a claim that
the other seven endpoints are nonterminal.  Exact exploratory enumeration
does in fact give `U` as the five terminal nonedges at `q`, but that negative
classification is not used here.

## 3. The unbounded exact-core theorem

### Theorem 3.1

Every seven-connected graph containing `C` as a subgraph contains a `K_7`
minor.

#### Proof

Let `G` be seven-connected and contain `C`.  Suppose, for a contradiction,
that `G` has no `K_7` minor.  Apply the seven-fan lemma from `q` to

\[
                  S=V(C)-\{q\}=A\mathbin{\dot\cup}U.  \tag{3.1}
\]

It gives seven paths from `q` to seven distinct vertices of `S`, pairwise
intersecting only at `q`, with all path interiors outside `S`.  Because `q`
is an endpoint of every simple fan path, those interiors avoid all of
`V(C)`.

If one fan endpoint were `u in U`, contract its fan path to an added `qu`
edge while retaining every vertex and edge of `C`.  Lemma 2.1 would then
give a `K_7` minor in `G`.  Therefore all seven endpoints lie in the
seven-element set `A`, and hence the endpoint set is exactly `A`.

Let `P_x` and `P_e` be the fan paths ending at `x` and `e`, respectively.
Let `y` be the predecessor of `e` on `P_e`.  Define

\[
\begin{aligned}
 X&=V(P_x)\cup V(P_e[q,y]),\\
 A_0&=\{a,p,r,s,c\},\\
 B&=\{b\},\quad D=\{d\},\quad E=\{e\},\\
 F&=\{f,h\},\quad G_0=\{g\}.
\end{aligned}                                           \tag{3.2}
\]

The seven sets are pairwise disjoint.  Indeed, the two fan paths intersect
only at `q`, their interiors avoid `C`, `P_x` ends at `x`, and the endpoint
`e` was omitted from `X`.  They are connected: `A_0` contains the path
`a-p-r-s-c`, `F` contains the edge `fh`, and the other assertions are
immediate.

Here is one literal contact for each of the 21 pairs:

| first bag | contacts with later bags |
|---|---|
| `X` | `XA_0:qs`, `XB:xb`, `XD:xd`, `XE:ye`, `XF:xh`, `XG_0:qg` |
| `A_0` | `A_0B:cb`, `A_0D:ad`, `A_0E:ae`, `A_0F:pf`, `A_0G_0:cg` |
| `B` | `BD:bd`, `BE:be`, `BF:bf`, `BG_0:bg` |
| `D` | `DE:de`, `DF:df`, `DG_0:dg` |
| `E` | `EF:ef`, `EG_0:eg` |
| `F` | `FG_0:hg` |

Notice in particular that `A_0G_0` uses `cg`, not the provenance route
`ga`: the marked vertex `q` on `ga` belongs to `X`.  Thus no ownership is
silently reused.  The seven sets in (3.2) form a `K_7`-minor model in `G`,
the desired contradiction.  \(\square\)

## 4. What survives for an arbitrary subdivision

Let `K` be an arbitrary subdivision of `C`, retaining all thirteen labels,
in a seven-connected graph `G`.  The five positive certificates in Lemma
2.1 lift through subdivision: a `K`-clean path from `q` to a named vertex
of `U` makes a subdivision of `C+qu`, and therefore gives a `K_7` minor.
Likewise, two internally disjoint `K`-clean paths from `q` to the literal
vertices `e,x` lift the model (3.2), with the unused route intervals assigned
along their incident branch sets.

There is nevertheless no valid subdivision-level counting inference from
Theorem 3.1.  Applying the fan lemma to
`V(K)-{q}` allows its seven endpoints to be internal vertices of the
subdivided core routes or of the two added paths.  Applying it only to the
seven named vertices in `A` makes the path interiors avoid `A`, but not the
owned route interiors.  Contracting such a dirty path to a new edge can
therefore destroy literal route ownership.  Neither operation supplies the
two `K`-clean paths used in (3.2).

The exact first-hit residue can be stated without ambiguity.  Delete
`V(K)-{q}` and let `D_q` be the component containing `q`; put

\[
                         \Omega_q=N_G(D_q).             \tag{4.1}
\]

Then

\[
                 \Omega_q\subseteq V(K)-\{q\},\qquad
                 |\Omega_q|\ge 7.
\]

Equality is an actual order-seven separation with boundary `Omega_q`.  In a
`K_7`-minor-free host,

\[
                  \Omega_q\cap\{b,d,f,h,p\}=\varnothing, \tag{4.2}
\]

because every attachment supplies a `K`-clean path from `q` and Lemma 2.1
lifts.  This exclusion extends along every subdivided edge incident with one
of those five vertices.  Indeed, if an attachment `z` lies internally on the
subdivided `uv` route with `u in U`, contract the `z`--`u` part of that route.
The retained subdivision and a clean `q`--`z` path then have `C+qu` as a
minor, so Lemma 2.1 applies.

Consequently every nonterminal first hit lies in the subdivision of the
eight-vertex graph on

\[
                    \{q,a,c,e,g,r,s,x\}
\]

with edge set

\[
 \{qa,qg,qs,ar,rs,sc,ae,ax,ce,cg,cx,eg\}.            \tag{4.3}
\]

This is the exact route confinement supplied by the five positive
certificates; no converse nonterminal claim is made for every point of that
skeleton.  Moreover, every seven-fan from `q` to `V(K)-{q}` has endpoint set
in `Omega_q` and cannot contain both literal endpoints `e,x`, by the lifted
model (3.2).

Consequently the remaining subdivision-level obligation is precise:

> either extract one seven-fan whose first-hit endpoint set contains both
> `e` and `x`, or show that the obstruction to doing so yields a bounded
> separator or response interface.

Extra internal route vertices are the only reason the exact seven-endpoint
count no longer performs this extraction.  Theorem 3.1 closes the suppressed
core but does not claim that this final first-hit obligation has already been
proved.
