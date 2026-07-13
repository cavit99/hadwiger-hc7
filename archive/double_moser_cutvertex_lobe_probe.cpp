// Conservative quotient probe for two lobes behind a cutvertex of the
// connected double-Moser body. Each lobe sees the hub and misses exactly
// two of the eight interface vertices {x1,x2,x3,x4,a,b,p,q}.

#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <utility>
#include <vector>

using Mask = uint16_t;
using Edge = std::pair<int, int>;

static Edge edge(int a, int b) {
  if (a > b) std::swap(a, b);
  return {a, b};
}

template <int n>
static std::vector<Mask> k7_model(const std::vector<Edge>& edges) {
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
  std::sort(connected.begin(), connected.end(), [](Mask left, Mask right) {
    if (std::popcount(left) != std::popcount(right))
      return std::popcount(left) < std::popcount(right);
    return left < right;
  });

  auto search = [&](auto&& self, std::vector<Mask> chosen,
                    const std::vector<int>& candidates, Mask used)
      -> std::vector<Mask> {
    if (chosen.size() == 7) return chosen;
    int needed = 7 - static_cast<int>(chosen.size());
    if (static_cast<int>(candidates.size()) < needed) return {};
    for (size_t position = 0; position < candidates.size(); ++position) {
      Mask bag = connected[candidates[position]];
      if (bag & used) continue;
      std::vector<int> next;
      for (size_t j = position + 1; j < candidates.size(); ++j) {
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
  return search(search, {}, all, 0);
}

static std::vector<Edge> graph_for(std::pair<int, int> first,
                                   std::pair<int, int> second,
                                   int hub_contacts = 0) {
  constexpr int u = 0, v = 1;
  constexpr std::array<int, 4> x{2, 3, 4, 5};
  constexpr int a = 6, b = 7, p = 8, q = 9;
  constexpr int hub = 10, d1 = 11, d2 = 12;
  constexpr std::array<int, 8> interface{2, 3, 4, 5, 6, 7, 8, 9};

  std::vector<Edge> edges;
  auto add = [&](int left, int right) { edges.push_back(edge(left, right)); };
  add(u, v);
  for (int root : x) {
    add(u, root);
    add(v, root);
  }
  add(u, p); add(u, q); add(v, a); add(v, b);
  add(x[0], x[1]); add(x[2], x[3]); add(a, b); add(p, q);
  add(a, x[0]); add(a, x[1]); add(b, x[2]); add(b, x[3]);
  add(q, x[0]); add(q, x[1]); add(p, x[2]); add(p, x[3]);
  add(hub, d1); add(hub, d2);
  for (int index = 0; index < 8; ++index)
    if (hub_contacts & (1 << index)) add(hub, interface[index]);

  for (auto [lobe, defect] :
       {std::pair{d1, first}, std::pair{d2, second}}) {
    for (int index = 0; index < 8; ++index)
      if (index != defect.first && index != defect.second)
        add(lobe, interface[index]);
  }
  std::sort(edges.begin(), edges.end());
  edges.erase(std::unique(edges.begin(), edges.end()), edges.end());
  return edges;
}

int main() {
  std::vector<std::pair<int, int>> defects;
  for (int first = 0; first < 8; ++first)
    for (int second = first + 1; second < 8; ++second)
      defects.emplace_back(first, second);

  int negative = 0;
  std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>> residual;
  for (auto first : defects)
    for (auto second : defects)
      if (k7_model<13>(graph_for(first, second)).empty()) {
        ++negative;
        residual.emplace_back(first, second);
        std::cout << "negative " << first.first << first.second
                  << '|' << second.first << second.second << '\n';
      }
  std::cout << "profiles=" << defects.size() * defects.size()
            << " negative=" << negative << '\n';
  bool restoration_survives = false;
  for (auto [first, second] : residual) {
    for (int which = 0; which < 4; ++which) {
      auto left = first;
      auto right = second;
      if (which == 0) left = {first.second, first.second};
      if (which == 1) left = {first.first, first.first};
      if (which == 2) right = {second.second, second.second};
      if (which == 3) right = {second.first, second.first};
      if (k7_model<13>(graph_for(left, right)).empty())
        restoration_survives = true;
    }
  }
  if (restoration_survives) return 1;

  auto is_residual = [&](auto left, auto right) {
    return std::find(residual.begin(), residual.end(),
                     std::pair{left, right}) != residual.end();
  };
  int residual_triangles = 0;
  for (auto first : defects)
    for (auto second : defects)
      for (auto third : defects)
        if (is_residual(first, second) &&
            is_residual(first, third) &&
            is_residual(second, third))
          ++residual_triangles;
  std::cout << "single-contact restorations surviving=0\n";
  std::cout << "residual relation triangles=" << residual_triangles << '\n';
  return residual_triangles == 0 ? 0 : 1;
}
