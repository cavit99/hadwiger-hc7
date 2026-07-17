# Independent audit: repeated-colour rooted-`K_4` exchange barrier

**Audited source:** `hc7_repeated_colour_rooted_k4_exchange_barrier.md`
**SHA-256:** `8c30b47253d63cbf98e5c8ee5901bbe81abc6b3eb3b20c8a5c6e0c5aad38df09`
**Verdict:** **GREEN.**

The independent audit was performed on source hash
`8445a5cb7014d23e87a6868cea6524056c6a494027799c44f193d5c2a5f0b301`.
The only subsequent source change replaced the status phrase “separate
internal audit pending” by “separate internal audit GREEN”; the
construction, proofs, and scope are unchanged.

The construction refutes exactly the stated quotient-only exchange claim.
All chromatic, colourful-set, rooted-model, complete-minor, and forced
colour-repetition assertions are correct.  The example deliberately stops
at the universal contraction and does not claim an expansion to an actual
seven-connected, seven-chromatic, minor-critical star-Kempe host.

## 1. The compressed core and its colourings

Let `C={c_1,c_2,c_3}` induce `K_3`, and let `s-z-u-t` be the disjoint
four-vertex path.  The join

\[
                         Q=C\vee(s-z-u-t)
\]

has chromatic number

\[
                         \chi(Q)=3+2=5.
\]

Deleting the internal path vertices gives

\[
                         R=C\vee\{s,t\}=K_5-st.
\]

The triangle requires three colours and the two nonadjacent vertices
`s,t` can share a fourth, so `chi(R)=4`.  The neighbourhood identities are
literal:

\[
 N_R(z)=C\cup\{s\}=S,
 \qquad
 N_R(u)=C\cup\{t\}=T.
\]

Each of `S,T` induces `K_4`; hence every proper four-colouring of `R`
uses all four colours on each set.  Thus both are colourful.

The graphs denoted `R+z` and `R+u` are respectively `Q-u` and `Q-z`.
They are subgraphs of the five-colourable graph `Q` and contain the
five-cliques

\[
                         C\cup\{s,z\},
 \qquad
                         C\cup\{u,t\}.
\]

Both therefore have chromatic number five, as stated.

## 2. Independent minor-exclusion checks

The identity used in the source,

\[
                         h(K_r\vee H)=r+h(H),
\]

is valid.  A complete-minor model has at most `r` branch sets containing
vertices of the clique factor.  Every remaining branch set lies wholly in
`H`, remains connected there, and those remaining sets form a complete
minor model in `H`.  This proves the upper bound; the lower bound follows
by adjoining the `r` clique singletons to a largest complete-minor model
of `H`.  Since a path has Hadwiger number two,

\[
                         h(Q)=3+h(P_4)=5.
\]

Thus `Q` has no `K_6` minor.

There is also a direct treewidth certificate.  Arrange the following three
bags in a path:

\[
 C\cup\{s,z\},\qquad
 C\cup\{z,u\},\qquad
 C\cup\{u,t\}.
\]

They cover every edge of `Q` and satisfy the running-intersection
condition.  Each has order five, so `tw(Q)<=4`.  Since the first bag
induces a `K_5`, `tw(Q)=4`; minor-monotonicity again excludes `K_6`.

After adding the universal vertex `x`, put `x` into each of these three
bags.  This gives a width-five tree decomposition of

\[
                         \widehat Q=x\vee Q=K_4\vee P_4.
\]

The graph contains the named `K_6`, so its treewidth is exactly five.
It consequently has no `K_7` minor.  Equivalently, the join identity gives

\[
                         h(\widehat Q)=4+h(P_4)=6.
\]

These decompositions independently confirm both complete-minor exclusions
without relying on the chromatic calculations.

## 3. Contact-maximal rooted model

The singleton sets

\[
 D_1=\{c_1\},\quad D_2=\{c_2\},\quad
 D_3=\{c_3\},\quad D_4=\{s\}
\]

form an `S`-rooted `K_4` model because `S` induces `K_4`.  The first three
branch sets meet `T`; `D_4` is the unique deficient branch set in this
model.

Suppose some `K_4` model had all four branch sets meeting both `S` and
`T`.  Since the four branch sets are disjoint and each of `S,T` has order
four, each branch set would contain exactly one vertex of `S` and exactly
one vertex of `T`.  The three common vertices `c_1,c_2,c_3` must therefore
belong to three distinct branch sets.  Each such branch set has already
used its unique vertex from both root sets and can contain neither `s` nor
`t`.  The fourth branch set must contain both `s,t`.

Every `s`--`t` path in `R` uses a vertex of `C`, but all three vertices of
`C` already lie in the other branch sets.  The fourth branch set cannot be
connected.  Hence no simultaneously `S`- and `T`-rooted model exists.
The displayed model has three `T` contacts, while four are impossible, so
it is contact-maximal and no exchange can increase its contact count.

## 4. Named `K_6` and the forced repeated colour

In `\widehat Q`, the vertices

\[
                         x,c_1,c_2,c_3,s,z
\]

induce `K_6`: the first four form the complete join factor, `sz` is an
edge of the path, and every vertex of that edge is adjacent to the complete
factor.  The vertex `u` is adjacent to `x,c_1,c_2,c_3,z` and is not
adjacent to `s`.

Every proper six-colouring assigns six distinct colours to the named
`K_6`.  Since `u` is adjacent to five of its six vertices, the only colour
available to `u` is the colour on `s=D_4`.  Therefore

\[
                  \operatorname{colour}(u)
                    =\operatorname{colour}(s)
                    =\operatorname{colour}(D_4)
\]

in every proper six-colouring.  This is precisely the proposed repeated
deficient label, yet Section 3 proves that no contact-increasing rooted
model exists.

The source's alternative path-colouring explanation is also correct: the
complete factor consumes four colours, and the connected bipartite path
must alternate the remaining two.

## 5. Scope and assumptions

- Graphs are finite and simple; a clique-minor model has pairwise disjoint
  nonempty connected branch sets that are pairwise adjacent.
- The phrase “unique deficient branch set” concerns the displayed
  contact-maximal model.  The proved global fact is that every `S`-rooted
  model has at most three `T`-contacting branch sets.
- The universal vertex `x` models only the contraction of the connected
  dominating subgraph from the star-Kempe theorem.  No bipartite expansion
  of `x`, no seven-connected host, and no seven-chromatic minor-critical
  graph is constructed here.
- Accordingly, the example does not test the size of the full separator
  after lifting through an actual `X`, and it does not refute an order-seven
  separation or two-vertex-transversal alternative in the full host.
- It does prove that `K_6`-minor-freeness of `Q`, `K_7`-minor-freeness of
  the universal contraction, and the exact repeated six-colour label do
  not by themselves force a label-preserving or unlabelled rooted-model
  improvement.

The terminology-only cleanup in the current source does not alter any
mathematical statement or proof.  No correction to the audited revision is
required.
