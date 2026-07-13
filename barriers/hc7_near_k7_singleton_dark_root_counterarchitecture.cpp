#include <array>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

using Mask = std::uint16_t;
constexpr int N = 12;
static std::vector<std::array<Mask, 7>> candidates;

static void rec(const std::vector<int>& v, int at, std::vector<Mask>& blocks) {
  if (static_cast<int>(blocks.size()) + static_cast<int>(v.size()) - at < 7) return;
  if (at == static_cast<int>(v.size())) {
    if (blocks.size() == 7) {
      std::array<Mask, 7> p{};
      std::copy(blocks.begin(), blocks.end(), p.begin());
      candidates.push_back(p);
    }
    return;
  }
  Mask bit = Mask(1) << v[at];
  for (std::size_t i = 0; i < blocks.size(); ++i) {
    blocks[i] |= bit;
    rec(v, at + 1, blocks);
    blocks[i] ^= bit;
  }
  if (blocks.size() < 7) {
    blocks.push_back(bit);
    rec(v, at + 1, blocks);
    blocks.pop_back();
  }
}

static bool connected(Mask block, const std::array<Mask, N>& adj) {
  Mask reached = block & Mask(-block);
  while (true) {
    Mask expanded = reached;
    for (Mask todo = reached; todo;) {
      Mask bit = todo & Mask(-todo);
      todo ^= bit;
      expanded |= adj[__builtin_ctz(static_cast<unsigned>(bit))] & block;
    }
    if (expanded == reached) return reached == block;
    reached = expanded;
  }
}

static bool has_k7(const std::array<Mask, N>& adj) {
  static const char* names[N] = {"h", "1", "2", "r", "a", "b", "c", "d", "e0", "e1", "e2", "e3"};
  for (const auto& p : candidates) {
    bool ok = true;
    std::array<Mask, 7> neighbours{};
    for (int i = 0; i < 7; ++i) {
      if (!connected(p[i], adj)) { ok = false; break; }
      for (Mask todo = p[i]; todo;) {
        Mask bit = todo & Mask(-todo);
        todo ^= bit;
        neighbours[i] |= adj[__builtin_ctz(static_cast<unsigned>(bit))];
      }
    }
    if (!ok) continue;
    for (int i = 0; i < 7 && ok; ++i)
      for (int j = 0; j < i; ++j)
        if (!(neighbours[i] & p[j])) { ok = false; break; }
    if (ok) {
      std::cout << "model=";
      for (int i = 0; i < 7; ++i) {
        if (i) std::cout << '|';
        for (int x = 0; x < N; ++x) if (p[i] & (Mask(1) << x)) std::cout << names[x];
      }
      std::cout << "\n";
      return true;
    }
  }
  return false;
}

int main() {
  for (int used = 0; used < (1 << N); ++used) {
    if (__builtin_popcount(static_cast<unsigned>(used)) < 7) continue;
    std::vector<int> vertices;
    for (int x = 0; x < N; ++x) if (used & (1 << x)) vertices.push_back(x);
    std::vector<Mask> blocks;
    rec(vertices, 0, blocks);
  }

  // h,1,2,r,a,b,c,d,e0,e1,e2,e3.
  std::array<Mask, N> adj{};
  auto edge = [&](int x, int y) { adj[x] |= Mask(1) << y; adj[y] |= Mask(1) << x; };
  for (int x = 0; x < 4; ++x) for (int y = x + 1; y < 4; ++y) edge(x, y);
  edge(4, 5); edge(4, 6); edge(5, 6);
  edge(0, 4); edge(1, 5); edge(2, 5); edge(3, 6);
  for (int x = 0; x < 7; ++x) edge(7, x);
  for (int x = 8; x < 12; ++x) for (int y = x + 1; y < 12; ++y) edge(x, y);
  for (int x = 8; x < 12; ++x) edge(5, x);
  edge(0, 8); edge(3, 9);
  edge(6, 8); edge(1, 8);
  edge(4, 9); edge(1, 9);
  edge(4, 10); edge(1, 10);
  edge(1, 11);

  std::cout << "candidate partitions=" << candidates.size() << "\n";
  std::cout << "has_K7_minor=" << (has_k7(adj) ? "true" : "false") << "\n";
}
