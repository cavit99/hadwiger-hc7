import itertools, networkx as nx

def colorable(D, contacts, state):
    # colors: 0 common, 1 singleton, 2 free; three other boundary colors forbidden universally
    # state AB: common contacts a,b; singleton c. AC: common a,c; singleton b
    pair = ('a','b') if state=='AB' else ('a','c')
    single = 'c' if state=='AB' else 'b'
    vs=list(D)
    lists={v:[2]+([] if any(v in contacts[x] for x in pair) else [0])+([] if v in contacts[single] else [1]) for v in vs}
    order=sorted(vs,key=lambda v:len(lists[v]))
    col={}
    def go(i):
        if i==len(order):return True
        v=order[i]
        for c in lists[v]:
            if all(col.get(w)!=c for w in D[v]):
                col[v]=c
                if go(i+1):return True
                del col[v]
        return False
    return go(0)

def rows(D,P,typ=0):
    # type0 AB|BC, type1 AC|BC
    left=('a','b') if typ==0 else ('a','c')
    right=('b','c')
    vs=set(D)
    con=[]
    for r in range(1,len(vs)+1):
      for S0 in itertools.combinations(vs,r):
        S=set(S0)
        if nx.is_connected(D.subgraph(S)): con.append(S)
    for X in con:
      if not all(X&P[z] for z in left):continue
      for Y in con:
        if X&Y or not all(Y&P[z] for z in right):continue
        if any(D.has_edge(x,y) for x in X for y in Y):return X,Y
    return None

for n in range(2,6):
  D=nx.complete_graph(n)
  for mask in range(1<<(3*n)):
    P={z:set() for z in 'abc'}
    for zi,z in enumerate('abc'):
      for v in range(n):
        if mask>>(zi*n+v)&1:P[z].add(v)
    if not all(P.values()) or len(P['b'])<2:continue
    if colorable(D,P,'AB') and not colorable(D,P,'AC') and not rows(D,P,0):
      print('counter',n,{z:sorted(P[z]) for z in P});raise SystemExit
print('none')
