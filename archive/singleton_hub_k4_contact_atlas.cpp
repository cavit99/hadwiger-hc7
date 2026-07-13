#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

using Mask = std::uint16_t;

static std::vector<std::array<Mask, 7>> candidates;

static void partition_rec(const std::vector<int>& vertices, int at,
                          std::vector<Mask>& blocks) {
  if (static_cast<int>(blocks.size()) + static_cast<int>(vertices.size()) - at < 7) return;
  if (at == static_cast<int>(vertices.size())) {
    if (blocks.size() == 7) {
      std::array<Mask, 7> item{};
      std::copy(blocks.begin(), blocks.end(), item.begin());
      candidates.push_back(item);
    }
    return;
  }
  Mask bit = Mask(1) << vertices[at];
  for (std::size_t i = 0; i < blocks.size(); ++i) {
    blocks[i] |= bit;
    partition_rec(vertices, at + 1, blocks);
    blocks[i] ^= bit;
  }
  if (blocks.size() < 7) {
    blocks.push_back(bit);
    partition_rec(vertices, at + 1, blocks);
    blocks.pop_back();
  }
}

static void make_candidates() {
  for (int used = 0; used < (1 << 10); ++used) {
    if (__builtin_popcount(static_cast<unsigned>(used)) < 7) continue;
    std::vector<int> vertices;
    for (int v = 0; v < 10; ++v) if (used & (1 << v)) vertices.push_back(v);
    std::vector<Mask> blocks;
    partition_rec(vertices, 0, blocks);
  }
}

static void add_edge(std::array<Mask, 10>& adj, int x, int y) {
  adj[x] |= Mask(1) << y;
  adj[y] |= Mask(1) << x;
}

static bool connected(Mask block, const std::array<Mask, 10>& adj) {
  Mask reached = block & Mask(-block);
  while (true) {
    Mask expanded = reached;
    Mask todo = reached;
    while (todo) {
      Mask bit = todo & Mask(-todo);
      todo ^= bit;
      int v = __builtin_ctz(static_cast<unsigned>(bit));
      expanded |= adj[v] & block;
    }
    if (expanded == reached) return reached == block;
    reached = expanded;
  }
}

static bool has_k7(const std::array<Mask, 10>& adj) {
  for (const auto& p : candidates) {
    bool ok = true;
    for (Mask block : p) if (!connected(block, adj)) { ok = false; break; }
    if (!ok) continue;
    for (int i = 0; i < 7 && ok; ++i) {
      Mask neighbours = 0;
      Mask todo = p[i];
      while (todo) {
        Mask bit = todo & Mask(-todo);
        todo ^= bit;
        neighbours |= adj[__builtin_ctz(static_cast<unsigned>(bit))];
      }
      for (int j = 0; j < i; ++j) if (!(neighbours & p[j])) { ok = false; break; }
    }
    if (ok) return true;
  }
  return false;
}

static void run_atlas(int h, int r) {
  // q0..q3=0..3, b=4,d=5,a=6,c=7,1=8,2=9.
  std::array<std::vector<int>, 4> base;
  base[0] = {h};
  base[1] = {r};
  base[2] = {h, r};
  base[3] = {h, r};
  for (auto& row : base) {
    std::sort(row.begin(), row.end());
    row.erase(std::unique(row.begin(), row.end()), row.end());
  }
  std::vector<std::pair<int, int>> free;
  for (int x = 0; x < 4; ++x) for (int q = 0; q < 4; ++q)
    if (std::find(base[x].begin(), base[x].end(), q) == base[x].end()) free.push_back({x, q});

  int total = 1 << free.size();
  std::vector<char> negative(total, false);
  int positive_count = 0;
  for (int selected = 0; selected < total; ++selected) {
    std::array<Mask, 10> adj{};
    for (int q = 0; q < 4; ++q) for (int p = q + 1; p < 4; ++p) add_edge(adj, q, p);
    for (int q = 0; q < 4; ++q) add_edge(adj, 4, q);
    for (int x = 5; x < 10; ++x) add_edge(adj, 4, x);
    for (int x = 6; x < 10; ++x) add_edge(adj, 5, x);
    add_edge(adj, 6, 7);
    add_edge(adj, 8, 9);
    add_edge(adj, 5, h);
    add_edge(adj, 5, r);
    for (int x = 0; x < 4; ++x) for (int q : base[x]) add_edge(adj, 6 + x, q);
    for (int bit = 0; bit < static_cast<int>(free.size()); ++bit)
      if (selected & (1 << bit)) add_edge(adj, 6 + free[bit].first, free[bit].second);
    if (has_k7(adj)) ++positive_count;
    else negative[selected] = true;
  }

  std::vector<int> maximal;
  for (int mask = 0; mask < total; ++mask) if (negative[mask]) {
    bool is_maximal = true;
    for (int bit = 0; bit < static_cast<int>(free.size()); ++bit)
      if (!(mask & (1 << bit)) && negative[mask | (1 << bit)]) { is_maximal = false; break; }
    if (is_maximal) maximal.push_back(mask);
  }
  std::cout << "H=" << h << " R=" << r << " free=" << free.size()
            << " positive=" << positive_count << " negative=" << total - positive_count
            << " maximal=" << maximal.size() << "\n";
  std::array<int, 5> minimum_column_hist{};
  std::array<int, 5> minimum_nonhub_column_hist{};
  std::array<int, 5> minimum_row_hist{};
  const char labels[4] = {'a', 'c', '1', '2'};
  bool printed_unique_dark_example = false;
  for (int mask : maximal) {
    std::array<std::vector<int>, 4> rows = base;
    for (int bit = 0; bit < static_cast<int>(free.size()); ++bit)
      if (mask & (1 << bit)) rows[free[bit].first].push_back(free[bit].second);
    int min_row = 4;
    int min_col = 4;
    int min_nonhub_col = 4;
    for (int x = 0; x < 4; ++x) min_row = std::min(min_row, static_cast<int>(rows[x].size()));
    for (int q = 0; q < 4; ++q) {
      int degree = 0;
      for (int x = 0; x < 4; ++x)
        if (std::find(rows[x].begin(), rows[x].end(), q) != rows[x].end()) ++degree;
      min_col = std::min(min_col, degree);
      if (q != h && q != r) min_nonhub_col = std::min(min_nonhub_col, degree);
    }
    ++minimum_row_hist[min_row];
    ++minimum_column_hist[min_col];
    ++minimum_nonhub_column_hist[min_nonhub_col];
    if (!printed_unique_dark_example) {
      auto sees = [&](int q, int first, int second) {
        return std::find(rows[first].begin(), rows[first].end(), q) != rows[first].end() ||
               std::find(rows[second].begin(), rows[second].end(), q) != rows[second].end();
      };
      for (int dark = 0; dark < 4 && !printed_unique_dark_example; ++dark) {
        if (dark == h || dark == r || sees(dark, 0, 1) || !sees(dark, 2, 3)) continue;
        bool all_others_cross = true;
        for (int q = 0; q < 4; ++q) if (q != dark)
          all_others_cross &= sees(q, 0, 1) && sees(q, 2, 3);
        if (!all_others_cross) continue;
        std::cout << "  unique-A-dark example dark=" << dark;
        for (int x = 0; x < 4; ++x) {
          std::sort(rows[x].begin(), rows[x].end());
          std::cout << " " << labels[x] << "=";
          for (int q : rows[x]) std::cout << q;
        }
        std::cout << "\n";
        printed_unique_dark_example = true;
      }
    }
    constexpr bool print_rows = false;
    if (print_rows) {
      std::cout << "  ";
      for (int x = 0; x < 4; ++x) {
        std::sort(rows[x].begin(), rows[x].end());
        std::cout << labels[x] << "=";
        for (int q : rows[x]) std::cout << q;
        std::cout << (x == 3 ? '\n' : ' ');
      }
    }
  }
  std::cout << "  min-row histogram";
  for (int i = 0; i <= 4; ++i) if (minimum_row_hist[i]) std::cout << " " << i << ":" << minimum_row_hist[i];
  std::cout << "\n  min-column histogram";
  for (int i = 0; i <= 4; ++i) if (minimum_column_hist[i]) std::cout << " " << i << ":" << minimum_column_hist[i];
  std::cout << "\n  min-nonhub-column histogram";
  for (int i = 0; i <= 4; ++i) if (minimum_nonhub_column_hist[i]) std::cout << " " << i << ":" << minimum_nonhub_column_hist[i];
  std::cout << "\n";
}

int main() {
  make_candidates();
  std::cout << "candidate branch partitions " << candidates.size() << "\n";
  run_atlas(0, 0);
  run_atlas(0, 1);
}
