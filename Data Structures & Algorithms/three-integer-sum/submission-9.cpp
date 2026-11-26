class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        vector<vector<int>> res;

        for (size_t i = 0; i < nums.size() - 2; i++)
        {   
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            int l = i + 1;
            int r = nums.size() - 1;

            while (l < r) {
                if (nums[i] + nums[l] + nums[r] == 0) {
                    vector<int> part_res {nums[i], nums[l], nums[r]};
                    res.push_back(part_res);
                    l++;
                    r--;
                    while (l < r && nums[l] == nums[l - 1]) l++;
                    while (l < r && nums[r] == nums[r + 1]) r--;
                } else if (nums[i] + nums[l] + nums[r] < 0) {
                    l++;
                } else {
                    r--;
                }

            }
        }

        return res;
        
    }
};
