import networkx as nx
E='01 05 07 08 0-11 12 15 16 18 23 26 28 29 34 36 39 3-10 45 46 4-10 4-11 56 5-11 78 79 7-10 7-11 89 9-10 10-11'.split()
def ep(s):
 a,b=s.split('-') if '-' in s else (s[0],s[1:])
 return int(a),int(b)
I=nx.Graph();I.add_nodes_from(range(12));I.add_edges_from(map(ep,E))
G=I.copy();G.add_nodes_from([12,13]);G.add_edge(12,13);G.add_edges_from((u,x) for u in [12,13] for x in range(12))
S=[12,13,1,5,11,7,8]
A=[0];B=[2,3,4,6,9,10]
def parts(side):
 H=G.subgraph(S+side);order=sorted(H,key=lambda x:-H.degree(x));col={};out=set()
 def canon():
  blocks={}
  for v in S:blocks.setdefault(col[v],[]).append(v)
  return tuple(sorted(tuple(sorted(x)) for x in blocks.values()))
 def go(i,used):
  if i==len(order):out.add(canon());return
  v=order[i]
  # canonical color introduction
  for c in range(min(used+1,6)):
   if all(col.get(w)!=c for w in H[v]):
    col[v]=c;go(i+1,max(used,c+1));del col[v]
 go(0,0);return out
for side in [A,B]:
 out=parts(side);print('SIDE',side,'N',len(out))
 for x in sorted(out):print(x)
