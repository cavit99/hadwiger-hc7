# A two-edge star contraction gives a coupled Kempe lock

## 1. The general critical-colouring lemma

Let \(G\) be \(k\)-critical, let \(vd,v\ell\in E(G)\), and assume
\(d\ell\notin E(G)\).  Let \(c\) be a proper \((k-1)\)-colouring of

\[
                         G-\{vd,v\ell\}
\]

in which \(v,d,\ell\) have the same colour \(\alpha\).  Such a
colouring is obtained by colouring the minor in which the connected
star \(\{v,d,\ell\}\) is contracted and then expanding its image.

For \(x\in\{d,\ell\}\) and \(\beta\ne\alpha\), write
\(K_\beta(x)\) for the \(\alpha/\beta\)-component containing \(x\).

### Theorem 1.1 (coupled two-edge Kempe lock)

The following hold.

1. For every \(\beta\ne\alpha\), at least one of
   \(K_\beta(d),K_\beta(\ell)\) contains \(v\).
2. If \(\beta\ne\gamma\), \(v\notin K_\beta(d)\), and
   \(v\notin K_\gamma(\ell)\), then either the two components meet
   (necessarily in an \(\alpha\)-coloured vertex), or an edge joins a
   \(\beta\)-coloured vertex of \(K_\beta(d)\) to a
   \(\gamma\)-coloured vertex of \(K_\gamma(\ell)\).

The symmetric statement holds after interchanging \(d,\ell\).

#### Proof

Suppose first that, for one colour \(\beta\), neither component contains
\(v\).  Interchange \(\alpha,\beta\) on every distinct component among
\(K_\beta(d),K_\beta(\ell)\).  This recolours both \(d,\ell\) with
\(\beta\) and leaves \(v\) with \(\alpha\).  The two recoloured
vertices are nonadjacent.  Restoring \(vd,v\ell\) therefore gives a
proper \((k-1)\)-colouring of \(G\), a contradiction.  This proves 1.

For 2, suppose the two displayed components were disjoint and there
were no edge between their \(\beta\)- and \(\gamma\)-coloured vertices.
Swap \(\alpha,\beta\) on \(K_\beta(d)\) and
\(\alpha,\gamma\) on \(K_\gamma(\ell)\).  Each switch is proper away
from edges between the two sets.  Across those sets the only possible
new monochromatic edge would have both ends recoloured to \(\alpha\),
so before the switches its ends would have colours \(\beta,\gamma\);
the hypothesis excludes precisely those edges.  Thus the two switches
recolour \(d,\ell\) away from \(\alpha\), leave \(v\) with
\(\alpha\), and preserve properness.  Restoring the star edges colours
\(G\), a contradiction.  If the components meet instead, a common
vertex has a colour in both \(\{\alpha,\beta\}\) and
\(\{\alpha,\gamma\}\), and is therefore \(\alpha\). \(\square\)

This is stronger than applying the ordinary critical-edge lemma to one
star edge at a time: a colour may be supported through either leaf, but
oppositely unsupported colours force either an actual same-colour
intersection or a cross-edge between their two non-\(\alpha\) colour
classes.

## 2. Exact trace at a degree-seven vertex

Assume now that \(G\) is a hypothetical minimal \(HC_7\)
counterexample, \(d(v)=7\), and \(d,\ell\in N(v)\) are nonadjacent.
Contract the star \(\{v,d,\ell\}\) and six-colour the proper minor.
The independent-set trace lemma says that the five vertices

\[
                         N(v)-\{d,\ell\}             \tag{2.1}
\]

receive the five colours different from \(\alpha\), one each.  Expand
the contracted vertex.  Theorem 1.1 therefore supplies a five-colour
coupled fan: each of the five rainbow colours has an
\(\alpha/\beta\)-connection from \(v\) to at least one of \(d,\ell\).
For two oppositely unsupported colours, the corresponding leaf
components either share an actual \(\alpha\)-vertex or have an actual
edge between their two non-\(\alpha\) colour classes.

In the central portal-swap row one may take \(d\in\{1,2,6\}\) and
choose \(\ell\in\{3,4\}\) with \(d\ell\notin E(G)\).  The colouring
is then simultaneously an accessible exact Moser trace and an
operation-level witness for the *coupled pair* \(vd,v\ell\).  It aligns
the exact trace with Theorem 1.1, but it is not by itself a colouring of
\(G-vd\), since the second star edge is also absent.

## 3. Scope

Theorem 1.1 does not itself produce disjoint branch sets.  Its exact
residue is a contact system consisting of shared \(\alpha\)-vertices
and cross-edges between the two non-\(\alpha\) colours.  In a
two-shore portal-swap geometry, a clean pair of oppositely supported
components gives the reserved connector exchange; otherwise (1.1)
forces a common \(\alpha\)-gate.  Converting that gate into a rooted
minor or a colour-gluable adhesion is the remaining step.
