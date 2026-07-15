# Atomic twin-seam packet transfer

**Status:** proved and independently audited.

## 1. Setup

Use the notation and all hypotheses of the
[atomic twin-seam crossed-state theorem](hc7_atomic_twin_seam_crossed_states.md).
Thus

\[
 I=T_D\cap T_E,\qquad A_0=T_D-T_E,\qquad B_0=T_E-T_D,
\]

\[
 \Omega_D=Z\mathbin{\dot\cup}I\mathbin{\dot\cup}A_0,
 \qquad
 \Omega_E=Z\mathbin{\dot\cup}I\mathbin{\dot\cup}B_0,
 \tag{1.1}
\]

where `|A_0|=|B_0|=2`.  The old rich shore `R` contains two
vertex-disjoint connected `S`-full packets `R_1,R_2`.

Write

\[
 a=\nu_D^{\Omega_D},\quad b=\nu_{B_D}^{\Omega_D},\quad
 c=\nu_E^{\Omega_E},\quad d=\nu_{B_E}^{\Omega_E}.       \tag{1.2}
\]

Each ordered pair `(a,b)` and `(c,d)` is an exact-seven packet vector.

## 2. Cross-lift lemma

### Lemma 2.1

\[
                         a\ge2\Longrightarrow d\ge2,
 \qquad
                         c\ge2\Longrightarrow b\ge2.      \tag{2.1}
\]

### Proof

Suppose `a>=2` and choose disjoint `Omega_D`-full packets
`Q_1,Q_2 subseteq D`.  Enumerate `A_0={a_1,a_2}` and put

\[
                         X_i=Q_i\cup\{a_i\}\cup R_i
                         \qquad(i=1,2).                    \tag{2.2}
\]

The three parts of each `X_i` lie respectively in `D`, `A_0`, and `R`,
so the two sets in (2.2) are disjoint.  Packet fullness gives an edge
from `a_i` to `Q_i`, because `a_i in Omega_D`, and an edge from `a_i`
to `R_i`, because `a_i in S`.  Hence each `X_i` is connected.

The open shore opposite `E` is

\[
                         B_E=D\cup A_0\cup R.              \tag{2.3}
\]

Every `Q_i` has a neighbour at each vertex of `Z union I`, while every
`R_i` has a neighbour at each vertex of `I union B_0`.  Consequently
`X_i` is `Omega_E`-full.  The two sets (2.2) are disjoint packets in
`B_E`, proving `d>=2`.

The second implication is symmetric.  Enumerate `B_0={b_1,b_2}`, take
two disjoint `Omega_E`-full packets in `E`, and join the `i`-th one through
`b_i` to `R_i`.  The resulting two connected sets lie in
`B_D=E union B_0 union R` and are `Omega_D`-full.  Thus `b>=2`. \(\square\)

## 3. Packet-vector normalization

### Theorem 3.1

The twin seam has at least one of the following outcomes.

1. One twin boundary has packet vector `(1,3)` up to orientation, and the
   audited adaptive packet-reflection theorem closes the cell.
2. One twin boundary is a **strict lobe-oriented `(1,2)` receiver**.  Its
   packet-one shore is `D` or `E`; the crossed-state theorem supplies the
   named contraction `f=dt` or `e=zu`, respectively, and an exact state of
   demand at least three intact on the packet-two closed shore.  Its literal
   boundary map replaces one old exclusive pair by the two gates `Z`, and
   its active packet-one shore has order strictly less than `|A|`.
3. Both twin packet vectors are exactly

   \[
                              (a,b)=(c,d)=(1,1).            \tag{3.1}
   \]

### Proof

The exact-seven packet theorem restricts each twin vector, up to
orientation, to `(1,1)`, `(1,2)`, or `(1,3)`.

If `b>=2` while `a=1`, the `Omega_D` vector is `(1,2)` or `(1,3)` with
the literal lobe `D` as its packet-one shore.  The latter is outcome 1.
In the former case Corollary 3.1 of the crossed-state theorem selects
`f=dt` and the state `Pi_D^f`, whose demand is strictly greater than
`b=2`; this is outcome 2.

If instead `a>=2`, Lemma 2.1 gives `d>=2`.  The exact-seven packet theorem
applied at `Omega_E` now forces `c=1` and `d in {2,3}`.  Again `d=3` is
outcome 1, while `d=2` is outcome 2 with packet-one lobe `E`, named
contraction `e=zu`, and state `Pi_E^phi` of demand greater than two.

Thus, in the absence of outcomes 1--2, `a=b=1`.  Interchanging `D,E` and
the two twin boundaries proves `c=d=1` as well.

For strictness in outcome 2, both `D` and `E` are nonempty components of
`A-Z`, where `|Z|=2`; hence

\[
                         |D|<|A|,\qquad |E|<|A|.           \tag{3.2}
\]

The old-to-new boundary maps are literal:

\[
 \Omega_D=(S-B_0)\cup Z,
 \qquad
 \Omega_E=(S-A_0)\cup Z.                                 \tag{3.3}
\]

The packet-two sides are witnessed either by their existing packets or by
the cross-lift construction (2.2).  The named colouring is proper on that
opposite closed side by the crossed-state theorem.  This proves every item
in outcome 2 and completes the normalization. \(\square\)

## 4. Exact scope

Outcome 2 is a genuine strict, labelled, high-demand `(1,2)` certificate:
it records the actual boundary, packet orientation, named proper-minor
operation, exact returned state, intact packet-two shore, and strict lobe
order.  It is **not automatically** the paired-triangle state required by
the older support-four recursion.  A global proof may delegate this
certificate only to a receiver theorem that accepts arbitrary high-demand
strict `(1,2)` cells and preserves a noncycling rank.

Accordingly Theorem 3.1 does not by itself discharge the `S1/S4` outcome of
the active double-lock theorem.  It does show that the genuinely
nondelegated twin-seam lock geometry may be normalized to the simultaneous
`(1,1)/(1,1)` cell; no portal enumeration is involved.
