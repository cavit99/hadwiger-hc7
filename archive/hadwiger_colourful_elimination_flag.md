# Colourful elimination flags

## Status

This note isolates a uniform recursive structure carried by every
inclusion-minimal colour-saturating set.  The construction is elementary
and exact.  The proposed flag-packaging step is **false**, already for a
fully explicit flag of order four.  See
`hadwiger_colourful_elimination_flag_counterexample.md`.  The failure is
a crossed pair of root connectors forced through one bottleneck vertex;
thus the entire nested descent does not by itself provide the disjoint
reserved connectors needed by a rooted clique model.

Throughout, a set (X\subseteq V(H)) is **(k)-colourful** if (H) is
(k)-colourable and every proper (k)-colouring of (H) uses all (k)
colours on (X).

## 1. Removing a private colour preserves colourfulness

### Lemma 1.1 (private-colour descent)

Let (X) be (k)-colourful in (H), and let (c) be a proper
(k)-colouring.  Suppose a colour (alpha) occurs on (X) exactly at
one vertex (x).  Put

\[
 A=c^{-1}(\alpha),\qquad H'=H-A,\qquad X'=X-\{x\}.
\]

Then (X') is ((k-1))-colourful in (H').  In particular,
(chi(H')=k-1).

#### Proof

The restriction of (c) shows that (H') is ((k-1))-colourable.
Suppose a proper colouring of (H') from the palette
([k]-\{\alpha\}) omitted a colour (gamma) on (X').  Keep that
colouring on (H') and give every vertex of the independent colour class
(A) colour (alpha).  This is a proper (k)-colouring of (H).  On
(X), the colour (alpha) occurs at (x), while (gamma) is absent,
contrary to the (k)-colourfulness of (X).  Hence (X') is
((k-1))-colourful.  A graph containing a ((k-1))-colourful set cannot
be coloured with fewer than (k-1) colours, proving the last assertion.
(square)

### Lemma 1.2 (private witnesses in a minimal colourful set)

If (X) is inclusion-minimal (k)-colourful, then for every (x\in X)
there is a proper (k)-colouring (c_x) and a colour (alpha_x) whose
trace on (X) is exactly ({x}).

#### Proof

The set (X-\{x\}) is not (k)-colourful, so some proper
(k)-colouring omits a colour (alpha_x) there.  Since (X) itself is
colourful, (x) has colour (alpha_x), and it is the unique such vertex
of (X). (square)

## 2. The nested flag

### Theorem 2.1 (colourful elimination flag)

Let (X_k) be an inclusion-minimal (k)-colourful set in (H_k).  There
exist induced subgraphs

\[
 H_1\subset H_2\subset\cdots\subset H_k,
\]

sets (X_i\subseteq V(H_i)), independent layers (A_i), distinguished
vertices (x_i\in X_i\cap A_i), and proper (i)-colourings (c_i) of
(H_i), for (i=k,k-1,\ldots,2), such that

1. (X_i) is inclusion-minimal (i)-colourful in (H_i);
2. (A_i) is one colour class of (c_i);
3. (A_i\cap X_i=\{x_i\});
4. (H_{i-1}=H_i-A_i); and
5. (X_{i-1}) is an inclusion-minimal ((i-1))-colourful subset of
   (X_i-\{x_i\}) in (H_{i-1}).

At the final step (H_1) has a nonempty one-colourful set (X_1); choose
(x_1\in X_1).  Thus the flag supplies (k) distinct roots
(x_1,\ldots,x_k) in pairwise disjoint independent layers.

#### Proof

Starting with ((H_k,X_k)), apply Lemma 1.2 to any (x_i\in X_i), and
let (A_i) be its private colour class.  Lemma 1.1 makes
(X_i-\{x_i\}) ((i-1))-colourful in (H_i-A_i).  Choose an
inclusion-minimal colourful subset there and continue.  Each later graph
is obtained by deleting the previous independent layer, so the layers
and distinguished roots are disjoint.  The process terminates at one
colour. (square)

## 3. The exact Kempe information at one descent

### Lemma 3.1 (private root sees every other boundary colour by a Kempe
component)

In the setting of Lemma 1.1, for every colour
(eta\ne\alpha), the ((\alpha,\beta))-component of (H) containing
(x) contains a vertex of (X) coloured (eta).

#### Proof

Otherwise interchange (alpha) and (eta) on that component.  The
unique (alpha)-vertex (x) of (X) ceases to have colour (alpha),
and no (eta)-coloured vertex of (X) changes to (alpha).  Thus the
new proper (k)-colouring omits (alpha) on (X), a contradiction.
(square)

For vertex-disjoint pairs of palette colours, the corresponding
bichromatic subgraphs are vertex-disjoint.  Hence any matching of colour
pairs has mutually disjoint Kempe repair paths.  What is not automatic is
that the endpoint selected in a current Kempe component is one of the
distinguished roots selected at a later descent.

## 4. Candidate uniform rooted principle and equivalence risk

The following natural target is now refuted:

> **Flag-packaging principle.**  Every colourful elimination flag of
> order (k) has a (K_k)-model whose (i)-th bag contains (x_i).

This would imply Holroyd's Strong Hadwiger statement and hence ordinary
Hadwiger: every colourful set contains an inclusion-minimal one, Theorem
2.1 produces a flag, and the resulting rooted model meets the original
set in every bag.

The principle would be theorem-strength, but it is not true.  Its extra
input over ordinary Kempe packaging is the *nested
private-colour descent*: after removing the whole current private colour
class, the residual boundary remains colourful for one fewer colour.
Any proof must use this nesting.  Pairwise Kempe connectivity alone is
known to be insufficient in the relevant range.

The explicit order-four construction in the counterexample note settles
the falsification target: it preserves every private-colour descent but
has no rooted clique model at the distinguished roots.  Consequently a
usable replacement must include a separator/capacity alternative or allow
the roots to be reselected.

The formerly proposed targets were:

1. Prove a reserved-connector induction: when the order-((i-1)) model is
   built in (H_i-A_i), leave a connected (x_i)-carrier through
   (A_i) adjacent to every old bag.
2. Construct a colourful elimination flag whose distinguished roots have
   no rooted clique model.  Such a construction must preserve every
   private-colour descent, not merely one fixed Kempe colouring.
