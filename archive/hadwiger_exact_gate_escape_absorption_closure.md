# Label-escape absorption closes the exact multicomponent two-gate cell

> **Status correction.**  The absorption move in Lemma 2.1 is valid, but
> the original formulation below combined it with a global
> contact-maximal/nontrivial-circuit potential.  Those hypotheses cannot
> coexist: at a globally contact-maximal model every uncontacted singleton
> is already nonlinkable.  Therefore this note must not be cited as a
> direct proof of a \(K_{r+1}\)-minor.  The correct nonvacuous statement is
> the local trichotomy in `hadwiger_root_free_bag_saturation.md`: absorbing
> the first external neighbour of \(B\) gives contact augmentation, a
> smaller Hall circuit, or a strict same-coordinate enlargement of
> \(B\).  In particular it eliminates the source-tight branch only modulo
> those explicit descent outcomes.  Sections 1--3 are retained below to
> document the branch-set check, but their former target-minor conclusion
> is superseded by that correction.

> **Status correction (12 July 2026).** Lemma 2.1 is a valid
> labelled-model improvement, but the global normalization in Section 1 is
> incompatible with a Hall circuit of order greater than one. In a globally
> contact-maximal model, every linkable singleton uncontacted bag would
> augment contact, whereas a nontrivial circuit makes all singleton proper
> subsets linkable. Consequently Theorem 3.1 does **not** prove a
> (K_{r+1})-minor. Its valid content is a descent/exit: more contact, a
> smaller circuit, or a larger accessible bag within a comparison class in
> which that circuit persists. The resulting exit cell remains open.

## 1. Setting and potential

Use the notation of
`hadwiger_exact_gate_omitted_bag_absorption.md` and
`hadwiger_source_tight_two_gate_web.md`.  Thus

\[
 |X|=r-2,\qquad Y=\{y_1,y_2\},\qquad |P|=|I|=r-1,
\]

the accessible bag is \(B\), the bags \((B_j:j\in I)\) are the
uncontacted deficient bags, and there are at least two components of
\(U-Y\).  Every such component has exact neighbourhood \(Y\cup P\).

Choose the labelled model and its Hall circuit lexicographically as in
Section 5 of `hadwiger_exact_gate_omitted_bag_absorption.md`:

1. maximize the number of contacted model bags;
2. subject to that, minimize the order of an inclusion-minimal
   nonlinkable family of uncontacted labels; and
3. subject to those choices, maximize \(|B|\).

Here the optimization ranges over **all** labelled \(K_r\)-models with
the globally maximum contact count, and over all Hall circuits in their
uncontacted labels.  It is not restricted to models which still display
the exact source-tight decomposition.  In the present cell the unique
contacted bag is the distinguished bag \(B\), so the last coordinate is
unambiguous.  This global domain is essential: after an improving move we
only need another labelled model with the same contact count and circuit
order; we do not need the old sets \(U,Y,P\) to remain canonical for that
new model.

The set

\[
 F=V(G-v)-\bigl(Q\cup U\cup X\bigr)
\tag{1.1}
\]

contains no neighbour of \(v\).  Indeed, all neighbours of \(v\)
outside the old model are \(R=X\mathbin{\dot\cup}Y\), and
\(Y\subseteq U\).

For a dead portal \(p\), recall that \(L(p)=\varnothing\).  A far
escape from \(K_p\) starts in \(K_p-p\), has all internal vertices in
\(F\), and ends at its first vertex of \(Q-K_p\).  It is a
\(B\)-bypass if that last vertex lies in \(B-K_p\), and a label escape
if it lies in a deficient bag.

Lemma 5.2 of the omitted-bag note excludes a \(B\)-bypass.  The same
potential excludes the other endpoint type as well.

## 2. The missing absorption move

### Lemma 2.1 (a label escape is a strict model move)

At the potential choice above, no dead private region has a label
escape.

#### Proof

Suppose that

\[
 T=t_0t_1\ldots t_m
\]

is a label escape from \(K_p\), with

\[
 t_0\in K_p-p,\qquad t_m\in B_b,
 \qquad t_1,\ldots,t_{m-1}\in F.
\tag{2.1}
\]

By the first-hit definition, no internal vertex of \(T\) belongs to an
old model bag.  Put

\[
 B^+=B\cup\{t_1,\ldots,t_{m-1}\}.
\tag{2.2}
\]

The set \(B^+\) is connected, because \(t_0\in B\) and the displayed
initial segment of \(T\) joins every added vertex to \(B\).  It is
disjoint from every \(B_j\), since the endpoint \(t_m\in B_b\) was
not added and the internal vertices are outside \(Q\).  Enlarging
\(B\) only retains old interbag edges, so

\[
       (B^+,B_1,\ldots,B_{r-1})
\tag{2.3}
\]

is again a labelled \(K_r\)-model.  In fact the last edge
\(t_{m-1}t_m\) is merely an additional \(B^+B_b\)-edge.

The added vertices lie in \(F\), which is disjoint from \(N(v)\) by
(1.1).  Hence (2.3) contacts exactly the same model bags as the old
model.  The label set \(I\) is still the same set of uncontacted bags.

It cannot be fully linkable relative to the new model: absorbing such a
linkage into the bags indexed by \(I\) would produce a labelled clique
model with more contacted bags, contrary to the first coordinate of the
potential.  Choose an inclusion-minimal nonlinkable set
\(J\subseteq I\) for (2.3).  It is a Hall circuit.  Minimality of the
second potential coordinate gives

\[
                         |J|\ge |I|.
\]

Since \(J\subseteq I\), this forces \(J=I\).  Thus (2.3), together
with the same circuit \(I\), is admissible for the third potential
coordinate.

Finally, \(m\ge2\).  If \(m=1\), the edge \(t_0t_m\) would put
\(t_0\in A_b\cap K_p\), contrary to \(L(p)=\varnothing\).  Therefore
at least one internal vertex is added in (2.2), and

\[
                         |B^+|>|B|,
\]

contrary to the last potential coordinate.  This proves the lemma.
\(\square\)

### Audit note

The endpoint \(t_m\) must not be absorbed.  Keeping it in \(B_b\)
is what preserves disjointness of the labelled model.  No far Hall
certificate is selected in this argument, so intersections between
\(T\) and omitted-label certificates are irrelevant.  They were an
artefact of trying to use \(T\) directly as a target-minor carrier
rather than first applying the model potential.

## 3. Conditional descent

### Theorem 3.1 (exact multicomponent source-tight descent)

Within a comparison class for which the first two potential coordinates
are meaningful and fixed, the exact source-tight cell

\[
 |P|=r-1,\qquad c(U-Y)\ge2
\tag{3.1}
\]

has no terminal representative. Before making the potential choice, the
valid conclusion is at least one of

1. a \(K_{r+1}\)-minor;
2. a model with more contacted bags; or
3. a Hall circuit of strictly smaller order; or
4. a labelled model with the same contact and circuit coordinates and a
   strictly larger accessible bag.

Iteration of outcome 4 is finite, but it may leave the exact source-tight
description. The status correction at the top explains why this does not
by itself close every exit cell.

#### Proof

Assume that the target, contact-augmentation, and smaller-circuit
outcomes have all been excluded and use the lexicographically selected
model.

Corollary 2.2 of `hadwiger_exact_gate_omitted_bag_absorption.md` gives
at least

\[
                    \left\lceil\frac{r-1}{2}\right\rceil
\tag{3.2}
\]

dead private regions.  Choose one, say \(K_p\).

If \(K_p=\{p\}\), Lemma 5.4 of that note gives a strict root-hub
model improvement, contradicting the potential.  Thus \(K_p\) is
nontrivial.  Lemma 5.1 of that note then supplies a far escape from
\(K_p\).  If it ends in \(B-K_p\), it is a \(B\)-bypass, excluded by
Lemma 5.2 there.  If it ends in a deficient bag, it is a label escape,
excluded by Lemma 2.1 above.  These are all possible first-hit endpoints
in \(Q-K_p\), a contradiction.

Hence no representative of (3.1) is terminal under these allowed moves.
\(\square\)

### Corollary 3.2 (withdrawn as a target-minor claim)

For \(r=6\), every label escape is a strict labelled-model expansion.
This removes the private-blocker pattern as a terminal representative of
a closed local comparison class. It does not prove that the eventual
higher-contact or smaller-circuit exit contains a \(K_7\)-minor.

## 4. Scope

The proof is uniform in \(r\) and does not require

* \(X\) to be a clique;
* any gate--\(X\) adjacency;
* a first-portal exact-trace carrier;
* three distinct endpoint labels; or
* synchronization of minor-operation states.

It uses the two exact web components only through the earlier
singleton-hub Lemma 5.4 and omitted-bag Corollary 2.2.  The new
label-escape absorption itself uses only the lexicographic model/circuit
potential and the fact that the escape interior is root-free and
model-free.
