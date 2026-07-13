// Classify two adjacent two-terminal carriers over the double-Moser core.

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
using Edge = std::pair<int, int>;
static Edge edge(int a, int b) { if (a > b) std::swap(a, b); return {a, b}; }

template <int n>
static bool has_k7(const std::set<Edge>& edges) {
  std::array<Mask, n> adj{};
  for (auto [a, b] : edges) { adj[a] |= Mask(1) << b; adj[b] |= Mask(1) << a; }
  std::array<Mask, 1 << n> nb{};
  std::vector<Mask> connected;
  for (Mask mask = 1; mask < (Mask(1) << n); ++mask) {
    Mask low = mask & -mask;
    nb[mask] = nb[mask ^ low] | adj[std::countr_zero(low)];
    Mask reached = low;
    while (true) {
      Mask next = reached | (nb[reached] & mask);
      if (next == reached) break;
      reached = next;
    }
    if (reached == mask) connected.push_back(mask);
  }
  std::sort(connected.begin(), connected.end(), [](Mask a, Mask b) {
    return std::popcount(a) != std::popcount(b)
        ? std::popcount(a) < std::popcount(b) : a < b;
  });
  auto search = [&](auto&& self, int depth, std::vector<int> candidates,
                    Mask used) -> bool {
    if (depth == 7) return true;
    int needed = 7 - depth;
    for (size_t position = 0; position < candidates.size(); ++position) {
      Mask bag = connected[candidates[position]];
      if (bag & used) continue;
      std::vector<int> next;
      for (size_t j = position + 1; j < candidates.size(); ++j) {
        Mask other = connected[candidates[j]];
        if (!(other & (used | bag)) && (nb[bag] & other))
          next.push_back(candidates[j]);
      }
      if (static_cast<int>(next.size()) >= needed - 1 &&
          self(self, depth + 1, std::move(next), used | bag))
        return true;
    }
    return false;
  };
  std::vector<int> all(connected.size());
  std::iota(all.begin(), all.end(), 0);
  return search(search, 0, std::move(all), 0);
}

static std::set<Edge> core() {
  constexpr int u = 0, v = 1, x1 = 2, x2 = 3, x3 = 4, x4 = 5;
  constexpr int a = 6, b = 7, p = 8, q = 9;
  std::set<Edge> edges;
  auto add = [&](int left, int right) { edges.insert(edge(left, right)); };
  add(u, v);
  for (int x : {x1, x2, x3, x4, p, q}) add(u, x);
  for (int x : {x1, x2, x3, x4, a, b}) add(v, x);
  for (auto [left, right] : std::array<Edge, 12>{{
       {x1,x2},{x3,x4},{a,b},{p,q},{a,x1},{a,x2},
       {b,x3},{b,x4},{p,x3},{p,x4},{q,x1},{q,x2}}})
    add(left, right);
  return edges;
}

int main() {
  constexpr std::array<int, 8> interface{2, 3, 4, 5, 6, 7, 8, 9};
  constexpr std::array<const char*, 8> name{"1","2","3","4","a","b","p","q"};
  std::vector<std::pair<int,int>> pairs;
  for (int left = 0; left < 8; ++left)
    for (int right = left + 1; right < 8; ++right)
      pairs.emplace_back(left, right);
  int good = 0;
  for (size_t i = 0; i < pairs.size(); ++i)
    for (size_t j = i + 1; j < pairs.size(); ++j) {
          auto [a,b] = pairs[i];
          auto [c,d] = pairs[j];
          if (a == c || a == d || b == c || b == d) continue;
          auto edges = core();
          edges.insert(edge(10, 11));
          edges.insert(edge(10, interface[a]));
          edges.insert(edge(10, interface[b]));
          edges.insert(edge(11, interface[c]));
          edges.insert(edge(11, interface[d]));
          if (has_k7<12>(edges)) {
            ++good;
            std::cout << name[a] << name[b] << '|' << name[c] << name[d] << '\n';
          }
    }
  std::cout << "good crossing pairs=" << good << '\n';
}
