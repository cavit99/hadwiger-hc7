# A common carrier cutvertex cannot block the singleton peel

## 1. Setting

Let \(G\) be seven-connected and \(K_7\)-minor-free, and suppose it has
a spanning \(K_7^-\)-model

\[
             \{h\},\{1\},\{2\},\{r\},C,D_0,D_1,           \tag{1.1}
\]

whose sole deficient pair is \(D_0D_1\).  Thus \(D_0,D_1\) are
anticomplete.  Put

\[
                         S=\{h,1,2,r\}.                    \tag{1.2}
\]

The carrier \(C\) is connected, and each of \(C,D_0,D_1\) is adjacent
to every vertex of \(S\).

Fix a connected protected set \(W\subseteq C\) which retains all
required carrier contacts to \(S\) and at least one contact to \(D_1\).
In the Moser singleton application one may require \(W\) to contain the
vertices supplying the \(h,1,2,r\) contacts and the literal
\(D_v\)-portal \(6\).

## 2. The cutvertex exclusion

### Theorem 2.1 (common blocking cutvertex gives \(K_7\) or a five-cut)

Let \(w\) be a cutvertex of \(C\), and assume \(W\) lies in the union of
\(\{w\}\) and components of \(C-w\) designated as the protected side.
Let \(\mathcal L\) be the set of all other components of \(C-w\) which
contain a \(C\)-side portal to \(D_0\).  Suppose

\[
                    N_C(D_0)\subseteq
                    \{w\}\cup\bigcup_{L\in\mathcal L}V(L).
                                                               \tag{2.1}
\]

Then \(G\) contains a \(K_7\)-minor.  Equivalently, in a
\(K_7\)-minor-free state no single carrier cutvertex can trap every
\(D_0\)-portal away from the protected side.

#### Proof

First suppose some \(L\in\mathcal L\) also has an edge to \(D_1\).
The partition

\[
                         C=L\mathbin{\dot\cup}(C-L)         \tag{2.2}
\]

has two nonempty connected sides: every component of \(C-w\) attaches
to \(w\), and \(w\notin L\).  The side \(L\) meets both \(D_0,D_1\);
the other side contains \(W\), hence retains all four contacts to \(S\)
and a \(D_1\)-contact.  The allocated split uses

\[
 \{h\},\{1\},\{2\},\{r\},\quad
 D_0\cup L,\quad D_1,\quad C-L.                           \tag{2.3}
\]

The last three bags form a triangle: \(L D_1\) joins the first two,
an edge from \(L\) to \(w\) joins the first and third, and the protected
\(D_1\)-contact joins the last two.  All their contacts to \(S\) are
retained by the old roots and by \(W\).  Hence (2.3) is a \(K_7\)-model.

We may therefore assume

\[
                         L\not\sim D_1
                         \quad(L\in\mathcal L).             \tag{2.4}
\]

Put

\[
                    Z=D_0\cup\bigcup_{L\in\mathcal L}V(L). \tag{2.5}
\]

The set \(Z\) is connected: \(D_0\) is connected and has an edge to
every member of \(\mathcal L\).  Because the model is spanning,
\(D_0\) has neighbours only in \(S\cup C\), apart from the forbidden
shore \(D_1\).  Each component \(L\) leaves \(C\) only through \(w\),
and by (2.4) it has no \(D_1\)-edge.  Therefore

\[
                              N_G(Z)\subseteq S\cup\{w\}.   \tag{2.6}
\]

The protected side of \(C-w\) and the nonempty shore \(D_1\) lie
outside \(Z\), so (2.6) is a genuine separator of order at most five.
This contradicts seven-connectivity. \(\square\)

### Corollary 2.2 (order-two blocker must be a mixed essential bridge)

Let \(X\subseteq V(C)\) have order at most two.  Suppose all
\(D_0\)-portals lie in \(X\) or in components \(\mathcal L\) of
\(C-X\) disjoint from the protected core.  Then some
\(L\in\mathcal L\) meets \(D_1\).  Moreover, if \(C-L\) is connected
for such an \(L\), then \(G\) contains a \(K_7\)-minor.

Consequently every surviving order-two blocker is a mixed component
\(L\) which is essential for connecting the two vertices of \(X\):
\(C-L\) is disconnected.  No blocker of order zero or one survives.

#### Proof

If every member of \(\mathcal L\) misses \(D_1\), put

\[
                    Z=D_0\cup\bigcup_{L\in\mathcal L}V(L).
\]

Exactly as in (2.6),

\[
                              N_G(Z)\subseteq S\cup X.
\]

This is a separator of order at most six, contrary to
seven-connectivity.  Hence some \(L\) is mixed.

If \(C-L\) is connected, use the same seven bags as (2.3), with
\(C-L\) as the retained carrier.  It contains the protected core and
therefore all required singleton contacts and a \(D_1\)-contact; the
component \(L\) meets both shores and has an edge to \(C-L\) through
\(X\).  These bags form a \(K_7\)-model.  Thus a minor-free mixed
component must disconnect the retained carrier when removed.

For \(|X|\le1\), the complement in \(C\) of a component of \(C-X\)
is connected, so the final alternative is impossible. \(\square\)

## 3. Consequences

The 21-vertex static counterstate in
hadwiger_singleton_two_star_hybrid_counterstate.md is excluded exactly
by Theorem 2.1: its three \(D_e\)-portal leaves lie behind the common
carrier cutvertex \(w\), none meets \(D_v\), and

\[
        N(D_e\cup\{p_1,p_2,p_3\})\subseteq\{h,1,2,r,w\}.
\]

Thus the static counterstate identifies a real local inference failure,
but its blocker cannot occur in a seven-connected host.

The theorem also sharpens the remaining protected-peel gap.  A surviving
common blocker is not a one-vertex carrier adhesion.  It must instead be
one of:

1. a nonseparating portal inside a two-connected carrier web;
2. an exact order-two carrier adhesion whose mixed portal component is
   essential for joining both adhesion vertices; or
3. a blocking configuration in which a \(D_0\)-portal component also
   meets \(D_1\), in which case the contact placement must fail one of
   the protected hypotheses used in (2.3).

Only these genuinely distributed states require a further
deletion/contraction transition.  The singular common-portal state is
already eliminated by global connectivity.
