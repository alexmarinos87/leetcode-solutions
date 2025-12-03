#include <bits/stdc++.h>
using namespace std;

using i64 = long long;

static inline i64 C2(i64 n) noexcept { return (n < 2) ? 0 : n * (n - 1) / 2; }

struct PairHash {
    size_t operator()(const pair<int,int>& p) const noexcept {
        uint64_t x = uint32_t(p.first), y = uint32_t(p.second);
        uint64_t z = (x << 32) ^ y;
        z += 0x9e3779b97f4a7c15ULL;
        z = (z ^ (z >> 30)) * 0xbf58476d1ce4e5b9ULL;
        z = (z ^ (z >> 27)) * 0x94d049bb133111ebULL;
        z ^= (z >> 31);
        return size_t(z);
    }
};
struct I64Hash {
    size_t operator()(long long x) const noexcept {
        uint64_t u = (uint64_t)x;
        u += 0x9e3779b97f4a7c15ULL;
        u = (u ^ (u >> 30)) * 0xbf58476d1ce4e5b9ULL;
        u = (u ^ (u >> 27)) * 0x94d049bb133111ebULL;
        u ^= (u >> 31);
        return size_t(u);
    }
};

static inline pair<int,int> norm_dir(int dx, int dy) noexcept {
    if (dx == 0) return {0, 1};
    if (dy == 0) return {1, 0};
    int adx = dx < 0 ? -dx : dx;
    int ady = dy < 0 ? -dy : dy;
    int g = std::gcd(adx, ady);
    dx /= g; dy /= g;
    if (dx < 0 || (dx == 0 && dy < 0)) { dx = -dx; dy = -dy; }
    return {dx, dy};
}

// Key for a line: (slope, c) where c = n·p with n = (-dy, dx) for primitive slope
struct LineKey {
    int dx, dy;
    i64 c;
    bool operator==(const LineKey& o) const noexcept {
        return dx == o.dx && dy == o.dy && c == o.c;
    }
};
struct LineKeyHash {
    size_t operator()(const LineKey& k) const noexcept {
        uint64_t a = (uint32_t)k.dx, b = (uint32_t)k.dy;
        uint64_t z = (a << 32) ^ b;
        // mix c in:
        uint64_t u = (uint64_t)k.c;
        z ^= (u + 0x9e3779b97f4a7c15ULL + (z<<6) + (z>>2));
        // finalize (splitmix-ish)
        z += 0x9e3779b97f4a7c15ULL;
        z = (z ^ (z >> 30)) * 0xbf58476d1ce4e5b9ULL;
        z = (z ^ (z >> 27)) * 0x94d049bb133111ebULL;
        z ^= (z >> 31);
        return (size_t)z;
    }
};

class Solution {
public:
    int countTrapezoids(vector<vector<int>>& points) {
        const int n = (int)points.size();
        if (n < 4) return 0;

        vector<pair<int,int>> pts;
        pts.reserve(n);
        for (auto& p : points) pts.emplace_back(p[0], p[1]);

        // 1) One pass over all pairs: build (slope,c) -> pairCount (this equals b_i for that line)
        unordered_map<LineKey, int, LineKeyHash> linePairCnt;
        linePairCnt.reserve((size_t)n * (n - 1) / 2);

        // Also accumulate per-slope aggregates (sumB, sumB2) on the fly to avoid a second scan.
        unordered_map<pair<int,int>, pair<long long,long long>, PairHash> slopeAgg;
        slopeAgg.reserve(linePairCnt.bucket_count() + 1024);

        // Buffer entries to finalize aggregates after counting pairs for lines
        // (we need final b_i per line; easier to do in two steps but still O(n^2))
        vector<LineKey> seenKeys; seenKeys.reserve((size_t)n * (n - 1) / 2);

        for (int i = 0; i < n; ++i) {
            const int xi = pts[i].first, yi = pts[i].second;
            for (int j = i + 1; j < n; ++j) {
                int dx0 = pts[j].first  - xi;
                int dy0 = pts[j].second - yi;
                auto s = norm_dir(dx0, dy0);    // primitive slope
                // primitive normal to that slope
                const long long nx = -(long long)s.second;
                const long long ny =  (long long)s.first;
                const long long c = nx * xi + ny * yi;

                LineKey key{ s.first, s.second, c };
                auto it = linePairCnt.find(key);
                if (it == linePairCnt.end()) {
                    linePairCnt.emplace(key, 1);
                    seenKeys.push_back(key);
                } else {
                    ++(it->second);
                }
            }
        }

        long long totalBySlope = 0;
        // Aggregate per slope: sumB and sumB2 from line pair-counts (b_i)
        for (const LineKey& k : seenKeys) {
            int b = linePairCnt[k];                // number of pairs on this line = C(m,2)
            auto& agg = slopeAgg[{k.dx, k.dy}];
            agg.first  += b;                       // sumB
            agg.second += 1LL * b * b;             // sumB2
        }
        for (auto& kv : slopeAgg) {
            long long sumB  = kv.second.first;
            long long sumB2 = kv.second.second;
            totalBySlope += (sumB * sumB - sumB2) / 2;
        }

        // 2) Parallelograms: sort-based mid-point grouping; subtract collinear pairs only
        // Build (mid_key, dir) for all pairs
        struct MidDir { long long mid; int dx, dy; };
        vector<MidDir> md;
        md.reserve((size_t)n * (n - 1) / 2);

        auto pack2 = [](long long a, long long b) noexcept -> long long {
            uint64_t ua = (uint32_t)a, ub = (uint32_t)b;
            return (long long)((ua << 32) | ub);
        };

        for (int i = 0; i < n; ++i) {
            const int xi = pts[i].first, yi = pts[i].second;
            for (int j = i + 1; j < n; ++j) {
                long long sx = (long long)xi + pts[j].first;
                long long sy = (long long)yi + pts[j].second;
                long long mid = pack2(sx, sy);

                int dx0 = pts[j].first  - xi;
                int dy0 = pts[j].second - yi;
                auto d = norm_dir(dx0, dy0);       // undirected canonical
                md.push_back({ mid, d.first, d.second });
            }
        }

        sort(md.begin(), md.end(), [](const MidDir& a, const MidDir& b){
            if (a.mid != b.mid) return a.mid < b.mid;
            if (a.dx != b.dx)   return a.dx < b.dx;
            return a.dy < b.dy;
        });

        long long parallelograms = 0;
        size_t L = md.size();
        size_t i = 0;
        while (i < L) {
            size_t j = i;
            // block with same mid
            while (j < L && md[j].mid == md[i].mid) ++j;
            long long kseg = (long long)(j - i);
            long long allPairs = C2(kseg);

            // subtract collinear segment-pairs: count per (dx,dy) within this mid block
            long long collinear = 0;
            size_t u = i;
            while (u < j) {
                size_t v = u + 1;
                while (v < j && md[v].dx == md[u].dx && md[v].dy == md[u].dy) ++v;
                long long cnt = (long long)(v - u);
                collinear += C2(cnt);
                u = v;
            }

            parallelograms += (allPairs - collinear);
            i = j;
        }

        long long ans = totalBySlope - parallelograms;
        if (ans < 0) ans = 0;
        return (int)ans;
    }
};

