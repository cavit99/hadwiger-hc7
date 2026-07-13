// Exact K7-minor atlas for the seven mixed ordinary-fan collisions
// combined with every covering split of an opposite Moser C5 crossing.

#include <algorithm>
#include <array>
#include <bit>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <set>
#include <string>
#include <utility>
#include <vector>

using Mask = uint16_t;

static std::pair<int, int> edge(int a, int b) {
  if (a > b) std::swap(a, b);
  return {a, b};
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
  connected.reserve(1 << n);
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
    const int needed = 7 - depth;
    if (static_cast<int>(candidates.size()) < needed) return false;
    for (size_t pos = 0; pos < candidates.size(); ++pos) {
      Mask bag = connected[candidates[pos]];
      if (bag & used) continue;
      std::vector<int> next;
      next.reserve(candidates.size() - pos - 1);
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
  for (int i = 0; i < static_cast<int>(all.size()); ++i) all[i] = i;
  return dfs(dfs, 0, all, 0);
}

int main(int argc, char** argv) {
  const std::array<int, 5> physical{0, 5, 2, 4, 6};
  using ProfilePair =
      std::pair<std::array<int, 2>, std::array<int, 2>>;
  const std::array<ProfilePair, 7> collisions{
      ProfilePair{{0, 3}, {1, 3}}, ProfilePair{{0, 2}, {2, 4}},
      ProfilePair{{0, 2}, {0, 3}}, ProfilePair{{1, 4}, {2, 4}},
      ProfilePair{{1, 3}, {1, 4}}, ProfilePair{{0, 2}, {1, 4}},
      ProfilePair{{0, 3}, {2, 4}},
  };
  const std::array<int, 5> order{0, 2, 6, 5, 4};
  const std::set<int> u{0, 2, 4, 5, 6};
  constexpr int a = 1, b = 3, w = 7, v = 8;
  constexpr int body = 9, z1 = 10, z2 = 11, x = 12, y = 13;

  std::set<std::pair<int, int>> base;
  for (auto [p, q] : std::array<std::pair<int, int>, 11>{
           {{0, 1}, {0, 2}, {0, 3}, {0, 4}, {1, 2}, {1, 6},
            {2, 6}, {3, 4}, {3, 5}, {4, 5}, {5, 6}}})
    base.insert(edge(p, q));
  for (int q = 0; q < 7; ++q) base.insert(edge(v, q));
  base.insert(edge(body, z1));
  base.insert(edge(body, z2));
  base.insert(edge(z1, z2));
  base.insert(edge(x, y));

  const std::array<std::array<int, 2>, 5> profiles{
      std::array<int, 2>{0, 2}, std::array<int, 2>{0, 3},
      std::array<int, 2>{1, 3}, std::array<int, 2>{1, 4},
      std::array<int, 2>{2, 4},
  };
  const bool pair_only = argc > 1 && std::string(argv[1]) == "pairs";

  if (!pair_only) {

  int checked = 0;
  int negative = 0;
  for (const auto& collision : collisions) {
    std::set<int> first_fan{a, w}, second_fan{a, w};
    for (int q : collision.first) first_fan.insert(physical[q]);
    for (int q : collision.second) second_fan.insert(physical[q]);
    std::set<int> body_labels = u;
    body_labels.insert(a);
    body_labels.insert(w);
    for (int q : first_fan) body_labels.erase(q);
    for (int q : second_fan) body_labels.erase(q);

    for (int omitted = 0; omitted < 5; ++omitted) {
      std::array<int, 4> places{};
      int at = 0;
      for (int i = 0; i < 5; ++i)
        if (i != omitted) places[at++] = i;
      std::set<int> first_cross{order[places[0]], order[places[2]]};
      std::set<int> second_cross{order[places[1]], order[places[3]]};
      std::vector<int> remaining;
      for (int q : u)
        if (!first_cross.count(q) && !second_cross.count(q))
          remaining.push_back(q);
      remaining.push_back(b);
      remaining.push_back(w);
      assert(remaining.size() == 3);
      for (int mask = 0; mask < 8; ++mask) {
        std::set<int> px = first_cross, py = second_cross;
        for (int i = 0; i < 3; ++i)
          (mask & (1 << i) ? px : py).insert(remaining[i]);

        auto graph = base;
        for (int q : first_fan) graph.insert(edge(z1, q));
        for (int q : second_fan) graph.insert(edge(z2, q));
        for (int q : body_labels) graph.insert(edge(body, q));
        for (int q : px) graph.insert(edge(x, q));
        for (int q : py) graph.insert(edge(y, q));
        if (!has_k7<14>(graph)) {
          ++negative;
          std::cout << "negative collision " << collision.first[0]
                    << collision.first[1] << "/" << collision.second[0]
                    << collision.second[1] << " omitted=" << omitted
                    << " mask=" << mask << std::endl;

          // The P14 fan vertex has boundary neighbours {a,5,6,w}.
          // Since a5 is the only missing edge inside {a,5,6}, Dirac's
          // alpha(N)<=2 forces aw or 5w.  Test both monotone repairs.
          auto with_aw = graph;
          with_aw.insert(edge(a, w));
          auto with_5w = graph;
          with_5w.insert(edge(5, w));
          bool aw_repairs = has_k7<14>(with_aw);
          bool fivew_repairs = has_k7<14>(with_5w);
          std::cout << "  Dirac repairs aw=" << aw_repairs
                    << " 5w=" << fivew_repairs << std::endl;
          assert(aw_repairs && fivew_repairs);

          // A third piece t, adjacent to both crossing carriers, is tested
          // after moving one non-demanded portal from its old carrier.
          constexpr int t = 14;
          bool repaired_once = false;
          for (int q : px) {
            if (first_cross.count(q)) continue;
            auto repaired = graph;
            repaired.erase(edge(x, q));
            repaired.insert(edge(x, t));
            repaired.insert(edge(y, t));
            repaired.insert(edge(t, q));
            if (has_k7<15>(repaired)) {
              std::cout << "  repaired from x by portal " << q << std::endl;
              repaired_once = true;
              break;
            }
          }
          if (!repaired_once) {
            for (int q : py) {
              if (second_cross.count(q)) continue;
              auto repaired = graph;
              repaired.erase(edge(y, q));
              repaired.insert(edge(x, t));
              repaired.insert(edge(y, t));
              repaired.insert(edge(t, q));
              if (has_k7<15>(repaired)) {
                std::cout << "  repaired from y by portal " << q << std::endl;
                repaired_once = true;
                break;
              }
            }
          }
          assert(repaired_once);
        }
        ++checked;
      }
    }
  }
  assert(checked == 7 * 5 * 8);
  assert(negative == 8);
  std::cout << "checked " << checked
            << " mixed-fan/opposite-crossing quotients; negative "
            << negative << "\n";

  // Three consecutive ordinary fan vertices.  This is the next local
  // window after all two-row singleton collisions have been eliminated.
  constexpr int body3 = 9, q1 = 10, q2 = 11, q3 = 12;
  constexpr int cx = 13, cy = 14;
  auto base3 = std::set<std::pair<int, int>>{};
  for (auto [p, q] : std::array<std::pair<int, int>, 11>{
           {{0, 1}, {0, 2}, {0, 3}, {0, 4}, {1, 2}, {1, 6},
            {2, 6}, {3, 4}, {3, 5}, {4, 5}, {5, 6}}})
    base3.insert(edge(p, q));
  for (int q = 0; q < 7; ++q) base3.insert(edge(v, q));
  for (int q : {q1, q2, q3}) base3.insert(edge(body3, q));
  base3.insert(edge(q1, q2));
  base3.insert(edge(q2, q3));
  base3.insert(edge(cx, cy));

  int triple_checked = 0, triple_negative = 0;
  for (const auto& p1 : profiles)
    for (const auto& p2 : profiles)
      for (const auto& p3 : profiles) {
        std::array<std::set<int>, 3> fan_contacts;
        for (auto& contacts : fan_contacts) contacts = {a, w};
        for (int q : p1) fan_contacts[0].insert(physical[q]);
        for (int q : p2) fan_contacts[1].insert(physical[q]);
        for (int q : p3) fan_contacts[2].insert(physical[q]);
        std::set<int> remainder = u;
        remainder.insert(a);
        remainder.insert(w);
        for (const auto& contacts : fan_contacts)
          for (int q : contacts) remainder.erase(q);

        for (int omitted = 0; omitted < 5; ++omitted) {
          std::array<int, 4> places{};
          int at = 0;
          for (int i = 0; i < 5; ++i)
            if (i != omitted) places[at++] = i;
          std::set<int> first_cross{order[places[0]], order[places[2]]};
          std::set<int> second_cross{order[places[1]], order[places[3]]};
          std::vector<int> remaining;
          for (int q : u)
            if (!first_cross.count(q) && !second_cross.count(q))
              remaining.push_back(q);
          remaining.push_back(b);
          remaining.push_back(w);
          for (int mask = 0; mask < 8; ++mask) {
            std::set<int> px = first_cross, py = second_cross;
            for (int i = 0; i < 3; ++i)
              (mask & (1 << i) ? px : py).insert(remaining[i]);
            auto graph = base3;
            for (int q : fan_contacts[0]) graph.insert(edge(q1, q));
            for (int q : fan_contacts[1]) graph.insert(edge(q2, q));
            for (int q : fan_contacts[2]) graph.insert(edge(q3, q));
            for (int q : remainder) graph.insert(edge(body3, q));
            for (int q : px) graph.insert(edge(cx, q));
            for (int q : py) graph.insert(edge(cy, q));
            if (!has_k7<15>(graph)) {
              ++triple_negative;
              std::cout << "negative fan triple " << p1[0] << p1[1]
                        << "/" << p2[0] << p2[1] << "/" << p3[0]
                        << p3[1] << " omitted=" << omitted
                        << " mask=" << mask << std::endl;
            }
            ++triple_checked;
          }
        }
      }
  assert(triple_checked == 5 * 5 * 5 * 5 * 8);
  assert(triple_negative == 0);
  std::cout << "checked " << triple_checked
            << " three-fan/opposite-crossing quotients; negative "
            << triple_negative << "\n";
  }

  // Endpoint colours of a two-vertex removable fan can shrink the lists,
  // so audit every unordered ordinary-profile pair, not only the seven
  // pairs which collide before the two outer-corner colours are imposed.
  int all_pair_checked = 0, all_pair_negative = 0;
  std::set<std::pair<int, int>> negative_pair_types;
  const std::array<std::pair<int, int>, 3> untested_pairs{
      std::pair<int, int>{0, 2}, std::pair<int, int>{1, 3},
      std::pair<int, int>{2, 4},
  };
  for (auto [first_profile, second_profile] : untested_pairs) {
      std::set<int> first_fan{a, w}, second_fan{a, w};
      for (int q : profiles[first_profile]) first_fan.insert(physical[q]);
      for (int q : profiles[second_profile]) second_fan.insert(physical[q]);
      std::set<int> body_labels = u;
      body_labels.insert(a);
      body_labels.insert(w);
      for (int q : first_fan) body_labels.erase(q);
      for (int q : second_fan) body_labels.erase(q);
      for (int omitted = 0; omitted < 5; ++omitted) {
        std::array<int, 4> places{};
        int at = 0;
        for (int i = 0; i < 5; ++i)
          if (i != omitted) places[at++] = i;
        std::set<int> first_cross{order[places[0]], order[places[2]]};
        std::set<int> second_cross{order[places[1]], order[places[3]]};
        std::vector<int> remaining;
        for (int q : u)
          if (!first_cross.count(q) && !second_cross.count(q))
            remaining.push_back(q);
        remaining.push_back(b);
        remaining.push_back(w);
        for (int mask = 0; mask < 8; ++mask) {
          std::set<int> px = first_cross, py = second_cross;
          for (int i = 0; i < 3; ++i)
            (mask & (1 << i) ? px : py).insert(remaining[i]);
          auto graph = base;
          for (int q : first_fan) graph.insert(edge(z1, q));
          for (int q : second_fan) graph.insert(edge(z2, q));
          for (int q : body_labels) graph.insert(edge(body, q));
          for (int q : px) graph.insert(edge(x, q));
          for (int q : py) graph.insert(edge(y, q));
          if (!has_k7<14>(graph)) {
            ++all_pair_negative;
            negative_pair_types.insert({first_profile, second_profile});
            // Both surviving types contain P13, whose boundary neighbours
            // are {a,4,5,w} with only 45 present among {a,4,5}.  Dirac
            // forces aw, or forces both 4w and 5w.  Either monotone repair
            // is K7-positive in every surviving quotient.
            auto with_aw = graph;
            with_aw.insert(edge(a, w));
            auto with_4w_5w = graph;
            with_4w_5w.insert(edge(4, w));
            with_4w_5w.insert(edge(5, w));
            assert(has_k7<14>(with_aw));
            assert(has_k7<14>(with_4w_5w));
          }
          ++all_pair_checked;
        }
      }
    }
  assert(all_pair_checked == 3 * 5 * 8);
  std::cout << "checked " << all_pair_checked
            << " remaining-pair/opposite-crossing quotients; negative "
            << all_pair_negative << " in profile types";
  for (auto [first, second] : negative_pair_types)
    std::cout << " " << profiles[first][0] << profiles[first][1] << "/"
              << profiles[second][0] << profiles[second][1];
  std::cout << "\n";
  const std::set<std::pair<int, int>> expected_negative_types{{0, 2},
                                                               {2, 4}};
  assert(all_pair_negative == 32);
  assert(negative_pair_types == expected_negative_types);
}
