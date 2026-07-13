#include <algorithm>
#include <array>
#include <atomic>
#include <bit>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <mutex>
#include <set>
#include <thread>
#include <utility>
#include <vector>

namespace {
constexpr int N=4, K=6, FULL=(1<<N)-1;
struct GraphCase { int atlas; std::vector<std::pair<int,int>> edges; };
const std::array<GraphCase,3> CASES={{
  {16,{{0,1},{0,3},{1,2},{2,3}}},
  {17,{{0,1},{0,2},{0,3},{1,2},{2,3}}},
  {18,{{0,1},{0,2},{0,3},{1,2},{1,3},{2,3}}}
}};
std::mutex out_mutex;
std::atomic<std::uint64_t> total_actual{0};

std::uint32_t graph_code(const std::vector<std::pair<int,int>>& edges,
                         const std::array<int,N>& permutation){
 std::uint32_t code=0;for(auto[u,v]:edges){int a=permutation[u],b=permutation[v];if(a>b)std::swap(a,b);code|=1u<<(a*N+b);}return code;}
std::uint32_t canonical_graph_code(const std::vector<std::pair<int,int>>& edges){
 std::array<int,N>p={0,1,2,3};std::uint32_t best=~0u;do{best=std::min(best,graph_code(edges,p));}while(std::next_permutation(p.begin(),p.end()));return best;}
bool biconnected(const std::vector<std::pair<int,int>>& edges){std::array<int,N>a{};for(auto[u,v]:edges){a[u]|=1<<v;a[v]|=1<<u;}
 for(int removed=-1;removed<N;++removed){int allowed=FULL;if(removed>=0)allowed^=1<<removed;int reached=allowed&-allowed;
  while(1){int expanded=reached;for(int v=0;v<N;++v)if(reached>>v&1)expanded|=a[v]&allowed;if(expanded==reached)break;reached=expanded;}if(reached!=allowed)return false;}return true;}
void verify_graph_list(){const std::array<std::pair<int,int>,6>E={{{0,1},{0,2},{0,3},{1,2},{1,3},{2,3}}};std::set<std::uint32_t>generated,listed;
 for(int m=0;m<(1<<6);++m){std::vector<std::pair<int,int>>e;for(int i=0;i<6;++i)if(m>>i&1)e.push_back(E[i]);if(biconnected(e))generated.insert(canonical_graph_code(e));}
 for(auto&g:CASES)listed.insert(canonical_graph_code(g.edges));if(generated!=listed||listed.size()!=3){std::cerr<<"incomplete order-four graph list\n";std::abort();}}

bool bad(int l,int r){
 const std::array<int,2>T={0b010101,0b101010};
 const std::array<int,3>M={0b001001,0b010010,0b100100};
 auto d=[&](int a,int b){return(l&a)==a&&(r&b)==b;};
 for(int x:T)if(d(0,x)||d(x,0))return true;
 for(int x:M){int f=0b111111^x;if(d(0,f)||d(f,0))return true;}
 for(int v=0;v<6;++v){int a=1<<v,b=(1<<((v+5)%6))|(1<<((v+1)%6));
  if(d(a,b)||d(b,a))return true;}
 for(int i=0;i<3;++i)for(int j=0;j<3;++j)if(i!=j&&d(M[i],M[j]))return true;
 return false;
}

struct Search{
 GraphCase g; std::array<int,N> adj{},deg{}; std::array<bool,1<<N> conn{};
 std::array<std::array<std::vector<int>,1<<N>,1<<N> pieces;
 std::vector<int> splits,reps; std::array<int,K> p{};
 std::uint64_t assignments=0,linkage=0,actual=0;
 explicit Search(GraphCase x):g(std::move(x)){
  for(auto[u,v]:g.edges){adj[u]|=1<<v;adj[v]|=1<<u;++deg[u];++deg[v];}
  for(int m=1;m<=FULL;++m){int r=m&-m;while(1){int e=r;for(int v=0;v<N;++v)if(r>>v&1)e|=adj[v]&m;if(e==r)break;r=e;}conn[m]=r==m;}
  for(int a=1;a<=FULL;++a)for(int b=1;b<=FULL;++b)for(int m=1;m<=FULL;++m)
   if(conn[m]&&(m&a)&&(m&b))pieces[a][b].push_back(m);
  for(int m=1;m<FULL;++m)if(conn[m]&&conn[FULL^m])splits.push_back(m);
  std::vector<std::array<int,N>> aut;std::array<int,N> q={0,1,2,3};
  do{bool ok=true;for(int i=0;i<N;++i)for(int j=i+1;j<N;++j)
   if(((adj[i]>>j)&1)!=((adj[q[i]]>>q[j])&1))ok=false;if(ok)aut.push_back(q);
  }while(std::next_permutation(q.begin(),q.end()));
  std::set<int>seen;for(int m=1;m<=FULL;++m)if(!seen.count(m)){int z=FULL;
   for(auto&a:aut){int im=0;for(int v=0;v<N;++v)if(m>>v&1)im|=1<<a[v];seen.insert(im);z=std::min(z,im);}reps.push_back(z);}
 }
 bool two(int a,int b,int c,int d,int oa=-1,int ob=-1){for(int x:pieces[p[a]][p[b]])for(int y:pieces[p[c]][p[d]])
  if(!(x&y)&&(oa<0||(x&p[oa])||(y&p[ob])))return true;return false;}
 bool three(int s){auto&A=pieces[p[s]][p[(s+1)%6]],&B=pieces[p[(s+2)%6]][p[(s+3)%6]],&C=pieces[p[(s+4)%6]][p[(s+5)%6]];
  for(int x:A)for(int y:B)if(!(x&y))for(int z:C)if(!(x&z)&&!(y&z))return true;return false;}
 bool signature(){std::array<bool,6>f{},u{};for(int i=0;i<6;++i){f[i]=two((i+4)%6,(i+5)%6,(i+2)%6,(i+3)%6);u[i]=two((i+4)%6,(i+5)%6,(i+2)%6,(i+3)%6,i,(i+1)%6);}
  int o=0;for(int i=0;i<3;++i)o+=f[i]&&f[i+3];if(o<2)return false;
  for(int i=0;i<3;++i)if(two(i,(i+1)%6,(i+3)%6,(i+4)%6))return false;
  if(three(0)||three(1))return false;for(int i=0;i<6;++i)if(f[i]&&u[i])return false;return true;}
 bool with_z(int zm){std::array<int,N>row{};for(int i=0;i<6;++i)for(int v=0;v<N;++v)if(p[i]>>v&1)row[v]|=1<<i;
  for(int v=0;v<N;++v){if(zm>>v&1)row[v]|=1<<6;if(deg[v]+std::popcount((unsigned)row[v])<7)return false;}
  for(int s:splits){int l=0,r=0;for(int v=0;v<N;++v)if(s>>v&1)l|=row[v];else r|=row[v];if(!bad(0b1111111^l,0b1111111^r))return false;}return true;}
 void rec(int i,int minsz){if(i==6){++assignments;if(!signature())return;++linkage;for(int z=1;z<=FULL;++z)if(with_z(z)){++actual;++total_actual;std::lock_guard<std::mutex>L(out_mutex);std::cout<<"SURVIVOR "<<g.atlas<<'\n';return;}return;}
  for(int m=1;m<=FULL;++m)if(std::popcount((unsigned)m)>=minsz){p[i]=m;rec(i+1,minsz);}}
 void run(){for(int x:reps){p[0]=x;rec(1,std::popcount((unsigned)x));}std::lock_guard<std::mutex>L(out_mutex);
  std::cout<<"graph "<<g.atlas<<" reps "<<reps.size()<<" assignments "<<assignments<<" linkage "<<linkage<<" actual "<<actual<<'\n';}
};
}
int main(){verify_graph_list();std::vector<std::thread>w;for(auto g:CASES)w.emplace_back([g]{Search(g).run();});for(auto&t:w)t.join();return total_actual==0?0:1;}
