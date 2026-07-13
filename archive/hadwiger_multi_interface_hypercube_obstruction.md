# The multi-interface state obstruction is a hypercube, not a star

## 1. Fixed-state relations for an interface matching

Let

\[
 e_i=x_i y_i\qquad(i\in[m])
\]

be a matching forming the complete interface between two pieces. For a
fixed labelled boundary state, let

\[
 {\cal A},{\cal B}\subseteq\Omega^m
\]

be the terminal-colour vectors realized on the two pieces. Failure to
extend the state over the unsplit shore says

\[
 \forall a\in{\cal A},\ \forall b\in{\cal B},
 \qquad \operatorname{Eq}(a,b)\neq\varnothing,    \tag{1.1}
\]

where

\[
 \operatorname{Eq}(a,b)=\{i:a_i=b_i\}.
\]

An \(e_i\)-deletion transition is a cross-pair with equality set
exactly \(\{i\}\). Contracting simultaneously the interface edges
indexed by \(J\subseteq[m]\), while retaining all other interface
edges, can remain in the same boundary state precisely when there is a
cross-pair with equality set exactly \(J\).

For \(m=2\), the star/XOR lemma rigidly classifies (1.1). The analogous
state-only statement is false for every \(m\ge3\).

## 2. A maximal binary cross-relation

Use only two terminal colours and identify them with \(\mathbb F_2\).
Write \({\bf1}\) for the all-one vector. Given a nonempty proper
\({\cal A}\subsetneq\mathbb F_2^m\), put

\[
 {\cal B}=\mathbb F_2^m-({\cal A}+{\bf1}).        \tag{2.1}
\]

Then \({\cal A},{\cal B}\) satisfy (1.1): the unique vector having no
coordinate equal to \(a\) is \(a+{\bf1}\), and it was deleted from
\({\cal B}\).

For a nonempty index set \(J\), let \({\bf1}_J\) be its incidence
vector. There is a pair \(a\in{\cal A},b\in{\cal B}\) with

\[
 \operatorname{Eq}(a,b)=J                         \tag{2.2}
\]

if and only if

\[
 {\cal A}+{\bf1}_J\neq{\cal A}.                  \tag{2.3}
\]

Indeed, choose \(a\in{\cal A}\) with
\(a+{\bf1}_J\notin{\cal A}\) and put

\[
 b=a+{\bf1}+{\bf1}_J.
\]

Then \(b+{\bf1}=a+{\bf1}_J\notin{\cal A}\), so
\(b\in{\cal B}\), and (2.2) holds. The converse follows by reversing
this calculation.

Thus simultaneous interface contractions are controlled by the
translation stabilizer

\[
 H({\cal A})=\{h:{\cal A}+h={\cal A}\},          \tag{2.4}
\]

not by the number of interface edges. A selected contraction is forced
to leave the state only when its incidence vector belongs to
\(H({\cal A})-\{0\}\).

## 3. Exact counterexample to state-diversity

### Theorem 3.1

For every \(m\ge3\), there are non-singleton cross-intersecting families
\({\cal A},{\cal B}\subseteq\{0,1\}^m\) such that, for every nonempty
\(J\subseteq[m]\), some cross-pair has equality set exactly \(J\).
Consequently:

1. the same state supplies every individual edge-deletion witness;
2. the same state can absorb every simultaneous contraction of selected
   interface edges; and
3. neither terminal relation is a singleton star.

#### Proof

Let

\[
 {\cal A}=\{0,e_1,\ldots,e_{m-1}\},              \tag{3.1}
\]

and define \({\cal B}\) by (2.1). Both families are non-singleton.
The translation stabilizer of \({\cal A}\) is trivial. To see this,
if \({\cal A}+h={\cal A}\), then \(h=0+h\in{\cal A}\). If
\(h=e_i\), choose \(j\neq i\) from \([m-1]\), which is possible for
\(m\ge3\); then \(e_j+h=e_i+e_j\notin{\cal A}\), a contradiction.
Thus \(h=0\).

For every nonempty \(J\), (2.3) now holds, and Section 2 supplies a
cross-pair with equality set exactly \(J\). Singleton \(J\)'s are the
individual deletion witnesses, while arbitrary \(J\)'s are precisely
the selected simultaneous contractions. \(\square\)

For \(m=3\), an explicit smallest instance is

\[
\begin{aligned}
 {\cal A}&=\{000,100,010\},\\
 {\cal B}&=\{000,001,010,100,110\}.
\end{aligned}                                    \tag{3.2}
\]

It realizes all seven nonempty equality sets.

## 4. Consequence for the \(m\ge3\) atomic branch

No argument using only the fixed-state terminal relations and selected
interface contractions can prove the proposed trichotomy

\[
 \text{three new states}\quad\text{or}\quad
 \text{a singleton terminal star}.
\]

The obstruction (3.1) has neither conclusion and absorbs every selected
contraction in the original state. This is an abstract relation
counterexample; it is not asserted here that a seven-connected,
\(K_7\)-minor-free, six-minor-critical shore realizes it. It identifies
the indispensable missing input.

The correct structural target is a **hypercube-realization exchange
lemma**: an almost-full counterexample-derived shore realizing all cube
directions in (2.2) must either

1. turn two cube directions into disjoint boundary carriers;
2. expose a genuine exact seven-cut separating their portal regions; or
3. admit a proper rooted minor preserving the whole extension family.

Unlike a further Hamming-family classification, this target uses the
placement of the portals and the minor-critical geometry. The \(m=2\)
alternating cycle in hadwiger_double_interface_contraction_exchange.md
is the first one-dimensional realization of the same hypercube
obstruction.
