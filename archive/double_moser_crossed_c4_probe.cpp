// Probe the strict relative-eight crossed-C4 carrier obstruction.

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
static std::pair<int,int> edge(int a,int b){if(a>b)std::swap(a,b);return {a,b};}

template<int n> std::vector<Mask> find_k7(const std::set<std::pair<int,int>>& es){
 std::array<Mask,n> adj{}; for(auto [a,b]:es){adj[a]|=Mask(1)<<b;adj[b]|=Mask(1)<<a;}
 std::vector<Mask> con; std::array<Mask,1<<n> nb{};
 for(Mask m=1;m<(Mask(1)<<n);++m){Mask l=m&-m;int v=std::countr_zero(l);nb[m]=nb[m^l]|adj[v];Mask r=l;while(1){Mask x=r|(nb[r]&m);if(x==r)break;r=x;}if(r==m)con.push_back(m);}
 std::sort(con.begin(),con.end(),[](Mask a,Mask b){return std::popcount(a)!=std::popcount(b)?std::popcount(a)<std::popcount(b):a<b;});
 std::vector<Mask> ans;
 auto dfs=[&](auto&& self,int d,size_t st,Mask used)->bool{if(d==7)return true;for(size_t i=st;i<con.size();++i){Mask m=con[i];if(m&used)continue;bool ok=1;for(Mask z:ans)if(!(nb[m]&z))ok=0;if(!ok)continue;ans.push_back(m);if(self(self,d+1,i+1,used|m))return true;ans.pop_back();}return false;};
 if(dfs(dfs,0,0,0))return ans;return {};
}

static std::set<std::pair<int,int>> core(){
 constexpr int u=0,v=1,x1=2,x2=3,x3=4,x4=5,a=6,b=7,p=8,q=9;
 std::set<std::pair<int,int>> e;auto add=[&](int x,int y){e.insert(edge(x,y));};
 add(u,v);for(int x:{x1,x2,x3,x4,p,q})add(u,x);for(int x:{x1,x2,x3,x4,a,b})add(v,x);
 add(x1,x2);add(x3,x4);add(a,b);add(p,q);for(int x:{x1,x2}){add(a,x);add(q,x);}for(int x:{x3,x4}){add(b,x);add(p,x);}
 return e;
}

static void report(const char* label,const std::set<std::pair<int,int>>& e){
 auto m=find_k7<14>(e);const char* name[]={"u","v","x1","x2","x3","x4","a","b","p","q","r0","r1","r2","r3"};
 std::cout<<label<<": "<<(m.empty()?"no K7":"K7")<<'\n';for(Mask z:m){std::cout<<'{';for(int i=0;i<14;++i)if(z&(Mask(1)<<i))std::cout<<name[i]<<',';std::cout<<"}\n";}
}

int main(){
 constexpr int x1=2,x2=3,x3=4,x4=5,a=6,b=7,p=8,q=9;
 auto e=core();auto add=[&](int x,int y){e.insert(edge(x,y));};
 for(int i=0;i<4;++i){int r=10+i;add(r,10+(i+1)%4);for(int z:{a,b,p,q})add(r,z);}
 for(int i:{0,1})add(x1,10+i);for(int i:{2,3})add(x2,10+i);for(int i:{1,2})add(x3,10+i);for(int i:{0,3})add(x4,10+i);
 report("crossed C4",e);

 auto f=core();auto put=[&](int x,int y){f.insert(edge(x,y));};
 for(auto [i,j]:std::array<std::pair<int,int>,5>{{{0,1},{1,2},{2,3},{3,0},{0,2}}})put(10+i,10+j);
 std::array<int,8> labels{a,b,x1,x2,x3,x4,p,q};
 std::array<int,8> masks{14,14,14,1,9,3,15,15};
 for(int k=0;k<8;++k)for(int i=0;i<4;++i)if(masks[k]&(1<<i))put(labels[k],10+i);
 report("strict diamond",f);
}
