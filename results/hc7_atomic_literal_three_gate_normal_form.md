# Atomic literal three-gate normal form

**Status:** proved and independently audited.

## 1. Setup

Use the connected-bipartite atomic exact-seven interface of the literal
two-gate theorem.  Let `Z` be a three-vertex cut of `G[A]`, and let `D` be
an off-frame component of `A-Z` satisfying

\[
                              N_A(D)=Z.                  \tag{1.1}
\]

For every component `C` of `A-Z`, write

\[
             \operatorname{Att}(C)=N_Z(C),
             \qquad T_C=N_S(C).                         \tag{1.2}
\]

## 2. The normal form

### Theorem 2.1

At least one of the following holds.

1. **Exact receiver.**  Some component `C` has `|T_C|=4`.  Then

   \[
        \operatorname{Att}(C)=Z,
        \qquad
        \Omega_C=Z\mathbin{\dot\cup}T_C=N_G(C)          \tag{2.1}
   \]

   is a literal order-seven receiver boundary with a strict lobe side.
2. **Carrier closure.**  A connected adjacent carrier partition has
   unordered support at least `(5,6)`, and `G` is six-colourable.
3. **Symmetric seam.**  The graph `A-Z` has exactly two components `D,E`,
   with `z in E`, and

   \[
      |T_D|=|T_E|=5,
      \qquad T_D\cup T_E=S,
      \qquad |T_D\cap T_E|=3.                           \tag{2.2}
   \]

   Every gate support lies in `T_D`, and

   \[
       N_S(g)\subseteq T_D\cap T_E
       \quad\text{for every }g\in\operatorname{Att}(E). \tag{2.3}
   \]

   Moreover `z notin Z` and `u in T_E-T_D`.

If `|Att(E)|=2`, outcome 3 is already the twin exact two-gate seam.  The
only genuinely new residue has

\[
                       \operatorname{Att}(D)
                  =\operatorname{Att}(E)=Z,             \tag{2.4}
\]

a literal `K_{2,3}`-skeleton with the support data (2.2)--(2.3).

### Proof

Two-connectivity of `A` gives

\[
                         |\operatorname{Att}(C)|\ge2.    \tag{2.5}
\]

The literal set `Att(C) union T_C` separates `C` from the old rich shore,
so seven-connectivity gives

\[
                 |\operatorname{Att}(C)|+|T_C|\ge7.     \tag{2.6}
\]

If `|T_C|=4`, formulas (2.5)--(2.6) force `Att(C)=Z`; (2.1) follows from
the absence of `A-R` edges.  Another component and the rich shore remain
outside, so this is an actual strict receiver.

Assume no support-four component exists.  Then (2.5)--(2.6) give
`|T_C|>=5` for every component.  For `E ne D` and
`e in Att(E)`, put

\[
                         X=E\cup\{e\},
                         \qquad Y=A-X.                  \tag{2.7}
\]

The set `X` is connected.  The set `Y` is connected because `D` meets all
three gates, hence joins the two members of `Z-{e}`, while every other
component retains at least one attachment in `Z-{e}`.  The sets are
adjacent because `E` has a second gate attachment.  They cover `A`, and
their supports contain `T_E,T_D`, respectively.  Both therefore have
support at least five.  The unordered `(5,6)` theorem gives outcome 2
unless every such split has profile exactly `(5,5)`.

In the latter case `T_D` and every `T_E` have order five.  If `A-Z` had at
least three components, choose distinct `E,F ne D`.  The split based at
`E` puts `T_D,T_F` in one five-support carrier, so `T_D=T_F`; the split
based at `F` similarly gives `T_D=T_E`.  Hence every component support is
one five-set `K`.  For any gate `g`, choose `e in Att(E)-{g}`; then `g`
lies in the carrier opposite `E`, and its support is contained in `K`.
This contradicts `S`-fullness of `A`.  Thus exactly two components remain.

For those components, the same split shows that every gate support lies in
`T_D`.  When `g in Att(E)`, choose the `E`-side allocation containing `g`;
its support is also contained in `T_E`, proving (2.3).  Fullness now gives
`T_D union T_E=S`, and (2.2) follows.

If `z` were a gate, choose `e in Att(E)-{z}`.  Then `z` lies on the
`D`-side of (2.7), whose support is exactly `T_D`, so `u in T_D`.  But
`D` does not contain `z`, and uniqueness of `zu` gives `u notin T_D`, a
contradiction.  Thus `z notin Z`; the off-frame choice of `D` puts `z in E`
and gives `u in T_E-T_D`.

Finally suppose `Att(E)={a,b}` and let `h` be the third gate.  In
`A-{a,b}`, the two components are `E` and the connected set `D union {h}`.
By the gate-support conclusion,

\[
             N_S(D\cup\{h\})=T_D\cup N_S(h)=T_D.
\]

Thus both sides have five contacts and each two-gate boundary has order
seven: this is precisely the twin seam of the two-gate theorem.  Otherwise
`Att(E)=Z`, proving (2.4).  \(\square\)

## 3. Exact residual

The theorem eliminates all literal three-gates except:

* an already named exact-seven receiver, whose packet/state normalization
  remains global; or
* one symmetric two-lobe seam with two or three common gates.

No clique-completion edge, palette-to-label identification, finite lobe
census, or assumed packet orientation is used.  Closing the symmetric seam
now becomes the single reusable exchange principle needed for the rural
gate branch.
