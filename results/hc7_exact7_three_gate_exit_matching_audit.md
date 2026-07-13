# Audit of the three-gate exit-matching theorem

## Verdict: GREEN

The proposed exit-matching lemma is correct under its stated hypotheses.  In
particular:

- the neighbourhood identities used to obtain the new exact-seven separation
  are literal identities in the host graph;
- every constructed packet is connected, lies in the correct open shore, and
  is full on the new boundary;
- the packets asserted to be disjoint are vertex-disjoint for explicit
  region-by-region reasons; and
- the residual exit-set family is classified exactly.  With at least two
  sibling lobes, the only obstruction is a common singleton exit.  With one
  sibling lobe, no additional restriction follows, and the candidate correctly
  keeps that case separate.

No correction to the candidate statement is required.

## 1. Exact neighbourhoods and the new seven-separation

Let `J` be a sibling lobe, i.e. a component of `C-X` other than `K`.
Then

\[
N_G(J)=X\cup N_S(J).
\]

This is an equality, not merely an inclusion:

1. Since `J` is a component of `C-X`, every neighbour of `J` inside `C`
   lies in `X`.
2. Since `C` is a component of `G[R]`, `J` has no neighbour in `R-C`.
3. Since `(L,S,R)` is a separation, `J` has no neighbour in `L`.
4. Its remaining neighbours are precisely its neighbours in `S`.
5. Because `C` is 3-connected and `C-X` has both `J` and `K` as components,
   every vertex of the 3-cut `X` has a neighbour in `J`.  Otherwise the other
   two vertices of `X` would separate `J` from `K` in `C`.

Thus every vertex of `X` really occurs in the neighbourhood, and the displayed
identity follows.  Deleting this neighbourhood isolates the nonempty set `J`,
while `L` survives on the other side.  Seven-connectivity therefore gives

\[
|X|+|N_S(J)|=|N_G(J)|\ge 7,
\]

so `|N_S(J)| >= 4`.  If `J` is not self-full, it misses at least one vertex of
the four-set `A`; hence its four or more boundary neighbours cannot all lie in
`A`, and

\[
E(J)=N_S(J)\cap T\ne\varnothing.
\]

The same argument for `K` gives

\[
N_G(K)=X\cup A=\Omega.
\]

Here all vertices of `X` hit `K` by hypothesis, and `A=N_S(K)`.  The set `K`
is nonempty, the opposite open shore is nonempty because it contains `L`, and
there are no edges between the two open shores.  Consequently `\Omega` is an
actual seven-boundary, and `K` is `\Omega`-full.

## 2. Audit of the packet construction

For `F` equal to `P` or `Q`, a nonself-full sibling `J`, and `t in E(J)`, set

\[
W(F,J,t)=F\cup\{t\}\cup J.
\]

This set lies wholly in the open shore opposite `K`:

- `P subseteq L`;
- `Q subseteq R-C`;
- `J subseteq C-X`; and
- `t in T=S-A`.

All four regions avoid `\Omega=X\cup A`.

It is connected.  The `S`-full packet `F` has a neighbour of `t`, while the
definition `t in E(J)` gives a neighbour of `t` in `J`.  Thus the literal host
edges through `t` join the two connected pieces.

It is `\Omega`-full.  The packet `F` supplies a neighbour for every vertex of
`A`, and 3-connectivity supplies a neighbour in `J` for every vertex of `X`.
No completion edge or inferred adjacency is used.

A self-full sibling `J_s` is itself an `\Omega`-full packet: it sees all of
`A` by definition and all of `X` by the preceding cut argument.

## 3. Literal disjointness

The construction with two distinct nonself-full siblings uses

\[
W(P,J_0,t_0),\qquad W(Q,J_1,t_1),
\]

where `J_0 != J_1` and `t_0 != t_1`.  The pieces are pairwise separated as
follows:

| Piece | Host region |
|---|---|
| `P` | `L` |
| `Q` | `R-C` |
| `J_0,J_1` | distinct components of `C-X` |
| `t_0,t_1` | distinct vertices of `S` |

The original separation makes `L`, `S`, and `R` disjoint; `Q` is outside `C`;
the sibling lobes are distinct components inside `C-X`; and the two anchor
vertices are distinct.  Therefore the two displayed packets have empty vertex
intersection.  Possible edges between the packets are irrelevant to packet
disjointness.

The mixed self-full case is equally literal.  A self-full sibling `J_s` is
disjoint from `W(P,J,t)`, because `J_s` and `J` are distinct components of
`C-X`, while `P` lies in `L` and `t` lies in `S`.  Two distinct self-full
siblings are disjoint because they are distinct components of `C-X`.

Thus every use of two packets in Lemma 3.1 is justified at the level of host
vertices.

## 4. Exact exit-set obstruction

Let `(E_i)_{i in I}` be nonempty subsets of the three-set `T`, with
`|I| >= 2`.  Suppose there is no choice of distinct indices `i,j` and distinct
representatives `u in E_i`, `v in E_j`.

If the union of the sets contains distinct elements `u` and `v`, then either
they occur in two different member sets, giving the required representatives
immediately, or they both occur in one set `E_i`.  In the latter case choose
another index `j` and any `w in E_j`; one of `u,v` differs from `w`, again
giving a two-set system of distinct representatives.  Hence the union has size
one.  Since every `E_i` is nonempty, all sets equal the same singleton.

The converse is immediate.  Therefore Lemma 3.2 gives precisely

\[
\text{no two-set SDR}
\quad\Longleftrightarrow\quad
E_i=\{t\}\text{ for every }i
\]

for one common `t in T`.

## 5. Exact residual family

Assume the two-packet outcome fails.

If there are at least two sibling lobes, none can be self-full: a self-full
lobe together with any second sibling invokes Lemma 3.1.  Hence every sibling
has a nonempty exit set.  Distinct exit representatives for two siblings would
again invoke Lemma 3.1, so the exit family has no two-set SDR.  Lemma 3.2 then
forces

\[
E(J)=\{t\}
\]

for every sibling `J` and one common `t in T`.  This proves both necessity and
sufficiency for failure of the distinct-exit matching step.  It does not assert
that some unrelated construction could not still find two full packets.

The one-sibling case must remain separate.  Its sole lobe may be self-full, or
it may be nonself-full with any nonempty exit set `E(J) subseteq T`.  Even when
`|E(J)| >= 2`, the apparent packets `W(P,J,t_0)` and `W(Q,J,t_1)` share the
entire lobe `J`, so distinct exits do not make them disjoint.  Thus no stronger
exit classification follows from the present construction when there is only
one sibling.

Accordingly the candidate's residual alternatives are exact:

1. exactly one sibling, with no further exit restriction; or
2. at least two siblings, all nonself-full and all having the same singleton
   exit.

## 6. Packet-vector consequence

In the two-packet outcome, the `K` shore has at least one full packet and the
opposite shore has at least two.  The exact-seven packet theorem gives

\[
\min\{\nu_K,\nu_{\mathrm{opp}}\}=1,
\qquad
\nu_K+\nu_{\mathrm{opp}}\le 4.
\]

Since `\nu_{opp} >= 2`, it follows that `\nu_K=1` and
`\nu_{opp} in {2,3}`.  Hence the new packet vector is `(1,2)` or `(1,3)`, with
`K` the thin shore.  Invoking the already audited `(1,3)` closure leaves the
stated `(1,2)` recursive geometry.

## 7. Trust boundary

This audit validates the exit matching and packet reconstruction only.  It does
not provide state preservation on `\Omega`, a pullback of the attained
paired-triangle partition, a decreasing global measure, or a closure of either
residual family.  The candidate explicitly records those limitations, so it
does not overstate what has been proved.
