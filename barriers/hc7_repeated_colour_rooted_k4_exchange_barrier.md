# Repeating the deficient branch-set colour does not provide a rooted `K_4` exchange

**Status:** barrier to an intermediate exchange claim; written proof;
separate internal audit GREEN.  This is not a counterexample to `HC_7`.

## 1. Claim refuted

The following proposed inference is false using only the compressed core
and its six-colour quotient response:

> Let `Q` be five-chromatic and `K_6`-minor-free, let adjacent vertices
> `z,u` have colourful neighbourhoods `S,T` in the four-chromatic graph
> `R=Q-\{z,u\}`, and choose an `S`-rooted `K_4` model maximizing the
> number of branch sets meeting `T`.  If a six-colouring after contracting
> the named model makes `u` repeat the colour of its unique deficient
> branch set, then a label-preserving exchange increases the number of
> branch sets meeting `T`.

The counterexample below retains the `K_6`-minor exclusion and has a
unique deficient branch set.  In fact, no `S`-rooted `K_4` model has four
branch sets meeting `T`, so no exchange of any kind can make the proposed
strict improvement.

## 2. The compressed core

Let `C` be the triangle on vertices `c_1,c_2,c_3`, let

\[
                              s-z-u-t                 \tag{2.1}
\]

be a four-vertex path disjoint from `C`, and put

\[
                              Q=C\vee(s-z-u-t).        \tag{2.2}
\]

Thus every vertex of `C` is adjacent to every vertex of the path.  Delete
the two internal path vertices and write

\[
       R=Q-\{z,u\}=C\vee\{s,t\},\qquad
       S=N_R(z)=C\cup\{s\},\qquad
       T=N_R(u)=C\cup\{t\}.                           \tag{2.3}
\]

### Proposition 2.1

The graph `Q` is five-chromatic and has no `K_6` minor.  The graph `R` is
four-chromatic, both `R+z` and `R+u` are five-chromatic, and both `S,T`
are colourful in `R`.

#### Proof

Chromatic number is additive under joins.  Hence

\[
                 \chi(Q)=\chi(K_3)+\chi(P_4)=3+2=5.  \tag{2.4}
\]

For completeness, if `h(H)` denotes the largest order of a complete
minor in `H`, then

\[
                         h(K_r\vee H)=r+h(H).          \tag{2.5}
\]

The lower bound is immediate.  For the reverse bound, in any complete
minor model at most `r` branch sets contain a vertex of the `K_r`; all
remaining branch sets lie in `H` and form a complete minor there.  Since
`h(P_4)=2`, equations (2.2) and (2.5) give `h(Q)=5`.  Thus `Q` has no
`K_6` minor.

The graph `R` is `K_5-st`, so it is four-chromatic.  Each of `R+z` and
`R+u` contains a `K_5`: respectively, these are
\(C\cup\{s,z\}\) and \(C\cup\{u,t\}\).  They are subgraphs of the
five-chromatic graph `Q`, so
both have chromatic number five.

Finally, each of `S,T` induces a `K_4`.  Every proper four-colouring of
`R` therefore uses all four colours on each set, so both are colourful.
\(\square\)

## 3. A maximal model with one deficient branch set

### Proposition 3.1

The four singleton branch sets

\[
        D_1=\{c_1\},\quad D_2=\{c_2\},\quad
        D_3=\{c_3\},\quad D_4=\{s\}                  \tag{3.1}
\]

form an `S`-rooted `K_4` model.  Exactly three of them meet `T`, and no
`K_4` model in `R` has every branch set meeting both `S` and `T`.
Consequently, (3.1) maximizes the number of `T`-contacting branch sets.

#### Proof

The set \(S=C\cup\{s\}\) induces a `K_4`, which proves the first
assertion.
The first three branch sets in (3.1) meet `T`, while `D_4` does not.

Suppose four pairwise disjoint branch sets formed a `K_4` model and each
met both `S` and `T`.  Since `|S|=|T|=4`, each branch set would contain
exactly one vertex of `S` and exactly one vertex of `T`.  The three common
vertices `c_1,c_2,c_3` would therefore lie in three distinct branch sets.
Every vertex of `R` belongs to \(S\cup T\), so those three branch sets
could contain neither `s` nor `t`.  The fourth branch set would have to
contain both `s` and `t`.  But `s,t` are nonadjacent, and every `s`--`t`
path in `R` uses a vertex of `C`, already belonging to one of the other
three branch sets.  The fourth branch set cannot be connected, a
contradiction.

Thus four contacts are impossible, while (3.1) has three.  It is
contact-maximal. \(\square\)

## 4. The exact repeated-colour response

Add one universal vertex `x` to `Q`.  This represents the vertex obtained
by contracting the connected dominating subgraph `X` in the star-Kempe
host.  The resulting graph is

\[
                         \widehat Q=x\vee Q=K_4\vee P_4,             \tag{4.1}
\]

where the complete factor is `\{x,c_1,c_2,c_3\}` and the path is (2.1).

### Proposition 4.1

The graph \(\widehat Q\) is six-chromatic and has no `K_7` minor.  The six
vertices

\[
                         x,c_1,c_2,c_3,s,z             \tag{4.2}
\]

form a `K_6`.  The vertex `u` is adjacent to every vertex in (4.2) except
`s`.  In every proper six-colouring of \(\widehat Q\), `u` and `s` receive
the same colour.

#### Proof

Join additivity and (2.5) give

\[
       \chi(\widehat Q)=4+2=6,
       \qquad h(\widehat Q)=4+h(P_4)=6.               \tag{4.3}
\]

Thus \(\widehat Q\) has no `K_7` minor.  The edge `sz`, together with the
complete factor in (4.1), gives the `K_6` in (4.2).  On the path (2.1),
the vertex `u` is adjacent to `z` and `t`, but not to `s`; it is also
adjacent to the complete factor.  This proves the stated adjacency
pattern.

In a proper six-colouring, the complete factor uses four distinct colours,
none of which can occur on the path.  The connected bipartite path must
use the remaining two colours, alternating along (2.1).  Hence `s,u`
receive one colour and `z,t` the other.  In particular,

\[
                         \operatorname{colour}(u)
                           =\operatorname{colour}(s)
                           =\operatorname{colour}(D_4).              \tag{4.4}
\]

This is exactly the unique repeated-colour response proposed for the
deficient branch set. \(\square\)

Equation (4.4) does not produce an exchange.  In `R-C` the two vertices
`s,t` are isolated.  Reaching the unused `T`-vertex `t` from `D_4=\{s\}`
requires a vertex of `C`, and each such vertex already belongs to a
different branch set in (3.1).  Proposition 3.1 shows that no
rearrangement, label-preserving or otherwise, can increase the contact
count.

## 5. Exact scope

The example satisfies the internal compressed-core conclusions

\[
 \chi(Q)=5,\quad Q\text{ is }K_6\text{-minor-free},\quad
 \chi(R)=4,\quad \chi(R+z)=\chi(R+u)=5,
\]

and \(\widehat Q\) is precisely the six-colourable, `K_7`-minor-free graph
obtained by adjoining the universal vertex that represents the contracted
connected dominating subgraph.  Thus neither the complete-minor exclusion
nor the uniqueness of the repeated label repairs the proposed exchange.

It is not a lifted `HC_7` host.  No expansion of `x` to the connected
induced bipartite subgraph `X` of a seven-connected, seven-chromatic graph
whose every proper minor is six-colourable is supplied.  In particular,
the separator `C` has order three in `R`; the example does not test how
its attachments expand through an actual `X`, does not refute an
order-seven separation outcome in such a host, and does not refute a
two-vertex transversal conclusion there.  It refutes only the inference
from the repeated quotient colour to a strict rooted-model exchange.
