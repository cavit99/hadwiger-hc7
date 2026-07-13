// Test the minimal planar Kempe-theta forced by a clean a-p blocker.
// Two q-b paths run through the singleton-colour roots x2 and x4;
// optionally a reverse-trace x1-x3 carrier is added.

#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <set>
#include <utility>
#include <vector>

using Mask = uint16_t;
using Edge = std::pair<int,int>;
static Edge edge(int a,int b){if(a>b)std::swap(a,b);return {a,b};}

template<int n>
static std::vector<Mask> find_k7(const std::set<Edge>& edges){
  std::array<Mask,n> adj{};
  for(auto [a,b]:edges){adj[a]|=Mask(1)<<b;adj[b]|=Mask(1)<<a;}
  std::array<Mask,1<<n> nb{};
  std::vector<Mask> conn;
  for(Mask m=1;m<(Mask(1)<<n);++m){
    Mask low=m&-m; nb[m]=nb[m^low]|adj[std::countr_zero(low)];
    Mask r=low;
    while(true){Mask s=r|(nb[r]&m);if(s==r)break;r=s;}
    if(r==m)conn.push_back(m);
  }
  std::sort(conn.begin(),conn.end(),[](Mask a,Mask b){
    return std::popcount(a)!=std::popcount(b)?
      std::popcount(a)<std::popcount(b):a<b;
  });
  auto dfs=[&](auto&& self,int d,std::vector<int> cand,Mask used,
               std::vector<Mask> chosen)->std::vector<Mask>{
    if(d==7)return chosen;
    int need=7-d;
    for(size_t i=0;i<cand.size();++i){
      Mask bag=conn[cand[i]]; if(bag&used)continue;
      std::vector<int> next;
      for(size_t j=i+1;j<cand.size();++j){
        Mask other=conn[cand[j]];
        if(!(other&(used|bag))&&(nb[bag]&other))next.push_back(cand[j]);
      }
      if((int)next.size()<need-1)continue;
      auto c=chosen;c.push_back(bag);
      auto ans=self(self,d+1,std::move(next),used|bag,std::move(c));
      if(!ans.empty())return ans;
    }
    return {};
  };
  std::vector<int> all(conn.size());std::iota(all.begin(),all.end(),0);
  return dfs(dfs,0,std::move(all),0,{});
}

int main(){
  // u,v,x1,x2,x3,x4,a,b,p,q,t,r,s,z
  enum {u,v,x1,x2,x3,x4,a,b,p,q,t,r,s,z,N};
  static_assert(N==14);
  const std::array<const char*,N> name{
    "u","v","x1","x2","x3","x4","a","b","p","q",
    "t","r","s","z"};
  std::set<Edge> E;
  auto add=[&](int x,int y){E.insert(edge(x,y));};
  add(u,v);
  for(int x:{x1,x2,x3,x4,p,q})add(u,x);
  for(int x:{x1,x2,x3,x4,a,b})add(v,x);
  for(auto [i,j]:std::array<Edge,12>{{
    {x1,x2},{x3,x4},{a,b},{p,q},{a,x1},{a,x2},
    {b,x3},{b,x4},{p,x3},{p,x4},{q,x1},{q,x2}}})add(i,j);
  // Clean reserved connector a-t-p.
  add(a,t);add(t,p);
  // Two internally disjoint q-b arcs through x2 and x4.
  add(x2,r);add(r,b);               // q-x2 is fixed
  add(q,s);add(s,x4);               // x4-b is fixed
  for(int reverse=0;reverse<2;++reverse){
    auto F=E;
    if(reverse){F.insert(edge(x1,z));F.insert(edge(z,x3));}
    auto model=find_k7<N>(F);
    std::cout<<"reverse="<<reverse<<" K7="<<(!model.empty())<<'\n';
    for(Mask bag:model){
      std::cout<<"{";
      for(int i=0;i<N;++i)if(bag&(Mask(1)<<i))std::cout<<name[i]<<",";
      std::cout<<"}";
    }
    std::cout<<'\n';
  }

  // Complementary-blocker four-path lock.  Reuse r as the intersection
  // of P(x2,b) with Zu(x1,x3), and s as the intersection of Q(q,x4)
  // with Zv(x1,x3).  Delete the earlier theta edges first.
  auto C=E;
  for(auto e0:std::array<Edge,6>{{
      {x2,r},{r,b},{q,s},{s,x4},{x1,z},{z,x3}}}) C.erase(edge(e0.first,e0.second));
  C.insert(edge(q,s));C.insert(edge(s,x4));
  C.insert(edge(x1,s));C.insert(edge(s,x3));
  C.insert(edge(x2,r));C.insert(edge(r,b));
  C.insert(edge(x1,r));C.insert(edge(r,x3));
  auto locked=find_k7<N>(C);
  std::cout<<"complementary_lock K7="<<(!locked.empty())<<'\n';
  for(Mask bag:locked){
    std::cout<<"{";
    for(int i=0;i<N;++i)if(bag&(Mask(1)<<i))std::cout<<name[i]<<",";
    std::cout<<"}";
  }
  std::cout<<'\n';
}
