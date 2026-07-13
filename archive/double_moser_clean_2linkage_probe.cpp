// Enumerate clean two-linkages on the eight interface labels of the
// double-Moser core.  Each path is contracted to one internal vertex.

#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <set>
#include <string>
#include <utility>
#include <vector>

using Mask = uint16_t;
using Edge = std::pair<int, int>;

static Edge edge(int a, int b) {
  if (a > b) std::swap(a, b);
  return {a, b};
}

template <int n>
static std::vector<Mask> find_k7(const std::set<Edge>& edges) {
  std::array<Mask, n> adj{};
  for (auto [a, b] : edges) {
    adj[a] |= Mask(1) << b;
    adj[b] |= Mask(1) << a;
  }
  std::array<Mask, 1 << n> neighbours{};
  std::vector<Mask> connected;
  for (Mask mask = 1; mask < (Mask(1) << n); ++mask) {
    Mask low = mask & -mask;
    int v = std::countr_zero(low);
    neighbours[mask] = neighbours[mask ^ low] | adj[v];
    Mask reached = low;
    while (true) {
      Mask next = reached | (neighbours[reached] & mask);
      if (next == reached) break;
      reached = next;
    }
    if (reached == mask) connected.push_back(mask);
  }
  std::sort(connected.begin(), connected.end(), [](Mask a, Mask b) {
    if (std::popcount(a) != std::popcount(b))
      return std::popcount(a) < std::popcount(b);
    return a < b;
  });
  auto search = [&](auto&& self, std::vector<Mask> chosen,
                    const std::vector<int>& candidates, Mask used)
      -> std::vector<Mask> {
    if (chosen.size() == 7) return chosen;
    int needed = 7 - static_cast<int>(chosen.size());
    if (static_cast<int>(candidates.size()) < needed) return {};
    for (size_t i = 0; i < candidates.size(); ++i) {
      Mask bag = connected[candidates[i]];
      if (bag & used) continue;
      std::vector<int> next;
      for (size_t j = i + 1; j < candidates.size(); ++j) {
        Mask other = connected[candidates[j]];
        if (!(other & (used | bag)) && (neighbours[bag] & other))
          next.push_back(candidates[j]);
      }
      if (static_cast<int>(next.size()) < needed - 1) continue;
      auto extended = chosen;
      extended.push_back(bag);
      auto answer = self(self, std::move(extended), next, used | bag);
      if (!answer.empty()) return answer;
    }
    return {};
  };
  std::vector<int> all(connected.size());
  std::iota(all.begin(), all.end(), 0);
  auto answer = search(search, {}, all, 0);
  if (!answer.empty()) return answer;
  return {};
}

static std::set<Edge> core() {
  constexpr int u = 0, v = 1, x1 = 2, x2 = 3, x3 = 4, x4 = 5;
  constexpr int a = 6, b = 7, p = 8, q = 9;
  std::set<Edge> edges;
  auto add = [&](int x, int y) { edges.insert(edge(x, y)); };
  add(u, v);
  for (int x : {x1, x2, x3, x4, p, q}) add(u, x);
  for (int x : {x1, x2, x3, x4, a, b}) add(v, x);
  add(x1, x2); add(x3, x4); add(a, b); add(p, q);
  for (int x : {x1, x2}) { add(a, x); add(q, x); }
  for (int x : {x3, x4}) { add(b, x); add(p, x); }
  return edges;
}

int main() {
  constexpr std::array<int, 8> interface{2, 3, 4, 5, 6, 7, 8, 9};
  constexpr std::array<const char*, 12> names{
      "u", "v", "x1", "x2", "x3", "x4", "a", "b", "p", "q",
      "r", "s"};
  int positive = 0;
  int total = 0;
  for (int i = 0; i < 8; ++i)
    for (int j = i + 1; j < 8; ++j)
      for (int k = i + 1; k < 8; ++k)
        if (k != j)
          for (int l = k + 1; l < 8; ++l)
            if (l != j) {
              // Avoid printing both orders of the two pairs.
              if (std::pair{i, j} > std::pair{k, l}) continue;
              ++total;
              auto edges = core();
              edges.insert(edge(10, interface[i]));
              edges.insert(edge(10, interface[j]));
              edges.insert(edge(11, interface[k]));
              edges.insert(edge(11, interface[l]));
              auto model = find_k7<12>(edges);
              if (!model.empty()) {
                ++positive;
                std::cout << names[interface[i]] << names[interface[j]]
                          << " | " << names[interface[k]] << names[interface[l]]
                          << " :";
                for (Mask bag : model) {
                  std::cout << " {";
                  for (int z = 0; z < 12; ++z)
                    if (bag & (Mask(1) << z)) std::cout << names[z] << ',';
                  std::cout << '}';
                }
                std::cout << '\n';
              }
  }
  std::cout << "positive=" << positive << " total=" << total << '\n';
  return 0;
}
