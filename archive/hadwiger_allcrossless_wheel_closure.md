# Arbitrary-order all-crossless wheel shores are boundary-reducible

## 1. Setting

Let (D=W_n) be a wheel with rim (R) of order (n) and hub (h).
Give it the reserved Moser boundary

\[
 L=U\mathbin{\dot\cup}\{a,w\},\qquad |U|=5,
\]

and assume:

1. (D) is full to (L);
2. for every nonempty proper (X\subsetneq D),
   \[
   \phi_D(X)=|N_D(X)-X|+|N_L(X)|\ge7;
   \tag{1.1}
   \]
3. all five disjoint-edge frames of the missing (C_5) on (U) are
   crossless; and
4. the common portal face is the rim (R).

The last condition is automatic when the wheel is the three-connected
bare web supplied by the simultaneous-pentagram theorem.  In particular,
the hub has no (U)-contact.

## 2. The bounded circular profile lemma

Number the missing cycle by (mathbb Z_5).  The exact portal-overlap lemma
gives, for every rim vertex (x), one of the following (U)-profiles:

* an independent set of the missing cycle, of order at most two; or
* a triple lock
  \[
  T_i=\{i,i+1,i+3\},\qquad P_{i+3}=\{x\}.
  \tag{2.1}
  \]

Since (x) has three neighbours in the wheel, (1.1) for ({x})
requires at least four boundary neighbours.  Hence a nonlocked rim vertex
has exactly a two-root present-edge profile and sees both (a,w).  A
locked vertex sees at least one of (a,w).  Empty and singleton root
profiles are impossible.

The following finite circular statement is exact.

### Lemma 2.1 (five/six occurrence classification)

Let a circular word of length five or six have letters among the five
present-pair profiles and the five triple-lock profiles.  Suppose that:

1. the profiles cover all five roots;
2. every triple's shield root occurs only at that triple position; and
3. for every occurrence choice in every disjoint-edge frame, disjoint
   demanded pairs are nondegenerate and alternate around the circle.

Then:

* at length five there are ten ordinary words and twenty-five locked
  words;
* at length six there are no ordinary words and thirty locked words; and
* every locked word has exactly one triple (T_i), while every other
  letter is the complementary present pair
  \[
  Q_i=\{i+2,i+4\}.
  \tag{2.2}
  \]

### Verification

There are only ten profile letters.  The dependency-free verifier
`moser_c5_wheel_profile_verify.py` constructs the five frame constraints
from their definition, permits every occurrence coincidence consistent
with disjoint supports, enforces the singleton shield, and checks all
(10^5+10^6) words.  It obtains

\[
\begin{array}{c|ccc}
|R|&\text{all}&\text{ordinary}&\text{locked}\\ \hline
5&35&10&25\\
6&30&0&30.
\end{array}
\]

For every locked survivor it then checks (2.2).  This is a finite proof of
the displayed circular implication; every real disk society satisfies the
constraints being checked.

The length-six row controls every longer word.  Indeed, from a full word
choose at most five positions covering all roots and add arbitrary
positions until six remain.  Crosslessness and the shield condition are
hereditary under deleting positions.  If a specified triple (x) and a
specified second position (y) must be retained, the triple already covers
three roots, so at most two further covering positions are needed before
padding to six.  Lemma 2.1 therefore gives:

### Corollary 2.2 (arbitrary length)

For a full crossless profile word of length (n\ge5), either

1. (n=5) and the word is one of the ten ordinary words; or
2. there is exactly one triple (T_i), and every other position has
   profile (Q_i).

## 3. The triple alternative is a six-cut

Suppose Corollary 2.2 gives a triple vertex (x).  Put

\[
 X=R-\{x\}.
\]

This is a nonempty proper set.  In the wheel,

\[
 N_D(X)-X=\{h,x\}.
\]

Every vertex of (X) is ordinary, so Section 2 and (2.2) give

\[
 N_L(X)=Q_i\cup\{a,w\}.
\]

Consequently

\[
 \phi_D(X)=2+4=6,
\]

contrary to (1.1).  Thus the triple alternative cannot occur.

It follows that (n=5), the rim profiles are one of the ten ordinary
pentagram systems, and every rim vertex sees (a,w).  Applying (1.1) to
the hub gives

\[
 5+|N_L(h)|\ge7.
\]

The hub has no (U)-contact, so it too sees both (a,w).  Hence (D) is
exactly one of the ten order-six wheel systems classified in
`hadwiger_critical_web_exchange_order6.md`.

## 4. Conversion theorem

### Theorem 4.1 (all-crossless wheel conversion)

Every all-crossless relative-7 reserved Moser wheel shore is
boundary-universal: every proper six-colour equality state of its
seven-label boundary extends over the shore.

In particular, none of the thirty high-root/nonstar Moser states can be a
new state created by an internal safe contraction of such a shore.

### Proof

Sections 2--3 reduce the arbitrary wheel to one of the ten order-six
systems.  The exact backtracking replay
`pentagram_critical_web_fullprofile_probe.py` checks all 111 proper
six-colour boundary states for each system and extends every one.  Therefore
the original extension family is the full state universe.  No internal
contraction can enlarge it. \(\square\)

This theorem disposes of all thirty residual transition states at once;
the crossed opposite shore is not needed in the wheel family.  The
remaining safe-contraction problem begins only when the all-crossless web
has a non-wheel planar core.
