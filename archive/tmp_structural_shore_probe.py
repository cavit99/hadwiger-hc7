import itertools, networkx as nx
from networkx.generators.atlas import graph_atlas_g

def shores(D,P):
    vs=set(D); con=[]
    for r in range(1,len(vs)+1):
      for S0 in itertools.combinations(vs,r):
        S=set(S0)
        if len(S)==1 or nx.is_connected(D.subgraph(S)):con.append(S)
    for X in con:
      if not X&P['a'] or not X&P['b']:continue
      for Y in con:
        if X&Y or not Y&P['b'] or not Y&P['c']:continue
        if any(D.has_edge(x,y) for x in X for y in Y):return X,Y
    return None

def one_gate(D,P):
    L=P['a']|P['c']; R=P['b']
    for z in D:
      H=D.copy();H.remove_node(z)
      L0=L-{z};R0=R-{z}
      if all(not nx.has_path(H,x,y) for x in L0 for y in R0):return z
    return None

for D in graph_atlas_g():
  n=len(D)
  if n<2 or n>5 or not nx.is_connected(D):continue
  vs=list(D)
  sets=[set(v for v in vs if mask>>v&1) for mask in range(1,1<<n)]
  for A in sets:
   for B in sets:
    for C in sets:
     P={'a':A,'b':B,'c':C}
     if not shores(D,P) and one_gate(D,P) is None:
      print('counter n',n,'edges',sorted(D.edges()),'P',{z:sorted(P[z]) for z in P});raise SystemExit
print('none through 6')
