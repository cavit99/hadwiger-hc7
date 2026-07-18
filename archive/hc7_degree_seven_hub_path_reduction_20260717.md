# Degree-seven common-end path reduction

**Status:** written draft; not yet independently audited.  This note proves
an explicit reduction in the degree-seven branch of the bounded-interface
programme.  It does not prove `HC_7`: its terminal residual is a genuine
two-disjoint-connected-subgraphs problem inside one exterior component.

## 1. Setup

Let `G` be a seven-connected graph with no `K_7` minor.  Let `u` have
degree seven, assume `G-N[u]` is nonempty, and put

\[
                         S=N_G(u),
\]

and assume

\[
                         \alpha(G[S])\le2.              \tag{1.1}
\]

Suppose there are distinct vertices

\[
              y,q_1,q_2,q_3,q_4,r,s\in S              \tag{1.2}
\]

such that `yq_i` is a nonedge for every `i`.  This is the common-end
alternative obtained when four returned nonedges have no two disjoint
members.

Write `Q={q_1,q_2,q_3,q_4}` and let the **exterior components** be the
components of `G-N[u]`.  Every exterior component has neighbourhood
exactly `S`: its neighbourhood is contained in `S`, has order at least
seven by seven-connectivity, and `|S|=7`.

## 2. The boundary four-clique and uniqueness of the exterior component

### Lemma 2.1

The set `Q` is a clique.  If neither `r` nor `s` is complete to `Q`, then
`yr,ys` are edges.

#### Proof

Two nonadjacent members of `Q`, together with `y`, would be an independent
set of order three, contrary to (1.1).  Thus `Q` is a clique.

If, for example, `yr` were a nonedge, then every `q_i` would have to be
adjacent to `r`, since otherwise `y,r,q_i` would be independent.  Thus
`r` would be complete to `Q`.  The assertion for `s` is symmetric.
\(\square\)

### Lemma 2.2 (two exterior components close)

There is exactly one exterior component.

#### Proof

There is at least one by hypothesis.  Suppose that `C,D` are two distinct exterior components.  The
following seven sets are pairwise disjoint and connected:

\[
 \{q_1\},\ldots,\{q_4\},\qquad
 \{u,y\},\qquad C,\qquad D\cup\{r\}.                  \tag{2.1}
\]

The first four are pairwise adjacent by Lemma 2.1.  The set `C` is
adjacent to each `q_i`, to `y`, and to `r`, because it is full to `S`.
The same is true of `D`.  Hence `C` is adjacent to `D union {r}` through
an edge from `C` to `r`.  The set `{u,y}` is adjacent to the four
singletons through `u`, to `C` through `y`, and to `D union {r}` through
the edge `ur`.  Finally `D union {r}` is adjacent to every `q_i` through
`D`.  Thus (2.1) is a `K_7`-minor model, a contradiction.  \(\square\)

Denote the unique exterior component by `C`.  In particular, every
neighbour of `y` outside `N[u]` lies in `C`.  Since `y` has at most two
neighbours in `S`, minimum degree seven gives at least four distinct
neighbours of `y` in `C`.

## 3. Exact connected-subgraph criterion

For `a in {r,s}`, define its missing boundary labels

\[
                    I_a=\{q\in Q:aq\notin E(G)\}.       \tag{3.1}
\]

### Lemma 3.1 (one connector and one repair subgraph)

Suppose there are disjoint connected subgraphs `T,D` of `G[C]` such that

1. `T` has a neighbour at `y` and at every vertex of `Q`;
2. for some `a in {r,s}`, `D` has a neighbour at `a` and at every member
   of `I_a`; and
3. there is a `T-D` edge.

Then `G` has a `K_7` minor.

#### Proof

Use the seven branch sets

\[
  \{q_1\},\ldots,\{q_4\},\qquad
  \{u\},\qquad \{y\}\cup T,\qquad \{a\}\cup D.       \tag{3.2}
\]

The four `Q`-singletons form a clique.  The singleton `{u}` is adjacent
to all six other branch sets.  The last two sets are connected and are
adjacent by the `T-D` edge.  The set `{y} union T` is adjacent to every
`Q`-singleton by the selected contacts of `T`.  If `q notin I_a`, the
edge `aq` joins `{a} union D` to `{q}`; if `q in I_a`, the selected
`D-q` edge does so.  Hence (3.2) is a `K_7`-minor model.  \(\square\)

### Corollary 3.2

Both `I_r` and `I_s` are nonempty.

#### Proof

Suppose `I_r` is empty.  Since `C` is connected and full to
`Q union {y,r}`, it contains a connected subgraph `T` meeting all six
corresponding portal sets.  Then

\[
 \{q_1\},\ldots,\{q_4\},\{u\},\{y\}\cup T,\{r\}
\]

is the model (3.2), with the last two branch sets adjacent through the
selected `r-T` edge.  The case `I_s=emptyset` is symmetric.
\(\square\)

## 4. What the four common-end paths provide

Assume now that for every `i` there is a `y-q_i` path whose internal
vertices lie in `C`.  This is exactly the information supplied when the
four failed Kempe lifts have the common end `y` and all lie in the same
open shore.

The four path interiors provide one portal in `C` for each required end.
Since `C` is connected, their union can be joined inside `C` to a connected
subgraph `T` having a neighbour at `y` and at every member of `Q`.  Choose
`T` inclusion-minimal with this property.  Its selected edge set may be
taken to be a tree; no assertion is made that `G[V(T)]` is induced.

By Lemma 3.1, the branch closes whenever one component `D` of `C-V(T)`
is adjacent to `T` and its boundary contacts include

\[
                        \{a\}\cup I_a                 \tag{4.1}
\]

for one of `a=r,s`.

There is also an exact separator alternative which must be retained.  For
every component `D` of `C-V(T)`, put

\[
 d(D)=|S-N_S(D)|,\qquad a(D)=|N_T(D)|.                 \tag{4.2}
\]

There are no edges from `D` to another component of `C-V(T)` or outside
`C union S`, so

\[
 |N_G(D)|=|N_S(D)|+|N_T(D)|=7-d(D)+a(D).               \tag{4.3}
\]

Seven-connectivity gives `a(D)>=d(D)`.  This yields the following exact
trichotomy.

1. If `d(D)=0`, then `D` is `S`-full.  It satisfies (4.1) for either row,
   and Lemma 3.1 gives a `K_7` minor.
2. If `d(D)>0` and `a(D)=d(D)`, then `N_G(D)` has order exactly seven and
   the `D`-side is strictly smaller than `C`.  The opposite side is also
   full: a boundary vertex having no neighbour there would make the other
   six boundary vertices a cut.
3. Otherwise `d(D)>0` and `a(D)>=d(D)+1`.

Thus a surviving common-end configuration has the following concrete
form:

* `C` is the unique exterior component;
* `I_r,I_s` are both nonempty;
* no component of `C-V(T)` satisfies (4.1) for either row; and
* every component of `C-V(T)` misses at least one boundary label and has
  strictly more attachments to `T` than the number of boundary labels it
  misses.

If `C=V(T)`, the last two conditions are vacuous and the whole exterior is
the minimal connector.  Otherwise the last alternative is a stable-bridge obstruction around the one
minimal five-terminal connector `T`.  It is substantially narrower than
the original four unrelated paths, but it is not a contradiction.

## 5. Exact limitation and next useful hypothesis

Seven-connectivity and fullness do not, by themselves, turn the four
paths into two labelled connected branch sets.  After Lemma 2.2 the
missing assertion is a two-disjoint-Steiner-subgraph statement in `C`.
Such a statement needs the literal attachment sets (or a proper-minor
colour response); it cannot be inferred from the existence of the four
paths alone.

A weakest directly useful extra hypothesis is precisely the existence of
the component `D` in (4.1).  A more structural theorem useful for the
programme would say that, for an inclusion-minimal `T`, the strict
attachment-surplus outcome cannot hold for every residual component (and
that `T` cannot span `C`) once the proper-minor colour responses on the
edges of `T` are imposed.  The equality case already returns an
**exact-seven**, two-sided-full neighbourhood; preservation of the named
edge-deletion response remains to be proved.  Proving the stronger dichotomy would close
the common-end same-shore branch by Lemma 3.1 and finite descent.  The unresolved
high-attachment alternative above shows exactly what such a theorem must
eliminate, using `K_7`-minor-freeness or contraction-critical colourings.

## 6. The proper-minor information left after uniqueness

There is one further simplification in a hypothetical minor-minimal
counterexample.  Since `C` is the unique component of `G-N[u]`,

\[
                         G-C=G[N[u]].                  \tag{6.1}
\]

Thus a boundary colouring extends through the opposite closed shore
exactly when it uses at most five colours on `S`: give `u` a sixth colour.

Let `e=vw` be any edge of `G[C]`, and let `phi` be a six-colouring of the
proper minor `G-e`.  Then:

1. `phi(v)=phi(w)`, since otherwise `phi` would colour `G`;
2. `phi|S` uses at most five colours and therefore extends through
   `G[N[u]]`;
3. the equality partition of `phi|S` does not extend through the original
   `C`-shore, since such an extension would glue to `phi|G[N[u]]`; and
4. each of `v,w` has a neighbour in every colour other than its own,
   since recolouring an endpoint with a missing colour would make the edge
   `e` proper and six-colour `G`; and
5. for every other colour `beta`, the vertices `v,w` lie in the same
   two-colour component on their common colour and `beta`.  Otherwise a
   Kempe interchange on the component containing `v` would separate their
   colours and again colour the restored graph.

Consequently the surviving stable-bridge obstruction is not an arbitrary
two-Steiner instance.  Every internal edge of `C` is critical relative to
an explicitly opposite-shore-compatible boundary colouring.  This is the
extra hypothesis that a positive splitting theorem should spend: an
edge of the minimal connector `T` supplies a compatible boundary response,
and failure to change its repeated endpoint colour supplies five saturated
bichromatic connections.  The unresolved step is still label-faithful:
those five colour witnesses need not first hit the prescribed `Q`-portal
classes.
