#include <array>
#include <algorithm>
#include <bit>
#include <cstdint>
#include <iostream>
#include <vector>

namespace {

constexpr int kVertices = 5;
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
        dominates(neighbours, singleton)) return true;
  }
  for (int i = 0; i < 3; ++i)
    for (int j = 0; j < 3; ++j)
      if (i != j && dominates(matching[i], matching[j])) return true;
  return false;
}

bool proper_hall_circuit(const std::array<int, kClasses>& portals) {
  std::array<int, 1 << kClasses> unions{};
  for (int labels = 1; labels < (1 << kClasses); ++labels) {
    const int bit = labels & -labels;
    const int index = std::countr_zero(static_cast<unsigned>(bit));
    unions[labels] = unions[labels ^ bit] | portals[index];
    if (labels != (1 << kClasses) - 1 &&
        std::popcount(static_cast<unsigned>(unions[labels])) <
            std::popcount(static_cast<unsigned>(labels))) return false;
  }
  return unions.back() == kFull;
}

bool all_splits_negative_and_degree(
    const std::array<int, kClasses>& portals, int z_portals) {
  std::array<int, kVertices> rows{};
  for (int label = 0; label < 6; ++label)
    for (int vertex = 0; vertex < kVertices; ++vertex)
      if ((portals[label] >> vertex) & 1) rows[vertex] |= 1 << label;
  for (int vertex = 0; vertex < kVertices; ++vertex) {
    if ((z_portals >> vertex) & 1) rows[vertex] |= 1 << 6;
    const int contacts = std::popcount(static_cast<unsigned>(rows[vertex]));
    if (4 + contacts < 7) return false;
  }

  for (int side = 1; side < kFull; ++side) {
    int contact_left = 0, contact_right = 0;
    for (int vertex = 0; vertex < kVertices; ++vertex) {
      if ((side >> vertex) & 1) contact_left |= rows[vertex];
      else contact_right |= rows[vertex];
    }
    const int defect_left = 0b1111111 ^ contact_left;
    const int defect_right = 0b1111111 ^ contact_right;
    if (!dominates_bad_defect(defect_left, defect_right)) return false;
  }
  return true;
}

bool inspect(const std::array<int, kClasses>& portals,
             std::uint64_t& linkage_survivors,
             std::uint64_t& hall_survivors) {
  std::array<bool, 6> frame{}, unlock{};
  for (int i = 0; i < 6; ++i) {
    frame[i] = has_two(portals, (i + 4) % 6, (i + 5) % 6,
                       (i + 2) % 6, (i + 3) % 6);
    unlock[i] = has_two(portals, (i + 4) % 6, (i + 5) % 6,
                        (i + 2) % 6, (i + 3) % 6, i, (i + 1) % 6);
  }
  int opposite_pairs = 0;
  for (int i = 0; i < 3; ++i) opposite_pairs += frame[i] && frame[i + 3];
  if (opposite_pairs < 2) return false;
  for (int i = 0; i < 3; ++i)
    if (has_two(portals, i, (i + 1) % 6, (i + 3) % 6,
                (i + 4) % 6)) return false;
  if (has_three(portals, 0) || has_three(portals, 1)) return false;
  for (int i = 0; i < 6; ++i)
    if (frame[i] && unlock[i]) return false;
  ++linkage_survivors;

  if (!proper_hall_circuit(portals)) return false;
  ++hall_survivors;
  for (int z_portals = 1; z_portals <= kFull; ++z_portals)
    if (all_splits_negative_and_degree(portals, z_portals)) return true;
  return false;
}

}  // namespace

int main() {
  // K5: every nonempty vertex set is connected.
  for (int left = 1; left <= kFull; ++left)
    for (int right = 1; right <= kFull; ++right)
      for (int set = 1; set <= kFull; ++set)
        if ((set & left) && (set & right)) pieces[left][right].push_back(set);

  std::array<int, kClasses> portals{};
  std::uint64_t assignments = 0, linkage_survivors = 0, hall_survivors = 0,
                hall_circuits = 0, actual_survivors = 0;

  // Rotate a minimum-cardinality class to position 0, then use the S5
  // symmetry of K5 to make it an initial segment.  This covers every
  // assignment, with harmless duplicates when minima are repeated.
  for (int first_size = 1; first_size <= 5; ++first_size) {
    portals[0] = (1 << first_size) - 1;
    const auto recurse = [&](auto&& self, int index) -> void {
      if (index == 6) {
        ++assignments;
        if (proper_hall_circuit(portals)) ++hall_circuits;
        if (inspect(portals, linkage_survivors, hall_survivors)) {
          ++actual_survivors;
          std::cout << "survivor";
          for (int mask : portals) std::cout << ' ' << mask;
          std::cout << '\n';
        }
        return;
      }
      for (int mask = 1; mask <= kFull; ++mask) {
        if (std::popcount(static_cast<unsigned>(mask)) < first_size) continue;
        portals[index] = mask;
        self(self, index + 1);
      }
    };
    recurse(recurse, 1);
  }

  std::cout << "symmetry-reduced assignments " << assignments << '\n';
  std::cout << "linkage survivors " << linkage_survivors << '\n';
  std::cout << "Hall circuits " << hall_circuits << '\n';
  std::cout << "Hall-circuit survivors " << hall_survivors << '\n';
  std::cout << "actual survivors " << actual_survivors << '\n';
  return actual_survivors == 0 ? 0 : 1;
}
