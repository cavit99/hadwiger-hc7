#include <array>
#include <cstdint>
#include <iostream>
#include <vector>

std::array<unsigned, 36> types{};
std::array<unsigned, 7> rows{};
std::array<int, 7> choice{};
std::uint64_t checked = 0;

bool assign_rows(int pos, unsigned used) {
  if (pos == 7) return true;
  unsigned miss = rows[pos];
  for (int x = 0; x < 9; ++x) {
    if ((used >> x) & 1U) continue;
    if ((miss >> x) & 1U) continue;
    bool good = true;
    for (int j = 0; j < pos; ++j) {
      int y = choice[j];
      if (((miss >> y) & 1U) && ((rows[j] >> x) & 1U)) {
        good = false;
        break;
      }
    }
    if (!good) continue;
    choice[pos] = x;
    if (assign_rows(pos + 1, used | (1U << x))) return true;
  }
  return false;
}

bool enumerate(int pos, int first_type) {
  if (pos == 7) {
    ++checked;
    if (!assign_rows(0, 0)) {
      std::cout << "COUNTEREXAMPLE";
      for (auto row : rows) std::cout << ' ' << row;
      std::cout << "\n";
      return false;
    }
    return true;
  }
  for (int t = first_type; t < 36; ++t) {
    rows[pos] = types[t];
    if (!enumerate(pos + 1, t)) return false;
  }
  return true;
}

int main() {
  int k = 0;
  for (int x = 0; x < 9; ++x)
    for (int y = x + 1; y < 9; ++y)
      types[k++] = (1U << x) | (1U << y);
  bool ok = enumerate(0, 0);
  std::cout << (ok ? "ALL_HAVE_CERTIFICATE " : "STOPPED ") << checked << "\n";
}
