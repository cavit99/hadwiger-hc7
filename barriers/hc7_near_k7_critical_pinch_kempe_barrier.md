# Seven-connected critical pinches need not split their Kempe detours

## Status

This is a sharp barrier to using ordinary edge criticality as a surrogate
for the missing labelled two-carrier split.  There is a seven-connected,
seven-vertex-critical graph and a critical edge `sw` with a six-colouring
of `G-sw` such that the five obligatory bichromatic `s-w` detours cannot
be chosen internally disjoint.  Two of the detours are forced through one
common-colour pinch vertex.

The graph does contain a `K_7` minor, so it is not a counterexample to
`HC_7` and is not seven-contraction-critical.  Its role is exact: it
shows that seven-connectivity, ordinary seven-criticality, and all five
Kempe detours do not by themselves repair a shared canonical gate.  A
valid proof must use labelled carrier placement, the actual-adhesion state,
or `K_7`-minor exclusion.

The executable certificate is
`hc7_near_k7_critical_pinch_kempe_barrier_verify.py`.

## 1. A four-connected four-critical core

Let `Q` be the nine-vertex graph with graph6 string

```
HCpvbqk
```

and edge set

\[
\begin{split}
\{&03,04,06,08,14,15,16,17,25,26,27,28,\\
  &35,36,37,47,48,58\}.
\end{split}                                                \tag{1.1}
\]

The verifier exhaustively checks that `Q` is four-connected and
four-vertex-critical.  Delete the edge `15` and use the proper
three-colouring

\[
\begin{array}{c|ccc}
\text{colour}&0&1&2\\ \hline
\text{vertices}&0,1,5&2,3,4&6,7,8.
\end{array}                                                \tag{1.2}
\]

The ends `1,5` have common colour `0`.  The entire `{0,1}`-induced
subgraph has the unique `1-5` path

\[
                         1-4-0-3-5,                        \tag{1.3}
\]

and the entire `{0,2}`-induced subgraph has the unique `1-5` path

\[
                         1-6-0-8-5.                        \tag{1.4}
\]

Thus both obligatory Kempe detours pass through the internal
common-colour vertex `0`.  Four-connectivity of the host does not prevent
the colour-restricted pinch.

## 2. The seven-connected lift

Join `Q` to a triangle on new vertices `9,10,11`; call the result `J`.
Chromatic number is additive under join, so `chi(J)=4+3=7`.  Deleting a
triangle vertex leaves `K_2 vee Q`, which is six-colourable, and deleting
a core vertex leaves `K_3 vee (Q-v)`, also six-colourable.  Hence `J` is
seven-vertex-critical.  The verifier also checks directly that

\[
                             \kappa(J)=7.                 \tag{2.1}
\]

Extend (1.2) by giving `9,10,11` three new colours.  In `J-15`, the five
bichromatic detour families are uniquely

\[
\begin{array}{lll}
1-4-0-3-5, & 1-6-0-8-5, & 1-9-5,\\
            &1-10-5,     & 1-11-5.
\end{array}                                                \tag{2.2}

The first two paths are forced to share vertex `0`; no internally
disjoint transversal of all five families exists.

For completeness, `J` has a literal `K_7` model.  The four core bags

\[
                         \{0\},\{3\},\{6\},\{1,4,5\}      \tag{2.3}
\]

form a `K_4` model in `Q`, and the three triangle singletons complete it
to `K_7`.

## 3. Consequence for the rotation spine

For a critical edge, Kempe switching guarantees one bichromatic detour
for each of the five other colours.  It does not guarantee that those
detours are internally disjoint, that their common-colour intersections
are actual separators of the host, or that any secondary colour names a
fixed near-clique row.  The graph above retains this obstruction even at
the exact connectivity required by the `HC_7` spine.

Accordingly, the shared-root canonical gate must be handled through the
labelled carrier split or through the equality partition on the actual
adhesion.  A proof that merely counts the five Kempe detours, or replaces
their common-colour pinch by a host cutvertex, is invalid.
