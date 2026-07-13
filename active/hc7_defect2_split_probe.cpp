#include <array>
#include <cstdint>
#include <iostream>
#include <vector>

// Discovery probe only.  It tests whether the elementary two-anchor K7
// construction or a carrier-aligned two-block state closes every
// triangle-free seven-boundary split with two defect sets of order <=2.

int main() {
    std::array<std::array<int,7>,7> eb{};
    int z=0;
    for(int i=0;i<7;i++) for(int j=i+1;j<7;j++) eb[i][j]=eb[j][i]=z++;
    auto edge=[&](std::uint32_t g,int i,int j){return i!=j && (g&(1u<<eb[i][j]));};
    std::vector<int> defects;
    for(int m=0;m<(1<<7);m++) if(__builtin_popcount((unsigned)m)<=2) defects.push_back(m);
    std::uint64_t survivors=0;
    for(std::uint32_t g=0;g<(1u<<21);g++) {
        bool tf=true;
        for(int a=0;a<7;a++) for(int b=a+1;b<7;b++) for(int c=b+1;c<7;c++)
            if(edge(g,a,b)&&edge(g,a,c)&&edge(g,b,c)) tf=false;
        if(!tf) continue;

        bool oneblock=false;
        for(int q=0;q<(1<<7);q++) {
            if(__builtin_popcount((unsigned)q)>2) continue;
            bool qc=true, ii=true;
            for(int i=0;i<7;i++) for(int j=i+1;j<7;j++) {
                if((q>>i&1)&&(q>>j&1)&&!edge(g,i,j)) qc=false;
                if(!(q>>i&1)&&!(q>>j&1)&&edge(g,i,j)) ii=false;
            }
            if(qc&&ii&&7-__builtin_popcount((unsigned)q)>=2) oneblock=true;
        }
        if(oneblock) continue;

        for(int A:defects) for(int B:defects) {
            bool repair=false;
            for(int q=0;q<7;q++) for(int r=q+1;r<7;r++) if(edge(g,q,r)) {
                for(int x=0;x<7;x++) if(x!=q&&x!=r&&!(A>>x&1)) {
                    if(((A>>q&1)&&!edge(g,x,q))||((A>>r&1)&&!edge(g,x,r))) continue;
                    for(int y=0;y<7;y++) if(y!=q&&y!=r&&y!=x&&!(B>>y&1)) {
                        if(((B>>q&1)&&!edge(g,y,q))||((B>>r&1)&&!edge(g,y,r))) continue;
                        repair=true;
                    }
                }
            }
            if(repair) continue;

            bool aligned=false;
            for(int X=0;X<(1<<7);X++) {
                int Y=((1<<7)-1)^X;
                if(__builtin_popcount((unsigned)X)<2||__builtin_popcount((unsigned)Y)<2) continue;
                if(A&X) continue; // X-carrier cannot connect a missed X label
                if(B&Y) continue;
                bool ind=true;
                for(int i=0;i<7;i++) for(int j=i+1;j<7;j++)
                    if((((X>>i&1)&&(X>>j&1))||((Y>>i&1)&&(Y>>j&1)))&&edge(g,i,j)) ind=false;
                if(ind) aligned=true;
            }
            if(aligned) continue;
            survivors++;
            if(survivors<=20)
                std::cout<<"survivor g="<<g<<" A="<<A<<" B="<<B<<"\n";
        }
    }
    std::cout<<"survivors="<<survivors<<"\n";
}
