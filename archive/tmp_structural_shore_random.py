import random,itertools,networkx as nx

def shores(D,P):
  vs=set(D); root=next(iter(vs))
  for bits in range(0,1<<(len(vs)-1)):
    X={root}; arr=list(vs-{root})
    for i,v in enumerate(arr):
      if bits>>i&1:X.add(v)
    Y=vs-X
    if not Y:continue
    if (len(X)==1 or nx.is_connected(D.subgraph(X))) and (len(Y)==1 or nx.is_connected(D.subgraph(Y))):
      if X&P['a'] and X&P['b'] and Y&P['b'] and Y&P['c']:return True
      if Y&P['a'] and Y&P['b'] and X&P['b'] and X&P['c']:return True
  return False

def gate(D,P):
  L=P['a']|P['c'];R=P['b']
  for z in D:
    H=D.copy();H.remove_node(z)
    if not (L-{z}) or not (R-{z}):return True
    comps={v:i for i,C in enumerate(nx.connected_components(H)) for v in C}
    if all(comps[x]!=comps[y] for x in L-{z} for y in R-{z}):return True
  return False

for n in range(3,11):
 for it in range(3000):
  D=nx.gnp_random_graph(n,random.uniform(.1,.8))
  if not nx.is_connected(D):continue
  P={z:{v for v in D if random.random()<.4} for z in 'abc'}
  if not all(P.values()):continue
  if not shores(D,P) and not gate(D,P):
   print('COUNTER',n,sorted(D.edges()),{z:sorted(P[z]) for z in P});raise SystemExit
print('none')
