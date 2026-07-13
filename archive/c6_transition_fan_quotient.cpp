#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <vector>

using Bags = std::array<uint16_t, 7>;
static std::vector<Bags> candidates;

static void rec(const std::vector<int>& support, int at,
                std::vector<uint16_t>& blocks) {
  if (at == (int)support.size()) {
    if (blocks.size() == 7) {
      Bags b{};
      std::copy(blocks.begin(), blocks.end(), b.begin());
      candidates.push_back(b);
    }
    return;
  }
  uint16_t bit = uint16_t(1) << support[at];
  for (size_t i = 0; i < blocks.size(); ++i) {
    blocks[i] |= bit;
    rec(support, at + 1, blocks);
    blocks[i] ^= bit;
  }
  if (blocks.size() < 7) {
    blocks.push_back(bit);
    rec(support, at + 1, blocks);
    blocks.pop_back();
  }
}

static void build_candidates() {
  for (int mask = 0; mask < (1 << 13); ++mask) {
    if (__builtin_popcount(mask) < 7) continue;
    std::vector<int> support;
    for (int i = 0; i < 13; ++i)
      if (mask & (1 << i)) support.push_back(i);
    std::vector<uint16_t> blocks{
        static_cast<uint16_t>(uint16_t(1) << support[0])};
    rec(support, 1, blocks);
  }
  std::sort(candidates.begin(), candidates.end(), [](const Bags& x,
                                                       const Bags& y) {
    int a = 0, b = 0;
    for (int i = 0; i < 7; ++i) {
      a += __builtin_popcount(x[i]);
      b += __builtin_popcount(y[i]);
    }
    return a > b;
  });
}

static void edge(std::array<uint16_t, 13>& a, int x, int y) {
  a[x] |= uint16_t(1) << y;
  a[y] |= uint16_t(1) << x;
}

static bool connected(uint16_t mask, const std::array<uint16_t, 13>& a) {
  uint16_t seen = mask & -mask;
  while (true) {
    uint16_t next = seen, bits = seen;
    while (bits) {
      int v = __builtin_ctz(bits);
      next |= a[v] & mask;
      bits &= bits - 1;
    }
    if (next == seen) return seen == mask;
    seen = next;
  }
}

static bool model(const std::array<uint16_t, 13>& a, Bags& answer) {
  for (const auto& b : candidates) {
    bool ok = true;
    std::array<uint16_t, 7> n{};
    for (int i = 0; i < 7 && ok; ++i) {
      if (!connected(b[i], a)) { ok = false; break; }
      uint16_t bits = b[i];
      while (bits) {
        int v = __builtin_ctz(bits);
        n[i] |= a[v];
        bits &= bits - 1;
      }
      for (int j = 0; j < i; ++j)
        if (!(n[i] & b[j])) { ok = false; break; }
    }
    if (ok) { answer = b; return true; }
  }
  return false;
}

// S=0..6, H=7, u=8, four arms=9..12 to supplied labels.
static std::array<uint16_t, 13> graph(const std::array<int,4>& labels,
                                      const std::vector<int>& direct) {
  std::array<uint16_t, 13> a{};
  for (int i = 0; i < 7; ++i)
    for (int j = i + 1; j < 7; ++j) {
      bool missing = i < 6 && j < 6 && (j == i + 1 || (i == 0 && j == 5));
      if (!missing) edge(a, i, j);
    }
  for (int i = 0; i < 7; ++i) edge(a, i, 7);
  for (int x : direct) edge(a, 8, x);
  for (int i = 0; i < 4; ++i) {
    edge(a, 8, 9 + i);
    edge(a, 9 + i, labels[i]);
  }
  return a;
}

// Exact L-M seven-adhesion cell split along the two labelled fan entries.
// S=0..6,H=7,u=8,A=9,x=10,R1=11,R5=12.
static std::array<uint16_t, 13> split_rung(int code) {
  std::array<uint16_t, 13> a{};
  for (int i = 0; i < 7; ++i)
    for (int j = i + 1; j < 7; ++j) {
      bool missing = i < 6 && j < 6 && (j == i + 1 || (i == 0 && j == 5));
      if (!missing) edge(a, i, j);
    }
  for (int s = 0; s < 7; ++s) edge(a, s, 7);
  for (int s : {0,2,3,4,6}) edge(a, s, 9);
  edge(a, 8, 2);
  edge(a, 8, 9);
  edge(a, 8, 10);
  edge(a, 10, 11);
  edge(a, 9, 12);
  edge(a, 11, 12);
  edge(a, 1, 11);
  edge(a, 5, 12);
  for (int label : {3,4,6}) {
    int digit = code % 3;
    code /= 3;
    if (digit != 1) edge(a, label, 11);
    if (digit != 0) edge(a, label, 12);
  }
  return a;
}

// Both labelled terminal pieces enter through one connected A-helper.
static std::array<uint16_t, 13> both_bypass(int code) {
  std::array<uint16_t, 13> a{};
  for (int i = 0; i < 7; ++i)
    for (int j = i + 1; j < 7; ++j) {
      bool missing = i < 6 && j < 6 && (j == i + 1 || (i == 0 && j == 5));
      if (!missing) edge(a, i, j);
    }
  for (int s = 0; s < 7; ++s) edge(a, s, 7);
  for (int s : {0,2,3,4,6}) edge(a, s, 9);
  edge(a, 8, 2);
  edge(a, 8, 9);
  edge(a, 9, 11);
  edge(a, 9, 12);
  edge(a, 11, 12);
  edge(a, 1, 11);
  edge(a, 5, 12);
  for (int label : {3,4,6}) {
    int digit = code % 3;
    code /= 3;
    if (digit != 1) edge(a, label, 11);
    if (digit != 0) edge(a, label, 12);
  }
  return a;
}

// Two disjoint A-prefixes retained: after contracting each prefix into
// its terminal piece, u meets R1,R5 separately and the residual A-core
// meets both pieces while retaining the aggregate A boundary row.
static std::array<uint16_t, 13> two_prefix_core(int code) {
  std::array<uint16_t, 13> a{};
  for (int i = 0; i < 7; ++i)
    for (int j = i + 1; j < 7; ++j) {
      bool missing = i < 6 && j < 6 && (j == i + 1 || (i == 0 && j == 5));
      if (!missing) edge(a, i, j);
    }
  for (int s = 0; s < 7; ++s) edge(a, s, 7);
  for (int s : {0,2,3,4,6}) edge(a, s, 9);
  edge(a, 8, 2);
  edge(a, 8, 11);
  edge(a, 8, 12);
  edge(a, 9, 11);
  edge(a, 9, 12);
  edge(a, 11, 12);
  edge(a, 1, 11);
  edge(a, 5, 12);
  for (int label : {3,4,6}) {
    int digit = code % 3;
    code /= 3;
    if (digit != 1) edge(a, label, 11);
    if (digit != 0) edge(a, label, 12);
  }
  return a;
}

// Minimal exclusive distribution of the aggregate A-row over the
// residual core K and the two retained prefix/terminal pieces, together
// with an exclusive distribution of C's three unlabelled contacts.
static std::array<uint16_t, 13> distributed_core(int a_code, int c_code) {
  std::array<uint16_t, 13> a{};
  for (int i = 0; i < 7; ++i)
    for (int j = i + 1; j < 7; ++j) {
      bool missing = i < 6 && j < 6 && (j == i + 1 || (i == 0 && j == 5));
      if (!missing) edge(a, i, j);
    }
  for (int s = 0; s < 7; ++s) edge(a, s, 7);
  edge(a, 8, 2);
  edge(a, 8, 11);
  edge(a, 8, 12);
  edge(a, 9, 11);
  edge(a, 9, 12);
  edge(a, 11, 12);
  edge(a, 1, 11);
  edge(a, 5, 12);
  for (int label : {0,2,3,4,6}) {
    int choice = a_code % 3;
    a_code /= 3;
    edge(a, label, choice == 0 ? 9 : (choice == 1 ? 11 : 12));
  }
  for (int label : {3,4,6}) {
    int choice = c_code % 2;
    c_code /= 2;
    edge(a, label, choice == 0 ? 11 : 12);
  }
  return a;
}

// Concentration repair: Y is the connected c5-side plus the two-fan
// prefixes; T0,T1,T4 partition the connected target core and induce a
// three-vertex tree.  central=0,1,4 selects its centre.
static std::array<uint16_t, 13> rooted_core_tree(int central) {
  std::array<uint16_t, 13> a{};
  for (int i = 0; i < 7; ++i)
    for (int j = i + 1; j < 7; ++j) {
      bool missing = i < 6 && j < 6 && (j == i + 1 || (i == 0 && j == 5));
      if (!missing) edge(a, i, j);
    }
  // H=7,u=8,Y=9,T0=10,T1=11,T4=12.
  for (int s = 0; s < 7; ++s) edge(a, s, 7);
  edge(a, 8, 2);
  edge(a, 8, 9);
  edge(a, 9, 5);
  edge(a, 9, 10);
  edge(a, 9, 12);
  edge(a, 0, 10);
  edge(a, 1, 11);
  edge(a, 4, 12);
  int centre = central == 0 ? 10 : (central == 1 ? 11 : 12);
  for (int vertex : {10,11,12})
    if (vertex != centre) edge(a, centre, vertex);
  return a;
}

int main(int argc, char** argv) {
  build_candidates();
  std::cout << "candidates " << candidates.size() << "\n";
  if (argc == 3) {
    int ac = std::stoi(argv[1]);
    int cc = std::stoi(argv[2]);
    Bags b{};
    bool yes = model(distributed_core(ac, cc), b);
    std::cout << "distributed-core " << ac << " " << cc << " " << yes << "\n";
    return yes ? 0 : 1;
  }
  if (argc == 2 && std::string(argv[1]) == "audit") {
    auto base = distributed_core(121, 0);
    for (int target : {9, 12}) {
      for (int label : {0, 2, 3, 4, 6}) {
        auto a = base;
        edge(a, target, label);
        Bags b{};
        std::cout << "add " << target << "-" << label << " "
                  << model(a, b) << "\n";
      }
    }
    auto maximal = base;
    for (int target : {9, 12})
      for (int label : {2, 3, 6}) edge(maximal, target, label);
    Bags b{};
    std::cout << "safe-overlap-maximal " << model(maximal, b) << "\n";
    return 0;
  }
  if (argc == 2 && std::string(argv[1]) == "rooted") {
    for (int centre : {0,1,4}) {
      Bags b{};
      bool yes = model(rooted_core_tree(centre), b);
      std::cout << "rooted-core centre " << centre << " " << yes << "\n";
      if (yes) {
        for (auto mask : b) {
          std::cout << "{";
          for (int i=0;i<13;++i) if (mask&(1<<i)) std::cout << i << ",";
          std::cout << "}";
        }
        std::cout << "\n";
      }
    }
    return 0;
  }
  struct Case { const char* name; std::array<int,4> arms; std::vector<int> direct; };
  std::vector<Case> cases = {
    {"L-M", {0,1,3,5}, {2}},
    {"M-R", {0,1,2,4}, {5}},
    {"L-R", {0,1,3,4}, {2,5}},
  };
  for (auto& c : cases) {
    Bags b{};
    bool yes = model(graph(c.arms,c.direct), b);
    std::cout << c.name << " " << yes << "\n";
    if (yes) {
      for (auto mask : b) {
        std::cout << "{";
        for (int i=0;i<13;++i) if (mask&(1<<i)) std::cout << i << ",";
        std::cout << "}";
      }
      std::cout << "\n";
    }
  }
  int negative = 0;
  for (int code = 0; code < 27; ++code) {
    Bags b{};
    bool yes = model(split_rung(code), b);
    if (!yes) ++negative;
    std::cout << "split-rung " << code << " " << yes << "\n";
    if (yes) {
      for (auto mask : b) {
        std::cout << "{";
        for (int i=0;i<13;++i) if (mask&(1<<i)) std::cout << i << ",";
        std::cout << "}";
      }
      std::cout << "\n";
    }
  }
  std::cout << "split-rung negative " << negative << "\n";
  negative = 0;
  for (int code = 0; code < 27; ++code) {
    Bags b{};
    bool yes = model(both_bypass(code), b);
    if (!yes) ++negative;
    std::cout << "both-bypass " << code << " " << yes << "\n";
  }
  std::cout << "both-bypass negative " << negative << "\n";
  negative = 0;
  for (int code = 0; code < 27; ++code) {
    Bags b{};
    bool yes = model(two_prefix_core(code), b);
    if (!yes) ++negative;
    std::cout << "two-prefix-core " << code << " " << yes << "\n";
    if (code == 0 && yes) {
      for (auto mask : b) {
        std::cout << "{";
        for (int i=0;i<13;++i) if (mask&(1<<i)) std::cout << i << ",";
        std::cout << "}";
      }
      std::cout << "\n";
    }
  }
  std::cout << "two-prefix-core negative " << negative << "\n";
  negative = 0;
  for (int ac = 0; ac < 243; ++ac) {
    for (int cc = 0; cc < 8; ++cc) {
      Bags b{};
      bool yes = model(distributed_core(ac, cc), b);
      if (!yes) {
        ++negative;
        if (negative <= 40)
          std::cout << "distributed-core negative " << ac << " " << cc << "\n";
      }
    }
  }
  std::cout << "distributed-core negative-count " << negative << "\n";
}
