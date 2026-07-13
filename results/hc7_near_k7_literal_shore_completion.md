# Literal shore completions in a coherent near-`K_7` carrier

## Status

This note records the exact label-preserving terminal output required
from a bridge/society recursion after coherent spanning transport.  Both
alternatives are elementary but important: they prevent an unlabelled
cross or a split with the wrong row contacts from being counted as
progress.

## Setting

Let

\[
                 A,B,C,U_1,U_2,U_3,U_4
\]

be pairwise disjoint connected sets.  The six foreign bags
`B,C,U_1,...,U_4` are pairwise adjacent, and `A` is adjacent to every
`U_i`.  No adjacency from `A` to `B` or `C` is initially assumed.

### Theorem 0 (uniform missing-star shore completion)

Let `t>=3`.  Let `V_1,...,V_{t-1}` be pairwise disjoint connected
pairwise adjacent foreign bags, and let `A` be a disjoint connected
carrier.  Suppose exactly `m>=0` of the foreign bags are anticomplete to
`A`.  If `A` contains `m+1` pairwise disjoint connected pairwise adjacent
sets `X_0,...,X_m`, and every `X_j` is adjacent to every one of the
`t-1-m` foreign bags which meets `A`, then `G` contains a `K_t` minor.

#### Proof

Use the `m+1` bags `X_j` and the `t-1-m` contacted foreign bags.  They
are disjoint and connected.  Each family is a clique model, and every
cross-pair is adjacent by hypothesis.  Their total number is

\[
                       (m+1)+(t-1-m)=t.
\]

They form a `K_t` model.  \(\square\)

Thus coherent transport of a missing star has an exact uniform terminal
target: the number of required carrier shores is one more than the number
of globally missing spokes.

### Lemma 1 (one-missing two-shore completion)

Suppose `A` is adjacent to one of `B,C`; call that bag `E`, and call the
other twin `D`.  If there are disjoint connected sets `X,Y subseteq A`
such that

1. `X` and `Y` are adjacent;
2. each of `X,Y` is adjacent to `E`; and
3. each of `X,Y` is adjacent to every `U_i`,

then `G` contains a `K_7` minor.

#### Proof

The seven branch sets are

\[
            X,\quad Y,\quad E,\quad U_1,U_2,U_3,U_4. \tag{1.1}
\]

The five retained foreign bags are pairwise adjacent.  Both `X,Y` meet
every one of them and meet each other.  Thus all seven sets in (1.1) are
connected, disjoint and pairwise adjacent.
\(\square\)

### Lemma 2 (both-missing three-shore completion)

Suppose `A` is anticomplete to both `B` and `C`.  If there are three
pairwise disjoint connected sets `X_1,X_2,X_3 subseteq A` such that

1. the `X_j` are pairwise adjacent; and
2. every `X_j` is adjacent to every `U_i`,

then `G` contains a `K_7` minor.

#### Proof

Use the seven branch sets

\[
                         X_1,X_2,X_3,U_1,U_2,U_3,U_4. \tag{1.2}
\]

The first three form a clique model by hypothesis, the last four form a
clique model by the old foreign-bag adjacencies, and every cross-pair is
adjacent by the full four-row contact assumption.  Hence (1.2) is a
`K_7` model. \(\square\)

## Path-bridge specialization

Assume the normalized core of `A` is the path

\[
                   P=p_0p_1\cdots p_m,
\]

where `p_0` is the sole old portal to `U_1,U_2` and `p_m` is the sole
old portal to `U_3,U_4`.  In the coherent spanning carrier, every added
piece is an old exterior component meeting `P`, and different pieces
are mutually anticomplete.

For a piece `K`, let its span be the interval from its first to its last
attachment on `P`, and let

\[
 \sigma(K)=\{F\in\{B,C,U_1,U_2,U_3,U_4\}:E(K,F)\ne\varnothing\}.
\]

Fix a path edge `p_jp_{j+1}`.  A family of pieces **crosses the cut** if
every member has an attachment in each of

\[
 L=\{p_0,\ldots,p_j\},\qquad
 R=\{p_{j+1},\ldots,p_m\}.
\]

In the one-missing branch, Lemma 1 applies whenever two disjoint
families `mathcal L,mathcal R` of cut-crossing pieces satisfy

\[
 \{E,U_3,U_4\}\subseteq\bigcup_{K\in\mathcal L}\sigma(K),\qquad
 \{E,U_1,U_2\}\subseteq\bigcup_{K\in\mathcal R}\sigma(K). \tag{1.3}
\]

Indeed take

\[
 X=L\cup\bigcup\mathcal L,\qquad
 Y=R\cup\bigcup\mathcal R.
\]

Each set is connected because every assigned piece attaches to its side
of `P`; they are disjoint and adjacent through `p_jp_{j+1}`.  Their old
endpoint contacts plus (1.3) give all five required rows.  Unused pieces
are simply omitted from the minor model.

Thus the target-free residue at a cut is an exact two-bin set-packing
failure: the crossing pieces cannot be divided into a left family
covering `{E,U_3,U_4}` and a disjoint right family covering
`{E,U_1,U_2}`.  This is the capacity state to which a bridge-overlap or
web theorem must respond.  Merely finding two crossing paths, with no
literal row supports, is insufficient.

For the both-missing branch the corresponding target is not (1.3): one
must extract three pairwise adjacent connected shores, each seeing all
four neutral rows, exactly as in Lemma 2.  This branch must not be
silently folded into the two-shore state.

## Exact finite dual of the two-shore capacity state

At a fixed path cut, let `mathcal K` be the set of pieces crossing the
cut.  Write

\[
 L_1=E,\quad L_2=U_3,\quad L_3=U_4,
 \qquad
 R_1=E,\quad R_2=U_1,\quad R_3=U_2,
\]

where the letters `L,R` record the shore which still needs that row.
For a demand `Q`, put

\[
             N(Q)=\{K\in\mathcal K:Q\in\sigma(K)\}.
\]

### Lemma 3 (three-piece capacity dual)

The two disjoint covering families in (1.3) exist if and only if there
are representatives

\[
                  k_i\in N(L_i)\qquad(1\le i\le3)       \tag{1.4}
\]

(not necessarily distinct) such that

\[
                  N(R_j)\nsubseteq\{k_1,k_2,k_3\}
                         \qquad(1\le j\le3).             \tag{1.5}
\]

Consequently, if the capacity state fails, then for every left
representative triple some right demand has all of its crossing support
concentrated in at most three pieces.  The symmetric assertion also
holds.  In particular, if every one of the six demand sets has order at
least four, the literal two-shore completion exists.

#### Proof

If (1.4)--(1.5) hold, assign the set
`{k_1,k_2,k_3}` to the left shore and every other crossing piece to the
right shore.  The selected set meets every `N(L_i)` by (1.4), while its
complement meets every `N(R_j)` by (1.5).  These are the required
disjoint covering families.

Conversely, let `mathcal L,mathcal R` be disjoint covering families.
Choose `k_i in mathcal L cap N(L_i)`.  Since `mathcal R` meets every
`N(R_j)` and is disjoint from `mathcal L`, no `N(R_j)` is contained in
`{k_1,k_2,k_3}`.  This proves (1.5).

Negating the equivalence gives the concentration assertion.  If all
right demand sets have at least four members, no one of them can be
contained in a three-element representative set, so any choices in
(1.4) work.  Interchanging left and right proves the symmetric form.
\(\square\)

Lemma 3 is an exact carrier-capacity certificate.  It does not turn the
at-most-three carrier pieces into an order-at-most-three vertex cut;
each piece may be arbitrarily large.  The reserved-core bridge theorem
still has to show that such concentration yields a labelled internal
split, a faithful colour-gluable adhesion, or the same global planar
pair.

### Lemma 4 (both-missing bridge-triangle completion)

In the both-missing branch, fix a cut `L|R` of `P`.  Suppose there is a
crossing piece `K_0` adjacent to all four `U_i`, and there are disjoint
families of other crossing pieces `mathcal L,mathcal R` such that

\[
 \{U_3,U_4\}\subseteq\bigcup_{K\in\mathcal L}\sigma(K),
 \qquad
 \{U_1,U_2\}\subseteq\bigcup_{K\in\mathcal R}\sigma(K). \tag{1.6}
\]

Then `G` contains a `K_7` minor.

#### Proof

Put

\[
 X=L\cup\bigcup\mathcal L,qquad
 Y=R\cup\bigcup\mathcal R,qquad Z=K_0.
\]

As before, `X,Y` are disjoint connected sets adjacent through the path
cut edge.  They see all four neutral rows by their endpoint contacts and
(1.6).  The connected set `Z` sees all four rows by hypothesis.  Since
`K_0` crosses the cut, it has an attachment in each of `L,R`, and hence
`Z` is adjacent to both `X,Y`.  The three shores are pairwise adjacent
and each sees every `U_i`; Lemma 2 applies. \(\square\)

This identifies the additional object required in the both-missing
branch: a literal four-row bridge which serves as the third vertex of
the shore triangle.  A two-shore web theorem cannot dispose of this
branch unless it either produces that bridge or first repairs one of the
two twin contacts.
