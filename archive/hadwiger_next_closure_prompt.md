# Hadwiger closure programme — next-run prompt

## Mission

Prove Hadwiger’s Conjecture in full:

For every integer \(t\ge1\), every finite simple graph with no \(K_t\)
minor is \((t-1)\)-colourable.

Disconnected graphs are allowed.  A proof of \(\mathrm{HC}_7\), a proof
for another finite set of values, a reduction to an equivalent conjecture,
or a new list of residual cases is not the terminal objective.  Treat
\(\mathrm{HC}_7\) as the first compulsory milestone and then extract the
uniform mechanism needed for every \(t\).

Assume for this task that a complete affirmative proof exists.  This is a
research instruction, not permission to assume an unproved lemma.

Use up to 64 agents dynamically.  Spend at least one hour before
considering termination.  Do not stop merely because a local success
criterion has been met.

## Authoritative workspace state

Read these files first, in this precedence order:

1. hadwiger_execute_round_results.md
2. hadwiger_strongest_valid_derivation.md
3. hadwiger_corrected_package_audit.md
4. hadwiger_exact_boundary_state_transfer.md
5. hadwiger_moser_supported_pair_transfer_closure.md
6. hadwiger_degree7_supported_transfer_orientation.md
7. hadwiger_degree8_three_component_closure.md
8. hadwiger_degree9_four_component_closure.md
9. hadwiger_moser_tricyclic_exteriors.md
10. hadwiger_expert_round_synthesis.md and its audit

When an older note conflicts with a later audit, the later audit controls.
In particular, do not reuse the old claimed contact-load \(s=1,s=2\), or
\(R_5\) closures.

## Audited starting package

### General least-counterexample reduction

If the conjecture fails, let \(t\ge7\) be the least failing parameter and
let \(G\) be a proper-minor-minimal \(K_t\)-minor-free graph with
\(\chi(G)=t\).  For a minimum-degree vertex \(v\), put

\[
H=G-v,\qquad N=N_G(v).
\]

The audited conclusions include

\[
\eta(G)=t-1,\quad \delta(G)\ge t,\quad \kappa(G)\ge7,
\]

\[
\chi(H)=\eta(H)=t-1,\quad \kappa(H)\ge6.
\]

Every proper \((t-1)\)-colouring of \(H\) uses every colour on \(N\), and
no proper subset of \(N\) is colour-saturating.  Contracting
\(\{v\}\cup S\) for any independent set \(S\subseteq N\) gives a
proper-minor colouring in which exactly the vertices of \(S\) receive the
contracted colour among \(N\).  Edge-deletion witnesses force the deleted
edge’s ends to have one colour and to see every other colour.

There is an unrooted \(K_{t-1}\)-model in \(H\), but no such model whose
every bag meets \(N\), since \(\{v\}\) would complete a \(K_t\)-model.

The exact uniform obstruction is therefore:

> Prove that the counterexample-derived saturation, one-step minor
> transition witnesses, connectivity, and an unrooted
> \(K_{t-1}\)-model force an \(N\)-meeting \(K_{t-1}\)-model.

Call this obstruction \((U)\).  Merely restating \((U)\) is not progress.

### General tools proved in the workspace

1. Uniform shore packing: \(m\) pairwise anticomplete connected shores,
   each missing at most \(q\) boundary vertices, have an
   \(N\)-meeting \(K_m\)-model when \(|N|\ge m+q^2\).  For \(q=2\), the
   sharper threshold is \(|N|\ge m+2\).
2. Exact boundary-state transfer: if one of two anticomplete exterior
   sides realizes an independent partition \(\Pi\) of \(N\) by disjoint,
   connected, pairwise adjacent contraction sets, then \(\Pi\) occurs
   exactly as a boundary colour state on the opposite side.  Bilateral
   realizations with at most \(t-2\) blocks colour \(G\).
3. The valid contact-model potential produces one contact-extremal
   \(K_{t-1}\)-model and one all-rigid maximum fan.  It does not quantify
   over every model or every fan.

### Current \(\mathrm{HC}_7\) state

An extremal bound gives a minimum-degree vertex of degree \(7,8,\) or \(9\).

* If \(d(v)=7\), then \(G-N[v]\) has exactly one component.  Every
  two-exterior case is closed: a dependency-free check of all \(2^{21}\)
  labelled seven-vertex neighbourhoods leaves only the Moser spindle and
  \(M+13\), and both are eliminated.
* In every exact degree-seven trace, one nonedge is the repeated pair and
  the five remaining roots receive distinct colours.  Kriesell–Mohr gives
  a rooted \(K_5\)-model on those five roots.  The remaining obstruction is
  to reserve a disjoint connector for the repeated pair.
* In the pure-Moser sole-exterior cell, every tree, unicyclic, bicyclic,
  and safely six-shore-contractible tricyclic exterior is eliminated.
  A survivor either has cyclomatic number at least four or contracts to
  one of two seven-vertex triangle cacti: the three-triangle friendship
  graph or the chain of three triangle blocks.
* In the exceptional \(K_3\mathbin{\dot\cup}K_4\) neighbourhood, the sole
  exterior has order at least eight.  The target is two disjoint connected
  helpers rooted in the \(K_3\)-side and complete to the four
  \(K_4\)-roots.
* If \(d(v)=8\), then \(G-N[v]\) has at most two components.
* If \(d(v)=9\), then \(G-N[v]\) has at most three components.

The degree-seven sparse refinements do not exhaust all one-component
degree-seven neighbourhoods.

### Near-clique input

Every non-six-colourable graph contains a \(K_7^\vee\)-minor.  The useful
unproved conclusion is a label-preserving one-bag peel or a separator of
order at most six.  Seven-connectivity and many attachments alone are
insufficient; \(K_2\) joined with an icosahedral graph is an explicit
counterarchitecture.  Contraction-critical colouring data must enter.

## Retractions and forbidden shortcuts

Do not use any of the following:

* ordinary \(t\)-critical graphs are \((t-1)\)-connected;
* \(\chi(G/e)\le\chi(G)\);
* \(K_t\)-minor-free implies \((t-2)\)-degenerate;
* list-Hadwiger;
* the old \(s=1,s=2,R_5\) RPC eliminations;
* a “spanning model” together with an “outside component”;
* four edges of the Moser missing \(C_5\) suffice for a rooted \(K_5\)
  (they give only \(K_5-e\));
* support data may be chosen as arbitrary binary labels;
* pairwise Kempe connectivity gives the required disjoint linkage;
* connectivity alone gives a removable rooted path or a port-labelled
  branch-bag split;
* abstract boundary colouring-extension sets alone are rigid enough;
* colourings of two pieces separated by an internal cut may be glued while
  ignoring the portal vertices and cross-edges.

Whenever a proposed lemma would also hold in the known counterarchitectures
without using minor-critical transitions, actively suspect it is false.

## Research objective and priority order

Run two coupled programmes.  Neither may be abandoned.

### Programme A — close \(\mathrm{HC}_7\)

#### A1. Reserved-connector theorem at degree seven

The primary target is:

> In a proper-minor-minimal \(\mathrm{HC}_7\) counterexample with
> \(d(v)=7\) and sole exterior \(C\), for some accessible repeated pair
> \(a,b\), there is an \(a\)-\(b\) path \(P\) and a rooted \(K_5\)-model
> on the five unique roots whose bags avoid \(P\).

This immediately yields the sixth bag \(P\), then a \(K_7\)-model with
\(\{v\}\).

Do not attack this as an arbitrary theorem about six-connected graphs.
Use all exact traces, edge-deletion witnesses, and one-step internal
deletion/contraction transitions.

Choose a rooted certificate minimizing its use of \(C\), decompose its
bridges, and prove one of:

1. a bridge switch or path rerouting reduces the certificate;
2. an \(a\)-\(b\) connector survives outside it;
3. failure produces an explicit adhesion of order at most six carrying a
   common exact colour partition; or
4. the bridge portals themselves form an \(N\)-meeting \(K_6\)-model.

For outcome 3, keep every portal in the common boundary and prove that the
two minor colourings align.  Anticompleteness may not be silently assumed.

Dispatch the two remaining tricyclic cactus quotients as a small parallel
task, but do not mistake that finite closure for the general
reserved-connector theorem.

#### A2. Exceptional \(K_3\dot\cup K_4\) sole exterior

Prove that the order-at-least-eight exterior contains two disjoint
connected \(A\)-rooted, \(B\)-complete helpers, or output a portalized
colour-gluable separation.  Use the full family of contraction witnesses,
not only degree lower bounds or static neighbourhood rows.

#### A3. Degree eight and degree nine

Close all remaining component counts:

\[
d(v)=8:\ 1\text{ or }2\text{ exterior components},
\]

\[
d(v)=9:\ 1,2,\text{ or }3\text{ exterior components}.
\]

Exploit the independent-set trace lemma, Dirac’s bounds
\(\alpha(N)\le3,4\), and the existing finite anchor-colouring machinery.
The desired finite-boundary output is always a dichotomy:

* an explicit \(N\)-meeting \(K_6\)-model; or
* one common independent boundary partition forced on every retained
  side by proper-minor contractions.

If a component is split, portals belong to the adhesion and must be
coloured consistently.  The existing degree-eight coarse cutvertex and
portal probes have explicit survivors, so do not retry that static
encoding.  Add one-step minor-transition data or genuine internal
linkage.  Also investigate combining several low-degree vertices rather
than treating each neighbourhood independently.

### Programme B — prove the uniform all-\(t\) mechanism

#### B1. Portalized exact-state transfer

Generalize the proved two-antichain-side theorem to a genuine separation
\((A,B)\) with adhesion \(X=A\cap B\).  State exact sufficient conditions
under which connected realizations of one independent partition of
\(X\cup N\) on the two sides force compatible proper-minor colourings.
Prove the colour alignment and expansion in full; specify which blocks
meet \(N\), which contain portals, and why \(v\) receives a missing colour.

This algebraic gluing lemma is a tool, not the final theorem.

#### B2. Contact-augmentation or colour-gluable-adhesion theorem

Fix a \(K_{t-1}\)-model in \(H\) maximizing contact with \(N\), using the
correct lexicographic potential.  Form the gammoid of paths from \(N\) to
labelled model bags.  If contact cannot be augmented:

1. obtain minimum separators by Menger;
2. uncross them into a lean or laminar decomposition rooted at \(N\);
3. retain every branch-set label and portal class in each adhesion; and
4. prove a dichotomy at some adhesion:
   * the torso supplies label-preserving routes that increase contact, or
   * both sides realize a common independent partition, so portalized
     exact-state transfer colours \(G\).

Use one-step minor transitions to rule out static boundary signatures that
are otherwise realizable.  For small adhesions, test whether knitted
colour-gluing applies.  For large adhesions, turn their size into the
disjoint routes needed for branch-set surgery.  Give the actual
inequalities; “small” and “large” may not be left qualitative.

The intended uniform endpoint is:

> Every counterexample-derived quadruple \((G,v,H,N)\) has an
> \(N\)-meeting \(K_{t-1}\)-model in \(H\).

Do not present “contact or a colourable separator” as progress unless the
separator outcome is proved from the counterexample hypotheses and the
colour gluing is completed.

#### B3. Independent near-clique/splitter route

Keep an independent team on a port-labelled peel-or-separator theorem for
the \(K_7^\vee\) model and its possible general-\(t\) analogue.  The lemma
must retain deficient-bag identities and all required adjacencies.
Contraction-critical edge-deletion colourings should be aligned with a
portal-minimal model.  A separator outcome must feed Programme B1.

## Multi-agent management

Maintain an explicit registry of approach families, live target lemmas,
counterexamples, and blocked routes.  Begin with independent teams on:

* reserved connectors and stable bridges;
* portalized colour transfer;
* contact gammoids and separator uncrossing;
* knitted/critical colour gluing;
* degree-eight/nine boundary cells;
* near-clique label-preserving surgery;
* computational falsification and finite signatures;
* adversarial proof audit.

Allocate agents dynamically rather than fixing counts.  Preserve at least
three incompatible proof routes through several rounds.  Cross-pollinate
only after each route has produced a precise lemma or obstruction.

Every research agent must return one of:

* a proved lemma with explicit constructions;
* a concrete counterexample to a proposed lemma;
* a finite exhaustive certificate with an independent verifier;
* a precise separator/branch-set configuration and the next missing
  implication.

Reject vague strategy reports.

When a route stalls on a lemma equivalent in strength to Hadwiger, mark it
blocked unless a new invariant, minor-transition mechanism, or constructive
induction is supplied.  Do not repeatedly reassign agents to a falsified
static boundary or connectivity-only statement.

## Computational standards

Computer search may discover finite lemmas, but every result must have:

1. an exact mathematical statement;
2. a discovery program separated from the verifier;
3. independently reconstructed constraints;
4. explicit branch-set or colouring witnesses;
5. complete isomorphism coverage, preferably by labelled exhaustive replay
   when feasible;
6. a clearly stated solver/trust boundary.

Do not extrapolate from bounded order or bounded cyclomatic number without a
proved contraction, decomposition, or minimal-obstruction theorem.

Public search may be used only for ordinary mathematical background and
standard named theorems, not to search for a solution to this exact
conjecture or benchmark.

## Mandatory adversarial audit

Audit every proposed proof for:

* branch-set disjointness and connectedness;
* every required pairwise bag adjacency;
* correct lifting after contractions;
* exact versus merely coarser boundary colour partitions;
* valid palette permutations on adhesions;
* portals retained on both sides of an internal separation;
* use of only the connectivity actually proved;
* isolated vertices, disconnected graphs, and small \(t\);
* circular use of \(\mathrm{HC}_t\), Strong Hadwiger, Hajós, list-Hadwiger,
  or an equivalent rooted-model assertion.

Run independent red-team agents against every candidate terminal proof.

## Terminal condition

Do not terminate after proving \(\mathrm{HC}_7\), after closing a finite
family, or after stating a new reduction.  After \(\mathrm{HC}_7\), use the
successful transfer/surgery mechanism to prove obstruction \((U)\) for the
least failing parameter \(t\), and finish the induction for every \(t\).

Return a complete self-contained proof of the stated conjecture only after
it survives adversarial audit, including disconnected graphs and all small
parameters.

If exhaustive work still fails to produce the complete proof, report only
the strongest genuinely new theorem proved in this run and the single exact
remaining implication, with every hypothesis stated.  Do not describe a
reduction as a solution.
