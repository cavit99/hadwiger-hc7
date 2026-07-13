# Independent audit: colourful rooted-`K_4` SPQR exchange

## Verdict

**GREEN AS PATCHED.**  The direct `R--R` theorem and, in particular, the
equal-defect pole repair in Lemma 7.3 are valid.  I found no counterexample
or illicit minor lift.  Two proof-text omissions should be repaired before
the note is cited:

1. the converse proof of Lemma 7.1 overlooks the subcase
   `alpha=beta*`; its conclusion is still true, by a one-line separate
   argument below; and
2. Theorem 7.2 needs an explicit fixed-partner argument to pass from one
   selected portal occurrence to the **full** portal set.  Hall forcing
   supplies exactly what that argument needs.

Neither repair adds a hypothesis or changes any stated outcome.

## 1. Compatibility graph: the omitted mate-defect subcase

Equation (7.3) is correct.  The sentence

> If `beta in W` and `alpha ne beta`, the mate edge `beta beta*` is
> present

is false when `alpha=beta*`, because `beta*` is then absent from the
vertex set.  This does not disconnect the graph.  In that subcase the
four vertices in the other two antipodal pairs induce a clique: their
mate edges are present, and every cross-edge between those pairs is
allowed by (7.3), since `beta` belongs to the deleted antipodal pair.
Moreover `beta` is adjacent to every one of those four vertices: for a
vertex `u` outside the `beta`-pair, the remaining roots in the unique
antipodal omission containing `beta,u` are `beta*=alpha` and `u*`, and
neither is `beta`.  Thus `H(alpha|beta)` is connected.

The other cases in the submitted proof are correct.  Hence Lemma 7.1,
including its exact six equal-defect exceptions, stands.

## 2. Full-set synchronization: the missing fixed-partner step

Fix a compatibility edge `ik` on the left.  Select distinct base
representatives

\[
                         a\in P_i\cap C_L,
             \qquad     b\in P_k\cap C_L.
\]

They exist because a Hall failure, or failure to force either displayed
incidence, is one of the excluded exact-seven/order-eight/capacity
outcomes.  Compatibility supplies distinct representatives of the
other two labels on the right.  Therefore, for **every** distinct
`r in P_i cap C_L`, `s in P_k cap C_L`, a rooted `K_4` at
`r,s,p,q` in the left torso would lift by Fabila--Monroy--Wood Lemma 12
to the forbidden colourful rooted `K_4`.  The planar rooted theorem
puts `r,s,p,q` on a face.

Let `F_ik` be the face containing `a,b,p,q`.  If
`r in P_i cap C_L` and `r != b`, use the pair `r,b`; its face shares the
three distinct vertices `p,q,b` with `F_ik`, so the two faces are equal.
If `r=b`, it is already on `F_ik`.  The symmetric argument, using the
fixed partner `a`, puts every occurrence of `P_k cap C_L` on `F_ik`.
Thus **both full portal sets** lie on one pole face.

For incident compatibility edges `ik` and `k ell`, choose any occurrence
of the common label `k`.  Their two full-set pole faces share that
occurrence and `p,q`; hence they are equal.  Connectivity of
`H(alpha|beta)` now propagates a single face through every label in a
component.  This is the precise justification needed in Theorem 7.2.

Portal occurrences at `p` or `q` are already on every pole face.  The
same proof applies in the right torso.

## 3. FMW localization and virtual-edge lifting

The use of Fabila--Monroy--Wood Lemma 12 in Theorem 7.2 is in the correct
direction.  A local rooted model at `r,s,p,q` in one augmented side,
together with two selected portal representatives in the other side,
lifts to the required global four-root model.  The roots are distinct by
the Hall choices.

Lemma 7.3 uses a slightly simpler lift.  In a direct `R--R` transition
the union is two-connected, so the opposite side contains a `p-q` path
whose internal vertices avoid the first side.  Contracting that path
onto the edge `pq` shows that the augmented torso is a minor of `D` while
keeping `p` and `q` distinct.  Consequently a rooted model at
`g,x,y,t` in the torso lifts to a rooted model at the same four vertices
in `D`, even when `g` is a pole and even when the model uses the virtual
edge.  There is no root identification.

## 4. Equal-defect pole repair

Assume the common defect is `c_a`.  Since neither open side has a
`c_a`-portal and the whole shore is full, some pole
`g in {p,q}` is a `c_a`-portal.  For an arbitrary mate occurrence
`x in P_{c_{a+3}} cap C_L`, Hall on the three labels
`c_{a+3},u,v`, followed by the forced-incidence form of Lemma 4.1,
gives distinct

\[
 x\in P_{c_{a+3}},\qquad y\in P_u,\qquad t\in P_v
\]

unless one of the explicitly retained cut/capacity outcomes occurs.
The four labels `c_a,c_{a+3},u,v` are exactly one antipodal omission.
By the lift in Section 3, a rooted `K_4` at `g,x,y,t` would be a
colourful rooted `K_4`, hence a `K_7` terminal.  Its absence makes those
four vertices cofacial.

The synchronized pole face already contains `g,y,t`.  Since these are
three distinct vertices, facial uniqueness in a simple three-connected
planar torso forces the new face to be the pole face.  Hence the
arbitrary mate occurrence `x` lies there.  Repeating on both sides puts
the entire mate class, and therefore all six cycle portal classes, on
the glued face.  This validates Lemma 7.3.

## 5. Colourful completion and final scope

The completion in Lemma 2.1 has the correct seven disjoint bags.  Adding
each boundary root to its colourful piece connects that bag; `R`, `{z}`
and the antipodal pair `M_j` give the last three.  Every cycle root is
adjacent to at least one end of `M_j`, and fullness/universality supply
all other adjacencies.  No contraction is reversed and no bag overlaps.

Corollary 7.4 is therefore sound **in its stated high-owner context**,
where the previously audited six-class SDR and cross-free frame packet
are available.  The note correctly retains the exact order-eight and
bounded-capacity alternatives; it does not claim that those operation
states have been discharged.

