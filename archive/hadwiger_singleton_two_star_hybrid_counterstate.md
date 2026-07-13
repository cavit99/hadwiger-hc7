# Static counterstate to the singleton anchored-trace/two-star hybrid

## Verdict

The root-anchored \(56\)-trace and the coupled two-edge-star lock do
**not** force an opposite-unsupported component or cross-edge to enter
the deficient left shore. They do not imply the protected peel of
Lemma 5.1 in hadwiger_singleton_gate_anchored_joint_trace.md.

The following explicit state realizes both colouring systems while all
four forced cross-edges stay in \(C\cup D_v\).

## Construction

Write \(x=3,y=4\). Start with the pure Moser graph on
\(N(v)=\{h,1,2,x,y,5,6\}\), and join \(v\) to all seven vertices.
Use four exterior hub roots \(r,e,q,q_0\), with

\[
 r,e\sim h,1,2,\qquad q,q_0\sim h,x,y.
\]

Put

\[
\begin{aligned}
C&=\{5,6,y,q,q_0,w,p_1,p_2,p_3,a_H,a_Y,t\},\\
D_e&=\{e\},\\
D_v&=\{v,x,b_1,b_2\}.
\end{aligned}
\]

Besides the Moser edges and the displayed root edges, add

\[
\begin{gathered}
yq,\ qw,\ q_0w,\ wp_i\ (i=1,2,3),\
wa_H,\ wa_Y,\ 6a_H,\ 6a_Y,\ 5t,\ 6t,\\
rh,r1,r2,rx,rw,re,\qquad
eh,e1,e2,ep_i\ (i=1,2,3),\\
xb_1,xb_2,\qquad
a_Hb_1,a_Hb_2,a_Yb_1,a_Yb_2.
\end{gathered}
\]

There are no other edges.

Then \(d(v)=7,d(h)=9\), and

\[
 \{h\},\{1\},\{2\},\{r\},C,D_e,D_v
\]

is a \(K_7^-\)-model whose sole deficient pair is \(D_eD_v\).
The three vertices \(p_1,p_2,p_3\) are distinct \(C\)-side portals to
\(D_e\).

## Exact \((6,x)\)-star trace

Delete \(v6,vx\). The following is a proper six-colouring:

\[
\begin{array}{c|l}
A&v,6,x,p_1,p_2,p_3\\
H&h,a_H\\
B_1&1,b_1,q\\
B_2&2,b_2,w,t\\
Y&y,e,a_Y\\
F&5,r,q_0.
\end{array}
\]

It descends to a colouring after contracting the star \(\{v,6,x\}\).
The five unique roots are \(h,1,2,y,5\), with colours
\(H,B_1,B_2,Y,F\).

The only potentially unsupported colours at \(6\) are \(H,Y\), and the
only potentially unsupported colours at \(x\) are \(B_1,B_2\). In fact

\[
\begin{aligned}
K_H(6)&=\{6,a_H\},&
K_Y(6)&=\{6,a_Y\},\\
K_{B_1}(x)&=\{x,b_1,q\},&
K_{B_2}(x)&=\{x,b_2\}.
\end{aligned}
\]

The four interactions required by the coupled Kempe lock are exactly

\[
 a_Hb_1,\quad a_Hb_2,\quad a_Yb_1,\quad a_Yb_2.
\]

All lie in \(C\cup D_v\); none meets \(D_e\). The literal colours have
owners

\[
O_H=O_Y=\{x\},\quad O_{B_1}=O_{B_2}=\{6\},\quad
O_F=\{6,x\}.
\]

Thus the reserved connectors returned by the two-edge exchange, such as
\(6-a_H-b_1-x\), also avoid \(D_e\).

## Simultaneous anchored \(56\)-trace

Delete \(56\). A second proper six-colouring is

\[
\begin{array}{c|l}
0&h,5,6,w,b_1,b_2\\
1&r,y,t,p_1,p_2,p_3,a_H,a_Y\\
2&x,1\\
3&v,e,q\\
4&2\\
5&q_0.
\end{array}
\]

It descends to the minor obtained by contracting
\(\{v,h,5,6\}\). The \(0/1\)-component containing \(5\) contains
\(h,r,5,6\), while the \(0/3\)-component containing \(5\) contains
\(h,e,5,6\). Hence even the singleton root and the other deficient
left root are both aligned with \(56\) in this one static colouring.

## No protected peel

The only \(C\)-\(D_e\) edges are \(p_ie\), and each \(p_i\) has the
unique neighbour \(w\) inside \(C\). The only \(r\)-\(C\) edge is
\(rw\).

Suppose \(C=X\dot\cup Y\) satisfied the protected-peel hypotheses, with
\(5\) or \(6\) in \(X\) and \(X\sim D_e\). Then \(X\) contains some
\(p_i\). Connectedness of \(X\), together with \(5,6\ne p_i\), forces
\(w\in X\). But retaining the \(rC\)-contact in \(Y\) forces
\(w\in Y\), a contradiction.

## Scope

This graph is a static interface realization. It is **not claimed** to
be seven-connected, \(K_7\)-minor-free, or contraction-critical.
Accordingly it does not refute a theorem using those global hypotheses.
It refutes precisely the inference

\[
\begin{gathered}
\text{three-plus-three carrier portals}
+\text{root-anchored \(56\)-components}\\
+\text{all coupled two-star intersection/cross-edge conclusions}
\quad\Longrightarrow\quad
\text{an interaction in \(D_e\) or a protected carrier peel}.
\end{gathered}
\]

Any successful closure must use a further one-step deletion/contraction
transition or another global counterexample property not encoded by
these two static witness systems.
