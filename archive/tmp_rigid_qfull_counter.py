import itertools,networkx as nx

def ext(D,P,state):
  # AB: a,b=0,c=1; AC: a,c=0,b=1; q1,q2,q3=2,3,4; free=5
  boundary={'a':0,'b':0,'c':1,'q1':2,'q2':3,'q3':4} if state=='AB' else {'a':0,'c':0,'b':1,'q1':2,'q2':3,'q3':4}
  L={v:[col for col in range(6) if all(not(v in P[z] and boundary[z]==col) for z in boundary)] for v in D}
  order=sorted(D,key=lambda v:len(L[v])); color={}
  def go(i):
    if i==len(order):return dict(color)
    v=order[i]
    for col in L[v]:
      if all(color.get(w)!=col for w in D[v]):
        color[v]=col
        z=go(i+1)
        if z:return z
        del color[v]
  return go(0)

def connsets(D, req):
  out=[]; V=list(D)
  for mask in range(1,1<<len(V)):
    S={V[i] for i in range(len(V)) if mask>>i&1}
    if (len(S)==1 or nx.is_connected(D.subgraph(S))) and all(S&P[z] for z in req):out.append(S)
  return out

def fullsplit(D,P,typ):
  qs=['q1','q2','q3']; left=qs+(['a','b'] if typ==0 else ['a','c']); right=qs+['b','c']
  for X in connsets(D,left):
    Y=set(D)-X
    if Y and (len(Y)==1 or nx.is_connected(D.subgraph(Y))) and all(Y&P[z] for z in right):return X,Y
  return None

for n,D in [(3,nx.complete_graph(3)),(4,nx.complete_graph(4)),(5,nx.complete_graph(5))]:
  sets=[{v for v in D if mask>>v&1} for mask in range(1,1<<n)]
  # fixed cyclic q portals for n3, random/all choices later
  qchoices=[]
  if n==3:qchoices=[{'q1':q1,'q2':q2,'q3':q3} for q1 in sets for q2 in sets for q3 in sets]
  else:
    # limited enumerate q sets size n-1
    qchoices=[{'q1':set(D)-{0},'q2':set(D)-{1},'q3':set(D)-{2}}]
  for Q in qchoices:
   for A in sets:
    for B in sets:
     for C in sets:
      P={**Q,'a':A,'b':B,'c':C}
      ca=ext(D,P,'AB'); cc=ext(D,P,'AC')
      if ca and not cc and not fullsplit(D,P,0):
       print('FOUND',n,{z:sorted(P[z]) for z in P},'ABcol',ca,'type1split',fullsplit(D,P,1));raise SystemExit
print('none')
