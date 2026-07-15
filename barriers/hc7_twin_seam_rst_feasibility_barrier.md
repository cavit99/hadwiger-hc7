# Barrier: the separating bundle does not force both RST pairings

**Status:** exact executable mechanism barrier.  It is not an `HC_7`
counterexample.  The host is explicitly six-colourable and contains a
literal `K_7` model, so it is killed by two terminal branches of the active
theorem.

The verifier is
[`../active/hc7_twin_seam_rst_feasibility_falsifier.py`](../active/hc7_twin_seam_rst_feasibility_falsifier.py).

## 1. Claim falsified

In the residual twin seam put

\[
 J=I\mathbin{\dot\cup}B_0,
 \qquad C_i=R_i\cup\{a_i\}\quad(i=1,2),
\]

and contract `C_i` to a root `c_i` in

\[
 W=G[D\cup A_0\cup R_1\cup R_2\cup\{p,q\}].
\]

Robertson--Seymour--Thomas (2.1) would produce the reserve-rooted cyclic
four-fragment model if both

\[
 \{p,c_1\},\{q,c_2\}
 \quad\hbox{and}\quad
 \{q,c_1\},\{p,c_2\}
\tag{1.1}
\]

were feasible.  The following implication is false:

> the literal twin geometry, seven-connectivity, packet vector
> `(1,1)/(1,1)`, crossed named responses, common equal/equal state, and the
> full separating five-rung response bundle force both pairings in (1.1).

The missing input is not another response path.  It is the global
forbidden-proper/proper state, equivalently the non-six-colourability and
strong critical kernel, or the terminal `K_7`/fixed-pair alternative.

## 2. The failed-pair web

The `D`-side four-terminal graph starts with the icosahedron.  For the
edge `0--1`, whose two common neighbours are `5,8`, label

```text
p=0, q=8, a1=1, a2=5
```

and delete

```text
p-a1, q-a1, p-a2.
```

The surviving terminal edges are `p-q` and `a1-a2`.  This is a literal
subgraph of the icosahedral four-web with cyclic frame

\[
                         p,q,a_1,a_2.
\]

The two old packets are joined to `a_1,a_2` and then contracted.  Exact
connected-set enumeration in the quotient proves

\[
 \{p,c_1\},\{q,c_2\}\text{ is infeasible},
 \qquad
 \{q,c_1\},\{p,c_2\}\text{ is feasible}.             \tag{2.1}
\]

Thus (2.1) is the genuine planar-web order obstruction from the Two Paths
Theorem, not a low-order cut or a missing packet.

### Global linkages do not localize

Both prescribed global pairings exist even in the common edge-deleted host
`G-{e,f}`.  They have the following disjoint literal representatives:

```text
p-i2-a1       q-i1-a2
q-i2-a1       p-i1-a2.
```

Neither pair uses `e=zu` or `f=qw2`.  The first pair realizes globally the
pairing which fails in the reserve quotient.  Its two paths necessarily
leave `W`, here through `i1,i2 in I`.  Consequently Jung's global
two-linkedness cannot be localized merely by shortening its paths or by
choosing the other prescribed pairing.

## 3. Frozen local hypotheses retained

The 25-vertex host has all of the following literal properties, checked
by the verifier.

1. Its vertex-connectivity and minimum degree are both seven.
2. The old thin shore is biconnected, the old boundary is connected and
   bipartite, there is no old thin--rich edge, and `zu` is the unique
   old-thin edge at `u`.
3. The lobe neighbourhoods are exactly

   \[
   N(D)=\Omega_D=Z\cup I\cup A_0,
   \qquad N(E)=\Omega_E=Z\cup I\cup B_0.
   \]

4. The two selected old packets are disjoint, connected and `S`-full.
   Exhaustive connected-subset enumeration gives all four residual packet
   numbers equal to one.
5. A displayed six-colouring `phi` of `G-zu` has a `0--1` lock in which
   `f=qw2` is a bridge separating `z` from `u`.  Swapping the `z` side
   gives the displayed colouring `psi` of `G-f`.
6. The exact partitions induced by `phi,psi` are crossed on both
   `Omega_D` and `Omega_E`.
7. In `psi`, for each of the four colours outside `{0,1}`, there is a
   literal `q-w2` path in that two-colour layer.  A complementary
   `0--1` path

   ```text
   q-p-z-u-a2-a1-w2
   ```

   contains `zu`.  This is the full separating response bundle.
8. A displayed colouring of `G-{e,f}` makes both named edges equal, so
   the common double-contraction chamber is also present.

## 4. Exact missing hypothesis

The verifier finally displays a proper six-colouring of the whole host.
Consequently the forbidden `(proper,proper)` corner of the common host is
present, and the graph is not strongly seven-contraction-critical.

Independently, it verifies the following seven literal branch sets:

```text
{b,r2}
{i2,w10}
{e1,q,w3,w9,y4,z}
{a1,r1,w4,w6}
{i3,w2}
{u}
{a2,i1,p,w11,w7,y3}.
```

They are disjoint and connected, and every pair is joined by a literal
host edge.  Thus the shell also takes the permitted `K_7` terminal.  These
two terminal certificates are why the shell does not refute the active
terminal-disjunctive theorem.

The safe research conclusion is therefore precise:

> Do not spend more response paths trying to prove the two RST pairings.
> In the failed-pair branch, take the returned four-web as the certificate
> and use strong criticality to show that its legal state transitions
> create the forbidden proper/proper colouring, a literal terminal model,
> or the strict separator already supplied by the reserve-rooted `C_4`
> exchange.

The web obstruction is already compatible with every audited local bundle
and packet invariant.  Any proof which never invokes the forbidden
proper/proper corner cannot eliminate it.
