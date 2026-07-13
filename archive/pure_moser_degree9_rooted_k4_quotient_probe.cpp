// Adversarial quotient probe for the degree-nine pure-Moser hub.
// The four E roots are made a literal K4 (stronger than a rooted model)
// and each is assigned a minimal portal type: complete to H1={1,2},
// complete to H2={3,4}, or complete to both.  Enumerate all 3^4 types.

#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <set>
#include <utility>
#include <vector>

using Mask=uint16_t;using Edge=std::pair<int,int>;
static Edge edge(int a,int b){if(a>b)std::swap(a,b);return{a,b};}

template<int n> static std::vector<Mask> find_k7(const std::set<Edge>& E){
 std::array<Mask,n>a{};for(auto[x,y]:E){a[x]|=Mask(1)<<y;a[y]|=Mask(1)<<x;}
 std::array<Mask,1<<n>nb{};std::vector<Mask>c;
 for(Mask m=1;m<(Mask(1)<<n);++m){Mask l=m&-m;nb[m]=nb[m^l]|a[std::countr_zero(l)];Mask r=l;while(1){Mask s=r|(nb[r]&m);if(s==r)break;r=s;}if(r==m)c.push_back(m);}
 std::sort(c.begin(),c.end(),[](Mask x,Mask y){return std::popcount(x)!=std::popcount(y)?std::popcount(x)<std::popcount(y):x<y;});
 auto go=[&](auto&&self,int d,std::vector<int>q,Mask used,std::vector<Mask>chosen)->std::vector<Mask>{if(d==7)return chosen;int need=7-d;for(size_t i=0;i<q.size();++i){Mask b=c[q[i]];if(b&used)continue;std::vector<int>nq;for(size_t j=i+1;j<q.size();++j){Mask o=c[q[j]];if(!(o&(used|b))&&(nb[b]&o))nq.push_back(q[j]);}if((int)nq.size()>=need-1){auto nc=chosen;nc.push_back(b);auto ans=self(self,d+1,std::move(nq),used|b,std::move(nc));if(!ans.empty())return ans;}}return {};};
 std::vector<int>q(c.size());std::iota(q.begin(),q.end(),0);return go(go,0,std::move(q),0,{});
}

int main(){
 // v,h,1,2,3,4,5,6,e0,e1,e2,e3
 enum{v,h,x1,x2,x3,x4,x5,x6,e0,e1,e2,e3,N};static_assert(N==12);
 std::set<Edge> base;auto add=[&](int x,int y){base.insert(edge(x,y));};
 for(int x:{h,x1,x2,x3,x4,x5,x6})add(v,x);
 for(auto [x,y]:std::array<Edge,11>{{{h,x1},{h,x2},{h,x3},{h,x4},{x1,x2},{x1,x6},{x2,x6},{x3,x4},{x3,x5},{x4,x5},{x5,x6}}})add(x,y);
 for(int e:{e0,e1,e2,e3})add(h,e);
 for(int i=e0;i<=e3;++i)for(int j=i+1;j<=e3;++j)add(i,j);
 int positive=0,negative=0;
 for(int code=0;code<81;++code){int z=code;auto E=base;std::array<int,4>t{};for(int i=0;i<4;++i){t[i]=z%3;z/=3;int e=e0+i;if(t[i]!=1){E.insert(edge(e,x1));E.insert(edge(e,x2));}if(t[i]!=0){E.insert(edge(e,x3));E.insert(edge(e,x4));}}
   auto model=find_k7<N>(E);
   if(!model.empty()){
     ++positive;
     if(code==0||code==1+3+9||code==1+3){
       static const std::array<const char*,N> nm{"v","h","1","2","3","4","5","6","E0","E1","E2","E3"};
       std::cout<<"model";for(int x:t)std::cout<<' '<<x;std::cout<<":";
       for(Mask b:model){std::cout<<" {";for(int i=0;i<N;++i)if(b&(Mask(1)<<i))std::cout<<nm[i]<<',';std::cout<<'}';}std::cout<<'\n';
     }
   }else{++negative;std::cout<<"negative";for(int x:t)std::cout<<' '<<x;std::cout<<'\n';}
 }
 std::cout<<"positive="<<positive<<" negative="<<negative<<'\n';
}
