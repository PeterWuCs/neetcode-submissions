class Solution {
public:
    int singleNumber(vector<int>& nums) {
        
        int first = nums[0];

        for (size_t i = 1; i < nums.size(); i++) {
            first ^= nums[i];
        }

        return first;
    }
};
