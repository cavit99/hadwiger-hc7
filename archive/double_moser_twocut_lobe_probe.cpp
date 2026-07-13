// Conservative quotient probe for two lobes behind a 2-separator of the
// connected double-Moser body.  Each lobe sees both separator vertices and
// misses at most two of the eight interface vertices.  The program checks
// both possibilities for the separator edge.

#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <string>
#include <tuple>
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
  return search(search, {}, all, 0);
}

static std::vector<Edge> graph_for(Mask first_defect, Mask second_defect,
                                   bool separator_edge,
                                   Mask z1_contacts = 0,
                                   Mask z2_contacts = 0) {
  constexpr int u = 0, v = 1;
  constexpr std::array<int, 4> x{2, 3, 4, 5};
  constexpr int a = 6, b = 7, p = 8, q = 9;
  constexpr int z1 = 10, z2 = 11, d1 = 12, d2 = 13;
  constexpr std::array<int, 8> interface{2, 3, 4, 5, 6, 7, 8, 9};
  std::vector<Edge> edges;
  auto add = [&](int left, int right) { edges.push_back(edge(left, right)); };
  add(u, v);
  for (int root : x) { add(u, root); add(v, root); }
  add(u, p); add(u, q); add(v, a); add(v, b);
  add(x[0], x[1]); add(x[2], x[3]); add(a, b); add(p, q);
  add(a, x[0]); add(a, x[1]); add(b, x[2]); add(b, x[3]);
  add(q, x[0]); add(q, x[1]); add(p, x[2]); add(p, x[3]);
  if (separator_edge) add(z1, z2);
  for (int i = 0; i < 8; ++i) {
    if (z1_contacts & (Mask(1) << i)) add(z1, interface[i]);
    if (z2_contacts & (Mask(1) << i)) add(z2, interface[i]);
  }
  for (int lobe : {d1, d2}) { add(lobe, z1); add(lobe, z2); }
  for (auto [lobe, defect] :
       {std::pair{d1, first_defect}, std::pair{d2, second_defect}}) {
    for (int i = 0; i < 8; ++i)
      if (!(defect & (Mask(1) << i))) add(lobe, interface[i]);
  }
  std::sort(edges.begin(), edges.end());
  edges.erase(std::unique(edges.begin(), edges.end()), edges.end());
  return edges;
}

static void print_mask(Mask mask) {
  static constexpr std::array<const char*, 8> names{
      "x1", "x2", "x3", "x4", "a", "b", "p", "q"};
  std::cout << '{';
  bool first = true;
  for (int i = 0; i < 8; ++i) if (mask & (Mask(1) << i)) {
    if (!first) std::cout << ',';
    std::cout << names[i];
    first = false;
  }
  std::cout << '}';
}

int main(int argc, char** argv) {
  if (argc > 1 && std::string(argv[1]) == "models") {
    static constexpr std::array<const char*, 14> names{
        "u", "v", "x1", "x2", "x3", "x4", "a", "b",
        "p", "q", "z1", "z2", "d", "e"};
    std::vector<std::tuple<Mask, Mask, int>> cases{
        {(Mask(1) << 0) | (Mask(1) << 2),
         (Mask(1) << 1) | (Mask(1) << 3), 0},
        {(Mask(1) << 0) | (Mask(1) << 4),
         (Mask(1) << 2) | (Mask(1) << 6), 0},
        {(Mask(1) << 4) | (Mask(1) << 5),
         (Mask(1) << 6) | (Mask(1) << 7), 4}};
    for (size_t index = 0; index < cases.size(); ++index) {
      auto [first, second, label] = cases[index];
      auto model = k7_model<14>(graph_for(
          first, second, false, Mask(1) << label, 0));
      std::cout << "representative " << index + 1 << '\n';
      for (Mask bag : model) {
        std::cout << "  {";
        bool comma = false;
        for (int vertex = 0; vertex < 14; ++vertex)
          if (bag & (Mask(1) << vertex)) {
            if (comma) std::cout << ',';
            std::cout << names[vertex];
            comma = true;
          }
        std::cout << "}\n";
      }
    }
    return 0;
  }
  if (argc > 1 && std::string(argv[1]) == "z") {
    // One representative of each exceptional defect orbit.  Bit order is
    // x1,x2,x3,x4,a,b,p,q.
    std::vector<std::pair<Mask, Mask>> reps{
        {(Mask(1) << 0) | (Mask(1) << 2),
         (Mask(1) << 1) | (Mask(1) << 3)},
        {(Mask(1) << 0) | (Mask(1) << 4),
         (Mask(1) << 2) | (Mask(1) << 6)},
        {(Mask(1) << 4) | (Mask(1) << 5),
         (Mask(1) << 6) | (Mask(1) << 7)}};
    for (bool separator_edge : {false, true}) {
      for (size_t rep = 0; rep < reps.size(); ++rep) {
        auto [first, second] = reps[rep];
        for (int which_z = 0; which_z < 2; ++which_z)
          for (int i = 0; i < 8; ++i) {
            Mask row = Mask(1) << i;
            auto model = k7_model<14>(graph_for(
                first, second, separator_edge,
                which_z == 0 ? row : 0,
                which_z == 1 ? row : 0));
            if (model.empty())
              std::cout << "survive edge=" << separator_edge
                        << " rep=" << rep + 1 << " z=" << which_z + 1
                        << " label=" << i << '\n';
          }
      }
    }
    return 0;
  }
  std::vector<Mask> defects;
  for (Mask mask = 0; mask < 256; ++mask)
    if (std::popcount(mask) <= 2) defects.push_back(mask);
  for (bool separator_edge : {false, true}) {
    int negative = 0;
    std::vector<std::pair<Mask, Mask>> residual;
    for (Mask first : defects) for (Mask second : defects) {
      auto model = k7_model<14>(graph_for(first, second, separator_edge));
      if (model.empty()) {
        ++negative;
        residual.emplace_back(first, second);
        std::cout << "negative edge=" << separator_edge << ' ';
        print_mask(first); std::cout << '|'; print_mask(second); std::cout << '\n';
      }
    }
    std::cout << "separator_edge=" << separator_edge
              << " profiles=" << defects.size() * defects.size()
              << " negative=" << negative << '\n';
  }
}
