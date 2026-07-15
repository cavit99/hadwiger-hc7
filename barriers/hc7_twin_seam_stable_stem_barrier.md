# Candidate barrier: stable stems defeat bundle-only carrier extraction

**Status:** draft mechanism barrier with an executable certificate.  It is
not a counterexample to the terminal-disjunctive twin-seam theorem and is
not yet promoted as an audited result.

## 1. Claim falsified

In the residual twin seam, write `Z={p,q}`, `A_0={a_1,a_2}` and
`B_0={u,b}`.  A sharp matched carrier pair in `D` consists of disjoint
connected sets

\[
 C_i\subseteq D\cup\{a_i\}\quad(i=1,2)
\]

such that `a_i in C_i` and each `C_i` has a literal neighbour at both
`p` and `q`.  Such a pair, combined with the two old `S`-full packets,
would create two `Omega_E`-full packets and contradict the residual packet
number one.  The symmetric definition applies in `E` with the two members
of `B_0`.

The following implication is false, even after retaining the exact twin
geometry, connectivity seven, both residual packet vectors, crossed named
responses and the common equal/equal state:

> the separating five-rung response bundle, or a response-matched bypass,
> forces a sharp matched carrier pair in one lobe.

The missing issue is literal stem shortening.  A rooted-cycle or linkage
certificate can reach `p` or `q` through one compulsory lobe vertex; it
does not automatically produce two branches adjacent to the singleton
gate itself.

## 2. Certificate

The verifier is
[`../active/hc7_twin_seam_stable_stem_probe.py`](../active/hc7_twin_seam_stable_stem_probe.py).
It constructs two 23-vertex hosts.  They differ by the single allowed
gate-to-common-duty edge `q-i2`.

Both hosts have the literal partition

\[
 Z=\{p,q\},\quad
 D=\{d,d_1,x_2,x_3,x_4,x_5\},\quad
 E=\{z,e_1,y_2,y_3,y_4,y_5\},
\]

\[
 I=\{i_1,i_2,i_3\},\quad
 A_0=\{a_1,a_2\},\quad
 B_0=\{u,b\},\quad
 R=\{r_1,r_2\}.
\]

The two stable stems are literal:

\[
 N_D(p)=\{d_1\},\qquad N_E(q)=\{e_1\}.               \tag{2.1}
\]

Therefore every `D`-carrier meeting both gates contains `d_1`, and every
`E`-carrier meeting both gates contains `e_1`.  No two such carriers can
be disjoint, regardless of the matching to the exclusive boundary pair.
The verifier also enumerates every connected candidate directly.

The remaining contacts are arranged so that

\[
 N_G(D)=\Omega_D=Z\cup I\cup A_0,qquad
 N_G(E)=\Omega_E=Z\cup I\cup B_0.                    \tag{2.2}
\]

The old boundary is connected and bipartite, `zu` is the unique `A-u`
edge, `A` is biconnected, there is no `A-R` edge, and `r_1,r_2` are
adjacent singleton `S`-full packets.  Exact connected-subset enumeration
gives

\[
 (\nu_D^{\Omega_D},\nu_{B_D}^{\Omega_D},
   \nu_E^{\Omega_E},\nu_{B_E}^{\Omega_E})=(1,1,1,1). \tag{2.3}
\]

The whole graph has vertex-connectivity exactly seven and minimum degree
seven.

## 3. The two response modes

In the separating host, a six-colouring of `G-zu` has a `0-1` lock in
which `f=qd` is a bridge separating `z` from `u`.  Swapping its
`{z,p,q}` side yields a six-colouring of `G-f`.  Besides the complementary
`d-a1-b-u-z-p-q` path through `zu`, that same response contains the four
colour-distinct bypasses

\[
                         d-x_j-q\quad(j=2,3,4,5).
\]

Thus the full separating response bundle is literal, but all four new
rungs terminate at the noncompulsory `q` side of `D`; they do not shorten
the opposite `p-d_1` stem.

In the bypass host, the extra edge `q-i2` creates the literal path

\[
                         z-p-q-i_2-u
\]

after `f` is deleted from the same `0-1` lock.  A displayed `G/f`
colouring satisfies `c_f(z)=phi(z)=0` and `c_f(u)=1`, so it selects this
very lock under the response-matching rule.  Its exact partitions remain
crossed on both twin boundaries.  The stable stems and packet vector
(2.3) are unchanged.

Both common edge-deletion hosts also have a displayed equal/equal
six-colouring, so the named double contraction is present.

## 4. Why this does not refute the active theorem

Both hosts are six-colourable; the verifier displays a proper/proper
six-colouring.  Both also contain the literal `K_7` model

```text
{d,i1,r1,x4}
{u}
{e1,i2}
{b}
{d1,i3,y2,y5}
{a1,r2,x3}
{a2,p,q,x2,x5,y3,y4,z}
```

Consequently they violate the non-six-colourable, strong
contraction-critical kernel and the `K_7`-minor-free hypothesis.  The
terminal branch of the full theorem closes them immediately.

The exact safe conclusion is narrower: neither the response bundle nor
response-matched bypass geometry, even with the twin boundaries, residual
packet vectors, seven-connectivity and equal/equal state, proves sharp
carrier extraction.  A valid proof must use the forbidden proper/proper
state or the terminal-minor/fixed-pair alternative to eliminate a stable
stem.  Treating an ordinary rooted `C_4` with a nontrivial gate stem as a
singleton-rooted `C_4` would be invalid.
