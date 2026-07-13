#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <random>
#include <vector>

// Random falsification search for the assertion that K_{3,3} has the
// Kriesell--Mohr property (*).  Each generated graph is the union of nine
// alternating two-colour root paths.  The rooted-minor check is exact.

using Mask = std::uint64_t;

struct Instance {
  int n{};
  std::array<int, 6> root{};
  std::vector<int> colour;
  std::vector<Mask> adj;
};

static bool connected(const Instance& g, Mask set, int root) {
  Mask seen = Mask{1} << root;
  Mask active = seen;
  while (active) {
    const int v = __builtin_ctzll(active);
    active &= active - 1;
    const Mask add = g.adj[v] & set & ~seen;
    seen |= add;
    active |= add;
  }
  return seen == set;
}

static bool touch(const Instance& g, Mask a, Mask b) {
  while (a) {
    const int v = __builtin_ctzll(a);
    a &= a - 1;
    if (g.adj[v] & b) return true;
  }
  return false;
}

struct MinorChecker {
  const Instance& g;
  std::array<std::vector<Mask>, 6> candidates;
  std::array<Mask, 6> chosen{};
  std::array<int, 6> order{0, 3, 1, 4, 2, 5};

  explicit MinorChecker(const Instance& graph) : g(graph) {
    Mask roots = 0;
    for (int r : g.root) roots |= Mask{1} << r;
    const Mask all = (Mask{1} << g.n) - 1;
    const Mask free = all & ~roots;
    std::vector<int> free_vertices;
    for (int v = 0; v < g.n; ++v)
      if ((free >> v) & 1) free_vertices.push_back(v);
    const std::uint64_t count = std::uint64_t{1} << free_vertices.size();
    for (int label = 0; label < 6; ++label) {
      for (std::uint64_t bits = 0; bits < count; ++bits) {
        Mask set = Mask{1} << g.root[label];
        for (std::size_t q = 0; q < free_vertices.size(); ++q)
          if ((bits >> q) & 1) set |= Mask{1} << free_vertices[q];
        if (connected(g, set, g.root[label])) candidates[label].push_back(set);
      }
      std::sort(candidates[label].begin(), candidates[label].end(),
                [](Mask a, Mask b) {
                  return __builtin_popcountll(a) < __builtin_popcountll(b);
                });
    }
  }

  bool search(int depth, Mask used) {
    if (depth == 6) return true;
    const int label = order[depth];
    for (Mask set : candidates[label]) {
      if (set & used) continue;
      bool ok = true;
      for (int q = 0; q < depth; ++q) {
        const int other = order[q];
        if ((label < 3) != (other < 3)) {
          if (!touch(g, set, chosen[other])) {
            ok = false;
            break;
          }
        }
      }
      if (!ok) continue;
      chosen[label] = set;
      if (search(depth + 1, used | set)) return true;
    }
    return false;
  }
};

static Instance random_instance(std::mt19937_64& rng, int n) {
  Instance g;
  g.n = n;
  g.colour.resize(n);
  g.adj.assign(n, 0);

  // Give every colour one root, then distribute the remaining vertices.
  std::array<std::vector<int>, 6> cls;
  for (int c = 0; c < 6; ++c) {
    g.root[c] = c;
    g.colour[c] = c;
    cls[c].push_back(c);
  }
  for (int v = 6; v < n; ++v) {
    const int c = rng() % 6;
    g.colour[v] = c;
    cls[c].push_back(v);
  }

  auto add_edge = [&](int u, int v) {
    g.adj[u] |= Mask{1} << v;
    g.adj[v] |= Mask{1} << u;
  };

  for (int i = 0; i < 3; ++i) {
    for (int j = 3; j < 6; ++j) {
      std::vector<int> left(cls[i].begin() + 1, cls[i].end());
      std::vector<int> right(cls[j].begin() + 1, cls[j].end());
      std::shuffle(left.begin(), left.end(), rng);
      std::shuffle(right.begin(), right.end(), rng);
      const int max_internal_pairs = std::min(left.size(), right.size());
      const int pairs = max_internal_pairs == 0 ? 0 : rng() % (max_internal_pairs + 1);
      std::vector<int> path{g.root[i]};
      for (int q = 0; q < pairs; ++q) {
        path.push_back(right[q]);
        path.push_back(left[q]);
      }
      path.push_back(g.root[j]);
      for (std::size_t q = 1; q < path.size(); ++q) add_edge(path[q - 1], path[q]);
    }
  }
  return g;
}

int main(int argc, char** argv) {
  const std::uint64_t trials = argc > 1 ? std::stoull(argv[1]) : 10000;
  const std::uint64_t seed = argc > 2 ? std::stoull(argv[2]) : 1;
  std::mt19937_64 rng(seed);
  for (std::uint64_t trial = 0; trial < trials; ++trial) {
    const int n = 14 + (rng() % 5);  // exact checker remains cheap up to 18.
    Instance g = random_instance(rng, n);
    MinorChecker checker(g);
    if (!checker.search(0, 0)) {
      std::cout << "COUNTEREXAMPLE n=" << n << " seed=" << seed
                << " trial=" << trial << "\n";
      for (int u = 0; u < n; ++u)
        for (int v = u + 1; v < n; ++v)
          if ((g.adj[u] >> v) & 1) std::cout << u << ' ' << v << '\n';
      return 1;
    }
    if ((trial + 1) % 1000 == 0) std::cerr << "checked " << trial + 1 << '\n';
  }
  std::cout << "No counterexample in " << trials << " exact checks.\n";
}
