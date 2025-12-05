class Solution {
public:
    int countPartitions(vector<int>& nums) {
        long long sum = 0;
        for (int x : nums) sum += x; // compute total s

        // parity check: D = 2L - S is even 
        // if s is even => all (n - 1) cuts work; else => 0
        return sum % 2 == 0 ? (int)nums.size() - 1 : 0;
    }
};
