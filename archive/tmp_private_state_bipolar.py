import itertools
V=range(6);X={0,1,2};Y={3,4,5}
def parts(S):
 if not S:return [()]
 a=min(S);out=[]
 for P in parts(set(S)-{a}):
  # new block
  out.append((frozenset({a}),)+P)
  for i in range(len(P)):
   Q=list(P);Q[i]=Q[i]|{a};out.append(tuple(Q))
 # canon dedup
 return list({tuple(sorted(p,key=lambda z:min(z))) for p in out})
PX=parts(X);PY=parts(Y)
states=[]
for x in PX:
 for y in PY:
  st=tuple(sorted(x+y+(frozenset({6}),),key=lambda z:min(z)))
  if len(st)<=6:states.append(st)
states=list(dict.fromkeys(states))
req=[]
for side in [X,Y]:
 for r in range(1,4):
  for P in map(frozenset,itertools.combinations(side,r)):
   req.append((P,[i for i,s in enumerate(states) if P in s]))
print('states',len(states),'req sizes',[(tuple(P),len(I)) for P,I in req])
# backtrack 2-color all states such each req both; z3 system
import z3
c=[z3.Bool(f'c{i}') for i in range(len(states))]
sol=z3.Solver()
for P,I in req:
 sol.add(z3.Or(*[c[i] for i in I]));sol.add(z3.Or(*[z3.Not(c[i]) for i in I]))
print(sol.check())
if sol.check()==z3.sat:
 m=sol.model()
 for val in [False,True]:
  print('FAM',val)
  for i,s in enumerate(states):
   if z3.is_true(m.eval(c[i]))==val:print(i,[sorted(b) for b in s])
