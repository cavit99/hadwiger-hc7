#!/usr/bin/env python3
"""Does the fixed old-boundary/full-helper skeleton already root K6?"""

from itertools import combinations


def graph_for(P):
    # old S: 0..5 cycle-complement vertices, z=6; helper h=7.
    S = range(7); h = 7
    edges = set()
    def add(a,b): edges.add(tuple(sorted((a,b))))
    for a,b in combinations(range(6),2):
        if (a-b)%6 not in (1,5): add(a,b)
    for a in range(6): add(a,6)
    for a in S: add(a,h)
    roots=[]; nxt=8
    for s in S:
        if s in P: roots.append(s)
        else:
            y=nxt; nxt+=1; roots.append(y); add(s,y)
    return nxt, edges, tuple(roots)


def find(P):
    n, edges, roots = graph_for(set(P))
    adj=[0]*n
    for a,b in edges: adj[a]|=1<<b; adj[b]|=1<<a
    rootmask=sum(1<<x for x in roots)
    conn=[]
    for m in range(1,1<<n):
        if not m&rootmask: continue
        seen=(m&-m); front=seen
        while front:
            b=front&-front; front-=b; x=b.bit_length()-1
            new=adj[x]&m&~seen; seen|=new; front|=new
        if seen==m: conn.append(m)
    neigh={m:0 for m in conn}
    for m in conn:
        x=m; z=0
        while x:
            b=x&-x;x-=b;z|=adj[b.bit_length()-1]
        neigh[m]=z
    conn.sort(key=lambda m:(m.bit_count(),m))
    def rec(chosen,start,used):
        if len(chosen)==6:return chosen
        for i in range(start,len(conn)):
            m=conn[i]
            if m&used:continue
            if any(not(neigh[m]&q) for q in chosen):continue
            got=rec(chosen+[m],i+1,used|m)
            if got:return got
        return None
    ans=rec([],0,0)
    print('P',P,'n',n,'connected',len(conn),'model',ans)


if __name__=='__main__':
    for P in ((0,2,4,6),(0,2,4),(0,3,6),(0,3),(0,2,6),(0,2),(0,)):
        find(P)
