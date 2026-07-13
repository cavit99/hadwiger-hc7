#include <algorithm>
#include <array>
#include <atomic>
#include <bit>
#include <cassert>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <mutex>
#include <set>
#include <thread>
#include <utility>
#include <vector>

namespace {

constexpr int N = 5;
constexpr int K = 6;
constexpr int FULL = (1 << N) - 1;

struct GraphCase {
  int atlas_index;
  std::vector<std::pair<int, int>> edges;
};

const std::array<GraphCase, 10> CASES = {{
    {38, {{0,1},{0,4},{1,2},{2,3},{3,4}}},
    {43, {{0,1},{0,3},{0,4},{1,2},{2,3},{3,4}}},
    {44, {{0,2},{0,3},{0,4},{1,2},{1,3},{1,4}}},
    {46, {{0,3},{0,4},{1,3},{1,4},{2,3},{2,4},{3,4}}},
    {47, {{0,1},{0,4},{1,2},{1,3},{1,4},{2,3},{3,4}}},
    {48, {{0,2},{0,3},{0,4},{1,2},{1,3},{1,4},{2,4}}},
    {49, {{0,1},{0,3},{0,4},{1,3},{1,4},{2,3},{2,4},{3,4}}},
    {50, {{0,1},{0,3},{0,4},{1,2},{1,4},{2,3},{2,4},{3,4}}},
    {51, {{0,1},{0,3},{0,4},{1,2},{1,3},{1,4},{2,3},{2,4},{3,4}}},
    {52, {{0,1},{0,2},{0,3},{0,4},{1,2},{1,3},{1,4},{2,3},{2,4},{3,4}}},
}};

std::mutex output_mutex;
std::atomic<std::uint64_t> total_actual{0};

std::uint32_t graph_code(const std::vector<std::pair<int,int>>& edges,
                         const std::array<int,N>& permutation) {
  std::uint32_t code = 0;
  for (auto [u,v] : edges) {
    int a = permutation[u], b = permutation[v];
    if (a > b) std::swap(a,b);
    code |= 1u << (a*N+b);
  }
  return code;
}

std::uint32_t canonical_graph_code(
    const std::vector<std::pair<int,int>>& edges) {
  std::array<int,N> p={0,1,2,3,4};
  std::uint32_t best=~0u;
  do { best=std::min(best,graph_code(edges,p)); }
  while(std::next_permutation(p.begin(),p.end()));
  return best;
}

bool biconnected(const std::vector<std::pair<int,int>>& edges) {
  std::array<int,N> a{};
  for(auto[u,v]:edges){a[u]|=1<<v;a[v]|=1<<u;}
  for(int removed=-1;removed<N;++removed){
    int allowed=FULL;
    if(removed>=0)allowed^=1<<removed;
    int reached=allowed&-allowed;
    while(true){int expanded=reached;for(int v=0;v<N;++v)
      if(reached>>v&1)expanded|=a[v]&allowed;
      if(expanded==reached)break;reached=expanded;}
    if(reached!=allowed)return false;
  }
  return true;
}

void verify_graph_list() {
  const std::array<std::pair<int,int>,10> all_edges={{{0,1},{0,2},{0,3},{0,4},
    {1,2},{1,3},{1,4},{2,3},{2,4},{3,4}}};
  std::set<std::uint32_t> generated, listed;
  for(int mask=0;mask<(1<<10);++mask){
    std::vector<std::pair<int,int>> edges;
    for(int i=0;i<10;++i)if(mask>>i&1)edges.push_back(all_edges[i]);
    if(biconnected(edges))generated.insert(canonical_graph_code(edges));
  }
  for(const auto& item:CASES)listed.insert(canonical_graph_code(item.edges));
  if(generated!=listed || listed.size()!=10){
    std::cerr << "incomplete order-five graph list\n";
    std::abort();
  }
}

bool dominates_bad_defect(int left, int right) {
  const std::array<int, 2> triangles = {0b010101, 0b101010};
  const std::array<int, 3> matching = {0b001001, 0b010010, 0b100100};
  auto dominates = [&](int a, int b) {
    return (left & a) == a && (right & b) == b;
  };
  for (int t : triangles)
    if (dominates(0, t) || dominates(t, 0)) return true;
  for (int m : matching) {
    int four = 0b111111 ^ m;
    if (dominates(0, four) || dominates(four, 0)) return true;
  }
  for (int v = 0; v < 6; ++v) {
    int one = 1 << v;
    int nf = (1 << ((v + 5) % 6)) | (1 << ((v + 1) % 6));
    if (dominates(one, nf) || dominates(nf, one)) return true;
  }
  for (int i = 0; i < 3; ++i)
    for (int j = 0; j < 3; ++j)
      if (i != j && dominates(matching[i], matching[j])) return true;
  return false;
}

struct Search {
  GraphCase graph;
  std::array<int, N> adjacency{};
  std::array<int, N> degree{};
  std::array<bool, 1 << N> connected{};
  std::array<std::array<std::vector<int>, 1 << N>, 1 << N> pieces;
  std::vector<int> split_sides;
  std::vector<int> first_representatives;
  std::array<int, K> portals{};
  std::uint64_t assignments = 0;
  std::uint64_t linkage_survivors = 0;
  std::uint64_t actual_survivors = 0;

  explicit Search(GraphCase input) : graph(std::move(input)) {
    for (auto [u, v] : graph.edges) {
      adjacency[u] |= 1 << v;
      adjacency[v] |= 1 << u;
      ++degree[u]; ++degree[v];
    }
    for (int mask = 1; mask <= FULL; ++mask) {
      int reached = mask & -mask;
      while (true) {
        int expanded = reached;
        for (int v = 0; v < N; ++v)
          if ((reached >> v) & 1) expanded |= adjacency[v] & mask;
        if (expanded == reached) break;
        reached = expanded;
      }
      connected[mask] = reached == mask;
    }
    for (int a = 1; a <= FULL; ++a)
      for (int b = 1; b <= FULL; ++b)
        for (int mask = 1; mask <= FULL; ++mask)
          if (connected[mask] && (mask & a) && (mask & b))
            pieces[a][b].push_back(mask);
    for (int side = 1; side < FULL; ++side)
      if (connected[side] && connected[FULL ^ side]) split_sides.push_back(side);
    compute_first_representatives();
  }

  void compute_first_representatives() {
    std::vector<std::array<int, N>> automorphisms;
    std::array<int, N> p = {0,1,2,3,4};
    do {
      bool okay = true;
      for (int i = 0; i < N; ++i)
        for (int j = i + 1; j < N; ++j)
          if (((adjacency[i] >> j) & 1) != ((adjacency[p[i]] >> p[j]) & 1))
            okay = false;
      if (okay) automorphisms.push_back(p);
    } while (std::next_permutation(p.begin(), p.end()));

    std::set<int> seen;
    for (int mask = 1; mask <= FULL; ++mask) {
      if (seen.count(mask)) continue;
      int representative = FULL;
      for (const auto& a : automorphisms) {
        int image = 0;
        for (int v = 0; v < N; ++v) if ((mask >> v) & 1) image |= 1 << a[v];
        seen.insert(image);
        representative = std::min(representative, image);
      }
      first_representatives.push_back(representative);
    }
  }

  bool has_two(int a, int b, int c, int d, int out_a = -1, int out_b = -1) {
    for (int x : pieces[portals[a]][portals[b]])
      for (int y : pieces[portals[c]][portals[d]])
        if (!(x & y) && (out_a < 0 || (x & portals[out_a]) ||
                                      (y & portals[out_b]))) return true;
    return false;
  }

  bool has_three(int parity) {
    const auto& a = pieces[portals[parity]][portals[(parity + 1) % 6]];
    const auto& b = pieces[portals[(parity + 2) % 6]][portals[(parity + 3) % 6]];
    const auto& c = pieces[portals[(parity + 4) % 6]][portals[(parity + 5) % 6]];
    for (int x : a) for (int y : b) if (!(x & y))
      for (int z : c) if (!(x & z) && !(y & z)) return true;
    return false;
  }

  bool linkage_signature() {
    std::array<bool, 6> frame{}, unlock{};
    for (int i = 0; i < 6; ++i) {
      frame[i] = has_two((i+4)%6,(i+5)%6,(i+2)%6,(i+3)%6);
      unlock[i] = has_two((i+4)%6,(i+5)%6,(i+2)%6,(i+3)%6,i,(i+1)%6);
    }
    int opposite = 0;
    for (int i = 0; i < 3; ++i) opposite += frame[i] && frame[i+3];
    if (opposite < 2) return false;
    for (int i = 0; i < 3; ++i)
      if (has_two(i,(i+1)%6,(i+3)%6,(i+4)%6)) return false;
    if (has_three(0) || has_three(1)) return false;
    for (int i = 0; i < 6; ++i) if (frame[i] && unlock[i]) return false;
    return true;
  }

  bool actual_with_z(int zmask) {
    std::array<int, N> rows{};
    for (int label = 0; label < 6; ++label)
      for (int v = 0; v < N; ++v)
        if ((portals[label] >> v) & 1) rows[v] |= 1 << label;
    for (int v = 0; v < N; ++v) {
      if ((zmask >> v) & 1) rows[v] |= 1 << 6;
      if (degree[v] + std::popcount(static_cast<unsigned>(rows[v])) < 7)
        return false;
    }
    for (int side : split_sides) {
      int left = 0, right = 0;
      for (int v = 0; v < N; ++v)
        if ((side >> v) & 1) left |= rows[v]; else right |= rows[v];
      int dl = 0b1111111 ^ left, dr = 0b1111111 ^ right;
      if (!dominates_bad_defect(dl, dr)) return false;
    }
    return true;
  }

  bool hall_prefix(int index) {
    // Test only subfamilies containing the newly assigned class.  The
    // full six-class family is deliberately deficient on five vertices.
    int newest = 1 << index;
    for (int labels = newest; labels < (1 << (index + 1)); ++labels) {
      if (!(labels & newest)) continue;
      if (index == 5 && labels == 0b111111) continue;
      int united = 0;
      for (int i = 0; i <= index; ++i) if ((labels >> i) & 1) united |= portals[i];
      if (std::popcount(static_cast<unsigned>(united)) <
          std::popcount(static_cast<unsigned>(labels))) return false;
    }
    return true;
  }

  void recurse(int index, int minimum_size) {
    if (index == 6) {
      ++assignments;
      int united = 0; for (int p : portals) united |= p;
      if (united != FULL) return;
      if (!linkage_signature()) return;
      ++linkage_survivors;
      for (int z = 1; z <= FULL; ++z) {
        if (actual_with_z(z)) {
          ++actual_survivors;
          ++total_actual;
          std::lock_guard<std::mutex> lock(output_mutex);
          std::cout << "SURVIVOR graph " << graph.atlas_index << " portals";
          for (int p : portals) std::cout << ' ' << p;
          std::cout << " z " << z << '\n';
          return;
        }
      }
      return;
    }
    for (int mask = 1; mask <= FULL; ++mask) {
      if (std::popcount(static_cast<unsigned>(mask)) < minimum_size) continue;
      portals[index] = mask;
      if (hall_prefix(index)) recurse(index + 1, minimum_size);
    }
  }

  void run() {
    for (int first : first_representatives) {
      portals[0] = first;
      recurse(1, std::popcount(static_cast<unsigned>(first)));
    }
    std::lock_guard<std::mutex> lock(output_mutex);
    std::cout << "graph " << graph.atlas_index
              << " representatives " << first_representatives.size()
              << " Hall assignments " << assignments
              << " linkage survivors " << linkage_survivors
              << " actual survivors " << actual_survivors << '\n';
  }
};

}  // namespace

int main() {
  verify_graph_list();
  std::vector<std::thread> workers;
  for (const auto& graph : CASES)
    workers.emplace_back([graph] { Search(graph).run(); });
  for (auto& worker : workers) worker.join();
  return total_actual == 0 ? 0 : 1;
}
