# The birooted \(K_4\) threshold after the 5-connected obstruction

## 1. Honest status

The 5-connected statement is false by
`hadwiger_birooted_k4_counterexample.md`.  The corresponding
6-connected statement survived the searches described below, but no
proof is presently available:

> **Threshold-6 candidate.**  If \(J\) is a 6-connected four-colourable
> graph and \(X,Y\) are colourful, then \(J\) has four pairwise
> adjacent disjoint connected branch sets, each meeting both \(X\) and
> \(Y\).

This remains a candidate lemma, not an established theorem.

## 2. Falsification evidence

The following independent families were tested exactly for every pair of
inclusion-minimal colourful sets in the generated graph.

1. All 6-connected four-colourable graphs through order nine.  At order
   eight the complement has maximum degree one, and four-colourability
   forces \(K_{2,2,2,2}\).  At order nine the complement has maximum
   degree two; four-colourability forces a triangle component and a
   six-vertex remainder with a perfect matching.  The four possible
   remainder types were all exhausted.
2. Every join of two connected bipartite graph-atlas graphs of total
   order at most ten which is 6-connected: 35 graphs and 33,484
   colourful pairs.
3. Every join \(I_a\vee B\) of total order at most ten, where \(B\) is
   a connected three-chromatic atlas graph and the join is 6-connected:
   49 graphs and 34,807 colourful pairs.
4. The natural sharp families \(P_5\vee P_5\), \(P_4\vee C_6\), and
   \(I_2\vee(I_2\vee C_6)\), for every minimal colourful pair.
5. More than 180,000 pairs in random dense 6-connected graphs with a
   planted four-colouring, together with targeted extensions of the
   eight-vertex 5-connected obstruction.

No counterexample was found.  These computations are evidence only;
they do not certify the unbounded statement.

## 3. Exact rooted-torso lemma

There is a clean proved condition which isolates the missing mechanism.

### Lemma 3.1 (contractible birooted cores)

Let \(H\) be a graph and let \(X,Y\subseteq V(H)\).  Suppose there are
four pairwise disjoint connected subgraphs

\[
                         P_1,P_2,P_3,P_4
\]

each meeting both \(X\) and \(Y\).  Contract every \(P_i\) to a vertex
\(p_i\), and take any further minor \(R\) without deleting or identifying
the four \(p_i\).  If either

1. \(R\) is 4-connected and nonplanar; or
2. \(R\) is 3-connected and planar, but \(p_1,p_2,p_3,p_4\) do not lie
   on one face,

then \(H\) has a \(K_4\)-model every bag of which meets both \(X\) and
\(Y\).

#### Proof

By the rooted-\(K_4\) theorem of Fabila-Monroy and Wood, \(R\) has a
\(K_4\)-model rooted respectively at \(p_1,p_2,p_3,p_4\) in either
case.  Lift that model through the contractions.  The branch bag
containing \(p_i\) expands to contain all of \(P_i\), and hence meets
both \(X\) and \(Y\). \(\square\)

Thus the sharp threshold question reduces to the following concrete
uniform statement.

> **Torso-preserving four-core lemma.**  Two colourful sets in a
> 6-connected four-colourable graph admit four disjoint connected
> \(X\)-to-\(Y\) cores whose contraction has a rooted \(K_4\); it would
> suffice that the contracted torso be 4-connected and nonplanar.

Ordinary Menger gives four disjoint \(X\)-to-\(Y\) paths, but it does
not preserve four-connectivity or nonplanarity after their contraction.
That is the exact unproved step; invoking the ordinary rooted-\(K_4\)
theorem before resolving it is not valid.

## 4. What an ambient \(HC_7\) host would have to provide

The graph \(J\) in the parity-compression theorem is induced by four
colour classes of a coloured minor.  Even if the ambient \(HC_7\) host
is seven-connected, \(J\) may have cutvertices or be disconnected.
Connectivity does not pass to an induced union of colour classes.
Consequently the threshold-6 candidate, even if proved, would not apply
directly.

The weakest presently rigorous transport hypothesis is relative rather
than intrinsic:

* in the allowed part of the ambient host, avoiding the compressed tree
  and all reserved branch bags, find four disjoint connected
  \(X_U\)-to-\(X_W\) cores;
* contract those cores and retain a minor satisfying one of the two
  rooted-torso conditions in Lemma 3.1.

External components may supply the missing torso edges, but virtual
torso edges cannot simply be declared real.  All paths used to realize
them must be simultaneously internally disjoint from the four cores and
from one another whenever the lifted rooted model needs them.  A mere
ambient no-small-separator statement does not guarantee this
simultaneous realization.

Therefore the parity-rooted compression currently transports only under
a **relative rooted-torso** hypothesis, not from ambient connectivity
alone.  This condition is strictly weaker than requiring the induced
four-colour slice \(J\) itself to be 6-connected, while recording exactly
the linkage resource the final minor construction consumes.
