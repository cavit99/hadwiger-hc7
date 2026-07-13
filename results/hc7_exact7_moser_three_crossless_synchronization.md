# Three-crossless synchronization for Moser frames

**Status:** proved and independently audited.  The occurrence-level finite
step is certified by the exact verifier cited below.

## 1. Common-face theorem

Let `D` be embedded in a closed disk with simple facial boundary cycle `F`.
Let

\[
                         P_0,P_1,P_2,P_3,P_4\subseteq V(F)
\]

be five literal portal sets admitting five distinct representatives.  The
sets themselves may overlap.  With indices modulo five, frame `j` consists
of the two demands

\[
             P_{j+1}\longleftrightarrow P_{j+2},\qquad
             P_{j+3}\longleftrightarrow P_{j+4}.       \tag{1.1}
\]

A frame is **crossless** if there are no two vertex-disjoint connected
subgraphs of `D`, one meeting the first two portal sets and the other
meeting the last two.

### Theorem 1.1

If any three of the five frames are crossless, then all five are crossless.

### Proof

Fix a system of distinct representatives, one on `F` for each portal set.
For any crossless frame and any choice of one facial occurrence from each
of its four portal sets, the following necessary disk rule holds whenever
the two demanded pairs are cross-disjoint:

* neither demanded pair may collapse to one occurrence; and
* the four occurrences alternate on `F`.

Indeed, a collapsed pair is a singleton support disjoint from a suitable
facial arc for the other pair.  Four distinct nonalternating occurrences
give two disjoint facial arcs realizing the two demands.

Applied to the five representatives, the three crossless-frame constraints
leave only the pentagram circular order

\[
                         0,2,4,1,3                    \tag{1.2}
\]

and its reverse, up to rotation.  This is the complete 24-order check in
`../archive/moser_c5_crossless_order_probe.py`.

Suppose a fourth frame has two disjoint connected supports.  Choose one
facial occurrence of each demanded portal label from those supports.
Occurrences belonging to one support may coincide, but occurrences in the
two disjoint supports cannot.  Together with the five fixed
representatives these give at most nine occurrences on `F`.  For each of
the original three crossless frames impose the disk rule above for every
choice among these occurrences.  Disjoint supports additionally require
either a within-support collapse or, when all four support occurrences are
distinct, a nonalternating order.

There are ten choices of the three crossless frames, two pentagram
orientations, and two candidate remaining frames.  The exact weak-order
verifier
`../archive/moser_c5_three_crossless_exact_probe.py` constructs all forty
systems, permits every coincidence not forbidden by genuine disjointness,
and returns

```text
checked 40 satisfiable 0
```

Every disk configuration induces one of those weak circular orders, so the
proposed fourth frame cannot be linked.  The same applies to the fifth
frame. `square`

## 2. Three-connected pure-Moser shore

Consider a three-connected relative shore `D` with seven literal boundary
labels, satisfying the full-attachment and relative seven-cut inequality
used in the Moser cell.  Let the five portal sets correspond to the five
unique roots of the exact `13` trace.

The Hall-deficiency argument gives five distinct portal representatives:
if a subfamily `I` had fewer than `|I|` portal vertices, a component left
after deleting them would have at most

\[
                         (|I|-1)+(7-|I|)=6
\]

external neighbours; if no component remained, the shore would have order
at most four.  Both contradict the installed hypotheses.

For a crossless frame, the relative Two Paths theorem and the relative
cut inequality give a bare-web embedding with all four full portal sets on
one face.  If three frames are crossless, Whitney uniqueness identifies
their embeddings.  Two distinct faces of a three-connected plane graph
cannot share the three distinct representatives belonging to the three
portal labels shared by two frames, so the three frame faces coincide.
Their labels cover all five portal sets.  Theorem 1.1 therefore applies.

### Corollary 2.1 (bilateral frame synchronization)

Each three-connected pure-Moser shore is either crossless for all five
frames or crossed for at least three.  Consequently, two such shores which
are not all-crossless have a common crossed frame.

### Proof

If a shore had at least three crossless frames, Theorem 1.1 would make all
five crossless.  Otherwise at least three are crossed.  Two subsets of a
five-set of order at least three intersect. `square`

## 3. Scope

The theorem removes bilateral drift between two non-all-web
three-connected shores.  It does not apply to merely two-connected shores
with frame-dependent facial embeddings, and it does not eliminate the
one-sided case in which exactly one shore is all-crossless.  Nor does a
common crossed frame by itself synchronize the extra `w` decoration; that
step is supplied only under the hypotheses of the audited decorated-state
exchange theorem.
