// Independent exact audit of the 9 x 9 double-Moser two-component profiles.

#include <algorithm>
#include <array>
#include <bit>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <set>
#include <string>
#include <utility>
#include <vector>

using Mask = uint16_t;

static std::pair<int, int> edge(int a, int b) {
  if (a > b) std::swap(a, b);
  return {a, b};
}

template <int n>
static std::vector<Mask> find_k7(const std::set<std::pair<int, int>>& edges) {
  std::array<Mask, n> adj{};
  for (auto [a, b] : edges) {
    adj[a] |= Mask(1) << b;
    adj[b] |= Mask(1) << a;
  }
  std::array<Mask, 1 << n> neighbours{};
  std::vector<Mask> connected;
  for (Mask mask = 1; mask < (Mask(1) << n); ++mask) {
    Mask low = mask & -mask;
    int vertex = std::countr_zero(low);
    neighbours[mask] = neighbours[mask ^ low] | adj[vertex];
    Mask reached = low;
    while (true) {
      Mask expanded = reached | (neighbours[reached] & mask);
      if (expanded == reached) break;
      reached = expanded;
    }
    if (reached == mask) connected.push_back(mask);
  }
  std::sort(connected.begin(), connected.end(), [](Mask a, Mask b) {
    if (std::popcount(a) != std::popcount(b))
      return std::popcount(a) < std::popcount(b);
    return a < b;
  });

  std::vector<Mask> answer;
  auto dfs = [&](auto&& self, int depth, size_t start, Mask used) -> bool {
    if (depth == 7) return true;
    for (size_t pos = start; pos < connected.size(); ++pos) {
      Mask bag = connected[pos];
      if (bag & used) continue;
      bool complete = true;
      for (Mask old : answer)
        if (!(neighbours[bag] & old)) complete = false;
      if (!complete) continue;
      answer.push_back(bag);
      if (self(self, depth + 1, pos + 1, used | bag)) return true;
      answer.pop_back();
    }
    return false;
  };
  if (dfs(dfs, 0, 0, 0)) return answer;
  return {};
}

// type 0=a/full, 1=b/full, 2=ab/full, 3+d=ab/miss d (0<=d<6).
static std::set<std::pair<int, int>> quotient(int type1, int type2) {
  constexpr int u = 0, v = 1, x1 = 2, x2 = 3, x3 = 4, x4 = 5;
  constexpr int a = 6, b = 7, p = 8, q = 9, r1 = 10, r2 = 11;
  const std::array<int, 6> w{x1, x2, x3, x4, p, q};
  std::set<std::pair<int, int>> edges;
  auto add = [&](int x, int y) { edges.insert(edge(x, y)); };
  add(u, v);
  for (int x : {x1, x2, x3, x4, p, q}) add(u, x);
  for (int x : {x1, x2, x3, x4, a, b}) add(v, x);
  add(x1, x2); add(x3, x4); add(a, b); add(p, q);
  for (int x : {x1, x2}) { add(a, x); add(q, x); }
  for (int x : {x3, x4}) { add(b, x); add(p, x); }
  for (auto [r, type] : {std::pair{r1, type1}, std::pair{r2, type2}}) {
    if (type != 1) add(r, a);
    if (type != 0) add(r, b);
    int defect = type >= 3 ? type - 3 : -1;
    for (int i = 0; i < 6; ++i)
      if (i != defect) add(r, w[i]);
  }
  return edges;
}

static std::string type_name(int type) {
  if (type == 0) return "a/full";
  if (type == 1) return "b/full";
  if (type == 2) return "ab/full";
  return "ab/miss" + std::to_string(type - 3);
}

int main() {
  constexpr std::array<const char*, 12> names{
      "u", "v", "x1", "x2", "x3", "x4", "a", "b", "p", "q", "D1", "D2"};
  int positive = 0;
  for (int left = 0; left < 9; ++left) {
    for (int right = 0; right < 9; ++right) {
      auto model = find_k7<12>(quotient(left, right));
      assert(!model.empty());
      ++positive;
      if (left <= right) {
        std::cout << type_name(left) << " | " << type_name(right) << ":";
        for (Mask bag : model) {
          std::cout << " {";
          bool first = true;
          for (int vertex = 0; vertex < 12; ++vertex) {
            if (!(bag & (Mask(1) << vertex))) continue;
            if (!first) std::cout << ',';
            first = false;
            std::cout << names[vertex];
          }
          std::cout << '}';
        }
        std::cout << '\n';
      }
    }
  }
  assert(positive == 81);
  std::cout << "verified 81/81 ordered profiles\n";
}
