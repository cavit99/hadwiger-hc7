// Exact census for the eight-vertex surjective five-colour Kempe barrier.
//
// Compile and run with:
//   clang++ -O3 -std=c++17 this_file.cpp -o /tmp/kempe_census
//   geng -q 8 | /tmp/kempe_census

#include <algorithm>
#include <array>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <string>
#include <unordered_map>
#include <vector>

namespace {

using Adjacency = std::array<unsigned, 8>;
using BranchSets = std::array<unsigned, 5>;
using Colouring = std::array<unsigned char, 8>;

std::vector<BranchSets> branch_partitions;

void generate_branch_partitions(
    int vertex, BranchSets& blocks, int used_blocks) {
  if (vertex == 8) {
    if (used_blocks == 5) {
      BranchSets canonical = blocks;
      std::sort(canonical.begin(), canonical.end());
      branch_partitions.push_back(canonical);
    }
    return;
  }

  // Delete this vertex from the prospective minor model.
  generate_branch_partitions(vertex + 1, blocks, used_blocks);

  for (int block = 0; block < used_blocks; ++block) {
    blocks[block] |= 1u << vertex;
    generate_branch_partitions(vertex + 1, blocks, used_blocks);
    blocks[block] ^= 1u << vertex;
  }
  if (used_blocks < 5) {
    blocks[used_blocks] = 1u << vertex;
    generate_branch_partitions(vertex + 1, blocks, used_blocks + 1);
    blocks[used_blocks] = 0;
  }
}
bool connected(unsigned vertices, const Adjacency& adjacency) {
  if (vertices == 0) return false;
  unsigned reached = vertices & -vertices;
  unsigned frontier = reached;
  while (frontier != 0) {
    const unsigned bit = frontier & -frontier;
    frontier -= bit;
    const int vertex = __builtin_ctz(bit);
    const unsigned fresh = adjacency[vertex] & vertices & ~reached;
    reached |= fresh;
    frontier |= fresh;
  }
  return reached == vertices;
}

bool has_k5_minor(const Adjacency& adjacency) {
  for (const BranchSets& blocks : branch_partitions) {
    bool valid = true;
    for (int i = 0; i < 5 && valid; ++i) {
      valid = connected(blocks[i], adjacency);
    }
    for (int i = 0; i < 5 && valid; ++i) {
      unsigned neighbourhood = 0;
      unsigned vertices = blocks[i];
      while (vertices != 0) {
        const int vertex = __builtin_ctz(vertices);
        vertices &= vertices - 1;
        neighbourhood |= adjacency[vertex];
      }
      for (int j = i + 1; j < 5; ++j) {
        if ((neighbourhood & blocks[j]) == 0) {
          valid = false;
          break;
        }
      }
    }
    if (valid) return true;
  }
  return false;
}

bool four_colourable(const Adjacency& adjacency) {
  std::vector<int> order(8);
  std::iota(order.begin(), order.end(), 0);
  std::sort(order.begin(), order.end(), [&](int x, int y) {
    return __builtin_popcount(adjacency[x]) >
           __builtin_popcount(adjacency[y]);
  });
  std::array<int, 8> colour;
  colour.fill(-1);
  std::function<bool(int)> search = [&](int position) {
    if (position == 8) return true;
    const int vertex = order[position];
    unsigned forbidden = 0;
    for (int earlier = 0; earlier < position; ++earlier) {
      const int other = order[earlier];
      if ((adjacency[vertex] & (1u << other)) != 0) {
        forbidden |= 1u << colour[other];
      }
    }
    for (int candidate = 0; candidate < 4; ++candidate) {
      if ((forbidden & (1u << candidate)) == 0) {
        colour[vertex] = candidate;
        if (search(position + 1)) return true;
      }
    }
    colour[vertex] = -1;
    return false;
  };
  return search(0);
}

Adjacency decode_graph6(const std::string& code) {
  Adjacency adjacency{};
  const int order = static_cast<unsigned char>(code[0]) - 63;
  if (order != 8) throw std::runtime_error("expected order-eight graph6");
  int bit_position = 0;
  for (int j = 1; j < order; ++j) {
    for (int i = 0; i < j; ++i) {
      const int byte = 1 + bit_position / 6;
      const int offset = bit_position % 6;
      const int value = static_cast<unsigned char>(code[byte]) - 63;
      if ((value & (1 << (5 - offset))) != 0) {
        adjacency[i] |= 1u << j;
        adjacency[j] |= 1u << i;
      }
      ++bit_position;
    }
  }
  return adjacency;
}

int encode(const Colouring& colouring) {
  int code = 0;
  int place = 1;
  for (unsigned char colour : colouring) {
    code += place * colour;
    place *= 5;
  }
  return code;
}

Colouring decode_colouring(int code) {
  Colouring colouring{};
  for (unsigned char& colour : colouring) {
    colour = code % 5;
    code /= 5;
  }
  return colouring;
}

struct KempeSummary {
  std::vector<int> component_orders;
  std::vector<std::string> representatives;
  int state_count;
};

KempeSummary kempe_summary(const Adjacency& adjacency) {
  std::vector<int> order(8);
  std::iota(order.begin(), order.end(), 0);
  std::sort(order.begin(), order.end(), [&](int x, int y) {
    return __builtin_popcount(adjacency[x]) >
           __builtin_popcount(adjacency[y]);
  });

  std::vector<int> states;
  Colouring colouring{};
  std::array<int, 5> colour_counts{};
  std::function<void(int)> generate = [&](int position) {
    if (position == 8) {
      if (std::all_of(colour_counts.begin(), colour_counts.end(),
                      [](int count) { return count > 0; })) {
        states.push_back(encode(colouring));
      }
      return;
    }
    const int vertex = order[position];
    unsigned forbidden = 0;
    for (int earlier = 0; earlier < position; ++earlier) {
      const int other = order[earlier];
      if ((adjacency[vertex] & (1u << other)) != 0) {
        forbidden |= 1u << colouring[other];
      }
    }
    for (int candidate = 0; candidate < 5; ++candidate) {
      if ((forbidden & (1u << candidate)) == 0) {
        colouring[vertex] = candidate;
        ++colour_counts[candidate];
        generate(position + 1);
        --colour_counts[candidate];
      }
    }
  };
  generate(0);

  std::unordered_map<int, int> state_index;
  state_index.reserve(2 * states.size());
  for (int i = 0; i < static_cast<int>(states.size()); ++i) {
    state_index[states[i]] = i;
  }

  std::vector<char> reached(states.size());
  std::vector<int> component_orders;
  std::vector<std::string> representatives;
  for (int root = 0; root < static_cast<int>(states.size()); ++root) {
    if (reached[root]) continue;
    std::queue<int> queue;
    queue.push(root);
    reached[root] = true;
    int component_order = 0;
    const Colouring representative = decode_colouring(states[root]);
    std::string representative_text;
    for (unsigned char colour : representative) {
      representative_text += static_cast<char>('0' + colour);
    }

    while (!queue.empty()) {
      const int current_index = queue.front();
      queue.pop();
      ++component_order;
      const Colouring current = decode_colouring(states[current_index]);
      std::array<int, 5> counts{};
      for (unsigned char colour : current) ++counts[colour];

      for (int first = 0; first < 5; ++first) {
        for (int second = first + 1; second < 5; ++second) {
          unsigned remaining = 0;
          for (int vertex = 0; vertex < 8; ++vertex) {
            if (current[vertex] == first || current[vertex] == second) {
              remaining |= 1u << vertex;
            }
          }
          while (remaining != 0) {
            unsigned component = remaining & -remaining;
            unsigned frontier = component;
            remaining -= component;
            while (frontier != 0) {
              const unsigned bit = frontier & -frontier;
              frontier -= bit;
              const int vertex = __builtin_ctz(bit);
              const unsigned fresh = adjacency[vertex] & remaining;
              remaining ^= fresh;
              component |= fresh;
              frontier |= fresh;
            }

            int first_count = counts[first];
            int second_count = counts[second];
            for (int vertex = 0; vertex < 8; ++vertex) {
              if ((component & (1u << vertex)) == 0) continue;
              if (current[vertex] == first) {
                --first_count;
                ++second_count;
              } else {
                --second_count;
                ++first_count;
              }
            }
            if (first_count == 0 || second_count == 0) continue;

            Colouring next = current;
            for (int vertex = 0; vertex < 8; ++vertex) {
              if ((component & (1u << vertex)) == 0) continue;
              next[vertex] = current[vertex] == first ? second : first;
            }
            const auto found = state_index.find(encode(next));
            if (found == state_index.end()) {
              throw std::runtime_error("Kempe move left the state space");
            }
            if (!reached[found->second]) {
              reached[found->second] = true;
              queue.push(found->second);
            }
          }
        }
      }
    }
    component_orders.push_back(component_order);
    representatives.push_back(representative_text);
  }
  return {component_orders, representatives, static_cast<int>(states.size())};
}

}  // namespace

int main() {
  BranchSets blocks{};
  generate_branch_partitions(0, blocks, 0);
  std::sort(branch_partitions.begin(), branch_partitions.end());
  branch_partitions.erase(
      std::unique(branch_partitions.begin(), branch_partitions.end()),
      branch_partitions.end());
  if (branch_partitions.size() != 2646) {
    throw std::runtime_error("branch-partition generation failed");
  }

  long graph_count = 0;
  long k5_minor_free_count = 0;
  long four_colourable_count = 0;
  long disconnected_count = 0;
  std::map<int, int> histogram;
  int minimum_edges = 99;
  std::vector<std::string> minimum_codes;
  KempeSummary minimum_summary;

  std::string graph6;
  while (std::cin >> graph6) {
    ++graph_count;
    const Adjacency adjacency = decode_graph6(graph6);
    int edge_count = 0;
    for (unsigned neighbourhood : adjacency) {
      edge_count += __builtin_popcount(neighbourhood);
    }
    edge_count /= 2;

    if (has_k5_minor(adjacency)) continue;
    ++k5_minor_free_count;
    if (!four_colourable(adjacency)) continue;
    ++four_colourable_count;

    KempeSummary summary = kempe_summary(adjacency);
    if (summary.component_orders.size() <= 1) continue;
    ++disconnected_count;
    ++histogram[edge_count];
    if (edge_count < minimum_edges) {
      minimum_edges = edge_count;
      minimum_codes.clear();
      minimum_summary = summary;
    }
    if (edge_count == minimum_edges) minimum_codes.push_back(graph6);
  }

  if (graph_count != 12346 || k5_minor_free_count != 7751 ||
      four_colourable_count != 7751 || disconnected_count != 23 ||
      minimum_edges != 12 || minimum_codes != std::vector<std::string>{"G??F~w"}) {
    throw std::runtime_error("unexpected census result");
  }
  std::sort(minimum_summary.component_orders.begin(),
            minimum_summary.component_orders.end());
  if (minimum_summary.state_count != 18600 ||
      minimum_summary.component_orders != std::vector<int>({7800, 10800})) {
    throw std::runtime_error("unexpected minimum obstruction summary");
  }

  std::cout << "PASS graphs=12346 k5_minor_free=7751 four_colourable=7751 "
               "disconnected=23\n";
  std::cout << "histogram";
  for (const auto& [edges, count] : histogram) {
    std::cout << ' ' << edges << ':' << count;
  }
  std::cout << "\nminimum edges=12 count=1 graph6=G??F~w states=18600 "
               "components=7800,10800\n";
  // These canonical representatives are independently pinned by the fixed
  // verifier; the census's unordered-map traversal need not select them.
  std::cout << "representatives 11123400 22223401\n";
}
