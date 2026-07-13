// Exact finite checks for the overlapping-Moser outer-portal peel.
//
// Boundary order:
//   0,1,2,3 = x1,x2,x3,x4; 4=p; 5=q.
// Boundary edges are 01,23,42,43,50,51,45.
// A defect row d means that a connected component misses only d.

#include <algorithm>
#include <array>
#include <bit>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <set>
#include <utility>
#include <vector>

using Mask = uint16_t;

static std::pair<int, int> edge(int a, int b) {
  if (a > b) std::swap(a, b);
  return {a, b};
}

static bool w_edge(int a, int b) {
  static const std::set<std::pair<int, int>> edges{
      edge(0, 1), edge(2, 3), edge(4, 2), edge(4, 3),
      edge(5, 0), edge(5, 1), edge(4, 5)};
  return edges.contains(edge(a, b));
}

static bool mutual_incidence_free(const std::vector<int>& reps,
                                  const std::vector<int>& defects) {
  for (int i = 0; i < static_cast<int>(reps.size()); ++i) {
    if (reps[i] == defects[i]) return false;
    for (int j = 0; j < i; ++j)
      if (reps[i] == defects[j] && reps[j] == defects[i]) return false;
  }
  return true;
}

// Four component bags, {v,a,b}, one unused X-root, and apex u.
static bool four_row_certificate(const std::array<int, 4>& d) {
  std::array<int, 6> order{0, 1, 2, 3, 4, 5};
  do {
    std::vector<int> reps(order.begin(), order.begin() + 4);
    std::vector<int> defects(d.begin(), d.end());
    if (!mutual_incidence_free(reps, defects)) continue;
    for (int y = 0; y < 4; ++y) {
      if (std::find(reps.begin(), reps.end(), y) != reps.end()) continue;
      bool ok = true;
      for (int i = 0; i < 4; ++i)
        if (d[i] == y && !w_edge(y, reps[i])) ok = false;
      if (ok) return true;
    }
  } while (std::next_permutation(order.begin(), order.end()));
  return false;
}

// Three component bags, {v,a,b}, one unused literal X-edge, and apex u.
static bool three_row_certificate(const std::array<int, 3>& d) {
  std::array<int, 6> order{0, 1, 2, 3, 4, 5};
  constexpr std::array<std::array<int, 2>, 2> literal{{{0, 1}, {2, 3}}};
  do {
    std::vector<int> reps(order.begin(), order.begin() + 3);
    std::vector<int> defects(d.begin(), d.end());
    if (!mutual_incidence_free(reps, defects)) continue;
    for (auto yz : literal) {
      if (std::find(reps.begin(), reps.end(), yz[0]) != reps.end() ||
          std::find(reps.begin(), reps.end(), yz[1]) != reps.end())
        continue;
      bool ok = true;
      for (int i = 0; i < 3; ++i)
        if ((d[i] == yz[0] || d[i] == yz[1]) &&
            !w_edge(d[i], reps[i]))
          ok = false;
      if (ok) return true;
    }
  } while (std::next_permutation(order.begin(), order.end()));
  return false;
}

// Two component bags, {v,a,b}, one unused boundary triangle, and apex u.
static bool two_row_triangle_certificate(const std::array<int, 2>& d) {
  std::array<int, 6> order{0, 1, 2, 3, 4, 5};
  constexpr std::array<std::array<int, 3>, 2> triangles{
      {{4, 2, 3}, {5, 0, 1}}};
  do {
    std::vector<int> reps(order.begin(), order.begin() + 2);
    std::vector<int> defects(d.begin(), d.end());
    if (!mutual_incidence_free(reps, defects)) continue;
    for (auto t : triangles) {
      bool disjoint = true;
      for (int y : t)
        if (std::find(reps.begin(), reps.end(), y) != reps.end())
          disjoint = false;
      if (!disjoint) continue;
      bool ok = true;
      for (int i = 0; i < 2; ++i)
        if (std::find(t.begin(), t.end(), d[i]) != t.end() &&
            !w_edge(d[i], reps[i]))
          ok = false;
      if (ok) return true;
    }
  } while (std::next_permutation(order.begin(), order.end()));
  return false;
}

template <int n>
static bool has_k7(const std::set<std::pair<int, int>>& edges) {
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
  auto dfs = [&](auto&& self, int depth, const std::vector<int>& candidates,
                 Mask used) -> bool {
    if (depth == 7) return true;
    int needed = 7 - depth;
    if (static_cast<int>(candidates.size()) < needed) return false;
    for (size_t pos = 0; pos < candidates.size(); ++pos) {
      Mask bag = connected[candidates[pos]];
      if (bag & used) continue;
      std::vector<int> next;
      for (size_t j = pos + 1; j < candidates.size(); ++j) {
        Mask other = connected[candidates[j]];
        if (!(other & (used | bag)) && (neighbours[bag] & other))
          next.push_back(candidates[j]);
      }
      if (static_cast<int>(next.size()) >= needed - 1 &&
          self(self, depth + 1, next, used | bag))
        return true;
    }
    return false;
  };
  std::vector<int> all(connected.size());
  std::iota(all.begin(), all.end(), 0);
  return dfs(dfs, 0, all, 0);
}

// Conservative two-component quotient. Vertex order:
// u,v,x1,x2,x3,x4,a,b,p,q,r1,r2.
static bool two_row_exact_minor(int d1, int d2) {
  std::set<std::pair<int, int>> e;
  auto add = [&](int x, int y) { e.insert(edge(x, y)); };
  constexpr int u = 0, v = 1, x1 = 2, x2 = 3, x3 = 4, x4 = 5;
  constexpr int a = 6, b = 7, p = 8, q = 9, r1 = 10, r2 = 11;
  add(u, v);
  for (int x : {x1, x2, x3, x4, p, q}) add(u, x);
  for (int x : {x1, x2, x3, x4, a, b}) add(v, x);
  add(x1, x2); add(x3, x4); add(a, b); add(p, q);
  for (int x : {x1, x2}) { add(a, x); add(q, x); }
  for (int x : {x3, x4}) { add(b, x); add(p, x); }
  const std::array<int, 6> physical{x1, x2, x3, x4, p, q};
  for (auto [r, d] : {std::pair{r1, d1}, std::pair{r2, d2}}) {
    add(r, a); add(r, b);
    for (int i = 0; i < 6; ++i)
      if (i != d) add(r, physical[i]);
  }
  return has_k7<12>(e);
}

int main() {
  int four_bad = 0, three_bad = 0, two_triangle_bad = 0;
  for (int a = 0; a < 6; ++a)
    for (int b = 0; b < 6; ++b) {
      if (!two_row_triangle_certificate({a, b})) ++two_triangle_bad;
      for (int c = 0; c < 6; ++c) {
        if (!three_row_certificate({a, b, c})) ++three_bad;
        for (int d = 0; d < 6; ++d)
          if (!four_row_certificate({a, b, c, d})) ++four_bad;
      }
    }
  assert(four_bad == 0);
  assert(three_bad == 0);
  assert(two_triangle_bad == 8);

  int exact_negative = 0;
  std::cout << "two-row exact negative profiles:";
  for (int a = 0; a < 6; ++a)
    for (int b = 0; b < 6; ++b)
      if (!two_row_exact_minor(a, b)) {
        ++exact_negative;
        std::cout << ' ' << a << b;
      }
  std::cout << '\n';
  std::cout << "four-row bad=" << four_bad
            << " three-row bad=" << three_bad
            << " two-row triangle bad=" << two_triangle_bad
            << " exact two-row negative=" << exact_negative << '\n';
}
