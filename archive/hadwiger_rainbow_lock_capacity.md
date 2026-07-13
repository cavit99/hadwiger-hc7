# Rainbow-core capacity in a locked Kempe shore

## 1. The exact Kempe-lock premise

Let \(f\) be the simultaneous reference colouring from the
double-operation repair theorem in
hadwiger_fixed_model_transition_gate.md.  Let \(W\) be the full
adhesion, including every protected vertex such as the apex.  Suppose
the \(C\)-shore is not repairable while \(f|_W\) is fixed, and let its
monochromatic defect edge be

\[
                         xy,\qquad f(x)=f(y)=\beta.           \tag{1.1}
\]

For \(\gamma\ne\beta\), write
\[
 K_x^\gamma,\ K_y^\gamma
\]
for the \(\{\beta,\gamma\}\)-components containing \(x,y\),
respectively.

### Lemma 1.1 (detour or two adhesion carriers)

For every \(\gamma\ne\beta\), exactly one of the following structural
alternatives holds.

1. \(K_x^\gamma=K_y^\gamma\).  There is a
   \(\{\beta,\gamma\}\)-detour joining \(x\) to \(y\).
2. \(K_x^\gamma\ne K_y^\gamma\), and both components meet \(W\).

#### Proof

If the components are distinct and, say, \(K_x^\gamma\cap W\) is
empty, the separation puts that whole component in the open
\(C\)-shore.  Switch \(\beta,\gamma\) on it.  This fixes \(W\), makes
\(x,y\) different, and repairs the defect edge without changing the
opposite operation.  That contradicts nonrepairability.  The same
argument applies to \(K_y^\gamma\).  \(\square\)

Thus nonrepairability alone does **not** imply two carriers in every
layer: a same-component detour is the other possibility.

For a colour \(\delta\), put

\[
                         n_\delta(W)=
 |\{w\in W:f(w)=\delta\}|.                                \tag{1.2}
\]

### Corollary 1.2 (two-hit inequality)

In alternative 2 of Lemma 1.1,

\[
                         n_\beta(W)+n_\gamma(W)\ge2.         \tag{1.3}
\]

#### Proof

Choose one adhesion vertex in each of the two distinct components.
They are distinct, and both have colour in \(\{\beta,\gamma\}\).
\(\square\)

Call (1.1) a **fully separated carrier lock** when alternative 2 holds
for every \(\gamma\ne\beta\).  The rest of the note gives the exact
capacity of such a lock.

### Lemma 1.3 (Kempe-layer union)

Let \(\Gamma\) be any set of colours for which alternative 2 of
Lemma 1.1 holds, and put

\[
 L_\Gamma=\bigcup_{\gamma\in\Gamma}K_x^\gamma,\qquad
 R_\Gamma=\bigcup_{\gamma\in\Gamma}K_y^\gamma.               \tag{1.4}
\]

Both unions are connected.  Exactly one of the following occurs.

1. They intersect.  Then some \(\gamma,\delta\in\Gamma\) give a
   \(\{\beta,\gamma,\delta\}\)-coloured \(x\)-to-\(y\) detour.
2. They are disjoint connected carriers, each meeting \(W\), and they
   are adjacent in the original graph through the edge \(xy\).

#### Proof

Every component in the left union contains \(x\), and every component
in the right union contains \(y\), proving connectedness.  If
\(z\in K_x^\gamma\cap K_y^\delta\), then \(z\) has colour \(\beta\)
unless \(\gamma=\delta\); the latter equality is impossible because
the two \(\gamma\)-components are distinct.  Concatenate an
\(x\)-to-\(z\) path in \(K_x^\gamma\) with a \(z\)-to-\(y\) path in
\(K_y^\delta\).  This is the claimed multicolour detour.

If the unions are disjoint, Lemma 1.1 says that each constituent
component, hence each union, meets \(W\).  The deleted defect edge
\(xy\) is an edge between the two unions in the original graph.
\(\square\)

The adhesion hits in outcome 2 are unlabelled: they may all be shadow
vertices in \(P\), and need not occupy distinct model portal classes.

## 2. A rainbow core and its shadows

Let

\[
                         W=R\mathbin{\dot\cup}P,              \tag{2.1}
\]

where \(R\) is rainbow under \(f\).  Put

\[
 h=|R|,\qquad
 C=f(R),\qquad
 p_\delta=|\{z\in P:f(z)=\delta\}|.                         \tag{2.2}
\]

Thus \(|C|=h\), and

\[
 n_\delta(W)=\mathbf1_{\delta\in C}+p_\delta.               \tag{2.3}
\]

### Theorem 2.1 (sharp shadow alternatives)

Assume a fully separated carrier lock at colour \(\beta\).

#### Case A: \(\beta\in C\)

Exactly the following capacity alternatives remain:

1. \(p_\beta\ge1\); or
2. \(p_\beta=0\) and
   \[
                         p_\gamma\ge1
                         \quad\text{for every }\gamma\notin C. \tag{2.4}
   \]

In particular, if \(h<r\), then

\[
                         |P|\ge1.                            \tag{2.5}
\]

#### Case B: \(\beta\notin C\)

Exactly the following capacity alternatives remain:

1. \(p_\beta\ge2\); or
2. \(p_\beta=1\) and
   \[
        p_\gamma\ge1
        \quad\text{for every }\gamma\notin C\cup\{\beta\};   \tag{2.6}
   \]
3. \(p_\beta=0\), and
   \[
   \begin{cases}
       p_\gamma\ge1,&\gamma\in C,\\
       p_\gamma\ge2,&\gamma\notin C\cup\{\beta\}.
   \end{cases}                                               \tag{2.7}
   \]

Consequently,

\[
                         |P|\ge\min\{2,r-h\}.                \tag{2.8}
\]

All these bounds are sharp at the level of the two-hit inequalities.

#### Proof

For every \(\gamma\ne\beta\), substitute (2.3) into (1.3):

\[
 p_\beta+p_\gamma
 \ge
 2-\mathbf1_{\beta\in C}-\mathbf1_{\gamma\in C}.             \tag{2.9}
\]

If \(\beta\in C\), (2.9) is automatic for
\(\gamma\in C-\{\beta\}\), and becomes
\[
                         p_\beta+p_\gamma\ge1
                         \quad(\gamma\notin C).
\]
This is exactly Case A.

Suppose \(\beta\notin C\).  For \(\gamma\in C\), (2.9) is
\[
                         p_\beta+p_\gamma\ge1,
\]
while for \(\gamma\notin C\cup\{\beta\}\) it is
\[
                         p_\beta+p_\gamma\ge2.
\]
Splitting according as \(p_\beta\ge2\), \(p_\beta=1\), or
\(p_\beta=0\) gives (2.6)--(2.7).

The three corresponding lower bounds on \(|P|\) are
\[
 2,\qquad
 1+(r-h-1)=r-h,\qquad
 h+2(r-h-1)=2r-h-2.
\]
Their minimum is \(\min\{2,r-h\}\), proving (2.8).

Sharpness for the inequalities is witnessed by, respectively:

* one additional \(\beta\)-shadow in Case A;
* two \(\beta\)-shadows in Case B when \(r-h\ge2\); and
* one \(\beta\)-shadow when \(r-h=1\).

The more detailed alternatives (2.4), (2.6), and (2.7) are attained by
putting exactly the stated minimum multiplicity of each colour in
\(P\).  \(\square\)

### Corollary 2.2 (no-shadow theorem)

If \(P=\varnothing\), a fully separated carrier lock is possible only
when

\[
                         h=r
 \quad\text{and}\quad
                         C=[r].                              \tag{2.10}
\]

In particular, \(P=\varnothing\) and \(h<r\) rule out a fully separated
carrier lock.

#### Proof

With no shadows, every colour has boundary multiplicity at most one.
Inequality (1.3) for all \(\gamma\ne\beta\) therefore forces both
\(\beta\) and every \(\gamma\) to occur on \(R\).  \(\square\)

This does not say that the shore becomes repairable.  It says that at
least one colour layer is a same-component detour layer.

### Corollary 2.3 (one-shadow classification)

Assume \(h<r\), \(|P|=1\), and a fully separated carrier lock.

1. If \(\beta\in C\), the sole shadow has colour \(\beta\), unless
   \(r-h=1\), in which case it may instead have the unique colour
   outside \(C\).
2. If \(\beta\notin C\), necessarily \(r-h=1\), and the sole shadow
   has colour \(\beta\).

#### Proof

In Case A of Theorem 2.1, avoiding a \(\beta\)-shadow requires one
shadow of every colour outside \(C\), possible with one vertex exactly
when \(r-h=1\).  In Case B, (2.8) makes \(r-h=1\) necessary; then
alternative 2 of Case B requires the sole vertex to have colour
\(\beta\).  \(\square\)

## 3. Forced detours when shadows are absent

The no-shadow conclusion can be sharpened without assuming a fully
separated lock.

### Theorem 3.1 (exact missing-core detour set)

Assume \(P=\varnothing\), but only the nonrepairability premise of
Lemma 1.1.

1. If \(\beta\in C\), then every colour
   \[
                         \gamma\notin C                       \tag{3.1}
   \]
   is a detour colour: \(K_x^\gamma=K_y^\gamma\).
2. If \(\beta\notin C\), then every
   \[
                         \gamma\ne\beta                       \tag{3.2}
   \]
   is a detour colour.

#### Proof

If a named layer had two distinct endpoint components, Corollary 1.2
would apply.  In case 1 its left side would be \(1+0=1\), and in case
2 it would be either \(0+1=1\) or \(0+0=0\), all below two.  Hence the
components coincide.  \(\square\)

So when \(|R|<r\), at least one actual bichromatic detour is forced.
When the defect colour is absent from the rainbow core, all \(r-1\)
layers are detour layers.

## 4. Hall-circuit specialization

Use the Hall-circuit simultaneous contraction from
hadwiger_crossed_arbitrary_minor_operations.md.  Its full adhesion is

\[
                         W=S=\{v\}\cup X\cup P,               \tag{4.1}
\]

and every reference colouring is rainbow on

\[
                         R=\{v\}\cup X.                      \tag{4.2}
\]

Since \(|X|=|I|-1\),

\[
                         h=|R|=|I|.                          \tag{4.3}
\]

### Corollary 4.1 (Hall rainbow-lock residue)

Let a nonrepairable Hall shore have defect colour \(\beta\).

1. If \(P=\varnothing\) and \(|I|<r\), the shore has a
   same-component bichromatic detour.  More precisely, Theorem 3.1
   gives all forced detour colours.
2. If there is no detour layer, then \(P\) must satisfy the sharp
   alternatives of Theorem 2.1 with \(h=|I|\).  In particular:
   * if \(\beta\in f(R)\), then \(P\ne\varnothing\);
   * if \(\beta\notin f(R)\), then
     \[
                         |P|\ge\min\{2,r-|I|\}.               \tag{4.4}
     \]
3. If \(P=\varnothing\) and \(|I|=r\), capacity alone permits a fully
   separated lock: the rainbow core already contains every palette
   colour.

Thus the exact portal-state residue is:

\[
\boxed{
\begin{array}{c}
\text{a bichromatic detour layer;}\\
\text{or a repeated defect-colour shadow in }P;\\
\text{or all missing core colours are represented in }P
\text{ with the multiplicities of (2.4), (2.6), (2.7);}\\
\text{or the circuit core itself uses all }r\text{ colours.}
\end{array}}
\tag{4.5}
\]

This is a genuine capacity theorem on actual adhesion vertices.  It
does not assert that a shadow vertex lies in a prescribed model portal
class.  Converting colour multiplicity on \(P\) into label-distributed
portals remains a separate matching/splitting step.

## 5. Audit boundary

The statement

> “nonrepairable implies two distinct endpoint components in every
> colour layer”

is false without an additional no-detour hypothesis.  Nonrepairability
also occurs when the endpoints lie in one Kempe component, because a
single component switch cannot separate them.  Theorems 2.1 and 2.2
therefore concern the fully separated carrier residue; Theorem 3.1
records exactly what happens when its capacity fails.
