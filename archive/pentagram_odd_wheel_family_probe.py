#!/usr/bin/env python3
"""Search repeated-portal odd wheels for a critical pentagram web.

Each rim vertex is incident with one of the five consecutive portal-pair
types forced by the pentagram order; w and a are complete to the shore.
"""

from __future__ import annotations

import itertools


U = tuple(range(5)); W, A = 5, 6; L = tuple(range(7))
MISSING = {tuple(sorted((i, (i + 1) % 5))) for i in U}
BEDGES = {tuple(sorted((i, j))) for i, j in itertools.combinations(U, 2)
          if tuple(sorted((i, j))) not in MISSING}
BEDGES |= {tuple(sorted((A, x))) for x in (0, 2, 4)}
PAIR_TYPES = ((0, 2), (0, 3), (1, 3), (1, 4), (2, 4))


def edge(x, y): return tuple(sorted((x, y)))


def partitions(items):
    blocks=[]
    def rec(i):
        if i==len(items): yield tuple(tuple(x) for x in blocks); return
        x=items[i]
        for b in blocks:
            b.append(x); yield from rec(i+1); b.pop()
        blocks.append([x]); yield from rec(i+1); blocks.pop()
    yield from rec(0)


STATES = tuple(p for p in partitions(L) if len(p)<=6 and all(
    edge(x,y) not in BEDGES for b in p for x,y in itertools.combinations(b,2)))


def decorated_states():
    out=set()
    for j in U:
        base=[{(j+1)%5,(j+2)%5},{(j+3)%5,(j+4)%5},{j},{A}]
        for pos in range(5):
            bs=[set(x) for x in base]
            if pos<4: bs[pos].add(W)
            else: bs.append({W})
            bs.sort(key=min); out.add(tuple(tuple(sorted(x)) for x in bs))
    return out


TARGET=decorated_states()


def instance(mult):
    rim=[]
    for typ,m in zip(PAIR_TYPES,mult): rim += [typ]*m
    n=len(rim); hub=n; vertices=tuple(range(n+1))
    edges={edge(i,(i+1)%n) for i in range(n)}|{edge(i,hub) for i in range(n)}
    rows=[]
    for pair in rim:
        rows.append((1<<W)|(1<<A)|sum(1<<x for x in pair))
    rows.append((1<<W)|(1<<A))
    return vertices,edges,tuple(rows)


def cut_ok(vertices,edges,rows):
    n=len(vertices)
    for mask in range(1,(1<<n)-1):
        xs={x for x in vertices if mask>>x&1}
        inner={y for y in set(vertices)-xs if any(edge(y,x) in edges for x in xs)}
        labels={j for x in xs for j in L if rows[x]>>j&1}
        if len(inner)+len(labels)<7: return False
    return True


def connected(xs,edges):
    seen={next(iter(xs))}; stack=list(seen)
    while stack:
        x=stack.pop()
        for y in xs:
            if y not in seen and edge(x,y) in edges: seen.add(y); stack.append(y)
    return seen==set(xs)


def linked_frames(vertices,edges,rows):
    conn=[frozenset(x for x in vertices if mask>>x&1) for mask in range(1,1<<len(vertices))]
    conn=[x for x in conn if connected(x,edges)]
    bad=[]
    for j in U:
        ab=((j+1)%5,(j+2)%5); cd=((j+3)%5,(j+4)%5)
        xx=[x for x in conn if all(any(rows[v]>>q&1 for v in x) for q in ab)]
        yy=[x for x in conn if all(any(rows[v]>>q&1 for v in x) for q in cd)]
        if any(x.isdisjoint(y) for x in xx for y in yy): bad.append(j)
    return bad


def extends(vertices,edges,rows,state,*,delete_vertex=None,delete_edge=None,contract_edge=None):
    vv=tuple(x for x in vertices if x!=delete_vertex); ee=set(edges)
    if delete_edge is not None: ee.discard(delete_edge)
    if contract_edge is not None: ee.discard(contract_edge)
    bc={x:c for c,b in enumerate(state) for x in b}; col={}
    def ok(x,c):
        if contract_edge is not None and x in contract_edge:
            y=contract_edge[0] if x==contract_edge[1] else contract_edge[1]
            if y in col and col[y]!=c:return False
        if any(y in col and col[y]==c and edge(x,y) in ee for y in vv):return False
        return all(bc[j]!=c for j in L if rows[x]>>j&1)
    def dfs(left):
        if not left:return contract_edge is None or col[contract_edge[0]]==col[contract_edge[1]]
        x=max(left,key=lambda z:sum(edge(z,y) in ee for y in vv)); rest=tuple(y for y in left if y!=x)
        choices=range(6)
        if contract_edge is not None and x in contract_edge:
            y=contract_edge[0] if x==contract_edge[1] else contract_edge[1]
            if y in col:choices=(col[y],)
        for c in choices:
            if ok(x,c):
                col[x]=c
                if dfs(rest):return True
                del col[x]
        return False
    return dfs(vv)


def report(mult):
    vertices,edges,rows=instance(mult)
    if not cut_ok(vertices,edges,rows):return None
    bad=linked_frames(vertices,edges,rows)
    if bad:return None
    base={p for p in STATES if extends(vertices,edges,rows,p)}
    if base==set(STATES): return ("universal",len(base))
    unchanged=[]; tg=[]
    for ed in sorted(edges):
        for op in ("delete","contract"):
            kw={"delete_edge":ed} if op=="delete" else {"contract_edge":ed}
            now={p for p in STATES if extends(vertices,edges,rows,p,**kw)}; gain=now-base
            if now==base:unchanged.append((op,ed))
            if gain&TARGET:tg.append((op,ed,len(gain&TARGET)))
    for x in vertices:
        now={p for p in STATES if extends(vertices,edges,rows,p,delete_vertex=x)};gain=now-base
        if now==base:unchanged.append(("delete-v",x))
        if gain&TARGET:tg.append(("delete-v",x,len(gain&TARGET)))
    return ("nonuniversal",len(base),len(TARGET-base),unchanged,tg)


def comps(total,parts=5,prefix=()):
    if parts==1:yield prefix+(total,);return
    for x in range(1,total-parts+2):yield from comps(total-x,parts-1,prefix+(x,))


def main():
    print("states",len(STATES),"targets",len(TARGET))
    for n in (5,6,7,8,9,10,11):
        for mult in comps(n):
            ans=report(mult)
            if ans is not None:
                print(mult,ans)


if __name__=="__main__":main()
