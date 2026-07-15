# Independent audit: failed-web two-apex guardrail

**Verdict:** **GREEN at the frozen hashes below.**  The graph is exactly
seven-connected, is `K_7`-minor-free, contains the stated cell-free failed
four-web pairing, and has the displayed literal spanning `K_6` model after
the two named edge deletions.  Its coherent fixed pair is `{a,b}`.  The
example is not contraction-critical and is not a frozen twin-seam instance;
it only refutes a connectivity-plus-model localization shortcut.

**Audited note:**
`barriers/hc7_twin_seam_failed_web_two_apex_barrier.md`.

**Note SHA-256:**
`df3ce12a985ae0f31c935ea99778c7fa5dc9136440c118f9256c724cbab9bbf3`.

**Executable certificate:**
`barriers/hc7_twin_seam_failed_web_two_apex_barrier_verify.py`.

**Certificate SHA-256:**
`458e3a1c7e6092e39ba69a4d5141fffd324060702847a2cea6ac83451b919731`.

## 1. Connectivity and excluded minor

Let `I_ico` be the icosahedral graph and `G=K_2 join I_ico`, with universal
adjacent apices `a,b`.  Removing at most six vertices leaves an apex, unless
both apices are removed; in that event at most four icosahedral vertices
are removed, and five-connectivity of the icosahedron keeps the remainder
connected.  Conversely, deleting `a,b` together with the five icosahedral
neighbours of one vertex isolates that vertex.  Hence `kappa(G)=7`.

In any clique-minor model, at most two branch sets meet `{a,b}`.  If a
`K_7` model existed, the other five branch sets would lie wholly in
`I_ico`; every adjacency between two such branch sets would be a literal
icosahedral edge.  They would therefore form a `K_5` minor in a planar
graph, impossible.  Thus `G` is `K_7`-minor-free.  Deleting `{a,b}` leaves
the planar icosahedron, so this pair is exactly the advertised fixed-pair
terminal.

## 2. Failed pairing

Deleting `T` from the icosahedron exposes the five-cycle

\[
 U_0U_1U_2U_3U_4U_0
\]

as a facial boundary.  The roots `p=U_0,q=U_1,c_1=U_3,c_2=U_4` occur in
the order `p,q,c_1,c_2`.  Paths for the pairing
`{p,c_1}|{q,c_2}` would join alternating vertices of one face and therefore
cannot be disjoint.  The other pairing is literal: use
`U_1-U_2-U_3` together with the edge `U_0U_4`.

The executable certificate independently enumerates all connected
carriers for the first pair and checks reachability of the second pair in
the complement.  It returns `false,true` for these two pairings.  The
rooted-`C_4` failure asserted here is the failure inside this selected web
host, not a claim that no larger supergraph could reroute through an apex.

## 3. Common-host spanning model

After deleting `aT` and `bB`, the six displayed bags are disjoint and
partition all fourteen vertices.  The certificate checks connectivity of
each bag and all twenty-one pairwise bag adjacencies.  In particular, the
deleted edges are not used: `F_1-F_5` is witnessed through `L_3`, and
`F_5-F_6` retains both `ab` and `bL_3`.  Thus this is a literal spanning
`K_6` model in the exact common two-edge-deletion host.

## 4. Executable replay and falsification scope

Running

```text
python3 barriers/hc7_twin_seam_failed_web_two_apex_barrier_verify.py
```

returns

```text
GREEN failed_web_two_apex_guardrail
order=14 connectivity=7 K7_minor=false
rst_pairings=false,true spanning_K6_in_common_host=true
fixed_pair={a,b} planar_remainder=true
```

The `K_7` exclusion is certified mathematically by the planar fixed-pair
argument rather than by a heuristic minor search.  The script verifies the
remaining finite claims deterministically.

The guardrail does not falsify the active terminal-disjunctive theorem:
the graph exits through its permitted fixed pair.  It also lacks the frozen
packet vectors, boundary maps, named Kempe responses, and strong
contraction-criticality.  Its exact lesson is narrower: seven-connectivity,
a failed cell-free four-web, `K_7`-minor-freeness, and an arbitrary spanning
`K_6` in the common deletion host cannot alone force localization to the
missing RST pairing.  Any successful decoder must exploit the critical
state data or detect the coherent two-apex outcome.
