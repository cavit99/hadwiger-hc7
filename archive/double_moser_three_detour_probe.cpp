// Discovery probe: add three internally disjoint clean paths, with six
// distinct endpoints, to the double-Moser core and test for K7.

#include <tuple>

#define main clean_two_linkage_original_main
#include "double_moser_clean_2linkage_probe.cpp"
#undef main

int main() {
  constexpr std::array<int, 8> interface{2, 3, 4, 5, 6, 7, 8, 9};
  constexpr std::array<const char*, 13> names{
      "u", "v", "x1", "x2", "x3", "x4", "a", "b", "p", "q",
      "r", "s", "t"};
  int total = 0, positive = 0;
  // Choose six terminals, then the fifteen perfect matchings, canonically.
  for (int omitted1 = 0; omitted1 < 8; ++omitted1)
    for (int omitted2 = omitted1 + 1; omitted2 < 8; ++omitted2) {
      std::vector<int> terminals;
      for (int i = 0; i < 8; ++i)
        if (i != omitted1 && i != omitted2) terminals.push_back(i);
      int first = terminals.front();
      for (size_t j = 1; j < terminals.size(); ++j) {
        int second = terminals[j];
        std::vector<int> rest;
        for (int x : terminals) if (x != first && x != second) rest.push_back(x);
        int third = rest.front();
        for (size_t l = 1; l < rest.size(); ++l) {
          int fourth = rest[l];
          std::vector<int> tail;
          for (int x : rest) if (x != third && x != fourth) tail.push_back(x);
          ++total;
          auto edges = core();
          for (auto [internal, left, right] :
               {std::tuple{10, first, second},
                std::tuple{11, third, fourth},
                std::tuple{12, tail[0], tail[1]}}) {
            edges.insert(edge(internal, interface[left]));
            edges.insert(edge(internal, interface[right]));
          }
          auto model = find_k7<13>(edges);
          if (!model.empty()) {
            ++positive;
            std::cout << names[interface[first]] << names[interface[second]]
                      << " | " << names[interface[third]] << names[interface[fourth]]
                      << " | " << names[interface[tail[0]]] << names[interface[tail[1]]]
                      << '\n';
          }
        }
      }
    }
  std::cout << "positive=" << positive << " total=" << total << '\n';
}
