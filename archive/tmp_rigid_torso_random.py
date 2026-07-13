exec(open('tmp_rigid_qfull_counter.py').read().split('for n,D in')[0])
import random

def universal_gate(D,P,typ):
 qs=['q1','q2','q3'];L=connsets(D,qs+(['a','b'] if typ==0 else ['a','c']));R=connsets(D,qs+['b','c'])
 for fam in (L,R):
  for r in (1,2):
   for Z in map(set,__import__('itertools').combinations(D,r)):
    if all(Z&S for S in fam): return Z
 return None

for n in range(4,10):
 for it in range(12000):
  D=nx.gnp_random_graph(n,random.uniform(.25,.9))
  if not nx.is_biconnected(D):continue
  P={z:{v for v in D if random.random()<random.uniform(.2,.8)} for z in ['q1','q2','q3','a','b','c']}
  if not all(P.values()):continue
  if ext(D,P,'AB') and not ext(D,P,'AC') and not fullsplit(D,P,0) and not universal_gate(D,P,0):
   print('FOUND',n,sorted(D.edges()),{z:sorted(P[z]) for z in P},'type1',fullsplit(D,P,1));raise SystemExit
print('none')
