#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <vector>

using Bags = std::array<uint16_t, 7>;

static std::vector<Bags> candidates;

static void partition_rec(const std::vector<int>& support, int index,
                          std::vector<uint16_t>& blocks) {
  if (index == static_cast<int>(support.size())) {
    if (blocks.size() == 7) {
      Bags bags{};
      std::copy(blocks.begin(), blocks.end(), bags.begin());
      candidates.push_back(bags);
    }
    return;
  }
  const uint16_t bit = uint16_t(1) << support[index];
  for (size_t i = 0; i < blocks.size(); ++i) {
    blocks[i] |= bit;
    partition_rec(support, index + 1, blocks);
    blocks[i] ^= bit;
  }
  if (blocks.size() < 7) {
    blocks.push_back(bit);
    partition_rec(support, index + 1, blocks);
    blocks.pop_back();
  }
}

static void build_candidates() {
  for (int mask = 0; mask < (1 << 12); ++mask) {
    if (__builtin_popcount(mask) < 7) continue;
    std::vector<int> support;
    for (int v = 0; v < 12; ++v)
      if (mask & (1 << v)) support.push_back(v);
    std::vector<uint16_t> blocks;
    blocks.push_back(uint16_t(1) << support[0]);
    partition_rec(support, 1, blocks);
  }
  std::sort(candidates.begin(), candidates.end(), [](const Bags& a,
                                                       const Bags& b) {
    int sa = 0, sb = 0;
    for (int i = 0; i < 7; ++i) {
      sa += __builtin_popcount(a[i]);
      sb += __builtin_popcount(b[i]);
    }
    return sa > sb;
  });
}

static bool connected(uint16_t mask, const std::array<uint16_t, 12>& adj) {
  uint16_t reached = mask & -mask;
  while (true) {
    uint16_t expanded = reached;
    uint16_t bits = reached;
    while (bits) {
      uint16_t low = bits & -bits;
      int v = __builtin_ctz(bits);
      expanded |= adj[v] & mask;
      bits ^= low;
    }
    if (expanded == reached) return reached == mask;
    reached = expanded;
  }
}

static bool has_k7(const std::array<uint16_t, 12>& adj) {
  for (const Bags& bags : candidates) {
    bool ok = true;
    std::array<uint16_t, 7> neighbours{};
    for (int i = 0; i < 7 && ok; ++i) {
      if (!connected(bags[i], adj)) {
        ok = false;
        break;
      }
      uint16_t bits = bags[i];
      while (bits) {
        int v = __builtin_ctz(bits);
        neighbours[i] |= adj[v];
        bits &= bits - 1;
      }
      for (int j = 0; j < i; ++j)
        if (!(neighbours[i] & bags[j])) {
          ok = false;
          break;
        }
    }
    if (ok) return true;
  }
  return false;
}

static void add_edge(std::array<uint16_t, 12>& adj, int a, int b) {
  adj[a] |= uint16_t(1) << b;
  adj[b] |= uint16_t(1) << a;
}

// Vertices: c0..c5,z=6,A1=7,A2=8,u=9,B=10,H=11.
static std::array<uint16_t, 12> graph(int split_code, int transition) {
  constexpr int z = 6, a1 = 7, a2 = 8, u = 9, b = 10, h = 11;
  std::array<uint16_t, 12> adj{};
  for (int i = 0; i < 7; ++i)
    for (int j = i + 1; j < 7; ++j) {
      bool missing = i < 6 && j < 6 && (j == i + 1 || (i == 0 && j == 5));
      if (!missing) add_edge(adj, i, j);
    }
  add_edge(adj, a1, a2);
  add_edge(adj, a1, u);
  add_edge(adj, a2, u);
  add_edge(adj, u, b);
  // By swapping A1,A2, fix the guaranteed A-B edge at A1-B.
  add_edge(adj, a1, b);
  for (int s = 0; s < 7; ++s) add_edge(adj, s, h);
  for (int s = 0; s < 7; ++s)
    if (s != 0 && s != 2) add_edge(adj, s, b);

  // Aggregate A row is {c0,c2,c3,c4,z}.  Ternary digit: A1 only,
  // A2 only, or both.
  const int labels[5] = {0, 2, 3, 4, z};
  int value = split_code;
  for (int label : labels) {
    int digit = value % 3;
    value /= 3;
    if (digit != 1) add_edge(adj, label, a1);
    if (digit != 0) add_edge(adj, label, a2);
  }

  if (transition == 0) {       // L-M minimal row
    add_edge(adj, 2, u);
  } else if (transition == 1) {  // M-R minimal row
    add_edge(adj, 5, u);
  } else {                     // direct L-R minimal row
    add_edge(adj, 2, u);
    add_edge(adj, 5, u);
  }
  return adj;
}

// Minimal exact L-M seven-adhesion rung.  Reuse vertices A1=A, A2=C,
// u=u, B=x, H=H.  C has the five-label B row and two entries A-C,x-C.
static std::array<uint16_t, 12> exact_rung_graph(int optional_u) {
  constexpr int z = 6, a = 7, c = 8, u = 9, x = 10, h = 11;
  std::array<uint16_t, 12> adj{};
  for (int i = 0; i < 7; ++i)
    for (int j = i + 1; j < 7; ++j) {
      bool missing = i < 6 && j < 6 && (j == i + 1 || (i == 0 && j == 5));
      if (!missing) add_edge(adj, i, j);
    }
  for (int s = 0; s < 7; ++s) add_edge(adj, s, h);
  for (int s : {0, 2, 3, 4, z}) add_edge(adj, s, a);
  for (int s : {1, 3, 4, 5, z}) add_edge(adj, s, c);
  add_edge(adj, u, a);
  add_edge(adj, u, x);
  add_edge(adj, a, c);
  add_edge(adj, x, c);
  add_edge(adj, u, 2);
  if (optional_u & 1) add_edge(adj, u, 4);
  if (optional_u & 2) add_edge(adj, u, z);
  return adj;
}

int main() {
  build_candidates();
  std::cout << "candidate partitions " << candidates.size() << "\n";
  for (int transition = 0; transition < 3; ++transition) {
    int negative = 0;
    for (int code = 0; code < 243; ++code) {
      if (!has_k7(graph(code, transition))) {
        ++negative;
        if (negative <= 100) std::cout << "negative " << transition << " " << code << "\n";
      }
    }
    std::cout << "transition " << transition << " negative " << negative << "\n";
  }
  for (int optional = 0; optional < 4; ++optional)
    std::cout << "exact L-M rung optional " << optional << " K7 "
              << has_k7(exact_rung_graph(optional)) << "\n";
}
