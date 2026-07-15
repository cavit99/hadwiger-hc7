# Independent audit: reserve-rooted `C_4` exchange in the atomic twin seam

**Verdict:** **GREEN at the frozen source hash below.**  Lemmas 2.1 and
2.2, Theorem 3.1, and Corollary 3.2 are correct in the stated atomic
twin-seam setting.  In particular, the induced host `W` really excludes
the unused part of the old rich shore, the new lobe has literal
neighbourhood exactly `S'`, the packet vector has the asserted orientation,
and contracting a boundary incidence produces the claimed high-demand
handoff.

The result remains conditional on the existence of a reserve-rooted
`C_4`.  Section 4 gives an exact Robertson--Seymour--Thomas feasibility
test for that model; it does not prove either feasibility condition.

**Audited source:**
`results/hc7_atomic_twin_seam_reserve_rooted_c4_exchange.md`.

**Source SHA-256:**
`1bcb104cc15d6fda5e86ff7dd374aa79222656a67c105575b2abe2239c401aff`.

## 1. Exact scope and frozen dependencies

The proof uses the full atomic twin-seam normal form, not merely the two
displayed neighbourhood equalities.  In particular,

\[
 A_{\rm old}-Z=D\mathbin{\dot\cup}E,
 \qquad S=I\mathbin{\dot\cup}A_0\mathbin{\dot\cup}B_0,
\]

`D,E` are distinct components of `G[A_old-Z]`, there is no old
`A_old-R` edge, and the ambient graph is seven-connected,
`K_7`-minor-free, and strongly seven-contraction-critical.  These are the
frozen hypotheses behind the phrase “atomic twin-seam notation.”  They
are used explicitly in (3.5), (3.7), the exact-seven packet theorem, and
Corollary 3.2.

The reserve sets are sound.  Since each old packet `R_i` is `S`-full,
`R_i` has a neighbour at `a_i`; hence

\[
 C_i=R_i\cup\{a_i\}
\]

is connected.  The two sets are disjoint, and each is `J`-full because
`J\subseteq S` and already every `R_i` contacts every literal member of
`J`.

The definition

\[
 W=G[D\cup A_0\cup V(R_1)\cup V(R_2)\cup\{p,q\}]
\]

is important and correct: `W` contains neither `E`, nor `J`, nor any
unused vertex of the old rich shore `R-(R_1\cup R_2)`.  No later argument
silently puts those omitted vertices back into a model bag.

## 2. Lemma 2.1: spoke normalization

For a connected `P` bag, a minimal tree joining `p,x_A,x_B` has a unique
median.  Its three terminal arms meet only at that median.  Retaining the
`p` arm and assigning the other two arms, with the median deleted, to
`A` and `B` therefore preserves disjointness and connectivity.  The first
arm edge supplies the required contact when an arm is nonempty; the
original selected model edge supplies it when the arm is empty.

The degenerate possibility `x_A=x_B` is harmless: take the common vertex
as the median, so both carrier arms are empty and the two selected model
edges give the two contacts.  The same convention handles a selected
endpoint equal to `p`.

After the `P` operation, the old `A-Q` and `Q-B` contacts remain.  The
same operation may then be applied to `Q` against the already enlarged
carriers.  Its arms lie in the old `Q` bag and are disjoint from every
current carrier, so the second operation does not undo the first.  Both
reserve sets remain in their named carrier bags.  Lemma 2.1 is therefore
valid.

## 3. Lemma 2.2: stem shortening

Let an `M`-path `L` join `x\in P^-` to `A`.  Its internal vertices avoid
all four old bags.  Consequently the four replacements

\[
 P'=P[p,x],\quad A'=A\cup(L-x),\quad Q'=Q,
 \quad B'=B\cup P(x,c_p]
\]

are pairwise disjoint and connected.  The first edge of `L` is the new
`P'-A'` contact, and the edge from `x` into the nonempty removed stem
suffix is the new `P'-B'` contact.  The old contacts through `Q` survive.
Moreover, `x` is adjacent to both new carriers, so this is again a
spoke-form model and its total stem length is strictly smaller.  The
other three endpoint choices are symmetric.  There is no hidden lifting
or branch-set overlap in this rerouting.

## 4. Zero-stem outcome

If `c_p=p` and `c_q=q`, disjointness from `P={p}` and `Q={q}` places
`A,B` wholly in

\[
 B_E=D\mathbin{\dot\cup}A_0\mathbin{\dot\cup}R.
\]

The contained reserves `C_1,C_2` provide all five contacts in `J`, and
spoke form provides both gate contacts.  Thus `A,B` are two disjoint
`Omega_E`-full packets, contradicting the normalized value
`nu_{B_E}^{Omega_E}=1`.  Outcome 1 is literal.

## 5. The strict-separator construction

The hubs are distinct because `P,Q` are disjoint.  They avoid `J` because
`W` contains no vertex of `J`.  Hence

\[
 S'=J\mathbin{\dot\cup}\{c_p,c_q\}
\]

has exactly seven literal vertices.

In `W-{c_p,c_q}`, a shortest path from `X_0=P^-\cup Q^-` to `A\cup B`
would have a last vertex in `X_0` and a first later vertex in `A\cup B`.
The intervening subpath has both ends in `M` and all internal vertices
outside `M`, because

\[
 M-\{c_p,c_q\}=X_0\mathbin{\dot\cup}A\mathbin{\dot\cup}B.
\]

It is therefore an `M`-path forbidden by Lemma 2.2.  It follows that the
union `X` of the reached components avoids both carrier bags.

This also proves the claimed containment

\[
 X\subseteq D\cup\{p,q\}.
\]

Indeed, `A_0\cup R_1\cup R_2` is contained in `A\cup B`, while `W`
contains no other old-rich-shore vertex.  Thus there is no unused `R`
through which a reached component could escape.

### Literal audit of `N_G(X^*)`

Put `C={c_p,c_q}` and `X^*=X\cup E`.  Every nonempty stem prefix contains
its named gate.  Since `E` is connected and contacts both `p,q`, it joins
all components included in `X`; hence `X^*` is connected.

Every possible external neighbour is accounted for as follows.

* From `E`, equation (1.1) permits only `Z\cup J`.  Each gate in `Z` is
  either in its nontrivial prefix `X` or is its trivial-stem hub in `C`.
* From `X\cap D`, equation (1.1) permits only `Z\cup I\cup A_0` outside
  `D`.  The gates again lie in `X\cup C`, `I\subseteq J`, and an edge to
  `A_0\subseteq A\cup B` would put that carrier in the same component of
  `W-C`, which was excluded above.
* From a gate in `X\cap Z`, neighbours in the old thin shore lie in
  `D\cup E\cup Z`, old-rich-shore neighbours are excluded by the absence
  of an old `A-R` edge, and old-boundary neighbours lie in
  `I\cup A_0\cup B_0`.  Here `I\cup B_0=J`, while an `A_0` neighbour is
  again impossible by the component definition of `X`.
* Any neighbour in `W-X` lies in `C`, since `X` is a union of components
  of `W-C`.

Therefore

\[
 N_G(X^*)\subseteq J\cup C=S'.
\]

The two carriers `A,B` lie outside `X^*\cup S'`, so the opposite open
shore is nonempty.  A proper subset of the seven-set `S'` as the
neighbourhood of nonempty `X^*` would be a cut of order at most six.
Seven-connectivity therefore gives `N_G(X^*)=S'`, making this an actual
seven-separation.

## 6. Packet orientation and strictness

The carrier bags remain disjoint, connected, and outside `X^*\cup S'`.
Each contains its `J`-full reserve, and each contacts both hubs by spoke
form.  Thus they are two disjoint `S'`-full packets on the opposite shore.
The connected shore `X^*`, whose literal neighbourhood is `S'`, is one
`S'`-full packet on its own side.

The audited exact-seven packet theorem says that the only packet vectors,
up to orientation, are `(1,1)`, `(1,2)`, and `(1,3)`, and one coordinate
is exactly one.  Since the carrier side has packet number at least two,
the orientation is forced:

\[
 (\nu_{X^*},\nu_{\rm opp})=(1,2)\quad\text{or}\quad(1,3).
\]

The audited adaptive theorem closes `(1,3)`, leaving the asserted
oriented `(1,2)` cell.

For strictness, all four model bags lie in `W`, the reserves fill every
`A_0` and selected-rich-shore vertex, and disjointness therefore puts each
hub in `D\cup Z`.  A nontrivial `p`-stem has `c_p\ne p`; it also cannot
equal `q\in Q`, so `c_p\in D`, and similarly for `q`.  At least one stem
is nontrivial, hence at least one vertex of `D` is omitted from `X^*`.
Since

\[
 X^*\subseteq D\cup E\cup Z=A_{\rm old}
 \quad\text{and}\quad C\cap X^*=\varnothing,
\]

one obtains `|X^*|<|A_old|` exactly as claimed.

## 7. Corollary 3.2: contraction, reflection, and gluing

Because `X^*` is `S'`-full, a literal edge `xs` with
`x\in X^*`, `s\in S'` exists.  Contracting it and retaining the name `s`
is a proper minor operation.  Strong contraction-criticality supplies a
six-colouring of `G/xs`.

Restrict that colouring to the **opposite packet-two closed shore** and
interpret the contracted image's colour as the colour of the untouched
literal `s`.  No vertex of that open shore was contracted.  Edges added at
`s` by the contraction only impose additional constraints, so the
restriction is a proper colouring of the original closed shore.  It gives
an exact independent-block partition `Pi` of the seven literal boundary
vertices.

If `d_{G[S']}(Pi)\le2`, apply exact packet reflection using the two packets
in that same opposite shore.  Its contractions are pulled back only to
the `X^*` closed shore, exactly in the legal direction of the reflection
lemma.  The construction either gives a literal `K_7`, or produces a
proper colouring of `G[X^*\cup S']` with equality partition exactly `Pi`.
The original contraction colouring gives the opposite closed-shore
colouring with the same exact partition.  A permutation of the six colour
names aligns the block colours, and the two colourings glue because the
open shores are anticomplete.

Thus a demand-at-most-two response is terminal.  In the unresolved branch
of the hypothetical counterexample,

\[
 d_{G[S']}(Pi)\ge3.
\]

This is a named high-demand handoff, not a proof that an arbitrary
contraction returns a prescribed paired-triangle state.

## 8. Robertson--Seymour--Thomas residual

Section 4 quotes Robertson, Seymour, and Thomas, *Hadwiger's conjecture
for `K_6`-free graphs* (1993), theorem (2.1), accurately.  For four
distinct roots `v_1,v_2,v_3,v_4`, that theorem says that a rooted cyclic
four-fragment model exists if and only if both subpartitions

\[
 \{v_1,v_2\},\{v_3,v_4\},
 \qquad
 \{v_2,v_3\},\{v_1,v_4\}
\]

are feasible by disjoint connected fragments.  Substitution of
`(v_1,v_2,v_3,v_4)=(p,r_1,q,r_2)` gives exactly (4.2).

Contracting each connected reserve `C_i` to `r_i` preserves four distinct
roots.  A rooted model in the quotient lifts by expanding the corresponding
root bag to contain all of `C_i`; connectivity, disjointness, and every
used adjacency are preserved.  Conversely, contracting a reserve-rooted
model gives the ordinary rooted model.  Thus the quotient equivalence is
exact.

Nothing in this audit promotes either feasibility test.  Seven-connectivity
alone is not invoked as a substitute, and a failed test may still return a
genuine Two-Paths/web obstruction.  The remaining allocation implication
in Section 4 is therefore correctly labelled as an obligation rather than
a theorem.

## 9. Trust boundary

What is proved is the conditional exchange

\[
 \text{reserve-rooted }C_4
 \Longrightarrow
 \text{two full packets, or terminal/strict oriented }(1,2)\text{ descent}.
\]

It does not prove existence of that rooted model, the twin-seam
double-lock theorem, the RST feasibility conditions, a general
state-preserving composition theorem, or `HC_7`.
