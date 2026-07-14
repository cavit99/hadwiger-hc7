# Common-exit three-gates: packet reflection and a finite literal quotient

**Status:** proved and independently audited.
The unbounded part has a hand-checkable proof.  The last fixed
fifteen-vertex quotient is certified by the proof-producing verifier
`hc7_exact7_common_exit_quotient_verify.py` and its frozen literal-template
catalogue.

## 1. Normalized input

Use the setup and notation of the audited state-free exit-matching theorem
`../results/hc7_exact7_three_gate_exit_matching.md`, in its common-exit
outcome.  Assume throughout that `G` is in the hypothetical minimal-`HC_7`
counterexample kernel: it is `K_7`-minor-free, `\chi(G)=7`, and every
proper minor is six-colourable.  Retain the attained paired-triangle notation from
`../results/hc7_exact7_binary_duty_cycle_or_gate.md`:

\[
 \Pi=\{B_1,B_2,B_3,\{c\}\},
 \qquad B_i=\{a_i,t_i\},                                \tag{1.1}
\]

where every `B_i` is independent, every two distinct `B_i` have a literal
edge between them, and `c` has a literal neighbour in every `B_i`.  The
dutyless descended lobe `K` has

\[
 N_S(K)=A:=\{c,a_1,a_2,a_3\}.                           \tag{1.2}
\]

Let `X=\{x_1,x_2,x_3\}` be the three-gate, let `C` be the old rich-shore
component containing `K`, and let `P` and `Q` be the two old connected
`S`-full packets, with

\[
                    P\subseteq L,
 \qquad             Q\subseteq R-C.                    \tag{1.3}
\]

Every component of `C-X` meets all three vertices of `X`.  Let
`\mathcal J` be the sibling lobes of `K`.  In the common-exit outcome there
is one literal `t\in\{t_1,t_2,t_3\}` such that every sibling is
non-self-full and

\[
                  N_S(J)\cap(S-A)=\{t\}
                  \qquad(J\in\mathcal J).               \tag{1.4}
\]

Permute the three paired duties and write

\[
                        t=t_1,
 \qquad                 u=t_2,
 \qquad                 v=t_3.                          \tag{1.5}
\]

The old component `C` is `S`-full.  Indeed, `N_G(C)\subseteq S` separates
the nonempty component `C` from the nonempty opposite shore, so
seven-connectivity and `|S|=7` give `N_G(C)=S`.  No lobe of `C-X` contacts
`u` or `v`: this follows from (1.2) for `K` and from (1.4) for every
sibling.  Therefore the two remaining boundary contacts are gate-only:

\[
                  N_C(u)\cap X\ne\varnothing,
 \qquad           N_C(v)\cap X\ne\varnothing.           \tag{1.6}
\]

No distinctness of the two selected gate neighbours in (1.6) is assumed.

## 2. Exact sibling supports

### Lemma 2.1 (one missing label per sibling)

For every `J\in\mathcal J` there is a unique label `a(J)\in A` such that

\[
                       N_S(J)=\{t\}\cup(A-\{a(J)\}).     \tag{2.1}
\]

#### Proof

The audited exit-matching theorem gives `|N_S(J)|\ge4`.  Equations
(1.4)--(1.5) put all of this support inside the five-set `A\cup\{t\}`.
The lobe is non-self-full, so it misses at least one member of `A`.
It cannot miss two members, because its support would then have order at
most three.  It cannot miss none, by non-self-fullness.  It therefore
misses exactly one member of `A` and has all four remaining available
contacts, which is (2.1).  \(\square\)

Write `J_a` for a sibling whose unique missing label is `a`.

## 3. Three siblings close without a boundary census

### Lemma 3.1 (three-sibling closure)

If `|\mathcal J|\ge3`, then `G` contains a literal `K_7` minor or the
audited `(1,3)` packet reflection six-colours `G`.

#### Proof

Select three siblings.  There are three missing-label multiset types.

**All three missing labels are equal.**  Let the common label be `a`, and
put

\[
                        \Omega_a=X\cup\{t\}\cup(A-\{a\}). \tag{3.1}
\]

For one selected sibling `J_a^0`, equation (2.1) gives
`N_G(J_a^0)=\Omega_a`; hence it is one full shore behind an actual
seven-boundary.  The other two selected siblings are disjoint
`\Omega_a`-full packets.  A third disjoint `\Omega_a`-full packet is

\[
                             P\cup\{a\}\cup K.           \tag{3.2}
\]

It is connected through the two literal edges from `a` to `P` and `K`.
The old packet `P` supplies every old-boundary contact in `\Omega_a`, and
`K` supplies all three gate contacts.  Thus the new vector has one packet
on the `J_a^0` shore and at least three on the other.  The exact-seven
packet theorem makes it `(1,3)`, which the audited adaptive reflection
theorem closes.

**Three distinct missing labels.**  Write them `\alpha,\beta,\gamma` and
let `r` be the fourth member of `A`.  The following are seven literal
branch sets:

\[
 \begin{array}{lll}
 P\cup\{u\},&Q\cup\{v\},&K\cup\{\alpha\},\\
 J_\alpha\cup\{\beta\},&
 J_\beta\cup\{\gamma\},&
 J_\gamma\cup\{t\},\\
 \{r\}.&&
 \end{array}                                             \tag{3.3}
\]

Every nonsingleton set is connected by fullness or (2.1).  The two packet
bags are adjacent because `P` contacts `v` and `Q` contacts `u`; each is
adjacent to every other bag because every other bag contains a literal
boundary anchor.  The last five bags form a clique as follows.  The `K`
bag sees the anchors `\beta,\gamma,r`, and `J_\gamma` sees `\alpha`.
The `J_\alpha` bag sees `\gamma,t,r`; the `J_\beta` bag sees `t,r`; and
`J_\gamma` sees `r`.  These are all ten required adjacencies.

**Exactly two missing labels.**  Rename the multiset
`\alpha,\alpha,\beta` and write

\[
                           A=\{\alpha,\beta,r,s\}.
\]

For two distinct siblings `J_\alpha^1,J_\alpha^2` and one `J_\beta`, use

\[
 \begin{array}{lll}
 P\cup\{u\},&Q\cup\{v\},&K\cup\{\alpha\},\\
 J_\alpha^1\cup\{\beta\},&
 J_\alpha^2\cup\{s\},&
 J_\beta\cup\{t\},\\
 \{r\}.&&
 \end{array}                                             \tag{3.4}
\]

Again the packet bags see every anchored bag and each other.  Among the
last five bags, `K` sees `\beta,s,r` and `J_\beta` sees `\alpha`;
`J_\alpha^1` sees `s,t,r`; `J_\alpha^2` sees `t,r`; and `J_\beta` sees
`r`.  Thus (3.4) is a literal `K_7` model.  This exhausts the three
multisets.  \(\square\)

The proof is unbounded: extra siblings are ignored after selecting three.
It uses no completion edge of a web and no colouring state on a descended
boundary.  As an independent finite replay of these displayed multiset
models, the accompanying verifier also checks all

\[
                          20\cdot512=10,240              \tag{3.5}
\]

three-sibling missing-multiset/minimal-boundary quotients.

## 4. The exact two-sibling quotient

The gate-only contacts (1.6) actually close the remaining two-sibling
case.  The following lemma records the fixed finite core separately so
that its computational dependency is explicit.

### Lemma 4.1 (paired-triangle common-exit quotient)

Let `S,A,X,P,Q,K,J_\alpha,J_\beta` have the incidence in Section 1 and
(2.1), where `\alpha,\beta\in A` are allowed to be equal.  Assume only:

1. every `B_i` is independent;
2. `c` has a literal neighbour in each `B_i`;
3. every two distinct `B_i` have a literal edge between them;
4. `P,Q` are complete to the literal set `S` and are nonadjacent;
5. `K,J_\alpha,J_\beta` are each complete to `X`, are pairwise
   nonadjacent, and have exactly the boundary supports in (1.2), (2.1);
6. `u` and `v` each have a neighbour in `X`.

Then this fifteen-vertex quotient contains a `K_7` minor with every branch
set of order at most three.

#### Proof

There is a short human branch-set model in one preliminary subcase.  If
`\alpha\ne\beta`, put `A-\{\alpha,\beta\}=\{r,s\}`.  When `rs` is an edge,
the seven bags

\[
 P\cup\{u\},\quad Q\cup\{v\},\quad K\cup\{\alpha\},
 \quad J_\alpha\cup\{\beta\},\quad J_\beta\cup\{t\},
 \quad\{r\},\quad\{s\}                                  \tag{4.1}
\]

form a clique model.  The packet verification is as in (3.3).  Among the
last five bags, `K` sees `\beta,r,s`, `J_\beta` sees `\alpha`,
`J_\alpha` sees `t,r,s`, `J_\beta` sees `r,s`, and the final missing
adjacency is the assumed edge `rs`.

It remains to check equal missing labels and the distinct-label subcase
`rs\notin E(G)`.  This is a fixed literal quotient, and the accompanying
verifier gives the following exhaustive proof.

First delete surplus edges.  Retain one of the two possible `c-B_i` edges
for each `i`, one of the four possible `B_i-B_j` edges for each pair
`i<j`, and one selected edge from each of `u,v` into `X`.  Edge deletion
cannot create a clique minor, so a model in every retained graph suffices.
There are

\[
                         2^3 4^3=512                    \tag{4.2}
\]

minimal paired-triangle boundary witnesses and nine selected gate-contact
pairs.

After fixing the common exit pair `B_1`, permutation of `B_2,B_3` leaves
three equal-label orbits

\[
                 \alpha=\beta\in\{c,a_1,a_2\},          \tag{4.3}
\]

and four unordered distinct-label orbits

\[
 \{\alpha,\beta\}\in
 \bigl\{\{c,a_1\},\{c,a_2\},
          \{a_1,a_2\},\{a_2,a_3\}\bigr\}.             \tag{4.4}
\]

The verifier checks all

\[
             3\cdot512\cdot9=13,824                    \tag{4.5}
\]

equal-label quotients.  In the distinct case it discards only witnesses
already covered by (4.1).  The four orbit representatives leave
`384,384,256,256` minimal boundary witnesses, respectively, so with the
nine gate-contact choices the hard count is

\[
                  (384+384+256+256)\cdot9=11,520.       \tag{4.6}
\]

For each
quotient the frozen catalogue supplies seven nonempty, disjoint connected
branch sets of order at most three and the verifier checks every one of
their 21 pairwise adjacencies using only the listed literal retained edges.

The proof check is solver-free.  The command

```text
python3 results/hc7_exact7_common_exit_quotient_verify.py
```

exhaustively replays the frozen monotone catalogue.  Every entry lists its
required retained boundary/gate edges and the corresponding seven literal
branch sets; `--show-templates` prints them.  The final coverage check
verifies that at least one entry applies to every one of the cases in (4.5)
and every hard distinct case.  The optional `--regenerate` mode uses Z3 to
rediscover and compress a catalogue, after which the same ordinary
finite-set and graph checks verify branch-set membership, disjointness,
connectivity, and adjacency.  Hence every minimal quotient contains a
literal `K_7` model, and restoring deleted edges proves the lemma.
\(\square\)

Two representative symbolic templates illustrate that the gate contacts
are spent literally.  In the orbit
`(\alpha,\beta)=(a_1,a_2)`, the nonedge between the remaining labels
`c,a_3` forces `ct_3`.  If `t_2,t_3` meet the same selected gate `x_2`, one
certificate is

\[
 \{c,t_3\},\ \{J_{a_1},t_1,x_1\},\ \{t_2,x_2\},
 \ \{K,x_3\},\ \{a_3,J_{a_2}\},\ \{a_1,P\},\ \{a_2,Q\}. \tag{4.7}
\]

If their selected gate neighbours are distinct, renamed `x_1,x_2`, a
certificate is

\[
 \{c\},\ \{J_{a_1},t_2,x_1\},\ \{t_3,x_2\},
 \ \{a_3,K,x_3\},\ \{J_{a_2},t_1\},\ \{P\},\ \{a_1,Q\}. \tag{4.8}
\]

Both lists are independently replayed by the general checker; the printed
catalogue supplies the other symmetry/edge choices.

## 5. Lifting the quotient

### Theorem 5.1 (common-exit gates with two siblings close)

In the counterexample-derived common-exit configuration, if
`|\mathcal J|\ge2`, then `G` contains a literal `K_7` minor or is
six-colourable by the audited `(1,3)` reflection.  Consequently the
common-exit outcome is eliminated; the only surviving exit-matching
residue is the separate one-sibling gate.

#### Proof

When there are at least three siblings, apply Lemma 3.1.  Suppose exactly
two remain, with missing labels `\alpha,\beta` supplied by Lemma 2.1.

Contract each of the five pairwise disjoint connected sets

\[
                          P,Q,K,J_\alpha,J_\beta          \tag{5.1}
\]

to one quotient vertex, while retaining the seven literal vertices of `S`
and the three literal gate vertices of `X`.  Delete every surplus edge.
The old paired-triangle state supplies items 1--3 of Lemma 4.1, packet
fullness supplies item 4, the lobe/gate certificate supplies item 5, and
(1.6) supplies item 6.  Lemma 4.1 gives a `K_7` model in this minor.
Expanding the five contracted vertices to their original connected sets
lifts its branch bags literally and gives a `K_7` minor in `G`.  \(\square\)

## 6. Exact residue and trust boundary

Combining this theorem with the audited exit-matching theorem leaves only
the **one-sibling** gate.  That sibling may be self-full, or if non-self-full
may have an exit set of order one, two, or three; the common-exit theorem
does not constrain it further.

The three-sibling closure is hand-checkable; its `10,240`-case replay is an
independent guardrail rather than a dependency.  The essential computation
is the solver-free frozen catalogue for the `11,520+13,824` two-sibling
quotients.  The result does not preserve an attained state on a descended
boundary and does not create a global lexicographic measure.  Its finite
step is a fixed fifteen-vertex quotient certificate, not an enumeration by
shore order.  A future human compression of Lemma 4.1 would remove the
finite computational dependency, but is not needed for the audited result.
