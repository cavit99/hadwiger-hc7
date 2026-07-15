# Global `K_5`-model transversal endgame

**Status:** open and `HC_7`-strength.  This is the global theorem which the
local near-model and exact-seven machinery is now required to prove.  It is
not an audited consequence of that machinery.

**Current mechanism (2026-07-15):** the earlier response-enriched state
graph was too broad to give more than tautological sink existence.  It has
been replaced by the literal
[`dominating-edge transition system`](hc7_global_dominating_edge_sink_goal.md).
The published dominating four-colour theorem makes that system closed on
two-sets, and terminal-cycle rotation makes every sink a cycle-rich family
of literal edges.  The active obligation is to classify that whole family,
not to refine another local portal state.  The
[`near-Hajós pair height`](hc7_global_near_hajos_pair_height.md) supplies
the uniform path geometry but is not yet a strict exchange invariant.

## 1. The global parameter

For a graph `G`, write

\[
 \tau_5(G)=\min\{|X|:G-X\text{ is }K_5\text{-minor-free}\}.       \tag{1.1}
\]

Equivalently, `tau_5(G)` is the minimum order of a vertex set meeting the
support of every `K_5` model of `G`.  This parameter is independent of a
chosen near model, adhesion, colouring, portal system or rotation.

There is a useful truncated version.  Let `K_r(G)` be the family of
supports of all `K_5` models using at most `r` vertices, and put

\[
 \tau_5^{\le r}(G)=\min\{|X|:X\cap U\ne\varnothing
                         \text{ for every }U\in K_r(G)\}.       \tag{1.2}
\]

The empty family has transversal number zero.  These numbers are
nondecreasing in `r`, and

\[
                  \tau_5^{\le |G|}(G)=\tau_5(G).          \tag{1.3}
\]

Define the **support-transversal height**

\[
 h_5(G)=\max\{r:5\le r\le |G|,
                         \tau_5^{\le r}(G)\le2\}.         \tag{1.4}
\]

The literal-`K_5` transversal theorem below makes this set nonempty in
the target-free seven-connected branch.  This is a genuine graph-global
quantity.  It does not depend on which pair witnesses the inequality at
one level.

If `G` is a hypothetical minor-minimal counterexample to `HC_7`, then

\[
                              \tau_5(G)\ge3.              \tag{1.5}
\]

Indeed, if `G-{p,q}` were `K_5`-minor-free, known `HC_5` would
four-colour it, and two fresh colours on `p,q` would six-colour `G`.

## 2. Exact endgame theorem

The clean global target is the following.

### Near-`K_7` transversal theorem

Every seven-connected, strongly 7-contraction-critical graph containing a
`K_7^vee` minor satisfies

\[
              G\succeq K_7\quad\text{or}\quad \tau_5(G)\le2.       \tag{2.1}
\]

This theorem would prove `HC_7`.  A minimal counterexample is
seven-connected, the Norin--Totschnig theorem supplies a `K_7^vee`
minor, and the first outcome is forbidden by hypothesis while the second
contradicts (1.5).

The target is deliberately `K_5`-minor-free after two deletions, not
planar after two deletions.  Planarity is stronger than the colouring
argument needs.

No counterexample was found even to the stronger version omitting
criticality in the complete exact census through order eleven: every
seven-connected host encountered already had a `K_7` minor.  The
joined-planar guardrails `K_2 vee H` satisfy (2.1) with their two universal
vertices.  This is evidence only.  The theorem is not a known corollary of
connectivity, rooted-minor theory or an apex theorem.

## 3. What is already global and proved

Four facts may be used without selecting one permanent near model.

1. **Actual `(1,2)` rank.**  Among all oriented actual exact-seven
   `(1,2)` separations, the order of the packet-one shore has a global
   minimum.  A handoff to a smaller actual `(1,2)` packet-one shore is a
   genuine contradiction, regardless of the returned state.
2. **Two-universal terminal.**  If `G=K_2 vee H`, then `G` is
   `K_7`-minor-free exactly when `H` is `K_5`-minor-free.  Under
   seven-connectivity the remainder is five-connected and hence planar.
3. **Pair/model first-hit lock.**  For a globally contact-maximal adjacent
   pair and `K_5` model in its deletion, every first model row reached by
   a pole-to-pole path was already contacted by that pole.  Six disjoint
   paths therefore form a literal locked channel system.
4. **Literal-`K_5` transversal.**  Every seven-connected graph either has
   a `K_7` minor or has a two-vertex transversal of all literal `K_5`
   subgraphs.  Hence a `K_7`-minor-free host has a pair `P` with
   `mu(P)>=6` for the support potential in Section 6.

In the language of (1.4), the last theorem proves

\[
                 K_7\not\preccurlyeq G\Longrightarrow h_5(G)\ge5.
                                                               \tag{3.1}
\]

The exact terminal is `h_5(G)=|G|`, which is equivalent to
`tau_5(G)<=2`.

The packet-to-root-connectivity theorem is also uniform, but it supplies
only an existential rooted core inside one closed shore.  It is a local
normalization, not a global rank.

## 4. Two failed pseudo-invariants

Neither of the following may be used as the progress measure.

* Rooted-`K_4` reselection has an exact involutive two-cycle preserving
  the roots, model union, bag sizes and boundary-contact vector.
* The globally maximal adjacent-pair/`K_5` contact profile can stop at
  `(4,5)`, exactly a labelled `K_7^-` state, while its numerical data do
  not identify the valid transversal pair.

Both failures occur in `K_2 vee I`, where `I` is the icosahedron.  They do
not refute a
criticality-based theorem; they prove that local model improvement and
raw contact order do not orient the proof.

## 5. The required global mechanism

The local programme is useful only if it proves one of the following
global statements.

1. **Transversal production:** directly produce one pair meeting every
   `K_5` model.
2. **Class-invariant descent:** map each whole neutral rotation/reselection
   component to a literal carrier and prove strict containment on every
   nonterminal exit.
3. **Sink coherence:** prove that all proper-minor responses in a sink
   neutral component yield a common exact state, a literal `K_7`, or the
   same two-vertex `K_5`-model transversal.

Finiteness of the state graph by itself proves nothing beyond the
existence of a sink strongly connected component.  The response-enriched
state graph has not yet been defined with a proved closed state language,
and no theorem currently classifies its sinks.  Consequently “sink
coherence” is a theorem target, not an existing invariant.

The atomic twin-seam exchange is retained only as a possible decoder for
an edge of this global system.  Closing another labelled portal cell is
not progress unless it proves a class-invariant exit or one of the
terminal outcomes above.

## 6. The uniform support-extension programme

The missing global invariant theorem now has an exact form:

> **Support-extension theorem.**  In a hypothetical minimal `HC_7`
> counterexample, for every `5<=r<|G|`,
> \[
>       \tau_5^{\le r}(G)\le2
>          \Longrightarrow \tau_5^{\le r+1}(G)\le2.      \tag{6.1}
> \]

Together with (3.1), induction would give `h_5(G)=|G|` and hence the
terminal pair.  This is one uniform theorem, not permission to enumerate
model supports one order at a time.  The first nontrivial level is a
laboratory for discovering its proof mechanism.

At `r=5`, every new order-six model has exactly one two-vertex edge-bag
and four singleton bags.  The proved support-six contraction dichotomy
shows that contracting that edge either preserves seven-connectivity or
exposes an actual exact-seven adhesion containing both split vertices.
In a minimal counterexample the contraction is exactly six-chromatic, and
both split endpoints see all five colours other than the contracted
colour in every six-colouring.  Thus the first extension step is a
stateful two-transversal pullback across a complementary vertex split,
with an exact-seven adhesion as its canonical alternative.

The target is

\[
                         \tau_5^{\le6}(G)\le2.           \tag{6.2}
\]

but a proof is valuable only if its pullback mechanism is stated so that
it can extend to an arbitrary minimal branch bag.  A four-pattern
calculation alone would merely restart the case programme.

## 7. The pairwise support potential

For a pair `P` define

\[
 \mu(P)=\min\{|V(\mathcal M)|:\mathcal M\text{ is a }K_5
                  \text{ model in }G-P\},                \tag{7.1}
\]

with `mu(P)=infinity` when no such model exists.  A terminal pair is
exactly a pair of infinite value.  Maximizing `mu(P)` is a legitimate
global selection principle and, unlike raw contact rank, recognizes the
universal pair in the joined-planar guardrails.

For a fixed `r`, a pair witnesses `tau_5^{<=r}(G)<=2` exactly when
`mu(P)>=r+1`.  Thus `mu` is best used as the witness carried by the global
height (1.4), not maximized in isolation.  Constructing a new model gives
only an upper bound on `mu(P)`; proving a strict increase requires excluding
every smaller model and is already a transversal statement.

The exact joined-icosahedron census gives values `5`, `7`, and `infinity`
on base--base, apex--base, and the universal apex pair, respectively.
Thus `mu` recognizes the terminal in the canonical guardrail, but the
whole neutral near-model rotation triangle remains at value five.  The
potential can normalize globally; it cannot orient a bare rotation.

The live finite-support normal form begins at `mu(P)=6`.  A minimum model
then consists of one two-vertex connected bag and four singleton bags.
Any theorem about this form is admitted only if it proves a pair with
larger `mu`, a terminal pair, or a reusable exchange valid beyond the one
displayed model.

## 8. Immediate research gate

The next result admitted to the proof spine must therefore be one of:

* a proof of the uniform support-extension theorem, beginning with (6.2);
* a theorem making the actual `(1,2)` thin-shore rank reachable from
  every nonterminal near-model sink; or
* a direct proof of sink coherence for the sharp `(4,5)`/`K_7^-`
  component.

Until one is proved, the programme has a global terminal formulation but
does not have the missing global invariant.

## 9. Literature boundary

Kawarabayashi--Luo--Niu--Zhang asked whether every `k`-connected
`K_k`-minor-free graph is `(k-5)`-apex.  At `k=7` this asks for a
two-vertex planarizing set in every seven-connected `K_7`-minor-free
graph.  The target (2.1) asks only for a `K_5`-minor transversal and keeps
the near-model and contraction-critical hypotheses, but it sits inside
that unresolved Jorgensen-type programme.

The literal-clique rung uses Theorem 1.10 of Niu--Zhang, *Cliques, minors
and apex graphs*, Discrete Mathematics 309 (2009), 4095--4107,
DOI `10.1016/j.disc.2008.12.009`.  Existing clique theorems do not apply
to arbitrary `K_5` branch-set models.  Existing minor packing--covering
theorems require much higher connectivity and do not give a cover of order
two.  No published theorem found in the literature review supplies (2.1).
