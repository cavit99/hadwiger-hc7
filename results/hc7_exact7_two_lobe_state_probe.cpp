#include <array>
#include <cstdint>
#include <iostream>
#include <vector>

// Exhaustive seven-label probe for the two-lobe state mechanism.
// Vertices are 0,...,6.  A,B are the literal label sets contacted by the
// two lobes.  We test whether two adjacent carriers with contact sets A,B
// fund an admissible two-block state as in the audited carrier lemma.

static int ei[7][7];

static bool is_clique(int q, uint32_t e) {
  for (int i=0;i<7;i++) if (q&(1<<i))
    for (int j=i+1;j<7;j++) if (q&(1<<j))
      if (!(e&(1u<<ei[i][j]))) return false;
  return true;
}

static bool is_independent(int a, uint32_t e) {
  for (int i=0;i<7;i++) if (a&(1<<i))
    for (int j=i+1;j<7;j++) if (a&(1<<j))
      if (e&(1u<<ei[i][j])) return false;
  return true;
}

static bool sees_block(int q, int block, uint32_t e) {
  if (block&(1<<q)) return true;
  for (int x=0;x<7;x++) if ((block&(1<<x)) && (e&(1u<<ei[q][x]))) return true;
  return false;
}

static bool two_state(int A, int B, uint32_t e) {
  // Q is a literal clique; I,J are nontrivial independent blocks.
  for (int Q=0;Q<128;Q++) {
    if (!is_clique(Q,e)) continue;
    int rem=127^Q;
    for (int I=rem;I;I=(I-1)&rem) {
      int J=rem^I;
      if (__builtin_popcount((unsigned)I)<2 || __builtin_popcount((unsigned)J)<2) continue;
      if ((I&~A) || (J&~B)) continue;
      if (!is_independent(I,e) || !is_independent(J,e)) continue;
      bool ok=true;
      for (int q=0;q<7;q++) if (Q&(1<<q)) {
        if (!((A&(1<<q)) || sees_block(q,I,e))) ok=false;
        if (!((B&(1<<q)) || sees_block(q,J,e))) ok=false;
      }
      if (ok) return true;
    }
  }
  return false;
}

static bool one_state(uint32_t e) {
  for (int I=1;I<128;I++) {
    if (__builtin_popcount((unsigned)I)<2 || !is_independent(I,e)) continue;
    int Q=127^I;
    if (is_clique(Q,e)) return true;
  }
  return false;
}

int main() {
  int k=0;
  for (int i=0;i<7;i++) for (int j=i+1;j<7;j++) ei[i][j]=ei[j][i]=k++;
  std::vector<uint32_t> tris;
  for (int i=0;i<7;i++) for (int j=i+1;j<7;j++) for (int l=j+1;l<7;l++)
    tris.push_back((1u<<ei[i][j])|(1u<<ei[i][l])|(1u<<ei[j][l]));

  long long checked=0, bad=0;
  for (uint32_t e=0;e<(1u<<21);e++) {
    bool tf=true; for (auto t:tris) if ((e&t)==t) {tf=false;break;}
    if (!tf || one_state(e)) continue;
    for (int A=0;A<128;A++) if (__builtin_popcount((unsigned)A)>=4)
      for (int B=0;B<128;B++) if (__builtin_popcount((unsigned)B)>=4 && (A|B)==127) {
        checked++;
        if (!two_state(A,B,e) && !two_state(B,A,e)) {
          bad++;
          if (bad<=40) {
            std::cout << "counterexample e="<<e<<" A="<<A<<" B="<<B
                      <<" sizes="<<__builtin_popcount((unsigned)A)<<","<<__builtin_popcount((unsigned)B)
                      <<" overlap="<<__builtin_popcount((unsigned)(A&B))<<"\n";
            std::cout << "edges";
            for(int i=0;i<7;i++)for(int j=i+1;j<7;j++)if(e&(1u<<ei[i][j]))std::cout<<" "<<i<<j;
            std::cout<<"\n";
          }
        }
      }
  }
  std::cout << "checked="<<checked<<" bad="<<bad<<"\n";
}
