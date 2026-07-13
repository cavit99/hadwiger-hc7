#include <array>
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <set>
#include <vector>

namespace {

constexpr int kVertices = 4;
constexpr int kClasses = 6;
constexpr int kFull = (1 << kVertices) - 1;

std::array<std::array<std::vector<int>, 1 << kVertices>, 1 << kVertices>
    pieces;

bool has_two(const std::array<int, kClasses>& portals, int a, int b,
             int c, int d, int outward_a = -1, int outward_b = -1) {
  for (int left : pieces[portals[a]][portals[b]]) {
    for (int right : pieces[portals[c]][portals[d]]) {
      if ((left & right) != 0) continue;
      if (outward_a < 0 || (left & portals[outward_a]) != 0 ||
          (right & portals[outward_b]) != 0) {
        return true;
      }
    }
  }
  return false;
}

bool has_three(const std::array<int, kClasses>& portals, int parity) {
  const auto& first = pieces[portals[parity]][portals[(parity + 1) % 6]];
  const auto& second =
      pieces[portals[(parity + 2) % 6]][portals[(parity + 3) % 6]];
  const auto& third =
      pieces[portals[(parity + 4) % 6]][portals[(parity + 5) % 6]];
  for (int x : first)
    for (int y : second)
      for (int z : third)
        if ((x & y) == 0 && (x & z) == 0 && (y & z) == 0) return true;
  return false;
}

bool dominates_bad_defect(int left, int right) {
  const std::array<int, 2> triangles = {0b010101, 0b101010};
  const std::array<int, 3> matching = {0b001001, 0b010010, 0b100100};

  auto dominates = [&](int base_left, int base_right) {
    return (left & base_left) == base_left &&
           (right & base_right) == base_right;
  };
  for (int triangle : triangles)
    if (dominates(0, triangle) || dominates(triangle, 0)) return true;
  for (int pair : matching) {
    const int four = 0b111111 ^ pair;
    if (dominates(0, four) || dominates(four, 0)) return true;
  }
  for (int vertex = 0; vertex < 6; ++vertex) {
    const int singleton = 1 << vertex;
    const int neighbours = (1 << ((vertex + 5) % 6)) |
                           (1 << ((vertex + 1) % 6));
    if (dominates(singleton, neighbours) ||
        dominates(neighbours, singleton)) {
      return true;
    }
  }
  for (int i = 0; i < 3; ++i)
    for (int j = 0; j < 3; ++j)
      if (i != j && dominates(matching[i], matching[j])) return true;
  return false;
}

bool all_splits_are_atlas_negative(
    const std::array<int, kClasses>& portals) {
  std::array<int, kVertices> row{};
  for (int boundary = 0; boundary < 6; ++boundary)
    for (int vertex = 0; vertex < kVertices; ++vertex)
      if ((portals[boundary] >> vertex) & 1) row[vertex] |= 1 << boundary;

  for (int side = 1; side < kFull; ++side) {
    int contact_left = 0;
    int contact_right = 0;
    for (int vertex = 0; vertex < kVertices; ++vertex) {
      if ((side >> vertex) & 1)
        contact_left |= row[vertex];
      else
        contact_right |= row[vertex];
    }
    const int defect_left = 0b111111 ^ contact_left;
    const int defect_right = 0b111111 ^ contact_right;
    if (!dominates_bad_defect(defect_left, defect_right)) return false;
  }
  return true;
}

std::uint32_t canonical_code(const std::array<int, kClasses>& portals) {
  std::array<int, kVertices> permutation = {0, 1, 2, 3};
  std::uint32_t best = ~std::uint32_t{0};
  do {
    for (int direction : {-1, 1}) {
      for (int shift = 0; shift < 6; ++shift) {
        std::uint32_t code = 0;
        for (int index = 0; index < 6; ++index) {
          int source = (direction * index + shift) % 6;
          if (source < 0) source += 6;
          int transformed = 0;
          for (int vertex = 0; vertex < 4; ++vertex)
            if ((portals[source] >> vertex) & 1)
              transformed |= 1 << permutation[vertex];
          code = (code << 4) | transformed;
        }
        best = std::min(best, code);
      }
    }
  } while (std::next_permutation(permutation.begin(), permutation.end()));
  return best;
}

void inspect(const std::array<int, kClasses>& portals, std::uint64_t& coarse,
             std::uint64_t& tight, std::uint64_t& atlas_tight,
             int& best_minimum_contact,
             std::array<int, kClasses>& best_example,
             std::set<std::uint32_t>& orbit_codes) {
  std::array<bool, 6> frame{};
  std::array<bool, 6> unlock{};
  for (int i = 0; i < 6; ++i) {
    frame[i] = has_two(portals, (i + 4) % 6, (i + 5) % 6,
                       (i + 2) % 6, (i + 3) % 6);
    unlock[i] = has_two(portals, (i + 4) % 6, (i + 5) % 6,
                        (i + 2) % 6, (i + 3) % 6, i, (i + 1) % 6);
  }
  int opposite_pairs = 0;
  for (int i = 0; i < 3; ++i) opposite_pairs += frame[i] && frame[i + 3];
  if (opposite_pairs < 2) return;

  for (int i = 0; i < 3; ++i)
    if (has_two(portals, i, (i + 1) % 6, (i + 3) % 6,
                (i + 4) % 6))
      return;
  if (has_three(portals, 0) || has_three(portals, 1)) return;
  ++coarse;

  for (int i = 0; i < 6; ++i)
    if (frame[i] && unlock[i]) return;
  ++tight;

  if (!all_splits_are_atlas_negative(portals)) return;
  ++atlas_tight;
  orbit_codes.insert(canonical_code(portals));

  int minimum_contact = 6;
  for (int vertex = 0; vertex < kVertices; ++vertex) {
    int count = 0;
    for (int boundary = 0; boundary < 6; ++boundary)
      count += (portals[boundary] >> vertex) & 1;
    if (count < minimum_contact) minimum_contact = count;
  }
  if (minimum_contact > best_minimum_contact) {
    best_minimum_contact = minimum_contact;
    best_example = portals;
  }
}

}  // namespace

int main() {
  for (int left = 1; left <= kFull; ++left) {
    for (int right = 1; right <= kFull; ++right) {
      for (int set = 1; set <= kFull; ++set)
        if ((set & left) != 0 && (set & right) != 0)
          pieces[left][right].push_back(set);
    }
  }

  std::uint64_t coarse = 0;
  std::uint64_t tight = 0;
  std::uint64_t atlas_tight = 0;
  int best_minimum_contact = -1;
  std::array<int, kClasses> best_example{};
  std::set<std::uint32_t> orbit_codes;
  std::array<int, kClasses> portals{};

  for (portals[0] = 1; portals[0] <= kFull; ++portals[0])
    for (portals[1] = 1; portals[1] <= kFull; ++portals[1])
      for (portals[2] = 1; portals[2] <= kFull; ++portals[2])
        for (portals[3] = 1; portals[3] <= kFull; ++portals[3])
          for (portals[4] = 1; portals[4] <= kFull; ++portals[4])
            for (portals[5] = 1; portals[5] <= kFull; ++portals[5])
              inspect(portals, coarse, tight, atlas_tight,
                      best_minimum_contact, best_example, orbit_codes);

  std::cout << "assignments " << 15 * 15 * 15 * 15 * 15 * 15 << '\n';
  std::cout << "coarse survivors " << coarse << '\n';
  std::cout << "tight survivors " << tight << '\n';
  std::cout << "tight + exact-split survivors " << atlas_tight << '\n';
  std::cout << "dihedral x S4 orbit types " << orbit_codes.size() << '\n';
  std::cout << "orbit representatives";
  for (std::uint32_t code : orbit_codes) std::cout << " 0x" << std::hex << code;
  std::cout << std::dec << '\n';
  std::cout << "maximum minimum C6-contact count " << best_minimum_contact
            << '\n';
  std::cout << "example";
  for (int mask : best_example) std::cout << ' ' << mask;
  std::cout << '\n';

  // With the universal seventh boundary contact, a K4 shore vertex has
  // total degree 3 + 1 + (# C6 contacts).  Thus delta >= 7 would require
  // minimum C6-contact count at least three.
  if (best_minimum_contact >= 3) return 1;
  return 0;
}
