# Complementary-lock near-`K_7` handoff

**Status:** proved and independently audited.

This note closes the transition obligation in the exact complementary
two-lobe lock.  The conclusion is a literal spanning `K_7^vee` model, not a
`K_7` model and not a six-colouring.  It is therefore an `S1` handoff rather
than a terminal proof of `HC_7`.

## 1. Abstract packing lemma

Let

\[
 S=\{c,a_1,t_1,a_2,t_2,a_3,t_3\},\qquad
 B_i=\{a_i,t_i\}.
\tag{1.1}
\]

Assume:

1. every `B_i` is independent;
2. `c` has a literal neighbour in every `B_i`;
3. `x,y` are distinct vertices outside `S`, and `D,E,L,Q` are pairwise
   disjoint nonempty connected sets, disjoint from `S union {x,y}`;
4. `L` and `Q` are `S`-full;
5. `D` and `E` each have a neighbour at both `x` and `y`;
6. the literal boundary contacts include

   \[
   \begin{aligned}
    &\{t_1,t_2,c,a_3,t_3\}\subseteq N_S(D),\\
    &\{a_1,a_2,c,a_3,t_3\}\subseteq N_S(E).
   \end{aligned}
   \tag{1.2}
   \]

No edge between `D` and `E` is required.

### Theorem 1.1 (two complementary lobes plus two full packets)

Under these hypotheses, the graph induced by the displayed sets contains
a literal `K_7^vee` model.  More precisely, choose

\[
 r\in B_3\cap N_S(c),\qquad B_3-\{r\}=\{s\}.
\tag{1.3}
\]

Then the seven branch sets

\[
 \begin{array}{lll}
  X=D\cup\{x\}, & Y=E\cup\{y\}, & F_1=L\cup B_1,\\
  F_2=Q\cup B_2, & \{c\}, & \{r\},\quad \{s\}
 \end{array}
\tag{1.4}
\]

are pairwise adjacent except possibly for the two pairs

\[
                         \{s,c\},\qquad \{s,r\}.
\tag{1.5}
\]

Thus `s` is a named singleton deficient centre and `c,r` are its two
named missing twins.

### Proof

All seven sets in (1.4) are nonempty and pairwise disjoint.  They are
connected: `D` meets `x`, `E` meets `y`, and each of the connected full
packets `L,Q` has a neighbour at both vertices of its assigned pair.

The sets `X,Y` are adjacent because `D` has a neighbour at `y` (and,
symmetrically, `E` has a neighbour at `x`).  The four cross-adjacencies
between `X,Y` and `F_1,F_2` are witnessed literally by

\[
       Dt_1,\quad Dt_2,\quad Ea_1,\quad Ea_2,
\tag{1.6}
\]

respectively.  The two packet bags are adjacent because `L` is `S`-full,
so `L` has, for example, a neighbour at the literal vertex `a_2` in
`F_2`.

Every one of `c,r,s` is adjacent to both `X` and `Y` by (1.2), and to both
`F_1,F_2` by fullness of `L,Q`.  Finally `c` is adjacent to `r` by the
choice (1.3).  The pair `rs` is a nonedge because `B_3` is independent;
the pair `cs` may or may not be an edge.  Consequently every required
edge of `K_7` is present between the seven bags except for at most the two
edges in (1.5), which share the deficient bag `{s}`.  Extra adjacency
`cs`, if present, is harmless.  The bags therefore form a literal
`K_7^vee` model.  \(\square\)

## 2. Application to the exact complementary lock

Use the setup and notation of
the archived Section 3 of
[`../archive/hc7_exact7_two_component_paired_exchange_long_draft.md`](../archive/hc7_exact7_two_component_paired_exchange_long_draft.md).
The old open
thin shore `L` is connected: every component of `G[L]` is `S`-full by
seven-connectivity, while its packet number is one.  The second rich
component `Q` is connected and `S`-full.  For the two lobes `D,E` of the
two-cut, equations (3.6)--(3.8) of that note give precisely (1.2), and
two-connectivity gives a neighbour from each lobe to each pole `x,y`.

### Corollary 2.1 (the live complementary lock reaches `S1`)

Every exact complementary two-lobe lock in the oriented `(1,2)` cell has
the spanning labelled `K_7^vee` model (1.4).  Its union is

\[
 D\cup E\cup\{x,y\}\cup L\cup Q\cup S=V(G).
\tag{2.1}
\]

Hence the lock is not a further exact-seven state-transition obligation:
it is a normalized near-`K_7` handoff with a singleton deficient centre.

This conclusion uses neither the later Kempe locks nor an edged defect
pair.  Those conditions may still be useful after the handoff, but they
are not needed to construct the near model.

### Corollary 2.2 (standardized trichotomy output)

Assume in addition that `G` is seven-connected.  Every complementary lock
has one of the following three outputs:

1. a literal `K_7` model;
2. an actual separator (full on every component side when its order is
   seven); or
3. a labelled one- or two-hole near-`K_7` model whose deficient centre is
   a proper nonempty connected subset of one of

   \[
                         X,\quad Y,\quad F_1,\quad F_2.
   \tag{2.2}
   \]

#### Proof

Use the notation of Theorem 1.1.  If `cs` is absent, `{s}` is anticomplete
to the two singleton twins `{c},{r}` and meets the four neutral bags
`X,Y,F_1,F_2`.  The model is spanning, so every neighbour of `s` lies in
those four bags.  Seven-connectivity gives `d_G(s)>=7`; hence the literal
neutral portal set has order at least seven.  The audited uniform
seven-root trichotomy in `hc7_near_k7_seven_root_trichotomy.md` applies and
gives exactly the three listed outcomes.

If `cs` is present, the model has one missing spoke, namely `sr`.  Apply
the audited singleton one-hole trichotomy in
`hc7_near_k7_singleton_one_hole_trichotomy.md` with missed row `{r}` and
contacted rows `{c},X,Y,F_1,F_2`.  Again the model is spanning, so its
neighbourhood hypothesis is exact.  The singleton row `{c}` cannot be the
two-root donor used by that theorem; consequently every nonterminal
deficiency rotation has its new centre in one of the four sets (2.2).
\(\square\)

## 3. Exact scope

The theorem does not upgrade `K_7^vee` to `K_7`.  It discharges only the
named step

\[
       \text{complementary two-lobe lock}\Longrightarrow
       \text{labelled near-`K_7` `S1` input}.
\]

Corollary 2.2 additionally places that input immediately into the audited
near-model rotation/adhesion system.  It does not prove that repeated
rotations terminate; that remains the global `S1` composition gap.

The static quotient in
`../barriers/hc7_exact7_complementary_lock_k7vee_barrier.md` is not a
counterexample to Theorem 1.1: that quotient contains only one full packet
`Q` and deliberately omits the second full packet `L`.  The second packet
is used essentially in the branch set `F_1=L\cup B_1`.
