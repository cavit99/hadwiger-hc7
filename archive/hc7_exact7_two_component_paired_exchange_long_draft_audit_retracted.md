# Independent audit: two-component paired-state exchange

**Verdict:** **RETRACTED as a whole-file audit.**  The main two-component
conclusion is valid and is now proved and audited in the shorter
`../results/hc7_exact7_two_component_paired_trichotomy.md`.  However, this
audit missed a defect in the long draft's auxiliary Lemma 4.2: its
`|A|=0,4` paragraph tries to expand `B_1 union B_2` as one colour block even
though the paired-state hypotheses give a literal edge between `B_1` and
`B_2`.  Those cases are impossible for the assumed proper colouring, but
the written contraction argument is invalid.  This archived audit must not
be used to certify the long draft.

Audited proof SHA-256:

```text
913c617d33a89880615e7a8ac16d09e9216dd37c04d59f7ae242d160dc16488b
```

There is one harmless expositional convention: after excluding the case in
which both rich components are singletons, relabel `C,Q` if necessary so
that `C` is nonsingleton.  All hypotheses and every subsequent construction
are symmetric under that relabelling.

## 1. Exact reflection criterion

In Lemma 1.1, each carrier plus its independent boundary pair is connected
because it contacts both literal vertices.  The three contracted bags are
pairwise adjacent through the stipulated literal edges between the three
old blocks; no adjacency between the interior carriers is needed.  Each bag
meets `c` through its assigned block.  The resulting `K_4` forces exactly
the four blocks of `Pi`, and the nonempty opposite shore makes the
contraction a proper minor.  Palette alignment and gluing are therefore
valid.

## 2. Low-complexity cases

### Cutvertex

For a component `D` of `C-z`, the open neighbourhood is contained in
`S union {z}` and separates `D` from the nonempty component `Q` (and from
the old opposite shore).  Seven-connectivity gives `|N_S(D)|>=6`.  A
second component of `C-z` lies in `E=C-D`; its six boundary contacts are
also contacts of `E`.  Thus both defects have size at most one and both
duty-availability sets have size at least two.  Two subsets of a three-set,
each of size at least two, have distinct representatives, so Lemma 1.1
applies.  Connectivity of `E` follows because it contains `z` and all
remaining components of `C-z`.

### Orders two and three

For an edge `C=xy`, minimum degree seven gives at least six literal
boundary neighbours at each endpoint, so the same representative argument
works.

For a triangle, each singleton defect has size at most two and fullness is
exactly the empty triple intersection.  If a split `x | yz` fails the
two-duty representative test, both availability sets are the same
singleton.  Hence `Delta_x` hits the other two duties and
`Delta_y intersect Delta_z` consists of exactly one literal in each of
those duties.  Since every singleton defect has size at most two, this
forces `Delta_y=Delta_z`.  Failure of all three cyclic splits then forces
all three defects equal, contradicting fullness.  Thus one split reflects.

The application of the independently audited uniform curvature theorem to
a three-connected `C`, with `Q` as the disjoint full packet, matches its
hypotheses exactly.

## 3. Two-cut and complementary lock

Let `D` be a component of `C-{x,y}`.  Two-connectivity makes every lobe
meet both poles.  Therefore `X=D+{x}` and `Y=C-X` are nonempty, connected,
disjoint, and adjacent.  The separator bound on `D` and on a second lobe
gives defect at most two for `X,Y`; fullness of `C=X union Y` makes the two
defects disjoint.

If the two availability sets have no distinct representatives, they must
both be one singleton duty.  A defect of size at most two leaves only that
duty precisely when it contains one literal from each of the other two
pairs.  Disjointness yields the complementary normalization

```text
Delta(X)={a1,a2},  Delta(Y)={t1,t2}.
```

The raw lobe `D` also has defect at most two by its own seven-separator
bound.  Since it already misses `a1,a2`, its defect is exactly that pair.
Swapping the retained pole gives `X'=D+{y}`.  If either missing label were
restored, `A(X')` would have at least two duties and hence would admit a
distinct representative with the nonempty availability set of its
complement.  Nonreflection therefore forces the same exact defect and
makes `y` miss both labels.  The symmetric argument makes `x` miss
`t1,t2`.  This justifies (3.5)--(3.6), including the word *exact*.

There can be only two lobes.  Relative to the first lobe, every other lobe
lies in a carrier missing the complementary pair and, by its raw defect
bound, misses exactly that pair.  Repeating the split with a second lobe
forces its complementary carrier to miss the first pair.  A third lobe
would then miss all four literals, contradicting its raw defect bound of
two.  Thus `C-{x,y}` consists exactly of the two named lobes `D,E`, and the
two displayed seven-boundaries are literal actual separators.

The transported-state remark is also safe: the old proper operation lies
outside `D`, even if it used old boundary vertices, so its pullback
restricts to the new closed `D`-side.  No paired-state shape is asserted on
the new boundary.

## 4. Auxiliary Kempe and synchronization lemmas

The diagonal Kempe swap exchanges both terminals in one diagonal and none
in the other, producing exactly `P|bar P|B3|c`; the three displayed rich
bags form the required `K_4`.  The enumeration in Lemma 4.2 exhausts the
block sizes `0/4`, `1/3`, and `2/2`; only the original and crossed
matchings survive.  Taking one Kempe-component trace at a time then leaves
only the trace `U` or the two traces `P,bar P`.

Lemma 5.1 is the separately audited multishore synchronization mechanism.
Its application is conditional on both complementary defect pairs being
independent and correctly proves that at least one must instead be edged.
Lemma 6.1 assigns the two post-swap colour blocks to the complementary
lobe carriers and the unchanged block to `Q`; all three meet `c`, so its
Kempe-component conclusion is valid.  These auxiliary locks are not needed
for the final handoff, but they introduce no uncovered branch.

## 5. Near-model handoff and exhaustion

The seven bags in (7.1) are exactly those checked in the independent audit
of `hc7_exact7_complementary_lock_near_k7_handoff.md`.  They are spanning,
and every pair is adjacent except at most `sc,sr`.  The both-missing and
one-hole trichotomies therefore return `K_7`, an actual separator, or a
labelled rotation to a proper connected part of one of the four neutral
bags.  This is an `S1` handoff, not a claim that rotations terminate.

Finally, the cases are exhaustive.  If both rich components are
singletons, deletion of one and copying the other twin's colour directly
six-colours `G`.  Otherwise choose a nonsingleton component as `C`.  A
cutvertex, order two/three, or three-connectivity reflects.  Every remaining
connected graph is two-connected but not three-connected and therefore has
a two-cut; that cut either reflects by Lemma 1.1 or is the exact
complementary lock just handed to `S1`.  No two-component paired-state case
is left outside the stated trichotomy.

## Scope

This theorem closes the two-*component* rich shore for an already attained
paired-triangle state.  It does not handle two full packets interlaced in
one rich component, packet vector `(1,1)`, arbitrary demand-three states,
or termination of the global near-model rotation/adhesion system.
