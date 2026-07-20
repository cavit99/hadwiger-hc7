# Two free root choices in the critical-edge response star

**Status:** written proof; [separately audited GREEN](hc7_order8_dual_free_root_response_star_audit.md).  This note
strengthens the arbitrary-edge response-star theorem only in its
pentagonal-bipyramid branch.  It does not close the low-degree contact
branch, the dirty-path exchange, the order-eight interface, or `HC_7`.

## 1. Setting

Let `G` be a seven-connected graph such that

\[
 \chi(G)=7,
 \qquad \chi(M)\le6\text{ for every proper minor }M\text{ of }G.
 \tag{1.1}
\]

Let `S` be an eight-vertex set for which `G-S` has exactly two components
`C,D`, each adjacent to every literal vertex of `S`.  Fix `v in C` and an
edge

\[
                         e=vx,\qquad x\in(C-v)\cup S.  \tag{1.2}
\]

The independently audited arbitrary-edge response-star theorem supplies
the exact separator and descent alternatives used below.  We repeat the
short construction needed to retain both nonresponse limbs before a root
is chosen.

## 2. Eight latent columns

### Lemma 2.1 (two nonresponse limbs)

At least one of the following holds.

1. A nonempty connected proper subset of `C` or `D` has an actual full
   neighbourhood of order seven.
2. A nonempty connected proper subset of `C` is a strict generic
   order-eight response-side descent for one of seven prescribed edges at
   `v`.
3. There are two eight-fans

   \[
               (P_s^C:s\in S),\qquad(P_s^D:s\in S)    \tag{2.1}
   \]

   from respective centres `v in C` and `w in D`, with common literal end
   set `S`, and a labelling

   \[
                    S=\{t,c_0,c_1,c_2,c_3,c_4,a,b\}   \tag{2.2}
   \]

   with the following properties.

   - The `t`-limb at `v` begins with `e` and contains `x`.
   - In a six-colouring of `G-e`, with `c(v)=c(x)=alpha`, the `c_i`-limb
     begins with the first edge of an `alpha,beta_i` Kempe path from `v`
     to `x`, where the `beta_i` are the five colours different from
     `alpha`.
   - The two remaining labels `a,b` belong to limbs whose first edges were
     not selected from those six response edges.

   For every `s in S`, put

   \[
                  K_s=(P_s^C-v)\cup(P_s^D-w).          \tag{2.3}
   \]

   The eight sets `K_s` are pairwise disjoint connected subgraphs.  For
   every choice `r in S`, consuming `K_r` produces adjacent connected
   roots

   \[
        R_C^r=P_r^C,
        \qquad R_D^r=P_r^D-\{r\},                     \tag{2.4}
   \]

   disjoint from the seven columns `K_s` with `s ne r`, and each root is
   adjacent to every one of those seven columns.

#### Proof

Six-colour `G-e`.  Its endpoints have one colour `alpha`.  For each of the
other five colours `beta_i`, the corresponding bichromatic component
containing `v` contains `x`; otherwise one Kempe interchange would make
`e` proper and six-colour `G`.  Choose a simple `v`--`x` path in each
component.  Its first neighbour has colour `beta_i`, so these five first
edges are distinct and are different from `e`.

Seven-connectivity gives `d_G(v)>=7`.  Pad the six response edges by one
further edge at `v` and apply the prescribed-first-edge all-boundary fan
lemma.  Its separator or response-side outcomes give outcome 1 or 2 here.
Otherwise it gives an eight-fan which preserves all six response first
edges and has two remaining limbs: the padded limb and the additional
limb supplied by strict-gammoid augmentation.  Label their ends `a,b`,
label the target end `t`, and label the five response-source ends
`c_0,...,c_4`.

Choose any `w in D`.  The ordinary fan form of Menger gives an eight-fan
from `w` to all of `S`, unless the same full-neighbourhood argument returns
outcome 1.  This proves (2.1)--(2.2).

For each `s`, the two fan tails in (2.3) meet at their common end `s` and
nowhere else, so `K_s` is connected and the eight such sets are pairwise
disjoint.  Fix `r in S`.  The two sets in (2.4) are connected and disjoint:
`R_C^r` contains `r`, while `R_D^r` is the other fan limb with its last
vertex removed.  They are adjacent through the last edge of `P_r^D`.
For `s ne r`, the first edge of `P_s^C` joins `R_C^r` to `K_s`, and the
first edge of `P_s^D` joins `R_D^r` to `K_s`.  Fan disjointness gives all
required disjointness.  \(\square\)

Let `K` denote the contact graph of the eight latent columns:

\[
 st\in E(K)\quad\Longleftrightarrow\quad
 E_G(K_s,K_t)\ne\varnothing.                           \tag{2.5}
\]

For a consumed label `r`, the contact graph of the seven surviving columns
is exactly the induced graph `K-r`.  Consequently, a `K_5` model in `K-r`,
together with `R_C^r,R_D^r`, lifts to an explicit `K_7`-minor model in
`G`.

## 3. The dual-free-root obstruction cannot persist

Write `B_5` for the pentagonal bipyramid

\[
                         B_5=\overline{K_2\mathbin{\dot\cup}C_5}. \tag{3.1}
\]

Its two poles are nonadjacent and complete to its five rim vertices, while
the rim induces a five-cycle.

### Theorem 3.1 (dual-free-root pentagonal-bipyramid closure)

Assume outcome 3 of Lemma 2.1 and assume that `G` has no `K_7` minor.  It
is impossible that both of the following statements hold.

1. `K-a` is a pentagonal bipyramid in which `t` is a pole and `b` is its
   unique nonneighbour.
2. `K-b` is a pentagonal bipyramid in which `t` is a pole and `a` is its
   unique nonneighbour.

Equivalently, the pole-target/auxiliary-column exception from the
seven-column response-star theorem cannot occur for both free-root choices
`a` and `b` in a `K_7`-minor-free host.

#### Proof

Suppose both statements hold.  From the first, the five response labels
`c_0,...,c_4` induce a five-cycle, and both `t` and `b` are complete to
that cycle.  From the second, `a` is complete to the same five vertices and
is nonadjacent to `t`.  Also `b` is nonadjacent to `t` by the first
statement.  Whether or not `a` and `b` contact one another, `K` therefore
contains as a subgraph the join

\[
                         I_3\vee C_5,                  \tag{3.2}
\]

where the independent three-set may be taken as `\{a,b,t\}`; if `ab` is
an edge, simply omit it from the subgraph.

Relabel the rim cyclically as

\[
                         c_0c_1c_2c_3c_4c_0.           \tag{3.3}
\]

The following five sets are branch sets of a `K_5` model in (3.2):

\[
       \{c_0\},\qquad
       \{c_1\},\qquad
       \{a\},\qquad
       \{c_2,b\},\qquad
       \{c_3,t\}.                                     \tag{3.4}
\]

The last two sets are connected because each pole is complete to the rim.
Every two displayed sets are adjacent: consecutive rim edges give
`c_0c_1` and `c_1c_2`, while any remaining required adjacency is supplied
by one of the pole-to-rim edges.  Importantly, this model avoids the rim
vertex `c_4`.

Now consume `K_{c_4}` in the construction of Lemma 2.1.  The two resulting
roots `R_C^{c_4},R_D^{c_4}` are adjacent and complete to all seven
surviving columns.  The five branch sets in (3.4) lift by taking unions of
their literal columns, and they are disjoint from the two roots.  Together
these seven connected sets form an explicit `K_7`-minor model in `G`, a
contradiction.  \(\square\)

## 4. Exact gain and trust boundary

Theorem 3.1 removes one sharply specified static obstruction.  The padded
edge and the gammoid-added edge are not committed in advance to “auxiliary
column” and “root limb” roles.  If both possible commitments make the
target a pole whose only missing contact is the other free label, the
unconsumed eight-column contact graph already contains the model in
(3.4), and a response-source limb unused by that model can instead be
consumed to form the two roots.

The theorem deliberately makes no stronger claim.

- One of `K-a,K-b` can have a `K_5` minor, in which case the construction is
  already terminal; but if it is `K_5`-minor-free and is not a pentagonal
  bipyramid, the seven-column structure theorem returns only a low-degree
  column.  That low-degree column need not be the target.
- The theorem does not force a clean Kempe path, split a dirty intermediate
  column, or preserve a selected response through an order-eight descent.
- It does not assert that the two free-root contact graphs are equal or
  that either one alone determines the eight-column graph.
- Consuming `c_4` is used only after the quotient `K_5` model is explicit;
  no response information is claimed to survive that terminal
  construction.

Thus the remaining contact alternatives are a genuine low-degree quotient
case, a pentagonal-bipyramid rim target with a noncontacting response
source, or a nonpersistent pole placement which must be coupled to the
other root choice.  Their dirty-path and colouring-response closures
remain open.

## 5. Dependencies

- the audited arbitrary-edge response-star theorem;
- the paired all-boundary column construction; and
- the elementary minor-model lifting rule.
