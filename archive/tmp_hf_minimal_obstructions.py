import networkx as nx,itertools
from networkx.generators.atlas import graph_atlas_g

def has_k7(F, cert=False):
    # H = complement(F) on 0..6 joined to independent a=7,b=8
    H=nx.complement(F)
    H.add_nodes_from([7,8])
    H.add_edges_from((x,s) for x in [7,8] for s in range(7))
    V=list(range(9)); allmask=(1<<9)-1
    con=[]
    for mask in range(1,1<<9):
      # no branch needs >3 vertices: with 7 bags on <=9 vertices
      if mask.bit_count()>3:continue
      X=[i for i in V if mask>>i&1]
      if len(X)==1 or nx.is_connected(H.subgraph(X)):
        con.append(mask)
    # adjacency bit matrix between branch masks
    def adjacent(x,y):
      if x&y:return False
      for i in V:
       if x>>i&1:
        for j in H[i]:
         if y>>j&1:return True
      return False
    # candidates ordered singleton first
    con.sort(key=lambda x:(x.bit_count(),x))
    def go(chosen,used,start):
      if len(chosen)==7:return chosen
      if 9-used.bit_count()<7-len(chosen):return None
      for z in range(start,len(con)):
       X=con[z]
       if X&used:continue
       if all(adjacent(X,Y) for Y in chosen):
        ans=go(chosen+[X],used|X,z+1)
        if ans:return ans
      return None
    ans=go([],0,0)
    if cert and ans:return [[i for i in V if m>>i&1] for m in ans]
    return bool(ans)

mins=[];targets=[]
for F in graph_atlas_g():
 if len(F)!=7:continue
 F=nx.convert_node_labels_to_integers(F)
 if has_k7(F):continue
 minimal=True
 for e in list(F.edges()):
  K=F.copy();K.remove_edge(*e)
  if not has_k7(K):minimal=False;break
 if minimal:mins.append(F)

print('minimal count',len(mins))
for i,F in enumerate(mins):
 print(i,'m',F.number_of_edges(),'deg',sorted(dict(F.degree()).values()),'components',sorted(map(len,nx.connected_components(F))), 'edges',sorted(F.edges()))
 print(' graph6',nx.to_graph6_bytes(F,header=False).strip().decode())
 ok=[]
 for Q0 in itertools.combinations(range(7),3):
  Q=set(Q0)
  if F.subgraph(Q).number_of_edges():continue
  W=set(range(7))-Q
  for M in itertools.combinations(F.subgraph(W).edges(),2):
   if len(set(M[0]+M[1]))==4:ok.append((tuple(sorted(Q)),M));break
 print(' q+2gates',ok[:3])
