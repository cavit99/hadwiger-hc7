# Simultaneous six-state exclusion on the minimal rank-two/rank-two 2-sum

## 1. Host

Let \(D\) have vertices

\[
  p,q,a,c,u,d,b,v
\]

and edges

\[
\begin{aligned}
 &pa,ac,cq,pu,uq,ua,uc,\\
 &pd,db,bq,pv,vq,vd,vb.
\end{aligned}
\]

The cut \(\{p,q\}\) has the two interiors

\[
 L=\{a,c,u\},\qquad R=\{d,b,v\}.
\]

Adding the virtual edge \(pq\) on either side gives a three-connected
wheel-like torso.  This is the smallest rank-two/rank-two architecture
which refutes the one-web SPQR leaf-flip argument.

For six nonempty portal classes \(P_0,\ldots,P_5\subseteq V(D)\), put
\(e_i=P_iP_{i+1}\), with subscripts modulo six.  A carrier for \(e_i\)
is a nonempty connected vertex set meeting both \(P_i\) and
\(P_{i+1}\).  Two demands are linked if they have disjoint carriers.

Frame \(i\) is present when the demands

\[
 e_{i-2},\qquad e_{i+2}
\]

are linked.  In a connected shore this carrier formulation is equivalent
to the adjacent-two-piece frame formulation: extend two disjoint carriers
along a shortest connector and split that connector at one edge.

## 2. Finite simultaneous-state lemma

### Theorem 2.1

Suppose:

1. \(P_0,\ldots,P_5\) have a system of six distinct representatives;
2. for \(i=0,1,2\), the antipodal demands \(e_i,e_{i+3}\) are not
   linked.

Then at most one of the three opposite frame pairs

\[
 \{0,3\},\qquad \{1,4\},\qquad \{2,5\}
\]

can be present in \(D\).

Consequently this minimal rank-two/rank-two host cannot be a high-owner
shore in the \(C_6\dot\cup K_1\) cell.

### Computer-assisted proof

`c6_two_r_torso_simultaneous_state_verify.py` performs an exact
same-vertex enumeration.

1. It generates all \(167\) nonempty connected vertex masks of \(D\).
2. It generates all \(2270\) ordered disjoint pairs of connected masks.
3. Boolean variable \(p_{i,x}\) records \(x\in P_i\).
4. Six pairwise-distinct integer variables select an SDR and are tied
   directly to the corresponding portal incidences.
5. For every demand and every connected mask, the formula says literally
   whether the mask meets both relevant portal classes.
6. Each antipodal exclusion universally forbids all \(2270\) possible
   disjoint carrier pairs.
7. Each owned frame is the disjunction of those same exact carrier pairs.

All three choices of two opposite frame pairs are unsatisfiable:

```text
vertices ('p', 'a', 'c', 'q', 'u', 'd', 'b', 'v')
connected carrier masks 167
ordered disjoint carrier pairs 2270
without SDR sat
with SDR, two owned opposite frame pairs {(0, 1): 'unsat',
                                         (0, 2): 'unsat',
                                         (1, 2): 'unsat'}
```

The check is stronger than the counterexample-derived test on this host:
it does not impose the outward-contact locks or either alternating
three-linkage exclusion.

The SDR is essential to this finite statement.  Removing it leaves a
satisfiable coarse portal state.  A variance check also shows that deleting
any one of the three antipodal exclusions, or any one of the four frame
requirements in a normalized two-pair instance, makes the formula
satisfiable.  Thus the contradiction genuinely uses the full simultaneous
six-state packet.

## 3. Scope

The theorem eliminates the explicit eight-vertex counterarchitecture to
the single-web rank argument; it does not restore that argument for an
arbitrary pair of SPQR torsos.  The uniform replacement suggested by this
finite result is:

> In a two-sum carrying an SDR for six portal classes, three antipodal
> crossless states and two owned opposite frame pairs either force a
> labelled linkage, or one side has portal rank at most one.

The eight-vertex theorem is the first exact positive cell for that
simultaneous-web statement.
