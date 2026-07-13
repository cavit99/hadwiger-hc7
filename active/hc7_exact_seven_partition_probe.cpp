#include <array>
#include <cstdint>
#include <iostream>
#include <vector>

// Exhaustively checks the seven-vertex combinatorial sublemma used in the
// exact-seven packet theorem.  Vertices are 0,...,6 and graphs are encoded
// by the 21 possible edges.

int main() {
    std::array<std::array<int, 7>, 7> bit{};
    int k = 0;
    for (int i = 0; i < 7; ++i)
        for (int j = i + 1; j < 7; ++j)
            bit[i][j] = bit[j][i] = k++;

    std::vector<std::uint32_t> triangles;
    for (int i = 0; i < 7; ++i)
        for (int j = i + 1; j < 7; ++j)
            for (int h = j + 1; h < 7; ++h)
                triangles.push_back((1u << bit[i][j]) |
                                    (1u << bit[i][h]) |
                                    (1u << bit[j][h]));

    struct Candidate {
        std::uint32_t forbidden;
        std::uint32_t required;
    };
    std::vector<Candidate> candidates;

    // S=I1 disjoint-union I2 disjoint-union Q, where I1,I2 are independent
    // of order at least two, and Q is a clique (necessarily of order <=2 in
    // a triangle-free graph, but allowing all Q is harmless).
    for (int qmask = 0; qmask < (1 << 7); ++qmask) {
        const int rem = ((1 << 7) - 1) ^ qmask;
        for (int i1 = rem; ; i1 = (i1 - 1) & rem) {
            const int i2 = rem ^ i1;
            if (__builtin_popcount(static_cast<unsigned>(i1)) >= 2 &&
                __builtin_popcount(static_cast<unsigned>(i2)) >= 2 &&
                i1 < i2) {
                std::uint32_t forbidden = 0, required = 0;
                for (int i = 0; i < 7; ++i) {
                    for (int j = i + 1; j < 7; ++j) {
                        const std::uint32_t e = 1u << bit[i][j];
                        if (((i1 >> i) & 1) && ((i1 >> j) & 1)) forbidden |= e;
                        if (((i2 >> i) & 1) && ((i2 >> j) & 1)) forbidden |= e;
                        if (((qmask >> i) & 1) && ((qmask >> j) & 1)) required |= e;
                    }
                }
                candidates.push_back({forbidden, required});
            }
            if (i1 == 0) break;
        }
    }

    auto bipartite_after_deleting = [&](std::uint32_t g, int deleted) {
        std::array<int, 7> colour;
        colour.fill(-1);
        for (int start = 0; start < 7; ++start) {
            if (start == deleted || colour[start] != -1) continue;
            std::array<int, 7> queue{};
            int head = 0, tail = 0;
            colour[start] = 0;
            queue[tail++] = start;
            while (head < tail) {
                int u = queue[head++];
                for (int w = 0; w < 7; ++w) {
                    if (w == deleted || w == u ||
                        !(g & (1u << bit[u][w]))) continue;
                    if (colour[w] == -1) {
                        colour[w] = colour[u] ^ 1;
                        queue[tail++] = w;
                    } else if (colour[w] == colour[u]) {
                        return false;
                    }
                }
            }
        }
        return true;
    };

    std::uint64_t triangle_free = 0;
    std::uint64_t nonbip_no_singleton = 0;
    std::uint64_t nonbip_no_balanced_singleton = 0;
    for (std::uint32_t g = 0; g < (1u << 21); ++g) {
        bool tf = true;
        for (std::uint32_t t : triangles) {
            if ((g & t) == t) { tf = false; break; }
        }
        if (!tf) continue;
        ++triangle_free;

        if (!bipartite_after_deleting(g, -1)) {
            bool singleton = false;
            bool balanced_singleton = false;
            for (int v = 0; v < 7; ++v)
                singleton |= bipartite_after_deleting(g, v);
            for (int v = 0; v < 7; ++v) {
                const int rem = ((1 << 7) - 1) ^ (1 << v);
                for (int a = rem; ; a = (a - 1) & rem) {
                    const int b = rem ^ a;
                    if (__builtin_popcount(static_cast<unsigned>(a)) >= 2 &&
                        __builtin_popcount(static_cast<unsigned>(b)) >= 2) {
                        bool ok = true;
                        for (int x = 0; x < 7; ++x)
                            for (int y = x + 1; y < 7; ++y)
                                if ((((a >> x) & 1) && ((a >> y) & 1)) ||
                                    (((b >> x) & 1) && ((b >> y) & 1)))
                                    ok &= !(g & (1u << bit[x][y]));
                        if (ok) balanced_singleton = true;
                    }
                    if (a == 0) break;
                }
            }
            if (!singleton) ++nonbip_no_singleton;
            if (!balanced_singleton) ++nonbip_no_balanced_singleton;
        }

        bool good = false;
        for (const Candidate &c : candidates) {
            if ((g & c.forbidden) == 0 && (g & c.required) == c.required) {
                good = true;
                break;
            }
        }
        if (!good) {
            std::cout << "COUNTEREXAMPLE " << g << "\n";
            return 1;
        }
    }
    std::cout << "GREEN labelled_triangle_free_graphs=" << triangle_free
              << " candidates=" << candidates.size()
              << " nonbip_no_singleton=" << nonbip_no_singleton
              << " nonbip_no_balanced_singleton="
              << nonbip_no_balanced_singleton << "\n";
    return 0;
}
